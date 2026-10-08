# Photon Distillation Yield Limits

**Success and photon-cost limits for passive purification of photon indistinguishability.**

How many imperfect photons must a passive optical network consume to herald one
photon with a much smaller first-order distinguishability error? This repository
records a converse showing that the leading photon cost of established Fourier
distillation is unavoidable within the stated resource class.

## Central result

For each fixed apparatus, let $p_0$ be its ideal-input heralding probability and
$c$ its first-order output-error coefficient:

$$
p_{\mathrm{herald}}(\epsilon)=p_0+O(\epsilon),\qquad
\epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2).
$$

Then every allowed sequence satisfies

$$
c_N\longrightarrow0\quad\Longrightarrow\quad
\limsup_{N\to\infty}p_{0,N}\le\frac14.
$$

Optimizing both the batch size and the network for a requested first-order
reduction factor $R$ gives the sharp leading ideal photon cost

$$
\mathcal C(R):=\inf_{c\le1/R}\frac{N}{p_0}=(4+o(1))R.
$$

Known Fourier protocols attain the limit. The contribution is the uniform
converse over unequal survivor couplings and arbitrary additional vacuum ports,
not a new Fourier mechanism or a new attainable quarter constant.

## Reading path

| Read | Purpose |
|---|---|
| [Model and claims](research/MODEL_AND_CLAIMS.md) | Resources, objectives, and order of limits. |
| [Theorem](research/THEOREM.md) | Stable yield bound and matching photon-cost law. |
| [Physical mechanism](research/PHYSICAL_MECHANISM.md) | Necessary output statistics and why counting a survivor is not purification. |
| [Proof map](research/PROOF_MAP.md) | Detailed derivations, counterexamples, and the exact four-photon certificate. |
| [Contribution review](research/CONTRIBUTION_REVIEW.md) | Positive and skeptical cases, without inflating inherited ingredients. |
| [Attribution](literature/ATTRIBUTION.md) | Version-pinned source roles and recorded reading boundaries. |
| [Verification](VERIFICATION.md) | Reproduce all 21 scientific check groups without changing evidence. |

## Scope

Each attempt uses independent imperfect single photons, a fixed passive
internal-mode-blind interferometer, arbitrary vacuum inputs, ideal number-resolving
detectors, and one survivor output chosen before the attempt. Rejected batches
count in the photon cost. The error derivative is taken at fixed apparatus before
the large-batch or large-reduction limit. This is not a fixed-nonzero-error,
loss-tolerant, or adaptive-output theorem.

Exact two-, three-, and four-photon optima at the best coefficient $c=1/N$
provide finite-resource companions. The four-photon optimum is attained with a
monitored vacuum tap. The complete finite-batch optimum for all $N\ge5$ is not
required by the central asymptotic theorem.

## Reproducibility and research record

The complete original research package is preserved in
[the dated archive](archive/README.md), including proofs, unchanged checkers,
canonical reports, and failed attempts. Active documents use the declared, reviewed
navigation and presentation changes recorded in
[ACTIVE_EDITS.json](provenance/ACTIVE_EDITS.json), preserving the scientific claims,
proofs, scope, attribution, and audit status. The proofs remain author-side;
passing checks establish neither independent proof review nor exhaustive priority.

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output-dir build/verification
```

The output directory must be new. [Verification](VERIFICATION.md) explains the
evidence and strict report comparison, including numerical-runtime differences.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

[MIT License](LICENSE), copyright 2026 Ruge Lin. The owner's original license
is preserved byte-for-byte. Referenced third-party publications are cited,
not redistributed.
