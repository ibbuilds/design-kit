"""Optional, read-only retrieval of scoped Canon sections and authority provenance.

The primary model chooses the question; this helper does not classify briefs,
browse, evaluate designs, write task memory, or add workflow steps.
"""
import argparse
from datetime import date
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / 'references'
KINDS = {'normative-standard', 'informative-guidance', 'platform-convention',
         'research-finding', 'design-system-pattern', 'heuristic'}
PLATFORMS = {'web', 'ios', 'ipados', 'macos', 'watchos', 'tvos', 'visionos', 'android', 'windows'}
CONTEXTS = {'service', 'transaction', 'commerce', 'tool', 'operations', 'editorial'}


def serialize(result):
    return json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n'


def section(entry, root=ROOT):
    path = (root / entry['local']).resolve()
    if not path.is_relative_to(root.resolve()) or path.suffix != '.md':
        raise ValueError('Knowledge must reference a local Markdown section')
    text = path.read_text(encoding='utf-8')
    heading = '## ' + entry['section']
    chunks = re.split(r'(?m)(?=^## )', text)
    found = [c.strip() for c in chunks if c.splitlines()[0] == heading]
    if len(found) != 1:
        raise ValueError(f'Missing or ambiguous knowledge section: {entry["id"]}')
    return found[0]


def load(root=ROOT, validate_sections=True):
    data = json.loads((root / 'experience.json').read_text(encoding='utf-8'))
    provenance = json.loads((root / 'sources.json').read_text(encoding='utf-8'))['sources']
    sources = {s['id']: s for s in provenance}
    if data.get('schema_version') != 1 or data.get('source_class') != 'experience-knowledge':
        raise ValueError('Expected experience knowledge registry version 1')
    authorities = {}
    from urllib.parse import urlsplit
    for a in data['authorities']:
        if a['id'] in authorities or not all(a.get(k) for k in ('name','scope','role','access')):
            raise ValueError('Incomplete or duplicate authority')
        for url in [a['url'], *a['related']]:
            p = urlsplit(url)
            if p.scheme != 'https' or not p.hostname or p.username or p.password:
                raise ValueError('Authority needs an official HTTPS entry point')
        date.fromisoformat(a['checked_on'])
        authorities[a['id']] = a
    seen = set()
    for e in data['entries']:
        if e['id'] in seen or e['evidence_type'] not in KINDS:
            raise ValueError('Duplicate entry or unknown evidence type')
        seen.add(e['id'])
        for field in ('needs','sources','authorities'):
            if not isinstance(e[field], list) or not e[field] or any(not isinstance(v, str) or not v for v in e[field]):
                raise ValueError('Knowledge requires needs and provenance')
        if set(e['sources']) - sources.keys() or set(e['authorities']) - authorities.keys():
            raise ValueError('Unresolved knowledge provenance')
        if set(e['platforms']) - PLATFORMS or set(e['contexts']) - CONTEXTS:
            raise ValueError('Unknown applicability qualifier')
        if validate_sections:
            section(e, root)
    return data, authorities, sources


def lookup(needs=(), platform=None, context=None, authorities=None, limit=3, max_chars=10000, read=(), root=ROOT, preview=False):
    if not 1 <= limit <= 6 or not 1000 <= max_chars <= 20000:
        raise ValueError('Use 1..6 sections and a 1000..20000 character knowledge budget')
    if platform is not None and platform not in PLATFORMS or context is not None and context not in CONTEXTS:
        raise ValueError('Unknown optional platform/context qualifier')
    if not isinstance(needs, (list, tuple)) or len(needs) > 12 or any(not isinstance(n,str) or len(n)>100 for n in needs):
        raise ValueError('Use at most 12 explicit decision needs')
    data, registry, sources = load(root, validate_sections=False)
    if authorities is not None and (not isinstance(authorities, (list, tuple)) or set(authorities)-registry.keys()):
        raise ValueError('Unknown authority restriction; never silently widen it')
    if len(read) > 6 or set(read) - {e['id'] for e in data['entries']}:
        raise ValueError('Unknown section or too many direct reads')
    remaining = set(needs)
    candidates, excluded = [], []
    for e in data['entries']:
        match = set(e['needs']) & remaining
        if not match and e['id'] not in read:
            continue
        reason = None
        if authorities is not None and not set(e['authorities']) <= set(authorities):
            reason = 'outside requested authority scope'
        if e['platforms'] and platform not in e['platforms']:
            reason = 'platform-specific; choose only when the target platform is known'
        if context is not None and e['contexts'] and context not in e['contexts']:
            reason = 'different task context'
        if reason:
            excluded.append({'id':e['id'], 'reason':reason})
        else:
            candidates.append(e)
    results, used = [], 0
    while candidates and len(results) < limit:
        # Complementarity over repeated coverage, preserving explicit need order.
        candidates.sort(key=lambda e: (-len(set(e['needs']) & remaining),
            min((list(needs).index(n) for n in e['needs'] if n in needs), default=999)))
        e = candidates.pop(0)
        if not set(e['needs']) & remaining and e['id'] not in read:
            continue
        citations = [{k:sources[s][k] for k in ('id','url','authority','scope','verified_on')}
                     for s in e['sources']]
        for citation in citations:
            if 'title' in sources[citation['id']]:
                citation['title'] = sources[citation['id']]['title']
        if preview:
            citations = [{k:c[k] for k in ('id','url','authority','verified_on')} for c in citations]
        item = {'id':e['id'], 'matched_needs':sorted(set(e['needs']) & set(needs)),
                'evidence_type':e['evidence_type'], 'applicability':{'platforms':e['platforms'], 'contexts':e['contexts']},
                'sources':citations,
                'authorities':[{'id':a, 'name':registry[a]['name']} for a in e['authorities']]}
        if preview:
            item.update(title=e['section'], local=e['local'])
        else:
            item['text'] = section(e, root)
        size = len(json.dumps(item, ensure_ascii=False))
        if used + size > max_chars:
            excluded.append({'id':e['id'], 'reason':'context budget; request this section separately if needed'})
            continue
        results.append(item);used += size;remaining -= set(e['needs'])
    for e in candidates:
        if set(e['needs']) & remaining or e['id'] in read:
            excluded.append({'id':e['id'], 'reason':'section limit; request separately if needed'})
    return {'sections':results, 'uncovered_needs':sorted(remaining), 'deferred':excluded,
            'knowledge_chars':used}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--need', action='append', default=[])
    p.add_argument('--read', action='append', default=[])
    p.add_argument('--platform', choices=sorted(PLATFORMS))
    p.add_argument('--context', choices=sorted(CONTEXTS))
    p.add_argument('--authority', action='append')
    p.add_argument('--limit', type=int, default=3)
    p.add_argument('--max-chars', type=int, default=10000)
    p.add_argument('--catalog', action='store_true')
    p.add_argument('--validate', action='store_true')
    p.add_argument('--search', action='store_true', help='Return candidate metadata without section text; hydrate with --read')
    p.add_argument('--authority-info', action='append', help='Read full records only for selected authority IDs')
    a = p.parse_args()
    try:
        if a.validate or a.catalog or a.authority_info:
            data, authorities, sources = load(validate_sections=a.validate)
            if a.authority_info:
                if set(a.authority_info) - authorities.keys():
                    raise ValueError('Unknown authority')
                result = {'authorities':[authorities[i] for i in dict.fromkeys(a.authority_info)]}
            else:
                result = {'authorities':len(authorities), 'sections':len(data['entries']), 'valid':True} if a.validate else {
                    'sections':[{k:e[k] for k in ('id','needs','platforms','contexts')} for e in data['entries']]}
        else:
            result = lookup(a.need, a.platform, a.context, a.authority, a.limit, a.max_chars, a.read, preview=a.search)
        print(serialize(result), end='')
    except (ValueError, OSError, KeyError, TypeError) as error:
        p.exit(2, f'Experience knowledge unavailable: {error}. Do not invent missing guidance.\n')
