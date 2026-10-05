"""Compatibility/protocol tests; live host verification is separate."""
import copy
import io
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_mcp import DiagnosticError, RPCError
from onepagelove_compat import Adapter, compatible_result, serve
sys.path.pop(0)


class Client:
    protocol = "2025-06-18"

    def __init__(self):
        self.calls = []
        self.result = {"content": [{"type": "text", "text": "Reference", "annotations": {"priority": 0.9}}]}

    def call(self, method, params=None, notification=False):
        self.calls.append((method, params, notification))
        if method == "initialize":
            return {"protocolVersion": self.protocol, "capabilities": {"tools": {"listChanged": True}},
                    "serverInfo": {"name": "One Page Love", "version": "1.4.1"}}
        if notification:
            return {}
        if method == "tools/list":
            return {"tools": [{"name": "search_inspiration", "inputSchema": {"type": "object"}}]}
        if isinstance(self.result, Exception):
            raise self.result
        return self.result


class CompatibilityTests(unittest.TestCase):
    def test_only_decimal_content_priority_changes(self):
        result = {"content": [
            {"type": "text", "text": "Title — live URL", "annotations": {"audience": ["user"], "priority": 0.9}},
            {"type": "image", "data": "unchanged-base64", "mimeType": "image/jpeg", "annotations": {"priority": 1.0}},
            {"type": "resource_link", "name": "Source", "uri": "https://example.com", "annotations": {"priority": 1}},
        ], "isError": False, "structuredContent": {"annotations": {"priority": 0.9}}, "_meta": {"keep": True}}
        before = copy.deepcopy(result)
        actual = compatible_result(result)
        expected = copy.deepcopy(result)
        del expected["content"][0]["annotations"]["priority"]
        del expected["content"][1]["annotations"]["priority"]
        self.assertEqual(expected, actual)
        self.assertEqual(before, result)

    def ready(self):
        client = Client()
        adapter = Adapter(client)
        adapter.dispatch({"jsonrpc": "2.0", "id": "init", "method": "initialize", "params": {"protocolVersion": "2026-07-28"}})
        adapter.dispatch({"jsonrpc": "2.0", "method": "notifications/initialized"})
        return adapter, client

    def test_negotiation_and_exactly_one_upstream_call_per_search(self):
        adapter, client = self.ready()
        self.assertEqual("2025-06-18", client.protocol)
        args = {"name": "search_sections", "arguments": {"section_type": "hero", "limit": 1}}
        reply = adapter.dispatch({"jsonrpc": "2.0", "id": "search", "method": "tools/call", "params": args})
        self.assertEqual("search", reply["id"])
        self.assertNotIn("priority", reply["result"]["content"][0]["annotations"])
        self.assertEqual([("initialize", client.calls[0][1], False), ("notifications/initialized", None, True),
                          ("tools/call", args, False)], client.calls)

    def test_original_schema_and_provider_errors_are_preserved(self):
        adapter, client = self.ready()
        reply = adapter.dispatch({"jsonrpc": "2.0", "id": 3, "method": "tools/list"})
        self.assertEqual("search_inspiration", reply["result"]["tools"][0]["name"])
        error = {"code": -32602, "message": "Invalid section", "data": {"allowed": ["hero"]}}
        client.result = RPCError(error)
        reply = adapter.dispatch({"jsonrpc": "2.0", "id": 4, "method": "tools/call"})
        self.assertEqual(error, reply["error"])
        client.result = {"content": [{"type": "text", "text": "No matches"}], "isError": False}
        reply = adapter.dispatch({"jsonrpc": "2.0", "id": 5, "method": "tools/call"})
        self.assertEqual(client.result, reply["result"])

    def test_transport_failure_is_not_an_empty_result_or_retry(self):
        adapter, client = self.ready()
        client.result = DiagnosticError("HTTP 429; Retry-After: 30")
        reply = adapter.dispatch({"jsonrpc": "2.0", "id": 4, "method": "tools/call"})
        self.assertIn("429", reply["error"]["message"])
        self.assertEqual(3, len(client.calls))

    def test_unknown_methods_and_preinitialize_calls_do_not_contact_provider(self):
        client = Client()
        adapter = Adapter(client)
        for method, code in (("resources/read", -32601), ("tools/call", -32002)):
            reply = adapter.dispatch({"jsonrpc": "2.0", "id": 1, "method": method})
            self.assertEqual(code, reply["error"]["code"])
        self.assertEqual([], client.calls)

    def test_stdio_stdout_contains_only_rpc_and_notifications_have_no_reply(self):
        adapter, client = self.ready()
        source = io.StringIO('\n'.join([
            '{broken json',
            json.dumps({"jsonrpc": "2.0", "method": "notifications/cancelled"}),
            json.dumps({"jsonrpc": "2.0", "id": 7, "method": "tools/call"}),
        ]) + '\n')
        output = io.StringIO()
        serve(source, output, adapter)
        replies = [json.loads(line) for line in output.getvalue().splitlines()]
        self.assertEqual(2, len(replies))
        self.assertEqual(-32700, replies[0]["error"]["code"])
        self.assertEqual(7, replies[1]["id"])


if __name__ == "__main__":
    unittest.main()
