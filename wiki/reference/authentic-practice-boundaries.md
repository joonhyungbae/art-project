# Authentic Practice Boundaries

For every tradition tag in the plugin's corpus, an **Authentic Practice Boundary** declares what the cited methodology requires that the AI **does not simulate**. The boundary is not a disclaimer added after the fact; it is part of the prompt structure that conditions the output.

## Why the boundaries exist

The practising-artist critique: algorithmic Oblique Strategies, simulated Cage, and AI-authored LeWitt instructions all *violate the constitutive features* of the methods they cite. A method's authenticity is not its rule but its embedded practice — the bodily, temporal, social, or material conditions the rule requires.

The boundary discipline refuses the simulacrum move. The plugin can invoke a tradition only by *also* declaring what it cannot do within that tradition.

## Worked boundary examples

### Oblique Strategies (Eno & Schmidt 1975)

> Boundary: The deck's **physical, finite, blindly-drawn character** is irreplaceable. An algorithmic Oblique-style provocation generator is no longer in the tradition the tag invokes, because the deck's constraint is that you cannot pick which card you draw — and the size of the deck is itself a meaningful limit.
>
> What the plugin does: issues an Oblique-style provocation card, then *goes silent* (preserved unhelpfulness). The plugin does not draw "the next" card on demand; the artist chooses to stop.

### Cage chance operations (Cage 1961)

> Boundary: The **artist's time spent performing the chance procedure** is part of the work. The Cage tradition is not about randomness; it is about the artist consenting to a procedure and committing the studio time to its outcomes.
>
> What the plugin does: proposes the chance procedure (which I Ching method, which dice, which playing-card protocol). The artist throws the dice, casts the coins, draws the cards — and lives with what comes.

### LeWitt instruction-based work (LeWitt 1967)

> Boundary: The **artist is the rule-setter**. LeWitt's instructions are not arbitrary; they are the artist's commitment to a system that the artist takes responsibility for.
>
> What the plugin does: prompts the artist to write the instruction. The plugin can ask "what would the rule be?" and offer scaffolding (constraints, examples from LeWitt's own works), but does not author the instruction.

### Viewpoints (Bogart & Landau 2005)

> Boundary: The work is **bodied, ensemble-based, and temporal**. Viewpoints is a physical training of attention, not a vocabulary of categories. The vocabulary (tempo, duration, kinesthetic response, repetition, etc.) is meaningful only because it indexes embodied training.
>
> What the plugin does: asks Viewpoints-derived questions about the intended encounter ("what tempo does the work expect of the viewer?" "what spatial relationship?"). The plugin does not perform Viewpoints work, design choreography, or substitute for an ensemble's rehearsal.

### Barrett & Bolt materiality

> Boundary: The work emerges through **the encounter with material; the medium talks back**. The artist's hand learning the material is what the practice-based research literature locates as the site of knowledge.
>
> What the plugin does: *refuses to substitute for* this commitment. The plugin produces propositional articulation (briefs, lineage maps) that travel into the studio, but the studio encounter is not modelled.

## How boundaries propagate

The Authentic Practice Boundary appears:

- **In every `provoke` card** that invokes a tradition tag.
- **In every `lineage` map entry** where the precedent's methodology is being adapted.
- **In the `brief` mode** Frayling-type declaration field, where the artist's chosen Frayling type triggers a boundary disclosure relevant to that type.
- **As an inline reference** in `rehearsal` mode if a persona references a tradition.

## What the boundaries are not

- **Not a refusal to use the tradition.** The plugin can and does invoke Oblique Strategies, Cage, LeWitt, Viewpoints. The boundary names what cannot be substituted, not what cannot be cited.
- **Not exhaustive.** A boundary names a few constitutive features; it does not claim to capture everything the cited methodology is or requires.
- **Not a guarantee.** The boundary is an architectural commitment; a future implementer could populate the schema dishonestly. The discipline is normative, not technically enforced.

## Adding boundaries for new traditions

When proposing a new tradition tag (see [Contributing](../contributing.md)), the boundary field is mandatory. A tradition tag without a boundary declaration will not be accepted into the corpus.

## See also

- [Tradition tags](tradition-tags.md) — the 6-field schema the boundary lives in.
- [Provoke mode](../modes/provoke.md) — boundaries in their most visible use.
- [Cognitive scaffold](../philosophy/cognitive-scaffold.md) — the position the boundary discipline operationalises.
