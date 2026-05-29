# First session

A walkthrough of a typical first encounter with the plugin. Use this as a script the first time, then drop the scaffolding.

## Scenario

You have a vague pull toward something — an image, a question, a recent encounter — but no concept yet. You're going to use `socratic` mode to surface what's actually there.

## Step 1 — Enter Socratic mode

In Claude Code:

```text
/art-project:socratic
```

The plugin will introduce itself briefly, then ask you the first Socratic question. Don't try to give a "correct" answer; the questions are designed to surface unfinished thought, not to extract finished thought.

## Step 2 — Stay rough

You'll be tempted to polish what you say. Don't. The plugin's `socratic` mode operates with a **stay-rough default** — it will not smooth your voice into AI register, and it will mark gaps as gaps rather than filling them with plausible-sounding text. The roughness of your answer is data the plugin uses; smoothing it loses information.

If you find yourself writing an artist-statement-sounding paragraph, stop. Write fragments instead. Single words. Half-sentences.

## Step 3 — Read the Concept Pull Map

After several rounds of Socratic questions, the plugin will produce a **Concept Pull Map**: named impulses, fragments, constraints, refusals, and *residue* (the part of the pull that didn't fit any other category). Read it slowly. The map is a snapshot of your unfinished thought, not a roadmap of where to go next.

If the map feels wrong, say so. The plugin will re-ask the questions that produced the misfit.

## Step 4 — Decide where to go next

The Concept Pull Map will usually suggest one of three next moves:

- **Still vague?** Stay in `socratic`. Another round.
- **Stuck on a specific question?** Switch to `provoke` for tradition-tagged provocations.
- **Have candidate precedents in mind?** Switch to `lineage`.

You don't have to decide immediately. You can close the session and come back to the Concept Pull Map later. If you started with `/art-project:ideate` (full project file mode), the map persists across sessions.

## What not to do in the first session

- **Don't ask for a Concept Brief.** Brief mode requires enough material to draft a 10-field document. First-session material is rarely sufficient.
- **Don't ask for lineage extension without artist-supplied candidates.** `lineage` mode requires you to name initial precedents; it will not invent lineage from impulse alone.
- **Don't ask for `rehearsal` critique.** Rehearsal mode is formative-not-decisional, designed for stress-testing a draft brief. Without a brief, there is nothing to stress-test.

## Switching language mid-session

The plugin matches your input language. If you started in Korean and want to switch to English (or vice versa), just write your next message in the target language; the plugin will switch on its next reply.

For artists writing across languages — say, drafting English grant applications while thinking in Korean — you can mix: write the rough material in your native language, then say "write this up in English" when you reach `brief` mode.

## After the first session

Read [Modes overview](../modes/overview.md) to see how the six modes connect. Then either pick a specific mode you need next, or start a `/art-project:ideate` full project file that will track state across multiple sessions.
