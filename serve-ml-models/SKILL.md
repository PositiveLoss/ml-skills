---
name: serve-ml-models
description: "Implement reliable ML inference services. Use for Python/native serving, HTTP/gRPC boundaries, batching, model lifecycle, preprocessing parity, timeouts, resource limits and readiness."
---

# Serve ML models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define versioned input/output schema, preprocessing, model identity, error behavior and supported shapes. Map request limits and deadline/latency budgets.
2. Load validated artifacts once per supported lifecycle and warm representative shapes. Bound batch queues, concurrency and memory; avoid per-request session/model construction.
3. Keep blocking/accelerator work off async request loops through a bounded executor/scheduler. Propagate request cancellation without pretending a non-cancelable native kernel stops immediately.
4. Verify preprocessing/tokenizer parity, status/error mapping and batch/single outputs. Separate model readiness from process liveness and record fallback/provider behavior.
5. Test overload shedding, deadline expiry, model swap/drain and rollback. Profile end-to-end latency including queueing, decoding and transfers.

## Acceptance evidence

Provide real request tests, bounded slow/oversized inputs, schema errors, batch parity and cleanup. Benchmark p50/p95/p99 with error/coverage rates and model/version tags.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
