"""Compare finite numeric JSON tensors by shape and elementwise tolerance."""
import argparse
import json
import math
from pathlib import Path


def tensor(value):
    if type(value) in (int, float):
        if not math.isfinite(value):
            raise ValueError("nonfinite tensor value")
        return (), [value]
    if not isinstance(value, list) or not value:
        raise ValueError("tensor must be numeric or a nonempty rectangular array")
    converted = [tensor(item) for item in value]
    shape = converted[0][0]
    if any(other != shape for other, _ in converted):
        raise ValueError("ragged tensor")
    return (len(value), *shape), [number for _, numbers in converted for number in numbers]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--atol", type=float, default=1e-6)
    parser.add_argument("--rtol", type=float, default=1e-5)
    args = parser.parse_args()
    if any(not math.isfinite(v) or v < 0 for v in (args.atol, args.rtol)):
        parser.error("tolerances must be finite and nonnegative")
    try:
        shape_a, a = tensor(json.loads(args.reference.read_text(encoding="utf-8")))
        shape_b, b = tensor(json.loads(args.candidate.read_text(encoding="utf-8")))
        if shape_a != shape_b:
            raise ValueError(f"shape mismatch: {shape_a} versus {shape_b}")
        errors = [abs(x - y) for x, y in zip(a, b)]
        if not all(math.isfinite(x) for x in errors):
            raise ValueError("overflow during comparison")
        failed = sum(error > args.atol + args.rtol * abs(x) for x, error in zip(a, errors))
        result = {"ok": failed == 0, "shape": shape_a, "elements": len(a), "failed_elements": failed,
                  "max_absolute_error": max(errors), "atol": args.atol, "rtol": args.rtol,
                  "scope": "Numerical fixture parity only; not graph validity or model quality."}
    except (ValueError, OSError, OverflowError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
