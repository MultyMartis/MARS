"""EAR Runtime R3 snapshot package validator — structural R3 boundary checks only.

Implements R3 candidate package checks per R3.1–R3.5. No R5 quality validation.
No publish validation. Standard library only. No network. No filesystem.
"""

from __future__ import annotations

from typing import Any

from shared.evidence_package_models import EvidencePackage
from shared.handoff_contract import (
    CANDIDATE_PACKAGE_QUALITY_LEVEL,
    SNAPSHOT_CONTRACT,
    check_identity_continuity,
)
from shared.snapshot_package_models import (
    PARENT_CONTRACT,
    SnapshotPackage,
)

_REQUIRED_SECTION_ATTRS: tuple[str, ...] = (
    "metadata",
    "environment",
    "file_manifest",
    "theme_info",
    "extension_inventory",
    "ocmod_inventory",
    "database_metadata",
    "seo_structure",
    "safe_unknown",
    "acquisition_log",
)

_FORBIDDEN_SERIALIZED_KEYS: frozenset[str] = frozenset(
    {
        "evidence_id",
        "site_ref",
        "published_at",
        "published_by",
        "quality_level",
    }
)


def validate_candidate_snapshot_package(
    snapshot: SnapshotPackage,
    evidence: EvidencePackage | None = None,
) -> dict[str, Any]:
    """Validate R3 candidate SnapshotPackage structure. Returns {valid, errors}."""
    errors: list[str] = []

    identity = snapshot.identity
    for field_name in ("snapshot_id", "acquisition_id", "site_id", "snapshot_contract"):
        value = getattr(identity, field_name, "")
        if not isinstance(value, str) or not value.strip():
            errors.append(f"identity.{field_name} must be a non-empty string")

    if identity.snapshot_contract != SNAPSHOT_CONTRACT:
        errors.append(
            f"identity.snapshot_contract must be {SNAPSHOT_CONTRACT!r}"
        )

    if evidence is not None:
        errors.extend(check_identity_continuity(evidence.identity, identity))

    metadata = snapshot.metadata
    if metadata.parent_contract != PARENT_CONTRACT:
        errors.append(f"metadata.parent_contract must be {PARENT_CONTRACT!r}")

    if metadata.package_quality_level != CANDIDATE_PACKAGE_QUALITY_LEVEL:
        errors.append(
            f"metadata.package_quality_level must be {CANDIDATE_PACKAGE_QUALITY_LEVEL} "
            "at R3 candidate boundary"
        )

    for field_name in ("created_at", "ear_mode", "operator_approval"):
        value = getattr(metadata, field_name, "")
        if field_name == "ear_mode" and (not isinstance(value, str)):
            errors.append("metadata.ear_mode must be a string")
        elif field_name != "ear_mode":
            if not isinstance(value, str) or not value.strip():
                errors.append(f"metadata.{field_name} must be a non-empty string")

    environment = snapshot.environment
    if not isinstance(environment.environment_class, str) or not environment.environment_class.strip():
        errors.append("environment.environment_class must be a non-empty string")

    for section_name in _REQUIRED_SECTION_ATTRS:
        if getattr(snapshot, section_name, None) is None:
            errors.append(f"required section missing: {section_name}")

    safe_entries = snapshot.safe_unknown.entries
    if not safe_entries:
        errors.append("safe_unknown.entries must be non-empty on candidate package")

    for idx, entry in enumerate(safe_entries):
        prefix = f"safe_unknown.entries[{idx}]"
        for field_name in ("topic", "reason", "impact"):
            value = getattr(entry, field_name, "")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}.{field_name} must be a non-empty string")

    acquisition_log = snapshot.acquisition_log
    for field_name in ("channel", "connector_class", "started_at", "completed_at"):
        value = getattr(acquisition_log, field_name, "")
        if not isinstance(value, str) or not value.strip():
            errors.append(f"acquisition_log.{field_name} must be a non-empty string")

    serialized = snapshot.to_dict()
    _scan_forbidden_keys(serialized, "", errors)

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }


def _scan_forbidden_keys(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, nested in value.items():
            key_path = f"{path}.{key}" if path else key
            if key in _FORBIDDEN_SERIALIZED_KEYS:
                errors.append(f"forbidden field in serialized package: {key_path}")
            _scan_forbidden_keys(nested, key_path, errors)
