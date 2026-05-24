# Mode Selection Guide (art-project v0.2)

> **Spec history.** This file was an art-inquiry 7-mode guide (full / quick / review / lit-review / fact-check / socratic / systematic-review) tied to an academic-research pipeline. The art-project v0.2 pivot replaced that with a single skill of six modes (socratic / provoke / lineage / brief / rehearsal / full) scoped to pre-studio articulation. This guide is rewritten to match.

## Overview

`art-ideation` exposes six modes, each addressing a different propositional articulation task. The modes are not phases of a pipeline. Each can be entered, exited, and re-entered independently. The `full` mode is the exception, since it opens a long-running project file in which the other five modes can be invoked across sessions.

The mode the artist needs depends on three signals:

1. **Concept state** — none, partial, draft, ready-for-submission
2. **Material supplied** — none, candidate lineage, draft brief
3. **Time horizon** — single session, weeks, months

## Decision flow

```
Artist input
    │
    ├── No concept yet, just a pull / fragment / unease
    │       └──→ socratic
    │
    ├── Partial concept, feels stuck
    │       ├── Wants displacement / what-ifs ──→ provoke
    │       └── Wants positioning with stated candidates ──→ lineage
    │
    ├── Enough material to draft a one-pager (grant, residency, exposition)
    │       └──→ brief
    │
    ├── Has draft brief, wants friction before submission
    │       └──→ rehearsal
    │
    ├── Long-running project across days or weeks
    │       └──→ full (project file)
    │
    └── Ambiguous → see intent_clarification_protocol.md (default to socratic)
```

## Per-mode detail

### socratic — pre-reflective articulation

**Enter when:** the artist has no work yet, no clear concept, only a pull or a fragment or a constraint. The mode is distinct from Schön's reflection-in-action (no work yet to reflect on), and that distinctness is the contribution.

**Output:** a Concept Pull Map with five fields, namely impulses, fragments, constraints, refusals, and a *residue* field that captures contradictions and half-formed material verbatim.

**IRON rule:** while intent detection reads as exploratory, no auto-convergence. No "want me to summarise?" prompts. The artist signals when they are ready to converge.

**Tradition tags wired:** Frayling (1993), Borgdorff (2011, 2012), Sullivan (2010), Smith & Dean (2009), Csikszentmihalyi (1996), Geneplore (Finke, Ward & Smith 1992). Schön (1983) cited as the distinction marker.

### provoke — tradition-tagged provocations with preserved unhelpfulness

**Enter when:** the artist has a partial concept and feels stuck on it. The mode generates provocations to displace the artist from a fixated default; it is not a refinement tool.

**Output:** 8–20 tradition-tagged provocation cards, each carrying an Authentic Practice Boundary and a counter-formulation that holds the provocation in tension rather than ranking it.

**IRON rule:** after issuing an Oblique-style provocation, the mode goes silent. No auto-interpretation. The artist asks for elaboration explicitly or doesn't get it. Provocations are not ranked or scored.

**Tradition tags wired:** Oblique Strategies (Eno & Schmidt 1975), SCAMPER (Eberle 1971), Cage chance operations, Bolt's experimental gesture (2007), Boden's three creativity types (2004), Dunne & Raby (2013) speculative design, Bogart Viewpoints (2005) for time-based / performance work, Bauhaus Vorkurs.

### lineage — constrained retrieval, not unsolicited consecration

**Enter when:** the artist has stated initial candidate references ("I think my work sits between X and Y") and wants the scaffold to extend the map. The mode is honestly self-described as retrieval, not ideation. It is for positioning, not for inspiration.

**Output:** a Lineage Map with 5–15 entries, each tagged kin / opposition / blind-spot / unexpected-neighbour, with a citation anchor. A mandatory training-data bias header opens every output.

**IRON rule:** does not propose lineage from the impulse alone. Requires artist-supplied initial candidates. Offers a `--no-lineage` opt-out at any point. When the session is in Korean or carries East-Asian subject signals, Korean and East-Asian sources are prioritised before global ones, and the routing decision is announced.

**Tradition tags wired:** Sullivan (2010) contextualist inquiry (strongest theory-to-mode fit); Frayling (1993); Manovich (2001); Boden & Edmonds (2009) taxonomy; Paul (2003); Popper / Couchot; Whitelaw (2004); Galanter (2003); Paik (1963); East-Asian yi / qi / yeobaek; Yuk Hui (2016) cosmotechnics.

### brief — Concept Brief with epistemic fields and stay-rough default

**Enter when:** the artist has enough material to draft a proposition document for a grant application, residency proposal, or doctoral exposition. The brief is not a marketing one-pager. It is a proposition document with explicit epistemic fields.

**Output:** a Concept Brief with the following fields, in order: working title, provocation, proposition, anti-proposition, condition for disconfirmation, intended encounter, lineage anchor, materials and scale, risk and refusal, Frayling-type declaration.

**IRON rules:** stay-rough default (prose stays in the artist's voice, no auto-smoothing). No auto-completion of gaps (empty fields are reported as gaps rather than filled with plausible-sounding text). The `--polish` flag is opt-in only.

**Tradition tags wired:** Borgdorff (2011, 2012) for the provocation field; Sullivan (2010) dialectical inquiry for the anti-proposition; Bogart (2005) for the intended encounter; Corita Kent (1968) and Saltz (2018) for the risk-refusal field; Frayling (1993) for the type declaration.

### rehearsal — Self-Critique Rehearsal (formative, not decisional)

**Enter when:** the artist has a draft brief and wants friction before facing real curators, peers, or critics. The mode is rehearsal, not critique; real critique is constituted by relational history the simulation does not have.

**Output:** a multi-persona rehearsal transcript (Curator, Practitioner-peer, Theorist, Devil's Advocate) with each critique line paired with the brief field it asks the artist to revisit. A mandatory disclaimer header opens every output.

**IRON rules:** the disclaimer is non-optional. Architectural friction kicks in after two invocations on the same brief within 14 days. The persona-collapse detector flags when all four personas converge on a single concern.

**Tradition tags wired:** Koestler (1964) bisociation for the foreign-domain voice; Csikszentmihalyi (1996) for the field-simulation framing; de Bono (1985) Six Hats for the persona-as-role discipline; Saltz (2018) for the critic-voice seed; Schön (1983) cited explicitly as the simulation-pedagogy risk marker.

### full — long-running project file across sessions

**Enter when:** the artist wants a project tracked across days and weeks rather than completed in one session. Real practice-based research ideation proceeds over months, and the mode operationalises Smith & Dean's (2009) iterative cyclic web as persistent state rather than as a single-session workflow constraint.

**Output:** a project file that accumulates state across sessions. Each session does one sub-mode at most. Cross-session re-entry is a first-class affordance.

**IRON rule:** no single-session compression of multi-week work. Brief and rehearsal in the same session is refused unless the artist explicitly overrides with `--compress`.

**Tradition tags wired:** Smith & Dean (2009) iterative cyclic web (primary); all other tradition tags pass through as the active sub-mode activates them.

## Common mis-selection scenarios

| Artist's situation | Likely mis-selection | Correct mode | Why |
|---|---|---|---|
| Has a clear concept, just wants writing help | `socratic` | `brief` | socratic is for the pre-concept stage; for an existing concept, brief is the correct entry point |
| Says "I'm stuck" but has no concept yet | `provoke` | `socratic` | provoke displaces a fixated concept; without a concept to displace, the mode has nothing to operate on |
| Wants lineage suggestions with no stated candidates | `lineage` | `socratic` then `provoke` | lineage's IRON rule requires artist-supplied candidates; without them, the mode would propose unsolicited lineage, which the design refuses |
| Wants a beautiful polished brief | `brief` with mental expectation of polish | `brief` with explicit `--polish` opt-in | the stay-rough default exists for good reason; auto-polish is opt-in not default |
| Already has external curator feedback, wants to revise | `rehearsal` | `brief` (revise directly) | rehearsal is preparation for external review, not a substitute for received external review; once real feedback exists, work directly in brief |

## Mode transitions

Transitions inside a single conversation are governed by intent detection. The skill announces transitions transparently rather than performing them silently. Common paths:

- `socratic → provoke` — the artist's impulse has stabilised; provocations may sharpen the next move
- `socratic → lineage` — the artist named candidate references during socratic dialogue; lineage extends them
- `socratic → brief` — the artist has enough material; brief converges (only at artist's explicit signal)
- `provoke → socratic` — a provocation surfaced a deeper question; return to surfacing mode
- `lineage → brief` — lineage has been mapped; the lineage anchor field of brief is now ready
- `brief → rehearsal` — a draft brief is in hand; rehearsal stress-tests it
- `rehearsal → brief` — rehearsal output is re-entrant into brief fields; the artist revises
- any mode `→ full` — the artist wants to persist state across sessions; full opens the project file

Transitions are user-initiated or explicitly suggested. The skill does not silently switch modes mid-conversation.

## When to use the full project file

`full` mode is appropriate when:

- the artist expects the project to take weeks or months from impulse to studio commitment
- the artist wants cross-session state (which sub-mode was last entered, which brief fields are filled, which provocations were marked productive)
- the artist will return to the same project across multiple Claude Code sessions
- the project will eventually need a Concept Brief plus rehearsal plus a clear handoff to studio work

`full` mode is inappropriate when:

- the task is a one-shot draft of a single deliverable (use the relevant single mode directly)
- the artist wants to chain socratic → provoke → lineage → brief → rehearsal in one sitting (the design refuses this; the temporal shape matters)
- the project does not exist yet and the artist is exploring whether to start one (start with `socratic` directly; the project file can be opened later)
