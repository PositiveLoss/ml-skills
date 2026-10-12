"""Train an offline sklearn toy baseline with train-only preprocessing."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output exists; choose a new path")
    import numpy as np
    import sklearn
    from sklearn.datasets import load_breast_cancer
    from sklearn.dummy import DummyClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, balanced_accuracy_score, log_loss
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    data = load_breast_cancer()
    X, y = data.data, data.target
    indices = np.arange(len(y))
    train, rest = train_test_split(indices, test_size=.4, random_state=args.seed, stratify=y)
    val, test = train_test_split(rest, test_size=.5, random_state=args.seed + 1, stratify=y[rest])
    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=args.seed))
    dummy = DummyClassifier(strategy="prior").fit(X[train], y[train])
    model.fit(X[train], y[train])
    assert np.allclose(model[0].mean_, X[train].mean(axis=0))
    assert not (set(train) & set(val) or set(train) & set(test) or set(val) & set(test))
    def score(estimator, ids):
        probability = estimator.predict_proba(X[ids])
        return {"n": len(ids), "accuracy": accuracy_score(y[ids], estimator.predict(X[ids])),
                "balanced_accuracy": balanced_accuracy_score(y[ids], estimator.predict(X[ids])),
                "log_loss": log_loss(y[ids], probability, labels=[0, 1])}
    report = {"dataset": "sklearn_breast_cancer_toy", "scope": "Offline toy fixture, not a clinical model or medical evaluation.",
              "seed": args.seed, "numpy": np.__version__, "sklearn": sklearn.__version__,
              "data_sha256": hashlib.sha256(X.tobytes() + y.tobytes()).hexdigest(),
              "splits": {name: ids.tolist() for name, ids in [("train", train), ("validation", val), ("test", test)]},
              "preprocessing_train_only": True, "hyperparameter_selection": "Fixed configuration; no search.",
              "validation": {"baseline": score(dummy, val), "candidate": score(model, val)},
              "test": {"baseline": score(dummy, test), "candidate": score(model, test)}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False), encoding="utf-8")
    print(str(args.output))


if __name__ == "__main__":
    main()
