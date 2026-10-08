# Model and claim hierarchy

The complete statements and proofs are in [THEOREM.md](THEOREM.md).

## Fixed resources

One attempt starts with $N$ independent single photons in distinct occupied
spatial inputs. Their internal states share a good mode and have the form

$$
\rho_i(\epsilon)=(1-\epsilon)|g\rangle\langle g|+\epsilon\sigma_i,
\qquad \operatorname{supp}\sigma_i\perp|g\rangle.
$$

A predetermined passive spatial unitary acts identically on internal modes.
Any number of extra vacuum inputs is allowed. One output is retained in advance;
all other outputs are measured by ideal photon-number-resolving detectors which
do not distinguish internal modes. Accepted records contain $N-1$ photons.
There are no losses, extra nonvacuum inputs, mode filters, intermediate adaptive
operations, or outcome-dependent survivor choices.

## Objectives and limits

At fixed apparatus, $p_{\mathrm{herald}}(\epsilon)=p_0+O(\epsilon)$ and
$\epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2)$, with $p_0>0$.
The derivative at zero error precedes the sequence in $N$ or the requested
reduction $R$. The remainder is not claimed uniform in $N\epsilon$.
Independent attempts consume $N/p_0$ input photons per success in this ideal limit.

| Role | Statement |
|---|---|
| Central converse | Any sequence with $c_N\to0$ has $\limsup p_{0,N}\le1/4$. |
| Resource optimum | Optimizing batch size and network gives $\mathcal C(R)=(4+o(1))R$. |
| Attainment | Established Fourier protocols achieve the asymptotic constant. |
| Finite companion | Sharp optima for $N=2,3,4$ at $c=1/N$, including vacuum extensions. |
| Necessary structure | Near-ceiling sequences have diffuse survivor couplings and an ideal unconditional thermal number marginal of mean one. |
| Control | Equal ideal single-photon yield does not imply equal purification; the acceptance rule matters. |

Thermal number statistics concern the unconditional designated output for ideal
inputs, not the internal purity of the heralded photon. The four-photon vacuum
tap is monitored; its vacuum coupling is not unobserved loss.

## Assessment boundary

The source comparison and contribution assessment are in
[CONTRIBUTION_REVIEW.md](CONTRIBUTION_REVIEW.md) and
[the attribution map](../literature/ATTRIBUTION.md). The leading cost is a
first-order ideal resource theorem, not a clock rate, detector-footprint optimum,
full architecture cost, or prediction at fixed nonzero input error.
