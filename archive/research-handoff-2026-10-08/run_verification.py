#!/usr/bin/env python3
"""Run the consolidated and all three preserved scientific suites.

This wrapper requires a new output directory outside the package. Canonical
reports and all scientific assertion tolerances are unchanged. Report equality
is stricter than mathematical correctness: numerical drift is recorded and
returns status 2 for review, never silently accepted or used to refresh a source.
"""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def verify_manifests():
    checks={}
    for p in sorted((ROOT/'prior').rglob('MANIFEST.json')):
        data=json.loads(p.read_text())
        for name,row in data.items():
            f=p.parent/name
            if sha(f)!=row['sha256'] or ('bytes' in row and f.stat().st_size!=row['bytes']):
                raise AssertionError(f'Protected input mismatch: {f.relative_to(ROOT)}')
        checks[str(p.relative_to(ROOT))]=len(data)
    if (ROOT/'MANIFEST.json').is_file():
        data=json.loads((ROOT/'MANIFEST.json').read_text())
        for name,row in data.items():
            if sha(ROOT/name)!=row['sha256']:
                raise AssertionError(f'Package mismatch: {name}')
        checks['MANIFEST.json']=len(data)
    return checks

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',required=True,type=Path)
    out=ap.parse_args().output_dir.resolve()
    if out.exists():ap.error('Output directory already exists')
    if out.is_relative_to(ROOT):ap.error('Use an output directory outside the package')
    before=verify_manifests();protected={str(p.relative_to(ROOT)):sha(p) for p in (ROOT/'prior').rglob('*') if p.is_file()}
    out.mkdir(parents=True)
    jobs=[('consolidation','check_consolidation.py','evidence/first.json',4),
          ('stability','prior/check_review.py','prior/evidence/final.json',5),
          ('global','prior/prior/check_followup.py','prior/prior/evidence/enriched.json',6),
          ('pilot','prior/prior/prior/check_pilot.py','prior/prior/prior/evidence/final.json',6)]
    env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    receipt={'manifests_before':before,'runs':[],'scope':'All original mathematical checks unchanged; report nonidentity requires review.'}
    status=0
    for name,script,reference,groups in jobs:
        report=out/f'{name}.json';log=out/f'{name}.log';start=time.monotonic()
        with log.open('x') as f:
            result=subprocess.run([sys.executable,str(ROOT/script),'--output',str(report)],cwd=ROOT,
                                  env=env,stdout=f,stderr=subprocess.STDOUT,timeout=60)
        row={'name':name,'script':script,'script_sha256':sha(ROOT/script),'returncode':result.returncode,
             'expected_groups':groups,'elapsed_seconds':time.monotonic()-start,'canonical':reference}
        if report.exists():
            data=json.loads(report.read_text());actual=data.get('test_groups',data.get('tests_run'))
            row.update(actual_groups=actual,status=data.get('status'),report_sha256=sha(report),
                       canonical_sha256=sha(ROOT/reference),byte_identical=report.read_bytes()==(ROOT/reference).read_bytes())
            if actual!=groups or data.get('status')!='PASS':status=1
            elif not row['byte_identical'] and status==0:status=2
        else:status=1
        if result.returncode:status=1
        receipt['runs'].append(row);print(name,row.get('status'),row.get('byte_identical'),flush=True)
    after={str(p.relative_to(ROOT)):sha(p) for p in (ROOT/'prior').rglob('*') if p.is_file()}
    if before!=verify_manifests() or protected!=after:raise AssertionError('Source changed during execution')
    receipt.update(protected_file_count=len(protected),source_unchanged=True,
                   status='PASS' if status==0 else ('REPORT_REVIEW_REQUIRED' if status==2 else 'FAIL'))
    with (out/'receipt.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    raise SystemExit(status)
if __name__=='__main__':main()
