"""Phase 1B-D3 controlled live producer pipeline (gated real HTTPS)."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any, Mapping, Optional

from .constants import SITE_ID
from .pipeline import process_fixture_dir
from .producer_classify import classify_transport_response, plan_retry_attempt
from .producer_config import ProducerProfile, ProducerSecrets
from .producer_constants import (
    D3_ENVELOPE_FILENAME,
    D3_PRODUCER_MARKER,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
    TRANSPORT_HTTP,
)
from .producer_d3_gates import (
    D3GateError,
    D3LiveAuthorization,
    assert_request_budget,
    default_d3_runs_dir,
    envelope_has_d3_marker,
    load_charter_state,
    save_charter_state,
)
from .producer_dispatch_guard import (
    SequentialDispatchError,
    SequentialDispatchGuard,
    get_default_guard,
)
from .producer_evidence import write_producer_evidence
from .producer_http import create_d3_live_transport
from .producer_request import build_outbound_request
from .producer_result import ProducerResult, elapsed_since_ms, new_producer_run_id


def apply_d3_synthetic_markers(envelope: dict[str, Any]) -> dict[str, Any]:
    """Annotate envelope with D3 producer marker without changing event_id inputs."""
    out = dict(envelope)
    producer = dict(out.get("producer") or {})
    producer["name"] = D3_PRODUCER_MARKER
    producer["version"] = "d3-controlled-1.0"
    out["producer"] = producer
    out["environment"] = "sandbox"
    action = dict(out.get("action") or {})
    action["text"] = (
        "D3 controlled synthetic producer test — sandbox only; "
        "not production; mars-client-ops-producer-live-d3"
    )
    out["action"] = action
    security = dict(out.get("security") or {})
    security["classification"] = "internal"
    security["contains_secrets"] = False
    security["redacted"] = True
    out["security"] = security
    return out


def build_d3_synthetic_envelope(fixture_dir: Path) -> dict[str, Any]:
    """Build envelope through canonical source→envelope path, then mark D3."""
    proc = process_fixture_dir(Path(fixture_dir), build_envelope=True)
    if not proc.distributable or proc.envelope is None:
        raise ValueError("fixture not distributable for D3 synthetic event")
    return apply_d3_synthetic_markers(dict(proc.envelope))


def persist_d3_envelope(envelope: Mapping[str, Any], runs_dir: Path) -> Path:
    runs_dir = Path(runs_dir)
    runs_dir.mkdir(parents=True, exist_ok=True)
    path = runs_dir / D3_ENVELOPE_FILENAME
    path.write_text(
        json.dumps(dict(envelope), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def load_persisted_d3_envelope(runs_dir: Path) -> dict[str, Any]:
    path = Path(runs_dir) / D3_ENVELOPE_FILENAME
    if not path.is_file():
        raise FileNotFoundError("persisted D3 envelope missing")
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("persisted D3 envelope malformed")
    return raw


def run_producer_d3_controlled(
    *,
    authorization: D3LiveAuthorization,
    profile: ProducerProfile,
    secrets: ProducerSecrets,
    fixture_dir: Optional[Path] = None,
    envelope: Optional[Mapping[str, Any]] = None,
    mode: str = "first_seen",
    concurrency: int = 1,
    evidence_dir: Optional[Path] = None,
    runs_dir: Optional[Path] = None,
    repo_root: Optional[Path] = None,
    guard: Optional[SequentialDispatchGuard] = None,
    producer_run_id: Optional[str] = None,
) -> ProducerResult:
    """Execute one gated live producer POST (FIRST_SEEN or exact replay)."""
    start = time.perf_counter()
    run_id = producer_run_id or new_producer_run_id()
    guard = guard or get_default_guard()
    root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[4]
    runs = Path(runs_dir) if runs_dir else default_d3_runs_dir(root)

    # Dry-run never reaches network
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
            final_state="D3_DRY_RUN_READY",
            redaction_status="redacted",
            network_calls=0,
            automatic_retry=False,
            endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
            extra={"dry_run": True, "mode": mode},
        )

    try:
        authorization.assert_live_allowed()
    except D3GateError as exc:
        return _blocked(run_id, profile, start, str(exc.detail), NETWORK_DISPATCH_NOT_AUTHORIZED_D3)

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
        if state.get("charter_consumed") and mode == "first_seen":
            raise D3GateError("charter already consumed")
        assert_request_budget(state, mode=mode)

        if mode == "exact_replay":
            built = load_persisted_d3_envelope(runs)
        elif envelope is not None:
            built = apply_d3_synthetic_markers(dict(envelope))
        elif fixture_dir is not None:
            built = build_d3_synthetic_envelope(Path(fixture_dir))
            persist_d3_envelope(built, runs)
        else:
            raise ValueError("fixture_dir or envelope required for FIRST_SEEN")

        if not envelope_has_d3_marker(built):
            raise D3GateError("D3 producer marker missing on envelope")

        event_id = str(built.get("event_id") or "")
        if mode == "exact_replay":
            prior = state.get("event_id")
            if prior and prior != event_id:
                raise D3GateError("replay event_id mismatch")

        request = build_outbound_request(
            built,
            profile,
            secrets,
            require_auth=True,
        )

        transport = create_d3_live_transport(
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

        # Count network call even on failure (budget consumed for live attempt)
        # Charter: no automatic retry; second POST reserved for exact replay only.
        # Only record success budget on unambiguous terminal outcomes for FIRST_SEEN,
        # but always increment attempt counter for live dispatch.
        new_state = dict(state)
        new_state["real_http_requests"] = int(new_state.get("real_http_requests") or 0) + 1
        new_state["event_id"] = event_id
        if mode == "first_seen":
            new_state["first_seen_consumed"] = True
            if classification.intake_accepted and classification.http_status == 202:
                new_state["first_seen_ok"] = True
            else:
                new_state["first_seen_ok"] = False
                new_state["charter_consumed"] = True  # no replay after ambiguous/fail
        elif mode == "exact_replay":
            new_state["exact_replay_consumed"] = True
            new_state["charter_consumed"] = True
        if int(new_state["real_http_requests"]) >= 2:
            new_state["charter_consumed"] = True
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
                "mode": mode,
                "d3_marker": D3_PRODUCER_MARKER,
                "auth_header_present": True,
                "auth_header_value": "<redacted>",
            },
        )
        if evidence_dir is not None:
            write_producer_evidence(result, Path(evidence_dir))
        return result
    except D3GateError as exc:
        return _blocked(run_id, profile, start, str(exc.detail), NETWORK_DISPATCH_NOT_AUTHORIZED_D3)
    except Exception as exc:  # noqa: BLE001
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
            extra={"error_type": type(exc).__name__},
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
        retry_decision="NOT_AUTHORIZED_D2"
        if final_state == NETWORK_DISPATCH_NOT_AUTHORIZED_D2
        else "TERMINAL_FAILURE",
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
