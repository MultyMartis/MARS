"""Phase 1B-D5 controlled real-source live producer (Pattern B).

explicit completed SITE-002 monitor artifact
  → D4 adapter
  → D5 authorization gate
  → D3 HTTPS transport (reused)
  → one bounded POST

No monitor execution. No auto-discovery. No replay. Max 1 real HTTP.
"""

from __future__ import annotations

import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Optional

from .constants import SITE_ID
from .producer_classify import classify_transport_response, plan_retry_attempt
from .producer_config import ProducerProfile, ProducerSecrets
from .producer_constants import (
    D5_PRODUCER_MARKER,
    D5_SOURCE_PROVENANCE,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
    TRANSPORT_HTTP,
)
from .producer_d3_gates import load_charter_state as load_d3_charter_state
from .producer_d3_gates import default_d3_runs_dir
from .producer_d5_gates import (
    D5GateError,
    D5LiveAuthorization,
    assert_request_budget,
    default_d5_runs_dir,
    envelope_has_d5_marker,
    load_charter_state,
    record_attempted_request,
    sanitize_source_label,
    save_charter_state,
    validate_explicit_source_path,
)
from .producer_dispatch_guard import (
    SequentialDispatchError,
    SequentialDispatchGuard,
    get_default_guard,
)
from .producer_evidence import write_producer_evidence
from .producer_http import create_d5_live_transport
from .producer_request import build_outbound_request
from .producer_result import ProducerResult, elapsed_since_ms, new_producer_run_id
from .site002_adapter import (
    RealSourceLiveDispatchNotAuthorized,
    adapt_source_dir,
    is_real_source_fixture,
)
from .site002_adapter_constants import (
    REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
    SOURCE_CONTRACT_VERSION,
)


def apply_d5_real_source_markers(envelope: dict[str, Any]) -> dict[str, Any]:
    """Annotate producer metadata only — does not alter identity-bearing fields."""
    out = dict(envelope)
    # Preserve identity fields: site, run_id, observed_at, status, metrics, reasons
    producer = dict(out.get("producer") or {})
    producer["name"] = D5_PRODUCER_MARKER
    producer["version"] = "d5-manual-real-source-1.0"
    out["producer"] = producer
    out["environment"] = "manual_real_source_controlled"
    meta = dict(out.get("meta") or {})
    meta["d5_delivery_phase"] = "1B-D5"
    meta["source_provenance"] = D5_SOURCE_PROVENANCE
    meta["source_contract"] = SOURCE_CONTRACT_VERSION
    out["meta"] = meta
    security = dict(out.get("security") or {})
    security["classification"] = "internal"
    security["contains_secrets"] = False
    security["redacted"] = True
    out["security"] = security
    return out


def build_d5_real_source_envelope(source_dir: Path) -> dict[str, Any]:
    """Build envelope via D4 adapter path, then apply D5 delivery marker."""
    # Reject committed sanitized fixtures as live real-source
    if is_real_source_fixture(source_dir):
        meta_path = Path(source_dir) / "fixture-meta.json"
        if meta_path.is_file() or "fixtures" in {p.lower() for p in Path(source_dir).parts}:
            # Storage real runs have no fixture-meta; committed fixtures do / live under fixtures/
            parts = {p.lower() for p in Path(source_dir).parts}
            if "fixtures" in parts or "site-002-real-source-adapter" in parts:
                raise D5GateError("sanitized D4 fixture rejected as live real-source")

    proc, _redaction, _fp = adapt_source_dir(Path(source_dir), build_envelope=True)
    if not proc.distributable or proc.envelope is None:
        raise D5GateError("source not distributable for D5 real-source event")
    if proc.security_rejected:
        raise D5GateError("source security rejected")
    if proc.normalized_status == "BLOCKED":
        # Authority/staleness BLOCKED must not be posted to client channel by default.
        raise D5GateError(
            f"source maps to BLOCKED ({proc.source_status}); live POST not approved"
        )
    return apply_d5_real_source_markers(dict(proc.envelope))


def double_build_event_id(source_dir: Path) -> tuple[str, str, dict[str, Any]]:
    """Build envelope twice; return (event_id_a, event_id_b, envelope_a)."""
    env_a = build_d5_real_source_envelope(source_dir)
    env_b = build_d5_real_source_envelope(source_dir)
    id_a = str(env_a.get("event_id") or "")
    id_b = str(env_b.get("event_id") or "")
    if not id_a or id_a != id_b:
        raise D5GateError("event_id not deterministic across double-build")
    # Marker must not change identity
    if id_a != str(
        adapt_source_dir(Path(source_dir), build_envelope=True)[0].envelope.get("event_id")
    ):
        raise D5GateError("D5 marker must not change event_id")
    return id_a, id_b, env_a


def build_source_preview(
    source_dir: Path,
    *,
    now_utc: Optional[datetime] = None,
) -> dict[str, Any]:
    """Sanitized preview for operator gate (network_calls=0)."""
    now = now_utc or datetime.now(timezone.utc)
    proc, redaction, fingerprint = adapt_source_dir(Path(source_dir), build_envelope=True)
    event_id = None
    if proc.envelope is not None:
        event_id = str(proc.envelope.get("event_id") or "") or None
    observed = proc.observed_at
    age_seconds = proc.age_seconds
    age_hours = round(float(age_seconds) / 3600.0, 2) if age_seconds is not None else None
    preview = {
        "source_label": sanitize_source_label(source_dir),
        "source_run_id": proc.run_id,
        "observed_at": observed,
        "source_age_seconds": age_seconds,
        "source_age_hours": age_hours,
        "verification_time_utc": now.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_classification": proc.source_status,
        "client_ops_mapped_status": proc.normalized_status,
        "safe_metrics": proc.metrics,
        "reason_codes": list(proc.reason_codes),
        "action_code": proc.action_code,
        "summary_code": proc.summary_code,
        "event_id": event_id,
        "source_contract_version": SOURCE_CONTRACT_VERSION,
        "source_provenance": D5_SOURCE_PROVENANCE,
        "firewall_result": "PASS" if redaction.get("run_log_loaded") is False else "UNKNOWN",
        "redaction_result": {
            "policy": redaction.get("policy"),
            "run_log_loaded": redaction.get("run_log_loaded"),
            "artifact_count": len(redaction.get("artifacts") or []),
        },
        "source_contract_fingerprint": fingerprint,
        "message_preview": proc.simple_text,
        "distributable": proc.distributable,
        "security_rejected": proc.security_rejected,
        "network_calls": 0,
    }
    return preview


def assess_preview_for_live(preview: Mapping[str, Any]) -> dict[str, Any]:
    """Return preview verdict — does not send."""
    status = str(preview.get("client_ops_mapped_status") or "")
    source_status = str(preview.get("source_classification") or "")
    msg = str(preview.get("message_preview") or "")
    unsafe_tokens = (
        "X:\\",
        "AI MARS STORAGE",
        "scheduled-monitors",
        "run.log",
        "password",
        "token",
        "api_key",
        "webhook/",
    )
    msg_unsafe = any(t.lower() in msg.lower() for t in unsafe_tokens if t != "X:\\")
    msg_unsafe = msg_unsafe or ("X:\\" in msg) or ("\\\\" in msg and "STORAGE" in msg.upper())

    if status == "BLOCKED" and "CONFLICT" in source_status:
        verdict = "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
        reason = "contradictory authority BLOCKED"
    elif status == "BLOCKED":
        verdict = "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
        reason = "BLOCKED status not safe for client-facing Telegram"
    elif msg_unsafe:
        verdict = "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
        reason = "message preview exposes internal path/secret markers"
    elif not preview.get("distributable"):
        verdict = "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
        reason = "source not distributable"
    elif preview.get("security_rejected"):
        verdict = "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
        reason = "security rejected"
    elif not preview.get("event_id"):
        verdict = "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST"
        reason = "event_id missing"
    else:
        verdict = "REAL_SOURCE_PREVIEW_APPROVED_FOR_ONE_LIVE_POST"
        reason = "preview safe for one controlled live POST"

    return {
        "verdict": verdict,
        "reason": reason,
        "approved": verdict == "REAL_SOURCE_PREVIEW_APPROVED_FOR_ONE_LIVE_POST",
        "network_calls": 0,
    }


def d3_charter_is_consumed(repo_root: Path) -> bool:
    state = load_d3_charter_state(default_d3_runs_dir(Path(repo_root)))
    return bool(state.get("charter_consumed"))


def run_producer_d5_controlled(
    *,
    authorization: D5LiveAuthorization,
    profile: ProducerProfile,
    secrets: ProducerSecrets,
    source_dir: Path,
    concurrency: int = 1,
    evidence_dir: Optional[Path] = None,
    runs_dir: Optional[Path] = None,
    repo_root: Optional[Path] = None,
    guard: Optional[SequentialDispatchGuard] = None,
    producer_run_id: Optional[str] = None,
    event_unseen_confirmed: bool = False,
) -> ProducerResult:
    """Execute one gated live real-source producer POST (Pattern B)."""
    start = time.perf_counter()
    run_id = producer_run_id or new_producer_run_id()
    guard = guard or get_default_guard()
    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[4]
    runs = Path(runs_dir) if runs_dir else default_d5_runs_dir(root)

    if authorization.dry_run:
        return ProducerResult(
            producer_run_id=run_id,
            event_id=None,
            site_id=profile.site_id or SITE_ID,
            status="DRY_RUN",
            transport_mode="http",
            dispatch_attempted=False,
            simulated_dispatch=False,
            http_status=None,
            business_result="NOT_DISPATCHED",
            dedupe_result="NA",
            retry_decision="NONE",
            retry_count=0,
            failure_category="DRY_RUN",
            intake_accepted=False,
            telegram_delivery_known=False,
            elapsed_ms=elapsed_since_ms(start),
            final_state="D5_DRY_RUN_READY",
            redaction_status="redacted",
            network_calls=0,
            automatic_retry=False,
            endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
            extra={"dry_run": True, "phase": "1B-D5"},
        )

    try:
        authorization.assert_live_allowed()
    except D5GateError as exc:
        return _blocked(run_id, profile, start, str(exc.detail), exc.code)

    if not event_unseen_confirmed:
        return _blocked(
            run_id,
            profile,
            start,
            "Data Table unseen precheck not confirmed",
            NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
        )

    try:
        guard.acquire(concurrency=concurrency)
    except SequentialDispatchError as exc:
        return ProducerResult(
            producer_run_id=run_id,
            event_id=None,
            site_id=profile.site_id or SITE_ID,
            status="BLOCKED",
            transport_mode=TRANSPORT_HTTP,
            dispatch_attempted=False,
            simulated_dispatch=False,
            http_status=None,
            business_result="NOT_DISPATCHED",
            dedupe_result="NA",
            retry_decision="TERMINAL_FAILURE",
            retry_count=0,
            failure_category="SEQUENTIAL_GUARD",
            intake_accepted=False,
            telegram_delivery_known=False,
            elapsed_ms=elapsed_since_ms(start),
            final_state="CONCURRENCY_REJECTED",
            redaction_status="redacted",
            network_calls=0,
            endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
            extra={"error": str(exc)},
        )

    try:
        state = load_charter_state(runs)
        assert_request_budget(state)

        validated = validate_explicit_source_path(Path(source_dir))
        id_a, id_b, built = double_build_event_id(validated)
        if id_a != id_b:
            raise D5GateError("event_id double-build mismatch")
        if not envelope_has_d5_marker(built):
            raise D5GateError("D5 producer marker missing on envelope")

        event_id = id_a
        request = build_outbound_request(
            built,
            profile,
            secrets,
            require_auth=True,
        )
        transport = create_d5_live_transport(
            profile=profile,
            secrets=secrets,
            authorization=authorization,
        )
        resp = transport.dispatch(request)
        classification = classify_transport_response(resp)
        retry_plan = plan_retry_attempt(
            event_id=event_id,
            envelope=built,
            classification=classification,
            retry_count=0,
            max_retries=0,
        )

        new_state = record_attempted_request(state, event_id=event_id)
        new_state["source_label"] = sanitize_source_label(validated)
        new_state["charter_created"] = True
        save_charter_state(runs, new_state)

        status = str(
            built.get("run", {}).get("normalized_status")
            or built.get("status")
            or "UNKNOWN"
        )
        result = ProducerResult(
            producer_run_id=run_id,
            event_id=event_id,
            site_id=str(
                built.get("site", {}).get("site_id") or profile.site_id or SITE_ID
            ),
            status=status,
            transport_mode=TRANSPORT_HTTP,
            dispatch_attempted=True,
            simulated_dispatch=False,
            http_status=classification.http_status,
            business_result=classification.business_result,
            dedupe_result=classification.dedupe_result,
            retry_decision=classification.retry_decision,
            retry_count=0,
            failure_category=classification.failure_category,
            intake_accepted=classification.intake_accepted,
            telegram_delivery_known=False,
            elapsed_ms=elapsed_since_ms(start),
            final_state=classification.final_state,
            redaction_status="redacted",
            observed_at=str(built.get("observed_at") or "") or None,
            network_calls=1,
            automatic_retry=False,
            endpoint_identity={
                **profile.sanitized_dict()["endpoint_identity"],
                **transport.endpoint.sanitized_dict(),
            },
            request_sanitized=request.sanitized_dict(),
            extra={
                "retry_plan": retry_plan,
                "transport_response": resp.sanitized_dict(),
                "real_network": True,
                "phase": "1B-D5",
                "d5_marker": D5_PRODUCER_MARKER,
                "source_label": sanitize_source_label(validated),
                "source_run_id": str(
                    built.get("run", {}).get("run_id")
                    or built.get("run_id")
                    or ""
                ),
                "auth_header_present": True,
                "auth_header_value": "<redacted>",
                "charter_consumed": True,
            },
        )
        if evidence_dir is not None:
            write_producer_evidence(result, Path(evidence_dir))
        return result
    except D5GateError as exc:
        return _blocked(run_id, profile, start, str(exc.detail), exc.code)
    except RealSourceLiveDispatchNotAuthorized as exc:
        return _blocked(
            run_id,
            profile,
            start,
            str(exc.detail),
            REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
        )
    except Exception:  # noqa: BLE001
        return ProducerResult(
            producer_run_id=run_id,
            event_id=None,
            site_id=profile.site_id or SITE_ID,
            status="ERROR",
            transport_mode=TRANSPORT_HTTP,
            dispatch_attempted=False,
            simulated_dispatch=False,
            http_status=None,
            business_result="ERROR",
            dedupe_result="NA",
            retry_decision="TERMINAL_FAILURE",
            retry_count=0,
            failure_category="UNEXPECTED",
            intake_accepted=False,
            telegram_delivery_known=False,
            elapsed_ms=elapsed_since_ms(start),
            final_state="ERROR",
            redaction_status="redacted",
            network_calls=0,
            endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
            extra={"error_type": "UNEXPECTED"},
        )
    finally:
        guard.release()


def _blocked(
    run_id: str,
    profile: ProducerProfile,
    start: float,
    detail: str,
    final_state: str,
) -> ProducerResult:
    return ProducerResult(
        producer_run_id=run_id,
        event_id=None,
        site_id=profile.site_id or SITE_ID,
        status="BLOCKED",
        transport_mode=TRANSPORT_HTTP,
        dispatch_attempted=False,
        simulated_dispatch=False,
        http_status=None,
        business_result="NOT_DISPATCHED",
        dedupe_result="NA",
        retry_decision="TERMINAL_FAILURE",
        retry_count=0,
        failure_category="DISPATCH_NOT_AUTHORIZED",
        intake_accepted=False,
        telegram_delivery_known=False,
        elapsed_ms=elapsed_since_ms(start),
        final_state=final_state,
        redaction_status="redacted",
        network_calls=0,
        endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
        extra={"error": detail},
    )


# Silence unused import lint for D3 code constant re-export clarity in tests
_ = NETWORK_DISPATCH_NOT_AUTHORIZED_D3
