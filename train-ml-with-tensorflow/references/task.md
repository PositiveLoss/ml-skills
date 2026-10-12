# Task reference

Do not assume a Keras native model file and a TensorFlow SavedModel are interchangeable across current versions. A repeated/shuffled dataset can hide its sample-count semantics; define steps-per-epoch consciously. Cache after stochastic augmentation changes the augmentation process. Validate exported preprocessing/signatures rather than only the training model object.

Primary sources:
- https://www.tensorflow.org/guide/keras/training_with_built_in_methods
- https://www.tensorflow.org/guide/function
- https://www.tensorflow.org/guide/saved_model
