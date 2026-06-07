"""EAR Runtime evidence validator — structural checks on EvidencePackage only.

Standard library only. No runtime execution. No remote access.
"""

from __future__ import annotations

from typing import Any

from shared.evidence_models import EvidencePackage


def validate_evidence_package(evidence: EvidencePackage) -> dict[str, Any]:
    """Validate an EvidencePackage object. Returns structured valid/errors result."""
    errors: list[str] = []

    if not isinstance(evidence.source, str) or not evidence.source.strip():
        errors.append("source must be a non-empty string")

    if not isinstance(evidence.site_id, str) or not evidence.site_id.strip():
        errors.append("site_id must be a non-empty string")

    if not isinstance(evidence.connector, str) or not evidence.connector.strip():
        errors.append("connector must be a non-empty string")

    if evidence.manifest_entry_count < 0:
        errors.append("manifest_entry_count must be >= 0")

    if evidence.manifest_excluded_count < 0:
        errors.append("manifest_excluded_count must be >= 0")

    if not isinstance(evidence.quality_level, str) or not evidence.quality_level.strip():
        errors.append("quality_level must be a non-empty string")

    if evidence.safe_unknown is None:
        errors.append("safe_unknown list must exist")

    if evidence.notes is None:
        errors.append("notes list must exist")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }
