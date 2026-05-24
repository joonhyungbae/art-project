#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def fail(message: str) -> None:
    ERRORS.append(message)


def expect_contains(rel_path: str, needle: str) -> None:
    text = read(rel_path)
    if needle not in text:
        fail(f"{rel_path}: missing expected text: {needle!r}")


def expect_absent(rel_path: str, needle: str) -> None:
    text = read(rel_path)
    if needle in text:
        fail(f"{rel_path}: forbidden text still present: {needle!r}")


def extract_section(text: str, start: str, end: str) -> str:
    start_idx = text.find(start)
    if start_idx == -1:
        fail(f"missing section start: {start!r}")
        return ""
    end_idx = text.find(end, start_idx + len(start))
    if end_idx == -1:
        fail(f"missing section end after {start!r}: {end!r}")
        return text[start_idx:]
    return text[start_idx:end_idx]


def check_relative_markdown_links(rel_path: str) -> None:
    text = read(rel_path)
    doc_path = ROOT / rel_path
    for raw_target in MARKDOWN_LINK_RE.findall(text):
        if raw_target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = raw_target.split("#", 1)[0]
        if not target:
            continue
        resolved = (doc_path.parent / target).resolve()
        if not resolved.exists():
            fail(f"{rel_path}: broken relative markdown link {raw_target!r}")


def check_mode_registry() -> None:
    rel_path = "MODE_REGISTRY.md"
    text = read(rel_path)
    expect_contains(rel_path, "Last updated: v0.1.0 (2026-05-22)")
    for heading in (
        "## art-inquiry (7 modes)",
        "## art-paper (12 modes)",
        "## art-reviewer (6 modes)",
    ):
        if heading not in text:
            fail(f"{rel_path}: missing mode heading {heading!r}")


def check_claude_md() -> None:
    rel_path = ".claude/CLAUDE.md"
    expect_contains(rel_path, "integrity check (Stage 2.5")
    expect_contains(rel_path, "final integrity check (Stage 4.5)")
    expect_contains(rel_path, "**Suite version**: 0.1.0")
    for forbidden in (
        "6th independent reviewer",
        "Peer review gains 6th independent reviewer",
    ):
        expect_absent(rel_path, forbidden)


def check_reviewer_version_block() -> None:
    rel_path = "art-reviewer/SKILL.md"
    text = read(rel_path)
    frontmatter_match = re.search(
        r'metadata:\s*[\s\S]*?\n\s+version:\s"([^"]+)"\n\s+last_updated:\s"([^"]+)"',
        text,
    )
    if not frontmatter_match:
        fail(f"{rel_path}: could not parse frontmatter version/last_updated")
        return
    version, last_updated = frontmatter_match.groups()

    version_block_match = re.search(r"\| Skill Version \| ([^|]+) \|", text)
    updated_block_match = re.search(r"\| Last Updated \| ([^|]+) \|", text)
    if not version_block_match or not updated_block_match:
        fail(f"{rel_path}: missing Version Info table rows")
        return

    version_block = version_block_match.group(1).strip()
    updated_block = updated_block_match.group(1).strip()

    if version != version_block:
        fail(
            f"{rel_path}: frontmatter version {version!r} does not match Version Info block {version_block!r}"
        )
    if last_updated != updated_block:
        fail(
            f"{rel_path}: frontmatter last_updated {last_updated!r} does not match Version Info block {updated_block!r}"
        )


def check_pipeline_docs() -> None:
    for rel_path in (
        "art-pipeline/SKILL.md",
        "art-pipeline/agents/pipeline_orchestrator_agent.md",
    ):
        expect_absent(rel_path, "auto-continue in 5 seconds")
        expect_contains(rel_path, "One-line status + explicit continue/pause prompt")

    expect_contains(
        "art-pipeline/agents/pipeline_orchestrator_agent.md",
        "Stage 2.5 can NEVER be skipped",
    )
    expect_contains(
        "art-pipeline/agents/pipeline_orchestrator_agent.md",
        "Stage 4.5 can NEVER be skipped",
    )


def check_readme_sections() -> None:
    rel_path = "README.md"
    text = read(rel_path)

    expect_contains(rel_path, "version-v0.1.0-blue")
    # art-paper changelog leads with the fork entry; the inherited ARS release history is
    # pointed to (CHANGELOG.md / ref/), not re-narrated in the README.
    expect_contains(rel_path, "### v0.1.0 (2026-05-22) — art-paper fork")
    expect_contains(rel_path, "### Inherited ARS history")
    for heading in (
        "#### Creative Inquiry (7 modes)",
        "#### Creative Paper (12 modes)",
        "#### Creative Reviewer (6 modes)",
        "### Creative Inquiry (v0.1)",
        "### Creative Paper (v0.1)",
        "### Creative Reviewer (v0.1)",
        "### Creative Pipeline (v0.1)",
    ):
        if heading not in text:
            fail(f"{rel_path}: missing heading {heading!r}")

    paper_usage = extract_section(
        text, "#### Creative Paper (12 modes)", "#### Creative Reviewer (6 modes)"
    )
    for expected in ("outline-only mode", "abstract-only mode", "disclosure mode"):
        if expected not in paper_usage:
            fail(f"{rel_path}: Creative Paper usage section missing {expected!r}")
    for forbidden in ("bilingual-abstract mode", "writing-polish mode", "full-auto mode"):
        if forbidden in paper_usage:
            fail(f"{rel_path}: Creative Paper usage section still contains {forbidden!r}")

    inquiry_usage = extract_section(
        text, "#### Creative Inquiry (7 modes)", "#### Creative Paper (12 modes)"
    )
    if "review mode" not in inquiry_usage:
        fail(f"{rel_path}: Creative Inquiry usage section missing 'review mode'")

    reviewer_usage = extract_section(
        text, "#### Creative Reviewer (6 modes)", "#### Creative Pipeline (Orchestrator)"
    )
    if "calibration mode" not in reviewer_usage:
        fail(f"{rel_path}: reviewer usage section missing 'calibration mode'")

    for forbidden in (
        "6th independent reviewer",
        "Peer review gains 6th independent reviewer",
    ):
        expect_absent(rel_path, forbidden)
    # DOCX contract lines moved to docs/SETUP.md in v3.3.6; checked there instead.
    expect_contains(rel_path, "DOCX (via Pandoc when available)")
    check_relative_markdown_links(rel_path)


def check_setup_docs() -> None:
    expect_contains("docs/SETUP.md", "Direct `.docx` generation uses [Pandoc]")
    expect_contains(
        "docs/SETUP.md",
        "Direct `.docx` generation requires Pandoc, and PDF generation requires the LaTeX toolchain above",
    )
    check_relative_markdown_links("docs/SETUP.md")


def check_docx_contract() -> None:
    expect_contains(
        "art-paper/SKILL.md",
        "LaTeX/DOCX (via Pandoc)/PDF/Markdown",
    )
    expect_contains(
        "art-paper/agents/formatter_agent.md",
        "If Pandoc is available, generate `.docx`; otherwise provide markdown + conversion instructions",
    )
    expect_contains(
        "art-pipeline/SKILL.md",
        "DOCX via Pandoc when available, otherwise conversion instructions",
    )
    expect_contains(
        "art-pipeline/agents/pipeline_orchestrator_agent.md",
        "DOCX via Pandoc when available (otherwise instructions)",
    )
    for rel_path in (
        "art-pipeline/SKILL.md",
        "art-pipeline/agents/pipeline_orchestrator_agent.md",
    ):
        expect_absent(rel_path, "Auto-produce MD + DOCX")


def check_reference_docs() -> None:
    expect_contains(
        "art-pipeline/references/passport_as_reset_boundary.md",
        "# Passport as Reset Boundary (v3.6.3)",
    )
    expect_contains(
        "art-pipeline/references/passport_as_reset_boundary.md",
        "## `resume_from_passport` mode contract",
    )
    expect_contains(
        "art-pipeline/references/passport_as_reset_boundary.md",
        "## Iron rules",
    )
    # Unified PASSPORT-RESET tag format across protocol doc + orchestrator emission + checkpoint template.
    # Divergence here breaks cross-session machine-stable handoff.
    tag_format = "[PASSPORT-RESET: hash=<hash>, stage=<completed>, next=<next>]"
    expect_contains(
        "art-pipeline/references/passport_as_reset_boundary.md",
        tag_format,
    )
    expect_contains(
        "art-pipeline/agents/pipeline_orchestrator_agent.md",
        tag_format,
    )


def main() -> int:
    check_mode_registry()
    check_claude_md()
    check_reviewer_version_block()
    check_pipeline_docs()
    check_readme_sections()
    # art-paper v0.1 ships English + Korean READMEs (README.md + README.ko-KR.md). The ARS
    # zh-TW / zh-CN / ja-JP README translations are not carried; their check functions were
    # removed in the 2026-05-23 Chinese-support drop (Stage 2 polish).
    check_setup_docs()
    check_docx_contract()
    check_reference_docs()

    if ERRORS:
        print("Spec consistency check failed:")
        for error in ERRORS:
            print(f"- {error}")
        return 1

    print("Spec consistency check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
