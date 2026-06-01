# Project Hypotheses

## H01: Reranking helps only after the data fix

Current belief: unresolved

Evidence:
- A7 supports the retrieval baseline.
- A8 is not decisive because the reranking comparison is not clean enough.

Risk:
- The old reranking note may be stale, but A8 may also be a true negative.

Next most informative contrast:
- Compare retrieval-only and retrieval-plus-reranking on the same data snapshot,
  same evaluation set, same scoring script, and same seed.

Update rule:
- Strengthen H1 if same-snapshot reranking beats retrieval-only by a meaningful
  precision delta without hurting recall.
- Weaken H1 if same-snapshot reranking remains flat or worse under the same
  scoring script.
