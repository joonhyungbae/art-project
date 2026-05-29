# art-project for Claude Code

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-D77757)](https://docs.claude.com/claude-code)
[![Version](https://img.shields.io/badge/version-v0.1.0--ideation-blue)](https://github.com/joonhyungbae/art-project/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Wiki](https://img.shields.io/badge/wiki-EN%20%2F%20KO-blue)](https://joonhyungbae.github.io/art-project/)

> [한국어 README](README.ko-KR.md) · 📖 Wiki: [English](https://joonhyungbae.github.io/art-project/) / [한국어](https://joonhyungbae.github.io/art-project/ko/)

A Claude Code plugin: a **pre-studio articulation scaffold** for practice-based artistic research. **Not an ideation engine.** The Penny / Ingold / Borgdorff critique that artistic ideation is non-linguistic, material, and inseparable from making is *accepted*; the plugin scopes itself to the propositional articulation work *around* ideation. The actual ideation happens in your studio, with material.

This plugin is the v0.2 synthesis of a four-agent design critique (artistic-research methodologist + HCI / AI-creativity researcher + practicing-artist studio-side review + Devil's Advocate). The single most consequential reframe — *"ideation engine" → "pre-studio articulation scaffold"* — converts the strongest critique of the v0.1 design (citing the very literature that disqualifies its method) into a scope statement. See [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).

---

## Install in 30 seconds

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

That installs one skill (`art-ideation`) plus six `/art-*` slash commands. No LaTeX toolchain required — v0.1 outputs Markdown by default.

Then try one of:
- `/art-project:socratic` — *"I have a vague pull toward something, I don't know what the work is yet"*
- `/art-project:provoke` — *"I'm stuck, throw constraints at me"*
- Or natural language: *"I want to think through a new project"* — the skill auto-routes via intent detection and announces the routing transparently.

See [QUICKSTART.md](QUICKSTART.md) for full first-session walkthroughs of each mode.

---

## What art-project gives you

One skill, six modes. Each mode wires to specific entries in a 25+ entry methodology reference layer (Boden, Geneplore, Frayling, Borgdorff, Sullivan, Eno, LeWitt, Cage, Bogart, Bauhaus, Manovich, Penny, Dunne & Raby, plus Korean / East-Asian and HCI prior-art).

| Mode | What it does | IRON RULE |
|---|---|---|
| `/art-project:socratic` | Pre-reflective dialogue surfacing impulse / fragments / constraints / refusals / **residue** | No auto-convergence under exploratory intent |
| `/art-project:provoke` | Tradition-tagged provocations (Oblique Strategies / SCAMPER / Cage chance / Bolt experimental gesture / Dunne & Raby PPPP / etc.) with **Authentic Practice Boundary** per method | Preserved **unhelpfulness** — silence after the provocation; no auto-interpretation |
| `/art-project:lineage` | Lineage Map extending **artist-supplied** initial candidates (kin / opposition / blind-spot / unexpected-neighbor) | Mandatory training-data bias header; Korean / East-Asian default routing on Korean sessions; honest self-description as *retrieval, not ideation* |
| `/art-project:brief` | Concept Brief with epistemic fields (proposition / **anti-proposition** / **disconfirmation condition** / **Frayling-type declaration**) | **Stay-rough** default — your voice stays in; **no auto-completion** of gaps |
| `/art-project:rehearsal` | Self-Critique Rehearsal (renamed from `panel` in v0.2) — Curator + Practitioner-peer + Theorist + Devil's Advocate | Mandatory disclaimer header; architectural friction after 2 invocations / 14 days on same concept; persona-collapse detector |
| `/art-project:ideate` | Long-running project file across days/weeks (Smith & Dean iterative cyclic web) | One mode per session; no single-session pipelining |

---

## Self-positioning

**Frayling layered hybrid** (Frayling 1993, *Research in Art and Design*):

- **Tool layer — research FOR art.** The plugin as software is an instrument for use by practice-based artists.
- **Reference layer — research INTO art.** [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md) is a second-order synthesis of how prior literature theorizes artistic ideation.
- **Design-choice layer — research THROUGH art/design.** The architectural choices (generation-evaluation separation, tension-over-ranking, lineage-with-opposition, formative-not-decisional self-critique rehearsal, tradition-tag attribution with Authentic Practice Boundaries) are themselves propositional claims about how AI assistance in PaR ideation should be architected.

**Epistemological position — *cognitive scaffold*** (Clark & Chalmers 1998; Malafouris 2013; Penny 2017). Neither inert tool nor co-author. The plugin operates *adjacent to* embodied practice, in the para-artistic space of articulation work.

**User asymmetry — this is not a universal tool.** For artists where propositional articulation is a bottleneck (early-career; second-language writers; PaR-doctoral candidates; under grant / residency deadline). **Not** for artists whose articulation is already fluent — that group should use Claude directly. Not for traditions where articulation is constitutively unwanted (improvisational, ritual, oral).

---

## Tradition tags + Authentic Practice Boundaries

Every plugin output carries **tradition tags** ("via Oblique Strategies", "via Sullivan's contextualist inquiry"). The honesty paragraph:

> Tradition tags indicate which entries in the methodology reference were loaded into the prompt that produced an output. They do **not** claim causal attribution — the LLM's actual generation mechanism is opaque. A tag is a *prompt-grounding* and *style-affinity* claim. The artist is encouraged to read the named primary source to deepen the engagement.

Each tradition carries an **Authentic Practice Boundary** naming what the cited method requires that the plugin defers to human execution:

- **Eno & Schmidt Oblique Strategies (1975)** — the physical, finite, blindly-drawn deck is constitutive. The plugin produces *Oblique-affine* provocations; obtain the actual deck for serious use. The plugin **goes silent** after issuing an Oblique-style provocation.
- **Cage chance operations** — the plugin *describes and proposes* chance methods (I Ching, coin toss). It does **not execute** them. **The artist throws the dice.** The time the artist spends performing the procedure is part of the work.
- **LeWitt instruction-based work** — the plugin *prompts the artist to write instructions*. It does **not author instructions** for the artist. LeWitt's "the idea is the machine that makes the art" requires the artist to be the rule-setter.
- **Bogart Viewpoints (1995)** — the plugin asks Viewpoints-derived questions about the intended encounter, but cannot perform Viewpoints work, which is bodied / ensemble / temporal.

Full list in [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md).

---

## Measured-harm disclosure (model-card style)

Following Mitchell et al. (2019, FAccT) Model Cards and Bender et al. (2021, FAccT) Stochastic Parrots, art-project ships with explicit harm-class disclosure. Six classes:

1. **Lineage hallucination** per sub-domain (anglophone media art / Korean media art / performance art / others). The plugin can hallucinate artist names, exhibition dates, or work titles in long-tail domains. v0.1 measures and discloses per-domain rates; v0.2 will integrate runtime grounding (Wikidata / ULAN / e-flux) and refuse-to-emit-on-low-confidence.
2. **Training-data canon bias.** The LLM's "lineage" reflects anglophone, well-funded, well-documented venues (Ars Electronica, ZKM, SIGGRAPH, Whitney, MIT). Every Lineage Map carries the bias disclosure header; Korean / East-Asian default routing on Korean sessions partially mitigates.
3. **Simulation-pedagogy risk (rehearsal).** Schön (1983) cited. Rehearsing on a simulacrum may train defensiveness or over-compliance when facing real critics. Mitigations: mandatory disclaimer + architectural friction + persona-collapse detector. Long-term effect cannot be measured by v0.1 alone.
4. **Authorship-perception shift (ghostwriter effect).** Wordcraft (Yuan et al. 2022, IUI), Sparks (Gero et al. 2022, DIS), Draxler et al. (2024, TOCHI — verify). Mitigations: footnote-level tradition-tag salience by default; `brief` stay-rough default.
5. **Conviviality / normalization risk** (Illich 1973; Turkle 2015; Hui 2016). The plugin's existence contributes to the normalization of LLM-mediation in cognitive domains where it was historically absent. The plugin takes the *contestable but defensible* position that architectural commitments to artist autonomy (refusal to rank, IRON RULE on human decision, lineage opt-out) place it on the convivial side. This is the position to be argued, not a fact.
6. **Bounded user population.** Per the user-asymmetry scope above. The plugin does not market beyond its scope.

Full detail: v0.2 synthesis spec §6.

---

## Failure modes the plugin makes visible

Three failure modes documented across the AI-creativity-tools literature and inherited mitigations:

1. **Frame-lock** — ask the AI to challenge its own thesis and every round stays inside the frame you set. The Devil's Advocate inside `rehearsal` attacks arguments, never premises. The persona-collapse detector flags when all four personas converge on a single voice.
2. **Sycophancy under pushback** — the model concedes too quickly when pressed, treating "the user pushed back" as evidence the attack was wrong rather than as persistence. The inherited **Concession Threshold Protocol** scores rebuttals 1–5; concession only at ≥4; no consecutive concessions.
3. **Intent misdetection** — the Socratic mentor tries to converge and produce deliverables when you are still exploring. The **Intent Detection Layer** classifies exploratory vs goal-oriented every 3 turns; exploratory mode disables auto-convergence.

The **Dialogue Health Indicator** self-checks every 5 turns for agreement spirals, premature convergence, and conflict avoidance, and injects a challenge when the pattern is detected.

---

## Citation faithfulness (lineage entries)

Lineage entries are anchored — artist name + work / text title + venue-date or publication. **No fabricated DOIs.** The L3 citation-faithfulness machinery is inherited from the parent suite and unchanged. Where the plugin is uncertain, entries are tagged `(verify)`; the artist must independently confirm before downstream use.

Note: hallucination risk is *higher* for art entities than for academic-DOI entities — see the measured-harm disclosure above. The plugin treats this as an open architectural problem to be addressed in v0.2 (runtime grounding) rather than a solved one.

---

## Languages

- **English** (default).
- **Korean** — Socratic mode and the auto-routing in natural-language entries use intent-based activation that works across languages (detects meaning, not specific keywords). The `lineage` mode routes Korean / East-Asian sources first on Korean sessions.

---

## Academic contribution and venue path

Per v0.2 synthesis spec §4.1, four claims:

- **Claim A** (Methodological) — an executable tradition-tag reference layer schema.
- **Claim B** (Design-research) — five architectural choices encoding PaR commitments.
- **Claim C** (Epistemological) — cognitive scaffold position (Clark & Chalmers; Malafouris; Penny).
- **Claim D** (Negative / boundary) — pre-studio articulation phase as structurally distinct from downstream PaR phases.

**Venue path (revised 2026-05-25 — conceptual paper first, empirical track later):**

1. ***Aslib Journal of Information Management* (Aslib JIM, Emerald)** — **primary, v0.1 publication.** **Conceptual paper** classification (4,000–10,000 words, structured abstract, no user-study required). Working draft in [`art-project_paper/`](art-project_paper/).
2. ***Digital Creativity*** (Routledge / T&F) — sibling methods paper, ~7,000 words. Submitted after Aslib JIM is in review.
3. ***ACM Creativity & Cognition* 2027 / 2028** — empirical track. Requires Study 1 (CSI + NASA-TLX pilot, N=12) plus longitudinal study; activates after the conceptual paper is submitted.
4. ***Journal for Artistic Research (JAR)*** — exposition (not traditional article). After Phase 5 publication establishes the framework.
5. ***Leonardo* / *ISEA* / *SIGGRAPH Art Papers*** — practitioner-facing, once longitudinal artist data exists.

See v0.2 spec §4.2 + §5 (evaluation protocol).

---

## Repo structure

```
art-project/
├── art-ideation/                                          # The single skill
├── shared/references/                                     # cross-skill references
│   ├── art_ideation_methodology.md                        # the v0.2 reference layer
│   ├── creative_art_terminology_glossary.md
│   ├── intent_clarification_protocol.md
│   └── protected_hedging_phrases.md
├── commands/                                              # 6 slash commands
├── skills/art-ideation                                    # symlink → ../art-ideation
├── agents/synthesis_agent.md                              # symlink → ../art-ideation/agents/synthesis_agent.md
├── .claude-plugin/{plugin.json, marketplace.json}
├── docs/design/
│   ├── 2026-05-24-art-project-v0.2-synthesis-spec.md      ← READ FIRST
│   ├── 2026-05-24-art-project-v0.1-pivot-spec.md          ← superseded
│   └── 2026-05-22-art-paper-v0.1-fork-spec.md             ← earlier (paper-era)
├── art-project_paper/                                     # maintainer's working paper (Aslib JIM) — NOT part of plugin
├── ref/academic-research-skills/                          # pristine ARS reference for diffing
├── POSITIONING.md
├── MODE_REGISTRY.md
├── QUICKSTART.md
├── CHANGELOG.md
├── LICENSE                                                # CC-BY-NC 4.0
└── README.md / README.ko-KR.md
```

---

## License

[CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Share + adapt + attribute, non-commercial use only.

**Attribution format:**

```
art-project (Version 0.1.0-ideation) [Computer software].
Pivoted from art-paper v0.1.0 (Joon-Hyung Bae),
itself forked from Academic Research Skills (Cheng-I Wu).
https://github.com/joonhyungbae/art-project
Companion paper: docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md.
```

---

## Provenance & contributors

**art-project maintainer** — the v0.2 design synthesis (Frayling layered hybrid self-positioning, cognitive-scaffold framing, user-asymmetry scope, tradition-tag-with-Authentic-Practice-Boundary architecture, six-mode reshape, measured-harm disclosure) is the work of an exhibiting artist, author of practice-based art papers at peer-reviewed venues, and AI researcher. Identity, affiliation, and specific venues are withheld while the accompanying methodology paper is under double-blind review; full attribution will be restored once review is complete.

**Pivoted from — art-paper v0.1.0** ([Joon-Hyung Bae](https://github.com/joonhyungbae)). The art-paper suite was the SIGGRAPH Asia Art Papers paper-authoring distribution; it has been *dropped* in this pivot. The art-paper code remains in this repo's git history; a future `art-paper` sibling distribution may re-publish it as a separate plugin.

**Upstream — Academic Research Skills (ARS).** art-paper was forked from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2 by [Cheng-I Wu (吳政宜)](https://github.com/Imbad0202). The genre-neutral safety machinery (L3 citation-faithfulness gate, Concession Threshold Protocol, Dialogue Health Indicator, intent detection, routing discipline) is inherited unchanged. Pristine ARS reference at [`ref/academic-research-skills/`](ref/academic-research-skills/).

**Four-agent design critique** (2026-05-24) — the v0.2 design was produced by synthesizing four specialist agent critiques: artistic-research methodologist (PaR / Frayling / Borgdorff / Sullivan jurisdiction), HCI / AI-creativity researcher (Shneiderman / Cherry-Latulipe / Davis / Wordcraft-Sparks lineage), practicing-artist studio-side review (real-use scenarios), Devil's Advocate (Penny / Ingold / Borgdorff / Wittgenstein / Illich attacks on the premise). The synthesis is the maintainer's; credit to the four critiques for surfacing the failure modes addressed in v0.2.

**Upstream ARS contributors** whose ARS-era work this project continues to benefit from: [@aspi6246](https://github.com/aspi6246) (read-only constraint + anti-pattern codification patterns), [@mchesbro1](https://github.com/mchesbro1) and [@cloudenochcsis](https://github.com/cloudenochcsis) (reviewer reference lists), [@eltociear](https://github.com/eltociear) and [@xpfo-go](https://github.com/xpfo-go) (upstream README translations).

---

## Changelog (recent)

See [CHANGELOG.md](CHANGELOG.md) for full history.

- **v0.1.0-ideation** (2026-05-24) — pivot from art-paper to art-project (pre-studio articulation scaffold). Drops paper-authoring scope (art-paper / art-reviewer / art-pipeline skills); pivots `art-inquiry` → `art-ideation` with six v0.2 modes; rebuilds the reference layer with positionality + Tensions + Authentic Practice Boundaries + restored critical edge on Penny / Borgdorff; adds HCI prior-art section; ships measured-harm disclosure.
- **v0.1.0** (2026-05-22) — art-paper fork from ARS v3.9.4.2 (now superseded; retained as provenance in CHANGELOG).
