# Task reference

A loss decrease may coexist with an unchanged model if logging uses stale predictions. Accidental detach/no_grad, zero learning rate or optimizer constructed before parameter replacement can prevent updates. Tensor shape broadcasting can produce plausible loss values for an invalid objective. Distinguish genuine GPU memory pressure from CPU loader growth and graph retention.

Primary sources:
- https://docs.pytorch.org/docs/stable/autograd.html
- https://docs.pytorch.org/docs/stable/notes/cuda.html
- https://scikit-learn.org/stable/common_pitfalls.html
