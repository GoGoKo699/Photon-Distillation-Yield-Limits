#!/usr/bin/env python3
"""Update only active-document/infrastructure hashes, never scientific hashes."""
import argparse
import json
from integrity import ROOT, current_metadata, verify_active, verify_archive


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    verify_archive()
    verify_active()
    path = ROOT/'provenance/DOCUMENTS.json'
    data = current_metadata()
    if args.write:
        path.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n')
    elif not path.exists() or json.loads(path.read_text()) != data:
        raise SystemExit('Run with --write after reviewing permitted active edits.')
    print('Active metadata verified; protected import hashes untouched.')

if __name__ == '__main__':
    main()
