#!/usr/bin/env python3
"""Install this skill locally without network access or application changes."""
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
import sys
import tempfile

PACKAGE = (
    "SKILL.md", "agents/openai.yaml", "README.md", "BRIEF.md", "TASTE.md",
    "GUIDELINES.md", "QA.md", "REFERENCES.md", "WORKFLOW.md", "RESEARCH.md",
    "docs/EXECUTION_DECISION.md", "scripts/install.py", "tests/test_install.py",
    "REFERENCE_ROUTER.md", "EXECUTION.md", "SOFTWARE.md",
    "DESIGN_DIRECTION.md", "docs/QUALITY_EVIDENCE.md",
)
MANIFEST = ".design-kit-manifest.json"
START = "<!-- design-kit:begin -->"
END = "<!-- design-kit:end -->"
POINTER = (
    START + "\nFor frontend design, implementation, or review, read and apply\n"
    "`.agents/skills/design-kit/SKILL.md`. Preserve this project's own\n"
    "instructions and use its existing brief and accepted implementation.\n" + END + "\n"
)
SOFTWARE_RULE = (
    "For programming tasks, read and apply `.agents/skills/design-kit/SOFTWARE.md`.\n"
    "Use Design Kit for visual/frontend decisions in mixed tasks; backend-only\n"
    "work does not need the design reference library.\n"
)
LEGACY = (
    "For frontend design, implementation or review, read `.design-kit/AGENTS.md`\n"
    "as supplemental guidance and follow its selective reading routes.\n"
    "Preserve this project's instructions, stack and conventions.\n"
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def guarded_path(root, relative):
    """Refuse symlinked write paths and non-directory parents."""
    path = root / relative
    if not path.is_relative_to(root):
        raise ValueError("Path outside target: " + str(path))
    current = root
    for part in Path(relative).parts:
        if part in ("..", ""):
            raise ValueError("Unsafe relative path")
        current = current / part
        if current.is_symlink():
            raise ValueError("Refusing symlink: " + str(current))
        if current != path and current.exists() and not current.is_dir():
            raise ValueError("Parent is not a directory: " + str(current))
    if path.exists() and not path.is_file():
        raise ValueError("Expected a file: " + str(path))
    return path


def pointer_text(text, with_software=None):
    """Replace only our block or the exact documented legacy pointer."""
    if text.count(START) != text.count(END) or text.count(START) > 1:
        raise ValueError("Malformed or duplicate Design Kit markers in instruction file")
    if START in text:
        start, end = text.index(START), text.index(END)
        if end < start:
            raise ValueError("Reversed Design Kit markers in instruction file")
        end += len(END)
        # Older manifests derive the choice only from our marked block,
        # never from arbitrary project prose.
        if with_software is None:
            with_software = ".agents/skills/design-kit/SOFTWARE.md" in text[start:end]
        if text[end:end + 2] == "\r\n":
            end += 2
        elif text[end:end + 1] == "\n":
            end += 1
        pointer = POINTER.replace(END, SOFTWARE_RULE + END) if with_software else POINTER
        return text[:start] + pointer + text[end:]
    text = text.replace(LEGACY, "").replace(LEGACY.replace("\n", "\r\n"), "")
    separator = "" if not text or text.endswith("\n") else "\n"
    pointer = POINTER.replace(END, SOFTWARE_RULE + END) if with_software else POINTER
    return text + separator + pointer


def instruction_path(target):
    """Write into the active root instruction file, not one Codex will skip."""
    override = guarded_path(target, "AGENTS.override.md")
    if override.exists() and override.read_bytes().strip():
        return override
    return guarded_path(target, "AGENTS.md")


def installation_plan(source, target, with_software=None):
    source, target = Path(source).resolve(), Path(target).resolve()
    if not target.is_dir():
        raise ValueError("Target must be an existing project directory")
    if target == source:
        raise ValueError("Select the application project, not the kit checkout")
    bundle = Path(".agents/skills/design-kit")
    manifest_path = guarded_path(target, bundle / MANIFEST)
    destination = target / bundle
    previous = {}
    previous_software = None
    if manifest_path.exists():
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("format") != 1 or data.get("name") != "design-kit":
            raise ValueError("Unrecognized installation manifest")
        previous = data.get("files")
        if not isinstance(previous, dict) or not set(previous).issubset(PACKAGE):
            raise ValueError("Invalid managed-file list")
        if not all(isinstance(v, str) and len(v) == 64 for v in previous.values()):
            raise ValueError("Invalid managed-file hashes")
        previous_software = data.get("software")
        if previous_software is not None and not isinstance(previous_software, bool):
            raise ValueError("Invalid software routing state")
    elif destination.exists() and any(destination.iterdir()):
        raise ValueError("Existing skill is not managed by this installer; review it first")

    planned, hashes = [], {}
    for relative in PACKAGE:
        incoming = guarded_path(source, relative)
        if not incoming.is_file():
            raise ValueError("Missing or symlinked package file: " + relative)
        payload = incoming.read_bytes()
        hashes[relative] = digest(payload)
        output = guarded_path(target, bundle / relative)
        if output.exists():
            current = output.read_bytes()
            if current == payload:
                continue
            if digest(current) != previous.get(relative):
                raise ValueError("Locally edited/unmanaged file; refusing overwrite: " + str(output))
        planned.append((output, payload))

    agents = instruction_path(target)
    old = agents.read_bytes() if agents.exists() else b""
    text = old.decode("utf-8")
    # The saved choice survives a new override or a return to a stale fallback
    # block. Older manifests derive their initial choice from the active block.
    routing = previous_software if with_software is None else with_software
    new = pointer_text(text, routing).encode("utf-8")
    data = {"format": 1, "name": "design-kit", "files": hashes,
            "software": SOFTWARE_RULE.encode("utf-8") in new}
    payload = (json.dumps(data, indent=2, sort_keys=True) + "\n").encode()
    if not manifest_path.exists() or manifest_path.read_bytes() != payload:
        planned.append((manifest_path, payload))
    if old != new:
        planned.append((agents, new))
    return planned


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else None
    fd, name = tempfile.mkstemp(prefix=".design-kit-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        if mode is not None:
            os.chmod(name, mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def install(source, target, check=False, with_software=None):
    # Preflight every conflict before changing any file. Writes are atomic per file.
    planned = installation_plan(source, target, with_software)
    if check:
        return planned
    originals = [(path, path.read_bytes() if path.exists() else None) for path, _ in planned]
    completed = []
    try:
        for (path, payload), (_, original) in zip(planned, originals):
            atomic_write(path, payload)
            completed.append((path, original))
    except OSError:
        # Best-effort rollback for ordinary write errors; not a crash transaction.
        for path, original in reversed(completed):
            try:
                path.unlink() if original is None else atomic_write(path, original)
            except OSError:
                pass
        raise
    return planned


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    parser.add_argument("--check", action="store_true", help="Report drift without writes (exit 1 if changes needed)")
    routing = parser.add_mutually_exclusive_group()
    routing.add_argument("--with-software", dest="with_software", action="store_true", help="Activate engineering guidance for programming as well as design")
    routing.add_argument("--design-only", dest="with_software", action="store_false", help="Keep only the frontend instruction pointer")
    parser.set_defaults(with_software=None)
    args = parser.parse_args()
    try:
        planned = install(Path(__file__).resolve().parents[1], args.target, args.check, args.with_software)
    except (ValueError, OSError) as error:
        print("ERROR: " + str(error), file=sys.stderr)
        return 2
    print(("CHECK: " if args.check else "INSTALL: ") + str(len(planned)) + " file(s) " + ("need changes" if args.check else "changed"))
    for path, _ in planned:
        print(path.relative_to(args.target.resolve()))
    print("No model calls, dependency installation, or network requests performed.")
    print("This is a package check, not a test of model activation or design quality.")
    return 1 if args.check and planned else 0


if __name__ == "__main__":
    raise SystemExit(main())
