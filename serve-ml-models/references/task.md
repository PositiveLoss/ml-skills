# Task reference

Dynamic batching increases utilization but may violate latency budgets. A canceled HTTP request can leave inference running unless ownership and cleanup are explicit. Native runtime threading plus service worker pools can oversubscribe CPUs. For gRPC, use the existing contract/streaming skills and preserve model metadata separately from transport schemas.

Primary sources:
- https://onnxruntime.ai/docs/performance/tune-performance/threading.html
- https://onnxruntime.ai/docs/get-started/with-python.html
- https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html
