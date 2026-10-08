"""Infrastructure tests, kept separate from the preserved scientific suites."""
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from integrity import (ROOT, check_entry, current_metadata, reproduce_active, safe_path,
                       source_files, verify_active, verify_archive, verify_links, verify_metadata)

class IntegrityTests(unittest.TestCase):
    def test_archive_inventory(self):
        self.assertEqual(verify_archive()['archive_files'], 89)

    def test_import_and_license(self):
        data = json.loads((ROOT/'provenance/IMPORT.json').read_text())
        self.assertEqual(data['repository'], 'GoGoKo699/Photon-Distillation-Yield-Limits')
        self.assertEqual(data['base_commit'], '5aa1c3aaa90375ef329e42e62260f06c37be2975')
        raw = (ROOT/'LICENSE').read_bytes()
        digest = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        self.assertEqual(digest, 'e17a781bf47c4aadf18b68fc593846a1193b86c1')

    def test_nested_manifests(self):
        self.assertEqual(sorted(verify_archive()['manifests'].values()), [14,40,61,88])

    def test_active_reproduction(self):
        self.assertEqual(verify_active(), 3)
        for row in json.loads((ROOT/'provenance/ACTIVE_EDITS.json').read_text())['copies']:
            source = (ROOT/row['source']).read_text()
            active = reproduce_active(row)
            self.assertEqual(re.findall(r'\$\$(.*?)\$\$', source, re.S),
                             re.findall(r'\$\$(.*?)\$\$', active, re.S))

    def test_metadata(self):
        self.assertGreaterEqual(verify_metadata(), 18)
        self.assertNotIn('provenance/IMPORT.json', current_metadata())
        self.assertFalse(any(p.startswith('archive/research-handoff-2026-10-08/') for p in current_metadata()))

    def test_links(self):
        self.assertGreater(verify_links(), 30)

    def test_contact_and_task(self):
        notice = 'This repository serves as a record of the work and a guide for the author’s self-directed learning.'
        for name in ['README.md', 'llms.txt']:
            self.assertIn(notice, (ROOT/name).read_text())
            self.assertIn('(mailto:gogoko699@gmail.com)', (ROOT/name).read_text())
        text = (ROOT/'research/MODEL_AND_CLAIMS.md').read_text()
        self.assertIn('outcome-dependent', text)
        self.assertIn('zero error precedes', text)
        self.assertIn('known Fourier', (ROOT/'work_orders/CURRENT.md').read_text())

    def test_readonly_pinned_workflow(self):
        text = (ROOT/'.github/workflows/verify.yml').read_text()
        self.assertIn('contents: read', text)
        self.assertNotIn('contents: write', text)
        self.assertIn('persist-credentials: false', text)
        self.assertIn('github.event.pull_request.head.sha', text)
        self.assertEqual(len(re.findall(r'uses: [^@\s]+@[0-9a-f]{40}', text)), 3)
        self.assertNotIn('git push', text)

    def test_python_syntax(self):
        for path in source_files():
            if path.suffix=='.py':
                ast.parse(path.read_text(), filename=str(path))

    def test_negative_integrity_controls(self):
        with self.assertRaises(ValueError): safe_path(ROOT, '../outside')
        with self.assertRaises(ValueError): safe_path(ROOT, '/tmp/outside')
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'sample';path.write_bytes(b'original')
            record={'sha256':hashlib.sha256(b'original').hexdigest(),'bytes':8}
            check_entry(path,record)
            path.write_bytes(b'modified')
            with self.assertRaises(AssertionError):check_entry(path,record)

if __name__=='__main__':unittest.main()
