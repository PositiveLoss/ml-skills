# Task reference

Use Java interop for ONNX Runtime or the current Android LiteRT APIs as supported by the project. Delegate/provider availability and speed depend on device/OS/model operators. Coroutine cancellation does not guarantee a native kernel stops. A ViewModel lifetime, application session lifetime and background worker lifetime are different ownership boundaries.

Primary sources:
- https://developers.google.com/edge/litert/android
- https://onnxruntime.ai/docs/get-started/with-java.html
- https://onnxruntime.ai/docs/tutorials/mobile/
