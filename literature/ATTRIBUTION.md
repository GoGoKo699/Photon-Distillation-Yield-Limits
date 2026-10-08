# Attribution and source comparison

The comparison concerns the fixed-output, passive, vacuum-extended,
independent-internal-error model in [MODEL_AND_CLAIMS](../research/MODEL_AND_CLAIMS.md).
The derivative at zero input error is taken at each fixed apparatus before the
large-size limit. [SOURCES.json](SOURCES.json) records versions, exact reading
locations, methods, and access limits; the original
[source record](../archive/research-handoff-2026-10-08/SOURCES.json) is preserved.

## Learning source

[Tichy, arXiv:1312.4266v2](https://arxiv.org/html/1312.4266v2) is the single
external tutorial for the [learning bridge](../research/TUTORIAL_BRIDGE.md).
It supplies interference prerequisites; the repository supplies the
distillation-specific steps. The research sources below serve attribution
and proof context.

## Existing results and the additional converse

| Source and locations | Existing result | Additional conclusion or distinction |
|---|---|---|
| [Somhorst et al., 2601.05947v1](https://arxiv.org/html/2601.05947v1), Section II Eq. (2); Appendix B, Theorem 1, Eqs. (10)–(24) | The optimal first-order error coefficient is $1/N$ for the stated $N$-mode problem; success optimization is identified separately. | The coefficient bound is inherited. The accepted-amplitude identity gives an explicit vacuum-extended formulation. The stable success bound treats every sequence with $c\to0$, including coefficients above $1/N$. |
| [Saied et al., 2404.14217v4](https://arxiv.org/html/2404.14217v4), Theorems III.2, III.4, III.5, III.9; Eqs. (III.4), (III.8)–(III.12) | Fourier-family purification attains $c=1/N$. Uniform survivor rows have a one-photon probability approaching $1/4$; Fourier selection gives achievable cost approximately $4N$ at sufficiently low input error. | A uniform-row calculation does not optimize over arbitrary rows. The added converse controls imbalance, arbitrary vacuum extensions, and batch size, giving $\mathcal C(R)=(4+o(1))R$. |
| Saied et al., Appendix D, Eqs. (D.1)–(D.4) and following discussion | Haar-averaged one-photon probability approaches $1/4$, while accepting every one-survivor pattern amplifies first-order error toward $2\epsilon$; analogous Fourier behavior is reported numerically. | Count-only failure is inherited. Haar averages do not bound a supremum over apparatuses. The direct weighted-row calculation supplies the stated generalization without claiming discovery of this failure mechanism. |
| [Somhorst et al., 2404.14262v4](https://arxiv.org/html/2404.14262v4), Sections II–IV, Eqs. (1)–(20); Section V, Eqs. (21)–(24); Appendix C, Eqs. (33)–(35) | Fourier phase selection and attainable linear cost; optimality discussions compare concatenation exponents and a normalized multiphoton slope bounded by $N$ with Fourier value $N-1$. | These optimality statements do not furnish an arbitrary-row success upper bound or a universal leading cost factor of four. The present result concerns that missing converse, not a new Fourier mechanism. |
| [Hoch et al., 2509.02296v1](https://arxiv.org/html/2509.02296v1), Eqs. (2)–(4); Appendices A–B, Eqs. (16)–(25) | For specified Gram/Bargmann data, optimize final pairwise HOM visibility, then success among visibility maximizers. Two photons enter the distillation interferometer; the third is an untouched reference. An optimal three-mode dilation is constructed. | This is a different objective and active-input count from the common-target, three-input-to-one derivative optimum. It does not supply an asymptotic all-network yield converse. |
| [Marshall, 2203.15197v3](https://arxiv.org/pdf/2203.15197v3), main text Eqs. (6)–(7), Appendix C; Appendix D, Eq. (D1) | Three-input attainment with success $1/3$ and coefficient $1/3$; four-input attainment with success $1/4$ and coefficient $1/4$. | The small-batch achieving constructions are inherited. The all-network upper bounds and vacuum-tapped four-input optimum are separate claims. |

The logical gap cannot be closed by combining the known coefficient bound with
one achieving family's yield: the first bounds batch size, while the second
does not bound competitors' success. Strongly coupled inputs can have raw
single-photon probabilities above one quarter. The converse controls their
accepted error amplitudes before taking a uniform limit over apparatuses.

## Related results with different roles

The passive-mixing central-limit framework of
[Becker, Datta, Lami and Rouze, CMP 383, 223–279 (2021)](https://doi.org/10.1007/s00220-021-03988-1)
is inherited. Its publisher Introduction and Section 2.4 characteristic-function
discussion were re-read in the physical-scope audit; the earlier reading is also
preserved in the original source record.
The additional distillation statement forces near-ceiling apparatuses into a
diffuse-row limit. The ensuing unconditional thermal number marginal does not
certify the heralded photon's internal purity.

The nonlinear-sign-shift comparison with
[Eisert, quant-ph/0409156](https://arxiv.org/pdf/quant-ph/0409156)
remains an inherited reading in the
[global proof's source record](../archive/research-handoff-2026-10-08/prior/prior/FOLLOWUP.md).
That task prescribes a phase operation on number-state superpositions with
ancillary resources. No reduction from internal-state purification to that task
is established; its quarter constant is not evidence for this converse.

[Somhorst and Renema, 2507.04805v2](https://arxiv.org/html/2507.04805v2),
Section III.2, Eqs. (12)–(14), compares lossy Fourier implementations and
conditional transmission. Those inaccessible loss modes differ from a monitored
vacuum tap; that comparison is not an ideal all-network success theorem.

## Reading boundary

The targeted primary-source comparison did not identify a directly covering
stable all-row converse. It includes the core papers' relevant references and
bounded title/topic searches for related work. It is not an exhaustive citation
graph search, priority certificate, or external independent review.

The retrieved arXiv search abstract for
[Robbio et al., 2609.37620](https://arxiv.org/abs/2609.37620), dated 29 September
2026, concerns interferometric certification and sample complexity. Direct
abstract, HTML, and PDF retrieval failed. It is recorded as abstract-screened,
not full-text reviewed or conclusively excluded.

Fresh core comparisons used primary HTML text; Marshall used parsed PDF text.
No figure values were extracted. Version records are evidence of the returned
versions, not a guarantee that every subsequent or separately published revision
has been found. The detailed contribution assessment is in
[CONTRIBUTION_REVIEW](../research/CONTRIBUTION_REVIEW.md).
