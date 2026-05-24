# art-paper Setup

Prerequisites and optional setup for art-paper, the practice-based art-paper fork of Academic Research Skills (ARS). If you only need Markdown output and the default Claude Opus 4.7 pipeline, you can skip most of this — see "Minimum viable setup" below.

> **Install endpoints.** art-paper installs from its own `joonhyungbae/art-paper` repo and marketplace; the `git clone` examples clone the same repo. The traditional symlink/copy flow targets the **`creative-*` skill directories** (`art-inquiry`, `art-paper`, `art-reviewer`, `art-pipeline`). The pristine ARS reference distribution is kept at `ref/academic-research-skills/` for diffing only — do not install from it.

---

## Minimum viable setup

1. Install Claude Code (see below).
2. Export `ANTHROPIC_API_KEY`.
3. `claude` in this repo (or any project that has art-paper in `.claude/skills/`).

That is enough for Markdown output + DOCX conversion instructions. Everything else in this document is optional.

---

## Install Claude Code

**Recommended: Native installer** (no Node.js required, auto-updates):

```bash
# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

<details>
<summary>Alternative: npm install (deprecated)</summary>

Requires Node.js 18+.

```bash
npm install -g @anthropic-ai/claude-code
```

</details>

## Set up API key

Get an Anthropic API key at <https://console.anthropic.com/>.

```bash
# Claude Code will prompt for your API key on first run
claude
```

Or set it as an environment variable:

```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## DOCX output (optional)

Direct `.docx` generation uses [Pandoc](https://pandoc.org/). If Pandoc is unavailable, the formatter falls back to Markdown + DOCX conversion instructions.

```bash
# macOS
brew install pandoc

# Linux (Debian/Ubuntu)
sudo apt-get install pandoc

# Windows — download from https://pandoc.org/installing.html
```

## acmart LaTeX → PDF output (canonical, optional toolchain)

The canonical art-paper output is **acmart LaTeX → PDF** (default class option `sigconf`). **IRON RULE: PDF is compiled from LaTeX, never HTML-to-PDF.** This requires a LaTeX toolchain plus the ACM `acmart` document class. **The toolchain is optional** — Markdown output and DOCX conversion instructions work without any of this.

**LaTeX engine** — [tectonic](https://tectonic-typesetting.github.io/) (recommended; downloads packages on demand) or a full TeX distribution (TeX Live / MiKTeX):

```bash
# macOS
brew install tectonic

# Linux (Debian/Ubuntu)
curl --proto '=https' --tlsv1.2 -fsSL https://drop-sh.fullyjustified.net | sh

# Windows — download from https://tectonic-typesetting.github.io/en-US/install.html
```

**ACM `acmart` document class** — the standard SIGGRAPH Asia / ACM template. Obtain it from [CTAN](https://ctan.org/pkg/acmart) or directly from the [ACM](https://www.acm.org/publications/proceedings-template). With tectonic, the class and `ACM-Reference-Format` bibliography style are fetched automatically on first compile; with TeX Live, install via your package manager (`tlmgr install acmart`) or unpack the CTAN bundle into your texmf tree. Do **not** rely on a stale vendored copy bundled in this repo — pull the current class from CTAN or the ACM so you track template updates.

> **Verify against the current CFP.** The exact `acmart` class option (e.g. `sigconf`), font requirements, anonymization rules, and any ACM Digital Library production constraints can change between SIGGRAPH Asia cycles. Confirm them against the current Art Papers CFP before final submission rather than trusting these defaults.

> If you only need Markdown output or DOCX conversion instructions, skip this entirely. Direct `.docx` generation requires Pandoc, and PDF generation requires the LaTeX toolchain above.

---

## Material Passport `literature_corpus[]` adapters (v3.6.4+, optional)

If you maintain a curated literature corpus (Zotero, Obsidian, a folder of PDFs, etc.), you can pre-load it into a Material Passport so Phase 1 art-paper agents read your library *before* searching external databases. This is opt-in and presence-based — when no corpus is supplied, art-paper runs the external-DB-only flow unchanged.

Three reference Python adapters ship with v3.6.4 at `scripts/adapters/`:

```bash
# 1. Install adapter dependencies (PyYAML + jsonschema, already in requirements-dev.txt)
pip install -r requirements-dev.txt

# 2. Run a reference adapter (pick one that matches your corpus source).
#    Both --passport and --rejection-log are required.
python scripts/adapters/folder_scan.py --input /path/to/pdfs               --passport passport.yaml --rejection-log rejection_log.yaml
python scripts/adapters/zotero.py      --input my-zotero-export.json       --passport passport.yaml --rejection-log rejection_log.yaml
python scripts/adapters/obsidian.py    --input ~/Obsidian/Lit\ Notes       --passport passport.yaml --rejection-log rejection_log.yaml

# 3. Pass the resulting passport.yaml into your art-paper session
#    (concrete invocation depends on which skill you're running — see scripts/adapters/README.md)
```

Each adapter emits two files: `passport.yaml` (Schema 9 with `literature_corpus[]` populated) and `rejection_log.yaml` (always emitted, empty when no rejections — closed enum of categorical reasons). Users with non-reference corpus sources are expected to write their own adapters following [`art-pipeline/references/adapters/overview.md`](../art-pipeline/references/adapters/overview.md).

v3.6.5 wires `bibliography_agent` (art-inquiry, Phase 1) and `literature_strategist_agent` (art-paper, Phase 1) as the consumers — both run the corpus-first / search-fills-gap flow when a non-empty corpus is present and parses cleanly. See [`art-pipeline/references/literature_corpus_consumers.md`](../art-pipeline/references/literature_corpus_consumers.md) for the consumer protocol.

## Optional environment flags (v3.5.1+)

art-paper exposes a few opt-in flags. All default to OFF; setting them changes behaviour for the current session only.

| Flag | Since | What it does | Reference |
|---|---|---|---|
| `CRS_CROSS_MODEL` | v3.0 | Enable cross-model verification (see next section) | [§"Cross-model verification"](#cross-model-verification-optional) |
| `CRS_SOCRATIC_READING_PROBE=1` | v3.5.1 | Activate the Socratic reading-check probe layer in `socratic_mentor_agent`. Goal-oriented intent only; fires at most once per session when user has cited a specific paper; decline logged without penalty. | `art-inquiry/agents/socratic_mentor_agent.md` |
| `CRS_PASSPORT_RESET=1` | v3.6.3 | Promote every FULL checkpoint to a context-reset boundary. Required to *emit* boundary entries; **not** required to invoke `resume_from_passport=<hash>` in a fresh session. With the flag ON in `systematic-review` mode, reset is mandatory at every FULL checkpoint. | `art-pipeline/references/passport_as_reset_boundary.md` |
| `CRS_CROSS_MODEL_SAMPLE_INTERVAL` | v3.5.0 | Sampling interval for cross-model integrity checks (advisory) | `shared/cross_model_verification.md` |

---

## Cross-model verification (optional)

art-paper works with Claude Opus 4.7 alone. For higher confidence, you can optionally enable a second AI model to independently verify integrity checks and challenge the devil's advocate.

### Quick setup

```bash
# Step 1: Set your API key (choose one or both)
export OPENAI_API_KEY="sk-your-key-here"        # For GPT-5.4 Pro
export GOOGLE_AI_API_KEY="AIza-your-key-here"    # For Gemini 3.1 Pro

# Step 2: Choose your cross-verification model
export CRS_CROSS_MODEL="gpt-5.4-pro"            # Best reasoning
# or: export CRS_CROSS_MODEL="gemini-3.1-pro-preview"  # Strong at factual verification

# Step 3: Run Claude Code as normal — cross-verification activates automatically
claude
```

### What changes when enabled

| Feature | Without cross-model | With cross-model |
|---|---|---|
| Integrity verification | Single-model 100% check | + 30% sample independently verified by 2nd model |
| Devil's Advocate | Single-model DA | + Cross-model generates independent critique, novel findings added |
| Peer Review | 5 reviewers (same model) | Same 5 reviewers + cross-model DA critique/calibration support |

### Cost

Full pipeline adds ~$0.60-1.10 in cross-model API costs (GPT-5.4 Pro pricing). See [`shared/cross_model_verification.md`](../shared/cross_model_verification.md) for the detailed breakdown.

### No API key? No problem

Without `CRS_CROSS_MODEL` set, everything works exactly as before. The cross-model features are invisible and add zero overhead.

---

## Installation methods

Claude discovers skills at `<install-root>/<skill-name>/SKILL.md`. This repo contains four separate skills, each with its own `SKILL.md`:

- `art-inquiry`
- `art-paper`
- `art-reviewer`
- `art-pipeline`

Do not install the whole repository as one nested skill folder under `.claude/skills/academic-research-skills/`; that buries the four `SKILL.md` files one level too deep for discovery. See Anthropic's [Claude Code Skills documentation](https://code.claude.com/docs/en/skills).

### Method 0: Claude Code Plugin (v3.7.0+, recommended for Claude Code CLI / IDE users)

If you use Claude Code CLI, VS Code extension, or JetBrains extension, install art-paper as a plugin:

```text
/plugin marketplace add joonhyungbae/art-paper
/plugin install art-paper
```

The `marketplace add` endpoint is the art-paper repo `joonhyungbae/art-paper`; the installed plugin is `art-paper`.

The four skills (`art-inquiry`, `art-paper`, `art-reviewer`, `art-pipeline`) are auto-discovered from the plugin's `skills/` directory.

**Strongly recommended: open auto-update.** Open the `/plugin` UI, find `art-paper`, and toggle auto-update on. To refresh manually: `/plugin update art-paper`. (`/plugin marketplace update` only refreshes the marketplace source list, not the installed plugin itself.)

**Plugin platform scope:**
- ✅ Claude Code CLI / VS Code extension / JetBrains extension — full support
- ❌ claude.ai web / Claude for Work / Anthropic API direct calls — plugins not supported; use Method 1 / 2 / 3 below
- ➡️ Codex CLI / other agent platforms — no art-paper sibling distribution exists at v0.1.

### Method 1: As project skills (recommended)

Use this when you want art-paper available inside an existing Claude Code project.

Clone the repo to a stable local path, then copy each skill folder into your project's `.claude/skills/` directory:

```bash
git clone https://github.com/joonhyungbae/art-paper.git ~/art-paper

cd /path/to/your/project
mkdir -p .claude/skills
cp -R ~/art-paper/art-inquiry .claude/skills/art-inquiry
cp -R ~/art-paper/art-paper .claude/skills/art-paper
cp -R ~/art-paper/art-reviewer .claude/skills/art-reviewer
cp -R ~/art-paper/art-pipeline .claude/skills/art-pipeline
```

Expected path shape:

```text
/path/to/your/project/.claude/skills/art-inquiry/SKILL.md
/path/to/your/project/.claude/skills/art-paper/SKILL.md
/path/to/your/project/.claude/skills/art-reviewer/SKILL.md
/path/to/your/project/.claude/skills/art-pipeline/SKILL.md
```

Then copy the `.claude/CLAUDE.md` content into your project's `.claude/CLAUDE.md` (merge with existing if you have one).

> **Global Claude Code installation:** To make these skills available across your Claude Code projects, install the four folders to `~/.claude/skills/` instead:
>
> ```bash
> git clone https://github.com/joonhyungbae/art-paper.git ~/art-paper
>
> mkdir -p ~/.claude/skills
> cp -R ~/art-paper/art-inquiry ~/.claude/skills/art-inquiry
> cp -R ~/art-paper/art-paper ~/.claude/skills/art-paper
> cp -R ~/art-paper/art-reviewer ~/.claude/skills/art-reviewer
> cp -R ~/art-paper/art-pipeline ~/.claude/skills/art-pipeline
> ```

### Method 2: As a standalone project

Use this when you want to work directly inside the art-paper repository.

```bash
git clone https://github.com/joonhyungbae/art-paper.git art-paper
cd art-paper
claude
```

<details>
<summary><strong>No Git?</strong> Download as ZIP instead</summary>

1. Go to <https://github.com/joonhyungbae/art-paper>
2. Click the green **Code** button → **Download ZIP**
3. Extract the ZIP to your desired location
4. For Method 1: copy the four extracted skill folders (`art-inquiry`, `art-paper`, `art-reviewer`, `art-pipeline`) into `.claude/skills/` inside your project
5. For standalone use: open a terminal in the extracted folder and run `claude`

</details>

### Method 3: Claude Cowork (desktop)

Use this when you want the four art-paper skills available in [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork), Claude Desktop's agentic workspace.

Cowork uses the same skill folder shape: `~/.claude/skills/<skill-name>/SKILL.md`.

#### Prerequisites

- Claude Desktop latest version on macOS or Windows. Download from Anthropic's [Claude Desktop page](https://claude.ai/download).
- Active internet connection; Cowork tasks call the Anthropic API.
- Keep Claude Desktop open while Cowork tasks run. Cowork runs inside the Desktop process.
- Folder/file permissions that allow Cowork to read and write in the project folder.
- A paid plan with Cowork access. See Anthropic's [Cowork requirements](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) for current plan availability.
- On Team or Enterprise plans, your organization admin may have disabled Skills, plugins, connectors, or egress. If installed skills do not register after restart, ask your admin to check org-level controls.

#### Option A: symlink install (fastest, single-machine)

Use symlinks if you work on one machine and want updates by pulling the repo.

```bash
git clone https://github.com/joonhyungbae/art-paper.git ~/art-paper

mkdir -p ~/.claude/skills
cd ~/.claude/skills
ln -s ~/art-paper/art-inquiry art-inquiry
ln -s ~/art-paper/art-paper art-paper
ln -s ~/art-paper/art-reviewer art-reviewer
ln -s ~/art-paper/art-pipeline art-pipeline
```

Expected path shape:

```text
~/.claude/skills/art-inquiry/SKILL.md
~/.claude/skills/art-paper/SKILL.md
~/.claude/skills/art-reviewer/SKILL.md
~/.claude/skills/art-pipeline/SKILL.md
```

If you sync `~/.claude/skills` across machines via a cloud folder, use Option B instead. Absolute-path symlinks can break on a fresh checkout or another machine.

#### Option B: copy install (cross-machine safe, no auto-update)

Use copies if you sync `~/.claude/skills` across machines or do not want symlinks. Updates require re-running the four `cp -R` commands.

```bash
git clone https://github.com/joonhyungbae/art-paper.git ~/art-paper

mkdir -p ~/.claude/skills
cp -R ~/art-paper/art-inquiry ~/.claude/skills/art-inquiry
cp -R ~/art-paper/art-paper ~/.claude/skills/art-paper
cp -R ~/art-paper/art-reviewer ~/.claude/skills/art-reviewer
cp -R ~/art-paper/art-pipeline ~/.claude/skills/art-pipeline
```

Expected path shape:

```text
~/.claude/skills/art-inquiry/SKILL.md
~/.claude/skills/art-paper/SKILL.md
~/.claude/skills/art-reviewer/SKILL.md
~/.claude/skills/art-pipeline/SKILL.md
```

#### Create or open a Cowork Project

See Anthropic's [Organize your tasks with Projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) for the canonical UI walk-through.

1. Open Claude Desktop.
2. Use the mode selector (**Chat / Cowork**) and switch to **Cowork**.
3. In **Tasks**, use the left navigation panel and choose **Use an existing folder**.
4. Select the local folder you want Cowork to work in. This creates a Cowork Project pointing at that folder.
5. Restart Cowork after installing or updating the skill folders so the four skills register.

#### How Cowork invokes the skills

Claude uses each skill's `description` to judge relevance, as described in Anthropic's [Skills documentation](https://code.claude.com/docs/en/skills). Example phrases such as "help me write a paper" are illustrative, not literal trigger phrases; paraphrased intent works too.

If description-based routing does not select the skill you want, Cowork also provides explicit UI surfaces described in Anthropic's [Cowork plugins documentation](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork):

- Type `/` in a Cowork Task to use the command palette and select an available skill.
- Use the `+` capability picker to add a skill to the current Task.

### Method 4: Use with claude.ai (web)

art-paper is a Claude Code-native suite. The four skills are 12-13-agent teams that depend on multi-agent orchestration, executable scripts under `scripts/`, and Material Passport file handoffs. claude.ai's web interface delivers a different runtime than Claude Code, and the two access paths it offers reach this repository in different ways:

- **Method 4b — Project + GitHub integration** (recommended for claude.ai users): brings the repository into a claude.ai Project as retrievable knowledge. Claude can read the skill bodies, references, schemas, and example outputs, and answer questions or draft against them. Not a Skill install — auto-loading and skill routing do not happen, but the content is fully available for reading and citation.
- **Method 4a — Custom Skill upload**: claude.ai's standard Skill install path (Settings → Capabilities → Skills, one zip per skill). Not recommended for this suite — see the rationale below before using it.

#### Prerequisites

- A claude.ai account. Plan availability differs by sub-method (see below).
- **For Method 4b**: claude.ai Projects are available across plan tiers per Anthropic's [What are Projects?](https://support.claude.com/en/articles/9517075-what-are-projects); paid plans (Pro, Max, Team, Enterprise) get larger knowledge capacity and stronger retrieval. GitHub authentication is required through the Anthropic connector — see [Using the GitHub integration](https://support.claude.com/en/articles/10167454-using-the-github-integration) and [Set up Claude integrations](https://support.claude.com/en/articles/10168395-set-up-claude-integrations). Private repositories require the Anthropic GitHub App to be authorized on the repo or organization. Team and Enterprise plans require owner-level connector enablement before users can add GitHub-sourced files.
- **For Method 4a**: Custom Skills are available on Free, Pro, Max, Team, and Enterprise per Anthropic's [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude). The same article notes that Skills require **code execution to be enabled** in Settings → Capabilities. No GitHub authentication is needed for Method 4a — you zip each skill folder locally and upload one zip per skill through Settings → Capabilities → Skills. Zip structure errors and the 200-character `description` cap surface as upload-time errors; see Anthropic's [Custom Skills packaging documentation](https://claude.com/docs/skills/how-to) and [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

#### Method 4b: Project + GitHub integration (recommended for claude.ai)

claude.ai Projects deliver content as static knowledge for Claude to retrieve and cite — see Anthropic's [What are Projects?](https://support.claude.com/en/articles/9517075-what-are-projects). This is NOT a Skill install. Skill auto-loading does not happen. Trigger phrases do not route. Claude can read the repo content for reading and citation, and answer questions about it, but does not execute the skills as agentic workflows.

Use this when you want claude.ai to have access to the repo content — including the agent definitions, references, and example outputs — for reading and citation, without needing agentic skill execution. For agentic execution, use Method 3 (Cowork) on the desktop, or Methods 1-2 in Claude Code.

1. Sign in to [claude.ai](https://claude.ai).
2. Create a new Project: **Projects** → **Create Project**.
3. Import from GitHub: in the Project, click **Files** → **+** → **GitHub** → select `joonhyungbae/art-paper`.
4. Select the folders/files below.

   | Select | Directory / file | Why |
   |---|---|---|
   | ✅ | `art-inquiry/` | Core skill content for reading |
   | ✅ | `art-paper/` | Core skill content for reading |
   | ✅ | `art-reviewer/` | Core skill content for reading |
   | ✅ | `art-pipeline/` | Core skill content for reading |
   | ✅ | `shared/` | Cross-model verification, handoff schemas, shared protocols |
   | ✅ | `scripts/` | `literature_corpus[]` adapters (`folder_scan`, `zotero`, `obsidian`) + schema validators; required for Material Passport corpus mode and CI-style validation |
   | ✅ | `MODE_REGISTRY.md` | Mode definitions |
   | Optional | `.claude/` | Project-level routing rules. Skip if you set Project Instructions in step 5 below (recommended path); include only if you prefer to keep routing rules visible as Project files. |
   | Optional | `examples/` | Useful for reference examples; skip if you want a smaller Project knowledge set |
   | Optional | `.github/`, READMEs, LICENSE, etc. | Repository metadata; not needed for core reading context |

5. (Recommended) Set **Instructions** in the Project to the content of `.claude/CLAUDE.md` for better routing.
6. Start chatting: "Guide my research on X" or "Help me write a paper about Y".

Anthropic's current [Project file limits](https://support.claude.com/en/articles/8241126-upload-files-to-claude) state that Project file count is not artificially capped at 200; files have a 30 MB per-file limit and total usable content is still subject to context-window limits at runtime. Keep the Project focused so Claude retrieves the relevant files reliably.

#### Method 4a: Custom Skill upload (not recommended for this suite)

Method 4a is claude.ai's standard Custom Skill install path: zip each skill folder, upload through Settings → Capabilities → Skills, and Claude treats it as an installed Skill with auto-loading and routing. claude.ai's Custom Skills do support multi-file skill packages including `scripts/` (see Anthropic's [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) on supporting files and code execution), so Method 4a is mechanically capable of hosting skills with executable assets. The reasons not to recommend it for this specific suite are different and compound:

1. **art-paper depends on Claude Code-only orchestration features**. Each art-paper skill drives 12-13 specialised agents through Claude Code's Task / subagent tooling and Material Passport file handoffs that resume across sessions. The Anthropic-documented scope of claude.ai's Custom Skill runtime — a containerised code-execution environment per session, with the Skills user guide ([Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)) describing skill activation but not multi-agent dispatch — does not include Claude Code's Task / subagent control surface. Method 4a is therefore expected to surface art-paper as the SKILL.md body's instructions, without the multi-agent dispatch that produces the suite's actual outputs. We have not run a live upload to characterise this in detail; the recommendation is forward-looking based on the Claude Code-specific assumptions baked into the agent orchestration, not on a measured failure.
2. **Cost to Claude Code and Cowork routing**. claude.ai limits each skill's `description` field to 200 characters per the [Custom Skills documentation](https://claude.com/docs/skills/how-to), while the [Agent Skills specification](https://agentskills.io/specification) and [Claude Code Skills documentation](https://code.claude.com/docs/en/skills) allow up to 1,024 characters. The four art-paper descriptions currently sit in the 440-842 range, front-loading routing keywords that Claude Code and Cowork use to discriminate between research, writing, review, and orchestration. Trimming them to fit Method 4a would weaken routing on Claude Code and Cowork — the platforms art-paper was built for — in exchange for an unverified partial fit on claude.ai.

**Recommended paths instead:**

- For agentic skill execution on the desktop, use [Method 3 (Cowork)](#method-3-claude-cowork-desktop). All four skills register as Cowork capabilities, with multi-agent orchestration intact.
- For claude.ai web access to the repo content, use [Method 4b (Project + GitHub integration)](#method-4b-project--github-integration-recommended-for-claudeai). Claude reads the skill bodies, references, and examples, and you can ask questions or draft against them in a normal claude.ai chat.
- For Claude Code projects, use [Method 1 (project skills)](#method-1-as-project-skills-recommended) or [Method 2 (standalone)](#method-2-as-a-standalone-project).

If you still want to try Method 4a despite the limitations above, zip each skill folder so the archive's top-level entry is `<skill-name>/SKILL.md` (not `<skill-name>/<skill-name>/SKILL.md` — that nesting buries the discovery file one level too deep). The `zip -r` commands below produce that shape correctly:

```bash
git clone https://github.com/joonhyungbae/art-paper.git art-paper
cd art-paper

zip -r art-inquiry.zip art-inquiry
zip -r art-paper.zip art-paper
zip -r art-reviewer.zip art-reviewer
zip -r art-pipeline.zip art-pipeline
```

Then in claude.ai:

1. Sign in to [claude.ai](https://claude.ai).
2. Open **Settings**.
3. Open **Capabilities**.
4. Open **Skills**.
5. Upload `art-inquiry.zip`.
6. Upload `art-paper.zip`.
7. Upload `art-reviewer.zip`.
8. Upload `art-pipeline.zip`.

The upload UI will reject each zip with a description-too-long error because every art-paper description exceeds claude.ai's 200-character cap. The descriptions are intentionally not trimmed; see the rationale above.

**claude.ai vs Claude Code:**

- Method 4b is for content reading, not active Skill execution. For agentic skill execution, prefer Methods 1-3.
- claude.ai does not support local shell commands; results may be less comprehensive than Claude Code workflows that rely on local scripts.
- Cross-model verification (`CRS_CROSS_MODEL`) requires Claude Code with API keys.
- Direct `.docx` generation requires Pandoc, and LaTeX/PDF output requires Claude Code with `tectonic`; claude.ai can still produce Markdown and DOCX conversion instructions.