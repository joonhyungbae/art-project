# Measured harms

The framework ships with explicit disclosure of six classes of harm the artefact can cause or contribute to. The disclosure follows the [model-cards format](https://dl.acm.org/doi/10.1145/3287560.3287596) (Mitchell et al. 2019) and the [stochastic-parrots disposition](https://dl.acm.org/doi/10.1145/3442188.3445922) (Bender et al. 2021) toward naming harms that AI systems propagate by design.

Naming what the framework can do badly is itself part of the design — not an add-on disclaimer.

## The six harm classes

### 1. Lineage hallucination on long-tail sub-domains

The `lineage` mode can hallucinate artists, exhibitions, and works in domains where training-data coverage is thin. The classic LLM failure mode: fabrication that is hard to distinguish from real precedent unless the artist already knows the field.

**Mitigation**: mandatory bias header on every Lineage Map; artist-supplied initial candidates required before lineage extension; `--no-lineage` opt-out.

### 2. Training-data canon bias

The LLM substrate over-represents anglophone media-art venues (Rhizome, e-flux, Frieze, Artforum), the 1990s–2010s US/UK/DE generative-art scene, and canonised conceptual art (LeWitt, Weiner, On Kawara). It under-represents non-anglophone PaR doctoral expositions, Korean / East-Asian media-art (especially post-2010), oral / ritual / improvisational traditions, and collective / anonymous practice.

**Mitigation**: runtime non-anglophone routing when session signals call for it; mandatory bias header in `lineage` mode. The underlying corpus bias is structural and is **named rather than concealed**.

### 3. Simulation-pedagogy risk in rehearsal

Drawing on [Schön 1983](https://www.basicbooks.com/titles/donald-a-schon/the-reflective-practitioner/9780465068784/): artists who rehearse repeatedly on the simulation may train themselves to defend against safe critique or over-comply with low-stakes feedback. The danger is that the artist becomes fluent at the simulated kind of critique and proportionally less prepared for the real kind.

**Mitigation**: mandatory disclaimer header on every rehearsal transcript; architectural friction after 2 invocations on the same concept within 14 days; persona-collapse detector. Long-term effect is named as an open question; the deferred longitudinal study is the proper instrument.

### 4. Authorship-perception shift in the brief mode

The [AI ghostwriter effect](https://dl.acm.org/doi/10.1145/3637875) (Draxler et al. 2024) is the under-claiming of AI contribution by users. Artists may take material from the brief into a grant application without registering that the framing came from the plugin, eroding their own self-knowledge of where their thinking ended and the scaffold began.

**Mitigation**: stay-rough default preserves the artist's voice verbatim (which the artist can hear is theirs); footnote-level tradition-tag attribution surfaces where the scaffolding came in. Draxler's own findings suggest footnote attribution is among the *weaker* interventions; the mitigations are design hypotheses, not solved. The between-subjects attribution-UI test is sequenced for future user studies.

### 5. Conviviality and normalisation risk

[Illich 1973](https://en.wikipedia.org/wiki/Tools_for_Conviviality): tools that promise to assist a faculty can normalise the mediation of that faculty until the unmediated version becomes the harder path. [Turkle 2015](https://www.penguinrandomhouse.com/books/315557/reclaiming-conversation-by-sherry-turkle/) extends this to attention and conversation; [Hui 2016](https://www.urbanomic.com/book/the-question-concerning-technology-in-china/) extends it to non-Western technological cosmologies.

The framework's existence contributes to the normalisation of LLM mediation in cognitive domains where the mediation was, until recently, absent.

**Mitigation**: architectural commitments to artist autonomy (refusal to rank, refusal to participate in the artwork, refusal to converge under exploratory intent, architectural friction in `rehearsal`) place the framework on the convivial side of Illich's line. The position is contestable rather than settled.

### 6. Bounded user population

The user-asymmetry scope statement is itself a harm disclosure. The framework is scoped for artists where propositional articulation is a bottleneck. For artists outside the named populations, the framework is **unsuitable rather than suboptimal**.

Specifically, the framework is unsuitable for:

- artists whose articulation is already fluent (the scaffold gets in the way)
- traditions in which articulation is constitutively unwanted (improvisational, ritual, oral)
- contexts where the propositional artefact actively damages the practice (some performance contexts; some ceremonial traditions)

Naming what the framework is not for is treated as a strengthening move, not a weakness.

## What this disclosure does NOT claim

- **Not exhaustive.** Six classes are named; new classes may surface in deployment.
- **Not solved.** Each class has mitigations; none is "fixed." The mitigations are design hypotheses awaiting user-study confirmation.
- **Not externally verified.** This is self-disclosure; an independent audit would surface harms the framework's architect does not see.

## Why disclose?

Three reasons:

1. **Honesty.** The framework cannot deliver what it does not name. Disclosing harm classes is a precondition for the artist to use the framework with informed consent.
2. **Auditability.** Each harm class connects to a specific architectural mitigation. The disclosure makes the mitigations checkable.
3. **Scope discipline.** Disclosure forces the framework to face what it does badly, which constrains the temptation to over-claim what it does well.

## See also

- [Cognitive scaffold](cognitive-scaffold.md) — the position whose harms are disclosed here.
- [Frayling typology](frayling-typology.md) — the typology that grounds the bounded-user-population class.
- [Authentic Practice Boundaries](../reference/authentic-practice-boundaries.md) — the per-method discipline that mitigates harm class #1.
