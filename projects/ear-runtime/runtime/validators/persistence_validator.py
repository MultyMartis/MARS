"""EAR Runtime persistence validator — layout and config checks only.

Standard library only. No writes. No network.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from shared.persistence_contract import (
    find_store_state_violation,
    output_root_under_ear_bulk,
)


def validate_persistence_layout(
    layout: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    """Validate persistence layout and config before Store write."""
    errors: list[str] = []

    output_root_value = config.get("output_root")
    if not isinstance(output_root_value, str) or not output_root_value.strip():
        errors.append("output_root must exist in config as a non-empty string")
    else:
        output_root = Path(output_root_value)
        if not output_root_under_ear_bulk(output_root):
            errors.append(
                "output_root must resolve under chartered EAR bulk root "
                r"(C:\AI MARS STORAGE\ear\)"
            )

    acquisition_id = layout.get("acquisition_id")
    if not isinstance(acquisition_id, str) or not acquisition_id.strip():
        errors.append("acquisition_id must be a non-empty string")

    snapshot_id = layout.get("snapshot_id")
    if not isinstance(snapshot_id, str) or not snapshot_id.strip():
        errors.append("snapshot_id must be a non-empty string")

    store_state = layout.get("store_state")
    violation = find_store_state_violation(store_state)
    if violation:
        errors.append(violation)

    paths = layout.get("paths")
    if not isinstance(paths, dict):
        errors.append("paths must be a dict")
    else:
        for key in ("snapshot_dir", "metadata_json", "safe_unknown_json", "acquisition_log_json"):
            value = paths.get(key)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"paths.{key} must be a non-empty string")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }
