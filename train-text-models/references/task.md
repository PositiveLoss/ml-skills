# Task reference

Random train/test splits can leak boilerplate/duplicate documents. Subword token indices are not character offsets; extraction span mapping needs tests. Classification probabilities, retrieval similarities and language-model likelihood are different outputs. Tokenizer identity is part of the model contract and should not silently update independently.

Primary sources:
- https://huggingface.co/docs/transformers/tasks/sequence_classification
- https://huggingface.co/docs/tokenizers/index
- https://scikit-learn.org/stable/modules/feature_extraction.html
