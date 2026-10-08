# Photon-distillation yield: consolidated research package

One central result: passive, fixed-output distillation whose first-order
indistinguishability coefficient tends to zero has ideal success at most one
quarter asymptotically. Fourier protocols attain the bound, yielding a matching
minimum photon cost after optimizing both batch size and network. A sharp
four-photon optimum is a finite-resource companion.

Start with [THEOREM](THEOREM.md), then [the physical mechanism](PHYSICAL_MECHANISM.md)
and [the contribution review](CLAIMS_AND_REVIEW.md). The [proposed handoff](PROJECT_HANDOFF.md)
contains the scope and preservation rules. This is not a created repository,
submitted manuscript, independent review, or experimental implementation.

Run all current and prior checks without overwriting evidence:

```bash
python run_verification.py --output-dir /tmp/photon-yield-check-UNIQUE
```

The package keeps the complete 62-file incoming checkpoint unchanged under
`prior/`; it includes no unrelated project code or third-party source PDFs.
`MANIFEST.json` lists every packaged file except itself. `SOURCES.json` records
primary-source reading boundaries. The central-limit argument is standard
machinery; the resource converse, not thermalization alone, is the contribution
under assessment.
