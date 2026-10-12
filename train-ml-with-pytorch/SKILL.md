---
name: train-ml-with-pytorch
description: "Implement PyTorch ML training loops and diagnose optimization or checkpoint failures. Use for autograd, loss reduction, DataLoader behavior, mixed precision, eval mode, deterministic smoke tests and resumable training."
---

# Train ML with PyTorch

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Inspect installed torch/device support and lock the training configuration. Establish CPU full-precision correctness before enabling AMP, compile or distribution.
2. Verify tensor shapes/dtypes, logits/targets, finite gradients and parameter updates. Reset gradients deliberately and normalize losses by the intended sample/token count.
3. Use model.train for optimization and model.eval with the correct no-grad/inference context for evaluation. Bound DataLoader workers and avoid retaining computation graphs in logging/history.
4. Enable AMP with APIs supported by the installed version; unscale before clipping if using a scaler. Ensure accumulation and scheduler steps match successful optimizer updates.
5. Preserve checkpoint/RNG/optimizer state and verify resume equivalence at a controlled boundary. Use safe loading policies for external artifacts and compare held-out quality/resource use.

## Acceptance evidence

Run scripts/torch_smoke.py on CPU: finite loss/gradients, changed weights, eval repeatability and uninterrupted-vs-resumed updates. Do not report AMP/GPU/distributed support from this fixture.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
