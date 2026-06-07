"""EAR Runtime R4.5 Publish Result models — Publish attempt outcome contract only.

Authoritative R4 promotion attempt artefact distinct from R5 ValidationResult,
R5 PublishEligibilityRecommendation, PublishedSnapshot content, and consumer intake.
Standard library only. No Publish Engine logic. No persistence. No filesystem access.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# R4 canonical publish result states — exactly three; no scores or percentages.
PUBLISH_RESULT_SUCCESS = "SUCCESS"
PUBLISH_RESULT_BLOCKED = "BLOCKED"
PUBLISH_RESULT_DEFERRED = "DEFERRED"

CANONICAL_PUBLISH_RESULT_STATES: tuple[str, ...] = (
    PUBLISH_RESULT_SUCCESS,
    PUBLISH_RESULT_BLOCKED,
    PUBLISH_RESULT_DEFERRED,
)

# Fixed boundary text per R4.5 PR-INV-R4-01.
PUBLISH_RESULT_BOUNDARY_DECLARATION = (
    "PublishResult records Publish attempt outcome only; no side effects by itself."
)

# PublishResultReference ref_type markers — citation only, not embedded aggregates.
PUBLISH_RESULT_REF_PUBLISHED_SNAPSHOT = "published_snapshot"
PUBLISH_RESULT_REF_PUBLISH_METADATA = "publish_metadata"


@dataclass(frozen=True)
class PublishResultState:
    """R4 Publish attempt outcome — distinct from R5 ValidationResult status."""

    value: str

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


@dataclass(frozen=True)
class PublishResultReference:
    """Lightweight pointer to a PublishedSnapshot or PublishMetadata aggregate."""

    ref_id: str
    ref_type: str
    snapshot_id: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "ref_id": self.ref_id,
            "ref_type": self.ref_type,
            "snapshot_id": self.snapshot_id,
        }


@dataclass(frozen=True)
class PublishResultSummary:
    """Operator-first Publish attempt outcome statement — no secrets or paths."""

    statement: str
    last_stage_evaluated: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "statement": self.statement,
            "last_stage_evaluated": self.last_stage_evaluated,
        }


@dataclass(frozen=True)
class PublishResultAudit:
    """Publish attempt audit record — HITL refs and gate satisfaction; not ValidationResult."""

    audit_id: str
    snapshot_id: str
    generated_at: str
    outcome: str
    operator_publish_approval_ref: str = ""
    validate_sign_off_ref: str = ""
    validation_result_ref: str = ""
    publish_recommendation_ref: str = ""
    gate_checklist: tuple[str, ...] = field(default_factory=tuple)
    last_stage_evaluated: int = 0
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "audit_id": self.audit_id,
            "snapshot_id": self.snapshot_id,
            "generated_at": self.generated_at,
            "outcome": self.outcome,
            "operator_publish_approval_ref": self.operator_publish_approval_ref,
            "validate_sign_off_ref": self.validate_sign_off_ref,
            "validation_result_ref": self.validation_result_ref,
            "publish_recommendation_ref": self.publish_recommendation_ref,
            "gate_checklist": list(self.gate_checklist),
            "last_stage_evaluated": self.last_stage_evaluated,
            "notes": self.notes,
        }


@dataclass(frozen=True)
class PublishResult:
    """Aggregate R4 Publish attempt outcome — sole authoritative R4 result artefact.

    Must not represent ValidationResult certification, PublishEligibilityRecommendation
    advisory authority, PublishedSnapshot content, or consumer intake execution.
    """

    publish_result_id: str
    publish_result_state: str
    summary: PublishResultSummary
    validation_result_ref: str
    publish_recommendation_ref: str
    notes: tuple[str, ...] = field(default_factory=tuple)
    audit_ref: str = ""
    published_snapshot_ref: PublishResultReference | None = None
    publish_metadata_ref: PublishResultReference | None = None
    snapshot_id: str = ""
    generated_at: str = ""
    boundary_declaration: str = PUBLISH_RESULT_BOUNDARY_DECLARATION

    def to_dict(self) -> dict[str, Any]:
        return {
            "publish_result_id": self.publish_result_id,
            "publish_result_state": self.publish_result_state,
            "summary": self.summary.to_dict(),
            "published_snapshot_ref": (
                self.published_snapshot_ref.to_dict()
                if self.published_snapshot_ref is not None
                else None
            ),
            "publish_metadata_ref": (
                self.publish_metadata_ref.to_dict()
                if self.publish_metadata_ref is not None
                else None
            ),
            "validation_result_ref": self.validation_result_ref,
            "publish_recommendation_ref": self.publish_recommendation_ref,
            "notes": list(self.notes),
            "audit_ref": self.audit_ref,
            "snapshot_id": self.snapshot_id,
            "generated_at": self.generated_at,
            "boundary_declaration": self.boundary_declaration,
        }
