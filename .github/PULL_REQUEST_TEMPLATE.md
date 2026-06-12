<!--
Thanks for sending a pull request. Please confirm the boxes below before
requesting review. PRs that touch architectural commitments should have an
issue opened first (label: needs-design-review) so the discussion is public.
-->

## What changed

<!-- One-paragraph summary. What did you change, and what file paths are affected? -->

## Why

<!-- Tie to a concrete artist need or a documented gap. Link the issue if there is one. -->

## Scope

- [ ] Tradition-tag addition (new entry in `shared/references/art_ideation_methodology.md`)
- [ ] Documentation / wiki correction
- [ ] Command-file clarification (no behaviour change)
- [ ] Agent honesty / drift correction
- [ ] Translation / internationalisation
- [ ] Typo / formatting
- [ ] Other — describe:

> PRs that change architectural commitments (the five v0.2 commitments, the IRON rules, the Authentic Practice Boundary schema) are out of scope for direct PRs; please open an issue first.

## Architectural commitment check

If your change touches any mode's output, confirm it respects:

- [ ] **Generation–evaluation separation** — generative cells stay generative
- [ ] **Tension over ranking** — no introduced ranking of provocations, lineage, briefs, or critiques
- [ ] **Lineage with opposition** — artist-supplied seed preserved; opposition tag still emitted
- [ ] **Formative-not-decisional rehearsal** — disclaimer + persona-collapse detector + friction preserved
- [ ] **Tradition-tag with Authentic Practice Boundary** — every cited method declares what the plugin defers to human execution

Not all five apply to every PR; check the ones relevant to your scope.

## Data hygiene

- [ ] **No pilot data added under `eval/pilot/`** (the whole directory is gitignored for copyright + double-anonymous reasons; reproducibility data is held locally until paper acceptance).
- [ ] **No copyrighted source text added** under any path (paper transcriptions, exhibition records, gallery materials).
- [ ] **No secrets or credentials.** API keys live in `.env` (gitignored). `.env.example` is the only tracked env file.
- [ ] **No absolute paths** (`/home/<user>/…` etc.) in tracked files.

## Bilingual content

- [ ] (If edited English wiki content) Korean counterpart on the apesuite wiki at least flagged for translation (link to apesuite issue):

## Tests / verification

<!-- For tradition-tag additions: which mode were you able to confirm the tag surfaces in?
     For documentation: did you cross-link from the wiki?
     For agent corrections: was the change a runtime fix or a documentation honesty pass? -->

## Code of Conduct

- [ ] I have read [`CODE_OF_CONDUCT.md`](../CODE_OF_CONDUCT.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md) and agree to follow both.
- [ ] My contribution is released under [CC-BY-NC 4.0](../LICENSE), the same license as the project.
