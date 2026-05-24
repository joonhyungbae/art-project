# Changelog

> **Provenance note.** This project is **art-project**, pivoted from **art-paper** v0.1.0 (which was itself forked from **academic-research-skills (ARS)** v3.9.4.2). The pivot dropped the paper-authoring scope. The full parent-suite changelog (ARS v1.0 → v3.9.4.2) is preserved at [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md) and is not re-narrated here.

---

## [0.1.0-ideation] — 2026-05-24 — art-project pivot from art-paper

**Headline:** the suite pivots from **downstream paper-authoring** (art-paper, SIGGRAPH Asia Art Papers) to **upstream pre-studio articulation** (art-project, conception phase). A four-agent design critique (artistic-research methodologist + HCI / AI-creativity researcher + practicing-artist studio-side review + Devil's Advocate) surfaced a self-undermining contradiction in the initial pivot (citing Penny / Ingold / Borgdorff while claiming to perform ideation those theorists define as non-linguistic). The v0.2 synthesis accepts the critique and rescopes the plugin as a **pre-studio articulation scaffold**, not an ideation engine.

### Single most consequential reframe

**"ideation engine" → "pre-studio articulation scaffold".** The plugin does *not* claim to participate in artistic ideation in the Penny / Ingold / Borgdorff sense — actual ideation happens in the studio, with material. The plugin scaffolds the propositional articulation work that surrounds ideation. This single reframe converts the strongest critique (Devil's Advocate Attack 1) into a scope statement.

### Self-positioning (new)

- **Frayling (1993) layered hybrid:** tool layer = research FOR art; reference layer = research INTO art; design-choice layer = research THROUGH art/design.
- **Epistemological position: cognitive scaffold** — Clark & Chalmers (1998), Malafouris (2013), Penny (2017). Neither inert tool nor co-author.
- **User asymmetry scope:** for artists where propositional articulation is a bottleneck (early-career, second-language writers, PaR-doctoral candidates, grant deadline). **Not** a universal art-ideation tool.

### Design specs

- **New:** [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md) — synthesizes the four-agent critique into the canonical v0.2 design.
- **Superseded:** [`docs/design/2026-05-24-art-project-v0.1-pivot-spec.md`](docs/design/2026-05-24-art-project-v0.1-pivot-spec.md) — initial pivot spec; retained as provenance with a superseded-by banner.

### Skill design — 6 modes

- **Single skill:** `art-ideation` (renamed from `art-inquiry`).
- **Six modes:**
  - `socratic` — pre-reflective articulation (distinct from Schön's reflection-in-action); **residue field** added to Concept Pull Map to preserve impulse messiness; **IRON RULE** no auto-convergence under exploratory intent.
  - `provoke` — tradition-tagged provocations with **preserved unhelpfulness** (no auto-interpretation, no ranking); per-method **Authentic Practice Boundary** naming what the cited method requires that the plugin defers to human execution (e.g. Cage: artist throws the dice; LeWitt: artist writes the instruction; Oblique Strategies: physical deck irreplaceable).
  - `lineage` — **requires artist-supplied initial candidates**; mandatory training-data bias header on every output; **Korean / East-Asian default routing** on Korean sessions; clean `--no-lineage` opt-out; honest mode self-description as "retrieval, not ideation".
  - `brief` — **epistemic fields** (proposition / anti-proposition / disconfirmation condition / Frayling-type declaration); **stay-rough default** preserving artist's voice; **no auto-completion** of gaps (acknowledged absence over plausible filler).
  - `rehearsal` *(renamed from `panel`)* — Self-Critique Rehearsal, formative not decisional; mandatory disclaimer header on every output; **persona-collapse detector**; **architectural friction** after 2 invocations / 14 days on same concept; output re-entrant into the Brief (not standalone judgement).
  - `full` — **long-running project file across sessions** (Smith & Dean iterative cyclic web in operational form); one mode per session; cross-session re-entry first-class. The Material Passport machinery is repurposed as the project-file schema.

### Reference layer — `art_ideation_methodology.md` v0.2 rewrite

- **Positionality opening** (new) — names author's situation, source-language situation, separation-vs-integration decision for Section E.
- **"Tradition tag, not provenance" honesty paragraph** (new) — clarifies that tags indicate prompt grounding and style affinity, **not** causal attribution.
- **"Contested in" fields** added to ~28 entries — engages the critical literature on each cited method (e.g. Christensen & Schunn 2007 on SCAMPER's empirical efficacy; Glăveanu 2010 on Boden's trait-property creativity; Galloway 2012 on Manovich's database thesis; Scrivener on Frayling FOR; Huhtamo & Parikka 2011 media archaeology on Popper/Couchot lineage shape).
- **Restored critical edge** on D8 Penny, C7 Barrett & Bolt, C6 Smith & Dean, C4 Borgdorff — v0.1 had sanitized their critical force; v0.2 names them as positions the plugin must *answer to*, not borrow from. The Penny entry in particular acknowledges that his critique of representational paradigms targets the LLM substrate the plugin runs on.
- **Authentic Practice Boundaries** added per cited method.
- **New "Tensions" section** — 6 named inter-entry conflicts:
  - T1 Boden's formalism vs Borgdorff's situatedness
  - T2 IDEO Design Thinking instrumental vs Sullivan / Barrett & Bolt epistemic
  - T3 Cage chance-as-erasure-of-taste vs Bogart Viewpoints-as-trained-attention
  - T4 Galanter effective-complexity vs LeWitt idea-first
  - T5 Western-PaR articulation requirement vs East-Asian yeobaek reserve-for-the-unsaid
  - T6 Tradition-tag-as-affinity vs methodology-as-embodied-craft
- **Inductive coding rationale** for the 5+1 mechanisms (replaces v0.1 assertion); **Appendix A** coding table added; Glăveanu's 5A model mapping noted as alternative theoretical anchor.
- **E3 Yuk Hui cosmotechnics** added; E4–E7 marked pending v0.2 Phase 1 library + consultation work.
- **New Section F — HCI / AI-Creativity-Support-Tools Prior Art** — 18 entries (Shneiderman 2007, Cherry & Latulipe 2014, Frich 2019, Wordcraft, Sparks, TaleBrush, Dramatron, AI Chains, Casual Creators, Davis 2016, Kantosalo & Toivonen 2016, Deterding MICI, Draxler ghostwriter, Amabile CAT, Lu AI Scientist, Mitchell Model Cards, Bender Stochastic Parrots, Zimmerman Research-through-Design). v0.1 had none of these.
- **Mounting matrix updated** — `panel` → `rehearsal`; `full` row added; E3 / E4–E7 included.

### Repo structure changes

- **Renamed:** `art-inquiry/` → `art-ideation/`.
- **Dropped (paper-authoring scope):**
  - Skill dirs: `art-paper/`, `art-reviewer/`, `art-pipeline/`.
  - 15 paper commands: `art-abstract`, `art-artist-statement`, `art-citation-check`, `art-disclosure`, `art-format-convert`, `art-full`, `art-lit-review`, `art-mark-read`, `art-outline`, `art-plan`, `art-reviewer`, `art-revision-coach`, `art-revision`, `art-unmark-read`, `art-work-doc`.
  - 7 paper-scoped shared references: `acm_reference_format`, `art_paper_structure_patterns`, `art_research_evidence_model`, `siggraph_acm_disclosure`, `irb_terminology_glossary`, `psychometric_terminology_glossary`, `word_count_conventions`.
  - 6 paper-scoped agents inside `art-ideation/agents/`: `ethics_review`, `meta_analysis`, `report_compiler`, `research_architect`, `risk_of_bias`, `timeline_extraction`.
  - 10 paper-scoped references inside `art-ideation/references/`: `apa7_style_guide`, `equator_reporting_guidelines`, `ethics_checklist`, `irb_decision_tree`, `systematic_review_protocol`, `systematic_review_toolkit`, `preregistration_guide`, `literature_monitoring_strategies`, `crossref_api_protocol`, `openalex_api_protocol`.
  - 5 paper-scoped templates: `evidence_assessment_template`, `literature_matrix_template`, `preregistration_template`, `prisma_protocol_template`, `prisma_report_template`.
  - 6 paper-scoped examples: `handoff_to_paper`, `policy_analysis`, `review_mode`, `systematic_review`, `fact_check_mode`, `exploratory_research`.
- **Created (new commands):** `art-socratic.md`, `art-provoke.md`, `art-lineage.md`, `art-brief.md`, `art-rehearsal.md`, `art-ideate.md`. Model routing: opus for `socratic` / `rehearsal` / `ideate` (high-leverage); sonnet for `provoke` / `lineage` / `brief`.
- **Symlinks fixed** — broken `skills/creative-*` symlinks (pointing to non-existent paths) removed; clean `skills/art-ideation` → `../art-ideation` created. `agents/synthesis_agent.md` repointed to `../art-ideation/agents/synthesis_agent.md`.
- **Preserved (intentionally):** `art-project_paper/` — the maintainer's working paper draft (Aslib JIM submission) lives in the repo but is **not** part of the plugin distribution. It is a separate writing project.

### Manifest changes

- Plugin name `art-paper` → `art-project` in `.claude-plugin/plugin.json` and `marketplace.json`.
- Description rewritten to reflect the pre-studio articulation scaffold framing.
- Keywords updated: `pre-studio-articulation`, `PaR`, `artistic-research`, `tradition-tag`, `cognitive-scaffold`, `extended-mind`, `creativity-support-tool`, `concept-brief`, `self-critique-rehearsal`, `lineage-positioning`.

### Project-level docs rewritten

- [`POSITIONING.md`](POSITIONING.md) — Frayling layered hybrid, cognitive scaffold, user asymmetry scope, measured-harm disclosure.
- [`MODE_REGISTRY.md`](MODE_REGISTRY.md) — 6 modes; default routing rules; mode-to-reference wiring with Authentic Practice Boundaries.
- [`.claude/CLAUDE.md`](.claude/CLAUDE.md) — project instructions for v0.2.
- This `CHANGELOG.md` — v0.1.0-ideation entry.
- [`README.md`](README.md) / [`README.ko-KR.md`](README.ko-KR.md) — public-facing rewrite.
- [`QUICKSTART.md`](QUICKSTART.md) — usage guide for the 6 modes.

### Academic contribution (committed)

Per v0.2 synthesis spec §4.1, four claims:

- **Claim A** (Methodological) — executable tradition-tag reference layer schema.
- **Claim B** (Design-research) — five architectural choices encoding PaR commitments: generation-evaluation separation (Geneplore + Corita Kent); tension-over-ranking (Bolt's experimental gesture); lineage-with-opposition (Sullivan contextualist); formative-not-decisional self-critique rehearsal (Borgdorff not-yet-knowing); tradition-tag-with-Authentic-Practice-Boundary (addressing the Penny / Ingold critique by declaring the plugin's non-participation in embodied practice).
- **Claim C** (Epistemological) — cognitive scaffold position (Clark & Chalmers; Malafouris; Penny).
- **Claim D** (Negative / boundary) — pre-studio articulation phase as structurally distinct from downstream PaR phases.

### Venue path (revised 2026-05-25 — conceptual paper first, empirical track later)

1. **Aslib JIM (Aslib Journal of Information Management, Emerald)** *primary, v0.1 publication.* **Conceptual paper** classification (4,000–10,000 w, structured abstract, Harvard / agsm refs). No user-study requirement. Submission feasible within weeks; the existing LaTeX skeleton at `art-project_paper/` is the working draft.
2. ***Digital Creativity (Routledge / T&F)*** sibling — methods paper, ~7,000 w. Submitted after Aslib JIM is in review (avoiding simultaneous-submission conflicts).
3. **ACM C&C 2027 / 2028** — empirical track. Activates after the conceptual paper is submitted; requires Study 1 (CSI + NASA-TLX pilot, N=12) plus the longitudinal artist study.
4. ***Journal for Artistic Research (JAR)*** sibling — as an exposition, not a traditional article. Best done after Phase 5 publication establishes the framework.
5. ***Leonardo* / *ISEA* / *SIGGRAPH Art Papers*** practitioner-facing — once empirical data from artist users exists (Studies 2–4 + longitudinal).

**Rationale for resequencing (vs. original v0.2 empirical-first path):** Aslib JIM Conceptual paper accepts the framework on its conceptual merits without empirical data, dissolving the 4–7-month delay the empirical-first path imposed before any publication exists. The reverse ordering (empirical first, conceptual second) would have left the framework un-argued in print as supplementary material to an empirical paper, which is structurally weaker. See v0.2 synthesis spec §4.2 + §7 for the full rationale.

### Measured-harm disclosure (model-card style, new)

Six harm classes named and disclosed (Mitchell et al. 2019 Model Cards format; Bender et al. 2021 Stochastic Parrots citing):

1. Lineage hallucination per sub-domain.
2. Training-data canon bias.
3. Simulation-pedagogy risk (rehearsal — Schön 1983 cited).
4. Authorship-perception shift (Wordcraft / Sparks / ghostwriter literature).
5. Conviviality / normalization risk (Illich 1973; Turkle 2015; Hui 2016).
6. Bounded user population (per user-asymmetry scope).

### Phase plan (revised 2026-05-25 — conceptual paper first, empirical track later)

- **Phase 0b** (2026-05-24 commit): v0.2 synthesis spec + reference-layer rewrite + project-level docs. ✅
- **Phase 1**: drop paper-scoped reference files; expand methodology reference E section with verified Korean / East-Asian sources. *Partial — drops done; E expansion pending library + consultation work.*
- **Phase 2**: drop paper-authoring skill dirs and commands; rename `art-inquiry/` → `art-ideation/`; fix symlinks. ✅
- **Phase 3**: rewrite `art-ideation/SKILL.md` for 6 v0.2 modes; create 6 new commands. *SKILL.md + commands done.* Agent-prompt rewrites for Authentic Practice Boundary enforcement + `full` mode project-file persistence pending v0.2 implementation work.
- **Phase 4**: project-level docs (README / QUICKSTART / CLAUDE.md / CHANGELOG / POSITIONING / MODE_REGISTRY). ✅
- **Phase 5 — Aslib JIM Conceptual paper** *(was empirical pilot before 2026-05-25 revision)*: draft per v0.2 spec §4.3 outline using existing LaTeX skeleton at `art-project_paper/`. **v0.1 publication target.** Off-platform, in progress.
- **Phase 6 — Aslib JIM revisions + parallel *Digital Creativity* draft**: off-platform.
- **Phase 7 — Empirical track activation** *(begins after Aslib JIM submission, in parallel with Phase 6)*: Study 1 design + OSF pre-registration + IRB; recruit N=12; run pilot. Output: ACM C&C 2027 / 2028 submission. Off-platform.
- **Phase 8 — JAR exposition** (after Phase 5 published). Off-platform.
- **Phase 9 — Studies 2–4 + 6-week longitudinal artist study.** Output: *Leonardo* / *ISEA* / *SIGGRAPH Art Papers* practitioner-facing paper. Off-platform, v0.2 / v0.3.

---

## [0.1.0] — 2026-05-22 — art-paper fork (superseded by 0.1.0-ideation above)

> Forked from ARS v3.9.4.2. Re-specialized the 4-skill suite from empirical scientific papers to **practice-based art research papers** targeting the **SIGGRAPH Asia Art Papers track**. Most of this scope has been **dropped** in the 2026-05-24 pivot above; this entry is retained as provenance.

- **4 skills renamed:** `deep-research` → `art-inquiry`, `academic-paper` → `art-paper`, `academic-paper-reviewer` → `art-reviewer`, `academic-pipeline` → `art-pipeline`.
- **Slash commands** renamed `ars-*` → `art-*` and extended to 15 with two new `art-paper` modes: **artist-statement** and **work-doc**.
- **Genre layer replaced** in `shared/references/`: `art_paper_structure_patterns.md`, `art_research_evidence_model.md`, `acm_reference_format.md`, `siggraph_acm_disclosure.md`, `creative_art_terminology_glossary.md`.
- **Output toolchain:** acmart LaTeX → PDF.
- **Reviewer reframed** as the SIGGRAPH Asia Art Papers jury.
- **Integrity gate re-scoped** to artwork / realization claim verification.
- **Fork design:** [`docs/design/2026-05-22-art-paper-v0.1-fork-spec.md`](docs/design/2026-05-22-art-paper-v0.1-fork-spec.md).
- Chinese-language support dropped in stage 1 (commit `27aa0da`, 2026-05-23) + stage 2 (commit `23f1fb5`, 2026-05-23).

---

### Inherited ARS history

Entries before the 2026-05-22 fork belong to the parent **academic-research-skills** suite. Full ARS changelog (v1.0 → v3.9.4.2) is at [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md). art-project does not re-narrate it here.
