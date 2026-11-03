# Anchor

Last changed: 2026-06-01

## Core question

- Does reranking improve answer precision once the data snapshot is fixed?

## Core method

- Mechanism: a reranker reorders the retriever's top 50 before generation.
- Prerequisite: the same data snapshot, evaluation set and scoring script for every arm.

## Claims

- C1: reranking raises precision@10 without hurting recall (evidence: H01, Table 1).

## Final system

- RAG pipeline on the current data snapshot (when the snapshot changes, every cell becomes `interim`).

## Main table

| table / figure | rows | columns or metric | cell status |
|---|---|---|---|
| Table 1 | retrieval only; retrieval + reranking | precision@10, recall@10 | pending |

## Peer grounding

- Precision@10 and recall@10 on the shared evaluation set, as in the team's earlier RAG reports.

## Terms

- A data fix is not a retrieval change: results across snapshots are not comparable.

## Scarce resources

- Human relevance labels: only for Table 1 cells, a 20-query smoke first.

## Off-table

- Query rewriting (no cell; recorded, not pitched).

## Corrections

- 2026-06-01: an old reranking note predates the data fix -> archived; read it only on explicit recall.
