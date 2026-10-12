# Task reference

Mobile providers/delegates may partition a graph and introduce expensive copies or CPU fallback. Desktop Apple MPS training and CoreML deployment are separate paths. Runtime packaging differs by ABI and accelerator package. For telephony/vision, measure full preprocessing and decode queues; model latency alone omits important on-device cost.

Primary sources:
- https://developers.google.com/edge/litert/android
- https://onnxruntime.ai/docs/tutorials/mobile/
- https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html
