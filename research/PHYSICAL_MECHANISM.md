# Why the limiting yield is one quarter

For a sequence with vanishing first-order error coefficient, approaching the
quarter yield ceiling forces a thermal number marginal in the limit. This is a
necessary consequence of the distillation bound, using established
quantum-central-limit behavior. All statements about the number distribution
refer to ideal inputs
($\epsilon=0$) and the selected output *before conditioning on the detector record*.

## 1. What an apparatus approaching the optimum must produce

The [stable theorem](THEOREM.md) proves that $c_N\to0$ and $p_{0,N}\to1/4$ require
$s_N=\sum_i p_i\to1$ and $\max_i p_i\to0$, where $p_i=|U_{0i}|^2$.
Then the unconditional survivor-mode density operator obeys

**(1)**

```math
\rho_{0,N}\longrightarrow
\tau_1=\sum_{m=0}^\infty\frac{|m_g\rangle\langle m_g|}{2^{m+1}}
\quad\hbox{in trace norm}.
```

The probabilities of zero, one, and at least two photons therefore tend to

**(2)**

```math
\Pr(n_0=0)\to\tfrac12,\qquad
\Pr(n_0=1)\to\tfrac14,\qquad
\Pr(n_0\ge2)\to\tfrac14.
```

Here $m_g$ photons occupy the same good internal mode. "Thermal" specifies the
geometric number law of a single mode, obtained by tracing the other outputs
of the pure optical state. Internal quality after heralding is determined by
the accepted error amplitudes.

For every allowed protocol, $p_0\le\Pr(n_0=1)$. At the ceiling, (2) implies

**(3)**

```math
\Pr(n_0=1)-p_0\to0,\qquad
p_0/\Pr(n_0=1)\to1.
```

Thus almost all *ideal-input probability* with exactly one survivor must be
accepted. This does not say that almost every detector pattern is accepted;
patterns with zero ideal amplitude can be essential error syndromes.
The survivor need not be measured in the protocol. Its hypothetical number law
is evaluated from the state, not supplied as an extra heralding resource.

## 2. Direct proof for arbitrary diffuse rows

The global ideal state has exactly $N$ photons. Tracing the detected modes removes
off-diagonal terms between different survivor photon numbers. Its reduced density
operator is therefore diagonal in the Fock basis.

For the Weyl characteristic function with $x=|\alpha|^2$, a single occupied input
contributes $e^{-p_ix/2}(1-p_ix)$; vacuum inputs contribute only Gaussian factors.
The full row is normalized, including its vacuum columns, so

**(4)**

```math
\chi_N(\alpha)=e^{-x/2}\prod_{i=1}^N(1-p_i x).
```

The factorization of characteristic functions under passive mixing and its
Gaussian limit are established quantum-central-limit machinery. Becker, Datta,
Lami and Rouze review the Cushen-Hudson result, with its optical $n$-splitter
interpretation and trace-norm convergence. We give the elementary fixed-Fock-input
weighted-row argument here.

Let $s=\sum_i p_i\le1$ and $v_2=\sum_i p_i^2$. The Laguerre polynomial $L_m$
and the trace-overlap formula give the exact photon probability

**(5)**

```math
P_m=\int_0^\infty e^{-x}L_m(x)\prod_i(1-p_ix)\,dx.
```

A telescoping estimate, valid on the entire half-line, is

**(6)**

```math
\left|\prod_i(1-p_ix)-e^{-sx}\right|
\le\frac{v_2x^2}{2}e^{sx/2}.
```

It follows from $|1-y|\le e^{y/2}$ and
$|1-y-e^{-y}|\le y^2/2$. No factor is assumed positive and no denominator
$1-p_ix$ is used. Substituting $e^{-sx}$ into (5) gives

```math
T_m(s)=\frac{s^m}{(1+s)^{m+1}}.
```

Using the absolute polynomial coefficients of $L_m$ and $s\le1$ yields

**(7)**

```math
|P_m-T_m(s)|\le C_m v_2,\qquad
C_m=4\sum_{k=0}^m\binom mk2^k(k+1)(k+2).
```

The exact mean of both distributions is $s$. For every fixed integer $K\ge0$,
Markov's inequality bounds the discarded number tails and gives

**(8)**

```math
\|\rho_{0,N}-\tau_s\|_1
\le v_2\sum_{m=0}^K C_m+\frac{2s}{K+1}.
```

If $\max_i p_i\to0$, then $v_2\le s\max_i p_i\to0$. First take the network
limit at fixed $K$, then let $K\to\infty$. This proves convergence to $\tau_{s_N}$.
If $s_N\to1$, continuity of the geometric probabilities proves (1).

Two useful exact identities are

**(9)**

```math
\langle n_0\rangle=s,\qquad
\langle n_0(n_0-1)\rangle=2(s^2-v_2),\qquad
\mathrm{Var}(n_0)=s+s^2-2v_2.
```

In particular a near-ceiling apparatus has ideal mean one and variance tending
to two. These are necessary number-statistics conditions, not sufficient evidence
of purification. Single-photon input errors cannot be inferred from them alone.

## 3. Same ideal success; opposite error behavior

For the standard $N$-mode Fourier matrix, keep output zero and compare two rules:

1. Accept every detector record with $N-1$ photons.
2. Require the same count and the usual zero total Fourier character.

The zero-transmission rule is inherited from the Fourier-distillation literature.
Every all-good one-survivor amplitude already has character zero. Thus both rules
have exactly the same ideal success $P_N(1)$. But errors populate the otherwise
suppressed records.

With a monitored tap of fixed transmissivity $0<s\le1$, the uniform row has
$p_i=s/N$. The tap count is included in the accepted $N-1$ total and need not
be zero; see the [optical construction](OPTICAL_CONSTRUCTION.md).
For the count-only rule, the bad-survivor numerator is

```math
A_N(s)=s\int_0^\infty e^{-x}(1-sx/N)^{N-1}\,dx,
```

whereas its ideal success is

```math
P_N(s)=s\int_0^\infty e^{-x}x(1-sx/N)^{N-1}\,dx.
```

The same global product envelope justifies dominated convergence, including
possible sign changes at large $x$. Consequently

**(10)**

```math
c_{\rm count}=\frac{A_N(s)}{P_N(s)}\longrightarrow1+s.
```

The ratios are defined only when $P_N(s)>0$. By contrast, the Fourier-character
rule has $c_{\rm Fourier}=1/N$ exactly at first order whenever this condition
holds (in particular for $N\ge3$, $0<s\le1$). At $s=1$, the count-only rule
tends to *twice* the input error,
while the properly selected rule suppresses that coefficient to zero. Both have
ideal success tending to $1/4$ and the same unconditional thermal number limit.

Exact finite controls:

| $N$ | tap $s$ | same ideal success | count-only $c$ | character-selected $c$ |
|---:|---:|---:|---:|---:|
| 2 | $1/2$ | $1/4$ | $3/2$ | $1/2$ |
| 3 | $1$ | $1/3$ | $5/3$ | $1/3$ |
| 4 | $1$ | $1/4$ | $17/8$ | $1/4$ |
| 4 | $4/5$ | $164/625$ | $74/41$ | $1/4$ |

The [four-photon derivation](../archive/research-handoff-2026-10-08/prior/prior/prior/PILOT.md)
also gives the tapped-four-photon countercontrol.
Saied et al., Appendix D, already report error amplification approaching twice the
input error when all one-survivor patterns are accepted, including numerical
checks for the Fourier case. This failure mechanism is therefore inherited.
The explicit uniform-row integral and weighted-row interpretation above are
checked against a separate Fock expansion for the finite examples. Selecting
Fourier-compatible detector records is essential; treating every single-survivor
event as purified is incorrect.

## 4. Why the central limit theorem alone is not the converse

A port with a macroscopic coupling need not be thermal. Consider one input with
$p_1=1/2$ and $n$ inputs with $p_i=1/(2n)$. Its mean remains one, but (4) approaches
$e^{-x}(1-x/2)$ rather than $e^{-3x/2}$. Formula (5) gives

```math
\Pr(n_0=1)\longrightarrow\frac8{27}>\frac14.
```

This is a raw one-photon probability, not a distillation success. The accepted-
amplitude constraint prevents using the strongly coupled photon to maintain a
vanishing error coefficient at that yield. In fact the grouped norm in the
stable proof has $\lambda=1/2$, $\omega=1/3$, and limiting upper bound
$Q_* =4/27$ for any vanishing-$c$ acceptance rule with this sequence of rows.

The essential order of reasoning is therefore: first constrain purification's
accepted amplitudes for all networks; then infer diffuse rows for networks
approaching the optimum; only then interpret the quarter through thermal
number statistics. Assuming thermal behavior at the outset would omit the
strongly coupled competitors the theorem must exclude.

## 5. Matching the minimum cost imposes additional equality conditions

Take a sequence of target improvements $R\to\infty$, with $c\le1/R$, for which
$N/(Rp_0)\to4$. Since $N/R\ge1$ and $\limsup p_0\le1/4$,

**(11)**

```math
\frac NR\to1,\qquad p_0\to\frac14,\qquad Nc\to1.
```

Together with the exact amplitude identity,

**(12)**

```math
\frac N{p_0}\sum_i\|a_i-a/N\|^2=Nc-1\to0.
```

Thus a leading-cost-optimal protocol must asymptotically use the smallest allowed
batch and saturate input-origin erasure in this normalized mean-square sense.
Yield optimality alone did not require $Nc\to1$. Equation (12) is not a separate
per-input relative convergence assertion.

The [physical interpretation details](PHYSICAL_INTERPRETATION.md) connect the
coefficient to a conditional internal-state observable and two-copy visibility,
and explain the role of each apparatus hypothesis.

## Verification

The [physical-mechanism checker](../archive/research-handoff-2026-10-08/check_consolidation.py)
evaluates complete number distributions using exact rational recursion, compares
them with a distinct factorial-moment expansion and direct normalized Fock
amplitudes, verifies the characteristic and moment identities, and checks the
count-only/character-selected comparison with explicit bad photons. Its largest
optical matrix is $6\times6$; the largest full occupation list has 252 entries.
Exact scalar rational recursions evaluate number distributions through 128 inputs.

These derivations interpret the stable distillation bound within its stated
resources and first-order qualification. The thermalization principle, Fourier
suppression law, and Fourier single-photon success constant are inherited.
