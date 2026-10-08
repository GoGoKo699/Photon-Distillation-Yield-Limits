# The result in context

Known Fourier protocols reduce the first-order distinguishability error by
$`1/N`$ with ideal success approaching $`1/4`$, at a photon cost approaching $`4N`$.
The central contribution is the matching all-network converse: every sequence
in the allowed fixed-output, passive, vacuum-extended class has limiting upper
success at most $`1/4`$ when its first-order error coefficient vanishes. Optimizing batch size as
well gives the sharp leading cost $`(4+o(1))R`$ for requested derivative-level
reduction $`R`$.

Known Fourier attainment, the necessary
thermal number marginal, and the exact four-photon optimum play distinct roles
alongside the central converse.

## Why the converse is needed

A balanced Fourier row alone does not control arbitrary competitors. Strongly
coupled inputs can produce a one-photon probability above one quarter. The proof
uses accepted error amplitudes, a grouped Gram norm, and a uniform product
estimate to control those inputs while allowing imbalance, arbitrary vacuum
enlargement, and larger batches with suboptimal but vanishing error coefficients.
The exact-coefficient theorem is a corollary of this stable form.

With $`c_N\to0`$, approaching the ceiling forces diffuse occupied-input couplings and total
occupied row norm approaching one. Known quantum-central-limit behavior then
gives the half-vacuum, quarter-single-photon, quarter-multiphoton marginal.
Assuming that marginal before excluding strongly coupled competitors would
omit the central optimization problem. The number law does not certify internal
purity: the detector selection rule is essential.

## How the results fit together

| Role | Result |
|---|---|
| Converse | Every allowed sequence with $`c\to0`$ has $`\limsup p_0\le1/4`$; optimizing batch size gives cost $`(4+o(1))R`$. |
| Attainment | Established Fourier-family protocols attain the leading cost. |
| Finite companion | Sharp success optima for two, three, and four photons at $`c=1/N`$; a monitored vacuum tap attains the four-photon value. |
| Necessary structure | Sequences with $`c_N\to0`$ and $`p_{0,N}\to1/4`$ have diffuse survivor couplings, a mean-one thermal number marginal, and asymptotically complete acceptance of the ideal one-survivor probability. |
| Selection control | Count-only acceptance has the same ideal yield as character selection but amplifies the leading error, as discussed in Saied et al., Appendix D. |
| Cost equality | Approaching cost $`4R`$ requires $`N/R\to1`$ and $`Nc\to1`$, together with asymptotically vanishing normalized mean-square deviation among the accepted input-origin amplitudes. |

## Relation to established results

The coefficient bound in Somhorst et al. (2601.05947v1) fixes the smallest
possible batch size for a requested first-order reduction. Fourier attainment
in Saied et al. (2404.14217v4) and Somhorst et al. (2404.14262v4) supplies an
achievable cost. The converse here bounds every allowed competitor's success,
which makes the leading factor of four an optimum over apparatus and batch size.

Hoch et al. (2509.02296v1) optimizes pairwise visibility with two active photons
and an untouched reference. Marshall (2203.15197v3) supplies small-batch
constructions. The [attribution map](../literature/ATTRIBUTION.md) compares the
objectives and credits these constructions, the coefficient optimum, and the
quantum-central-limit background. The comparison uses the versions and sections
recorded in [SOURCES.json](../literature/SOURCES.json).

## Physical meaning and evidence

The known Fourier scheme already pays the asymptotically minimum photon cost
among fixed, passive, vacuum-extended apparatuses with a predetermined survivor.
The result identifies both an unavoidable resource cost and the output structure
of protocols approaching it. The cost counts every input photon in repeated
attempts, including rejected batches, with the zero-error derivative taken
before increasing the requested reduction.

The [proof details](PROOF_DETAILS.md) establish the uniform converse; the
[optical construction](OPTICAL_CONSTRUCTION.md) gives attainment and the exact
finite certificates. The [physical interpretation](PHYSICAL_INTERPRETATION.md)
connects the coefficient to heralded internal quality and interference visibility.
[Verification](../VERIFICATION.md) reproduces the 21 scientific check groups
and records revision-specific report comparisons.
