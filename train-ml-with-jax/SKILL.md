---
name: train-ml-with-jax
description: "Implement and review JAX training with explicit state and random keys. Use for jit/grad/vmap, pytrees, RNG reuse, compilation shapes, distributed sharding, numerical checks and checkpoint/export compatibility."
---

# Train ML with JAX

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Pin JAX/jaxlib/backend and inspect device availability. Define parameter, optimizer, RNG and data state as explicit pytrees rather than mutable captured globals.
2. Validate unjitted forward/loss/gradient behavior and finite differences on a tiny fixture. Split/advance random keys deliberately; avoid reusing keys for independent dropout/augmentation.
3. JIT stable-shape pure steps; identify static arguments and Python control flow that changes tracing. Use runtime debug/check APIs where supported rather than assuming Python print executes each step.
4. Monitor recompilation, dtype/X64 settings, device transfers and asynchronous execution. Synchronize on completion when benchmarking.
5. Verify checkpoint state and sharding layouts, then test the actual export/serving consumer. Treat experimental APIs and distributed topology as version-dependent.

## Acceptance evidence

Show same input/state produces the expected step, keys advance correctly, gradients pass a numerical check and benchmarks wait for device work. Record tested devices and compilation behavior.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
