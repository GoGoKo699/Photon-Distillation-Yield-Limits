# Fourier attainment and sharp small-batch limits

The Fourier construction attains the asymptotic yield in [the theorem](THEOREM.md)
using a fixed survivor output and ordinary photon-number-resolving detection.
A monitored vacuum tap also attains the sharp two- and four-photon optima.
This note specifies its accepted records, proves its first-order coefficient,
and states the finite-size converse with its boundary conditions.

All statements use the [independent internal-error model](MODEL_AND_CLAIMS.md).
There are $N\ge2$ occupied inputs, one photon in each, and the interferometer acts
identically on every internal mode. Ideal success is denoted by $p_0$ and the
first-order output-error coefficient by $c$. The error derivative is taken at
zero input error for each fixed apparatus.

## 1. Unitary and detector rule

Index the occupied inputs and Fourier outputs by $0,\ldots,N-1$. Define

```math
\omega=e^{2\pi i/N},\qquad (F_N)_{rj}=\frac{\omega^{rj}}{\sqrt N}.
```

Add one vacuum input, indexed by $N$, and mix Fourier output zero with that
vacuum through a beam splitter of intensity transmissivity $s$, where
$0<s\le1$. A real phase convention for the beam splitter on outputs $(0,N)$ is

```math
B_s=\begin{pmatrix}\sqrt{s}&\sqrt{1-s}\\
-\sqrt{1-s}&\sqrt{s}\end{pmatrix},
\qquad U_s=B_s^{(0,N)}(F_N\oplus1).
```

Output zero is chosen as the survivor before the attempt. Its occupied-input
intensities are $p_j=|U_{0j}|^2=s/N$. Measure outputs $1,\ldots,N$, including the
tap output $N$, with ideal internal-mode-insensitive number-resolving detectors.
For a detected record $\mathbf n=(n_1,\ldots,n_{N-1},n_{\rm tap})$, accept exactly
when

**(1)**

```math
n_{\rm tap}+\sum_{r=1}^{N-1}n_r=N-1,
\qquad K(\mathbf n):=\sum_{r=1}^{N-1}r n_r\equiv0\pmod N.
```

The total count leaves exactly one photon at the predetermined survivor in
this lossless model. **The tap count may be nonzero.** Its Fourier character is
zero, so it contributes to the total count but not to $K$. The tap is a measured
output of a unitary apparatus; no photon is discarded as unobserved loss.
At $s=1$ the extra vacuum port is decoupled and may be omitted.

## 2. Accepted amplitudes erase the erroneous photon's input label

Let $u_i=U_{0i}$, and let $\widetilde a_i^\dagger$ be the part of the output
creation operator of input $i$ supported on measured ports. In the detected
$(N-1)$-photon space put

```math
v_i=u_i\prod_{j\ne i}\widetilde a_j^\dagger|0\rangle,
\qquad v=\sum_i v_i.
```

Here $v$ is the all-good one-survivor amplitude, whereas $v_i$ is the detected
all-good amplitude when input $i$ alone is erroneous and that photon survives.
Write $V_i(\mathbf n)=\langle\mathbf n|v_i\rangle$, with normalized detector Fock
states. A cyclic shift of the occupied input columns multiplies row $r$ by
$\omega^r$. The survivor and tap rows both have character zero. Therefore

**(2)**

```math
V_{i+1}(\mathbf n)=\omega^{K(\mathbf n)}V_i(\mathbf n),
```

with input labels interpreted modulo $N$. On the accepted sector all $V_i$ are
equal. Outside that sector their sum vanishes by the finite geometric sum.
Consequently every nonzero ideal one-survivor amplitude obeys (1), and the
accepted probability equals the complete ideal probability of one photon in
output zero.

Let $P$ select (1). The general amplitude identities give

```math
p_0=\|Pv\|^2,\qquad cp_0=\sum_i\|Pv_i\|^2.
```

Equation (2) implies $Pv_i=Pv/N$, and hence $c=1/N$ whenever $p_0>0$.
This uses equality of complex amplitudes, not merely probabilities. The proof
applies to every integer $N$; primality is unnecessary. It also applies to
arbitrary input-dependent bad internal states orthogonal to the shared good
mode, because the detected photons are all good in every bad-survivor term.

Some records in the accepted character sector can have zero ideal amplitude.
For any such record, $\sum_iV_i=NV_i=0$, so every bad-survivor amplitude also
vanishes. Including or removing these ideal-dark records changes neither $p_0$
nor $c$. Their contributions to finite-error heralding can differ.

## 3. Exact success and its positive domain

For ideal input photons, the survivor factorial moments are

```math
\langle(n_0)_k\rangle=(k!)^2 e_k(p_1,\ldots,p_N)
=(k!)^2\binom Nk(s/N)^k.
```

Finite factorial-moment inversion therefore gives the exact success

**(3)**

```math
P_N(s):=p_0
=\sum_{k=1}^N(-1)^{k-1}k\,k!\binom Nk(s/N)^k
=s\int_0^\infty xe^{-x}(1-sx/N)^{N-1}\,dx.
```

The integral follows by expanding the finite power and integrating each
monomial. It is an exact probability even when its integrand changes sign.

For $N\ge3$, an explicit nonzero accepted record before tapping is

```math
n_0=1,\qquad n_1=N-2,\qquad n_2=1,
```

with all other outputs empty. It has $K=N$. In its permanent, choose input $i$
for row zero and input $j\ne i$ for row two. The remaining $N-2$ repeated rows
are row one. The relevant phase sum is

```math
\sum_{i\ne j}\omega^{j-i}=-N,
```

so, after the output Fock normalization, the event probability is

**(4)**

```math
\frac{N^2(N-2)!}{N^N}>0.
```

In the tapped apparatus the same record with tap count zero has $s$ times this
probability. Thus $P_N(s)>0$ for every $N\ge3$ and $0<s\le1$.

For two inputs,

```math
P_2(s)=s(1-s).
```

An accepted event has no photon in Fourier output one and one photon at the
tap. It arises when the two photons bunch into Fourier output zero and the tap
splits them. Its success is positive for $0<s<1$. The untapped $N=2$, $s=1$
apparatus has zero success, so its conditional coefficient is undefined.
At $s=0$ the designated output has no occupied-input coupling and no positive
success is possible for any $N$.

Requiring zero photons at the tap in addition to (1) would give success
$sP_N(1)$: only the original one-photon component can then contribute. Such a
restriction would remove the two-photon success and the four-photon yield gain.

## 4. Fixed-coupling asymptotic attainment

For each fixed $0<s\le1$, the elementary bound $|1-y|\le e^{y/2}$ for $y\ge0$
implies

```math
\left|sxe^{-x}(1-sx/N)^{N-1}\right|\le xe^{-x/2}.
```

Dominated convergence in (3) gives

**(5)**

```math
P_N(s)\longrightarrow s\int_0^\infty xe^{-(1+s)x}\,dx
=\frac{s}{(1+s)^2},\qquad c=\frac1N.
```

Together with the fixed-coupling converse in [the theorem](THEOREM.md), this
proves the sharp ceiling under $\sum_i p_i\le s$. At $s=1$ it attains the quarter
yield. Choosing $N=\max\{3,\lceil R\rceil\}$ gives $c\le1/R$ and the matching
leading photon cost $(4+o(1))R$.

The Fourier circuit, character selection, and untapped asymptotic yield are
established constructions; their attribution is detailed in
[the source comparison](../literature/ATTRIBUTION.md). The purpose of (1)–(5) is
to make the physical attainment explicit in the vacuum-extended resource class.

## 5. Sharp two-, three-, and four-photon bounds

For a general allowed apparatus, the identity

```math
\sum_i\|Pv_i-Pv/N\|^2=p_0(c-1/N)
```

implies $Pv_i=Pv/N$ at $c=1/N$. If any occupied-input survivor coupling vanishes,
then $v_i=0$, so this equality forces $p_0=0$. Such boundary rows cannot attain
a positive optimum. For positive couplings, the Gram bound is

**(6)**

```math
p_0\le B_N(p):=\min_{\sum_i z_i=N}z^\dagger Gz,
\qquad G_{ij}=\langle v_i|v_j\rangle.
```

This is an upper bound even after allowing coherent detector projections.
The construction above attains the values needed below using number records.

| Input photons | Maximum success at $c=1/N$ | Attaining tap transmissivity |
|---:|---:|---:|
| 2 | $1/4$ | $s=1/2$ |
| 3 | $1/3$ | $s=1$ |
| 4 | $P_4(\eta_*)=0.262466988211219\ldots$ | $s=\eta_*=0.783216061320573\ldots$ |

For two inputs, $s=p_1+p_2$ gives

```math
B_2(p)=\frac{4p_1p_2(1-s)}s\le s(1-s)\le\frac14.
```

The positive optimum requires $p_1=p_2=1/4$. At $s=1$ the constrained Gram
minimum is zero, including its singular balanced case; at $s=0$ there is no
survivor coupling.

For three inputs, put $s=e_1(p)$, $t=e_2(p)$, $r=e_3(p)$, and $u=1-s$. Then

```math
B_3(p)=\frac{9r[u^2+2ut+2(s+1)r]}{ut+(s+3)r}
\le s-\frac43s^2+\frac23s^3\le\frac13.
```

The denominator is positive for positive couplings. The fixed-sum balancing
inequality follows from the nonnegative Schur-derivative identity in the
[two- and three-photon proof](../archive/research-handoff-2026-10-08/prior/prior/prior/PILOT.md).
The balanced value has derivative $2(s-2/3)^2+1/9>0$, so the maximum is at
$p_1=p_2=p_3=1/3$. Zero-coupling boundaries are covered by the amplitude argument
preceding (6).

For four inputs, put $s=e_1(p)$, $t=e_2(p)$, $r=e_3(p)$, and $w=e_4(p)$.
The trial vector $z_i=4/(p_i\sum_j1/p_j)$ in (6) yields

```math
B_4(p)\le U_4(p)
=\frac{16w}{r}(1-s+2t-6r)-\frac{16w^2}{r^2}(8-6s)
\le P_4(s),
```

**(7)**

```math
P_4(s)=s-\frac32s^2+\frac98s^3-\frac38s^4.
```

The last inequality is certified over the full physical domain. Sort the
couplings and write

```math
p=\frac1\Lambda(a,a+b,a+b+c,a+b+c+d),\qquad
\Lambda=4a+3b+2c+d+v,
```

with $a,b,c,d,v\ge0$. Every physical row is covered by its successive sorted
differences and $v=1-s$, for which $\Lambda=1$. For positive couplings,
$\Lambda>0$ and $r>0$. The denominator-cleared expression
$8\Lambda^{10}r^2[P_4(s)-U_4(p)]$ has exactly 613 positive integer monomials of
degree ten, listed in the
[exact coefficient certificate](../archive/research-handoff-2026-10-08/prior/prior/certificates/four_photon_positive.json).
The [global proof](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md)
gives its polynomial formula and regeneration procedure.

In particular, the terms $480a^6b^4$, $512a^6c^4$, and $480a^6d^4$ make the gap
strict for every positive unbalanced row. The remaining scalar function obeys

```math
P_4''(s)=-\frac34(6s^2-9s+4)<0.
```

Since $P_4'(0)=1$ and $P_4'(1)=-1/8$, its unique maximizer in $(0,1)$ is the root

```math
8-24\eta_*+27\eta_*^2-12\eta_*^3=0.
```

The monitored Fourier construction attains (7) at $p_i=s/4$. Therefore the
four-photon global optimum is $P_4(\eta_*)$, and every attaining apparatus has
survivor intensities $p_i=\eta_*/4$. This identifies the optimal intensity row;
it does not fix the entire interferometer or its detector implementation.
The [certificate audit](../archive/research-handoff-2026-10-08/prior/THEOREM.md)
supplies an independent integer-polynomial regeneration and exact root enclosure.

These small-batch optima concern different requested coefficients $1/N$.
They are finite-resource companions to the stable asymptotic converse, under
the same ideal first-order model.
