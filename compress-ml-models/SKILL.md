---
name: compress-ml-models
description: "Reduce ML model size, latency or memory through quantization, pruning and distillation. Use for PTQ/QAT, representative calibration, teacher/student leakage, sparse runtime support and deployment-quality tradeoffs."
---

# Compress ML models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Freeze a correct source model, task metrics and target hardware/runtime/operator support. Measure model/activation size, latency and memory baseline.
2. Choose quantization, pruning or distillation from measured bottlenecks. Use representative permitted training/calibration data, excluding the blind test set.
3. Verify quantization ranges/dtypes and calibration coverage; check whether sparse/pruned structures accelerate the actual runtime rather than only reducing zeros in tensors.
4. Compare source/candidate predictions on boundary/slice inputs and task metrics. Include preprocessing/decoder changes and teacher-data overlap in the evaluation.
5. Benchmark the complete target-device pipeline and preserve rollback artifacts. Report accuracy/latency/memory tradeoffs and unsupported operators/fallbacks.

## Acceptance evidence

Provide numerical and task-level parity budgets, calibration-data identity, hardware measurements and sensitive slices. Do not infer speedup from parameter count or a nominal INT8 file alone.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
