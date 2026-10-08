# Operational meaning of the photon-distillation limit

The [yield theorem](THEOREM.md) concerns the probability of heralding a single
photon with reduced internal-mode error. Its two relevant observables are the
heralded photon's internal state and the designated output's unconditional
photon number. They answer different questions. This note makes their relation
explicit; the detailed number-distribution calculations are in
[PHYSICAL_MECHANISM.md](PHYSICAL_MECHANISM.md), and the optical acceptance rule is
specified in [OPTICAL_CONSTRUCTION.md](OPTICAL_CONSTRUCTION.md).

## 1. What the first-order error coefficient measures

For a successful trial, let $\rho_{\mathrm{out}}(\epsilon)$ be the normalized
internal density operator of the surviving photon. Define

$$
\epsilon_{\mathrm{out}}(\epsilon)
=1-\langle g|\rho_{\mathrm{out}}(\epsilon)|g\rangle.
$$

There is exactly one survivor: the apparatus conserves photon number, starts
with exactly $N$ photons, and accepts only records containing $N-1$ detected
photons. This is a heralding conclusion, not an additional measurement of the
survivor.

Use the accepted amplitudes $a_i$ from [THEOREM.md, Section 2](THEOREM.md#2-accepted-amplitudes-constrain-purification).
At fixed apparatus, the probability that input $i$ is the only bad input is
$\epsilon+O(\epsilon^2)$. If this bad photon survives, all detected photons
occupy the good internal mode; the joint success weight is
$\epsilon\|a_i\|^2+O(\epsilon^2)$ and the survivor retains internal state
$\sigma_i$. If instead a good photon survives, the bad internal excitation is
in the detected modes. These detected sectors are orthogonal, so tracing them
cannot create coherence between $|g\rangle$ and its orthogonal complement.

Normalizing by the success probability $p_0+O(\epsilon)$ therefore gives

$$
\rho_{\mathrm{out}}(\epsilon)
=(1-c\epsilon)|g\rangle\langle g|
+\frac{\epsilon}{p_0}\sum_i\|a_i\|^2\sigma_i
+O(\epsilon^2),
\qquad
c=\frac{\sum_i\|a_i\|^2}{p_0}.
\tag{1}
$$

The remainder is in trace norm for each fixed apparatus with $p_0>0$. The
coefficient of the good-state term follows from normalization. No assumption
that different bad states are mutually orthogonal, identical, pure, or jointly
diagonal is needed: only one bad photon contributes at first order. Their
overlaps can affect higher-order terms. The common good mode need not be known
to the apparatus, which acts identically on every internal mode.

The Cauchy--Schwarz identity

$$
\sum_i\|a_i-a/N\|^2=p_0(c-1/N),\qquad a=\sum_i a_i,
\tag{2}
$$

expresses the coefficient optimum operationally. On accepted records, ideal
survivor amplitudes add coherently, whereas the independent single-error
alternatives contribute probabilities. Equality $c=1/N$ requires the accepted
amplitudes associated with each possible input origin to coincide. It is an
amplitude condition, not a claim that a detector assigns classical labels to
otherwise identical photons.

### Relation to Hong--Ou--Mandel visibility

For two independently prepared exact single photons with internal states
$\rho$ and $\rho'$, ideal balanced-beamsplitter interference gives coincidence
probability $(1-\operatorname{Tr}(\rho\rho'))/2$, hence visibility
$V=\operatorname{Tr}(\rho\rho')$. For two independent successful repetitions
of the same distillation protocol, (1) implies

$$
V_{\mathrm{out}}=1-2c\epsilon+O(\epsilon^2).
\tag{3}
$$

Two raw input photons sharing the common good mode have
$V_{\mathrm{in}}=1-2\epsilon+O(\epsilon^2)$ even when their bad states differ.
Thus $c$ is also the reduction factor for the leading visibility deficit in
this comparison. Against a perfect reference $|g\rangle$, the output visibility
is instead $1-c\epsilon+O(\epsilon^2)$; the factor two belongs to comparing two
imperfect photons.

These relations assume independent preparations and the exact single-photon,
ideal-interference setting. They do not identify an uncorrected experimental
visibility with $\epsilon$ in the presence of multiphoton or detection errors.
The connection between visibility and the independent random-source error
models is discussed in [Saied et al., Section II.2](https://arxiv.org/html/2404.14217v4).

## 2. Why the resource assumptions enter the proof

The [model statement](MODEL_AND_CLAIMS.md) fixes the protocol class. Its
assumptions have the following specific roles.

| Assumption | Role in the argument |
|---|---|
| Independent inputs with a common first-order error probability | Each single-error alternative has weight $\epsilon+O(\epsilon^2)$, giving the unweighted sum in (1). |
| Bad states orthogonal to the common good mode | Separates good and bad survivor populations and makes the detected sectors used above orthogonal. |
| Passive optics acting identically on internal modes | The same spatial amplitudes describe good photons and a single bad photon; photon number is conserved. |
| Extra inputs are vacuum | The occupied columns remain orthonormal and the survivor intensities satisfy $\sum_i p_i\le1$, with no additional photons supplied. |
| One output designated before the trial | All competitors reduce to one survivor row and its associated detector-space Gram matrix. |
| Ideal internal-insensitive number detection | The measured $N-1$ count certifies one survivor; acceptance selects spatial records without measuring internal errors directly. |

These choices describe the direct distillation operation used in
[Saied et al., Protocol III.1](https://arxiv.org/html/2404.14217v4) and
[Somhorst et al., Section II and Appendix B](https://arxiv.org/html/2601.05947v1).
The arbitrary vacuum extension enlarges the comparison beyond a square network
with every input occupied. In particular, a monitored vacuum tap is an allowed
part of the apparatus, as detailed in the
[construction](OPTICAL_CONSTRUCTION.md); its detected photons belong to the
heralding record.

The proof also bounds an enlarged mathematical class of contractions on the
detected all-good photon space. This strengthens the converse without asserting
that arbitrary coherent detector projections are physically implemented.
Internal-mode filtering, correlated source preparation, or choosing a survivor
after observing outcomes changes the resource model and is not covered by that
enlargement.

## 3. What the necessary thermal marginal says

Suppose $c_N\to0$ and $p_{0,N}\to1/4$. The theorem first forces

$$
s_N=\sum_i p_i\to1,\qquad \max_i p_i\to0.
\tag{4}
$$

Only then does the thermal interpretation follow. At ideal input
($\epsilon=0$), the designated output before conditioning has Weyl
characteristic function

$$
\chi_N(\alpha)=e^{-x/2}\prod_i(1-p_i x),\qquad x=|\alpha|^2.
\tag{5}
$$

The Gaussian vacuum factors include every input column, so their exponent uses
the full normalized row even when $s_N<1$. For diffuse occupied couplings,
the product approaches $e^{-s_Nx}$, the number-state characteristic function
of a thermal mode with mean $s_N$ after multiplication by $e^{-x/2}$.
This is the passive-mixing central-limit mechanism; see
[Becker, Datta, Lami and Rouze, Introduction and Section 2.4](https://doi.org/10.1007/s00220-021-03988-1).

The convergence here is in trace norm, not just a match of the first two
moments. To see why, write $v_2=\sum_i p_i^2$. The explicit weighted-row estimate
in [PHYSICAL_MECHANISM.md, Section 2](PHYSICAL_MECHANISM.md#2-direct-proof-for-arbitrary-diffuse-rows)
bounds the difference of each fixed number probability by $C_m v_2$.
Both the actual and thermal distributions have exact mean $s_N\le1$.
Consequently, for every fixed cutoff $K$,

$$
\|\rho_{0,N}-\tau_{s_N}\|_1
\le v_2\sum_{m=0}^K C_m+\frac{2s_N}{K+1},
\qquad
\tau_s=\sum_{m\ge0}\frac{s^m}{(1+s)^{m+1}}|m_g\rangle\langle m_g|.
\tag{6}
$$

The first term vanishes because $v_2\le s_N\max_i p_i\to0$.
Taking the network limit before sending $K$ to infinity controls the entire
number distribution, including its tail. Equation (4) then gives
$\rho_{0,N}\to\tau_1$ in trace norm.

The resulting probabilities $1/2$ for vacuum, $1/4$ for one photon, and $1/4$
for two or more photons concern the unconditional spatial output. Every photon
in these ideal-input components occupies the same good internal mode. The
mixed number marginal results from tracing other outputs; it is not an
internal-state error distribution or evidence of heating. Conditioning on a
successful record instead leaves exactly one photon, whose internal quality is
described by (1).

## 4. Why equal ideal yield does not certify purification

For the Fourier construction, compare accepting every $N-1$ count with requiring
the same count and zero total Fourier character. At ideal input, every
one-survivor event already satisfies the character condition, so the two rules
have the same success probability and unconditional number marginal.

For a uniform row $p_i=s/N$ with fixed $0<s\le1$ and positive ideal success,
the direct integrals in [PHYSICAL_MECHANISM.md](PHYSICAL_MECHANISM.md) give

$$
P_N(s)\longrightarrow\frac{s}{(1+s)^2},\qquad
A_N(s)\longrightarrow\frac{s}{1+s},\qquad
c_{\mathrm{count}}=\frac{A_N(s)}{P_N(s)}\longrightarrow1+s.
\tag{7}
$$

The character-selected rule instead has $c=1/N$. At $s=1$, count-only acceptance
therefore doubles the leading error while character selection suppresses it.
For example, the four-photon untapped network has ideal success $1/4$ under
both rules, but the respective coefficients are $17/8$ and $1/4$.
The failure of count-only selection is already discussed in
[Saied et al., Appendix D](https://arxiv.org/html/2404.14217v4).

Zero character is a necessary condition for a nonzero ideal Fourier amplitude;
it need not be sufficient. For some $N$, additional cancellations make a
zero-character pattern ideal-dark. This distinction does not spoil the
first-order result: character symmetry makes all its $a_i$ equal, and its
zero ideal amplitude gives $\sum_i a_i=0$, hence every $a_i=0$. Such a pattern
can contribute no first-order bad-survivor numerator. Adding it to an accepted
set with $p_0>0$ does not change $p_0$ or $c$, although it can affect higher-order
behavior. Accepting only ideal-dark patterns has
$p_0=0$ and lies outside the objective. The distinction between ideal patterns
and the character condition is treated in Saied et al., Theorem III.11.

## 5. Strong coupling can raise raw yield but cannot evade the converse

Consider one survivor intensity $p_1=1/2$ and $n$ others equal to $1/(2n)$.
The total mean is one, but a finite fraction of the coupling stays in one input.
Its limiting characteristic function is
$e^{-x}(1-x/2)$, rather than the thermal $e^{-3x/2}$. Laguerre inversion gives
the raw single-photon probability

$$
P_1\longrightarrow
\int_0^\infty e^{-3x/2}(1-x)(1-x/2)\,dx
=\frac8{27}>\frac14.
\tag{8}
$$

Thus a bound on raw single-photon probability alone cannot establish the
distillation theorem. Grouping the one strongly coupled input separately in
the accepted-amplitude proof gives $\lambda=1/2$, $\omega=1/3$, and

$$
Q_*=\frac13\int_0^\infty e^{-3x/2}(1-x/2)\,dx=\frac4{27}.
\tag{9}
$$

The diffuse group's squared intensities sum to $1/(4n)$, so the uniform
replacement error vanishes. The accepted-amplitude inequality becomes
$p_0[1-(2/3)\sqrt c]_+^2\le Q$, with $Q\to4/27$. Therefore any sequence of
acceptance rules on these rows with $c\to0$ has
$\limsup p_0\le4/27$. This is an upper bound for this row sequence, not an
attaining construction. The larger raw yield comes from a distribution that
the purification constraint cannot exploit at vanishing first-order error.

## 6. Order of limits and photon consumption

At each fixed apparatus, first take the derivative at $\epsilon=0$ to define
$c$, and evaluate ideal success $p_0$. The asymptotic optimization then varies
the apparatus and batch size. Independent repeated attempts consume $N/p_0$
input photons per success in this ideal limit, so the theorem's
$\mathcal C(R)=(4+o(1))R$ is a leading photon-consumption law for a requested
derivative-level error reduction $R$.

This order matters: the probability of multiple input errors and the expansion
remainder need not remain small uniformly as $N$ grows at fixed nonzero
$\epsilon$. Equations (1), (3), and (7) do not reverse those limits. The result
settles the stated static, single-survivor optimization; finite-error operation
or a different optical resource class requires a separate claim.
