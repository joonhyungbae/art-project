# Full project file mode

> Slash command: `/art-project:ideate` — for projects that span weeks or months across multiple sessions.

## What it does

Maintains a **long-running project file** that accumulates state across multiple Claude Code sessions (days or weeks apart). Each session runs at most one mode (socratic, provoke, lineage, brief, or rehearsal); the file records which mode ran, what materials it produced, and the artist's annotations.

The mode is the operational response to Smith & Dean's iterative cyclic web framing — ideation is not a single up-front phase but recurs across the project lifecycle.

## When to use

- You expect the project to take more than one Claude Code session.
- You want material from earlier sessions (Concept Pull Map, Lineage Map, brief drafts) to persist and be referenceable.
- You're working under a multi-week grant or residency timeline.
- Trigger phrases: "start a new project", "open my project file", "continue where I left off".

## How project files work (v0.2: plugin-managed at `~/.art-project/projects/`)

The plugin maintains a single markdown file per project at `~/.art-project/projects/<codename>/project.md`.

**On a new project**, you supply a codename; the plugin `mkdir -p`'s the directory, writes the project header (codename, created date, sessions counter, brief description), surfaces the file path and the written content to you for confirmation, and asks which sub-mode to start.

**On a returning session**, the plugin scans `~/.art-project/projects/` for codename matches, reads `project.md` directly, summarises the last 1–2 session blocks, and asks where you want to continue.

**At end of each session**, the plugin appends a verbatim Session block to `project.md` (mode, date, output, artist-notes placeholder) and increments the sessions counter. The diff is surfaced before writing.

**The file stays yours.** It is plain markdown in a known, predictable location — you can `git init` the `~/.art-project/projects/<codename>/` directory, sync it via Dropbox or rsync, edit by hand, copy to a collaborator. The plugin manages the read/append cycle; everything else is your filesystem.

**Graceful fallback.** If `~` is unwritable for any reason (sandboxed environment, permission error), the plugin falls back to the v0.1 artist-managed model — emits the session log as text you paste-back — and announces the fallback explicitly. The cross-session-continuity claim is then artist-load, not plugin-load, and the plugin says so.

## One mode per session rule

Each session in a full project file runs **at most one mode**. The reason: cross-mode pipelining within a session is what `provoke → brief → rehearsal` rapid-fire tools optimise for, and that pattern actively undermines the cyclic web. The full mode forces the artist to close the session after one mode and return later, in studio time, with the produced material.

If you find yourself wanting to switch modes mid-session, close the session and start a new one for the next mode.

## IRON rules (full-specific)

- **One mode per session** — enforced architecturally; if you try to switch modes within a session, the plugin will warn and require explicit override.
- **No single-session pipelining** — `socratic → brief` in one sitting is structurally hostile to the cyclic web; the plugin refuses to pipeline.
- **Project file persists at `~/.art-project/projects/<codename>/project.md`** — all session outputs are appended; nothing is overwritten. The plugin manages the read/append cycle, but the file remains plain markdown the artist can git-track, sync, or edit by hand.

## What the project file looks like

```text
# art-project: inscription-counter-inscription
created: 2026-04-12
sessions: 7

─────────────────────────────────────────────────────
SESSION 1 — socratic — 2026-04-12 16:30
─────────────────────────────────────────────────────
[Concept Pull Map produced. Stored below.]

[map content...]

ARTIST NOTES (added 2026-04-14):
- the residue feels like the most live thing
- the constraint about "not a memorial" is now stronger

─────────────────────────────────────────────────────
SESSION 2 — provoke — 2026-04-18 10:15
─────────────────────────────────────────────────────
[12 provocation cards. Stored below.]

[cards content...]

ARTIST NOTES (added 2026-04-21):
- card 3 (LeWitt) and card 9 (Cage) keep returning
- sat with them for 4 days; decided card 9 is the one

─────────────────────────────────────────────────────
SESSION 3 — lineage — 2026-04-25 09:00
[etc.]
```

## What not to do

- **Don't run `full` for a single-session task.** If you only need one brief drafted from material you already have, use `/art-project:brief` directly.
- **Don't try to pipeline modes within a session.** The plugin enforces the one-mode-per-session rule.
- **Don't expect the plugin to "manage" the project for you.** The project file is yours; the plugin appends to it but does not direct it.

## Cross-session resume

When you re-enter a project file, the plugin shows a brief summary (last session's mode, what it produced, what mode you might run next) and then asks what you want to do. You can:

- Run a new mode session.
- Annotate an earlier session's output.
- Read the file as a whole.
- Close without modifying.

## Where to go next

- The full mode IS the next mode. From within `full`, you choose which sub-mode to run each session.
- See [Modes overview](overview.md) for which sub-mode fits which moment.

## See also

- [First session](../getting-started/first-session.md) — if you want to start in `full` rather than a single mode.
- [Cognitive scaffold](../philosophy/cognitive-scaffold.md) — why ideation-across-time matters.
