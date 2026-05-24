# Art Ideation Methodology — Reference Layer (v0.2)

Survey of validated **pre-studio articulation methodologies** that operate at the early phase of an art project. Used by the `art-ideation` skill as the knowledge base for socratic prompting, provocation cards, lineage positioning, Concept Brief drafting, and self-critique rehearsal.

> **Scope note.** This is a *reference* layer, not a literature review. Each entry gives author/year, the methodology's core gesture, the **ideation mechanism** it activates, an **Authentic Practice Boundary** naming what the plugin defers to human execution, a **contested in** field where the source has been critiqued in the literature, and the **skill hook** where it can be mounted (mode: `socratic`, `provoke`, `lineage`, `brief`, `rehearsal`).

> **Tradition tag, not provenance.** When this file is cited by a plugin output ("via Oblique Strategies", "via Sullivan's contextualist inquiry"), the tag indicates which entries were loaded into the prompt that produced the output. It does **not** claim causal attribution — the LLM's actual generation mechanism is opaque. A tag is a *prompt-grounding* and *style-affinity* claim: the output aims to operate in the tradition named, and was conditioned by it; whether it succeeds in that aim is for the artist to judge. The artist is encouraged to read the named primary source to deepen the engagement. The L3 citation-faithfulness rule still applies — `(verify)`-tagged claims downstream must not be asserted without independent confirmation.

> **Mode legend** (v0.2 — `panel` renamed to `rehearsal`):
> - **socratic** — Q&A loop drawing the artist out (open questions, no answers).
> - **provoke** — constraint / disruption injected to force a non-default move (with preserved unhelpfulness — no auto-interpretation).
> - **lineage** — positions the work against precedent (artists, theories, traditions) only after the artist supplies initial candidates; carries mandatory training-data bias header.
> - **brief** — converges the dialogue into a written Concept Brief with epistemic fields (proposition / anti-proposition / disconfirmation condition / Frayling-type declaration); stay-rough default.
> - **rehearsal** — multi-persona Self-Critique Rehearsal around a draft Brief (formative, not decisional); persona-collapse detector active.

---

## 0. Positionality (new in v0.2)

This document was authored by a Korean researcher who works at once as an exhibiting artist, an author of practice-based art papers at peer-reviewed venues, and an AI researcher publishing in the field. Sources were read primarily in English and Korean. Chinese classical aesthetic sources (Xie He, Jing Hao, Su Shi) are taken via Korean Joseon-period reception and translated Sino-Korean materials, not directly from contemporary Sinology. The choice to organize this reference into a separate **Section E** for Korean / East-Asian context — rather than integrating those entries into A–D — is a deliberate trade-off:

- *Pro-integration argument:* a separate Section E enacts a centre/periphery framing that the very decolonial-methods literature (Tuck & Yang 2012; Smith 1999) the plugin should engage explicitly *critiques*. The most rigorous move would be to thread East-Asian entries into A–D wherever they fit by mechanism rather than by geography.
- *Pro-separation argument (chosen here):* the reference layer's primary readership in v0.1 is Western-PaR-trained artists and reviewers for whom East-Asian entries are unfamiliar; a separate section makes the contribution visible and harder to skim past. Integration is the v0.2/v0.3 aspiration.

This positionality is itself a contestable choice and is named here so it can be argued back against. The v0.2 plan (see [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](../../docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md) §3 point 5) is to expand Section E from 3 to 5–7 verified entries, ideally via consultation with working Korean media-art curators / scholars, and to eventually integrate the entries into A–D.

**On the corpus represented below.** The 25+ entries below skew Western (A–D) by a roughly 4:1 ratio, mirroring the training-data canon bias the plugin discloses in the `lineage` mode header. This is a *systematic defect* of the v0.1 reference layer, not a feature; it is named here as such. The plugin's Korean / East-Asian default routing on Korean sessions partially mitigates *runtime* bias but cannot mitigate the underlying corpus imbalance.

---

## A. General Creativity & Cognitive Theories

### A1. Margaret Boden (1990, 2004) — *The Creative Mind: Myths and Mechanisms*; three types of creativity
- Distinguishes **combinational** (novel combinations of familiar ideas), **exploratory** (mapping new territory within an existing conceptual space), and **transformational** (changing the rules of the conceptual space itself) creativity.
- **Ideation mechanism:** typology lets the artist diagnose *what kind* of move they are attempting; transformational creativity in particular is triggered by altering or dropping a constraint that defines the current space.
- **Authentic Practice Boundary:** Boden's framework is *typological*; the plugin can offer the typology as a diagnostic prompt but cannot determine which type any specific artistic move belongs to. The artist judges.
- **Contested in:** Glăveanu (2010, "Paradigms in the Study of Creativity", *Review of General Psychology* 14(1) — verify exact page) critiques the trait-property treatment of creativity in Boden and proposes a relational alternative (his 5A model — actor / action / artifact / audience / affordance). The Boden typology operates within what Glăveanu calls the "He-paradigm" (creativity as property of an individual mind); the plugin's design that bridges Boden with Csikszentmihalyi's systems model (A4) implicitly takes Glăveanu's critique seriously without naming it.
- **Hook:** `provoke` (offer all three types as alternative attack angles); `socratic` ("Are you combining, exploring, or transforming?").

### A2. Finke, Ward & Smith (1992) — *Creative Cognition: Theory, Research, and Applications*; **Geneplore model**
- Two-phase cognitive model: a **generative** phase produces *preinventive structures* (vague mental forms, visual / conceptual proto-ideas), then an **exploratory** phase interprets, extends, and constrains them toward usable concepts.
- **Ideation mechanism:** forces a separation between *making something to think with* and *evaluating what it could be*; suppresses premature convergence.
- **Authentic Practice Boundary:** Geneplore is a *cognitive-laboratory* model with mixed external validity for studio practice (see contested-in below). The plugin uses it as a *discipline* — generation before evaluation — without claiming the cognitive model is the actual mechanism artists use.
- **Contested in:** the original studies were short-form word/picture tasks; generalization to multi-week studio ideation is empirically thin. PaR theorists (especially Barrett & Bolt 2007, C7) would argue the model imports a propositional psychology onto a domain where ideation is *materially* constituted, not phase-separated in the mind.
- **Hook:** `socratic` two-pass loop — first elicit raw forms ("describe an image or fragment, no need to justify"), then re-interpret ("what could this become?"); pairs with `provoke`.

### A3. Arthur Koestler (1964) — *The Act of Creation*; **bisociation**
- Creativity = the collision of two normally unrelated frames of reference ("matrices"), producing humor, scientific discovery, or art depending on the affective register.
- **Ideation mechanism:** deliberately picks a *second, alien* domain and forces an analogy / collision with the primary one.
- **Authentic Practice Boundary:** Koestler's framework assumes the artist already knows both domains. The plugin can suggest the second domain from its training-data corpus, but the resulting collision will be biased toward LLM-clustered "alien" domains, which may not be alien at all to the artist; the artist should expect to override the plugin's domain suggestions frequently.
- **Contested in:** widely cited as a precursor in cognitive science but rarely as the operative theory; competing frameworks (Conceptual-Blending, Fauconnier & Turner 2002, *The Way We Think* — verify) refine bisociation into a more granular blending operation.
- **Hook:** `provoke` (draw a random distant-domain card and require integration); `rehearsal` (a domain-foreign reviewer voice).

### A4. Mihaly Csikszentmihalyi (1996, 1999) — *Creativity: Flow and the Psychology of Discovery and Invention*; **systems model**
- Creativity is not a property of the individual alone but emerges from a system of three components: **domain** (the symbolic body of knowledge / conventions), **field** (the gatekeepers and institutions that validate), and **person** (the contributor). A novelty becomes "creative" only when the field accepts it into the domain.
- **Ideation mechanism:** reframes ideation as a *positioning* act — what domain rule are you challenging? what field will judge it? — preventing solipsistic novelty.
- **Authentic Practice Boundary:** "field" varies sharply across art-world geographies and is *not* a uniform global gatekeeper set. The plugin's training data over-represents anglophone fields (Ars Electronica, ZKM, Whitney, SIGGRAPH); using Csikszentmihalyi via this plugin risks installing an anglophone field-model as the default. East-Asian, Latin-American, African, and indigenous art fields are systematically under-represented.
- **Contested in:** the systems model is sometimes critiqued (e.g. Glăveanu, op. cit.; postcolonial art-history literature) for assuming the field as a stable validator; in practice, field composition is contested and shifts with each gatekeeping event. The plugin should treat "field" as plural and contested, not as a unified arbiter.
- **Hook:** `lineage` (map domain + field around the nascent idea); `rehearsal` (simulate field gatekeepers — curator, peer artist, critic).

### A5. Ronald Finke (1990) — *Creative Imagery: Discoveries and Inventions in Visualization*; **preinventive structures**
- Subcomponent of Geneplore: classifies the proto-forms generated in the generative phase (visual patterns, object forms, mental blends, categorical exemplars, mental models, verbal combinations) as having properties — novelty, ambiguity, meaningfulness, emergence, incongruity — that *invite* later interpretation.
- **Ideation mechanism:** licenses deliberately ambiguous or incongruous proto-forms as legitimate ideation output; treats half-formed sketches as raw material, not failure.
- **Authentic Practice Boundary:** Finke's "preinventive structures" are *mental*; the plugin's analog is text-fragments emitted under `socratic` mode with the residue field. The mapping is approximate, not equivalent.
- **Contested in:** same generalization-from-lab concern as A2.
- **Hook:** `provoke` (request explicitly ambiguous / incongruous fragments before interpretation); `brief` (capture preinventive structures verbatim under the *residue* field, mark for later interpretation pass).

---

## B. Design & Planning Methodologies

### B1. IDEO / Stanford d.school (popularized 1990s–2000s, Tim Brown 2009 *Change by Design*) — **Design Thinking** (empathize → define → ideate → prototype → test)
- Five-phase human-centered design process. The **ideate** phase explicitly separates divergent generation from convergent selection and prescribes group techniques (HMW ["How Might We"] questions, brainstorming rules, affinity clustering).
- **Ideation mechanism:** stage-gates ideation so generation is not throttled by evaluation; reframes problem as a "How Might We…" question (specific enough to act on, open enough to permit multiple answers).
- **Authentic Practice Boundary:** Design Thinking is built for *user-centered design*. Art is not user-centered. The plugin can borrow individual techniques (HMW reformulation, divergent/convergent discipline) but should not import the user-centered frame whole — Sullivan/Borgdorff/Barrett & Bolt (C5/C4/C7) would diagnose user-centered framing as a category error for PaR.
- **Contested in:** the Design Thinking framework has been critiqued for over-instrumentalizing creativity (Iskander 2018, *Stanford Social Innovation Review*; Vinsel & Russell 2020, *The Innovation Delusion*); the divergence/convergence schema is borrowed from convergent-task literature (Guilford) whose ecological validity in real design teams is contested.
- **Hook:** `brief` (HMW reformulation of the artist's provocation); `socratic` (empathize-phase questions); caveat — offered as *technique*, not as the operative frame.

### B2. Bob Eberle (1971) — *SCAMPER: Games for Imagination Development* — **SCAMPER**
- Checklist of seven transformation operators applied to an existing object/idea: **S**ubstitute, **C**ombine, **A**dapt, **M**odify (or Magnify/Minify), **P**ut to other uses, **E**liminate, **R**everse/Rearrange. Building on Alex Osborn's earlier idea-generation prompts.
- **Ideation mechanism:** forces lateral mutations on a base concept; each operator yields a distinct candidate variant, defeating fixation.
- **Authentic Practice Boundary:** SCAMPER is a *checklist*, not an interpretation. The plugin can cycle the seven operators but the *value* of each mutation is judged by the artist. The tag is for *style affinity*, not an empirical-effectiveness claim.
- **Contested in:** the empirical literature on SCAMPER's actual effectiveness in designer cognition is mixed and weaker than the popularity of the checklist would suggest. See Christensen & Schunn (2007, "The relationship of analogical distance to analogical function and preinventive structure: the case of engineering design", *Memory & Cognition* 35(1) — verify); Goldschmidt & Tatsa (2005, "How good are good ideas?", *Design Studies* 26 — verify) on related concerns about ideation-tool efficacy. The plugin's `provoke` mode should not claim SCAMPER-tagged provocations are demonstrably more effective; they are *style-affine* with the checklist tradition.
- **Hook:** `provoke` (cycle the seven operators against the artist's current concept and capture each mutation as a candidate direction).

### B3. Edward de Bono (1967 *The Use of Lateral Thinking*; 1985 *Six Thinking Hats*) — **Lateral Thinking** + **Six Hats**
- *Lateral thinking* = deliberate disruption of linear/logical ("vertical") reasoning via provocations (PO), random entry, escape, reversal. *Six Hats* = role-segregated thinking modes (white=facts, red=emotion, black=critique, yellow=optimism, green=generation, blue=process).
- **Ideation mechanism:** PO ("provocative operation") suspends judgment to let an absurd premise generate consequences; Hats parallelize otherwise-conflicting cognitive stances so they don't cancel each other.
- **Authentic Practice Boundary:** de Bono's methods are *facilitated workshop* techniques in their original use; running them solo with a chatbot is a degraded form. The plugin can simulate the structure but not the social-accountability that group facilitation provides.
- **Contested in:** de Bono's work is widely deployed in management training but lightly engaged in cognitive-science literature; the empirical evidence is thin (and de Bono himself often eschewed empirical framing). Treat as a heuristic tradition, not a validated method.
- **Hook:** `provoke` (PO prompts: "Po: the museum has no walls"); `rehearsal` (cast each Hat as a voice around the embryonic idea).

### B4. Genrich Altshuller (1956 onward, English-language consolidation 1984 *Creativity as an Exact Science*) — **TRIZ** + 40 inventive principles
- Theory of inventive problem solving derived from patent analysis. Frames invention as the resolution of **contradictions** between desired parameters; offers a contradiction matrix mapping to **40 inventive principles** (segmentation, asymmetry, nesting, dynamism, inversion, etc.).
- **Ideation mechanism:** reframes the design problem as a contradiction to be resolved rather than a trade-off to be compromised; principles act as analogical heuristics. Direct transfer to art is partial — works best for art with a technical/engineering layer (kinetic, interactive, robotic).
- **Authentic Practice Boundary:** TRIZ assumes an *engineering* contradiction (resolvable parameters); art frequently *holds* contradictions rather than resolves them (Barrett & Bolt 2007). Offered as a heuristic for the engineering layer of art-and-technology work, not as a method for the artistic question.
- **Contested in:** TRIZ's empirical performance outside its origin patent-corpus is contested in design-methodology literature.
- **Hook:** `provoke` for tech-heavy art projects (surface the contradiction, suggest principles); `lineage` when positioning relative to media-art engineering precedent.

### B5. Bernd Rohrbach (1968) — **6-3-5 / Brainwriting**
- Structured silent group ideation: 6 participants, each writes 3 ideas on a sheet, sheets rotated 5 times; participants build on what others wrote. Counters the social-loafing and dominance failures of unstructured brainstorming.
- **Ideation mechanism:** parallel + asynchronous + visual; each round is a *recombination* on the prior round's residue.
- **Authentic Practice Boundary:** brainwriting requires *multiple humans*. Single-artist use with a simulated set of voices is a degraded form (mode `rehearsal` partial; not used in `provoke`).
- **Contested in:** moderate empirical support compared to brainstorming in workshop settings; minimal evidence for solo use.
- **Hook:** `rehearsal` (simulate the 6 voices as agents passing a shared sheet, with explicit acknowledgement of the degraded-form limitation).

---

## C. Art-Specific Methodologies (highest priority for this reference)

### C1. Brian Eno & Peter Schmidt (1975, 1st ed.; later editions) — **Oblique Strategies: Over One Hundred Worthwhile Dilemmas**
- A deck of cards, each bearing a single cryptic instruction ("Honor thy error as a hidden intention", "Use an old idea", "Turn it upside down"). Drawn at moments of creative impasse.
- **Ideation mechanism:** introduces *aleatory constraint* — a deliberately under-specified prompt forces interpretation, displacing the artist from a fixated path. The card's authority is procedural, not semantic.
- **Authentic Practice Boundary:** the physical, finite, blindly-drawn character of the deck is *constitutive* of its working. The plugin's `provoke` mode produces Oblique-*affine* provocations under prompt grounding; it cannot replicate (i) the artist's bodily ritual of drawing, (ii) the deck's finite set (you eventually meet every card again), (iii) the deck's authorship-history (two specific humans with shared practice). The plugin must default to **silence after the provocation** — no auto-interpretation, no "would you like to discuss this?" follow-up. The artist is encouraged to obtain the actual deck for serious use.
- **Contested in:** the deck's continued cultural authority (50+ years in active use) is itself the validation; serious critique is rare. The contested point is the *transfer* to software / chatbot form (this plugin included): does an algorithmic Oblique Strategies retain the constitutive features, or only the surface? The plugin takes the position that it preserves *style affinity* but not *constitutive character*.
- **Hook:** `provoke` (canonical pattern — surface a strategy when the dialogue plateaus, then go silent).

### C2. Sol LeWitt (1967 *Paragraphs on Conceptual Art*, *Artforum*; 1969 *Sentences on Conceptual Art*, *0–9 / Art-Language*) — **Conceptual Art / idea-first**
- "The idea becomes a machine that makes the art." Execution is subordinate to the concept; the plan / instruction-set *is* the work. The artist is rule-setter, not necessarily fabricator.
- **Ideation mechanism:** ideation IS the work — forces the artist to formalize the concept as a transmissible rule / instruction, exposing any vagueness; permits delegation of execution.
- **Authentic Practice Boundary:** LeWitt's framework reserves the *rule-setting* position for the artist. A plugin that authors instructions on the artist's behalf occupies the position LeWitt's framework *excluded*. The plugin's `brief` mode must therefore *prompt the artist to write instructions*, not author instructions for the artist.
- **Contested in:** the LeWitt position has been contested (Krauss 1979, "Sculpture in the Expanded Field"; later media theory) for being insufficiently attentive to material specificity; counter-positions privilege the *execution* as inseparable from the idea.
- **Hook:** `brief` (force the artist to state the work as a one-paragraph instruction-set, in the artist's own words); `socratic` ("If you handed this to a fabricator, what would they need? what would still be ambiguous?").

### C3. Christopher Frayling (1993) — *Research in Art and Design*, RCA Research Papers 1(1) — **research into / through / for art**
- Tripartite distinction: research **INTO** art (historical, theoretical — art as object of study); research **THROUGH** art (practice as the means of inquiry, materials / process generate knowledge); research **FOR** art (research that supports the making, with the artwork as the output where knowledge is embodied — Frayling himself noted this last category as the hardest to articulate).
- **Ideation mechanism:** lets the artist locate their project on the through / for axis early, which determines what counts as evidence and what the eventual paper will need to defend.
- **Authentic Practice Boundary:** the Frayling typology is *meta-methodological*. Naming the type does not perform the research; that work still happens in the studio or in the writing.
- **Contested in:** Scrivener (2002, "The art object does not embody a form of knowledge", *Working Papers in Art and Design* — verify) critiques the FOR category as ill-defined. Candy & Edmonds (2018, *Interacting: Art, Research and the Creative Practitioner* — verify) refine the typology. Borgdorff (2012, C4) further articulates "research IN the arts" which partially supersedes Frayling THROUGH.
- **Hook:** `brief` (typing the project on the Frayling axis is part of the Concept Brief — required field in v0.2); `lineage` (positions against the art-research tradition). **Note:** v0.2 plugin itself declares a Frayling layered hybrid self-position (FOR = tool, INTO = reference layer, THROUGH = design choices); see [`POSITIONING.md`](../../POSITIONING.md) "Self-positioning".

### C4. Henk Borgdorff (2011, "The Production of Knowledge in Artistic Research", in *The Routledge Companion to Research in the Arts*; 2012 *The Conflict of the Faculties: Perspectives on Artistic Research and Academia*)
- Argues artistic research is a legitimate mode of knowledge production whose object is "**not-yet-knowing**" embodied in artistic practice. The knowledge *resides in the artwork*. Distinguishes research **on**, **for**, and **in** the arts; the latter is practice-as-research, where the artwork is the primary site of inquiry. Insists on the dual-discourse criterion: artistic research must contribute simultaneously to art-world discourse *and* to academic discourse (verifiability, criticisability, accumulability).
- **Ideation mechanism:** ideation framed as articulating the *research question implicit in a making impulse* — what does this work want to find out? What can only be found out by making it?
- **Authentic Practice Boundary (substantive — restored from v0.1):** Borgdorff's "not-yet-knowing" is *embodied in the artwork*. The plugin produces **language**, not artworks. Under Borgdorff's strict definition, no plugin output is, by itself, *artistic knowledge*. The plugin operates *adjacent to* artistic research, in the propositional-articulation space surrounding it — the v0.2 framing as "pre-studio articulation scaffold" (POSITIONING.md §1) addresses this restoration directly. The plugin must not claim its outputs *are* artistic research outputs; the outputs are *preparatory* to artistic research.
- **Contested in:** Sullivan (2010, C5) holds an arguably stronger position that *practice itself* is research (not via embodiment-in-artwork). The plugin sits between Borgdorff and Sullivan on this: it accepts Borgdorff that artistic knowledge resides in the work, and accepts Sullivan that practice is the inquiry — and concludes that the plugin's role is therefore *para-artistic articulation*, not artistic research.
- **Hook:** `socratic` ("What can only be discovered by making this work, not by reading or thinking about it?" — note the question is *honest about the plugin's limit*: it can ask, but cannot itself discover); `brief` (research-question articulation field; the *disconfirmation condition* field operationalizes Borgdorff's criticisability gate).

### C5. Graeme Sullivan (2010, 2nd ed.) — *Art Practice as Research: Inquiry in Visual Arts*
- Proposes a framework of inquiry built around three practices: **conceptual** (theorist as artist), **dialectical** (artist as critical agent), and **contextual** (artist as activist / in-context). Visual-arts research generates theory via making.
- **Ideation mechanism:** typology of artist-as-researcher stances; choosing a stance early shapes what the ideation looks for (concept refinement vs. critique vs. context engagement).
- **Authentic Practice Boundary:** Sullivan locates the *epistemic event* in the practice itself. The plugin sits *outside* practice; using Sullivan via plugin risks importing his vocabulary while losing the locus of his claim. The plugin's `lineage` mode kin / opposition / blind-spot / unexpected-neighbor schema directly enacts Sullivan's *contextualist* third practice — using Sullivan honestly requires committing to that contextualist framing rather than treating lineage as marketing or kin-listing.
- **Contested in:** Sullivan's position is sometimes critiqued as insufficiently attentive to material specificity (Barrett & Bolt 2007, C7) and as overgeneralized from visual-arts to all PaR. The PaR field is plural; Sullivan is one strong position, not consensus.
- **Hook:** `lineage` (contextualist inquiry — strongest mode-to-theory fit in the entire reference layer); `brief` (select stance, declare it as the work's epistemic position).

### C6. Hazel Smith & Roger T. Dean (eds., 2009) — *Practice-Led Research, Research-Led Practice in the Creative Arts*
- Anthology arguing that practice-led research and research-led practice form an *iterative cyclic web* rather than a linear hierarchy; the **iterative cyclic web** model proposes that idea, practice, theory, and outcome loop and re-enter at multiple points, in any order, over time.
- **Ideation mechanism:** licenses re-entry — ideation is not a single up-front phase but a recurring node revisited as the work develops. Counters the linear "ideate then make then write" fallacy.
- **Authentic Practice Boundary (substantive — restored from v0.1):** Smith & Dean's web is *temporal* and *non-linear*. The v0.1 plugin's `full` mode chained socratic → provoke → lineage → brief → panel **in one session** — this directly contradicted the iterative cyclic web while citing it as backing. The v0.2 `full` mode (now a long-running project file with sessions days / weeks apart) is the corrected operational form.
- **Contested in:** the iterative cyclic web is sometimes critiqued as descriptively true but not operationally constraining — it permits any sequence, which means it doesn't prescribe. The plugin's response is to make re-entry a first-class affordance (the `full` mode project file persistence) rather than a single-session loop.
- **Hook:** `full` (project-file shape across sessions); `socratic` ("Where are you in the cycle right now — making, theorizing, or re-ideating?").

### C7. Estelle Barrett & Barbara Bolt (eds., 2007) — *Practice as Research: Approaches to Creative Arts Enquiry*
- Foregrounds the *materiality* of practice as a knowledge-producing process (drawing on Heidegger via Bolt's "handlability", Bourdieu's habitus). Knowledge is generated *through* engagement with material. Bolt's chapter on **the experimental gesture** — interventions whose value lies in the *displacement* they enact, not in the content they propose — directly anchors the v0.2 `provoke` mode framing.
- **Ideation mechanism:** locates ideation in the encounter with material — the medium "talks back" and the idea forms through that exchange, not prior to it. Bolt's experimental gesture suggests provocations should be experiments whose outcome is unknown, not solutions whose form is known.
- **Authentic Practice Boundary (substantive — restored from v0.1):** Bolt's argument is that *material engagement* is the knowledge-producing event. The plugin produces *text*, not material engagement. The most honest plugin use of Barrett & Bolt is in `provoke` mode as a *prompt back into material*: "Pick up the material first. What does it suggest *before* you have an idea?" — explicitly redirecting the artist from the chat to the studio. The plugin's role here is *to displace itself*.
- **Contested in:** the material-engagement position is sometimes critiqued (e.g. from a more semiotic / discursive position) for under-theorizing the linguistic / symbolic layer of artistic meaning. The plugin's existence implicitly takes the semiotic side; Barrett & Bolt would not endorse a chat-based ideation tool. The plugin acknowledges this tension explicitly (see Tensions §T6).
- **Hook:** `provoke` (experimental-gesture provocations that redirect to material); `socratic` (material-first prompts when the dialogue has gone abstract).

### C8. Anne Bogart & Tina Landau (2005) — *The Viewpoints Book: A Practical Guide to Viewpoints and Composition*
- Movement / composition method (originally Mary Overlie's six Viewpoints, expanded by Bogart / Landau). Nine physical and vocal viewpoints organized along **time** (tempo, duration, kinesthetic response, repetition) and **space** (shape, gesture, architecture, spatial relationship, topography), plus pitch / dynamic / timbre for voice. Used to compose performance without predetermined narrative.
- **Ideation mechanism:** decomposes a performance idea into orthogonal axes so the artist can ideate one axis at a time; ideation becomes structured exploration of compositional parameters.
- **Authentic Practice Boundary:** Viewpoints work is *bodied, ensemble-based, temporal* — a studio practice with multiple performers in space. The plugin can ask Viewpoints-*derived* questions about the *intended encounter* but cannot perform Viewpoints work. Tag denotes pedagogical affinity, not method execution.
- **Contested in:** Viewpoints is contested within performance theory for being insufficiently attentive to dramaturgy / narrative; the plugin's use of it is restricted to the *intended encounter* dimension of the Concept Brief, not as a general ideation method.
- **Hook:** `brief` (intended-encounter field — what spatial / temporal / kinesthetic relation does the work propose for the audience?); `provoke` for time-based / performance / installation work (cycle through viewpoints as ideation prompts, with the Authentic Practice Boundary disclaimer).

### C9. Corita Kent (1968) — **10 Rules** (Immaculate Heart College Art Department Rules, often co-attributed to John Cage who is named in Rule 10)
- Ten classroom rules used as an artistic ethos: e.g., "Find a place you trust and then try trusting it for a while"; "General duties of a student: pull everything out of your teacher, your fellow students"; "Be self-disciplined"; "Don't try to create and analyze at the same time"; "Be happy whenever you can manage it"; "The only rule is work" (often quoted from Cage). Famously displayed in Cage's studio.
- **Ideation mechanism:** behavioral / ethos scaffolding — separates the *making* time from the *judging* time, legitimizes copying and experimentation as routes to ideation.
- **Authentic Practice Boundary:** the rules were *classroom rules* in a specific pedagogical relationship; transferred out of that context (especially as bullet-point reminders in a chat) they risk becoming inspirational posters. The plugin uses them as guardrails on dialogue discipline (rule 4 + rule 8 — "consider everything an experiment", "don't create and analyze at the same time"), not as inspirational content.
- **Contested in:** the rules are widely cited but rarely deeply analyzed; some scholars (verify) have noted the rules' specific Catholic-progressive pedagogy at Immaculate Heart context, which is often stripped when the rules are circulated as universal art-school wisdom.
- **Hook:** `socratic` (use rules 4 and 8 as guardrails on the ideation session itself); `provoke`.

### C10. Jerry Saltz (2018, *Vulture*; expanded in 2020 *How to Be an Artist*) — **33 rules / How to Be an Artist**
- Critic's manual of rules for the practicing artist, organized as steps from "Begin" through "Learn how to think like an artist" to "Survive". Examples: "Work, work, work", "Develop forms of discipline", "Embed thought in material", "Listen to the stupid voices in your head", "Art is not about understanding".
- **Ideation mechanism:** demystifies the ideation block by reframing it as a productivity / identity problem rather than a metaphysical one; "embed thought in material" is a directive to externalize ideation early.
- **Authentic Practice Boundary:** Saltz writes as a *critic*, not a methodologist. The rules are aphoristic and partial; the plugin uses them as *encouragement / unblocking prompts* under `socratic` and `rehearsal` (where Saltz's critic-voice fits), not as a method.
- **Contested in:** Saltz has been critiqued (within art-criticism circles) for the populism of the *Vulture* style. The plugin uses Saltz selectively, weighted toward the working-practice rules rather than the art-market rules.
- **Hook:** `socratic` (encouragement / unblocking prompts when the artist is stuck on legitimacy rather than concept); `provoke`; `rehearsal` as the critic-voice persona seed.

### C11. John Cage (1937 *The Future of Music: Credo*; *Music of Changes* 1951 using *I Ching*; 1961 *Silence*) — **chance operations / indeterminacy**
- Compositional method using non-intentional procedures (I Ching coin tosses, star charts, imperfections in paper) to remove the composer's preference from determinative decisions. Distinguishes **chance operations** (used to compose a fixed score) from **indeterminacy** (the score leaves performance decisions open).
- **Ideation mechanism:** procedurally outsources decisions the artist would otherwise make from taste / habit; surfaces what taste was hiding. Closely related to Eno's Oblique Strategies (which Cage influenced).
- **Authentic Practice Boundary (substantive — restored from v0.1):** Cage's epistemic point includes the *time the artist spends performing the procedure* — throwing the coins, consulting the I Ching table, transcribing the result by hand. The plugin **must not generate chance results**. Cage himself, although he used computers in works like *HPSCHD*, always preserved the temporal-material character of the procedure as part of the work. The plugin can *propose* a chance method — "consider letting an I Ching toss decide between these three options" — and *describe* what the artist would need to do, but the throw itself stays with the artist.
- **Contested in:** Cage's chance operations are sometimes critiqued for not actually removing taste (the procedure-design itself encodes taste — which I Ching mappings, which coin choice, etc.). The plugin's deferral of execution side-steps this critique: the artist's taste enters where the artist designs and executes the procedure.
- **Hook:** `provoke` (offer to *describe* a chance-operation move — never execute it — to break a taste-locked decision); `socratic` ("Which of your current decisions are you making from habit?").

### C12. Bauhaus **Vorkurs** / Preliminary Course (1919–1933; Johannes Itten 1919–1923; later Moholy-Nagy and Josef Albers) — material / form / color preliminary
- Mandatory introductory course at the Bauhaus: systematic exploration of materials (texture, weight, structure), forms (point, line, plane, primary shapes), and color (Itten's color theory; Albers' interaction-of-color exercises later at Black Mountain / Yale). Goal: strip prior artistic habit and rebuild perception from first principles.
- **Ideation mechanism:** material / form / color *exercises* as ideation seeds — letting the medium's elementary grammar generate concepts. Decouples ideation from subject-matter / representation.
- **Authentic Practice Boundary:** Vorkurs is a *studio* pedagogy that requires *physical materials* in a workshop setting. The plugin can describe exercises and reference Albers / Itten as a tag, but cannot replicate the studio. Tag denotes pedagogical affinity, not method execution.
- **Contested in:** Bauhaus pedagogy is widely cited but has been critiqued (postcolonial design history, e.g. Margolin 2013 — verify) for its universalist claims about perception, which assume a specific (Western, modernist, ocularcentric) viewer.
- **Hook:** `provoke` (offer a Vorkurs-style exercise as a seed when the artist is stuck on subject, with the Authentic Practice Boundary disclaimer); `lineage` (positions formalist / materialist work).

---

## D. Media-Art & Technology-Specific Ideation

### D1. Lev Manovich (2001 *The Language of New Media*; 2013 *Software Takes Command*) — **software studies / database as symbolic form**
- *The Language of New Media* proposes new-media principles (numerical representation, modularity, automation, variability, transcoding) and argues the **database** has replaced narrative as the dominant symbolic form of the computer age. *Software Takes Command* extends this into "software studies".
- **Ideation mechanism:** reframes the work as a *system* (database + interface + algorithm) rather than a single object; the ideation question becomes "what is the database, what is the interface to it, what does navigation reveal?"
- **Authentic Practice Boundary:** Manovich's framework was formulated in 2001 — pre-deep-learning, pre-large-language-model. Applying his principles to contemporary AI-mediated work requires updating that the plugin does not perform automatically. Treat as a historically-positioned vocabulary.
- **Contested in:** Galloway (2012, *The Interface Effect*) contests the database-as-symbolic-form thesis, arguing that *interface* (not database) is the operative symbolic form. Chun (2011, *Programmed Visions*) further complicates the software-studies frame. The plugin should not treat Manovich as the sole or settled new-media theorist.
- **Hook:** `brief` (specify the work along Manovich's principles, then test the specification against Galloway / Chun if the work is interface-heavy); `lineage` (new-media positioning, contested-in noted).

### D2. Casey Reas & Ben Fry (2007 *Processing: A Programming Handbook for Visual Designers and Artists*; co-creators of Processing 2001) — **generative-art ideation patterns**
- Established a pedagogical canon for code-as-medium: structured ideation around computational primitives (form, motion, image, color, transformation, data) and patterns (recursion, particle systems, agent behaviors, image manipulation). Reas's own work foregrounds rule-based generation as composition.
- **Ideation mechanism:** the *primitive* and the *rule* are the unit of ideation; an idea is a small executable rule whose behavior over time / iteration is the work.
- **Authentic Practice Boundary:** Reas / Fry's approach is *code-first* — the rule is meaningful only when executed. The plugin can describe rules and gesture at outcomes but cannot run them; the artist's experience of writing and running the rule is the locus of ideation. Tag denotes pedagogical kinship, not method substitute.
- **Contested in:** the Processing / generative-art canon has been critiqued (e.g. for its formalist tendency, its under-attention to politics of code, its anglophone-male-dominated lineage). Counter-positions (Critical Code Studies; the *Black Software* lineage — McIlwain 2019) widen the field.
- **Hook:** `provoke` (suggest a primitive + a rule, prompt the artist to execute it and report back); `brief` (specify the rule as the work, in the LeWitt sense for code).

### D3. Mitchell Whitelaw (2004) — *Metacreation: Art and Artificial Life* — **metacreation**
- Term for artworks that create or are creative, drawing on artificial life. Surveys a-life art (Karl Sims, Christa Sommerer & Laurent Mignonneau, etc.) and asks what it means for the artist to delegate creation to a system.
- **Ideation mechanism:** ideation becomes design of a *generative system whose outputs are the work*; the artist authors at the meta-level — rules of behavior, environment, selection pressure — not the individual artifact.
- **Authentic Practice Boundary:** metacreation work assumes the artist designs the *generator*; using this plugin to "delegate creation" of the *concept* itself would be a category error — the plugin is meta-articulation, not meta-creation.
- **Contested in:** the autonomy claims in a-life / metacreation literature are contested (the system's "autonomy" is always bounded by the artist's design choices); see Galanter (D4) for the complexity-theory critique.
- **Hook:** `brief` (articulate the work at the meta-level — what is the system, what are its degrees of freedom?); `lineage` (a-life / generative-art tradition).

### D4. Philip Galanter (2003) — "What is Generative Art? Complexity Theory as a Context for Art Theory" (GA2003 conference paper) — **generative art via complexity**
- Defines generative art as "any art practice where the artist uses a system… set into motion with some degree of autonomy contributing to or resulting in a completed work of art". Argues complexity theory (effective complexity between order and disorder) provides a context for evaluating generative work.
- **Ideation mechanism:** scales the ideation question along an order ↔ disorder axis — where on the complexity spectrum should the system sit? This is a parameter the artist can deliberately set rather than stumble into.
- **Authentic Practice Boundary:** Galanter's effective-complexity criterion is *evaluative* (good generative art sits between pure order and pure noise); using it as an ideation prompt risks importing his aesthetic preference. The plugin offers it as a *parameter to consider*, not as a quality criterion.
- **Contested in:** the effective-complexity criterion is one aesthetic position among several; competing positions privilege specific kinds of order (highly-rule-based work like LeWitt) or specific kinds of disorder (chance / Cage). See also Tension §T4.
- **Hook:** `provoke` ("Where on the order ↔ disorder axis is this idea? What if you moved it?"); `lineage`.

### D5. Margaret Boden & Ernest Edmonds (2009) — "What is generative art?", *Digital Creativity* 20(1–2) — generative-art taxonomy
- Proposes 11 categories of generative / computer art (Ele-art, C-art, D-art, CA-art, G-art, CI-art, Evo-art, R-art, I-art, CG-art, VR-art) distinguishing by *what is computed*, *whether autonomy is involved*, and *whether interaction is involved*.
- **Ideation mechanism:** typology forces the artist to specify exactly *which* sense of "generative" or "interactive" their work claims, defeating the common over-claim.
- **Authentic Practice Boundary:** taxonomies date. The 11-category scheme from 2009 may not capture contemporary AI / LLM / diffusion-model art cleanly; the artist may need to argue *for a new category* rather than fit into an existing one.
- **Contested in:** taxonomies are perpetually contested; the *fact of category multiplicity* is itself the value of consulting this entry, not the specific 11.
- **Hook:** `brief` (force a category claim and require an anchor); pairs with `creative_art_terminology_glossary.md`.

### D6. Christiane Paul (2003 *Digital Art*, 1st ed.; subsequent expanded editions; ed. 2016 *A Companion to Digital Art*) — **digital-art curatorial perspective**
- Curator's survey of digital / new-media art organizing the field by *forms* (installation, software, net.art, virtual, sound) and *themes* (artificial life, telepresence, body, surveillance, database). Identifies recurring conceptual provocations of the field.
- **Ideation mechanism:** thematic catalog acts as a *prompt library* — the artist can locate their nascent idea against established digital-art themes and either align with or push against them.
- **Authentic Practice Boundary:** a curator's survey is a *snapshot* of the field at the survey's date; the plugin's use of Paul as a theme library inherits whatever the canon was when Paul wrote, with associated training-data bias.
- **Contested in:** any single curatorial survey is a partial view of the field. Counter-perspectives (e.g. *Decentering Curation* lineage; non-Western curatorial surveys) widen the field. Use with the canon-bias disclosure.
- **Hook:** `lineage` (theme + form positioning, with bias disclosure); `provoke` (a theme card the artist hasn't considered).

### D7. Edmond Couchot & Frank Popper — **art-and-technology lineage**
- Frank Popper (1993 *Art of the Electronic Age*; 2007 *From Technological to Virtual Art*) traces a continuous lineage from kinetic and luminous art through cybernetic, video, and digital / virtual art, with the through-line of the artist's engagement with technology as medium and subject. Edmond Couchot (key works in French, e.g., 1998 *La Technologie dans l'art* and 2003 *L'Art numérique* with Norbert Hillaire) frames digital art around dialogue / uncertainty between human and machine ("commutation"). **(verify)** specific term-translations and chapter claims for Couchot — sources are primarily Francophone and not all are in widespread English translation.
- **Ideation mechanism:** provides a historical *positioning vocabulary* (kinetic → cybernetic → video → digital → virtual → networked) — the artist can locate their move within this lineage.
- **Authentic Practice Boundary:** the lineage as drawn is *European*, heavily French / German, with limited engagement with non-Western media-art histories. East-Asian media art (E1 Paik onward) is not in Popper / Couchot's main narrative.
- **Contested in:** the linear / progressive shape of the Popper / Couchot lineage (each phase superseding the prior) is contested by media archaeology (Huhtamo & Parikka 2011 — verify), which proposes non-linear, return-and-detour readings of media history.
- **Hook:** `lineage` primarily, with explicit pairing with East-Asian sources (E1, E2) when the artist's work is in or near East-Asian context.

### D8. Simon Penny (2017) — *Making Sense: Cognition, Computing, Art, and Embodiment*
- Argues for an **embodied / situated / enactive** epistemology of art-and-engineering practice, **against** the dominant computational / representational paradigm. Builds on the author's decades of robotic and interactive art practice. Ideation grounded in *sensorimotor engagement*, not symbol manipulation.
- **Ideation mechanism:** reframes the technical art-making question from "what should the system represent?" to "what should the embodied encounter be?" — body-first ideation for interactive / robotic work.
- **Authentic Practice Boundary (substantive — restored from v0.1):** Penny's argument is **directly aimed at exactly the representational paradigm that LLMs implement**. The v0.1 plugin sanitized this entry by treating Penny as a friendly hook for "body-first ideation"; v0.2 restores the critical edge: *Penny's position is one the plugin must answer to, not borrow from*. The plugin's response is the §1.3 cognitive-scaffold framing (POSITIONING.md): the plugin is positioned as a *propositional articulation* scaffold operating *adjacent to* embodied practice, not as a substitute. Penny's critique remains the strongest single attack on the plugin's existence, and the v0.2 reframe (from "ideation engine" to "pre-studio articulation scaffold") is the operational response.
- **Contested in:** Penny's enactive-epistemology position is itself contested by more representationalist cognitive-science positions; the plugin's substrate (an LLM) implicitly takes a representationalist side that Penny argues against. The plugin acknowledges this tension explicitly in Tensions §T1.
- **Hook:** `socratic` ("Describe the encounter from the participant's body, not from the system's behavior" — *and* note in the response that the plugin can ask the question but cannot itself perform the embodied work); `brief`.

### D9. Anthony Dunne & Fiona Raby (2013) — *Speculative Everything: Design, Fiction, and Social Dreaming* — **Speculative Design**
- Design used to ask *what-if* questions about preferable, plausible, possible, and probable futures (the **PPPP cone**, after Stuart Candy / Hancock & Bezold). Diegetic prototypes and design fictions materialize alternative futures as discursive objects.
- **Ideation mechanism:** what-if scenario generation as a structured ideation move; the cone of futures gives four registers in which to pitch the scenario.
- **Authentic Practice Boundary:** speculative design's *strongest* moves are *materialized* (props, films, exhibitions, design fictions) — diegetic prototypes that make the future encounter-able. The plugin's `provoke` mode produces *language* what-ifs; the artist must materialize them for the speculative-design move to land.
- **Contested in:** speculative design has been critiqued (e.g. by the design-justice lineage — Costanza-Chock 2020 *Design Justice*, verify) for the often-unmarked positionality of who gets to imagine which futures.
- **Hook:** `provoke` ("What's the preferable-vs-probable version of this idea?"); `brief` (state the work as a speculative scenario; note Costanza-Chock's positionality critique).

---

## E. Korean / East Asian Context

> **Sub-section positionality note (see also §0).** This section is currently 3 entries and is the area where the v0.2 reference layer is *most* under-developed. The v0.2 plan (synthesis spec §3 point 5) is to expand to 5–7 verified entries, ideally via consultation with working Korean media-art curators / scholars. The conservative `(verify)` discipline below reflects the maintainer's commitment not to fabricate authority where it isn't earned; expansion will follow library and consultation work.

### E1. Nam June Paik (백남준) (1963 *Exposition of Music – Electronic Television*, Wuppertal; 1995 *Electronic Superhighway*) — **TV as canvas / random access**
- Paik's early gestures established the cathode-ray tube as a plastic material (magnet-deformed images), and *Random Access* (1963) — magnetic tape strips on a wall played by hand with a detached tape head — proposed non-linear, viewer-determined access as a compositional principle long before "interactive media" was a term.
- **Ideation mechanism:** treats the technical apparatus's *constraint* (linearity, broadcast, single-channel) as the ideation target — invert the constraint to find the work. Aligns with Boden's transformational creativity (changing the rule of the space).
- **Authentic Practice Boundary:** Paik's work is a *specific* historical-material practice; the plugin can use his apparatus-inversion logic as a heuristic but does not substitute for engagement with the Nam June Paik Art Center research catalogues and the Korean / Fluxus media-art literature.
- **Contested in:** Paik's reception has shifted across decades; recent Korean scholarship has worked to recover the Korean-language and Korean-context dimensions of his practice often flattened in Western reception.
- **Hook:** `provoke` ("What is the default constraint of your apparatus? Invert it."); `lineage` (Korean / global media-art positioning).

### E2. East Asian aesthetic concepts — **의(意 yi) / 기(氣 qi) / 여백(餘白 yeobaek)**
- **의(意)** — intent, conception, the *idea* a work carries (the artist's conception preceding and surviving the brushstroke; classical East Asian painting and calligraphy theory treats yi as primary, brush-and-ink as its trace). **(verify)** for the specific canonical sources — relevant treatises include Chinese classical texts e.g. Jing Hao's *Bifa ji* (筆法記, 10th c.) and Su Shi's writings on literati painting, and Korean Joseon-period painting theory.
- **기(氣)** — vital energy / breath / dynamism that should animate brushwork and composition; Xie He's **Six Principles of Chinese Painting** (謝赫六法, 6th c.) names **氣韻生動 (qiyun shengdong)** — "spirit resonance / life-movement" — as the first principle.
- **여백(餘白)** — "remaining white" / negative space / pregnant emptiness as compositional element; not absence but *charged emptiness* that activates the marked area. Strong in Korean Joseon painting and continues in modern Korean abstraction (e.g., Dansaekhwa 단색화 discourse). **(verify)** for specific scholarly framings — the term is widely used in Korean art writing but canonical academic citations are diffuse.
- **Ideation mechanism:** trio reframes ideation as **conception (yi) → energetic register (qi) → compositional reserve (yeobaek)** — what is the intent, what is the energy it must carry, what is deliberately left out / unfilled?
- **Authentic Practice Boundary (substantive):** the *yeobaek* principle is **structurally hostile** to the plugin's default behavior (LLMs are trained to fill space with text). The plugin's use of yeobaek as a tradition tag is *aspirational and contradictory*: the tradition itself would judge the plugin's articulation work as the wrong instinct. This contradiction is named here rather than concealed (see Tensions §T5). Honest use: the plugin can *ask the artist what to leave out*, but cannot model yeobaek; the answer is the artist's.
- **Contested in:** the East-Asian aesthetic canon is itself plural and contested; *literati* painting theory differs from court-painting theory differs from contemporary Korean art-writing. The plugin should not present a unified "East-Asian aesthetic" framework.
- **Hook:** `socratic` (three-question prompt around yi / qi / yeobaek when working with East Asian aesthetic lineage); `lineage`.

### E3. Yuk Hui (許煜) (2016, *The Question Concerning Technology in China: An Essay in Cosmotechnics*; 2019 *Recursivity and Contingency*; 2021 *Art and Cosmotechnics*) — **cosmotechnics**
- Argues that there is no single, universal "technology" — instead, multiple cosmotechnics (configurations of technical relation, ethics, and cosmology), of which the modern-Western technological condition is one. Calls for a "technodiversity" parallel to biodiversity.
- **Ideation mechanism:** provides a philosophical vocabulary for Korean / East-Asian media artists who want to position their practice *neither* as derivative of Western media-art history *nor* as reactive ethnonationalist alternative, but as a different cosmotechnical configuration. Particularly relevant for AI / generative-art work that wants to engage non-Western technical philosophies.
- **Authentic Practice Boundary:** cosmotechnics is a *philosophical position*, not a method. The plugin can tag work that engages this tradition but does not perform cosmotechnical analysis itself.
- **Contested in:** the cosmotechnics thesis is debated (within Continental philosophy, postcolonial studies, philosophy of technology) — for the strength of the claim that *the* Chinese cosmotechnics is recoverable from classical sources, and for the operational specificity of "technodiversity". The plugin treats it as one strong position within a contested field, not consensus.
- **Hook:** `lineage` (especially for AI / generative-art work positioned in East-Asian context); `brief` (cosmotechnical framing as one available situated-argument option).

### E4–E7. Further Korean / East-Asian sources — **expansion planned for v0.2 (Phase 1, library + consultation work)**
- Nam June Paik Art Center research catalogues — specific entries to be verified and added.
- Kim Hong-hee (김홍희) — specific titles on Korean media-art curation to be verified and added.
- Lee Yongwoo (이용우) — specific writings on Korean contemporary art to be verified and added.
- 1990s–2000s Korean media-art lineage — Forum A, early Gwangju Biennale Korean artists; specific names and entries pending verification.
- Korean academic journal sources (*현대미술학논문집* and adjacent) — specific issues / articles to be verified and added.
- Hwang Doojin (황두진) — primarily an architect; framing him as an art-ideation theorist is **(verify)** — do not cite without confirmation that the user's reference is the same Hwang Doojin and that an art-ideation contribution can be cited.
- Su-Mei Tse — Luxembourg-based artist of Chinese descent, not Korean; cited for her cross-cultural practice but should not be miscategorized as a Korean theorist. **(verify)** before citing as a methodology source.
- *Optional Western/diaspora sources adjacent to East-Asian media art:* Joline Blais & Jon Ippolito (2006 *At the Edge of Art*) frequently engages Asian media-art; useful as secondary positioning.
- **Hook:** `lineage` for Korean / East Asian media-art positioning, contingent on per-source verification.

---

## F. HCI / AI-Creativity-Support-Tools Prior Art (new in v0.2)

This section is **not a methodology reference for the artist** — it is for the maintainer / paper author / reviewer to position art-project against the existing landscape of LLM-based creativity-support tools. Each entry is shorter than A–E and is here for citation, not for ideation hook.

### F1. Shneiderman (2007) — "Creativity support tools: Accelerating discovery and innovation", *Communications of the ACM* 50(12)
- Eight design principles for CSTs (support exploration; low thresholds, high ceilings, wide walls; many paths and styles; collaboration; open interchange; simple-as-possible / powerful-as-needed; black-box transparency; evolutionary refinement). art-project's position vs the eight is scored in the synthesis spec §1 (HCI Critique Q1.1).

### F2. Cherry & Latulipe (2014) — "Quantifying the creativity support of digital tools through the Creativity Support Index", *ACM TOCHI* 21(4)
- The **CSI** — six factors (Enjoyment, Exploration, Expressiveness, Immersion, Results Worth Effort, Collaboration) measured via paired comparisons + agreement items. art-project's evaluation protocol (synthesis spec §5.1, Study 1) uses CSI with two documented adaptations (Expressiveness reframed; Collaboration dropped).

### F3. Frich, MacDonald Vermeulen, Remy, Biskjaer & Dalsgaard (2019) — "Mapping the landscape of creativity support tools research", *CHI 2019*
- Field-defining survey of CST research. Finds the field understudies user agency (relevant for art-project's IRON-RULE-on-human-decision commitment).

### F4. Yuan, Coenen, Reif & Ippolito (2022) — "Wordcraft: Story writing with large language models", *IUI 2022*
- LLM-assisted creative writing tool. Tested writers' attribution practices and control preferences. Relevant for art-project's *tradition tag* attribution-UI choice (HCI Q4).

### F5. Gero, Liu & Chilton (2022) — "Sparks: Inspiration for science writing using language models", *DIS 2022*
- LLM-generated "spark" sentences for scientific writing. Tested attribution-UI variants; found attribution salience affects sense of authorship. The strongest direct prior art for art-project's `provoke` mode and the *tradition tag* footnote default.

### F6. Mirowski, Mathewson, Pittman & Evans (2023) — "Co-writing screenplays and theatre scripts with language models", *CHI 2023* (Dramatron)
- Hierarchical LLM theatre script generation, evaluated with playwrights. Generative counterpoint to art-project: Dramatron makes the artifact, art-project does not.

### F7. Chung, Kim, Cha, Jeon, Cho, Park, Lee & Bareiß (2022) — "TaleBrush: Sketching stories with generative pretrained language models", *CHI 2022*
- Sketch-based control of LLM story generation; co-creative in Davis's (F10) sense. Cited as contrast.

### F8. Wu, Terry & Cai (2022) — "AI Chains: Transparent and controllable human-AI interaction by chaining large language model prompts", *CHI 2022*
- Chained-prompt LLM tasks. art-project's v0.1 `full` mode chain was the same pattern; v0.2 reshape (long-running project file, sessions days/weeks apart) departs from this in alignment with Smith & Dean (C6).

### F9. Compton & Mateas (2015) — "Casual Creators", *ICCC 2015*; Compton (2019) — "Generative Art and Computational Creativity"
- *Casual Creators* frame distinguishes tools that *generate outputs* from tools that *generate possibility-space*. art-project is the latter (it generates language as articulation possibility-space, not artwork candidates).

### F10. Davis, Hsiao, Singh, Li & Magerko (2016) — "Empirically studying participatory sense-making in abstract drawing with a co-creative cognitive agent", *IUI 2016*
- Defines **co-creative system** as one that contributes its own creative agency to a shared artifact. art-project is **not** co-creative in this sense (it does not contribute to the artwork — the artwork doesn't exist at ideation-time).

### F11. Kantosalo & Toivonen (2016) — "Modes for creative human-computer collaboration: Alternating and task-divided co-creativity", *ICCC 2016*
- Formalizes co-creativity into alternating vs task-divided modes. art-project is neither (it is a *support tool* in Shneiderman's sense, not a co-creative system).

### F12. Deterding, Hook, Fiebrink, Gillies, Gow, Akten, Compton, Cook & Nack (2017) — "Mixed-initiative creative interfaces", *CHI 2017 Workshop*
- Defines **MICI** = systems where both human and machine can take initiative. art-project explicitly **rejects** mixed-initiative in v0.1 (turn-taking, IRON RULE), with Frich (F3) and Draxler (F13) cited in support of artist autonomy.

### F13. Draxler, Werner, Lehmann, Hoppe, Schmidt, Buschek & Welsch (2024) — "The AI ghostwriter effect: When users do not perceive ownership of AI-generated text but self-declare as authors", *ACM TOCHI* **(verify exact volume / DOI)**
- Empirical finding that AI-assisted writing users underclaim AI contribution (ghostwriter effect). Cited by art-project for the stay-rough default on `brief` mode and the footnote-level tradition-tag salience.

### F14. Amabile (1982) — "Social psychology of creativity: A consensual assessment technique", *JPSP* 43(5)
- **CAT** (Consensual Assessment Technique) for evaluating creative output via expert raters. art-project's Study 2 (synthesis spec §5.2) uses CAT to rate Concept Briefs.

### F15. Lu et al. (2024) — *The AI Scientist: Towards fully automated open-ended scientific discovery* **(verify final venue / arXiv id)**
- Autonomous-pipeline scientific-discovery system. Cited as contrast: art-project explicitly under-claims agency (IRON RULE, human decision) whereas AI Scientist over-claims it.

### F16. Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji & Gebru (2019) — "Model Cards for Model Reporting", *FAccT 2019*
- Model-card disclosure format. art-project's measured-harm disclosure (synthesis spec §6 + POSITIONING.md) follows this template.

### F17. Bender, Gebru, McMillan-Major & Shmitchell (2021) — "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?", *FAccT 2021*
- The training-data-canon and propagation-of-bias arguments cited in the lineage-mode bias disclosure.

### F18. Zimmerman, Forlizzi & Evenson (2007) — "Research through Design as a Method for Interaction Design Research in HCI", *CHI 2007*
- Design-research methodology tradition that legitimizes artifact-papers without user-study (used by art-project v0.1 to frame the Study-1-deferred publication path).

---

## Tensions — explicit inter-entry conflicts the reference layer holds without flattening (new in v0.2)

The reference layer mixes positions that do not agree. v0.1 papered over the disagreements; v0.2 names them. Each tension is a place where the plugin's design must take a side, hold both sides, or rotate between them by context.

### T1. Boden's formalism (A1) vs Borgdorff's situatedness (C4) — *is ideation a search-space operation or a not-yet-knowing?*

Boden's typology treats creativity as operations on representational *conceptual spaces*; transformation = changing the space's rules. Borgdorff treats artistic-research ideation as articulating *not-yet-knowing* that the artwork itself will eventually embody — *not* a search-space operation but a pre-articulate orientation. The plugin uses both: Boden for the `provoke` mode's typology of attack angles, Borgdorff for the `socratic` mode's question "what can only be discovered by making this work?". **Position the plugin takes:** *use both contextually*, but acknowledge that Borgdorff would diagnose Boden's framework as importing a propositional psychology onto pre-propositional ground. The plugin's footnote-level tradition tags make the switch between frames visible.

### T2. IDEO Design Thinking (B1) vs Sullivan / Barrett & Bolt (C5, C7) — *instrumental vs epistemic framing of ideation*

Design Thinking treats ideation as an *instrumental* phase (divergence then convergence, in service of a downstream user need). Sullivan and Barrett & Bolt treat ideation-as-practice as *epistemic* (the activity itself is knowledge-producing, with no separable "outcome-for-user"). The plugin's `brief` mode reaches toward an *outcome document*, which leans instrumental; the `socratic` mode reaches toward articulating not-yet-knowing, which leans epistemic. **Position the plugin takes:** the modes are *not* arranged in a pipeline from epistemic to instrumental; the artist can re-enter `socratic` from `brief` at any time. The IDEO-style outcome-orientation is offered as a *technique within `brief`*, not as the operative frame for the whole plugin.

### T3. Cage's chance-as-erasure-of-taste (C11) vs Bogart's Viewpoints-as-trained-attention (C8) — *opposite stances on the artist's pre-formed perception*

Cage's procedures *remove* the artist's taste from determinative decisions; Bogart's Viewpoints train and *sharpen* the artist's attention. Both are cited in `provoke`. **Position the plugin takes:** offer both as alternative attack angles when the artist is stuck — Cage when the artist suspects their taste is the problem, Bogart when the artist suspects their attention is the problem. The diagnosis is the artist's; the plugin should never default to one.

### T4. Galanter's effective-complexity criterion (D4) vs LeWitt's idea-first (C2) — *incompatible generative-art aesthetics*

Galanter's criterion rewards generative work that sits between pure order and pure noise; LeWitt's rule-based work often sits explicitly in *high-order* territory (the rule's clarity is the value). Galanter would, on his criterion, judge much classical LeWitt work as aesthetically thin; LeWitt would judge Galanter's criterion as importing a science-of-complexity aesthetic onto conceptual ground. The plugin's `provoke` mode cites both. **Position the plugin takes:** make the disagreement visible to the artist when both are activated in the same session; do not adjudicate.

### T5. Western-PaR articulation requirement (Frayling / Borgdorff / Sullivan) vs East-Asian yeobaek's reserve-for-the-unsaid (E2) — *should everything be put into language?*

PaR vocabulary (Frayling INTO/THROUGH/FOR; Borgdorff dual-discourse; Sullivan three practices) **requires articulation** — the research must be verbalizable for academic standing. The East-Asian *yeobaek* principle holds that the *unsaid* is constitutive of the work's meaning; over-articulation kills the work. The plugin, by producing text articulation as its output, structurally favors the PaR side. **Position the plugin takes:** name this contradiction (this entry is the operational form of naming it); in `socratic` and `brief` modes, include explicit "what does this work refuse to say?" / "what is the *yeobaek* of this Brief?" fields; preserve the artist's right to leave fields empty (the stay-rough default makes this possible).

### T6. Tradition-tag-as-affinity (this plugin's claim) vs methodology-as-embodied-craft (Barrett & Bolt C7; Cage C11; Penny D8; Practicing-Artist critique) — *does an LLM tag honor a tradition or borrow its authority?*

The plugin claims its tradition tags indicate *style affinity* and *prompt grounding*, not causal generation (see "Tradition tag, not provenance" scope note above). The substantive counter-claim — that methodologies like Oblique Strategies (constitutively physical and finite), Cage's chance operations (constitutively temporal), LeWitt's instructions (constitutively human-authored), Bogart's Viewpoints (constitutively bodied) — *cannot* be honored by an LLM tag, because the constitutive features are precisely what the tag elides. **Position the plugin takes:** acknowledge the critique in the Authentic Practice Boundary on each method (added in v0.2); design the plugin to *redirect to the source* rather than substitute for it (e.g. the `provoke` mode goes silent after an Oblique-style provocation rather than interpret it; the Cage chance method is described, not executed; the LeWitt instruction is prompted from the artist, not authored for them). The critique is not fully answerable by the v0.1 plugin and is *named* rather than resolved.

---

## Meta-observation: cross-cutting ideation mechanisms (revised in v0.2 — inductive coding rationale)

> **Methodological note (new in v0.2, addressing Methodologist Critique Q4 point iii).** The five (plus one) mechanisms below are derived by **inductive coding** of the entries in §§A–E. Each entry was coded on three dimensions: (a) *what the mechanism operates on* — a constraint, a domain pairing, a position-claim, a temporal-ordering rule, or a material interlocutor; (b) *what the artist does in response* — accepts displacement, performs analogy, takes a stance, defers judgment, listens; (c) *where the locus of ideation activity sits* — in language, in operation, in the social field, between phases, in material. The five clusters are emergent from this coding; the sixth (Field/jury simulation) is weaker because it has fewer entries (5) and most of those entries (B3 Six Hats, B5 Brainwriting, C10 Saltz) are workshop / criticism techniques rather than method-foundational. The coding table is given in Appendix A. An alternative theoretical anchor would be Glăveanu's (2010) 5A model — actor / action / artifact / audience / affordance — which the inductive clusters partially map onto (Constraint-as-displacement ↔ affordance; Heterogeneous-domain ↔ action; Lineage-positioning ↔ audience + actor; Generation-evaluation separation ↔ action's temporal shape; Material-as-interlocutor ↔ artifact; Field/jury simulation ↔ audience). v0.2 takes the inductive-coding option as the primary justification; future iterations may anchor to Glăveanu more directly.

Pulling across A–E with the coding above, five mechanisms recur. These form the **backbone for the art-project mode design** — each mode in the skill activates at least one.

1. **Constraint-as-displacement** — deliberately imposing an under-specified, alien, or aleatory constraint to displace the artist from a fixated default. *Examples:* Oblique Strategies (C1), Cage's chance operations (C11), de Bono's PO (B3), Eno-influenced Reas / Fry rule sets (D2), Paik's apparatus-constraint inversion (E1). → **`provoke` mode is the natural home.**

2. **Heterogeneous-domain collision** — forcing an analogy or graft between the artist's domain and an alien one (cognitive, material, cultural, technical). *Examples:* Koestler's bisociation (A3), TRIZ analogical principles (B4), SCAMPER's combine / adapt operators (B2), Csikszentmihalyi's domain-crossing (A4). → **`provoke` + `rehearsal` (a foreign-domain voice).**

3. **Lineage-positioning** — locating the nascent idea within an art-historical / methodological / cultural lineage so that "novelty" is defined relationally, not in a vacuum. *Examples:* Frayling's INTO/THROUGH/FOR (C3), Sullivan's contextualist inquiry (C5), Manovich's new-media principles (D1), Boden & Edmonds taxonomy (D5), Paul's themes (D6), Popper / Couchot lineage (D7), East-Asian aesthetic vocabulary (E2), Yuk Hui cosmotechnics (E3). → **`lineage` mode (with the v0.2 constraint that the artist supplies initial candidates first); outputs feed the Concept Brief's lineage anchor.**

4. **Generation-evaluation separation** — explicitly de-coupling the *making / proposing* of proto-ideas from the *judging* of them, on the cognitive evidence (Geneplore, A2/A5) and the practitioner ethos (Corita Kent C9; Saltz C10) that premature evaluation suffocates generation. *Examples:* Geneplore's generate / explore split (A2, A5), Design Thinking's diverge / converge (B1), brainwriting's silent-then-discuss (B5), Six Hats' role separation (B3), Corita Kent rule 8 (C9), Saltz's "embed thought in material" (C10). → **`socratic` mode enforces this temporally; never asks "is this good?" before "what is it?". The IRON RULE on auto-convergence under exploratory intent is the operational form.**

5. **Material / system as interlocutor** — letting the medium, the system, or the body talk back; ideation forms *through* the encounter with material / code / space rather than prior to it. *Examples:* Barrett & Bolt's experimental gesture (C7), Vorkurs (C12), Reas / Fry computational primitives (D2), Whitelaw's metacreation (D3), Penny's embodied epistemology (D8), East-Asian qi / yeobaek-as-compositional-element (E2), Smith & Dean's iterative cyclic web (C6). → **`socratic` and `provoke` modes support material-first prompts ("pick up the material first") and re-entry; the v0.2 `full` mode's cross-session project file is the operational form of "letting material talk back over weeks".**

A sixth, weaker, mechanism worth flagging:

6. **Field / jury simulation** — testing the embryonic idea against simulated gatekeepers (curator, peer, critic, public) before committing. *Examples:* Csikszentmihalyi's field (A4), Six Hats roles (B3), brainwriting's parallel voices (B5), Saltz as critic-voice (C10). → **`rehearsal` mode (renamed from `panel` in v0.2 to commit to method-not-evaluation; carries mandatory disclaimer and persona-collapse detector).** Note: this mechanism is weakest because the simulation cannot replicate the *relational history* real gatekeepers carry (Devil's Advocate Attack 4); `rehearsal` is rehearsal for the encounter, not the encounter itself.

---

## Mounting matrix (mode × methodology, condensed, v0.2)

| Mode | Primary tradition tags wired |
|---|---|
| **socratic** | A1, A2, A5, C2, C4, C6, C9, C10, C11, D8, E2 |
| **provoke** | A1, A3, A5, B2, B3, B4, B5, C1, C7, C8, C11, C12, D2, D4, D6, D9, E1 |
| **lineage** | A4, B4, C3, C5, D1, D3, D4, D5, D6, D7, E1, E2, E3, E4–E7 (pending expansion) |
| **brief** | A5, B1, C2, C3, C5, D1, D3, D5, D8, D9, E3 |
| **rehearsal** *(renamed from panel)* | A3, A4, B3, B5, C10 |
| **full** *(cross-session project file)* | C6 primary (iterative cyclic web); all others as re-entry |

---

## Notes on use in `art-project`

- This file is loaded by the ideation skill's reference loader. Entries are kept *short* so the full set fits in the working context; deeper engagement should re-fetch the named primary sources rather than expand this file.
- Where an entry is tagged **(verify)**, the skill must not assert the claim downstream without independent confirmation. The L3 citation-faithfulness gate applies unchanged.
- Hooks suggest *where* in the plugin a tradition can be mounted; they do not force exclusive assignment — most traditions span 2–3 modes and the mounting matrix above is the canonical multi-mount reference.
- East-Asian and Korean entries (§E) are deliberately conservative and currently under-developed; expansion is v0.2 Phase 1 work with library + consultation effort.

---

## Appendix A — Inductive coding of §§A–E entries on the three dimensions

(Coding rationale for the 5+1 mechanisms above. Sketch form; fully populated table is v0.2 Phase 1 work.)

| Entry | (a) operates on | (b) artist does | (c) locus of activity | → mechanism cluster |
|---|---|---|---|---|
| A1 Boden | conceptual-space typology | diagnoses move-type | propositional | 1, 4 |
| A2 Geneplore | phase ordering | generates then explores | propositional / cognitive | 4 |
| A3 Koestler | domain pairing | performs collision | propositional | 2 |
| A4 Csikszentmihalyi | field-domain-person | positions self | social | 3, 6 |
| A5 Finke (preinventive) | ambiguity tolerance | makes incongruous proto-forms | cognitive | 4, 5 |
| B1 Design Thinking | divergence-convergence | stages ideation | propositional | 4 |
| B2 SCAMPER | transformation operators | mutates base | propositional | 1, 2 |
| B3 de Bono PO + Hats | aleatory premise + role | suspends judgment + role-plays | propositional | 1, 2, 4, 6 |
| B4 TRIZ | contradiction + principles | finds inventive principle | propositional | 1, 2 |
| B5 Brainwriting | parallel voices | builds on residue | social | 2, 4, 6 |
| C1 Oblique Strategies | aleatory constraint | interprets card | propositional + procedural | 1 |
| C2 LeWitt | rule-as-work | authors instruction | propositional | 1 (rule-as-constraint), 5 (rule-as-execution-engine) |
| C3 Frayling | meta-methodological typology | types own project | propositional | 3 |
| C4 Borgdorff | not-yet-knowing | articulates research question | propositional / pre-propositional | 4, 5 |
| C5 Sullivan | three stances | selects stance | propositional + social | 3 |
| C6 Smith & Dean | iterative cyclic web | re-enters | temporal / between phases | 4, 5 |
| C7 Barrett & Bolt | material engagement | listens to material | material | 5 |
| C8 Bogart Viewpoints | compositional axes | ideates per axis | material / temporal | 5 |
| C9 Corita Kent | ethos | separates make from judge | behavioral | 4 |
| C10 Saltz | aphoristic rules | unblocks identity | behavioral | 4, 6 |
| C11 Cage | chance procedure | executes procedure | procedural / temporal | 1, 4 |
| C12 Bauhaus Vorkurs | material primitives | explores systematically | material | 5 |
| D1 Manovich | new-media principles | specifies system | propositional | 3 |
| D2 Reas/Fry | primitive + rule | writes + runs code | material (code) | 1, 5 |
| D3 Whitelaw metacreation | meta-level system design | authors generator | propositional | 3, 5 |
| D4 Galanter complexity | order-disorder parameter | tunes complexity | propositional | 1 |
| D5 Boden & Edmonds taxonomy | category typology | specifies category | propositional | 3 |
| D6 Paul themes | curatorial theme library | locates within themes | propositional | 3 |
| D7 Popper/Couchot lineage | historical lineage | positions within | propositional / social | 3 |
| D8 Penny | embodied / sensorimotor frame | shifts to body-first | material | 5 |
| D9 Dunne & Raby | PPPP futures | pitches scenario | propositional | 1, 2 |
| E1 Paik | apparatus constraint | inverts | material | 1, 3 |
| E2 yi/qi/yeobaek | conception / energy / reserve | articulates trio | propositional + material | 4, 5 |
| E3 Yuk Hui cosmotechnics | technodiversity position | positions within East-Asian | propositional + social | 3 |

The clustering rule for the inductive 5+1 mechanisms: cluster on dimension (a) primarily; entries with multiple dominant (a) values appear in multiple clusters. The coding is the maintainer's; alternative codings are defensible and would yield slightly different cluster sets.
