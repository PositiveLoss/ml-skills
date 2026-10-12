---
name: train-deep-learning-models
description: "Design and implement deep-learning training experiments across frameworks. Use for architecture/baseline choice, optimization, initialization, batching, regularization, checkpoints and controlled quality comparisons."
---

# Train deep learning models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define task/data contract and establish a small baseline before selecting network complexity. Check architecture receptive field, output dimension and available data/compute.
2. Verify a single forward/backward step, finite loss/gradients and ability to overfit a tiny clean batch. Check label alignment, padding/masks and output/loss compatibility.
3. Separate training/evaluation modes and use fold-correct preprocessing. Control seeds, data loader order, regularization, optimizer and learning-rate schedule; record effective batch semantics.
4. Save model, optimizer, scheduler, scaler and RNG/data-progress state as required for resumability. Compare uninterrupted with resumed training in a bounded fixture.
5. Select checkpoints by validation only and evaluate a fixed chosen candidate on blind test slices. Profile resource use rather than attributing every quality gain to architecture.

## Acceptance evidence

Provide tiny-batch overfit, gradient/mask checks, validation curves, exact checkpoint selection policy and a resume test. Mark distributed/GPU results separately from CPU smoke results.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
