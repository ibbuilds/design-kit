"""Run fresh read-only Codex workflow probes. Saves evidence; never grades itself."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent


def run(output, case_ids, model=None):
    output = Path(output).absolute()
    output.mkdir(parents=True, exist_ok=False)
    executable = shutil.which('codex')
    if not executable:
        raise RuntimeError('Codex CLI is required; no simulated fallback')
    cases = json.loads((HERE / 'cases.json').read_text(encoding='utf-8'))
    selected = [c for c in cases if not case_ids or c['id'] in case_ids]
    if case_ids and len(selected) != len(set(case_ids)):
        raise ValueError('Unknown or duplicate case ID')
    with tempfile.TemporaryDirectory(prefix='design-kit-eval-workspace-') as workspace:
        for case in selected:
            # Expected criteria are deliberately withheld from the evaluated model.
            prompt = (case['request'] + '\n\nThis is a bounded, read-only workflow probe. '
                      'Use relevant installed skills as you ordinarily would; read only the '
                      'resources needed for this request. Do not modify files or external apps, '
                      'browse websites, install tools, or start agents. Stop before any external '
                      'action. Report what you actually read and did in the required JSON. '
                      'Do not pretend that an unobserved artifact was inspected.')
            command = [executable, 'exec', '--ephemeral', '--json', '--sandbox', 'read-only',
                       '--skip-git-repo-check', '-C', workspace, '--output-schema',
                       str(HERE / 'response.schema.json'), '-o', str(output / (case['id'] + '.json')), '-']
            if model:
                command[2:2] = ['--model', model]
            with (output / (case['id'] + '.events.jsonl')).open('w', encoding='utf-8') as log:
                completed = subprocess.run(command, input=prompt, text=True, encoding='utf-8',
                                           stdout=log, stderr=subprocess.STDOUT, timeout=300)
            print(json.dumps({'id': case['id'], 'exit_code': completed.returncode}), flush=True)
            if completed.returncode:
                raise RuntimeError(f"Probe failed: {case['id']}; inspect its log, do not report pass")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    parser.add_argument('--case', action='append')
    parser.add_argument('--model', help='Explicit per-probe compatibility override; saved settings unchanged')
    args = parser.parse_args()
    run(args.output, args.case, args.model)
