---
name: test-ml-software
description: "Develop meaningful tests for ML code and serving boundaries. Use for preprocessing contracts, gradients, metamorphic tests, train/eval behavior, save/reload parity, export regressions and nondeterministic tolerance design."
---

# Test ML software

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Separate software invariants from dataset-dependent quality gates. Identify stable contracts for schema, transformations, gradients, serialization and serving lifecycle.
2. Test tiny analytically checkable problems and deliberate failures: permuted columns, invalid masks, NaNs, duplicate groups or incompatible model metadata.
3. Use metamorphic invariants only where the task supports them: batch/single equivalence, permutation invariance of sets or translation invariance within the chosen preprocessing.
4. Set numerical tolerances by dtype/backend and compare absolute/relative errors plus task decisions. Test train/eval changes and checkpoint/export round trips.
5. Use fixed small datasets in CI and risk-based GPU/device jobs. Record which failures are genuine regressions versus stochastic quality fluctuation.

## Acceptance evidence

Show each test detects a plausible fault, runs within bounded resources and does not merely mirror the implementation. Provide both numerical parity and end-to-end decision/metric checks.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
