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
        self.assertEqual(len(result['sources']), 22)
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

    def test_authority_tiers_and_new_sources(self):
        resolved=policy.resolve(self.config)
        sources=resolved['sources']+resolved['specialist_sources']
        tiers={t:{s['id'] for s in sources if s['tier']==t} for t in (1,2,3)}
        self.assertEqual(tiers[1],{'recent','a1-gallery','siteinspire','hoverstates','refs-gallery','minimal-gallery','site-of-sites','awwwards'})
        self.assertEqual(tiers[2],{'60fps','landing-love','design-spells','typewolf','fonts-in-use','brand-identity','bpando','rebrand-gallery','brand-new','loadmore','codrops','details','letterform'})
        self.assertEqual(tiers[3],{'httpster','landingfolio'})
        self.assertTrue(all(s['allowed_roles'] and s['inappropriate_roles'] for s in sources))
        for domain in ('godly.design','godly.website'):
            self.assertIsNone(policy.source_for('https://'+domain+'/',resolved,True))

    def test_macro_specialist_and_spatial_routes(self):
        resolved=policy.resolve(self.config)
        self.assertTrue(all(s['tier']==1 for s in policy.select('highest quality SaaS landing macro art direction',policy=resolved)))
        self.assertEqual([s['source'] for s in policy.select('button motion',policy=resolved)][:2],['60fps.design','Design Spells'])
        self.assertEqual([s['source'] for s in policy.select('typography',policy=resolved)][:2],['Typewolf','Fonts In Use'])
        self.assertTrue(all(s['tier']==1 for s in policy.select('spatial storytelling',policy=resolved)))
        self.assertTrue(all(s['tier']==2 for s in policy.select('branding',policy=resolved)))
        self.assertNotIn('Httpster',[s['source'] for s in policy.select('software editorial typography',policy=resolved)])
        self.assertEqual(policy.select('software',scopes=['https://www.landingfolio.com/'],policy=resolved)[0]['tier'],3)

    def test_legacy_source_preferences_retire_wrong_domains_without_rewriting(self):
        self.configure(sources=[{'id':'godly-recent','name':'Godly / Recent','url':'https://recent.design/',
            'aliases':['https://godly.design/','https://godly.website/']},
            {'name':'Wrong Godly','url':'https://godly.design/'}],specialist_sources=[])
        before=self.config.read_bytes();resolved=policy.resolve(self.config)
        self.assertEqual(len(resolved['sources']),1)
        self.assertEqual(resolved['sources'][0]['id'],'recent')
        self.assertEqual(resolved['sources'][0]['aliases'],[])
        self.assertEqual(before,self.config.read_bytes())

    def test_invalid_tiers_and_role_metadata_fail_closed(self):
        for extra in ({'tier':True},{'tier':0},{'tier':4},{'allowed_roles':[]},{'provenance_aliases':'bad'}):
            self.configure(sources=[{'name':'Custom','url':'https://example.org/',**extra}])
            with self.assertRaises(ValueError):policy.resolve(self.config)


if __name__ == '__main__':
    unittest.main()
