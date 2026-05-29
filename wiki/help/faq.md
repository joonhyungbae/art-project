# FAQ

Quick answers to recurring questions. For the architectural rationale behind any of these, see the linked Philosophy or Reference page.

## Scope and positioning

### Is this an AI art generator?

No. The plugin produces **language** — questions, briefs, lineage maps, rehearsal transcripts — that the artist takes back to the studio. It never produces the artwork. See [Cognitive scaffold](../philosophy/cognitive-scaffold.md).

### Why not just use ChatGPT for the same thing?

You can, but the plugin enforces specific disciplines a general assistant does not: refusal to fabricate lineage, mandatory training-data bias headers, authentic-practice boundaries per cited tradition, no auto-convergence under exploratory intent, and architectural friction against repeated-rehearsal simulation-pedagogy harms. These are the framework's IRON rules. See [Modes overview](../modes/overview.md).

### Is the plugin meant for everyone?

No. It is scoped to artists for whom propositional articulation is a bottleneck (early-career, second-language, doctoral-candidate, deadline-pressured, collective). It is **unsuitable** (not suboptimal) for artists whose articulation is already fluent, and for traditions where articulation is constitutively unwanted (improvisational, ritual, oral). See [Measured harms](../philosophy/measured-harms.md) §6.

### Why "pre-studio articulation" and not just "ideation"?

The plugin accepts the strong critique that artistic ideation is non-linguistic, material, and inseparable from making (Penny, Ingold, Borgdorff). The propositional work *around* ideation — grant applications, doctoral expositions, residency proposals, collaborator briefings — is a different, separable phase that the plugin scopes itself to. See [Frayling typology](../philosophy/frayling-typology.md).

## Modes and routing

### Which mode do I use for what?

| Situation | Mode |
|---|---|
| Vague pull, no concept yet | [`socratic`](../modes/socratic.md) |
| Partial concept, stuck | [`provoke`](../modes/provoke.md) |
| Have candidate precedents, want extension | [`lineage`](../modes/lineage.md) |
| Have material, need a proposition document | [`brief`](../modes/brief.md) |
| Have a brief, stress-test before submission | [`rehearsal`](../modes/rehearsal.md) |
| Project across weeks or months | [`full`](../modes/full.md) |

Full table at [Modes overview](../modes/overview.md).

### Can I run multiple modes in one session?

In single-mode commands (`/art-project:brief`, `/art-project:provoke`, etc.) you can — but the plugin will refuse to *auto-pipeline* (e.g. it will not run `socratic → brief` back-to-back without your explicit re-trigger). In `/art-project:ideate` (full project file mode), the **one-mode-per-session** rule is architecturally enforced: the plugin will warn and require explicit override if you try.

### Why does `lineage` refuse to start until I name precedents?

Because lineage hallucination on long-tail sub-domains is the most common LLM lineage-tool failure mode, and artist-supplied initial candidates materially constrain the failure space. See [`lineage`](../modes/lineage.md). If you have no precedents, start with [`socratic`](../modes/socratic.md) or [`provoke`](../modes/provoke.md).

### What is the difference between `brief` and `rehearsal`?

`brief` produces the 10-field Concept Brief (the *document*). `rehearsal` stress-tests an existing brief by simulating four persona critics (Curator + Practitioner-peer + Theorist + Devil's Advocate). You generally do `brief` first, then `rehearsal`. Running `rehearsal` without a brief produces nothing useful.

## Outputs and data

### Where does my project file live?

For `/art-project:ideate` (full mode), the plugin tells you the path when you create the project file. Default name: `art-project-{slug}.md` in your current working directory. The file is yours; the plugin appends to it but does not direct it. See [`full`](../modes/full.md).

### Can I export to Word / PDF?

The plugin produces Markdown by default. PDF / DOCX export is deferred to a future version (v0.2+). In the meantime, pipe the output through Pandoc or a similar tool.

### Does the plugin send my project file anywhere?

It is processed through the Claude API like any Claude Code session input. It is not transmitted to any other service. The plugin itself does not phone home.

### What language will the output be in?

Whatever language you input. Korean input produces Korean output; English input produces English. You can mix mid-session (write rough material in Korean, then say "write this up in English" when you reach `brief` mode).

## Licensing and contribution

### Can I use this commercially?

The plugin is CC-BY-NC 4.0. Non-commercial use is permitted; commercial use requires separate licensing. Contact the maintainer.

### Can I extend the tradition-tag corpus?

Yes. See [Contributing](../contributing.md) §1. Especially welcomed: non-anglophone traditions, oral methodologies, Global South practices. The Authentic Practice Boundary field is mandatory for every new tag.

### Can I propose a new harm class?

Yes. See [Contributing](../contributing.md) §2. The current 6 classes are not exhaustive.

## Architecture details

### What is an Authentic Practice Boundary?

For every tradition the plugin cites (Oblique Strategies, Cage, LeWitt, Viewpoints, etc.), the plugin pairs the citation with an explicit declaration of what the cited method requires that the AI does *not* simulate. See [Authentic Practice Boundaries](../reference/authentic-practice-boundaries.md) for examples.

### Why does `rehearsal` warn me after the second use on the same concept?

Architectural friction against simulation-pedagogy harm (Schön 1983): artists who rehearse repeatedly on simulation may train themselves to defend against the simulated kind of critique, which is structurally different from the critique they will actually face. The friction is not advisory; it fires every time after the threshold. See [`rehearsal`](../modes/rehearsal.md) and [Measured harms](../philosophy/measured-harms.md) §3.

### What is "stay-rough default"?

When `brief` mode pulls material from prior modes (e.g. fragments from a `socratic` session), it preserves the artist's voice verbatim — it does not smooth fragments into AI-statement register. Empty fields are reported as `[gap, not in input]` rather than fabricated. This is the no-fabrication discipline. To request smoothing for submission, use `--polish` opt-in flag. See [Concept Brief schema](../reference/concept-brief.md) §Stay-rough default.

## Versions and updates

### How do I know what version I have?

Run any plugin slash command; the version line appears in the preamble. Or check the [CHANGELOG](https://github.com/joonhyungbae/art-project/blob/main/CHANGELOG.md).

### How do I update?

```text
/plugin update art-project
```

### Will updates break my existing project files?

Project files follow a stable Markdown format; updates extend but do not break. If a mode is renamed (e.g. `panel → rehearsal` in v0.2), the plugin handles legacy mode-name references gracefully.

## Where this FAQ stops

This is a quick-answer index, not a manual. For each topic above, the linked Modes / Reference / Philosophy page is the canonical source. If a question recurs that is not here, [Contributing](../contributing.md) §3 explains how to add it.
