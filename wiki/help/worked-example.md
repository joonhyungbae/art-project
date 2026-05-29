# Worked example: a project from impulse to brief

A single fictional artist takes a project from a vague pull through five modes over four weeks, using `/art-project:ideate` as the umbrella project file. The example is deliberately concrete: real-feeling fragments, named tradition tags, an Authentic Practice Boundary that fires, a failed lineage candidate, a rehearsal friction warning. Names of artists and works in the lineage map are illustrative.

If you want shorter per-mode examples, see each mode page. This page shows how the modes *connect across studio time*.

## The artist

Soo-jin is a doctoral candidate in Seoul preparing an exposition for the *Journal for Artistic Research*. She works in alternative photography and family-archive material. Her exposition deadline is six weeks out. She has fragments and intuitions, no concept yet.

## Week 1, Session 1 — Socratic

```text
> /art-project:ideate

[Plugin: New project? Continue existing? Reading directory…
  No existing art-project-*.md found. Starting new.
  Project slug?]

> inscription-counter-inscription

[Plugin: Created art-project-inscription-counter-inscription.md
  in /Users/sj/studio/. Choose mode for this session:]

> socratic

[Plugin: Socratic mode active. Stay rough — fragments, not paragraphs.
  Concept Pull Map at the end. First question:

  What did you notice recently that you couldn't immediately
  explain — an image, a phrase, an encounter?]

> there's this old photograph my grandmother left
> the back has handwriting that isn't hers

[Plugin: Whose handwriting do you think it is, and what does that
  uncertainty do to the photograph for you?]

> i can't tell. dealer's? archivist's? it claims something
> about the photo but not as the photo's author
> kind of marks the photo without owning it

[continues for 8 rounds]

[Plugin: Concept Pull Map for session 1:

  IMPULSES
  - marks that don't claim authorship
  - the back of a thing as document

  FRAGMENTS
  - grandmother's photographs (count unknown)
  - handwriting that isn't hers
  - "inscription / counter-inscription"

  CONSTRAINTS
  - viewer can touch (handle the photograph)
  - dim light
  - single viewer at a time

  REFUSALS
  - not a memorial
  - not family history
  - not nostalgia

  RESIDUE
  - the dealer or archivist figure as
    "writer without authorship claim"
  - this feels load-bearing but I can't say why]
```

She closes the session. Sits with the map for two days.

## Week 1, Session 2 — Provoke

Two days later she returns. The Constraints feel stable but the Refusals are nagging — three things she does *not* want the work to be. She is stuck.

```text
> /art-project:ideate

[Plugin: Resuming inscription-counter-inscription.
  Last session: socratic, 2026-04-12.
  Choose mode:]

> provoke

[Plugin: Provoke mode active. 12 tradition-tagged provocation cards,
  each with an Authentic Practice Boundary, each with a
  counter-formulation. System will go silent after delivery.]

> i'm stuck on the refusals
> the work keeps wanting to become a memorial

[Plugin: 12 cards follow.]

  Card 3 of 12
  ─────────────────────────────────────────────
  PROVOCATION:    What if the documentation IS
                  the work?

  TRADITION TAG:  LeWitt instruction-based art
                  (Paragraphs on Conceptual Art,
                  1967)

  AUTHENTIC PRACTICE BOUNDARY:
                  LeWitt requires that the artist
                  write the instruction. The plugin
                  proposes the provocation but does
                  not author the instruction for you.

  COUNTER-FORMULATION:
                  Or: what if there is no
                  documentation, only the trace?
  ─────────────────────────────────────────────

  [11 other cards follow.]

  [System silent.]
```

She reads all 12 cards over several days. Card 3 (LeWitt) and Card 9 (Cage chance operations) keep returning. She decides Card 9 is the one — the chance procedure as a way to *not* memorialise.

## Week 2, Session 3 — Lineage

```text
> /art-project:ideate

> lineage

[Plugin: Lineage mode requires artist-supplied initial candidates.
  Name at least two precedent artists, works, or texts.]

> on kawara date paintings — as OPPOSITION
> sophie calle ghosts — as kin maybe
> hannah villiger — kin, alternative photography

[Plugin: Mandatory training-data bias header (read fully):]

  TRAINING-DATA BIAS DISCLOSURE
  ─────────────────────────────────────────────
  LLM substrate over-represents: anglophone media-art
  venues; 1990s–2010s US/UK/DE generative-art scene;
  canonised conceptual art (LeWitt, Weiner, Kawara).

  Under-represented: non-anglophone PaR doctoral
  expositions; Korean / East-Asian media-art (esp.
  post-2010); oral / ritual / improvisational
  traditions.

  Korean / East-Asian default routing is ON for
  this session (input language: Korean detected;
  Korean precedent declaration: yes).
  ─────────────────────────────────────────────

[Plugin: Lineage Map (12 entries) follows, with kin / opposition /
  blind-spot / unexpected-neighbor tags.]

  Entry 4
  ─────────────────────────────────────────────
  Park Hyunki, "Untitled (TV stone tower)" (1979).
  TAG: kin
  Korean / East-Asian routing surfaced this entry.
  Why kin: Park's stone-with-monitor work treats the
  *object that bears the image* as the question, not
  the image itself. Your work's back-of-photo
  inscription does similar work on a smaller scale.
  ─────────────────────────────────────────────

  Entry 9
  ─────────────────────────────────────────────
  "An Artist You Might Not Know" (anglophone
  generative-art scene, 1990s).
  TAG: unexpected-neighbor — flagged for verification.
  This is an unexpected-neighbor entry; the plugin's
  confidence here is LOW and the bias header above
  applies most strongly to this entry. Verify before
  citing.
  ─────────────────────────────────────────────

  [10 other entries.]
```

She verifies Entry 9 with a quick search. The artist exists; the specific work does not. She removes the entry and annotates the project file: "lineage entry 9 was a hallucination — verified by web search; removed." This is the bias-header discipline working: a flagged low-confidence entry gets external verification before it survives.

## Week 3, Session 4 — Brief

She has Soo-jin's material now: a map, a chosen tradition (Cage chance operations), an opposition (Kawara), kin (Park Hyunki).

```text
> /art-project:ideate

> brief

[Plugin: Brief mode active. Stay-rough default ON.
  Pulling material from sessions 1, 2, 3 of this project file.
  Empty fields reported as [gap, not in input].
  10 fields follow.]

  CONCEPT BRIEF — inscription-counter-inscription

  1. Working title:
     inscription / counter-inscription

  2. Provocation [Borgdorff sense]:
     What does it mean for an inscription to
     disclaim its authorship?

  3. Proposition:
     [stay-rough from session 1 socratic]
     the work is about marks that don't claim authorship

  4. Anti-proposition:
     [stay-rough from session 2 provoke (card 3 + card 9)]
     the work argues against the curatorial assumption
     that authorship is the locus of value

  5. Disconfirmation condition:
     the work fails if the viewer reads it as a memorial.

  6. Intended encounter:
     [from session 1 socratic constraints]
     a single viewer at a time, in dim light,
     with permission to handle the work

  7. Lineage anchor:
     OPPOSITION: On Kawara date paintings (Kawara
     claims authorship through ritual; this work
     refuses the claim).
     KIN: Park Hyunki, "Untitled (TV stone tower)"
     (1979).

  8. Materials and scale:
     [stay-rough from session 1 socratic]
     photographs, the size of a hand. number unknown
     yet. duration of viewing: unbounded.

  9. Risk and refusal:
     Risk: the work reads as nostalgia.
     Refusal: not a memorial; not a family history piece.

  10. Frayling-type declaration:
     [REQUIRED: artist must declare]

> research-FOR art

[Plugin: Research-FOR art confirmed. Brief complete.
  Empty fields: none.
  Cautious fields: none.
  Stay-rough fragments preserved verbatim.

  To request smoothing for submission, use:
    /art-project:brief --polish
  Polish is opt-in. Default is rough.]
```

She does not run `--polish` yet. The exposition is two weeks out; she wants to sit with the rough brief first.

## Week 4, Session 5 — Rehearsal

```text
> /art-project:ideate

> rehearsal

[Plugin: Rehearsal mode active.

  REHEARSAL DISCLAIMER
  ─────────────────────────────────────────────
  This is formative practice, not decisional review.
  The personas below are simulated; their questions
  do not substitute for real curatorial, peer, or
  critical feedback. Real critique is constituted
  by relational history the simulation does not have.
  ─────────────────────────────────────────────

  Four personas will question the brief:
    Curator + Practitioner-peer + Theorist + Devil's Advocate.

  Begin.]

  [CURATOR]
  The brief says "single viewer at a time, in dim
  light, with permission to handle the work." For
  a JAR exposition that is a constraint, not a
  context. How are you proposing to translate the
  intended encounter into JAR's online format?

> [Soo-jin answers, and so on for the other three personas]

  [DEVIL'S ADVOCATE]
  The refusal "not a memorial" is doing a lot of
  work. What if the work IS a memorial and the
  refusal is your defence against admitting it?
```

She does not have a clean answer to the Devil's Advocate question. The session ends without a verdict — rehearsal is formative-not-decisional. She returns to her studio with the question.

Two days later, she runs rehearsal again on the same project. The plugin fires the architectural friction:

```text
> /art-project:ideate

> rehearsal

  FRICTION WARNING
  ─────────────────────────────────────────────
  You have rehearsed this concept 2 times in the
  last 14 days. Further rehearsal risks
  simulation-pedagogy harm (Schön 1983)…

  Consider:
    (a) taking the brief to a real interlocutor
    (b) returning to socratic / provoke with the
        questions that surfaced in rehearsal
    (c) sitting with the brief without further rehearsal

  Proceed anyway? [y/N]
  ─────────────────────────────────────────────

> n
```

She chooses (b). Returns to socratic with the Devil's Advocate question. The project file now has six sessions, an annotated lineage map with one hallucination caught and removed, a rough brief, and an honest open question.

## What this example shows

- **Cross-session persistence**: every session's output lives in the project file; later sessions reference earlier ones.
- **One mode per session in `full`**: she did not try to pipeline socratic → brief in one sitting.
- **Stay-rough preserved across modes**: brief mode pulls fragments from sessions 1–3 verbatim, not as polished prose.
- **Bias header discipline catches a hallucination**: Entry 9 of the Lineage Map was flagged as unexpected-neighbor with low confidence; verification removed it.
- **Authentic Practice Boundary fires per card**: every provoke card declared what the cited methodology requires that the AI does not perform.
- **Architectural friction in rehearsal**: she rehearsed twice in 14 days; the plugin warned; she chose a different path.
- **The artwork does not exist yet**. The plugin produces language; the studio work still has to happen.

## See also

- Each mode in detail: [Socratic](../modes/socratic.md), [Provoke](../modes/provoke.md), [Lineage](../modes/lineage.md), [Brief](../modes/brief.md), [Rehearsal](../modes/rehearsal.md), [Full](../modes/full.md).
- The Concept Brief schema: [Reference](../reference/concept-brief.md).
- Why the friction warnings: [Measured harms](../philosophy/measured-harms.md) §3.
