# Provoke mode

> Slash command: `/art-provoke` — for when you have a partial concept and feel stuck.

## What it does

Produces a **tradition-tagged provocation set** of 8–20 cards. Each card is tagged with a methodology (Eno/Schmidt Oblique Strategies, Cage chance operations, LeWitt instruction-art, Viewpoints, etc.), carries an explicit **Authentic Practice Boundary** naming what that methodology requires that the AI does not simulate, and ships with a **counter-formulation** so the provocation does not collapse into a single reading.

After issuing the cards, the system goes silent. The plugin does not interpret the cards on the artist's behalf. This is the **preserved unhelpfulness** rule.

## When to use

- You have a partial concept and feel stuck.
- You want to be displaced from a familiar pattern, not refined within it.
- Trigger phrases: "give me provocations", "what if", "throw constraints at me" / 막혔어.

## Output structure

Each card has:

1. **The provocation** (short, declarative, often imperative)
2. **Tradition tag** (which methodology grounds the provocation)
3. **Authentic Practice Boundary** (what the cited methodology requires that the AI cannot perform)
4. **Counter-formulation** (the opposite or adjacent move, deliberately listed so the provocation cannot be read as instruction)

## IRON rules

- **Tension-over-ranking** — every provocation ships with a counter-formulation; the set is not ranked.
- **Preserved unhelpfulness** — after issuing cards, the plugin goes silent. It does not interpret which card you should follow, what they mean for your work, or how to combine them.
- **No simulacrum of methodology** — for any cited methodology, the Authentic Practice Boundary names what cannot be substituted (e.g. the physical blind-drawn character of the Oblique Strategies deck; the artist's time performing a Cage chance operation).

## What not to do

- **Don't ask the plugin to pick a card for you.** It will refuse. Picking is your work.
- **Don't ask the plugin to "explain what this means for my project."** It will refuse. The provocation is meant to displace, not to instruct.
- **Don't run `provoke` if you're still in `socratic` territory** (i.e. no concept yet). Provocations against an empty space do not displace; they invent.

## Example output (abbreviated)

```text
Card 3 of 12
─────────────────────────────────────────────────────
PROVOCATION:    What if the documentation IS the work?

TRADITION TAG:  LeWitt instruction-based art (Paragraphs
                on Conceptual Art, 1967)

AUTHENTIC PRACTICE BOUNDARY:
                LeWitt requires that the artist write the
                instruction. The plugin proposes the
                provocation but does not author the
                instruction for you.

COUNTER-FORMULATION:
                Or: what if there is no documentation,
                only the trace?
─────────────────────────────────────────────────────

[12 cards delivered. System silent. Sit with them.]
```

## Where to go next

After provocations:

- Sit with the cards for hours or days; do not jump to next mode immediately.
- If the cards surface a candidate lineage, switch to [`lineage`](lineage.md).
- If a card produces enough material for a brief, switch to [`brief`](brief.md).
- If you need more provocations on a specific tag, re-enter `provoke` with that tag named.

## See also

- [Authentic Practice Boundaries](../reference/authentic-practice-boundaries.md) — the per-method declarations.
- [Tradition tags](../reference/tradition-tags.md) — the corpus the provocations draw from.
