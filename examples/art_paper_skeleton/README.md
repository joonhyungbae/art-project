# art-paper art-paper skeleton (acmart)

A minimal, **compilable** starting point for a SIGGRAPH Asia Art Paper produced
with art-paper. It demonstrates the canonical art-paper output path:

- `acmart` `sigconf` document class (the art-paper default; **verify the exact class
  for the current Art Papers track against the CFP**).
- **ACM Reference Format** bibliography (`\bibliographystyle{ACM-Reference-Format}`).
- The **Practice-Based Art Paper** structure (Pattern 1 — see
  `shared/references/art_paper_structure_patterns.md`).
- The genre-specific **artwork citation** (`@misc` with venue+date as the L3
  locator — see `shared/references/acm_reference_format.md`).
- A two-channel **AI-usage disclosure** in the acknowledgements (artwork-making
  vs. paper-writing — see `shared/references/siggraph_acm_disclosure.md`).

## Build

```sh
latexmk -pdf paper.tex
# or the canonical sequence:
pdflatex paper.tex && bibtex paper && pdflatex paper.tex && pdflatex paper.tex
```

Requires the ACM `acmart` package and `ACM-Reference-Format.bst` (ships with
recent TeX Live as `texlive-publishers`, or install acmart from CTAN). Verified
to compile to a clean PDF with citations resolved in ACM Reference Format.

> This is a template with placeholder content, not a submission. Replace each
> section with your work, and run the art-paper pipeline (`/art-full`) to draft and
> review a real paper.
