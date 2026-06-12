# Quick Start

Get from zero to your first pre-studio articulation session in 3 steps.

art-project is a Claude Code plugin: a **pre-studio articulation scaffold** for practice-based artistic research. **Not** an ideation engine. It scaffolds the propositional work *around* artistic ideation — surfacing the impulse, generating tradition-tagged provocations, mapping (when you supply candidates) precedent lineage, drafting a Concept Brief, and rehearsing self-critique. The actual ideation happens in your studio, with material. See [POSITIONING.md](POSITIONING.md) for the full self-positioning.

## Step 1: Install

Inside Claude Code:

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

That installs one skill (`art-ideation`) plus six `/art-project:*` slash commands (Claude Code namespaces them by plugin name; the command files in `commands/` use bare mode names — `socratic.md`, `provoke.md`, …).

## Step 2: Launch

```bash
claude
```

## Step 3: Start working

You can use either the slash commands (when you know the mode) or a natural-language entry (when you don't — the skill auto-routes and announces the routing transparently).

### Example 1 — Vague pull, no concept yet (`/art-project:socratic`)

```
You: "I have a vague pull toward something about insomnia and surveillance,
      I don't know what the work is yet"
```

Socratic mode surfaces *impulses / fragments / constraints / refusals / residue* through guided dialogue. **IRON RULE:** while you are still exploratory, the skill will not converge or summarize without your explicit request. Don't expect a deliverable in the first session — the mode is designed to keep you exploring.

### Example 2 — Stuck, need provocations (`/art-project:provoke`)

```
You: "I'm a month into LED matrix experiments and I'm stuck on what it's
      about. Throw some constraints at me."
```

Provoke mode issues 8–20 tradition-tagged provocations (Oblique Strategies / SCAMPER / Cage chance / Bolt experimental gesture / Dunne & Raby PPPP / etc.), each with an **Authentic Practice Boundary** naming what the cited method requires that the plugin defers to you (e.g. for Cage: you throw the dice; the plugin does not). After an Oblique-style provocation, the plugin **goes silent**. No auto-interpretation.

### Example 3 — Position against lineage (`/art-project:lineage`)

```
You: "I think my work sits somewhere between Casey Reas and Nam June Paik —
      can you extend that?"
```

Lineage mode requires you to supply initial candidates first. It then extends — kin / opposition / blind-spot / unexpected-neighbor — with a **mandatory training-data bias header** (the plugin's lineage is biased toward anglophone media-art venues). If you start a Korean-language session or the work signals East-Asian context (yi/qi/yeobaek, dansaekhwa, Korean media-art post-Paik), Korean / East-Asian sources are prioritized. You can `--no-lineage` opt out at any point.

### Example 4 — Need a one-pager for a grant deadline (`/art-project:brief`)

```
You: "I have enough material now. Help me draft a concept brief for a residency
      application due next week."
```

Brief mode produces a Concept Brief with epistemic fields: provocation / proposition / **anti-proposition** / **condition for disconfirmation** / intended encounter / lineage anchor / materials / risk-refusal / **Frayling type declaration**.

**IRON RULE — stay-rough default.** The plugin forces articulation of each field but does *not* smooth your prose. Your voice stays in. AI-detectable polish is itself a reject signal at real review venues; `--polish` is opt-in only.

**IRON RULE — no auto-completion.** If you can't articulate the disconfirmation condition or the anti-proposition, the plugin reports the gap rather than filling it with plausible-sounding text.

### Example 5 — Rehearse before facing real reviewers (`/art-project:rehearsal`)

```
You: "I have a draft brief. Walk it through a panel before I submit."
```

Rehearsal mode (renamed from `panel` in v0.2) runs four personas — Curator + Practitioner-peer + Theorist + Devil's Advocate — over your draft Brief. **Mandatory disclaimer** on every output: *this is rehearsal, not critique. Real critique operates differently and will surprise you. Use this to surface your own blind spots before submitting to actual reviewers.* Architectural friction kicks in if you rehearse the same brief more than 2 times in 14 days. Persona-collapse detector flags when all four personas raise the same concern.

### Example 6 — Open a long-running project file (`/art-project:ideate`)

```
You: "I want to start a project file for the insomnia/surveillance work"
```

Full mode opens a **long-running project file** across sessions — days and weeks apart, not a single-session pipeline. Each session does one mode at most; the plugin remembers where you were and lets you re-enter. Smith & Dean (2009) iterative cyclic web in operational form. Resist the urge to compress weeks into one session; the temporal shape matters.

### Natural-language entry (no slash command)

```
You: "I want to think through a new project"
```

The skill auto-routes via intent detection and announces the routing: *"Starting in socratic mode (exploratory intent detected). I'll suggest switching modes when the dialogue suggests it."* Mode transitions are also announced and offered, never silently performed.

## Which mode should I use?

| Your situation | Mode |
|---|---|
| Vague pull, no concept yet | `/art-project:socratic` |
| Stuck, need provocations | `/art-project:provoke` |
| Have candidate lineage, want extension | `/art-project:lineage` |
| Need a proposition document (grant, residency, expo) | `/art-project:brief` |
| Have a brief, want rehearsal before submission | `/art-project:rehearsal` |
| Want to track a long-running project across sessions | `/art-project:ideate` |
| Unclear, prefer natural language | start a session without a slash command |

## When art-project is NOT the right tool

- Your articulation is already fluent. Use Claude directly.
- You want the AI to *make the artwork*. art-project produces language; it does not generate images, sound, or video.
- You want a paper-writing tool. art-project's predecessor is `art-paper`; that scope was dropped in this pivot. The Concept Brief produced by art-project is designed to bridge to a future art-paper sibling distribution.
- You are in a tradition where articulation is constitutively unwanted (improvisational, ritual, oral). The plugin is structurally biased toward propositional articulation; using it on traditions hostile to that bias will frustrate you.

## What's next?

- [Full README](README.md) — features, design rationale, full mode descriptions
- [POSITIONING.md](POSITIONING.md) — Frayling layered hybrid, cognitive scaffold position, measured-harm disclosure
- [MODE_REGISTRY.md](MODE_REGISTRY.md) — 6-mode single source of truth
- [v0.2 synthesis design spec](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md) — the design after four-agent critique
- [Methodology reference](shared/references/art_ideation_methodology.md) — 25+ entries (Boden, Geneplore, Frayling, Borgdorff, Sullivan, Eno, LeWitt, Cage, Bogart, Bauhaus, Manovich, Penny, Dunne & Raby, plus Korean / East-Asian and HCI prior-art)
- [한국어 README](README.ko-KR.md)
