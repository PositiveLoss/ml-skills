# Task reference

Detection/segmentation metrics depend on label quality, thresholds and ignored regions. OCR CER/WER requires declared normalization and document/speaker-like grouping. Random splitting of nearby video frames can dramatically overstate generalization. Treat pretrained benchmark overlap as evaluation contamination when it is material.

Primary sources:
- https://docs.pytorch.org/vision/stable/index.html
- https://docs.pytorch.org/vision/stable/auto_examples/transforms/plot_transforms_e2e.html
- https://huggingface.co/docs/transformers/tasks/object_detection
