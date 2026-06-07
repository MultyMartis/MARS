"""EAR Runtime connector contract — validation constants and helpers only.

Single source of truth for connector-side config expectations.
Standard library only. No runtime execution. No network code.
"""

from __future__ import annotations

from typing import Any

REQUIRED_CONFIG_FIELDS: tuple[str, ...] = (
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

SUPPORTED_CONNECTOR: str = "sftp_readonly"
SUPPORTED_MODE: str = "mode_2"
SUPPORTED_TRACK: str = "connected"
SUPPORTED_SNAPSHOT_TARGET: str = "level_1"

ENUM_FIELD_EXPECTATIONS: dict[str, str] = {
    "connector": SUPPORTED_CONNECTOR,
    "mode": SUPPORTED_MODE,
    "track": SUPPORTED_TRACK,
    "snapshot_target": SUPPORTED_SNAPSHOT_TARGET,
}

PATH_FIELDS: tuple[str, ...] = (
    "remote_root",
    "output_root",
    "allowed_paths",
    "excluded_paths",
)

CONNECTOR_CLASS: str = "sftp_readonly"
CONNECTOR_VERSION: str = "0.1.0-skeleton"
EXECUTION_MODE_PLAN: str = "PLAN_ONLY"
NETWORK_ACCESS: str = "DISABLED"
IMPLEMENTATION_STATE: str = "SKELETON"


def find_missing_required_fields(data: dict[str, Any]) -> list[str]:
    """Return sorted names of required config fields absent from *data*."""
    return sorted(field for field in REQUIRED_CONFIG_FIELDS if field not in data)


def find_enum_violations(data: dict[str, Any]) -> list[str]:
    """Return human-readable messages for enum fields that violate contract."""
    violations: list[str] = []
    for field, expected in ENUM_FIELD_EXPECTATIONS.items():
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, str):
            violations.append(f"{field} must be a string")
            continue
        if value != expected:
            violations.append(
                f"{field} must equal {expected!r} (got {value!r})"
            )
    return violations
