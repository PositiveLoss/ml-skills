# Task reference

Static calibration and dynamic quantization serve different operator/workload cases. Quantized kernels/provider support and partitioning determine speed. Distillation targets may leak evaluation information when the teacher consumed the holdout. Pruning requires a runtime/kernel that exploits the structure to translate sparsity into latency savings.

Primary sources:
- https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html
- https://docs.pytorch.org/docs/stable/quantization.html
