"""EAR Runtime R4.7 Publish Engine — orchestration skeleton only.

Seven-stage Publish flow per R4.7 architecture. Mock gate verification only — no Store
adapter, no consumer registry, no persistence, no CLI integration, no filesystem writes.
Standard library only.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import Any

from shared.publish_eligibility_models import (
    PUBLISH_ELIGIBILITY_ELIGIBLE,
    PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES,
    PUBLISH_ELIGIBILITY_NOT_ELIGIBLE,
    PublishEligibilityRecommendation,
)
from shared.publish_metadata_models import (
    AUDIT_OUTCOME_BLOCKED,
    AUDIT_OUTCOME_DEFERRED,
    AUDIT_OUTCOME_GATE_SATISFIED,
    PublishMetadata,
)
from shared.publish_result_models import (
    PUBLISH_RESULT_BLOCKED,
    PUBLISH_RESULT_DEFERRED,
    PUBLISH_RESULT_REF_PUBLISH_METADATA,
    PUBLISH_RESULT_REF_PUBLISHED_SNAPSHOT,
    PUBLISH_RESULT_SUCCESS,
    PublishResult,
    PublishResultAudit,
    PublishResultReference,
    PublishResultSummary,
)
from shared.publish_state_models import PUBLISH_STATE_STORED_UNPUBLISHED
from shared.published_snapshot_models import (
    PUBLISH_STATE_PUBLISHED,
    QUALITY_CLAIM_STAGE_PUBLISHED,
    VISIBILITY_STATE_GRANTED,
    VISIBILITY_STATE_NONE,
    PublishedSnapshot,
    PublishedSnapshotConsumerVisibility,
    PublishedSnapshotIdentity,
    PublishedSnapshotMetadata,
    PublishedSnapshotPublication,
)
from shared.snapshot_package_models import (
    PARENT_CONTRACT,
    SNAPSHOT_CONTRACT,
    SnapshotPackage,
)
from shared.validate_report_models import ValidateReport
from shared.validation_result_models import (
    VALIDATION_STATUS_FAIL,
    VALIDATION_STATUS_PASS,
    VALIDATION_STATUS_PASS_WITH_NOTES,
    ValidationResult,
)

PUBLISHER_VERSION = "ear-publish-engine-skeleton-v1"

_ACCEPTABLE_VALIDATION_STATUSES: frozenset[str] = frozenset(
    {VALIDATION_STATUS_PASS, VALIDATION_STATUS_PASS_WITH_NOTES}
)
_ACCEPTABLE_ELIGIBILITY_STATES: frozenset[str] = frozenset(
    {PUBLISH_ELIGIBILITY_ELIGIBLE, PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES}
)


@dataclass(frozen=True)
class PreconditionContext:
    """Stage 1 precondition record — orchestration only."""

    snapshot_present: bool
    r5_bundle_present: bool
    snapshot_id_aligned: bool
    publish_state_pre_publish: bool
    store_placement_confirmed: bool
    hard_fail: bool
    defer: bool
    fail_reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class EligibilityContext:
    """Stage 2 eligibility verification record — consumption only."""

    validation_status_acceptable: bool
    recommendation_acceptable: bool
    validate_report_coherent: bool
    hard_fail: bool
    fail_reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class HitlContext:
    """Stage 3 Publish HITL verification record — operator decision only."""

    hitl_approved: bool
    approval_ref_present: bool
    consumer_target_declared: bool
    hard_fail: bool
    defer: bool
    fail_reasons: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class PublishRunContext:
    """Read-only Publish run inputs — no snapshot mutation."""

    snapshot: SnapshotPackage
    validation_result: ValidationResult
    validate_report: ValidateReport
    publish_eligibility: PublishEligibilityRecommendation
    hitl_approved: bool
    operator_publish_approval_ref: str
    consumer_target: str
    published_by: str
    published_at: str
    publish_reason: str
    current_publish_state: str
    store_placement_confirmed: bool
    validate_sign_off_ref: str
    store_placement_ref: str
    in_memory_path: bool
    preconditions: PreconditionContext
    eligibility: EligibilityContext | None = None
    hitl: HitlContext | None = None


@dataclass(frozen=True)
class PublishEngineOutput:
    """Authoritative R4 Publish output bundle per R4.7 PE-O-01–02."""

    publish_result: PublishResult
    published_snapshot: PublishedSnapshot | None = None
    publish_metadata: PublishMetadata | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "publish_result": self.publish_result.to_dict(),
            "published_snapshot": (
                self.published_snapshot.to_dict()
                if self.published_snapshot is not None
                else None
            ),
            "publish_metadata": (
                self.publish_metadata.to_dict()
                if self.publish_metadata is not None
                else None
            ),
        }


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _build_stable_id(prefix: str, snapshot_id: str, timestamp: str) -> str:
    safe_ts = timestamp.replace(":", "").replace("+", "")
    return f"{prefix}-{snapshot_id}-{safe_ts}"


def _is_mock_snapshot_id(snapshot_id: str) -> bool:
    return snapshot_id.startswith("snap-mock-")


def _verify_preconditions(
    snapshot: SnapshotPackage | None,
    *,
    validation_result: ValidationResult | None,
    validate_report: ValidateReport | None,
    publish_eligibility: PublishEligibilityRecommendation | None,
    current_publish_state: str,
    store_placement_confirmed: bool,
    in_memory_path: bool,
) -> PreconditionContext:
    """Stage 1 — entry gate; fail closed on hard precondition failures."""
    fail_reasons: list[str] = []
    defer = False

    if snapshot is None:
        fail_reasons.append("Validated Snapshot Package is required (PE-I-01)")

    if validation_result is None or publish_eligibility is None:
        fail_reasons.append("R5 bundle is required (PE-I-02, PE-I-04)")

    if validate_report is None:
        fail_reasons.append("ValidateReport is required when policy requires (PE-I-03)")

    snapshot_id = snapshot.identity.snapshot_id if snapshot is not None else ""
    if snapshot is not None and validation_result is not None:
        if validation_result.audit is not None:
            if validation_result.audit.validated_snapshot_id != snapshot_id:
                fail_reasons.append("ValidationResult snapshot_id mismatch (PE-I-06)")

    if snapshot is not None and publish_eligibility is not None:
        if publish_eligibility.snapshot_id and publish_eligibility.snapshot_id != snapshot_id:
            fail_reasons.append("PublishEligibilityRecommendation snapshot_id mismatch")

    if snapshot is not None and validate_report is not None:
        if validate_report.summary.snapshot_id != snapshot_id:
            fail_reasons.append("ValidateReport snapshot_id mismatch")

    if current_publish_state != PUBLISH_STATE_STORED_UNPUBLISHED:
        fail_reasons.append(
            f"publish_state must be {PUBLISH_STATE_STORED_UNPUBLISHED!r} before Publish"
        )

    if snapshot is not None and not in_memory_path:
        if _is_mock_snapshot_id(snapshot_id):
            fail_reasons.append("Mock snapshot_id rejected on production path (Stage 1)")

    if not store_placement_confirmed and not in_memory_path:
        defer = True
        fail_reasons.append("Store placement confirmation pending (PE-I-07)")

    hard_fail = bool(fail_reasons) and not defer
    return PreconditionContext(
        snapshot_present=snapshot is not None,
        r5_bundle_present=(
            validation_result is not None and publish_eligibility is not None
        ),
        snapshot_id_aligned=not any("mismatch" in reason for reason in fail_reasons),
        publish_state_pre_publish=current_publish_state == PUBLISH_STATE_STORED_UNPUBLISHED,
        store_placement_confirmed=store_placement_confirmed or in_memory_path,
        hard_fail=hard_fail,
        defer=defer and not hard_fail,
        fail_reasons=tuple(fail_reasons),
    )


def _verify_eligibility(
    context: PublishRunContext,
) -> EligibilityContext:
    """Stage 2 — consume R5 bundle; never re-Validate or emit recommendation."""
    fail_reasons: list[str] = []

    status = context.validation_result.summary.status.value
    recommendation_state = context.publish_eligibility.recommendation_state

    validation_acceptable = status in _ACCEPTABLE_VALIDATION_STATUSES
    recommendation_acceptable = recommendation_state in _ACCEPTABLE_ELIGIBILITY_STATES

    if status == VALIDATION_STATUS_FAIL:
        fail_reasons.append("ValidationResult FAIL blocks default Publish path (PE-MAP-R4-01)")

    if recommendation_state == PUBLISH_ELIGIBILITY_NOT_ELIGIBLE:
        fail_reasons.append(
            "PublishEligibilityRecommendation NOT_ELIGIBLE blocks default path (PE-MAP-R4-02)"
        )

    report_coherent = (
        context.validate_report.result_ref == context.validation_result.result_id
    )
    if not report_coherent:
        fail_reasons.append("ValidateReport result_ref incoherent with ValidationResult")

    if (
        context.publish_eligibility.validation_result_ref
        and context.publish_eligibility.validation_result_ref
        != context.validation_result.result_id
    ):
        fail_reasons.append("PublishEligibilityRecommendation validation_result_ref mismatch")

    return EligibilityContext(
        validation_status_acceptable=validation_acceptable,
        recommendation_acceptable=recommendation_acceptable,
        validate_report_coherent=report_coherent,
        hard_fail=bool(fail_reasons),
        fail_reasons=tuple(fail_reasons),
    )


def _verify_hitl(
    *,
    hitl_approved: bool,
    operator_publish_approval_ref: str,
    consumer_target: str,
    recommendation_state: str,
) -> HitlContext:
    """Stage 3 — Publish HITL only; distinct from Validate sign-off."""
    fail_reasons: list[str] = []
    defer = False
    hard_fail = False

    if not hitl_approved:
        defer = True
        fail_reasons.append("Operator Publish HITL approval pending (Stage 3)")

    if hitl_approved and not operator_publish_approval_ref:
        hard_fail = True
        fail_reasons.append("operator_publish_approval_ref required when approved")

    if not consumer_target:
        hard_fail = True
        fail_reasons.append("consumer_target declaration required (PE-I-09)")

    if recommendation_state == PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES and hitl_approved:
        pass  # acknowledgment recorded in notes at emission

    return HitlContext(
        hitl_approved=hitl_approved,
        approval_ref_present=bool(operator_publish_approval_ref),
        consumer_target_declared=bool(consumer_target),
        hard_fail=hard_fail,
        defer=defer and not hard_fail,
        fail_reasons=tuple(fail_reasons),
    )


def _build_published_snapshot(
    context: PublishRunContext,
    *,
    published_snapshot_ref: str,
) -> PublishedSnapshot:
    """Stage 4 — compose promotion aggregate; read-only snapshot citation only."""
    snapshot = context.snapshot
    identity = snapshot.identity
    certified_level = context.validation_result.summary.certified_quality_level
    frozen_level = certified_level if certified_level is not None else 0

    return PublishedSnapshot(
        identity=PublishedSnapshotIdentity(
            snapshot_id=identity.snapshot_id,
            acquisition_id=identity.acquisition_id,
            site_id=identity.site_id,
            snapshot_contract=identity.snapshot_contract,
            parent_contract=PARENT_CONTRACT,
        ),
        snapshot=snapshot,
        publish_metadata=PublishedSnapshotMetadata(
            published_at=context.published_at,
            published_by=context.published_by,
            consumer_target=context.consumer_target,
            frozen_package_quality_level=frozen_level,
            quality_claim_stage=QUALITY_CLAIM_STAGE_PUBLISHED,
        ),
        publication=PublishedSnapshotPublication(
            publish_state=PUBLISH_STATE_PUBLISHED,
            operator_publish_approval_ref=context.operator_publish_approval_ref,
            validation_result_ref=context.validation_result.result_id,
            store_placement_ref=context.store_placement_ref,
            publish_eligibility_at_gate=context.publish_eligibility.recommendation_id,
            published_snapshot_ref=published_snapshot_ref,
        ),
        consumer_visibility=PublishedSnapshotConsumerVisibility(
            consumer_target=context.consumer_target,
            visibility_state=VISIBILITY_STATE_NONE,
            visibility_granted_at="",
            intake_reference_key=identity.snapshot_id,
        ),
    )


def _attach_publish_metadata(
    context: PublishRunContext,
    published_snapshot: PublishedSnapshot,
    *,
    publish_audit_ref: str,
) -> tuple[PublishedSnapshot, PublishMetadata]:
    """Stage 5 — attach R4 publish metadata; freeze certified quality claim only."""
    metadata = PublishMetadata(
        snapshot_id=context.snapshot.identity.snapshot_id,
        published_at=context.published_at,
        published_by=context.published_by,
        consumer_target=context.consumer_target,
        publish_reason=context.publish_reason,
        publish_audit_ref=publish_audit_ref,
    )

    updated_snapshot = replace(
        published_snapshot,
        publish_metadata=PublishedSnapshotMetadata(
            published_at=metadata.published_at,
            published_by=metadata.published_by,
            consumer_target=metadata.consumer_target,
            frozen_package_quality_level=(
                published_snapshot.publish_metadata.frozen_package_quality_level
            ),
            quality_claim_stage=QUALITY_CLAIM_STAGE_PUBLISHED,
        ),
    )
    return updated_snapshot, metadata


def _grant_visibility(
    published_snapshot: PublishedSnapshot,
    *,
    granted_at: str,
) -> PublishedSnapshot:
    """Stage 6 — logical visibility grant; no consumer execution."""
    visibility = PublishedSnapshotConsumerVisibility(
        consumer_target=published_snapshot.consumer_visibility.consumer_target,
        visibility_state=VISIBILITY_STATE_GRANTED,
        visibility_granted_at=granted_at,
        intake_reference_key=published_snapshot.identity.snapshot_id,
    )
    return replace(published_snapshot, consumer_visibility=visibility)


def _resolve_result_state(
    *,
    preconditions: PreconditionContext,
    eligibility: EligibilityContext | None,
    hitl: HitlContext | None,
    promotion_complete: bool,
) -> tuple[str, int, tuple[str, ...]]:
    """Map gate outcomes to PublishResult state — fail closed."""
    notes: list[str] = []

    if preconditions.defer:
        return PUBLISH_RESULT_DEFERRED, 1, preconditions.fail_reasons

    if preconditions.hard_fail:
        return PUBLISH_RESULT_BLOCKED, 1, preconditions.fail_reasons

    if eligibility is None:
        return PUBLISH_RESULT_BLOCKED, 1, ("Eligibility verification not performed.",)

    if eligibility.hard_fail:
        return PUBLISH_RESULT_BLOCKED, 2, eligibility.fail_reasons

    if hitl is None:
        return PUBLISH_RESULT_BLOCKED, 2, ("HITL verification not performed.",)

    if hitl.defer:
        return PUBLISH_RESULT_DEFERRED, 3, hitl.fail_reasons

    if hitl.hard_fail:
        return PUBLISH_RESULT_BLOCKED, 3, hitl.fail_reasons

    if promotion_complete:
        notes.append("Promotion stages 4–6 completed (mock).")
        return PUBLISH_RESULT_SUCCESS, 7, tuple(notes)

    return PUBLISH_RESULT_BLOCKED, 6, ("Promotion incomplete.",)


def _emit_publish_result(
    context: PublishRunContext,
    *,
    result_state: str,
    last_stage: int,
    result_notes: tuple[str, ...],
    published_snapshot: PublishedSnapshot | None,
    publish_metadata: PublishMetadata | None,
    published_snapshot_ref_id: str | None,
    publish_metadata_ref_id: str | None,
) -> PublishResult:
    """Stage 7 — emit sole authoritative R4 Publish attempt outcome."""
    snapshot_id = context.snapshot.identity.snapshot_id
    timestamp = context.published_at

    if result_state == PUBLISH_RESULT_SUCCESS:
        statement = "Publish attempt completed — promotion executed (mock)."
        audit_outcome = AUDIT_OUTCOME_GATE_SATISFIED
    elif result_state == PUBLISH_RESULT_DEFERRED:
        statement = "Publish attempt deferred — preconditions or HITL pending."
        audit_outcome = AUDIT_OUTCOME_DEFERRED
    else:
        statement = "Publish attempt blocked — fail closed; no promotion executed."
        audit_outcome = AUDIT_OUTCOME_BLOCKED

    audit_id = _build_stable_id("publish-audit", snapshot_id, timestamp)
    publish_result_id = _build_stable_id("publish-result", snapshot_id, timestamp)

    gate_checklist = (
        f"stage_1_preconditions:{'pass' if not context.preconditions.hard_fail else 'fail'}",
        f"stage_2_eligibility:{'pass' if context.eligibility and not context.eligibility.hard_fail else 'pending'}",
        f"stage_3_hitl:{'pass' if context.hitl and context.hitl.hitl_approved else 'pending'}",
    )

    audit = PublishResultAudit(
        audit_id=audit_id,
        snapshot_id=snapshot_id,
        generated_at=timestamp,
        outcome=audit_outcome,
        operator_publish_approval_ref=context.operator_publish_approval_ref,
        validate_sign_off_ref=context.validate_sign_off_ref,
        validation_result_ref=context.validation_result.result_id,
        publish_recommendation_ref=context.publish_eligibility.recommendation_id,
        gate_checklist=gate_checklist,
        last_stage_evaluated=last_stage,
        notes="; ".join(result_notes),
    )

    published_ref: PublishResultReference | None = None
    metadata_ref: PublishResultReference | None = None
    if result_state == PUBLISH_RESULT_SUCCESS:
        if published_snapshot_ref_id is None or publish_metadata_ref_id is None:
            raise ValueError("SUCCESS requires output refs (PR-INV-R4-04)")
        published_ref = PublishResultReference(
            ref_id=published_snapshot_ref_id,
            ref_type=PUBLISH_RESULT_REF_PUBLISHED_SNAPSHOT,
            snapshot_id=snapshot_id,
        )
        metadata_ref = PublishResultReference(
            ref_id=publish_metadata_ref_id,
            ref_type=PUBLISH_RESULT_REF_PUBLISH_METADATA,
            snapshot_id=snapshot_id,
        )

    combined_notes = result_notes
    if (
        context.publish_eligibility.recommendation_state
        == PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES
        and result_state == PUBLISH_RESULT_SUCCESS
    ):
        combined_notes = combined_notes + ("ELIGIBLE_WITH_NOTES acknowledged at Publish.",)

    return PublishResult(
        publish_result_id=publish_result_id,
        publish_result_state=result_state,
        summary=PublishResultSummary(
            statement=statement,
            last_stage_evaluated=last_stage,
        ),
        validation_result_ref=context.validation_result.result_id,
        publish_recommendation_ref=context.publish_eligibility.recommendation_id,
        notes=combined_notes,
        audit_ref=audit.audit_id,
        published_snapshot_ref=published_ref,
        publish_metadata_ref=metadata_ref,
        snapshot_id=snapshot_id,
        generated_at=timestamp,
    )


def run_publish(
    snapshot: SnapshotPackage | None,
    *,
    validation_result: ValidationResult,
    validate_report: ValidateReport,
    publish_eligibility: PublishEligibilityRecommendation,
    hitl_approved: bool = False,
    operator_publish_approval_ref: str = "",
    consumer_target: str = "ocpilot",
    published_by: str = "operator:unknown",
    published_at: str | None = None,
    publish_reason: str = "Operator-approved validated snapshot promotion.",
    current_publish_state: str = PUBLISH_STATE_STORED_UNPUBLISHED,
    store_placement_confirmed: bool = True,
    validate_sign_off_ref: str = "",
    store_placement_ref: str = "",
    in_memory_path: bool = True,
) -> PublishEngineOutput:
    """Run R4 Publish Engine skeleton — seven stages; mock gate verification only.

    Does not validate, certify quality, perform R3 assembly, mutate snapshot content,
    write Store state, or write filesystem. Raises ValueError when snapshot is absent.
    """
    if snapshot is None:
        raise ValueError("Validated Snapshot Package is required (PE-I-01)")

    timestamp = published_at or _utc_now_iso()

    preconditions = _verify_preconditions(
        snapshot,
        validation_result=validation_result,
        validate_report=validate_report,
        publish_eligibility=publish_eligibility,
        current_publish_state=current_publish_state,
        store_placement_confirmed=store_placement_confirmed,
        in_memory_path=in_memory_path,
    )

    run_context = PublishRunContext(
        snapshot=snapshot,
        validation_result=validation_result,
        validate_report=validate_report,
        publish_eligibility=publish_eligibility,
        hitl_approved=hitl_approved,
        operator_publish_approval_ref=operator_publish_approval_ref,
        consumer_target=consumer_target,
        published_by=published_by,
        published_at=timestamp,
        publish_reason=publish_reason,
        current_publish_state=current_publish_state,
        store_placement_confirmed=store_placement_confirmed,
        validate_sign_off_ref=validate_sign_off_ref,
        store_placement_ref=store_placement_ref,
        in_memory_path=in_memory_path,
        preconditions=preconditions,
    )

    eligibility: EligibilityContext | None = None
    hitl: HitlContext | None = None
    published_snapshot: PublishedSnapshot | None = None
    publish_metadata: PublishMetadata | None = None
    published_snapshot_ref_id: str | None = None
    publish_metadata_ref_id: str | None = None
    promotion_complete = False

    if not preconditions.hard_fail and not preconditions.defer:
        eligibility = _verify_eligibility(run_context)
        run_context = replace(run_context, eligibility=eligibility)

        if not eligibility.hard_fail:
            hitl = _verify_hitl(
                hitl_approved=hitl_approved,
                operator_publish_approval_ref=operator_publish_approval_ref,
                consumer_target=consumer_target,
                recommendation_state=publish_eligibility.recommendation_state,
            )
            run_context = replace(run_context, hitl=hitl)

            if not hitl.hard_fail and not hitl.defer and hitl.hitl_approved:
                published_snapshot_ref_id = _build_stable_id(
                    "published-snapshot",
                    snapshot.identity.snapshot_id,
                    timestamp,
                )
                publish_metadata_ref_id = _build_stable_id(
                    "publish-metadata",
                    snapshot.identity.snapshot_id,
                    timestamp,
                )
                audit_ref = _build_stable_id(
                    "publish-audit",
                    snapshot.identity.snapshot_id,
                    timestamp,
                )

                published_snapshot = _build_published_snapshot(
                    run_context,
                    published_snapshot_ref=published_snapshot_ref_id,
                )
                published_snapshot, publish_metadata = _attach_publish_metadata(
                    run_context,
                    published_snapshot,
                    publish_audit_ref=audit_ref,
                )
                published_snapshot = _grant_visibility(
                    published_snapshot,
                    granted_at=timestamp,
                )
                promotion_complete = True

    result_state, last_stage, result_notes = _resolve_result_state(
        preconditions=preconditions,
        eligibility=eligibility,
        hitl=hitl,
        promotion_complete=promotion_complete,
    )

    publish_result = _emit_publish_result(
        run_context,
        result_state=result_state,
        last_stage=last_stage,
        result_notes=result_notes,
        published_snapshot=published_snapshot,
        publish_metadata=publish_metadata,
        published_snapshot_ref_id=published_snapshot_ref_id,
        publish_metadata_ref_id=publish_metadata_ref_id,
    )

    if result_state != PUBLISH_RESULT_SUCCESS:
        published_snapshot = None
        publish_metadata = None

    return PublishEngineOutput(
        publish_result=publish_result,
        published_snapshot=published_snapshot,
        publish_metadata=publish_metadata,
    )


# ---------------------------------------------------------------------------
# Implementation verification — smoke tests only; not a test suite.
# ---------------------------------------------------------------------------


def _minimal_snapshot(snapshot_id: str) -> SnapshotPackage:
    from shared.snapshot_package_models import (
        SnapshotAcquisitionLog,
        SnapshotDatabaseMetadata,
        SnapshotEnvironment,
        SnapshotExtensionInventory,
        SnapshotFileManifest,
        SnapshotIdentity,
        SnapshotMetadata,
        SnapshotOcmodInventory,
        SnapshotSafeUnknown,
        SnapshotSeoStructure,
        SnapshotThemeInfo,
    )

    return SnapshotPackage(
        identity=SnapshotIdentity(
            snapshot_id=snapshot_id,
            acquisition_id="acq-verify-001",
            site_id="site-verify-001",
            snapshot_contract=SNAPSHOT_CONTRACT,
        ),
        metadata=SnapshotMetadata(
            parent_contract=PARENT_CONTRACT,
            created_at="2026-06-07T00:00:00+00:00",
            ear_mode="pilot",
            operator_approval="approved",
            package_quality_level=0,
        ),
        environment=SnapshotEnvironment(environment_class="TEST"),
        file_manifest=SnapshotFileManifest(),
        theme_info=SnapshotThemeInfo(),
        extension_inventory=SnapshotExtensionInventory(),
        ocmod_inventory=SnapshotOcmodInventory(),
        database_metadata=SnapshotDatabaseMetadata(),
        seo_structure=SnapshotSeoStructure(),
        safe_unknown=SnapshotSafeUnknown(),
        acquisition_log=SnapshotAcquisitionLog(),
    )


def _minimal_r5_bundle(
    snapshot: SnapshotPackage,
    *,
    validation_status: str,
    recommendation_state: str,
) -> tuple[ValidationResult, ValidateReport, PublishEligibilityRecommendation]:
    from shared.validation_result_models import (
        ValidationAudit,
        ValidationRecommendation,
        ValidationStatus,
        ValidationSummary,
    )

    snapshot_id = snapshot.identity.snapshot_id
    timestamp = "2026-06-07T12:00:00+00:00"
    result_id = f"validate-{snapshot_id}-verify"
    report_id = f"report-{snapshot_id}-verify"
    recommendation_id = f"recommendation-{snapshot_id}-verify"

    certified_level = 0 if validation_status != VALIDATION_STATUS_FAIL else None

    validation_result = ValidationResult(
        result_id=result_id,
        summary=ValidationSummary(
            status=ValidationStatus(value=validation_status),
            finding_count=0,
            blocker_count=0,
            warning_count=0,
            certified_quality_level=certified_level,
        ),
        audit=ValidationAudit(
            validator_version="verify",
            validated_at=timestamp,
            validated_snapshot_id=snapshot_id,
            operator_ref="operator:verify",
            contract_ref=SNAPSHOT_CONTRACT,
        ),
    )

    from shared.validate_report_models import (
        VALIDATE_REPORT_SECTION_AUDIT,
        VALIDATE_REPORT_SECTION_BLOCKERS,
        VALIDATE_REPORT_SECTION_CONSISTENCY,
        VALIDATE_REPORT_SECTION_IDENTITY,
        VALIDATE_REPORT_SECTION_POSSESSION,
        VALIDATE_REPORT_SECTION_QUALITY,
        VALIDATE_REPORT_SECTION_READINESS,
        VALIDATE_REPORT_SECTION_REDACTION,
        VALIDATE_REPORT_SECTION_STRUCTURE,
        VALIDATE_REPORT_SECTION_WARNINGS,
        ValidateReportAudit,
        ValidateReportSection,
        ValidateReportSummary,
    )

    validate_report = ValidateReport(
        report_id=report_id,
        result_ref=result_id,
        generated_at=timestamp,
        summary=ValidateReportSummary(
            validation_status=validation_status,
            result_ref=result_id,
            snapshot_id=snapshot_id,
            finding_count=0,
            blocker_count=0,
            warning_count=0,
            certified_quality_level=certified_level,
            recommendation_ref=recommendation_id,
        ),
        identity_review=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_IDENTITY,
            category=VALIDATE_REPORT_SECTION_IDENTITY,
            title="Identity Review",
        ),
        structure_review=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_STRUCTURE,
            category=VALIDATE_REPORT_SECTION_STRUCTURE,
            title="Structure Review",
        ),
        possession_review=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_POSSESSION,
            category=VALIDATE_REPORT_SECTION_POSSESSION,
            title="Possession Review",
        ),
        quality_assessment=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_QUALITY,
            category=VALIDATE_REPORT_SECTION_QUALITY,
            title="Quality Assessment",
        ),
        redaction_review=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_REDACTION,
            category=VALIDATE_REPORT_SECTION_REDACTION,
            title="Redaction Review",
        ),
        readiness_review=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_READINESS,
            category=VALIDATE_REPORT_SECTION_READINESS,
            title="Readiness Review",
        ),
        consistency_review=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_CONSISTENCY,
            category=VALIDATE_REPORT_SECTION_CONSISTENCY,
            title="Consistency Review",
        ),
        blockers=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_BLOCKERS,
            category="blockers",
            title="Blockers",
        ),
        warnings=ValidateReportSection(
            section_id=VALIDATE_REPORT_SECTION_WARNINGS,
            category="warnings",
            title="Warnings",
        ),
        audit_trail=ValidateReportAudit(
            report_id=report_id,
            result_ref=result_id,
            validated_at=timestamp,
            validated_snapshot_id=snapshot_id,
            validator_version="verify",
            contract_ref=SNAPSHOT_CONTRACT,
            operator_ref="operator:verify",
        ),
    )

    publish_eligibility = PublishEligibilityRecommendation(
        recommendation_id=recommendation_id,
        recommendation_state=recommendation_state,
        summary="verification fixture",
        validation_result_ref=result_id,
        validate_report_ref=report_id,
        derived_from_status=validation_status,
        snapshot_id=snapshot_id,
        generated_at=timestamp,
    )

    return validation_result, validate_report, publish_eligibility


def _run_verification() -> None:
    snapshot = _minimal_snapshot("snap-verify-success-001")

    # SUCCESS path — PASS + ELIGIBLE + hitl_approved=True
    vr, report, rec = _minimal_r5_bundle(
        snapshot,
        validation_status=VALIDATION_STATUS_PASS,
        recommendation_state=PUBLISH_ELIGIBILITY_ELIGIBLE,
    )
    success_out = run_publish(
        snapshot,
        validation_result=vr,
        validate_report=report,
        publish_eligibility=rec,
        hitl_approved=True,
        operator_publish_approval_ref="hitl:publish-approve-001",
        published_at="2026-06-07T12:00:00+00:00",
    )
    assert success_out.publish_result.publish_result_state == PUBLISH_RESULT_SUCCESS
    assert success_out.publish_result.published_snapshot_ref is not None
    assert success_out.publish_result.publish_metadata_ref is not None
    assert success_out.published_snapshot is not None
    assert (
        success_out.published_snapshot.identity.snapshot_id
        == snapshot.identity.snapshot_id
    )
    assert success_out.published_snapshot.snapshot is snapshot

    # BLOCKED path — NOT_ELIGIBLE
    _, report_block, rec_block = _minimal_r5_bundle(
        snapshot,
        validation_status=VALIDATION_STATUS_PASS,
        recommendation_state=PUBLISH_ELIGIBILITY_NOT_ELIGIBLE,
    )
    blocked_out = run_publish(
        snapshot,
        validation_result=vr,
        validate_report=report_block,
        publish_eligibility=rec_block,
        hitl_approved=True,
        operator_publish_approval_ref="hitl:publish-approve-001",
        published_at="2026-06-07T12:01:00+00:00",
    )
    assert blocked_out.publish_result.publish_result_state == PUBLISH_RESULT_BLOCKED
    assert blocked_out.publish_result.published_snapshot_ref is None
    assert blocked_out.publish_result.publish_metadata_ref is None
    assert blocked_out.published_snapshot is None

    # DEFERRED path — hitl_approved=False
    deferred_out = run_publish(
        snapshot,
        validation_result=vr,
        validate_report=report,
        publish_eligibility=rec,
        hitl_approved=False,
        published_at="2026-06-07T12:02:00+00:00",
    )
    assert deferred_out.publish_result.publish_result_state == PUBLISH_RESULT_DEFERRED
    assert deferred_out.publish_result.published_snapshot_ref is None
    assert deferred_out.published_snapshot is None

    # PASS_WITH_NOTES + ELIGIBLE_WITH_NOTES + hitl_approved=True → SUCCESS
    vr_notes, report_notes, rec_notes = _minimal_r5_bundle(
        snapshot,
        validation_status=VALIDATION_STATUS_PASS_WITH_NOTES,
        recommendation_state=PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES,
    )
    notes_out = run_publish(
        snapshot,
        validation_result=vr_notes,
        validate_report=report_notes,
        publish_eligibility=rec_notes,
        hitl_approved=True,
        operator_publish_approval_ref="hitl:publish-approve-002",
        published_at="2026-06-07T12:03:00+00:00",
    )
    assert notes_out.publish_result.publish_result_state == PUBLISH_RESULT_SUCCESS

    print("ear_publish_engine verification: PASS (SUCCESS, BLOCKED, DEFERRED)")


if __name__ == "__main__":
    _run_verification()
