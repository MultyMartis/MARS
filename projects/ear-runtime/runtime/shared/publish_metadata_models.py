"""EAR Runtime R4.4 Publish Metadata models — publication facts only.

Authoritative R4 publish metadata registry distinct from R3 snapshot content,
R5 ValidationResult / ValidateReport, R5 quality certification, R2 evidence,
R4.3 consumer visibility semantics, and Store persist encoding.
Standard library only. No Publish Engine. No Store adapter. No persistence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Canonical R4 publish metadata field identifiers — assigned at Publish only.
METADATA_FIELD_PUBLISHED_AT = "published_at"
METADATA_FIELD_PUBLISHED_BY = "published_by"
METADATA_FIELD_CONSUMER_TARGET = "consumer_target"
METADATA_FIELD_PUBLISH_REASON = "publish_reason"
METADATA_FIELD_PUBLISH_AUDIT_REF = "publish_audit_ref"

CANONICAL_PUBLISH_METADATA_FIELD_IDS: tuple[str, ...] = (
    METADATA_FIELD_PUBLISHED_AT,
    METADATA_FIELD_PUBLISHED_BY,
    METADATA_FIELD_CONSUMER_TARGET,
    METADATA_FIELD_PUBLISH_REASON,
    METADATA_FIELD_PUBLISH_AUDIT_REF,
)

# Assignment timing markers — semantics only; enforcement deferred to R4.7.
ASSIGNMENT_AT_PUBLISH_ONLY = "at_publish_only"
ASSIGNMENT_OPERATOR_DECLARATION = "operator_declaration"
ASSIGNMENT_R4_RECORDS = "r4_records"

# Field ownership markers.
METADATA_OWNER_R4 = "R4"
METADATA_OWNER_OPERATOR = "operator"
METADATA_OWNER_R3 = "R3"
METADATA_OWNER_R5 = "R5"
METADATA_OWNER_STORE = "R1.8"

# Immutability policy markers.
IMMUTABILITY_IMMUTABLE_AFTER_PUBLISH = "immutable_after_publish"
IMMUTABILITY_DISCOURAGED_IN_PLACE_EDIT = "discouraged_in_place_edit"

# Audit record outcome markers — gate satisfaction semantics only.
AUDIT_OUTCOME_GATE_SATISFIED = "gate_satisfied"
AUDIT_OUTCOME_BLOCKED = "blocked"
AUDIT_OUTCOME_DEFERRED = "deferred"


@dataclass(frozen=True)
class PublishMetadataReference:
    """Lightweight publish-metadata pointer for PublishedSnapshot and audit citations."""

    snapshot_id: str
    published_at: str = ""
    publish_audit_ref: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "published_at": self.published_at,
            "publish_audit_ref": self.publish_audit_ref,
        }


@dataclass(frozen=True)
class PublishMetadataField:
    """Single canonical publish metadata field specification — contract only."""

    field_id: str
    title: str
    required_at_publish: bool
    assigned_by: str
    owner: str
    assignment_timing: str
    immutability: str
    meaning: str
    not_owner: tuple[str, ...] = field(default_factory=tuple)
    survives_from_snapshot: bool = False
    authority: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "field_id": self.field_id,
            "title": self.title,
            "required_at_publish": self.required_at_publish,
            "assigned_by": self.assigned_by,
            "owner": self.owner,
            "assignment_timing": self.assignment_timing,
            "immutability": self.immutability,
            "meaning": self.meaning,
            "not_owner": list(self.not_owner),
            "survives_from_snapshot": self.survives_from_snapshot,
            "authority": self.authority,
        }


@dataclass(frozen=True)
class PublishMetadataAudit:
    """Publish gate audit record — publication facts and HITL refs, not ValidationResult."""

    audit_id: str
    snapshot_id: str
    published_at: str
    published_by: str
    operator_publish_approval_ref: str
    publish_reason: str
    outcome: str
    validation_result_ref: str = ""
    publish_eligibility_at_gate: str = ""
    store_placement_ref: str = ""
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "audit_id": self.audit_id,
            "snapshot_id": self.snapshot_id,
            "published_at": self.published_at,
            "published_by": self.published_by,
            "operator_publish_approval_ref": self.operator_publish_approval_ref,
            "publish_reason": self.publish_reason,
            "outcome": self.outcome,
            "validation_result_ref": self.validation_result_ref,
            "publish_eligibility_at_gate": self.publish_eligibility_at_gate,
            "store_placement_ref": self.store_placement_ref,
            "notes": self.notes,
        }

    def to_reference(self) -> PublishMetadataReference:
        return PublishMetadataReference(
            snapshot_id=self.snapshot_id,
            published_at=self.published_at,
            publish_audit_ref=self.audit_id,
        )


@dataclass(frozen=True)
class PublishMetadata:
    """Aggregate R4 publish metadata — publication facts assigned at Publish only.

    Represents: when, by whom, for which consumer target, why, and audit citation.
    Must not represent: ValidationResult, quality certification, snapshot content,
    or consumer visibility grant (R4.3).
    """

    snapshot_id: str
    published_at: str
    published_by: str
    consumer_target: str
    publish_reason: str
    publish_audit_ref: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "published_at": self.published_at,
            "published_by": self.published_by,
            "consumer_target": self.consumer_target,
            "publish_reason": self.publish_reason,
            "publish_audit_ref": self.publish_audit_ref,
        }

    def to_reference(self) -> PublishMetadataReference:
        return PublishMetadataReference(
            snapshot_id=self.snapshot_id,
            published_at=self.published_at,
            publish_audit_ref=self.publish_audit_ref,
        )

    def field_values(self) -> dict[str, str]:
        """Return canonical field map excluding snapshot_id citation key."""
        return {
            METADATA_FIELD_PUBLISHED_AT: self.published_at,
            METADATA_FIELD_PUBLISHED_BY: self.published_by,
            METADATA_FIELD_CONSUMER_TARGET: self.consumer_target,
            METADATA_FIELD_PUBLISH_REASON: self.publish_reason,
            METADATA_FIELD_PUBLISH_AUDIT_REF: self.publish_audit_ref,
        }


@dataclass(frozen=True)
class PublishMetadataInvariant:
    """Publish metadata boundary rule — PM-INV-R4-* semantics only."""

    invariant_id: str
    title: str
    statement: str
    owner: str
    authority: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "invariant_id": self.invariant_id,
            "title": self.title,
            "statement": self.statement,
            "owner": self.owner,
            "authority": self.authority,
        }


@dataclass(frozen=True)
class PublishMetadataRegistry:
    """Canonical registry of R4 publish metadata fields, invariants, and ownership."""

    metadata_fields: tuple[PublishMetadataField, ...] = field(default_factory=tuple)
    invariants: tuple[PublishMetadataInvariant, ...] = field(default_factory=tuple)

    def get_field(self, field_id: str) -> PublishMetadataField | None:
        for metadata_field in self.metadata_fields:
            if metadata_field.field_id == field_id:
                return metadata_field
        return None

    def get_invariant(self, invariant_id: str) -> PublishMetadataInvariant | None:
        for invariant in self.invariants:
            if invariant.invariant_id == invariant_id:
                return invariant
        return None

    def field_ids(self) -> tuple[str, ...]:
        return tuple(metadata_field.field_id for metadata_field in self.metadata_fields)

    def required_field_ids(self) -> tuple[str, ...]:
        return tuple(
            metadata_field.field_id
            for metadata_field in self.metadata_fields
            if metadata_field.required_at_publish
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "metadata_fields": [metadata_field.to_dict() for metadata_field in self.metadata_fields],
            "invariants": [invariant.to_dict() for invariant in self.invariants],
        }


def _build_canonical_metadata_fields() -> tuple[PublishMetadataField, ...]:
    return (
        PublishMetadataField(
            field_id=METADATA_FIELD_PUBLISHED_AT,
            title="Published at",
            required_at_publish=True,
            assigned_by=METADATA_OWNER_R4,
            owner=METADATA_OWNER_R4,
            assignment_timing=ASSIGNMENT_AT_PUBLISH_ONLY,
            immutability=IMMUTABILITY_IMMUTABLE_AFTER_PUBLISH,
            meaning=(
                "ISO-8601-style timestamp when R4 Publish gate executed — not Validate time, "
                "not Store persist time."
            ),
            not_owner=(METADATA_OWNER_R5, METADATA_OWNER_R3, METADATA_OWNER_STORE),
            survives_from_snapshot=False,
            authority="R4-CHARTER O-R4-03; I-R4-08",
        ),
        PublishMetadataField(
            field_id=METADATA_FIELD_PUBLISHED_BY,
            title="Published by",
            required_at_publish=True,
            assigned_by=METADATA_OWNER_R4,
            owner=METADATA_OWNER_R4,
            assignment_timing=ASSIGNMENT_AT_PUBLISH_ONLY,
            immutability=IMMUTABILITY_IMMUTABLE_AFTER_PUBLISH,
            meaning=(
                "Operator or HITL identity ref who approved Publish — distinct from Validate sign-off "
                "and distinct from R5 validator identity."
            ),
            not_owner=(METADATA_OWNER_R5,),
            survives_from_snapshot=False,
            authority="R4-CHARTER O-R4-03; I-R4-08",
        ),
        PublishMetadataField(
            field_id=METADATA_FIELD_CONSUMER_TARGET,
            title="Consumer target",
            required_at_publish=True,
            assigned_by=METADATA_OWNER_OPERATOR,
            owner=METADATA_OWNER_R4,
            assignment_timing=ASSIGNMENT_OPERATOR_DECLARATION,
            immutability=IMMUTABILITY_IMMUTABLE_AFTER_PUBLISH,
            meaning=(
                "Registered consumer program identifier (e.g. ocpilot) declared by operator and "
                "recorded at Publish — routing label only; does not grant visibility by itself."
            ),
            not_owner=(METADATA_OWNER_R5, METADATA_OWNER_R3),
            survives_from_snapshot=False,
            authority="R4-CHARTER I-R4-09; R4.3 CV-R4-05",
        ),
        PublishMetadataField(
            field_id=METADATA_FIELD_PUBLISH_REASON,
            title="Publish reason",
            required_at_publish=True,
            assigned_by=METADATA_OWNER_R4,
            owner=METADATA_OWNER_R4,
            assignment_timing=ASSIGNMENT_AT_PUBLISH_ONLY,
            immutability=IMMUTABILITY_IMMUTABLE_AFTER_PUBLISH,
            meaning=(
                "Operator-facing publication rationale — why this validated snapshot was promoted "
                "to consumer visibility. Not a validation finding or quality assessment."
            ),
            not_owner=(METADATA_OWNER_R5,),
            survives_from_snapshot=False,
            authority="R4 Implementation Charter § R4.4",
        ),
        PublishMetadataField(
            field_id=METADATA_FIELD_PUBLISH_AUDIT_REF,
            title="Publish audit ref",
            required_at_publish=True,
            assigned_by=METADATA_OWNER_R4,
            owner=METADATA_OWNER_R4,
            assignment_timing=ASSIGNMENT_AT_PUBLISH_ONLY,
            immutability=IMMUTABILITY_IMMUTABLE_AFTER_PUBLISH,
            meaning=(
                "Opaque citation to PublishMetadataAudit or acquisition-log publish record — "
                "gate satisfaction audit, not ValidationResult embed."
            ),
            not_owner=(METADATA_OWNER_R5,),
            survives_from_snapshot=False,
            authority="R4-CHARTER O-R4-06; R4.5 PublishResult deferred",
        ),
    )


def _build_canonical_invariants() -> tuple[PublishMetadataInvariant, ...]:
    return (
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-01",
            title="Publication facts only",
            statement=(
                "Publish metadata records publication facts — when, by whom, for whom, why, "
                "and audit citation. It must not embed ValidationResult, quality certification, "
                "or snapshot section content."
            ),
            owner=METADATA_OWNER_R4,
            authority="R4.4 mission",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-02",
            title="Assigned at Publish only",
            statement=(
                "All canonical publish metadata fields are absent before R4 Publish execution "
                "and assigned once at Publish — not at Store, Validate, or assembly."
            ),
            owner=METADATA_OWNER_R4,
            authority="R4 Implementation Charter § R4.4",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-03",
            title="Immutable after Publish",
            statement=(
                "In-place edit of publish metadata after Publish is discouraged; corrections "
                "require new acquisition cycle with new snapshot_id — publish gate is not reversible."
            ),
            owner=METADATA_OWNER_R4,
            authority="R1.8B immutability; PST-R4-F03",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-04",
            title="Not validation metadata",
            statement=(
                "Validate timestamps, ValidationResult outcomes, ValidateReport findings, and "
                "PublishEligibilityRecommendation are R5 artefacts — cited opaquely in audit only, "
                "never owned as publish metadata fields."
            ),
            owner=METADATA_OWNER_R5,
            authority="R5.1; R5.6 PE-INV-R5-01",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-05",
            title="Not quality metadata",
            statement=(
                "Certified package_quality_level is R5 possession metadata frozen on "
                "PublishedSnapshot aggregate (R4.1) — not a canonical publish metadata field. "
                "R4 must not upgrade or certify quality in publish metadata."
            ),
            owner=METADATA_OWNER_R5,
            authority="R5.3; Q-INV-R5-01",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-06",
            title="consumer_target does not imply visibility",
            statement=(
                "Setting consumer_target in config or metadata without R4 Publish execution does "
                "not grant consumer visibility — visibility requires publish_state published and "
                "R4.3 visibility grant (CV-R4-01; CV-R4-05)."
            ),
            owner=METADATA_OWNER_R4,
            authority="R4.3; R4 Implementation Charter § What does not make a snapshot published",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-07",
            title="Store vs Publish metadata",
            statement=(
                "Store placement records validated snapshot identity and R5 certified level — "
                "publish metadata is added only at Publish. Store persist without Publish leaves "
                "canonical fields absent."
            ),
            owner=METADATA_OWNER_STORE,
            authority="R1.8B § Store vs Publish",
        ),
        PublishMetadataInvariant(
            invariant_id="PM-INV-R4-08",
            title="R4 ownership boundary",
            statement=(
                "R4 owns publish metadata assignment only — not quality certification, validation "
                "results, evidence, or snapshot content."
            ),
            owner=METADATA_OWNER_R4,
            authority="R4-CHARTER ownership matrix",
        ),
    )


CANONICAL_PUBLISH_METADATA_REGISTRY = PublishMetadataRegistry(
    metadata_fields=_build_canonical_metadata_fields(),
    invariants=_build_canonical_invariants(),
)
