# Task reference

ONNX Java native artifacts depend on platform/provider packages. DJL uses engines with different operator/device/training support; NDManager ownership can invalidate arrays outside their manager scope. Java heap size is not a full measure of native tensor/session memory. Track off-heap resources and avoid oversubscribing native thread pools.

Primary sources:
- https://onnxruntime.ai/docs/get-started/with-java.html
- https://docs.djl.ai/
