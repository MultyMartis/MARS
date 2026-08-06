"""Domain models for Phase 1A offline exporter core."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional


class NormalizedStatus(str, Enum):
    OK = "OK"
    ATTENTION = "ATTENTION"
    FAILED = "FAILED"
    BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class SiteIdentity:
    site_id: str
    site_name: str
    domain: str


@dataclass(frozen=True)
class ProducerIdentity:
    name: str
    version: str


@dataclass
class SourceMetrics:
    """Trusted metric bag. Absent values remain None (never silent-zero)."""

    baseline_count: Optional[int] = None
    current_count: Optional[int] = None
    added_urls: Optional[int] = None
    removed_urls: Optional[int] = None
    onboarding_needed_count: Optional[int] = None

    def all_core_present(self) -> bool:
        return all(
            v is not None
            for v in (
                self.baseline_count,
                self.current_count,
                self.added_urls,
                self.removed_urls,
                self.onboarding_needed_count,
            )
        )

    def as_dict(self) -> dict[str, Optional[int]]:
        return {
            "baseline_count": self.baseline_count,
            "current_count": self.current_count,
            "added_urls": self.added_urls,
            "removed_urls": self.removed_urls,
            "onboarding_needed_count": self.onboarding_needed_count,
        }

    def as_required_int_dict(self) -> dict[str, int]:
        if not self.all_core_present():
            raise ValueError("metrics incomplete; cannot coerce to integers")
        return {
            "baseline_count": int(self.baseline_count),  # type: ignore[arg-type]
            "current_count": int(self.current_count),  # type: ignore[arg-type]
            "added_urls": int(self.added_urls),  # type: ignore[arg-type]
            "removed_urls": int(self.removed_urls),  # type: ignore[arg-type]
            "onboarding_needed_count": int(
                self.onboarding_needed_count
            ),  # type: ignore[arg-type]
        }


@dataclass
class ParsedArtifacts:
    """Independently parsed source artifacts (immutable content maps)."""

    monitor_classification: Optional[dict[str, Any]] = None
    changed_summary: Optional[dict[str, Any]] = None
    run_summary: Optional[dict[str, Any]] = None
    run_log: Optional[str] = None
    missing: list[str] = field(default_factory=list)
    malformed: list[str] = field(default_factory=list)
    raw_hashes: dict[str, str] = field(default_factory=dict)


@dataclass
class FixtureMeta:
    """Optional fixture metadata (offline tests only)."""

    now_utc: Optional[datetime] = None
    action_text_override: Optional[str] = None
    generated_at: Optional[datetime] = None
    display_timezone: Optional[str] = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "FixtureMeta":
        now = data.get("now_utc")
        gen = data.get("generated_at")
        return FixtureMeta(
            now_utc=_parse_optional_dt(now),
            action_text_override=data.get("action_text_override"),
            generated_at=_parse_optional_dt(gen),
            display_timezone=data.get("display_timezone"),
        )


def _parse_optional_dt(value: Any) -> Optional[datetime]:
    if value is None:
        return None
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, str):
        text = value.strip()
        if text.endswith("Z"):
            text = text[:-1] + "+00:00"
        dt = datetime.fromisoformat(text)
    else:
        raise TypeError("timestamp must be str or datetime")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def to_utc_z(dt: datetime) -> str:
    """Format datetime as UTC ISO-8601 with ``Z`` suffix."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    utc = dt.astimezone(timezone.utc)
    # Drop microseconds for stable identity / fixtures unless present.
    if utc.microsecond:
        return utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    return utc.strftime("%Y-%m-%dT%H:%M:%SZ")
