"""EAR Runtime R5.5 Validate Report models — operator audit contract only.

Human-readable structured review artefact distinct from ValidationResult outcome
authority and PublishEligibilityRecommendation gate signal.
Standard library only. No validation logic. No filesystem access. No Publish.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Fixed boundary text per R5.5 VR-INV-R5-01.
VALIDATE_REPORT_BOUNDARY_DECLARATION = (
    "Validate Report is record-only; no side effects."
)

# Canonical section identifiers — align with R5.5 eleven-section contract.
VALIDATE_REPORT_SECTION_SUMMARY = "summary"
VALIDATE_REPORT_SECTION_IDENTITY = "identity_review"
VALIDATE_REPORT_SECTION_STRUCTURE = "structure_review"
VALIDATE_REPORT_SECTION_POSSESSION = "possession_review"
VALIDATE_REPORT_SECTION_QUALITY = "quality_assessment"
VALIDATE_REPORT_SECTION_REDACTION = "redaction_review"
VALIDATE_REPORT_SECTION_READINESS = "readiness_review"
VALIDATE_REPORT_SECTION_CONSISTENCY = "consistency_review"
VALIDATE_REPORT_SECTION_BLOCKERS = "blockers"
VALIDATE_REPORT_SECTION_WARNINGS = "warnings"
VALIDATE_REPORT_SECTION_AUDIT = "audit_trail"


@dataclass(frozen=True)
class ValidateReportReference:
    """Lightweight pointer to a finding, outcome, or companion artefact."""

    ref_id: str
    ref_type: str
    category: str = ""
    title: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "ref_id": self.ref_id,
            "ref_type": self.ref_type,
            "category": self.category,
            "title": self.title,
        }


@dataclass(frozen=True)
class ValidateReportSummary:
    """Section 1 — operator-first Validate run overview."""

    validation_status: str
    result_ref: str
    snapshot_id: str
    finding_count: int
    blocker_count: int
    warning_count: int
    r2_precondition_pass: bool | None = None
    r3_precondition_pass: bool | None = None
    target_certify_level: int | None = None
    certified_quality_level: int | None = None
    operator_note: str = ""
    downgrade_indicator: bool = False
    recommendation_ref: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "validation_status": self.validation_status,
            "result_ref": self.result_ref,
            "snapshot_id": self.snapshot_id,
            "finding_count": self.finding_count,
            "blocker_count": self.blocker_count,
            "warning_count": self.warning_count,
            "r2_precondition_pass": self.r2_precondition_pass,
            "r3_precondition_pass": self.r3_precondition_pass,
            "target_certify_level": self.target_certify_level,
            "certified_quality_level": self.certified_quality_level,
            "operator_note": self.operator_note,
            "downgrade_indicator": self.downgrade_indicator,
            "recommendation_ref": self.recommendation_ref,
        }


@dataclass(frozen=True)
class ValidateReportSection:
    """Single review section shell — category-bound findings; record only."""

    section_id: str
    category: str
    title: str
    findings: tuple[ValidateReportReference, ...] = field(default_factory=tuple)
    notes: str = ""
    item_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "section_id": self.section_id,
            "category": self.category,
            "title": self.title,
            "findings": [finding.to_dict() for finding in self.findings],
            "notes": self.notes,
            "item_count": self.item_count,
        }


@dataclass(frozen=True)
class ValidateReportAudit:
    """Section 11 — Validate run provenance and audit correlation."""

    report_id: str
    result_ref: str
    validated_at: str
    validated_snapshot_id: str
    validator_version: str
    contract_ref: str
    operator_ref: str
    acquisition_id: str = ""
    evidence_package_ref: str = ""
    r2_precondition_at: str = ""
    r3_precondition_at: str = ""
    reviewed_by: str = ""
    reviewed_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "result_ref": self.result_ref,
            "validated_at": self.validated_at,
            "validated_snapshot_id": self.validated_snapshot_id,
            "validator_version": self.validator_version,
            "contract_ref": self.contract_ref,
            "operator_ref": self.operator_ref,
            "acquisition_id": self.acquisition_id,
            "evidence_package_ref": self.evidence_package_ref,
            "r2_precondition_at": self.r2_precondition_at,
            "r3_precondition_at": self.r3_precondition_at,
            "reviewed_by": self.reviewed_by,
            "reviewed_at": self.reviewed_at,
        }


@dataclass(frozen=True)
class ValidateReport:
    """Operator-facing structured Validate audit — eleven required sections.

    Records validation outcomes only. Does not perform validation, assign certified
    quality, execute Publish, or mutate snapshot, evidence, quarantine, or Store.
    """

    report_id: str
    result_ref: str
    generated_at: str
    summary: ValidateReportSummary
    identity_review: ValidateReportSection
    structure_review: ValidateReportSection
    possession_review: ValidateReportSection
    quality_assessment: ValidateReportSection
    redaction_review: ValidateReportSection
    readiness_review: ValidateReportSection
    consistency_review: ValidateReportSection
    blockers: ValidateReportSection
    warnings: ValidateReportSection
    audit_trail: ValidateReportAudit
    target_certify_level: int | None = None
    boundary_declaration: str = VALIDATE_REPORT_BOUNDARY_DECLARATION

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "result_ref": self.result_ref,
            "generated_at": self.generated_at,
            "target_certify_level": self.target_certify_level,
            "summary": self.summary.to_dict(),
            "identity_review": self.identity_review.to_dict(),
            "structure_review": self.structure_review.to_dict(),
            "possession_review": self.possession_review.to_dict(),
            "quality_assessment": self.quality_assessment.to_dict(),
            "redaction_review": self.redaction_review.to_dict(),
            "readiness_review": self.readiness_review.to_dict(),
            "consistency_review": self.consistency_review.to_dict(),
            "blockers": self.blockers.to_dict(),
            "warnings": self.warnings.to_dict(),
            "audit_trail": self.audit_trail.to_dict(),
            "boundary_declaration": self.boundary_declaration,
        }
