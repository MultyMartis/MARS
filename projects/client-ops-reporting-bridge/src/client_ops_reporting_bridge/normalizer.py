"""Deterministic normalization algorithm (Phase 1A offline)."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Callable, Optional

from .artifact_loader import extract_aliased, has_aliased_key
from .constants import (
    ACTION_TEXT,
    MAX_FUTURE_SKEW_SECONDS,
    MONITOR_CLASSIFICATION_ALIASES,
    STALE_AFTER_SECONDS,
    SUPPORTED_SOURCE_CLASSIFICATIONS,
)
from .errors import ProcessResult, ValidationIssue
from .models import FixtureMeta, ParsedArtifacts, SourceMetrics, to_utc_z
from .source_validation import (
    detect_duplicate_metric_conflicts,
    extract_metrics,
    extract_monitor_classification,
    extract_run_fields,
    parse_timestamp,
    validate_required_presence,
)

Clock = Callable[[], datetime]


def _blocked(
    *,
    summary_code: str,
    action_code: str,
    reason_codes: list[str],
    source_status: str = "",
    run_id: str = "",
    observed_at: Optional[str] = None,
    age_seconds: Optional[int] = None,
    stale: bool = False,
    metrics: Optional[SourceMetrics] = None,
    metrics_trusted: bool = False,
    issues: Optional[list[ValidationIssue]] = None,
    action_text_override: Optional[str] = None,
) -> ProcessResult:
    reasons = sorted(set(reason_codes))
    text = action_text_override or ACTION_TEXT.get(
        action_code, ACTION_TEXT["REVIEW_SOURCE_ARTIFACTS"]
    )
    return ProcessResult(
        ok=False,
        normalized_status="BLOCKED",
        summary_code=summary_code,
        action_code=action_code,
        action_required=True,
        reason_codes=reasons,
        action_text=text,
        source_status=source_status or summary_code,
        run_id=run_id,
        observed_at=observed_at,
        age_seconds=age_seconds,
        stale=stale,
        metrics=metrics.as_dict() if metrics else None,
        metrics_trusted=metrics_trusted,
        distributable=False,
        issues=list(issues or []),
    )


def _establish_observed_at(
    artifacts: ParsedArtifacts,
    run_fields: dict,
) -> tuple[Optional[datetime], list[ValidationIssue]]:
    issues: list[ValidationIssue] = []
    if run_fields.get("finished_at") is not None:
        return run_fields["finished_at"], issues

    monitor = artifacts.monitor_classification
    if monitor is not None and has_aliased_key(
        monitor, MONITOR_CLASSIFICATION_ALIASES, "observed_at"
    ):
        raw = extract_aliased(
            monitor, MONITOR_CLASSIFICATION_ALIASES, "observed_at"
        )
        dt, issue = parse_timestamp(raw)
        if issue is not None:
            issues.append(issue)
            return None, issues
        return dt, issues

    issues.append(
        ValidationIssue(
            code="OBSERVED_AT_UNPARSEABLE",
            message="no authoritative observed_at / finished_at",
        )
    )
    return None, issues


def normalize(
    artifacts: ParsedArtifacts,
    *,
    now_utc: Optional[datetime] = None,
    meta: Optional[FixtureMeta] = None,
    clock: Optional[Clock] = None,
) -> ProcessResult:
    """Normalize parsed artifacts into a ProcessResult.

    ``now_utc`` / ``meta.now_utc`` / ``clock`` provide injectable time.
    Machine clock is used only when no injectable value is provided.
    """
    meta = meta or FixtureMeta()
    if now_utc is not None:
        now = now_utc
    elif meta.now_utc is not None:
        now = meta.now_utc
    elif clock is not None:
        now = clock()
    else:
        now = datetime.now(timezone.utc)
    if now.tzinfo is None:
        now = now.replace(tzinfo=timezone.utc)
    else:
        now = now.astimezone(timezone.utc)

    override = meta.action_text_override

    presence_issues = validate_required_presence(artifacts)
    if artifacts.missing:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_MISSING",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=[
                "SOURCE_REQUIRED_ARTIFACT_MISSING",
                "REQUIRED_ARTIFACT_MISSING",
            ],
            issues=presence_issues,
            action_text_override=override,
        )
    if artifacts.malformed:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_MALFORMED",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=["SOURCE_JSON_MALFORMED", "JSON_PARSE_FAILED"],
            issues=presence_issues,
            action_text_override=override,
        )

    classification, class_issues = extract_monitor_classification(artifacts)
    run_fields, run_issues = extract_run_fields(artifacts)
    metrics, metric_issues = extract_metrics(artifacts)
    all_issues = class_issues + run_issues + metric_issues

    run_id = run_fields.get("run_id") or ""

    # Missing required fields → BLOCKED (no silent zeros)
    missing_field_codes = {
        i.code
        for i in all_issues
        if i.code
        in {
            "SOURCE_REQUIRED_FIELD_MISSING",
            "REQUIRED_FIELD_MISSING",
        }
    }
    if missing_field_codes or not metrics.all_core_present():
        # Distinguish missing baseline specifically
        summary = "SOURCE_ARTIFACT_MISSING"
        reasons = [
            "SOURCE_REQUIRED_FIELD_MISSING",
            "REQUIRED_FIELD_MISSING",
        ]
        return _blocked(
            summary_code=summary,
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=reasons,
            run_id=run_id,
            metrics=metrics,
            metrics_trusted=False,
            issues=all_issues,
            action_text_override=override,
        )

    negative = [i for i in all_issues if i.code in {"SOURCE_METRIC_NEGATIVE", "NEGATIVE_METRIC"}]
    if negative:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=["SOURCE_METRIC_NEGATIVE", "NEGATIVE_METRIC"],
            run_id=run_id,
            metrics=metrics,
            metrics_trusted=False,
            issues=all_issues,
            action_text_override=override,
        )

    observed_dt, obs_issues = _establish_observed_at(artifacts, run_fields)
    all_issues.extend(obs_issues)
    if observed_dt is None:
        return _blocked(
            summary_code="SOURCE_TIME_INVALID",
            action_code="REVIEW_SOURCE_TIME",
            reason_codes=["OBSERVED_AT_UNPARSEABLE", "SOURCE_TIME_IN_FUTURE"],
            run_id=run_id,
            metrics=metrics,
            metrics_trusted=False,
            issues=all_issues,
            action_text_override=override,
        )

    observed_at = to_utc_z(observed_dt)
    skew = (observed_dt - now).total_seconds()
    if skew > MAX_FUTURE_SKEW_SECONDS:
        age = int((now - observed_dt).total_seconds())
        return _blocked(
            summary_code="SOURCE_TIME_INVALID",
            action_code="REVIEW_SOURCE_TIME",
            reason_codes=["SOURCE_TIME_IN_FUTURE", "OBSERVED_AT_IN_FUTURE"],
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age if age >= 0 else None,
            metrics=metrics,
            metrics_trusted=metrics.all_core_present(),
            issues=all_issues,
            action_text_override=override,
        )

    age_seconds = int((now - observed_dt).total_seconds())
    if age_seconds < 0:
        return _blocked(
            summary_code="SOURCE_TIME_INVALID",
            action_code="REVIEW_SOURCE_TIME",
            reason_codes=["CLOCK_SKEW_NEGATIVE_AGE"],
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            metrics_trusted=False,
            issues=all_issues,
            action_text_override=override,
        )

    if age_seconds > STALE_AFTER_SECONDS:
        return _blocked(
            summary_code="SOURCE_REPORT_STALE",
            action_code="REVIEW_SCHEDULER_AND_ARTIFACTS",
            reason_codes=["SOURCE_REPORT_TOO_OLD", "SOURCE_STALE"],
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            stale=True,
            metrics=metrics,
            metrics_trusted=metrics.all_core_present(),
            issues=all_issues,
            action_text_override=override,
        )

    if classification is None:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_MISSING",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=["SOURCE_REQUIRED_FIELD_MISSING"],
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            issues=all_issues,
            action_text_override=override,
        )

    if classification not in SUPPORTED_SOURCE_CLASSIFICATIONS:
        return _blocked(
            summary_code="SOURCE_SCHEMA_UNSUPPORTED",
            action_code="REVIEW_SCHEMA_COMPATIBILITY",
            reason_codes=[
                "SOURCE_CLASSIFICATION_UNKNOWN",
                "UNSUPPORTED_SOURCE_VOCABULARY",
            ],
            source_status=classification,
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            metrics_trusted=metrics.all_core_present(),
            issues=all_issues,
            action_text_override=override,
        )

    # Metric equation when all four present
    b = metrics.baseline_count
    c = metrics.current_count
    a = metrics.added_urls
    r = metrics.removed_urls
    assert b is not None and c is not None and a is not None and r is not None
    if c != b + a - r:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=[
                "SOURCE_METRIC_CONFLICT",
                "METRIC_DELTA_INCONSISTENT",
            ],
            source_status=classification,
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            # Counts are present integers; conflict is logical, not missing.
            metrics_trusted=True,
            issues=all_issues,
            action_text_override=override,
        )

    dup_issues = detect_duplicate_metric_conflicts(artifacts, metrics)
    all_issues.extend(dup_issues)
    if dup_issues:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=["SOURCE_METRIC_CONFLICT"],
            source_status=classification,
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            metrics_trusted=True,
            issues=all_issues,
            action_text_override=override,
        )

    run_class = run_fields.get("classification")
    if run_class is not None and run_class != classification:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=[
                "SOURCE_CLASSIFICATION_CONFLICT",
                "CLASSIFICATION_MISMATCH",
                "RUN_SUMMARY_VS_MONITOR_CLASSIFICATION",
            ],
            source_status="SOURCE_ARTIFACT_CONFLICT",
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            metrics_trusted=True,
            issues=all_issues,
            action_text_override=override,
        )

    onboarding = metrics.onboarding_needed_count
    assert onboarding is not None
    if classification == "NO_ACTION_REQUIRED" and onboarding > 0:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=[
                "SOURCE_CLASSIFICATION_CONFLICT",
                "ONBOARDING_COUNT_CONFLICT",
            ],
            source_status="SOURCE_ARTIFACT_CONFLICT",
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            metrics_trusted=True,
            issues=all_issues,
            action_text_override=override,
        )
    if classification == "ONBOARDING_REQUIRED" and onboarding == 0:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=[
                "SOURCE_CLASSIFICATION_CONFLICT",
                "ONBOARDING_COUNT_CONFLICT",
            ],
            source_status="SOURCE_ARTIFACT_CONFLICT",
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            metrics_trusted=True,
            issues=all_issues,
            action_text_override=override,
        )

    # Execution failure
    exit_code = run_fields.get("exit_code")
    failed = classification == "FAILURE_REVIEW_REQUIRED" or (
        isinstance(exit_code, int) and exit_code != 0
    )
    if failed:
        reasons = ["SOURCE_EXIT_CODE_NONZERO", "MONITOR_EXECUTION_FAILED"]
        return ProcessResult(
            ok=False,
            normalized_status="FAILED",
            summary_code="SOURCE_EXECUTION_FAILED",
            action_code="REVIEW_SOURCE_FAILURE",
            action_required=True,
            reason_codes=sorted(set(reasons)),
            action_text=override
            or ACTION_TEXT["REVIEW_SOURCE_FAILURE"],
            source_status=classification,
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            stale=False,
            metrics=metrics.as_dict(),
            metrics_trusted=True,
            distributable=False,  # set true after envelope+security
            issues=all_issues,
        )

    reasons: list[str] = []
    if a == 0 and r == 0 and b == c:
        reasons.append("BASELINE_DELTA_ZERO")
    else:
        reasons.append("BASELINE_DELTA_NONZERO")

    if classification == "ONBOARDING_REQUIRED":
        reasons.extend(["ONBOARDING_COUNT_NONZERO", "CATEGORY_PLP_ADDED"])
        status = "ATTENTION"
        summary = "ONBOARDING_REQUIRED"
        action = "REVIEW_ONBOARDING"
    elif classification == "HYGIENE_REVIEW_REQUIRED":
        reasons.append("HYGIENE_FLAGS_PRESENT")
        status = "ATTENTION"
        summary = "HYGIENE_REVIEW_REQUIRED"
        action = "REVIEW_HYGIENE"
    elif classification == "NO_ACTION_REQUIRED":
        status = "OK"
        summary = "NO_ACTION_REQUIRED"
        action = "NONE"
    else:
        return _blocked(
            summary_code="SOURCE_ARTIFACT_CONFLICT",
            action_code="REVIEW_SOURCE_ARTIFACTS",
            reason_codes=["SOURCE_CLASSIFICATION_CONFLICT"],
            source_status=classification,
            run_id=run_id,
            observed_at=observed_at,
            age_seconds=age_seconds,
            metrics=metrics,
            issues=all_issues,
            action_text_override=override,
        )

    return ProcessResult(
        ok=status == "OK",
        normalized_status=status,
        summary_code=summary,
        action_code=action,
        action_required=action != "NONE",
        reason_codes=sorted(set(reasons)),
        action_text=override or ACTION_TEXT[action],
        source_status=classification,
        run_id=run_id,
        observed_at=observed_at,
        age_seconds=age_seconds,
        stale=False,
        metrics=metrics.as_dict(),
        metrics_trusted=True,
        distributable=False,
        issues=all_issues,
    )
