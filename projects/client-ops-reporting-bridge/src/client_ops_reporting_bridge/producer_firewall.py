"""Raw-monitor → producer input firewall (allowlist only)."""

from __future__ import annotations

from typing import Any, Mapping

from .constants import NORMALIZED_STATUSES
from .producer_constants import (
    PRODUCER_INPUT_ALLOWLIST,
    RAW_MONITOR_FORBIDDEN_KEYS,
)


class SourceFirewallError(ValueError):
    """Raised when raw monitor payload violates the producer firewall."""


def _lower_keys(d: Mapping[str, Any]) -> dict[str, Any]:
    return {str(k).lower(): v for k, v in d.items()}


def assert_no_forbidden_keys(payload: Mapping[str, Any], *, path: str = "root") -> None:
    for key, value in payload.items():
        lk = str(key).lower()
        if lk in RAW_MONITOR_FORBIDDEN_KEYS or any(
            bad in lk
            for bad in (
                "password",
                "secret",
                "token",
                "authorization",
                "cookie",
                "stack",
                "traceback",
                "private_key",
            )
        ):
            raise SourceFirewallError(f"forbidden field rejected: {path}.{key}")
        if isinstance(value, dict):
            assert_no_forbidden_keys(value, path=f"{path}.{key}")
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    assert_no_forbidden_keys(item, path=f"{path}.{key}[{i}]")


def normalize_producer_input(raw: Mapping[str, Any]) -> dict[str, Any]:
    """Allowlist-normalize a producer input object.

    Rejects unknown top-level keys that look sensitive; strips other unknown
    top-level keys. Does not blindly serialize arbitrary monitor JSON.
    """
    if not isinstance(raw, Mapping):
        raise SourceFirewallError("producer input must be an object")

    assert_no_forbidden_keys(raw)

    out: dict[str, Any] = {}
    for key, value in raw.items():
        if key in PRODUCER_INPUT_ALLOWLIST:
            out[key] = value
        # silently drop unknown non-forbidden keys (do not pass through)

    status = out.get("normalized_status") or out.get("status")
    if status is not None:
        status_s = str(status)
        if status_s not in NORMALIZED_STATUSES:
            raise SourceFirewallError(f"unsupported status rejected: {status_s}")
        out["normalized_status"] = status_s
        out["status"] = status_s

    # Metrics allowlist if present
    metrics = out.get("metrics")
    if isinstance(metrics, dict):
        allowed_m = {
            "baseline_count",
            "current_count",
            "added_urls",
            "removed_urls",
            "onboarding_needed_count",
        }
        cleaned = {k: metrics[k] for k in allowed_m if k in metrics}
        # reject metric keys that look like paths/secrets
        for k in metrics:
            if k not in allowed_m:
                lk = str(k).lower()
                if lk in RAW_MONITOR_FORBIDDEN_KEYS or "path" in lk or "password" in lk:
                    raise SourceFirewallError(f"forbidden metric field: {k}")
        out["metrics"] = cleaned

    return out


def extract_allowlisted_from_hostile(raw: Mapping[str, Any]) -> dict[str, Any]:
    """Strict mode used by tests: any forbidden key → reject entire payload."""
    assert_no_forbidden_keys(raw)
    return normalize_producer_input(raw)
