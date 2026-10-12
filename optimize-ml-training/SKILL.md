---
name: optimize-ml-training
description: "Profile and improve ML training speed and memory. Use for loader bottlenecks, AMP, compilation, accumulation, checkpointing, batch sizing, kernels and evidence-based training efficiency comparisons."
---

# Optimize ML training

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Establish fixed data/model/config and measurement scope: samples/tokens per second, time to target quality, peak host/device memory and cost. Separate warmup/compilation from steady state.
2. Profile data loading, transfers, compute, synchronization and logging. Synchronize accelerator work before timing and record input shape/padding distribution.
3. Apply one supported change at a time: precision, batching, worker/prefetch bounds, compiled steps or activation checkpointing. Preserve effective batch/loss semantics.
4. Rerun gradient, checkpoint and validation checks; detect numerical drift and unsupported backend fallback. Include throughput, tail step time and memory under realistic data.
5. Compare time-to-quality and total compute, not just faster steps with worse optimization. Retain raw traces and rollback the change if evidence does not support it.

## Acceptance evidence

Provide a baseline/candidate benchmark with device/version, synchronization, repeated runs, memory and held-out quality. State whether improvements include compile/setup time.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
