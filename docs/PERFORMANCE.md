# art-paper Performance Notes

> Forked from academic-research-skills (ARS). Token budgets and long-running-session guidance are inherited from the genre-neutral pipeline machinery; the genre layer (art-paper authoring, jury review) does not materially change the per-stage token shape. The version tags below (v3.x) are inherited ARS provenance — the art-paper suite is v0.1.0.

> **Recommended model: Claude Opus 4.7** with **Max plan** (or equivalent configuration). Opus 4.7 uses adaptive thinking; you no longer set a fixed thinking budget.
>
> The full art-paper pipeline (10 stages) consumes a **large amount of tokens** — a single end-to-end run can exceed 200K input + 100K output tokens depending on paper length and revision rounds. Budget accordingly.
>
> Individual skills (e.g., `art-inquiry` alone, or `art-reviewer` alone) consume significantly less.

## Estimated token usage by mode

| Skill / Mode | Input Tokens | Output Tokens | Estimated Cost (Opus 4.7) |
|---|---|---|---|
| `art-inquiry` socratic | ~30K | ~15K | ~$0.60 |
| `art-inquiry` full | ~60K | ~30K | ~$1.20 |
| `art-inquiry` systematic-review | ~100K | ~50K | ~$2.00 |
| `art-paper` plan | ~40K | ~20K | ~$0.80 |
| `art-paper` full | ~80K | ~50K | ~$1.80 |
| `art-reviewer` full | ~50K | ~30K | ~$1.10 |
| `art-reviewer` quick | ~15K | ~8K | ~$0.30 |
| **Full pipeline (10 stages)** | **~200K+** | **~100K+** | **~$4-6** |
| + Cross-model verification | +~10K (external) | +~5K (external) | +~$0.60-1.10 |

*Estimates based on a ~15,000-word paper with ~60 references (the inherited ARS basis). SIGGRAPH Asia Art Papers are typically much shorter — verify the exact length budget against the current Art Papers CFP and scale these estimates down accordingly. Actual usage varies with paper length, revision rounds, and dialogue depth. Costs at Anthropic API pricing as of April 2026.*

## Recommended Claude Code settings

| Setting | What it does | How to enable | Docs |
|---|---|---|---|
| **Agent Team** (optional) | Enables `TeamCreate` / `SendMessage` tools for manual multi-agent coordination. **art-paper's internal parallelization does not require this flag** — skills spawn subagents via the built-in `Agent` tool directly. Only useful if you want to manually orchestrate persistent team workflows across sessions. | Set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (research preview) | Experimental feature — no stable docs yet |
| **Skip Permissions** | Bypasses per-tool confirmation prompts, enabling uninterrupted autonomous execution across all pipeline stages | Launch with `claude --dangerously-skip-permissions` | [Permissions](https://docs.anthropic.com/en/docs/claude-code/cli-reference) · [Advanced Usage](https://docs.anthropic.com/en/docs/claude-code/advanced) |

> **⚠️ Skip Permissions**: This flag disables all tool-use confirmation dialogs. Use at your own discretion — it is convenient for trusted, long-running pipelines but removes the safety net of manual approval. Only enable this in environments where you are comfortable with Claude executing file reads, writes, and shell commands without asking first.

### v3.7.0 Plugin agents and model routing

When art-paper is installed as a Claude Code plugin (`/plugin install art-paper`), three downstream worker agents are exposed as plugin-shipped subagents: `synthesis_agent`, `research_architect_agent`, and `report_compiler_agent`. Each declares `model: inherit` in its frontmatter, which means they run under the **dispatching session's model** rather than a pinned floor:

- An Opus session running the full pipeline gets Opus agents, preserving the integrative depth those agents were designed for.
- A Sonnet session gets Sonnet agents, matching the cost/latency profile of the parent run.
- The agents never silently fall back to Haiku — `inherit` resolves through the parent session's model, which is itself gated by the project policy of "no Haiku for art-paper runs."

This means **plugin-agent token costs track the per-mode estimates above unchanged**; there is no separate plugin agent surcharge or discount, because dispatched agents inherit the same model the parent run already pays for. If you change the main session model mid-pipeline (e.g., downshift to Sonnet for a long revision pass), the next agent dispatch picks up the new floor automatically.

Other art-paper agents (`bibliography_agent`, `literature_strategist_agent`, etc.) are not plugin-exposed at v0.1; they remain in-skill prompt templates that the main session executes inline, with no separate model routing layer. Wider plugin-agent coverage is deferred to a future release.

## Long-running session management

The full academic pipeline is designed for human-in-the-loop execution, with mandatory user confirmation at every stage. In practice, a full run often spans hours to days — longer than Anthropic's prompt cache TTL (5 minutes). Two consequences:

1. **Cache misses between checkpoints are normal.** When a stage checkpoint pauses longer than 5 minutes, the next stage reads its context uncached. This is an unavoidable cost of human-paced pipelines.
2. **Cross-session resume relies on Material Passport.** art-paper does not maintain its own orchestrator state between sessions. To resume in a new session, paste your Material Passport YAML back; the orchestrator reads `compliance_history[]` and stage completion markers to locate your breakpoint.

### v3.6.2 Sprint Contract jury cost (always-on for `full` / `realization-focus`)

The Schema 13 sprint contract gate splits each juror agent's run into Phase 1 (paper-content-blind, commits scoring plan) + Phase 2 (paper-visible review). For modes that ship templates (`full` panel 5 + `realization-focus` panel 2 — the panel-2 template ships as `shared/contracts/reviewer/methodology_focus.json`), each juror therefore costs roughly two LLM turns instead of one. Reserved modes (`re-review` / `calibration` / `guided` / `quick`) keep pre-v3.6.2 behaviour.

| Skill / Mode | Effect on tokens | Notes |
|---|---|---|
| `art-reviewer full` | ~+30-40% input + small output bump per juror × 5 jurors | Each juror reads the contract template + paper metadata in Phase 1, then full paper in Phase 2 |
| `art-reviewer realization-focus` | Same shape, panel 2 | Two jurors (Chair + practitioner-researcher / realization) each run two phases |
| Synthesizer (always one) | +~2-3K input | Reads contract + juror outputs to run three-step mechanical protocol |

Empirical measurement pending real review runs at scale. The two-phase shape is non-optional for the gated modes; treat as fixed overhead, not a tunable.

### v3.4.0 compliance agent cost

Adding the mode-aware `compliance_agent` to Stage 2.5 and Stage 4.5 increases full-pipeline SR tokens by approximately:

| Skill / Mode | Input Tokens | Output Tokens | Estimated Cost |
|---|---|---|---|
| `art-inquiry systematic-review` (2.5 only) | +~5–8K | +~3–5K | +~$0.15 |
| Full pipeline SR (2.5 + 4.5) | +~10–15K | +~5–8K | +~$0.30 |
| `art-paper full` (pre-finalize) | +~3–5K | +~2–3K | +~$0.08 |

These are on top of the existing per-skill costs in the table above (same 15,000-word / 60-reference basis; see footnote on line 23). Cross-model verification costs (if enabled) are unchanged.

### v3.6.3 Passport reset boundary (opt-in)

When `CRS_PASSPORT_RESET=1` is set, every FULL checkpoint becomes a context-reset boundary. The intended workflow is:

1. Run a stage to FULL checkpoint in session A.
2. Copy the `[PASSPORT-RESET: hash=<hash>, stage=<completed>, next=<next>]` tag from the checkpoint notification.
3. Start a fresh Claude Code session (session B) and paste `resume_from_passport=<hash>`. Optional overrides: `resume_from_passport=<hash> stage=<n> mode=<m>`.
4. Session B loads only the passport ledger; no replay of session A's turns. The orchestrator locates the matching `kind: boundary` entry, appends a `kind: resume` entry to consume it, and continues. The resumed stage is determined by: a `stage=` CLI override if supplied, else the matched option's `next_stage` when the boundary carries a `pending_decision` (the orchestrator re-prompts the user first), else the recorded `next` field. `next` MAY be `null` when all decision branches terminate.

**When reset beats continuation:**

- Long pipelines where session A has accumulated >100K input tokens of context that the next stage does not actually need.
- `systematic-review` mode runs where stage independence is cleanly defined by the Material Passport.
- Any case where you hit the 5-minute prompt-cache TTL mid-pipeline; a reset lets the next stage start fresh instead of paying a cache miss on a bloated context.

**When continuation still wins:**

- Short pipelines (< 30K input tokens end-to-end).
- Stages with implicit in-session state that the passport does not capture (e.g., a Socratic dialogue branch the user wants to keep warm).
- When the flag is OFF, continuation is the unchanged pre-v3.6.3 default.

**Passport file location convention:**

By default, the orchestrator looks for the passport file in `./passports/<slug>/` or matching `./material_passport*.yaml` relative to the current working directory. Resolving the hash to a passport file on disk is the integrator's responsibility; the orchestrator loads whichever passport the enclosing tool provides. See §"Passport file location convention" above for the `./passports/<slug>/` default.

The resume command only defines the hash and optional stage/mode overrides:

```
resume_from_passport=<hash> [stage=<n>] [mode=<m>]
```

There is no path syntax on the resume command itself. Custom passport locations are configured in the project's `CLAUDE.md` or handled by the integrator's tooling before the orchestrator is invoked.

**Empirical token savings:** measurement pending a real `systematic-review` run with instrumentation. This section will be updated with observed token deltas once available; until then, no numeric claim is made. See [`../art-pipeline/references/passport_as_reset_boundary.md`](../art-pipeline/references/passport_as_reset_boundary.md) for the full protocol.

## Literature corpus ingestion (v3.6.4+)

The Material Passport `literature_corpus[]` field is populated by user-written adapters, not art-paper itself. Three reference adapters ship at `scripts/adapters/folder_scan.py`, `scripts/adapters/zotero.py`, `scripts/adapters/obsidian.py` (inherited from ARS v3.6.4). See [`scripts/adapters/README.md`](../scripts/adapters/README.md) for how to run them and how to write your own.

### Performance posture

- Adapters run out-of-band (before a art-paper session, not during). Their runtime is the user's problem, not art-paper's.
- Adapters must be deterministic: re-running on identical input produces byte-identical output modulo timestamps.
- `literature_corpus[]` entries are sorted by `citation_key`; rejections are sorted by `source`.
- Adapter output size grows linearly with corpus size. A 500-entry Zotero library typically produces a passport of ~300 KB YAML. art-paper consumers should lazy-load when the corpus is large.

### Ingestion-layer boundaries

- Does not ingest PDFs, extract text, or run OCR.
- Does not call the Zotero Web API, Notion API, or any live service.
- Does not fetch paywalled content or use user credentials to access institutional libraries.

These boundaries are deliberate and reflect the inherited ARS data-layer decision (kept unchanged in art-paper): art-paper is a writing/review-layer framework; corpus integration stays in user-owned code. Users who want API-based live-sync adapters are expected to write them themselves, using the three reference adapters as starting points.

### Consumer-side integration

As of v3.6.5, two Phase 1 literature agents read `literature_corpus[]` via the **corpus-first, search-fills-gap** flow: `art-inquiry/agents/bibliography_agent.md` and `art-paper/agents/literature_strategist_agent.md`. Both consumers follow the same five-step shared flow and four Iron Rules (Same criteria / No silent skip / No corpus mutation / Graceful fallback on parse failure). Search Strategy reports gain a PRE-SCREENED reproducibility block that enumerates included / excluded / skipped corpus entries with F3 zero-hit and F4 provenance reporting. Consumer integration is presence-based — auto-engages when the passport carries a non-empty `literature_corpus[]` and parses cleanly; parse failures fall back to external-DB-only flow with a `[CORPUS PARSE FAILURE]` surface.

See [`art-pipeline/references/literature_corpus_consumers.md`](../art-pipeline/references/literature_corpus_consumers.md) for the full consumer protocol. `citation_compliance_agent` corpus integration is deferred (target version TBD post-v3.8).

### v3.6.5 corpus consumer cost (presence-gated)

When the Material Passport carries a non-empty `literature_corpus[]`, Phase 1 reads scale with corpus size. The PRE-SCREENED block emit itself is prompt-layer (effectively free); the LLM cost is Step 1 pre-screening — applying the current Inclusion / Exclusion criteria to each corpus entry's `title` (always present) and any populated optional fields (`abstract` / `tags`).

| Corpus size | Step 1 pre-screening (per consumer) | Notes |
|---|---|---|
| Empty / absent | 0 | External-DB-only flow runs unchanged |
| ~50 entries (typical Zotero subset) | +~3-5K input + ~1-2K output | Title + abstract scan |
| ~200 entries | +~10-15K input + ~3-5K output | Title-only scan dominates; abstract scan only when populated |
| ~500 entries (large library) | +~25-40K input + ~8-12K output | Consider trimming the corpus before passport emit |

Step 2 search-fills-gap reduces external-DB cost when `uncovered_topics` is small (case A), which can offset Step 1 cost. Empirical net delta pending real systematic-review run instrumentation; until then, no aggregate numeric claim is made. Parse failures cost roughly one short turn (parse + emit `[CORPUS PARSE FAILURE]` + fall back).

## v3.6.7 Step 6 cross-model audit wrapper (onboarding)

v3.6.7 Step 6 ships `scripts/run_codex_audit.sh` and `scripts/parse_audit_verdict.py`, which dispatch a separate codex CLI process to audit `synthesis_agent`, `research_architect_agent` (survey-designer mode), and `report_compiler_agent` (abstract-only mode) deliverables before stage transitions. The wrapper is the boundary object between deployment-side audit execution and art-paper-side artifact verification — see ARS v3.6.7 Step 6 spec §4 (kept as inherited provenance at [`ref/academic-research-skills/docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md`](../ref/academic-research-skills/docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md)) for the full contract.

### codex CLI install + credentials

The wrapper invokes `codex exec --json -m gpt-5.5 -c 'model_reasoning_effort="xhigh"'`. Required setup before first audit run:

| Step | macOS | Linux / WSL |
|---|---|---|
| Install codex CLI | `brew install codex` (or vendor installer) | vendor installer |
| Verify install | `codex --version` should print a `codex-cli X.Y.Z` line; the wrapper requires bare-semver match `^[0-9]+\.[0-9]+\.[0-9]+$` | same |
| Authenticate | `codex login` (browser SSO) OR set `OPENAI_API_KEY=...` in shell rc | same |
| Bash 4+ | `brew install bash` (stock macOS ships 3.2 — not supported) | distro default usually 5.x |
| `jq` | `brew install jq` | distro package |
| `sha256sum` (optional — wrapper falls back to `shasum -a 256`) | `brew install coreutils` | preinstalled |

The wrapper preflights every dependency at startup (§4.1 dependency table) and exits 64 (`EX_USAGE`) with `missing dependency: <name>` before touching any artifact file. No partial state is written when a dependency is missing.

### Required environment

| Variable | Required? | Purpose |
|---|---|---|
| `OPENAI_API_KEY` (or codex SSO session) | yes | codex CLI authentication |
| Standard PATH containing `codex`, `git`, `jq`, `python3` | yes | wrapper preflight checks each |
| Working directory inside the art-paper repo | yes | `git rev-parse --short HEAD` for `runner.git_sha`, repo-relative paths in sidecar |

The wrapper does NOT read any art-paper-specific environment variables (no `CRS_*` flags affect Step 6). Audit dispatch is purely flag-driven.

### Threat-model boundary

Per ARS v3.6.7 Step 6 spec §1.2 ([`ref/academic-research-skills/docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md`](../ref/academic-research-skills/docs/design/2026-04-30-ars-v3.6.7-step-6-orchestrator-hooks-spec.md), kept as inherited provenance), Step 6 defends against Pattern C3 (sub-agent fabricated audit metadata, where a downstream agent claims to have run audit and surfaces simulated findings). The artifact-as-contract design closes the inadvertent-overclaim attack surface: the wrapper produces four cryptographically-pinned files (jsonl + sidecar + verdict + proposal entry), and the orchestrator runs eleven layered verification checks before merging any audit outcome into the Material Passport.

Step 6 is **known-insufficient against motivated forgery** (a determined attacker with shell access could invoke codex with a different model and the JSONL stream alone would not betray them — see §9.1 R2). Two structural mitigations apply:

- **§4.7 wrapper-not-LLM-callable rule.** The wrapper MUST NOT be invoked by an in-LLM Bash tool call from the same session producing the audited deliverable. Allowed invokers: human interactive shell, CI workflow step, SubagentStop hook, second-terminal Bash from outside the LLM session. Same-session in-LLM invocation creates the Pattern C3 motive-and-means combination the artifact-as-contract design was chosen to disrupt.
- **Lifecycle ownership (§3.7 family E).** The wrapper writes only to `--output-dir`, never to the passport file. The orchestrator is the sole writer of `audit_artifact[]` entries. A wrapper-emitted proposal carrying `verdict.verified_at` or `verdict.verified_by` is rejected as malformed at lifecycle step 4 (Pattern C3 attack surface).

Deployment-side discipline is the load-bearing defense for the residual motivated-forgery surface; ARS spec-level enforcement is the partial inversion of the three downstream agent prompts (§6) so the agent has no awareness that a downstream audit exists, removing the trigger for fabricated tool-call hallucination.

### Wrapper exit-code contract

The wrapper's process exit code always agrees with the verdict it just wrote (§4.6):

| Exit code | Meaning | Verdict status | Orchestrator response |
|---|---|---|---|
| `0` | Audit completed cleanly | `PASS` / `MINOR` / `MATERIAL` | Read verdict, run §5.2 eleven gating checks, ship or block per §5.3 |
| `64` (`EX_USAGE`) | Input validation failed | none (no files written) | Block, surface `<missing flag>` error to user |
| `70` (`EX_SOFTWARE`) | codex itself exited 70 OR `parse_audit_verdict.py --probe` rejected JSONL OR bundle TOCTOU mutation detected | `AUDIT_FAILED` (with `failure_reason`) | §5.6 Path B5 short-circuits to BLOCK without gating |
| `73` (`EX_CANTCREAT`) | Tee write failed (disk full / EIO) | none / partial (cleaned up) | Block, surface filesystem error |
| `75` (`EX_TEMPFAIL`) | codex rate-limited OR SIGTERM/SIGINT received | `AUDIT_FAILED` | Same as 70: BLOCK without gating; deployment may apply backoff before retry |
| Other non-zero (1, 2, 137, …) | codex exited with a code not enumerated above; wrapper preserves the code rather than normalizing | `AUDIT_FAILED` | Same as 70: BLOCK without gating |

Even on AUDIT_FAILED, the wrapper writes all four contract files (jsonl placeholder + sidecar with `process.exit_code` carrying codex's actual exit + verdict.yaml carrying `status: AUDIT_FAILED` + proposal entry) so orchestrator can distinguish "audit ran but failed" (proposal exists with `AUDIT_FAILED`) from "audit never ran" (no proposal at all). Both states block transition; only `PASS / MINOR / MATERIAL` proposals reach the eleven gating checks.

### Cost posture

A typical Phase 2 chapter audit (synthesis + verification + bibliography bundle) runs codex `gpt-5.5` at `xhigh` reasoning effort for 30-90 seconds wall-clock per round. ARS-side cost is constant: the wrapper adds ~1-2 KB of metadata (sidecar + proposal entry) per audit run regardless of bundle size; the orchestrator's eleven-gate verification is sub-second per audit. The dominant cost is codex API usage on the deployment side, governed by audit template Section 1's three-round convergence target (§10 ship-quality target update).
