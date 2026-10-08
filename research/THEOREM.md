# A stable yield limit for passive photon-indistinguishability distillation

## Physical question and result

How many imperfect photons must a passive network consume to herald one photon
whose first-order distinguishability error is reduced by a large factor? Fourier
protocols already achieve approximately four photons per unit of reduction.
The contribution here is the matching converse, including unbalanced networks,
arbitrary vacuum inputs, and purification coefficients that vanish without
saturating the best coefficient at each batch size.

For the class specified below, write $p_0$ for ideal-input success and $c$ for the
first-order output-error coefficient. Then

$$
c_N\to0\quad\Longrightarrow\quad\limsup p_{0,N}\le\frac14.
\tag{T1}
$$

The known Fourier sequence has $c_N=1/N$ and $p_{0,N}\to1/4$. If $R$ is a requested
first-order error-reduction factor, optimizing both batch size and apparatus gives

$$
\mathcal C(R):=\inf_{c\le1/R}\frac{N}{p_0}=(4+o(1))R.
\tag{T2}
$$

Every sequence with vanishing first-order error coefficient and success
approaching the quarter ceiling must also approach a thermal photon-number
marginal of mean one at the selected output before conditioning. The
[physical mechanism account](PHYSICAL_MECHANISM.md) explains this necessary
structure and distinguishes number statistics from internal-mode purification.

## 1. Operational contract

At each fixed finite $N\ge2$, prepare one photon in each of $N$ occupied spatial
inputs. Their independent internal states are

$$
\rho_i(\epsilon)=(1-\epsilon)|g\rangle\langle g|+\epsilon\sigma_i,
\qquad \operatorname{supp}\sigma_i\perp |g\rangle.
$$

The same target mode $|g\rangle$ is shared. The single-error analysis is independent
of whether distinct errors share a bad mode. Higher-order terms need not be.
A fixed passive unitary acts identically on every internal mode. Additional inputs
may be vacuum. One spatial output is designated before the attempt; every other
output is measured by ideal photon-number-resolving, internal-mode-insensitive
detectors. Accepted records contain $N-1$ measured photons. No loss, added
nonvacuum resources, internal-mode filters, intermediate adaptation, or
outcome-dependent choice of retained output is allowed.

Define $\epsilon_{\rm out}=1-\langle g|\rho_{\rm out}|g\rangle$ for the
conditional single-photon internal state. For each fixed apparatus, with $p_0>0$,

$$
p_{\rm herald}(\epsilon)=p_0+O(\epsilon),\qquad
\epsilon_{\rm out}=c\epsilon+O(\epsilon^2).
$$

The derivative is taken at zero error first. The large-$N$ or large-$R$ limit is
taken afterward. No uniform finite-$\epsilon$ remainder is asserted. Independent
repeated attempts cost $N/p_0$ photons in this ideal limit, including rejected
batches. Source-generation overhead, loss, clock rate, and detection footprint
are different resources and are not inferred from this cost.

## 2. Accepted amplitudes constrain purification

Let $u_i=U_{0i}$, $p_i=|u_i|^2$, and
$\widetilde a_i^\dagger=\sum_{r\ne0}U_{ri}b_r^\dagger$. The $N$ occupied columns
are orthonormal, so $p_i\ge0$ and $\sum_i p_i\le1$. In the detected
$(N-1)$-photon Fock space define

$$
v_i=u_i\prod_{j\ne i}\widetilde a_j^\dagger|0\rangle,\qquad
v=\sum_i v_i.
$$

Let $P$ select accepted number patterns, and put $a_i=Pv_i$, $a=Pv$.
The all-good input has one-photon survivor amplitude $v$. When input $i$ alone is
bad and survives, the detected photons are all good, with amplitude $v_i$.
Thus

$$
p_0=\|a\|^2,\qquad cp_0=\sum_i\|a_i\|^2,
\qquad
\sum_i\|a_i-a/N\|^2=p_0(c-1/N).
\tag{1}
$$

In particular $c\ge1/N$. At equality, all accepted amplitudes $a_i$ coincide.
The coefficient optimum is established in the literature; (1) gives a direct
vacuum-extended formulation. The stable converse does not assume equality.
Allowing a general detector-space contraction only enlarges the comparison class.
It does not assert that arbitrary coherent projections are physically available.

The complete optical Gram matrix depends only on the survivor intensities:

$$
G_{ii}=p_i\sum_{k=0}^{N-1}(-1)^k k!e_k(p_{\setminus i}),\qquad
G_{ij}=-p_ip_j\sum_{k=0}^{N-2}(-1)^k(k+1)!e_k(p_{\setminus i,j}).
\tag{2}
$$

This follows by expanding permanents of minors of $I-u^*u$. The original
creation-operator proof and independent Fock checks are preserved in
[the initial pilot](../archive/research-handoff-2026-10-08/prior/prior/prior/PILOT.md).

## 3. The uniform bound over arbitrary output rows

Choose $\delta>c$. Put $A=\{i:p_i>\delta\}$ and $D=A^c$, and define

$$
m=|A|\le1/\delta,\quad \sigma=\sum_Ap_i,\quad
\lambda=\sum_Dp_i,\quad v_2=\sum_Dp_i^2\le\delta,
\quad \omega=\frac\lambda{1+\lambda}.
$$

Consider the unnormalized detector vector
$v_\omega=\sum_Dv_i+\omega\sum_Av_i$, with squared norm $Q$.
For $f(x)=\prod_A(1-p_ix)$ and $g(x)=\prod_D(1-p_ix)$, expansion of (2) gives

$$
Q=\int_0^\infty e^{-x}
\{-f(g'+xg'')-2\omega xf'g'-\omega^2g(f'+xf'')\}\,dx.
\tag{3}
$$

Replacing $g$ by $e^{-\lambda x}$ and integrating by parts gives

$$
Q_* =\frac{\lambda}{1+\lambda}
\int_0^\infty e^{-(1+\lambda)x}f(x)\,dx
=\frac{\lambda}{(1+\lambda)^2}p_{\emptyset}.
\tag{4}
$$

Here $p_{\emptyset}=\operatorname{per}(I-bb^\dagger)$ with
$b_i=\sqrt{p_i/(1+\lambda)}$ for $i\in A$. Since $\|b\|^2\le1$, this is an
actual zero-photon probability for an auxiliary passive optical port. Thus
$0\le p_{\emptyset}\le1$. The integrand itself can have either sign. The
auxiliary probability is a mathematical bound, not an added optical resource.

For every $x\ge0$, telescoping the products and differentiating the finite
products gives

$$
|g-e^{-\lambda x}|\le v_2(x^2/2)e^{\lambda x/2},
$$
$$
|g'+\lambda e^{-\lambda x}|\le v_2(x+\lambda x^2/2)e^{\lambda x/2},
$$
$$
|g''-\lambda^2e^{-\lambda x}|\le
v_2(1+2\lambda x+\lambda^2x^2/2)e^{\lambda x/2}.
$$

Use $|1-y|\le e^{y/2}$ and $0\le e^{-y}-1+y\le y^2/2$ for $y\ge0$,
plus $|f^{(r)}|\le\sigma^r e^{\sigma x/2}$, $r\le2$. The complete replacement
error is bounded by

$$
|Q-Q_*|\le v_2\int_0^\infty e^{-x/2}
(2x+\tfrac52x^2+\tfrac12x^3)\,dx=96v_2.
\tag{5}
$$

This estimate includes all zeros and sign changes of the factors, with no division
by them. It is uniform in $N$, row imbalance, and the number of empty ports.
The [proof details](PROOF_DETAILS.md) give the mixed-error reduction, complete
telescoping and integration-by-parts algebra, and uniform cost-infimum argument.
The [original stable proof](../archive/research-handoff-2026-10-08/prior/THEOREM.md)
is preserved unchanged.

## 4. Stable converse and sharpness

By (1), $a_A=\sum_Aa_i$ has norm at most $\sqrt{mc p_0}$. Since
$Pv_\omega=a-(1-\omega)a_A$, the triangle inequality yields

$$
p_0[1-(1-\omega)\sqrt{mc}]_+^2\le Q.
$$

Combining (4)-(5), $\lambda\le1$, and $m\le1/\delta$ gives

$$
p_0\le\min\left\{1,
\frac{1/4+96\delta}{(1-\sqrt{c/\delta})^2}\right\},\qquad\delta>c.
\tag{6}
$$

For $c\to0$, use $\delta=c^{1/3}$. This proves T1. The constant 96 is a coarse
uniformity certificate, not a useful small-batch engineering estimate.

The Fourier protocol and its ideal success approaching $1/4$ are inherited from
Saied et al., Theorem III.5. Its suppression of the coefficient to $1/N$ supplies
a matching sequence. For T2, $c\le1/R$ requires $N\ge R$ by (1), and (6) bounds
all such competitors uniformly. The Fourier protocol with $N=\max(3,\lceil R\rceil)$
attains the leading cost. The approximately $4N$ attainable cost is already in
Saied et al., Theorem III.9; the lower bound over all networks and batch sizes is
the added implication.

## 5. Necessary form of a near-optimal apparatus

If $c_N\to0$ and $p_{0,N}\to1/4$, then

$$
s_N:=\sum_i p_i\to1,\qquad\max_i p_i\to0.
\tag{7}
$$

If $s_N\le s<1$ on a subsequence, (4)-(6) give an upper limit
$s/(1+s)^2<1/4$. If some $p_i\ge a>0$, then $\lambda\le1-a$ for vanishing
$\delta$, giving upper limit $(1-a)/(2-a)^2<1/4$. These contradictions prove (7).
Exact balance is not necessary; many individually weak contributions are.

For fixed $0<s\le1$ under the constraint $\sum_i p_i\le s$, the sharp
asymptotic ceiling is $s/(1+s)^2$, attained by a Fourier output with a monitored
tap of transmissivity $s$. The tap may register photons; its count contributes
to the accepted total $N-1$. The [optical construction](OPTICAL_CONSTRUCTION.md)
specifies the acceptance rule and proves positive success for all $N\ge3$.
The zero-coupling endpoint has no positive-success protocol, as explained in the
[scientific audit](SCIENTIFIC_AUDIT.md).

The [mechanism note](PHYSICAL_MECHANISM.md) translates (7) into trace-norm
convergence of the unconditional survivor marginal to a mean-one thermal number
state and derives the complementary need for the detector selection rule.

## 6. Sharp finite-resource companion

At the exactly optimal coefficient $c=1/N$, the known achieving circuits and the
preserved all-network converses give

| $N$ | Maximum ideal success | Ideal mean input consumption |
|---:|---:|---:|
| 2 | $1/4$ | $8$ |
| 3 | $1/3$ | $9$ |
| 4 | $P_4(\eta_*)$ | $4/P_4(\eta_*)$ |

Here

$$
P_4(\eta)=\eta-\tfrac32\eta^2+\tfrac98\eta^3-\tfrac38\eta^4,
\qquad 8-24\eta_*+27\eta_*^2-12\eta_*^3=0,
$$

with the unique root in $(0,1)$,
$\eta_*=0.783216061320573\ldots$ and
$P_4(\eta_*)=0.262466988211219\ldots$.
A Fourier network with one monitored vacuum tap attains it. An exact degree-ten
polynomial with 613 positive monomials certifies the converse; an independent
integer implementation verifies every coefficient and the equality condition
$p_i=\eta_*/4$. The full network is not uniquely fixed by that condition.
See [global proof](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md) and [independent audit](../archive/research-handoff-2026-10-08/prior/THEOREM.md).

The targets differ between rows. This is not a comparison at common final purity.
No exact optimum for all $N\ge5$ is asserted.

## Contribution and scope

The central claim is the stable all-network cost limit. The thermal marginal is
its physical interpretation and necessary consequence, not a new central limit
theorem. The four-photon certificate is a finite-size companion. All claims use
the fixed-output, ideal first-order resource class stated in Section 1.

The [contribution assessment](CONTRIBUTION_REVIEW.md) separates the converse from
known attaining constructions and records the source-reading boundaries. The
proofs and [reproducibility checks](../VERIFICATION.md) are author-side evidence;
they do not constitute independent proof review, exhaustive priority clearance,
or a hardware-performance guarantee. Detailed original derivations remain in the
[research archive](../archive/README.md).
