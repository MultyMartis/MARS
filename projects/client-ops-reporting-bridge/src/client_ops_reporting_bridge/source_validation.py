"""Source artifact field validation (fail closed, no silent zeros)."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from .artifact_loader import extract_aliased, has_aliased_key
from .constants import (
    CHANGED_SUMMARY_ALIASES,
    MONITOR_CLASSIFICATION_ALIASES,
    RUN_SUMMARY_ALIASES,
)
from .errors import ValidationIssue
from .models import ParsedArtifacts, SourceMetrics


def _reject_bool_as_int(value: Any, field: str, artifact: str) -> Optional[ValidationIssue]:
    if isinstance(value, bool):
        return ValidationIssue(
            code="SOURCE_REQUIRED_FIELD_MISSING",
            message="boolean is not accepted as integer metric",
            artifact=artifact,
            field=field,
        )
    return None


def require_non_negative_int(
    value: Any,
    *,
    field: str,
    artifact: str,
) -> tuple[Optional[int], list[ValidationIssue]]:
    """Validate an integer metric; never coerce missing to zero."""
    issues: list[ValidationIssue] = []
    bool_issue = _reject_bool_as_int(value, field, artifact)
    if bool_issue is not None:
        return None, [bool_issue]
    if not isinstance(value, int):
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_FIELD_MISSING",
                message="metric must be an integer",
                artifact=artifact,
                field=field,
            )
        )
        return None, issues
    if value < 0:
        issues.append(
            ValidationIssue(
                code="SOURCE_METRIC_NEGATIVE",
                message="metric must be >= 0",
                artifact=artifact,
                field=field,
            )
        )
        return None, issues
    return value, issues


def parse_timestamp(value: Any) -> tuple[Optional[datetime], Optional[ValidationIssue]]:
    """Parse ISO-8601 timestamp to aware UTC datetime."""
    if not isinstance(value, str) or not value.strip():
        return None, ValidationIssue(
            code="OBSERVED_AT_UNPARSEABLE",
            message="timestamp missing or not a string",
        )
    text = value.strip()
    try:
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None, ValidationIssue(
            code="OBSERVED_AT_UNPARSEABLE",
            message="timestamp not parseable as ISO-8601",
        )
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc), None


def validate_required_presence(
    artifacts: ParsedArtifacts,
) -> list[ValidationIssue]:
    """Validate required files present and parseable."""
    issues: list[ValidationIssue] = []
    for name in artifacts.missing:
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_ARTIFACT_MISSING",
                message="required artifact missing",
                artifact=name,
            )
        )
    for name in artifacts.malformed:
        issues.append(
            ValidationIssue(
                code="SOURCE_JSON_MALFORMED",
                message="required artifact JSON malformed",
                artifact=name,
            )
        )
    return issues


def extract_metrics(artifacts: ParsedArtifacts) -> tuple[SourceMetrics, list[ValidationIssue]]:
    """Extract metrics with alias mapping; fail closed on absence."""
    issues: list[ValidationIssue] = []
    metrics = SourceMetrics()
    changed = artifacts.changed_summary
    monitor = artifacts.monitor_classification
    run = artifacts.run_summary

    if changed is None:
        return metrics, issues

    for logical in (
        "baseline_count",
        "current_count",
        "added_urls",
        "removed_urls",
    ):
        if not has_aliased_key(changed, CHANGED_SUMMARY_ALIASES, logical):
            issues.append(
                ValidationIssue(
                    code="SOURCE_REQUIRED_FIELD_MISSING",
                    message="required metric field missing",
                    artifact="changed-summary.json",
                    field=logical,
                )
            )
            continue
        raw = extract_aliased(changed, CHANGED_SUMMARY_ALIASES, logical)
        value, field_issues = require_non_negative_int(
            raw, field=logical, artifact="changed-summary.json"
        )
        issues.extend(field_issues)
        setattr(metrics, logical, value)

    # Onboarding: prefer monitor-classification, else changed-summary, else run.
    onboarding_raw: Any = None
    onboarding_artifact = "monitor-classification.json"
    if monitor is not None and has_aliased_key(
        monitor, MONITOR_CLASSIFICATION_ALIASES, "onboarding_needs_count"
    ):
        onboarding_raw = extract_aliased(
            monitor, MONITOR_CLASSIFICATION_ALIASES, "onboarding_needs_count"
        )
    elif has_aliased_key(
        changed, CHANGED_SUMMARY_ALIASES, "onboarding_needs_count"
    ):
        onboarding_artifact = "changed-summary.json"
        onboarding_raw = extract_aliased(
            changed, CHANGED_SUMMARY_ALIASES, "onboarding_needs_count"
        )
    elif run is not None and has_aliased_key(
        run, RUN_SUMMARY_ALIASES, "onboarding_needs_count"
    ):
        onboarding_artifact = "run-summary.json"
        onboarding_raw = extract_aliased(
            run, RUN_SUMMARY_ALIASES, "onboarding_needs_count"
        )
    else:
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_FIELD_MISSING",
                message="onboarding_needs_count missing from authorities",
                field="onboarding_needs_count",
            )
        )
        return metrics, issues

    value, field_issues = require_non_negative_int(
        onboarding_raw,
        field="onboarding_needs_count",
        artifact=onboarding_artifact,
    )
    issues.extend(field_issues)
    metrics.onboarding_needed_count = value
    return metrics, issues


def extract_monitor_classification(
    artifacts: ParsedArtifacts,
) -> tuple[Optional[str], list[ValidationIssue]]:
    issues: list[ValidationIssue] = []
    monitor = artifacts.monitor_classification
    if monitor is None:
        return None, issues
    if not has_aliased_key(
        monitor, MONITOR_CLASSIFICATION_ALIASES, "classification"
    ):
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_FIELD_MISSING",
                message="classification missing",
                artifact="monitor-classification.json",
                field="classification",
            )
        )
        return None, issues
    raw = extract_aliased(
        monitor, MONITOR_CLASSIFICATION_ALIASES, "classification"
    )
    if not isinstance(raw, str) or not raw.strip():
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_FIELD_MISSING",
                message="classification must be a non-empty string",
                artifact="monitor-classification.json",
                field="classification",
            )
        )
        return None, issues
    return raw.strip(), issues


def extract_run_fields(
    artifacts: ParsedArtifacts,
) -> tuple[dict[str, Any], list[ValidationIssue]]:
    """Extract run-summary execution metadata."""
    issues: list[ValidationIssue] = []
    out: dict[str, Any] = {
        "classification": None,
        "run_id": None,
        "started_at": None,
        "finished_at": None,
        "exit_code": None,
        "duration_seconds": None,
        "added_count": None,
        "onboarding_needs_count": None,
    }
    run = artifacts.run_summary
    if run is None:
        return out, issues

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "classification"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "classification")
        if isinstance(raw, str) and raw.strip():
            out["classification"] = raw.strip()

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "run_id"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "run_id")
        if isinstance(raw, str) and raw.strip():
            out["run_id"] = raw.strip()
        else:
            issues.append(
                ValidationIssue(
                    code="SOURCE_REQUIRED_FIELD_MISSING",
                    message="run_id invalid",
                    artifact="run-summary.json",
                    field="run_id",
                )
            )
    else:
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_FIELD_MISSING",
                message="run_id missing",
                artifact="run-summary.json",
                field="run_id",
            )
        )

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "finished_at"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "finished_at")
        dt, issue = parse_timestamp(raw)
        if issue is not None:
            issues.append(issue)
        else:
            out["finished_at"] = dt

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "started_at"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "started_at")
        dt, issue = parse_timestamp(raw)
        if issue is None:
            out["started_at"] = dt

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "exit_code"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "exit_code")
        bool_issue = _reject_bool_as_int(raw, "exit_code", "run-summary.json")
        if bool_issue is not None:
            issues.append(bool_issue)
        elif isinstance(raw, int):
            out["exit_code"] = raw
        else:
            issues.append(
                ValidationIssue(
                    code="SOURCE_REQUIRED_FIELD_MISSING",
                    message="exit_code must be integer",
                    artifact="run-summary.json",
                    field="exit_code",
                )
            )

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "duration_seconds"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "duration_seconds")
        if isinstance(raw, int) and not isinstance(raw, bool):
            out["duration_seconds"] = raw

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "added_count"):
        raw = extract_aliased(run, RUN_SUMMARY_ALIASES, "added_count")
        value, field_issues = require_non_negative_int(
            raw, field="added_count", artifact="run-summary.json"
        )
        issues.extend(field_issues)
        out["added_count"] = value

    if has_aliased_key(run, RUN_SUMMARY_ALIASES, "onboarding_needs_count"):
        raw = extract_aliased(
            run, RUN_SUMMARY_ALIASES, "onboarding_needs_count"
        )
        value, field_issues = require_non_negative_int(
            raw, field="onboarding_needs_count", artifact="run-summary.json"
        )
        issues.extend(field_issues)
        out["onboarding_needs_count"] = value

    return out, issues


def detect_duplicate_metric_conflicts(
    artifacts: ParsedArtifacts,
    metrics: SourceMetrics,
) -> list[ValidationIssue]:
    """Detect same metric with different values across machine-readable sources."""
    issues: list[ValidationIssue] = []
    changed = artifacts.changed_summary or {}
    run = artifacts.run_summary or {}
    monitor = artifacts.monitor_classification or {}

    # added_urls vs run-summary.added_count
    if metrics.added_urls is not None and has_aliased_key(
        run, RUN_SUMMARY_ALIASES, "added_count"
    ):
        run_added = extract_aliased(run, RUN_SUMMARY_ALIASES, "added_count")
        if isinstance(run_added, int) and not isinstance(run_added, bool):
            if run_added != metrics.added_urls:
                issues.append(
                    ValidationIssue(
                        code="SOURCE_METRIC_CONFLICT",
                        message="added count differs across sources",
                        field="added_urls",
                    )
                )

    # onboarding across monitor / changed / run when multiple present
    values: list[int] = []
    for doc, aliases, art in (
        (monitor, MONITOR_CLASSIFICATION_ALIASES, "monitor"),
        (changed, CHANGED_SUMMARY_ALIASES, "changed"),
        (run, RUN_SUMMARY_ALIASES, "run"),
    ):
        if doc and has_aliased_key(doc, aliases, "onboarding_needs_count"):
            raw = extract_aliased(doc, aliases, "onboarding_needs_count")
            if isinstance(raw, int) and not isinstance(raw, bool):
                values.append(raw)
    if len(set(values)) > 1:
        issues.append(
            ValidationIssue(
                code="SOURCE_METRIC_CONFLICT",
                message="onboarding count differs across sources",
                field="onboarding_needs_count",
            )
        )
    return issues
