"""EAR Runtime snapshot validator — structural checks on SnapshotPackage only.

Standard library only. No runtime execution. No remote access.
"""

from __future__ import annotations

from typing import Any

from shared.snapshot_models import SnapshotPackage


def validate_snapshot_package(snapshot: SnapshotPackage) -> dict[str, Any]:
    """Validate a SnapshotPackage object. Returns structured valid/errors result."""
    errors: list[str] = []

    if not isinstance(snapshot.snapshot_id, str) or not snapshot.snapshot_id.strip():
        errors.append("snapshot_id must be a non-empty string")

    if not isinstance(snapshot.site_id, str) or not snapshot.site_id.strip():
        errors.append("site_id must be a non-empty string")

    if not isinstance(snapshot.source, str) or not snapshot.source.strip():
        errors.append("source must be a non-empty string")

    if not isinstance(snapshot.connector, str) or not snapshot.connector.strip():
        errors.append("connector must be a non-empty string")

    if not isinstance(snapshot.quality_level, str) or not snapshot.quality_level.strip():
        errors.append("quality_level must be a non-empty string")

    if snapshot.entry_count < 0:
        errors.append("entry_count must be >= 0")

    if snapshot.excluded_count < 0:
        errors.append("excluded_count must be >= 0")

    if snapshot.safe_unknown is None:
        errors.append("safe_unknown list must exist")

    if snapshot.notes is None:
        errors.append("notes list must exist")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }
