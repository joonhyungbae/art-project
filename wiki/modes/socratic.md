# Socratic mode

> Slash command: `/art-project:socratic` — for when there is no concept yet, only a pull.

## What it does

Pre-reflective surfacing through Socratic dialogue. Produces a **Concept Pull Map**: named impulses, fragments, constraints, refusals, and *residue* (the part of the pull that didn't fit any other category).

## When to use

- You feel pulled toward something but cannot say what.
- You can describe an encounter (an image, a phrase, a recent reading) but cannot say why it matters to you.
- A grant deadline is coming and the only honest answer to "what is this work about" is "I'm not sure yet."
- Trigger phrases: "guide me", "I don't know what I'm doing yet", "help me find what the work wants to be" / 도와줘, 잘 모르겠어.

## What the dialogue looks like

The plugin opens with a stance question (often something like "What did you notice that you couldn't immediately explain?"), then follows your answer with progressively finer questions. Questions are deliberately *unfinished* — they leave the answer space open rather than constraining it. After 5–10 rounds, the plugin produces the Concept Pull Map.

## The Concept Pull Map

Five named sections:

- **Impulses** — what you keep being drawn to, even when you don't know why
- **Fragments** — partial materials, phrases, images that are concrete but not yet connected
- **Constraints** — what the work cannot do, who it cannot serve, what register it refuses
- **Refusals** — what you specifically do not want this work to become
- **Residue** — the part of the pull that fits none of the above; explicitly named as remainder rather than discarded

The map is a snapshot of the unfinished thought, not a roadmap.

## IRON rules

- **Stay-rough default** — your voice is preserved verbatim in your answers; the plugin does not smooth your fragments into AI-statement prose.
- **No auto-convergence under exploratory intent** — the plugin will not, at the end of `socratic`, tell you "your concept is X." It will offer the map and ask which fragment you want to follow.
- **Turn-taking** — the plugin does not advance to the next question until you respond.

## What not to do

- Don't write paragraph-length artist-statement-style answers; write fragments. Roughness is data.
- Don't ask the plugin to "summarise where I am" before the map is produced; summaries collapse the pull into a single direction before the work is ready.
- Don't ask for lineage or provocations inside Socratic mode; switch modes explicitly.

## Example session opener

```text
You: /art-project:socratic
Plugin: [Socratic mode active. I'll ask questions designed to surface
        unfinished thought rather than extract finished thought. Stay
        rough — write fragments, not paragraphs. We'll end with a
        Concept Pull Map.]

Plugin: What did you notice recently that you couldn't immediately
        explain — an image, a phrase, an encounter?

You: there was this old photograph my grandmother left, and
     the back of it has handwriting that's not hers

Plugin: [continues with finer questions]
```

## Where to go next

After the Concept Pull Map:

- Stay in `socratic` for another round if still vague.
- Switch to [`provoke`](provoke.md) for tradition-tagged provocations on a stuck fragment.
- Switch to [`lineage`](lineage.md) if you can name initial precedents.

## See also

- [First session](../getting-started/first-session.md)
- [Cognitive scaffold](../philosophy/cognitive-scaffold.md) — why the plugin refuses to interpret on your behalf
