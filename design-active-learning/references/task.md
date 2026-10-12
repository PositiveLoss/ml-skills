# Task reference

Uncertainty sampling can select out-of-distribution noise and miss confident mistakes. Selection changes the labeled-data distribution; naive evaluation on acquired examples is biased. Diversity and uncertainty scores depend on model/encoder revisions. Batch acquisition must account for within-batch redundancy.

Primary sources:
- https://arxiv.org/abs/1708.00489
- https://scikit-learn.org/stable/modules/calibration.html
