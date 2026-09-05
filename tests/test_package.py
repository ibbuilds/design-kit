import json
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/design-director'


class PackageTests(unittest.TestCase):
    def test_distribution_excludes_development_machinery(self):
        spec = importlib.util.spec_from_file_location('package', ROOT / 'scripts/package.py')
        package = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(package)
        selected = {p.relative_to(ROOT).as_posix() for p in package.files()}
        self.assertIn('.codex-plugin/plugin.json', selected)
        self.assertIn('skills/design-director/SKILL.md', selected)
        self.assertIn('skills/design-director/scripts/session.py', selected)
        self.assertTrue(all(p == 'README.md' or p.startswith(('.codex-plugin/', 'skills/'))
                            for p in selected))

    def test_local_links_resolve(self):
        for p in ROOT.rglob('*.md'):
            if '.git' in p.parts:
                continue
            for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                self.assertTrue((p.parent / target.split('#')[0]).exists(), (p, target))

    def test_one_primary_skill_and_manifest(self):
        manifest = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        self.assertEqual(manifest['name'], ROOT.name)
        self.assertEqual(manifest['skills'], './skills/')
        self.assertEqual(list(ROOT.glob('skills/*/SKILL.md')), [SKILL / 'SKILL.md'])
        self.assertNotIn('dependencies', manifest)  # No undocumented plugin dependencies.

    def test_canon_citations_and_pattern_metadata(self):
        registry = json.loads((SKILL / 'references/sources.json').read_text())
        sources = {s['id']: s for s in registry['sources']}
        self.assertEqual(len(sources), len(registry['sources']))
        for source in sources.values():
            self.assertTrue(source['url'].startswith('https://'))
            self.assertRegex(source['verified_on'], r'^\d{4}-\d{2}-\d{2}$')
            self.assertTrue(source['scope'])
            self.assertTrue(source['authority'])
        for p in (SKILL / 'references/canon').glob('*.md'):
            for section in p.read_text(encoding='utf-8').split('\n## ')[1:]:
                for key in ['Principle / problem', 'Use:', 'Do not use:', 'Alternatives:',
                            'Exceptions:', 'Accessibility:', 'Source / scope:']:
                    self.assertIn(key, section, (p, section[:60]))
                source_tail = section.split('Source / scope:')[1]
                ids = re.findall(r'`([a-z][a-z0-9-]+)`', source_tail)
                self.assertTrue(ids, (p, section[:60]))
                self.assertTrue(set(ids) <= sources.keys(), (p, ids))

    def test_no_bundled_raster_or_application_code(self):
        forbidden = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.tsx', '.jsx', '.vue', '.html'}
        for p in ROOT.rglob('*'):
            if '.git' not in p.parts and 'dist' not in p.parts:
                self.assertNotIn(p.suffix.lower(), forbidden, str(p))

    def test_representative_benchmark_families(self):
        cases = json.loads((ROOT / 'evals/benchmarks.json').read_text(encoding='utf-8'))
        expected = {
            'portfolio-showcase', 'marketing-product', 'dense-dashboard',
            'productivity-application', 'mobile-flow', 'editorial-reading'
        }
        self.assertEqual({case['id'] for case in cases}, expected)
        self.assertEqual(len(cases), len(expected))
        for case in cases:
            self.assertTrue(case['representative_request'])
            self.assertTrue(case['adequacy_evidence'])
            self.assertTrue(case['priority_dimensions'])
            self.assertTrue(case['reference_roles'])


if __name__ == '__main__':
    unittest.main()
