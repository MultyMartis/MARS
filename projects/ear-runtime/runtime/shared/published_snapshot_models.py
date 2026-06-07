"""EAR Runtime R4.1 Published Snapshot models — consumer-visible promotion contract only.

Authoritative R4 promotion artefact distinct from R3 candidate SnapshotPackage,
R5 ValidationResult, R5 PublishEligibilityRecommendation, and consumer intake objects.
Standard library only. No Publish Engine. No Store adapter. No validation logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .snapshot_package_models import SnapshotPackage

# R4 publication state — full lifecycle enum deferred to R4.2.
PUBLISH_STATE_PUBLISHED = "published"

# R4 consumer visibility states — grant model deferred to R4.3.
VISIBILITY_STATE_GRANTED = "granted"
VISIBILITY_STATE_NONE = "none"

# Quality claim stage — third semantic stage per R5.3 (candidate / certified / published).
QUALITY_CLAIM_STAGE_PUBLISHED = "published"


@dataclass(frozen=True)
class PublishedSnapshotIdentity:
    """R4 consumer citation identity — same snapshot_id as validated stored snapshot.

    snapshot_id is the immutable consumer citation key (R3.2; R1.8B).
    R4 cites identity; R4 must not reassign or mutate snapshot_id at Publish.
    """

    snapshot_id: str
    acquisition_id: str
    site_id: str
    snapshot_contract: str
    parent_contract: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "acquisition_id": self.acquisition_id,
            "site_id": self.site_id,
            "snapshot_contract": self.snapshot_contract,
            "parent_contract": self.parent_contract,
        }


@dataclass(frozen=True)
class PublishedSnapshotMetadata:
    """R4-owned publish metadata — assigned at Publish only.

    frozen_package_quality_level is a freeze of R5 certified_quality_level — not
    certification. R4 must not upgrade, recompute, or reassess quality here.
    """

    published_at: str
    published_by: str
    consumer_target: str
    frozen_package_quality_level: int
    quality_claim_stage: str = QUALITY_CLAIM_STAGE_PUBLISHED

    def to_dict(self) -> dict[str, Any]:
        return {
            "published_at": self.published_at,
            "published_by": self.published_by,
            "consumer_target": self.consumer_target,
            "frozen_package_quality_level": self.frozen_package_quality_level,
            "quality_claim_stage": self.quality_claim_stage,
        }


@dataclass(frozen=True)
class PublishedSnapshotPublication:
    """R4 publication record — gate satisfaction and Store citation only.

    validation_result_ref and publish_eligibility_at_gate are opaque citations to
    R5 precondition artefacts — not embedded ValidationResult or recommendation objects.
    store_placement_ref cites R1.8B layout; R4 does not own Store persist.
    """

    publish_state: str
    operator_publish_approval_ref: str
    validation_result_ref: str
    store_placement_ref: str
    publish_eligibility_at_gate: str = ""
    bulk_root: str = ""
    published_snapshot_ref: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "publish_state": self.publish_state,
            "operator_publish_approval_ref": self.operator_publish_approval_ref,
            "validation_result_ref": self.validation_result_ref,
            "store_placement_ref": self.store_placement_ref,
            "publish_eligibility_at_gate": self.publish_eligibility_at_gate,
            "bulk_root": self.bulk_root,
            "published_snapshot_ref": self.published_snapshot_ref,
        }


@dataclass(frozen=True)
class PublishedSnapshotConsumerVisibility:
    """R4 consumer visibility grant — logical permission to begin Consume.

    Distinct from credential handoff and consumer intake execution (consumer programs).
    Visibility begins only after Publish; stored-unpublished snapshots carry none.
    """

    consumer_target: str
    visibility_state: str
    visibility_granted_at: str
    intake_reference_key: str
    consumer_registry_pointer: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "consumer_target": self.consumer_target,
            "visibility_state": self.visibility_state,
            "visibility_granted_at": self.visibility_granted_at,
            "intake_reference_key": self.intake_reference_key,
            "consumer_registry_pointer": self.consumer_registry_pointer,
        }


@dataclass(frozen=True)
class PublishedSnapshot:
    """Aggregate R4 Published Snapshot — validated snapshot promotion, not assembly.

    Represents: validated snapshot (read-only) + publish metadata + publication record
    + consumer visibility grant.

    Must not represent: candidate snapshot, ValidationResult, PublishEligibilityRecommendation,
    or consumer intake object.
    """

    identity: PublishedSnapshotIdentity
    snapshot: SnapshotPackage
    publish_metadata: PublishedSnapshotMetadata
    publication: PublishedSnapshotPublication
    consumer_visibility: PublishedSnapshotConsumerVisibility

    def to_dict(self) -> dict[str, Any]:
        return {
            "identity": self.identity.to_dict(),
            "snapshot": self.snapshot.to_dict(),
            "publish_metadata": self.publish_metadata.to_dict(),
            "publication": self.publication.to_dict(),
            "consumer_visibility": self.consumer_visibility.to_dict(),
        }
