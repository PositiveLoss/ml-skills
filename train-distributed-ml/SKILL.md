---
name: train-distributed-ml
description: "Implement and diagnose distributed ML training. Use for PyTorch DDP/FSDP or existing JAX/TF strategies, sharding, samplers, gradient synchronization, uneven batches, failure recovery and global metric correctness."
---

# Train distributed ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Establish a correct single-device run, then pin runtime/backend/topology and define global batch, gradient accumulation and data sharding.
2. Ensure each rank receives intended samples without accidental duplicate/leaked evaluation. Handle sampler epochs, padding/uneven batches and valid-token loss normalization.
3. Verify synchronized parameters/gradients and collective call order. Avoid rank-conditional operations that deadlock or silently change gradient reduction semantics.
4. Aggregate metric numerators/denominators and predictions correctly across ranks. Check checkpoint formats, optimizer shards, RNG states and topology-dependent restore.
5. Exercise controlled worker failure/restart with bounded shutdown, then compare distributed quality/resource use against the single-device reference.

## Acceptance evidence

Provide a small multi-process test, global-batch/loss equivalence evidence and checkpoint recovery. Do not claim multi-GPU, multi-node or network-backend support from a single CPU run.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
