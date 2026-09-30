"""Source-boundary regressions; these do not test reference taste or model behavior."""
import importlib.util
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reference_scope", ROOT / "scripts/reference_scope.py")
scope = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scope)


class ReferenceScopeTests(unittest.TestCase):
    def setUp(self):
        self.records = scope.read_catalog()
        self.eligible, self.excluded = scope.select(self.records)

    def test_real_catalog_permalinks_and_www_are_admitted(self):
        self.assertTrue(scope.check("https://www.onepagelove.com/a-specific-entry", self.eligible)["allowed"])
        self.assertTrue(scope.check("https://onepagelove.com/a-specific-entry", self.eligible)["allowed"])

    def test_hostname_suffix_and_subdomain_impersonation_are_rejected(self):
        for url in ("https://onepagelove.com.evil.test/x", "https://evilonepagelove.com/x",
                    "https://fake.onepagelove.com/x", "https://evil.test/?source=onepagelove.com"):
            with self.subTest(url=url):
                self.assertFalse(scope.check(url, self.eligible)["allowed"])

    def test_credentials_protocol_and_port_bypasses_are_invalid(self):
        for url in ("https://evil@onepagelove.com/x", "file:///onepagelove.com",
                    "javascript:onepagelove.com", "https://onepagelove.com:444/x", "//onepagelove.com/x"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                scope.check(url, self.eligible)

    def test_restricted_catalog_hosts_do_not_become_fallbacks(self):
        self.assertFalse(scope.check("https://www.a1.gallery/websites/x", self.eligible)["allowed"])
        self.assertTrue(any(record["host"] == "a1.gallery" for record in self.excluded))
        self.assertFalse(any("/Appllama/" in record["url"] for record in self.eligible))

    def test_section_selection_does_not_expand_to_entire_catalog(self):
        sources, _ = scope.select(self.records, ["Typography, color and extracted style"])
        self.assertTrue(scope.check("https://fontsinuse.com/uses/123", sources)["allowed"])
        self.assertFalse(scope.check("https://www.nngroup.com/articles/x", sources)["allowed"])

    def test_unknown_section_fails_instead_of_searching_everywhere(self):
        with self.assertRaises(ValueError):
            scope.select(self.records, ["Typograhpy"])

    def test_extra_user_source_is_explicit_and_labeled(self):
        url = "https://example.org/references"
        self.assertFalse(scope.check(url, self.eligible)["allowed"])
        sources, _ = scope.select(self.records, source_urls=[url])
        result = scope.check("https://example.org/entry", sources)
        self.assertTrue(result["allowed"])
        self.assertEqual("explicit-user-source", result["matched_sources"][0]["provenance"])

    def test_original_product_is_not_falsely_classified_as_catalog_source(self):
        self.assertFalse(scope.check("https://some-featured-product.example/home", self.eligible)["allowed"])

    def test_shared_github_host_is_restricted_to_cited_repositories(self):
        self.assertTrue(scope.check("https://github.com/pmndrs/drei/tree/master", self.eligible)["allowed"])
        self.assertFalse(scope.check("https://github.com/unrelated/style-prompts", self.eligible)["allowed"])
        self.assertFalse(scope.check("https://github.com/Appllama/appllama-skills", self.eligible)["allowed"])
        with self.assertRaises(ValueError):
            scope.check("https://github.com/pmndrs/drei/%2e%2e/%2e%2e/unrelated", self.eligible)


    def test_queries_keep_distinct_repositories_on_a_shared_host(self):
        queries = scope.search_queries(self.eligible, "composition")
        github = [q for q in queries if q["source_host"] == "github.com"]
        self.assertGreaterEqual(len(github), 2)
        self.assertTrue(any(q["source_scope"] == "github.com/pmndrs/drei" for q in github))
        self.assertTrue(all(q["source_scope"].count("/") == 2 for q in github))
        self.assertFalse(any(q["query"] == "site:github.com composition" for q in github))

    def run_cli(self, *args):
        output, errors = StringIO(), StringIO()
        with redirect_stdout(output), redirect_stderr(errors):
            status = scope.main(args)
        return status, output.getvalue(), errors.getvalue()

    def test_source_only_query_does_not_include_catalog(self):
        status, output, errors = self.run_cli(
            "queries", "--source-url", "https://example.org/references", "--query", "editorial")
        self.assertEqual(0, status, errors)
        self.assertEqual(["site:example.org editorial"],
                         [q["query"] for q in json.loads(output)["queries"]])

    def test_multiple_source_only_queries_preserve_repository_scopes_and_deduplicate(self):
        status, output, errors = self.run_cli(
            "queries", "--source-url", "https://github.com/designer/first",
            "--source-url", "https://github.com/designer/second",
            "--source-url", "https://github.com/designer/first/tree/main", "--query", "layout")
        self.assertEqual(0, status, errors)
        self.assertEqual({"github.com/designer/first", "github.com/designer/second"},
                         {q["source_scope"] for q in json.loads(output)["queries"]})
        self.assertEqual(2, len(json.loads(output)["queries"]))

    def test_section_plus_user_source_queries_are_only_the_requested_union(self):
        section = "Typography, color and extracted style"
        selected, _ = scope.select(self.records, [section])
        expected = {q["source_scope"] for q in scope.search_queries(selected, "type")}
        status, output, errors = self.run_cli(
            "queries", "--section", section, "--source-url", "https://example.org", "--query", "type")
        self.assertEqual(0, status, errors)
        self.assertEqual(expected | {"example.org"},
                         {q["source_scope"] for q in json.loads(output)["queries"]})

    def test_queries_without_scope_fail_without_producing_searches(self):
        status, output, errors = self.run_cli("queries", "--query", "layout")
        self.assertEqual(2, status)
        self.assertEqual("", output)
        self.assertIn("error", json.loads(errors))

    def test_default_check_keeps_catalog_and_explicit_user_sources(self):
        status, output, errors = self.run_cli(
            "check", "https://onepagelove.com/entry", "https://example.org/entry",
            "--source-url", "https://example.org")
        self.assertEqual(0, status, errors)
        self.assertTrue(all(r["allowed"] for r in json.loads(output)["results"]))


if __name__ == "__main__":
    unittest.main()
