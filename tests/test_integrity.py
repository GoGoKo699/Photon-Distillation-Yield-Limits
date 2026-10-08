"""Infrastructure tests, kept separate from the preserved scientific suites."""
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from integrity import (ROOT, check_entry, current_metadata, reproduce_active, safe_path,
                       source_files, verify_active, verify_archive, verify_links, verify_metadata)
import sync_active


def display_equations(text):
    """Read both supported display delimiters in document order."""
    matches = re.finditer(r'\$\$(.*?)\$\$|^```math[^\S\n]*\n(.*?)^```[^\S\n]*$',
                          text, re.S | re.M)
    return [m.group(1) if m.group(1) is not None else m.group(2) for m in matches]


def mathematical_content(tex):
    """Ignore layout and named-function typography, retaining structure and tokens."""
    tex = re.sub(r'\\tag\{[^{}]*\}', '', tex)
    tex = re.sub(r'\\operatorname\{(Tr|per|supp|Var)\}', r'\\mathrm{\1}', tex)
    parts = re.split(r'(\\(?:begin|end)\{[^{}]+\}|\\\\|(?<!\\)&)', tex)
    stack, kept = [], []
    layout = {'aligned', 'gathered', 'split'}
    for part in parts:
        environment = re.fullmatch(r'\\(begin|end)\{([^{}]+)\}', part)
        if environment:
            kind, name = environment.groups()
            if kind == 'begin':
                stack.append(name)
            else:
                assert stack and stack.pop() == name, 'Unbalanced TeX environment'
            if name not in layout:
                kept.append(part)
        elif part in ('&', '\\\\') and stack and all(name in layout for name in stack):
            continue
        else:
            kept.append(part)
    assert not stack, 'Unclosed TeX environment'
    result = re.sub(r'\\(?:qquad\b|quad\b|[,;!: ])', '', ''.join(kept))
    return re.sub(r'\s+', '', result)


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
            self.assertEqual([mathematical_content(eq) for eq in display_equations(source)],
                             [mathematical_content(eq) for eq in display_equations(active)])
            for tag in re.findall(r'\\tag\{([^{}]+)\}', source):
                self.assertIn(f'**({tag})**', active)
        # Matrix row/column structure and mathematical relations stay significant.
        matrix = r'\begin{pmatrix}a&b\\c&d\end{pmatrix}'
        self.assertNotEqual(mathematical_content(matrix),
                            mathematical_content(r'\begin{pmatrix}a&b&c&d\end{pmatrix}'))
        self.assertNotEqual(mathematical_content('a=b'), mathematical_content('a<b'))
        self.assertEqual(mathematical_content(r'\operatorname{Tr}(\rho)'),
                         mathematical_content(r'\mathrm{Tr}(\rho)'))
        self.assertNotEqual(mathematical_content(r'\operatorname{Tr}(A)'),
                            mathematical_content(r'\operatorname{Tr}(B)'))
        self.assertNotEqual(mathematical_content(r'\operatorname{per}(A)'),
                            mathematical_content(r'\operatorname{Tr}(A)'))

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
        self.assertIn('One output is retained in advance', text)
        self.assertIn('zero error precedes', text)
        self.assertIn('known Fourier', (ROOT/'maintenance/CURRENT.md').read_text())

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

    def assert_active_write_rejected(self, second_destination):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            protected = ['LICENSE', 'archive/research-handoff-2026-10-08/THEOREM.md',
                         'provenance/IMPORT.json', 'tools/verify.py']
            for name in ['research/active.md', *protected]:
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('original\n')
            source = 'archive/research-handoff-2026-10-08/THEOREM.md'
            copies = [{'destination': name, 'source': source,
                       'source_sha256': hashlib.sha256(b'original\n').hexdigest(),
                       'destination_sha256': '',
                       'replacements': [{'old': 'original', 'new': 'changed', 'count': 1}]}
                      for name in ['research/active.md', second_destination]]
            (root/'provenance/ACTIVE_EDITS.json').write_text(json.dumps({'copies': copies}))
            before = {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            with patch.object(sync_active, 'ROOT', root), patch('integrity.ROOT', root), \
                    patch.object(sync_active, 'verify_archive'), \
                    patch.object(sys, 'argv', ['sync_active.py', '--write']):
                with self.assertRaises(ValueError):
                    sync_active.main()
            after = {p.relative_to(root): p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(before, after, 'Rejected specifications must not partially write files')

    def test_active_sync_rejects_protected_destinations_before_writing(self):
        for destination in ['LICENSE', 'archive/research-handoff-2026-10-08/THEOREM.md',
                            'provenance/IMPORT.json', 'provenance/ACTIVE_EDITS.json',
                            'tools/verify.py']:
            with self.subTest(destination=destination):
                self.assert_active_write_rejected(destination)

    def test_active_sync_rejects_duplicate_destinations_before_writing(self):
        self.assert_active_write_rejected('research/active.md')

if __name__=='__main__':unittest.main()
