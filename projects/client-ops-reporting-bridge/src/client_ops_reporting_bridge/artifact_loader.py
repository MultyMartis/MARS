"""Read-only loading of fixture / run artifact folders."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Optional

from .constants import OPTIONAL_ARTIFACTS, REQUIRED_ARTIFACTS
from .models import FixtureMeta, ParsedArtifacts


def sha256_file(path: Path) -> str:
    """Return hex SHA-256 of file bytes."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_fixture_meta(fixture_dir: Path) -> FixtureMeta:
    """Load optional ``fixture-meta.json`` (offline pins only)."""
    meta_path = fixture_dir / "fixture-meta.json"
    if not meta_path.is_file():
        return FixtureMeta()
    raw = meta_path.read_text(encoding="utf-8")
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("fixture-meta.json must be a JSON object")
    return FixtureMeta.from_dict(data)


def load_artifacts(run_dir: Path) -> ParsedArtifacts:
    """Load required and optional artifacts from a local directory.

    Source files are opened read-only. Content is never written back.
    Each JSON document is parsed independently.
    """
    run_dir = run_dir.resolve()
    result = ParsedArtifacts()

    for name in REQUIRED_ARTIFACTS:
        path = run_dir / name
        if not path.is_file():
            result.missing.append(name)
            continue
        result.raw_hashes[name] = sha256_file(path)
        try:
            text = path.read_text(encoding="utf-8")
            data = json.loads(text)
        except (OSError, UnicodeError, json.JSONDecodeError):
            result.malformed.append(name)
            continue
        if not isinstance(data, dict):
            result.malformed.append(name)
            continue
        if name == "monitor-classification.json":
            result.monitor_classification = data
        elif name == "changed-summary.json":
            result.changed_summary = data
        elif name == "run-summary.json":
            result.run_summary = data

    for name in OPTIONAL_ARTIFACTS:
        path = run_dir / name
        if path.is_file():
            result.raw_hashes[name] = sha256_file(path)
            try:
                result.run_log = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                # Optional debug evidence only — malformed log does not
                # override machine-readable authorities; record as absent.
                result.run_log = None

    return result


def snapshot_source_hashes(run_dir: Path) -> dict[str, str]:
    """Hash required (+ optional present) source files for immutability tests."""
    run_dir = run_dir.resolve()
    hashes: dict[str, str] = {}
    for name in list(REQUIRED_ARTIFACTS) + list(OPTIONAL_ARTIFACTS):
        path = run_dir / name
        if path.is_file():
            hashes[name] = sha256_file(path)
    return hashes


def read_json_object(path: Path) -> dict[str, Any]:
    """Read a UTF-8 JSON object from disk."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path.name} must be a JSON object")
    return data


def extract_aliased(
    document: dict[str, Any],
    aliases: dict[str, Any] | dict[str, tuple[str, ...]],
    field_name: str,
) -> Any:
    """Return first present alias value for ``field_name``, else None."""
    names = aliases[field_name]
    for name in names:
        if name in document:
            return document[name]
    return None


def has_aliased_key(
    document: dict[str, Any],
    aliases: dict[str, Any] | dict[str, tuple[str, ...]],
    field_name: str,
) -> bool:
    """True when any approved alias key is present."""
    names = aliases[field_name]
    return any(name in document for name in names)
