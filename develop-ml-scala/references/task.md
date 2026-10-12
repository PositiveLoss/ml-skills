# Task reference

Spark Pipeline stages separate transformers and estimators but do not automatically prevent temporal/group leakage. CrossValidator split defaults must match the intended unit. Random seed does not guarantee partition/order-independent numerical results. ONNX/DJL inference on Scala uses JVM/native APIs and needs explicit executor lifecycle and thread budgets.

Primary sources:
- https://spark.apache.org/docs/latest/ml-pipeline.html
- https://spark.apache.org/docs/latest/ml-tuning.html
- https://onnxruntime.ai/docs/get-started/with-java.html
