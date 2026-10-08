# Verification

## Full check

Use Python 3.13.5 and the versions pinned in [requirements.txt](requirements.txt).
The original environment is preserved in
[the research archive](archive/research-handoff-2026-10-08/environment.json).

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output-dir build/verification
```

Choose a new output directory for every run. The repository wrapper verifies all
89 archived files, four nested manifests, the owner's original license, declared
active-copy changes, document hashes, and local links. It then runs the infrastructure
tests and delegates to the original, unchanged verification wrapper for all four
scientific suites:

| Suite | Groups | Canonical report within the archive |
|---|---:|---|
| Consolidation and physical interpretation | 4 | `evidence/first.json` |
| Stability and independent certificate | 5 | `prior/evidence/final.json` |
| Global converse and four-photon optimum | 6 | `prior/prior/evidence/enriched.json` |
| Initial pilot | 6 | `prior/prior/prior/evidence/final.json` |

The wrapper records source hashes and verifies they are unchanged after execution.
It also records the exact commit/tree, environment, logs, complete JSON report
differences, and byte equality. It never updates original reports or modifies
scientific assertions or tolerances.

## Exit codes and evidence

`0` means all checks and exact canonical report comparisons pass. `1` indicates a
failure. `2` means the original mathematical suites passed but at least one generated
report differs from its canonical bytes; those differences require explicit review.
Do not treat status 2 as a verified pass or refresh the original reference to hide it.
No separate numerical tolerance is used to silently accept a mismatch.

Floating-point report bytes can depend on the numerical runtime even with pinned
Python and package versions. The [hosted report review](provenance/HOSTED_REPORT_REVIEW.json)
records the initial PR and merged-main evidence: all 21 scientific groups passed,
while 60 floating-point leaves differed by at most $`6.11\times10^{-16}`$.
A local BLAS-dispatch experiment reproduced 58 of those differences exactly;
the remaining two were quadrature values satisfying the unchanged bound checks.
The original reports, assertions, and tolerances remain unchanged. These runs
retain status 2 and a failed hosted workflow result; the explicit review records
why those exact revisions were accepted. A new mismatch must be reviewed again.

The artifact contains `source-manifest.json`, `repository-receipt.json`,
`report-comparisons.json`, infrastructure logs, and the original wrapper's reports
and receipt. Scientific check success is evidence for reproducibility, not a substitute
for the analytical uniform proof or an independent novelty assessment.

## Hosted checks

The [workflow](.github/workflows/verify.yml) checks out the actual PR head, not only
a synthetic merge revision, and separately runs on merged main. It uses pinned
actions, read-only contents permission, and does not retain checkout credentials.
Inspect the artifact and compare every source hash with the reviewed tree before
merging the expected head. Verify main independently after the merge.

Use the live workflow result and its artifact for revision-specific status.
The historical report review does not establish the status of a later revision.

## Permitted document regeneration

Review explicit presentation changes in `provenance/ACTIVE_EDITS.json`, then run:

```bash
python tools/sync_active.py --write
python tools/sync_metadata.py --write
python -m unittest discover -s tests -v
```

Both commands first verify protected sources. Only active destination hashes and
active-document/infrastructure metadata may be regenerated. The import manifest,
archived scientific sources, canonical reports, and license remain protected.
Active-copy destinations must be distinct Markdown files under `research/`; all
destinations and replacement specifications are checked before any file is written.
