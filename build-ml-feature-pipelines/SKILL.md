---
name: build-ml-feature-pipelines
description: "Build and review preprocessing/feature pipelines for ML. Use for scaling, imputation, categorical encoding, feature stores, point-in-time joins, tokenizer versions, audio/image preprocessing and train-serving skew."
---

# Build ML feature pipelines

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define input schema, units, missing-value behavior and feature availability time. Distinguish deterministic transformations from fitted state.
2. Fit all learned transformations inside the training fold. Include categorical vocabularies, target encoders, imputers and feature selection; use out-of-fold target encoding where justified.
3. Use point-in-time-correct joins and label horizons for historical data. Track source versions and avoid backfilled features unavailable during real prediction.
4. Serialize preprocessing metadata with the model: feature order, dtype, normalization, tokenizer/label maps, sampling rate and shape conventions. Apply identical inference transformations.
5. Test unknown/missing/out-of-range inputs and batch/single parity. Check stale feature availability and online/offline differences before serving.

## Acceptance evidence

Show preprocessing was fitted on training units only, and golden raw inputs produce equivalent features/predictions in train and serve implementations. Assert changed column order or tokenizer identity is rejected.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
