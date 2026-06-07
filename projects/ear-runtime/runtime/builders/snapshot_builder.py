"""EAR Runtime snapshot builder — EvidencePackage to SnapshotPackage mapping only.

Standard library only. No filesystem access. No network. No hashing.
"""

from __future__ import annotations

from shared.evidence_models import EvidencePackage
from shared.snapshot_models import SnapshotPackage


def build_snapshot_package(evidence: EvidencePackage) -> SnapshotPackage:
    """Map an EvidencePackage to a SnapshotPackage without enrichment or IO."""
    snapshot_id = f"snap-mock-{evidence.site_id}-{evidence.source}"
    return SnapshotPackage(
        snapshot_id=snapshot_id,
        site_id=evidence.site_id,
        source=evidence.source,
        connector=evidence.connector,
        quality_level=evidence.quality_level,
        entry_count=evidence.manifest_entry_count,
        excluded_count=evidence.manifest_excluded_count,
        created_from="mock_evidence_package",
        safe_unknown=list(evidence.safe_unknown),
        notes=list(evidence.notes),
    )
