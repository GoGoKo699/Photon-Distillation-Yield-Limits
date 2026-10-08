# Model and claim hierarchy

The [tutorial bridge](TUTORIAL_BRIDGE.md) introduces the optical notation and
a worked heralding example. The complete statements and proofs are in
[THEOREM.md](THEOREM.md).

## Fixed resources

One attempt starts with $`N`$ independent single photons in distinct occupied
spatial inputs. Their internal states share a good mode and have the form

```math
\rho_i(\epsilon)=(1-\epsilon)|g\rangle\langle g|+\epsilon\sigma_i,
\qquad \mathrm{supp}\sigma_i\perp|g\rangle.
```

A fixed, lossless passive spatial unitary acts identically on internal modes.
Every additional input is vacuum; their number is unrestricted.
One output is retained in advance;
all other outputs are measured by ideal photon-number-resolving detectors which
do not distinguish internal modes. Accepted records contain $`N-1`$ photons.

## Objectives and limits

For the conditional internal state, define
$`\epsilon_{\mathrm{out}}=1-\langle g|\rho_{\mathrm{out}}|g\rangle`$.
At fixed apparatus, $`p_{\mathrm{herald}}(\epsilon)=p_0+O(\epsilon)`$ and
$`\epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2)`$, with $`p_0>0`$.
The derivative at zero error precedes the sequence in $`N`$ or the requested
reduction $`R`$. The expansion remainder is controlled at each fixed apparatus.
Independent attempts consume $`N/p_0`$ input photons per success in this ideal limit.

| Role | Statement |
|---|---|
| Central converse | Any sequence with $`c_N\to0`$ has $`\limsup p_{0,N}\le1/4`$. |
| Resource optimum | Optimizing batch size and network gives $`\mathcal C(R)=(4+o(1))R`$. |
| Attainment | Established Fourier protocols achieve the asymptotic constant. |
| Finite companion | Sharp optima for $`N=2,3,4`$ at $`c=1/N`$, including vacuum extensions. |
| Necessary structure | Sequences with $`c_N\to0`$ and $`p_{0,N}\to1/4`$ have diffuse survivor couplings and an ideal unconditional thermal number marginal of mean one. |
| Control | Equal ideal single-photon yield does not imply equal purification; the acceptance rule matters. |

Thermal number statistics concern the unconditional designated output for ideal
inputs, not the internal purity of the heralded photon. The four-photon vacuum
tap is monitored; its count contributes to the accepted total and may be nonzero.
The [construction](OPTICAL_CONSTRUCTION.md) specifies the complete rule.
The [physical interpretation](PHYSICAL_INTERPRETATION.md) derives the corresponding
first-order two-copy interference visibility and explains each hypothesis.

## Resource and attribution

The optimized resource is ideal mean input-photon consumption under the
first-order model above. [The result in context](CONTRIBUTION_REVIEW.md) and
[the attribution map](../literature/ATTRIBUTION.md) relate the converse to
established constructions and coefficient bounds.
