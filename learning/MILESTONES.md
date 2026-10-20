# Thirty milestones for photon-distillation yield limits

This is a project-defined understanding map for any reader, including an LLM.
It is independent of a particular learner’s background, answers or progress.
The map covers the connected scientific story rather than every technical lemma.

The single educational anchor is **Malte C. Tichy, Interference of Identical
Particles from Entanglement to Boson-Sampling** (2014), arXiv:1312.4266v2.
The [source bridge](TICHY_BRIDGE.md) fixes its section and notation dictionary.
Source references to Tichy below use that selected version. The anchor supplies
optical prerequisites; the universal distillation converse is derived in the
project’s scientific account, not attributed to the tutorial.

**Allocation: 10 background/preliminaries milestones and 20 narrative/innovation
milestones.** The background assembles one complete heralded optical task from
single-photon objects. The longer narrative follows a single resource question
through amplitude constraints, attaining examples, a uniform arbitrary-network
bound, and its global physical interpretation. Each phase progresses from local
objects to a synthesis. Dependencies refer only to earlier milestones.

## Phase I — Background and preliminaries

### M01 — A photon has spatial and internal degrees of freedom

**Phase:** Background/preliminaries.  
**Central question:** Which part of a photon does the interferometer change?  
**Understanding target:** Distinguish a spatial port from an internal wavepacket and identify the common good internal mode. A change of port is not itself a change of internal quality.  
**Dependencies:** None.  
**Story role:** Begin with the physical carrier and the observable whose error will be reduced.  
**Conceptual connection:** Connect an internal density operator to a spatial creation operator without conflating the two spaces.  
**Sources:** Tichy §2.2.1; [bridge §2](TICHY_BRIDGE.md#2-translate-the-notation); [model](../science/MODEL_AND_CLAIMS.md).

### M02 — Independent internal errors

**Phase:** Background/preliminaries.  
**Central question:** What does one erroneous input mean in a mixed many-photon preparation?  
**Understanding target:** Read the independent input mixture with a shared good mode and orthogonal bad components. Distinguish independence from assumptions about overlap between different bad states.  
**Dependencies:** M01.  
**Story role:** Specify which input alternatives can contribute at first order.  
**Conceptual connection:** Connect single-photon mixtures to a product preparation and to the single-error sector.  
**Sources:** Tichy §4.3; [bridge §3](TICHY_BRIDGE.md#3-separate-the-ideal-amplitude-from-one-erroneous-input); [mixed-error proof](../science/PROOF_DETAILS.md#1-independent-mixed-errors-and-accepted-amplitudes).

### M03 — Bosonic occupation states

**Phase:** Background/preliminaries.  
**Central question:** Why do repeated photons in one port require factorial normalization?  
**Understanding target:** Explain normalized Fock states and the square-root factorial relating a creation-operator monomial to its probability amplitude.  
**Dependencies:** M01.  
**Story role:** Supply the normalization needed for complete interference calculations.  
**Conceptual connection:** Connect bosonic creation algebra to probabilities when outputs contain collisions.  
**Sources:** Tichy §2.1.2 and §3.4, Eq. (60); [bridge §2](TICHY_BRIDGE.md#2-translate-the-notation).

### M04 — Passive unitaries and empty inputs

**Phase:** Background/preliminaries.  
**Central question:** How does an arbitrary vacuum extension enter the retained output?  
**Understanding target:** Translate the output-first unitary convention, identify its occupied columns, and explain why their survivor intensities sum to at most one. Unused row norm is vacuum coupling, not loss.  
**Dependencies:** M01, M03.  
**Story role:** Extend the local optical description to the allowed network class.  
**Conceptual connection:** Connect column orthogonality, photon conservation and the selected survivor row.  
**Sources:** Tichy §§2.2.1, 3.1–3.2; [bridge §2](TICHY_BRIDGE.md#2-translate-the-notation); [fixed resources](../science/MODEL_AND_CLAIMS.md#fixed-resources).

### M05 — Amplitudes versus probabilities

**Phase:** Background/preliminaries.  
**Central question:** When do two alternatives interfere rather than add incoherently?  
**Understanding target:** Distinguish coherent alternatives for identical photons from mixture alternatives or alternatives carrying orthogonal internal records. Relate this distinction to two-photon interference.  
**Dependencies:** M02, M03, M04.  
**Story role:** Identify the physical source of the later error-reduction identity.  
**Conceptual connection:** Connect distinguishability information to the addition of complex amplitudes.  
**Sources:** Tichy §2.1.2 and §4.3; [bridge §§3–4](TICHY_BRIDGE.md#3-separate-the-ideal-amplitude-from-one-erroneous-input).

### M06 — Many-photon transition amplitudes

**Phase:** Background/preliminaries.  
**Central question:** How is an occupation probability computed from a spatial unitary?  
**Understanding target:** Explain repeated output rows, permanents and output factorials for one photon per occupied input. Distinguish the optical matrix dimension from a Fock-space dimension.  
**Dependencies:** M03, M04, M05.  
**Story role:** Scale the elementary interference language to a photon batch.  
**Conceptual connection:** Connect permutations of indistinguishable input origins to normalized detector amplitudes.  
**Sources:** Tichy §§3.1–3.2 and §3.4, Eq. (60); [bridge §2](TICHY_BRIDGE.md#2-translate-the-notation); [optical construction](../science/OPTICAL_CONSTRUCTION.md).

### M07 — Heralding without measuring internal error

**Phase:** Background/preliminaries.  
**Central question:** What does an accepted detector record certify?  
**Understanding target:** Explain why N−1 measured photons certify one survivor only under the stated lossless counting assumptions, and why an internal-insensitive detector must be traced over its internal degrees of freedom.  
**Dependencies:** M02, M04, M05, M06.  
**Story role:** Turn a passive network into a conditional purification operation.  
**Conceptual connection:** Connect number-pattern selection to a normalized conditional internal state.  
**Sources:** Tichy §2.3.2; [bridge §4](TICHY_BRIDGE.md#4-work-through-two-photons-and-one-monitored-vacuum-tap); [conditional-state interpretation](../science/PHYSICAL_INTERPRETATION.md#1-what-the-first-order-error-coefficient-measures).

### M08 — The derivative-first objective

**Phase:** Background/preliminaries.  
**Central question:** Which limit defines first-order purification?  
**Understanding target:** Distinguish ideal success p₀, the input error ε and the conditional coefficient c. Take the derivative at fixed apparatus before increasing N or the requested reduction; do not assume a uniform finite-error remainder.  
**Dependencies:** M02, M07.  
**Story role:** Define the exact optimization rather than a different finite-error task.  
**Conceptual connection:** Connect conditional normalization to the order in which resource limits are taken.  
**Sources:** [model objectives](../science/MODEL_AND_CLAIMS.md#objectives-and-limits); [bridge §3](TICHY_BRIDGE.md#3-separate-the-ideal-amplitude-from-one-erroneous-input).

### M09 — Count every attempted photon batch

**Phase:** Background/preliminaries.  
**Central question:** Why is the ideal mean consumption N/p₀ rather than N?  
**Understanding target:** Explain repeated independent attempts, rejected batches and a requested first-order reduction R. Compare apparatuses only after matching their purification objective.  
**Dependencies:** M07, M08.  
**Story role:** Translate heralding into the resource being optimized.  
**Conceptual connection:** Connect a success probability to mean input-photon consumption without claiming a clock rate or hardware throughput.  
**Sources:** [model objectives](../science/MODEL_AND_CLAIMS.md#objectives-and-limits); [interpretation §6](../science/PHYSICAL_INTERPRETATION.md#6-order-of-limits-and-photon-consumption).

### M10 — A complete two-photon purifier

**Phase:** Background/preliminaries.  
**Central question:** How do the optical state, detector record, error coefficient and cost fit together?  
**Understanding target:** Follow the two occupied inputs, monitored vacuum tap and retained output through normalized amplitudes. Recover ideal success 1/4, coefficient 1/2 and ideal consumption eight without treating the tap click as loss.  
**Dependencies:** M01, M02, M03, M04, M05, M06, M07, M08, M09.  
**Story role:** Synthesize the background into one complete instance of the scientific task.  
**Conceptual connection:** Join interference, internal tracing, conditioning and failed-attempt accounting.  
**Sources:** [complete worked example](TICHY_BRIDGE.md#4-work-through-two-photons-and-one-monitored-vacuum-tap); [apparatus hypotheses](../science/PHYSICAL_INTERPRETATION.md#2-why-the-resource-assumptions-enter-the-proof).

## Phase II — Narrative and innovation

### M11 — Bad-survivor detector vectors

**Phase:** Narrative/innovation.  
**Central question:** Why can every erroneous-survivor alternative be represented in the same detector space?  
**Understanding target:** Construct vᵢ when photon i is the sole bad input and survives: every detected photon is then good. Explain why the ideal one-survivor vector is the coherent sum of the vᵢ.  
**Dependencies:** M02, M06, M07, M10.  
**Story role:** Begin the converse with a local amplitude decomposition.  
**Conceptual connection:** Connect input-origin alternatives to a common detected-mode Hilbert space.  
**Sources:** [theorem §2](../science/THEOREM.md#2-accepted-amplitudes-constrain-purification); [mixed-error proof](../science/PROOF_DETAILS.md#1-independent-mixed-errors-and-accepted-amplitudes).

### M12 — Accepted amplitudes determine the error derivative

**Phase:** Narrative/innovation.  
**Central question:** Why is cp₀ the sum of accepted bad-survivor squared norms?  
**Understanding target:** Use aᵢ=Pvᵢ to distinguish ideal coherent success from independent single-error probabilities. Explain the denominator p₀+O(ε) and the extension to mixed, input-dependent bad states.  
**Dependencies:** M08, M11.  
**Story role:** Establish the observable quantity the universal proof must control.  
**Conceptual connection:** Connect the detector vectors to the conditional internal density operator.  
**Sources:** [proof details §1](../science/PROOF_DETAILS.md#1-independent-mixed-errors-and-accepted-amplitudes); [conditional state](../science/PHYSICAL_INTERPRETATION.md#1-what-the-first-order-error-coefficient-measures).

### M13 — The coefficient bound and input-origin erasure

**Phase:** Narrative/innovation.  
**Central question:** What must be equal to attain c=1/N?  
**Understanding target:** Explain the nonnegative Cauchy residual and why equality requires coincident complex accepted amplitudes, not merely equal probabilities. Identify the coefficient bound as an inherited result.  
**Dependencies:** M11, M12.  
**Story role:** Expose the exact constraint linking purification and accepted information.  
**Conceptual connection:** Connect a norm identity to the removal of information about a possible erroneous survivor’s input origin.  
**Sources:** [theorem §2](../science/THEOREM.md#2-accepted-amplitudes-constrain-purification); [attribution](../references/ATTRIBUTION.md#existing-results-and-the-additional-converse).

### M14 — One-row Gram reduction

**Phase:** Narrative/innovation.  
**Central question:** How can a bound ignore the detailed layout of every detector port?  
**Understanding target:** Derive the role of the Gram matrix of the vᵢ and its dependence only on survivor intensities. Distinguish the coherent-projection relaxation from physical number-pattern selection, including zero and singular couplings.  
**Dependencies:** M04, M06, M11, M13.  
**Story role:** Reduce an all-network comparison to row data without shrinking its resources.  
**Conceptual connection:** Connect unitarity and bosonic Gram permanents to a necessary success bound.  
**Sources:** [Gram derivation](../science/PROOF_DETAILS.md#2-gram-reduction-without-inverses-or-factor-denominators); [finite-resource Gram bound](../science/OPTICAL_CONSTRUCTION.md#5-sharp-two--three--and-four-photon-bounds).

### M15 — Fourier character selection

**Phase:** Narrative/innovation.  
**Central question:** Why do the accepted Fourier records erase input origin?  
**Understanding target:** Follow cyclic input permutations through arbitrary output occupations, including collisions. Explain the zero-character rule, why primality is unnecessary, and why ideal-dark accepted records do not change p₀ or c.  
**Dependencies:** M06, M11, M13.  
**Story role:** Supply the symmetry argument for a physically attaining family.  
**Conceptual connection:** Connect the anchor’s Fourier suppression example to the project’s heralding condition for all bosonic occupations.  
**Sources:** Tichy §3.7.1; [bridge §5](TICHY_BRIDGE.md#5-extend-fourier-selection-to-collisions); [construction §2](../science/OPTICAL_CONSTRUCTION.md#2-accepted-amplitudes-erase-the-erroneous-photons-input-label).

### M16 — A monitored tap and its exact success law

**Phase:** Narrative/innovation.  
**Central question:** Which tap events can increase success without changing the first-order coefficient?  
**Understanding target:** Include nonzero tap counts in the N−1 total while assigning the tap character zero. Explain the exact Pₙ(s) formula and its positive-success domain, including the exceptional untapped two-input case.  
**Dependencies:** M04, M07, M10, M15.  
**Story role:** Complete the attaining apparatus and distinguish vacuum coupling from unobserved loss.  
**Conceptual connection:** Connect factorial moments, photon subtraction and coherent character selection.  
**Sources:** [construction §§1–3](../science/OPTICAL_CONSTRUCTION.md#1-unitary-and-detector-rule); [positive domain](../science/OPTICAL_CONSTRUCTION.md#3-exact-success-and-its-positive-domain).

### M17 — Sharp two- and three-input bounds

**Phase:** Narrative/innovation.  
**Central question:** Why can additional empty ports not improve these two small-batch optima?  
**Understanding target:** Combine the general Gram relaxation with the two- and three-input optimization and their physical attainment. Explain why their costs are not comparisons at identical output-purity targets.  
**Dependencies:** M09, M13, M14, M16.  
**Story role:** Close exact finite examples before the general asymptotic argument.  
**Conceptual connection:** Connect a necessary optical bound to a matching apparatus, keeping coefficient targets distinct.  
**Sources:** [sharp small batches](../science/OPTICAL_CONSTRUCTION.md#5-sharp-two--three--and-four-photon-bounds); [original detailed certificate](../archive/research-handoff-2026-10-08/prior/prior/prior/PILOT.md).

### M18 — The four-input optimum and certificate

**Phase:** Narrative/innovation.  
**Central question:** What makes a polynomial certificate a global optical bound?  
**Understanding target:** Explain the sorted-coupling parameterization, positive denominator, nonnegative coefficient certificate and Fourier-tap attainment. Distinguish the unique optimal intensity row from uniqueness of the whole network and from an unsupported general balancing rule.  
**Dependencies:** M14, M16, M17.  
**Story role:** Establish the finite-resource companion without relying on sampled interferometers.  
**Conceptual connection:** Connect a bound over all row intensities to exact algebraic verification and a physical implementation.  
**Sources:** [four-input proof](../science/OPTICAL_CONSTRUCTION.md#5-sharp-two--three--and-four-photon-bounds); [integer certificate](../archive/research-handoff-2026-10-08/prior/prior/certificates/four_photon_positive.json); [verification](../verification/README.md).

### M19 — Strong and weak survivor couplings

**Phase:** Narrative/innovation.  
**Central question:** Why must the universal proof keep the strongly coupled inputs?  
**Understanding target:** Partition the occupied inputs at a threshold δ, bound the size of the strong group and the squared intensities of the weak group. Explain why assuming a balanced or already diffuse row would omit competitors.  
**Dependencies:** M04, M12, M14.  
**Story role:** Begin the arbitrary-row asymptotic comparison.  
**Conceptual connection:** Connect limited total row norm to a controlled decomposition rather than an assumed architecture.  
**Sources:** [theorem §3](../science/THEOREM.md#3-the-uniform-bound-over-arbitrary-output-rows); [strong-coupling control](../science/PHYSICAL_INTERPRETATION.md#5-strong-coupling-can-raise-raw-yield-but-cannot-evade-the-converse).

### M20 — The exact grouped integral

**Phase:** Narrative/innovation.  
**Central question:** Why may a squared norm have a signed integral representation?  
**Understanding target:** Explain how diagonal, within-group and cross-group Gram terms produce Q. Keep the finite-product derivative identity distinct from any pointwise positivity claim.  
**Dependencies:** M14, M19.  
**Story role:** Express the full comparison in a form permitting a uniform limit.  
**Conceptual connection:** Connect bosonic permanent sums to scalar integrals without dividing by product factors.  
**Sources:** [grouped Gram identity](../science/PROOF_DETAILS.md#2-gram-reduction-without-inverses-or-factor-denominators); [theorem §3](../science/THEOREM.md#3-the-uniform-bound-over-arbitrary-output-rows).

### M21 — The auxiliary no-photon probability

**Phase:** Narrative/innovation.  
**Central question:** Where does the bound on the limiting grouped norm come from?  
**Understanding target:** Track the integration-by-parts boundary terms and the chosen weight ω. Identify the resulting permanent as an actual auxiliary no-photon probability, not an extra device resource or a positive integrand.  
**Dependencies:** M04, M19, M20.  
**Story role:** Identify the probability bound underlying the numerical quarter.  
**Conceptual connection:** Connect a signed algebraic expression to a normalized passive-optical event.  
**Sources:** [boundary terms and auxiliary probability](../science/PROOF_DETAILS.md#3-exponential-replacement-and-its-boundary-terms).

### M22 — Uniform replacement, not a pointwise shortcut

**Phase:** Narrative/innovation.  
**Central question:** What permits optimization over a changing sequence of apparatuses?  
**Understanding target:** Explain the product and derivative envelopes, control through zeros and sign changes, and the size-independent integrated error 96v₂. Distinguish a uniform proof from a numerical fit or a useful small-batch estimate.  
**Dependencies:** M19, M20, M21.  
**Story role:** Control the limiting step over every allowed network.  
**Conceptual connection:** Connect small individual couplings to an error bound valid on the whole integration domain.  
**Sources:** [uniform estimates](../science/PROOF_DETAILS.md#4-a-uniform-error-bound-over-the-whole-half-line); [verification scope](../verification/README.md#exit-codes-and-evidence).

### M23 — The stable quarter-yield ceiling

**Phase:** Narrative/innovation.  
**Central question:** Why does vanishing c suffice without equality c=1/N?  
**Understanding target:** Bound the accepted strong-group amplitude, apply the norm inequality and choose δ as c tends to zero. State the universal limsup bound with its derivative-first order and contrast it with finite-batch success above one quarter.  
**Dependencies:** M12, M19, M21, M22.  
**Story role:** Complete the central all-network converse.  
**Conceptual connection:** Connect first-order quality to a success bound that survives suboptimal within-batch suppression.  
**Sources:** [stable converse](../science/PROOF_DETAILS.md#5-the-stable-ceiling-and-constrained-coupling); [theorem §4](../science/THEOREM.md#4-stable-converse-and-sharpness).

### M24 — Optimize photon cost over batch size

**Phase:** Narrative/innovation.  
**Central question:** Why can a larger batch with weaker purification not improve the leading cost?  
**Understanding target:** Combine N≥R with the uniform success bound and known Fourier attainment. Explain the infimum over both apparatus and batch size, even when no finite minimizer is assumed, to obtain the leading 4R cost.  
**Dependencies:** M09, M13, M16, M23.  
**Story role:** Turn the success ceiling into the project’s central resource conclusion.  
**Conceptual connection:** Connect a coefficient lower bound and a uniform yield upper bound; neither an attaining family nor an average alone supplies the converse.  
**Sources:** [cost-infimum proof](../science/PROOF_DETAILS.md#6-attainment-and-the-infimum-over-batch-size); [result in context](../references/CONTRIBUTION_REVIEW.md).

### M25 — Necessary form of near-optimal rows

**Phase:** Narrative/innovation.  
**Central question:** What must an apparatus approaching the ceiling do with its couplings?  
**Understanding target:** Explain why occupied row norm must approach one and every individual coupling must vanish. Distinguish necessary diffuseness from exact balance or sufficient purification, and interpret the constrained s/(1+s)² ceiling.  
**Dependencies:** M19, M21, M23.  
**Story role:** Extract structural consequences beyond the value of the optimum.  
**Conceptual connection:** Connect equality in the resource limit to how the survivor receives photons from many inputs.  
**Sources:** [necessary apparatus form](../science/THEOREM.md#5-necessary-form-of-a-near-optimal-apparatus); [fixed-coupling attainment](../science/OPTICAL_CONSTRUCTION.md#4-fixed-coupling-asymptotic-attainment).

### M26 — The whole output number distribution

**Phase:** Narrative/innovation.  
**Central question:** Why does a near-optimal ideal output become thermal before heralding?  
**Understanding target:** Use the exact characteristic function and diffuse-row condition, then control the number tail to understand trace-norm convergence. Interpret half vacuum, quarter single photon and quarter multiple photons without introducing internal error or loss.  
**Dependencies:** M03, M25.  
**Story role:** Derive the physical number statistics forced by the optimum.  
**Conceptual connection:** Connect established passive-mixing central-limit behavior to a necessary consequence of the distillation converse.  
**Sources:** [number-law derivation](../science/PHYSICAL_MECHANISM.md#2-direct-proof-for-arbitrary-diffuse-rows); [related-work attribution](../references/ATTRIBUTION.md#related-results).

### M27 — Number statistics do not certify purification

**Phase:** Narrative/innovation.  
**Central question:** How can the same ideal yield accompany opposite error behavior?  
**Understanding target:** Compare count-only and character-selected records, including ideal-dark patterns. Explain the strongly coupled raw-yield example and why neither its success count nor thermal statistics prove an internal-quality improvement.  
**Dependencies:** M12, M15, M23, M26.  
**Story role:** Test the physical interpretation against nonpurifying controls.  
**Conceptual connection:** Connect accepted error amplitudes to the distinction between raw single-photon probability and purified-photon yield.  
**Sources:** [selection controls](../science/PHYSICAL_MECHANISM.md#3-same-ideal-success-opposite-error-behavior); [strong-coupling example](../science/PHYSICAL_MECHANISM.md#4-why-the-central-limit-theorem-alone-is-not-the-converse).

### M28 — Cost equality and interference visibility

**Phase:** Narrative/innovation.  
**Central question:** What observable quality and amplitude structure accompany leading-cost optimality?  
**Understanding target:** Explain N/R→1 and Nc→1 at cost 4R, the normalized mean-square input-origin condition, and the leading HOM visibility deficit for two independent successful outputs. Distinguish a perfect-reference comparison from a two-imperfect-photon comparison.  
**Dependencies:** M05, M12, M13, M24, M27.  
**Story role:** Join the asymptotic resource result to its conditional internal-state meaning.  
**Conceptual connection:** Connect accepted amplitude erasure, minimum batch size and an operational interference observable without inferring finite-error hardware performance.  
**Sources:** [cost equality](../science/PHYSICAL_MECHANISM.md#5-matching-the-minimum-cost-imposes-additional-equality-conditions); [HOM interpretation](../science/PHYSICAL_INTERPRETATION.md#relation-to-hong--ou--mandel-visibility).

### M29 — Contribution and evidence boundaries

**Phase:** Narrative/innovation.  
**Central question:** Which conclusions are inherited, proved here, or only numerically checked?  
**Understanding target:** Separate the coefficient optimum, Fourier attaining construction and central-limit tools from the stable arbitrary-row converse and finite certificates. Distinguish exact certificate checks from uniform proof, and targeted source comparison from exhaustive priority.  
**Dependencies:** M18, M23, M24, M26, M28.  
**Story role:** Assess the completed result against the strongest relevant predecessors.  
**Conceptual connection:** Connect each scientific claim to its authoritative proof, source role and reproducibility evidence.  
**Sources:** [attribution](../references/ATTRIBUTION.md); [structured source record](../references/SOURCES.json); [proof map](../science/PROOF_MAP.md); [verification](../verification/README.md).

### M30 — The complete purification resource law

**Phase:** Narrative/innovation.  
**Central question:** What does the optimum settle, and which hypotheses carry that conclusion?  
**Understanding target:** Explain the task from input preparation through accepted amplitudes, the uniform success converse, Fourier attainment and optimized photon consumption. Preserve the predetermined-survivor and derivative-first qualifications, and distinguish the finite companion, necessary number statistics and heralded internal quality.  
**Dependencies:** M10, M13, M16, M18, M23, M24, M25, M26, M27, M28, M29.  
**Story role:** Synthesize the narrative into one bounded scientific contribution.  
**Conceptual connection:** Connect the local interference mechanism to the global optimal-resource statement and its precise domain.  
**Sources:** [scientific route](../science/README.md); [model](../science/MODEL_AND_CLAIMS.md); [theorem](../science/THEOREM.md); [physical interpretation](../science/PHYSICAL_INTERPRETATION.md).

