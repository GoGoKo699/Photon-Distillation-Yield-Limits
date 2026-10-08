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

The [updated attribution map](../literature/ATTRIBUTION.md) and
[version-pinned reading record](../literature/SOURCES.json) record the targeted
primary-source audit of 8 October 2026. It inspected the coefficient optimum in
Somhorst et al. (2601.05947v1), Fourier attainment and its cost in Saied et al.
(2404.14217v4), and the resource-scaling and multiphoton-slope optimality arguments
in Somhorst et al. (2404.14262v4). None of those inspected arguments supplies the
stable arbitrary-row success converse. The inference is bounded by those sources
and the documented search, not an exhaustive priority claim.

Hoch et al. (2509.02296v1) optimizes pairwise visibility using two active photons
and an untouched reference, followed by success optimization at the best
visibility. Its three-photon experiment is not the same three-input common-target
problem. Marshall's small-batch constructions, the established quantum central
limit background, and Saied's count-only failure mechanism retain their attribution.

The fresh core readings used primary HTML text; Marshall was read as parsed PDF
text. Earlier source-access limitations remain in the immutable archive and are
not retroactively changed. The new record distinguishes fresh full-text readings,
inherited comparisons, and an abstract-only screen whose full text was unavailable.
No unviewed figure or extracted plot value supports the result.

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
