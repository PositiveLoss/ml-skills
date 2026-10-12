# Task reference

Changing candidate set size can change ranking metrics without improving the model. Sampled negatives and real catalog ranking are different evaluations. Logged clicks are confounded by exposure and position; offline relevance metrics do not automatically correct this. Training and serving must agree on embedding normalization/dimension and similarity.

Primary sources:
- https://scikit-learn.org/stable/modules/model_evaluation.html
- https://www.tensorflow.org/recommenders
