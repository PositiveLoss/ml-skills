# Task reference

An increasing training score with stagnant validation can reflect leakage, distribution mismatch or overfitting; inspect data before adding layers. Averaging per-batch metrics without sample weighting can bias the result. Dropout and batch-normalization behavior differs between train/eval. Compare architecture changes with the same optimization budget and report uncertainty across seeds when material.

Primary sources:
- https://docs.pytorch.org/docs/stable/autograd.html
- https://docs.pytorch.org/docs/stable/optim.html
- https://docs.pytorch.org/docs/stable/notes/randomness.html
