"""Build a new local marketplace using installed official creator helpers.

Never overwrites an existing output directory, registers a marketplace or pushes Git.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = ('.codex-plugin', 'skills', 'README.md')


def files():
    result = []
    for name in INCLUDE:
        entry = ROOT / name
        if not entry.exists():
            raise ValueError(f'Required package entry missing: {name}')
        for path in ([entry] if entry.is_file() else entry.rglob('*')):
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
                raise ValueError(f'Package may not contain links/reparse points: {path}')
            if path.is_file() and '__pycache__' not in path.parts and path.suffix not in ('.pyc', '.pyo'):
                result.append(path)
    return sorted(result)


def build(output, creator):
    output = Path(output).absolute()
    creator = Path(creator).resolve()
    helpers = creator / 'scripts'
    for helper in ('create_basic_plugin.py', 'validate_plugin.py'):
        if not (helpers / helper).is_file():
            raise ValueError(f'Installed plugin-creator helper missing: {helper}')
    selected = files()
    if output.exists() or Path(str(output) + '.zip').exists():
        raise ValueError('Use a new output path; existing packages are never overwritten')
    output.mkdir(parents=True)
    subprocess.run([sys.executable, '-B', str(helpers / 'create_basic_plugin.py'),
                    'design-kit', '--path', str(output / 'plugins'), '--with-marketplace',
                    '--marketplace-path', str(output / '.agents/plugins/marketplace.json')], check=True)
    plugin = output / 'plugins/design-kit'
    for source in selected:
        target = plugin / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    subprocess.run([sys.executable, '-B', str(helpers / 'validate_plugin.py'), str(plugin)], check=True)
    archive = Path(str(output) + '.zip')
    with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as z:
        for path in sorted(output.rglob('*')):
            if path.is_file():
                z.write(path, path.relative_to(output).as_posix())
    return {'marketplace_root': str(output), 'plugin_root': str(plugin),
            'archive': str(archive), 'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--creator-skill', required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.output, args.creator_skill), indent=2))
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(2, f'{exc}\n')
