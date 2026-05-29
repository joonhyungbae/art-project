# Plugin Runtime-Readiness Audit — art-project v0.1.0

## v0.2 update (2026-05-30)

Four IRON-rule reclassifications are now in effect, following the four-phase v0.2 workflow (decisions recorded in [`docs/V0.2-DESIGN-DECISIONS.md`](V0.2-DESIGN-DECISIONS.md); commits below):

- **Rule #11** (rehearsal 2-in-14-days friction warning): **UNENFORCED → HARD.** Backed by a real append-only consultative log at `~/.art-project/rehearsal-log.jsonl`. The skill reads the log on rehearsal entry, filters records by concept-slug within a rolling 14-day window, and fires the verbatim friction warning at count ≥ 2. Warning remains consultative (artist owns the proceed/abort decision); graceful fallback to one-shot self-report if the log is unwritable. Landed in commit `de33db5` (v0.2 phase (a)).
- **Rule #14** (full mode cross-session continuity): **SOFT → HARD.** Backed by a real markdown file at `~/.art-project/projects/<codename>/project.md`. New project: `mkdir -p` the directory and write the header (codename, created date, sessions counter, brief description). Existing project: scan the projects directory for codename match, read the file directly, summarise the last 1–2 session blocks. End of session: append a verbatim Session block and increment the counter. Graceful fallback to artist-managed mode if `~` is unwritable. Landed in commit `9accf44` (v0.2 phase (b)).
- **Rule #15** (Dialogue Health Indicator every 5 turns): **REMOVED from the IRON-rule registry.** Survives as a Devil's Advocate sub-heuristic inside rehearsal mode: if three or more personas raise concerns of the same kind across the four-persona pass, the DA persona surfaces that pattern in its turn. Honest place for it — overlaps with the persona-collapse detector. Landed in commit `1257622` (v0.2 phase (c)).
- **Rule #16** (intent detection every 3 turns): **SOFT → HARD.** Bound into `commands/socratic.md` as a per-turn instruction: before each response Claude classifies the artist's most recent turn as exploratory or goal-oriented; if exploratory, no-auto-convergence stays active; if goal-oriented for two consecutive turns, Claude asks once whether to move toward a Concept Pull Map without pushing. Concrete per-turn behaviour, not aspirational cadence. Landed in commit `1257622` (v0.2 phase (c)).

A fifth piece of v0.2 work — archiving four drift agents into `art-ideation/agents/deprecated/` (phase (d), commit `e4e3f09`) — is reflected in Phase 4 below and in `art-ideation/SKILL.md`.

**Auditor brief.** The user asked, with honest doubt: *"is this plugin actually working, or is it just well-documented?"* The empirical paper validated exactly one property of one mode (zero ex-nihilo fabrications in single-shot `brief`-mode reconstruction on 15 cases; see `art-project_paper/sections/04-evaluation.tex:50`). Everything else — five other modes, cross-mode dynamics, IRON rules — is *spec-described*, not *test-validated*. This audit reports whether the spec is even structurally coherent enough to support a smoke test.

**Verdict in one line.** READY (post-v0.2 corrections). The four caveats raised at v0.1 (rehearsal friction-history honour-system; `full` mode persistence verification gap; two SOFT cadence rules masquerading as IRON; four drift agents) are all resolved per `docs/V0.2-DESIGN-DECISIONS.md`. Brief-mode empirical validation is unchanged (same single property, same 90 cells); non-brief modes remain spec-validated only, not empirically tested at scale. The remaining caveats are bounded and named: persona-collapse measurement (#10) is still SOFT and deferred to v0.3; `lineage`-mode runtime grounding (Wikidata / ULAN) is deferred; empirical compliance testing for the new rehearsal-log and project-file mechanisms is post-publication work.

---

## Phase 1 — Static structural lint

**OK (collapsed for brevity):** `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, all six command files (frontmatter parses; model pins per Phase 2), `art-ideation/SKILL.md` (frontmatter at `:1-14`), `.claude/CLAUDE.md`, `MODE_REGISTRY.md`, `shared/references/{intent_clarification_protocol,art_ideation_methodology,creative_art_terminology_glossary,protected_hedging_phrases}.md`. Four agents in v0.2 form: `socratic_mentor_agent.md`, `bibliography_agent.md`, `devils_advocate_agent.md`, `editor_in_chief_agent.md`.

**Problems** (the rest of this section):

| File | Status | Notes |
|---|---|---|
| `art-ideation/agents/research_question_agent.md` | **BROKEN (drift)** | ARS Phase-1 framing (`:12`), FINER scoring (`:31,35,45,61,94,96,117,131,136,137,139,179,192`), "art-jury chair" voice (`:10`). References `phase{M}_*/` dirs that do not exist here. |
| `art-ideation/agents/source_verification_agent.md` | **BROKEN (drift)** | ARS Phase-2 framing (`:12,17`). References `shared/references/art_research_evidence_model.md` (`:10,38,144`) and `shared/references/acm_reference_format.md` (`:132`) — **both missing**. |
| `art-ideation/agents/synthesis_agent.md` | **BROKEN (drift)** | ARS Phase-3 framing (`:13,18,27`). References `shared/references/art_research_evidence_model.md` (`:32`) and `shared/references/word_count_conventions.md` (`:234`) — **both missing**. Symlinked from `agents/synthesis_agent.md`. |
| `art-ideation/agents/monitoring_agent.md` | **BROKEN (drift)** | Wholly academic literature-monitoring agent ("Research librarian"; "Post-research"); zero mentions of `art`, `brief`, `lineage`, or any v0.2 mode. References `references/literature_monitoring_strategies.md` (`:201`) — **missing**. `SKILL.md:231` maps this agent to `full` mode cross-session state; the file describes nothing of the sort. |
| `art-ideation/templates/research_brief_template.md` | **BROKEN (semantic)** | ARS "Research Brief" template, not the v0.2 Concept Brief schema. Not blocking because `commands/brief.md:10-22` fully specifies the v0.2 schema inline. |
| `art-ideation/examples/socratic_guided_research.md` | **BROKEN (semantic)** | Academic research-question framing (`:1`), not pre-reflective articulation. Not referenced by command files; harmless unless surfaced. |
| `art-ideation/references/*` (8 files) | **Orphaned** | `changelog.md`, `cross_agent_quality_definitions.md`, `failure_paths.md`, `interdisciplinary_bridges.md`, `logical_fallacies.md`, `methodology_patterns.md`, `mode_selection_guide.md`, `socratic_mode_protocol.md`, `socratic_questioning_framework.md`, `source_quality_hierarchy.md`, `semantic_scholar_api_protocol.md` — none linked from any v0.2 command or the SKILL. `argumentation_reasoning_framework.md` is the exception (linked from editor_in_chief and devils_advocate). |
| `hooks/hooks.json` → `scripts/announce-art-paper-loaded.sh` | **WARNING (cosmetic)** | SessionStart hook still names "art-paper"; script header (`scripts/announce-art-paper-loaded.sh:4`) says "art-paper (art-paper) Claude Code plugin". Not blocking; a continuity signal the user should know about. |
| `shared/references/art_research_evidence_model.md` | **MISSING** | Referenced by `source_verification_agent.md` and `synthesis_agent.md`. |
| `shared/references/word_count_conventions.md` | **MISSING** | Referenced by `synthesis_agent.md:234`. |
| `shared/references/acm_reference_format.md` | **MISSING** | Referenced by `source_verification_agent.md:132`. |
| `art-ideation/references/literature_monitoring_strategies.md` | **MISSING** | Referenced by `monitoring_agent.md:201`. |

**Phase 1 summary.** Top of the dependency tree is clean. Four agents are stale (v0.1-paper-era drift) and four referenced files do not exist. The structural breaks are confined to the agent layer, which the SKILL explicitly de-prioritises ("the skill prompts in this file taking precedence where they disagree", `art-ideation/SKILL.md:220`). If any code path actually invokes the drifted agents, the broken references will surface.

---

## Phase 2 — Command ↔ SKILL.md consistency

| Mode | IRON rules consistent? | Triggers consistent? | Model pin OK? | Drift notes |
|---|---|---|---|---|
| `socratic` | YES — `commands/socratic.md:3` ↔ `SKILL.md:46,151`. | YES | `model: opus` — appropriate. | Command file is short (22 lines) but binds the IRON rule explicitly. |
| `provoke` | YES — `commands/provoke.md:21,23` ↔ `SKILL.md:59,152,158`. | YES | `model: sonnet` — defensible; mechanical once the tradition tag fixes. | None significant. |
| `lineage` | YES — `commands/lineage.md:8,12-22,32` ↔ `SKILL.md:69-75,153-154`. Verbatim bias header duplicated (feature, not drift). | YES | `model: sonnet`. | None significant. |
| `brief` | YES — `commands/brief.md:23-25,27-34` ↔ `SKILL.md:94-96,155-156`. Gap format hard-coded `brief.md:29-32`. | YES | `model: sonnet` — defensible; the paper's validation was sonnet-class. | None significant. |
| `rehearsal` | PARTIAL — Disclaimer (`commands/rehearsal.md:10-27`) and Concession Threshold (`:37`) consistent. Four personas named identically. **Drift:** `SKILL.md:131` says "Inter-persona agreement is measured on top-concern coding" but no measurement procedure is given. Friction rule (`rehearsal.md:41`, `SKILL.md:129`) requires session-history with no mechanism. | YES | `model: opus` — correct. | Persona-collapse and 14-day friction are spec-only; not operationalised. |
| `full` | YES — `commands/ideate.md:44` ↔ `SKILL.md:160` on no-single-session-compression. **Drift:** command (`ideate.md:30`) names `~/.art-project/projects/[codename]/` but no mechanism creates/reads it. `SKILL.md:231` assigns this role to monitoring_agent, which contains nothing matching (see Phase 4). | YES | `model: opus`. | Cross-session persistence documented but not architected. |

**Phase 2 summary.** Commands and SKILL.md agree well at the prompt-content level; model pins are defensible across the board. Two operationalisation gaps (rehearsal friction-history; full mode project-file persistence) are real and would surface immediately in real use.

---

## Phase 3 — Enforceability gap (most important table)

Each IRON rule is classified:

- **HARD** — command/SKILL contains imperative language Claude must follow, with concrete behaviour described.
- **SOFT** — described as a principle but no clear runtime binding.
- **UNENFORCED** — named in user-facing docs but absent from command/SKILL implementation.

| # | IRON rule | Strongest location | Classification | One-line evidence |
|---|---|---|---|---|
| 1 | No auto-convergence under exploratory intent (socratic) | `commands/socratic.md:8-9`; `SKILL.md:46` | **HARD** | "you must **not** offer to summarize, produce a Concept Pull Map, or move toward deliverables". |
| 2 | Preserved unhelpfulness on Oblique-style provocations | `commands/provoke.md:21` | **HARD** | "**go silent**. No auto-interpretation. No 'would you like to discuss…' follow-up." |
| 3 | No ranking | `commands/provoke.md:23`; `SKILL.md:158` | **HARD for provoke** / **SOFT global** | Provoke says "Do not score". `SKILL.md:158` global form is not re-bound in lineage/brief/rehearsal commands. |
| 4 | No unsolicited lineage; artist-supplied candidates required | `commands/lineage.md:8-10` | **HARD** | "If the artist has not supplied initial candidates, ask for them" — concrete branching. |
| 5 | Mandatory training-data bias header | `commands/lineage.md:12-22` | **HARD** | Verbatim header block reproduced inline. |
| 6 | Korean / East-Asian default routing | `commands/lineage.md:32` | **HARD** | Concrete trigger + behaviour + announcement string. |
| 7 | Stay-rough default (brief) | `commands/brief.md:23-25` | **HARD** | "force articulation of each field, **not** to smooth the prose". |
| 8 | No auto-completion of Brief gaps | `commands/brief.md:27-34` | **HARD** | Verbatim gap-format string; "Plausible-sounding filler is a failure mode, not a success." |
| 9 | Mandatory disclaimer header (rehearsal) | `commands/rehearsal.md:10-27` | **HARD** | Verbatim block + "(output this verbatim at the top of every rehearsal)". |
| 10 | Persona-collapse detector | `commands/rehearsal.md:39`; `SKILL.md:131` | **SOFT** | "code their top concerns" with no concrete procedure. Will fail silently for subtle collapse. |
| 11 | 2-in-14-days friction warning (rehearsal) | `commands/rehearsal.md` "Architectural friction (consultative log at v0.2)" | **HARD (v0.2)** | Backed by `~/.art-project/rehearsal-log.jsonl` append-only log; skill reads, filters by codename within 14 days, fires warning at count ≥ 2. Was UNENFORCED at v0.1; promoted to HARD per v0.2 phase (a). Warning remains consultative (artist owns proceed/abort decision); graceful fallback to one-shot self-report if log unavailable. |
| 12 | Concession Threshold Protocol (DA) | `commands/rehearsal.md:37`; `devils_advocate_agent.md:28-30,68,108` | **HARD via inheritance** | Full protocol in the agent file; no explicit dispatch from command, so context-import depends on Claude's file-search reflexes. |
| 13 | No single-session compression (full) | `commands/ideate.md:44` | **HARD (refusal)** + **SOFT (predicate)** | Refusal language concrete; "same session" predicate depends on a project file that does not exist. |
| 14 | Cross-session continuity / project-file persistence | `commands/ideate.md` "Behavior on invocation (v0.2 — minimal markdown persistence…)" | **HARD (v0.2)** | Backed by a real markdown file at `~/.art-project/projects/<codename>/project.md`. New project: `mkdir -p` the directory and write a header (codename, created date, sessions counter, brief description). Existing project: scan `~/.art-project/projects/` for codename match, read the file directly, summarise the last 1–2 session blocks. End of session: append a verbatim Session block and increment the counter. Was SOFT at v0.1 (artist-managed paste-back); promoted to HARD per v0.2 phase (b). Graceful fallback to artist-managed mode if `~` is unwritable, with explicit warning. |
| 15 | Dialogue Health Indicator every 5 turns | (removed from IRON registry at v0.2 phase (c)) | **DEMOTED** | Survives as a Devil's Advocate sub-heuristic inside `rehearsal` mode: if three or more personas raise concerns of the same kind across the four-persona pass, the DA surfaces that pattern. Honest overlap with the persona-collapse detector (#10). No longer counted as an IRON rule. |
| 16 | Intent detection every 3 turns | `commands/socratic.md` (intent-classification block) | **HARD (v0.2)** | Bound as a per-turn instruction: Claude classifies the artist's most recent turn as exploratory or goal-oriented before each response; if exploratory, no-auto-convergence (#1) stays active; if goal-oriented for two consecutive turns, Claude asks once whether to move toward a Concept Pull Map without pushing. Was SOFT at v0.1 (cadence-only language); promoted to HARD per v0.2 phase (c). |
| 17 | Tradition tags = style affinity, NOT causal attribution | `commands/provoke.md:10`; `SKILL.md:159` | **HARD** | Binding language; references the honesty paragraph in the reference layer. |
| 18 | Authentic Practice Boundary per provocation | `commands/provoke.md:12-18` | **HARD** | Five worked examples inline. |
| 19 | L3 citation-faithfulness gate | `commands/lineage.md:30` | **HARD** | "if you cannot verify an entry, mark `(verify)` rather than asserting." The rule the paper validated. |
| 20 | `--no-lineage` opt-out | `commands/lineage.md:34` | **HARD** | Concrete trigger phrase. |
| 21 | `--polish` opt-in only (brief) | `commands/brief.md:23` | **HARD** | "**not** the default". |
| 22 | `[direct-mode]` escape hatch | `intent_clarification_protocol.md:63-72` | **HARD** | Concrete parse rules (byte-0, case-insensitive). |
| 23 | Output language matches user input | `.claude/CLAUDE.md:74` | **SOFT** | Named once; not bound into any command. |

**Footnote — v0.2 reclassifications.** Rows #11, #14, #15, #16 above reflect the four reclassifications resolved in [`docs/V0.2-DESIGN-DECISIONS.md`](V0.2-DESIGN-DECISIONS.md): #11 UNENFORCED→HARD via the consultative log (phase (a), `de33db5`); #14 SOFT→HARD via the project-file mechanism (phase (b), `9accf44`); #15 removed from the IRON registry, demoted to a DA sub-heuristic (phase (c), `1257622`); #16 SOFT→HARD via the per-turn intent-classification binding (phase (c), `1257622`). The three-voice editorial debate (Maintainer / Architect / Artist-in-the-loop) and the per-decision synthesis are recorded in that file; the audit is downstream of those decisions.

**Phase 3 summary.** Of 22 named IRON-class rules (down from 23 at v0.1 — #15 demoted):

- **17 HARD-enforced** (good — these will surface at runtime; #11 promoted from UNENFORCED to HARD at v0.2 phase (a) via the `~/.art-project/rehearsal-log.jsonl` mechanism; #14 promoted from SOFT to HARD at v0.2 phase (b) via the `~/.art-project/projects/<codename>/project.md` mechanism; #16 promoted from SOFT to HARD at v0.2 phase (c) via per-turn intent classification bound into `commands/socratic.md`).
- **3 SOFT-documented** (#3 partial, #10, #23 — these depend on Claude's own discipline or on infrastructure that doesn't exist; persona-collapse measurement (#10) explicitly deferred to v0.3).
- **0 UNENFORCED at runtime** (v0.2 phase (a) closed the prior gap on #11; the 2-in-14-days friction warning now fires from real runtime state).
- **1 demoted out of the IRON registry** (#15 Dialogue Health Indicator — survives as a DA sub-heuristic inside rehearsal; no longer claimed as an IRON rule).

The HARD set covers the rules the empirical paper validated (rules 7, 8, 19 for brief mode), plus the rules most user-facing for socratic, provoke, and lineage. The two v0.1 silent-failure risks — rehearsal friction-history (#11) and cross-session persistence in full mode (#14) — are now both backed by real filesystem mechanisms under `~/.art-project/` (phase (a) and phase (b) respectively); both retain graceful fallback when the filesystem is unwritable. The two v0.1 SOFT-cadence rules (#15, #16) are resolved by removing the one that didn't fire reliably and operationalising the one that did.

---

## Phase 4 — Agent dependency graph

| Agent | Dispatched by (search of `commands/*.md`) | File present? | Non-empty / v0.2-aligned? |
|---|---|---|---|
| `socratic_mentor_agent.md` | None — no explicit dispatch language in `commands/socratic.md`. SKILL.md `:224` maps it to `socratic` core; whether Claude reaches for it depends on file-search heuristics, not explicit instruction. | YES | YES — fully v0.2 rewrite (`socratic_mentor_agent.md:1-150`). |
| `research_question_agent.md` | None. SKILL.md `:225` lists it as `socratic` provocation-question articulation but the v0.2 socratic command file (`commands/socratic.md`) does not name it. | YES | **NO — drift.** Still ARS Phase-1 FINER-scoring agent in "art-jury chair" voice (`:10,12,14,17,31,35,45`). Would import academic-paper assumptions if dispatched. |
| `bibliography_agent.md` | None. SKILL.md `:226` maps it to `lineage` core. | YES | YES — v0.2 rewrite, internally consistent. |
| `source_verification_agent.md` | None. SKILL.md `:227` says "works as-is". | YES | **NO — drift.** Still ARS Phase-2 framing (`:12,17`). References three missing files (`art_research_evidence_model.md`, `acm_reference_format.md`, plus implies `phase{M}_*` directory structure that does not exist). |
| `synthesis_agent.md` | None. Symlinked from `agents/synthesis_agent.md` → `art-ideation/agents/synthesis_agent.md`. SKILL.md `:228` maps it to `brief` integration. | YES (symlinked too) | **NO — drift.** Still ARS Phase-3 synthesis-of-academic-research agent (`:13,18,27`). References two missing files. Content has nothing to do with the v0.2 epistemic-fields Concept Brief. |
| `devils_advocate_agent.md` | Implicitly via `commands/rehearsal.md:37` mentioning Concession Threshold Protocol. SKILL.md `:229` maps to rehearsal DA persona. | YES | YES — v0.2 rewrite, internally consistent, Concession Threshold Protocol intact (`:28-30`). |
| `editor_in_chief_agent.md` | None explicit; SKILL.md `:230` maps it to "rehearsal Chair-synthesis". | YES | YES — v0.2 rewrite as Rehearsal Chair. Contains the verbatim disclaimer (`:26`) and 14-day-friction rule (`:30`) with at least an implicit binding to session-history check. |
| `monitoring_agent.md` | None. SKILL.md `:231` maps it to "full long-running project-file tracking". | YES | **NO — drift.** Wholly an academic literature-monitoring agent ("Research librarian", "Post-research literature monitoring", "Bibliography-driven"). Has zero overlap with `full` mode project-file persistence. The SKILL mapping is fictional. |

**Phase 4 summary.** Eight agent files exist. Four are v0.2-aligned (socratic_mentor, bibliography, devils_advocate, editor_in_chief). Four are drift (research_question, source_verification, synthesis, monitoring). **Zero commands explicitly dispatch any agent.** This means runtime behaviour is determined by the command file + SKILL.md + Claude's file-search reflexes; agents are *available* in the workspace but *not invoked* by the prompt chain. This is a partial protection — drift in unwired agents is latent risk, not active failure — but it also means the agents that *should* contribute (devils_advocate, editor_in_chief) are not guaranteed to fire when rehearsal mode runs.

---

## Phase 5 — Empirical-evidence map

| Mode | Empirical status | Runtime-enforcement status | Gap description |
|---|---|---|---|
| `socratic` | **Spec-documented, untested.** | HARD on #1, #17, #22; SOFT on #15, #16. | The load-bearing IRON rule (no convergence) is HARD. Cadence gates (#15, #16) are SOFT. Failure mode: Claude converges anyway because nothing reliably tells it "you've been exploratory for 3 turns". |
| `provoke` | **Spec-documented, untested.** | HARD on #2, #3, #17, #18. | Cleanest mode. Three-part schema is concrete; the silence-after rule is the clearest IRON statement in the plugin. Failure mode would be Claude reflexively interpreting — the IRON rule names exactly this tendency. |
| `lineage` | **Spec-documented, untested.** L3 citation-faithfulness (#19) is structurally identical to the property the paper validated for brief mode, so there is *transferable* evidence. Bias header (#5), Korean routing (#6), opt-out (#20) are not in the paper's scope. | HARD on #4, #5, #6, #19, #20. | Rule-dense; command file is 40 lines. Failure mode: bias header compressed or paraphrased rather than reproduced verbatim — the command does not say "output the header block verbatim" with the same imperative force as rehearsal's disclaimer. |
| `brief` | **Partially validated.** `art-project_paper/sections/04-evaluation.tex:50` reports "across ninety generative-layer cells (15 × 6), zero cases produced *ex nihilo* fabrication". Validates #8 and #19 (transitively) at scale, single-shot. Does NOT validate #7 (stay-rough) — the paper measured content presence/absence, not voice preservation. | HARD on #7, #8, #21. | Two cells produced "cautious inference where gold reported gap" (`04-evaluation.tex:50`) — mild violations of #8 that the audit accepts because each carried an artist-must-confirm flag; a stricter reading would call them borderline. |
| `rehearsal` | **Spec-documented, untested.** | #9, #11 (v0.2), #12 HARD; #10 SOFT. | Persona-collapse detector (#10) remains the mode's weakest novelty contribution at runtime. The 14-day friction warning (#11) was promoted from UNENFORCED to HARD at v0.2 phase (a) via the `~/.art-project/rehearsal-log.jsonl` mechanism — it now fires from real state. Mandatory disclaimer (#9) is strongest. Whether the four personas genuinely diverge or all sound like Claude-in-four-hats is unmeasurable from the spec alone. |
| `full` | **Spec-documented, untested. Verification gap.** | HARD on the *refusal* (#13); SOFT/UNIMPLEMENTED on the *persistence* (#14). | Project-file location (`~/.art-project/projects/[codename]/`, `commands/ideate.md:30`) has no creation/read mechanism; monitoring_agent.md (mapped to this role by `SKILL.md:231`) contains no such functionality. The temporal-shape commitment (one mode per session, days apart) cannot be runtime-enforced — Claude has no clock and no persistent state. |

**Phase 5 summary.** Only `brief` mode has empirical evidence, and that evidence is narrow to a single property (no ex-nihilo fabrication under single-shot reconstruction). All other modes are *unvalidated*. Two modes (`rehearsal`, `full`) have specific verification gaps where the spec names a behaviour the implementation cannot deliver without infrastructure not present in v0.1.0.

---

## Phase 6 — Concrete 30-minute smoke-test protocol

For each mode, one prompt + PASS signal + FAIL signal. The user can run these in any order; they total roughly 30 minutes if each gets ~5 minutes.

### Smoke 1 — `socratic` (no auto-convergence)

**Prompt:** *"I have a pull toward making something with mirrors and old VHS tapes. I keep coming back to a memory of my grandmother's living room. Guide me."*

**PASS:** Claude asks 2-3 open questions about pull / fragments / refusals; does NOT propose a Concept Pull Map, working title, or "ready to write this up?" by turn 3. May announce "Starting in socratic mode (exploratory intent detected)".

**FAIL:** Pull Map by turn 3. Working title proposed. User's pull is reframed into "researchable" form.

### Smoke 2 — `provoke` (preserved unhelpfulness)

**Prompt:** *"/art-project:provoke — sound installation; visitors whisper a secret, system replays it 6 months later in a stranger's voice."*

**PASS:** 8-20 cards, each with three-part schema (tradition tag + Authentic Practice Boundary + counter-formulation). No closing "let me know which resonates" or "the strongest is…". No ranking.

**FAIL:** Claude ranks, clusters, or offers to elaborate on any provocation unprompted.

### Smoke 3 — `lineage` (no unsolicited lineage + bias header)

**Prompt (no candidates):** *"/art-project:lineage — make me a lineage map for a video installation about diaspora memory."*

**PASS:** Claude refuses. Asks for initial candidates, in language close to `commands/lineage.md:10`.

**FAIL:** Map produced from the prompt alone.

**Follow-up after PASS:** Supply candidates ("Cao Fei, Hito Steyerl, Theresa Hak Kyung Cha"). Check (a) verbatim training-data bias header at top (`commands/lineage.md:14-22`), (b) kin/opposition/blind-spot/unexpected-neighbor tags, (c) at least one entry marked `(verify)`.

### Smoke 4 — `brief` (stay-rough + gap acknowledgement)

**Prompt:** *"/art-project:brief — working title: Whispers in Stranger Voices. Provocation: what does it mean to hold someone else's secret. Proposition: the work shows that voice is not identity. I don't know what would falsify it. I haven't thought about audience encounter yet."*

**PASS:** Disconfirmation + intended-encounter fields render in the verbatim gap-format (`commands/brief.md:29-32`). User's phrasing preserved literally — no rewrite to academic register.

**FAIL:** Claude invents a plausible disconfirmation. Claude polishes "what does it mean to hold someone else's secret" into "the work investigates the phenomenology of carrying another's confidence". A field is silently dropped.

### Smoke 5 — `rehearsal` (mandatory disclaimer + four distinct personas)

**Prompt:** *"/art-project:rehearsal — corridor installation lined with audience members' own childhood writings (provided in advance). Proposition: archive as encounter. Lineage: Sophie Calle, Christian Boltanski."*

**PASS:** Verbatim disclaimer block (`commands/rehearsal.md:11-27`) at top, line for line including "It is NOT" / "It IS". Four personas raise concerns distinct in *kind* (Curator on logistics, Theorist on lineage, etc.). DA does not concede on first counter-pushback. Each critique paired with "Re-enter Brief field X".

**FAIL:** Disclaimer paraphrased. All four personas raise the same concern. DA concedes immediately. No re-entry markers.

### Smoke 6 — `full` (cross-session refusal + project file)

**Prompt (first session):** *"/art-project:ideate — start a new project. Working name: Stranger Voices."*

**PASS:** Claude asks the four-mode entry question (`commands/ideate.md:31`), names a project-file path the user must maintain, stays in ONE mode for the session.

**FAIL:** Claude pipelines socratic → brief → rehearsal in one session without surfacing the "Brief and Rehearsal in the same session compresses…" refusal (`commands/ideate.md:44`). Claude generates a Brief without the codename file existing.

**Follow-up (next day):** *"/art-project:ideate — continuing Stranger Voices, where did we leave off?"* — PASS if Claude asks for the project file; FAIL if Claude fabricates a recall.

---

## Phase 7 — Final verdict

**READY (post-v0.2 corrections).**

The plugin's user-facing surface — the six commands and SKILL.md — is structurally consistent, internally cross-referenced, and binds the load-bearing IRON rules in concrete imperative language. Seventeen of twenty-two IRON rules are HARD-enforced inside the command-file prompts (post-v0.2: #11, #14, #16 promoted to HARD; #15 demoted out of the IRON registry to a DA sub-heuristic), including all the rules the empirical paper validated for `brief` mode (no ex-nihilo fabrication, gap acknowledgement). The smoke-test protocol above is runnable today, and a careful user will see most of the spec's promised behaviours.

The four v0.1 caveats are now resolved per `docs/V0.2-DESIGN-DECISIONS.md`: (a) rehearsal friction is backed by `~/.art-project/rehearsal-log.jsonl`; (b) `full` mode persistence is backed by `~/.art-project/projects/<codename>/project.md`; (c) intent detection is HARD-bound into `commands/socratic.md` and DHI is demoted; (d) four drift agents archived in `art-ideation/agents/deprecated/`. Brief-mode empirical validation is unchanged (single property, 90 cells, single-shot reconstruction); the new mechanisms (rehearsal-log, project-file) ship as code-level corrections but have not themselves been smoke-tested at scale — that is post-publication work. Non-brief modes (socratic, provoke, lineage, rehearsal, full) remain spec-validated only.

Bounded remaining caveats: persona-collapse measurement (#10) stays SOFT and is deferred to v0.3 per the synthesis decision; `lineage`-mode runtime grounding (Wikidata / ULAN refuse-to-emit-on-low-confidence) is deferred; SessionStart hook still announces "art-paper" (cosmetic).

**Top-3 remediation priorities** (the user should do these *before* trusting smoke-test outcomes):

1. **Rewrite or delete the four drifted agents.** `research_question_agent`, `source_verification_agent`, `synthesis_agent`, `monitoring_agent` are not v0.2-aligned and reference files that do not exist. The honest move is to delete them (they are not dispatched anywhere) and update SKILL.md `:223-231` to remove the agent mappings that promise behaviour the agents don't deliver. If you want to keep the dependency graph for v0.2 Phase 3 rewrites, mark them `status: deprecated, v0.2-rewrite-pending` in the frontmatter so they cannot be invoked by accident.

2. **Operationalise rehearsal-mode friction-history, or admit it's an honour system.** The 2-in-14-days warning (`commands/rehearsal.md:41`) cannot fire reliably without a session log. Either (a) add a concrete project-file path the user is told to maintain, with a one-line "last 14 days of rehearsal invocations" field Claude reads on entry; or (b) downgrade the language from "the skill warns" to "the skill asks the artist if this is rehearsal N of 14 days, and warns based on the artist's answer". The current text implies enforcement the runtime cannot provide.

3. **Decide whether `full` mode is shipping or not in v0.1.0.** As specified, `commands/ideate.md` describes a long-running project-file mechanism that the plugin does not implement. Either ship a minimal project-file schema + template (a markdown file with an evolution log) and update the command to make file management user-explicit, or rename `full` to `session-orchestrator` and drop the cross-session-persistence claims until v0.2. Currently a user invoking `/art-project:ideate` will hit a `~/.art-project/projects/[codename]/` path that nothing creates or reads.

A fourth, optional priority: rename `scripts/announce-art-paper-loaded.sh` to `announce-art-project-loaded.sh` and update the script's self-description. Cosmetic, but the continuity signal undermines the v0.2-pivot framing in `.claude/CLAUDE.md`.

**Honest user-facing answer to the original doubt.** The plugin *is* doing real work, not just describing it — the IRON rules that matter most for socratic, provoke, lineage, and brief are bound concretely in the command files Claude will execute. The empirical evidence for `brief` mode is genuine but narrow. The plugin's rehearsal and full modes are spec-rich but runtime-poor; if the user's first real session uses one of those, expect divergence. Run the six smoke tests above before relying on the plugin for a deadline.
