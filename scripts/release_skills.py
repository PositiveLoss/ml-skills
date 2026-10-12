#!/usr/bin/env python3
"""Validate standalone skills and package their resources into a ZIP."""

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_DEFLATED, ZipFile

import yaml

EXCLUDED_DIRECTORIES = {"__pycache__", "node_modules", "venv", "env", "build", "dist"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def included(path):
    return not (
        any(part.startswith(".") or part in EXCLUDED_DIRECTORIES for part in path.parts)
        or path.suffix in EXCLUDED_SUFFIXES
    )


def validate_skill(root, skill, files):
    path = root / skill / "SKILL.md"
    source = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", source, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict) or data.get("name") != skill:
        raise ValueError(f"{path}: name must match the skill directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill) or len(skill) > 64:
        raise ValueError(f"{path}: invalid skill name")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        raise ValueError(f"{path}: description must contain 1–1024 characters")
    if not source[match.end():].strip():
        raise ValueError(f"{path}: empty instructions")
    metadata = Path(skill) / "agents" / "openai.yaml"
    if metadata not in files:
        raise ValueError(f"{metadata}: missing agent metadata")
    agent = yaml.safe_load((root / metadata).read_text(encoding="utf-8"))
    interface = agent.get("interface") if isinstance(agent, dict) else None
    if not isinstance(interface, dict):
        raise ValueError(f"{metadata}: missing interface mapping")
    for field in ("display_name", "short_description", "default_prompt"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{metadata}: missing {field}")
    if not 25 <= len(interface["short_description"]) <= 64:
        raise ValueError(f"{metadata}: short_description must be 25–64 characters")
    if f"${skill}" not in interface["default_prompt"]:
        raise ValueError(f"{metadata}: default_prompt must mention ${skill}")


def package(root, output):
    root = root.resolve()
    output = output.resolve()
    skills = sorted(
        path.name for path in root.iterdir()
        if included(Path(path.name)) and path.is_dir() and (path / "SKILL.md").is_file()
    )
    if not skills:
        raise ValueError("No skill directories found")
    files = {Path("README.md")}
    for skill in skills:
        if (root / skill).is_symlink():
            raise ValueError(f"{skill}: symlinked skills are not supported")
        for path in (root / skill).rglob("*"):
            relative = path.relative_to(root)
            if not included(relative):
                continue
            if path.is_symlink():
                raise ValueError(f"{relative}: symlinks are not supported")
            if path.is_file():
                files.add(relative)
    for relative in files:
        path = root / relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"{relative}: expected a regular file")
        if path == output:
            raise ValueError("Output archive must be outside the packaged resources")
    for skill in skills:
        validate_skill(root, skill, files)
    for relative in sorted(files):
        if relative.suffix != ".md":
            continue
        source = (root / relative).read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", source):
            link = urlsplit(target.strip("<>"))
            if link.scheme or link.netloc or not link.path:
                continue
            resolved = (root / relative.parent / unquote(link.path)).resolve()
            try:
                resource = resolved.relative_to(root)
            except ValueError as exc:
                raise ValueError(f"{relative}: link escapes package: {target}") from exc
            if resource not in files:
                raise ValueError(f"{relative}: link missing from package: {target}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED) as archive:
        for relative in sorted(files):
            archive.write(root / relative, arcname=relative.as_posix())
    print(f"Validated {len(skills)} skills; packaged {len(files)} files in {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("dist/machine-learning-skills.zip"))
    args = parser.parse_args()
    try:
        package(Path(__file__).resolve().parents[1], args.output)
    except (ValueError, OSError, yaml.YAMLError) as exc:
        parser.exit(1, f"Skill packaging failed: {exc}\n")


if __name__ == "__main__":
    main()
