"""EAR Runtime R5.1 Validation Result models — EAR Validate output contract only.

Authoritative R5 certification artefact distinct from R2 structural validation,
R3 assembly eligibility, Publish approval, and consumer readiness.
Standard library only. No validation logic. No filesystem access. No Publish.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# R5 canonical validation statuses — not R2/R3 pass semantics.
VALIDATION_STATUS_PASS = "PASS"
VALIDATION_STATUS_PASS_WITH_NOTES = "PASS_WITH_NOTES"
VALIDATION_STATUS_FAIL = "FAIL"

# R5 canonical severity levels — no scoring, weighting, or percentages.
VALIDATION_SEVERITY_INFO = "INFO"
VALIDATION_SEVERITY_WARNING = "WARNING"
VALIDATION_SEVERITY_ERROR = "ERROR"
VALIDATION_SEVERITY_BLOCKER = "BLOCKER"

# R5 validation categories per R5 Charter — references only, no rule logic.
VALIDATION_CATEGORY_IDENTITY = "identity"
VALIDATION_CATEGORY_STRUCTURE = "structure"
VALIDATION_CATEGORY_POSSESSION = "possession"
VALIDATION_CATEGORY_QUALITY = "quality"
VALIDATION_CATEGORY_REDACTION = "redaction"
VALIDATION_CATEGORY_READINESS = "readiness"
VALIDATION_CATEGORY_CONSISTENCY = "consistency"

# R5 Publish Eligibility Recommendation — advisory only; R4 decides Publish.
VALIDATION_RECOMMENDATION_ELIGIBLE = "ELIGIBLE"
VALIDATION_RECOMMENDATION_ELIGIBLE_WITH_NOTES = "ELIGIBLE_WITH_NOTES"
VALIDATION_RECOMMENDATION_NOT_ELIGIBLE = "NOT_ELIGIBLE"


@dataclass(frozen=True)
class ValidationStatus:
    """R5 EAR Validate outcome — distinct from R2 structural pass and R3 assembly pass."""

    value: str

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


@dataclass(frozen=True)
class ValidationSeverity:
    """R5 finding severity — no scoring or weighting."""

    value: str

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


@dataclass(frozen=True)
class ValidationCategoryRef:
    """Reference to an R5 validation category — types only, no rule implementation."""

    category: str

    def to_dict(self) -> dict[str, Any]:
        return {"category": self.category}


@dataclass(frozen=True)
class ValidationRecommendation:
    """R5 Publish Eligibility Recommendation — recommendation != Publish; operator HITL required."""

    value: str

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


@dataclass(frozen=True)
class ValidationFinding:
    """Single R5 validation finding — operator-facing; no paths, credentials, or publish actions."""

    finding_id: str
    category: ValidationCategoryRef
    severity: ValidationSeverity
    title: str
    description: str
    recommendation: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "finding_id": self.finding_id,
            "category": self.category.to_dict(),
            "severity": self.severity.to_dict(),
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation,
        }


@dataclass(frozen=True)
class ValidationSummary:
    """R5 aggregate outcome summary — certified_quality_level is R5-owned; no certification logic here."""

    status: ValidationStatus
    finding_count: int
    blocker_count: int
    warning_count: int
    certified_quality_level: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.to_dict(),
            "finding_count": self.finding_count,
            "blocker_count": self.blocker_count,
            "warning_count": self.warning_count,
            "certified_quality_level": self.certified_quality_level,
        }


@dataclass(frozen=True)
class ValidationAudit:
    """R5 Validate audit metadata — no implementation logic."""

    validator_version: str
    validated_at: str
    validated_snapshot_id: str
    operator_ref: str
    contract_ref: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "validator_version": self.validator_version,
            "validated_at": self.validated_at,
            "validated_snapshot_id": self.validated_snapshot_id,
            "operator_ref": self.operator_ref,
            "contract_ref": self.contract_ref,
        }


@dataclass(frozen=True)
class ValidationResult:
    """Aggregate R5 EAR Validate output — sole authoritative R5 certification artefact.

    Must not represent R2 structural validation, R3 assembly validation,
    Publish approval, or consumer readiness.
    """

    result_id: str
    summary: ValidationSummary
    findings: tuple[ValidationFinding, ...] = field(default_factory=tuple)
    audit: ValidationAudit | None = None
    recommendation: ValidationRecommendation | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "result_id": self.result_id,
            "summary": self.summary.to_dict(),
            "findings": [finding.to_dict() for finding in self.findings],
            "audit": self.audit.to_dict() if self.audit is not None else None,
            "recommendation": (
                self.recommendation.to_dict()
                if self.recommendation is not None
                else None
            ),
        }
