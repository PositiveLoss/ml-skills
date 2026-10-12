# Task reference

Prefer composable fitted pipelines such as ColumnTransformer/Pipeline for tabular training. Sparse/dense conversions and one-hot cardinality can dominate memory. Avoid computing normalization statistics across a blind test set. For audio/image pipelines, record channel order, resampling/filtering and normalization with model identity rather than duplicating handwritten defaults in each service.

Primary sources:
- https://scikit-learn.org/stable/modules/compose.html
- https://scikit-learn.org/stable/modules/preprocessing.html
