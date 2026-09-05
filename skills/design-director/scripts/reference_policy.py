"""Read-only source preferences. No browsing, configuration writes or task memory."""
import json
import argparse
import os
import re
from pathlib import Path
import sys
from urllib.parse import urlsplit

DEFAULTS = Path(__file__).resolve().parents[1] / 'references/reference-sources.json'


def preferences_path():
    if os.name == 'nt':
        base = Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData/Local'))
    else:
        base = Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config'))
    return base / 'design-kit/preferences.json'


def validate(data):
    if not isinstance(data, dict) or type(data.get('version')) is not int or data['version'] != 1:
        raise ValueError('Expected reference preferences version 1')
    if set(data) - {'version', 'sources', 'specialist_sources'}:
        raise ValueError('Unknown reference preference field')
    for key in ('sources', 'specialist_sources'):
        if key not in data:
            continue
        if not isinstance(data[key], list):
            raise ValueError(f'{key} must be a list; [] disables this pool')
        seen = set()
        for source in data[key]:
            if not isinstance(source, dict) or set(source) - {'name', 'url', 'when', 'id', 'aliases', 'provenance_aliases', 'collection', 'verified_on', 'acquisition', 'specialties', 'preferred_subset', 'artifacts', 'request_interval_seconds', 'tier', 'allowed_roles', 'inappropriate_roles'}:
                raise ValueError('Expected source name, url and optional when')
            if not all(isinstance(source.get(k), str) and source[k].strip() for k in ('name', 'url')):
                raise ValueError('Source name and URL must be nonempty strings')
            if 'when' in source and (not isinstance(source['when'], str) or not source['when'].strip()):
                raise ValueError('when must describe relevance')
            url = source['url']
            parsed = urlsplit(url)
            if (parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password
                    or parsed.port not in (None, 443) or parsed.query or parsed.fragment
                    or any(c.isspace() for c in url) or '\\' in url
                    or '%' in parsed.path or any(p in ('.', '..') for p in parsed.path.split('/'))):
                raise ValueError('Source must be a credential-free HTTPS origin/path scope')
            normalized = (parsed.hostname.lower(), parsed.path.rstrip('/'))
            if normalized in seen:
                raise ValueError('Duplicate source scope')
            seen.add(normalized)
            aliases = source.get('aliases', [])
            if not isinstance(aliases, list):
                raise ValueError('aliases must be a list of explicit source scopes')
            historical = source.get('provenance_aliases', [])
            if not isinstance(historical, list):
                raise ValueError('provenance_aliases must be a list; never active discovery scopes')
            extra = aliases + historical + ([source['collection']] if 'collection' in source else [])
            for value in extra:
                validate({'version': 1, 'sources': [{'name': source['name'], 'url': value}]})
            for field in ('specialties', 'allowed_roles', 'inappropriate_roles'):
                if field in source and (not isinstance(source[field], list) or not source[field] or any(not isinstance(x, str) or not x.strip() for x in source[field])):
                    raise ValueError(f'{field} must be nonempty text labels')
            if 'tier' in source and (type(source['tier']) is not int or source['tier'] not in (1, 2, 3)):
                raise ValueError('Source tier must be 1, 2 or 3')
            if 'request_interval_seconds' in source and (type(source['request_interval_seconds']) not in (int, float) or not 0.5 <= source['request_interval_seconds'] <= 60):
                raise ValueError('Source request interval must be 0.5..60 seconds')
            if 'artifacts' in source and (not isinstance(source['artifacts'], str) or not source['artifacts'].strip()):
                raise ValueError('artifacts must describe verified availability or uncertainty')
            if 'preferred_subset' in source:
                subset = source['preferred_subset']
                if not isinstance(subset, dict) or set(subset) != {'label', 'url', 'broader_use'} or any(not isinstance(v, str) or not v.strip() for v in subset.values()):
                    raise ValueError('Expected editorial subset label, URL and broader-use distinction')
                # Query-bearing collection links are entry points, never new scopes.
                if not source_for(subset['url'], {'sources': [source], 'specialist_sources': []}):
                    raise ValueError('Editorial subset must remain within its approved source')
            for field in ('id', 'verified_on'):
                if field in source and (not isinstance(source[field], str) or not source[field].strip()):
                    raise ValueError(f'{field} must be nonempty text')
            if 'acquisition' in source:
                a = source['acquisition']
                fields = {'mode','retention','bulk','discovery','evidence','constraints','integration'}
                if not isinstance(a,dict) or set(a) != fields:
                    raise ValueError('Expected complete acquisition policy')
                if a['mode'] not in ('broad','bounded','targeted','research','link-only'):
                    raise ValueError('Unknown acquisition mode')
                if a['retention'] not in ('local-reference','per-item','link-only') or a['bulk'] not in ('permitted','prohibited','not-established'):
                    raise ValueError('Unknown retention/bulk policy')
                if a['mode']=='broad' and a['bulk']!='permitted':
                    raise ValueError('Broad acquisition requires established bulk permission')
                for field in ('discovery','evidence'):
                    if not isinstance(a[field],list) or not a[field] or any(not isinstance(x,str) or not x.strip() for x in a[field]):
                        raise ValueError(f'Expected acquisition {field} list')
                for field in ('constraints','integration'):
                    if not isinstance(a[field],str) or not a[field].strip():
                        raise ValueError(f'Expected acquisition {field}')
    return data


def resolve(path=None, defaults=DEFAULTS):
    """Present fields replace their pool completely; absent fields inherit defaults."""
    base = validate(json.loads(Path(defaults).read_text(encoding='utf-8')))
    path = Path(path) if path is not None else preferences_path()
    try:
        raw = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # Only absence permits defaults; malformed/unreadable preferences fail closed.
        if path.is_symlink():
            raise ValueError('Broken preferences link; do not silently use defaults')
        user = {}
    else:
        user = validate(json.loads(raw))
    return {
        'version': 1,
        'preferences_path': str(path),
        'sources': current_pool(user.get('sources', base['sources']), base),
        'specialist_sources': current_pool(user.get('specialist_sources', base['specialist_sources']), base),
        'origin': {k: 'user' if k in user else 'built-in' for k in ('sources', 'specialist_sources')},
    }


def current_pool(pool, base):
    """Read-time retirement of stale identity aliases; never rewrite user data."""
    current = base['sources'] + base.get('specialist_sources', [])
    result = []
    for original in pool:
        source = dict(original)
        host = urlsplit(source['url']).hostname.removeprefix('www.')
        if host == 'godly.design':
            continue
        if host == 'godly.website':
            source = dict(next(s for s in current if s['id'] == 'recent'))
        elif host == 'recent.design':
            source.update(name='Recent', id='recent')
        if 'aliases' in source:
            source['aliases'] = [a for a in source['aliases'] if urlsplit(a).hostname.removeprefix('www.') not in ('godly.design', 'godly.website')]
        canonical = next((s for s in current if s['url'].rstrip('/') == source['url'].rstrip('/')), None)
        if canonical:
            for field in ('tier', 'allowed_roles', 'inappropriate_roles'):
                if field in canonical:
                    source[field] = canonical[field]
        if source not in result:
            result.append(source)
    return result


def editorially_eligible(source, record):
    # Access to the domain does not approve every item in the domain's collection.
    if source.get('id') != 'siteinspire':
        return True
    if record.get('source_metadata', {}).get('curated_subset') == 'Selected':
        return True
    collection = 'https://www.siteinspire.com/websites/selected'
    return any(p.get('observed_on', '').rstrip('/') == collection
               for p in record.get('acquisition_provenance', []))


def source_for(page, policy=None, specialist=False, *, retained=False):
    """An exact approved origin/path, never an outbound gallery link or CDN host."""
    from session import url, in_scope
    from urllib.parse import urlunsplit
    def normalized(value):
        p = urlsplit(url(value))
        host = p.hostname.removeprefix('www.')
        return urlunsplit(('https', host, p.path, p.query, ''))
    try:
        page = normalized(page)
    except (ValueError, TypeError):
        return None
    policy = resolve() if policy is None else policy
    pool = policy['sources'] + (policy['specialist_sources'] if specialist else [])
    for source in pool:
        scopes = [source['url'], *source.get('aliases', [])]
        if retained:
            scopes += source.get('provenance_aliases', [])
        if any(in_scope(page, normalized(scope)) for scope in scopes):
            return source
    return None


def acquisition_for(source):
    # Older user preference records remain valid, but never inherit permission to
    # automate or retain images from an unrelated default gallery.
    return source.get('acquisition', {'mode':'research','retention':'per-item',
        'bulk':'not-established','discovery':['observed source navigation'],
        'evidence':[], 'constraints':'Verify current access and individual retention rights before acquisition.',
        'integration':'No integration verified.'})


def words(text):
    return set(re.findall(r'[^\W_]+', text.casefold())) - set(
        'a an the design improve this for of and best premium high end quality website websites web page landing software saas product general macro overall art direction composition'.split())


def specialty_matches(source, query):
    need = words(query)
    lexical = lambda text: set(re.findall(r'[^\W_]+', text.casefold())) - {'a', 'an', 'the', 'for', 'of', 'and', 'design'}
    context = lexical(query)
    matches = []
    for label in source.get('specialties', []):
        terms = words(label)
        if terms & need:
            full = lexical(label)
            overlap = len(full & context)
            matches.append((overlap / len(full) + overlap + (4 if full <= context else 0), label))
    return sorted(matches, reverse=True)


def authority(source, query=''):
    """Retrieval priority only. Never certifies an individual visual's quality.

    Unknown custom sources keep user ordering ahead of defaults. Tier 2 has maximum
    authority on a specialty match; general art direction starts with Tier 1.
    Tier 3 semantic overlap can never move it above either relevant authority.
    """
    tier = source.get('tier')
    if tier is None:
        return 0
    if tier == 2 and any(words(label) and words(label) <= words(query) for label in source.get('specialties', [])):
        return 0
    return {1: 1, 2: 2, 3: 3}[tier]


def select(query, limit=4, policy=None, specialist=False, scopes=None):
    """Bounded authority-first discovery; no network or visual acceptance."""
    from session import in_scope
    if not isinstance(query, str) or len(query) > 2000 or not 1 <= limit <= 8:
        raise ValueError('Use a compact query and source limit 1..8')
    policy = resolve() if policy is None else policy
    pool = policy['sources'] + (policy['specialist_sources'] if specialist else [])
    ranked = []
    for i, source in enumerate(pool):
        if scopes is not None and not any(in_scope(source['url'], s) or in_scope(s, source['url']) for s in scopes):
            continue
        matches = specialty_matches(source, query)
        score = max((m[0] for m in matches), default=0)
        ranked.append((authority(source, query), score, i, source, [label for _, label in matches]))
    ranked.sort(key=lambda x: (x[0], -x[1], x[2]))
    # Return a useful slice of the leading authority group; no forced tier phases.
    if ranked:
        leading = ranked[0][0]
        score = ranked[0][1]
        ranked = [row for row in ranked if row[0] == leading
                  or (leading == 0 and row[0] == 1 and row[1] > 0)]
        if score > 0:
            ranked = [row for row in ranked if row[1] >= score / 2]
    return [{'source': s['name'], 'scope': s['url'], 'entry': s.get('preferred_subset', {}).get('url', s.get('collection', s['url'])),
             'tier': s.get('tier'), 'allowed_roles': s.get('allowed_roles', []),
             'inappropriate_roles': s.get('inappropriate_roles', []),
             'matched_specialties': labels, 'preferred_subset': s.get('preferred_subset'),
             'query': query, 'acquisition': acquisition_for(s), 'artifacts': s.get('artifacts', 'Inspect relevant source artifacts; availability is not visual verification.')}
            for _, _, _, s, labels in ranked[:limit]]


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument('--query')
        parser.add_argument('--limit', type=int, default=4)
        parser.add_argument('--specialist', action='store_true')
        args = parser.parse_args()
        result = select(args.query, args.limit, specialist=args.specialist) if args.query is not None else resolve()
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except (ValueError, OSError) as error:
        print(f'Reference preferences unavailable: {error}. Do not fall back to defaults.', file=sys.stderr)
        sys.exit(1)
