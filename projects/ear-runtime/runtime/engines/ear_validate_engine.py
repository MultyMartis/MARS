"""EAR Runtime R5.7 Validate Engine — orchestration skeleton only.

Seven-stage Validate flow per R5.7 architecture. Mock assessors only — no R5-V-* rules,
no persistence, no CLI integration, no filesystem writes, no Publish, no snapshot mutation.
Standard library only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from shared.publish_eligibility_models import (
    PUBLISH_ELIGIBILITY_BOUNDARY_DECLARATION,
    PUBLISH_ELIGIBILITY_ELIGIBLE,
    PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES,
    PUBLISH_ELIGIBILITY_NOT_ELIGIBLE,
    PublishEligibilityRecommendation,
)
from shared.quality_possession_models import (
    CANONICAL_QUALITY_POSSESSION_REGISTRY,
    QUALITY_CLAIM_STAGE_CERTIFIED,
    QUALITY_LEVEL_L0,
    QualityPossessionAssessment,
    QualityPossessionReference,
)
from shared.redaction_review_models import (
    REDACTION_RECOMMENDATION_NO_ACTION_REQUIRED,
    REDACTION_STATUS_CLEAR,
    RedactionAudit,
    RedactionRecommendation,
    RedactionReview,
    RedactionReviewSummary,
    RedactionStatus,
)
from shared.snapshot_package_models import SNAPSHOT_CONTRACT, SnapshotPackage
from shared.validate_report_models import (
    VALIDATE_REPORT_BOUNDARY_DECLARATION,
    VALIDATE_REPORT_SECTION_BLOCKERS,
    VALIDATE_REPORT_SECTION_CONSISTENCY,
    VALIDATE_REPORT_SECTION_IDENTITY,
    VALIDATE_REPORT_SECTION_POSSESSION,
    VALIDATE_REPORT_SECTION_QUALITY,
    VALIDATE_REPORT_SECTION_READINESS,
    VALIDATE_REPORT_SECTION_REDACTION,
    VALIDATE_REPORT_SECTION_STRUCTURE,
    VALIDATE_REPORT_SECTION_WARNINGS,
    ValidateReport,
    ValidateReportAudit,
    ValidateReportReference,
    ValidateReportSection,
    ValidateReportSummary,
)
from shared.validation_category_models import (
    CANONICAL_VALIDATION_CATEGORY_REGISTRY,
    VALIDATION_CATEGORY_CONSISTENCY,
    VALIDATION_CATEGORY_IDENTITY,
    VALIDATION_CATEGORY_POSSESSION,
    VALIDATION_CATEGORY_QUALITY,
    VALIDATION_CATEGORY_READINESS,
    VALIDATION_CATEGORY_REDACTION,
    VALIDATION_CATEGORY_STRUCTURE,
)
from shared.validation_result_models import (
    VALIDATION_CATEGORY_CONSISTENCY as FINDING_CATEGORY_CONSISTENCY,
    VALIDATION_CATEGORY_IDENTITY as FINDING_CATEGORY_IDENTITY,
    VALIDATION_CATEGORY_POSSESSION as FINDING_CATEGORY_POSSESSION,
    VALIDATION_CATEGORY_QUALITY as FINDING_CATEGORY_QUALITY,
    VALIDATION_CATEGORY_READINESS as FINDING_CATEGORY_READINESS,
    VALIDATION_CATEGORY_REDACTION as FINDING_CATEGORY_REDACTION,
    VALIDATION_CATEGORY_STRUCTURE as FINDING_CATEGORY_STRUCTURE,
    VALIDATION_RECOMMENDATION_ELIGIBLE,
    VALIDATION_RECOMMENDATION_ELIGIBLE_WITH_NOTES,
    VALIDATION_RECOMMENDATION_NOT_ELIGIBLE,
    VALIDATION_SEVERITY_BLOCKER,
    VALIDATION_SEVERITY_WARNING,
    VALIDATION_STATUS_FAIL,
    VALIDATION_STATUS_PASS,
    VALIDATION_STATUS_PASS_WITH_NOTES,
    ValidationAudit,
    ValidationCategoryRef,
    ValidationFinding,
    ValidationRecommendation,
    ValidationResult,
    ValidationSeverity,
    ValidationStatus,
    ValidationSummary,
)

VALIDATOR_VERSION = "ear-validate-engine-skeleton-v1"

# R5.3 conceptual record alias per R5.7 VE-O-05.
PossessionAssessmentRecord = QualityPossessionAssessment

_CANONICAL_CATEGORY_ORDER: tuple[str, ...] = (
    VALIDATION_CATEGORY_IDENTITY,
    VALIDATION_CATEGORY_STRUCTURE,
    VALIDATION_CATEGORY_POSSESSION,
    VALIDATION_CATEGORY_CONSISTENCY,
    VALIDATION_CATEGORY_QUALITY,
    VALIDATION_CATEGORY_REDACTION,
    VALIDATION_CATEGORY_READINESS,
)


@dataclass(frozen=True)
class PreconditionContext:
    """Stage 1 precondition flags — orchestration record only."""

    candidate_present: bool
    r2_structural_pass: bool | None
    r3_assembly_pass: bool | None
    hard_fail: bool
    fail_reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class ValidateRunContext:
    """Read-only Validate run inputs — no snapshot mutation."""

    snapshot: SnapshotPackage
    target_certify_level: int | None
    operator_ref: str
    validated_at: str
    contract_ref: str
    r2_structural_pass: bool | None
    r3_assembly_pass: bool | None
    preconditions: PreconditionContext


@dataclass(frozen=True)
class ValidateEngineOutput:
    """Authoritative R5 Validate output bundle per R5.7 VE-O-01–06."""

    validation_result: ValidationResult
    validate_report: ValidateReport
    publish_eligibility_recommendation: PublishEligibilityRecommendation
    redaction_review: RedactionReview
    possession_assessment: PossessionAssessmentRecord

    def to_dict(self) -> dict[str, Any]:
        return {
            "validation_result": self.validation_result.to_dict(),
            "validate_report": self.validate_report.to_dict(),
            "publish_eligibility_recommendation": (
                self.publish_eligibility_recommendation.to_dict()
            ),
            "redaction_review": self.redaction_review.to_dict(),
            "possession_assessment": self.possession_assessment.to_dict(),
        }


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _build_stable_id(prefix: str, snapshot_id: str, timestamp: str) -> str:
    safe_ts = timestamp.replace(":", "").replace("+", "")
    return f"{prefix}-{snapshot_id}-{safe_ts}"


def _assess_identity(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _assess_structure(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _assess_possession(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _assess_consistency(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _assess_quality(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _assess_redaction(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _assess_readiness(context: ValidateRunContext) -> tuple[ValidationFinding, ...]:
    return ()


def _dispatch_category_assessor(
    category_id: str,
    context: ValidateRunContext,
) -> tuple[ValidationFinding, ...]:
    assessors = {
        VALIDATION_CATEGORY_IDENTITY: _assess_identity,
        VALIDATION_CATEGORY_STRUCTURE: _assess_structure,
        VALIDATION_CATEGORY_POSSESSION: _assess_possession,
        VALIDATION_CATEGORY_CONSISTENCY: _assess_consistency,
        VALIDATION_CATEGORY_QUALITY: _assess_quality,
        VALIDATION_CATEGORY_REDACTION: _assess_redaction,
        VALIDATION_CATEGORY_READINESS: _assess_readiness,
    }
    assessor = assessors.get(category_id)
    if assessor is None:
        return ()
    return assessor(context)


def _stage_preconditions(
    snapshot: SnapshotPackage | None,
    *,
    target_certify_level: int | None,
    r2_structural_pass: bool | None,
    r3_assembly_pass: bool | None,
) -> PreconditionContext:
    """Stage 1 — entry gate; fail closed on hard precondition failures."""
    fail_reasons: list[str] = []

    if snapshot is None:
        fail_reasons.append("Candidate Snapshot Package is required (VE-I-01)")

    if snapshot is not None:
        identity = snapshot.identity
        if identity.snapshot_contract != SNAPSHOT_CONTRACT:
            fail_reasons.append(
                f"Candidate must use R3 contract path {SNAPSHOT_CONTRACT!r}"
            )

    if target_certify_level is not None and target_certify_level not in (0, 1, 2, 3):
        fail_reasons.append("target_certify_level must be in 0–3 when supplied")

    if r3_assembly_pass is False:
        fail_reasons.append("R3 assembly eligibility precondition failed (VB-R3-01)")

    if r2_structural_pass is False:
        fail_reasons.append("R2 structural validation precondition failed")

    hard_fail = bool(fail_reasons)
    return PreconditionContext(
        candidate_present=snapshot is not None,
        r2_structural_pass=r2_structural_pass,
        r3_assembly_pass=r3_assembly_pass,
        hard_fail=hard_fail,
        fail_reasons=tuple(fail_reasons),
    )


def _stage_category_evaluation(
    context: ValidateRunContext,
) -> tuple[ValidationFinding, ...]:
    """Stage 2 — dispatch seven categories in canonical order."""
    if context.preconditions.hard_fail:
        return ()

    findings: list[ValidationFinding] = []
    for category_id in _CANONICAL_CATEGORY_ORDER:
        if CANONICAL_VALIDATION_CATEGORY_REGISTRY.get(category_id) is None:
            continue
        findings.extend(_dispatch_category_assessor(category_id, context))
    return tuple(findings)


def _stage_quality_assessment(
    context: ValidateRunContext,
    category_findings: tuple[ValidationFinding, ...],
) -> PossessionAssessmentRecord:
    """Stage 3 — mock certified level wiring; no possession algorithms."""
    snapshot_id = context.snapshot.identity.snapshot_id
    timestamp = context.validated_at
    target = context.target_certify_level
    hard_fail = context.preconditions.hard_fail

    if hard_fail:
        level_id = QUALITY_LEVEL_L0
        summary = "Precondition failure — certified level not assigned."
    else:
        level_id = target if target is not None else QUALITY_LEVEL_L0
        if CANONICAL_QUALITY_POSSESSION_REGISTRY.get(level_id) is None:
            level_id = QUALITY_LEVEL_L0
        summary = (
            "Skeleton assessment — mock certified level; "
            "R3 candidate L0 placeholder ≠ R5 certified L0 (VB-R3-06)."
        )

    target_ref = (
        QualityPossessionReference(level_id=target)
        if target is not None
        else None
    )
    return PossessionAssessmentRecord(
        assessment_id=_build_stable_id("possession", snapshot_id, timestamp),
        claim_stage=QUALITY_CLAIM_STAGE_CERTIFIED,
        level=QualityPossessionReference(level_id=level_id),
        target_level=target_ref,
        summary=summary,
    )


def _stage_redaction_review(context: ValidateRunContext) -> RedactionReview:
    """Stage 4 — mock RedactionReview aggregate; no scanners."""
    identity = context.snapshot.identity
    timestamp = context.validated_at
    return RedactionReview(
        review_id=_build_stable_id("redaction", identity.snapshot_id, timestamp),
        summary=RedactionReviewSummary(
            status=RedactionStatus(value=REDACTION_STATUS_CLEAR),
            finding_count=0,
            blocked_count=0,
            review_required_count=0,
        ),
        findings=(),
        audit=RedactionAudit(
            reviewer_version=VALIDATOR_VERSION,
            reviewed_at=timestamp,
            reviewed_snapshot_id=identity.snapshot_id,
            operator_ref=context.operator_ref,
            contract_ref=context.contract_ref,
        ),
        recommendation=RedactionRecommendation(
            value=REDACTION_RECOMMENDATION_NO_ACTION_REQUIRED
        ),
    )


def _precondition_blocker_findings(
    preconditions: PreconditionContext,
) -> tuple[ValidationFinding, ...]:
    findings: list[ValidationFinding] = []
    for index, reason in enumerate(preconditions.fail_reasons):
        findings.append(
            ValidationFinding(
                finding_id=f"precondition-blocker-{index + 1}",
                category=ValidationCategoryRef(category=FINDING_CATEGORY_READINESS),
                severity=ValidationSeverity(value=VALIDATION_SEVERITY_BLOCKER),
                title="Validate precondition failure",
                description=reason,
            )
        )
    return tuple(findings)


def _derive_validation_status(
    findings: tuple[ValidationFinding, ...],
    preconditions: PreconditionContext,
) -> str:
    """Stage 5 status derivation — VE-MAP-R5-01 conceptual; no scoring."""
    if preconditions.hard_fail:
        return VALIDATION_STATUS_FAIL

    has_blocker = any(
        finding.severity.value == VALIDATION_SEVERITY_BLOCKER for finding in findings
    )
    if has_blocker:
        return VALIDATION_STATUS_FAIL

    has_warning = any(
        finding.severity.value == VALIDATION_SEVERITY_WARNING for finding in findings
    )
    if has_warning:
        return VALIDATION_STATUS_PASS_WITH_NOTES

    return VALIDATION_STATUS_PASS


def _recommendation_value_for_status(status: str) -> str:
    """VE-MAP-R5-06 default mapping — one-way advisory."""
    if status == VALIDATION_STATUS_PASS:
        return VALIDATION_RECOMMENDATION_ELIGIBLE
    if status == VALIDATION_STATUS_PASS_WITH_NOTES:
        return VALIDATION_RECOMMENDATION_ELIGIBLE_WITH_NOTES
    return VALIDATION_RECOMMENDATION_NOT_ELIGIBLE


def _publish_state_for_status(status: str) -> str:
    if status == VALIDATION_STATUS_PASS:
        return PUBLISH_ELIGIBILITY_ELIGIBLE
    if status == VALIDATION_STATUS_PASS_WITH_NOTES:
        return PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES
    return PUBLISH_ELIGIBILITY_NOT_ELIGIBLE


def _count_severity(
    findings: tuple[ValidationFinding, ...],
    severity: str,
) -> int:
    return sum(1 for finding in findings if finding.severity.value == severity)


def _stage_outcome_aggregation(
    context: ValidateRunContext,
    category_findings: tuple[ValidationFinding, ...],
    possession_assessment: PossessionAssessmentRecord,
    redaction_review: RedactionReview,
) -> ValidationResult:
    """Stage 5 — build authoritative ValidationResult."""
    precondition_findings = _precondition_blocker_findings(context.preconditions)
    all_findings = precondition_findings + category_findings
    status_value = _derive_validation_status(all_findings, context.preconditions)

    blocker_count = _count_severity(all_findings, VALIDATION_SEVERITY_BLOCKER)
    warning_count = _count_severity(all_findings, VALIDATION_SEVERITY_WARNING)
    finding_count = len(all_findings)

    certified_level: int | None
    if status_value == VALIDATION_STATUS_FAIL:
        certified_level = None
    else:
        certified_level = possession_assessment.level.level_id

    snapshot_id = context.snapshot.identity.snapshot_id
    result_id = _build_stable_id("validate", snapshot_id, context.validated_at)

    return ValidationResult(
        result_id=result_id,
        summary=ValidationSummary(
            status=ValidationStatus(value=status_value),
            finding_count=finding_count,
            blocker_count=blocker_count,
            warning_count=warning_count,
            certified_quality_level=certified_level,
        ),
        findings=all_findings,
        audit=ValidationAudit(
            validator_version=VALIDATOR_VERSION,
            validated_at=context.validated_at,
            validated_snapshot_id=snapshot_id,
            operator_ref=context.operator_ref,
            contract_ref=context.contract_ref,
        ),
        recommendation=ValidationRecommendation(
            value=_recommendation_value_for_status(status_value)
        ),
    )


def _finding_to_reference(finding: ValidationFinding) -> ValidateReportReference:
    return ValidateReportReference(
        ref_id=finding.finding_id,
        ref_type="finding",
        category=finding.category.category,
        title=finding.title,
    )


def _build_category_section(
    section_id: str,
    category: str,
    title: str,
    findings: tuple[ValidationFinding, ...],
    notes: str = "",
) -> ValidateReportSection:
    refs = tuple(_finding_to_reference(finding) for finding in findings)
    return ValidateReportSection(
        section_id=section_id,
        category=category,
        title=title,
        findings=refs,
        notes=notes,
        item_count=len(refs),
    )


def _findings_for_category(
    findings: tuple[ValidationFinding, ...],
    category: str,
) -> tuple[ValidationFinding, ...]:
    return tuple(
        finding for finding in findings if finding.category.category == category
    )


def _stage_validate_report_assembly(
    context: ValidateRunContext,
    validation_result: ValidationResult,
    possession_assessment: PossessionAssessmentRecord,
    redaction_review: RedactionReview,
    recommendation_id: str,
) -> ValidateReport:
    """Stage 6 — assemble eleven-section ValidateReport."""
    findings = validation_result.findings
    snapshot = context.snapshot
    identity = snapshot.identity
    summary = validation_result.summary
    report_id = _build_stable_id("report", identity.snapshot_id, context.validated_at)

    blocker_findings = tuple(
        finding
        for finding in findings
        if finding.severity.value == VALIDATION_SEVERITY_BLOCKER
    )
    warning_findings = tuple(
        finding
        for finding in findings
        if finding.severity.value == VALIDATION_SEVERITY_WARNING
    )

    downgrade = False
    target = context.target_certify_level
    certified = summary.certified_quality_level
    if target is not None and certified is not None and certified < target:
        downgrade = True

    report_summary = ValidateReportSummary(
        validation_status=summary.status.value,
        result_ref=validation_result.result_id,
        snapshot_id=identity.snapshot_id,
        finding_count=summary.finding_count,
        blocker_count=summary.blocker_count,
        warning_count=summary.warning_count,
        r2_precondition_pass=context.preconditions.r2_structural_pass,
        r3_precondition_pass=context.preconditions.r3_assembly_pass,
        target_certify_level=target,
        certified_quality_level=certified,
        downgrade_indicator=downgrade,
        recommendation_ref=recommendation_id,
    )

    quality_notes = (
        f"Certified quality level: {certified if certified is not None else 'none'}. "
        "R3 candidate L0 placeholder ≠ R5 certified L0 (VB-R3-06)."
    )
    redaction_notes = (
        f"Redaction status: {redaction_review.summary.status.value}. "
        f"Blocked count: {redaction_review.summary.blocked_count}."
    )
    readiness_notes = (
        "Publish Eligibility Recommendation reference only — not Publish. "
        f"Recommendation id: {recommendation_id}."
    )

    return ValidateReport(
        report_id=report_id,
        result_ref=validation_result.result_id,
        generated_at=context.validated_at,
        target_certify_level=target,
        summary=report_summary,
        identity_review=_build_category_section(
            VALIDATE_REPORT_SECTION_IDENTITY,
            FINDING_CATEGORY_IDENTITY,
            "Identity Review",
            _findings_for_category(findings, FINDING_CATEGORY_IDENTITY),
        ),
        structure_review=_build_category_section(
            VALIDATE_REPORT_SECTION_STRUCTURE,
            FINDING_CATEGORY_STRUCTURE,
            "Structure Review",
            _findings_for_category(findings, FINDING_CATEGORY_STRUCTURE),
        ),
        possession_review=_build_category_section(
            VALIDATE_REPORT_SECTION_POSSESSION,
            FINDING_CATEGORY_POSSESSION,
            "Possession Review",
            _findings_for_category(findings, FINDING_CATEGORY_POSSESSION),
            notes=possession_assessment.summary,
        ),
        quality_assessment=_build_category_section(
            VALIDATE_REPORT_SECTION_QUALITY,
            FINDING_CATEGORY_QUALITY,
            "Quality Assessment",
            _findings_for_category(findings, FINDING_CATEGORY_QUALITY),
            notes=quality_notes,
        ),
        redaction_review=_build_category_section(
            VALIDATE_REPORT_SECTION_REDACTION,
            FINDING_CATEGORY_REDACTION,
            "Redaction Review",
            _findings_for_category(findings, FINDING_CATEGORY_REDACTION),
            notes=redaction_notes,
        ),
        readiness_review=_build_category_section(
            VALIDATE_REPORT_SECTION_READINESS,
            FINDING_CATEGORY_READINESS,
            "Readiness Review",
            _findings_for_category(findings, FINDING_CATEGORY_READINESS),
            notes=readiness_notes,
        ),
        consistency_review=_build_category_section(
            VALIDATE_REPORT_SECTION_CONSISTENCY,
            FINDING_CATEGORY_CONSISTENCY,
            "Consistency Review",
            _findings_for_category(findings, FINDING_CATEGORY_CONSISTENCY),
        ),
        blockers=_build_category_section(
            VALIDATE_REPORT_SECTION_BLOCKERS,
            "blockers",
            "Blockers",
            blocker_findings,
        ),
        warnings=_build_category_section(
            VALIDATE_REPORT_SECTION_WARNINGS,
            "warnings",
            "Warnings",
            warning_findings,
        ),
        audit_trail=ValidateReportAudit(
            report_id=report_id,
            result_ref=validation_result.result_id,
            validated_at=context.validated_at,
            validated_snapshot_id=identity.snapshot_id,
            validator_version=VALIDATOR_VERSION,
            contract_ref=context.contract_ref,
            operator_ref=context.operator_ref,
            acquisition_id=identity.acquisition_id,
        ),
        boundary_declaration=VALIDATE_REPORT_BOUNDARY_DECLARATION,
    )


def _stage_publish_recommendation_assembly(
    context: ValidateRunContext,
    validation_result: ValidationResult,
    validate_report: ValidateReport,
    recommendation_id: str,
) -> PublishEligibilityRecommendation:
    """Stage 7 — assemble advisory PublishEligibilityRecommendation."""
    status_value = validation_result.summary.status.value
    publish_state = _publish_state_for_status(status_value)
    snapshot_id = context.snapshot.identity.snapshot_id

    blockers = tuple(
        f"{finding.category.category}: {finding.title}"
        for finding in validation_result.findings
        if finding.severity.value == VALIDATION_SEVERITY_BLOCKER
    )
    notes = tuple(
        f"{finding.category.category}: {finding.title}"
        for finding in validation_result.findings
        if finding.severity.value == VALIDATION_SEVERITY_WARNING
    )

    required_actions: tuple[str, ...] = ()
    if publish_state == PUBLISH_ELIGIBILITY_NOT_ELIGIBLE:
        required_actions = ("Review blockers and re-Validate after remediation.",)
    elif publish_state == PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES:
        required_actions = ("Review warnings before Publish consideration.",)
    else:
        required_actions = ("Operator HITL review mandatory before R4 Publish.",)

    if publish_state == PUBLISH_ELIGIBILITY_NOT_ELIGIBLE:
        summary = "NOT ELIGIBLE — mandatory blockers or precondition failures recorded."
    elif publish_state == PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES:
        summary = "ELIGIBLE WITH NOTES — Publish consideration allowed with operator review."
    else:
        summary = "ELIGIBLE — no mandatory blockers; operator HITL still required."

    return PublishEligibilityRecommendation(
        recommendation_id=recommendation_id,
        recommendation_state=publish_state,
        summary=summary,
        blocking_reasons=blockers,
        notes=notes,
        required_operator_actions=required_actions,
        validation_result_ref=validation_result.result_id,
        validate_report_ref=validate_report.report_id,
        derived_from_status=status_value,
        snapshot_id=snapshot_id,
        generated_at=context.validated_at,
        boundary_declaration=PUBLISH_ELIGIBILITY_BOUNDARY_DECLARATION,
    )


def run_validate(
    snapshot: SnapshotPackage | None,
    *,
    target_certify_level: int | None = None,
    operator_ref: str = "operator:unknown",
    validated_at: str | None = None,
    contract_ref: str = SNAPSHOT_CONTRACT,
    r2_structural_pass: bool | None = None,
    r3_assembly_pass: bool | None = None,
) -> ValidateEngineOutput:
    """Run R5 Validate Engine skeleton — seven stages; mock assessors only.

    Does not publish, mutate snapshot/evidence/quarantine, perform R2/R3 validation,
    or write to filesystem. Raises ValueError when candidate snapshot is absent.
    """
    if snapshot is None:
        raise ValueError("Candidate Snapshot Package is required (VE-I-01)")

    timestamp = validated_at or _utc_now_iso()
    preconditions = _stage_preconditions(
        snapshot,
        target_certify_level=target_certify_level,
        r2_structural_pass=r2_structural_pass,
        r3_assembly_pass=r3_assembly_pass,
    )

    run_context = ValidateRunContext(
        snapshot=snapshot,
        target_certify_level=target_certify_level,
        operator_ref=operator_ref,
        validated_at=timestamp,
        contract_ref=contract_ref,
        r2_structural_pass=r2_structural_pass,
        r3_assembly_pass=r3_assembly_pass,
        preconditions=preconditions,
    )

    category_findings = _stage_category_evaluation(run_context)
    possession_assessment = _stage_quality_assessment(run_context, category_findings)
    redaction_review = _stage_redaction_review(run_context)
    validation_result = _stage_outcome_aggregation(
        run_context,
        category_findings,
        possession_assessment,
        redaction_review,
    )

    recommendation_id = _build_stable_id(
        "recommendation",
        snapshot.identity.snapshot_id,
        timestamp,
    )
    validate_report = _stage_validate_report_assembly(
        run_context,
        validation_result,
        possession_assessment,
        redaction_review,
        recommendation_id,
    )
    publish_recommendation = _stage_publish_recommendation_assembly(
        run_context,
        validation_result,
        validate_report,
        recommendation_id,
    )

    return ValidateEngineOutput(
        validation_result=validation_result,
        validate_report=validate_report,
        publish_eligibility_recommendation=publish_recommendation,
        redaction_review=redaction_review,
        possession_assessment=possession_assessment,
    )
