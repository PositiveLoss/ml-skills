---
name: debug-ml-training
description: "Diagnose failing or misleading ML training. Use for NaNs, loss explosions, no learning, accidental freezing, target/mask errors, validation gaps, OOM, data-loader hangs and checkpoint regressions."
---

# Debug ML training

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Reproduce on a tiny fixed dataset and capture model/data/config/seed/device versions. Separate data, forward, loss, backward, optimizer, evaluation and serialization stages.
2. Inspect real examples, labels, tensor ranges, masks and sample ordering. Confirm a simple model can learn and the current model can overfit a tiny clean batch.
3. Check finite activations/gradients, parameters requiring gradients, optimizer membership, learning rate and update counts. Locate the first invalid operation before applying blanket clipping.
4. Inspect train/eval mode, metric aggregation and split leakage. Measure retained graphs, buffers, loader queues and synchronization when diagnosing OOM or hangs.
5. Fix the smallest supported cause and add a regression test that fails before the patch. Rerun the original workload plus quality checks affected by the fix.

## Acceptance evidence

Provide a minimal reproduction, first failing stage, before/after evidence and bounded regression. Avoid declaring a numerical bug solved merely because NaNs were suppressed or batches skipped.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
