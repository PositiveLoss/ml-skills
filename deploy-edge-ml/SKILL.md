---
name: deploy-edge-ml
description: "Deploy ML inference on Android, Apple or embedded/edge devices. Use for LiteRT/ONNX Runtime mobile/CoreML, quantized models, accelerator delegates/providers, thermal limits, offline assets and ABI packaging."
---

# Deploy edge ML

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Specify device/OS/ABI, supported runtime/provider, memory/power/latency and offline update constraints. Separate desktop correctness from actual device support.
2. Export a validated model/preprocessing contract and inspect operators, delegate coverage, CPU fallback and supported shapes. Choose quantization using representative calibration inputs.
3. Package verified assets/native libraries and manage session/tensor lifetime. Keep inference off UI/audio realtime threads and bound frame/chunk queues.
4. Test startup, repeated inference, app background/restart, asset corruption and provider failure. Measure warm/cold latency, peak memory, energy and sustained thermal throttling.
5. Compare device predictions with the source model and task metrics. Maintain rollback/versioned asset identity and document unsupported devices/providers.

## Acceptance evidence

Provide device/OS/runtime/provider evidence and sustained measurements. Do not infer Android/iOS/CoreML/MPS acceleration or hard realtime performance from a desktop CPU test.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
