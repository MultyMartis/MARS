"""Offline sequential runtime producer pipeline (Phase 1B-D2)."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any, Mapping, Optional

from .constants import SITE_ID
from .pipeline import process_fixture_dir
from .producer_classify import Classification, classify_transport_response, plan_retry_attempt
from .producer_config import (
    ProducerProfile,
    ProducerSecrets,
    offline_default_profile,
)
from .producer_constants import (
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    TRANSPORT_DISABLED,
    TRANSPORT_MOCK,
)
from .producer_dispatch_guard import (
    SequentialDispatchError,
    SequentialDispatchGuard,
    get_default_guard,
)
from .producer_evidence import write_producer_evidence
from .producer_request import build_outbound_request
from .producer_result import ProducerResult, elapsed_since_ms, new_producer_run_id
from .producer_transport import (
    NetworkDispatchNotAuthorized,
    TransportResponse,
    create_transport,
)


def run_producer_offline(
    *,
    fixture_dir: Optional[Path] = None,
    envelope: Optional[Mapping[str, Any]] = None,
    profile: Optional[ProducerProfile] = None,
    secrets: Optional[ProducerSecrets] = None,
    transport_mode: str = TRANSPORT_MOCK,
    mock_fixture: str = "202_accepted",
    fixture_transport_path: Optional[Path] = None,
    concurrency: int = 1,
    retry_count: int = 0,
    evidence_dir: Optional[Path] = None,
    guard: Optional[SequentialDispatchGuard] = None,
    require_auth: bool = False,
    producer_run_id: Optional[str] = None,
) -> ProducerResult:
    """Run the offline producer once (sequential, simulated transport only)."""
    start = time.perf_counter()
    run_id = producer_run_id or new_producer_run_id()
    profile = profile or offline_default_profile()
    guard = guard or get_default_guard()

    try:
        guard.acquire(concurrency=concurrency)
    except SequentialDispatchError as exc:
        return ProducerResult(
            producer_run_id=run_id,
            event_id=None,
            site_id=profile.site_id or SITE_ID,
            status="BLOCKED",
            transport_mode=transport_mode,
            dispatch_attempted=False,
            simulated_dispatch=False,
            http_status=None,
            business_result="NOT_DISPATCHED",
            dedupe_result="NA",
            retry_decision="TERMINAL_FAILURE",
            retry_count=retry_count,
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
        # Live HTTP / unauthorized modes fail closed before any work
        if transport_mode.strip().lower() == "http":
            raise NetworkDispatchNotAuthorized("transport=http")

        built_envelope: dict[str, Any]
        status = "UNKNOWN"
        observed_at = None
        if envelope is not None:
            built_envelope = dict(envelope)
            status = str(
                built_envelope.get("run", {}).get("normalized_status")
                or built_envelope.get("status")
                or "UNKNOWN"
            )
            observed_at = built_envelope.get("observed_at")
        elif fixture_dir is not None:
            proc = process_fixture_dir(Path(fixture_dir), build_envelope=True)
            if not proc.distributable or proc.envelope is None:
                return ProducerResult(
                    producer_run_id=run_id,
                    event_id=None,
                    site_id=profile.site_id or SITE_ID,
                    status=proc.normalized_status,
                    transport_mode=transport_mode,
                    dispatch_attempted=False,
                    simulated_dispatch=False,
                    http_status=None,
                    business_result="NOT_DISPATCHED",
                    dedupe_result="NA",
                    retry_decision="TERMINAL_FAILURE",
                    retry_count=retry_count,
                    failure_category="SOURCE_NOT_DISTRIBUTABLE",
                    intake_accepted=False,
                    telegram_delivery_known=False,
                    elapsed_ms=elapsed_since_ms(start),
                    final_state="SOURCE_BLOCKED",
                    redaction_status="redacted",
                    observed_at=proc.observed_at,
                    network_calls=0,
                    endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
                    extra={"summary_code": proc.summary_code},
                )
            built_envelope = dict(proc.envelope)
            status = proc.normalized_status
            observed_at = proc.observed_at
        else:
            raise ValueError("fixture_dir or envelope required")

        event_id = str(built_envelope.get("event_id") or "")
        request = build_outbound_request(
            built_envelope,
            profile,
            secrets,
            require_auth=require_auth,
        )

        transport = create_transport(
            transport_mode,
            mock_fixture=mock_fixture,
            fixture_path=fixture_transport_path,
        )

        simulated = transport_mode != TRANSPORT_DISABLED
        dispatch_attempted = transport_mode != TRANSPORT_DISABLED

        if transport_mode == TRANSPORT_DISABLED:
            resp = TransportResponse(
                ok=False,
                error_class="TRANSPORT_DISABLED",
                error_detail="transport=disabled",
                simulated=True,
                network_calls=0,
            )
        else:
            resp = transport.dispatch(request)

        classification: Classification = classify_transport_response(resp)
        retry_plan = plan_retry_attempt(
            event_id=event_id,
            envelope=built_envelope,
            classification=classification,
            retry_count=retry_count,
            max_retries=0,  # D2: automatic retries disabled
        )

        result = ProducerResult(
            producer_run_id=run_id,
            event_id=event_id,
            site_id=str(
                built_envelope.get("site", {}).get("site_id")
                or profile.site_id
                or SITE_ID
            ),
            status=status,
            transport_mode=transport_mode,
            dispatch_attempted=dispatch_attempted,
            simulated_dispatch=simulated and dispatch_attempted,
            http_status=classification.http_status,
            business_result=classification.business_result,
            dedupe_result=classification.dedupe_result,
            retry_decision=classification.retry_decision,
            retry_count=retry_count,
            failure_category=classification.failure_category,
            intake_accepted=classification.intake_accepted,
            telegram_delivery_known=False,
            elapsed_ms=elapsed_since_ms(start),
            final_state=classification.final_state,
            redaction_status="redacted",
            observed_at=str(observed_at) if observed_at else None,
            n8n_execution_id=None,
            telegram_message_id=None,
            network_calls=0,
            automatic_retry=False,
            endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
            request_sanitized=request.sanitized_dict(),
            extra={
                "retry_plan": retry_plan,
                "transport_response": resp.sanitized_dict(),
            },
        )

        if evidence_dir is not None:
            write_producer_evidence(result, Path(evidence_dir))

        return result
    except NetworkDispatchNotAuthorized as exc:
        return ProducerResult(
            producer_run_id=run_id,
            event_id=None,
            site_id=profile.site_id or SITE_ID,
            status="BLOCKED",
            transport_mode=transport_mode,
            dispatch_attempted=False,
            simulated_dispatch=False,
            http_status=None,
            business_result="NOT_DISPATCHED",
            dedupe_result="NA",
            retry_decision="NOT_AUTHORIZED_D2",
            retry_count=retry_count,
            failure_category="DISPATCH_NOT_AUTHORIZED",
            intake_accepted=False,
            telegram_delivery_known=False,
            elapsed_ms=elapsed_since_ms(start),
            final_state=NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
            redaction_status="redacted",
            network_calls=0,
            endpoint_identity=profile.sanitized_dict()["endpoint_identity"],
            extra={"error": str(exc)},
        )
    finally:
        guard.release()


def build_retry_simulation(
    previous: ProducerResult,
    envelope: Mapping[str, Any],
    *,
    mock_fixture: str,
    profile: Optional[ProducerProfile] = None,
) -> ProducerResult:
    """Simulate a manual retry attempt preserving event_id (no auto-dispatch)."""
    assert previous.event_id == envelope.get("event_id"), "event_id must be preserved"
    return run_producer_offline(
        envelope=envelope,
        profile=profile,
        transport_mode=TRANSPORT_MOCK,
        mock_fixture=mock_fixture,
        retry_count=(previous.retry_count or 0) + 1,
        concurrency=1,
    )
