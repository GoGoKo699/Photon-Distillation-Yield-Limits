# Photon Distillation Yield Limits

**How many imperfect photons must passive optics consume to herald one photon with a much smaller distinguishability error?** This project gives a sharp leading photon-cost law, a stable success ceiling and exact small-batch optima for an ideal, predetermined-survivor task.

One attempt uses $`N`$ independent single photons with a common good internal mode, a lossless passive interferometer acting identically on internal modes, arbitrary additional vacuum inputs, and ideal internal-insensitive photon-number-resolving detectors. One output is retained in advance; an accepted record contains $`N-1`$ detected photons.

For each fixed apparatus, define ideal success $`p_0>0`$ and the first-order output-error coefficient $`c`$ by

```math
p_{\mathrm{herald}}(\epsilon)=p_0+O(\epsilon),
\qquad \epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2).
```

The zero-error derivative is taken before increasing the batch size or requested reduction. Counting rejected attempts, the ideal mean input cost is $`N/p_0`$.

## The resource law

Every allowed sequence satisfies

```math
c_N\longrightarrow0
\quad\Longrightarrow\quad
\limsup_{N\to\infty}p_{0,N}\le\frac14.
```

Optimizing both the interferometer and batch size for a requested first-order reduction $`R`$ gives

```math
\mathcal C(R):=\inf_{c\le1/R}\frac{N}{p_0}=(4+o(1))R.
```

[Known Fourier protocols](references/ATTRIBUTION.md) attain the quarter yield and approximately $`4N`$ cost at coefficient $`1/N`$. The contribution here is the matching converse over arbitrary survivor rows and vacuum extensions. It also covers coefficients that vanish without attaining $`1/N`$ at every size.

| Resource regime | Optimal ideal success | Ideal mean photon consumption |
|---|---:|---:|
| Two inputs, $`c=1/2`$ | $`1/4`$ | $`8`$ |
| Three inputs, $`c=1/3`$ | $`1/3`$ | $`9`$ |
| Four inputs, $`c=1/4`$ | $`0.262466988\ldots`$ | $`15.24001181\ldots`$ |
| Requested reduction $`R\to\infty`$, batch size optimized | Sharp asymptotic ceiling $`1/4`$ | $`(4+o(1))R`$ |

The small rows have different purification targets. A [monitored vacuum tap](science/OPTICAL_CONSTRUCTION.md) attains the two- and four-input optima; its detected photons are part of the heralding record, not unobserved loss.

## Read the science

The [scientific entrypoint](science/README.md) connects the full account. Each topic has a direct route:

| Question | Authoritative account |
|---|---|
| What resources and order of limits define the claim? | [Model and claims](science/MODEL_AND_CLAIMS.md) |
| Why can no competing network improve the leading cost? | [Theorem](science/THEOREM.md) and [uniform proof details](science/PROOF_DETAILS.md) |
| Which apparatus attains the bounds? | [Fourier construction and exact small batches](science/OPTICAL_CONSTRUCTION.md) |
| Why does one quarter appear, and why is counting insufficient? | [Output-number mechanism](science/PHYSICAL_MECHANISM.md) |
| What internal state and interference visibility are heralded? | [Physical interpretation](science/PHYSICAL_INTERPRETATION.md) |
| Which ingredients are inherited? | [Result in context](references/CONTRIBUTION_REVIEW.md), [attribution](references/ATTRIBUTION.md) and [structured bibliography](references/SOURCES.json) |
| Where are the certificates and reproducible checks? | [Proof map](science/PROOF_MAP.md) and [verification](verification/README.md) |

Approaching the ceiling with vanishing $`c_N`$ forces many individually weak survivor couplings whose total intensity approaches one. The ideal unconditional output then has vacuum, single-photon and multiphoton probabilities approaching $`1/2`$, $`1/4`$ and $`1/4`$. This thermal number marginal precedes heralding: **it does not certify the internal purity of the retained photon**. Equal ideal yield can accompany purification or error amplification, depending on which detector patterns are accepted.

## Learn the project

The single educational anchor is **Malte C. Tichy, Interference of Identical Particles from Entanglement to Boson-Sampling**, *Journal of Physics B* **47**, 103001 (2014), arXiv:1312.4266v2.

Use the [Tichy bridge](learning/TICHY_BRIDGE.md) for selected sections, translated notation and a complete two-photon example. The [30-milestone map](learning/MILESTONES.md) supplies a common understanding route: **10 background/preliminaries milestones** assemble the optical task, and **20 narrative/innovation milestones** connect the amplitude constraints, attaining circuits, uniform converse and physical consequences. The [learning entrypoint](learning/README.md) explains how the two resources fit together.

The [LLM reading guide](llms.txt) maps scientific questions and study intentions to these authoritative files. The map is independent of any reader’s assessment history.

## Reproduce the checks

From the repository root:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output-dir build/verification
```

Use a new output directory. The [verification guide](verification/README.md) specifies the pinned environment, all 21 original scientific check groups, preservation checks and report-review rules. Finite calculations check optical identities and exact certificates; the general resource law rests on the uniform analytical proof.

## Scope

This is an ideal first-order result with independent internal errors and a predetermined survivor. Its expansion is defined at each fixed apparatus; it is not a uniform finite-input-error or loss-tolerant throughput guarantee. The quarter is an asymptotic purification ceiling, not an upper bound on every small-batch success or every raw single-photon event. The source comparison records its specific versions, passages and access limits.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

Code is available under the [MIT license](LICENSE). Referenced publications retain their respective licenses.
