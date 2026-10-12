# Task reference

Model formats and C++ loading paths evolve; do not assume a deprecated TorchScript export is required for every modern deployment. Tensor views and from-blob tensors can outlive borrowed storage incorrectly. Mixing runtime binaries built with different C++ ABIs can fail despite identical headers. Use supported package targets and dependency versions.

Primary sources:
- https://onnxruntime.ai/docs/get-started/with-cpp.html
- https://docs.pytorch.org/cppdocs/
