import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/design-director/scripts/reference_policy.py'
spec = importlib.util.spec_from_file_location('reference_policy', SCRIPT)
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class ReferencePolicyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.config = Path(self.temp.name) / 'preferences.json'

    def configure(self, **fields):
        self.config.write_text(json.dumps({'version': 1, **fields}), encoding='utf-8')

    def test_absent_preferences_uses_defaults_without_creating_files(self):
        result = policy.resolve(self.config)
        self.assertEqual(len(result['sources']), 7)
        self.assertEqual(result['origin']['sources'], 'built-in')
        self.assertFalse(self.config.exists())

    def test_preferred_pool_replaces_not_extends_defaults(self):
        sources = [{'name': 'My selected gallery', 'url': 'https://example.org/selected'}]
        self.configure(sources=sources, specialist_sources=[])
        before = self.config.read_bytes()
        result = policy.resolve(self.config)
        self.assertEqual(result['sources'], sources)
        self.assertEqual(result['specialist_sources'], [])
        self.assertEqual(result['origin']['sources'], 'user')
        self.assertEqual(self.config.read_bytes(), before)

    def test_empty_pools_disable_automatic_reference_sources(self):
        self.configure(sources=[], specialist_sources=[])
        result = policy.resolve(self.config)
        self.assertEqual(result['sources'] + result['specialist_sources'], [])

    def test_omitted_pool_inherits(self):
        self.configure(sources=[])
        self.assertEqual(policy.resolve(self.config)['origin']['specialist_sources'], 'built-in')

    def test_bad_preferences_never_silently_expand_sources(self):
        for raw in ('{', '{"version":2}', '{"version":true}', '{"version":1,"soruces":[]}',
                    '{"version":1,"sources":null}'):
            with self.subTest(raw=raw):
                self.config.write_text(raw)
                with self.assertRaises(ValueError):
                    policy.resolve(self.config)

    def test_unsafe_scopes_rejected(self):
        for url in ('http://example.org', 'https://user:secret@example.org',
                    'https://example.org/../private', 'https://example.org/%2e%2e',
                    'https://example.org?token=secret', 'https://example.org:8443',
                    'https://example.org\\private'):
            with self.subTest(url=url):
                self.configure(sources=[{'name': 'source', 'url': url}])
                with self.assertRaises(ValueError):
                    policy.resolve(self.config)


if __name__ == '__main__':
    unittest.main()
