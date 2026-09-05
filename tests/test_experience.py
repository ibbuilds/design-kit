import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/design-director/scripts'))
import experience
import reference_policy


class ExperienceTests(unittest.TestCase):
    def test_registry_and_evidence_resolve_without_visual_source_expansion(self):
        data, authorities, sources = experience.load()
        self.assertEqual(set(authorities), {'apple','material','fluent','w3c','nng','govuk','uswds','baymard','carbon','sap','spectrum','atlassian'})
        self.assertEqual({e['evidence_type'] for e in data['entries']}, experience.KINDS)
        self.assertEqual(sources['wcag22']['authority'], 'normative-standard')
        self.assertEqual(sources['apg-patterns']['authority'], 'informative-standard-guidance')
        with tempfile.TemporaryDirectory() as temp:
            policy = reference_policy.resolve(Path(temp)/'absent')
            self.assertEqual(len(policy['sources']+policy['specialist_sources']),23)
            for a in authorities.values():
                self.assertIsNone(reference_policy.source_for(a['url'], policy, specialist=True))

    def test_representative_problem_decompositions(self):
        cases=json.loads((ROOT/'evals/experience-retrieval.json').read_text())['cases']
        for case in cases:
            with self.subTest(case=case['id']):
                r=experience.lookup(case['needs'],case['platform'],case['context'],limit=4,max_chars=14000)
                self.assertEqual({s['id'] for s in r['sections']},set(case['expected']))
                selected={a['id'] for s in r['sections'] for a in s['authorities']}
                self.assertFalse(selected & set(case['excluded_authorities']))
                self.assertLessEqual(r['knowledge_chars'],14000)
                self.assertTrue(all(s['sources'] for s in r['sections']))
                if case['id']=='novel':
                    self.assertNotIn('underwater',json.dumps(r['sections']).lower())
                    self.assertIn('domain evidence',json.dumps(r['sections']))

    def test_narrow_form_and_complex_context_scale_differently(self):
        narrow=experience.lookup()
        form=experience.lookup(['validation'])
        complex_=experience.lookup(['batch-selection','live-status','keyboard-access'],'web')
        self.assertEqual(narrow['knowledge_chars'],0)
        self.assertEqual(len(form['sections']),1)
        self.assertEqual(len(complex_['sections']),3)
        self.assertLess(form['knowledge_chars'],complex_['knowledge_chars'])

    def test_qualifiers_unknowns_and_user_restrictions_fail_closed(self):
        self.assertEqual(experience.lookup(['platform-expectations'])['sections'],[])
        self.assertEqual(experience.lookup(['checkout-burden'],context='operations')['sections'],[])
        self.assertEqual(experience.lookup(['validation'],authorities=[])['sections'],[])
        self.assertEqual(experience.lookup(['record-comparison'],authorities=['carbon'])['sections'],[])
        unknown=experience.lookup(['an-unfamiliar-domain'])
        self.assertEqual(unknown['sections'],[])
        self.assertEqual(unknown['uncovered_needs'],['an-unfamiliar-domain'])
        for kwargs in ({'authorities':['unapproved']},{'limit':7},{'max_chars':999999},{'platform':'all'},{'read':['../secret']}):
            with self.assertRaises(ValueError):experience.lookup(**kwargs)

    def test_context_bound_defers_whole_sections_and_direct_read_preserves_provenance(self):
        r=experience.lookup(['validation'],max_chars=1000)
        self.assertEqual(r['sections'],[])
        self.assertEqual(r['uncovered_needs'],['validation'])
        direct=experience.lookup(read=['tool-modes'],context='tool')
        self.assertEqual(direct['sections'][0]['id'],'tool-modes')
        self.assertIn('No Spectrum palette',direct['sections'][0]['text'])
        self.assertEqual({s['id'] for s in direct['sections'][0]['sources']},{'spectrum-actions','nng-complex'})

    def test_scope_revisions_do_not_keep_previous_task_context(self):
        experience.lookup(['checkout-burden'],context='commerce')
        revised=experience.lookup(['record-comparison'],context='operations')
        self.assertNotIn('baymard',json.dumps(revised).lower())
        self.assertEqual(experience.lookup()['sections'],[])
        self.assertEqual(experience.lookup(['platform-expectations'],'ios')['sections'][0]['id'],'apple-platform')
        self.assertEqual(experience.lookup(['platform-expectations'],'android')['sections'][0]['id'],'android-platform')

    def test_direct_reads_never_silently_disappear_at_section_limit(self):
        requested=['form-recovery','tool-modes','editing-history','recurrence']
        r=experience.lookup(read=requested,limit=2)
        delivered={s['id'] for s in r['sections']}
        deferred={s['id'] for s in r['deferred']}
        self.assertEqual(delivered | deferred,set(requested))
        self.assertFalse(delivered & deferred)
        self.assertEqual(len(delivered),2)
        rest=experience.lookup(read=sorted(deferred),limit=2)
        self.assertEqual({s['id'] for s in rest['sections']},deferred)

    def test_browser_verified_authorities_retain_scoped_research(self):
        r=experience.lookup(['cell-aggregation','large-selection'],context='operations')
        self.assertEqual(r['sections'][0]['id'],'analytical-structure')
        self.assertEqual(r['sections'][0]['sources'][0]['id'],'sap-analytical')
        self.assertIn('loaded rows',r['sections'][0]['text'])
        commerce=experience.lookup(['product-finding'],context='commerce')['sections'][0]
        self.assertEqual(commerce['evidence_type'],'research-finding')
        self.assertIn('normal browser',commerce['text'])

    def test_missing_local_section_is_an_explicit_gap(self):
        e=copy.deepcopy(experience.load()[0]['entries'][0]);e['local']='../outside.md'
        with self.assertRaises(ValueError):experience.section(e)
        e['local']='canon/forms.md';e['section']='Does not exist'
        with self.assertRaises(ValueError):experience.section(e)

    def test_discovery_defers_section_reads_and_precise_need_reads_only_selected(self):
        with patch.object(experience,'section',wraps=experience.section) as read:
            candidates=experience.lookup(['validation'],preview=True)
            self.assertEqual(read.call_count,0)
            full=experience.lookup(read=[s['id'] for s in candidates['sections']])
            self.assertEqual(read.call_count,1)
        self.assertNotIn('text',candidates['sections'][0])
        self.assertEqual(full['sections'][0]['id'],'form-recovery')
        self.assertEqual([{k:s[k] for k in ('id','url','authority','verified_on')}
                          for s in full['sections'][0]['sources']], candidates['sections'][0]['sources'])
        self.assertLess(len(experience.serialize(candidates)),len(experience.serialize(full)))
        with patch.object(experience,'section',wraps=experience.section) as read:
            experience.load()
            self.assertEqual(read.call_count,len(experience.load(validate_sections=False)[0]['entries']))

    def test_known_gaps_are_scoped_and_evidence_remains_classified(self):
        for need,expected in [('mixed-direction','bidi'),('recurring-events','recurrence'),('editing-history','editing-history')]:
            r=experience.lookup([need])
            self.assertEqual([s['id'] for s in r['sections']],[expected])
        draft=experience.lookup(['recurring-events'])['sections'][0]
        self.assertEqual(next(s['authority'] for s in draft['sources'] if s['id']=='w3c-timezone'),'informative-draft')
        self.assertEqual(experience.lookup(['rtl-mirroring'])['sections'],[])
        self.assertEqual(experience.lookup(['rtl-mirroring'],platform='ios')['sections'][0]['id'],'rtl-mirroring')
        self.assertEqual(experience.lookup(['editing-history'],context='commerce')['sections'],[])
        self.assertEqual(experience.lookup(['recurring-events'],authorities=['w3c'])['sections'],[])
        self.assertEqual(experience.lookup()['sections'],[])


if __name__ == '__main__':
    unittest.main()
