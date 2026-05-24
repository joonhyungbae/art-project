# art-project

A Claude Code plugin: a **pre-studio articulation scaffold** for practice-based artistic research. **Not an ideation engine.** The Penny / Ingold / Borgdorff critique that artistic ideation is non-linguistic, material, and inseparable from making is accepted; the plugin scopes itself to the propositional work *around* ideation. Pivoted from art-paper v0.1.0 (itself forked from academic-research-skills v3.9.4.2); paper-authoring scope dropped.

> **Design spec:** [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](../docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).
> v0.1 pivot spec ([`2026-05-24-art-project-v0.1-pivot-spec.md`](../docs/design/2026-05-24-art-project-v0.1-pivot-spec.md)) is superseded; retained for provenance.

## Skill (one)

| Skill | Purpose | Modes |
|---|---|---|
| `art-ideation` v0.1.0 | Pre-studio articulation scaffold | `socratic`, `provoke`, `lineage`, `brief`, `rehearsal`, `full` (project file) |

## Self-positioning (Frayling layered hybrid)

- **Tool layer — research FOR art.** The plugin as software is an instrument for use by practice-based artists.
- **Reference layer — research INTO art.** [`shared/references/art_ideation_methodology.md`](../shared/references/art_ideation_methodology.md) is a second-order synthesis of how prior literature theorizes artistic ideation.
- **Design-choice layer — research THROUGH art/design.** The architectural choices (generation-evaluation separation, tension-over-ranking, lineage-with-opposition, formative-not-decisional self-critique rehearsal, tradition-tag attribution with Authentic Practice Boundaries) are propositional claims about how AI assistance in PaR ideation should be architected.

## Epistemological position

**Cognitive scaffold** (Clark & Chalmers 1998; Malafouris 2013; Penny 2017). Neither inert tool nor co-author. The plugin operates *adjacent to* embodied practice, in the para-artistic space of articulation work.

## User asymmetry scope

For artists where **propositional articulation is a bottleneck**: early-career artists; second-language writers; artist-researchers preparing PaR doctoral expositions; artists under grant / residency deadline; artists for whom external scaffolding helps; collectives mid-project. **Not** a universal art-ideation tool; structurally unsuitable for artists whose articulation is already fluent, and for traditions where articulation is constitutively unwanted (improvisational, ritual, oral).

## Reference layer (what makes this art-ideation-grounded)

The shared reference layer lives in `shared/references/`:

- [`art_ideation_methodology.md`](../shared/references/art_ideation_methodology.md) — 25+ entries across general creativity theory (A), design methodology (B), art-specific methods (C), media-art / generative-art (D), Korean / East-Asian context (E); plus HCI prior-art (F). Each entry: tradition tag, ideation mechanism, **Authentic Practice Boundary** (what the cited method requires that the plugin defers to human execution), **contested in** field, skill hook. v0.2 additions: positionality opening, Tensions section (6 named inter-entry conflicts), inductive coding rationale for the 5+1 cross-cutting mechanisms, restored critical edge on D8 Penny / C7 Barrett & Bolt / C6 Smith & Dean / C4 Borgdorff.
- [`creative_art_terminology_glossary.md`](../shared/references/creative_art_terminology_glossary.md) — practice-based vs practice-led, generative / interactive / autonomous, authorship / credit, copyright / exhibition-rights, reception terms.
- [`intent_clarification_protocol.md`](../shared/references/intent_clarification_protocol.md) — routing discipline.
- [`protected_hedging_phrases.md`](../shared/references/protected_hedging_phrases.md) — hedging discipline for novelty / capability claims.

**Output:** Markdown (default). PDF / DOCX export deferred to v0.2.

## Routing Discipline

**Step 0 — Escape hatch:** if the user's first message begins with `[direct-mode]` (case-insensitive, byte-0 after whitespace strip), strip it and route directly per explicit intent.

Otherwise classify:
1. **Explicit clear intent** — `/art-*` slash command or unambiguous trigger ("guide me through a new project", "draft a concept brief", "rehearse critique") → route directly.
2. **Ambiguous, no materials** → clarify per [`intent_clarification_protocol.md`](../shared/references/intent_clarification_protocol.md).
3. **Cross-mode materials** → suggest the most upstream applicable mode and let the artist confirm.

## Routing Rules (mode selection)

| Situation | Recommended mode |
|---|---|
| No concept yet, vague pull | `socratic` |
| Partial concept, feels stuck | `provoke` |
| Has stated candidate lineage, wants extension | `lineage` |
| Has enough material, needs a proposition document | `brief` |
| Has a draft brief, wants rehearsal before submission | `rehearsal` |
| Wants the whole arc across weeks | `full` (project file) |
| Ambiguous, no materials | `socratic` (default — guides first) |
| Mode unclear, natural-language entry | auto-route via intent detection; **announce the routing transparently** |

When auto-routing, announce: *"Starting in socratic mode (exploratory intent detected). I'll suggest switching modes when the dialogue suggests it."* Mode transitions are also announced and offered, never silently performed.

## Key Rules (art-ideation genre)

- The plugin produces **language**, not artworks. The artwork is the artist's; ideation happens in the studio.
- **Tradition tags indicate prompt grounding and style affinity, NOT causal attribution.** See honesty paragraph in [`art_ideation_methodology.md`](../shared/references/art_ideation_methodology.md).
- Each tradition carries an **Authentic Practice Boundary** naming what the cited method requires that the plugin defers to human execution (e.g. Cage: plugin proposes the chance procedure, artist throws the dice; LeWitt: plugin prompts the artist to write the instruction, does not author it; Oblique Strategies: physical deck irreplaceable).
- **`lineage` mode requires artist-supplied initial candidates** before extending; never proposes lineage from impulse alone. Mandatory training-data bias header on every Lineage Map. Korean / East-Asian default routing on Korean sessions. `--no-lineage` opt-out always available.
- **`brief` mode stay-rough default** — prose stays in the artist's voice; no auto-smoothing. Empty fields are reported as gaps, not filled with plausible-sounding text. `--polish` is opt-in only.
- **`rehearsal` mode formative-not-decisional** — mandatory disclaimer header on every output; persona-collapse detector; architectural friction after repeated use on same concept.
- **`full` mode is a long-running project file** across days/weeks (Smith & Dean iterative cyclic web). Each session does one mode at most. No single-session pipelining.
- The inherited **L3 citation-faithfulness gate** applies to lineage entries — no fabricated artists, exhibitions, theories. Use `(verify)` when uncertain.
- **Refusal to rank** — provocations, lineage entries, brief drafts, rehearsal critiques. The artist decides.
- **Default output language matches user input.**

## IRON RULES (genre-neutral, inherited from parent suite)

- **No auto-convergence under exploratory intent** (socratic mode).
- **Preserved unhelpfulness** on Oblique-style provocations (provoke mode goes silent after the provocation; no auto-interpretation).
- **Concession Threshold Protocol** for the Devil's Advocate inside `rehearsal` — no premature concessions; concession only at rebuttal score ≥4 on the 1–5 scale.
- **Dialogue Health Indicator** every 5 turns — agreement spirals, premature convergence, conflict avoidance — injects a challenge when pattern detected.
- **Intent detection** every 3 turns — exploratory vs goal-oriented classification.

## Measured-harm disclosure (model-card style)

Six harm classes — see [`POSITIONING.md`](../POSITIONING.md) and v0.2 synthesis spec §6:

1. Lineage hallucination per sub-domain (anglophone media art / Korean media art / performance art — others).
2. Training-data canon bias (operational form: `lineage` mode header).
3. Simulation-pedagogy risk (`rehearsal` — Schön 1983 cited; mitigations: disclaimer + friction + persona-collapse detector).
4. Authorship-perception shift (Wordcraft / Sparks / ghostwriter literature).
5. Conviviality / normalization risk (Illich 1973; Turkle 2015; Hui 2016).
6. Bounded user population (see User asymmetry scope above).

## Repo structure

```
art-project/
├── art-ideation/                         # The single skill
│   ├── SKILL.md                          # 6-mode specification
│   ├── agents/                           # inherited agents (some v0.2-rewrite pending)
│   ├── references/                       # skill-local references
│   ├── templates/                        # research_brief_template.md (v0.2-rewrite pending → concept_brief_template.md)
│   └── examples/                         # socratic_guided_research.md (v0.2-rewrite pending)
├── shared/
│   └── references/                       # cross-skill references
│       ├── art_ideation_methodology.md   # the load-bearing v0.2 reference
│       ├── creative_art_terminology_glossary.md
│       ├── intent_clarification_protocol.md
│       └── protected_hedging_phrases.md
├── skills/art-ideation                   # symlink → ../art-ideation
├── agents/synthesis_agent.md             # symlink → ../art-ideation/agents/synthesis_agent.md
├── commands/                             # 6 slash commands (art-socratic, art-provoke, art-lineage, art-brief, art-rehearsal, art-ideate)
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── docs/design/
│   ├── 2026-05-24-art-project-v0.2-synthesis-spec.md  ← READ FIRST
│   ├── 2026-05-24-art-project-v0.1-pivot-spec.md      ← superseded; provenance
│   └── 2026-05-22-art-paper-v0.1-fork-spec.md         ← earlier (paper-era); provenance
├── art-project_paper/                    # maintainer's working paper (Aslib JIM submission) — NOT part of the plugin
├── ref/academic-research-skills/         # pristine ARS reference for diffing
├── POSITIONING.md                        # public positioning
├── MODE_REGISTRY.md                      # 6-mode single source of truth
├── README.md, README.ko-KR.md
├── QUICKSTART.md
├── CHANGELOG.md
└── LICENSE                               # CC-BY-NC 4.0
```

## Academic contribution (committed)

Per v0.2 synthesis spec §4.1, four claims:

- **Claim A** (Methodological): executable tradition-tag reference layer schema.
- **Claim B** (Design-research): five architectural choices encoding PaR commitments (generation-evaluation separation; tension-over-ranking; lineage-with-opposition; formative self-critique rehearsal; tradition-tag-with-Authentic-Practice-Boundary).
- **Claim C** (Epistemological): cognitive scaffold position (Clark & Chalmers; Malafouris; Penny).
- **Claim D** (Negative / boundary): pre-studio articulation phase as structurally distinct from downstream PaR phases.

**Venue path (revised 2026-05-25 — conceptual paper first, empirical track later):**
1. **Aslib JIM Conceptual paper** (Emerald, no user-study requirement) — *primary, v0.1 publication.* Conceptual classification, 4,000–10,000 w, structured abstract.
2. ***Digital Creativity* (Routledge)** — sibling methods paper, after Aslib JIM is in review.
3. **ACM C&C 2027 / 2028** — empirical track activates after the conceptual paper is submitted; requires Study 1 (N=12 CSI / NASA-TLX pilot).
4. ***Journal for Artistic Research (JAR)*** exposition — after Phase 5 publication establishes the framework.
5. ***Leonardo* / *ISEA* / *SIGGRAPH Art Papers*** — practitioner-facing, after longitudinal data exists.

## Version Info

- **Plugin version:** 0.1.0 (design synthesis 2026-05-24)
- **Pivoted from:** art-paper v0.1.0
- **Forked from (ultimately):** academic-research-skills v3.9.4.2
- **License:** CC-BY-NC 4.0
- **Suite name:** `art-project`
