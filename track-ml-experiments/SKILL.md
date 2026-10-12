---
name: track-ml-experiments
description: "Set up consistent ML experiment tracking with MLflow or the existing tracker. Use for run identity, dataset lineage, hyperparameters, artifacts, nested trials, metric step semantics and model comparison."
---

# Track ML experiments

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Choose the existing tracking backend and define run, trial, fold and seed identities. Record immutable code/data/config/environment references before execution.
2. Log parameters and metrics with explicit step/unit/aggregation semantics. Separate train, validation, final test and deployment metrics; avoid logging validation values under misleading test names.
3. Preserve checkpoint/tokenizer/preprocessing/label metadata and raw evaluation predictions where permitted. Hash large artifacts and bound logging volume.
4. Include failed/pruned/retried runs and compute budgets. Compare only runs with compatible evaluation populations and protocols.
5. Test interrupted-run recovery and artifact restoration without assuming a tracker automatically ensures reproducibility or authorizes model publication.

## Acceptance evidence

Provide a minimal recorded run whose artifacts/config restore correctly and metrics have consistent steps. Show comparisons expose data/split/version differences rather than sorting incompatible scores.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
