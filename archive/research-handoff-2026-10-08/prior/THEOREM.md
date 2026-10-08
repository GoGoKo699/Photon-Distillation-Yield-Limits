# A stable success ceiling for first-order photon purification

**8 October 2026 — focused review of the independent distillation-yield candidate.**

## Main conclusion and status

The preceding all-network theorem and exact four-photon optimum survive the present
author-side audit. The new conclusion removes a potential fragility: the asymptotic
quarter-success ceiling does not require the first-order error coefficient to equal
its optimum exactly.

For any sequence of the protocols below, with ideal heralding probabilities
$p_{0,N}>0$ and first-order output-error coefficients $c_N$,

$$
c_N\longrightarrow0
\quad\Longrightarrow\quad
\limsup_{N\to\infty}p_{0,N}\le\frac14.
\tag{A}
$$

The known Fourier protocols attain $c_N=1/N$ and $p_{0,N}\to1/4$. Thus this is a
sharp asymptotic ceiling even when the required error suppression is weaker than
optimal by a growing factor, provided its coefficient still tends to zero.

Equivalently, if $R$ is a requested first-order reduction factor, and the batch
size and network are both optimized, the least ideal-limit mean input consumption is

$$
\boxed{\mathcal C(R)=(4+o(1))R\qquad(R\to\infty).}
\tag{B}
$$

The definition of $\mathcal C$ and order of limits are stated below. Neither (A) nor
(B) describes fixed-nonzero-error or lossy hardware performance.

This is an addition to, not a silent replacement of, the preceding checkpoint.
The old theorem was restricted to $c_N=1/N$ and expressly left coefficient
stability unresolved. Its complete source and reports remain unchanged in `prior/`.
The new argument is a short consequence of the audited grouped-Gram bound once
exact amplitude equality is replaced by an inequality for accepted heavy-input
amplitudes. No new optical resource is introduced.

## 1. Resources and definitions

For every finite $N$, prepare $N$ independent single photons, one in each occupied
spatial input. Their internal density matrices have target component $|g\rangle$
with probability $1-\epsilon$ and a component orthogonal to it with probability
$\epsilon$. At first order only one erroneous input occurs, so whether multiple
erroneous photons would occupy the same or different bad modes is irrelevant to
$c_N$ but can matter at finite $\epsilon$.

A predetermined passive interferometer acts identically on each internal mode.
Arbitrarily many additional inputs may be vacuum. Retain one output chosen before
the attempt and measure all others with ideal number-resolving detectors which do
not resolve internal modes. Accepted patterns contain $N-1$ detected photons.
No intermediate adaptation, extra nonvacuum inputs, internal-mode filtering, loss,
or outcome-dependent survivor choice is included.

For a fixed network and acceptance rule,

$$
p_{\rm herald}(\epsilon)=p_0+O(\epsilon),\qquad
\epsilon_{\rm out}=c\epsilon+O(\epsilon^2),\qquad p_0>0.
$$

The expansion is at fixed $N$ and fixed apparatus. Its remainder need not be
uniform as $N$ grows. The ideal-limit mean photon consumption for independently
repeated attempts is $N/p_0$; rejected attempts consume all $N$ input photons.
Source-production costs, clock rates, and loss are not inferred from it.

The success ceiling is not a universal finite-batch bound: $N=3$, $c=1/3$ can
have success $1/3$. Nor does it exclude routing one input straight to the output:
that has $p_0=1$ but $c=1$.

The input model, Fourier purification, its $1/N$ coefficient, and its attainable
success approaching $1/4$ are established [S26, SMAR25, M22]. The subject of this
record is the converse over unbalanced and vacuum-extended apparatuses, and its
stability under less-than-optimal first-order suppression.

## 2. Detector amplitudes, without assuming optimal error suppression

Write $u_i=U_{0i}$, $p_i=|u_i|^2$, and
$\widetilde a_i^\dagger=\sum_{r\ne0}U_{ri}b_r^\dagger$ for the detected part of
the output of occupied input $i$. Unitarity gives $\sum_i p_i\le1$.

In the $(N-1)$-photon detected-mode space define

$$
v_i=u_i\prod_{j\ne i}\widetilde a_j^\dagger|0\rangle,\qquad
v=\sum_i v_i.
$$

For accepted number patterns represented by $P$, set $a_i=Pv_i$, $a=\sum_i a_i$.
Exactly,

$$
p_0=\|a\|^2,\qquad cp_0=\sum_i\|a_i\|^2.
\tag{1}
$$

The first identity concerns all-good inputs. In the second, input $i$ is the
sole erroneous photon and survives, so the detected photons are all in the
target mode. The first-order mixture sums these mutually exclusive error
alternatives incoherently.

Cauchy gives

$$
cp_0-\frac{p_0}{N}
=\sum_i\|a_i-a/N\|^2\ge0,\qquad c\ge1/N.
\tag{2}
$$

At equality, every $a_i=a/N$; this is the earlier optimal-coefficient condition.
The present proof uses (1), not that equality. All norm bounds also hold for a
detector-space contraction. This is an upper-bound relaxation, not an asserted
implementation of arbitrary coherent detector projections.

The Gram entries, obtained by expanding the bosonic permanents, remain

$$
G_{ii}=p_i\sum_{k=0}^{N-1}(-1)^k k! e_k(p_{\setminus i}),\quad
G_{ij}=-p_ip_j\sum_{k=0}^{N-2}(-1)^k(k+1)! e_k(p_{\setminus i,j}).
\tag{3}
$$

Thus the full optical interferometer enters this converse only through its
survivor-row intensities. The creation-operator derivation is preserved in
`prior/prior/PILOT.md`; the review independently checks the amplitudes using
repeated-row permanents in normalized Fock states.

## 3. The audited heavy/light bound

Choose any $\delta>0$. Define the strongly coupled set
$A=\{i:p_i>\delta\}$ and its complement $D$. Put

$$
m=|A|,\quad \sigma=\sum_Ap_i,\quad\lambda=\sum_Dp_i,\quad
v_2=\sum_Dp_i^2.
$$

Then $m\le1/\delta$, $\sigma+\lambda\le1$, and $v_2\le\delta\lambda\le\delta$.
Set $\omega=\lambda/(1+\lambda)$ and form the unnormalized vector

$$
v_\omega=\sum_Dv_i+\omega\sum_Av_i,\qquad Q=\|v_\omega\|^2.
$$

The preceding proof establishes, uniformly over all rows and all vacuum extensions,

$$
Q\le\frac{\lambda}{(1+\lambda)^2}p_{\emptyset}+96v_2,
\qquad 0\le p_{\emptyset}\le1.
\tag{4}
$$

For clarity, the complete input to that estimate is reproduced here. With

$$
f(x)=\prod_A(1-p_ix),\qquad g(x)=\prod_D(1-p_ix),
$$

the exact grouped Gram integral is

$$
Q=\int_0^\infty e^{-x}
[-f(g'+xg'')-2\omega xf'g'-\omega^2g(f'+xf'')]\,dx.
\tag{5}
$$

Replacing $g$ and its derivatives by those of $e^{-\lambda x}$ gives

$$
Q_*=\frac{\lambda}{1+\lambda}
\int_0^\infty e^{-(1+\lambda)x}f(x)\,dx
=\frac{\lambda}{(1+\lambda)^2}p_{\emptyset}.
\tag{6}
$$

The last equality identifies

$$
p_{\emptyset}=\operatorname{per}(I-bb^\dagger),\qquad
b_i=\sqrt{p_i/(1+\lambda)}\quad(i\in A).
$$

Since $\|b\|^2=\sigma/(1+\lambda)\le1$, this is the probability for zero photons
in one port of a valid auxiliary passive scattering problem. The integrand need
not be positive: its probability interpretation is essential. No auxiliary
thermal or nonvacuum state is given to the purification protocol.

The uniform replacement follows from $|1-y|\le e^{y/2}$ and
$0\le e^{-y}-1+y\le y^2/2$ for $y\ge0$. Telescoping products yields

$$
|g-e^{-\lambda x}|\le v_2(x^2/2)e^{\lambda x/2},
$$

$$
|g'+\lambda e^{-\lambda x}|
\le v_2(x+\lambda x^2/2)e^{\lambda x/2},
$$

$$
|g''-\lambda^2e^{-\lambda x}|
\le v_2(1+2\lambda x+\lambda^2x^2/2)e^{\lambda x/2}.
$$

Also $|f^{(r)}|\le\sigma^r e^{\sigma x/2}$ for $r=0,1,2$.
Substitution into (5) gives an error integrable over the full half-line,

$$
|Q-Q_*|\le v_2\int_0^\infty e^{-x/2}
(2x+\tfrac52x^2+\tfrac12x^3)\,dx=96v_2.
\tag{7}
$$

The coefficients before bounding them are
$5\lambda/2+2\omega\sigma+\omega^2\sigma/2\le5/2$ and
$(\lambda+\omega\sigma)^2/2\le1/2$.
There is no division by a factor $1-p_ix$, so zeros of those factors cause no
gap. The boundary terms in the integration by parts leading to (6) are retained.

This is the same uniform estimate as the earlier theorem. It has not been
weakened or made conditional on numerical convergence.

## 4. A stable ceiling: exact amplitude erasure is unnecessary

The accepted grouped vector is

$$
Pv_\omega=a-(1-\omega)a_A,\qquad a_A=\sum_{i\in A}a_i.
$$

Equation (1) gives

$$
\|a_A\|\le\sqrt{m\sum_A\|a_i\|^2}\le\sqrt{mc\,p_0}.
$$

Triangle inequality and $\|P\|\le1$ therefore imply

$$
p_0[1-(1-\omega)\sqrt{mc}]_+^2\le Q.
\tag{8}
$$

This is the new step. No $c=1/N$ equality is used, and no trial-vector
normalization proportional to $N$ is needed.

Because $\omega\ge0$, $m\le1/\delta$, and
$\lambda/(1+\lambda)^2\le1/4$, (4) gives the all-protocol bound

$$
\boxed{
p_0\le\min\left\{1,
\frac{1/4+96\delta}{[1-\sqrt{c/\delta}]^2}\right\},
\qquad \delta>c.
}
\tag{9}
$$

For $0<c<1$, choose $\delta=c^{1/3}$:

$$
p_0\le\min\left\{1,\frac{1/4+96c^{1/3}}{(1-c^{1/3})^2}\right\}.
\tag{10}
$$

Consequently, for any sequence with $c_N\to0$,

$$
\limsup p_{0,N}\le1/4.
$$

The constants are coarse. Equation (10) is not a competitive finite-size
engineering estimate. Its role is to control the joint optimization uniformly,
rather than take the limit of a fixed row. The conclusion covers, for example,
$c_N=2/N$, $c_N=N^{-1/2}$, or arbitrarily slow vanishing $c_N$.

For comparison, a finer equality-defect calculation remains available. For any
$\sum_i z_i=N$, equation (2) gives

$$
p_0\left[1-\|z-\mathbf1\|_2\sqrt{c-1/N}\right]_+^2\le z^\dagger Gz.
$$

At $c=1/N$ it recovers the exact earlier bound. This identity is checked but is
not needed for the simpler universal proof above.

## 5. An exact asymptotic photon-cost optimization

Let $R>1$ be the desired first-order improvement factor and define

$$
\mathcal C(R)=
\inf_{\substack{N\ge2,\ {\rm allowed\ protocol}\\p_0>0,\ c\le1/R}}
\frac{N}{p_0}.
\tag{11}
$$

Batch size is part of the optimization. The constraints and cost are still
ideal-input/first-order quantities, not finite-$\epsilon$ performance.

From (2), $N\ge1/c\ge R$. The uniform bound (9), with
$\delta=R^{-1/3}$, applies to every competitor and gives
$p_0\le1/4+O(R^{-1/3})$. Therefore

$$
\mathcal C(R)\ge(4-o(1))R.
$$

Take the known Fourier purifier with $N=\max\{3,\lceil R\rceil\}$:
$c=1/N\le1/R$ and $p_0=P_N(1)\to1/4$. It gives
$\mathcal C(R)\le(4+o(1))R$, proving (B).

Thus allowing more input photons while accepting a suboptimal error coefficient
cannot improve the leading photon cost for a requested large first-order
improvement. The Fourier achieving cost and error scaling are inherited; the
uniform lower bound over this enlarged choice of $N$ is the corollary here.

The order is always: define the derivative at $\epsilon=0$ for each fixed
apparatus, then take the requested reduction $R$ large. The result does not
interchange those limits or control its second-order error remainder.

## 6. What approaching the ceiling requires

The proof gives necessary properties of any sequence with $c_N\to0$ and
$p_{0,N}\to1/4$. Let $s_N=\sum_i p_i$. Then

$$
\boxed{s_N\to1,\qquad \max_i p_i\to0.}
\tag{12}
$$

Indeed, if $s_N\le s<1$ along a subsequence, (4) and (8) give
$\limsup p_0\le s/(1+s)^2<1/4$. If some $p_i\ge a>0$ along a subsequence,
choose the vanishing threshold in (10). That input is in $A$, so
$\lambda\le1-a$ and

$$
\limsup p_0\le\frac{1-a}{(2-a)^2}
=\frac14-\frac{a^2}{4(2-a)^2}<\frac14.
$$

These properties do not require exactly equal $p_i=1/N$, nor do they guarantee
that an arbitrary accepted-pattern rule purifies.

More generally, if occupied-input coupling to the survivor is constrained by
$\sum p_i\le s$ for fixed $0<s\le1$, the sharp asymptotic success under
$c_N=1/N$ (and the ceiling under any $c_N\to0$) is

$$
\frac{s}{(1+s)^2}.
\tag{13}
$$

The lower limit is achieved by the known Fourier network with a monitored
vacuum tap of transmissivity $s$. This follows from

$$
P_N(s)=s\int_0^\infty e^{-x}x(1-sx/N)^{N-1}\,dx
\longrightarrow\frac{s}{(1+s)^2}.
$$

Here $1-s$ is unused occupied-input norm in the selected output row, not
unobserved photon loss. All other outputs, including the tap, are measured.

The factor $s/(1+s)^2$ is also the one-photon probability of a geometric/thermal
number distribution of mean $s$. It provides a useful interpretation of the
many-weak-coupling limit, not a new thermal input resource. The nontrivial
converse shows why retaining strongly coupled inputs cannot bypass that
limit while making the first-order bad-survivor coefficient vanish.

## 7. Four photons: certificate audit and equality cases

The previous optimum remains

$$
p_4^\star=P_4(\eta_*),\quad
P_4(s)=s-\tfrac32s^2+\tfrac98s^3-\tfrac38s^4,
$$

where $\eta_*$ is the unique root in $(0,1)$ of
$8-24s+27s^2-12s^3=0$. Its higher-precision values are

$$
\eta_*=0.78321606132057325424704180384677\ldots,
$$

$$
p_4^\star=0.26246698821121936438896802380397\ldots.
$$

The prior decimal optimizer output was accurate to floating-point precision,
not an exact enclosure. A new attempted rational interval around those old
digits missed the root. It was replaced by endpoints checked using exact
polynomial signs; no objective or theorem changed. The failed new driver and
endpoint patch are retained.

The 613-term degree-ten certificate was regenerated in this review by an
independent sparse integer-polynomial implementation, without relying on the
earlier SymPy expansion. Every coefficient and monomial agrees.

Its terms include

$$
480a^6b^4,\quad512a^6c^4,\quad480a^6d^4,
$$

where $a$ is the smallest positive sorted intensity numerator and $b,c,d$ its
successive differences. Consequently the certificate is strictly positive
whenever all occupied survivor couplings are nonzero and any two are unequal.
The zero-coupling cases cannot have positive yield at coefficient $1/4$.
Therefore attaining the four-photon optimum requires

$$
p_1=p_2=p_3=p_4=\eta_*/4.
$$

This is uniqueness of the optimal survivor intensity row, not uniqueness of the
entire interferometer or detector implementation. The Fourier-plus-monitored-tap
network attains it.

## 8. Attribution and what remains to assess

[S26] proves the optimal first-order coefficient for the stated $N$-mode
unitaries, and Section II explicitly distinguishes the unresolved success
question. [SMAR25, Theorems III.5 and III.9] supplies the uniform-row Fourier
success limit and its approximately $4N$ achieving cost. They are not new values
discovered here.

The candidate additional implication is the converse for arbitrary rows and
vacuum extensions, now stable under any vanishing first-order coefficient.
The four-photon all-network certificate is a finite-batch companion, not a
second project. No finite-$N\ge5$ optimizer is claimed.

The source review in `REVIEW.md` grants all inherited tools and constructions.
It has not identified a directly covering all-row ceiling in the passages
inspected. This is not exhaustive priority clearance or independent proof
review.

The scope remains passive, independent-input, one predetermined survivor,
internal-mode-insensitive counting, and first-order. Correlated input errors,
adaptive survivor routing, additional photons, finite-error uniformity, detector
loss, and architectural fault-tolerance overheads are not consequences of these
formulas.

## Sources

[S26] F. H. B. Somhorst et al., *Below-threshold error reduction in single photons
through photon distillation*, arXiv:2601.05947v1,
https://arxiv.org/html/2601.05947v1 .
Section II and Appendix B were reread. The public version record returned v1.

[SMAR25] J. Saied, J. Marshall, N. Anand, E. G. Rieffel, *General protocols for
the efficient distillation of indistinguishable photons*, Phys. Rev. Applied 23,
034079 (2025), arXiv:2404.14217v4,
https://arxiv.org/pdf/2404.14217v4 .
Theorem III.5 explicitly assumes a uniformly coupled first row; Theorem III.9
gives the achieving cost with its small-error qualification. Relevant
finite-error/optimization and discussion passages were read in the primary PDF.
The current public version record returned v4.

[M22] J. Marshall, *Distillation of Indistinguishable Photons*, Phys. Rev. Lett.
129, 213601 (2022), arXiv:2203.15197.
The three-photon achieving construction is credited via the prior reading record;
no fresh independent reading of its entire paper is claimed here.

[H25] F. Hoch et al., *Optimal distillation of photonic indistinguishability*,
arXiv:2509.02296,
https://arxiv.org/pdf/2509.02296 .
The protocol section and Fig. 1 on PDF page 2 distinguish two active photons plus
an untouched reference from purification of all $N$ active mixed inputs. Its
optimum is not silently transferred to this task.

[S24/25] F. H. B. Somhorst et al., *Photon distillation schemes with reduced
resource costs based on multiphoton Fourier interference*, arXiv:2404.14262v4,
https://arxiv.org/html/2404.14262v4 .
Its Fourier construction, heralding analysis, and finite-error/loss distinctions
are predecessors. No published plot values or experimental claims were imported.
