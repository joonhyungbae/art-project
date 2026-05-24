---
name: art-brief
description: "Concept Brief with epistemic fields (proposition / anti-proposition / disconfirmation condition / Frayling-type declaration). Stay-rough default — prose stays in the artist's voice. No auto-completion of gaps."
model: sonnet
---

Invoke the `art-ideation` skill in **brief** mode.

Produce a Concept Brief with the v0.2 epistemic schema. The Brief is **not** a marketing one-pager; it is a *proposition document* in the Journal for Artistic Research / Research Catalogue exposition tradition.

**Required fields (in order):**

1. **Working title** — artist's preferred title; provisional is fine.
2. **Provocation** — the research question implicit in the impulse (Borgdorff 2011, 2012, C4). What does the work want to find out? What can only be found out by making it?
3. **Proposition** — the claim the work proposes. What does this work *say*, even if only as a hypothesis the making will test?
4. **Anti-proposition** — what the work *refuses* to assert (Sullivan 2010, C5, dialectical inquiry). The negative space of the proposition.
5. **Condition for disconfirmation** — what reception or failure would falsify the proposition? (Borgdorff's criticisability gate.) This converts the Brief from belief-document to proposition-document.
6. **Intended encounter** (Bogart Viewpoints, C8) — spatial / temporal / kinesthetic relation the work proposes for the audience. Where do they stand? What duration is asked of them? What sensory register?
7. **Lineage anchor** — at most 3 precedent references, with the lineage-mode training-data bias disclosure attached if applicable.
8. **Materials / medium / scale** — concrete enough to be planned, vague enough to permit discovery.
9. **Risk / refusal** (Corita Kent C9; Saltz C10) — what might the work fail at? What does the artist refuse to do for it (even if it would help reception)?
10. **Frayling type declaration** (Frayling 1993, C3) — INTO / THROUGH / FOR. Which kind of research does this work perform?

**IRON RULE — stay-rough default.** Prose stays in the artist's voice. Your job is to *force articulation of each field*, **not** to smooth the prose. Default behavior: ask the artist to dictate the proposition / anti-proposition / disconfirmation / etc. and capture the wording with minimal edit. Preserve grammatical quirks, mid-sentence stops, contradictory clauses. A `--polish` flag exists for ESL or grammar pass, but is **not** the default.

The reason for stay-rough: AI-detectable smoothness is itself a reject signal at real review venues (curators, grant committees, residencies have learned to spot LLM-polished applications). Keeping the artist's voice — including its roughness — is the v0.2 mitigation against ghost-writer-effect harm.

**IRON RULE — no auto-completion of gaps.** If the artist cannot articulate the disconfirmation condition or the anti-proposition, **report the gap** rather than filling it. Format the empty field as:

```
**Condition for disconfirmation:** *[artist did not articulate; gap acknowledged
per Borgdorff criticisability discipline — return to this field before submission]*
```

Plausible-sounding filler in these fields is a failure mode, not a success. Empty + acknowledged > filled + fabricated.

See [`art-ideation/SKILL.md`](../art-ideation/SKILL.md) for the full mode specification.
