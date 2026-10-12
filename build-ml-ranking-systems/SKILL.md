---
name: build-ml-ranking-systems
description: "Build and evaluate ML retrieval/recommendation/ranking systems. Use for candidate generation, embeddings, negative sampling, leakage, cold start, query-group metrics, reranking and offline/online differences."
---

# Build ML ranking systems

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define query/user context, candidate universe, relevance/exposure labels and decision-time features. Separate retrieval recall from reranker performance.
2. Split by entity/time and construct training negatives without revealing future labels or test candidates. Inspect exposure/position bias and feedback loops.
3. Compare lexical/popularity/simple retrieval baselines with embedding/ranking candidates. Preserve index, encoder, tokenizer and candidate snapshot identities.
4. Compute recall/MRR/NDCG with explicit cutoff, relevance gains, ties and candidate universe. Resample queries/users rather than every candidate row.
5. Evaluate cold-start, latency, index freshness and online behavior through the declared rollout protocol. Do not infer online business lift from a favorable offline metric alone.

## Acceptance evidence

Provide fixed query/candidate fixtures, ranking-metric definitions and retrieval-vs-reranker breakdown. Verify index/encoder mismatch detection and query-level uncertainty.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
