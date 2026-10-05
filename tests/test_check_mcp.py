"""Protocol diagnostics with fake network responses; these do not test live host activation."""
import base64
import importlib.util
import json
from pathlib import Path
import unittest
import urllib.error

SPEC = importlib.util.spec_from_file_location("check_mcp", Path(__file__).resolve().parents[1] / "scripts/check_mcp.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class Response:
    def __init__(self, payload, headers=None):
        self.payload = payload
        self.headers = headers or {"Content-Type": "application/json"}

    def read(self, limit):
        return self.payload[:limit]

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


class DiagnosticTests(unittest.TestCase):
    def test_sse_notification_before_matching_reply(self):
        raw = b'data: {"jsonrpc":"2.0","method":"notifications/tools/list_changed"}\n\nevent: message\ndata: {"jsonrpc":"2.0","id":3,"result":{"tools":[]}}\n\n'
        self.assertEqual({"tools": []}, module.decode_response(raw, "text/event-stream; charset=utf-8", 3))

    def test_wrong_id_never_counts_as_success(self):
        with self.assertRaises(module.DiagnosticError):
            module.decode_response(b'{"jsonrpc":"2.0","id":2,"result":{}}', "application/json", 3)

    def test_rpc_error_is_not_empty_catalog(self):
        with self.assertRaises(module.DiagnosticError):
            module.decode_response(b'{"jsonrpc":"2.0","id":3,"error":{"code":-32602}}', "application/json", 3)

    def test_html_error_is_not_a_protocol_response(self):
        with self.assertRaises(module.DiagnosticError):
            module.decode_response(b'<html>Gateway error</html>', "text/html", 1)

    def test_oversized_response_is_rejected(self):
        client = module.Client(opener=lambda *a, **k: Response(b'x' * (module.MAX_BYTES + 1)))
        with self.assertRaises(module.DiagnosticError):
            client.call("tools/list")

    def test_rate_limit_is_reported_without_retry(self):
        calls = []
        def opener(request, **kwargs):
            calls.append(request)
            raise urllib.error.HTTPError(module.ENDPOINT, 429, "limit", {"Retry-After": "30"}, None)
        report = module.diagnose(module.Client(opener=opener))
        self.assertEqual(1, len(calls))
        self.assertIn("Retry-After: 30", report["error"])
        self.assertFalse(report["host_connection_verified"])

    def test_bad_image_does_not_establish_evidence(self):
        with self.assertRaises(module.DiagnosticError):
            module.inspect_search({"content": [{"type": "image", "mimeType": "image/jpeg", "data": "not base64"}]})

    def test_tool_error_is_not_empty_search(self):
        with self.assertRaises(module.DiagnosticError):
            module.inspect_search({"isError": True, "content": []})

    def test_changed_schema_cannot_trigger_an_invented_tool_call(self):
        class FakeClient:
            protocol = module.PROTOCOL
            def __init__(self):
                self.methods = []
            def call(self, method, params=None, notification=False):
                self.methods.append(method)
                if method == "initialize":
                    return {"protocolVersion": module.PROTOCOL, "serverInfo": {}}
                if method == "tools/list":
                    return {"tools": [{"name": "search_inspiration", "inputSchema": {"properties": {"query": {}, "limit": {}}, "required": ["new_argument"]}}]}
                return {}
        client = FakeClient()
        report = module.diagnose(client, "minimal")
        self.assertIn("schema changed", report["error"])
        self.assertNotIn("tools/call", client.methods)

    def test_protocol_mismatch_stops_before_followup_requests(self):
        class FakeClient:
            def call(self, method, params=None, notification=False):
                self_outer.assertEqual("initialize", method)
                return {"protocolVersion": "unknown", "serverInfo": {}}
        self_outer = self
        report = module.diagnose(FakeClient())
        self.assertIn("error", report)
        self.assertFalse(report["endpoint_initialized"])

    def test_success_preserves_host_and_visual_limits_and_session(self):
        calls = []
        def opener(request, **kwargs):
            payload = json.loads(request.data)
            calls.append(payload)
            method = payload["method"]
            if method == "initialize":
                result = {"protocolVersion": "2025-03-26", "serverInfo": {"version": "test"}}
            else:
                self.assertEqual("session-token", request.get_header("Mcp-session-id"))
                self.assertEqual("2025-03-26", request.get_header("Mcp-protocol-version"))
                if method == "notifications/initialized":
                    self.assertNotIn("id", payload)
                    return Response(b'')
                if method == "tools/list":
                    result = {"tools": [{"name": "search_inspiration", "inputSchema": {"properties": {"query": {}, "limit": {}}}}]}
                else:
                    self.assertEqual(1, payload["params"]["arguments"]["limit"])
                    result = {"content": [{"type": "image", "mimeType": "image/jpeg", "data": base64.b64encode(b'image bytes').decode()}, {"type": "text", "text": "Source link"}]}
            return Response(json.dumps({"jsonrpc": "2.0", "id": payload["id"], "result": result}).encode(), {"Content-Type": "application/json", "Mcp-Session-Id": "session-token"})
        report = module.diagnose(module.Client(opener=opener), "dark minimal")
        self.assertNotIn("error", report)
        self.assertTrue(report["search_executed"])
        self.assertEqual(1, report["image_blocks_received"])
        self.assertFalse(report["host_connection_verified"])
        self.assertFalse(report["visually_inspected"])
        self.assertNotIn("session-token", json.dumps(report))
        self.assertEqual(4, len(calls))


if __name__ == "__main__":
    unittest.main()
