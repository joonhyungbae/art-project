# Marketplace discoverability — ready-to-apply actions

The plugin already ships through the canonical Claude Code mechanism:

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

This document lists the *additional* discoverability moves you can apply **from a web browser in ~15 minutes**, using copy-paste material assembled here so you do not need to draft anything yourself.

---

## 1. GitHub Topics (5 min, web UI)

Open the repo on github.com → **About** (top-right gear icon) → **Topics** field.

Paste these topics (GitHub topics must be lowercase, hyphen-separated, ≤50 chars). Order does not matter:

```text
claude-code-plugin
claude-code
anthropic
ai-creativity-tool
creativity-support-tool
practice-based-research
artistic-research
par
pre-studio-articulation
concept-brief
tradition-tag
authentic-practice-boundary
cognitive-scaffold
extended-mind
artist-statement
grant-writing
doctoral-exposition
korean-art
east-asian-aesthetics
art-and-technology
generative-art
oblique-strategies
john-cage
sol-lewitt
practice-as-research
research-through-design
research-for-art
research-into-art
self-critique-rehearsal
lineage-mapping
```

While at the **About** panel, also set:
- **Description**: *A Claude Code plugin: pre-studio articulation scaffold for practice-based artistic research. Not an ideation engine. Six modes (socratic / provoke / lineage / brief / rehearsal / full) grounded in a tradition-tag reference layer with authentic-practice boundaries.*
- **Website**: `https://apesuite.org/plugins/` (apesuite is the canonical wiki host as of 2026-06-12)
- Check ☑ **Include in the home page** under Releases, Packages.

GitHub topics surface the repo on `github.com/topics/<topic>` pages and in GitHub search. The first three (`claude-code-plugin`, `claude-code`, `anthropic`) target the Claude Code ecosystem; the remainder target the practice-based-research and creativity-support-tool research communities.

---

## 2. awesome-claude-code PR (10 min, prepare locally → submit via web)

The community list lives at `github.com/hesreallyhim/awesome-claude-code` (the most active one as of 2026-05). It accepts PRs in a specific structured format.

### Step 1 — Fork + clone

On github.com, click **Fork** on `hesreallyhim/awesome-claude-code`. Then locally:

```bash
git clone https://github.com/<your-github-username>/awesome-claude-code.git
cd awesome-claude-code
git checkout -b add-art-project
```

### Step 2 — Find the right section

Open `README.md`. The list is sectioned (Hooks / Status Lines / Slash Commands / Workflows & Knowledge Guides / CLI Tools / Plugins or similar). Find the **Plugins** section (it may be named "Marketplaces / Plugins" or "Community Plugins"). If a Plugins section does not yet exist, the simplest move is to add a new `## 🎨 Plugins — Art & Practice-Based Research` section near the bottom.

### Step 3 — Paste this entry verbatim

```markdown
- [art-project](https://github.com/joonhyungbae/art-project) — A pre-studio articulation scaffold for practice-based artistic research. Six modes (socratic / provoke / lineage / brief / rehearsal / full) grounded in a tradition-tag reference layer with authentic-practice boundaries (Eno & Schmidt, Cage, LeWitt, Bogart, Frayling, Borgdorff, Sullivan). Not an ideation engine; scoped to the propositional articulation work *around* ideation. Bilingual EN/KO wiki, CC-BY-NC 4.0. [_install:_ `/plugin marketplace add joonhyungbae/art-project`]
```

### Step 4 — Commit, push, open PR

```bash
git add README.md
git commit -m "Add art-project (pre-studio articulation scaffold for PaR)"
git push origin add-art-project
```

Then on github.com, open the PR. **PR title:**

> Add art-project — pre-studio articulation scaffold for practice-based artistic research

**PR body** (copy-paste):

```markdown
## What
Adds art-project, a Claude Code plugin that scaffolds the pre-studio articulation phase of practice-based artistic research.

## Why a different category from other CST plugins
art-project deliberately scopes *outside* artistic ideation itself (accepting the Penny / Ingold / Borgdorff critique that artistic ideation is non-linguistic, material, inseparable from making). It targets the propositional work *around* ideation — grant applications, doctoral expositions, residency proposals, collaborator briefings — for artists whose articulation is a bottleneck (early-career, second-language writers, PaR-doctoral candidates, grant-deadline). Six modes (socratic / provoke / lineage / brief / rehearsal / full) operationalise the cognitive-scaffold position of Clark & Chalmers 1998 / Malafouris 2013.

## Differentiation
- Tradition-tag reference layer + per-method **Authentic Practice Boundary** (each cited methodology declares what the plugin does *not* simulate — e.g. Cage proposes the chance procedure, the artist throws the dice; LeWitt prompts the artist to write the instruction; Oblique Strategies' physical deck is irreplaceable).
- Bilingual EN / KO wiki (Korean / East-Asian default routing on Korean sessions; non-anglophone lineage entries prioritised).
- No-fabrication discipline validated empirically: zero ex-nihilo fabrications across 90 generative-layer cells in a reconstruction benchmark (15 cases × 6 fields).

## Reproducibility / scholarly basis
Underlying paper is in submission to *Digital Creativity* (Routledge / T&F, AHCI). Reproducibility package includes input packs, gold briefs, pre-registration hash, and analysis scripts.

## License
CC-BY-NC 4.0.
```

---

## 3. SEO / wiki landing-page nudge (already shipped)

The wiki's `site_description` (`mkdocs.yml`) was tightened in this commit to surface the load-bearing keywords (`pre-studio articulation`, `practice-based artistic research`, `tradition-tag`, `authentic-practice boundaries`, `Frayling`, `Borgdorff`, `Penny`, `Ingold`) in the HTML `<meta name="description">` tag. Once the GitHub Pages workflow re-fires (any future push will trigger it; the next manual push will do), Google's crawler picks up the new meta in the next indexing cycle.

You can also (optional) add a Twitter card and Open Graph block to `mkdocs.yml` `extra:` for prettier social-share previews — let me know if you want it.

---

## 4. Single-tweet / Discord announcement template

For an Anthropic Discord `#showcase` post or a single X / Threads post once the *Digital Creativity* paper is accepted:

```text
🎨 Releasing art-project, a Claude Code plugin for the *pre-studio articulation phase* of practice-based artistic research.

Not an ideation engine. The plugin scaffolds the propositional work AROUND ideation:
- /art-project:socratic — surface impulse before a work exists
- /art-project:provoke — tradition-tagged provocations w/ Authentic Practice Boundaries
- /art-project:lineage — extend artist-supplied precedents (bias header mandatory)
- /art-project:brief — 10-field Concept Brief, stay-rough default
- /art-project:rehearsal — 4-persona stress test, formative not decisional
- /art-project:ideate — long-running project file across weeks

EN/KO wiki: https://apesuite.org/plugins/
Install: /plugin marketplace add joonhyungbae/art-project
Paper (in submission): *Digital Creativity* (Routledge / T&F).
License: CC-BY-NC 4.0.

For: early-career artists, second-language writers, PaR-doctoral candidates, grant-deadline-pressured collectives.
NOT for: artists whose articulation is already fluent; oral, ritual, improvisational traditions where the propositional artefact actively damages the practice.
```

(Korean version available on request — say the word.)

---

## 5. Academic-venue announcement (if/when DC paper is accepted)

After acceptance, the paper's cover letter and author-bio note are the most impactful discoverability move you can make. The paper's *Digital Creativity* readership overlaps exactly with the plugin's target user population. Two passive moves:

- Cover-letter pointer to the wiki URL alongside the reproducibility-package URL.
- Author-bio note mentioning the plugin: *"…and is the maintainer of `art-project`, the cognitive-scaffold plugin the paper documents (https://apesuite.org/plugins/)."*

Both are zero-effort once the paper is in author-proofs.

---

## What this document is and is not

**Is.** A copy-paste checklist of discoverability moves that respect the plugin's actual character (CC-BY-NC, decentralised marketplace model, scholarly basis). All material in here is ready to apply without further drafting.

**Is not.** A growth-hack playbook. The plugin's natural audience is specific (artists where propositional articulation is a bottleneck); the moves above target that audience cleanly. Broader claims would misrepresent the user-asymmetry scope statement.
