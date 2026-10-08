# Focused proof and contribution review

**8 October 2026. No repository has been accessed or modified.**

## Decision

Retain and consolidate one theoretical contribution. The resource law is now
stable against a natural objection: demanding the exactly optimal coefficient
$c=1/N$ is not what causes the asymptotic success penalty. Any vanishing
first-order coefficient has the same quarter-yield ceiling, and optimizing both
batch size and network for an improvement factor $R$ costs $(4+o(1))R$ input
photons in the declared ideal/first-order limit.

This does not establish finite-error hardware performance. Strong confidence
about journal significance or priority is not supplied by the proof audit.
The useful next transition is to a compact theorem/claim record, not a requirement
to solve all larger finite batches, loss, or adaptive architectures.

## Audit of the existing theorem

1. **Operation and denominator.** The bad-survivor first-order numerator is
   $\sum_i\|Pv_i\|^2$; the denominator is $p_0+O(\epsilon)$, so its first-order
   derivative uses $p_0$. The success class retains exactly one photon without
   resolving its internal mode. No origin label is secretly available.

2. **Equality and nonoptimal inputs.** The accepted vectors, not only their
   probabilities, must agree at $c=1/N$. The Cauchy residual is exact. Retaining
   that residual or simply bounding the total accepted heavy-input amplitude
   proves the new stability result. This is a new derivation relative to the
   preceding checkpoint, not a statement silently inserted into the old proof.

3. **Gram reduction.** Repeated-row permanents in normalized Fock bases agree
   with independently expanded creation-operator amplitudes. The Gram entries
   use only the occupied part of the selected unitary row and keep all vacuum
   extensions. Singular cases in the older exact-coefficient proof remain
   separately defined.

4. **Grouped integral.** The first- and second-derivative terms agree with the
   direct quadratic norm. Integration by parts retains its boundary terms.
   Products may be signed; the limiting integral is bounded using an actual
   auxiliary no-photon probability, not a false positivity assumption.

5. **Uniformity.** The telescoping estimates hold on the entire integration
   range, including zeros and sign changes of individual factors. The constant
   96 is size independent. Finite sampled values support, but do not prove,
   this analytical uniformity.

6. **Four-photon certificate.** A separate integer coefficient convolution
   regenerates every one of the 613 positive monomials. Selected strict-positive
   terms also fix the equality case for the survivor intensities. The global
   value and the failure of the old Schur-concavity route are unchanged.

No blocking mathematical issue was found in these reviewed steps. This is
internal author-side scrutiny, not independent review.

## Claim-level source reconstruction

| Source | What is already established | Additional implication assessed here |
|---|---|---|
| Somhorst et al., 2601.05947v1, Section II and Appendix B | Optimal first-order coefficient; success distinguished as a separate problem. | A uniform ceiling over all survivor rows and arbitrary vacuum extensions; stability for any vanishing coefficient. |
| Saied et al., 2404.14217v4, Theorems III.5 and III.9 | Explicit uniform-first-row/Fourier success tending to one quarter and its approximately $4N$ achieving cost. | Matching converse when the first row is not uniform or has vacuum coupling; optimization over batch size for a requested derivative-level improvement. |
| Somhorst et al., 2404.14262v4, Section IV | Fourier heralding structure and discussion of low-error and loss regimes. | No new Fourier mechanism is claimed. The converse must not be read as a nonzero-error or lossy optimum. |
| Hoch et al., 2509.02296, protocol section and Fig. 1 | A two-active-photon circuit optimized relative to an untouched reference. | Different objective and active resources; it does not immediately constrain the present $N$-input-to-one target-mode task. |

The attempt to reconstruct the new ceiling from the predecessors reaches the
known uniform-row attainable sequence. It does not control a sequence with one
or more macroscopic survivor couplings. The heavy/light argument and accepted
amplitude constraint supply that missing step.

The new robustness corollary follows concisely from that argument. Its short
proof is not evidence of prior publication, nor does a new formula alone settle
physical significance. The central question is the unavoidable cost of strongly
suppressing first-order distinguishability with this passive resource set.

The current public arXiv records returned v4 for 2404.14217 and v1 for
2601.05947. Exact searches also returned related Bell-measurement and
photon-sorting work; no claims were based on those unrelated search snippets or
secondary summaries. The old nonlinear-sign-shift comparison remains in the
prior record and was not freshly audited in this pass.

## Positive and skeptical cases

**Positive.** The approximately four-photon-per-unit-reduction cost of the
established construction is not an accident of a balanced interferometer or
an artifact of requiring exact saturation of $1/N$. Increasing the vacuum-mode
count, unbalancing the network, or choosing a larger batch at a suboptimal
coefficient does not improve that leading ideal-limit cost. Four photons provide
a sharp finite companion where a vacuum tap helps and its optimum can be certified.

**Skeptical.** The resources are ideal and predetermined, and the result concerns
a derivative at zero input error. It does not itself lower an experimental error
rate or assess the full cost of an architecture. The finite convergence bound
has a large, conservative constant. Broad significance must rest on the
completed fundamental limit, not the small four-photon numerical improvement
or the number of passing checks.

The thermal one-photon probability is an interpretation of the diffuse-coupling
limit, not a new thermalization protocol or a grant of thermal ancillae.

## Verification

Five new groups pass on two completed runs with identical JSON reports.
The preceding six-group global checker and six-group pilot pass unchanged and
reproduce their canonical reports byte-for-byte. Exact report comparisons and
input hashes are in `RUN_RECORD.json` and `evidence/report_comparisons.json`.

All 41 incoming archive files and both nested manifests remain unchanged.
The new direct-permanent checks use optical matrices up to dimension six; the
embedded active-subset controls use matrices up to dimension eight. The legacy
global suite reaches dimension seven. No large optical Fock-state simulation or
experiment is implied.

The first new run passed four groups but failed the attempted rational
enclosure of the tap optimum. Both endpoints obtained from earlier uncertified
decimals lay below the true root. Exact signs now verify a correct interval.
The previous decimal approximation was within ordinary solver accuracy; the
polynomial, optimum characterization and all legacy assertions are unchanged.
The failed driver, failure report, and patch remain in `development/` and
`evidence/`.

A runtime HTTP request to arXiv failed because the container could not resolve
the host. Web-tool primary text remained available. The Saied PDF screenshot
attempt failed; no plot values were used. Hoch PDF page 2 rendered successfully
and confirmed the reference-photon path in Fig. 1. An initial report-writing
attempt from the non-root Python runtime was blocked by directory ownership;
the comparisons were recomputed and written by the container runtime without
modifying any scientific result.

## Boundaries

This record creates no repository, manuscript submission, author contact, or
external action. The quantum-group, Bell, monitoring, electron-preparation and
other protected projects remain separate. Their PDFs and code are not inputs.

Finite-$N\ge5$ exact optima, correlated source errors, loss, finite-$\epsilon$
uniformity, multiple retained outputs, adaptive survivor selection and extra
nonvacuum resources are outside the theorem. They are not required merely to
judge the present contribution.
