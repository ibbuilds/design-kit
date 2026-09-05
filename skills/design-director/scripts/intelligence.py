"""Persistent visual memory over retained receipts; SQLite is a rebuildable cache.

No model calls, implicit discovery, or image interpretation. One local writer at a time.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import io
import json
import math
from pathlib import Path
import re
import sqlite3
import sys

import reference_policy
import session

STOP = set('a an the and or with for this that of to in on very strong improve design page use'.split())
GROUPS = [
    'image imagery photograph photography photographic photo',
    'type typography typographic lettering font',
    'asymmetry asymmetric asymmetrical unconventional',
    'hospitality hotel resort accommodation stay travel',
    'architecture architectural building spatial',
    'editorial publishing magazine reading',
    'ecommerce commerce shop shopping retail',
    'premium luxury luxurious refined',
    'navigation nav menu wayfinding',
    'table tables grid rows data dense density',
    'pricing price plans comparison compare',
    'form forms input service booking checkout',
    'material materiality materials',
    'tactile tactility',
    'texture textured textures grain',
    'depth dimensional dimensionality elevation elevated',
    'shadow shadows shadowing',
    'surface surfaces',
    'layer layers layered layering overlap overlapping',
    'transparency transparent translucent translucency',
    'edge edges',
    'frame framing framed',
    'mask masks masking cutout cutouts extraction',
    'composite composites compositing composited',
    'microinteraction microinteractions hover',
    'motion interaction animation animated transition choreography',
    'portfolio showcase work projects',
    'space whitespace negative quiet spacious',
]
SYNONYMS = {w: set(g.split()) for g in GROUPS for w in g.split()}
MOTION_TERMS = {'motion', 'animation', 'animations', 'animated', 'interaction',
                'interactions', 'microinteraction', 'microinteractions',
                'choreography', 'hover', 'swipe', 'scroll', 'gif', 'video', 'easing'}
EVIDENCE_SCOPES = {'full-site', 'page', 'hero', 'section', 'component', 'detail',
                   'motion-sequence', 'typography', 'brand', 'mobile'}


def serialize(result):
    return json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n'


def now():
    return datetime.now(timezone.utc).isoformat()


def tokens(value):
    return set(re.findall(r'[^\W_]+', value.casefold())) - STOP


def expand(value):
    terms = tokens(value)
    return set().union(*(SYNONYMS.get(t, {t}) for t in terms)) if terms else set()


def checked(path, _receipts=None):
    path = Path(path).absolute()
    key = str(path.parent)
    if _receipts is not None and key in _receipts:
        root, data = _receipts[key]
    else:
        root, data = session.load(path.parent)
        if _receipts is not None:
            _receipts[key] = (root, data)
    record = data['files'].get(path.name)
    if not record or not path.name.startswith('asset-'):
        raise ValueError('Choose a retained reference image')
    session.ordinary(path)
    content = path.read_bytes()
    if session.digest(content) != record['sha256']:
        raise ValueError('Image changed since import; preserve it and repair provenance explicitly')
    return root, data, record, content


def source_metadata(path, metadata):
    """Provider labels stay separate from model observations and legacy index text."""
    root, data, record, _ = checked(path)
    allowed = {'title', 'tags', 'description', 'creator', 'date', 'project', 'evidence_url', 'typefaces', 'medium', 'editorial_context', 'curated_subset'}
    if not isinstance(metadata, dict) or set(metadata) - allowed:
        raise ValueError('Unknown source metadata field')
    if len(json.dumps(metadata)) > 6000:
        raise ValueError('Source metadata must be compact')
    for k, v in metadata.items():
        if k in ('tags', 'typefaces'):
            if not isinstance(v, list) or any(not isinstance(x, str) for x in v):
                raise ValueError('Source tags must be text')
        elif not isinstance(v, str):
            raise ValueError('Source metadata fields must be text')
    evidence_urls = [record['page'], record['asset']] + [p['observed_on'] for p in record.get('acquisition_provenance', [])]
    if metadata.get('evidence_url') not in evidence_urls:
        raise ValueError('Source metadata needs its observed page or asset URL')
    record['source_metadata'] = {**metadata, 'recorded_at': now()}
    session.save(root, data)
    return {'path': str(path), 'source_metadata': record['source_metadata']}


def analyze(path, analysis):
    """Accept only a primary-session inspection attestation tied to exact bytes.

    The caller must really view the image. This validates evidence structure, not
    cognition; tools cannot guarantee that the caller's statement is truthful.
    """
    from PIL import Image
    root, data, record, content = checked(path)
    allowed = {'inspection', 'observations', 'mechanisms', 'families', 'surfaces',
               'limitations', 'use_cases', 'confidence', 'sequence'}
    if not isinstance(analysis, dict) or set(analysis) - allowed:
        raise ValueError('Unknown analysis field; keep task application outside memory')
    if len(json.dumps(analysis)) > 12000:
        raise ValueError('Keep visual intelligence compact')
    inspection = analysis.get('inspection', {})
    if (set(inspection) != {'sha256', 'method', 'evidence', 'region', 'observed_at'}
            or inspection.get('sha256') != record['sha256']
            or inspection.get('method') not in ('primary-image-view', 'primary-motion-view')
            or any(not isinstance(v, str) or not v.strip() for v in inspection.values())):
        raise ValueError('Exact hash, actual primary viewing method, evidence, region and time required')
    datetime.fromisoformat(inspection['observed_at'].replace('Z', '+00:00'))
    for field in ('observations', 'families', 'surfaces', 'limitations', 'use_cases'):
        values = analysis.get(field, [])
        if (not isinstance(values, list) or len(values) > 16
                or any(not isinstance(v, str) or not v.strip() or len(v) > 700 for v in values)):
            raise ValueError(f'Invalid {field}')
    if not analysis.get('observations'):
        raise ValueError('Actual visible observations required')
    mechanisms = analysis.get('mechanisms', [])
    if not isinstance(mechanisms, list) or not 1 <= len(mechanisms) <= 8:
        raise ValueError('Record 1–8 concrete transferable mechanisms')
    for m in mechanisms:
        if (not isinstance(m, dict) or not {'role', 'visible', 'effect'} <= set(m)
                or set(m) - {'role', 'visible', 'effect', 'evidence', 'scope', 'quality'}
                or any(not isinstance(m[k], str) or not m[k].strip() or len(m[k]) > 700
                       for k in ('role', 'visible', 'effect'))):
            raise ValueError('Each mechanism needs role, visible cause and reasoned effect')
        if 'evidence' in m:
            e = m['evidence']
            if (not isinstance(e, dict) or set(e) != {'strength', 'basis'}
                    or e['strength'] not in ('clear', 'limited')
                    or not isinstance(e['basis'], str) or not e['basis'].strip()
                    or len(e['basis']) > 400):
                raise ValueError('Mechanism evidence needs clear/limited strength and a visible basis or limitation')
        if 'scope' in m:
            if (not isinstance(m['scope'], list) or not m['scope']
                    or any(s not in EVIDENCE_SCOPES for s in m['scope'])):
                raise ValueError('Use explicit evidence scopes for this mechanism')
            if '/section/' in record['page'] and set(m['scope']) & {'full-site', 'page'}:
                raise ValueError('A section capture cannot establish page or full-site authority')
        if 'quality' in m:
            q = m['quality']
            if (not isinstance(q, dict) or set(q) != {'ambition', 'basis'}
                    or q['ambition'] not in ('ordinary', 'high')
                    or not isinstance(q['basis'], str) or not 20 <= len(q['basis']) <= 500):
                raise ValueError('Quality needs a role-specific ambition threshold and observed basis')
            if q['ambition'] == 'high' and (not m.get('scope') or m.get('evidence', {}).get('strength') != 'clear'):
                raise ValueError('Elite eligibility requires clear, scoped evidence; source tier is insufficient')
        if (tokens(m['role']) & MOTION_TERMS or 'motion-sequence' in m.get('scope', [])) and inspection['method'] != 'primary-motion-view':
            raise ValueError('Motion/interaction mechanisms require actual motion evidence')
    if analysis.get('confidence') not in ('high', 'medium', 'low'):
        raise ValueError('Record confidence explicitly')
    with Image.open(io.BytesIO(content)) as im:
        im.load()
        size = list(im.size)
        if inspection['method'] == 'primary-motion-view' and getattr(im, 'n_frames', 1) < 2:
            raise ValueError('Retained static image cannot substantiate motion')
        frames = getattr(im, 'n_frames', 1)
    if inspection['method'] == 'primary-motion-view':
        validate_sequence(analysis.get('sequence'), minimum_states=min(3, frames))
    elif 'sequence' in analysis:
        raise ValueError('First-frame/static inspection cannot contain motion sequence claims')
    record['analysis'] = {**analysis, 'schema': 3, 'recorded_at': now(), 'image_size': size,
                          'media': {'frames': frames, 'animated': frames > 1}}
    session.save(root, data)
    return {'path': str(path), 'status': 'analyzed', 'sha256': record['sha256']}


def validate_sequence(sequence, minimum_states=3):
    """Validate an observation receipt, never pretend software watched the motion."""
    fields = {'method', 'states', 'trigger', 'continuity', 'spatial_relationship',
              'purpose', 'transferable_mechanism', 'repetition', 'timing_basis'}
    if not isinstance(sequence, dict) or set(sequence) != fields:
        raise ValueError('Motion requires sequence states, trigger, continuity, spatial relationship, purpose, mechanism, repetition and timing basis')
    if sequence['method'] not in ('playback', 'representative-frames'):
        raise ValueError('Inspect playback or representative frames across the sequence')
    for field in fields - {'states', 'method'}:
        if not isinstance(sequence[field], str) or not 1 <= len(sequence[field]) <= 700:
            raise ValueError(f'Record observed {field}, or explicitly state it is unknown')
    states = sequence['states']
    if not isinstance(states, list) or not minimum_states <= len(states) <= 24:
        raise ValueError('Inspect start, transition/progression and end; a first frame is static evidence only')
    positions = []
    for state in states:
        if (not isinstance(state, dict) or set(state) != {'position', 'visible'}
                or type(state['position']) not in (int, float) or not 0 <= state['position'] <= 1
                or not isinstance(state['visible'], str) or not 1 <= len(state['visible']) <= 700):
            raise ValueError('Each observed sequence state needs a normalized position and visible change')
        positions.append(state['position'])
    if positions != sorted(set(positions)) or positions[0] != 0 or positions[-1] != 1:
        raise ValueError('Sequence observations must span ordered start through end, not repeated first frames')
    return sequence


def motion_evidence(analysis):
    if analysis.get('inspection', {}).get('method') != 'primary-motion-view':
        return False
    try:
        validate_sequence(analysis.get('sequence'), min(3, analysis.get('media', {}).get('frames', 3)))
    except (ValueError, TypeError):
        return False
    return True


def eligible(mechanism, ambition='ordinary', evidence_scope=None):
    if evidence_scope and evidence_scope not in mechanism.get('scope', []):
        return False
    return ambition != 'high' or (mechanism.get('quality', {}).get('ambition') == 'high'
        and mechanism.get('evidence', {}).get('strength') == 'clear' and bool(mechanism.get('scope')))


def exclude(path, reason):
    """Retain a non-design/broken visual, but remove it from normal design retrieval."""
    root, data, record, _ = checked(path)
    if not isinstance(reason,str) or not 15 <= len(reason) <= 1000:
        raise ValueError('Explain the observed reason for exclusion')
    record['visual_exclusion'] = {'sha256': record['sha256'], 'reason': reason, 'recorded_at': now()}
    session.save(root,data)
    return {'preserved': str(path), 'excluded': True}


def records():
    for item in session.list_sessions():
        for name, record in item['files'].items():
            if name.startswith('asset-'):
                yield str(Path(item['session']) / name), record


def cache_path():
    return session.storage_base() / 'intelligence.sqlite3'


def connect():
    base = session.storage_base()
    base.mkdir(parents=True, exist_ok=True)
    session.ordinary(base, directory=True)
    path = cache_path()
    if path.exists():
        session.ordinary(path)
    db = sqlite3.connect(path)
    db.execute('CREATE TABLE IF NOT EXISTS refs (path TEXT PRIMARY KEY, fingerprint TEXT, payload TEXT)')
    db.execute('CREATE VIRTUAL TABLE IF NOT EXISTS search USING fts5(path UNINDEXED, mechanisms, observations, surfaces, families, metadata, provenance)')
    return db


def sync():
    """Incremental transactional cache refresh; no migration writes to old receipts."""
    db = connect()
    try:
        known = dict(db.execute('SELECT path, fingerprint FROM refs'))
        seen = set()
        with db:
            for path, record in records():
                seen.add(path)
                fingerprint = session.digest(json.dumps(record, sort_keys=True).encode())
                if known.get(path) == fingerprint:
                    continue
                a = record.get('analysis', {})
                if a.get('inspection', {}).get('sha256') != record['sha256']:
                    a = {}
                m = record.get('source_metadata', {})
                old = record.get('index', {})
                payload = {**record, 'analysis': a, 'path': path}
                db.execute('INSERT OR REPLACE INTO refs VALUES(?,?,?)', (path, fingerprint, json.dumps(payload)))
                db.execute('DELETE FROM search WHERE path=?', (path,))
                db.execute('INSERT INTO search VALUES(?,?,?,?,?,?,?)', (path,
                    ' '.join(mechanism_text(x) for x in a.get('mechanisms', [])),
                    ' '.join(a.get('observations', []) + a.get('use_cases', [])),
                    ' '.join(a.get('surfaces', [])), ' '.join(a.get('families', [])),
                    json.dumps(m) + ' ' + json.dumps(old),
                    (record.get('page') or '') + ' ' + (record.get('asset') or '')))
            for path in known.keys() - seen:
                db.execute('DELETE FROM refs WHERE path=?', (path,))
                db.execute('DELETE FROM search WHERE path=?', (path,))
        return {'indexed': len(seen), 'cache': str(cache_path())}
    finally:
        db.close()


def compact(hit, query='', role=None):
    """Defer observations/receipt detail; retain concrete causes and effects."""
    mechanisms = hit['mechanisms']
    terms = expand(query)
    mechanisms = sorted(mechanisms, key=lambda m: (
        mechanism_order(m, role) if role else (),
        -len(terms & tokens(m['visible'] + ' ' + m['effect']))))
    result = {**{k: hit[k] for k in ('path','sha256','page','source','title',
            'analysis_status','task_match','evidence','limitations','source_tier','authority_priority')},
            'mechanisms': [disclose(m) for m in mechanisms[:2]]}
    if role and mechanisms:
        result['contribution_match'] = contribution_match(mechanisms[0], role)
    if hit['project'] != hit['page']:
        result['project'] = hit['project']
    return result


def mechanism_text(mechanism):
    # Evidence limitations must not become positive search terms.
    return ' '.join(mechanism[k] for k in ('role', 'visible', 'effect'))


def matched_terms(query, text):
    evidence_terms = tokens(text)
    return {t for t in tokens(query) if SYNONYMS.get(t, {t}) & evidence_terms}


def contribution_match(mechanism, role):
    matched = matched_terms(role, mechanism_text(mechanism))
    missing = tokens(role) - matched
    return {'matched': sorted(matched), 'unmatched': sorted(missing),
            'status': 'none' if not matched else 'partial' if missing else 'candidate'}


def mechanism_matches(mechanism, role):
    """Retain partial recall, but never equate it with a resolved contribution."""
    return bool(contribution_match(mechanism, role)['matched'])


def mechanism_order(mechanism, role):
    match = contribution_match(mechanism, role)
    strength = mechanism.get('evidence', {}).get('strength', 'unassessed')
    return (bool(match['unmatched']), -len(match['matched']),
            {'clear': 0, 'unassessed': 1, 'limited': 2}[strength],
            -len(matched_terms(role, mechanism['role'])))


def mechanism_key(mechanism):
    # Exact repeats only; semantic novelty is a primary visual judgment.
    return tuple(sorted(tokens(mechanism['visible']))), tuple(sorted(tokens(mechanism['effect'])))


def disclose(mechanism):
    return {**mechanism, 'evidence': mechanism.get('evidence', {'strength': 'unassessed'}),
            'scope': mechanism.get('scope', []),
            'quality': mechanism.get('quality', {'ambition': 'unassessed'})}


def hydrate(path, sha256=None, specialist=False, scopes=None, policy=None, receipt=False):
    """Recheck current permission and bytes before exposing the complete receipt."""
    policy = reference_policy.resolve() if policy is None else policy
    _, _, record, _ = checked(path)
    if sha256 is not None and sha256 != record['sha256']:
        raise ValueError('Selection hash changed; retrieve current evidence again')
    source = reference_policy.source_for(record['page'], policy, specialist, retained=True)
    if not source or not reference_policy.editorially_eligible(source, record) or (scopes is not None and not any(session.in_scope(record['page'], s) for s in scopes)):
        raise ValueError('Reference outside current source scope')
    if record.get('visual_exclusion', {}).get('sha256') == record['sha256']:
        raise ValueError('Reference excluded but preserved')
    analysis = record.get('analysis', {})
    if analysis and analysis.get('inspection', {}).get('sha256') != record['sha256']:
        raise ValueError('Analysis no longer matches retained bytes')
    if receipt:
        return {'path':str(path), 'source':source['name'], 'record':record, 'open_required':True}
    return {'path':str(path), 'sha256':record['sha256'], 'page':record['page'],
            'source':source['name'], 'analysis':analysis,
            'source_tier':source.get('tier'), 'motion_claims_supported':motion_evidence(analysis),
            'source_metadata':record.get('source_metadata', {}), 'open_required':True}


def hydrate_selected(paths, hashes=None, specialist=False, scopes=None, receipt=False):
    if not 1 <= len(paths) <= 6 or (hashes is not None and len(hashes) != len(paths)):
        raise ValueError('Hydrate 1..6 paths with one optional expected hash per path')
    policy = reference_policy.resolve()
    return {'results':[hydrate(p, hashes[i] if hashes else None, specialist, scopes, policy, receipt)
                       for i,p in enumerate(paths)]}


def search(query='', limit=4, offset=0, surface=None, family=None, role=None,
           specialist=False, scopes=None, policy=None, analyzed_only=False, full=False,
           _synced=False, _receipts=None, _verified=None, ambition='ordinary', evidence_scope=None):
    if not 1 <= limit <= 24 or offset < 0 or offset > 10000 or len(query) > 1000:
        raise ValueError('Bound retrieval to 1–24 results and offset 0–10000; query <=1000 characters')
    if ambition not in ('ordinary', 'high') or (evidence_scope and evidence_scope not in EVIDENCE_SCOPES):
        raise ValueError('Use ordinary/high ambition and a supported evidence scope')
    policy = reference_policy.resolve() if policy is None else policy
    if scopes is not None:
        scopes = [session.url(s) for s in scopes]
    if not _synced:
        sync()
    receipts = {} if _receipts is None else _receipts
    verified = {} if _verified is None else _verified
    terms = expand(query + ' ' + (role or ''))
    needs_motion = bool(tokens(query + ' ' + (role or '')) & MOTION_TERMS)
    match = ' OR '.join('"' + t + '"' for t in sorted(terms))
    db = connect()
    try:
        if match:
            rows = db.execute('SELECT r.payload, bm25(search,0,8,4,7,4,1,0.15) FROM search JOIN refs r ON r.path=search.path WHERE search MATCH ? ORDER BY 2', (match,))
        else:
            rows = db.execute('SELECT payload, 0 FROM refs ORDER BY path')
        hits = []
        for raw, rank in rows:
            r = json.loads(raw)
            if r.get('visual_exclusion', {}).get('sha256') == r['sha256']:
                continue
            source = reference_policy.source_for(r['page'], policy, specialist, retained=True)
            if not source or not reference_policy.editorially_eligible(source, r) or (scopes is not None and not any(session.in_scope(r['page'], s) for s in scopes)):
                continue
            a = r.get('analysis', {})
            if needs_motion and not motion_evidence(a):
                continue
            mechanisms = [m for m in a.get('mechanisms', []) if eligible(m, ambition, evidence_scope)]
            if (ambition == 'high' or evidence_scope) and not mechanisms:
                continue
            if analyzed_only and not a:
                continue
            if surface and not expand(surface) & tokens(' '.join(a.get('surfaces', []))):
                continue
            if family and not expand(family) & tokens(' '.join(a.get('families', []))):
                continue
            if role and not any(mechanism_matches(m, role) for m in mechanisms):
                continue
            try:
                if r['path'] not in verified:
                    verified[r['path']] = checked(r['path'], receipts)[2]['sha256']
                if verified[r['path']] != r['sha256']:
                    continue
            except (ValueError, OSError):
                continue
            visible = ' '.join(a.get('observations', []) + a.get('families', [])
                               + a.get('surfaces', [])
                               + [mechanism_text(m) for m in mechanisms])
            covered = sorted(matched_terms(query, visible))
            provider = json.dumps(r.get('source_metadata', {})) + ' ' + json.dumps(r.get('index', {}))
            hits.append({'path': r['path'], 'sha256': r['sha256'], 'page': r['page'],
                'source': source['name'], 'title': r.get('source_metadata', {}).get('title', r.get('index', {}).get('title', '')),
                'source_tier': source.get('tier'),
                'authority_priority': reference_policy.authority(source, role or query),
                'project': r.get('source_metadata', {}).get('project', r['page']),
                'analysis_status': 'analyzed' if a else 'uninspected',
                'matched_visual_terms': covered, 'rank': round(-rank, 8),
                'task_match': {'observed': covered,
                               'metadata_only': sorted(matched_terms(query, provider) - set(covered))},
                'evidence': {'image_size': a.get('image_size'),
                             'method': a.get('inspection', {}).get('method', 'uninspected'),
                             'motion_claims_supported': motion_evidence(a)},
                'observations': a.get('observations', []), 'mechanisms': mechanisms,
                'limitations': a.get('limitations', []), 'surfaces': a.get('surfaces', []),
                'open_required': True})
        hits.sort(key=lambda h: (
            min(mechanism_order(m, role) for m in h['mechanisms']) if role else (),
            h['authority_priority'],
            -len(h['matched_visual_terms']), -h['rank'], h['path']))
        selected = hits[offset:offset + limit]
        covered = set().union(*(set(h['matched_visual_terms']) for h in selected)) if selected else set()
        return {'total': len(hits), 'limit': limit, 'offset': offset,
                'results': selected if full else [compact(h, query, role) for h in selected],
                'uncovered_terms': sorted(tokens(query) - covered),
                'coverage': 'no-match' if not hits else 'candidate-evidence-needs-primary-review',
                'threshold': ambition, 'evidence_scope': evidence_scope,
                'next': 'Hydrate and inspect each selected visual. Unassessed quality/scope is not elite eligibility. Judge role, ambition, evidence adequacy and new contribution; siblings and lexical matches do not complete creative coverage.'}
    finally:
        db.close()


def complementary(roles, query='', specialist=False, scopes=None, full=False, ambition='ordinary', evidence_scope=None):
    if (not isinstance(roles, (list, tuple)) or not 1 <= len(roles) <= 8
            or any(not isinstance(r, str) or not tokens(r) or len(r) > 120 for r in roles)
            or len({r.casefold().strip() for r in roles}) != len(roles)):
        raise ValueError('Choose 1–8 distinct nonempty decision roles, each <=120 characters')
    if not isinstance(query, str) or len(query) > 800:
        raise ValueError('Keep shared task context <=800 characters')
    sync()
    policy = reference_policy.resolve()
    receipts, verified = {}, {}
    used, projects, sources, selections = set(), set(), set(), []
    mechanisms_used = {}
    for role in roles:
        result = search(query, role=role, limit=24, specialist=specialist,
                        scopes=scopes, analyzed_only=True, full=True, policy=policy,
                        _synced=True, _receipts=receipts, _verified=verified,
                        ambition=ambition, evidence_scope=evidence_scope)
        needs = tokens(role)
        candidates = []
        for h in result['results']:
            matching = [m for m in h['mechanisms'] if mechanism_matches(m, role)]
            matching.sort(key=lambda m: (mechanism_order(m, role), mechanism_key(m) in mechanisms_used))
            m = matching[0]
            matched = set(contribution_match(m, role)['matched'])
            key = mechanism_key(m)
            rank = (mechanism_order(m, role), key in mechanisms_used,
                    h['authority_priority'],
                    -len(h['task_match']['observed']),
                    h['project'] in projects, h['source'] in sources, -h['rank'], h['path'])
            candidates.append((rank, h, m, matched, key))
        candidates.sort(key=lambda row: row[0])
        candidate = candidates[0][1] if candidates else None
        selection = {'role': role, 'reference': None, 'gap': candidate is None}
        if candidate:
            _, _, mechanism, matched, key = candidates[0]
            reference = candidate if full else compact(candidate, query, role)
            if not full:
                reference['mechanisms'] = [disclose(mechanism)]
                reference['contribution_match'] = contribution_match(mechanism, role)
            selection.update(reference=reference,
                gap=bool(needs - matched) or mechanism.get('evidence', {}).get('strength') == 'limited',
                role_terms={'matched': sorted(matched), 'unmatched': sorted(needs - matched)},
                reused_reference=candidate['sha256'] in used,
                reused_project=candidate['project'] in projects,
                same_mechanism_as=list(mechanisms_used.get(key, [])))
            mechanisms_used.setdefault(key, []).append(role)
            used.add(candidate['sha256'])
            projects.add(candidate['project'])
            sources.add(candidate['source'])
        selections.append(selection)
    return {'roles': selections, 'open_required': True,
            'coverage': 'lexical-candidates-not-creative-coverage',
            'next': 'Inspect matching mechanisms. Partial matches and limited evidence leave gaps; unassessed strength and paraphrased repeats need judgment. Gap false means a candidate, never completed creative coverage.'}


def gap(query, surface=None, specialist=False, scopes=None, ambition='ordinary', evidence_scope=None):
    result = search(query, surface=surface, specialist=specialist, scopes=scopes, analyzed_only=True,
                    ambition=ambition, evidence_scope=evidence_scope)
    return {'local': result, 'discovery_if_needed': reference_policy.select(' '.join(filter(None, [query, surface])), specialist=specialist, scopes=scopes),
            'boundary': 'Discover within these approved scopes using observed search/filter links. No guessed endpoints, outbound sites, or CDN discovery. Stop on restrictions. Acquire only observed permitted visual assets; then inspect, analyze and retrieve again.'}


def coverage():
    rows = list(records())
    counts = {k: Counter() for k in ('sources', 'families', 'surfaces', 'roles', 'status')}
    invalid, hashes = [], Counter()
    for path, r in rows:
        hashes[r['sha256']] += 1
        source = reference_policy.source_for(r['page'], specialist=True, retained=True)
        counts['sources'][source['name'] if source else 'outside-current-policy'] += 1
        try:
            checked(path)
        except (ValueError, OSError):
            invalid.append(path)
            continue
        a = r.get('analysis', {})
        status = 'analyzed' if a.get('inspection', {}).get('sha256') == r['sha256'] else 'uninspected'
        if r.get('visual_exclusion', {}).get('sha256') == r['sha256']: status = 'excluded-preserved'
        counts['status'][status] += 1
        for k in ('families', 'surfaces'):
            counts[k].update(a.get(k, []))
        counts['roles'].update(m['role'] for m in a.get('mechanisms', []))
    return {'retained': len(rows), **{k: dict(v) for k,v in counts.items()}, 'invalid': invalid,
            'exact_duplicate_excess': sum(n-1 for n in hashes.values()), 'cache_rebuildable': True}


def view(paths, output):
    """Make a bounded readable sheet. Creation is NOT visual inspection evidence."""
    from PIL import Image, ImageOps, ImageDraw
    if not 1 <= len(paths) <= 6:
        raise ValueError('View 1–6 images at a time; open originals for fine details')
    out = Path(output).absolute()
    if out.exists():
        raise ValueError('Use a new temporary sheet filename')
    tiles, evidence = [], []
    for i, p in enumerate(paths):
        _, _, r, content = checked(p)
        with Image.open(io.BytesIO(content)) as im:
            im.seek(0)
            frame_count = getattr(im, 'n_frames', 1)
            thumb = ImageOps.contain(im.convert('RGB'), (800, 900))
            tile = Image.new('RGB', (820, thumb.height + 55), 'white')
            tile.paste(thumb, ((820-thumb.width)//2, 40))
            ImageDraw.Draw(tile).text((10, 10), f'{i+1} | {r["sha256"][:12]} | {im.width}x{im.height}', fill='black')
            tiles.append(tile)
        evidence.append({'number': i+1, 'path': str(p), 'sha256': r['sha256'],
                         'frames': frame_count, 'evidence_kind': 'first-frame-only' if frame_count > 1 else 'static'})
    cols = min(2, len(tiles))
    row_heights = [max(t.height for t in tiles[i:i+cols]) for i in range(0,len(tiles),cols)]
    canvas = Image.new('RGB', (cols*820, sum(row_heights)), '#cccccc')
    for i, tile in enumerate(tiles):
        canvas.paste(tile, ((i%cols)*820, sum(row_heights[:i//cols])))
    canvas.save(out)
    return {'sheet': str(out), 'images': evidence, 'inspection_status': 'not-yet-viewed',
            'next': 'Open this sheet. Animated items show FIRST FRAME ONLY: static evidence, never motion. Prefer playback or run frames for the selected item and inspect the sequence before motion analysis.'}


def frames(path, output, count=6):
    """Expose animated-image progression without claiming the model inspected it."""
    from PIL import Image, ImageOps, ImageDraw
    if not 3 <= count <= 12:
        raise ValueError('Use 3..12 representative frames')
    _, _, record, content = checked(path)
    out = Path(output).absolute()
    if out.exists():
        raise ValueError('Use a new temporary sequence sheet filename')
    with Image.open(io.BytesIO(content)) as im:
        n = getattr(im, 'n_frames', 1)
        if n < 2:
            raise ValueError('Static image has no motion sequence')
        if n > 3000:
            raise ValueError('Sequence exceeds bounded frame inspection; use available playback')
        indices = sorted({round(i * (n - 1) / (min(count, n) - 1)) for i in range(min(count, n))})
        tiles, positions, elapsed = [], [], 0
        for i in range(n):
            im.seek(i)
            if i in indices:
                thumb = ImageOps.contain(im.convert('RGB'), (640, 700))
                tile = Image.new('RGB', (660, thumb.height + 50), 'white')
                tile.paste(thumb, ((660-thumb.width)//2, 40))
                ImageDraw.Draw(tile).text((8, 10), f'Frame {i}/{n-1} | encoded start {elapsed}ms', fill='black')
                tiles.append(tile)
                positions.append({'frame': i, 'position': i/(n-1), 'encoded_start_ms': elapsed})
            elapsed += im.info.get('duration', 0)
    cols = min(3, len(tiles))
    height = max(t.height for t in tiles)
    sheet = Image.new('RGB', (cols*660, math.ceil(len(tiles)/cols)*height), '#cccccc')
    for i, tile in enumerate(tiles):
        sheet.paste(tile, ((i%cols)*660, (i//cols)*height))
    sheet.save(out)
    return {'sheet': str(out), 'sha256': record['sha256'], 'frames': n, 'samples': positions,
            'encoded_duration_ms': elapsed, 'inspection_status': 'not-yet-viewed',
            'next': 'Open this sequence sheet, then inspect extra frames/playback where needed. Sampling can miss brief events and cannot certify easing or physical feel. Record trigger/repetition as unknown when unobserved; encoded times are not measured real interaction timings.'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('sync'); sub.add_parser('coverage')
    for cmd in ('search', 'gap', 'complementary'):
        q = sub.add_parser(cmd)
        q.add_argument('--query', default='')
        q.add_argument('--specialist', action='store_true')
        q.add_argument('--scope', action='append', dest='scopes')
        q.add_argument('--ambition', choices=('ordinary', 'high'), default='ordinary')
        q.add_argument('--evidence-scope', choices=sorted(EVIDENCE_SCOPES))
        if cmd == 'complementary': q.add_argument('--role', action='append', required=True, dest='roles')
        else: q.add_argument('--surface')
        if cmd == 'search':
            q.add_argument('--family'); q.add_argument('--role')
            q.add_argument('--limit', type=int, default=4); q.add_argument('--offset', type=int, default=0)
            q.add_argument('--analyzed-only', action='store_true')
        if cmd != 'gap': q.add_argument('--full', action='store_true')
    q = sub.add_parser('hydrate'); q.add_argument('--path', required=True, action='append', dest='paths')
    q.add_argument('--sha256', action='append', dest='hashes'); q.add_argument('--specialist', action='store_true')
    q.add_argument('--receipt', action='store_true', help='Include complete acquisition/legacy record for a provenance question')
    q.add_argument('--scope', action='append', dest='scopes')
    for cmd in ('analyze', 'metadata'):
        q = sub.add_parser(cmd); q.add_argument('--path', required=True); q.add_argument('--input', required=True)
    q = sub.add_parser('exclude'); q.add_argument('--path', required=True); q.add_argument('--reason', required=True)
    q = sub.add_parser('view'); q.add_argument('--path', action='append', required=True, dest='paths'); q.add_argument('--output', required=True)
    q = sub.add_parser('frames'); q.add_argument('--path', required=True); q.add_argument('--output', required=True)
    q.add_argument('--count', type=int, default=6)
    a = vars(p.parse_args()); cmd = a.pop('command')
    try:
        if cmd in ('analyze','metadata'):
            payload = json.loads(Path(a.pop('input')).read_text(encoding='utf-8'))
            result = analyze(a['path'], payload) if cmd == 'analyze' else source_metadata(a['path'], payload)
        elif cmd == 'hydrate':
            result = hydrate_selected(**a)
        else:
            result = globals()[cmd](**a)
        print(serialize(result), end='')
    except (ValueError, OSError, KeyError, TypeError, sqlite3.Error) as exc:
        p.exit(2, f'{type(exc).__name__}: {exc}\n')


if __name__ == '__main__':
    main()
