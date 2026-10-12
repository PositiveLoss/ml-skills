# Task reference

A smaller Brier loss does not by itself prove better calibration. ECE depends on binning and can conceal sparse-bin uncertainty. Isotonic calibration can overfit small datasets; temperature scaling preserves some rankings but not every task property. A score of 0.9 is not a guaranteed 90% confidence for an arbitrary new deployment distribution.

Primary sources:
- https://scikit-learn.org/stable/modules/calibration.html
- https://scikit-learn.org/stable/modules/classification_threshold.html
