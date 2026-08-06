"""Build and validate ``mars.client_ops.report`` v1 envelopes."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from .constants import (
    ENVIRONMENT_DEFAULT,
    EVENT_TYPE,
    PRODUCER_NAME,
    PRODUCER_VERSION,
    SCHEMA_NAME,
    SCHEMA_VERSION,
    SITE_DOMAIN,
    SITE_ID,
    SITE_NAME,
)
from .delivery_eligibility import FRESH_AND_ELIGIBLE
from .errors import ProcessResult, ValidationIssue
from .event_identity import compute_event_id
from .models import FixtureMeta, to_utc_z
from .security_validator import validate_envelope_security


REQUIRED_TOP_LEVEL = (
    "schema_name",
    "schema_version",
    "event_id",
    "event_type",
    "generated_at",
    "observed_at",
    "environment",
    "site",
    "producer",
    "run",
    "action",
    "metrics",
    "freshness",
    "security",
)


def can_build_distributable_envelope(result: ProcessResult) -> bool:
    """Contract requires integer metrics; only build when trusted and complete."""
    if result.observed_at is None or result.age_seconds is None:
        return False
    if not result.run_id:
        return False
    if not result.metrics_trusted or result.metrics is None:
        return False
    for key in (
        "baseline_count",
        "current_count",
        "added_urls",
        "removed_urls",
        "onboarding_needed_count",
    ):
        val = result.metrics.get(key)
        if not isinstance(val, int) or isinstance(val, bool):
            return False
    return True


def build_envelope(
    result: ProcessResult,
    *,
    generated_at: Optional[datetime] = None,
    meta: Optional[FixtureMeta] = None,
    environment: str = ENVIRONMENT_DEFAULT,
) -> tuple[Optional[dict[str, Any]], list[ValidationIssue]]:
    """Construct envelope from a ProcessResult when contract-complete.

    Returns ``(None, issues)`` when metrics/time/run_id prevent a valid
    distributable envelope under the frozen integer-only metrics contract.
    """
    meta = meta or FixtureMeta()
    issues: list[ValidationIssue] = []

    if not can_build_distributable_envelope(result):
        issues.append(
            ValidationIssue(
                code="SOURCE_REQUIRED_FIELD_MISSING",
                message=(
                    "cannot build distributable envelope: incomplete or "
                    "untrusted metrics/time (contract requires integers)"
                ),
            )
        )
        return None, issues

    assert result.metrics is not None
    assert result.observed_at is not None
    assert result.age_seconds is not None

    if generated_at is not None:
        gen = generated_at
    elif meta.generated_at is not None:
        gen = meta.generated_at
    else:
        gen = datetime.now(timezone.utc)
    if gen.tzinfo is None:
        gen = gen.replace(tzinfo=timezone.utc)
    else:
        gen = gen.astimezone(timezone.utc)

    metrics_int = {
        "baseline_count": int(result.metrics["baseline_count"]),  # type: ignore[arg-type]
        "current_count": int(result.metrics["current_count"]),  # type: ignore[arg-type]
        "added_urls": int(result.metrics["added_urls"]),  # type: ignore[arg-type]
        "removed_urls": int(result.metrics["removed_urls"]),  # type: ignore[arg-type]
        "onboarding_needed_count": int(
            result.metrics["onboarding_needed_count"]
        ),  # type: ignore[arg-type]
    }

    event_id = compute_event_id(
        site_id=SITE_ID,
        event_type=EVENT_TYPE,
        run_id=result.run_id,
        observed_at=result.observed_at,
        normalized_status=result.normalized_status,
        summary_code=result.summary_code,
        metrics=metrics_int,
        reason_codes=result.reason_codes,
        action_code=result.action_code,
    )

    envelope: dict[str, Any] = {
        "schema_name": SCHEMA_NAME,
        "schema_version": SCHEMA_VERSION,
        "event_id": event_id,
        "event_type": EVENT_TYPE,
        "generated_at": to_utc_z(gen),
        "observed_at": result.observed_at,
        "environment": environment,
        "site": {
            "site_id": SITE_ID,
            "site_name": SITE_NAME,
            "domain": SITE_DOMAIN,
        },
        "producer": {
            "name": PRODUCER_NAME,
            "version": PRODUCER_VERSION,
        },
        "run": {
            "run_id": result.run_id,
            "source_status": result.source_status,
            "normalized_status": result.normalized_status,
            "summary_code": result.summary_code,
            "reason_codes": list(result.reason_codes),
        },
        "action": {
            "required": bool(result.action_required),
            "code": result.action_code,
            "text": result.action_text,
        },
        "metrics": metrics_int,
        "freshness": {
            "age_seconds": int(result.age_seconds),
            "stale": bool(result.stale),
        },
        "security": {
            "classification": "internal",
            "contains_secrets": False,
            "redacted": True,
        },
    }

    shape_issues = validate_envelope_shape(envelope)
    issues.extend(shape_issues)
    if shape_issues:
        return None, issues

    return envelope, issues


def validate_envelope_shape(envelope: dict[str, Any]) -> list[ValidationIssue]:
    """Validate required Phase 0A shape (no routing/delivery/AI)."""
    issues: list[ValidationIssue] = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in envelope:
            issues.append(
                ValidationIssue(
                    code="SOURCE_REQUIRED_FIELD_MISSING",
                    message="required envelope field missing",
                    field=key,
                )
            )

    forbidden = {
        "delivery",
        "ai",
        "routing",
        "telegram",
        "chat_id",
        "bot_token",
        "webhook",
    }
    for key in forbidden:
        if key in envelope:
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_SECRET_MARKER_DETECTED",
                    message="forbidden top-level field",
                    field=key,
                )
            )

    if envelope.get("schema_name") != SCHEMA_NAME:
        issues.append(
            ValidationIssue(
                code="UNSUPPORTED_SOURCE_VOCABULARY",
                message="schema_name mismatch",
                field="schema_name",
            )
        )

    metrics = envelope.get("metrics")
    if isinstance(metrics, dict):
        for mkey in (
            "baseline_count",
            "current_count",
            "added_urls",
            "removed_urls",
            "onboarding_needed_count",
        ):
            val = metrics.get(mkey)
            if not isinstance(val, int) or isinstance(val, bool):
                issues.append(
                    ValidationIssue(
                        code="SOURCE_REQUIRED_FIELD_MISSING",
                        message="metric must be integer",
                        field=f"metrics.{mkey}",
                    )
                )

    return issues


def attach_envelope_with_security(
    result: ProcessResult,
    *,
    generated_at: Optional[datetime] = None,
    meta: Optional[FixtureMeta] = None,
) -> ProcessResult:
    """Build envelope, run security validation, update ProcessResult."""
    envelope, build_issues = build_envelope(
        result, generated_at=generated_at, meta=meta
    )
    result.issues.extend(build_issues)

    if envelope is None:
        result.distributable = False
        result.envelope = None
        # Keep prior blocked/failed status; mark non-distributable.
        return result

    # Apply optional fixture action override into envelope before security.
    if meta and meta.action_text_override:
        envelope = dict(envelope)
        action = dict(envelope["action"])
        action["text"] = meta.action_text_override
        envelope["action"] = action
        result.action_text = meta.action_text_override

    sec_issues = validate_envelope_security(envelope)
    if sec_issues:
        result.security_rejected = True
        result.distributable = False
        result.envelope = None
        result.ok = False
        result.normalized_status = "BLOCKED"
        result.summary_code = "ENVELOPE_SECURITY_REJECTED"
        result.action_code = "REVIEW_ENVELOPE_SECURITY"
        result.action_required = True
        result.action_text = (
            "конверт отклонён проверкой безопасности — не публиковать"
        )
        result.reason_codes = sorted({i.code for i in sec_issues})
        result.issues.extend(sec_issues)
        result.source_status = "ENVELOPE_SECURITY_REJECTED"
        result.delivery_eligibility = "NOT_SAFE_TO_SEND"
        result.freshness_reason = "ENVELOPE_SECURITY_REJECTED"
        return result

    # D6F1B: promote action.text to full Russian operator Telegram body.
    try:
        from .telegram_operator_message import apply_operator_message_to_envelope

        envelope = apply_operator_message_to_envelope(envelope)
        result.action_text = str((envelope.get("action") or {}).get("text") or result.action_text)
    except Exception:
        # Formatter must not block envelope identity; n8n fallback still formats.
        pass

    # Keep envelope for identity/preview even when stale; customer delivery
    # requires FRESH_AND_ELIGIBLE (D6B). Age does not enter event_id material.
    result.envelope = envelope
    if (
        result.delivery_eligibility == FRESH_AND_ELIGIBLE
        and result.normalized_status != "BLOCKED"
        and not result.security_rejected
    ):
        result.distributable = True
    else:
        result.distributable = False
    return result
