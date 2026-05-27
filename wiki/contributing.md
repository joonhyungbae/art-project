# Contributing

The art-project plugin is open under CC-BY-NC 4.0. Contributions are welcome in four categories.

## 1. Adding a tradition tag

The corpus at [`shared/references/art_ideation_methodology.md`](https://github.com/joonhyungbae/art-project/blob/main/shared/references/art_ideation_methodology.md) is open. To propose a new tradition tag, submit a PR with the 6-field schema populated:

1. **Author + year** (with DOI or stable URL)
2. **Core gesture** (one sentence)
3. **Ideation mechanism**
4. **Authentic Practice Boundary** (mandatory — what the methodology requires that the AI does not simulate)
5. **Contested in** (counter-positions or critiques)
6. **Skill-hook** (which modes consume the entry)

PRs missing the Authentic Practice Boundary field will not be accepted. See [Tradition tags](reference/tradition-tags.md) and [Authentic Practice Boundaries](reference/authentic-practice-boundaries.md) for the rationale.

**Especially welcomed**: non-anglophone tradition tags. The current corpus has Korean / East-Asian entries (Paik, Hui, Lee & Lee 2024) and is otherwise anglophone-heavy. Tags from oral traditions, Indigenous practice, Global South methodologies, and traditions that resist textual fixation but can be cited with appropriate boundaries are all welcomed.

## 2. Reporting a measured-harm class

The [6 named harm classes](philosophy/measured-harms.md) are not exhaustive. If you identify a harm class the plugin's documentation does not name, file an issue with:

- **Class name** (proposed)
- **Description** (what kind of harm, in what context)
- **Mitigation candidate** (if any — "none yet" is acceptable)
- **Where it surfaces** (which mode, which output type)

Harm-class issues are triaged before feature requests.

## 3. Documentation contributions (this wiki)

The wiki lives in `wiki/` in the repository root. To contribute:

- Edit the relevant `.md` file (English) and `.ko.md` file (Korean) **together**. The plugin's translation discipline requires both languages to update in lockstep; the Korean version is not a secondary translation but a parallel canonical version.
- For new pages, also update `mkdocs.yml` `nav:` section + the `nav_translations:` keys for both `en` and `ko` locales.
- Build locally with `mkdocs serve` (requires `pip install mkdocs-material mkdocs-static-i18n`) and verify both language paths render correctly.

### Translation discipline

When editing one language file, the other language's file must be updated in the same PR. Drift between language versions is treated as a documentation bug. If the Korean and English versions cannot say the same thing (because the concept is hard to translate), the difference must be explicitly named in the file — not papered over.

## 4. Code contributions (the plugin itself)

For changes to the plugin code (`art-ideation/`, `commands/`, `agents/`), follow the standard PR flow:

1. Open an issue first describing the change. For architectural changes (IRON rule modifications, new modes, schema extensions), the issue must reference the [POSITIONING.md](https://github.com/joonhyungbae/art-project/blob/main/POSITIONING.md) constraints the change respects.
2. Branch from `main`; commit messages follow conventional-commits style.
3. Run the test suite (`pytest` from repository root).
4. Submit PR with description, rationale, and links to relevant docs.

**Not accepted without discussion first**:

- Removing or weakening any IRON rule.
- Removing the Authentic Practice Boundary discipline.
- Removing the mandatory bias header on `lineage` mode.
- Removing the disclaimer header or architectural friction on `rehearsal` mode.
- Adding mode-pipelining within a single session.

These are the architectural commitments the framework rests on. Changes to them require synthesis-spec-level discussion first; see [`docs/design/`](https://github.com/joonhyungbae/art-project/blob/main/docs/design/).

## Code of conduct

Be respectful of the artists this plugin is for. Critiques of the framework are welcome; dismissals of practice-based research, of non-anglophone art-research traditions, or of artists who use AI as a cognitive partner are not.

## License

CC-BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International). Contributions are accepted under the same license. Commercial use of the framework or derivatives requires separate licensing — contact the maintainer.

## Maintainer

Joonhyung Bae — [GitHub](https://github.com/joonhyungbae)

## See also

- [POSITIONING.md](https://github.com/joonhyungbae/art-project/blob/main/POSITIONING.md) — the framework's public positioning and constraints.
- [MODE_REGISTRY.md](https://github.com/joonhyungbae/art-project/blob/main/MODE_REGISTRY.md) — the single source of truth for modes.
- [CHANGELOG.md](https://github.com/joonhyungbae/art-project/blob/main/CHANGELOG.md) — version history.
