# Frayling typology

[Christopher Frayling 1993](https://researchonline.rca.ac.uk/384/9/frayling_research_in_art_and_design_1993_OCR.pdf) distinguished three kinds of research relationship between practitioner and the field of art / design:

- **Research *into* art** — historical or theoretical inquiry whose object is art. The art historian's work.
- **Research *through* art** — inquiry in which artistic practice is the means of generating knowledge. The artist as researcher; the practice produces findings.
- **Research *for* art** — inquiry that supports the making, with the artwork itself as the locus where the knowledge is embodied. The hardest category to articulate.

Frayling himself flagged the third as the most difficult: it is research whose output is not a paper but an artwork that *embeds* the knowledge, often non-propositionally.

## Why the plugin uses this typology

Three reasons:

1. **It is the most widely-engaged practice-based research typology in English-language PaR literature**, and the plugin's target population (artists writing across languages, doctoral exposition candidates) will likely encounter it.
2. **It forces an epistemological commitment** that English-language artist statements often paper over. Stating which kind of research the project is — and being held to that — is itself part of the practice-based research discipline.
3. **The third category's articulation difficulty is the plugin's design space.** The framework scaffolds the propositional articulation work *around* research-for-art, where Frayling himself flagged the difficulty.

## What the plugin does NOT do with the typology

Earlier framework drafts treated the plugin as a Frayling "layered hybrid" — assigning research-for, research-into, and research-through to different sub-artefacts of the project (the running plugin / the reference layer / the design-choice layer). This is a Frayling move Frayling would not recognise: he distinguished kinds of *knowledge claim*, not labels for sub-artefacts of a single project.

The current framework drops the layered-hybrid framing. The paper is research *for* art (the artist's own pre-studio articulation tooling) with a research-*into*-art component (the tradition-tag reference layer and its corpus survey). The design-choice rationale is treated as [design-research-through-design](https://dl.acm.org/doi/10.1145/1240624.1240704) (Zimmerman et al. 2007), not as a free-standing research-through-art claim — because the design-choice layer lacks the embodied-knowledge locus the research-through-art category requires.

## Sullivan's three stances (the finer-grained vocabulary)

[Sullivan 2010](https://us.sagepub.com/en-us/nam/art-practice-as-research/book230864) structures the same territory with three *stances* rather than three kinds of research:

- **Conceptual** — the artist makes a claim and tests it through making.
- **Dialectical** — the artist places a position against its opposite and works the tension.
- **Contextual** — the artist positions the work in lineage.

The plugin uses Sullivan's vocabulary in specific places:

- The **lineage-positioning move** in [`lineage`](../modes/lineage.md) is contextual.
- The **tension-over-ranking commitment** (provocations + counter-formulations in [`provoke`](../modes/provoke.md)) is dialectical.
- The **four named contributions** of the framework (see [README](https://github.com/joonhyungbae/art-project)) are conceptual.

## The Frayling-type declaration field

In [`brief`](../modes/brief.md) mode, field 10 of the Concept Brief is the Frayling-type declaration. The artist must state whether the project is research *into*, *through*, or *for* art. The plugin will not pick on the artist's behalf.

The system prompt accompanying the brief mode is instructed to weight downstream fields differently per declaration:

- Research-*through*-art → emphasis on methodology-as-medium tensions (provocation, anti-proposition).
- Research-*for*-art → emphasis on proposition-disconfirmation pairing.
- Research-*into*-art → emphasis on lineage anchor and intended encounter.

Whether the conditioning changes downstream cell content (versus serving as a reflexive prompt to the artist alone) is **unablated**. The plugin's behaviour around the field exists to surface the epistemological commitment; whether the field *operates* on downstream cells is an empirical question for future user studies.

## Reading Frayling honestly

Frayling's typology has been refined and contested by [Borgdorff](https://lup.nl/publications/art/the-conflict-of-the-faculties/), [Sullivan](https://us.sagepub.com/en-us/nam/art-practice-as-research/book230864), [Smith & Dean](https://edinburghuniversitypress.com/book-practice-led-research-research-led-practice-in-the-creative-arts.html), [Barrett & Bolt](https://www.bloomsbury.com/us/practice-as-research-9781845115593/). These critiques surface in the plugin's design choices:

- Borgdorff's *not-yet-knowing* / dual-discourse → [Concept Brief](../reference/concept-brief.md) Provocation field; Smith & Dean's *iterative cyclic web* → [`full` mode](../modes/full.md) cross-session structure; Barrett & Bolt's *materiality* → [Authentic Practice Boundaries](../reference/authentic-practice-boundaries.md).

The framework does not collapse these into Frayling. They are honored as distinct, and Frayling is named only where Frayling's specific contribution does work.

## See also

- [Cognitive scaffold](cognitive-scaffold.md) — the plugin's position within the typology.
- [Brief mode](../modes/brief.md) — where the declaration field lives.
- [Concept Brief schema](../reference/concept-brief.md) — full field specification.
