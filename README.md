# Photon Distillation Yield Limits

**Passive purification of photon indistinguishability has an unavoidable leading photon cost.**

How many imperfect photons must a passive optical network consume to herald one
photon with a much smaller distinguishability error? Established Fourier
protocols approach four photons consumed per unit of first-order error reduction.
This repository proves the matching limit across the stated apparatus class,
including unequal couplings and additional vacuum ports.

| Read next | Purpose |
|---|---|
| [Tutorial bridge](research/TUTORIAL_BRIDGE.md) · [Physical interpretation](research/PHYSICAL_INTERPRETATION.md) | Learn from one external tutorial, calculate a small example, and identify the measured quantities. |
| [Theorem](research/THEOREM.md) · [Proof details](research/PROOF_DETAILS.md) | Follow the stable yield bound and optimized photon-cost law. |
| [Model and claims](research/MODEL_AND_CLAIMS.md) · [Optical construction](research/OPTICAL_CONSTRUCTION.md) | Check the resources, accepted detector records, and attaining networks. |
| [Physical mechanism](research/PHYSICAL_MECHANISM.md) | Understand the necessary number statistics and the role of pattern selection. |
| [The result in context](research/CONTRIBUTION_REVIEW.md) · [Attribution](literature/ATTRIBUTION.md) | Separate the converse from established constructions and related bounds. |
| [Proof map](research/PROOF_MAP.md) · [Verification](VERIFICATION.md) | Locate complete derivations and reproduce the checks. |
| [LLM guide](llms.txt) | Find relevant research questions, search phrases, and authoritative files. |

## What is being optimized

One attempt uses $`N`$ independent single photons with a shared good internal mode,
a fixed passive interferometer that acts identically on internal modes, and any
number of vacuum inputs. One output is retained in advance. Ideal number-resolving
detectors measure all other outputs; accepted records contain $`N-1`$ photons.

Let $`p_0>0`$ be the ideal-input success probability and $`c`$ the first-order
coefficient of the retained photon's internal-mode error:

```math
p_{\mathrm{herald}}(\epsilon)=p_0+O(\epsilon),
\qquad \epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2).
```

The error derivative is taken at fixed apparatus, before increasing the batch
size or requested reduction. Independent attempts consume $`N/p_0`$ photons per
success in this ideal limit, including rejected batches.

## Yield and photon cost

Every allowed sequence obeys the stable bound

```math
c_N\longrightarrow0
\quad\Longrightarrow\quad
\limsup_{N\to\infty}p_{0,N}\le\frac14.
```

For a requested first-order reduction factor $`R`$, optimizing both the network
and the batch size therefore gives

```math
\mathcal C(R):=\inf_{c\le1/R}\frac{N}{p_0}=(4+o(1))R.
```

Known Fourier protocols attain this leading cost. The converse controls
arbitrary survivor couplings, vacuum enlargement, and batches whose error
coefficient vanishes without attaining $`1/N`$ at each size.

| Consequence | Meaning |
|---|---|
| Sharp leading cost | Stronger first-order purification cannot improve on the asymptotic Fourier photon-consumption rate in this class. |
| Necessary output structure | With $`c_N\to0`$, approaching the quarter ceiling forces the occupied-input survivor couplings to become individually weak, with total intensity approaching one. |
| Exact small batches | At $`c=1/N`$, the sharp success probabilities are $`1/4`$ for two photons, $`1/3`$ for three, and $`0.262466988\ldots`$ for four. |

The [optical construction](research/OPTICAL_CONSTRUCTION.md) specifies the
monitored vacuum tap that attains the two- and four-photon optima. Its detector
may register photons; those counts contribute to the heralding record.

## Why counting one photon is not enough

A network can have a raw one-photon output probability larger than one quarter.
The purification requirement constrains which of those events can be accepted.
The proof first controls accepted amplitudes associated with different input
origins, then establishes the uniform yield bound.

For a sequence with $`c_N\to0`$ and $`p_{0,N}\to1/4`$, the ideal unconditional output number
law becomes thermal, with vacuum, one-photon, and multiphoton probabilities
approaching $`1/2`$, $`1/4`$, and $`1/4`$. The
[physical mechanism](research/PHYSICAL_MECHANISM.md) derives this consequence.
The same ideal yield can accompany very different output errors: accepting every
one-survivor count in the Fourier network amplifies the leading error, while
Fourier-character selection suppresses it. Number statistics alone do not
certify internal-state purification.

## One tutorial, then this result

The selected learning anchor is:

> Malte C. Tichy, **Interference of Identical Particles from Entanglement to Boson-Sampling**,
> *Journal of Physics B* **47**, 103001 (2014).
> [Tutorial, arXiv:1312.4266v2](https://arxiv.org/html/1312.4266v2) ·
> [Published article](https://doi.org/10.1088/0953-4075/47/10/103001)

The [tutorial bridge](research/TUTORIAL_BRIDGE.md) selects a short route through
that source, translates its conventions, works out a two-photon herald by hand,
and connects accepted amplitudes to the yield theorem. It assumes basic quantum
mechanics and linear algebra. Other references document attribution and proof
inputs; the learning route uses this one external source.

## Evidence and reproduction

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python tools/verify.py --output-dir build/verification
```

Use a new output directory. The 21 scientific groups check identities, optical
examples, and exact certificates. The large-size result rests on the uniform
analytical proof. [Verification](VERIFICATION.md) explains source preservation,
strict report comparisons, and numerical-runtime differences; the
[proof map](research/PROOF_MAP.md) links the complete evidence.

The theorem concerns ideal first-order photon consumption in the specified
static, predetermined-survivor model. Its order of limits and physical
hypotheses are stated in [Model and claims](research/MODEL_AND_CLAIMS.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) supplies relevant questions, search phrases, and direct
links to the current scientific record.

Code is available under the owner's original [MIT license](LICENSE). Linked
third-party papers are not redistributed or relicensed by this repository.
