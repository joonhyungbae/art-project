#!/usr/bin/env python3
"""Paper-mode reconstruction for the F2 clean-control extension.

Given a case directory with input/ files (documentation, exhibition_record,
concept_memo, bibliography, LEAKAGE_AUDIT), invoke Anthropic API to produce
reconstruction/paper.md.

Usage:
    python paper_reconstructor.py <case_dir>

Env:
    ANTHROPIC_API_KEY (sourced from /home/jhbae/creative-research-skills/.env if not in env)
"""
from __future__ import annotations
import os
import sys
import argparse
from pathlib import Path

import anthropic

DOTENV = Path("/home/jhbae/creative-research-skills/.env")
if not os.environ.get("ANTHROPIC_API_KEY") and DOTENV.exists():
    for line in DOTENV.read_text().splitlines():
        if line.startswith("ANTHROPIC_API_KEY="):
            os.environ["ANTHROPIC_API_KEY"] = line.split("=", 1)[1].strip()
            break

MODEL = "claude-sonnet-4-5-20250929"
MAX_TOKENS = 16384
TEMPERATURE = 0.7

SYSTEM_PROMPT = """You are reconstructing a practice-based art research paper from an INPUT PACK alone.

You are operating inside a reconstruction-benchmark firewall. The published gold paper is held out. You will only see the input pack, which carries pre-writing transferable factual material about the artwork (its physical form, system, exhibition record, neutral concept seed, and cited precedents bibliography). The pack deliberately WITHHOLDS the original paper's framing, thesis, provocation, audience-reception interpretation, and reflection.

Your task: produce a single self-contained practice-based art paper in Markdown, in the standard SIGGRAPH Asia Art Papers format. Sections should include (adapt as the input warrants):
- Title (your own choice)
- Abstract
- Introduction / Context
- Conceptual Framework
- The Work (factual description)
- Realization / Methods of Making
- Reception / Discussion
- Conclusion

IRON RULE — no auto-completion. Where the input pack does not provide enough material for a particular sentence, claim, or section, mark the gap explicitly (for example "[gap — not in input pack]" or hedge with "the public documentation does not specify ..."). Do NOT fabricate plausible-sounding filler. Authorial framing, thesis, and provocation must be derived from your own reading of the documented facts; mark them as your interpretation rather than as the artist's stated position.

Output: a single Markdown document. Begin with a YAML frontmatter block:

---
title: "<your title>"
type: practice-based-art-paper
pattern: 1
---

Then the paper body with section headings. Aim for 3000-5000 words depending on input richness. Do not include any explanation outside the paper itself."""

USER_TEMPLATE = """INPUT PACK — clean-control reconstruction case.

## documentation.md

{documentation}

## exhibition_record.md

{exhibition}

## concept_memo.md

{concept_memo}

## bibliography.bib

{bibliography}

## LEAKAGE_AUDIT.md (provenance + withheld layers; for your reference only)

{leakage_audit}

---

Reconstruct the practice-based art paper from the above input pack alone. Output the paper as a single Markdown document with YAML frontmatter."""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("case_dir")
    args = p.parse_args()
    case_dir = Path(args.case_dir).resolve()
    input_dir = case_dir / "input"

    documentation = (input_dir / "documentation.md").read_text()
    exhibition = (input_dir / "exhibition_record.md").read_text()
    concept_memo = (input_dir / "concept_memo.md").read_text()
    bibliography = (input_dir / "bibliography.bib").read_text()
    leakage_audit = (input_dir / "LEAKAGE_AUDIT.md").read_text()

    user_msg = USER_TEMPLATE.format(
        documentation=documentation,
        exhibition=exhibition,
        concept_memo=concept_memo,
        bibliography=bibliography,
        leakage_audit=leakage_audit,
    )

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )

    paper_md = resp.content[0].text

    out_dir = case_dir / "reconstruction"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "paper.md").write_text(paper_md)
    (out_dir / "refs.bib").write_text("% Reconstruction bibliography (auto-emitted; may be empty).\n")
    print(f"Wrote {out_dir / 'paper.md'}, {len(paper_md)} chars")
    print(f"Model: {MODEL}, input tokens: {resp.usage.input_tokens}, output tokens: {resp.usage.output_tokens}")


if __name__ == "__main__":
    main()
