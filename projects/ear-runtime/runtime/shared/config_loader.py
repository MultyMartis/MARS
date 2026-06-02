"""EAR Runtime config loader — JSON parse and validation only.

Standard library only. No credential resolution, no network, no SFTP.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

REQUIRED_FIELDS: tuple[str, ...] = (
    "site_id",
    "pilot_id",
    "track",
    "mode",
    "connector",
    "environment",
    "snapshot_target",
    "credential_ref",
    "remote_root",
    "allowed_paths",
    "excluded_paths",
    "output_root",
    "dry_run",
)

FORBIDDEN_ENUMS: dict[str, str] = {
    "connector": "sftp_readonly",
    "mode": "mode_2",
    "track": "connected",
    "snapshot_target": "level_1",
}

PATH_FIELDS: tuple[str, ...] = (
    "remote_root",
    "output_root",
    "allowed_paths",
    "excluded_paths",
)

PASSWORD_LIKE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"password", re.IGNORECASE),
    re.compile(r"passwd", re.IGNORECASE),
    re.compile(r"\bpwd\b", re.IGNORECASE),
    re.compile(r"secret", re.IGNORECASE),
    re.compile(r"api[_-]?key", re.IGNORECASE),
    re.compile(r"private[_-]?key", re.IGNORECASE),
    re.compile(r"BEGIN\s+(RSA\s+)?PRIVATE\s+KEY", re.IGNORECASE),
    re.compile(r"Bearer\s+\S+", re.IGNORECASE),
)


class ConfigValidationError(ValueError):
    """Raised when config JSON fails validation."""


def load_config(config_path: str | Path) -> dict[str, Any]:
    """Load and validate a runtime config JSON file.

    Returns a structured dict on success. Raises ConfigValidationError on failure.
    Does not resolve credentials, access remotes, or create outputs.
    """
    path = Path(config_path)

    if path.is_symlink():
        raise ConfigValidationError(f"Symlink config paths are not allowed: {path}")

    resolved = path.resolve()
    if not resolved.is_file():
        raise ConfigValidationError(f"Config file not found: {path}")

    try:
        raw = resolved.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigValidationError(f"Cannot read config file: {path}") from exc

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ConfigValidationError(f"Invalid JSON in config file: {exc}") from exc

    if not isinstance(data, dict):
        raise ConfigValidationError("Config root must be a JSON object")

    _validate_required_fields(data)
    _validate_enums(data)
    _validate_dry_run(data)
    _validate_non_empty_strings(data, ("remote_root", "output_root"))
    _validate_credential_ref(data["credential_ref"])
    _validate_path_fields(data)

    return dict(data)


def _validate_required_fields(data: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        raise ConfigValidationError(
            f"Missing required field(s): {', '.join(sorted(missing))}"
        )


def _validate_enums(data: dict[str, Any]) -> None:
    for field, expected in FORBIDDEN_ENUMS.items():
        value = data[field]
        if not isinstance(value, str):
            raise ConfigValidationError(f"{field} must be a string")
        if value != expected:
            raise ConfigValidationError(
                f"{field} must equal {expected!r} (got {value!r})"
            )


def _validate_dry_run(data: dict[str, Any]) -> None:
    if data["dry_run"] is not True:
        raise ConfigValidationError("dry_run must be true")


def _validate_non_empty_strings(data: dict[str, Any], fields: tuple[str, ...]) -> None:
    for field in fields:
        value = data[field]
        if not isinstance(value, str):
            raise ConfigValidationError(f"{field} must be a string")
        if not value.strip():
            raise ConfigValidationError(f"{field} must not be empty")


def _validate_credential_ref(value: Any) -> None:
    if not isinstance(value, str):
        raise ConfigValidationError("credential_ref must be a string")
    if not value.strip():
        raise ConfigValidationError("credential_ref must not be empty")
    for pattern in PASSWORD_LIKE_PATTERNS:
        if pattern.search(value):
            raise ConfigValidationError(
                "credential_ref contains password-like content and is rejected"
            )


def _validate_path_fields(data: dict[str, Any]) -> None:
    for field in ("remote_root", "output_root"):
        _reject_path_traversal(data[field], field)

    for field in ("allowed_paths", "excluded_paths"):
        paths = data[field]
        if not isinstance(paths, list):
            raise ConfigValidationError(f"{field} must be a list")
        for index, item in enumerate(paths):
            if not isinstance(item, str):
                raise ConfigValidationError(
                    f"{field}[{index}] must be a string"
                )
            _reject_path_traversal(item, f"{field}[{index}]")


def _reject_path_traversal(value: str, field_name: str) -> None:
    if ".." in value.replace("\\", "/").split("/"):
        raise ConfigValidationError(
            f"{field_name} must not contain path traversal (..)"
        )
