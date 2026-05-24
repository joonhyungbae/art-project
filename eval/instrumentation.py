#!/usr/bin/env python3
"""art-paper reconstruction-benchmark instrumentation (§4 of the evaluation methodology).

Computes the AUTOMATABLE metrics over a art-paper reconstruction vs. a held-out gold
art paper. **It instruments; it does not score quality.** Every metric carries a
`does_not_license` field naming what it must NOT be read as.

Hard discipline (methodology §3): high text-similarity to the gold is a
CONTAMINATION WARNING, never a success. The contamination/similarity metrics are
reported and read in reverse.

Stdlib-only (no torch / no network), so the pilot is automatable solo. An
optional embedding backend can be wired in later for §4 row 6; the default
lexical n-gram path runs everywhere.

Layout expected (see eval/pilot/_TEMPLATE/):
    <pilot_case>/
        meta.yaml              # paper id, medium, contamination probe result, ...
        gold/paper.md          # held-out published paper (NEVER in generating context)
        gold/refs.bib          # gold bibliography
        reconstruction/paper.md
        reconstruction/refs.bib

Usage:
    python eval/instrumentation.py <pilot_case_dir>           # human-readable
    python eval/instrumentation.py <pilot_case_dir> --json    # machine-readable
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

# --- Section model: the Practice-Based Art Paper (Pattern 1) layers. ---------
# Maps each canonical layer to (a) heading-match keywords and (b) whether the
# layer is TRANSFERABLE (should converge with gold) or GENERATIVE (should
# diverge). This drives the per-layer divergence signal (§4 row 6 / §1.2 thesis).
# Heading keywords are checked in order; first match wins, so put the more
# specific layers (conceptual_framework "concept design") before broader ones
# (realization "design"). Real art papers rarely use the canonical names, so the
# synonym sets are deliberately broad; a section that matches nothing is recorded
# but left unaligned.
LAYERS = [
    ("introduction_context", ["introduction", "context", "inspiration", "motivation"], "mixed"),
    ("conceptual_framework", ["conceptual framework", "framework", "concept design", "concept", "background", "related work", "related concepts"], "generative"),
    ("the_work", ["the work", "the installation", "installation", "the artwork", "artwork appearance", "description", "artwork"], "transferable"),
    ("realization", ["realization", "realisation", "methods of making", "implementation", "system design", "interaction design", "pipeline", "technical", "system", "design", "method"], "transferable"),
    ("reflection_discussion", ["reflection", "discussion", "feedback", "findings", "observations", "evaluation", "results"], "generative"),
    ("conclusion", ["conclusion", "future work"], "mixed"),
    # Catch-all (no keywords; assigned only by the _split_sections fallback). Content
    # sections with idiosyncratic, work-specific names describe the work itself and
    # are factual/transferable, so unmatched substantive sections default here
    # rather than being orphaned — the generative layers (framework/reflection) are
    # the ones that are reliably named.
    ("other_work", [], "transferable"),
]

# Claim triggers for the anchoring metric, grouped by claim kind (evidence model §4).
CLAIM_TRIGGERS = {
    # Reception = evaluative/sentiment claims about audience response. A bare
    # audience noun ("visitors walk beneath it") is neutral description, not a
    # reception claim, so triggers require a sentiment/evaluation, not just the noun.
    "reception": [r"\bwidely\b", r"\bacclaim", r"\bmoved\b", r"\bamazed\b",
                  r"\bcaptivat", r"\b(audiences?|viewers?|visitors?)\b[^.]{0,40}\b(loved|enjoyed|were (moved|amazed|captivated|delighted)|responded enthusiastically)\b",
                  r"\bwell[- ]received\b", r"\bcritical(ly)? (acclaim|reception)\b",
                  r"\bdeeply (moved|affected|engaged)\b"],
    # "first," as a sentence enumerator (First, Second, ...) is not a novelty
    # claim, so the noun-phrase form requires "first" NOT immediately followed by
    # a comma. Negated/hedged novelty ("not new", "do not claim ... unprecedented")
    # is handled by the hedge patterns below, which mark such sentences as anchored.
    "novelty": [r"\bfirst\b(?!,)\s+(?:[\w-]+\s+){0,5}(work|artwork|installation|piece|system|time|to)\b",
                r"\bnovel\b", r"\bunprecedented\b", r"\bgroundbreaking\b", r"\bpioneering\b"],
    "capability": [r"\breal[- ]time\b", r"\bautonomous(ly)?\b", r"\bfully automat", r"\bself[- ]organi"],
}

# Anchors that legitimately support a claim (evidence model §3).
ANCHOR_PATTERNS = [
    r"\[\d+\]",                              # ACM numeric citation
    r"\\cite", r"\\citep", r"\\citet",        # latex citation
    r"\b(19|20)\d{2}\b",                      # a year (exhibition/venue date)
    r"\bexhibit", r"\binstall", r"\bgallery\b", r"\bfestival\b", r"\bbiennale\b",
    r"\bwe (observed|recorded|documented|measured|logged)\b",
]
# Hedges (protected-hedging contract) — an honest hedge also "satisfies" anchoring.
HEDGE_PATTERNS = [
    r"\bin this (installation|work|piece|exhibition|context)\b",
    r"\bfor these (visitors|participants|viewers)\b",
    r"\bappear(s|ed)?\b", r"\bseem(s|ed)?\b", r"\bmay\b", r"\bmight\b",
    r"\bwe did not (measure|quantify|survey|run|benchmark)\b", r"\banecdotal", r"\bsuggest(s|ed)?\b",
    # Negated / disclaimed novelty is itself an honest hedge, not an unanchored claim.
    r"\bnot new\b", r"\bnot (the |a )?first\b", r"\bnot unprecedented\b",
    r"\b(do|does|did|don't|do not|does not) not? claim\b", r"\bwe (make )?no claim\b",
    r"\bwe do not claim\b",
]

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
_WORD = re.compile(r"[a-z0-9']+")


# --- helpers -----------------------------------------------------------------
def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _tokens(text: str) -> list[str]:
    return _WORD.findall(text.lower())


def _ngrams(tokens: list[str], n: int) -> Counter:
    return Counter(tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)) if len(tokens) >= n else Counter()


def _ngram_containment(a: str, b: str, n: int = 8) -> float:
    """Fraction of `a`'s n-grams that also appear in `b`. Read in REVERSE:
    high containment of reconstruction-in-gold ⇒ memorization/contamination flag."""
    ta, tb = _tokens(a), _tokens(b)
    na, nb = _ngrams(ta, n), set(_ngrams(tb, n))
    if not na:
        return 0.0
    hit = sum(c for g, c in na.items() if g in nb)
    return round(hit / sum(na.values()), 4)


def _token_jaccard(a: str, b: str) -> float:
    ta, tb = set(_tokens(a)), set(_tokens(b))
    if not ta and not tb:
        return 0.0
    return round(len(ta & tb) / len(ta | tb), 4)


def _embedding_backend():
    """Lazily import the sibling embedding_backend module (eval/), ensuring eval/ is
    importable whether instrumentation.py is run as a script or imported elsewhere."""
    import importlib
    import sys
    from pathlib import Path
    d = str(Path(__file__).resolve().parent)
    if d not in sys.path:
        sys.path.insert(0, d)
    return importlib.import_module("embedding_backend")


# --- bibliography parsing ----------------------------------------------------
_BIB_ENTRY = re.compile(r"@\w+\s*\{\s*([^,]+),(.*?)\n\}", re.DOTALL)
_BIB_FIELD = re.compile(r"(\w+)\s*=\s*[{\"]+(.*?)[}\"]+\s*,?\s*$", re.MULTILINE)


def parse_bib(text: str) -> list[dict]:
    out = []
    for key, body in _BIB_ENTRY.findall(text):
        fields = {k.lower(): v.strip() for k, v in _BIB_FIELD.findall(body)}
        out.append({"key": key.strip(), **fields})
    return out


def _norm_title(title: str) -> str:
    """Lowercase, drop parentheticals (subtitles like '(Facework)'), strip non-alnum."""
    title = re.sub(r"\(.*?\)", "", title)
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def _norm_doi(doi: str) -> str:
    return re.sub(r"\s+", "", doi.lower())


def _refs_match(a: dict, b: dict) -> bool:
    """Do two bib entries refer to the same work? DOI-equal, title-equal, or one
    normalized title is a prefix of the other (handles subtitle truncation)."""
    da, db = a.get("doi"), b.get("doi")
    if da and db and _norm_doi(da) == _norm_doi(db):
        return True
    ta, tb = _norm_title(a.get("title", "")), _norm_title(b.get("title", ""))
    if not ta or not tb:
        return False
    if ta == tb:
        return True
    shorter = min(ta, tb, key=len)
    return len(shorter) >= 12 and (ta.startswith(tb) or tb.startswith(ta))


# --- metrics -----------------------------------------------------------------
def citation_set_pr(recon_bib: str, gold_bib: str) -> dict:
    recon = parse_bib(recon_bib)
    gold = parse_bib(gold_bib)
    matched_gold: set[int] = set()  # greedy 1:1 match
    shared = 0
    for r in recon:
        for i, g in enumerate(gold):
            if i in matched_gold:
                continue
            if _refs_match(r, g):
                matched_gold.add(i)
                shared += 1
                break
    precision = round(shared / len(recon), 4) if recon else 0.0
    recall = round(len(matched_gold) / len(gold), 4) if gold else 0.0
    return {
        "metric": "citation_set_precision_recall",
        "measures": "did art-paper surface the gold's precedent works + theory (lineage/discourse layer)",
        "does_not_license": "quality",
        "precision": precision, "recall": recall,
        "recon_count": len(recon), "gold_count": len(gold), "shared": shared,
    }


def anchoring_rate(recon_text: str) -> dict:
    anchor_re = re.compile("|".join(ANCHOR_PATTERNS), re.IGNORECASE)
    hedge_re = re.compile("|".join(HEDGE_PATTERNS), re.IGNORECASE)
    trigger_res = {k: re.compile("|".join(v), re.IGNORECASE) for k, v in CLAIM_TRIGGERS.items()}
    claims, anchored = 0, 0
    unanchored_examples = []
    for sent in _SENT_SPLIT.split(recon_text):
        kinds = [k for k, r in trigger_res.items() if r.search(sent)]
        if not kinds:
            continue
        claims += 1
        if anchor_re.search(sent) or hedge_re.search(sent):
            anchored += 1
        elif len(unanchored_examples) < 8:
            unanchored_examples.append({"kinds": kinds, "sentence": sent.strip()[:200]})
    return {
        "metric": "anchoring_rate",
        "measures": "fraction of reception/novelty/capability claims carrying an observable anchor or explicit hedge",
        "does_not_license": "quality",
        "claims_detected": claims,
        "anchored": anchored,
        "rate": round(anchored / claims, 4) if claims else None,
        "unanchored_examples": unanchored_examples,
    }


# Front-matter / boundary headings that must NOT be captured as a layer (and that
# end the current layer): ACM metadata, references, acknowledgments, abstract.
_META_HEADINGS = ("ccs concept", "keywords", "acm reference", "references",
                  "acknowledg", "abstract", "bibliography")


def _split_sections(text: str) -> dict:
    """Split markdown into {layer_key: section_text}, level-aware.

    Real art papers nest content under idiosyncratic subsection headings (2.1, 4.2,
    5.1) that don't match layer keywords. We roll those subsections up into the
    parent layer rather than orphaning their text. A level-1 heading is the document
    title (skipped); a metadata/boundary heading ends the current layer.
    """
    parts = re.split(r"^(#{1,4})\s+(.*)$", text, flags=re.MULTILINE)
    # parts: [pre, hashes1, head1, body1, hashes2, head2, body2, ...]
    sections: dict[str, str] = {}
    current = None
    for i in range(1, len(parts) - 2, 3):
        level = len(parts[i])
        head = parts[i + 1].strip().lower()
        body = parts[i + 2]
        if level <= 1:                       # document title — not a layer
            current = None
            continue
        is_meta = any(mh in head for mh in _META_HEADINGS)
        matched = None
        if not is_meta:
            for key, kws, _ in LAYERS:
                if any(kw in head for kw in kws):
                    matched = key
                    break
        if matched:
            current = matched
            sections.setdefault(current, "")
            sections[current] += "\n" + body
        elif is_meta:
            current = None                   # references / acks / metadata boundary
        elif level >= 3 and current:
            sections[current] += "\n" + body  # subsection rolls up into parent layer
        else:
            # Unmatched substantive top-level section (idiosyncratic name): treat as
            # the work/realization (transferable) rather than orphaning it.
            current = "other_work"
            sections.setdefault(current, "")
            sections[current] += "\n" + body
    return sections


def structural_coverage(recon_text: str) -> dict:
    sections = _split_sections(recon_text)
    # Only keyworded layers are "expected"; other_work is a catch-all, not required.
    expected = [(k, kw, kd) for k, kw, kd in LAYERS if kw]
    present = {key: (key in sections and bool(sections[key].strip())) for key, _, _ in expected}
    return {
        "metric": "structural_coverage",
        "measures": "did the output produce the expected Pattern-1 layers",
        "does_not_license": "quality",
        "present": present,
        "coverage": round(sum(present.values()) / len(present), 4),
    }


def contamination_probe(recon_text: str, gold_text: str, embed: bool = False) -> dict:
    cont = _ngram_containment(recon_text, gold_text, n=8)
    flag = "HIGH-CONTAMINATION-WARNING" if cont >= 0.10 else ("ELEVATED" if cont >= 0.03 else "ok")
    out = {
        "metric": "embedding/ngram_contamination_probe",
        "measures": "verbatim/semantic overlap with gold — READ IN REVERSE",
        "does_not_license": "quality OR success",
        "ngram8_containment_recon_in_gold": cont,
        "flag": flag,
        "note": "High overlap ⇒ memorization flag (methodology §3 inversion rule), NOT a good result.",
    }
    if embed:
        eb = _embedding_backend()
        out["semantic_max_chunk_cosine"] = eb.semantic_max_chunk(recon_text, gold_text)
        out["embed_model"] = eb.model_name()
        # NOTE: within one paper this is TOPIC-CONFOUNDED — recon and gold are about
        # the same artwork, so chunk cosine is high (~0.95) even with zero verbatim
        # overlap. Do NOT read it as memorization. The n-gram signal above is the
        # verbatim-contamination measure; a meaningful semantic contamination signal
        # needs a cross-paper baseline (subtract similarity to OTHER papers) — future work.
        out["semantic_note"] = ("TOPIC-CONFOUNDED within one paper; not a memorization signal "
                                "without a cross-paper baseline. Use the n-gram measure for contamination.")
    return out


def per_layer_similarity(recon_text: str, gold_text: str, embed: bool = False) -> dict:
    rs, gs = _split_sections(recon_text), _split_sections(gold_text)
    # Per-layer rows are descriptive only — gold and recon may segment work vs.
    # realization differently (one paper nests realization under "The Installation").
    rows = []
    for key, _, kind in LAYERS:
        if key in rs and key in gs:
            rows.append({
                "layer": key, "kind": kind,
                "token_jaccard": _token_jaccard(rs[key], gs[key]),
                "ngram4_containment": _ngram_containment(rs[key], gs[key], n=4),
            })

    def blob(d: dict, kind: str) -> str:
        return " ".join(d[k] for k, _, kd in LAYERS if kd == kind and k in d)

    g_t, r_t = blob(gs, "transferable"), blob(rs, "transferable")
    g_g, r_g = blob(gs, "generative"), blob(rs, "generative")
    t_sim = _token_jaccard(g_t, r_t) if (g_t.strip() and r_t.strip()) else None
    g_sim = _token_jaccard(g_g, r_g) if (g_g.strip() and r_g.strip()) else None
    # The thesis is tested on GROUPED blobs (robust to per-paper segmentation):
    # transferable content should converge more than generative content.
    out = {
        "metric": "per_layer_similarity_divergence",
        "measures": "transferable layers should converge (higher), generative layers diverge (lower) — descriptive",
        "does_not_license": "'high = good'",
        "note": "transferable/generative similarity computed on grouped layer blobs, robust to whether a paper splits or nests work vs. realization.",
        "rows": rows,
        "transferable_similarity": t_sim,
        "generative_similarity": g_sim,
        "thesis_supported": (t_sim > g_sim) if (t_sim is not None and g_sim is not None) else None,
    }
    if embed:
        eb = _embedding_backend()
        # blob mean-pool cosine — SATURATES on shared topic (kept for transparency)
        st = eb.semantic_similarity(g_t, r_t) if (g_t.strip() and r_t.strip()) else None
        sg = eb.semantic_similarity(g_g, r_g) if (g_g.strip() and r_g.strip()) else None
        # chunk-alignment — "was this content reproduced?", more discriminating
        at = eb.semantic_alignment(g_t, r_t) if (g_t.strip() and r_t.strip()) else None
        ag = eb.semantic_alignment(g_g, r_g) if (g_g.strip() and r_g.strip()) else None
        out["semantic_blob_transferable"] = st
        out["semantic_blob_generative"] = sg
        out["semantic_align_transferable"] = at
        out["semantic_align_generative"] = ag
        out["semantic_thesis_supported"] = (at > ag) if (at is not None and ag is not None) else None
        out["embed_model"] = eb.model_name()
        out["semantic_caveat"] = ("Sentence-embedding cosine is topic-saturated within one paper; "
                                  "the LEXICAL measure discriminates transferable vs generative best. "
                                  "chunk-alignment > blob cosine but both are topic-influenced.")
    return out


def instrument_case(case_dir: Path, embed: bool = False) -> dict:
    gold_paper = _read(case_dir / "gold" / "paper.md")
    gold_bib = _read(case_dir / "gold" / "refs.bib")
    recon_paper = _read(case_dir / "reconstruction" / "paper.md")
    recon_bib = _read(case_dir / "reconstruction" / "refs.bib")
    if not gold_paper or not recon_paper:
        raise FileNotFoundError(
            f"{case_dir}: need gold/paper.md and reconstruction/paper.md (see eval/pilot/_TEMPLATE/)"
        )
    return {
        "case": case_dir.name,
        "instrumentation_only": True,
        "quality_scored": False,
        "metrics": {
            "citation_set_pr": citation_set_pr(recon_bib, gold_bib),
            "anchoring_rate": anchoring_rate(recon_paper),
            "structural_coverage": structural_coverage(recon_paper),
            "contamination_probe": contamination_probe(recon_paper, gold_paper, embed=embed),
            "per_layer_similarity": per_layer_similarity(recon_paper, gold_paper, embed=embed),
        },
    }


def _print_human(result: dict) -> None:
    m = result["metrics"]
    print(f"\n=== Reconstruction instrumentation — case: {result['case']} ===")
    print("    (instruments; does NOT score quality — see methodology §1 forbidden claims)\n")
    c = m["citation_set_pr"]
    print(f"Citation set   precision={c['precision']}  recall={c['recall']}  ({c['shared']}/{c['gold_count']} gold precedents surfaced)")
    a = m["anchoring_rate"]
    print(f"Anchoring rate {a['rate']}  ({a['anchored']}/{a['claims_detected']} reception/novelty/capability claims anchored or hedged)")
    s = m["structural_coverage"]
    print(f"Struct cover   {s['coverage']}  layers present: {[k for k,v in s['present'].items() if v]}")
    p = m["contamination_probe"]
    print(f"Contamination  8-gram containment={p['ngram8_containment_recon_in_gold']}  -> {p['flag']}  (HIGH = bad: memorization)")
    pl = m["per_layer_similarity"]
    print(f"Per-layer sim  transferable={pl['transferable_similarity']}  generative={pl['generative_similarity']}  thesis_supported={pl['thesis_supported']}  (LEXICAL, grouped — primary discriminator)")
    if "semantic_align_transferable" in pl:
        print(f"  semantic align transferable={pl['semantic_align_transferable']}  generative={pl['semantic_align_generative']}  ({pl.get('embed_model')})")
        print(f"  semantic blob  transferable={pl['semantic_blob_transferable']}  generative={pl['semantic_blob_generative']}  (SATURATED — topic-confounded)")
    if "semantic_max_chunk_cosine" in p:
        print(f"  semantic contamination max-chunk={p['semantic_max_chunk_cosine']}  (TOPIC-CONFOUNDED — not memorization; use n-gram)")
    for r in pl["rows"]:
        print(f"               - {r['layer']:24s} [{r['kind']:12s}] jaccard={r['token_jaccard']}")
    if a["unanchored_examples"]:
        print("\nUnanchored claim examples (review for reception/novelty/capability inflation):")
        for ex in a["unanchored_examples"]:
            print(f"   ({','.join(ex['kinds'])}) {ex['sentence']}")
    print()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="art-paper reconstruction-benchmark instrumentation (§4).")
    ap.add_argument("case_dir", help="pilot case directory (see eval/pilot/_TEMPLATE/)")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--embed", action="store_true",
                    help="add semantic (sentence-embedding) similarity via eval/embedding_backend.py (needs sentence-transformers)")
    args = ap.parse_args(argv)
    result = instrument_case(Path(args.case_dir), embed=args.embed)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        _print_human(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
