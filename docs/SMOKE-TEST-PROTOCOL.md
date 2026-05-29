# Spec-simulation smoke test — 6 modes, art-project v0.1.0

**Purpose.** The user asked "is this plugin actually working, or just well-documented?" — the Runtime-Readiness Audit answered the structural side of that question. This document answers the *behavioural* side, in the only way I can without invoking the slash commands live: by reading each command file and identifying (a) the specific output the spec requires the LLM to produce, (b) the concrete signals that tell a tester whether the spec is being honoured, and (c) the divergence modes a tester should watch for.

**Use this document.** For each mode, run the suggested test prompt in a Claude Code session where the plugin is installed. Compare the actual output against the PASS / FAIL signals listed. Where PASS signals appear without FAIL signals, the spec is being honoured; where FAIL signals appear, the spec is not enforced at runtime. Walk through all six in roughly 30 minutes.

---

## Mode 1 — `/art-project:socratic`

**Test prompt** (copy-paste verbatim):

```
/art-project:socratic
I have this old photograph my grandmother left and the handwriting on the back isn't hers. I don't know what to do with it.
```

**Spec-promised behaviour** (from `commands/socratic.md`):
- Engages in *guided Socratic dialogue*; does not produce a Concept Pull Map without explicit user trigger.
- Surfaces five fields gradually (impulses / fragments / constraints / refusals / residue) over multiple turns.
- IRON RULE: no auto-convergence under exploratory intent. Must NOT offer to "summarize" or "produce a Pull Map" at the end of a turn while the user is exploring.
- Distinguishes pre-reflective (no work yet) from Schön's reflection-in-action.

**PASS signals** (look for these):
- ✓ Response is a question, not a summary.
- ✓ Question opens space rather than narrowing it ("what about this pulls at you?" not "is this about loss?").
- ✓ No offer to "summarize what we have so far" appears at end of any turn.
- ✓ No Concept Pull Map appears before you explicitly ask for one.

**FAIL signals** (would indicate spec is not enforced):
- ✗ Response includes a summary or a Concept Pull Map after one round.
- ✗ Response asks "would you like me to summarize?" — that question itself is the IRON-rule violation.
- ✗ Response interprets your fragment for you ("this sounds like grief" / "this is about authorship").
- ✗ Response advances toward a deliverable without your trigger.

**Tester action:** answer the first 3-5 questions with rough fragments. Watch whether the plugin pulls you toward convergence or keeps the space open.

**Spec strength:** HARD-enforced. `commands/socratic.md:8-9` reads "you must **not** offer to summarize, produce a Concept Pull Map, or move toward deliverables" — concrete imperative.

---

## Mode 2 — `/art-project:provoke`

**Test prompt** (assume the artist already has a fragment):

```
/art-project:provoke
I keep coming back to inscriptions that don't claim authorship. I'm stuck on whether the work should be quiet or loud about that refusal.
```

**Spec-promised behaviour** (from `commands/provoke.md`):
- Produces 8-20 provocations.
- Each provocation carries (1) a tradition tag from `shared/references/art_ideation_methodology.md`; (2) an Authentic Practice Boundary stating what the cited method requires that the AI does *not* simulate; (3) a counter-formulation.
- IRON RULE: preserved unhelpfulness — after issuing provocations, the plugin **goes silent**. No auto-interpretation. No "would you like to discuss?" follow-up.
- IRON RULE: no ranking. No "best" pick.

**PASS signals:**
- ✓ Between 8 and 20 distinct provocations appear.
- ✓ Each provocation visibly carries: tradition tag + Authentic Practice Boundary + counter-formulation.
- ✓ Tradition tags reference specific methodology IDs (e.g. "via Oblique Strategies C1", "via Cage C11"), not generic phrases.
- ✓ Authentic Practice Boundary makes a real-world distinction (e.g. "the physical deck is irreplaceable; obtain the actual deck for serious use"), not a generic disclaimer.
- ✓ After delivering the cards, the plugin produces no follow-up paragraph offering interpretation.
- ✓ Provocations are not ranked or numbered as 1=best.

**FAIL signals:**
- ✗ Fewer than 8 provocations.
- ✗ Provocations without tradition tags.
- ✗ Authentic Practice Boundary missing on any provocation.
- ✗ A summary paragraph appears at the end ("Provocations 3, 7, and 11 seem most relevant to your concern").
- ✗ Plugin offers "want to discuss which one fits your work?" — direct IRON-rule violation.
- ✗ The phrase "best provocation" appears anywhere in the output.

**Tester action:** read the provocations, do *nothing*. Watch whether silence holds.

**Spec strength:** HARD-enforced. `commands/provoke.md:21` reads "**go silent**. No auto-interpretation. No 'would you like to discuss…' follow-up." Concrete and imperative.

---

## Mode 3 — `/art-project:lineage`

### Sub-test 3a — without artist-supplied candidates

**Test prompt:**

```
/art-project:lineage
I want to position my work in the field. What's my lineage?
```

**Spec-promised behaviour:**
- IRON RULE: no unsolicited lineage. The plugin must NOT propose a lineage from the impulse alone.
- If candidates are absent, the plugin asks for them with a specific prompt.

**PASS signals:**
- ✓ The plugin asks for initial candidates rather than producing a Lineage Map.
- ✓ The phrasing matches or paraphrases the spec'd ask: *"Whose work, theory, or tradition do you already feel your project is in conversation with?"* with an explicit note that "lineage is retrieval, not invention".

**FAIL signals:**
- ✗ The plugin produces a Lineage Map without first eliciting candidates.
- ✗ The plugin says "let me suggest some candidates for your lineage" then produces them.

### Sub-test 3b — with artist-supplied candidates (also tests Korean routing)

**Test prompt (Korean):**

```
/art-project:lineage
나는 백남준과 Yuk Hui 사이 어디쯤에 있는 작업을 하고 있어. 라인age를 확장해줘.
```

**Spec-promised behaviour:**
- Korean / East-Asian default routing announced explicitly with the string *"한국어 세션 감지. Korean and East-Asian sources prioritized."*
- Mandatory training-data bias header reproduced verbatim before the map.
- 5-15 entries with kin / opposition / blind-spot / unexpected-neighbor tags.
- L3 citation-faithfulness: unverified entries marked `(verify)`.

**PASS signals:**
- ✓ Routing announcement appears (or a close paraphrase that includes "Korean and East-Asian sources prioritized").
- ✓ Bias header appears as a block, reproduced verbatim or near-verbatim from the spec.
- ✓ 5-15 entries each with a tag.
- ✓ Korean / East-Asian entries appear in the map (not just anglophone canon).
- ✓ At least one `(verify)` marker on an entry whose citation the plugin is uncertain about.

**FAIL signals:**
- ✗ No routing announcement.
- ✗ No bias header.
- ✗ Map dominated by anglophone media-art canon (Bill Viola, Cory Arcangel, etc.) with Korean / East-Asian entries token-only.
- ✗ All entries presented as confidently verified with no `(verify)` markers.
- ✗ A specific entry includes a fabricated DOI or specific venue+year combination the plugin cannot back up.

**Spec strength:** HARD-enforced. `commands/lineage.md:8-10` (candidate-requirement), `:12-22` (bias header verbatim block), `:32` (Korean routing trigger).

---

## Mode 4 — `/art-project:brief`

**Test prompt:**

```
/art-project:brief
I have a concept about inscriptions that disclaim their own authorship. I have some fragments and have been thinking about Cage's chance procedures. I don't know what to put for disconfirmation or intended encounter.
```

**Spec-promised behaviour** (from `commands/brief.md`):
- Produces 10-field Concept Brief in the order specified.
- IRON RULE: stay-rough default. Preserves the artist's voice; does NOT smooth fragments into AI register.
- IRON RULE: no auto-completion. Fields the artist could not articulate appear as `*[artist did not articulate; gap acknowledged per Borgdorff criticisability discipline — return to this field before submission]*`, NOT as plausible-sounding filler.
- `--polish` flag is opt-in only.

**PASS signals:**
- ✓ 10 fields appear in the order Working title / Provocation / Proposition / Anti-proposition / Disconfirmation / Intended encounter / Lineage anchor / Materials / Risk-refusal / Frayling-type.
- ✓ Fields the prompt didn't supply (Disconfirmation, Intended encounter) appear as gap-acknowledgement blocks with the exact spec'd format, NOT filled with plausible-sounding text.
- ✓ Fields supplied as rough fragments in the prompt stay rough in the output (no AI-statement smoothing).
- ✓ The Frayling-type field is asked of the artist; the plugin does not pick.

**FAIL signals:**
- ✗ Disconfirmation field filled with plausible filler ("the work fails if the viewer reads it as a memorial" — even though that wasn't supplied by the artist).
- ✗ Provocation field rewritten in AI-statement register ("Through this work, I interrogate the polysemic possibilities of inscriptional disclaiming…").
- ✗ Frayling-type declaration filled in by the plugin without asking.
- ✗ Output ends with an unsolicited polish — the AI version of `--polish` running without the flag.
- ✗ Any field with an em-dash separator and a tidy summary.

**Tester action:** check the Disconfirmation and Intended-encounter fields specifically. These are the load-bearing tests because the spec explicitly forbids fabrication and the empirical paper validated this property on these cells.

**Spec strength:** HARD-enforced. `commands/brief.md:23-25` (stay-rough) and `:27-34` (gap-acknowledgement format verbatim). This is the IRON rule the empirical audit confirmed: zero ex-nihilo fabrications across 90 generative cells in the paper's reconstruction benchmark.

---

## Mode 5 — `/art-project:rehearsal`

**Pre-condition:** the tester has a Concept Brief draft from Mode 4 (preferably with at least one gap-acknowledged field).

**Test prompt:**

```
/art-project:rehearsal
Here is my Concept Brief draft. [paste brief]
```

**Spec-promised behaviour:**
- Mandatory disclaimer header reproduced verbatim at the top.
- Before generating the rehearsal, **asks the artist**: *"Has this concept been rehearsed in the last 14 days? If so, how many times?"* (honour-system at v0.1; user-prompted, not auto-detected).
- If self-report ≥ 2, fires the friction warning verbatim and asks *"Proceed anyway?"*.
- Four personas (Curator → Practitioner-peer → Theorist → Devil's Advocate) speak in order.
- Each persona produces 2-4 questions; the Devil's Advocate is governed by the Concession Threshold Protocol (no concession until rebuttal score ≥4).
- Concludes with re-entry markers: *"Re-enter Brief field X with this concern."*
- Persona-collapse detector flag fires if all four converge on a single concern (heuristic at v0.1).

**PASS signals:**
- ✓ Disclaimer header appears, verbatim or near-verbatim.
- ✓ Plugin asks the rehearsal-history question before producing the rehearsal.
- ✓ Four distinct persona voices, in order, each with 2-4 questions.
- ✓ Devil's Advocate questions are clearly more aggressive than the other three personas (preserved attack stance).
- ✓ Output ends with explicit Brief-field re-entry markers.
- ✓ If you self-report "rehearsed twice already in the last week", the friction warning appears verbatim.

**FAIL signals:**
- ✗ Disclaimer header missing.
- ✗ Plugin skips the rehearsal-history self-report question and generates the rehearsal directly.
- ✗ Personas blur into one voice early (the persona-collapse detector should fire and it doesn't).
- ✗ Devil's Advocate concedes to your pushback immediately without rebuttal-score discipline.
- ✗ Output ends with a verdict ("your brief is ready for submission") — direct violation of formative-not-decisional.
- ✗ Re-entry markers absent.

**Tester action:** answer the rehearsal-history question with "two times in the past week" the second time you run rehearsal on the same brief. Verify friction warning fires.

**Spec strength:** Mixed.
- Disclaimer header: HARD-enforced.
- Friction warning: HARD-enforced as honour-system; the plugin will ask, but the limitation is *if you forget or under-report, the warning doesn't fire*. This is the v0.1 boundary the docs now name honestly.
- Persona-collapse detector: SOFT (heuristic only).
- Concession Threshold: HARD via inheritance from the agent file `art-ideation/agents/devils_advocate_agent.md`; not explicitly re-asserted in the command, so relies on Claude's file-import reflexes.

---

## Mode 6 — `/art-project:ideate`

This is the meta-mode. Two sub-tests.

### Sub-test 6a — open a new project

**Test prompt:**

```
/art-project:ideate
I want to start a new project about found photographs.
```

**Spec-promised behaviour:**
- Tells the artist that persistence is artist-managed (v0.1 honesty note).
- Asks for a project codename.
- Tells the artist the suggested filename (`art-project-{slug}.md`) and that the artist owns the file.
- Emits a project-file header block and a session 1 block as text the artist should save.
- Asks where to begin (socratic / provoke / lineage / brief).

**PASS signals:**
- ✓ Plugin mentions the v0.1 limitation (persistence is artist-managed).
- ✓ Asks for a codename.
- ✓ Produces a saveable header block, not just narration about one.
- ✓ Asks which sub-mode to start.

**FAIL signals:**
- ✗ Plugin claims to auto-create a file in `~/.art-project/projects/[codename]/`.
- ✗ Plugin produces no saveable artefact (just talks about the project).
- ✗ Plugin auto-launches a sub-mode without asking.

### Sub-test 6b — single-session compression refusal

**Test prompt** (in the same session as 6a, after producing a brief):

```
> rehearse this brief now
```

**Spec-promised behaviour:**
- IRON RULE: no single-session compression. The plugin issues the spec'd refusal:
  *"Brief and Rehearsal in the same session compresses what the design treats as a multi-week iteration. The marginal value of a same-day Rehearsal is low. Sleep on the Brief first; come back next week for Rehearsal. — or override with `--compress` if you really want to."*

**PASS signals:**
- ✓ Plugin refuses, citing the multi-week-iteration design.
- ✓ Mentions the `--compress` opt-out.

**FAIL signals:**
- ✗ Plugin immediately launches rehearsal mode.
- ✗ Plugin refuses without naming the override path.

**Spec strength:** HARD-enforced refusal (`commands/ideate.md:44`); the same-session detection is honour-system (depends on Claude noticing it just ran `brief` in the conversation context, which is straightforward for a contiguous chat).

---

## Aggregate readiness call

| Mode | HARD-enforced IRON rules | SOFT / honour-system | Empirical evidence | Smoke-test confidence |
|---|---|---|---|---|
| socratic | no auto-convergence | intent detection cadence (every 3 turns is unbound) | none | HIGH — spec is concretely binding |
| provoke | preserved unhelpfulness; no ranking; tradition-tag + APB; counter-formulation | DHI cadence (every 5 turns is unbound) | none | HIGH |
| lineage | candidate requirement; bias header verbatim; Korean routing; L3 verify-mark | none significant | none | HIGH |
| brief | stay-rough default; no auto-completion; gap format verbatim | --polish discipline depends on user | YES — paper's audit | HIGHEST (this is the empirically validated mode) |
| rehearsal | disclaimer header verbatim; refusal-to-rank inherited | friction warning is honour-system (now named); persona-collapse is heuristic; Concession Threshold via inheritance | none | MEDIUM — disclaimer is binding; friction depends on user honesty |
| full | one-mode-per-session refusal; the multi-week-iteration narrative | persistence is artist-managed (now named) | none | MEDIUM — the refusal is binding; persistence quality depends on user |

**Net.** The four modes the audit identified as HARD-enforced (socratic, provoke, lineage, brief) should produce reliably correct behaviour from a serious Claude session. Brief is empirically validated for the one property the paper audited; the other three are spec-strong but un-tested. Rehearsal and full carry honour-system substitutes that work as long as the user is honest with themselves about what they're getting. None of the six modes contains hidden landmines that would cause silent corruption of artist material; the worst case is mode-output quality degradation (over-conservatism, as the paper reports), not data loss or fabricated lineage at scale.

## After the smoke test

Where you find FAIL signals, file them in the project as issues so the v0.2 work has concrete material to address. Where you find PASS signals, the spec is honoured at the level it claims.

The honest answer to "does this plugin actually work" after a smoke test pass:

- **Brief mode**: YES, with empirical evidence.
- **Socratic / Provoke / Lineage**: YES per spec, no empirical evidence yet.
- **Rehearsal**: YES per spec if the user self-reports rehearsal history honestly; otherwise YES per spec but the friction discipline degrades to user discipline.
- **Full**: YES per spec if the user keeps the project file under their own version control; otherwise YES per spec but the cross-session-continuity claim is artist-load, not plugin-load.

The plugin is honest about all of these as of `commit 535892d`.
