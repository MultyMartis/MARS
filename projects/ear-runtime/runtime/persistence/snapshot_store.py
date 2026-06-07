"""EAR Runtime snapshot store — mock Store persist only.

Standard library only. No network. No publish. No overwrite.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from builders.persistence_layout_builder import build_persistence_layout
from shared.snapshot_models import SnapshotPackage
from validators.persistence_validator import validate_persistence_layout


class PersistenceError(Exception):
    """Raised when mock persist cannot proceed (fail closed)."""


def persist_mock_snapshot(
    snapshot_package: SnapshotPackage,
    config: dict[str, Any],
) -> dict[str, Any]:
    """Persist a mock snapshot package to the EAR Store layout.

    Creates directories under output_root only. Writes three JSON files.
    Fails closed if validation fails or snapshot_id already exists.
    """
    layout = build_persistence_layout(snapshot_package, config)
    validation = validate_persistence_layout(layout, config)
    if not validation["valid"]:
        raise PersistenceError(
            f"Persistence validation failed: {'; '.join(validation['errors'])}"
        )

    snapshot_dir = Path(layout["paths"]["snapshot_dir"])
    output_root = Path(config["output_root"]).resolve()

    try:
        snapshot_dir.resolve().relative_to(output_root)
    except ValueError as exc:
        raise PersistenceError(
            "snapshot_dir must resolve under configured output_root"
        ) from exc

    if snapshot_dir.exists():
        raise PersistenceError(
            f"snapshot_id already exists (immutable store): {snapshot_package.snapshot_id}"
        )

    snapshot_dir.mkdir(parents=True, exist_ok=False)

    written: dict[str, str] = {}
    file_map = (
        ("metadata.json", layout["metadata"]),
        ("safe-unknown.json", layout["safe_unknown"]),
        ("acquisition-log.json", layout["acquisition_log"]),
    )
    for filename, payload in file_map:
        target = snapshot_dir / filename
        if target.exists():
            raise PersistenceError(f"refusing to overwrite existing file: {target}")
        target.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        written[filename] = str(target.resolve())

    return {
        "snapshot_id": layout["snapshot_id"],
        "acquisition_id": layout["acquisition_id"],
        "output_root": str(output_root),
        "store_state": layout["store_state"],
        "paths": dict(layout["paths"]),
        "written_files": written,
        "validation": validation,
    }
