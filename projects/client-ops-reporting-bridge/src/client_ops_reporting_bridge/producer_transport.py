"""Transport abstraction — disabled / fixture / mock only in D2.

Real HTTP transport is intentionally absent / blocked.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Mapping, Optional, Protocol

from .producer_constants import (
    D2_ALLOWED_TRANSPORTS,
    MOCK_FIXTURE_NAMES,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    TRANSPORT_DISABLED,
    TRANSPORT_FIXTURE,
    TRANSPORT_HTTP,
    TRANSPORT_MOCK,
)
from .producer_request import OutboundRequest


class NetworkDispatchNotAuthorized(RuntimeError):
    """Raised when live HTTP dispatch is attempted during D2."""

    def __init__(self, detail: str = "") -> None:
        msg = NETWORK_DISPATCH_NOT_AUTHORIZED_D2
        if detail:
            msg = f"{msg}: {detail}"
        super().__init__(msg)
        self.code = NETWORK_DISPATCH_NOT_AUTHORIZED_D2


@dataclass
class TransportResponse:
    """Simulated or future real transport outcome."""

    ok: bool
    http_status: Optional[int] = None
    body: Optional[dict[str, Any]] = None
    raw_body: Optional[str] = None
    error_class: Optional[str] = None
    error_detail: Optional[str] = None
    simulated: bool = True
    network_calls: int = 0
    headers: dict[str, str] = field(default_factory=dict)

    def sanitized_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "http_status": self.http_status,
            "error_class": self.error_class,
            "simulated": self.simulated,
            "network_calls": self.network_calls,
            "body_keys": sorted(self.body.keys()) if isinstance(self.body, dict) else None,
        }


class Transport(Protocol):
    mode: str

    def dispatch(self, request: OutboundRequest) -> TransportResponse:
        ...


@dataclass
class DisabledTransport:
    mode: str = TRANSPORT_DISABLED
    network_calls: int = 0

    def dispatch(self, request: OutboundRequest) -> TransportResponse:
        self.network_calls += 0
        return TransportResponse(
            ok=False,
            http_status=None,
            error_class="TRANSPORT_DISABLED",
            error_detail="transport=disabled; no dispatch",
            simulated=True,
            network_calls=0,
        )


@dataclass
class MockTransport:
    """In-memory mock keyed by fixture name."""

    fixture_name: str
    mode: str = TRANSPORT_MOCK
    network_calls: int = 0

    def dispatch(self, request: OutboundRequest) -> TransportResponse:
        # Simulated only — never increments real network.
        self.network_calls = 0
        name = self.fixture_name
        if name not in MOCK_FIXTURE_NAMES:
            return TransportResponse(
                ok=False,
                error_class="UNEXPECTED_RESPONSE",
                error_detail="unknown mock fixture",
                simulated=True,
                network_calls=0,
            )
        return _mock_response_for(name, request)


@dataclass
class FixtureTransport:
    """Load a JSON transport response from a local fixture file."""

    path: Path
    mode: str = TRANSPORT_FIXTURE
    network_calls: int = 0

    def dispatch(self, request: OutboundRequest) -> TransportResponse:
        self.network_calls = 0
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        return TransportResponse(
            ok=bool(raw.get("ok", True)),
            http_status=raw.get("http_status"),
            body=raw.get("body") if isinstance(raw.get("body"), dict) else None,
            raw_body=raw.get("raw_body"),
            error_class=raw.get("error_class"),
            error_detail=raw.get("error_detail"),
            simulated=True,
            network_calls=0,
            headers=dict(raw.get("headers") or {}),
        )


@dataclass
class BlockedHttpTransport:
    """Future HTTP stub — always raises; never dials."""

    mode: str = TRANSPORT_HTTP
    network_calls: int = 0

    def dispatch(self, request: OutboundRequest) -> TransportResponse:
        raise NetworkDispatchNotAuthorized("http transport blocked in D2")


def create_transport(
    mode: str,
    *,
    mock_fixture: Optional[str] = None,
    fixture_path: Optional[Path] = None,
) -> Any:
    mode_n = (mode or TRANSPORT_DISABLED).strip().lower()
    if mode_n == TRANSPORT_HTTP:
        raise NetworkDispatchNotAuthorized("transport=http not authorized in D2")
    if mode_n not in D2_ALLOWED_TRANSPORTS:
        raise NetworkDispatchNotAuthorized(f"transport={mode_n} not authorized in D2")
    if mode_n == TRANSPORT_DISABLED:
        return DisabledTransport()
    if mode_n == TRANSPORT_MOCK:
        if not mock_fixture:
            raise ValueError("mock_fixture required for transport=mock")
        return MockTransport(fixture_name=mock_fixture)
    if mode_n == TRANSPORT_FIXTURE:
        if fixture_path is None:
            raise ValueError("fixture_path required for transport=fixture")
        return FixtureTransport(path=Path(fixture_path))
    raise NetworkDispatchNotAuthorized(f"transport={mode_n} not authorized in D2")


def _mock_response_for(name: str, request: OutboundRequest) -> TransportResponse:
    event_id = request.body.get("event_id")
    mapping = {
        "202_accepted": TransportResponse(
            ok=True,
            http_status=202,
            body={
                "result": "ACCEPTED",
                "dedupe_result": "FIRST_SEEN",
                "event_id": event_id,
            },
            simulated=True,
            network_calls=0,
        ),
        "200_duplicate_suppressed": TransportResponse(
            ok=True,
            http_status=200,
            body={
                "result": "DUPLICATE_SUPPRESSED",
                "dedupe_result": "DUPLICATE",
                "event_id": event_id,
            },
            simulated=True,
            network_calls=0,
        ),
        "409_event_id_conflict": TransportResponse(
            ok=False,
            http_status=409,
            body={
                "result": "EVENT_ID_CONFLICT",
                "dedupe_result": "EVENT_ID_CONFLICT",
                "event_id": event_id,
            },
            simulated=True,
            network_calls=0,
        ),
        "400_validation": TransportResponse(
            ok=False,
            http_status=400,
            body={"result": "INVALID_SCHEMA", "error": "validation"},
            simulated=True,
            network_calls=0,
        ),
        "403_auth": TransportResponse(
            ok=False,
            http_status=403,
            body={"result": "UNAUTHORIZED"},
            simulated=True,
            network_calls=0,
        ),
        "500_internal": TransportResponse(
            ok=False,
            http_status=500,
            body={"result": "INTERNAL_ERROR"},
            simulated=True,
            network_calls=0,
        ),
        "connect_failure": TransportResponse(
            ok=False,
            http_status=None,
            error_class="CONNECT_FAILURE",
            error_detail="simulated connect failure",
            simulated=True,
            network_calls=0,
        ),
        "dns_failure": TransportResponse(
            ok=False,
            http_status=None,
            error_class="DNS_FAILURE",
            error_detail="simulated dns failure",
            simulated=True,
            network_calls=0,
        ),
        "tls_failure": TransportResponse(
            ok=False,
            http_status=None,
            error_class="TLS_FAILURE",
            error_detail="simulated tls failure",
            simulated=True,
            network_calls=0,
        ),
        "read_timeout_ambiguous": TransportResponse(
            ok=False,
            http_status=None,
            error_class="READ_TIMEOUT_AMBIGUOUS",
            error_detail="simulated read timeout after possible send",
            simulated=True,
            network_calls=0,
        ),
        "malformed_response": TransportResponse(
            ok=False,
            http_status=200,
            raw_body="<html>not-json",
            error_class="MALFORMED_RESPONSE",
            simulated=True,
            network_calls=0,
        ),
        "unexpected_response": TransportResponse(
            ok=False,
            http_status=418,
            body={"result": "TEAPOT"},
            simulated=True,
            network_calls=0,
        ),
        "workflow_inactive": TransportResponse(
            ok=False,
            http_status=404,
            body={"message": "webhook not registered", "hint": "workflow inactive"},
            error_class="WORKFLOW_INACTIVE",
            simulated=True,
            network_calls=0,
        ),
        "network_unknown": TransportResponse(
            ok=False,
            http_status=None,
            error_class="NETWORK_UNKNOWN",
            error_detail="simulated unknown network error",
            simulated=True,
            network_calls=0,
        ),
    }
    return mapping[name]
