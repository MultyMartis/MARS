"""EAR Runtime persistence layout builder — SnapshotPackage to layout dict only.

Standard library only. No filesystem access. No network. No writes.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from shared.persistence_contract import (
    DEFAULT_CONSUMER_TARGET,
    DEFAULT_CREATED_FROM,
    DEFAULT_PACKAGE_QUALITY_LEVEL_MOCK,
    MOCK_UNPOPULATED_SECTIONS,
    PARENT_CONTRACT,
    SNAPSHOT_CONTRACT,
    STORE_STATE_UNPUBLISHED,
    build_mock_acquisition_id,
)
from shared.snapshot_models import SnapshotPackage


def build_persistence_layout(
    snapshot: SnapshotPackage,
    config: dict[str, Any],
) -> dict[str, Any]:
    """Translate SnapshotPackage + config into a persistence layout data structure."""
    output_root = Path(config["output_root"])
    acquisition_id = build_mock_acquisition_id(snapshot.site_id, snapshot.source)
    snapshot_dir = (
        output_root / acquisition_id / "snapshots" / snapshot.snapshot_id
    )
    created_at = datetime.now(timezone.utc).isoformat()
    bulk_root = str(snapshot_dir.resolve())

    metadata: dict[str, Any] = {
        "snapshot_id": snapshot.snapshot_id,
        "snapshot_contract": SNAPSHOT_CONTRACT,
        "parent_contract": PARENT_CONTRACT,
        "site_id": snapshot.site_id,
        "created_at": created_at,
        "ear_mode": config.get("mode"),
        "operator_approval_ref": "mock_persist",
        "package_quality_level": DEFAULT_PACKAGE_QUALITY_LEVEL_MOCK,
        "quality_level_runtime": snapshot.quality_level,
        "consumer_target": DEFAULT_CONSUMER_TARGET,
        "bulk_root": bulk_root,
        "store_state": STORE_STATE_UNPUBLISHED,
        "publish_state": STORE_STATE_UNPUBLISHED,
        "entry_count": snapshot.entry_count,
        "excluded_count": snapshot.excluded_count,
        "pilot_id": config.get("pilot_id"),
        "environment_class": config.get("environment"),
        "created_from": snapshot.created_from or DEFAULT_CREATED_FROM,
        "source_runtime": snapshot.source,
        "connector_runtime": snapshot.connector,
    }

    safe_unknown_entries: list[dict[str, str]] = []
    for topic in snapshot.safe_unknown:
        safe_unknown_entries.append(
            {
                "topic": topic,
                "reason": "runtime_flat_safe_unknown",
                "impact": "section_honesty_deferred",
                "unblock": "R3_live_section_builders",
            }
        )
    for section in MOCK_UNPOPULATED_SECTIONS:
        safe_unknown_entries.append(
            {
                "topic": section,
                "reason": "mock_pipeline_not_populated",
                "impact": "package_quality_level_0",
                "unblock": "R3_live_acquisition_or_section_builder",
            }
        )

    acquisition_log: dict[str, Any] = {
        "acquisition_id": acquisition_id,
        "snapshot_id": snapshot.snapshot_id,
        "site_id": snapshot.site_id,
        "channel": snapshot.connector,
        "ear_mode": config.get("mode"),
        "pilot_id": config.get("pilot_id"),
        "environment": config.get("environment"),
        "store_state": STORE_STATE_UNPUBLISHED,
        "created_at": created_at,
        "tooling_note": list(snapshot.notes),
        "created_from": snapshot.created_from or DEFAULT_CREATED_FROM,
        "persist_mode": "mock_store_only",
    }

    return {
        "output_root": str(output_root),
        "acquisition_id": acquisition_id,
        "snapshot_id": snapshot.snapshot_id,
        "store_state": STORE_STATE_UNPUBLISHED,
        "metadata": metadata,
        "safe_unknown": safe_unknown_entries,
        "acquisition_log": acquisition_log,
        "paths": {
            "snapshot_dir": str(snapshot_dir),
            "metadata_json": str(snapshot_dir / "metadata.json"),
            "safe_unknown_json": str(snapshot_dir / "safe-unknown.json"),
            "acquisition_log_json": str(snapshot_dir / "acquisition-log.json"),
        },
    }
