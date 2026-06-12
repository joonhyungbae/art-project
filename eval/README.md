# Reconstruction-Benchmark Harness

Stdlib-only metric engine for instrumenting a model reconstruction against a held-out gold paper. It **instruments**; it does **not** score quality.

This engine was developed for the companion paper currently in submission to *Digital Creativity* (Routledge / Taylor & Francis); the plugin ships the engine, not the data.

## What's here

| Path | Role |
|---|---|
| `instrumentation.py` | the metric engine (stdlib-only; CLI + importable) |
| `embedding_backend.py` | optional sentence-embedding similarity (needs `sentence-transformers` + `torch`) |
| `report_template.yaml` | report template, conforms to `shared/benchmark_report.schema.json` |
| `fixtures/synthetic_case/` | a synthetic case proving the engine runs end-to-end |

The engine is self-tested against the synthetic fixture only.

> **Pilot data is not in this repo.** Per-case extracted inputs, gold transcriptions, model reconstructions, and aggregated results are gitignored under `eval/pilot/` (the whole directory) because the `gold/paper.md` files are transcriptions of paywalled journal/proceedings sources (Digital Creativity / Routledge–T&F, Leonardo / MIT Press, ISEA, SIGGRAPH Asia / ACM). The reproducibility package — input packs, gold briefs, pre-registration hash, and per-case results — will be released through the companion paper's supplementary-materials channel after acceptance. The plugin ships only the harness code and the synthetic test fixture.

## Metrics (`instrumentation.py`)

Each metric carries a `does_not_license` field naming what it must NOT be read as.

- **citation_set_pr** — did art-paper surface the gold's precedent works/theory? (lineage layer)
- **anchoring_rate** — fraction of reception/novelty/capability claims anchored or hedged
- **structural_coverage** — did the output produce the Pattern-1 layers?
- **contamination_probe** — n-gram overlap with gold, **read in reverse** (high = memorization flag)
- **per_layer_similarity** — transferable layers should converge, generative layers diverge

## Run

```sh
# try the engine on the bundled synthetic case
python eval/instrumentation.py eval/fixtures/synthetic_case
python eval/instrumentation.py eval/fixtures/synthetic_case --json
```

To run the engine on a real case, populate `eval/pilot/<paper_id>/{gold,input,reconstruction}/` locally — the directory shape mirrors `eval/fixtures/synthetic_case/`. Each subdirectory holds `paper.md` and `refs.bib`.

## Semantic (GPU) backend

`eval/embedding_backend.py` adds optional sentence-embedding similarity (run with `python eval/instrumentation.py <case> --embed`; needs `sentence-transformers` + `torch`, model via `CRS_EMBED_MODEL`, default `BAAI/bge-small-en-v1.5`). Default runs stay stdlib/lexical so the test suite needs no GPU.

Empirical observation from harness development: naive sentence-embedding cosine is **topic-saturated within a single paper** — every layer of the same artwork embeds at ~0.95, so blob cosine barely separates transferable from generative layers. The lexical n-gram/Jaccard primary metric is the better discriminator for the transferable/generative pattern; the embedding contamination probe is topic-confounded (high chunk cosine even with zero verbatim overlap). Use the n-gram measure for contamination; a meaningful semantic contamination signal needs a cross-paper baseline.

## Boundaries (honest)

- The engine is automatable solo (stdlib only); the input/gold extraction and the paid pipeline run are human steps — the harness makes them turnkey.
- `per_layer_similarity` uses lexical n-gram/Jaccard; the embedding backend is an optional alternate, and the default lexical path runs everywhere.
- Quality is never scored. A blindable cross-model LLM judge is a separate concern from this engine.
