"""Repository integrity checks; never regenerate scientific reference material."""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', 'build', '__pycache__', '.venv'}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_files(root: Path = ROOT) -> list[Path]:
    return sorted(p for p in root.rglob('*') if p.is_file()
                  and not any(part in EXCLUDED for part in p.relative_to(root).parts))


def safe_path(root: Path, name: str) -> Path:
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError(f'Unsafe recorded path: {name}')
    result = root / relative
    if not result.resolve().is_relative_to(root.resolve()) or result.is_symlink():
        raise ValueError(f'Path escaped root: {name}')
    return result


def check_entry(path: Path, record: dict) -> None:
    if not path.is_file() or path.is_symlink():
        raise AssertionError(f'Missing/nonregular protected file: {path}')
    if sha256(path) != record['sha256']:
        raise AssertionError(f'Hash mismatch: {path}')
    if 'bytes' in record and path.stat().st_size != record['bytes']:
        raise AssertionError(f'Size mismatch: {path}')


def verify_archive() -> dict:
    info = json.loads((ROOT/'provenance/IMPORT.json').read_text())
    if info['repository'] != 'GoGoKo699/Photon-Distillation-Yield-Limits':
        raise AssertionError('Wrong repository')
    archive = safe_path(ROOT, info['archive_root'])
    actual = {str(p.relative_to(archive)) for p in archive.rglob('*') if p.is_file()}
    if actual != set(info['files']):
        raise AssertionError('Archive inventory mismatch')
    for name, rec in info['files'].items():
        check_entry(safe_path(archive, name), rec)
    check_entry(ROOT/'LICENSE', {'sha256': info['license_sha256']})
    manifests = {}
    for manifest in sorted(archive.rglob('MANIFEST.json')):
        data = json.loads(manifest.read_text())
        for name, rec in data.items():
            check_entry(safe_path(manifest.parent, name), rec)
        manifests[str(manifest.relative_to(archive))] = len(data)
    return {'archive_files': len(actual), 'manifests': manifests,
            'license_sha256': info['license_sha256']}


def reproduce_active(row: dict) -> str:
    source = safe_path(ROOT, row['source'])
    check_entry(source, {'sha256': row['source_sha256']})
    text = source.read_text()
    for replacement in row['replacements']:
        old, new = replacement['old'], replacement['new']
        if text.count(old) != replacement['count']:
            raise AssertionError(f'Active replacement count mismatch: {row["destination"]}')
        text = text.replace(old, new)
    return text


def verify_active() -> int:
    rows = json.loads((ROOT/'provenance/ACTIVE_EDITS.json').read_text())['copies']
    for row in rows:
        destination = safe_path(ROOT, row['destination'])
        expected = reproduce_active(row).encode('utf-8')
        if destination.read_bytes() != expected:
            raise AssertionError(f'Undeclared active edit: {destination}')
        check_entry(destination, {'sha256': row['destination_sha256']})
    return len(rows)


def metadata_paths() -> list[Path]:
    return [p for p in source_files() if not p.relative_to(ROOT).as_posix().startswith('archive/research-handoff-2026-10-08/')
            and p.relative_to(ROOT).as_posix() not in
            {'LICENSE', 'provenance/IMPORT.json', 'provenance/DOCUMENTS.json'}]


def current_metadata() -> dict:
    return {str(p.relative_to(ROOT)): {'sha256': sha256(p), 'bytes': p.stat().st_size}
            for p in metadata_paths()}


def verify_metadata() -> int:
    expected = json.loads((ROOT/'provenance/DOCUMENTS.json').read_text())
    if expected != current_metadata():
        raise AssertionError('Active-document/infrastructure integrity metadata mismatch')
    return len(expected)


def verify_links() -> int:
    count = 0
    for document in source_files():
        if document.suffix != '.md' or document.relative_to(ROOT).as_posix().startswith('archive/research-handoff-2026-10-08/'):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', document.read_text()):
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            path = unquote(target.split('#', 1)[0])
            resolved = (document.parent / path).resolve()
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                raise AssertionError(f'Broken local link: {document}: {target}')
            count += 1
    return count


def snapshot() -> dict:
    return {str(p.relative_to(ROOT)): {'sha256': sha256(p), 'bytes': p.stat().st_size}
            for p in source_files()}


def verify_all() -> dict:
    return {**verify_archive(), 'active_copies': verify_active(),
            'metadata_files': verify_metadata(), 'local_links': verify_links()}
