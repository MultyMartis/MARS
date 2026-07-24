"""Response classification and retry decision (no real retries)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from .producer_constants import (
    BUSINESS_AMBIGUOUS,
    BUSINESS_DUPLICATE_SUPPRESSED,
    BUSINESS_ERROR,
    BUSINESS_EVENT_ID_CONFLICT,
    BUSINESS_INTAKE_ACCEPTED,
    BUSINESS_NOT_DISPATCHED,
    BUSINESS_REJECTED,
    CLASS_CONNECT_FAILURE,
    CLASS_DNS_FAILURE,
    CLASS_HTTP_200_DUPLICATE_SUPPRESSED,
    CLASS_HTTP_202_INTAKE_ACCEPTED,
    CLASS_HTTP_400_AUTH_OR_VALIDATION,
    CLASS_HTTP_401_403_AUTH,
    CLASS_HTTP_409_EVENT_ID_CONFLICT,
    CLASS_HTTP_5XX,
    CLASS_MALFORMED_RESPONSE,
    CLASS_NETWORK_UNKNOWN,
    CLASS_READ_TIMEOUT_AMBIGUOUS,
    CLASS_TLS_FAILURE,
    CLASS_TRANSPORT_DISABLED,
    CLASS_UNEXPECTED_RESPONSE,
    CLASS_WORKFLOW_INACTIVE,
    DEDUPE_CONFLICT,
    DEDUPE_DUPLICATE,
    DEDUPE_FIRST_SEEN,
    DEDUPE_NA,
    DEDUPE_UNKNOWN,
    RETRY_FUTURE_ELIGIBLE,
    RETRY_MANUAL_DEDUPE_CHECK_REQUIRED,
    RETRY_NONE,
    RETRY_TERMINAL_FAILURE,
    RETRY_TERMINAL_SUCCESS,
)
from .producer_transport import TransportResponse


@dataclass(frozen=True)
class Classification:
    failure_category: str
    business_result: str
    dedupe_result: str
    retry_decision: str
    automatic_retry: bool
    intake_accepted: bool
    telegram_delivery_known: bool
    final_state: str
    http_status: Optional[int] = None

    def sanitized_dict(self) -> dict[str, Any]:
        return {
            "failure_category": self.failure_category,
            "business_result": self.business_result,
            "dedupe_result": self.dedupe_result,
            "retry_decision": self.retry_decision,
            "automatic_retry": self.automatic_retry,
            "intake_accepted": self.intake_accepted,
            "telegram_delivery_known": self.telegram_delivery_known,
            "final_state": self.final_state,
            "http_status": self.http_status,
        }


def classify_transport_response(resp: TransportResponse) -> Classification:
    """Map a (simulated) transport response to producer semantics.

    HTTP 202 → INTAKE_ACCEPTED (not Telegram SENT).
    Automatic retry is always False in D2 (max_retries default 0).
    """
    # Explicit error_class from mock/fixture takes precedence for network classes
    ec = (resp.error_class or "").upper()
    status = resp.http_status
    body = resp.body if isinstance(resp.body, dict) else {}

    if ec == "TRANSPORT_DISABLED" or (
        status is None and ec == "" and not resp.ok and resp.error_detail
        and "disabled" in (resp.error_detail or "")
    ):
        return Classification(
            failure_category=CLASS_TRANSPORT_DISABLED,
            business_result=BUSINESS_NOT_DISPATCHED,
            dedupe_result=DEDUPE_NA,
            retry_decision=RETRY_NONE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="NOT_DISPATCHED",
            http_status=None,
        )

    if ec == CLASS_READ_TIMEOUT_AMBIGUOUS or ec == "READ_TIMEOUT_AMBIGUOUS":
        return Classification(
            failure_category=CLASS_READ_TIMEOUT_AMBIGUOUS,
            business_result=BUSINESS_AMBIGUOUS,
            dedupe_result=DEDUPE_UNKNOWN,
            retry_decision=RETRY_MANUAL_DEDUPE_CHECK_REQUIRED,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="AMBIGUOUS_TIMEOUT",
            http_status=None,
        )

    if ec == CLASS_CONNECT_FAILURE:
        return _future_retry(CLASS_CONNECT_FAILURE, status)
    if ec == CLASS_DNS_FAILURE:
        return _future_retry(CLASS_DNS_FAILURE, status)
    if ec == CLASS_TLS_FAILURE:
        return _future_retry(CLASS_TLS_FAILURE, status)
    if ec == CLASS_NETWORK_UNKNOWN:
        return _future_retry(CLASS_NETWORK_UNKNOWN, status)
    if ec == CLASS_MALFORMED_RESPONSE or (
        resp.raw_body and status is not None and body == {}
    ):
        return Classification(
            failure_category=CLASS_MALFORMED_RESPONSE,
            business_result=BUSINESS_ERROR,
            dedupe_result=DEDUPE_UNKNOWN,
            retry_decision=RETRY_TERMINAL_FAILURE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="MALFORMED_RESPONSE",
            http_status=status,
        )
    if ec == CLASS_WORKFLOW_INACTIVE or (
        status == 404
        and "inactive" in str(body.get("hint", "")).lower()
    ):
        return Classification(
            failure_category=CLASS_WORKFLOW_INACTIVE,
            business_result=BUSINESS_ERROR,
            dedupe_result=DEDUPE_NA,
            retry_decision=RETRY_TERMINAL_FAILURE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="WORKFLOW_INACTIVE",
            http_status=status,
        )

    if status == 202:
        dedupe = str(body.get("dedupe_result") or DEDUPE_FIRST_SEEN)
        return Classification(
            failure_category=CLASS_HTTP_202_INTAKE_ACCEPTED,
            business_result=BUSINESS_INTAKE_ACCEPTED,
            dedupe_result=dedupe,
            retry_decision=RETRY_TERMINAL_SUCCESS,
            automatic_retry=False,
            intake_accepted=True,
            telegram_delivery_known=False,  # Pattern B — not inferable
            final_state="INTAKE_ACCEPTED",
            http_status=202,
        )

    if status == 200:
        result = str(body.get("result") or "").upper()
        dedupe = str(body.get("dedupe_result") or "").upper()
        if (
            "DUPLICATE" in result
            or dedupe == "DUPLICATE"
            or result == "DUPLICATE_SUPPRESSED"
        ):
            return Classification(
                failure_category=CLASS_HTTP_200_DUPLICATE_SUPPRESSED,
                business_result=BUSINESS_DUPLICATE_SUPPRESSED,
                dedupe_result=DEDUPE_DUPLICATE,
                retry_decision=RETRY_TERMINAL_SUCCESS,
                automatic_retry=False,
                intake_accepted=True,
                telegram_delivery_known=False,
                final_state="DUPLICATE_SUPPRESSED",
                http_status=200,
            )
        return Classification(
            failure_category=CLASS_UNEXPECTED_RESPONSE,
            business_result=BUSINESS_ERROR,
            dedupe_result=DEDUPE_UNKNOWN,
            retry_decision=RETRY_TERMINAL_FAILURE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="UNEXPECTED_RESPONSE",
            http_status=200,
        )

    if status == 409:
        return Classification(
            failure_category=CLASS_HTTP_409_EVENT_ID_CONFLICT,
            business_result=BUSINESS_EVENT_ID_CONFLICT,
            dedupe_result=DEDUPE_CONFLICT,
            retry_decision=RETRY_TERMINAL_FAILURE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="EVENT_ID_CONFLICT",
            http_status=409,
        )

    if status in {401, 403}:
        return Classification(
            failure_category=CLASS_HTTP_401_403_AUTH,
            business_result=BUSINESS_REJECTED,
            dedupe_result=DEDUPE_NA,
            retry_decision=RETRY_TERMINAL_FAILURE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="AUTH_REJECTED",
            http_status=status,
        )

    if status is not None and 400 <= status < 500:
        return Classification(
            failure_category=CLASS_HTTP_400_AUTH_OR_VALIDATION,
            business_result=BUSINESS_REJECTED,
            dedupe_result=DEDUPE_NA,
            retry_decision=RETRY_TERMINAL_FAILURE,
            automatic_retry=False,
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="VALIDATION_REJECTED",
            http_status=status,
        )

    if status is not None and 500 <= status < 600:
        return Classification(
            failure_category=CLASS_HTTP_5XX,
            business_result=BUSINESS_ERROR,
            dedupe_result=DEDUPE_UNKNOWN,
            retry_decision=RETRY_FUTURE_ELIGIBLE,
            automatic_retry=False,  # D2: not enabled
            intake_accepted=False,
            telegram_delivery_known=False,
            final_state="HTTP_5XX",
            http_status=status,
        )

    if status is None and not resp.ok:
        return _future_retry(CLASS_NETWORK_UNKNOWN, None)

    return Classification(
        failure_category=CLASS_UNEXPECTED_RESPONSE,
        business_result=BUSINESS_ERROR,
        dedupe_result=DEDUPE_UNKNOWN,
        retry_decision=RETRY_TERMINAL_FAILURE,
        automatic_retry=False,
        intake_accepted=False,
        telegram_delivery_known=False,
        final_state="UNEXPECTED_RESPONSE",
        http_status=status,
    )


def _future_retry(category: str, status: Optional[int]) -> Classification:
    return Classification(
        failure_category=category,
        business_result=BUSINESS_ERROR,
        dedupe_result=DEDUPE_UNKNOWN,
        retry_decision=RETRY_FUTURE_ELIGIBLE,
        automatic_retry=False,
        intake_accepted=False,
        telegram_delivery_known=False,
        final_state=category,
        http_status=status,
    )


def plan_retry_attempt(
    *,
    event_id: str,
    envelope: dict,
    classification: Classification,
    retry_count: int,
    max_retries: int = 0,
) -> dict[str, Any]:
    """Plan a future retry without performing it.

    Preserves event_id and envelope identity. Never auto-dispatches.
    """
    eligible = classification.retry_decision == RETRY_FUTURE_ELIGIBLE
    would_auto = False  # D2: always false; max_retries default 0
    if eligible and max_retries > 0 and retry_count < max_retries:
        # Still do not auto-run in D2 — only report hypothetical
        would_auto = False

    return {
        "event_id": event_id,
        "same_event_id": True,
        "envelope_event_id": envelope.get("event_id"),
        "retry_count_next": retry_count + 1 if eligible else retry_count,
        "automatic_retry": would_auto,
        "retry_decision": classification.retry_decision,
        "requires_manual_dedupe_check": (
            classification.retry_decision == RETRY_MANUAL_DEDUPE_CHECK_REQUIRED
        ),
        "dispatch_triggered": False,
    }
