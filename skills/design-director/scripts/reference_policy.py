"""Read-only source preferences. No browsing, configuration writes or task memory."""
import json
import os
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
            if not isinstance(source, dict) or set(source) - {'name', 'url', 'when'}:
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
        'sources': user.get('sources', base['sources']),
        'specialist_sources': user.get('specialist_sources', base['specialist_sources']),
        'origin': {k: 'user' if k in user else 'built-in' for k in ('sources', 'specialist_sources')},
    }


if __name__ == '__main__':
    try:
        print(json.dumps(resolve(), indent=2, ensure_ascii=False))
    except (ValueError, OSError) as error:
        print(f'Reference preferences unavailable: {error}. Do not fall back to defaults.', file=sys.stderr)
        sys.exit(1)
