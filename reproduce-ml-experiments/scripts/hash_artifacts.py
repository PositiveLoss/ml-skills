"""Create or verify SHA-256 integrity manifests without loading model code."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def contained(root, relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("manifest paths must stay inside the root")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("resolved path escapes the root")
    return resolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("create", "verify"):
        sub = subparsers.add_parser(name)
        sub.add_argument("--root", type=Path, required=True)
        sub.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    root, manifest = args.root.resolve(), args.manifest.resolve()
    if not root.is_dir():
        parser.error("root must be a directory")
    try:
        if args.command == "create":
            if manifest.exists():
                raise ValueError("manifest exists; choose a new path")
            files = []
            for path in sorted(root.rglob("*")):
                if path.is_symlink():
                    raise ValueError("symlinks are not accepted for integrity manifests")
                if path.is_file() and path.resolve() != manifest:
                    files.append({"path": path.relative_to(root).as_posix(), "sha256": digest(path), "bytes": path.stat().st_size})
            if not files:
                raise ValueError("artifact root is empty")
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(json.dumps({"algorithm": "sha256", "files": files}, indent=2), encoding="utf-8")
            result = {"ok": True, "files": len(files), "manifest": str(manifest)}
        else:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("algorithm") != "sha256" or not isinstance(data.get("files"), list) or not data["files"]:
                raise ValueError("invalid manifest")
            failures, seen = [], set()
            for item in data["files"]:
                if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not item["path"]:
                    raise ValueError("invalid file entry")
                relative = item["path"]
                if relative in seen:
                    raise ValueError("duplicate manifest path")
                seen.add(relative)
                path = contained(root, relative)
                if not path.is_file():
                    failures.append({"path": relative, "kind": "missing"})
                elif digest(path) != item.get("sha256") or path.stat().st_size != item.get("bytes"):
                    failures.append({"path": relative, "kind": "modified"})
            result = {"ok": not failures, "files": len(seen), "failures": failures,
                      "scope": "Integrity of listed files only; not authenticity or detection of extra unlisted files."}
    except (OSError, ValueError, TypeError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
