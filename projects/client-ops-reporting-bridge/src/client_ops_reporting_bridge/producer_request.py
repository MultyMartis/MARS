"""Outbound HTTP request builder (representation only; no network)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Mapping, Optional

from .producer_config import ProducerProfile, ProducerSecrets
from .producer_constants import AUTH_HEADER_NAME, CONTENT_TYPE_JSON


@dataclass(frozen=True)
class OutboundRequest:
    """Logical outbound request. Never stores full production URL with secret."""

    method: str
    host_class: str
    route_configured: bool
    content_type: str
    auth_header_name: str
    auth_header_present: bool
    body: dict[str, Any]
    connect_timeout_ms: int
    request_timeout_ms: int
    # Redacted header map for evidence / tests
    headers_redacted: Mapping[str, str]

    def body_json(self) -> str:
        return json.dumps(self.body, ensure_ascii=False, separators=(",", ":"), sort_keys=True)

    def sanitized_dict(self) -> dict[str, Any]:
        return {
            "method": self.method,
            "host_class": self.host_class,
            "route_configured": self.route_configured,
            "content_type": self.content_type,
            "auth_header_name": self.auth_header_name,
            "auth_header_present": self.auth_header_present,
            "headers_redacted": dict(self.headers_redacted),
            "body_event_id": self.body.get("event_id"),
            "body_schema_name": self.body.get("schema_name"),
            "connect_timeout_ms": self.connect_timeout_ms,
            "request_timeout_ms": self.request_timeout_ms,
        }


def build_outbound_request(
    envelope: Mapping[str, Any],
    profile: ProducerProfile,
    secrets: Optional[ProducerSecrets] = None,
    *,
    require_auth: bool = False,
) -> OutboundRequest:
    """Build a POST representation for the Client Ops webhook.

    Does not perform DNS or HTTP. Full URL is never assembled into logs.
    """
    auth_present = False
    auth_value: Optional[str] = None
    if secrets is not None and secrets.auth_secret_present:
        auth_value = secrets.get_auth_secret()
        auth_present = bool(auth_value)

    if require_auth and not auth_present:
        raise ValueError("auth secret required but missing")

    headers_redacted = {
        "Content-Type": CONTENT_TYPE_JSON,
        AUTH_HEADER_NAME: "<redacted>" if auth_present else "<absent>",
    }

    body = dict(envelope)
    return OutboundRequest(
        method="POST",
        host_class=profile.host_class,
        route_configured=bool(profile.webhook_route),
        content_type=CONTENT_TYPE_JSON,
        auth_header_name=AUTH_HEADER_NAME,
        auth_header_present=auth_present,
        body=body,
        connect_timeout_ms=profile.connect_timeout_ms,
        request_timeout_ms=profile.request_timeout_ms,
        headers_redacted=headers_redacted,
    )


def assert_no_secret_leak(text: str, secret: Optional[str]) -> bool:
    """Return True if secret is absent from text (True also when secret empty)."""
    if not secret:
        return True
    return secret not in text
