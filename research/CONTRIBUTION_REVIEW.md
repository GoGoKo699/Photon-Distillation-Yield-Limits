# Contribution assessment

Known Fourier protocols reduce the first-order distinguishability error by
$1/N$ with ideal success approaching $1/4$, at a photon cost approaching $4N$.
The central contribution is the matching all-network converse: every sequence
in the allowed fixed-output, passive, vacuum-extended class has limiting upper
success at most $1/4$ when its first-order error coefficient vanishes. Optimizing batch size as
well gives the sharp leading cost $(4+o(1))R$ for requested derivative-level
reduction $R$.

This is a bounded resource theorem. Known Fourier attainment, the necessary
thermal number marginal, and the exact four-photon optimum play distinct roles
alongside the central converse.

## Why the converse is needed

A balanced Fourier row alone does not control arbitrary competitors. Strongly
coupled inputs can produce a one-photon probability above one quarter. The proof
uses accepted error amplitudes, a grouped Gram norm, and a uniform product
estimate to control those inputs while allowing imbalance, arbitrary vacuum
enlargement, and larger batches with suboptimal but vanishing error coefficients.
The exact-coefficient theorem is a corollary of this stable form.

Approaching the ceiling forces diffuse occupied-input couplings and total
occupied row norm approaching one. Known quantum-central-limit behavior then
gives the half-vacuum, quarter-single-photon, quarter-multiphoton marginal.
Assuming that marginal before excluding strongly coupled competitors would
omit the central optimization problem. The number law does not certify internal
purity: the detector selection rule is essential.

## Claim hierarchy

| Role | Content | Boundary |
|---|---|---|
| Central | Stable all-network $1/4$ success ceiling as $c\to0$; matching $(4+o(1))R$ input cost. | Each fixed network is expanded at $\epsilon=0$ before the sequence is taken. |
| Sharpness | Known Fourier-family protocols. | Not a new achieving architecture or a new quarter constant for that family. |
| Finite companion | All-network two-, three-, and four-photon optima at $c=1/N$; a monitored vacuum tap attains the four-photon value. | No full finite-$N\ge5$ classification. |
| Interpretation | Necessary diffuse-row structure; thermal number marginal for every near-ceiling sequence; asymptotically complete acceptance of ideal one-survivor probability. | A number law is not an internal-purity certificate. |
| Control | Count-only acceptance has the same ideal yield but fails to purify; the uniform-row coefficient tends to $1+s$. | This failure mechanism already appears in Saied Appendix D. |
| Cost equality | Approaching cost $4R$ requires $N/R\to1$ and $Nc\to1$, in addition to yield optimality. | Normalized mean-square amplitude erasure, not a unique complete interferometer. |

## Source attribution and reading boundaries

**Somhorst et al., [arXiv:2601.05947v1](https://arxiv.org/html/2601.05947v1).**
Section II distinguishes the error coefficient optimum from the then-open
success optimum. Appendix B's theorem is for an $N\times N$ passive matrix.
The amplitude identity here explicitly includes vacuum enlargement. The source's
experimental conclusions do not establish attainment of this first-order bound
by imperfect hardware.

**Saied et al., [arXiv:2404.14217v4](https://arxiv.org/pdf/2404.14217v4),
Phys. Rev. Applied 23, 034079 (2025).** Theorem III.5 assumes a uniformly coupled
first row and proves the attainable quarter limit. Theorem III.9 states the $4N$
cost for error sufficiently small relative to $N$. Appendix D obtains the
Haar-averaged one-photon probability approaching a quarter and explicitly warns
that accepting all one-survivor patterns amplifies error, reporting the same
behavior numerically for Fourier interference. Neither common number statistics
nor the need for pattern selection is a separate first-discovery claim here.
Those selected random-matrix calculations do not supply the uniform
arbitrary-network converse. The parsed theorem and appendix text were read;
PDF page rendering was unavailable, and no source figure data were extracted.

**Somhorst et al., [arXiv:2404.14262v4](https://arxiv.org/html/2404.14262v4).**
Sections II–III were read for the scalable Fourier construction,
zero-transmission character rule, internal-error distinctions, and finite-error
qualification. These are inherited; the source's finite-error performance is
not substituted for the derivative objective.

**Becker, Datta, Lami and Rouze, Communications in Mathematical Physics 383,
223–279 (2021), [DOI 10.1007/s00220-021-03988-1](https://doi.org/10.1007/s00220-021-03988-1).**
The publisher's full text, Introduction and characteristic-function discussion,
was read for the Cushen-Hudson optical central limit interpretation, passive
characteristic factorization, and trace-norm convergence. The arXiv PDF/HTML was
unavailable. The Fock-input weighted-row proof here supplies an exact
characteristic function and direct coefficient/tail estimate under the row
condition forced by the converse. It does not claim a new CLT or an optimal rate.

The earlier Hoch et al. comparison is preserved in the
[source review](../archive/research-handoff-2026-10-08/prior/REVIEW.md); the
nonlinear-sign-shift comparison is in the
[global proof](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md).
These are inherited readings, not fresh audits. The version checks recorded in
the [original assessment](../archive/research-handoff-2026-10-08/CLAIMS_AND_REVIEW.md)
returned v4 for 2404.14217 and v1 for 2601.05947. Its bounded search found no
directly covering stable all-row converse; this is not exhaustive priority clearance.
No unviewed image or plotted number supports the claims.

## Significance, scope, and audit status

The positive case is an unavoidable leading resource cost for a specified
physical operation: the known Fourier scheme already pays the asymptotically
minimum photon cost among the allowed static apparatuses. The main claim is the
converse, rather than a thermalization principle, known Fourier suppression,
or the small percentage gain in the four-photon example.

The skeptical case is the ideal first-order, predetermined-survivor scope.
Finite-error yield, loss tolerance, clock rate, encoded logical performance,
and adaptive-output optimization require different claims. The proof uses
elementary tools but needs uniform control across apparatuses; exactness,
proof length, and the thermal interpretation alone do not settle broad physical
significance. The analytical proof and its checks remain author-side evidence,
subject to independent scrutiny.

The recorded four suites passed all 21 groups (4+5+6+6), with canonical reports
reproduced byte-for-byte. [Verification](../VERIFICATION.md) gives the reproducible
procedure; the original [run record](../archive/research-handoff-2026-10-08/RUN_RECORD.json)
and [report comparisons](../archive/research-handoff-2026-10-08/evidence/report_comparisons.json)
preserve the audit evidence. The physical-mechanism checks use optical matrices
up to $6\times6$ and at most 252 occupation amplitudes; number-law calculations
through 128 inputs use scalar exact rational recursions. Earlier small-network
checks reach dimension 8. No large optical Fock-state simulation or experiment
underlies these results, and no scientific assertion or tolerance was changed to
obtain a pass.

The established contribution is retained at this scope. Finite error, photon
loss, adaptive survivor routing, correlated inputs, internal-mode manipulation,
extra nonvacuum ancillas, and every finite-batch optimum are separate questions.
A named proof objection, directly covering source, or explicitly selected new
claim can reopen the research.
