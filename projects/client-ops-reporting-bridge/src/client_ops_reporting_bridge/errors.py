"""Typed error and result types for the offline exporter core."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


class ExporterError(Exception):
    """Base error for offline exporter core."""


class UsageError(ExporterError):
    """CLI usage or configuration error."""


class UnsafeOutputPathError(ExporterError):
    """Output path is outside approved Phase 1A boundaries."""


class InternalExporterError(ExporterError):
    """Unexpected internal failure."""


@dataclass(frozen=True)
class ValidationIssue:
    """Sanitized validation issue (never carries raw secrets)."""

    code: str
    message: str
    artifact: Optional[str] = None
    field: Optional[str] = None


@dataclass
class ProcessResult:
    """Outcome of offline validate / normalize / build.

    When ``distributable`` is False, ``envelope`` must not be written as a
    publishable artifact (missing metrics, security rejection, etc.).
    """

    ok: bool
    normalized_status: str
    summary_code: str
    action_code: str
    action_required: bool
    reason_codes: list[str] = field(default_factory=list)
    action_text: str = ""
    source_status: str = ""
    run_id: str = ""
    observed_at: Optional[str] = None
    age_seconds: Optional[int] = None
    stale: bool = False
    # Phase 1B-D6B: evaluation-time delivery gate (not durable ledger state).
    delivery_eligibility: str = "NOT_SAFE_TO_SEND"
    freshness_threshold_seconds: Optional[int] = None
    freshness_reason: str = ""
    metrics: Optional[dict[str, Optional[int]]] = None
    metrics_trusted: bool = False
    envelope: Optional[dict[str, Any]] = None
    distributable: bool = False
    issues: list[ValidationIssue] = field(default_factory=list)
    simple_text: Optional[str] = None
    security_rejected: bool = False

    def to_sanitized_dict(self) -> dict[str, Any]:
        """Compact CLI/test diagnostics without secrets or paths."""
        return {
            "ok": self.ok,
            "normalized_status": self.normalized_status,
            "summary_code": self.summary_code,
            "action_code": self.action_code,
            "action_required": self.action_required,
            "reason_codes": list(self.reason_codes),
            "source_status": self.source_status,
            "run_id": self.run_id,
            "observed_at": self.observed_at,
            "age_seconds": self.age_seconds,
            "stale": self.stale,
            "delivery_eligibility": self.delivery_eligibility,
            "freshness_threshold_seconds": self.freshness_threshold_seconds,
            "freshness_reason": self.freshness_reason,
            "metrics_trusted": self.metrics_trusted,
            "distributable": self.distributable,
            "security_rejected": self.security_rejected,
            "issue_codes": [i.code for i in self.issues],
        }
