#!/usr/bin/env python3
"""Verify source integrity and run all 21 original scientific check groups.

The archived wrapper and every scientific assertion remain unchanged. Exit code
2 means canonical report review is required; it is not silently converted to a pass.
"""
from __future__ import annotations
import argparse
import json
import os
import platform
from pathlib import Path
import subprocess
import sys
from integrity import ROOT, snapshot, verify_all


def dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')


def git_value(*args: str):
    result = subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else None


def differences(expected, actual, path='$'):
    found = []
    if type(expected) is not type(actual):
        return [{'path': path, 'kind': 'type', 'expected': repr(expected), 'actual': repr(actual)}]
    if isinstance(expected, dict):
        if set(expected) != set(actual):
            found.append({'path': path, 'kind': 'keys', 'expected': sorted(expected), 'actual': sorted(actual)})
        for key in sorted(set(expected) & set(actual)):
            found += differences(expected[key], actual[key], f'{path}.{key}')
    elif isinstance(expected, list):
        if len(expected) != len(actual):
            found.append({'path': path, 'kind': 'length', 'expected': len(expected), 'actual': len(actual)})
        for i, (left, right) in enumerate(zip(expected, actual)):
            found += differences(left, right, f'{path}[{i}]')
    elif expected != actual:
        row = {'path': path, 'kind': 'value', 'expected': expected, 'actual': actual}
        if isinstance(expected, (int, float)) and not isinstance(expected, bool):
            row['absolute_difference'] = abs(expected-actual)
        found.append(row)
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    archive = ROOT/'archive/research-handoff-2026-10-08'
    if out.exists():
        parser.error('Output directory must be new')
    if out.is_relative_to(ROOT) and not out.is_relative_to(ROOT/'build'):
        parser.error('Use build/ or an external directory, never the source tree or archive')
    checks = verify_all()
    before = snapshot()
    out.mkdir(parents=True)
    dump(out/'source-manifest.json', before)
    import numpy, scipy, sympy
    dump(out/'environment.json', {'python': sys.version, 'platform': platform.platform(),
         'numpy': numpy.__version__, 'scipy': scipy.__version__, 'sympy': sympy.__version__})
    env = os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    with (out/'infrastructure.log').open('w') as log:
        tests = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                               cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=60)
    receipt = {'integrity': checks, 'commit': git_value('rev-parse', 'HEAD'),
               'tree': git_value('rev-parse', 'HEAD^{tree}'),
               'infrastructure_returncode': tests.returncode,
               'git_status': git_value('status', '--porcelain'),
               'execution_context': 'github_actions' if os.environ.get('GITHUB_ACTIONS') == 'true' else 'local'}
    if tests.returncode:
        receipt['status'] = 'FAIL'
        dump(out/'repository-receipt.json', receipt)
        return 1
    with (out/'scientific-wrapper.log').open('w') as log:
        result = subprocess.run([sys.executable, str(archive/'run_verification.py'),
                                 '--output-dir', str(out/'scientific')],
                                cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=300)
    receipt['scientific_wrapper_returncode'] = result.returncode
    source_equal = before == snapshot()
    verify_all()
    receipt['all_source_unchanged'] = source_equal
    source_receipt = out/'scientific/receipt.json'
    comparisons = []
    total_groups = 0
    if source_receipt.is_file():
        run_record = json.loads(source_receipt.read_text())
        for row in run_record['runs']:
            total_groups += row.get('actual_groups', 0)
            generated = out/'scientific'/f'{row["name"]}.json'
            original = archive/row['canonical']
            comparisons.append({'name': row['name'], 'byte_identical': generated.read_bytes()==original.read_bytes(),
                                'differences': differences(json.loads(original.read_text()), json.loads(generated.read_text()))})
        receipt['scientific_status'] = run_record['status']
    dump(out/'report-comparisons.json', comparisons)
    receipt['scientific_groups'] = total_groups
    receipt['source_files'] = len(before)
    receipt['all_canonical_reports_byte_identical'] = len(comparisons)==4 and all(r['byte_identical'] for r in comparisons)
    code = result.returncode
    if not source_equal or total_groups != 21:
        code = 1
    receipt['status'] = 'PASS' if code==0 else ('REPORT_REVIEW_REQUIRED' if code==2 else 'FAIL')
    dump(out/'repository-receipt.json', receipt)
    print(json.dumps(receipt, indent=2))
    return code

if __name__ == '__main__':
    raise SystemExit(main())
