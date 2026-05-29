# Rehearsal mode

> Slash command: `/art-project:rehearsal` — for stress-testing a draft brief before submission.

## What it does

Runs a **self-critique rehearsal** in which the brief is questioned from four named personas: **Curator**, **Practitioner-peer**, **Theorist**, and **Devil's Advocate**. The output is a transcript: each persona's questions, the artist's responses (or stuck points), and a summary of where the brief held and where it bent.

The mode is **formative-not-decisional**: it exists so the artist can practice articulating their work under questioning *before* facing real curators, peers, or critics. It does not substitute for real critique.

## When to use

- You have a draft Concept Brief from [`brief`](brief.md) mode.
- A submission, studio visit, or peer review is coming.
- You want to find weak articulation points before someone else does.
- Trigger phrases: "stress-test this", "rehearse for curatorial feedback", "tear it apart in safety".

## Mandatory disclaimer header

Every rehearsal transcript opens with:

```text
REHEARSAL DISCLAIMER
─────────────────────────────────────────────────────
This is formative practice, not decisional review. The
personas below are simulated; their questions do not
substitute for real curatorial, peer, or critical
feedback. Real critique is constituted by relational
history the simulation does not have.

Use this rehearsal to practice articulating your work
under questioning. Do not use it as evidence that the
brief is "ready" or "not ready" — that judgement
requires real interlocutors.
─────────────────────────────────────────────────────
```

The disclaimer is not optional.

## Architectural friction (v0.1: honour-system)

The plugin has no session-history mechanism in v0.1, so the friction works as a *prompted self-report*. Before generating the rehearsal output, the plugin asks the artist: *"Has this concept been rehearsed in the last 14 days? If so, how many times?"* If the answer is **two or more**, the plugin issues this warning:

```text
FRICTION WARNING
─────────────────────────────────────────────────────
You have rehearsed this concept 2 times in the last 14
days. Further rehearsal risks simulation-pedagogy harm
(Schön 1983): artists who rehearse repeatedly on the
simulation may train themselves to defend against safe
critique, which is structurally different from the
critique they will actually face.

Consider: (a) taking the brief to a real interlocutor;
(b) returning to socratic / provoke with the questions
that surfaced in rehearsal; (c) sitting with the brief
without further rehearsal.

Proceed anyway? [y/N]
─────────────────────────────────────────────────────
```

**v0.1 honest limitation.** This warning fires only when the artist self-reports rehearsal history accurately. The plugin cannot detect rehearsal frequency on its own; that mechanism is v0.2 work. If the artist forgets or under-reports, the warning does not fire. The friction is therefore a *normative discipline* the user opts into, not a hard architectural gate.

## Persona-collapse detector

If during the rehearsal, two or more personas converge to the same line of questioning, the plugin flags a **persona collapse**: the simulation is failing to maintain distinct perspectives, and the rehearsal is no longer informative. The artist is invited to end the session.

## The four personas

- **Curator** — asks about the work's relationship to a programme, a venue, a public. Cares about coherence with curatorial vocabulary and institutional fit.
- **Practitioner-peer** — asks about the studio decisions the brief implies. Cares about materials, time, what the work demands of its maker.
- **Theorist** — asks about the work's theoretical anchors and what the work claims to know. Cares about epistemological coherence.
- **Devil's Advocate** — asks the question the artist most fears being asked. Cares about productive discomfort.

## IRON rules

- **Formative-not-decisional** — the disclaimer header is mandatory; the rehearsal output is never framed as evaluation.
- **Architectural friction** — the 2/14 friction warning fires automatically.
- **Persona-collapse detector** — the plugin self-monitors for persona convergence and flags it.

## What not to do

- **Don't run `rehearsal` without a Concept Brief.** There is nothing to stress-test.
- **Don't treat the rehearsal as feedback.** Real feedback comes from real interlocutors with relational history.
- **Don't use rehearsal to "fix" the brief in the moment.** Use it to find weak points; return to the relevant mode to address them.

## Where to go next

- If the rehearsal surfaces a weak field, return to `socratic` / `provoke` / `lineage` for that field.
- If the brief held, the next step is real critique (studio visit, peer reading, submission).
- If you find yourself wanting to re-rehearse the same concept, the friction warning is a real signal — sit with it.

## See also

- [Measured harms](../philosophy/measured-harms.md) — the simulation-pedagogy harm class.
- [Brief mode](brief.md) — what you should have before entering rehearsal.
