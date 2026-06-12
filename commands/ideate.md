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

The plugin persists a project-file across sessions — a single plain-markdown file per project — so that `ideate` is a long-running scaffold across days/weeks, not a single-session orchestration.

**Behavior on invocation (v0.2 — minimal markdown persistence at `~/.art-project/projects/<codename>/project.md`).**

The plugin manages a single markdown file per project at `~/.art-project/projects/<codename>/project.md`. Plain markdown, no schema lock-in; the artist can still git-track it, edit it directly between sessions, copy it across machines. The plugin reads the file at session start and appends a session block at session end. The artist still owns the file — every write is shown before it lands, the artist can edit or refuse it, and direct edits between sessions are first-class.

**Writability precheck (run before any of the branches below).** Attempt to ensure `~/.art-project/projects/` exists and is writable (e.g. `mkdir -p ~/.art-project/projects/` and a write probe). If the home directory is unwritable, read-only, or otherwise blocks the mechanism, fall back gracefully to the v0.1 **artist-managed** mode (artist designates a filename, pastes the file back next session, the plugin emits the session log as text for the artist to append) and warn explicitly: *"Couldn't write to `~/.art-project/projects/` ([reason]). Falling back to artist-managed mode — you'll need to designate a filename and paste the file back next session. The cross-session persistence guarantee is downgraded for this run."*

1. **If the artist says this is a new project:**
   - Ask what to call the project (working title or codename). Slugify if needed (lowercase, hyphens, ASCII).
   - Run `mkdir -p ~/.art-project/projects/<codename>/` and create `~/.art-project/projects/<codename>/project.md` with a header block:
     ```
     # <codename>

     - **Created:** YYYY-MM-DD
     - **Sessions:** 1
     - **Brief description:** <one-line description, asked from the artist>
     ```
   - Show the artist the path and the header that was written; offer to edit before continuing.
   - Ask: *"Where do you want to begin? `socratic` (no concept yet) / `provoke` (stuck) / `lineage` (positioning) / `brief` (have material, need a proposition document) — or just describe your state in natural language and I'll suggest."*

2. **If the artist says this is an existing project:**
   - Scan `~/.art-project/projects/` for matching codenames (substring + slug match against the artist's mention).
     - **Exactly one match:** read `~/.art-project/projects/<codename>/project.md` directly; no paste required.
     - **Multiple matches:** list the candidate codenames with their `Created` dates and last-session dates, ask the artist to disambiguate.
     - **No match:** fall back to the new-project flow above, noting that no existing project was found.
   - Once the file is loaded, display a brief summary of the last 1–2 session blocks (date, mode, key outputs, any open re-entry markers; include any inter-session **Artist notes** the artist added directly).
   - Ask: *"You last worked on this on [date], in [mode]. The state was [summary]. Where to today? Continue [last mode] / move to [suggested next mode] / different mode / just talk."*

3. **One mode per session.** Do not auto-chain socratic → provoke → lineage → brief → rehearsal. The temporal shape matters. If the artist wants to do multiple modes today, ask explicitly; do not pipeline.

4. **End-of-session append.** Before closing the session, append a Session block to `~/.art-project/projects/<codename>/project.md` using this format **verbatim**:

   ```
   ---

   ## Session N — YYYY-MM-DD HH:MM — <mode>

   [Session output goes here verbatim — Concept Pull Map, provocation cards, lineage map, brief, rehearsal transcript, etc.]

   ### Artist notes (optional; added between sessions by the artist directly)

   ---
   ```

   Then increment the `Sessions:` counter in the header. Show the artist the appended block and the new counter value before writing; the artist can edit or refuse. If the writability precheck failed and we are in artist-managed fallback, emit the block as text for the artist to paste into their own file instead.

**IRON RULE — no single-session compression.** Do not produce a Concept Brief and a Rehearsal in the same session unless the artist *explicitly* requests it and acknowledges that this contradicts the design's temporal-shape commitment. The default refusal: *"Brief and Rehearsal in the same session compresses what the design treats as a multi-week iteration. The marginal value of a same-day Rehearsal is low. Sleep on the Brief first; come back next week for Rehearsal. — or override with `--compress` if you really want to."*

Wire to: Smith & Dean (2009, C6) iterative cyclic web (primary). All other tradition tags pass through as the sub-mode in the current session activates them.

See [`art-ideation/SKILL.md`](../art-ideation/SKILL.md) for the full mode specification.
