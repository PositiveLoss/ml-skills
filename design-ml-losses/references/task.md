# Task reference

Class weighting, focal losses and negative sampling alter effective training distributions and may affect calibration. All-masked batches need defined behavior rather than division by zero. Gradient accumulation can change reduction scaling. Pair/list ranking loss requires correctly constructed candidate groups; random unrelated comparisons may optimize the wrong task.

Primary sources:
- https://docs.pytorch.org/docs/stable/nn.html
- https://scikit-learn.org/stable/modules/model_evaluation.html
