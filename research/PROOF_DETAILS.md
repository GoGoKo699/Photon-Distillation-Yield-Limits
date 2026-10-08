# Proof details for the uniform yield and photon-cost limits

This supplement proves the uniform estimates used in
[THEOREM.md](THEOREM.md), under the fixed resources in
[MODEL_AND_CLAIMS.md](MODEL_AND_CLAIMS.md). The matching physical construction is
given in [OPTICAL_CONSTRUCTION.md](OPTICAL_CONSTRUCTION.md).

All error derivatives below are taken at fixed finite photon number and fixed
apparatus. Only after defining those derivatives do we vary the apparatus or
take the large-resource limit.

## 1. Independent mixed errors and accepted amplitudes

Let $`I=\{1,\ldots,N\}`$ index the occupied inputs. Write

```math
u_i=U_{0i},\qquad p_i=|u_i|^2,\qquad
\widetilde a_i^\dagger=\sum_{r\ne0}U_{ri}b_r^\dagger.
```

The designated survivor is output 0. Every unoccupied input is vacuum, so the
occupied columns are orthonormal and

```math
\sum_i p_i\le1,\qquad
[\widetilde a_i,\widetilde a_j^\dagger]=\delta_{ij}-u_i^*u_j.
```

In the detected $`(N-1)`$-photon Fock space, with all detected photons in the good
internal mode, define

```math
v_i=u_i\prod_{j\ne i}\widetilde a_j^\dagger|0\rangle,
\qquad v=\sum_i v_i.
```

Let $`P`$ project onto accepted number patterns, and set $`a_i=Pv_i`$, $`a=Pv`$.
Expanding the all-good output state by its survivor photon number shows that
$`v`$ is exactly its one-survivor detected amplitude. Hence $`p_0=\|a\|^2`$.

For an input with only photon $`i`$ in a normalized internal state orthogonal to
$`|g\rangle`$, the event that the survivor is bad leaves every detected photon
good. Its detected amplitude is $`v_i`$, and its accepted probability is
$`q_i=\|a_i\|^2`$. Internal-blind optics makes this probability independent of the
particular normalized bad state. By linearity it is also $`q_i`$ for any density
matrix $`\sigma_i`$ supported orthogonally to $`|g\rangle`$.

Let $`h_i`$ be the total herald probability with only input $`i`$ bad. For the
independent input states
$`\rho_i(\epsilon)=(1-\epsilon)|g\rangle\langle g|+\epsilon\sigma_i`$, the
herald probability $`h(\epsilon)`$ and the joint probability $`b(\epsilon)`$ of a
herald and a bad survivor satisfy

```math
\begin{aligned}
h(\epsilon)
&=(1-\epsilon)^N p_0
 +\epsilon(1-\epsilon)^{N-1}\sum_i h_i+O(\epsilon^2),\\
b(\epsilon)
&=\epsilon(1-\epsilon)^{N-1}\sum_i q_i+O(\epsilon^2).
\end{aligned}
```

The different single-error inputs are mixture alternatives and add
incoherently. Since $`p_0>0`$, division gives

```math
c=\lim_{\epsilon\to0}\frac{b(\epsilon)}{\epsilon h(\epsilon)}
=\frac{\sum_i\|a_i\|^2}{p_0}.
```

Consequently,

**(D1)**

```math
\sum_i\|a_i-a/N\|^2
=p_0(c-1/N),\qquad c\ge1/N.
```

No bound uniform in $`N`$ on either error-expansion remainder is used.

## 2. Gram reduction without inverses or factor denominators

Put $`G_{ij}=\langle v_i,v_j\rangle`$ and
$`h_E(x)=\prod_{i\in E}(1-p_i x)`$, with $`h_\varnothing=1`$.
Bosonic creation-operator overlaps are permanents of the corresponding
single-particle Gram minors. For a diagonal entry, choosing $`k`$ rank-one
columns from $`I\setminus\{i\}`$ contributes
$`(-1)^k k!`$ times their intensity product. For an off-diagonal entry, the
unmatched row and column force one rank-one factor. Choosing another $`k`$ common
indices contributes $`(-1)^{k+1}(k+1)!`$; the external factors $`u_i^*u_j`$
cancel the remaining phases. Thus

```math
\begin{aligned}
G_{ii}&=p_i\sum_{k=0}^{N-1}(-1)^k k!e_k(p_{I\setminus\{i\}}),\\
G_{ij}&=-p_i p_j\sum_{k=0}^{N-2}(-1)^k(k+1)!
 e_k(p_{I\setminus\{i,j\}}),\qquad i\ne j.
\end{aligned}
```

Using $`\int_0^\infty e^{-x}x^k\,dx=k!`$ gives the equivalent identities

**(D2)**

```math
\begin{aligned}
G_{ii}&=p_i\int_0^\infty e^{-x}h_{I\setminus\{i\}}(x)\,dx,\\
G_{ij}&=-p_i p_j\int_0^\infty xe^{-x}
 h_{I\setminus\{i,j\}}(x)\,dx,\qquad i\ne j.
\end{aligned}
```

These are polynomial identities. They apply directly to zero couplings and
singular Gram matrices, with no inverse or division by $`1-p_i x`$.

Partition $`I=A\sqcup D`$ and write

```math
f=h_A,\quad g=h_D,\quad
\sigma=\sum_Ap_i,\quad\lambda=\sum_Dp_i,\quad
v_2=\sum_Dp_i^2,\quad\omega=\frac{\lambda}{1+\lambda}.
```

For $`v_\omega=\sum_Dv_i+\omega\sum_Av_i`$, let $`Q=\|v_\omega\|^2`$.
Grouping (D2) into diagonal terms, ordered pairs within each group, and
cross-group pairs gives exactly

**(D3)**

```math
Q=\int_0^\infty e^{-x}
\left[-f(g'+xg'')-2\omega xf'g'-\omega^2g(f'+xf'')\right]dx.
```

All derivatives here are derivatives of finite products. Empty groups are
included by the convention $`h_\varnothing=1`$.

## 3. Exponential replacement and its boundary terms

Replace $`g`$ in (D3) by $`e^{-\lambda x}`$, including its derivatives, and call
the resulting integral $`Q_*`$. Put

```math
t=1+\lambda,\qquad
J_0=\int_0^\infty e^{-tx}f(x)\,dx,\qquad
J_1=\int_0^\infty xe^{-tx}f(x)\,dx.
```

Since $`f(0)=1`$ and a polynomial times $`e^{-tx}`$ vanishes at infinity,
integration by parts yields

```math
\begin{aligned}
\int_0^\infty e^{-tx}f'(x)\,dx&=tJ_0-1,\\
\int_0^\infty xe^{-tx}f'(x)\,dx&=tJ_1-J_0,\\
\int_0^\infty xe^{-tx}f''(x)\,dx&=t^2J_1-2tJ_0+1.
\end{aligned}
```

Substitution in (D3) therefore gives

**(D4)**

```math
Q_*=(\lambda-2\omega\lambda+\omega^2t)J_0
 -(\lambda-\omega t)^2J_1
=\frac{\lambda}{t}J_0.
```

The boundary constants cancel, as does the coefficient of $`J_1`$.
Let $`b_i=\sqrt{p_i/t}`$ for $`i\in A`$. Expanding the permanent, or changing
variables to $`y=tx`$ in $`J_0`$, shows that

```math
tJ_0=\mathrm{per}(I-bb^\dagger)=:p_{\emptyset}.
```

Here $`\|b\|^2=\sigma/t\le1`$. Complete this occupied-input row by a vacuum
component and then to a unitary. For one ideal photon in each occupied input,
the probability of zero photons at that output is precisely the permanent of
the detected Gram matrix $`I-bb^\dagger`$. Thus $`0\le p_{\emptyset}\le1`$ and

**(D5)**

```math
Q_* =\frac{\lambda}{(1+\lambda)^2}p_{\emptyset}.
```

This auxiliary probability justifies the sign and the upper bound. The
integrand containing $`f`$ need not be nonnegative.

## 4. A uniform error bound over the whole half-line

For $`y\ge0`$,

```math
|1-y|\le e^{y/2},\qquad
0\le e^{-y}-1+y\le y^2/2.
```

Telescoping the product $`h_E`$ against the product of $`e^{-p_i x}`$ therefore
gives, for every $`x\ge0`$,

```math
|h_E(x)-e^{-\lambda_E x}|
\le\frac{x^2}{2}\left(\sum_{i\in E}p_i^2\right)e^{\lambda_E x/2},
\qquad\lambda_E=\sum_{i\in E}p_i.
```

In particular this bounds $`g-e^{-\lambda x}`$. To bound its derivatives, use

```math
g'=-\sum_{i\in D}p_i h_{D\setminus\{i\}},\qquad
g''=\sum_{\substack{i,j\in D\\i\ne j}}
p_i p_j h_{D\setminus\{i,j\}}.
```

For $`g'`$, replacing each shorter product by its exponential contributes at
most $`\lambda v_2x^2e^{\lambda x/2}/2`$. Restoring the omitted factor in those
exponentials contributes at most $`v_2x e^{\lambda x/2}`$, by
$`1-e^{-p_i x}\le p_i x`$. For $`g''`$, the product replacement contributes at
most $`\lambda^2v_2x^2e^{\lambda x/2}/2`$. Restoring the two omitted factors
uses

```math
\sum_{i\ne j}p_i p_j(p_i+p_j)\le2\lambda v_2.
```

Finally $`\lambda^2-\sum_{i\ne j}p_i p_j=v_2`$ accounts for the missing diagonal
terms. Combining these bounds gives

**(D6)**

```math
\begin{aligned}
|g-e^{-\lambda x}|&\le v_2\frac{x^2}{2}e^{\lambda x/2},\\
|g'+\lambda e^{-\lambda x}|&\le
 v_2\left(x+\frac{\lambda x^2}{2}\right)e^{\lambda x/2},\\
|g''-\lambda^2e^{-\lambda x}|&\le
 v_2\left(1+2\lambda x+\frac{\lambda^2x^2}{2}\right)e^{\lambda x/2}.
\end{aligned}
```

The same finite-product differentiation gives
$`|f^{(r)}(x)|\le\sigma^r e^{\sigma x/2}`$ for $`r=0,1,2`$.
Since $`\sigma+\lambda\le1`$, substituting (D6) into (D3) gives

```math
|Q-Q_*|\le v_2\int_0^\infty e^{-x/2}
\left(2x+A_2x^2+A_3x^3\right)dx,
```

where

```math
A_2=\frac52\lambda+2\omega\sigma+\frac12\omega^2\sigma\le\frac52,
\qquad A_3=\frac12(\lambda+\omega\sigma)^2\le\frac12.
```

These inequalities use $`0\le\omega\le1`$ and $`\lambda+\sigma\le1`$.
The remaining integral is explicit:

**(D7)**

```math
|Q-Q_*|\le v_2\int_0^\infty e^{-x/2}
\left(2x+\frac52x^2+\frac12x^3\right)dx
=(8+40+48)v_2=96v_2.
```

This estimate includes every zero and sign change of every product factor. Its
constant is independent of photon number, output-row imbalance, and the number
of vacuum inputs.

## 5. The stable ceiling and constrained coupling

Choose $`\delta>c`$ and take $`A=\{i:p_i>\delta\}`$, $`D=A^c`$.
Then $`m=|A|\le1/\delta`$ and $`v_2\le\delta\lambda\le\delta`$.
By (D1),

```math
\left\|\sum_Aa_i\right\|^2
\le m\sum_A\|a_i\|^2\le mc p_0.
```

Since $`Pv_\omega=a-(1-\omega)\sum_Aa_i`$ and $`\|P\|\le1`$,

```math
p_0\left[1-(1-\omega)\sqrt{mc}\right]_+^2\le Q.
```

Combining this with (D5) and (D7), and weakening the denominator using
$`(1-\omega)\sqrt{mc}\le\sqrt{c/\delta}<1`$, proves

**(D8)**

```math
p_0\le\min\left\{1,
\frac{1/4+96\delta}{(1-\sqrt{c/\delta})^2}\right\}.
```

For $`0<c<1`$, set $`\delta=c^{1/3}`$. Along every sequence with $`c\to0`$,
the right side tends to $`1/4`$. The estimate is uniform over the sequence of
apparatuses; no fixed-row limit is substituted for their optimization.

More generally, under $`\sum_i p_i\le s`$ with fixed $`0<s\le1`$, replace $`1/4`$
in (D8) by $`s/(1+s)^2`$. Indeed $`\lambda\le s`$ and
$`\lambda/(1+\lambda)^2`$ is increasing on $`[0,1]`$. The construction below makes
this constrained asymptotic ceiling sharp. The endpoint $`s=0`$ admits no
positive herald probability and therefore no coefficient $`c`$ in this model.

## 6. Attainment and the infimum over batch size

For $`N\ge3`$, the Fourier construction with a monitored tap of transmissivity
$`s`$, described in [OPTICAL_CONSTRUCTION.md](OPTICAL_CONSTRUCTION.md), has
$`c=1/N`$ and ideal success

```math
P_N(s)=s\int_0^\infty e^{-x}x(1-sx/N)^{N-1}\,dx.
```

For $`0<s\le1`$, the absolute value of this integrand is at most
$`sx e^{-x/2}`$, uniformly in $`N`$. It converges pointwise to
$`sx e^{-(1+s)x}`$, so dominated convergence gives

**(D9)**

```math
P_N(s)\longrightarrow\frac{s}{(1+s)^2}.
```

Now let $`R>1`$, with the cost infimum taken over all allowed apparatuses and
integer batch sizes satisfying $`p_0>0`$ and $`c\le1/R`$.
Equation (D1) requires $`N\ge\lceil R\rceil`$ for every competitor.
Set $`t_R=R^{-1/3}`$ and choose $`\delta=t_R`$ in (D8). Since
$`\sqrt{c/\delta}\le t_R<1`$, all competitors obey

```math
p_0\le B_R:=\min\left\{1,
\frac{1/4+96t_R}{(1-t_R)^2}\right\}.
```

It follows directly, whether or not the infimum is attained, that

```math
\mathcal C(R)\ge\frac{\lceil R\rceil}{B_R}=(4-o(1))R.
```

For the upper bound, choose the Fourier protocol with $`s=1`$ and
$`N=\lceil R\rceil`$ for sufficiently large $`R`$. It has $`c=1/N\le1/R`$ and,
by (D9), $`p_0\to1/4`$. Thus

```math
\mathcal C(R)\le\frac{\lceil R\rceil}{P_{\lceil R\rceil}(1)}
=(4+o(1))R.
```

Both bounds concern the zero-error derivative and ideal success defined for
each fixed apparatus. They do not interchange the input-error limit with the
batch-size or requested-reduction limit.
