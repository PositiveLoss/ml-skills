# Task reference

GroupKFold/StratifiedGroupKFold and TimeSeriesSplit answer different questions; combining groups and time can require a custom splitter. Stratification must not override entity isolation. Bootstrap groups or time blocks according to dependence, not every row independently. Use the exact manifest helper in audit-ml-datasets when available, but independently enforce timestamps and label horizons.

Primary sources:
- https://scikit-learn.org/stable/modules/cross_validation.html
- https://scikit-learn.org/stable/common_pitfalls.html
