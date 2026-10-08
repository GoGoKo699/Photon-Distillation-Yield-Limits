#!/usr/bin/env python3
"""Regenerate active copies from explicit presentation-only edit specifications."""
import argparse
import hashlib
import json
from integrity import ROOT, reproduce_active, safe_path, verify_archive


def active_destinations(rows):
    """Validate every target before generation can write any file."""
    destinations = []
    seen = set()
    for row in rows:
        path = safe_path(ROOT, row['destination'])
        resolved = path.resolve()
        if path.suffix != '.md' or not resolved.is_relative_to(ROOT/'research'):
            raise ValueError(f'Active destination must be a research Markdown document: {path}')
        if resolved in seen:
            raise ValueError(f'Duplicate active destination: {path}')
        seen.add(resolved)
        destinations.append(path)
    return destinations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    verify_archive()
    specification = ROOT/'provenance/ACTIVE_EDITS.json'
    data = json.loads(specification.read_text())
    destinations = active_destinations(data['copies'])
    prepared = [(row, path, reproduce_active(row))
                for row, path in zip(data['copies'], destinations)]
    for row, path, text in prepared:
        digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
        if args.write:
            path.write_text(text)
            row['destination_sha256'] = digest
        elif path.read_text() != text or row['destination_sha256'] != digest:
            raise SystemExit(f'Active copy needs regeneration: {path}')
    if args.write:
        specification.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    verify_archive()
    print('Active presentation copies verified; protected sources unchanged.')

if __name__ == '__main__':
    main()
