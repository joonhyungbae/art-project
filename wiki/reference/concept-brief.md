# Concept Brief schema

The 10-field schema that [`brief`](../modes/brief.md) mode produces. Each field has explicit epistemic structure; the schema is fixed before any session runs.

## The 10 fields

### 1. Working title

A placeholder name for the work. Acceptable to use `[working title]` or `untitled-N`. The field exists so the brief has a referenceable handle; it is not a commitment.

### 2. Provocation

The *not-yet-knowing* the work pursues, in [Borgdorff 2012](https://doi.org/10.4000/critiquedart.1380)'s sense. Not a question the work answers; a question the work holds open.

**Good provocation**: "What does it mean for an inscription to disclaim its authorship?"
**Bad provocation** (too answerable): "How do photographs decay?"

### 3. Proposition

The claim the work makes. Often the hardest field. Stay-rough default applies — fragments are acceptable.

**Example**: "the work is about marks that don't claim authorship"

### 4. Anti-proposition

What the work argues *against*, in [Sullivan 2010](https://us.sagepub.com/en-us/nam/art-practice-as-research/book230864)'s dialectical sense. The opposing position the work positions itself against.

**Example** (paired with the proposition above): "the work argues against the curatorial assumption that authorship is the locus of value"

### 5. Disconfirmation condition

What would *falsify* the work, in studio terms. Not a logical falsification; an artistic one. What viewing experience or critical reading would mean the work failed at its own stated aims?

**Example**: "the work fails if the viewer reads it as a memorial"

### 6. Intended encounter

How the work means to be met, in the [Viewpoints](https://www.tcg.org/Publications/Books/PublicationDetail/View/the-viewpoints-book) sense (Bogart & Landau 2005). Includes spatial, temporal, bodily, and social dimensions of encounter.

**Example**: "a single viewer at a time, in dim light, with permission to handle the work"

### 7. Lineage anchor

The precedent the work positions against. From a [`lineage`](../modes/lineage.md) Map.

**Example**: "opposition to On Kawara's date paintings (Kawara claims authorship through ritual; this work refuses the claim). Kin: [the artist's lineage candidate]"

### 8. Materials and scale

The material commitment of the work, including size, count, and duration. Fragmentary is fine.

**Example**: "photographs, the size of a hand. number unknown yet. duration of viewing: unbounded"

### 9. Risk and refusal

Partitioned into two sub-claims:

- **Risk**: what the work risks (a reading, an outcome, a mis-reception).
- **Refusal**: what the work specifically does not want to become.

The risk sub-claim is *transferable* (it can be paraphrased without loss). The refusal sub-claim is *generative* (it shapes the work going forward).

**Example**:
- Risk: "the work reads as nostalgia"
- Refusal: "not a memorial; not a family history piece"

### 10. Frayling-type declaration

Research [*into*](../philosophy/frayling-typology.md) / *through* / *for* art. The artist must declare; the plugin will not pick for them.

**Example**: "Research-FOR art (a piece in support of the making, with the work as the locus of knowledge). [Artist must confirm.]"

## Cell partitioning for the reconstruction benchmark

The 10 fields produce **11 cells** per case at scoring time, because field 9 (Risk/refusal) partitions into two sub-claims. Of the 11 cells:

- **6 are generative-layer**: Provocation, Proposition, Anti-proposition, Disconfirmation condition, Refusal sub-claim, Frayling-type declaration. These are cells where the gold reading carries the artist's claim that should not be inferable from documentation alone.
- **5 are transferable or mixed**: Working title, Intended encounter, Lineage anchor, Materials and scale, Risk sub-claim. These are cells where input-pack content can support the gold reading without leakage.

This partition is fixed by the schema, not chosen after reconstruction. See the [paper's §4 audit design](https://github.com/joonhyungbae/art-project/blob/main/art-project_paper/sections/04-evaluation.tex) for the benchmark.

## Stay-rough default

By default, the brief preserves the artist's voice verbatim in any field that came from prior modes. Empty fields are reported as `[gap, not in input]`. The plugin does *not* smooth fragments into AI register, and does *not* fabricate content for empty fields.

To request smoothing for submission, use `/art-project:brief --polish`. The flag is opt-in only.

## See also

- [Brief mode](../modes/brief.md) — how to enter brief mode.
- [Frayling typology](../philosophy/frayling-typology.md) — the declaration field's epistemological commitment.
