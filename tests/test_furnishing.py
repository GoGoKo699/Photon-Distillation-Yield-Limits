"""Reading-route checks; the original scientific suites remain unchanged."""
import hashlib
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def math_payload(text):
    return [m.group(0) for m in re.finditer(
        r'^```math[^\S\n]*\n.*?^```[^\S\n]*$|\$`.*?`\$', text, re.M | re.S)]


def reading_pages():
    return [ROOT/'README.md', *(p for folder in ('science', 'learning', 'references')
                               for p in (ROOT/folder).glob('*.md'))]


def heading_ids(text):
    """GitHub-style slugs for the plain-text headings used in these pages."""
    text = re.sub(r'^```.*?^```[^\S\n]*$', '', text, flags=re.S | re.M)
    counts, identifiers = {}, set()
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        count = counts.get(slug, 0)
        identifiers.add(slug if count == 0 else f'{slug}-{count}')
        counts[slug] = count + 1
    identifiers.update(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    return identifiers


class FurnishingTests(unittest.TestCase):
    def test_topic_layout_and_entrypoints(self):
        for directory in ('science', 'learning', 'references', 'verification'):
            self.assertTrue((ROOT/directory/'README.md').is_file())
        self.assertFalse((ROOT/'research').exists() and any((ROOT/'research').iterdir()))
        self.assertFalse((ROOT/'literature').exists() and any((ROOT/'literature').iterdir()))
        self.assertFalse((ROOT/'VERIFICATION.md').exists())
        for name in ('README.md', 'llms.txt'):
            text = (ROOT/name).read_text()
            self.assertIn('learning/MILESTONES.md', text)
            self.assertIn('learning/TICHY_BRIDGE.md', text)
            self.assertIn('science/THEOREM.md', text)
            self.assertIn('verification/README.md', text)

    def test_thirty_project_milestones_and_dependencies(self):
        text = (ROOT/'learning/MILESTONES.md').read_text()
        records = re.findall(r'^### M(\d{2}) — (.*?)(?=^### M\d{2} —|\Z)', text, re.M | re.S)
        self.assertEqual([int(i) for i, _ in records], list(range(1, 31)))
        for i, body in records:
            for field in ('Phase', 'Central question', 'Understanding target', 'Dependencies',
                          'Story role', 'Conceptual connection', 'Sources'):
                self.assertRegex(body, rf'\*\*{field}:\*\*\s+\S')
            phase = 'Background/preliminaries' if int(i) <= 10 else 'Narrative/innovation'
            self.assertIn(f'**Phase:** {phase}.', body)
            deps = re.search(r'\*\*Dependencies:\*\* (.*?)\n', body).group(1)
            for earlier in re.findall(r'M(\d{2})', deps):
                self.assertLess(int(earlier), int(i))
                self.assertGreaterEqual(int(earlier), 1)
            sources = body.split('**Sources:**', 1)[1]
            self.assertRegex(sources, r'\]\((?:\.\./science/|TICHY_BRIDGE\.md|\.\./references/)')
        self.assertIn('Synthesize the background', records[9][1])
        self.assertIn('Synthesize the narrative', records[29][1])

    def test_selected_anchor_and_public_learning_boundary(self):
        for name in ('learning/README.md', 'learning/TICHY_BRIDGE.md', 'learning/MILESTONES.md'):
            text = (ROOT/name).read_text()
            self.assertIn('Tichy', text)
            self.assertIn('1312.4266v2', text)
        sources = json.loads((ROOT/'references/SOURCES.json').read_text())['sources']
        anchor = [row for row in sources if row['id'] == 'T14']
        self.assertEqual(len(anchor), 1)
        self.assertEqual(anchor[0]['version'], 'arXiv:1312.4266v2')
        for page in reading_pages():
            text = page.read_text()
            for forbidden in ('COACHING.md', 'Revise → Learn → Test', 'challenge failed',
                              'learner score', 'Gwen', 'Guinevere'):
                self.assertNotIn(forbidden, text)

    def test_preserved_migrated_math_and_source_identity(self):
        record = json.loads((ROOT/'provenance/REFURNISH.json').read_text())
        self.assertEqual(record['baseline_commit'], '99074550e4955891cae2c2630c2da7570ec34269')
        self.assertEqual(record['preservation']['archive_files'], 89)
        self.assertEqual(record['preservation']['scientific_groups'], 21)
        self.assertEqual(len(record['moved_documents']), 11)
        for row in record['moved_documents']:
            raw = (ROOT/row['new_path']).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row['new_sha256'])
            payload = json.dumps(math_payload(raw.decode()), ensure_ascii=False).encode()
            self.assertEqual(hashlib.sha256(payload).hexdigest(), row['math_sha256'])
        raw = (ROOT/'references/SOURCES.json').read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        self.assertEqual(blob, record['unchanged_move']['blob_sha'])

    def test_local_reading_links_and_fragments(self):
        for page in reading_pages():
            for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
                if urlsplit(target).scheme:
                    continue
                name, _, fragment = target.partition('#')
                dest = (page.parent/unquote(name)).resolve() if name else page
                self.assertTrue(dest.is_relative_to(ROOT), (page, target))
                self.assertTrue(dest.exists(), (page, target))
                if fragment:
                    self.assertIn(unquote(fragment), heading_ids(dest.read_text()), (page, target))

    def test_math_delimiters_in_reading_pages(self):
        for page in reading_pages():
            text = page.read_text()
            self.assertEqual(len(re.findall(r'^```', text, re.M)) % 2, 0, page)
            self.assertNotIn('$$', text)
            self.assertNotIn(r'\tag{', text)
            without_fences = re.sub(r'^```.*?^```[^\S\n]*$', '', text, flags=re.S | re.M)
            without_inline = re.sub(r'\$`.*?`\$', '', without_fences)
            self.assertNotIn('$', without_inline, page)


if __name__ == '__main__':
    unittest.main()
