# Modes overview

The plugin exposes a single skill (`art-ideation`) with six modes. Each mode operates under three core architectural commitments (the IRON rules) and two subordinate disciplines. The mode design is documented in detail in [MODE_REGISTRY.md](https://github.com/joonhyungbae/art-project/blob/main/MODE_REGISTRY.md) in the repository.

## The six modes

| Mode | Slash command | Output | Oversight tier |
|---|---|---|---|
| [Socratic](socratic.md) | `/art-project:socratic` | Dialogue + Concept Pull Map | Very High |
| [Provoke](provoke.md) | `/art-project:provoke` | Tradition-tagged provocation set (8–20 cards) | High |
| [Lineage](lineage.md) | `/art-project:lineage` | Lineage Map (5–15 precedents tagged kin / opposition / blind-spot) | Medium |
| [Brief](brief.md) | `/art-project:brief` | 10-field Concept Brief | High |
| [Rehearsal](rehearsal.md) | `/art-project:rehearsal` | Self-critique rehearsal transcript (4 personas) | High |
| [Full](full.md) | `/art-project:ideate` | Long-running project file across sessions | Very High |

## Default routing rules

| Situation | Recommended mode |
|---|---|
| No concept yet, vague pull | `socratic` |
| Partial concept, feels stuck | `provoke` |
| Has stated candidate lineage, wants extension | `lineage` |
| Has enough material, needs a proposition document | `brief` |
| Has a draft brief, wants stress-test before submission | `rehearsal` |
| Wants the whole arc across weeks | `full` |
| Ambiguous, no materials | `socratic` (default — guides first) |

## The IRON rules (shared across modes)

1. **Generation–evaluation separation** — no auto-convergence under exploratory intent. The plugin will produce candidates but will not rank them or converge to a single recommendation when the artist is still exploring.
2. **Tension-over-ranking** — provocations ship with counter-formulations; the system goes silent after issuing an Oblique-style card. The plugin refuses to interpret its own provocations on the artist's behalf.
3. **Tradition-tag with authentic-practice boundary** — each cited methodology is paired with an explicit declaration of what the AI does not simulate. See [Authentic Practice Boundaries](../reference/authentic-practice-boundaries.md).

## Two subordinate disciplines

- **Lineage-with-opposition** — `lineage` mode requires artist-supplied initial candidates, ships with a mandatory training-data bias header, and offers `--no-lineage` opt-out.
- **Formative-not-decisional rehearsal** — `rehearsal` mode ships with a disclaimer header, architectural friction (warns after 2 invocations / 14 days on the same concept), and a persona-collapse detector.

## What no mode does

- No mode produces an artwork.
- No mode ranks artists, ideas, or methodologies.
- No mode advances without explicit user trigger (turn-taking IRON rule).
- No mode auto-converges under exploratory intent.

## Naming note: `panel → rehearsal` (v0.2)

In v0.1 the rehearsal mode was called `panel`. The rename commits to the *method-not-evaluation* verdict: `rehearsal` exists so the artist can practice articulating their work under questioning *before* facing real curators, peers, or critics. Real critique is constituted by relational history (the curator's studio visits over years, the peer's stake in the scene) that no simulation has; rehearsal is for the artist's own preparation, not for substitute review.

## Mode transitions

Mode transitions are explicit. When you switch from `socratic` to `provoke`, the plugin will announce the transition rather than silently changing behaviour. This is the **mode transition transparency** rule.

If you start with `/art-project:ideate` (full project file), the file tracks which mode each session was in, so cross-session transitions are auditable.

## See also

- [First session](../getting-started/first-session.md) — walkthrough of starting in `socratic`.
- [Concept Brief schema](../reference/concept-brief.md) — what `brief` mode produces.
- [Cognitive scaffold](../philosophy/cognitive-scaffold.md) — the philosophical position the modes operationalise.
