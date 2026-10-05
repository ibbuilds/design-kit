#!/usr/bin/env python3
"""Fixed-endpoint One Page Love stdio adapter for Codex's decimal-priority bug.

No extra packages, model calls, retries, local listener or reference cache.
Only decimal content annotations.priority is removed; reference content is intact.
"""
import copy
import json
import sys

from check_mcp import Client, DiagnosticError, MAX_BYTES, RPCError, SUPPORTED_PROTOCOLS


def compatible_result(result):
    result = copy.deepcopy(result)
    if not isinstance(result.get("content"), list):
        raise DiagnosticError("Provider tool result has no content array")
    for block in result.get("content", []):
        if not isinstance(block, dict):
            continue
        annotations = block.get("annotations")
        if isinstance(annotations, dict) and isinstance(annotations.get("priority"), float):
            del annotations["priority"]
    return result


class Adapter:
    def __init__(self, client=None):
        self.client = client or Client(timeout=25)
        self.initialized = False
        self.ready = False

    def dispatch(self, request):
        """Return one JSON-RPC reply, or None for a notification."""
        if (not isinstance(request, dict) or request.get("jsonrpc") != "2.0" or
                not isinstance(request.get("method"), str)):
            return self.error(None, -32600, "Invalid JSON-RPC request")
        request_id = request.get("id")
        if isinstance(request_id, bool) or not isinstance(request_id, (str, int, type(None))):
            return self.error(None, -32600, "Invalid JSON-RPC request ID")
        method, params = request["method"], request.get("params", {})
        notification = "id" not in request
        try:
            if notification:
                if method == "notifications/initialized" and self.initialized and not self.ready:
                    self.client.call(method, notification=True)
                    self.ready = True
                return None
            if not isinstance(params, dict):
                return self.error(request_id, -32602, "Parameters must be an object")
            if method == "initialize":
                if self.initialized:
                    return self.error(request_id, -32600, "Already initialized; reconnect the server")
                version = params.get("protocolVersion")
                self.client.protocol = version if version in SUPPORTED_PROTOCOLS else SUPPORTED_PROTOCOLS[-1]
                result = self.client.call(method, {
                    "protocolVersion": self.client.protocol, "capabilities": {},
                    "clientInfo": params.get("clientInfo", {"name": "design-kit-codex-compat", "version": "1.0"})})
                if result.get("protocolVersion") not in SUPPORTED_PROTOCOLS:
                    raise DiagnosticError("Unsupported provider protocol; use the direct connection")
                self.client.protocol = result["protocolVersion"]
                # This adapter forwards tools only, not server-initiated event streams.
                result = {**result, "capabilities": {"tools": {}}}
                self.initialized = True
            elif method == "ping":
                result = {}
            elif method in ("tools/list", "tools/call"):
                if not self.ready:
                    return self.error(request_id, -32002, "Server is not initialized")
                result = self.client.call(method, params)
                if method == "tools/call":
                    result = compatible_result(result)
            else:
                return self.error(request_id, -32601, "Method not supported by this tools-only adapter")
            return {"jsonrpc": "2.0", "id": request_id, "result": result}
        except RPCError as error:
            if notification:
                print(str(error), file=sys.stderr)
                return None
            if isinstance(error.error, dict):
                return {"jsonrpc": "2.0", "id": request_id, "error": error.error}
            return self.error(request_id, -32000, str(error))
        except DiagnosticError as error:
            if notification:
                print(str(error), file=sys.stderr)
                return None
            return self.error(request_id, -32000, str(error))

    @staticmethod
    def error(request_id, code, message):
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}


def serve(input_stream, output_stream, adapter=None):
    adapter = adapter or Adapter()
    while True:
        line = input_stream.readline(MAX_BYTES + 1)
        if not line:
            return
        if len(line) > MAX_BYTES:
            reply = adapter.error(None, -32600, "Request exceeds adapter size limit")
        else:
            try:
                reply = adapter.dispatch(json.loads(line))
            except (ValueError, UnicodeError):
                reply = adapter.error(None, -32700, "Invalid JSON")
        if reply is not None:
            output_stream.write(json.dumps(reply, ensure_ascii=True) + "\n")
            output_stream.flush()
        if len(line) > MAX_BYTES:
            return


if __name__ == "__main__":
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    serve(sys.stdin, sys.stdout)
