# Positioning

## What this is

art-project is a **pre-studio articulation scaffold** for practice-based artistic research — a Claude Code plugin that assists an artist with the **propositional articulation work** that surrounds the conception of a new project. It does not claim to participate in artistic ideation itself; the cited PaR literature (Frayling 1993; Borgdorff 2011, 2012; Sullivan 2010; Smith & Dean 2009; Barrett & Bolt 2007; Penny 2017) is unanimous that ideation in art is non-linguistic, material, and inseparable from making — *that* work happens in the studio. art-project scaffolds what surrounds that work: surfacing the impulse, generating tension-holding provocations, mapping (when the artist requests it) precedent lineage, drafting a Concept Brief, and rehearsing self-critique before facing actual reviewers.

The plugin is pivoted from [art-paper v0.1.0](https://github.com/joonhyungbae/art-paper), itself forked from [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills). The genre-neutral safety machinery (citation-faithfulness, intent detection, Devil's Advocate concession-threshold, dialogue health monitoring) is inherited; the downstream paper-authoring scope has been dropped; the design-research framework has been substantially revised in light of a four-agent critique (artistic-research methodologist + HCI/AI-creativity researcher + practicing-artist studio-side review + Devil's Advocate). See [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md) for the full design synthesis.

## Self-positioning (Frayling layered hybrid)

Following Frayling's (1993, *Research in Art and Design*, RCA Research Papers 1(1)) three-category typology, art-project declares its position in layers:

- **Tool layer — research FOR art.** The plugin as software is an instrument for use by practice-based artists. This is its primary public face.
- **Reference layer — research INTO art.** [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md) is a second-order synthesis of how prior literature theorizes artistic ideation. It is *about* artistic practice; it does not *do* it.
- **Design-choice layer — research THROUGH art/design.** The architectural choices (generation-evaluation separation, tension-over-ranking, lineage-with-opposition, formative-not-decisional self-critique rehearsal, tradition-tag attribution with Authentic Practice Boundaries) are themselves propositional claims about how AI assistance in PaR ideation should be architected. The plugin-as-artefact demonstrates the claims; the accompanying paper argues them.

## Epistemological position — cognitive scaffold

art-project occupies the **cognitive scaffold** position — neither inert tool nor co-author. The literature anchors:

- **Clark & Chalmers (1998), "The Extended Mind", *Analysis* 58(1):7–19** — cognition can extend into external scaffolds that meet parity and reliability conditions. The plugin is such a scaffold, in the same family as Eno & Schmidt's Oblique Strategies deck, an artist's notebook, or a peer-conversation partner.
- **Malafouris (2013), *How Things Shape the Mind: A Theory of Material Engagement*** — cognition is constituted in engagement with materials and tools, not located behind the skin.
- **Penny (2017), *Making Sense*** — embodied practice is the locus of artistic knowing. art-project operates *adjacent to* that locus, in the para-artistic space of articulation work, and does not claim to substitute for it.

The cognitive-scaffold framing has three virtues for v0.1:
- it leaves authorship of the artwork unambiguously with the human (clean for AI-disclosure compliance and copyright);
- it is consistent with the design choices the plugin already makes (refusal to rank, tension-over-resolution, formative-not-decisional critique);
- it has academic precedent and can be cited (extended-cognition literature), so reviewers do not have to take it on faith.

## User asymmetry — who this is for

art-project is **not a universal art-ideation tool**. It is scoped to artists for whom **propositional articulation is a bottleneck**:

- early-career artists who have not yet developed the genre conventions of artist statement / grant proposal / concept brief
- artists writing in a second language (especially Korean-first artists writing English grant applications, and vice versa)
- artist-researchers preparing PaR doctoral expositions where the articulation work *is* part of the research
- artists working under deadline (grant cycles, residency applications, biennale calls)
- artists for whom external scaffolding helps (verify with adaptive-tooling literature before formal claims)
- collectives mid-project who need a shared articulation document

For artists whose propositional articulation is already fluent, the plugin is structurally unsuitable — the practicing-artist studio-side reviewer's blunt conclusion ("I would currently turn it off and use Claude directly") is the correct response for that group.

## Grounding

art-project is **not** a brainstorm-app dressed in art vocabulary. Its load-bearing decisions are grounded in a reference layer that models prior research on artistic ideation. Each ideation mode wires to specific entries — see [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md) — through declared **tradition tags** with **Authentic Practice Boundaries** that name what the plugin defers to human execution.

The design decisions — that articulation is constraint-based detour rather than free association; that provocations are held in tension with counter-formulations rather than ranked; that lineage maps include *opposition* and *blind-spot* entries rather than only kin; that the rehearsal critique is *formative* rather than decisional — were made from inside practice. The maintainer (Joon-Hyung Bae) works at once as an exhibiting artist, an author of practice-based art papers at peer-reviewed venues, and an AI researcher publishing in the field.

License: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Restricts commercial use by design, to keep the tool free for art and academic communities.

## What this is not

- **Not an autonomous ideation system.** The Penny / Ingold / Borgdorff critique that artistic ideation is non-linguistic, material, and embodied is *accepted*. art-project produces language; ideation happens elsewhere.
- **Not a substitute for studio practice, peer critique, or curatorial review.** The `rehearsal` mode is rehearsal *for* future review, not a substitute for it. Real critique operates differently and will surprise the artist.
- **Not a universal art-ideation tool.** See "User asymmetry" above.
- **Not a literature search tool dressed as a creative act.** The `lineage` mode is honestly named as retrieval. It is *not* ideation. It exists for positioning, with a mandatory training-data bias disclosure.
- **Not an authorship system.** The plugin does not claim authorship or co-authorship of the artwork or the eventual project. Outputs are material the artist takes back to the studio.

## Tradition tags — what the label claims and does not claim

art-project outputs carry **tradition tags** ("via Oblique Strategies", "via Boden's transformational creativity", "via Sullivan's contextualist inquiry"). The honesty paragraph:

> Tradition tags indicate which entries in the methodology reference were loaded into the prompt that produced an output. They do not claim causal attribution — the LLM's actual generation mechanism is opaque. A tag is a *prompt-grounding* and *style-affinity* claim: this output aims to operate in the tradition named, and was conditioned by it; whether it succeeds in that aim is for the artist to judge, and the artist is encouraged to read the named primary source to deepen the engagement.

Each tradition carries an **Authentic Practice Boundary** that names what the plugin *does not simulate* and defers to human execution. Examples:

- **Eno & Schmidt's Oblique Strategies (1975).** Boundary: the plugin proposes Oblique-style provocations but cannot replicate the *physical, finite, blindly-drawn* character of the deck. Obtain the actual deck for serious use.
- **Cage's chance operations.** Boundary: the plugin describes and suggests chance methods (I Ching, coin toss) but *does not execute them*. The artist throws the dice; the artist's time is part of the work.
- **LeWitt's instruction-based work.** Boundary: the plugin prompts the artist to write instructions but *does not author instructions for the artist*.
- **Bogart's Viewpoints.** Boundary: the plugin asks Viewpoints-derived questions but cannot perform Viewpoints work, which is bodied, ensemble-based, and temporal.

Full list in [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md) §2.3.

## Measured-harm disclosure (model-card-style summary)

Following Mitchell et al. (2019, "Model Cards for Model Reporting", FAccT) and Bender et al. (2021, "On the Dangers of Stochastic Parrots", FAccT), art-project ships with explicit harm-class disclosure. Summary:

- **Lineage hallucination.** The plugin can hallucinate artist names, exhibition dates, or work titles in long-tail domains (Korean media art; performance art; oral / indigenous lineages). v0.1 *measures and discloses* per-domain hallucination rates; v0.2 will integrate runtime grounding (Wikidata / ULAN / e-flux) and refuse-to-emit-on-low-confidence.
- **Training-data canon bias.** The LLM's "lineage" reflects anglophone, well-funded, well-documented venues (Ars Electronica, ZKM, SIGGRAPH, Whitney, MIT). Every `lineage` output carries the bias disclosure header. Korean / East-Asian default routing partially mitigates for Korean-language sessions.
- **Simulation-pedagogy risk (rehearsal mode).** Rehearsing on a simulacrum may train either defensiveness or over-compliance when facing real critics (Schön 1983; Devil's Advocate critique). The mandatory disclaimer + architectural friction (warn after 2 rehearsals / 14 days on same concept) + persona-collapse detection are the v0.1 mitigations. Long-term effect cannot be measured by v0.1 alone.
- **Authorship-perception shift (ghostwriter effect).** Following Draxler et al. (2024, TOCHI — verify) and Gero et al. (2022, Sparks, DIS). The stay-rough default on `brief` mode and the footnote-level tradition-tag salience are v0.1 mitigations.
- **Conviviality / normalization risk** (Illich 1973; Turkle 2015; Hui 2016). The plugin's existence contributes to the normalization of LLM-mediation in cognitive domains where it was historically absent. The plugin takes the *contestable but defensible* position that its architectural commitments to artist autonomy (refusal-to-rank, formative-not-decisional, intent-classified Socratic, IRON RULE on human decision, lineage opt-out) place it on the convivial side. This is the position to be argued, not a fact.
- **Bounded user population.** Per the user-asymmetry scope above: the plugin is structurally unsuitable for artists whose articulation is already fluent, and for traditions where articulation is constitutively unwanted (improvisational, ritual, oral).

Full disclosure detail in the v0.2 synthesis spec §6.

## Design philosophy

**Assistive, not deceptive.** art-project does not hide that AI was involved. Tradition tags are visible (footnote level by default); the methodology reference is open and citable; the harm-class disclosure is part of the artifact.

**Human-in-the-loop, always.** Even though the suite is one skill, the checkpoint discipline is preserved:
- `full` mode now opens a long-running project file rather than a single-session pipeline; sessions are days or weeks apart, in alignment with how PaR ideation actually proceeds (Smith & Dean 2009).
- `socratic` mode disables auto-convergence in exploratory intent — no premature "want me to summarize?" prompts.
- `rehearsal` mode renders **formative rehearsal**, not an accept/reject decision. There is no acceptance threshold; the output is structured friction that re-enters the Concept Brief.
- `lineage` mode does not propose lineage without artist-supplied initial candidates, and offers a clean `--no-lineage` opt-out at any point.

**Failure modes are made visible, not hidden.**
- The Devil's Advocate inside `rehearsal` is subject to the inherited **Concession Threshold Protocol** — no premature concessions; concession only at rebuttal score ≥4 on the 1–5 scale.
- `socratic` HARD-binds **exploratory vs goal-oriented intent** classification every 3 turns and refuses to drive toward deliverables while exploration signals are still present.
- Inside `rehearsal`, the Devil's Advocate runs a **Dialogue Health** sub-check every 5 turns for agreement spirals, premature convergence, and conflict avoidance, and injects a challenge when the pattern is detected (v0.2 phase c demoted this from a suite-wide mechanism to a `rehearsal`-scoped sub-heuristic).
- The **Persona Collapse Detector** in `rehearsal` flags when all four personas raise the same concern (the rehearsal has lost its multi-perspectivity).

These mechanisms are genre-neutral and inherited unchanged from the parent suite. They exist so that the artist can see where the AI might be flattening their thinking — not so that the AI can claim it is always right.

## Allowed uses

- **Pre-studio articulation work** for a new project: `socratic` to surface the impulse, `provoke` for tension-holding what-if cards, `lineage` (with artist-supplied initial candidates) for positioning, `brief` for the proposition document.
- **PaR doctoral expositions** where the articulation work is itself part of the research.
- **Grant and residency applications** under deadline.
- **Bilingual articulation work** (Korean ↔ English), with Korean / East-Asian default lineage routing.
- **Studio collective coordination** — a shared articulation document.
- **Self-critique rehearsal** before facing curators or peers (with the mandatory disclaimer that this is *not* substitute critique).
- **Teaching** — art-school faculty demonstrating PaR methodology via the executable reference layer, or running structured ideation exercises with students under explicit pedagogical framing.

## Discouraged uses

- Submitting plugin-produced Concept Briefs verbatim. The stay-rough default mitigates but does not eliminate the AI-detectable polish problem; the artist's voice must be in the final document.
- Treating `rehearsal` critique as a substitute for actual peer or curator review.
- Letting `lineage` mode propose your lineage *for* you (the mode is designed to refuse this; the artist supplies candidates first).
- Using `full` mode to compress weeks of ideation into one session. The mode is a long-running project file; respect its temporal shape.
- Generating provocations and presenting them as the artist's own without acknowledging methodology grounding (tradition tags are part of the output; do not strip them).
- Using the plugin to *settle* an impulse prematurely. Socratic mode is designed to keep the artist in exploration; forcing convergence is misuse.

## Prohibited uses (per license)

- Commercial SaaS or hosted services built on art-project.
- Consulting or freelance services that package art-project as a paid product.
- Enterprise or institutional paid deployments without separate licensing.
- Commercial API wrappers or resale of art-project functionality.

These reflect policy intent. See the [CC BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/) for legal terms. For commercial licensing inquiries, contact the maintainer.

## Citing this tool

```
art-project (Version 0.1.0) [Computer software].
Pivoted from art-paper v0.1.0 (Joon-Hyung Bae),
itself forked from Academic Research Skills (Cheng-I Wu).
https://github.com/joonhyungbae/art-project
Companion paper: see docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md.
```
