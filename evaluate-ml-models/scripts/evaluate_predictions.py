"""Score fixed binary predictions; optionally bootstrap accuracy by independent groups."""
import argparse
from collections import defaultdict
import json
import math
from pathlib import Path
import random


def load_rows(path, grouped):
    rows, seen = [], set()
    with path.open(encoding="utf-8") as stream:
        for number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError("row must be an object")
                sid, y, p = row.get("sample_id"), row.get("y_true"), row.get("probability")
                if not isinstance(sid, str) or not sid.strip() or sid in seen:
                    raise ValueError("sample_id must be unique and nonempty")
                if type(y) is not int or y not in (0, 1):
                    raise ValueError("y_true must be integer 0 or 1")
                if type(p) not in (float, int) or not math.isfinite(p) or not 0 <= p <= 1:
                    raise ValueError("probability must be finite and in [0,1]")
                if grouped and (not isinstance(row.get("group_id"), str) or not row["group_id"].strip()):
                    raise ValueError("group_id required for grouped bootstrap")
                seen.add(sid)
                rows.append(row)
            except (ValueError, TypeError) as error:
                raise ValueError(f"line {number}: {error}") from error
    if not rows:
        raise ValueError("predictions must not be empty")
    return rows


def metrics(rows, threshold):
    tp = fp = tn = fn = 0
    brier = logloss = 0.0
    epsilon = 1e-15
    for row in rows:
        y, p = row["y_true"], row["probability"]
        pred = int(p >= threshold)
        tp += int(y == 1 and pred == 1)
        tn += int(y == 0 and pred == 0)
        fp += int(y == 0 and pred == 1)
        fn += int(y == 1 and pred == 0)
        brier += (p - y) ** 2
        clipped = min(1 - epsilon, max(epsilon, p))
        logloss -= y * math.log(clipped) + (1 - y) * math.log1p(-clipped)
    def ratio(a, b):
        return a / b if b else None
    recall, specificity = ratio(tp, tp + fn), ratio(tn, tn + fp)
    return {"n": len(rows), "tp": tp, "fp": fp, "tn": tn, "fn": fn,
            "accuracy": (tp + tn) / len(rows), "precision": ratio(tp, tp + fp),
            "recall": recall, "specificity": specificity, "f1": ratio(2 * tp, 2 * tp + fp + fn),
            "balanced_accuracy": (recall + specificity) / 2 if recall is not None and specificity is not None else None,
            "brier": brier / len(rows), "log_loss": logloss / len(rows)}


def quantile(values, q):
    values = sorted(values)
    position = (len(values) - 1) * q
    lo, hi = math.floor(position), math.ceil(position)
    return values[lo] + (position - lo) * (values[hi] - values[lo])


def bootstrap(rows, threshold, iterations, seed, grouped):
    units = defaultdict(list)
    for row in rows:
        units[row["group_id"] if grouped else row["sample_id"]].append(row)
    keys, rng, scores = sorted(units), random.Random(seed), []
    if len(keys) < 2:
        raise ValueError("bootstrap needs at least two resampling units")
    for _ in range(iterations):
        selected = [row for key in rng.choices(keys, k=len(keys)) for row in units[key]]
        scores.append(metrics(selected, threshold)["accuracy"])
    return {"metric": "accuracy", "confidence": 0.95, "method": "percentile_cluster" if grouped else "percentile_iid_rows",
            "low": quantile(scores, .025), "high": quantile(scores, .975),
            "iterations": iterations, "units": len(keys), "seed": seed,
            "warning": "Few independent units or dependence between units can invalidate interval interpretation."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("predictions", type=Path)
    parser.add_argument("--threshold", type=float, default=0.5)
    parser.add_argument("--bootstrap", type=int, default=0)
    parser.add_argument("--grouped", action="store_true")
    parser.add_argument("--seed", type=int, default=17)
    args = parser.parse_args()
    if not math.isfinite(args.threshold) or not 0 <= args.threshold <= 1:
        parser.error("threshold must be finite and in [0,1]")
    if args.bootstrap < 0 or args.bootstrap == 1:
        parser.error("bootstrap must be 0 or at least 2")
    if args.grouped and args.bootstrap == 0:
        parser.error("--grouped requires --bootstrap")
    try:
        rows = load_rows(args.predictions, args.grouped)
        result = {"threshold": args.threshold, "metrics": metrics(rows, args.threshold),
                  "interval": bootstrap(rows, args.threshold, args.bootstrap, args.seed, args.grouped) if args.bootstrap else None,
                  "selection": "Fixed threshold; no tuning or calibration performed."}
    except (ValueError, OSError, OverflowError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
