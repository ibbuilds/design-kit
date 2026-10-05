#!/usr/bin/env python3
"""Diagnose the public One Page Love endpoint; this does not verify the host MCP connection."""
import argparse
import base64
import binascii
import json
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.onepagelove.com/mcp"
MAX_BYTES = 4 * 1024 * 1024
PROTOCOL = "2024-11-05"
SUPPORTED_PROTOCOLS = (PROTOCOL, "2025-03-26", "2025-06-18")


class DiagnosticError(Exception):
    pass


def decode_response(raw, content_type, request_id):
    """Read JSON or SSE, ignoring notifications rather than confusing them with the reply."""
    try:
        if "text/event-stream" in content_type.lower():
            messages, data = [], []
            for line in raw.decode("utf-8").splitlines() + [""]:
                if line.startswith("data:"):
                    data.append(line[5:].lstrip())
                elif not line and data:
                    messages.append(json.loads("\n".join(data)))
                    data = []
        elif "application/json" in content_type.lower():
            messages = [json.loads(raw)]
        else:
            raise DiagnosticError("Unsupported response content type")
    except (ValueError, UnicodeError) as error:
        raise DiagnosticError("Invalid JSON/SSE response") from error
    for message in messages:
        if not isinstance(message, dict) or message.get("id") != request_id:
            continue
        if message.get("jsonrpc") != "2.0":
            raise DiagnosticError("Invalid JSON-RPC version")
        if "error" in message:
            error = message["error"]
            code = error.get("code") if isinstance(error, dict) else None
            raise DiagnosticError("Provider JSON-RPC error: " + str(code))
        if "result" in message and isinstance(message["result"], dict):
            return message["result"]
        raise DiagnosticError("Expected an object result")
    raise DiagnosticError("No matching JSON-RPC response; host connection remains unverified")


class Client:
    def __init__(self, timeout=15, opener=urllib.request.urlopen):
        self.timeout, self.opener = timeout, opener
        self.session = None
        self.counter = 0
        self.protocol = PROTOCOL

    def call(self, method, params=None, notification=False):
        self.counter += 1
        payload = {"jsonrpc": "2.0", "method": method}
        if not notification:
            payload["id"] = self.counter
        if params is not None:
            payload["params"] = params
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json, text/event-stream",
                   "MCP-Protocol-Version": self.protocol}
        if self.session:
            headers["Mcp-Session-Id"] = self.session
        request = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode(), headers=headers)
        try:
            with self.opener(request, timeout=self.timeout) as response:
                self.session = response.headers.get("Mcp-Session-Id") or self.session
                raw = response.read(MAX_BYTES + 1)
                if len(raw) > MAX_BYTES:
                    raise DiagnosticError("Response exceeds diagnostic size limit")
                if notification:
                    return {}
                return decode_response(raw, response.headers.get("Content-Type", ""), self.counter)
        except urllib.error.HTTPError as error:
            retry = error.headers.get("Retry-After") if error.headers else None
            raise DiagnosticError("HTTP " + str(error.code) +
                                  ("; Retry-After: " + retry if retry else "")) from error
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            raise DiagnosticError("Endpoint connection failed: " + type(error).__name__) from error


def inspect_search(result):
    if result.get("isError"):
        raise DiagnosticError("Provider returned a tool error; no visual evidence established")
    content = result.get("content")
    if not isinstance(content, list):
        raise DiagnosticError("Tool result has no content array")
    images, text = 0, False
    for block in content:
        if not isinstance(block, dict):
            raise DiagnosticError("Invalid content block")
        if block.get("type") == "image":
            if block.get("mimeType") not in ("image/jpeg", "image/png", "image/webp", "image/gif"):
                raise DiagnosticError("Unsupported image content type")
            try:
                value = block.get("data")
                if not isinstance(value, str) or not base64.b64decode(value, validate=True):
                    raise DiagnosticError("Empty or invalid image data")
            except (ValueError, binascii.Error) as error:
                raise DiagnosticError("Invalid base64 image") from error
            images += 1
        if block.get("type") == "text" and isinstance(block.get("text"), str):
            text = text or bool(block["text"].strip())
    return {"image_blocks_received": images, "text_received": text,
            "visually_inspected": False}


def diagnose(client, search=None):
    report = {"provider": "onepagelove", "endpoint": ENDPOINT,
              "host_connection_verified": False, "configured": "not inspected",
              "endpoint_initialized": False, "tools_discovered": [], "search_executed": False}
    try:
        result = client.call("initialize", {"protocolVersion": PROTOCOL, "capabilities": {},
                             "clientInfo": {"name": "design-kit-diagnostic", "version": "1.0"}})
        if result.get("protocolVersion") not in SUPPORTED_PROTOCOLS or not isinstance(result.get("serverInfo"), dict):
            raise DiagnosticError("Incomplete initialization response")
        client.protocol = result["protocolVersion"]
        report["endpoint_initialized"] = True
        report["server_version"] = result["serverInfo"].get("version")
        client.call("notifications/initialized", notification=True)
        tools = client.call("tools/list").get("tools")
        if not isinstance(tools, list) or any(not isinstance(t, dict) or not isinstance(t.get("name"), str) for t in tools):
            raise DiagnosticError("Invalid tool listing")
        report["tools_discovered"] = [t["name"] for t in tools]
        if search is not None:
            tool = next((t for t in tools if t["name"] == "search_inspiration"), None)
            schema = tool.get("inputSchema") if tool else None
            fields = schema.get("properties") if isinstance(schema, dict) else None
            required = schema.get("required", []) if isinstance(schema, dict) else []
            if (not isinstance(fields, dict) or not isinstance(required, list) or
                    any(name not in ("query", "limit") for name in required) or
                    not all(name in fields for name in ("query", "limit"))):
                raise DiagnosticError("Search schema changed; inspect host tools before querying")
            result = client.call("tools/call", {"name": tool["name"],
                                 "arguments": {"query": search, "limit": 1}})
            report["search_executed"] = True
            report.update(inspect_search(result))
            report["empty_result"] = not report["text_received"] and not report["image_blocks_received"]
        report["status"] = "endpoint responded; host and visual inspection remain unverified"
    except DiagnosticError as error:
        report["error"] = str(error)
        report["status"] = "diagnostic failed; use the disclosed eligible fallback"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--search", help="Optional small search (one result); may consume provider quota")
    parser.add_argument("--timeout", type=float, default=15, help="Timeout per request, 1-30 seconds")
    args = parser.parse_args()
    if not 1 <= args.timeout <= 30 or (args.search is not None and not args.search.strip()):
        parser.error("Use a timeout of 1-30 seconds and a nonempty search")
    report = diagnose(Client(args.timeout), args.search)
    print(json.dumps(report, indent=2))
    return 1 if "error" in report else 0


if __name__ == "__main__":
    sys.exit(main())
