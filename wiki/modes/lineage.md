# Lineage mode

> Slash command: `/art-lineage` — for when you have candidate precedents and want to extend them.

## What it does

Produces a **Lineage Map** of 5–15 precedent artists / works / texts, each tagged with one of four positions relative to your work: **kin** (close affinity), **opposition** (productive contrast), **blind-spot** (something the kin tradition does not see), or **unexpected-neighbor** (precedent the artist would not have surfaced themselves).

The map ships with a **mandatory training-data bias header** disclosing which sub-domains the LLM substrate over-represents and which it under-represents.

## When to use

- You can name 2–3 candidate precedents and want the map extended.
- You want to position your work in a tradition before drafting the brief.
- Trigger phrases: "who else has done this", "where am I in the field", "position my work".

## Hard requirement: artist-supplied initial candidates

`lineage` mode **will not generate lineage from impulse alone**. You must supply at least 2 candidate precedents (artists, works, texts) before the plugin will extend. The reason: lineage hallucination on long-tail sub-domains is the most common failure mode of LLM lineage tools, and artist-supplied anchors materially constrain the failure space.

If you have no candidates yet, switch to [`socratic`](socratic.md) or [`provoke`](provoke.md) first.

## Training-data bias header (mandatory)

Every Lineage Map ships with a disclosure:

```text
TRAINING-DATA BIAS DISCLOSURE
─────────────────────────────────────────────────────
LLM substrate over-represents: anglophone media-art
venues (Rhizome, e-flux, Frieze, Artforum); 1990s-2010s
US/UK/DE generative-art scene; canonised conceptual art
(LeWitt, Weiner, On Kawara).

Under-represented: non-anglophone PaR doctoral expositions;
Korean / East-Asian media-art scene (esp. post-2010);
oral, ritual, and improvisational traditions; collective
and anonymous practice.

This map should be read with that bias in mind. Add
non-anglophone candidates explicitly if your work draws
on those traditions; the plugin will route accordingly.
─────────────────────────────────────────────────────
```

## Position tags

- **Kin** — precedent shares method, material, or stake. Use to position lineage continuity.
- **Opposition** — precedent works against your stake; the contrast clarifies what your work *is*.
- **Blind-spot** — precedent's tradition does not see something your work does. Names what your work brings.
- **Unexpected-neighbor** — precedent the artist would not have surfaced; flagged for the artist to evaluate, not asserted as relevant.

## Korean / East-Asian default routing

When the session signals (input language, named candidates, explicit declaration) suggest Korean or East-Asian context, the plugin prioritises non-anglophone sources in the Lineage Map. The bias header still ships, but the corpus weighting shifts.

## Opt-out

If you want a Lineage Map *without* the training-data bias header (e.g. for a sub-domain where the bias is irrelevant), use `--no-lineage` flag in your request. The flag is always available.

## What not to do

- **Don't request lineage extension without supplying initial candidates.** The plugin will ask for candidates first.
- **Don't treat the Lineage Map as ranked.** The four position tags are categorical, not ordered.
- **Don't treat unexpected-neighbor entries as endorsements.** They are flagged for your evaluation.

## Where to go next

- If the Lineage Map produces a strong sense of position, switch to [`brief`](brief.md) and use the lineage as the lineage-anchor field.
- If a kin entry suggests a methodology you want to interrogate, switch to [`provoke`](provoke.md) with that tradition tag.

## See also

- [Tradition tags](../reference/tradition-tags.md) — the corpus of methodologies the plugin draws from.
- [Measured harms](../philosophy/measured-harms.md) — why the bias header is mandatory.
