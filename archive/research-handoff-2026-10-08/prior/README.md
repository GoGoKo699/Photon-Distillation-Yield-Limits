# Photon-distillation yield: proof review and stable ceiling

Read [THEOREM.md](THEOREM.md) for the model, stability theorem, sharp asymptotic
photon cost, necessary optimal-row properties, and four-photon certificate.
[REVIEW.md](REVIEW.md) separates the scientific claims, predecessors, internal
checks and unresolved contribution assessment.

The preceding checkpoint is preserved byte-for-byte in `prior/`.
Nothing here edits a research repository or starts a different optical model.

Run with the existing dependencies (`numpy`, `scipy`, `sympy`):

```bash
python check_review.py --output evidence/a_new_report.json
python prior/check_followup.py --output evidence/a_new_global_report.json
python prior/prior/check_pilot.py --output evidence/a_new_pilot_report.json
```

Report paths must not exist. The new checker includes five diagnostic groups.
The two preserved checkers each contain six groups. Finite checks are not a
substitute for the analytical uniform bound or independent review.

The quarter limit concerns ideal herald probability and first-order input
error suppression. It is not a universal finite-batch bound or a fixed-error,
lossy-device guarantee.
