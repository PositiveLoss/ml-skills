---
name: audit-ml-datasets
description: "Audit training/evaluation data quality and provenance for machine learning. Use for label errors, duplicate leakage, corrupt samples, sampling bias, missingness, dataset permissions and manifest validation."
---

# Audit ML datasets

Read [ML evidence contract](references/evidence.md) before implementation and [task reference](references/task.md) for task-specific decisions and checks.

Read [executable helper](references/tools.md) before using the bundled script and fixtures.

## Workflow

1. Inventory sources, collection/labeling procedures, consent/licensing scope, schema, units, timestamps and dataset revisions. Trace samples to their original entity/session/document rather than filenames alone.
2. Measure missingness, impossible ranges, corrupt files, label distribution and disagreement. Inspect representative examples and edge slices; distinguish label noise from a genuinely ambiguous task.
3. Check exact/content duplicates and related entities across splits. Use near-duplicate methods appropriate to audio/images/text and document their thresholds instead of asserting exact hashes detect all leakage.
4. Compare sampling and label availability with the target deployment population. Identify outcome-dependent selection, stale labels and features created after the prediction time.
5. Produce a prioritized repair/annotation plan and rerun audits on a versioned manifest. Preserve raw inputs and log exclusions with reasons rather than silently deleting troublesome samples.

## Acceptance evidence

Provide reproducible counts, sample-level issue examples, cross-split overlaps and coverage slices. Show malformed input and an intentional group/content overlap fail the bundled manifest checker.

Report the change, supported versions/devices, evaluation units and actually executed checks. Separate reproducible findings from proposed experiments and untested backends.
