"""Offline deterministic SIMPLE text formatter (no Telegram)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any, Mapping, Optional

from .constants import DISPLAY_TIMEZONE, EVENT_TITLE, SITE_NAME

# Europe/Moscow is permanently UTC+3 (no DST) since 2014.
# Prefer zoneinfo when tzdata is available; otherwise use a fixed offset so
# offline tests remain stdlib-only on Windows without the tzdata package.
_MOSCOW_FIXED = timezone(timedelta(hours=3), name="Europe/Moscow")


def _resolve_tz(tz_name: str) -> timezone:
    if tz_name in {"Europe/Moscow", "Europe/Moscow"}:
        try:
            from zoneinfo import ZoneInfo

            return ZoneInfo("Europe/Moscow")  # type: ignore[return-value]
        except Exception:
            return _MOSCOW_FIXED
    try:
        from zoneinfo import ZoneInfo

        return ZoneInfo(tz_name)  # type: ignore[return-value]
    except Exception as exc:
        raise ValueError(f"unsupported display timezone: {tz_name}") from exc


def _parse_utc(value: str) -> datetime:
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    dt = datetime.fromisoformat(text)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def format_run_local(
    observed_at: str,
    *,
    tz_name: str = DISPLAY_TIMEZONE,
) -> str:
    """Format observed_at as ``YYYY-MM-DD HH:mm`` in explicit timezone."""
    local = _parse_utc(observed_at).astimezone(_resolve_tz(tz_name))
    return local.strftime("%Y-%m-%d %H:%M")


def format_simple(
    envelope: Mapping[str, Any],
    *,
    tz_name: Optional[str] = None,
) -> str:
    """Render SIMPLE template from a normalized envelope.

    No Telegram call. No secrets. No paths.
    """
    tz = tz_name or DISPLAY_TIMEZONE
    site_name = envelope.get("site", {}).get("site_name", SITE_NAME)
    status = envelope["run"]["normalized_status"]
    metrics = envelope["metrics"]
    action_text = str(envelope["action"]["text"]).strip()
    # Lowercase first letter for OK "none" style consistency with templates
    # when action is NONE; otherwise keep documented Russian text.
    if envelope["action"].get("code") == "NONE":
        action_display = "none"
    else:
        action_display = action_text

    run_line = format_run_local(str(envelope["observed_at"]), tz_name=tz)

    lines = [
        f"{site_name} · {status}",
        EVENT_TITLE,
        "",
        f"Baseline: {metrics['baseline_count']}",
        f"Current: {metrics['current_count']}",
        f"Added: {metrics['added_urls']}",
        f"Removed: {metrics['removed_urls']}",
        f"Onboarding needed: {metrics['onboarding_needed_count']}",
        "",
        f"Action: {action_display}",
        f"Run: {run_line}",
    ]
    return "\n".join(lines) + "\n"
