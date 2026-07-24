"""Normalized producer result model."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ProducerResult:
    producer_run_id: str
    event_id: Optional[str]
    site_id: str
    status: str
    transport_mode: str
    dispatch_attempted: bool
    simulated_dispatch: bool
    http_status: Optional[int]
    business_result: str
    dedupe_result: str
    retry_decision: str
    retry_count: int
    failure_category: str
    intake_accepted: bool
    telegram_delivery_known: bool
    elapsed_ms: int
    final_state: str
    redaction_status: str
    observed_at: Optional[str] = None
    n8n_execution_id: Optional[str] = None
    telegram_message_id: Optional[str] = None
    network_calls: int = 0
    automatic_retry: bool = False
    endpoint_identity: dict[str, Any] = field(default_factory=dict)
    request_sanitized: Optional[dict[str, Any]] = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_sanitized_dict(self) -> dict[str, Any]:
        return {
            "producer_run_id": self.producer_run_id,
            "event_id": self.event_id,
            "site_id": self.site_id,
            "status": self.status,
            "observed_at": self.observed_at,
            "transport_mode": self.transport_mode,
            "dispatch_attempted": self.dispatch_attempted,
            "simulated_dispatch": self.simulated_dispatch,
            "http_status": self.http_status,
            "business_result": self.business_result,
            "dedupe_result": self.dedupe_result,
            "retry_decision": self.retry_decision,
            "retry_count": self.retry_count,
            "failure_category": self.failure_category,
            "intake_accepted": self.intake_accepted,
            "telegram_delivery_known": self.telegram_delivery_known,
            "telegram_message_id": self.telegram_message_id,
            "n8n_execution_id": self.n8n_execution_id,
            "elapsed_ms": self.elapsed_ms,
            "final_state": self.final_state,
            "redaction_status": self.redaction_status,
            "network_calls": self.network_calls,
            "automatic_retry": self.automatic_retry,
            "endpoint_identity": dict(self.endpoint_identity),
            "request_sanitized": self.request_sanitized,
            "extra": dict(self.extra) if self.extra else {},
        }


def new_producer_run_id() -> str:
    return str(uuid.uuid4())


def elapsed_since_ms(start: float) -> int:
    return int((time.perf_counter() - start) * 1000)
