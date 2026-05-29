# art-project v0.2 — Design + Paper Synthesis Spec

**Status:** Design synthesis (Phase 0b — supersedes v0.1 pivot spec on the points addressed below)
**Date:** 2026-05-24
**Author note:** This document synthesizes the outputs of a four-agent design critique:

1. *Artistic-research methodologist* (PaR / Frayling / Borgdorff / Sullivan perspective)
2. *HCI / AI-creativity researcher* (Shneiderman / Cherry-Latulipe / Davis / Wordcraft-Sparks lineage)
3. *Practicing artist studio-side review* (real-use scenarios; what survives in a studio)
4. *Devil's Advocate* (Penny / Ingold / Borgdorff / Wittgenstein / Illich attacks on the premise)

The full critiques are available in the conversation transcript backing this commit and should be read alongside this spec. This document is the **synthesis** — the design decisions that survived the cross-fire.

> **Single most consequential move in this revision:** drop the term **"ideation engine"** in favor of **"pre-studio articulation scaffold"**. art-project does *not* claim to participate in artistic ideation in the Penny / Ingold / Borgdorff sense. Ideation, on the cited literature's own definition, happens in the studio with material. art-project *prepares* the artist for that work — it scaffolds the propositional articulation that surrounds ideation. This reframe converts the single most lethal critique (Devil's Advocate Attack 1 — that the plugin cites the very literature that disqualifies its method) into a scope statement.

---

## 1. What art-project is (revised)

### 1.1 Definition

art-project is a **pre-studio articulation scaffold** — a Claude Code plugin that assists a practice-based artist in the **propositional articulation work** that surrounds the conception of a new project: surfacing the impulse, generating tension-holding provocations, mapping (when the artist requests it) precedent lineage, drafting a Concept Brief, and rehearsing self-critique. The artistic ideation itself happens elsewhere — in the studio, in materials, in bodies, in time. The plugin's job is to help the artist *enter* that work with sharper language and a clearer set of refusals.

The reframe addresses the Devil's Advocate / Penny / Ingold / Borgdorff attack head-on: the plugin does not claim to do what only studio practice does. It claims to scaffold the part of artistic-research labor that *is* propositional — the part that goes into grants, statements, doctoral expositions, peer-review responses, collaborator briefings, and the artist's own future-self memos.

### 1.2 Frayling self-positioning (layered hybrid)

Following Methodologist Critique Q1, art-project declares its position within Frayling's (1993, *Research in Art and Design*, RCA Research Papers 1(1)) three-category typology explicitly, in layers:

- **Tool layer — research FOR art.** The plugin as software is an instrument intended for use by practice-based artists. This is its primary public face.
- **Reference layer — research INTO art.** `shared/references/art_ideation_methodology.md` is a second-order synthesis of how prior literature theorizes artistic ideation. It is *about* artistic practice; it does not *do* it.
- **Design-choice layer — research THROUGH art/design.** The architectural choices in the plugin (generation-evaluation separation, tension-over-ranking, lineage-with-opposition, formative-not-decisional self-critique, tradition-tag attribution, refusal-to-rank) are themselves propositional claims about how AI assistance in PaR ideation should be architected. The plugin-as-artefact is the demonstration; the accompanying paper argues the claims.

This three-layer declaration is itself the contribution. Each layer is evaluable by its own criteria; conflating them is the mistake Frayling himself flagged in 1993 and that every PaR theorist since (Candy 2006 *Practice-Based Research: A Guide* (verify); Skains 2018 *Creative Practice as Research* (verify); Borgdorff 2011, 2012) has insisted on declaring.

### 1.3 Epistemological position (the cognitive-scaffold frame)

Following Methodologist Critique Q3 and consistent with Devil's Advocate Reframe 1, art-project occupies the **cognitive scaffold** position — neither *inert tool* (which would make it Sullivan-conservative and reduce the contribution to "a curated prompt library") nor *co-author / co-investigator* (which would require empirical evidence the v0.1 plugin does not have, and would invite the AI-authorship overclaiming critique).

The defensible middle is:

- **Clark & Chalmers (1998), "The Extended Mind", *Analysis* 58(1):7–19** — cognition can extend into external scaffolds that meet the parity and reliability conditions. The plugin is such a scaffold in the same family as Eno & Schmidt's Oblique Strategies deck, an artist's notebook, or a peer-conversation partner — not an author of the artist's thinking.
- **Malafouris (2013), *How Things Shape the Mind: A Theory of Material Engagement*** — cognition is constituted in the engagement with materials and tools, not located behind the skin. The plugin is a propositional-material engagement partner.
- **Penny (2017), *Making Sense*** (already cited at D8 in the methodology reference, but with its critical edge restored in v0.2) — embodied practice is the locus of artistic knowing; this plugin operates *adjacent to* that locus, in the para-artistic space of articulation work, and does not claim to substitute for it.

The cognitive-scaffold framing has three further virtues:
- it leaves authorship of the artwork unambiguously with the human (clean for SIGGRAPH Asia AI-disclosure compliance and for copyright);
- it is consistent with the design choices the plugin already makes (refusal to rank, tension-over-resolution, formative-not-decisional critique);
- it has academic precedent and can be cited (Clark & Chalmers; Malafouris; the extended-cognition literature generally), so reviewers do not have to take it on faith.

### 1.4 User asymmetry — scope statement (this is not a universal tool)

Following Devil's Advocate Reframe 2 and Practicing Artist Q6/Q8, art-project explicitly scopes itself to artists for whom **propositional articulation is a bottleneck**, not to all artists. This is a *scope* claim, not a marketing claim:

- early-career artists who have not yet developed the genre conventions of the artist statement / grant proposal / concept brief
- artists writing in a second language (especially Korean-first artists writing English grant applications, and vice versa)
- artist-researchers preparing PaR doctoral expositions where the articulation work *is* part of the research
- artists working under deadline (grant cycles, residency applications, biennale call-for-works)
- artists for whom external scaffolding helps (the practicing-artist critique flags neurodivergent artists specifically — verify with the relevant adaptive-tooling literature before publishing this scope explicitly)
- collectives mid-project who need a shared articulation document

The plugin is **not** intended for, and should be expected to add little value to, artists for whom propositional articulation is already fluent. The practicing-artist critique's blunt conclusion — *"I would currently turn it off and use Claude directly"* — is the correct response for this group. The plugin's value is concentrated where the bottleneck is real.

This scope statement neutralizes two attacks simultaneously: (a) Devil's Advocate Attack 5 ("the real user is the researcher, not the artist") because the user is now a specific subgroup whose needs are nameable; (b) the universal-tool overreach implicit in v0.1.

---

## 2. Skill design (revised)

One skill, six modes. The modes have been **renamed and reshaped** in light of the four critiques. Changes are flagged inline.

### 2.1 Mode table

| Mode | New name (if changed) | Spectrum | Output | Oversight |
|---|---|---|---|---|
| `socratic` | (unchanged) | Originality | Concept Pull Map | Very High |
| `provoke` | (unchanged) | Originality | Tradition-tagged provocation set | High |
| `lineage` | (unchanged, but behaviorally constrained) | Fidelity | Lineage Map (with bias disclosure) | Medium |
| `brief` | (unchanged, schema rebuilt) | Balanced | Concept Brief (epistemic fields, stay-rough) | High |
| ~~`panel`~~ | **`rehearsal`** | Balanced | Self-Critique Rehearsal transcript | High |
| `full` | (unchanged name, behavior reshaped) | Balanced | Long-running project file across sessions | Very High |

The renaming of `panel` → `rehearsal` is consequential: it commits to Methodologist's "method-not-evaluation" verdict (Q5) and Devil's Advocate's "rehearsal scaffold, not critique" framing (Attack 4 remediation). The word "panel" implied judgement; "rehearsal" implies preparation for judgement that will happen elsewhere.

### 2.2 Mode reshapings — what each mode now does and does not do

#### `socratic` — pre-reflective articulation, not Schön reflective practice

**What it is.** Guided dialogue that surfaces the artist's impulse-fragments-constraints-refusals before there is a work to reflect on. This is **pre-reflective** in the strict sense (Methodologist Q5 socratic): the artist has not yet made the move on which to reflect, so this is *not* Schön's (1983, *The Reflective Practitioner*) reflection-in-action. Stating this distinction explicitly — rather than letting reviewers ask why Schön is absent — is the v0.2 move.

**What it does not do.** It does not converge. The IRON RULE that auto-convergence is disabled in exploratory intent (inherited from the parent suite) is preserved and made explicit: while intent-detection classifies the artist's state as exploratory, the plugin will not produce a Concept Pull Map without explicit user trigger. The practicing-artist Scenario A worry — that a clean 4-category Pull Map *flattens* the messiness of a month-long impulse — is partially mitigated by adding a **"residue" field** to the Pull Map (Practicing-Artist proposed "Studio note dump" mode merged in): contradictions, half-finished fragments, and impulses that don't fit the four categories are captured *verbatim* under "residue" rather than forced into the schema.

**Tradition tags wired:** Frayling (1993), Borgdorff (2011, 2012), Sullivan (2010), Smith & Dean (2009), Csikszentmihalyi (1996, 1999); plus Geneplore (Finke, Ward & Smith 1992) for the explicit generation-before-evaluation discipline. Schön is *cited but not wired* — used only as the distinction marker.

#### `provoke` — experimental gestures with preserved unhelpfulness

**What it is.** The provocation engine — but **with the Practicing-Artist Q3 "unhelpfulness" constraint** loaded explicitly into the prompt. The Oblique Strategies deck (Eno & Schmidt 1975) draws its authority from being physical, finite, and *unwilling to interpret itself*. The plugin's `provoke` mode, when issuing an Oblique-style provocation, must default to silence after the provocation. No interpretation. No "would you like to discuss how this applies?" follow-up. The artist asks for an interpretation explicitly or doesn't get one.

This is reinforced by binding provocations to **Bolt's (2007) "experimental gesture"** notion (Barrett & Bolt, *Practice as Research*) — provocations are interventions whose value is in the displacement they enact, not in the content they propose. The plugin will not rank provocations and will not converge.

**Tradition tags wired:** Eno & Schmidt (Oblique Strategies, 1975), SCAMPER (Eberle 1971 — but see §2.3 "tradition tag honesty" below: SCAMPER has weak empirical support in designer-cognition studies, e.g. Christensen & Schunn (2007); the tag is for *style affinity*, not effectiveness claim), de Bono (1967, 1985), Cage (chance operations — but see §2.3 Authentic Practice Boundary: the plugin proposes the method, the *artist executes* it), Boden (1990, 2004) for the combinational/exploratory/transformational typology, Dunne & Raby (2013) for the speculative-design what-if mode.

**Authentic Practice Boundaries** declared per cited method (see §2.3).

#### `lineage` — constrained retrieval, not unsolicited consecration

**What it changes.** This is the mode that took the heaviest fire, from three of the four critics (Devil's Advocate Attack 3, Practicing Artist Q4 + Q7, Methodologist Q4 East-Asian positionality). The reshape:

1. **No unsolicited lineage.** The mode does *not* propose a lineage from the impulse alone. The artist must provide initial candidates ("I think my work sits between X and Y"). The plugin extends — adds kin, opposition, blind-spots, unexpected neighbors — but never *opens* the lineage. This addresses Practicing-Artist Q4 (the 3-year self-discovery journey must not be short-circuited) and Devil's Advocate Attack 3 (consecration risk).
2. **Training-data bias disclosure mandatory.** Every lineage output carries a header note: *"This lineage map reflects the plugin's training-data clustering, which is biased toward anglophone media-art venues (Ars Electronica, ZKM, SIGGRAPH, Whitney, MIT). Entries outside that scope are systematically under-represented; entries in oral, indigenous, or non-anglophone-published traditions may be absent entirely. Treat as a partial map, not the canon."* This is the operational form of Devil's Advocate Reframe 3 (measured-harm disclosure).
3. **Korean / East-Asian default routing.** When the mode is invoked in Korean *or* when subject-domain signals indicate East-Asian context (e.g. work draws on yi/qi/yeobaek vocabulary, dansaekhwa lineage, Korean media-art post-Paik), the plugin prioritizes Korean and East-Asian sources before global ones, and announces this routing decision. This addresses Practicing-Artist Q7 (currently the lineage mode in Korean returns Western sources by default — a *misleading bilingual*).
4. **Opt-out clean.** The mode must offer a clean `--no-lineage` flag at any point in the dialogue so the artist can refuse the consecration. The Practicing-Artist's Q4 worry — that being told one's lineage *prevents* the work that would have refused that lineage — is real; the architectural answer is to make refusal a first-class option.
5. **Honest naming.** The mode's docstring now reads: *"Lineage mapping is a retrieval operation that surfaces precedent works/artists/texts the LLM clusters near your stated candidates. It is not ideation. It is closer to a guided literature search than to a creative act. Use it for positioning, not for inspiration."* Devil's Advocate Attack 3's "lineage = retrieval, not ideation" critique becomes the mode's self-description.

**Methodological standing.** With these reshapes, this is still — per Methodologist Q5 — the mode whose PaR-standing is *highest*, because the kin/opposition/blind-spot/unexpected-neighbor schema directly enacts Sullivan's (2010) contextualist inquiry: lineage as a deliberate epistemic act of self-positioning, not as marketing.

#### `brief` — Concept Brief with epistemic fields and "stay-rough" default

**What it changes.** This is the mode the Practicing Artist (Scenario C) flagged as a *dangerous convenience*: AI-polished briefs are detectable from a kilometer away and read as reject signals by real reviewers. The Methodologist (Q5 brief) independently flagged that the schema as written produces a one-pager, not a PaR proposition document. The reshape combines both fixes:

1. **Schema rebuilt with epistemic fields (Methodologist's prescription):**
   - *Working title*
   - *Provocation* (Borgdorff: the research question implicit in the impulse)
   - *Proposition* — what claim the work proposes
   - *Anti-proposition* — what the work refuses to assert (Sullivan dialectical inquiry)
   - *Condition for disconfirmation* — what reception or failure would falsify the proposition
   - *Intended encounter* (Bogart 1995, Viewpoints) — what spatial / temporal / kinesthetic relation the work proposes for the audience
   - *Lineage anchor* (with bias disclosure as in §2.2 lineage)
   - *Materials / medium / scale*
   - *Risk / refusal* (Corita Kent 1968; Saltz 2018) — what the work might fail at and what the artist refuses to do for it
   - *Frayling type declaration* — INTO / THROUGH / FOR (which of the artist's own research the work performs)

2. **Stay-rough default (Practicing Artist's prescription):** the prose stays in the artist's voice. The plugin's job is to *force articulation of each epistemic field* but not to *smooth the prose*. The default behavior is to ask the artist to dictate the proposition / anti-proposition / etc. and capture the wording with minimal edit. A `--polish` flag exists for the case where the artist wants ESL or grammar pass, but it is *not* the default. This converts the "AI-detectable smoothness" failure mode into an opt-in.

3. **No auto-completion.** If the artist cannot articulate the disconfirmation condition or the anti-proposition, the plugin reports the gap rather than filling it. Borgdorff's criticisability gate is satisfied by *acknowledged absence*, not by plausible-sounding filler.

With these two changes — epistemic fields + stay-rough — the Concept Brief becomes a defensible PaR *proposition document* (in the JAR / Research Catalogue tradition's "exposition" sense), not a polished marketing one-pager. This satisfies Borgdorff's criticisability gate, Sullivan's dialectical stance, and Frayling's typing requirement *simultaneously*.

#### `rehearsal` (renamed from `panel`) — Self-Critique Rehearsal, not critique

**What it changes.** Per Devil's Advocate Attack 4 + Methodologist Q5 panel + Practicing Artist Q5: the renamed `rehearsal` mode commits explicitly to being a *rehearsal scaffold*, not a critique. It exists so the artist can rehearse articulating their work under questioning *before* facing real curators, peers, or critics.

The architectural changes:

1. **Mandatory disclaimer header on every invocation** (Practicing-Artist Q5 boilerplate, refined):
   > "This is a Self-Critique Rehearsal. It is *not* curatorial review, peer critique, or evaluation. It is practice articulating your work under pressure. The personas are simulations; they have no studio history, no shared context with you, no skin in the game. Real critique operates differently and will surprise you. Use this rehearsal to surface your own blind spots before submitting work to actual reviewers."

2. **Architectural friction against repeated use on the same concept.** If the same Concept Brief is run through rehearsal more than 2 times within a 14-day window, the plugin warns: *"You have rehearsed this concept multiple times. Consider showing it to an external reader before further rehearsal — the marginal value of additional rehearsal is low compared to one round of real feedback."*

3. **Persona disagreement is a quality signal (HCI Q5.2).** Inter-persona agreement is measured on top-concern coding; if all four personas (Curator, Practitioner, Theorist, Devil's Advocate) raise the same concern, the plugin flags *"panel collapse — personas have converged on a single voice, indicating the rehearsal has lost its diversity. Try changing the Brief or restarting."*

4. **Rehearsal outputs are structurally re-entrant into the Brief.** The Methodologist's Q5 prescription — that rehearsal critique should be *material to be processed*, not *judgement to be received* — is enforced by making the rehearsal output a list of *prompts back into `brief`*, not a list of evaluative scores. Each rehearsal critique line is paired with: *"Re-enter Brief field X with this concern."*

5. **The four personas are still:** Curator + Practitioner-peer + Theorist + Devil's Advocate. v0.2 keeps the count at four (per the v0.1 OQ3 default). Custom personas remain v0.2-deferred.

#### `full` — long-running project tracker, not single-session pipeline

**What it changes.** The Practicing Artist's Scenario A and Q8 ("real ideation takes weeks to months") and the Methodologist's Smith & Dean iterative-cyclic-web compliance (Q5 full) converge on the same prescription: `full` mode is *not* a single-session pipeline.

The v0.2 reshape:

1. **`full` opens a *project file*, not a session.** The artist's `art-project` work is now persistent across sessions. Each invocation of any mode appends to the project file. The user can return weeks or months later and continue.
2. **Each session does one mode at most.** The v0.1 chain (socratic → provoke → lineage → brief → rehearsal in one session) is abandoned. A typical project file evolves: socratic-session-1, socratic-session-2 (a week later), provoke-session-1, lineage-session-1 (with artist's candidates), brief-draft-1, rehearsal-1, brief-draft-2, etc. The Smith & Dean (2009) iterative cyclic web is now the *actual* shape.
3. **Cross-session re-entry is a first-class mode.** The "Re-entry mode" the Practicing Artist proposed is built into `full`: re-opening the project file shows the prior state and asks where to resume.
4. **The Material Passport machinery inherited from ARS is repurposed here** as the project-file schema (no longer used for single-session pipeline orchestration, since there is no longer a pipeline).

This brings the plugin into alignment with how PaR ideation actually proceeds, and turns the v0.1 OQ2 / OQ5 (cross-session continuity, bridge schema to art-paper) into the *primary* design surface.

### 2.3 Tradition tags (renamed from "methodology provenance") + Authentic Practice Boundaries

Per HCI Q4 and Practicing Artist Q3, the term **"methodology provenance"** is dropped and replaced with **"tradition tag"** throughout the plugin, documentation, and paper. The rationale is the HCI critique's most honest single observation: what v0.1 called "provenance" is *not* a causal trace of how the LLM generated the output — it is metadata about which entries in the methodology reference were loaded into the prompt. The label indicates *prompt grounding and stylistic affinity*, not generation cause.

**Honesty paragraph (this exact text, or close to it, appears in `art_ideation_methodology.md` opening, in `POSITIONING.md`, and in the paper):**

> "Tradition tags indicate which entries in the methodology reference were loaded into the prompt that produced an output. They do not claim causal attribution — the LLM's actual generation mechanism is opaque. A tag is a *prompt-grounding* and *style-affinity* claim: this output aims to operate in the tradition named, and was conditioned by it; whether it succeeds in that aim is for the artist to judge, and the artist is encouraged to read the named primary source to deepen the engagement."

**Authentic Practice Boundaries** are added per cited method — Practicing Artist Q3's "Authentic Practice Boundary" prescription. Each tradition tag carries a sub-field naming the part of the cited method that the plugin **does not simulate** and defers to human execution:

- **Eno & Schmidt's Oblique Strategies (1975).** Boundary: the plugin proposes Oblique-style provocations but cannot replicate the *physical, finite, blindly-drawn* character of the deck. The artist is encouraged to obtain the actual deck for serious use; the plugin's provocations are at most *Oblique-affine*.
- **Cage's chance operations.** Boundary: the plugin can describe and suggest chance methods (I Ching, coin toss, etc.) but **does not execute them**. The artist throws the dice. Cage's epistemic point is that the *artist's time* spent performing the procedure is part of the work; an LLM-generated "chance result" would void that.
- **LeWitt's instruction-based work (1967, "Paragraphs on Conceptual Art"; 1969, "Sentences on Conceptual Art").** Boundary: the plugin can *prompt the artist to write instructions* but **does not author instructions for the artist**. LeWitt's "the idea is the machine that makes the art" requires the artist to be the rule-setter; a plugin that writes the rule occupies the position LeWitt's framework reserved for the artist.
- **Bogart's Viewpoints (1995).** Boundary: the plugin can ask Viewpoints-derived questions about the *intended encounter* but cannot perform Viewpoints work, which is bodied, ensemble-based, and temporal.
- **SCAMPER (Eberle 1971).** Boundary: per Christensen & Schunn (2007 — verify exact citation) and others, SCAMPER's empirical efficacy in designer cognition is contested. The tag is for *style affinity*, not a claim that SCAMPER-tagged provocations are demonstrably more effective. Critical-literature note added to the reference layer entry.
- **Bauhaus Vorkurs.** Boundary: the plugin can describe Vorkurs-style exercises but cannot replicate the *material studio* in which they were taught. Tag denotes pedagogical affinity, not method execution.
- **Practice-based research literature (Frayling, Borgdorff, Sullivan, Smith & Dean, Barrett & Bolt).** Boundary: the plugin is itself a *tool* (research FOR) and a *synthesis* (research INTO) within this literature; it does not perform PaR (research THROUGH would require artistic practice). This is the §1.2 layered hybrid in operational form.

The Authentic Practice Boundary table is the operational form of Critique-3's strongest contribution: it makes the *limits* of the tradition tags visible, which strengthens the academic standing of the entire reference architecture.

### 2.4 Default routing and mode-transparency

Per Practicing Artist Q2, the slash-command mode-selection burden is mostly removed. The user can:

- invoke a specific mode via slash (`/art-project:socratic`, `/art-project:provoke`, etc.) when they know what they want, or
- start a natural-language session ("I want to think through a new project") and let the plugin auto-route via intent detection.

When auto-routing, the plugin **announces the routing decision transparently**: *"Starting in socratic mode (exploratory intent detected). I'll suggest switching modes when the dialogue suggests it."* Mode transitions are similarly announced: *"Your impulse has stabilized; would you like to move to provoke or lineage, or continue exploring?"*

Mode-switching becomes a transparent *suggestion* from the plugin, never a hidden state change. This addresses HCI's "what is the system doing?" transparency requirement and Practicing Artist's "I shouldn't have to know what mode I need" usability requirement simultaneously.

---

## 3. Reference layer — what changes (revised)

The methodology reference document (`shared/references/art_ideation_methodology.md`) is restructured per the Methodologist Q4 four-point prescription and the Devil's Advocate Attack 2 sub-attacks. Specific revisions (the actual document changes are made in a separate commit to that file):

1. **Opening positionality paragraph** (new). Names the author's situation (Korean researcher, dual artist/AI-researcher position; sources read primarily in English and Korean; East-Asian classical sources via Korean Joseon-period reception and translated Sino-Korean materials, not directly from contemporary Sinology), the rationale for the document's structure, and the deliberate decision-points (e.g., whether E is integrated or separate — see point 5).
2. **"Contested in" field per entry** (new). Each methodology entry gains a field naming a counter-position or contested reading where one exists in the literature. Examples added in v0.2:
   - A1 Boden: Glăveanu (2010, "Paradigms in the Study of Creativity", *Review of General Psychology* 14(1) — verify) critique of trait-property creativity.
   - B2 SCAMPER: Christensen & Schunn (2007 — verify) on SCAMPER's contested empirical efficacy.
   - C3 Frayling: Scrivener critique of the FOR category as ill-defined (verify).
   - D1 Manovich: Galloway (2012, *The Interface Effect*) contests the database-as-symbolic-form thesis.
3. **"Tensions" section** (new, between Meta-observation and Mounting Matrix). Names 4–6 inter-entry conflicts the reference layer holds without flattening:
   - Boden's formalism (A1) vs Borgdorff's situatedness (C4) — whether ideation is a search-space operation or a not-yet-knowing.
   - IDEO Design Thinking (B1) vs Sullivan/Barrett & Bolt (C5, C7) — instrumental vs epistemic framing.
   - Cage's chance-as-erasure-of-taste (C11) vs Bogart's Viewpoints-as-trained-attention (C8).
   - Galanter's effective-complexity criterion (D4) vs LeWitt's idea-first (C2).
   - Western PaR's articulation requirement (Frayling/Borgdorff/Sullivan) vs East-Asian yi/qi/yeobaek's reserve-for-the-unsaid (E2).
   - Methodology-provenance-as-affinity-tag (this plugin's claim) vs traditional methodology-as-embodied-craft (the Practicing-Artist Q3 attack).
4. **5+1 mechanisms justified** (revision). The Methodologist's Q4 prescription: convert "we noticed these" into either (a) explicit inductive coding (each entry coded on dimensions X/Y/Z; the five mechanisms are emergent clusters), or (b) anchor to a prior framework (Sawyer 2012; Glăveanu's 5A — actor/action/artifact/audience/affordance). v0.2 takes option (a) and adds a coding table as an appendix to the reference document.
5. **East-Asian section reshaped.** Two changes:
   - Section E gets an opening positionality paragraph (per point 1) explicitly addressing the centre/periphery framing question.
   - E is **expanded from 3 to 5–7 verified entries** per Practicing Artist Q7. Targets for verification (the actual verification work follows in a separate task, with library work + consultation with Korean media-art curators):
     * Nam June Paik Art Center research catalogues (verify specific entries)
     * Kim Hong-hee (김홍희) on Korean media-art curation (verify specific titles)
     * Yuk Hui (許煜), *The Question Concerning Technology in China* (2016), on cosmotechnics — already strongly precedent for the East-Asian-AI-art discussion
     * Lee Yongwoo (이용우) on Korean contemporary art (verify)
     * 1990s–2000s Korean media-art lineage (Forum A, early Gwangju Biennale Korean artists; specific names pending verification)
     * Korean academic journal sources (*현대미술학논문집* and adjacent; verify specific issues)
   - Long-term aspiration: contributing Korean media-art curator/scholar as named reference-layer co-author (Practicing Artist Q7), which would simultaneously strengthen the authority and remove the single-author positionality problem.
6. **Restored critical edge on D6/D8, C6/C7.** v0.1 sanitized Penny (D8), Barrett & Bolt (C7), Borgdorff (C4), Smith & Dean (C6) by stripping their critical force (Devil's Advocate Attack 1 substantive finding). v0.2 restores the critique: these entries explicitly say *what they argue against*, which includes — in Penny's case — exactly the representational-paradigm framework the plugin's LLM substrate implements. This is uncomfortable to keep but methodologically essential: the plugin must cite the critique that targets it, and respond to it (which §1.1 reframe does).
7. **HCI prior-art subsection added** (new section in reference layer or in the paper's related-work — see §4). Positions art-project in the LLM-creativity-tools landscape:
   - Wordcraft (Yuan et al. 2022, IUI) — writer-assist LLM with attribution.
   - Sparks (Gero et al. 2022, DIS) — LLM-generated spark sentences for scientific writing; attribution-UI tested.
   - TaleBrush (Chung et al. 2022, CHI) — sketch-controlled LLM story generation.
   - Dramatron (Mirowski et al. 2023, CHI) — hierarchical LLM theatre scripts.
   - AI Chains (Wu et al. 2022, CHI) — chained-prompt LLM tasks.
   - Frich et al. (2019, CHI) — CST landscape map.
   - Shneiderman (2007, CACM) — CST design principles.
   - Cherry & Latulipe (2014, TOCHI) — Creativity Support Index.
   - Compton & Mateas (2015, ICCC) — Casual Creators / possibility-space framing.
   - Davis et al. (2016, IUI) — co-creative cognitive agent.
   - Kantosalo & Toivonen (2016, ICCC) — alternating vs task-divided co-creativity.
   - Deterding et al. (2017, CHI workshop) — Mixed-Initiative Creative Interfaces.
   - Draxler et al. (2024, TOCHI — verify) — AI ghostwriter effect on perceived authorship.

   These are the **killer prior-art citations** from HCI Critique. v0.1 had none of them.

---

## 4. Academic contribution and venue path

Following Methodologist Q6 (best contribution claim) and HCI Q7 (venue path), v0.2 commits to a specific contribution claim and a specific publication path.

### 4.1 The contribution claim (single sentence + four sub-claims)

> **art-project v0.1 demonstrates that an LLM-based pre-studio articulation scaffold for practice-based artistic research can be architected to encode specific PaR commitments — generation-evaluation separation, tension-over-ranking, lineage-with-opposition, formative self-critique rehearsal — and that the architectural choices themselves constitute the propositional contribution, supported by an executable tradition-tag reference layer drawn from the prior literature on artistic ideation.**

The four sub-claims (each is independently defensible):

- **Claim A — Methodological contribution.** An executable tradition-tag reference layer encoding prior research on artistic ideation (Boden, Geneplore, Frayling, Borgdorff, Sullivan, Smith & Dean, Barrett & Bolt, Cage, Eno, LeWitt, Bogart, Bauhaus, Manovich, Reas/Fry, Whitelaw, Galanter, Paul, Penny, Dunne & Raby, plus East-Asian entries) can be constructed such that each prompt carries declared style-affinity to a named tradition, each tradition carries an Authentic Practice Boundary, and ideation modes wire to specific entries by mechanism. The schema is the contribution; the plugin is its proof-of-instance.

- **Claim B — Design-research contribution.** AI-assisted pre-studio articulation can be architected to encode specific PaR commitments. Five architectural choices and their literature anchors: (i) generation-evaluation separation → Geneplore (Finke, Ward & Smith 1992); (ii) tension-over-ranking → Bolt (2007, experimental gesture); (iii) lineage-with-opposition → Sullivan (2010, contextualist inquiry); (iv) formative self-critique-rehearsal, not decisional panel → Borgdorff (2011, 2012, not-yet-knowing); (v) tradition-tag-with-boundary → addresses the Penny/Ingold critique by declaring the plugin's non-participation in embodied practice. These are propositional contributions, not implementation details.

- **Claim C — Epistemological contribution.** A pre-studio articulation scaffold can occupy the *cognitive scaffold* position (Clark & Chalmers 1998; Malafouris 2013; Penny 2017) — neither inert tool nor co-author — and this position is operationalizable through tradition-tag attribution, intent-detection, refusal-to-rank, mandatory bias disclosure, and architectural friction against simulacrum-of-critique misuse.

- **Claim D — Negative / boundary claim.** The pre-studio articulation phase of practice-based art research is structurally distinct from downstream phases (making, exhibiting, writing-up). Its primary material is the artist's pull, refusals, and chosen lineage — not artwork-as-evidence. AI assistance designed for this phase therefore requires a different evidence model, evaluation logic, and tradition-tag discipline than downstream AI tools (image generation, paper-writing, documentation). The plugin is a worked example of that distinct design space.

### 4.2 Venue path (committed — revised 2026-05-25)

> **Revision note (2026-05-25):** The original v0.2 venue path put ACM C&C 2027 first, gated on a Study 1 (N=12 CSI / NASA-TLX) pilot. The maintainer has decided to defer empirical evaluation and pursue **Aslib JIM as a Conceptual paper** as the **first publication** instead. Rationale: (a) the v0.2 Claims A–D are all *conceptual / design-research* claims that do not require empirical evaluation to be defensible (per Borgdorff's dual-discourse criterion, criticisability is satisfied by argument viability + provenance traceability, not necessarily by user-study data); (b) Aslib JIM explicitly accepts *Conceptual paper*, *Viewpoint*, and *Technical paper* categories without empirical requirement; (c) timing — Aslib JIM submission is feasible immediately (weeks), whereas the C&C path requires 4–7 months for pilot + analysis. The C&C / *Digital Creativity* / JAR / *Leonardo* path is retained as v0.2 / v0.3 work, sequenced *after* the conceptual paper has established the framework.

**Revised publication path:**

1. **First publication: *Aslib Journal of Information Management (Aslib JIM)*** — Emerald Publishing. **Conceptual paper** classification (4,000–10,000 words; the journal accepts Research / Viewpoint / Technical / **Conceptual** / Case study / Literature review / General review). Frame as: *"A tradition-grounded scaffold for pre-studio articulation in practice-based artistic research: architecture, design rationale, and methodological commitments."*
   - **Why Aslib JIM is a defensible fit:** the journal's scope includes scholarly-communication tooling, research-methodology contributions, AI in research workflows, and digital-humanities methods — all of which the executable tradition-tag reference layer (Claim A) and the design-research-as-PaR-commitment-encoding argument (Claim B) sit cleanly inside. The journal has published on AI-assisted research workflows (verify recent issues for direct precedent — pending library check).
   - **Reframing for the Aslib JIM readership:** PaR vocabulary (Frayling / Borgdorff / Sullivan) is *preserved* in the body but the title and abstract foreground the **research-methodology** contribution rather than the artistic-research one. Working title candidates:
     - "Tradition-tagged AI scaffolding for pre-studio articulation in practice-based artistic research: a conceptual framework"
     - "When AI cannot participate: designing cognitive scaffolds for the propositional-articulation phase of artistic research"
     - "Authentic practice boundaries: a model-card-style discipline for AI tools that cite methodologies they cannot perform"
   - **Submission risk:** Aslib JIM's reviewer pool may have fewer PaR specialists than the eventual JAR / C&C audience. Claim B (architectural choices as PaR commitments) is the most exposed to under-recognition. Mitigation: develop Claim B with information-science vocabulary as well (provenance metadata schema; controlled-vocabulary integration; scholarly-tool architecture pattern) so the contribution registers in two registers simultaneously.

2. **Parallel sibling: *Digital Creativity (Routledge / T&F)*** — methods paper, ~7,000 words. Frame as: *"An executable tradition-grounded reference layer for AI-assisted articulation in practice-based art research."* Foregrounds Claim A + Claim D. *Digital Creativity* has the right reviewer pool (Boden & Edmonds 2009 published there) for the creativity-research framing the Aslib JIM submission underweights. Submission timing: after Aslib JIM is in review (avoid simultaneous-submission conflicts; check both journals' policies).

3. **JAR sibling: *Journal for Artistic Research*** — as an **exposition** rather than a traditional article. The plugin + the methodology reference + the design choices become a navigable exposition; the reader engages the artifact directly. Best done after the Aslib JIM + Digital Creativity publications establish the conceptual framework that the JAR exposition then *demonstrates* rather than has to *argue*.

4. **Empirical / artist-facing track (v0.2 / v0.3 work, deferred):** *ACM Creativity & Cognition 2027 or 2028*, *Leonardo*, *ISEA*, *SIGGRAPH Art Papers*. These require Study 1 (CSI + NASA-TLX pilot, §5.1) and the longitudinal artist study (§5.2). Sequenced *after* the conceptual paper establishes the framework, so the empirical paper can cite the conceptual paper as the framework being tested. This is the *intended* path: Conceptual framework → empirical validation, not the reverse.

**Not pursued at all in v0.1 series:** CHI full paper (requires the full HCI evaluation suite — Studies 1+2+3 — which is v0.2 work at the earliest); ICCC full paper (overlaps too much with C&C; choose one when the empirical track activates).

### 4.3 Companion paper outline — Aslib JIM Conceptual paper (revised 2026-05-25)

Aslib JIM Conceptual paper structural requirements (per the journal's author guide, in `art-project_paper/guideForAuthor.md` — verify against current online version):

- **Length:** 4,000–10,000 words (body + abstract + refs + tables + figures + appendices; tables / figures count as ~250 words each).
- **Structured abstract:** ≤250 words, four sub-headings: **Purpose / Design (methodology / approach) / Findings / Originality**.
- **Keywords:** ≤12.
- **Article classification:** one selected — **Conceptual paper**.
- **Anonymized for review:** no author identifiers; no "our previous work" formulations.
- **Tables numbered Roman (I, II, …); figures numbered Arabic (1, 2, …).**
- **References:** Harvard / agsm style (per the working manuscript's existing `references.bib`).

**Outline (target ~8,000 words body):**

1. **Introduction** (~1,000 w). The pre-studio articulation problem in practice-based artistic research. Why this phase is structurally distinct from downstream paper-authoring / making (Claim D). Why existing AI tools — image generators, writing assistants, paper-writing pipelines — do not address this phase. Statement of contribution (Claims A + B + C + D in one paragraph). Roadmap for the paper.

2. **Related work** (~1,500 w). Four strands:
   - **Practice-based artistic research methodology** — Frayling (1993), Borgdorff (2011, 2012), Sullivan (2010), Smith & Dean (2009), Barrett & Bolt (2007).
   - **AI-assisted creativity-support tools (CST)** — Shneiderman (2007), Cherry & Latulipe (2014), Frich et al. (2019), Wordcraft, Sparks, TaleBrush, Dramatron, AI Chains, Casual Creators (Compton & Mateas 2015), Davis et al. (2016) on co-creativity.
   - **Extended cognition / cognitive scaffolds** — Clark & Chalmers (1998), Malafouris (2013), Penny (2017).
   - **Critical AI literature on artistic practice** — Ingold (2013), Penny (2017), Borgdorff's dual-discourse position. The paper *engages* this literature head-on; it does not bypass.

3. **The pre-studio articulation problem and the Frayling layered hybrid** (~1,200 w). §1.1–§1.4 of this spec. The single most consequential reframe: ideation engine → articulation scaffold. The user-asymmetry scope statement. The Frayling layered hybrid self-positioning. The cognitive-scaffold framing as the defensible middle position between inert tool and co-author.

4. **System architecture: six modes and the tradition-tag reference layer** (~1,800 w). §2 + §3 of this spec. Compress the six modes into one table + one paragraph each; expand the tradition-tag + Authentic Practice Boundary discipline (§2.3) as the load-bearing architectural contribution. Tradition-tag-not-provenance honesty paragraph in full.

5. **Design choices as PaR commitments** (~1,200 w). Claim B in full. Five architectural choices, each anchored to its PaR literature:
   - generation-evaluation separation → Geneplore + Corita Kent
   - tension-over-ranking → Bolt's experimental gesture
   - lineage-with-opposition → Sullivan's contextualist inquiry
   - formative self-critique rehearsal → Borgdorff's not-yet-knowing
   - tradition-tag-with-Authentic-Practice-Boundary → the design's response to the Penny / Ingold category-error attack

6. **Measured-harm disclosure (model-card style)** (~800 w). §6 of this spec. The six harm classes, named and disclosed: lineage hallucination, training-data canon bias, simulation-pedagogy risk, authorship-perception shift, conviviality risk, bounded user population. Cite Mitchell et al. (2019) Model Cards + Bender et al. (2021) Stochastic Parrots as the methodological precedent.

7. **Discussion: the four claims and the conceptual contribution** (~1,000 w). Reprise Claims A–D. What the v0.1 plugin demonstrates and what it explicitly defers. The contestability of the cognitive-scaffold position (acknowledged, not papered over). The conviviality question (Illich / Turkle / Hui) named as a critique the framework must answer to.

8. **Limitations and future work** (~500 w). Empirical evaluation deferred — Studies 1–4 and the longitudinal artist study (§5) are *future work* the conceptual paper *invites* rather than performs. Reviewers can engage the framework on its conceptual merits; empirical adequacy is a downstream question for ACM C&C 2027/2028 + *Leonardo* / *ISEA*. Other limitations: East-Asian section under-development (E4–E7 pending); agent prompt rewrites pending v0.2 implementation; runtime grounding for lineage entries deferred to v0.2.

**Structured abstract draft** (≤250 words):

- **Purpose** — Articulate a conceptual framework for AI-assisted **pre-studio articulation** in practice-based artistic research (PaR): the propositional work surrounding artistic ideation, distinct from artistic ideation itself.
- **Design / methodology / approach** — Design-research synthesis of (i) PaR methodological literature (Frayling 1993; Borgdorff 2011, 2012; Sullivan 2010; Smith & Dean 2009; Barrett & Bolt 2007; Penny 2017); (ii) AI-creativity-support-tool literature (Shneiderman 2007; Cherry & Latulipe 2014; Frich et al. 2019; LLM-creativity tools — Wordcraft, Sparks, Dramatron); (iii) extended-cognition philosophy (Clark & Chalmers 1998; Malafouris 2013). Validated through a four-agent design critique addressing the strongest attacks on the premise. Demonstrated through an open-source Claude Code plugin (art-project) as a worked example.
- **Findings** — (1) An executable tradition-tag reference layer encoding 25+ prior ideation methodologies can be architected such that each prompt carries declared style-affinity, each tradition carries an Authentic Practice Boundary, and modes wire to entries by mechanism. (2) Five architectural choices (generation-evaluation separation; tension-over-ranking; lineage-with-opposition; formative self-critique rehearsal; tradition-tag-with-Authentic-Practice-Boundary) operationalize specific PaR commitments. (3) A cognitive-scaffold position is operationalizable through provenance tagging, intent detection, refusal-to-rank, and architectural friction against simulacrum-of-critique misuse. (4) The pre-studio articulation phase is structurally distinct from downstream PaR phases and requires a different AI-assistance evidence model.
- **Originality** — First system-level synthesis of PaR ideation methodology + AI-CST design + extended cognition into an *executable* reference layer. Introduces the **Authentic Practice Boundary** discipline as a response to the methodology-citation-as-rhetorical-legitimation critique. Names the **pre-studio articulation phase** as a distinct PaR design space.

**Keywords (≤12 candidates):** practice-based research; artistic research; pre-studio articulation; cognitive scaffold; extended mind; AI-assisted methodology; tradition tag; provenance metadata; creativity support tools; large language models; design research; research methodology.

---

## 5. Evaluation protocol (future work — empirical track, deferred from v0.1 conceptual publication)

> **Revision note (2026-05-25):** The v0.1 publication target moves from ACM C&C 2027 (empirical) to *Aslib JIM* Conceptual paper (no empirical requirement) — see §4.2. Study 1 is therefore **no longer the v0.1 gate**; it becomes the **first deliverable of the empirical track**, which is now sequenced *after* the conceptual paper has established the framework being tested. This protocol section is retained as the empirical-track plan, not as a v0.1 blocker.

Following HCI Q2 prescription + Practicing Artist Q8 ("3–5 artists × 6 weeks longitudinal") + Methodologist Q7 ("where is the artist?" reviewer attack). Study 1 is the first step of the empirical track; the longitudinal artist study runs in parallel.

### 5.1 Study 1 — Pilot CSI + NASA-TLX (first empirical-track deliverable; v0.2 / v0.3 work)

- **N = 12** practicing artists (target distribution: 4 generative/code-based; 4 sculptural/installation; 4 mixed-media; recruited via MFA programs + ISEA networks; minimum 3 years practice; 4 must be Korean-first artists to test bilingual claim).
- **Design:** within-subjects, 2 conditions × counterbalanced order, 45 min each, 60 min combined interview + Brief-rating.
  - **Condition A — art-project** (`socratic` + `provoke` + `brief` modes).
  - **Condition B — baseline:** Claude (no plugin) + physical Oblique Strategies deck (where applicable) + open web.
- **Task:** Each artist arrives with a vague impulse for a real upcoming project. Each condition: produce a one-page Concept Brief.
- **Measures:**
  - **CSI** (Cherry & Latulipe 2014) — adapted: Expressiveness reframed to "the tool let me articulate the work I want to make"; Collaboration scored zero (single-user); other factors unchanged.
  - **NASA-TLX** — secondary measure, especially for `rehearsal` mode if used.
  - **Open interview** (30 min): "What did each tool make easier / harder?" "Where did each tool flatten your thinking?" "Would you use this in your studio?" "Did either tool surface a precedent or angle you didn't have before?" "Did either tool feel like it was *replacing* your thinking?"
  - **Brief-quality micro-rating**: each artist rates their own two briefs on five 7-point Likert items (specificity, conceptual coherence, lineage situatedness, voice-authenticity, would-submit-as-is).
- **Analysis:** CSI factor means with paired-sample tests; NASA-TLX descriptive; thematic analysis of interviews (Braun & Clarke 2006); paired-sample brief-quality comparison.
- **Pre-registration:** OSF, before recruitment begins.
- **Reproducibility:** all evaluation runs use Claude API with `temperature=0.7, seed=42`; artist-facing default elsewhere is `temperature=0.9, no seed`. Full prompt set + reference-layer state at evaluation time is versioned and archived.

### 5.2 Studies 2–4 (deferred to v0.2 with the artist longitudinal in parallel)

- **Study 2 — Concept Brief CAT-rating.** 5 expert raters score N=24 briefs from Study 1 on creativity, conceptual coherence, lineage situatedness, voice authenticity, feasibility. Inter-rater alpha target ≥0.7.
- **Study 3 — Attribution UI / Tradition tag salience.** N=30 between-subjects, 3 conditions (no tags / footnote tags / inline tags). Measures: Brief delta + Sparks-style ownership questionnaire + think-aloud.
- **Study 4 — `provoke` mode calibration.** Held-out 50 human-generated provocations; have raters score on novelty + usefulness; compare to plugin output distribution.
- **Longitudinal artist study (parallel).** 5 artists × 6 weeks of free use, weekly 30-min interviews. Practicing Artist Q8 prescription. Diary-style data. This is the *artist-side* validity check that protects against Devil's Advocate Attack 5 ("paper artifact, not artist tool").

### 5.3 Honesty about what v0.1 conceptual paper does and does not evaluate (revised 2026-05-25)

The Aslib JIM Conceptual paper will state explicitly in its Limitations section:

> "This paper presents a conceptual framework and a worked-example artifact (the art-project plugin v0.1). It does not perform empirical user-study evaluation; the framework's adequacy is argued on (i) defensibility of the architectural choices against the cited PaR and CST literature, (ii) coherence of the tradition-tag + Authentic Practice Boundary discipline as a response to the Penny / Ingold category-error attack, and (iii) traceability of the design decisions to the four-agent design critique (transcript available as supplementary material). Empirical evaluation — Study 1 (within-subjects CSI + NASA-TLX pilot, N=12); Study 2 (CAT-rated brief quality); Study 3 (attribution-UI between-subjects); Study 4 (provoke-mode calibration); plus a 6-week longitudinal artist study — is sequenced as the next phase of work (cf. §5 of the synthesis design spec, available as supplementary material). The conceptual paper is the framework that the empirical phase tests; per Borgdorff's (2011) dual-discourse criterion, the framework's criticisability is satisfied here by argument viability + provenance traceability, with empirical accumulability following downstream."

This pre-empts the "where is the artist?" reviewer attack at Aslib JIM in a different way than the v0.2 original framing anticipated for ACM C&C: the answer is *"this is a conceptual paper; the framework is the contribution; empirical adequacy is downstream work the framework explicitly invites"*. Acknowledging the bound is more publishable at a conceptual-paper-accepting venue than papering over it.

---

## 6. Measured-harm disclosure (new section, model-card style)

Following Devil's Advocate Reframe 3 + Bender et al. (2021, "On the Dangers of Stochastic Parrots", FAccT) + Mitchell et al. (2019, "Model Cards for Model Reporting", FAccT). v0.1 ships with a measured-harm disclosure document — a section in `POSITIONING.md`, a paragraph in the paper, and a tracked-issues list in the repo.

The six harm classes the plugin tracks and discloses:

### 6.1 Lineage hallucination (per-domain measured rate)

The plugin must measure and disclose:

- For at least 3 sub-domains (anglophone media art / Korean media art / performance art — others optionally), the empirical rate at which plugin-generated lineage entries fail verification against a domain expert or against Wikidata / ULAN / e-flux / Nam June Paik Art Center catalogues.
- v0.1 target: **report measured rates**, not necessarily achieve a threshold. Honest measurement is publishable; suppressed measurement is not.
- v0.2 architectural mitigation: runtime grounding against Wikidata / ULAN / e-flux for any lineage entity emitted. If confidence is low, emit no entry rather than a hedged entry.

### 6.2 Training-data canon bias

The plugin's training-data clustering is biased toward anglophone, well-funded, well-documented venues (Ars Electronica, ZKM, SIGGRAPH, Whitney, MIT, Tate). The `lineage` mode's bias disclosure (§2.2 point 2) is the *operational* form. The model-card-style disclosure quantifies it where possible:

- For a fixed test set of 20 ambiguous impulses, what fraction of `lineage` outputs cite only anglophone sources?
- For Korean-language inputs, what fraction cite at least one Korean source after the v0.2 East-Asian-default routing?

These rates are reported.

### 6.3 Simulation-pedagogy harm (rehearsal mode)

Following Devil's Advocate Attack 4 + Schön (1983) — extended risk that rehearsing on a simulacrum trains either defensiveness or over-compliance when facing real critics. v0.1's mitigations:

- Mandatory disclaimer (§2.2 `rehearsal`).
- Architectural friction (warn after 2 rehearsals/14 days on same concept).
- Inter-persona-agreement gate (flag panel collapse).
- v0.1 *cannot* measure the long-term effect of rehearsal use on artists' real-critique reception; this is a v0.2/v0.3 longitudinal question. The disclosure says so.

### 6.4 Authorship-perception shift (Wordcraft / Sparks / ghostwriter)

Following HCI Q4 and Draxler et al. (2024 — verify): users may perceive AI-assisted articulation as less their own (the ghostwriter effect) or — paradoxically — *more* their own when attribution is hidden. v0.1's mitigations:

- Tradition tags default to footnote-level salience (HCI Q4.1 prescription); inline tag mode is opt-in (e.g. for teaching).
- The honesty paragraph (§2.3) clarifies that tags are *prompt-grounding*, not generation cause.
- The `brief` stay-rough default reduces the polish-induced ghostwriter effect.

### 6.5 Conviviality / normalization risk (Illich, Turkle, Hui)

Following Devil's Advocate Attack 7 + Illich (1973, *Tools for Conviviality*) + Turkle (2015, *Reclaiming Conversation*) + Hui (2016, *The Question Concerning Technology in China*). The plugin's existence contributes to the normalization of LLM-mediation in cognitive domains where the mediation was historically absent. v0.1 takes the *contestable but defensible* position that:

- The plugin's architectural commitments to artist autonomy (refusal-to-rank, formative-not-decisional, intent-classified Socratic, IRON RULE on human decision, opt-out on lineage) place it on the convivial side of Illich's line — but this is the position to be argued, not a fact.
- The plugin **does not** include a use-frequency limit or taper protocol in v0.1 (which Devil's Advocate proposed). The disclosure says so and treats it as v0.2 design question OQ8 (open question, see §8).

### 6.6 Bounded user population

Per §1.4 scope statement: the plugin is for artists for whom propositional articulation is a bottleneck. For artists outside that population — particularly fluent artist-writers with established practices, traditions where articulation is constitutively unwanted (improvisational, ritual, oral) — the plugin is structurally unsuitable. The disclosure names this and does not market beyond it.

---

## 7. What changes in repo state vs. v0.1 pivot spec

| File | v0.1 status | v0.2 action |
|---|---|---|
| `docs/design/2026-05-24-art-project-v0.1-pivot-spec.md` | created | mark as *superseded by v0.2 on Sections §1, §3 mode design, §6 contribution, §7 phase plan, §8 OQs*; keep for provenance |
| `docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md` | — | new; this document |
| `shared/references/art_ideation_methodology.md` | created (catalog form) | rewrite per §3: positionality, contested-in fields, Tensions section, 5+1 justification, expand E to 5–7 entries, restore critical edge on D6/D8/C6/C7, add HCI prior-art subsection |
| `POSITIONING.md` | created (ideation-engine frame) | rewrite for pre-studio-articulation-scaffold frame; add cognitive-scaffold position; add user-asymmetry scope; add measured-harm summary |
| `MODE_REGISTRY.md` | created (6 modes, `panel`) | update: rename `panel` → `rehearsal`; update mode descriptions per §2.2; update tradition-tag wiring |
| `.claude-plugin/plugin.json`, `marketplace.json` | created | minor: update description to reflect pre-studio-articulation framing; keep name `art-project` |
| `commands/` | not yet rewritten | follow §2.4 — `art-socratic`, `art-provoke`, `art-lineage`, `art-brief`, `art-rehearsal`, `art-ideate` (full mode) |
| `art-paper/`, `art-reviewer/`, `art-pipeline/`, `art-project_paper/` skill dirs | still present | unchanged — physical deletion deferred until v0.2 implementation phase begins (this spec is design; not yet implementation) |
| `art-inquiry/` skill dir | still present | rename to `art-ideation/` deferred until implementation phase |

Implementation phases (revised 2026-05-25 — conceptual paper sequenced *before* empirical evaluation):

- **Phase 0b** (committed 2026-05-24): v0.2 synthesis spec + reference-layer rewrite + POSITIONING / MODE_REGISTRY updates. ✅
- **Phase 1**: drop paper-scoped reference files; expand methodology reference E section with verified Korean / East-Asian sources. *Partial — drops complete; E expansion pending library + consultation work.*
- **Phase 2**: drop paper-authoring skill dirs; drop 15 paper commands; rename `art-inquiry/` → `art-ideation/`. ✅
- **Phase 3**: rewrite `art-ideation/SKILL.md` for six v0.2 modes; create 6 new commands. *SKILL.md + commands complete.* Agent-prompt rewrites for Authentic Practice Boundary enforcement + `full` mode project-file persistence pending v0.2 implementation work.
- **Phase 4**: README / QUICKSTART / CLAUDE.md / CHANGELOG rewrite. ✅
- **Phase 5 — Conceptual paper (Aslib JIM)** *(new sequencing per 2026-05-25 revision; was empirical pilot before)*: draft the Aslib JIM Conceptual paper per §4.3 outline using the existing LaTeX skeleton at `art-project_paper/`. Structured abstract + 6 sections + Harvard / agsm refs. Target: submission to Aslib JIM within weeks of this revision. **This is the v0.1 publication.**
- **Phase 6 — Aslib JIM revisions + parallel *Digital Creativity* draft**: respond to Aslib JIM reviews; in parallel draft the *Digital Creativity* sibling paper (~7,000 w) that foregrounds Claim A + Claim D for the creativity-research readership.
- **Phase 7 — Empirical track activation** *(begins after Aslib JIM submission, in parallel with Phase 6)*: Study 1 design + OSF pre-registration + IRB; recruit N=12; run pilot. Output: ACM C&C 2027 / 2028 submission.
- **Phase 8** — JAR exposition (after Phase 5 published).
- **Phase 9** — Studies 2–4 + 6-week longitudinal artist study. Output: *Leonardo* / *ISEA* / *SIGGRAPH Art Papers* practitioner-facing paper.

> **Rationale for the resequencing (vs. the v0.2-original empirical-first path):** Aslib JIM Conceptual paper accepts the framework on its conceptual merits without empirical data; submitting now establishes the framework that the eventual empirical paper (Phase 7) then tests. The reverse ordering (empirical first, then conceptual) would have required maintaining a published-but-unargued framework as supplementary material to an empirical paper, which is structurally weaker. The conceptual-first sequencing also dissolves the 4–7-month delay that the empirical-first path imposed before any publication exists.

---

## 8. Open questions (revised; supersede v0.1 OQ list)

- **OQ1 — License.** Keep CC-BY-NC 4.0 (default unchanged from v0.1 OQ1).
- **OQ2 — Methodology reference as user-facing primer.** Decision: keep in `shared/references/` but link prominently from README and from the paper. The reference layer is structurally a *reference*, not a primer — making it user-facing risks turning it into a textbook and losing the executable-affordance contribution. Closed as decided.
- **OQ3 — Custom panel personas.** Closed: v0.1 four personas (Curator, Practitioner, Theorist, Devil's Advocate); v0.2 may add user-supplied.
- **OQ4 — Output format.** Markdown only in v0.1. PDF / DOCX export of Concept Brief deferred to v0.2 (only after the stay-rough default is validated — see §2.2 brief).
- **OQ5 — Bridge schema to art-paper.** Closed: yes, the Concept Brief schema (§2.2 brief) is the bridge document. A future `art-paper` sibling distribution consumes it as input.
- **OQ6 (new) — Runtime grounding for lineage entities.** Should `lineage` mode integrate Wikidata / ULAN / e-flux retrieval at runtime? v0.1: no (instrumented disclosure only). v0.2: yes (architectural mitigation per §6.1).
- **OQ7 (new) — Contributing Korean media-art scholar as reference-layer co-author.** Should the E-section expansion (§3 point 5) be done as solo library work or as a commissioned/co-authored contribution from a working Korean media-art curator/scholar? Default: pursue co-authorship; if not feasible, library work with full attribution of consulted sources.
- **OQ8 (new) — Use-frequency limit / taper protocol.** Should the plugin actively encourage decreasing reliance over time (Devil's Advocate Attack 7 mitigation)? v0.1: no, but disclose conviviality question openly. v0.2: design open.
- **OQ9 (new) — Korean / East-Asian default routing details.** §2.2 lineage point 3 specifies the routing but defers the detection logic (subject-domain signals). v0.2 work.
- **OQ10 (new) — Stay-rough default robustness.** §2.2 brief stay-rough behavior needs prompt-engineering work to actually preserve the artist's voice rather than regress to LLM-default polish. v0.2 work + Study 3 (attribution UI) overlap.

---

## 9. Out of scope for v0.1 (renamed)

- Generative image / sound / video sketches from the Brief.
- Real-time collaboration (multiple artists ideating together).
- Studio-log ingestion (importing prior notebooks, sketches).
- Grant-application templates beyond the Concept Brief.
- Curator-side ingestion (curator using the plugin to evaluate submitted Briefs).
- Mixed-initiative behavior (the v0.1 explicit commitment is turn-taking; HCI Q3 Position A).
- Full longitudinal artist study (deferred to Phase 9 in the revised 2026-05-25 sequencing — empirical track).
- ICCC / CHI full-paper submission (deferred until evaluation suite is complete).

---

## Provenance of this spec

This spec is itself a worked example of the design-through-critique discipline the plugin's `rehearsal` mode is meant to scaffold for artists. The four agent critiques that produced it operated under the same architectural commitments the plugin enforces: tradition-tagged personas, formative-not-decisional output, no auto-convergence between agents, explicit user (the maintainer) decision at the synthesis step. The audit trail is intentional; the maintainer claims design responsibility for the synthesis, with credit to the four agent critiques for surfacing the failure modes addressed here.

The maintainer also notes — per Devil's Advocate Attack 5 — that v0.1 is *currently* closer to a paper artifact than to an artist tool. Phase 7 (Study 1 + longitudinal, in the revised 2026-05-25 sequencing) is the work that converts that situation. Until then, the framing in §1.4 (user asymmetry scope) is the honest answer, and the Aslib JIM Conceptual paper (Phase 5) is explicit that the framework's empirical adequacy is downstream work the conceptual paper invites rather than performs (§5.3).
