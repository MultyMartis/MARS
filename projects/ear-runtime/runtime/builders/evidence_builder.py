"""EAR Runtime evidence builder — Manifest + Config to EvidencePackage mapping only.

Standard library only. No filesystem access. No network. No hashing.
"""

from __future__ import annotations

from typing import Any

from shared.evidence_models import EvidencePackage
from shared.manifest_models import Manifest


def build_evidence_package(
    manifest: Manifest,
    config: dict[str, Any],
) -> EvidencePackage:
    """Map a Manifest and config to an EvidencePackage without enrichment or IO."""
    return EvidencePackage(
        source=manifest.source,
        site_id=config["site_id"],
        connector=config["connector"],
        manifest_entry_count=manifest.entry_count,
        manifest_excluded_count=manifest.excluded_count,
        quality_level="mock",
        safe_unknown=[],
        notes=[],
    )
