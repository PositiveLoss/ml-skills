---
name: maintain-ml-pipelines
description: "Build and maintain reproducible ML data/training/evaluation/release pipelines. Use for orchestration, data/model versioning, cached stages, lineage, checkpoint restart, CI quality gates and artifact promotion."
---

# Maintain ML pipelines

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Model stages and artifact contracts: ingest, validate, split, preprocess, train, evaluate, package and promote. Distinguish immutable inputs from temporary/cache outputs.
2. Key caches by data/split/config/code/tool identity; avoid reuse after preprocessing or label changes. Make stage reruns idempotent and atomic for artifact publication.
3. Use bounded resources, explicit failure/retry policies and resumable checkpoints. Prevent retried training/promotion from silently duplicating records or changing evaluation ownership.
4. Gate quality, schema, export parity and serving performance separately. Keep release authorization/credentials out of untrusted data jobs or PR runs.
5. Verify a fresh small end-to-end run, interruption recovery, invalid input rejection and rollback. Document provenance through the deployed artifact.

## Acceptance evidence

Show lineage, deterministic cache invalidation and controlled failure recovery. Include negative tests for stale data/config artifacts and unsuccessful evaluations that must block promotion.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
