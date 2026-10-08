# Optimal heralding yield at the photon-distillation error limit

**8 October 2026 — independent post-quantum-group research pilot.**

## Decision and claim hierarchy

**One bounded GO for the success-probability question, not promotion of a paper.**
The known optimal first-order error coefficient is 1/N. This pilot turns its
equality condition into a finite-dimensional bound on the ideal heralding
probability, allowing arbitrarily many vacuum ports. The resulting optimization
is solved exactly for N=2 and N=3: the maximum ideal success probabilities are
1/4 and 1/3. Existing protocols attain both.

At N=4, a monitored vacuum tap on a Fourier output attains ideal success
164/625=0.2624 at the same first-order coefficient 1/4, versus 1/4 success for
the untapped Fourier scheme. This changes the available mode/detector resources,
not the photon count. Its optimum is proved only within the specified tapped
family; global success optimality at N>=4 is unresolved.

The prospective contribution is the yield limitation and the remaining
all-network optimization, not a new claim that indistinguishability can be
distilled or that the error coefficient is 1/N. A roughly five-percent gain is
not by itself the intended physical advance. The next task must attack the
remaining optimum, not produce more tap settings.

The Compton and correlated-annealing pilots remain parked. No repository was
accessed or modified. The quantum-group memory, monitored-capacity, planar-Bell,
and electron-preparation projects and their PDFs were not scientific inputs.
No previous scientific checker was imported or rerun.

## 1. Physical task and the source-level gap

The task consumes N single photons, one in each of N occupied spatial inputs.
Each has the same target internal mode |g>, with independent probability epsilon
of an internal mode orthogonal to |g>. All error probabilities are equal. The
orthogonal components may differ between inputs; at first order only one such
component is present. A mixed orthogonal component gives the same first-order
calculation by linearity.

A passive M-mode unitary U acts identically on all internal states, with M>=N
and all other inputs in vacuum. One predetermined output mode is retained.
Photon-number-resolving measurements on every other mode do not resolve internal
states. A chosen set of number records containing N-1 detected photons heralds
exactly one survivor in the ideal lossless model.

The objective is the ideal-input success probability p0>0, subject to the
conditional retained-photon error

$$
\epsilon_{\rm out}=\epsilon/N+O(\epsilon^2).
$$

The limit is epsilon->0 at fixed N and a fixed circuit and acceptance rule.
It is not a finite-error optimization or a uniform limit with N growing while
epsilon stays fixed. Every attempted photon batch, including failure, is counted.
The limiting average input-photon consumption is N/p0.

No extra photon, internal-mode filter, squeezing, recorded input error label,
intermediate adaptive optical control, or outcome-dependent choice of survivor
port is permitted. All optical phases and beam splitters are ideal. Additional
vacuum modes and detectors are explicitly allowed and counted as hardware
resources, but are not assigned an implementation loss. Loss, false counts,
imperfect components and source multiphoton contamination require a different
performance calculation. In particular, losing one photon can turn an apparent
N-1-count herald into a vacuum output; our theorem does not certify against that
event.

Marshall [M22] introduced a three-photon construction with p0=1/3 and
epsilon_out=epsilon/3+O(epsilon^2). General Fourier constructions [S24a,S24b]
achieve 1/N error reduction with p0 approaching 1/4 at large N.
Somhorst et al. [S26], Section II and Appendix B, prove the error-coefficient
optimum for N-by-N unitary networks and explicitly leave success optimality open.
The present Cauchy calculation also covers additional vacuum inputs.

This is a source-anchored distinction between **purity improvement** and **how
often that improvement is heralded**.

## 2. Equality at the error limit

Let output 0 be retained. Define

$$
u_i=U_{0i},\quad p_i=|u_i|^2,\quad \sum_{i=1}^N p_i\le1,\qquad
\widetilde a_i^\dagger=\sum_{r\ne0}U_{ri}b_r^\dagger.
$$

In the (N-1)-photon detected-mode Fock space, put

$$
|v_i\rangle=u_i\prod_{j\ne i}\widetilde a_j^\dagger|0\rangle,\qquad
|v\rangle=\sum_i|v_i\rangle .
$$

The ideal amplitude with one retained photon is v. If input i contains the sole
bad internal state and that photon survives, the detected photons are all good
and their amplitude is v_i. Thus the same detected-mode space describes all
these alternatives, irrespective of the particular orthogonal bad state.

Let P be the orthogonal projector onto accepted number patterns. Then

$$
p_0=\|Pv\|^2,\qquad
c:=\lim_{\epsilon\to0}\epsilon_{\rm out}/\epsilon
=\frac{\sum_i\|Pv_i\|^2}{p_0}.
$$

The denominator at nonzero error is p0+O(epsilon), so replacing it by p0 is
legitimate for this coefficient. The norm identity

$$
\sum_i\|Pv_i\|^2-\frac{p_0}{N}
=\sum_i\left\|Pv_i-\frac{Pv}{N}\right\|^2
\tag{1}
$$

proves the inherited bound c>=1/N. It also gives the exact equality condition:

$$
c=1/N
\quad\Longleftrightarrow\quad
Pv_i=Pv_j\quad\hbox{for all }i,j.
\tag{2}
$$

The accepted detected amplitudes, including their phases, must erase the input
origin of a possible bad survivor. Equal classical probabilities are insufficient.

This is a Cauchy-Schwarz equality statement, not a new general purification
principle. The source's symmetric-single-error argument [S26, Appendix B] supplies
the same optimal coefficient.

## 3. A yield bound depending only on the retained output row

Let W=span{v_i-v_j}. Equation (2) implies that the accepted subspace is contained
in W-perp. Even allowing an arbitrary coherent detected-space projector rather
than just number-pattern selection,

$$
p_0\le\|\Pi_{W^\perp}v\|^2
=\min_{\mathbf1^\dagger z=N}z^\dagger Gz
=:B_N(\mathbf p),\qquad G_{ij}=\langle v_i|v_j\rangle.
\tag{3}
$$

The minimization form includes singular G. For nonsingular G it is

$$
B_N(\mathbf p)=\frac{N^2}{\mathbf1^T G^{-1}\mathbf1}.
\tag{4}
$$

For singular G, a null vector with nonzero component sum makes the minimum zero.
Otherwise G's pseudoinverse gives the same constrained minimum. This distinction
matters, for example, for a two-mode balanced beam splitter with no vacuum tap.

Unitarity gives
<0|tilde a_i tilde a_j^dagger|0>=delta_ij-u_i^*u_j.
Expanding the corresponding permanents eliminates every detector-row detail.
With e_k denoting elementary symmetric polynomials,

$$
G_{ii}=p_i\sum_{k=0}^{N-1}(-1)^k k!\,e_k(\mathbf p_{\setminus i}),
$$

$$
G_{ij}=-p_ip_j\sum_{k=0}^{N-2}(-1)^k(k+1)!\,
e_k(\mathbf p_{\setminus i,j}),\qquad i\ne j.
\tag{5}
$$

A principal minor of I-u*u contains k chosen rank-one factors in k! permutations.
For the off-diagonal minor the unmatched row and column add one required
rank-one factor, producing (k+1)!. The factors u_i from v_i cancel the phases.
This proves dependence only on intensities, including arbitrary extra vacuum
ports.

Equations (3)-(5) are an upper-bound relaxation, not a universal physical
implementation of the minimizing projection. They reduce an all-network
necessary condition to N real nonnegative numbers with sum at most one.

## 4. Sharp two- and three-photon optima, including vacuum ports

For N=2, writing s=p1+p2,

$$
B_2=\frac{4p_1p_2(1-s)}s
\le s(1-s)\le\frac14.
$$

A two-mode Fourier/Hong-Ou-Mandel beam splitter, followed by a half-transmitting
vacuum tap on the retained port, attains p1=p2=1/4 and success 1/4 with
c=1/2. Photon bunching followed by subtraction is an inherited mechanism [M22].
The result here is the matching upper bound in the declared fixed-output class.

For N=3, put

$$
s=p_1+p_2+p_3,\quad t=p_1p_2+p_1p_3+p_2p_3,\quad r=p_1p_2p_3,\quad u=1-s.
$$

Inverting (5) gives

$$
B_3=
\frac{9r[u^2+2ut+2(s+1)r]}{ut+(s+3)r}.
\tag{6}
$$

To maximize at fixed s, denote the right side by f(s,t,r), and let w be the
third probability when comparing p_i,p_j. For D=ut+(s+3)r,

$$
\frac{D^2}{9}(f_t+w f_r)
=
u^3(wt-r)+2u^2wt^2+4u(2-u)wtr
+2(2-u)(4-u)wr^2+4ur^2\ge0.
\tag{7}
$$

Every term is nonnegative: 0<=u<=1 and wt-r=w^2(p_i+p_j)>=0.
Therefore

$$
(p_i-p_j)(\partial_{p_i}B_3-\partial_{p_j}B_3)
=-(p_i-p_j)^2(f_t+w f_r)\le0.
$$

So B3 is Schur-concave at fixed sum: balancing the probabilities cannot decrease
it. The balanced value is

$$
B_3\le s-\frac43s^2+\frac23s^3.
$$

Its derivative is 2(s-2/3)^2+1/9>0. Since s<=1,

$$
\boxed{p_0\le1/3\quad\text{whenever }c=1/3.}
\tag{8}
$$

Boundary points follow by continuity; if a retained-port input coupling vanishes,
a nonzero accepted v cannot satisfy (2). Standard three-mode Fourier
distillation attains p0=1/3 and c=1/3. Thus the bound is tight even after arbitrary
vacuum modes are allowed.

This is not a new three-photon protocol: its achieving construction and success
value are in Marshall [M22]. The additional claim is that no fixed-output passive
network in the declared class has greater ideal success at that coefficient.
The determinant expression, positive Schur identity, and derivative are checked
symbolically. Their proof is not inferred from numerical unitary optimization.

The limiting minimum mean photon costs for the optimal two- and three-photon
tasks are respectively 8 and 9. The tasks have different target error reductions;
the number 8 does not make the two-photon operation the better one at fixed purity.

## 5. A vacuum tap changes the four-photon answer

Take the N-mode Fourier matrix F_N, an additional vacuum mode N, and mix output
0 with that vacuum through a beam splitter of intensity transmissivity eta:

$$
U(\eta)=B_{0,N}(\eta)(F_N\oplus1).
$$

The retained row has p_i=eta/N. Measure every other output, including tap N.
Accept a record if it has N-1 detected photons and

$$
\sum_{r=1}^{N-1}r n_r=0\pmod N.
\tag{9}
$$

The tap carries Fourier character zero. Cyclically permuting the occupied input
columns multiplies each detected pattern by its character. On (9), every v_i
has the same amplitude. The ideal input has character zero, so its nonzero
one-survivor amplitudes all obey (9). This proves both c=1/N and saturation of
the Gram upper bound at this balanced row.

The standard Fourier symmetry and suppression methods are inherited from
[S24a,S24b]. The tap preserves their relevant character, rather than replacing
interference with an independent loss process.

The exact ideal success is

$$
P_N(\eta)=
\sum_{k=1}^N(-1)^{k-1}k\,k!\binom Nk(\eta/N)^k.
\tag{10}
$$

One derivation uses
< (n_0)_k > = (k!)^2 e_k(p)
and inversion of the factorial moments to obtain Prob(n0=1).
Equivalently, thin the original Fourier-port photon number through the monitored
beam splitter. At eta=1, (10) is the established Fourier heralding formula.

For N=4,

$$
P_4(\eta)=\eta-\frac32\eta^2+\frac98\eta^3-\frac38\eta^4.
$$

At the exact rational setting eta=4/5,

$$
\boxed{p_0=\frac{164}{625}=0.2624,\qquad c=\frac14,}
$$

compared with p0=1/4 for eta=1. The same four input photons now herald 4.96%
more frequently. The limiting photon cost changes from 16 to 625/41 =
15.243902439... photons per output.

The Fourier output port's ideal probabilities before tapping are
Prob(n0=0,1,2,3,4)=(15/32,1/4,3/16,0,3/32).
At eta=4/5, the originally one-, two-, and four-photon terms respectively
contribute .2, .06, and .0024 to the new one-survivor yield. Both beam-splitter
outputs are accounted for, and the phase-character check is still required.

P4''=-(3/4)(6 eta^2-9 eta+4)<0, so the unique root of P4' on (0,1) is the
global maximum **within this tapped Fourier family**:

$$
\eta_*=0.7832160613205729\ldots,\qquad
P_4(\eta_*)=0.2624669882112195\ldots.
$$

Global optimality over all four-photon optical networks is not established.
Nor is the comparison a criticism of the N-mode predecessor: it enlarges the
mode/detector resources while holding photon inputs and leading error reduction
fixed. A generalization that treats empty ports as automatically irrelevant to
success would be false.

## 6. Finite-error calculations and controls

The leading-order guarantee is shared by two different independent error models:
orthogonal bad bits (each erroneous input has its own orthogonal mode), and
same bad bits (all errors occupy one common orthogonal internal mode). At second
and higher order they differ, as in [S24a,S26].

For N=4 we explicitly enumerate all 16 input error masks and all resulting
Fock amplitudes. Define H_k and B_k as the sums, over masks with k bad inputs, of
the accepted probability and accepted bad-survivor probability. Then

$$
h(\epsilon)=\sum_{k=0}^4H_k\epsilon^k(1-\epsilon)^{4-k},\quad
\epsilon_{\rm out}=
\frac{\sum_{k=0}^4B_k\epsilon^k(1-\epsilon)^{4-k}}{h(\epsilon)}.
$$

No additional binomial factor is applied; H_k,B_k already sum over masks.

At eta=4/5 the exact arrays are:

| Error model | H_k, k=0,...,4 | B_k, k=0,...,4 |
|---|---|---|
| Distinct bad modes | (164,164,332,244,61)/625 | (0,41,191,183,61)/625 |
| One common bad mode | (164,164,364,164,164)/625 | (0,41,182,123,164)/625 |

At epsilon=.01, the distinct-bad-mode calculation gives

| Device | Herald probability | Conditional error |
|---|---:|---:|
| Untapped Fourier | .2426241272 | .0026268796 |
| eta=4/5 tap | .2546589080 | .0026182428 |

But in the common-bad-mode model, the output error increases slightly:
.0026012574 untapped versus .0026122838 tapped, even while the success improves.
Thus the tap is not a universal finite-error improvement in both objectives.

A negative control removes condition (9) but still accepts all one-survivor
events. At eta=4/5 its first-order error is 1.8048780488 epsilon, worse even than
the input. Counting survivors alone does not perform distillation.

Another control passes one input directly to the output and detects the others.
It succeeds with probability one but has c=1 rather than 1/N. The yield upper
bounds do not apply after the optimal-error requirement is dropped.

## 7. Prior-art reconstruction and remaining task

[M22] already gives the three-photon success of 1/3 and the four-photon success
of 1/4 for its constructions. Its inspected discussion calls the chosen scheme
the best found and allows improved circuits; it does not prove (8) for all
vacuum-extended networks.

[S24a,S24b] supply the general Fourier circuits, symmetry tests, success formulas,
and finite-error models. Setting eta=1 in (10) recovers their heralding expression.
Our untapped common-bad-mode coefficients reproduce [S24a, Appendix F] exactly.
Bunching and photon subtraction are also older ideas, discussed explicitly
by Marshall. The tap is not a new primitive.

[S26] supplies the coefficient bound and explicitly distinguishes its optimum
from the unresolved success question. Our added Cauchy equality analysis is a
way of addressing that question, not a replacement novelty claim for 1/N.

Hoch et al. [H25], despite its broad title, optimizes a different task: two
active photons interfere, while a third is left untouched as a reference; the
objective is their output-reference HOM visibility. It is not three active
noisy inputs distilled to a single photon at coefficient 1/3. Its formulas
should not be silently transferred to (8), nor dismissed merely because its
notation differs.

The positive case is a resource question with partial sharp answers and a
systematic general bound. The skeptical case is that the remaining proof may
reduce to a tractable polynomial optimization, while a small success gain alone
does not establish broad significance. Neither a new bound formula nor a passing
test suite settles the publication case.

The next bounded task is to maximize B_N(p) on p>=0, sum p<=1, or find an
unbalanced counterexample to the balanced-row candidate. Balanced rows are
physically attainable by the construction above. Proving they maximize the
relaxation would close the optical optimum; failure would reveal precisely
which further optical realizability issue remains. No general balanced-row
optimality, fixed-error tradeoff, or large-N success optimum is asserted here.

Targeted searches and the inspected passages have not supplied the same
vacuum-robust three-photon converse or this particular four-photon tap
comparison. This is not exhaustive priority clearance. No author contact,
manuscript, or new repository is initiated.

## 8. Verification and source-reading boundaries

The first formal five-group suite passed. It was preserved unchanged, then
enriched with the complete N=3 Schur argument and an independent exact
Gaussian-integer Fock expansion. All six final groups passed, and the repeated
JSON reports are byte-identical. No scientific assertion tolerance was relaxed.

The exact expansion uses fourth roots of unity and rational eta, with occupation
factorials applied only after multiplying integer creation polynomials. It
independently agrees with normalized-Fock creation-operator calculations for all
error masks. This supplies rational certificates, not Monte Carlo estimates.

The largest optical matrix is 7 by 7; the largest Gram matrix tested directly
is 5 by 5. Four photons with distinct internal labels have at most 625 nonzero
occupation amplitudes in the explicit five-port checks. No large quantum
state simulation or optical experiment was performed. Finite tests do not
replace the proof of the all-network N=3 bound.

A cross-tool filesystem permission error occurred while saving the enriched
checker; no mathematical test was running and the save failed. Write permission
was corrected only for this new local pilot, the file was written and read back,
and the formal suites then passed. There were no scientific test failures.

The PDF source reads below used parsed primary text. A requested page image
of [H25, p.3] succeeded and confirmed the circuit/task distinction. Screenshot
requests for [S24a, pp.14 and 54] failed; no plot or raster-only values are used.
Unrelated automatically available old project PDFs were not used.

### Primary sources

- **[M22]** Jeffrey Marshall, *Distillation of Indistinguishable Photons*,
  Phys. Rev. Lett. 129, 213601 (2022), arXiv:2203.15197v3.
  https://arxiv.org/pdf/2203.15197
  Read model/noise Eq.(3), three-photon construction and success Eq.(6), resource
  comparison and four-photon statement, and related-work discussion of
  bunching/subtraction. No claim of rereading every robustness appendix.

- **[S24a]** Jason Saied, Jeffrey Marshall, Namit Anand, Eleanor G. Rieffel,
  *General protocols for the efficient distillation of indistinguishable photons*,
  arXiv:2404.14217v4.
  https://arxiv.org/pdf/2404.14217v4
  Read protocol definitions, relevant symmetry/suppression and first-order
  theorems, ideal heralding formula and resource comparison, and Fourier N=4
  same-bad-bit polynomials in Appendix F. Not all 61 pages were independently
  audited.

- **[S24b]** F. H. B. Somhorst et al., *Photon distillation schemes with reduced
  resource costs based on multiphoton Fourier interference*, arXiv:2404.14262v4.
  https://arxiv.org/html/2404.14262v4
  Read Fourier construction, Eq.(19) and Appendix D moment derivation, and
  Appendix E's loss-versus-erasure distinction. No device figures are used as
  numerical evidence.

- **[S26]** F. H. B. Somhorst et al., *Below-threshold error reduction in single
  photons through photon distillation*, arXiv:2601.05947v1.
  https://arxiv.org/html/2601.05947v1
  Read Section II's explicit open success-probability statement, independent
  error models in Appendix A, and the N-by-N optimal-error proof in Appendix B.
  Its experimental performance is not reanalyzed.

- **[H25]** Francesco Hoch et al., *Optimal distillation of photonic
  indistinguishability*, arXiv:2509.02296v1.
  https://arxiv.org/pdf/2509.02296
  Read model, task definition and optimal three-mode network section; p.3 was
  rendered to verify that only two photons enter the active distillation network
  and the third is an untouched comparator. This is a different output task,
  not a directly covering three-active-input yield theorem.
