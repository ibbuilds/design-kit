"""Development-only route replay. Measures emitted text, not a live model trace.

Requires tiktoken in the development environment, never in the installed plugin.
The corpus is read-only; the rebuildable SQLite cache goes to --scratch.
"""
import argparse
import hashlib
import json
from pathlib import Path
import statistics
import sys
import time
from unittest.mock import patch

ROUTES = {
    'shadow': {},
    'button': {'docs': ['craft/interaction-motion.md']},
    'finish': {'docs': ['quality.md', 'craft/finish.md']},
    'form': {'needs': ['validation']},
    'table': {'needs': ['record-comparison', 'batch-selection', 'record-filtering', 'keyboard-access']},
    'operations': {'needs': ['batch-selection', 'live-status', 'record-filtering', 'keyboard-access'],
                   'docs': ['process.md', 'quality.md', 'craft/art-direction.md', 'craft/composition.md'], 'query': 'density navigation', 'selected': 2},
    'landing': {'docs': ['process.md', 'quality.md', 'craft/art-direction.md', 'craft/typography.md', 'craft/composition.md'],
                'sections': [('canon/content.md', 'Persuasion with credible evidence')],
                'query': 'typography composition imagery', 'selected': 2},
    'ambitious-landing': {'docs': ['process.md', 'quality.md', 'craft/art-direction.md', 'craft/typography.md',
                                   'craft/composition.md', 'craft/finish.md'],
                         'sections': [('canon/content.md', 'Persuasion with credible evidence')],
                         'query': 'typography composition imagery', 'selected': 2},
    'expressive-assets': {'docs': ['process.md', 'quality.md', 'craft/art-direction.md',
                                  'craft/typography.md', 'craft/composition.md', 'craft/assets.md', 'craft/finish.md'],
                         'sections': [('canon/content.md', 'Persuasion with credible evidence')],
                         'query': 'typography composition imagery', 'selected': 2},
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, required=True)
    p.add_argument('--scratch', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=True)
    skill = a.root / 'skills/design-director'
    sys.path.insert(0, str(skill / 'scripts'))
    import experience
    import intelligence
    import session
    import tiktoken
    enc = tiktoken.get_encoding('o200k_base')
    def measure(s):
        return {'chars': len(s), 'tokens': len(enc.encode(s)), 'sha256': hashlib.sha256(s.encode()).hexdigest()}
    def emit(v):
        return json.dumps(v, ensure_ascii=False, indent=2) + '\n'
    core = (skill / 'SKILL.md').read_text(encoding='utf-8')
    report = {'method': 'tiktoken o200k_base; exact text token counts, NOT verified selected-model tokenizer parity. Scripted plausible routes, not observed model activation. Excludes host/tool schemas, live Figma payloads and image tokens.',
              'core': measure(core), 'body': measure(core.split('---', 2)[2].lstrip()), 'routes': {}}
    report['discovery_metadata'] = measure(core.split('---', 2)[1].strip())
    registry = json.loads((skill/'references/experience.json').read_text(encoding='utf-8'))
    report['authorities'] = registry['authorities']
    report['visual_source_registry_sha256'] = hashlib.sha256((skill/'references/reference-sources.json').read_bytes()).hexdigest()
    rows = list(intelligence.records())
    report['corpus'] = {'records': len(rows), 'receipt_digest': hashlib.sha256(emit(rows).encode()).hexdigest(),
                        'asset_hashes': {r['sha256']: session.digest(Path(path).read_bytes()) for path, r in rows}}
    bookmarks = session.storage_base()/'bookmarks.json'
    report['corpus']['bookmarks_sha256'] = hashlib.sha256(bookmarks.read_bytes()).hexdigest() if bookmarks.exists() else None
    with patch.object(intelligence, 'cache_path', return_value=a.scratch/'index.sqlite3'):
        for name, route in ROUTES.items():
            docs = ['figma.md', *route.get('docs', [])]
            # Complete-design routes now consume foundations; local routes do not.
            if name in ('operations', 'landing', 'ambitious-landing', 'expressive-assets'):
                docs.append('design-foundations.md')
                if 'craft/typography.md' not in docs:
                    docs.append('craft/typography.md')
            if name in ('operations', 'landing', 'ambitious-landing', 'expressive-assets') and (skill/'references/figma-create.md').exists():
                docs.append('figma-create.md')
            outputs, calls, knowledge, evidence = [], 0, [], []
            if route.get('needs'):
                docs += ['experience.md']
                selected = experience.lookup(route['needs'], platform='web', limit=4, max_chars=14000)
                knowledge = [{'id':s['id'], 'text_sha256':hashlib.sha256(s['text'].encode()).hexdigest(),
                              'sources':[c['id'] for c in s['sources']]} for s in selected['sections']]
                outputs.append(getattr(experience, 'serialize', emit)(selected))
                calls += 1
            if route.get('query'):
                docs += ['visual-references.md', 'intelligence.md']
                result = intelligence.search(route['query'], analyzed_only=True)
                evidence = [h['sha256'] for h in result['results']]
                outputs.append(getattr(intelligence, 'serialize', emit)(result)); calls += 1
                if hasattr(intelligence, 'hydrate_selected'):
                    hits = result['results'][:route['selected']]
                    outputs.append(intelligence.serialize(intelligence.hydrate_selected(
                        [h['path'] for h in hits], [h['sha256'] for h in hits]))); calls += 1
            for local, heading in route.get('sections', []):
                outputs.append(experience.section({'id':heading, 'local':local, 'section':heading}))
            parts = [core] + [(skill/'references'/d).read_text(encoding='utf-8') for d in docs] + outputs
            report['routes'][name] = {'total': measure('\n'.join(parts)), 'docs': docs,
                'documents': {d: measure((skill/'references'/d).read_text(encoding='utf-8')) for d in docs},
                'outputs': [measure(o) for o in outputs], 'helper_calls': calls, 'external_requests': 0,
                'knowledge':knowledge, 'reference_candidates':evidence,
                'candidate_count': len(result['results']) if route.get('query') else 0,
                'selected_count': route.get('selected', 0)}
        timings = {}
        for label, fn in [('experience', lambda: experience.lookup(['validation'])),
                          ('visual', lambda: intelligence.search('typography composition imagery', analyzed_only=True)),
                          ('complementary', lambda: intelligence.complementary(['composition','typography','imagery']))]:
            elapsed = []
            for _ in range(5):
                start=time.perf_counter(); fn(); elapsed.append((time.perf_counter()-start)*1000)
            timings[label]={'median_ms':round(statistics.median(elapsed),2), 'samples_ms':[round(n,2) for n in elapsed]}
        report['timings']=timings
    a.output.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='corpus'}, indent=2))


if __name__ == '__main__':
    main()
