#!/usr/bin/env bash
# version: 0.1.0
#
# SessionStart hook script for the art-paper (art-paper) Claude Code plugin.
#
# Reads the SessionStart event JSON on stdin and emits a hookSpecificOutput
# JSON with `additionalContext` describing what art-paper provides in this session.
# The plugin loader injects that context into the LLM's first turn so the
# user (and Claude) can see, on session start, that art-paper is loaded and which
# slash commands and plugin agents are available.
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
    ANNOUNCE="art-paper plugin still loaded after ${SOURCE}. Slash commands: /art-full /art-plan /art-outline /art-revision /art-revision-coach /art-abstract /art-lit-review /art-reviewer /art-format-convert /art-citation-check /art-disclosure /art-mark-read /art-unmark-read. Plugin agents: synthesis_agent, research_architect_agent, report_compiler_agent."
    ;;
  startup|clear|*)
    ANNOUNCE="art-paper (art-paper) plugin loaded — practice-based art papers for the SIGGRAPH Asia Art Papers track (proceedings on the ACM Digital Library; verify against the current CFP).

Slash commands (13) — model routing pinned in frontmatter:
  /art-full              opus    Full art-paper pipeline (inquiry → write → jury review → revise → finalize)
  /art-revision-coach    opus    Parse jury comments → Revision Roadmap + Response Letter skeleton
  /art-reviewer          opus    art-reviewer full mode — simulated SIGGRAPH Asia Art Papers jury
  /art-plan              sonnet  Socratic section-by-section art-paper planning
  /art-outline           sonnet  Detailed outline + evidence map (no full draft)
  /art-revision          sonnet  Revised draft + response to jury
  /art-abstract          sonnet  Art-paper abstract + keywords
  /art-lit-review        sonnet  Conceptual-lineage / precedent-works review in paper format
  /art-format-convert    sonnet  Convert paper between acmart LaTeX / DOCX / PDF / Markdown
  /art-citation-check    sonnet  ACM Reference Format citation error report
  /art-disclosure        sonnet  ACM / SIGGRAPH Asia AI-usage disclosure statement
  /art-mark-read         sonnet  Record human-read signal for one or more citation keys
  /art-unmark-read       sonnet  Rescind a prior human-read mark for one or more citation keys

Plugin agents (3, model: inherit) — dispatched by the art-paper pipeline:
  synthesis_agent             Cross-source integration; artwork-as-evidence triangulation
  research_architect_agent    Practice-based methodology blueprint
  report_compiler_agent       ACM Reference Format art-paper drafting (Phase 4 + Phase 6)

Other art-paper agents (bibliography_agent, literature_strategist_agent, field_analyst_agent, etc.) remain in-skill prompt templates loaded via SKILL.md, not plugin agents.

The artwork is primary evidence (shared/references/art_research_evidence_model.md). Output is acmart LaTeX → PDF. Verify venue specifics against the current SIGGRAPH Asia Art Papers CFP.

Token budget reference: docs/PERFORMANCE.md (a single full pipeline run ≈ \$4–6 on Opus 4.7)."
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
