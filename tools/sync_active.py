#!/usr/bin/env python3
"""Regenerate active copies from explicit presentation-only edit specifications."""
import argparse
import hashlib
import json
from integrity import ROOT, reproduce_active, safe_path, verify_archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    verify_archive()
    specification = ROOT/'provenance/ACTIVE_EDITS.json'
    data = json.loads(specification.read_text())
    for row in data['copies']:
        text = reproduce_active(row)
        path = safe_path(ROOT, row['destination'])
        digest = hashlib.sha256(text.encode('utf-8')).hexdigest()
        if args.write:
            path.write_text(text)
            row['destination_sha256'] = digest
        elif path.read_text() != text or row['destination_sha256'] != digest:
            raise SystemExit(f'Active copy needs regeneration: {path}')
    if args.write:
        specification.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    print('Active presentation copies verified; protected sources unchanged.')

if __name__ == '__main__':
    main()
