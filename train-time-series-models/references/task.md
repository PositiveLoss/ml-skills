# Task reference

MAPE is unstable or undefined near zero; aggregated errors can hide important entities/horizons. Sliding windows can share targets/features across folds even when timestamp ranges appear separated. Backtesting retraining at each origin is different from testing one fixed model. Record observation versus event timestamps for delayed feeds.

Primary sources:
- https://scikit-learn.org/stable/modules/cross_validation.html
- https://www.statsmodels.org/stable/tsa.html
