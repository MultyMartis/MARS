"""Deterministic event_id (UUID v5 over SHA-256 of canonical identity)."""

from __future__ import annotations

import hashlib
import json
import uuid
from typing import Any, Mapping, Optional, Sequence

from .constants import MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID, SCHEMA_MAJOR


def _namespace() -> uuid.UUID:
    return uuid.UUID(MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID)


def build_canonical_identity(
    *,
    site_id: str,
    event_type: str,
    run_id: str,
    observed_at: str,
    normalized_status: str,
    summary_code: str,
    metrics: Mapping[str, int],
    reason_codes: Sequence[str],
    action_code: str,
    schema_major: int = SCHEMA_MAJOR,
) -> dict[str, Any]:
    """Build the canonical identity document (no generated_at / delivery)."""
    return {
        "action_code": action_code,
        "event_type": event_type,
        "metrics": {
            "added_urls": int(metrics["added_urls"]),
            "baseline_count": int(metrics["baseline_count"]),
            "current_count": int(metrics["current_count"]),
            "onboarding_needed_count": int(metrics["onboarding_needed_count"]),
            "removed_urls": int(metrics["removed_urls"]),
        },
        "normalized_status": normalized_status,
        "observed_at": observed_at,
        "reason_codes": sorted(reason_codes),
        "run_id": run_id,
        "schema_major": int(schema_major),
        "site_id": site_id,
        "summary_code": summary_code,
    }


def canonical_identity_bytes(identity: Mapping[str, Any]) -> bytes:
    """UTF-8 compact JSON with sorted keys at every level."""
    return json.dumps(
        identity,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compute_event_id(
    *,
    site_id: str,
    event_type: str,
    run_id: str,
    observed_at: str,
    normalized_status: str,
    summary_code: str,
    metrics: Mapping[str, int],
    reason_codes: Sequence[str],
    action_code: str,
    schema_major: int = SCHEMA_MAJOR,
    identity_out: Optional[dict[str, Any]] = None,
) -> str:
    """Return deterministic UUID v5 string for the normalized observation."""
    identity = build_canonical_identity(
        site_id=site_id,
        event_type=event_type,
        run_id=run_id,
        observed_at=observed_at,
        normalized_status=normalized_status,
        summary_code=summary_code,
        metrics=metrics,
        reason_codes=reason_codes,
        action_code=action_code,
        schema_major=schema_major,
    )
    if identity_out is not None:
        identity_out.clear()
        identity_out.update(identity)
    name = sha256_hex(canonical_identity_bytes(identity))
    return str(uuid.uuid5(_namespace(), name))
