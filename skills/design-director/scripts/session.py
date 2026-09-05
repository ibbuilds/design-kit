"""User-retained Design Kit references. No network or automatic deletion.

Ownership receipts prevent accidental deletion, not attacks by another process
running as the same user. Do not share a live session directory with other writers.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import uuid
from urllib.parse import urlsplit, urlunsplit

MAX_BYTES = 25 * 1024 * 1024
MARKER = 'session.json'


def storage_base():
    if os.name == 'nt':
        base = Path(os.environ.get('LOCALAPPDATA', Path.home() / 'AppData' / 'Local'))
    else:
        base = Path(os.environ.get('XDG_DATA_HOME', Path.home() / '.local' / 'share'))
    return base / 'design-kit' / 'references'



def digest(data):
    return hashlib.sha256(data).hexdigest()


def ordinary(path, directory=False):
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
        raise ValueError('Links and Windows reparse points are not managed')
    if directory != stat.S_ISDIR(info.st_mode):
        raise ValueError('Unexpected file type')
    if not directory and (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1):
        raise ValueError('Only ordinary, single-link files are managed')


def url(value):
    p = urlsplit(value)
    if (p.scheme != 'https' or not p.hostname or p.username or p.password
            or p.port not in (None, 443) or '\\' in value
            or any(ord(c) < 33 for c in value)):
        raise ValueError('Use a credential-free HTTPS URL without whitespace')
    # Keep paths/queries exact; reject encoded path separators/traversal ambiguity.
    if re.search(r'%(?:2f|5c|2e)', p.path, re.I) or '..' in p.path.split('/'):
        raise ValueError('Ambiguous path scope')
    return urlunsplit(('https', p.hostname.lower(), p.path or '/', p.query, ''))


def in_scope(page, scope):
    p, s = urlsplit(url(page)), urlsplit(url(scope))
    base = s.path.rstrip('/')
    return (p.netloc == s.netloc and (p.path == base or p.path.startswith(base + '/'))
            and (not s.query or p.query == s.query))


def init():
    base = storage_base().absolute()
    if base.exists():
        ordinary(base, directory=True)
    base.mkdir(parents=True, exist_ok=True)
    root = Path(tempfile.mkdtemp(prefix='design-kit-session-', dir=base)).absolute()
    data = {'schema': 1, 'owner': 'design-kit', 'id': uuid.uuid4().hex,
            'root': str(root), 'scopes': [], 'grants': [], 'files': {}}
    (root / MARKER).write_text(json.dumps(data, indent=2), encoding='utf-8')
    return {'session': str(root)}


def load(root):
    root = Path(root).absolute()
    ordinary(root, directory=True)
    if (root.parent.resolve() != storage_base().resolve()
            or not re.fullmatch(r'design-kit-session-[a-zA-Z0-9_\-]+', root.name)):
        raise ValueError('Session must be a direct child of Design Kit reference storage')
    ordinary(root / MARKER)
    data = json.loads((root / MARKER).read_text(encoding='utf-8'))
    if (data.get('owner') != 'design-kit' or data.get('schema') != 1
            or data.get('root') != str(root)
            or not re.fullmatch('[0-9a-f]{32}', data.get('id', ''))):
        raise ValueError('Invalid session receipt')
    for name, record in data['files'].items():
        if not re.fullmatch(r'(?:asset|note)-[0-9a-f]{32}\.(?:png|jpg|gif|webp|txt|json)', name):
            raise ValueError('Unsafe managed filename')
        if not re.fullmatch('[0-9a-f]{64}', record.get('sha256', '')):
            raise ValueError('Invalid file receipt')
    return root, data


def save(root, data):
    ordinary(root / MARKER)
    # All operations are local and sequential; never launch concurrent writers.
    with (root / MARKER).open('w', encoding='utf-8') as handle:
        json.dump(data, handle, indent=2)


def approve(root, scope):
    root, data = load(root)
    scope = url(scope)
    if scope not in data['scopes']:
        data['scopes'].append(scope)
        save(root, data)
    return {'approved_scope': scope}


def grant(root, page, asset, permission_checked):
    root, data = load(root)
    page, asset = url(page), url(asset)
    if not permission_checked or not any(in_scope(page, s) for s in data['scopes']):
        raise ValueError('Approved source page and permission check required')
    entry = {'page': page, 'asset': asset}
    if entry not in data['grants']:
        data['grants'].append(entry)
        save(root, data)
    return entry


def image_extension(data):
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'png'
    if data.startswith(b'\xff\xd8\xff'):
        return 'jpg'
    if data.startswith((b'GIF87a', b'GIF89a')):
        return 'gif'
    if data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return 'webp'
    raise ValueError('Expected raster image bytes, not HTML/SVG or executable content')


def put(root, source, page=None, asset=None, note=False):
    if str(source) == '-':
        return put_bytes(root, sys.stdin.buffer.read(MAX_BYTES + 1), page, asset, note)
    source = Path(source)
    ordinary(source)
    if source.stat().st_size > MAX_BYTES:
        raise ValueError('Asset exceeds per-file storage bound')
    with source.open('rb') as handle:
        content = handle.read(MAX_BYTES + 1)
    return put_bytes(root, content, page, asset, note)


def put_bytes(root, content, page=None, asset=None, note=False):
    root, data = load(root)
    if len(content) > MAX_BYTES:
        raise ValueError('Asset changed beyond storage bound')
    if note:
        content.decode('utf-8')
        extension = 'txt'
    else:
        if not page or not asset:
            raise ValueError('Reference provenance required')
        page, asset = url(page), url(asset)
        if {'page': page, 'asset': asset} not in data['grants']:
            raise ValueError('Exact observed asset URL has no grant')
        extension = image_extension(content)
    checksum = digest(content)
    # Retained sessions together form one library. Never re-import identical
    # image bytes merely because a new task uses another session.
    pools = [(root, data['files'])]
    if not note:
        pools += [(Path(s['session']), s['files']) for s in list_sessions()
                  if Path(s['session']) != root]
    for candidate_root, records in pools:
        for name, record in records.items():
            path = candidate_root / name
            if record['sha256'] != checksum or not path.exists():
                continue
            try:
                ordinary(path)
                if digest(path.read_bytes()) == checksum:
                    return {'path': str(path), 'duplicate': True}
            except (ValueError, OSError):
                continue
    name = ('note-' if note else 'asset-') + uuid.uuid4().hex + '.' + extension
    with (root / name).open('xb') as handle:
        handle.write(content)
    data['files'][name] = {'sha256': checksum, 'bytes': len(content),
                           'page': page, 'asset': asset}
    save(root, data)
    return {'path': str(root / name), 'duplicate': False}


def plan(root):
    root, data = load(root)
    delete, preserve = [], []
    for name, record in data['files'].items():
        path = root / name
        if not path.exists() and not path.is_symlink():
            continue
        try:
            ordinary(path)
            if path.stat().st_size != record['bytes'] or digest(path.read_bytes()) != record['sha256']:
                raise ValueError('Managed file changed after import')
            delete.append(name)
        except (ValueError, OSError) as exc:
            preserve.append({'name': name, 'reason': str(exc)})
    for path in root.iterdir():
        if path.name != MARKER and path.name not in data['files']:
            preserve.append({'name': path.name, 'reason': 'Not owned by this session'})
    result = {'session': str(root), 'delete': sorted(delete),
              'preserve': sorted(preserve, key=lambda r: r['name']),
              'receipt_hash': digest((root / MARKER).read_bytes())}
    result['approval_digest'] = digest(json.dumps(result, sort_keys=True).encode())
    return result


def cleanup(root, approved_digest, user_requested=False):
    if not user_requested:
        raise ValueError('Explicit user cleanup request required; completion is not consent')
    current = plan(root)
    if current['approval_digest'] != approved_digest:
        raise ValueError('Cleanup plan changed; inspect a fresh plan')
    root, data = load(root)
    for name in current['delete']:
        path = root / name
        ordinary(path)
        if digest(path.read_bytes()) != data['files'][name]['sha256']:
            raise ValueError('File changed during cleanup; preserved')
        path.unlink()
        del data['files'][name]
    save(root, data)
    if set(p.name for p in root.iterdir()) == {MARKER}:
        (root / MARKER).unlink()
        root.rmdir()
    return {'deleted': current['delete'], 'preserved': current['preserve'],
            'session_removed': not root.exists()}


def list_sessions():
    base = storage_base()
    if not base.exists():
        return []
    ordinary(base, directory=True)
    results = []
    for candidate in sorted(base.iterdir()):
        try:
            root, data = load(candidate)
            results.append({'session': str(root), 'scopes': data['scopes'],
                            'files': data['files'], 'grants': data['grants']})
        except (OSError, ValueError, KeyError, TypeError):
            continue
    return results


def annotate(root, filename, title, tags=(), description=''):
    """Attach reusable retrieval metadata to an existing image receipt."""
    root, data = load(root)
    if filename not in data['files'] or not filename.startswith('asset-'):
        raise ValueError('Choose an existing reference image filename')
    if not isinstance(title, str) or not title.strip() or len(title) > 200:
        raise ValueError('Title must contain 1–200 characters')
    if (not isinstance(description, str) or len(description) > 1200
            or len(tags) > 24 or any(not isinstance(t, str) or not t.strip()
                                      or len(t) > 80 for t in tags)):
        raise ValueError('Use compact reusable description and tags')
    ordinary(root / filename)
    data['files'][filename]['index'] = {
        'title': title.strip(), 'tags': sorted(set(t.strip() for t in tags)),
        'description': description.strip(),
    }
    save(root, data)
    return {'path': str(root / filename), **data['files'][filename]['index']}


def search(query='', scope=None, limit=20, offset=0):
    """Read-only paged search over existing receipts, including legacy records.

    No database or duplicate index; metadata is not a visual inspection claim.
    """
    if not 1 <= limit <= 100 or offset < 0:
        raise ValueError('Limit must be 1–100 and offset nonnegative')
    if scope:
        scope = url(scope)
    terms = query.casefold().split()
    hits = []
    for item in list_sessions():
        for name, record in item['files'].items():
            if not name.startswith('asset-'):
                continue
            page = record.get('page') or ''
            if scope and (not page or not in_scope(page, scope)):
                continue
            metadata = record.get('index', {})
            searchable = ' '.join([page, record.get('asset') or '',
                                   metadata.get('title', ''),
                                   metadata.get('description', ''),
                                   ' '.join(metadata.get('tags', []))]).casefold()
            if not all(term in searchable for term in terms):
                continue
            path = Path(item['session']) / name
            try:
                ordinary(path)
            except (OSError, ValueError):
                continue
            hits.append({'path': str(path), 'page': page, 'asset': record.get('asset'),
                         'sha256': record['sha256'], **metadata})
    hits.sort(key=lambda h: (h.get('title', '').casefold(), h['path']))
    return {'total': len(hits), 'offset': offset, 'limit': limit,
            'results': hits[offset:offset + limit]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('init')
    sub.add_parser('list')
    search_parser = sub.add_parser('search')
    search_parser.add_argument('--query', default='')
    search_parser.add_argument('--scope')
    search_parser.add_argument('--limit', type=int, default=20)
    search_parser.add_argument('--offset', type=int, default=0)
    for name in ('approve', 'allow-asset', 'put', 'annotate', 'plan', 'cleanup'):
        q = sub.add_parser(name)
        q.add_argument('--session', required=True)
        if name == 'approve':
            q.add_argument('--scope', required=True)
        elif name == 'allow-asset':
            q.add_argument('--page', required=True)
            q.add_argument('--asset-url', required=True)
            q.add_argument('--permission-checked', action='store_true')
        elif name == 'put':
            q.add_argument('--input', required=True)
            q.add_argument('--page')
            q.add_argument('--asset-url')
            q.add_argument('--note', action='store_true')
        elif name == 'annotate':
            q.add_argument('--file', required=True, help='Managed image filename')
            q.add_argument('--title', required=True)
            q.add_argument('--tag', action='append', default=[])
            q.add_argument('--description', default='')
        elif name == 'cleanup':
            q.add_argument('--apply', required=True, help='Digest from inspected plan')
            q.add_argument('--user-requested', action='store_true', help='Only after explicit user cleanup request')
    a = p.parse_args()
    try:
        if a.command == 'init': result = init()
        elif a.command == 'list': result = list_sessions()
        elif a.command == 'search': result = search(a.query, a.scope, a.limit, a.offset)
        elif a.command == 'approve': result = approve(a.session, a.scope)
        elif a.command == 'allow-asset': result = grant(a.session, a.page, a.asset_url, a.permission_checked)
        elif a.command == 'put': result = put(a.session, a.input, a.page, a.asset_url, a.note)
        elif a.command == 'annotate': result = annotate(a.session, a.file, a.title, a.tag, a.description)
        elif a.command == 'plan': result = plan(a.session)
        else: result = cleanup(a.session, a.apply, a.user_requested)
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        p.exit(2, f'{type(exc).__name__}: {exc}\n')


if __name__ == '__main__':
    main()
