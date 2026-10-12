---
name: reproduce-ml-experiments
description: "Reproduce ML experiments and training checkpoints. Use for seed/version/device manifests, dataset identities, clean environment reruns, resumability, paper result verification and reproducibility claims."
---

# Reproduce ML experiments

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Capture executable code/config, data/split hashes, preprocessing, dependency/compiler/device versions and randomness sources. Identify missing originals before choosing substitutes.
2. Reproduce the smallest claimed result with a controlled environment and fixed evaluation. Distinguish exact rerun, approximate reproduction and independent reimplementation.
3. Restore optimizer, scheduler, scaler, RNG and data-progress state when testing resume. Verify data-loader shuffle/worker seeds and checkpoint boundary semantics.
4. Compare metric distributions across seeds and resource costs, not only a best run. State nondeterministic kernels and version/device limitations.
5. Package commands, manifests and evidence without private data/secrets. Preserve raw failures and explain materially different preprocessing, compute or evaluation.

## Acceptance evidence

Show a fresh rerun and controlled uninterrupted/resumed comparison. Confirm file hashes with scripts/hash_artifacts.py; state what hash equality proves and what it does not.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
