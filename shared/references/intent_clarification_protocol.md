# Intent Clarification Protocol (art-project v0.2)

> **Spec history.** This file was originally an ARS v3.9.2 hot-fix for a multi-phase paper-authoring pipeline. The art-project v0.2 pivot dropped the paper pipeline in favour of a single skill (`art-ideation`) with six modes, and this file is rewritten to match. The "pipeline phases" framing of the original no longer applies. See [`../../docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](../../docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).

## Purpose

When the user's request does not unambiguously identify which mode of `art-ideation` to enter, the main session **clarifies before dispatching**. Auto-routing on ambiguous intent leads to premature convergence in `socratic`, mis-scoped retrieval in `lineage`, or polished-but-empty output in `brief` — all failure modes the v0.2 design explicitly avoids.

This protocol defines:

1. When clarification fires (3 trigger classes)
2. How the clarification message is structured (a-d options in markdown body, NOT `AskUserQuestion`)
3. How the `[direct-mode]` escape hatch works
4. Worked examples

## Trigger condition table

| Condition | Routing class | Action |
|---|---|---|
| User invokes `/art-*` slash command | Explicit | Route directly to the named mode; no clarification |
| User uses an unambiguous trigger phrase (e.g., "guide me through a new project", "draft a concept brief for my work", "rehearse my brief") | Explicit | Route directly; no clarification |
| User describes a situation that maps cleanly to one mode (e.g., "no idea yet, just a pull", "stuck on the LED matrix experiments", "submitting to a residency next week") | Inferred-but-explicit | Auto-route with a transparent announcement of which mode and why |
| User provides materials or context that span multiple modes (e.g., a partial brief plus a list of candidate lineage figures) | Cross-mode ambiguous | **Clarify** with a-d options |
| User provides no materials and no clear request | No materials ambiguous | **Clarify** with a-d options |
| User's first message begins with `[direct-mode]` (byte-0, case-insensitive) | Escape hatch | Strip prefix and route on the stripped content; skip clarification |

**Default-to-`socratic` rule.** When the situation is genuinely ambiguous and the artist has supplied no materials, the safe default is `socratic`. The mode is designed to keep the artist in exploration until they signal readiness to converge, so it cannot do harm in the way a premature `brief` or `lineage` invocation would. The clarification message should still offer the four options below; but if the artist replies with "just start", default to `socratic`.

## The six modes (for the clarification options)

| Mode | When it fits |
|---|---|
| `socratic` | No concept yet; just a pull, a fragment, a constraint |
| `provoke` | A partial concept that feels stuck; wants displacement |
| `lineage` | A partial concept and stated candidate references; wants positioning |
| `brief` | Enough material to draft a Concept Brief for a grant, residency, or collaborator |
| `rehearsal` | A draft brief; wants self-critique rehearsal before facing real reviewers |
| `full` | A long-running project the artist wants to track across days or weeks |

## Clarification message template

When clarification fires, the main session emits a message in this shape (markdown body, multi-select a-d format):

```markdown
I see you've described <summary of what the user said / provided>. Which mode would help most?

(a) **Socratic dialogue** — I'll ask questions to surface your impulses, constraints, and refusals. No deliverable until you signal ready. Use `/art-project:socratic`.
(b) **Provocations** — I'll throw tradition-tagged what-ifs at you, then go silent so you can sit with them. Use `/art-project:provoke`.
(c) **<one of: Lineage / Brief / Rehearsal / Full>** — <one-line description tuned to what the user said>. Use `/art-<mode>`.
(d) **Something else** — describe what you're trying to do.

Pick a-d, or describe the target output. To skip this clarification, prefix your next message with `[direct-mode]`.
```

**Discipline rules:**

- 3-4 candidate options + open "something else"; never more than 4 (avoid choice paralysis).
- Each option names the slash command so the user sees what gets invoked.
- Pick the three most plausible modes for the artist's situation rather than always listing the same three; the third option is the variable slot.
- Last sentence mentions `[direct-mode]` so the user knows the escape hatch exists.
- Do NOT call the `AskUserQuestion` tool — options live in the markdown body of the chat response.

## `[direct-mode]` escape hatch

**Behaviour:**

- **Position:** Token must be the first non-whitespace token of the user's first message. Leading whitespace is stripped on parse. Token appearing mid-message does NOT qualify.
- **Case:** Case-insensitive. `[direct-mode]`, `[Direct-Mode]`, `[DIRECT-MODE]` all accepted.
- **Bracket form:** Only the literal `[direct-mode]` (square brackets, hyphen between words) is recognised. Variants like `(direct-mode)`, `<direct-mode>`, `[direct mode]`, `[directmode]` are NOT recognised.
- **Strip:** The literal token (with surrounding whitespace) is stripped before any downstream agent sees the message.
- **Effect:** Bypasses the cross-mode-ambiguous and no-materials-ambiguous clarification triggers. Main session routes the stripped message directly per Explicit handling.
- **Fallback:** If the stripped message still has no clear mode named, the Explicit step falls through to clarification. `[direct-mode]` bypasses cross-mode clarification, not all routing. If the artist wants to bypass even ambiguous-intent clarification, they must name a specific mode (e.g., `[direct-mode] /art-project:socratic`).

## Worked examples

### Example 1: vague pull, no materials → clarify (default to socratic if asked)

**User input:**
> I want to start something new but I have no idea what yet.

**Detection:** No materials, ambiguous intent.

**Main session response:**
> Got it. Which mode would help most?
>
> (a) **Socratic dialogue** — I'll ask questions to surface your impulses, constraints, and refusals. No deliverable until you signal ready. Use `/art-project:socratic`.
> (b) **Provocations** — I'll throw tradition-tagged what-ifs at you to see if any catch. Use `/art-project:provoke`.
> (c) **Open a project file** — start a long-running file you can come back to over weeks. Use `/art-project:ideate`.
> (d) **Something else** — describe what you're trying to do.
>
> Pick a-d, or just say "start" and I'll begin in socratic mode (the safer default for this stage).

### Example 2: explicit intent → no clarification

**User input:**
> Guide me through a new project. I'm in a sound-installation impulse but it's still very vague.

**Detection:** Explicit trigger ("guide me through a new project"). Mode `socratic` matches cleanly.

**Main session response:** Routes directly to `art-socratic`, announces the routing transparently per `SKILL.md` discipline.

### Example 3: cross-mode ambiguous → clarify

**User input:**
> I've got a draft concept and a list of artists I think are precedents — Casey Reas, Paik, maybe Whitelaw. What now?

**Detection:** Concept (could go to `brief`) + lineage candidates (`lineage`) → cross-mode.

**Main session response:**
> You have a draft concept and named lineage candidates, which is enough material to go several ways. Which would help most?
>
> (a) **Lineage mapping** — extend your candidates with kin / opposition / blind-spot / unexpected-neighbour entries, with a training-data bias header. Use `/art-project:lineage`.
> (b) **Draft the Concept Brief** — write up the concept in proposition / anti-proposition / disconfirmation form with your stated lineage as one of the fields. Stay-rough default. Use `/art-project:brief`.
> (c) **Provocations against the current concept** — see if there are angles you haven't considered before committing to the brief. Use `/art-project:provoke`.
> (d) **Something else** — describe what you're trying to do.

### Example 4: `[direct-mode]` honored

**User input:**
> [direct-mode] just start brief mode, I have a residency deadline

**Stripped message:** `just start brief mode, I have a residency deadline`

**Main session response:** Routes directly to `art-brief`. No clarification fires.

### Example 5: `[direct-mode]` mid-message → NOT honored

**User input:**
> Hi, can you [direct-mode] just start brief mode?

**Token position:** Not byte-0. Escape hatch ignored.

**Main session response:** Detects "start brief mode" as a possible explicit trigger; routes to `art-brief` per Explicit handling. (In this case `[direct-mode]` mid-message changes nothing because the explicit trigger was clean enough to route on its own. The mid-position is still an anti-pattern; do not rely on it.)

## When this protocol does NOT apply

- **Within a mode that has already been entered.** If `socratic` is running and the artist's reply has a new angle, the mode handles it. The protocol governs the entry point of a session, not within-mode turns.
- **Mode transitions inside `full`.** The `full` mode's project-file behaviour switches modes session-by-session with the artist's confirmation. Each new session starts at the entry point, where this protocol applies; within a session, the active mode is in charge.
- **System messages and tool outputs.** The protocol classifies user-authored content. Tool outputs, system reminders, and Claude Code-internal messages bypass it.

## Forward note

This protocol may evolve as the v0.2 plugin matures. The `[direct-mode]` escape hatch is retained from the parent suite because it has proven useful, but if a future v0.3 introduces structured intake the protocol may be replaced by envelope-declared intent. Until that happens, the markdown-body clarification pattern is the source of truth.
