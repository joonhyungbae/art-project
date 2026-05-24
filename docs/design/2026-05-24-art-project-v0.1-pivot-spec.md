# art-project v0.1 — Pivot Spec: from art-paper authoring to art-project ideation

> **Status — SUPERSEDED (2026-05-24, same-day revision).**
> This v0.1 pivot spec is superseded by [`2026-05-24-art-project-v0.2-synthesis-spec.md`](2026-05-24-art-project-v0.2-synthesis-spec.md) on the following points:
> - §1.2 ("What 'ideation' means here") → v0.2 §1.1 reframes the plugin as a **pre-studio articulation scaffold**, not an ideation engine. The Penny / Ingold / Borgdorff critique that ideation is non-linguistic, material, and inseparable from making is *accepted*; the plugin scopes itself to the propositional work *around* ideation.
> - §3 mode design → v0.2 §2 renames `panel` → `rehearsal` (commit to method-not-evaluation), reshapes `lineage` to require artist-supplied initial candidates + bias disclosure, rebuilds the `brief` schema with epistemic fields (proposition / anti-proposition / disconfirmation / Frayling-type) + stay-rough default, and converts `full` from a single-session chain to a long-running project file.
> - §3 "methodology provenance" → v0.2 §2.3 renames to **"tradition tag"** (HCI critique: the v0.1 term overstates causal attribution) and adds per-method **Authentic Practice Boundaries**.
> - §1.2 epistemological framing → v0.2 §1.3 adopts **cognitive scaffold** position (Clark & Chalmers 1998; Malafouris 2013).
> - §1.2 + new — v0.2 §1.4 adds an explicit **user-asymmetry scope statement** (the plugin is for artists where propositional articulation is a bottleneck, not all artists).
> - §2.2 Goals — v0.2 §1.2 declares a **Frayling layered hybrid self-positioning** (tool layer = FOR; reference layer = INTO; design-choice layer = THROUGH).
> - §6 contribution claim → v0.2 §4 commits to Claims A + B + C + D and a specific venue path (*ACM C&C 2027* primary, *Digital Creativity* parallel, *JAR* as exposition).
> - §7 phase plan + new — v0.2 §5 adds an explicit **evaluation protocol** (Study 1 CSI/NASA-TLX pilot N=12 required for v0.1 publication, Studies 2–4 + longitudinal deferred to v0.2).
> - §7 + new — v0.2 §6 adds a **measured-harm disclosure** (model-card style: lineage hallucination rate, canon bias, simulation-pedagogy risk, authorship-perception shift, conviviality position, bounded user population).
> - §8 OQs — v0.2 §8 closes OQ2 / OQ3 / OQ5 and adds OQ6 / OQ7 / OQ8 / OQ9 / OQ10.
>
> The v0.1 spec is retained for provenance — it records the design state immediately before the four-agent critique that produced v0.2. Read v0.2 first.

**Status:** Design draft (Phase 0 — superseded; see banner above)
**Date:** 2026-05-24
**Target:** art-project v0.1 (pivoted from art-paper v0.1.0, which was itself forked from academic-research-skills v3.9.4.2)
**Scope:** Re-specialize the suite from **downstream paper authoring** (SIGGRAPH Asia Art Papers) to **upstream art-project ideation** — the conception / brainstorming phase before any artwork is made or paper is written. Drop the paper-writing, jury-review, and pipeline-orchestration skills. Keep, expand, and rename the upstream inquiry skill into a dedicated ideation engine grounded in **prior research on artistic ideation methodology**.
**Reference baseline:** art-paper v0.1.0 (current repo state); pristine ARS reference remains at `ref/academic-research-skills/` for diffing.
**Pivot principle:** A Claude plugin that helps an artist **start** a project — articulate the impulse, generate provocations, map lineage, draft a Concept Brief, and stress-test it via a multi-persona panel — without forcing the artist into paper-writing scaffolding they may not need at this stage.

---

## 1. Background & Motivation

### 1.1 Why pivot

art-paper v0.1.0 is a strong **downstream** tool: it scaffolds the work that happens once an artist already knows what the work is (or will be), and is writing it up for SIGGRAPH Asia Art Papers. But the art-paper pipeline only really activates at the point where there is already:

- A work (or planned work) clear enough to be documented.
- A provocation articulable in language.
- A position takeable inside an existing discourse.

In practice, the **hardest, riskiest, most generative** phase of an art project sits **earlier** than that: the period when an artist has a pull, a fragment, a constraint, a question — but no work yet, no language for the work, no claim about the work. Existing AI tooling tends to skip past this phase and demand premature articulation. The art-paper suite, as currently shaped, also skips it.

**This pivot moves the suite to that earlier phase.** Paper authoring is dropped (it can be re-added as a sibling distribution if needed; the art-paper code remains in git history). The new suite's job is to **help an artist begin a project**.

### 1.2 What "ideation" means here

Not the brainstorm-app sense of "give me 50 random ideas". Ideation in art is closer to:

- **Articulating an impulse** that arrived as image, sensation, technical itch, or unease — into something the artist can act on without flattening it.
- **Generating provocations** that hold tension (what-if-the-machine-mourned, what-if-the-camera-refused-to-look) rather than mere variations.
- **Locating the work in a lineage** of precedent artists and ideas — not to imitate, but to know what room one is walking into.
- **Drafting a Concept Brief** that survives contact with collaborators, curators, and the artist's own future self.
- **Stress-testing the concept** through perspectives the artist cannot easily simulate alone (curator, practitioner peer, theorist, devil's advocate).

This is supported by an established body of work — Boden's three creativity types, Finke et al.'s Geneplore model, Eno & Schmidt's Oblique Strategies, LeWitt's conceptual-art writings, Frayling / Borgdorff / Sullivan on artistic research, Cage's chance operations, Dunne & Raby's speculative design, and others. The new suite models these as a **reference layer**, not as a fixed pipeline.

### 1.3 What changes vs. what stays

| Axis | art-paper v0.1.0 | art-project v0.1 |
|---|---|---|
| Phase of work | downstream: write & review a paper | **upstream: conceive a project** |
| Primary output | acmart LaTeX → PDF | Concept Brief (Markdown), Provocation Set, Lineage Map, Panel Critique |
| Primary evidence | the artwork (documented) | the artist's own pull + the lineage they sit in |
| Skills | 4 (inquiry, paper, reviewer, pipeline) | **1** (`art-ideation`) with 6 modes |
| Reviewer model | SIGGRAPH Asia jury (acceptance decision) | **Panel critique** (curator + practitioner + theorist + devil's advocate) — formative, not decisional |
| Citation format | ACM Reference Format (mandatory) | Lightweight references for lineage mapping; ACM/MLA/Chicago available but optional |
| Genre layer | "the artwork as primary evidence" | **"prior art-ideation methodology as the engine"** |
| Output toolchain | acmart, LaTeX, PDF | Markdown by default; format-convert deferred to v0.2 |

**Retained, unchanged, from the parent suites:**

- The L3 citation-faithfulness machinery (lineage references must anchor to a verifiable work/text — no fabricated artists, exhibitions, or theories). IRON RULE preserved.
- The Socratic intent-detection layer (exploratory vs goal-oriented every 3 turns; auto-convergence disabled in exploratory mode).
- The Devil's Advocate concession-threshold protocol (no premature concessions; concession only at rebuttal score ≥4).
- The Dialogue Health Indicator (self-check every 5 turns for premature convergence / agreement spirals).
- The routing discipline + intent clarification protocol.
- The two-channel AI disclosure idea is preserved in principle — but at the ideation stage, the relevant disclosure is **"AI was used to ideate"** as a single channel; the artwork-making and paper-writing channels become relevant later (out of scope for v0.1).

## 2. Goals & Non-Goals

### 2.1 Goals (v0.1)

1. **Drop paper-authoring scope**: remove `art-paper/`, `art-reviewer/`, `art-pipeline/`, `art-project_paper/` and their commands. The git history retains them; a future `art-paper` plugin can be re-published as a sibling distribution.
2. **Pivot `art-inquiry` into `art-ideation`** with six modes (§3).
3. **Build a methodology reference layer** at `shared/references/art_ideation_methodology.md` modeling prior research on artistic ideation (Boden, Geneplore, Oblique Strategies, LeWitt, Frayling/Borgdorff/Sullivan, Cage, Dunne & Raby, etc.) — the agent reads this; the user can read it directly as a primer.
4. **Rebrand the plugin**: name → `art-project`; commands → `/art-*` (ideation-focused); marketplace metadata, README, POSITIONING, MODE_REGISTRY all updated.
5. **Preserve all genre-neutral safety mechanisms** unchanged: citation-faithfulness (L3), intent detection, concession-threshold, dialogue-health, routing discipline.

### 2.2 Non-Goals (v0.1)

- Authoring a paper from the Concept Brief. (Out of scope; a separate `art-paper` plugin can consume the Brief later.)
- Generating image / sound / video sketches. The output is **language** — questions, briefs, lineage, critique — that an artist takes back to their studio.
- Auto-deciding what the work should be. The artist decides. The plugin offers structured material.
- Multi-language UI. Korean and English supported via intent-based activation; deeper localization deferred.
- Paid-tier or hosted-service integrations.

## 3. Skill Design: `art-ideation`

One skill, six modes. Naming follows the parent suite's pattern; the directory is `art-ideation/`.

| Mode | Spectrum | Output | Oversight | Triggers (illustrative) |
|---|---|---|---|---|
| `socratic` | Originality | Dialogue transcript + **Concept Pull Map** (impulses, fragments, constraints, refusals named) | Very High | "guide me", "I don't know what I'm doing yet", "help me find what the work wants to be" |
| `provoke` | Originality | **Provocation Set** (8–20 generative what-if / Oblique-Strategies-style cards, each held in tension with a counter-formulation) | High | "give me provocations", "what if", "throw constraints at me" |
| `lineage` | Fidelity | **Lineage Map** (5–15 precedent artists/works/texts with positional notes: kin, opposition, blind-spot, unexpected-neighbor), each entry citation-anchored | Medium | "who else has done this", "what's the lineage", "position my work" |
| `brief` | Balanced | **Concept Brief** (working title, provocation, situated argument, intended encounter, materials/medium/scale, lineage anchor, risk/refusal) | High | "draft a concept brief", "write up what I have so far", "I need a one-pager for [grant / collaborator]" |
| `panel` | Balanced | **Panel Critique** — Curator + Practitioner-peer + Theorist + Devil's Advocate + Chair-synthesis | High | "stress-test this", "critique the concept", "panel review" |
| `full` | Balanced | Full ideation pass: socratic → provoke → lineage → brief → panel, with explicit user checkpoints between each | Very High | "start a new project", "I want to ideate from scratch", "run the full ideation" |

**Default routing rule:** When intent is ambiguous and no concept exists yet, **prefer `socratic`**. When a partial concept exists, prefer `provoke` or `lineage`. When the artist asks for a deliverable, prefer `brief`. When the artist asks for criticism, prefer `panel`. `full` is opt-in.

### 3.1 Mode mechanics — how each mode draws on the methodology reference

Each mode is wired to specific entries in `shared/references/art_ideation_methodology.md`:

- **`socratic`** consumes the practice-based research literature (Frayling, Borgdorff, Sullivan, Smith & Dean, Barrett & Bolt) and the Csikszentmihalyi systems model. The mentor's questions surface the *domain × field × person* triangle: what tradition the artist is talking to, what gatekeepers/audiences they imagine, what they themselves bring that nobody else does.
- **`provoke`** consumes Oblique Strategies (Eno & Schmidt), SCAMPER, de Bono's lateral thinking, Cage's chance operations, Boden's combinational / exploratory / transformational creativity, Dunne & Raby's speculative design. The provocation engine generates cards in the style of these methods, **with named provenance** — every provocation says which tradition produced it, so the artist can pull the thread further.
- **`lineage`** consumes the practice-based research literature + the art-and-technology lineage (Couchot, Popper, Penny, Manovich, Paul, Galanter, Whitelaw, Reas/Fry) + LeWitt's conceptual-art writings + Bauhaus vorkurs. Lineage entries are anchored to verifiable works/texts (citation-faithfulness L3 applies).
- **`brief`** consumes all of the above, plus Bogart's Viewpoints (for the *encounter* dimension — what spatial, temporal, kinesthetic relation the work proposes), Corita Kent's rules + Saltz's rules (for the *risk / refusal* dimension — what the artist refuses).
- **`panel`** uses the parent suite's multi-persona reviewer machinery, **re-scoped from juried-acceptance to formative critique**. No accept/reject decision is rendered; the output is structured friction.

### 3.2 What the skill does NOT do

- Does **not** decide what is "good art".
- Does **not** rank provocations or pick the winner.
- Does **not** suppress contradictions; provocations are produced **in tension** with counter-formulations.
- Does **not** treat lineage as marketing ("you're the next X"); lineage is positional, including *opposition* and *blind-spot* entries.
- Does **not** push to deliverables. The Socratic mode can run indefinitely if the artist is still exploring.

## 4. Reference Layer (`shared/references/`)

### 4.1 New (Phase 1)

- **`art_ideation_methodology.md`** — the key new reference. Authored from the Phase-0 research pass; covers (a) general creativity / cognition theory, (b) design / planning methodology, (c) art-domain-specific methods, (d) media-art / generative-art specifics, (e) East-Asian / Korean context. Each entry: author/year, core idea, **ideation mechanism** (what it actually does), **integration hook** (which mode consumes it). Closes with a **cross-cutting mechanisms** section (3–5 patterns the methods share — e.g. constraint-based detour, heterogeneous-domain collision, positioning-within-a-lineage), which forms the design backbone of the ideation modes.

### 4.2 Retained (with light edits — ideation framing)

- `creative_art_terminology_glossary.md` — terminology for practice-based / practice-led / generative / interactive / authorship / collaboration. Useful at ideation, kept.
- `intent_clarification_protocol.md` — routing discipline. Unchanged; the skill set is smaller now so routing is simpler.
- `protected_hedging_phrases.md` — keeps hedging discipline for novelty / capability claims that arise even at ideation ("first work to…", "real-time", "autonomous").

### 4.3 Dropped (paper-authoring scope)

- `acm_reference_format.md` — paper citation format. Drop from default; v0.2 may reintroduce for cite-while-you-ideate.
- `art_paper_structure_patterns.md` — paper structures. Drop.
- `art_research_evidence_model.md` — about defending claims about an existing artwork; no artwork yet at ideation.
- `siggraph_acm_disclosure.md` — venue-specific. Drop.
- `irb_terminology_glossary.md`, `psychometric_terminology_glossary.md` — ARS-era empirical scope. Drop.
- `word_count_conventions.md` — paper length budgets. Drop.

## 5. Plugin Packaging Rebrand (Phase 3)

| File | Change |
|---|---|
| `.claude-plugin/plugin.json` | name → `art-project`; description → "Claude plugin for art-project ideation"; keywords → ideation / concept-development / practice-based / art-and-technology |
| `.claude-plugin/marketplace.json` | mirror plugin.json; single plugin entry pointing to `./` |
| `commands/` | Drop all 15 paper commands. Add: `/art-ideate` (full mode), `/art-socratic`, `/art-provoke`, `/art-lineage`, `/art-brief`, `/art-panel`. Model routing: opus for `socratic` / `panel` / `full` (high-leverage), sonnet for `provoke` / `lineage` / `brief`. |
| `agents/` | Keep `synthesis_agent`, drop `report_compiler_agent` and `research_architect_agent` (paper-scoped). Add `panel_persona_agent` (the four-persona critique panel) and `provocation_engine_agent`. |
| `.claude/CLAUDE.md` | rewrite project instructions for art-project framing — single skill, six modes, methodology-reference grounding |
| `POSITIONING.md`, `README.md`, `README.ko-KR.md`, `QUICKSTART.md`, `MODE_REGISTRY.md`, `CHANGELOG.md` | rewrite for art-project framing |
| `art-paper/`, `art-reviewer/`, `art-pipeline/`, `art-project_paper/` skill dirs | `git rm -r` (history retained) |
| `art-inquiry/` skill dir | `git mv` to `art-ideation/`; rewrite SKILL.md for the six new modes; replace agent prompts to consume `art_ideation_methodology.md` |
| `skills/` symlinks | re-point to the new `art-ideation/` only |

## 6. Preserved Unchanged (genre-neutral skeleton)

- L3 citation-faithfulness machinery (lineage citations anchored, no fabrication).
- Intent detection (exploratory vs goal-oriented).
- Concession-threshold protocol for Devil's Advocate within the panel mode.
- Dialogue Health Indicator.
- Routing discipline + intent clarification protocol.
- Material Passport handoff schemas — **trimmed**: pipeline is gone, but the schema is reused for cross-session resume of a long Socratic dialogue.

## 7. Phase Plan

- **Phase 0** (this doc): spec + decisions. *In progress.*
- **Phase 1:** author `shared/references/art_ideation_methodology.md` from the research pass; trim the reference layer (drop paper-scoped files).
- **Phase 2:** rebrand the plugin packaging (plugin.json, marketplace.json, commands, agents). Drop the three paper-authoring skill dirs. Rename `art-inquiry/` → `art-ideation/`.
- **Phase 3:** rewrite `art-ideation/SKILL.md` for the six new modes; rewrite agent prompts to consume the new reference.
- **Phase 4:** rewrite project-level docs (POSITIONING, README, MODE_REGISTRY, CLAUDE.md, QUICKSTART, CHANGELOG).
- **Phase 5:** end-to-end validation with one sample ideation pass (e.g. "I want to make something about insomnia and surveillance, I don't know what yet" → full mode).

## 8. Open Questions (track, do not block Phase 1)

- **OQ1: License.** art-paper ships CC-BY-NC 4.0 (noncommercial restriction). Should art-project keep CC-BY-NC, or move to a more permissive license given the upstream-only scope? Default: keep CC-BY-NC for symmetry.
- **OQ2: Methodology reference as user-facing primer.** Should `art_ideation_methodology.md` be promoted to a top-level `METHODOLOGY.md` so artists read it directly (not just the agent)? Default: keep in `shared/references/` for v0.1, link prominently from README.
- **OQ3: Panel composition.** v0.1 panel = Curator + Practitioner-peer + Theorist + Devil's Advocate. Should a fifth persona (e.g. "Audience" / "Funder" / "Technologist") be added optionally? Default: keep four for v0.1; allow user-supplied custom personas in v0.2.
- **OQ4: Output format.** v0.1 outputs Markdown only. Should the Concept Brief also export to a PDF / DOCX template suitable for grants? Default: defer to v0.2.
- **OQ5: Bridge to art-paper.** Should the Concept Brief have a documented schema (Material Passport-style) so a future art-paper plugin can ingest it? Default: yes — add a minimal schema in Phase 1, even if no consumer exists yet.

## 9. Out of scope for v0.1 (named, parked)

- Generative image / sound / video sketches from the Brief.
- Real-time collaboration (multiple artists ideating together).
- Studio-log integration (importing prior notebooks, sketches).
- Grant-application templates.
- Curator-side ingestion (a curator using the plugin to evaluate submitted Briefs).
