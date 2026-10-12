# Task reference

Use the actual versioned OrtApi interface and documented Release functions. Tensor type/shape/allocator ownership is part of the ABI contract. An ONNX inference session is not a general autograd trainer. For custom training kernels, independently validate gradients and numerical state; keep those claims separate from exported-model inference.

Primary sources:
- https://onnxruntime.ai/docs/get-started/with-c.html
- https://onnxruntime.ai/docs/api/c/
