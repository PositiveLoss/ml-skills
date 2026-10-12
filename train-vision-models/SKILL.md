---
name: train-vision-models
description: "Train and evaluate image/video ML, detection, segmentation and OCR/HTR. Use for source-image leakage, augmentation label geometry, class imbalance, transfer learning, NMS/decoder behavior and deployment preprocessing."
---

# Train vision models

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

## Workflow

1. Define classification/detection/segmentation/OCR target and annotation format. Inspect original images/documents/video sessions, label quality and target deployment cameras/domains.
2. Split original sources before crops/frames/augmentations; separate near duplicates and related document pages where needed. Track temporal/spatial correlation.
3. Verify channel order, orientation, resizing, coordinate systems, normalization and padding. Apply geometric transforms consistently to boxes/masks/text annotations; augment training only.
4. Establish pretrained/frozen and small baseline models, verify tiny-batch learning and task-appropriate losses. Record pretrained-data overlap and augmentation budget.
5. Evaluate per-class/size/domain metrics with fixed IoU/NMS/decoder thresholds; include OCR normalization and frame-to-document aggregation. Verify source-vs-runtime preprocessing and output geometry.

## Acceptance evidence

Provide golden geometry/augmentation examples, original-source split audit and held-out error slices. Device inference must preserve resize/channel/postprocessing behavior, not only network logits.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
