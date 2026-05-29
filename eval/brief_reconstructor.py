"""art-project brief-mode reconstruction wrapper for Phase 3 empirical evaluation.

Given a per-case directory at <case_dir>/input/ (documentation.md +
exhibition_record.md + bibliography.bib), invoke art-project's brief mode via
the Anthropic API to produce <case_dir>/reconstruction/reconstructed-brief.md
and reconstruction-meta.json.

The system prompt assembles art-ideation/SKILL.md + commands/art-brief.md +
shared/references/art_ideation_methodology.md as a single cached block. The user
message carries the input-pack contents. Single-shot call (no multi-turn
dialogue), adapted from the brief mode's interactive default for reconstruction
benchmark use.

Usage:
    python eval/brief_reconstructor.py <case_dir>

Environment:
    ANTHROPIC_API_KEY must be set.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = REPO_ROOT / "art-ideation" / "SKILL.md"
BRIEF_CMD_PATH = REPO_ROOT / "commands" / "art-brief.md"
METHODOLOGY_PATH = REPO_ROOT / "shared" / "references" / "art_ideation_methodology.md"

DEFAULT_MODEL = "claude-sonnet-4-6"
TEMPERATURE = 0.7
SEED_LABEL = 42  # Anthropic API has no seed parameter; recorded for run-labelling only.
MAX_TOKENS = 16384

RECONSTRUCTION_FRAMING = (
    "You are operating as the art-project plugin's `brief` mode for a "
    "reconstruction benchmark. The artist is not present, so the interactive "
    "stay-rough capture is suspended (there is no artist voice to preserve). "
    "Produce the 10-field Concept Brief from the input pack alone "
    "(documentation, exhibition record, bibliography). "
    "The no-auto-completion IRON RULE remains active: where the input does not "
    "provide enough material to articulate a field, report the gap as "
    "`[gap — not in input]` rather than fabricating plausible-sounding filler. "
    "Output a single Markdown document with the 10 fields in order, each "
    "field labelled with its layer (transferable / generative / mixed) per the "
    "v0.2 epistemic schema. Do not include any preamble or postscript outside "
    "the brief itself."
)


def build_system_blocks() -> list[dict]:
    """Stable system prompt with one cache_control breakpoint on the full block."""
    skill_md = SKILL_PATH.read_text(encoding="utf-8")
    brief_md = BRIEF_CMD_PATH.read_text(encoding="utf-8")
    methodology_md = METHODOLOGY_PATH.read_text(encoding="utf-8")

    body = (
        RECONSTRUCTION_FRAMING
        + "\n\n---\n\n# art-ideation/SKILL.md\n\n"
        + skill_md
        + "\n\n---\n\n# commands/art-brief.md\n\n"
        + brief_md
        + "\n\n---\n\n# shared/references/art_ideation_methodology.md\n\n"
        + methodology_md
    )

    return [
        {
            "type": "text",
            "text": body,
            "cache_control": {"type": "ephemeral"},
        }
    ]


def load_input_pack(case_dir: Path) -> str:
    input_dir = case_dir / "input"
    documentation = (input_dir / "documentation.md").read_text(encoding="utf-8")
    exhibition = (input_dir / "exhibition_record.md").read_text(encoding="utf-8")
    bibliography = (input_dir / "bibliography.bib").read_text(encoding="utf-8")

    return (
        "# INPUT PACK\n\n"
        "## documentation.md\n\n"
        + documentation
        + "\n\n## exhibition_record.md\n\n"
        + exhibition
        + "\n\n## bibliography.bib\n\n```bibtex\n"
        + bibliography
        + "\n```\n\n---\n\n"
        "Produce the 10-field Concept Brief now."
    )


def prompt_digest(system_blocks: list[dict], user_text: str) -> str:
    h = hashlib.sha256()
    for block in system_blocks:
        h.update(block["text"].encode("utf-8"))
    h.update(b"\n---USER---\n")
    h.update(user_text.encode("utf-8"))
    return h.hexdigest()


def run_reconstruction(case_dir: Path, model: str = DEFAULT_MODEL, output_subdir: str = "reconstruction") -> None:
    case_dir = case_dir.resolve()
    if not (case_dir / "input").is_dir():
        sys.exit(f"error: {case_dir}/input/ not found")

    output_dir = case_dir / output_subdir
    output_dir.mkdir(exist_ok=True)
    out_brief = output_dir / "reconstructed-brief.md"
    out_meta = output_dir / "reconstruction-meta.json"

    system_blocks = build_system_blocks()
    user_text = load_input_pack(case_dir)
    digest = prompt_digest(system_blocks, user_text)

    client = anthropic.Anthropic()
    started_at = datetime.now(timezone.utc).isoformat()

    with client.messages.stream(
        model=model,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
        system=system_blocks,
        messages=[{"role": "user", "content": user_text}],
    ) as stream:
        message = stream.get_final_message()

    finished_at = datetime.now(timezone.utc).isoformat()

    text_blocks = [b.text for b in message.content if b.type == "text"]
    body = "\n".join(text_blocks).strip()
    out_brief.write_text(body + "\n", encoding="utf-8")

    usage = message.usage
    meta = {
        "case": case_dir.name,
        "model": model,
        "temperature": TEMPERATURE,
        "seed_label": SEED_LABEL,
        "max_tokens": MAX_TOKENS,
        "prompt_sha256": digest,
        "started_at": started_at,
        "finished_at": finished_at,
        "stop_reason": message.stop_reason,
        "usage": {
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
        },
        "source_files": {
            "skill_md": str(SKILL_PATH.relative_to(REPO_ROOT)),
            "brief_command": str(BRIEF_CMD_PATH.relative_to(REPO_ROOT)),
            "methodology": str(METHODOLOGY_PATH.relative_to(REPO_ROOT)),
        },
    }
    out_meta.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    print(f"wrote: {out_brief}")
    print(f"wrote: {out_meta}")
    print(
        f"input_tokens={meta['usage']['input_tokens']} "
        f"output_tokens={meta['usage']['output_tokens']} "
        f"cache_read={meta['usage']['cache_read_input_tokens']} "
        f"cache_create={meta['usage']['cache_creation_input_tokens']}"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case_dir", help="Path to per-case directory containing input/ subdir")
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Anthropic model id (default: {DEFAULT_MODEL}). Use e.g. 'claude-haiku-4-5' for within-family judge runs.",
    )
    parser.add_argument(
        "--output-subdir",
        default="reconstruction",
        help="Subdirectory under case_dir for output (default: reconstruction). Use 'reconstruction-haiku' to keep model variants separate.",
    )
    args = parser.parse_args()
    run_reconstruction(Path(args.case_dir), model=args.model, output_subdir=args.output_subdir)


if __name__ == "__main__":
    main()
