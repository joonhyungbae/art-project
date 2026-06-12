# Art-Project for Claude Code

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-D77757)](https://docs.claude.com/claude-code)
[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](https://github.com/joonhyungbae/art-project/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Wiki](https://img.shields.io/badge/wiki-EN%20%2F%20KO-blue)](https://apesuite.org/plugins/#/art-project/en/index)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

> [한국어 README](README.ko-KR.md) · 📖 Wiki: [English](https://apesuite.org/plugins/#/art-project/en/index) / [한국어](https://apesuite.org/plugins/#/art-project/ko/index)

A Claude Code plugin: a **pre-studio articulation scaffold** for practice-based artistic research. **Not an ideation engine.** The plugin accepts the Penny / Ingold / Borgdorff critique that artistic ideation is non-linguistic, material, and inseparable from making — and scopes itself to the propositional articulation work *around* ideation: grant applications, doctoral expositions, residency proposals, collaborator briefings. The actual ideation happens in your studio, with material.

---

## Companion plugin

**art-project** and **art-paper** are two sibling Claude Code plugins for practice-based artistic research, by the same maintainer, covering opposite ends of a project's life:

| | Plugin | Phase | What it scaffolds |
|---|---|---|---|
| **← you are here** | **[art-project](https://github.com/joonhyungbae/art-project)** | *before the work* | Pre-studio articulation — impulse surfacing, tradition-tagged provocations, lineage positioning, a Concept Brief, self-critique rehearsal |
| | **[art-paper](https://github.com/joonhyungbae/art-paper)** | *after the work* | Practice-based art-paper authoring — inquiry, drafting, ACM citation, a SIGGRAPH Asia jury, acmart LaTeX → PDF |

The arc: **art-project** articulate the concept → *make the work in your studio* → **art-paper** write the juried paper. Each stands alone; together they span concept-to-publication.

> Lineage: both descend from [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) (Cheng-I Wu). art-paper forked the suite into the art-paper genre; art-project then pivoted from art-paper into the pre-studio phase.

---

## Install (30 seconds)

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

That gives you one skill (`art-ideation`) with six modes, accessed via `/art-project:*` slash commands. Outputs are Markdown; no toolchain required.

> **Plan note.** Three of the six commands (`socratic`, `rehearsal`, `ideate`) request **Claude Opus** because they carry the load-bearing IRON RULES (intent classification, persona stability, multi-session synthesis). The other three (`provoke`, `lineage`, `brief`) default to Claude Sonnet. If your Claude plan does not include Opus access, `socratic` / `rehearsal` / `ideate` fall through to your plan's default model — most rules still apply, but persona and intent-classification discipline is weaker. The wiki has a model-tier note.

**Try one of:**

- `/art-project:socratic` — *"I have a vague pull toward something."*
- `/art-project:provoke` — *"I'm stuck. Throw constraints at me."*
- Natural language: *"Guide me through a new project."* The plugin auto-routes by intent and announces the routing transparently.

**👉 [Wiki — apesuite.org/plugins/#/art-project](https://apesuite.org/plugins/#/art-project/en/index)** and [QUICKSTART.md](QUICKSTART.md) — full walkthroughs.

---

## What it does

One skill (`art-ideation`), six modes.

| Slash command | What it produces | Load-bearing rule |
|---|---|---|
| `/art-project:socratic` | Concept Pull Map (impulse / fragments / constraints / refusals / **residue**) | No auto-convergence under exploratory intent — HARD-bound by per-3-turn intent classification |
| `/art-project:provoke` | 8–20 tradition-tagged provocations with an [Authentic Practice Boundary](https://apesuite.org/plugins/#/art-project/en/reference/authentic-practice-boundaries) per method | **Preserved unhelpfulness** — silence after delivery, no auto-interpretation, no ranking |
| `/art-project:lineage` | Lineage Map extending **artist-supplied** initial candidates (kin / opposition / blind-spot / unexpected-neighbor) | Mandatory training-data bias header; Korean / East-Asian default routing on KO sessions; honest self-description as *retrieval, not ideation* |
| `/art-project:brief` | 10-field Concept Brief (proposition / anti-proposition / **disconfirmation condition** / **Frayling-type declaration** / …) | Stay-rough default — voice preserved; **no auto-completion** of gaps |
| `/art-project:rehearsal` | 4-persona self-critique (Curator + Practitioner-peer + Theorist + Devil's Advocate) | Formative not decisional; mandatory disclaimer; consultative friction backed by `~/.art-project/rehearsal-log.jsonl` |
| `/art-project:ideate` | Long-running project file at `~/.art-project/projects/<codename>/project.md`, across weeks (Smith & Dean iterative cyclic web) | One mode per session; no single-session pipelining |

Each mode wires to a 25+ entry methodology reference layer (Frayling, Borgdorff, Sullivan, Smith & Dean, Eno & Schmidt, LeWitt, Cage, Bogart, Bauhaus, Manovich, Penny, Dunne & Raby, plus Korean / East-Asian and HCI prior-art). Full reference at the [wiki](https://apesuite.org/plugins/#/art-project/en/reference/tradition-tags).

---

## Design rationale

**Cognitive-scaffold position** (Clark & Chalmers 1998; Malafouris 2013; Penny 2017). Neither inert tool nor co-author. Five architectural commitments (generation–evaluation separation; tension-over-ranking; lineage-with-opposition; formative-not-decisional rehearsal; tradition-tag-with-Authentic-Practice-Boundary) operationalise specific practice-based research positions; tradition-tag attribution comes with explicit **Authentic Practice Boundaries** naming what each cited method requires that the plugin does *not* simulate.

> *Example.* For Cage chance operations, the plugin proposes the procedure (which I Ching method, which dice protocol); **the artist throws the dice**. The time the artist spends performing the procedure is part of the work. The plugin does not execute the chance operation, because doing so would re-route the constitutive feature of the method.

Detail: [cognitive scaffold](https://apesuite.org/plugins/#/art-project/en/philosophy/cognitive-scaffold), [Frayling typology](https://apesuite.org/plugins/#/art-project/en/philosophy/frayling-typology), [Authentic Practice Boundaries](https://apesuite.org/plugins/#/art-project/en/reference/authentic-practice-boundaries), [measured harms](https://apesuite.org/plugins/#/art-project/en/philosophy/measured-harms), and the [v0.2 synthesis spec](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).

---

## Who it's for

For artists where **propositional articulation is a bottleneck**:

- early-career artists who have not yet absorbed artist-statement conventions
- artists writing across languages (e.g. a Korean-first artist writing English grant applications)
- doctoral candidates preparing expositions for venues such as the *Journal for Artistic Research*
- artists under grant or residency deadlines
- collectives needing a shared articulation document

**Not** for artists whose articulation is already fluent (use Claude directly), nor for traditions where articulation is constitutively unwanted (improvisational, ritual, oral). Naming the boundary is part of the design — see [philosophy / measured harms §6](https://apesuite.org/plugins/#/art-project/en/philosophy/measured-harms).

Bilingual: English default, Korean / East-Asian routing on Korean sessions. **Honest disclosure:** the East-Asian section of the reference layer is the most under-developed (3 entries as of v0.1.0; expansion pending library work). On Korean sessions, `lineage` surfaces a training-data bias header and may still fall back to anglophone Korean-studies sources rather than Korean-language primary sources. Treat the Korean experience as *seeded* rather than *fully parallel* to the English one until v0.2 reference expansion.

---

## Companion paper

A reconstruction-benchmark compliance audit (15 published case studies, **zero ex-nihilo fabrications across 90 generative-layer cells** — verified against pre-registered, hash-frozen criteria; full per-case data will ship with the paper's supplementary materials on acceptance) is in submission to ***Digital Creativity*** (Routledge / Taylor & Francis, AHCI). The working draft is held locally during peer review; the reproducibility package (input packs, gold briefs, pre-registration hash, per-case results) is released through the paper's supplementary-materials channel after acceptance.

The plugin is the worked example; the contribution is the framework it instantiates. User studies with practising artists are sequenced as the next paper. The same methodology audit is the [companion paper](https://github.com/joonhyungbae/art-paper#companion-paper) shared with **art-paper**.

---

## License & attribution

[CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Share + adapt + attribute, non-commercial use only.

```text
art-project (Version 0.1.0).
Pivoted from art-paper v0.1.0; ultimately forked from
Academic Research Skills (Cheng-I Wu) v3.9.4.2.
https://github.com/joonhyungbae/art-project
Companion paper: docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md
```

---

## Provenance

**Maintainer.** Joon-Hyung Bae (`joonhyungbae` on GitHub; `jh.bae@kaist.ac.kr`). The v0.2 design synthesis (Frayling layered hybrid self-positioning, cognitive-scaffold framing, tradition-tag-with-Authentic-Practice-Boundary architecture, six-mode reshape, measured-harm disclosure) is the maintainer's work.

**Lineage.** [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2 ([Cheng-I Wu](https://github.com/Imbad0202)) → art-paper v0.1.0 → art-project v0.1.0. The genre-neutral safety machinery (L3 citation-faithfulness gate, Concession Threshold Protocol, intent detection, routing discipline) is inherited unchanged from ARS. The maintainer keeps a local pristine ARS clone under `ref/academic-research-skills/` for diffing; that directory is gitignored and not part of the published plugin.

**Four-agent design critique** (2026-05-24) — the v0.2 design was synthesised from four specialist agent critiques: artistic-research methodologist (PaR / Frayling / Borgdorff / Sullivan), HCI / AI-creativity researcher (Shneiderman / Cherry-Latulipe / Davis / Wordcraft-Sparks), practising-artist studio-side review, Devil's Advocate (Penny / Ingold / Borgdorff / Wittgenstein / Illich attacks on the premise).

---

## Repo layout

```text
art-project/
├── art-ideation/
│   ├── SKILL.md                       # the single skill spec
│   ├── agents/                        # 4 v0.2-aligned + 4 archived under deprecated/
│   ├── references/ + templates/       # in-skill references and (deprecated) templates
│   └── examples/                      # in-skill examples (v0.1-deprecated; see wiki)
├── commands/                          # 6 slash-command files (bare names: brief, ideate, …)
├── shared/references/                 # methodology reference + glossaries + routing
├── docs/                              # design spec / audits / verification / ops
├── ref/academic-research-skills/      # pristine ARS reference (gitignored; local-only)
├── hooks/ + scripts/                  # SessionStart hook + announce script
├── .claude-plugin/{plugin,marketplace}.json
└── README{,.ko-KR}.md, LICENSE, NOTICE, SECURITY, CHANGELOG, MODE_REGISTRY,
    POSITIONING, QUICKSTART
```

---

## Changelog (recent)

See [CHANGELOG.md](CHANGELOG.md) for full history.

- **v0.1.0** (2026-05-24, pivot from art-paper) — drops paper-authoring scope; pivots `art-inquiry` → `art-ideation` with six modes; rebuilds the reference layer (positionality + tensions + Authentic Practice Boundaries + restored critical edge on Penny / Borgdorff); adds HCI prior-art section; ships measured-harm disclosure.
- **v0.2 internal milestones** (2026-05-30) — runtime-readiness honesty sweep; intent-detection HARD-bound in `socratic`; Dialogue Health Indicator demoted to Devil's-Advocate sub-heuristic inside `rehearsal`; rehearsal friction backed by real `~/.art-project/rehearsal-log.jsonl` log (was honour-system); `ideate` full-mode persistence at `~/.art-project/projects/<codename>/project.md` (was artist-managed); v0.1-drift agents archived under `art-ideation/agents/deprecated/`. Documented in [`docs/V0.2-DESIGN-DECISIONS.md`](docs/V0.2-DESIGN-DECISIONS.md) and verified in [`docs/V0.2-VERIFICATION.md`](docs/V0.2-VERIFICATION.md).
- **Wiki canonical → apesuite** (2026-06-12) — the user wiki now lives at [apesuite.org/plugins/](https://apesuite.org/plugins/); the MkDocs mirror previously deployed to GitHub Pages has been removed.
