# Optimal-first-order photon purification: a sharp asymptotic yield and the four-photon optimum

**8 October 2026 — continuation of the independent photon-distillation pilot.**

## Decision and claim hierarchy

The large-input success optimum now has a matching all-network converse:

$$
\boxed{\lim_{N\to\infty}p_N^\star=\tfrac14.}
$$

The known Fourier construction attains this limit. The new result is that no other network in the declared class improves the asymptotic ideal-input yield, even with arbitrarily many vacuum modes and arbitrarily unbalanced coupling to the retained output. Separately, the tapped four-photon construction from the preceding pilot is globally optimal, not merely optimal within its one-parameter family.

**GO for a focused theorem and contribution review.** The central question is the unavoidable photon overhead at optimal first-order purification. The four-photon theorem is a finite-resource consequence, not a second project. The full finite-N optimum for N>=5 remains unresolved, but is not needed for the asymptotic theorem. These are author-side proofs, not independent review or exhaustive priority clearance. No repository is accessed, created, or modified.

The earlier partial-monitoring, planar-Bell, quantum-group-memory, electron-preparation, and other spin-off projects remain outside this work. The unrelated PDFs retained in the conversation are not scientific inputs. The preceding distillation note, code, evidence, and manifest remain unchanged under `prior/`.

## 1. Operational definition and order of limits

For each fixed N>=2, an attempt uses N independent single photons, one in each occupied input port. Each has target internal mode |g> with probability 1-epsilon, and an orthogonal erroneous internal mode with probability epsilon. At first order, only one erroneous input occurs, so whether different erroneous photons share a mode or occupy distinct orthogonal modes does not affect the coefficient. At finite epsilon those models can differ, as the preceding pilot explicitly checked.

A fixed passive interferometer acts on spatial ports identically for every internal mode. Any number of extra vacuum inputs is allowed. One output port is chosen in advance as the survivor; all other outputs are measured by ideal number-resolving detectors that do not distinguish internal modes. The accepted patterns contain N-1 measured photons. There are no photon losses, dark counts, extra nonvacuum inputs, nonlinear optical interactions, internal-mode filters, intermediate adaptation, or outcome-dependent survivor choices.

Write p0 for ideal-input success. For p0>0, let c be the coefficient in

$$
\epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2).
$$

Let p_N^star be the supremum of p0 among such protocols with **c=1/N exactly**. The protocol can depend on N, but is fixed in its Taylor expansion around epsilon=0. The expansion and optimization refer to each fixed N first. Only afterward is N taken large.

Thus the asymptotic photon-cost conclusion is

$$
\inf\frac{N}{p_0}=\frac{N}{p_N^\star}=(4+o(1))N.
$$

The infimum includes failed attempts. This is not a fixed-nonzero-error theorem, a bound uniform in N epsilon, a success-versus-approximate-coefficient tradeoff, a hardware throughput, or a loss-tolerant resource estimate. It does not constrain a protocol that accepts worse first-order purification, or one that changes the listed resources.

The optimal error coefficient is inherited from Somhorst et al. [S26]. Their Appendix B states its proof for an N-by-N passive unitary. The direct amplitude identity below also covers the additional vacuum inputs explicitly. The Fourier success limit 1/4 and its approximately 4N achieving cost are already proved in Saied et al. [SMAR25]; they are not new values predicted here.

## 2. The accepted amplitudes must erase input origin

Let u_i=U_(0i), p_i=|u_i|^2, and write a tilde over the part of each output creation operator supported on the measured ports. The detector state when photon i is the erroneous survivor is

$$
v_i=u_i\prod_{j\ne i}\widetilde a_j^\dagger|0\rangle,\qquad v=\sum_{i=1}^Nv_i.
$$

For the projector P selecting the accepted detector patterns,

$$
p_0=\|Pv\|^2,\qquad
cp_0=\sum_i\|Pv_i\|^2.
$$

The exact Cauchy identity gives

$$
\sum_i\|Pv_i\|^2-\frac{p_0}{N}
=\sum_i\left\|Pv_i-\frac{Pv}{N}\right\|^2.
$$

Consequently c=1/N requires Pv_i=Pv/N for every i. Complex amplitudes, not just probabilities, must coincide. If a survivor coupling p_i vanishes, v_i=0 forces p0=0 at this coefficient; such rows cannot improve a positive optimum.

For any real or complex z with sum_i z_i=N, equal accepted amplitudes imply

$$
\boxed{p_0\le\left\|\sum_i z_iv_i\right\|^2=z^\dagger Gz,\quad G_{ij}=\langle v_i|v_j\rangle.}
\tag{1}
$$

Minimizing gives the preceding pilot's bound B_N(p). This is also valid if one grants an arbitrary coherent detector-space projection, so proving this bound does not assume that every mathematical projector is realizable by number detection.

The retained output row satisfies p_i>=0 and sum_i p_i<=1. Vacuum inputs occupy the unused row norm. Unitarity and the bosonic creation algebra give

$$
G_{ii}=p_i\sum_{k=0}^{N-1}(-1)^k k!\,e_k(p_{\setminus i}),
$$

$$
G_{ij}=-p_ip_j\sum_{k=0}^{N-2}(-1)^k(k+1)!\,e_k(p_{\setminus i,j})\quad(i\ne j).
\tag{2}
$$

All detector rows disappear from this expression. Only the occupied-input intensities in the survivor row remain. The derivation and independent Fock-space checks are preserved in `prior/PILOT.md`.

## 3. Why a direct balancing proof is not available

The N=3 proof in the pilot established Schur-concavity at fixed total intensity. The same monotonicity is false at N=4. For

$$
p=(1/10,1/1000,2/5,2/5),\qquad
p'=(1/4,1/1000,2/5,1/4),
$$

p' is obtained by averaging the first and fourth entries. Both sums are 901/1000. Exact rational inversion of G gives

$$
B_4(p)=\frac{399293056}{53030171875},\qquad
B_4(p')=\frac{7964707}{1070608750},
$$

$$
B_4(p)-B_4(p')=
\frac{8186973478119}{90839305637406250}>0.
$$

This refutes the proposed Schur-concavity route, **not** balanced-row global optimality. The four-photon global theorem is proved separately below. No finite-N balancing theorem for N>=5 is claimed or required by the asymptotic argument.

## 4. A uniform all-network asymptotic converse

### 4.1 Separate strongly and weakly coupled inputs

Fix delta>1/N. Let A={i:p_i>delta}, let m=|A|, and let D be the remaining indices. Then m<=1/delta<N. Define

$$
\sigma=\sum_{i\in A}p_i,\qquad
\lambda=\sum_{i\in D}p_i,\qquad
v_2=\sum_{i\in D}p_i^2\le\delta\lambda\le\delta.
$$

Here sigma+lambda<=1. Put

$$
f(x)=\prod_{i\in A}(1-p_ix),\qquad
g(x)=\prod_{i\in D}(1-p_ix),\qquad
\omega=\frac{\lambda}{1+\lambda}.
$$

Choose z_i=beta on D and z_i=beta omega on A, with

$$
\beta=\frac{N}{N-m+m\omega}
=\frac{N}{N-m/(1+\lambda)}
\le\frac1{1-1/(N\delta)}.
$$

These coefficients sum to N. They are trial weights in a mathematical bound, not an additional optical filter or a change to the physical apparatus. Equation (1) gives p0<=beta^2 Q, where

$$
Q=\left\|\sum_{i\in D}v_i+\omega\sum_{i\in A}v_i\right\|^2.
$$

Using k!=integral_0^infinity exp(-x)x^k dx in (2) yields exactly

$$
Q=\int_0^\infty e^{-x}\big\{-f(g'+xg'')
-2\omega x f'g'-\omega^2g(f'+xf'')\big\}\,dx.
\tag{3}
$$

Although the polynomial integrand need not be positive, Q is a squared norm.

### 4.2 Evaluate the diffuse-input comparison exactly

Replace g by g_star=exp(-lambda x) in (3), including its derivatives, and call the result Q_star. Integration by parts gives

$$
\boxed{Q_*=\frac{\lambda}{1+\lambda}
\int_0^\infty e^{-(1+\lambda)x}f(x)\,dx.}
\tag{4}
$$

For completeness, let h=1+lambda and J_k=integral exp(-hx)x^k f(x)dx. Before choosing omega, the expression is

$$
[\lambda-2\omega\lambda+\omega^2h]J_0
-(\lambda-\omega h)^2J_1.
$$

The specified omega cancels J1 and leaves lambda J0/h. All boundary terms are included; f(0)=1 and exponential damping kills the terms at infinity.

The remaining integral has a probability interpretation:

$$
h\int_0^\infty e^{-hx}f(x)dx
=\operatorname{per}(I-aa^\dagger),\qquad
 a_i=\sqrt{p_i/h}\quad(i\in A).
$$

Since ||a||^2=sigma/h<=1, these can be the couplings of a valid passive output port to m occupied single-photon inputs. The permanent is the probability that none of those photons exits that port. It is between zero and one, including m=0. Therefore

$$
\boxed{0\le Q_*\le\frac{\lambda}{(1+\lambda)^2}\le\frac14.}
\tag{5}
$$

This use of a probability bounds an integral with potentially signed factors; it does not assume f(x)>=0. The quantity lambda/(1+lambda)^2 is also the one-photon probability of a thermal number distribution of mean lambda. No thermal input, reservoir, or extra noise is introduced into the physical protocol.

### 4.3 Control the replacement uniformly

A pointwise small-coupling approximation is insufficient: the number of factors and the integration range both grow. The following global inequalities close that gap. For y>=0,

$$
|1-y|\le e^{y/2},\qquad
0\le e^{-y}-1+y\le y^2/2.
$$

For 0<=y<=1 the first inequality is immediate. For y>=1, the largest value of (y-1)e^(-y/2) is 2e^(-3/2)<1. The second follows from Taylor's integral remainder. Telescoping products and differentiating by sums over distinct indices give, for all x>=0,

$$
|g-e^{-\lambda x}|\le\frac{v_2x^2}{2}e^{\lambda x/2},
$$

$$
|g'+\lambda e^{-\lambda x}|
\le v_2\left(x+\frac{\lambda x^2}{2}\right)e^{\lambda x/2},
$$

$$
|g''-\lambda^2e^{-\lambda x}|
\le v_2\left(1+2\lambda x+\frac{\lambda^2x^2}{2}\right)e^{\lambda x/2}.
\tag{6}
$$

In the first-derivative estimate, replacing the product excluding i contributes at most lambda v2 x^2/2; restoring its missing exponential contributes at most v2 x. In the second derivative, the corresponding terms are lambda^2 v2 x^2/2 and 2lambda v2 x, with the missing diagonal i=j contributing v2. These estimates do not divide by a factor 1-p_i x, so they hold at its zeros as well.

For r=0,1,2, the other product satisfies |f^(r)(x)|<=sigma^r exp(sigma x/2). Substitution into (3) bounds the error integrand by

$$
v_2 e^{-x/2}\big[2x+Bx^2+Cx^3\big],
$$

$$
B=\frac52\lambda+2\omega\sigma+\frac12\omega^2\sigma\le\frac52,
\qquad C=\frac12(\lambda+\omega\sigma)^2\le\frac12.
$$

Here sigma+lambda<=1 and 0<=omega<=1/2 were used. Integrating all three terms gives

$$
\boxed{|Q-Q_*|\le96v_2\le96\delta.}
\tag{7}
$$

The constant 96 is deliberately conservative: 2 integral xe^(-x/2)=8, (5/2) integral x^2e^(-x/2)=40, and (1/2) integral x^3e^(-x/2)=48. It is independent of N, m, the row, and the number of vacuum ports.

### 4.4 Take the supremum before the limit

Equations (1), (5), and (7) prove, uniformly over all networks in the declared class,

$$
\boxed{
p_0\le\min\left\{1,
\frac{1/4+96\delta}{[1-1/(N\delta)]^2}\right\},
\qquad\delta>1/N.
}
\tag{8}
$$

Choosing delta=N^(-1/2) shows limsup p_N^star<=1/4. This is a rigorous but coarse finite-size estimate; it should not be used to claim a practical crossover size or a tight finite-N optimum. It avoids assuming that all individual p_i become small: finitely or slowly growing numbers of strongly coupled inputs are handled by the tailored trial weights and the no-photon bound.

## 5. The known Fourier sequence attains the bound

For the N-mode Fourier interferometer, optionally tapped with vacuum at transmissivity eta, the survivor row is p_i=eta/N. Cyclically permuting the input columns multiplies each detector row by a Fourier character, while the survivor and its tap have character zero. Keeping the zero-character detection patterns gives Pv_i=Pv_j.

With ideal inputs every nonzero one-survivor amplitude already lies in that character sector. Hence its success is exactly

$$
P_N(\eta)=\sum_{k=1}^N(-1)^{k-1}k\,k!\binom Nk(\eta/N)^k
=\eta\int_0^\infty e^{-x}x(1-\eta x/N)^{N-1}\,dx.
\tag{9}
$$

This saturation at a balanced row was established in the preceding pilot. Selecting ideal patterns only, or all symmetry-allowed patterns, agrees on p0 and c; patterns with vanishing ideal amplitude also have vanishing bad-survivor amplitude under the equal-amplitude condition. Higher-order error terms can differ.

The untapped eta=1 construction for N>2 is inherited from the Fourier-distillation literature. Saied et al. [SMAR25, Theorem III.5] already proves lim P_N(1)=1/4. A short independent check is dominated convergence in (9): the integrand is bounded in absolute value by xe^(-x/2), and tends to xe^(-2x). Thus

$$
\lim_{N\to\infty}P_N(1)=\int_0^\infty xe^{-2x}dx=1/4.
$$

Combining this known attainable sequence with the new uniform converse gives

$$
\boxed{\lim_{N\to\infty}p_N^\star=1/4.}
\tag{10}
$$

The theorem is not a claim that every finite N has optimum 1/4, or that arbitrary small relaxations of c=1/N obey the same bound. N=3 already has optimum 1/3. Ordinary routing can have p0=1 but c=1; it violates the required purification coefficient, not the success bound.

## 6. Exact four-photon global optimization

For N=4 and all p_i>0, choose a different trial vector in (1):

$$
z_i=\frac4{p_i\sum_j1/p_j}.
$$

Writing s=e1(p), t=e2(p), r=e3(p), w=e4(p), exact substitution into G gives

$$
B_4(p)\le U_4(p)=
\frac{16w}{r}(1-s+2t-6r)-\frac{16w^2}{r^2}(8-6s).
\tag{11}
$$

We prove

$$
U_4(p)\le P_4(s)=s-\frac32s^2+\frac98s^3-\frac38s^4,
\qquad 0\le s\le1,
\tag{12}
$$

by an exact nonnegative-coefficient certificate, not a floating-point optimizer.

### 6.1 A reproducible polynomial certificate

Sort the probabilities and parameterize them as

$$
p=\frac1\Lambda(a,a+b,a+b+c,a+b+c+d),\qquad
\Lambda=S+v,
$$

where a,b,c,d,v>=0 and S,T,R,W are the elementary symmetric polynomials of the four numerators. This covers every physical row: use the successive differences of sorted p and v=1-s, in which case Lambda=1.

Clearing positive denominators, (12) is equivalent to nonnegativity of

$$
\begin{aligned}
\mathcal P={}&R^2(8S\Lambda^3-12S^2\Lambda^2+9S^3\Lambda-3S^4)\\
&-128WR(\Lambda^3-S\Lambda^2+2T\Lambda-6R)\\
&+128W^2(8\Lambda^2-6S\Lambda).
\end{aligned}
\tag{13}
$$

More precisely, P=8 Lambda^10 r(p)^2 [P4(s(p))-U4(p)]. Its expansion in a,b,c,d,v has **613 nonzero monomials, all with positive integer coefficients**, and is homogeneous of degree ten. The minimum nonzero coefficient is two. The numbers of monomials with v-exponents 0,1,2,3 are 225,178,126,84 respectively.

`certificates/four_photon_positive.json` records every coefficient and exponent tuple. The checker regenerates (13), verifies exact equality with that file, verifies all coefficient signs and degrees, and verifies symbolically that (11) is the quadratic trial obtained from G. This is a finite computer-assisted algebraic certificate; no sampling of p establishes its sign. When b=c=d=0, the polynomial vanishes, consistent with equality for a balanced row. If any physical p_i vanishes, p0=0 at c=1/4 as noted in Section 2, covering boundary cases without division by zero.

### 6.2 Attainment and the unique tap setting

For the balanced row p_i=s/4, the physical Fourier-plus-tap construction attains P4(s). Therefore the complete four-photon optimum, including arbitrary vacuum ports, is

$$
\boxed{p_4^\star=\max_{0\le s\le1}P_4(s).}
$$

Its second derivative is

$$
P_4''(s)=-\frac34(6s^2-9s+4)<0.
$$

Since P4'(0)>0 and P4'(1)<0, it has exactly one maximizing point eta_star in (0,1):

$$
8-24\eta_*+27\eta_*^2-12\eta_*^3=0,
$$

$$
\eta_*=0.7832160613205729\ldots,\qquad
p_4^\star=0.2624669882112195\ldots,
$$

$$
4/p_4^\star=15.240011809717618\ldots.
$$

These decimal values are numerical evaluations of an exact algebraic optimum, not interval-certified decimals. The rational point eta=4/5 has success 164/625, as already certified in the pilot. The new fact is that optimizing this one-parameter implementation reaches the all-network four-photon optimum.

The additional vacuum port is a resource: the construction adds a beam splitter and a monitored output. The theorem compares photon consumption, not equal footprint or equal optical loss. It grants all competing networks arbitrary additional empty ports, so adding more of them cannot improve the stated ideal four-photon result.

## 7. Implication-level comparison and scientific allocation

[S26] explicitly distinguishes the optimal first-order error coefficient from the then-open success-probability problem. Its reference to an achieving cost of approximately 4N is not a proof that every network requires it. [SMAR25] already proves the 1/4 limit for Fourier/Hadamard constructions and, more generally, evaluates ideal single-survivor counting for an N-by-N unitary with a uniformly coupled first row. That hypothesis excludes arbitrary unbalanced rows and vacuum-coupled survivor rows. Our converse treats both without postulating balanced optimality.

The earlier pilot already credited [M22] for the achieving three-photon success 1/3 and [S24/25] for the scalable Fourier construction. Their optical mechanisms are not reclaimed. The three-photon global ceiling came from the preceding pilot; the four-photon global certificate is new here. The finite-error caveats from those works and the pilot remain: different internal-error models and photon loss change the practical objective.

A superficially similar 1/4 theorem exists in [E05] for the nonlinear-sign-shift gate. Its task is a prescribed diagonal phase operation on arbitrary superpositions of different photon numbers, with ancillary resources. It does not automatically constrain purification of internal distinguishability from N occupied inputs. No reduction from our task to that gate is established. That paper is a direct precedent for rigorous all-network optical success bounds, not a source of the present constant by numerical coincidence.

The present targeted search did not identify a matching unrestricted-row asymptotic converse or four-photon optimization in the inspected sources. This is not exhaustive priority clearance. The asymptotic theorem should be independently attacked at the amplitude equality, grouped Gram integral, and uniform replacement; the four-photon result has a separately regenerable exact certificate.

The positive physical case is that the approximately four-input-batches overhead of familiar Fourier purification is not an accident of that architecture: under exact optimal first-order purification, all allowed passive networks have the same best leading ideal-input photon cost. Extra vacuum modes can improve finite batches, but not that asymptotic constant. The skeptical case is that this is a fundamental limit for an ideal, first-order and fixed-output task; its finite-error or hardware impact cannot be inferred without additional analysis.

**Continue with focused consolidation and claim-level review, not automatic expansion.** The arbitrary finite-N optimum for N>=5, a stability bound for nearly optimal coefficients, finite-epsilon operating curves, adaptive survivor selection, loss, extra photons, and hardware design are separate questions. They are not silently solved, and need not all be solved before assessing this theorem. No manuscript submission, author contact, repository creation, or protected-project change occurs here.

## 8. Sources, numerical scope, and record

- **[S26]** F. H. B. Somhorst et al., *Below-threshold error reduction in single photons through photon distillation*, arXiv:2601.05947v1. Primary HTML Section II and Appendix B inspected. Section II explicitly separates error optimality and open success optimality. No experimental performance estimate is imported. <https://arxiv.org/html/2601.05947v1>
- **[SMAR25]** J. Saied, J. Marshall, N. Anand, E. G. Rieffel, *General protocols for the efficient distillation of indistinguishable photons*, Phys. Rev. Applied 23, 034079 (2025), arXiv:2404.14217v4. Primary PDF Theorems III.2, III.5 and III.9, first-order scope, and Appendix D comparison inspected. Theorem III.5 already proves the attainable 1/4 limit; the finite-error and source-cost statements keep their order-of-limits qualification. No plotted value is used. A PDF screenshot attempt failed; parsed theorem text was readable. <https://arxiv.org/pdf/2404.14217v4>
- **[M22]** J. Marshall, *Distillation of Indistinguishable Photons*, Phys. Rev. Lett. 129, 213601 (2022), arXiv:2203.15197. Achieving three-photon construction credited in the preserved pilot. Primary abstract checked this turn; the detailed construction reading is inherited from the pilot, not claimed independently repeated here. <https://arxiv.org/abs/2203.15197>
- **[S24/25]** F. H. B. Somhorst et al., *Photon distillation schemes with reduced resource costs based on multiphoton Fourier interference*, arXiv:2404.14262v4. Primary HTML Section IV and photon-loss discussion inspected for matching task and limits. No apparatus advantage is inferred. <https://arxiv.org/html/2404.14262v4>
- **[E05]** J. Eisert, *Optimizing linear optics quantum gates*, Phys. Rev. Lett. 95, 040502 (2005), arXiv:quant-ph/0409156. Primary PDF problem specification and nonlinear-sign-shift conclusion inspected. Phase-gate and internal-state-purification resources are distinct. PDF screenshot failed; no visual information was used. <https://arxiv.org/pdf/quant-ph/0409156>

The new checker has six groups: the exact grouped quadratic and independent optical Gram; global product/derivative bounds and the constant 96; no-click normalization and all-network trial weights; the exact four-photon positive polynomial and optical attainment; the rational failure of Schur-concavity; and the known Fourier achieving sequence with a nonpurifying-routing control. The largest new optical unitary is 7-by-7. The exact polynomial has five formal variables; large-N checks use scalar integration, not large optical Fock-space simulation. Random-row checks are deterministic-seed diagnostics, not a proof of global optimization.

The first formal run exposed two test-driver errors: an all-heavy algebraic fixture was normalized even though it violates delta>1/N, and a SymPy substitution used a symbol with mismatched assumptions. The unnormalized fixture is retained as an out-of-domain control and the actual real symbol is now substituted. No physical model, scientific inequality, or tolerance changed. A later report retained the raw roundoff in the exactly zero untapped two-photon success, while replacing the meaningless division by that near-zero value with the exact zero and an undefined photon cost. Independent exact checks were also enriched. Earlier scripts, patches, and reports remain available.

The final enriched six-group suite passed twice with byte-identical reports. The original six-group pilot passed unchanged and reproduced its canonical report byte-for-byte. All fifteen incoming archive members remain unchanged. Checks support the formulas and normalization; the uniform proof is the analytical argument in Section 4, not the numerical sequence. `RUN_RECORD.json` records hashes, differences, execution boundaries, and the exploratory limitations.
