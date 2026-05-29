#!/usr/bin/env bash
# version: 0.1.0
#
# SessionStart hook script for the art-project Claude Code plugin.
#
# Reads the SessionStart event JSON on stdin and emits a hookSpecificOutput
# JSON with `additionalContext` describing what art-project provides in this
# session. The plugin loader injects that context into the LLM's first turn
# so the user (and Claude) can see, on session start, that art-project is
# loaded and which slash commands and (v0.2-aligned) plugin agents are
# available.
#
# Renamed and rewritten on 2026-05-30 from the prior art-paper-era version,
# which still announced 13 art-paper slash commands and a SIGGRAPH Asia
# trajectory. The Runtime-Readiness Audit on the same date classified that
# announcement as misinformation; this rewrite brings the SessionStart hook
# into line with the actual v0.1.0 art-project plugin surface.
#
# Allowed invokers: Claude Code's plugin loader (SessionStart event).
# This script is safe to run from any context; it does not invoke codex,
# does not write outside its own stdout, and produces no side effects on
# the working tree.
#
# Exit codes:
#   0    Always — even on parse failure, fall back to the long-form announce.
#   2    Reserved (not used; SessionStart cannot block).

set -euo pipefail

# ---------------------------------------------------------------------------
# Bash 3.2 compatible (no associative arrays, no `${!var}`, no hot-path
# here-strings) so macOS stock /bin/bash users see the announce without
# installing a newer bash.
# ---------------------------------------------------------------------------
INPUT=""
if [[ ! -t 0 ]]; then
  INPUT=$(cat)
fi

SOURCE="startup"
if [[ -n "${INPUT}" ]]; then
  if [[ "${INPUT}" =~ \"source\"[[:space:]]*:[[:space:]]*\"([a-z]+)\" ]]; then
    SOURCE="${BASH_REMATCH[1]}"
  fi
fi

case "${SOURCE}" in
  compact|resume)
    ANNOUNCE="art-project plugin still loaded after ${SOURCE}. Slash commands: /art-project:socratic /art-project:provoke /art-project:lineage /art-project:brief /art-project:rehearsal /art-project:ideate. Plugin agents (v0.2-aligned, dispatched lazily): socratic_mentor_agent, bibliography_agent, devils_advocate_agent, editor_in_chief_agent. Four legacy agents (research_question, source_verification, synthesis, monitoring) are v0.1-deprecated, retained as historical artefacts — see art-ideation/SKILL.md Agent inventory."
    ;;
  startup|clear|*)
    ANNOUNCE="art-project plugin loaded — a pre-studio articulation scaffold for practice-based artistic research. NOT an ideation engine: the Penny / Ingold / Borgdorff critique that artistic ideation is non-linguistic, material, and inseparable from making is accepted; the plugin scopes itself to the propositional articulation work around ideation. The actual ideation happens in the studio, with material.

One skill (art-ideation), six modes — slash commands with model routing pinned in frontmatter:
  /art-project:socratic    opus    Pre-reflective dialogue surfacing impulse / fragments / constraints / refusals / residue. IRON RULE: no auto-convergence under exploratory intent.
  /art-project:provoke     sonnet  Tradition-tagged provocations with preserved unhelpfulness (no auto-interpretation), counter-formulations in tension, Authentic Practice Boundary per card.
  /art-project:lineage     sonnet  Lineage Map extending artist-supplied initial candidates. Mandatory training-data bias header. Korean / East-Asian default routing on Korean sessions.
  /art-project:brief       sonnet  Concept Brief with epistemic fields (proposition / anti-proposition / disconfirmation / Frayling-type declaration). Stay-rough default — prose stays in the artist's voice; no auto-completion of gaps.
  /art-project:rehearsal   opus    Self-Critique Rehearsal (Curator + Practitioner-peer + Theorist + Devil's Advocate). Formative not decisional. Mandatory disclaimer; persona-collapse detector; architectural friction against repeated use.
  /art-project:ideate      opus    Open or continue a long-running art-project file across multiple sessions (Smith & Dean iterative cyclic web). One mode per session; cross-session re-entry is first-class.

Natural-language entry is also supported (e.g. \"guide me through a new project\", \"이 작품 자료 좀 정리해줘\"); the skill auto-routes via intent detection and announces the routing decision transparently.

Plugin agents (v0.2-aligned, lazy-dispatch via SKILL.md):
  socratic_mentor_agent       Pre-reflective dialogue support (Frayling / Borgdorff / Sullivan).
  bibliography_agent          Lineage retrieval support; East-Asian default-routing wiring documented in commands/lineage.md.
  devils_advocate_agent       Rehearsal Devil's-Advocate persona; Concession Threshold Protocol intact.
  editor_in_chief_agent       Rehearsal Chair-synthesis; full formative-not-decisional reshape pending.

Four legacy agents (research_question, source_verification, synthesis, monitoring) carry v0.1-DEPRECATED banners — do not invoke. See art-ideation/SKILL.md Agent inventory + docs/PLUGIN-RUNTIME-READINESS-AUDIT.md.

User wiki: https://joonhyungbae.github.io/art-project/ (EN) / /ko/ (KO).
License: CC-BY-NC 4.0. Design spec: docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md."
    ;;
esac

escape_json() {
  local raw="$1"
  raw="${raw//\\/\\\\}"
  raw="${raw//\"/\\\"}"
  raw="${raw//$'\n'/\\n}"
  printf '%s' "${raw}"
}

ESCAPED=$(escape_json "${ANNOUNCE}")

cat <<JSON
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"${ESCAPED}"}}
JSON

exit 0
