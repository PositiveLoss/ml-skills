"""Validate exact sample, group and content isolation in a JSONL split manifest."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re


def audit(path):
    issues = []
    ids, groups, hashes = {}, {}, {}
    counts = Counter()
    with path.open(encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
                if not isinstance(row, dict):
                    raise ValueError("record must be an object")
                for key in ("sample_id", "split", "group_id", "content_sha256"):
                    if not isinstance(row.get(key), str) or not row[key].strip():
                        raise ValueError(f"{key} must be a nonempty string")
                split = row["split"]
                if split not in ("train", "validation", "test"):
                    raise ValueError("split must be train, validation or test")
                if not re.fullmatch(r"[0-9a-fA-F]{64}", row["content_sha256"]):
                    raise ValueError("content_sha256 must be a 64-digit hexadecimal hash")
                counts[split] += 1
                sid = row["sample_id"]
                if sid in ids:
                    issues.append({"line": line_no, "kind": "duplicate_id", "sample_id": sid})
                ids[sid] = split
                for mapping, value, kind in (
                    (groups, row["group_id"], "group_overlap"),
                    (hashes, row["content_sha256"].lower(), "content_overlap"),
                ):
                    if value in mapping and mapping[value] != split:
                        issues.append({"line": line_no, "kind": kind, "sample_id": sid})
                    else:
                        mapping[value] = split
            except (ValueError, TypeError) as error:
                issues.append({"line": line_no, "kind": "invalid_record", "message": str(error)})
    if not counts:
        issues.append({"kind": "empty_manifest"})
    return {"ok": not issues, "split_counts": dict(counts), "issues": issues,
            "scope": "Exact manifest checks only; hashes must be supplied from trusted file hashing."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        result = audit(args.manifest)
    except OSError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
