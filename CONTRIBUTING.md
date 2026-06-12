# Contributing to art-project

Thanks for your interest. This document is a short pointer; the substantive
guidance lives on the wiki.

## Three things to know first

1. **art-project is opinionated, not configurable.** Six modes, one skill,
   a tradition-tag reference layer with Authentic Practice Boundaries, and
   five architectural commitments (generation-evaluation separation;
   tension-over-ranking; lineage-with-opposition; formative-not-decisional
   rehearsal; tradition-tag-with-Authentic-Practice-Boundary). New features
   are evaluated against those commitments, not against general convenience.
   See [`POSITIONING.md`](POSITIONING.md) and the
   [v0.2 synthesis spec](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).

2. **Tradition-tag additions are the easiest contribution.** New entries to
   [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md)
   are welcome — especially from underrepresented traditions
   (non-anglophone, oral, ritual, ceremonial). Each entry must declare its
   **Authentic Practice Boundary**: what the cited method requires that the
   plugin defers to human execution. Without that field, the entry is not
   merge-ready.

3. **Companion paper is in peer review.** A reconstruction-benchmark audit
   paper is in submission to *Digital Creativity*. The plugin itself is
   public; the paper draft and per-case reproducibility data are held
   locally and will be released through the paper's supplementary-materials
   channel after acceptance. Contributions to the plugin can proceed
   independently of that review timeline.

## Where to start

| You want to … | Go to |
|---|---|
| Report a bug | [open an issue](https://github.com/joonhyungbae/art-project/issues/new/choose) using the **Bug report** template |
| Suggest a feature or new mode | [open an issue](https://github.com/joonhyungbae/art-project/issues/new/choose) using the **Feature request** template |
| Add a tradition tag | follow the schema in [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md); send a PR |
| Translate the wiki to a new language | wiki contribution guide: <https://apesuite.org/plugins/#/art-project/en/contributing> |
| Report a vulnerability | see [`SECURITY.md`](SECURITY.md) — use GitHub's private vulnerability reporting, not a public issue |

## Pull-request checklist

- [ ] PR scope is one of: tradition-tag addition, documentation fix,
      command-file clarification, agent honesty correction, translation,
      typo. PRs that change the architectural commitments are out of
      scope; open an issue first.
- [ ] No pilot data or copyrighted source material added under `eval/pilot/`
      (the entire directory is gitignored: `gold/paper.md` files are
      transcriptions of paywalled journal/proceedings sources).
- [ ] No paper-specific tracked content beyond what is already in the repo;
      maintainer's working paper sits in the sibling `art-project_paper/` repo.
- [ ] If you added a tradition tag, the entry includes: tradition name,
      ideation mechanism, **Authentic Practice Boundary**, **contested in**
      field, skill hook, citation.
- [ ] Bilingual changes: if you edited English wiki content, the Korean
      counterpart on the apesuite wiki is at least flagged for translation
      (open a wiki issue at <https://github.com/jh-bae/apesuite>).
- [ ] You have read and agree to the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## License

By contributing you agree that your contribution is released under
[CC-BY-NC 4.0](LICENSE), the same license as the project. Non-commercial
restriction applies to derivative works of the plugin itself; it does **not**
restrict artworks made by users with the plugin's help.

## Code of conduct

[`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — Contributor Covenant 2.1, with
two project-specific clarifications (theoretical critique vs. ad-hominem;
Authentic Practice Boundary as load-bearing). Reports go to
**jh.bae@kaist.ac.kr** or via GitHub private vulnerability reporting.
