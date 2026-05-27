# Tradition tags

The plugin grounds its provocations, lineage extensions, and authentic-practice boundaries in a corpus of prior ideation methodologies. Each entry is a **tradition tag**, structured by a fixed 6-field schema.

## The six fields per entry

1. **Author + year** — the bibliographic anchor that allows the artist to read the primary source.
2. **Core gesture** — the methodology's central move, in one sentence.
3. **Ideation mechanism** — what the methodology activates (chance, constraint, instruction, embodied protocol, …).
4. **Authentic Practice Boundary** — what the methodology requires that the AI does not simulate. See [Authentic Practice Boundaries](authentic-practice-boundaries.md).
5. **Contested in** — counter-positions or critiques the methodology has received.
6. **Skill-hook** — which plugin modes (socratic, provoke, lineage, brief, rehearsal, full) consume the entry.

## The corpus (approximately 25 entries)

Spread across five categories:

- **General creativity and cognition theory** — Geneplore (Finke / Ward / Smith 1992), combinational / exploratory / transformational creativity (Boden 2004), SCAMPER (Eberle 1971).
- **Design and planning methodology** — Shneiderman creativity-support principles (2007), reflective practice (Schön 1983), studio-as-laboratory (Edmonds et al. 2005).
- **Art-specific methodologies** — Oblique Strategies (Eno & Schmidt 1975), instruction art (LeWitt 1967), chance operations (Cage 1961), Viewpoints (Bogart & Landau 2005).
- **Media-art and technology** — embodied epistemology (Penny 2017), speculative design (Dunne & Raby 2013).
- **Non-anglophone context** — Paik *Exposition of music* (1963), cosmotechnics (Hui 2016), Korean-context PaR (Lee & Lee 2024).

The non-anglophone category is **deliberately incomplete** — it is the [`measured harms`](../philosophy/measured-harms.md) class that is currently under-developed. Korean-context candidates ship in v0.1 but the wider East-Asian and Global-South coverage is targeted for v0.3+.

## What a tradition tag is and is not

- A tradition tag is a **prompt-grounding and style-affinity claim**: it says "this entry was loaded into the prompt; the output aims to operate within the style affinity of this tradition."
- A tradition tag is **not a causal-attribution claim**. The plugin does not claim the LLM's generation mechanism is causally traceable to the named tradition; the mechanism is opaque.

This distinction is load-bearing. The label `tradition tag` is deliberate: the plugin refuses to overclaim and rests the contribution on the grounding work actually done (prompt conditioning, boundary declaration, bibliographic anchoring).

## How tags appear in plugin output

- **In `provoke`**: every provocation card carries one or more tags. The artist can see exactly which tradition the provocation was conditioned on.
- **In `lineage`**: lineage map entries are tagged with their methodological tradition where relevant.
- **In `brief`**: the brief's Provocation, Proposition, Anti-proposition, Lineage anchor, and Frayling-type-declaration fields carry tags showing which traditions ground each cell.

## Adding new tags

The corpus is open. To propose a new tradition tag, submit a PR to the [`shared/references/art_ideation_methodology.md`](https://github.com/joonhyungbae/art-project/blob/main/shared/references/art_ideation_methodology.md) file with the 6-field structure populated. See [Contributing](../contributing.md).

## See also

- [Authentic Practice Boundaries](authentic-practice-boundaries.md) — the per-method declarations.
- [Provoke mode](../modes/provoke.md) — where tradition tags get the heaviest use.
- [Lineage mode](../modes/lineage.md) — where tradition tags shape position attribution.
