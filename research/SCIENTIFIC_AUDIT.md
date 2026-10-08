# Scientific audit of the yield and cost theorem

The 8 October 2026 audit re-examined the mathematical and physical obligations
needed for the contribution in [THEOREM.md](THEOREM.md). The stable converse and
its optimized photon-cost consequence survive this audit. No blocking defect was
found within the [declared model](MODEL_AND_CLAIMS.md).

This was an author-side audit with separate agent-assisted rederivations. It is
not external independent review. The new notes are research derivations and
source comparisons; they do not replace the immutable original record.

## Questions resolved

| Obligation | Result and evidence |
|---|---|
| Independent, mixed, nonidentical internal errors | The first-order bad-survivor numerator is the sum of the accepted input-origin norms. No overlaps between different bad states enter. [Proof details, Section 1](PROOF_DETAILS.md). |
| Arbitrary vacuum enlargement and singular rows | The Gram reduction uses minors of the occupied-column Gram matrix and contains no inverse or division by a coupling. Zero couplings and singular matrices remain covered. [Proof details](PROOF_DETAILS.md). |
| Uniformity over all rows and sizes | Product and derivative estimates hold over the entire integration domain, including sign changes. The integrated remainder is bounded by the unchanged constant 96. [Proof details](PROOF_DETAILS.md). |
| Positivity in the grouped estimate | Integration-by-parts boundary constants cancel. Positivity comes from a genuine auxiliary vacuum probability, not from the signed polynomial integrand. [Proof details](PROOF_DETAILS.md). |
| Optimizing batch size without an attained minimum | A single bound applies to every competitor at a requested reduction, before taking the infimum. No error/size limits are interchanged. [Proof details](PROOF_DETAILS.md). |
| Physically specified attaining family | The Fourier tap is measured, its photons count toward the herald, and the character rule makes every accepted input-origin amplitude equal. An explicit event proves positive success for every size at least three and positive transmissivity. [Optical construction](OPTICAL_CONSTRUCTION.md). |
| Exact finite optima and boundaries | The two- and three-input Gram bounds and the four-input polynomial bound were reconstructed. All 613 positive degree-ten certificate coefficients agree exactly with the saved certificate. Zero-coupling boundaries and the restricted equality conclusion are explicit. [Optical construction](OPTICAL_CONSTRUCTION.md). |
| Meaning of output quality | The conditional good-mode infidelity is defined explicitly and determines the leading visibility deficit for two independent output photons. [Physical interpretation](PHYSICAL_INTERPRETATION.md). |
| Thermal interpretation and controls | The coefficient/tail estimate gives trace-norm convergence only after diffuseness is proved. Count-only acceptance and the strongly coupled row retain their different error/yield behavior. [Physical mechanism](PHYSICAL_MECHANISM.md) and [interpretation](PHYSICAL_INTERPRETATION.md). |
| Closest existing optimality results | The updated comparison distinguishes coefficient, success, scaling, pairwise-visibility, and finite-error objectives. The inspected sources do not supply the stable arbitrary-row success converse. [Attribution](../literature/ATTRIBUTION.md) and [reading record](../literature/SOURCES.json). |

## Precision changes to active claims

The active fixed-coupling sentence previously wrote the constraint as
$\sum_i p_i\le s\le1$ while also calling the ceiling attained. Its intended
attainment domain is **fixed $0<s\le1$**, as already specified in the archived
stable derivation. At $s=0$, the retained output receives no occupied-input
amplitude: $p_0=0$, so the conditional coefficient is undefined. Zero is only the
limiting ceiling as positive $s$ tends to zero. This endpoint precision does not
alter the stable quarter theorem or the optimized cost law.

Similarly, the Fourier coefficient and count-only ratio are asserted only for
positive ideal success. The untapped two-input Fourier circuit has zero success;
its tapped circuit at $s=1/2$ is the stated finite optimum. For every $N\ge3$ and
$0<s\le1$, the positive-success witness closes this issue.

The monitored tap may detect photons. Restricting it to zero counts would define
a different acceptance rule and lose the stated two- and four-input attainment.
The archived construction already allowed nonzero tap counts; the active account
now states the rule explicitly. The output-error definition and corresponding
conditional density operator make explicit the quantity already used by the
accepted-amplitude proof.

These changes are declared in
[ACTIVE_EDITS.json](../provenance/ACTIVE_EDITS.json). Original equation blocks,
archived assertions, reports, tolerances, and certificate bytes are unchanged.

## Evidence and remaining boundaries

The analytical checks address universal statements; finite calculations are
cross-checks. The [verification procedure](../VERIFICATION.md) reproduces all 21
original scientific groups and checks preservation separately from the proofs.
Revision-specific local and hosted receipts belong to the reviewed pull request.
A hosted report mismatch remains a visible review condition; it is not converted
into success by modifying tolerances or canonical results.

The targeted source audit includes explicit optimality language in the closest
papers, not just their construction formulas. It found no directly covering
converse in the inspected material. An abstract-only recent screen with
unavailable full text is recorded as such. This is a bounded literature finding,
not proof of exhaustive priority.

No unresolved internal proof obligation was identified for the stated theorem.
External specialist scrutiny remains distinct from this author-side work.
Finite nonzero error, loss, correlated inputs, adaptive survivors, additional
nonvacuum resources, and exact optima at every larger finite size are separate
research problems. None is needed to establish the present first-order result.
