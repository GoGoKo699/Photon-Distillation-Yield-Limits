# Photon-distillation yield pilot

Read `PILOT.md` for the physical task, exact three-photon success bound,
four-photon monitored-vacuum construction, attribution, and unresolved general optimum.

This is an independent research record, not a manuscript or an initialized repository.
The first-order 1/N error limit and the Fourier protocols are inherited. The candidate
result is their success-optimality constraint, including vacuum modes.

## Reproduce

Dependencies: NumPy, SciPy, SymPy. Versions from the completed runs are recorded in
`environment.json`. No network access or old project files are needed.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python check_pilot.py --output new_report.json
```

The output path must not already exist. Six unittest groups execute. Numerical
tolerances remain in the source; symbolic/rational certificates do not use them.
`evidence/final.json` and `evidence/repeat.json` are byte-identical.
The first passing five-group source and report are preserved; the enrichment is
not called a repair of a failed scientific test.

No large Hilbert-space simulation or optical experiment was performed. Ideal
success and first-order suppression do not establish a finite-error, loss-tolerant
hardware benefit.

## Record

- `SOURCES.json`: primary sources and precise reading boundaries.
- `evidence/`: unmodified logs and reports from actual runs.
- `development/`: first passing checker and explicit enrichment diff.
- `RUN_RECORD.json`: checks, scope, and operational issue.
- `MANIFEST.json`: SHA-256 hashes and byte sizes of all package files except itself.

The next question is the global yield bound for N>=4, not another noise model.
Protected repositories and earlier pilot evidence were neither imported nor modified.
