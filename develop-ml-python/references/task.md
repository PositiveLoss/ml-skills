# Task reference

Prefer reusable functions/pipelines and explicit resource scopes over hidden notebook globals. NumPy views, dtype casts, multiprocessing start methods and thread pools affect memory/correctness. Use the bundled train-tabular-ml and train-ml-with-pytorch CPU examples as runnable smoke starting points; they are not benchmarks for production data.

Primary sources:
- https://scikit-learn.org/stable/common_pitfalls.html
- https://docs.pytorch.org/docs/stable/notes/randomness.html
- https://onnxruntime.ai/docs/get-started/with-python.html
