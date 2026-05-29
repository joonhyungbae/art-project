# Troubleshooting

Common issues, what causes them, what to do. Each problem has a one-line diagnosis and a concrete next step.

## Installation

### `/art-project:socratic` returns "command not found"

**Cause**: the plugin is not installed, not enabled, or your session was started before the install completed.

**Fix**:
1. Verify install: `/plugin list` should include `art-project`.
2. If missing, install: `/plugin marketplace add joonhyungbae/art-project` then `/plugin install art-project`.
3. If listed but disabled, enable it in Claude Code settings.
4. Restart your Claude Code session — slash commands are loaded at session start.

### Plugin appears installed but slash commands are still missing

**Cause**: Claude Code is caching the previous session's plugin list.

**Fix**: full restart of Claude Code (not just a new window). The session-start hook reloads plugin slash commands.

### `mkdocs serve` returns "Address already in use"

**Cause**: some other process is holding port 8000 (often a previous `mkdocs serve` you forgot to close, or an unrelated dev server).

**Fix**: use a different port: `mkdocs serve -a localhost:8001`. Or find and stop the holding process: `lsof -i :8000` then `kill <pid>` if it is in fact stale.

## Modes refuse to start

### `/art-project:lineage` says "supply at least two candidate precedents"

**Cause**: not a bug; it is the [lineage IRON rule](../modes/lineage.md). Lineage hallucination on long-tail sub-domains is the most common LLM lineage-tool failure mode, so the plugin requires artist-supplied anchors.

**Fix**: name 2 or more precedent artists, works, or texts before invoking lineage. If you have none, start with [`socratic`](../modes/socratic.md) (impulse surfacing) or [`provoke`](../modes/provoke.md) (constraint generation) first.

### `/art-project:rehearsal` says "no brief found"

**Cause**: rehearsal mode stress-tests an existing Concept Brief; it has nothing to test if you have not run `brief` first.

**Fix**: run [`brief`](../modes/brief.md) and produce a 10-field Concept Brief. Then return to `rehearsal`.

### `/art-project:rehearsal` says "friction warning: you have rehearsed this concept N times in the last 14 days"

**Cause**: not a bug; it is the [rehearsal architectural friction](../modes/rehearsal.md). After 2 invocations on the same concept within 14 days, the plugin warns about simulation-pedagogy harm (Schön 1983).

**Fix**: read the warning fully. Three honest paths it suggests: (a) take the brief to a real interlocutor; (b) return to socratic/provoke with the questions rehearsal surfaced; (c) sit with the brief without further rehearsal. Override is possible but should be deliberate.

## Outputs feel wrong

### Brief mode shows all fields as `[gap, not in input]`

**Cause**: you ran `brief` on insufficient material. The plugin's stay-rough default refuses to fabricate content for empty fields.

**Fix**: this is the correct behaviour. Go back to [`socratic`](../modes/socratic.md), [`provoke`](../modes/provoke.md), or [`lineage`](../modes/lineage.md) to generate the material the missing fields need. Then return to brief.

### Brief mode output sounds like AI-statement boilerplate

**Cause**: you used `--polish` and the smoothing flattened the artist's voice. Or you wrote your material in AI-statement register to begin with.

**Fix**: drop `--polish` and re-run; the stay-rough default preserves rough fragments verbatim. If the underlying material is already AI-toned, return to [`socratic`](../modes/socratic.md) with the instruction "stay rough, write fragments not paragraphs."

### Concept Pull Map (from socratic) feels wrong / does not match what I said

**Cause**: the Socratic dialogue followed your answers into a misreading. This is a normal failure mode.

**Fix**: say so directly. The plugin will re-ask the questions that produced the misfit. You can also reject any of the five categories (Impulses / Fragments / Constraints / Refusals / Residue) and have the plugin re-derive the map from your correction.

### Lineage map cites an artist I have never heard of

**Cause**: training-data canon bias or, in rare cases, lineage hallucination on a long-tail sub-domain. The mandatory bias header on every lineage map names the over- and under-represented sub-domains; if your work is in an under-represented area, treat unexpected-neighbor entries with extra scepticism.

**Fix**: read the bias header attached to the map. If the entry feels invented, ask the plugin "verify the citation for [entry]: source, year, primary reference." If verification fails, treat it as hallucination and remove it. See [Measured harms](../philosophy/measured-harms.md) §1.

### Provoke cards feel generic / not tradition-tagged

**Cause**: the plugin failed to ground a provocation in a tradition. This is rare but happens when the input is too abstract for any tradition to anchor.

**Fix**: give the plugin more concrete material to anchor in (a specific image, a phrase, a recent encounter), or explicitly request a tagged subset: `/art-project:provoke --tradition=oblique-strategies` or `--tradition=cage`.

## Project file (full mode)

### I cannot find my project file

**Cause**: project files default to `art-project-{slug}.md` in your *current Claude Code working directory* at the time of creation. If your working directory has changed, the file is in the original location.

**Fix**: search: `find ~ -name "art-project-*.md" -type f 2>/dev/null` (Unix) / `Get-ChildItem -Path $HOME -Filter "art-project-*.md" -Recurse -ErrorAction SilentlyContinue` (PowerShell).

### The plugin refuses to switch modes within one session

**Cause**: not a bug; it is the [full mode one-mode-per-session IRON rule](../modes/full.md). Cross-mode pipelining within a session structurally undermines the iterative cyclic web (Smith & Dean 2009).

**Fix**: close the session after the current mode finishes. Return to the project file in a new session for the next mode. The "studio time between sessions" is part of the design, not a limitation.

### Cross-session re-entry shows the wrong summary

**Cause**: the project file was edited outside the plugin between sessions (manually, by another tool, or by a sync conflict).

**Fix**: read the file directly to verify state. If it is corrupted, restore from version control (the project file should be in a git repo or backed up). The plugin does not auto-version project files — that is the artist's responsibility.

## Language and routing

### The plugin replies in English when I want Korean

**Cause**: the plugin matches the language of your input. If your input was mostly English (e.g. you typed a slash command + an English follow-up), the reply is in English.

**Fix**: write your next message in Korean. The plugin switches on its next reply. For persistent Korean preference within `/art-project:ideate`, add the line `language: ko` to the project file's frontmatter.

### Lineage map is anglophone-heavy when my work is Korean-context

**Cause**: training-data canon bias. The plugin's Korean / East-Asian default routing fires on session signals (input language, named candidates, explicit declaration); if those signals are weak, the routing may not engage.

**Fix**: name Korean precedents explicitly (e.g. "extend from Paik Nam-June and Lee Bul"), or use `--non-anglophone` flag to force the routing.

## Builds and dev

### MkDocs build warns about Material 2.0 deprecations

**Cause**: the Material for MkDocs team displays a banner about upcoming MkDocs 2.0 incompatibility on every build.

**Fix**: ignore; this is informational and unrelated to your build. Your build state is what `INFO -- Documentation built in N.NN seconds` says.

### Wiki Korean pages return 404 on the deployed site

**Cause**: GitHub Pages not enabled, or enabled with the wrong source.

**Fix**: in the repo Settings → Pages, set Source to **"GitHub Actions"** (not "Deploy from a branch"). Push or rerun the workflow; live URL is `https://<user>.github.io/art-project/` (en) + `/ko/` (ko).

### Local `mkdocs serve` returns 404 on `/ko/`

**Cause**: the dev server can serve the default locale at root but, depending on plugin/version, may not route to the `/ko/` prefix locally.

**Fix**: run `mkdocs build` and verify `site/ko/index.html` exists. The deployed site (via GitHub Actions) serves both locales correctly even if the local dev server's i18n routing is partial.

## When this page does not help

If a problem is not here:

1. Check the relevant mode page in [Modes](../modes/overview.md) for the IRON rules that govern that mode.
2. Check [Measured harms](../philosophy/measured-harms.md) for whether the behaviour is a known failure mode + mitigation.
3. Open an issue at the [repository](https://github.com/joonhyungbae/art-project/issues) with the slash command you ran, the exact error or unexpected output, and your platform (CLI / desktop app / web).
