"""Self-test for the art-paper reconstruction-benchmark instrumentation (eval/instrumentation.py).

Proves the §4 metric engine runs end-to-end on the synthetic fixture and that the
key invariants hold. Loaded via importlib so we don't make `eval/` a Python package
(the name `eval` would shadow the builtin in some contexts).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_INSTR = ROOT / "eval" / "instrumentation.py"
_FIXTURE = ROOT / "eval" / "fixtures" / "synthetic_case"


def _load_module():
    spec = importlib.util.spec_from_file_location("art_paper_eval_instrumentation", _INSTR)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


instr = _load_module()


@pytest.fixture(scope="module")
def result():
    return instr.instrument_case(_FIXTURE)


def test_engine_runs_and_is_instrumentation_only(result):
    assert result["instrumentation_only"] is True
    assert result["quality_scored"] is False
    assert set(result["metrics"]) == {
        "citation_set_pr", "anchoring_rate", "structural_coverage",
        "contamination_probe", "per_layer_similarity",
    }


def test_every_metric_declares_what_it_does_not_license(result):
    for m in result["metrics"].values():
        assert m.get("does_not_license"), f"{m.get('metric')} must declare does_not_license"
        assert "quality" in m["does_not_license"] or "good" in m["does_not_license"]


def test_citation_set_pr(result):
    c = result["metrics"]["citation_set_pr"]
    # fixture: recon shares 2 of gold's 3 refs (sensorInstall, newMaterialism) + 1 extra
    assert c["gold_count"] == 3 and c["recon_count"] == 3 and c["shared"] == 2
    assert c["precision"] == pytest.approx(2 / 3, abs=1e-3)
    assert c["recall"] == pytest.approx(2 / 3, abs=1e-3)


def test_anchoring_flags_reception_inflation(result):
    a = result["metrics"]["anchoring_rate"]
    assert a["claims_detected"] >= 3
    # the unanchored "Audiences were deeply moved" must be surfaced
    joined = " ".join(ex["sentence"] for ex in a["unanchored_examples"]).lower()
    assert "deeply moved" in joined
    assert 0.0 <= a["rate"] <= 1.0


def test_structural_coverage_full_on_pattern1_fixture(result):
    assert result["metrics"]["structural_coverage"]["coverage"] == pytest.approx(1.0)


def test_contamination_probe_is_reverse_read(result):
    p = result["metrics"]["contamination_probe"]
    assert "REVERSE" in p["measures"] or "reverse" in p["note"].lower()
    assert p["flag"] in {"ok", "ELEVATED", "HIGH-CONTAMINATION-WARNING"}


def test_per_layer_divergence_thesis(result):
    pl = result["metrics"]["per_layer_similarity"]
    # the thesis: transferable content converges (higher) > generative content (lower),
    # tested on grouped layer blobs (robust to per-paper segmentation)
    assert pl["transferable_similarity"] is not None and pl["generative_similarity"] is not None
    assert pl["transferable_similarity"] > pl["generative_similarity"]
    assert pl["thesis_supported"] is True


def test_high_similarity_is_not_treated_as_quality(result):
    # discipline check: no metric exposes a "quality" or "score" verdict field
    for m in result["metrics"].values():
        assert "quality_score" not in m and "verdict" not in m
