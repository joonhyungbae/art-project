# Brief mode

> Slash command: `/art-project:brief` — for when you have enough material for a proposition document.

## What it does

Produces a **10-field Concept Brief** that the artist can take to a grant application, residency proposal, doctoral exposition, or collaborator briefing. The mode operates with a **stay-rough default**: the artist's voice is preserved (not smoothed into AI register), and empty fields are reported as gaps rather than filled with plausible-sounding text.

See [Concept Brief schema](../reference/concept-brief.md) for the full field-by-field specification.

## When to use

- You've been through `socratic` / `provoke` / `lineage` and have substantial material.
- A submission deadline forces you to produce a proposition document.
- You want to make your epistemological commitments visible (Frayling type, lineage anchor, disconfirmation condition) before they get smuggled into prose.
- Trigger phrases: "draft a concept brief", "write up what I have so far", "one-pager for [grant / collaborator / self]".

## The 10 fields

1. **Working title** — placeholder is acceptable.
2. **Provocation** (Borgdorff sense) — the not-yet-knowing the work pursues.
3. **Proposition** — the claim the work makes.
4. **Anti-proposition** (Sullivan dialectical sense) — what the work argues against.
5. **Disconfirmation condition** — what would falsify the work, in studio terms.
6. **Intended encounter** (Viewpoints sense) — how the work means to be met.
7. **Lineage anchor** — the precedent the work positions against (from `lineage` mode).
8. **Materials and scale** — the material commitment, including size and duration.
9. **Risk and refusal** — what the work risks; what it refuses to do or be.
10. **Frayling-type declaration** — research *into* / *through* / *for* art.

## IRON rules

- **Stay-rough default** — the artist's voice is preserved verbatim in any field that came from prior modes. The plugin does not smooth fragments into prose.
- **Gaps reported as gaps** — if a field has no material, the plugin marks it `[gap, not in input]` rather than fabricating content. This is the **no-fabrication** discipline.
- **`--polish` is opt-in only** — if you want the brief smoothed for submission, you must explicitly request it. The default is rough.

## Frayling-type declaration

This is the field most artists skip. The plugin requires you to make the declaration explicit: is your project research *into* art (historical / theoretical inquiry whose object is art), research *through* art (artistic practice as means of generating knowledge), or research *for* art (inquiry that supports the making, with the artwork itself as the locus of knowledge)?

Frayling himself flagged the third category as the hardest to articulate. The field exists to surface the difficulty rather than paper over it. See [Frayling typology](../philosophy/frayling-typology.md).

## What not to do

- **Don't run `brief` on insufficient material.** If most fields will be `[gap]`, go back to `socratic` or `provoke` first.
- **Don't ask the plugin to "fill in the gaps."** Gap-acknowledgement is the rule. Polish (with `--polish`) does not fill gaps; it smooths existing material.
- **Don't treat the brief as final.** It is a snapshot at a moment in your thinking; the next session may produce a different brief.

## Output example (abbreviated)

```text
CONCEPT BRIEF — [working title]

1. Working title: "Inscription / counter-inscription"

2. Provocation:
   What the artist wrote and what was written on the artist —
   the back of a photograph; the family record that was not
   the family's. [Borgdorff: not-yet-knowing.]

3. Proposition:
   [stay-rough from session 4 socratic]
   the work is about marks that don't claim authorship

4. Anti-proposition:
   [gap, not in input]

5. Disconfirmation condition:
   the work fails if the viewer reads it as a memorial.

6. Intended encounter:
   [gap, not in input]

7. Lineage anchor:
   From Lineage Map: opposition to On Kawara's date paintings
   (Kawara claims authorship through ritual; this work refuses
   the claim). Kin: [the artist's lineage candidate, name held
   for review].

8. Materials and scale:
   [stay-rough from session 2 socratic]
   photographs, the size of a hand. number unknown yet.

9. Risk and refusal:
   Risk: the work reads as nostalgia.
   Refusal: not a memorial; not a family history piece.

10. Frayling-type declaration:
    Research-FOR art (a piece in support of the making, with
    the work as the locus of knowledge). [Artist must confirm.]
```

## Where to go next

- Sit with the brief for a day or more before submitting.
- For stress-testing before submission, switch to [`rehearsal`](rehearsal.md).
- If gaps need filling, return to `socratic` / `provoke` / `lineage` for the relevant field.

## See also

- [Concept Brief schema](../reference/concept-brief.md) — full field-by-field specification.
- [Frayling typology](../philosophy/frayling-typology.md) — what the declaration field commits the artist to.
