"""Optional GPU embedding backend for the §4 per-layer / contamination metrics.

Default instrumentation is stdlib-only (lexical n-gram/Jaccard). This module adds
SEMANTIC similarity via sentence-transformers when available, which the methodology
§4 row 6 actually specifies ("sentence-embedding cosine") — lexical Jaccard
understates transferable convergence because the reconstruction paraphrases.

Used only when `instrumentation.py --embed` is passed. Import is guarded so the
default path (and CI without a GPU) never depends on torch.

Model: override with CRS_EMBED_MODEL (default: a small BGE retrieval model that
fits trivially on a 24GB GPU and is fine on CPU too).
"""
from __future__ import annotations

import os
import re

_MODEL_NAME = os.environ.get("CRS_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
_SENT = re.compile(r"(?<=[.!?])\s+")
_model = None


def available() -> bool:
    try:
        import sentence_transformers  # noqa: F401
        return True
    except Exception:
        return False


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _model = SentenceTransformer(_MODEL_NAME, device=device)
    return _model


def _chunks(text: str, max_sents: int = 5) -> list[str]:
    sents = [s.strip() for s in _SENT.split(text) if s.strip()]
    if not sents:
        return []
    return [" ".join(sents[i:i + max_sents]) for i in range(0, len(sents), max_sents)]


def _doc_vector(text: str):
    """Mean-pooled, L2-normalized embedding over sentence chunks (handles long text)."""
    import numpy as np
    chunks = _chunks(text)
    if not chunks:
        return None
    emb = _get_model().encode(chunks, normalize_embeddings=True, show_progress_bar=False)
    v = np.asarray(emb).mean(axis=0)
    n = (v @ v) ** 0.5
    return v / n if n else v


def semantic_similarity(a: str, b: str):
    """Cosine similarity of two texts' mean-pooled embeddings, or None if empty."""
    va, vb = _doc_vector(a), _doc_vector(b)
    if va is None or vb is None:
        return None
    return round(float(va @ vb), 4)


def semantic_alignment(gold: str, recon: str):
    """Mean over GOLD chunks of the best-matching RECON chunk cosine — "was this
    specific content reproduced?". More discriminating than blob mean-pool cosine
    (which saturates on shared topic), but still topic-influenced; report alongside
    the lexical measure, which discriminates transferable vs generative best."""
    import numpy as np
    cg, cr = _chunks(gold), _chunks(recon)
    if not cg or not cr:
        return None
    m = _get_model()
    eg = np.asarray(m.encode(cg, normalize_embeddings=True, show_progress_bar=False))
    er = np.asarray(m.encode(cr, normalize_embeddings=True, show_progress_bar=False))
    return round(float((eg @ er.T).max(axis=1).mean()), 4)


def semantic_max_chunk(a: str, b: str):
    """Max chunk-to-chunk cosine — a paraphrase-memorization signal for contamination
    (high semantic match with low verbatim n-gram = possible memorized paraphrase)."""
    import numpy as np
    ca, cb = _chunks(a), _chunks(b)
    if not ca or not cb:
        return None
    m = _get_model()
    ea = np.asarray(m.encode(ca, normalize_embeddings=True, show_progress_bar=False))
    eb = np.asarray(m.encode(cb, normalize_embeddings=True, show_progress_bar=False))
    return round(float((ea @ eb.T).max()), 4)


def model_name() -> str:
    return _MODEL_NAME
