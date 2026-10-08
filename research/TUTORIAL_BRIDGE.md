# From multiphoton interference to a distillation yield limit

Start with Malte C. Tichy, *Interference of Identical Particles from Entanglement
to Boson-Sampling*, **J. Phys. B 47, 103001 (2014)**,
[arXiv:1312.4266v2](https://arxiv.org/html/1312.4266v2)
([PDF](https://arxiv.org/pdf/1312.4266v2),
[DOI](https://doi.org/10.1088/0953-4075/47/10/103001)).
This tutorial supplies the optical language. The route below selects what is
needed here; the subsequent derivations connect it to the
[photon-distillation model](MODEL_AND_CLAIMS.md).

## 1. Read with a specific question

| Tutorial section | What to extract |
|---|---|
| 2.1.2 | Creation operators, Fock normalization, two-photon interference |
| 2.2.1 | Spatial evolution that leaves internal modes unchanged |
| 2.3.2 | Conditioning on photon counts |
| 3.1–3.2 | Multimode unitaries and occupation amplitudes |
| 3.4, especially Eq. (60) | Permanent probabilities and factorials |
| 3.7.1 | Fourier symmetry and forbidden outcomes |
| 4.3 | Several distinguishability components |

Ask throughout: **which alternatives add as amplitudes, and which add as
probabilities?** That distinction will determine the purification coefficient.
The tutorial's illustrative Fourier proof uses collision-free configurations.
Section 5 below supplies the extension to arbitrary bosonic occupations.

## 2. Translate the notation

| Tutorial convention | Convention here |
|---|---|
| $`N`$ particles, $`n`$ modes | $`N`$ occupied inputs; additional modes may be vacuum |
| $`U^{\mathrm{Tichy}}_{jr}`$: input first | $`U_{rj}=U^{\mathrm{Tichy}}_{jr}`$: output first |
| Occupations $`\vec r,\vec s`$ | Input occupations and detector record $`\mathbf n`$ |
| Internal wave-packet labels | Good mode $`g`$ and orthogonal bad states |
| Overlap coefficients $`c_{jk}`$ | Distinct from our error derivative $`c`$ |

Thus $`U=(U^{\mathrm{Tichy}})^{\mathsf T}`$: transpose the numerical matrix,
with no complex conjugation. Both describe the same creation-operator
substitution:

```math
a_j^\dagger[\phi]\longmapsto\sum_r U_{rj}b_r^\dagger[\phi].
```

The internal state $`\phi`$ is unchanged. Bosonic Fock normalization is

```math
\lvert\mathbf n\rangle
=\prod_r\frac{(b_r^\dagger)^{n_r}}{\sqrt{n_r!}}\lvert0\rangle.
```

Consequently a coefficient of $`(b_r^\dagger)^2\lvert0\rangle`$ must be
multiplied by $`\sqrt2`$ to obtain the amplitude of the normalized two-photon
state. With one photon per occupied input, an output amplitude is the permanent
of the matrix with repeated output rows, divided by
$`\sqrt{\prod_r n_r!}`$. These factors matter even in the two-photon example.

## 3. Separate the ideal amplitude from one erroneous input

Each input has independent internal state

```math
\rho_i(\epsilon)=(1-\epsilon)\lvert g\rangle\langle g\rvert
+\epsilon\sigma_i,\qquad
\operatorname{supp}\sigma_i\perp\lvert g\rangle.
```

Retain output zero and measure all other outputs. Accepted records contain
$`N-1`$ photons. At fixed apparatus define ideal success $`p_0>0`$ and
$`\epsilon_{\mathrm{out}}=c\epsilon+O(\epsilon^2)`$, where output error means
population orthogonal to $`g`$. The derivative is taken before varying $`N`$.

Write $`u_i=U_{0i}`$ and split the transformed creation operator into survivor
and detected parts:

```math
a_i^\dagger[g]\longmapsto
u_i b_0^\dagger[g]+\widetilde a_i^\dagger[g],\qquad
v_i=u_i\prod_{j\ne i}\widetilde a_j^\dagger[g]\lvert0\rangle.
```

In the ideal one-survivor sector, any input can supply the survivor. These
alternatives are indistinguishable, so the detector vector is
$`v=\sum_i v_i`$. Let $`P`$ keep the accepted number records, and set
$`a_i=Pv_i`$, $`a=\sum_i a_i`$. Then $`p_0=\lVert a\rVert^2`$.

If input $`i`$ alone is bad and survives, the detected photons are all good and
have vector $`v_i`$. This input alternative has probability
$`\epsilon+O(\epsilon^2)`$. Independence therefore gives an erroneous-survivor
success probability $`\epsilon\sum_i\lVert a_i\rVert^2+O(\epsilon^2)`$.
Dividing by $`p_0+O(\epsilon)`$ yields

```math
cp_0=\sum_i\lVert a_i\rVert^2,\qquad
\sum_i\left\lVert a_i-\frac aN\right\rVert^2
=p_0\left(c-\frac1N\right).
```

The second equality follows by expanding the squares and using
$`\sum_i a_i=a`$. Thus $`c\ge1/N`$, with equality exactly when all accepted
vectors equal $`a/N`$. Overlaps between different bad states do not enter this
first-order calculation: each contributing alternative contains just one bad
photon. The [physical interpretation](PHYSICAL_INTERPRETATION.md) derives the
conditional density operator and its connection to interference visibility.

## 4. Work through two photons and one monitored vacuum tap

Use two occupied inputs, Fourier outputs zero and one, and one vacuum input.
Split Fourier output zero with a balanced tap; retain transmitted output zero
and measure Fourier output one and the tap output $`t`$. In our convention,

```math
U=\begin{pmatrix}
1/2&1/2&1/\sqrt2\\
1/\sqrt2&-1/\sqrt2&0\\
-1/2&-1/2&1/\sqrt2
\end{pmatrix}.
```

The columns are occupied inputs zero and one, then vacuum; the rows are
survivor zero, measured output one, then tap. They are orthonormal. For either
internal state, the occupied-input substitutions are

```math
a_0^\dagger\mapsto\frac{b_0^\dagger-b_t^\dagger}{2}
+\frac{b_1^\dagger}{\sqrt2},\qquad
a_1^\dagger\mapsto\frac{b_0^\dagger-b_t^\dagger}{2}
-\frac{b_1^\dagger}{\sqrt2}.
```

Accept the single detector record $`(n_1,n_t)=(0,1)`$. Photon conservation
then leaves one photon in the predetermined survivor. The tap click is part
of success; it is not unobserved loss.

For two good photons, multiplying the substitutions gives

```math
\lvert\Psi_g\rangle=
\left[\frac{(b_0^\dagger)^2}{4}
-\frac{b_0^\dagger b_t^\dagger}{2}
+\frac{(b_t^\dagger)^2}{4}
-\frac{(b_1^\dagger)^2}{2}\right]\lvert0\rangle.
```

In normalized Fock states, ordered as $`(0,1,t)`$, this is

```math
\lvert\Psi_g\rangle=
\frac{\lvert2,0,0\rangle}{2\sqrt2}
-\frac{\lvert1,0,1\rangle}{2}
+\frac{\lvert0,0,2\rangle}{2\sqrt2}
-\frac{\lvert0,2,0\rangle}{\sqrt2}.
```

The squared amplitudes sum to one. The accepted amplitude is $`-1/2`$, so
$`p_0=1/4`$. Its two input-origin contributions are each
$`(1/2)(-1/2)=-1/4`$.

To check the error physically, let input zero carry an orthogonal bad mode
$`h`$ and input one remain good. The accepted part is

```math
-\frac14 b_0^\dagger[h]b_t^\dagger[g]\lvert0\rangle
-\frac14 b_0^\dagger[g]b_t^\dagger[h]\lvert0\rangle.
```

The two terms have orthogonal tap states. Tracing the internal-insensitive
detector adds their probabilities: success is $`1/8`$, and success with a bad
survivor is $`1/16`$. A bad photon in input one gives the same values.
Therefore

```math
p_{\mathrm{herald}}(\epsilon)
=\frac14(1-2\epsilon)+2\epsilon\frac18+O(\epsilon^2)
=\frac14-\frac\epsilon4+O(\epsilon^2),
```

```math
\epsilon_{\mathrm{out}}
=\frac{2\epsilon(1/16)+O(\epsilon^2)}
{1/4-\epsilon/4+O(\epsilon^2)}
=\frac\epsilon2+O(\epsilon^2).
```

Thus $`c=1/2`$, saturating the coefficient bound. Independent repetitions
consume $`2/p_0=8`$ input photons per success in the ideal limit, including
rejected trials. Without the tap, two-photon Fourier interference has no
one-survivor event: both photons leave together.

## 5. Extend Fourier selection to collisions

For $`N`$ inputs use $`(F_N)_{rj}=\omega^{rj}/\sqrt N`$, with
$`\omega=e^{2\pi i/N}`$. A cyclic shift of every input label multiplies
output row $`r`$ by $`\omega^r`$. The all-good input product is invariant
under that shift, because its creation operators commute. An output monomial
with occupations $`n_r`$ acquires phase $`\omega^{\sum_r rn_r}`$.
Its amplitude can be nonzero only when

```math
\sum_r r n_r\equiv0\pmod N.
```

This argument includes repeated powers of creation operators, so it permits
arbitrary collisions. A tap on Fourier output zero has character zero as well.
With one retained photon in output zero, accept measured total count $`N-1`$
and zero character. Define the detector amplitudes from Section 3 by
$`V_i(\mathbf n)=\langle\mathbf n\vert v_i\rangle`$. Cyclicity gives
$`V_{i+1}(\mathbf n)=\omega^{\sum_r rn_r}V_i(\mathbf n)`$. Thus all accepted
$`a_i`$ coincide and $`c=1/N`$ whenever $`p_0>0`$.
The [optical construction](OPTICAL_CONSTRUCTION.md) gives the complete unitary,
positive-success cases, and exact success formula.

## 6. From attainment to optimality

The Fourier family attains $`p_0\to1/4`$. Proving optimality requires controlling
every allowed network, including unbalanced survivor couplings: a large raw
one-photon probability alone does not guarantee purification. The
[central theorem](THEOREM.md) and [proof details](PROOF_DETAILS.md) combine the
accepted-amplitude constraint with a uniform bound on strongly and weakly
coupled inputs, proving $`c_N\to0\Rightarrow\limsup p_{0,N}\le1/4`$.

For requested first-order reduction $`R`$, Section 3 forces $`N\ge R`$.
The uniform yield converse and Fourier attainment together give minimum
leading consumption $`\mathcal C(R)=(4+o(1))R`$. When $`c_N\to0`$ and
$`p_{0,N}\to1/4`$, the occupied-input survivor intensities
$`p_i=|U_{0i}|^2`$ satisfy $`\max_i p_i\to0`$ and $`\sum_i p_i\to1`$.
Their ideal
unconditional output then approaches a mean-one thermal number distribution
in trace norm, as derived in [the physical mechanism](PHYSICAL_MECHANISM.md).
That number distribution precedes heralding; the internal quality of the
heralded photon is governed by the accepted amplitudes instead.

The [attribution map](../literature/ATTRIBUTION.md) documents the research sources
underlying the construction and converse.
