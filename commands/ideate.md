---
description: "Open or continue a long-running art-project file across multiple sessions (days/weeks apart). Smith & Dean iterative cyclic web in operational form. NOT a single-session pipeline. Each session does one mode at most; cross-session re-entry is first-class."
model: opus
---

Invoke the `art-ideation` skill in **full** mode (long-running project file).

**This is not a single-session pipeline.** Real PaR ideation proceeds over weeks or months (Smith & Dean 2009, *Practice-Led Research, Research-Led Practice*, C6 — iterative cyclic web). `full` mode opens a **project file** that persists across sessions; each session does *one mode at most*; the artist returns days or weeks later and continues.

A typical project-file evolution:

```
2026-03-15  socratic-session-1   → impulse surfaced; residue captured
2026-03-22  socratic-session-2   → constraints clarified; refusals named
2026-04-05  provoke-session-1    → 12 provocations issued, 3 marked productive
2026-04-12  lineage-session-1    → 8 candidates supplied by artist; map extended
2026-04-26  brief-draft-1        → 6 of 10 fields articulated; 4 gap-acknowledged
2026-05-10  rehearsal-1          → 4 personas; 5 re-entry points flagged
2026-05-17  brief-draft-2        → re-entries addressed; 9 of 10 fields filled
2026-06-01  rehearsal-2          → panel-collapse detected; warned artist to seek external reader
2026-06-15  → artist takes Brief to actual curator
```

The Material Passport machinery inherited from the parent suite (originally for single-session pipeline orchestration) is repurposed as the **project-file schema** — persistent state across sessions, not a state machine.

**Behavior on invocation:**

1. **If no project file exists for this artist:**
   - Ask the artist what to call the project (working title or codename).
   - Create the project file (markdown, in a location the user designates or in `~/.art-project/projects/[codename]/`).
   - Ask: *"Where do you want to begin? `socratic` (no concept yet) / `provoke` (stuck) / `lineage` (positioning) / `brief` (have material, need a proposition document) — or just describe your state in natural language and I'll suggest."*

2. **If a project file exists:**
   - Read the file. Display a summary of the last 1–2 sessions.
   - Ask: *"You last worked on this on [date], in [mode]. The state was [summary]. Where to today? Continue [last mode] / move to [suggested next mode] / different mode / just talk."*

3. **One mode per session.** Do not auto-chain socratic → provoke → lineage → brief → rehearsal. The temporal shape matters. If the artist wants to do multiple modes today, ask explicitly; do not pipeline.

4. **End-of-session checkpoint.** Before closing the session, append to the project file:
   - Date + mode + duration
   - Key outputs (Pull Map fields touched / provocations marked / lineage entries added / brief fields filled / rehearsal critiques flagged)
   - Open questions / re-entry markers for next session

**IRON RULE — no single-session compression.** Do not produce a Concept Brief and a Rehearsal in the same session unless the artist *explicitly* requests it and acknowledges that this contradicts the design's temporal-shape commitment. The default refusal: *"Brief and Rehearsal in the same session compresses what the design treats as a multi-week iteration. The marginal value of a same-day Rehearsal is low. Sleep on the Brief first; come back next week for Rehearsal. — or override with `--compress` if you really want to."*

Wire to: Smith & Dean (2009, C6) iterative cyclic web (primary). All other tradition tags pass through as the sub-mode in the current session activates them.

See [`art-ideation/SKILL.md`](../art-ideation/SKILL.md) for the full mode specification.
