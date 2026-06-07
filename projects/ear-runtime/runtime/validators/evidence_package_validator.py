"""EAR Runtime R2 evidence package validator — structural R2 boundary checks only.

Implements R2-V-* from R2.4-EVIDENCE-VALIDATION-BOUNDARY-v1.md.
Standard library only. No network. No filesystem. No R5 checks.
"""

from __future__ import annotations

import re
from typing import Any

from shared.evidence_package_models import (
    ARTIFACT_STATUS_MISSING,
    ARTIFACT_STATUS_PARTIAL,
    ARTIFACT_STATUS_PRESENT,
    ARTIFACT_STATUS_SKIPPED,
    ARTIFACT_STATUS_UNKNOWN,
    ARTIFACT_TYPE_CONNECTOR_OUTPUT,
    ARTIFACT_TYPE_IDENTITY,
    ARTIFACT_TYPE_LOG,
    ARTIFACT_TYPE_MANIFEST,
    ARTIFACT_TYPE_METADATA,
    ARTIFACT_TYPE_OTHER,
    ARTIFACT_TYPE_SAFE_UNKNOWN,
    CONNECTOR_STATUS_FAILED,
    CONNECTOR_STATUS_PARTIAL,
    CONNECTOR_STATUS_SUCCESS,
    EvidencePackage,
)

_ALLOWED_CONNECTOR_STATUSES: frozenset[str] = frozenset(
    {
        CONNECTOR_STATUS_SUCCESS,
        CONNECTOR_STATUS_PARTIAL,
        CONNECTOR_STATUS_FAILED,
    }
)

_ALLOWED_ARTIFACT_STATUSES: frozenset[str] = frozenset(
    {
        ARTIFACT_STATUS_PRESENT,
        ARTIFACT_STATUS_MISSING,
        ARTIFACT_STATUS_PARTIAL,
        ARTIFACT_STATUS_SKIPPED,
        ARTIFACT_STATUS_UNKNOWN,
    }
)

_ALLOWED_ARTIFACT_TYPES: frozenset[str] = frozenset(
    {
        ARTIFACT_TYPE_IDENTITY,
        ARTIFACT_TYPE_MANIFEST,
        ARTIFACT_TYPE_CONNECTOR_OUTPUT,
        ARTIFACT_TYPE_LOG,
        ARTIFACT_TYPE_METADATA,
        ARTIFACT_TYPE_SAFE_UNKNOWN,
        ARTIFACT_TYPE_OTHER,
    }
)

_CONNECTOR_ENUM_ON_ARTIFACT: frozenset[str] = frozenset(
    {
        CONNECTOR_STATUS_SUCCESS,
        CONNECTOR_STATUS_PARTIAL,
        CONNECTOR_STATUS_FAILED,
    }
)

_OPENCART_SECTION_PREFIXES: tuple[str, ...] = (
    "file-manifest/",
    "theme-info/",
    "extension-inventory/",
    "ocmod-inventory/",
    "database-metadata/",
    "seo-structure/",
)

_FORBIDDEN_SERIALIZED_KEYS: frozenset[str] = frozenset(
    {
        "evidence_id",
        "site_id",
        "snapshot_id",
        "package_quality_level",
        "quality_level",
        "snapshot_contract",
    }
)

_CREDENTIAL_HEURISTIC = re.compile(
    r"(password|passwd|\bpwd\b|secret|api[_-]?key|private[_-]?key|Bearer\s+\S+)",
    re.IGNORECASE,
)


def validate_contract_evidence_package(package: EvidencePackage) -> dict[str, Any]:
    """Validate R2.1 EvidencePackage structure. Returns {valid, errors}."""
    errors: list[str] = []

    identity = package.identity
    for field_name in ("acquisition_id", "site_ref", "connector_class"):
        value = getattr(identity, field_name, "")
        if not isinstance(value, str) or not value.strip():
            errors.append(f"identity.{field_name} must be a non-empty string")

    provenance = package.provenance
    for field_name in ("channel", "started_at", "operator_approval_ref"):
        value = getattr(provenance, field_name, "")
        if not isinstance(value, str) or not value.strip():
            errors.append(f"provenance.{field_name} must be a non-empty string")

    terminal = package.status.connector_status in _ALLOWED_CONNECTOR_STATUSES
    completed_at = provenance.completed_at
    if terminal:
        if not isinstance(completed_at, str) or not completed_at.strip():
            errors.append(
                "provenance.completed_at must be non-empty when connector run is terminal"
            )

    connector_status = package.status.connector_status
    if connector_status not in _ALLOWED_CONNECTOR_STATUSES:
        errors.append(
            "status.connector_status must be one of: success, partial, failed"
        )

    index = package.artifact_index
    artifacts = index.artifacts
    if index.artifact_count != len(artifacts):
        errors.append(
            f"artifact_index.artifact_count ({index.artifact_count}) "
            f"must equal len(artifacts) ({len(artifacts)})"
        )

    refs_seen: set[str] = set()
    has_manifest = False
    for idx, artifact in enumerate(artifacts):
        prefix = f"artifact_index.artifacts[{idx}]"
        for field_name in ("artifact_type", "artifact_ref", "status"):
            value = getattr(artifact, field_name, "")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}.{field_name} must be a non-empty string")

        if artifact.artifact_ref in refs_seen:
            errors.append(
                f"artifact_ref must be unique within index (duplicate: {artifact.artifact_ref!r})"
            )
        refs_seen.add(artifact.artifact_ref)

        if artifact.artifact_type not in _ALLOWED_ARTIFACT_TYPES:
            errors.append(
                f"{prefix}.artifact_type {artifact.artifact_type!r} is not a canonical type"
            )

        if artifact.artifact_type == ARTIFACT_TYPE_MANIFEST:
            has_manifest = True

        if artifact.status not in _ALLOWED_ARTIFACT_STATUSES:
            errors.append(
                f"{prefix}.status {artifact.status!r} is not an allowed artifact status"
            )

        if artifact.status in _CONNECTOR_ENUM_ON_ARTIFACT:
            errors.append(
                f"{prefix}.status must not reuse connector enum value {artifact.status!r}"
            )

        for section_prefix in _OPENCART_SECTION_PREFIXES:
            if artifact.artifact_ref.startswith(section_prefix):
                errors.append(
                    f"{prefix}.artifact_ref must not use OpenCart section path prefix "
                    f"{section_prefix!r}"
                )

    if not has_manifest:
        has_safe_unknown = any(
            a.artifact_type == ARTIFACT_TYPE_SAFE_UNKNOWN for a in artifacts
        )
        if not has_safe_unknown:
            errors.append(
                "artifact_index must include at least one manifest-class entry "
                "or safe-unknown placeholder"
            )

    if connector_status == CONNECTOR_STATUS_FAILED and not package.errors:
        errors.append(
            "errors must be non-empty when connector_status is failed"
        )

    serialized = package.to_dict()
    _scan_forbidden_keys(serialized, "", errors)
    _scan_credential_patterns(serialized, "", errors)

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


def _scan_credential_patterns(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, str) and _CREDENTIAL_HEURISTIC.search(value):
        errors.append(f"possible credential pattern in serialized field: {path or 'root'}")
    elif isinstance(value, dict):
        for key, nested in value.items():
            _scan_credential_patterns(nested, f"{path}.{key}" if path else key, errors)
    elif isinstance(value, list):
        for idx, item in enumerate(value):
            _scan_credential_patterns(item, f"{path}[{idx}]", errors)
