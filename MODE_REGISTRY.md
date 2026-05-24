# Mode Registry

Single source of truth for all modes in the art-project plugin. **6 modes** across **1 skill** (`art-ideation`).

art-project is a **pre-studio articulation scaffold** (not an ideation engine), pivoted from art-paper v0.1.0 (itself forked from academic-research-skills v3.9.4.2). The mode names and behaviors below reflect the v0.2 synthesis spec ([`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md)), which supersedes the v0.1 pivot spec on mode design.

When adding or modifying modes, update this file first — `art-ideation/SKILL.md` and `.claude/CLAUDE.md` should reference this registry.

Last updated: v0.1.0-design (2026-05-24, post-synthesis)

---

## art-ideation (6 modes)

The plugin's outputs are **language** — questions, briefs, lineage maps, rehearsal transcripts — that the artist takes back to the studio. The artistic ideation itself happens elsewhere (in materials, in time, in bodies). The plugin scaffolds the *propositional articulation work* that surrounds ideation.

| Mode | Spectrum | Output | Oversight | Slash command | Triggers (illustrative) |
|---|---|---|---|---|---|
| `socratic` | Originality | Dialogue + **Concept Pull Map** (named impulses / fragments / constraints / refusals / **residue**) | Very High | `/art-socratic` | "guide me", "I don't know what I'm doing yet", "help me find what the work wants to be", 도와줘 / 잘 모르겠어 |
| `provoke` | Originality | **Tradition-tagged provocation set** (8–20 cards, each tagged + **Authentic Practice Boundary** named, with counter-formulation; *unhelpfulness preserved* — no auto-interpretation) | High | `/art-provoke` | "give me provocations", "what if", "throw constraints at me", 막혔어 |
| `lineage` | Fidelity | **Lineage Map** (5–15 precedent artists / works / texts, tagged kin / opposition / blind-spot / unexpected-neighbor; **mandatory training-data bias header**; **requires artist-supplied initial candidates**) | Medium | `/art-lineage` | "who else has done this", "where am I in the field", "position my work" |
| `brief` | Balanced | **Concept Brief** with epistemic fields (proposition / anti-proposition / disconfirmation condition / intended encounter / lineage anchor / risk-refusal / Frayling-type declaration); **stay-rough default** (artist's voice preserved) | High | `/art-brief` | "draft a concept brief", "write up what I have so far", "one-pager for [grant / collaborator / self]" |
| `rehearsal` | Balanced | **Self-Critique Rehearsal** transcript — Curator + Practitioner-peer + Theorist + Devil's Advocate; **formative-not-decisional**; **persona-collapse detector active**; **architectural friction** (warns after 2 invocations / 14 days on same concept) | High | `/art-rehearsal` | "stress-test this", "rehearse for curatorial feedback", "tear it apart in safety" |
| `full` | Balanced | **Long-running project file** — accumulates state across multiple sessions (days/weeks apart); one mode per session; cross-session re-entry | Very High | `/art-ideate` | "start a new project", "open my project file", "continue where I left off" |

### Mode renaming from v0.1

- **`panel` → `rehearsal`** (v0.2). The renaming commits to the *method-not-evaluation* verdict: `rehearsal` exists so the artist can practice articulating their work under questioning *before* facing real curators, peers, or critics. Real critique is constituted by relational history (the curator's studio visits over years, the peer's stake in the scene) that no simulation has; the rehearsal is for the artist's own preparation, not for substitute review.

### Default routing rules

| Situation | Recommended mode |
|---|---|
| No concept yet, vague pull | `socratic` |
| Partial concept, feels stuck | `provoke` |
| Has stated candidate lineage, wants extension | `lineage` |
| Has enough material, needs a proposition document | `brief` |
| Has a draft brief, wants rehearsal before submission | `rehearsal` |
| Wants the whole arc, across weeks | `full` (project file) |
| Ambiguous, no materials | `socratic` (default — guides first) |
| Mode unclear, prefers natural-language | start a session without slash command; intent detection auto-routes with transparent announcements |

### Mode-switching policy

Per the v0.2 spec §2.4 (response to Practicing Artist Q2):

- Slash commands are available when the artist knows what they need.
- Natural-language session start triggers **auto-routing via intent detection** with transparent announcements: *"Starting in socratic mode (exploratory intent detected). I'll suggest switching modes when the dialogue suggests it."*
- Mode transitions are similarly announced and offered, never silently performed: *"Your impulse has stabilized; would you like to move to `provoke` or `lineage`, or continue exploring?"*
- The artist may decline any mode transition and continue in the current mode.

**Spectrum:** *fidelity* = template-heavy, predictable output; *balanced* = default; *originality* = exploratory, template-light.

**Oversight levels:**

| Level | Meaning |
|---|---|
| Very High | User-led dialogue or mandatory checkpoints at every stage |
| High | User confirms key decisions (provocation set, brief framing, rehearsal scope) |
| Medium | Structured format with limited decision points |
| Low | Mechanical / template-driven, minimal human input |

### Mode-to-reference wiring (with Authentic Practice Boundaries)

Each mode draws on specific entries in [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md). The reference layer is restructured in v0.2 (positionality opening, contested-in fields, Tensions section, justified 5+1 mechanisms, expanded East-Asian section, restored critical edge on Penny / Barrett & Bolt / Smith & Dean / Borgdorff). Per-mode wiring:

| Mode | Primary tradition tags wired | Key Authentic Practice Boundaries |
|---|---|---|
| `socratic` | Frayling (1993), Borgdorff (2011, 2012), Sullivan (2010), Smith & Dean (2009), Csikszentmihalyi (1996, 1999), Geneplore (Finke, Ward & Smith 1992). **Cited but not wired:** Schön (1983) — used only to mark the distinction between *pre-reflective* articulation (this mode) and Schön's *reflection-in-action* | This mode is *pre-reflective*: no work exists yet to reflect on |
| `provoke` | Eno & Schmidt (Oblique Strategies, 1975); SCAMPER (Eberle 1971, with Christensen & Schunn 2007 critical note); de Bono (1967, 1985); Cage (chance operations); Boden (1990, 2004); Dunne & Raby (2013); Bolt (2007, experimental gesture) | Oblique Strategies: physical deck is irreplaceable; Cage: plugin proposes, artist executes; LeWitt: plugin prompts artist to write instructions, does not author them |
| `lineage` | Sullivan (2010, contextualist inquiry); PaR literature; art-and-technology lineage (Couchot, Popper, Penny, Manovich, Paul, Galanter, Whitelaw, Reas/Fry); LeWitt; Bauhaus; Korean / East-Asian sources (E-section expanded in v0.2) | Lineage is **retrieval**, not ideation; requires artist-supplied initial candidates; mandatory training-data bias header; clean `--no-lineage` opt-out |
| `brief` | All of the above + Bogart (Viewpoints) for *intended encounter*; Corita Kent + Saltz for *risk/refusal*. **Frayling-type declaration field** ties back to §1.2 of v0.2 spec | Stay-rough default — plugin forces field articulation but does not smooth prose; `--polish` flag opt-in only |
| `rehearsal` | Inherited multi-persona reviewer machinery, **re-scoped from juried-acceptance to formative rehearsal**. Schön (1983) cited explicitly to mark the *simulation-pedagogy* risk | Mandatory disclaimer; architectural friction after repeated use; persona-collapse detector; rehearsal output is re-entrant into Brief fields, not standalone judgement |
| `full` | All of the above, plus Smith & Dean (2009) **iterative cyclic web** for the cross-session shape | Cannot be compressed into one session; project file persists across weeks/months |

---

## Summary

| Metric | Count |
|---|---|
| Total modes | 6 |
| Fidelity | 1 |
| Balanced | 3 |
| Originality | 2 |

---

## What is NOT in this registry (out of scope for v0.1)

- **Paper authoring modes** (full / plan / outline-only / revision / abstract-only / lit-review / format-convert / citation-check / disclosure / artist-statement / work-doc) — dropped from art-paper v0.1.0. Available via the art-paper sibling distribution (git history of this repo).
- **Jury review modes** (full / re-review / quick / realization-focus / guided / calibration) — dropped. The `rehearsal` mode is *formative*, not a juried accept/reject simulation.
- **Pipeline orchestration as state machine** — dropped. The `full` mode is a project file, not a pipeline.
- **Mixed-initiative behavior** — explicitly out of scope per v0.2 §1.1 (HCI Q3 Position A: turn-taking as defended commitment, grounded in artist autonomy, citing Frich et al. 2019 and Draxler et al. 2024).
- **Image / sound / video generation** — outside the language-scaffold scope.
- **Real-time multi-artist collaboration** — single-user in v0.1.

These exclusions are deliberate: art-project is the **pre-studio articulation** phase. Downstream tools (papers, statements, documentation, image generation) are the artist's choice and live elsewhere. Once an artist has a Concept Brief, the bridge to a future art-paper distribution is the Brief schema itself (v0.2 OQ5 resolved: the Brief is the bridge document).
