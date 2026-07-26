"""Phase 1B-D3 gated real HTTPS transport for controlled producer POST.

Importing this module does not open network connections.
Live dispatch requires D3LiveAuthorization.assert_live_allowed().
"""

from __future__ import annotations

import json
import socket
import ssl
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from typing import Any, Optional
from urllib.parse import urlparse, urlunparse

from .producer_config import ProducerProfile, ProducerSecrets
from .producer_constants import (
    AUTH_HEADER_NAME,
    CONTENT_TYPE_JSON,
    D3_APPROVED_HOST,
    D3_ROUTE_PREFIX,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
    TRANSPORT_HTTP,
)
from .producer_d3_gates import D3GateError, D3LiveAuthorization
from .producer_d5_gates import D5GateError, D5LiveAuthorization
from .producer_request import OutboundRequest
from .producer_transport import TransportResponse

LiveAuthorization = D3LiveAuthorization | D5LiveAuthorization


class EndpointAllowlistError(ValueError):
    """Endpoint failed D3 allowlist validation (sanitized message only)."""


@dataclass(frozen=True)
class AllowedEndpoint:
    """Validated endpoint identity — never log .url."""

    scheme: str
    host: str
    path: str
    port: Optional[int]
    route_class_ok: bool
    # Private: callers must not print.
    _url: str = field(repr=False, compare=False)

    def sanitized_dict(self) -> dict[str, Any]:
        return {
            "scheme": self.scheme,
            "host_approved": self.host == D3_APPROVED_HOST,
            "host_len": len(self.host),
            "path_prefix_ok": self.path.startswith(D3_ROUTE_PREFIX),
            "route_class_ok": self.route_class_ok,
            "port": self.port,
            "query_present": False,
            "fragment_present": False,
            "userinfo_present": False,
        }


def compose_webhook_url(profile: ProducerProfile) -> str:
    """Compose URL from ignored profile parts (not for logging)."""
    base = (profile.webhook_base or "").rstrip("/")
    route = profile.webhook_route or ""
    if not route.startswith("/"):
        route = "/" + route
    # If base already ends with /webhook and route is full path, join carefully
    if route.startswith("/webhook/") and base.endswith("/webhook"):
        # unusual — treat route as absolute path on host
        parsed = urlparse(base)
        return urlunparse((parsed.scheme, parsed.netloc, route, "", "", ""))
    return f"{base}{route}"


def validate_and_allow_endpoint(profile: ProducerProfile) -> AllowedEndpoint:
    """Validate HTTPS Client Ops webhook endpoint from ignored profile."""
    if not profile.webhook_base or not profile.webhook_route:
        raise EndpointAllowlistError("endpoint profile incomplete")
    if "?" in profile.webhook_base or "#" in profile.webhook_base:
        raise EndpointAllowlistError("base must not include query or fragment")
    if "://" in profile.webhook_route or "?" in profile.webhook_route or "#" in profile.webhook_route:
        raise EndpointAllowlistError("route must be a path segment")

    url = compose_webhook_url(profile)
    parsed = urlparse(url)

    if parsed.scheme != "https":
        raise EndpointAllowlistError("scheme must be https")
    if parsed.username or parsed.password:
        raise EndpointAllowlistError("userinfo forbidden")
    if parsed.query:
        raise EndpointAllowlistError("query string forbidden")
    if parsed.fragment:
        raise EndpointAllowlistError("fragment forbidden")

    host = (parsed.hostname or "").lower()
    if not host:
        raise EndpointAllowlistError("host missing")
    if host in {"localhost", "127.0.0.1", "::1"}:
        raise EndpointAllowlistError("localhost forbidden")
    if host != D3_APPROVED_HOST:
        raise EndpointAllowlistError("host not on allowlist")

    path = parsed.path or ""
    if not path.startswith(D3_ROUTE_PREFIX):
        raise EndpointAllowlistError("route class invalid")
    if ".." in path:
        raise EndpointAllowlistError("path traversal forbidden")

    port = parsed.port
    if port is not None and port != 443:
        raise EndpointAllowlistError("unexpected port")

    # Rebuild without query/fragment to be safe
    clean = urlunparse(("https", host if port is None else f"{host}:{port}", path, "", "", ""))
    return AllowedEndpoint(
        scheme="https",
        host=host,
        path=path,
        port=port,
        route_class_ok=True,
        _url=clean,
    )


class _NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        raise EndpointAllowlistError("redirects are not followed")


@dataclass
class LiveHttpTransport:
    """Synchronous HTTPS POST — one request at a time; no library retries."""

    endpoint: AllowedEndpoint
    auth_secret: str
    connect_timeout_s: float
    read_timeout_s: float
    authorization: LiveAuthorization
    mode: str = TRANSPORT_HTTP
    network_calls: int = 0
    tls_verify: bool = True  # cannot be disabled for live D3/D5

    def dispatch(self, request: OutboundRequest) -> TransportResponse:
        self.authorization.assert_live_allowed()
        if not self.tls_verify:
            raise D3GateError("TLS verification cannot be disabled")
        if not request.auth_header_present:
            raise D3GateError("auth header required for live POST")
        if not self.auth_secret:
            raise D3GateError("auth secret empty")

        body_bytes = request.body_json().encode("utf-8")
        headers = {
            "Content-Type": CONTENT_TYPE_JSON,
            "Accept": "application/json",
            AUTH_HEADER_NAME: self.auth_secret,
        }
        req = urllib.request.Request(
            self.endpoint._url,
            data=body_bytes,
            headers=headers,
            method="POST",
        )
        ctx = ssl.create_default_context()
        opener = urllib.request.build_opener(
            _NoRedirectHandler(),
            urllib.request.HTTPSHandler(context=ctx),
        )
        timeout = max(self.connect_timeout_s, 0.1) + max(self.read_timeout_s, 0.1)
        # urllib uses a single timeout; prefer request timeout bound
        timeout = max(self.read_timeout_s, self.connect_timeout_s)

        self.network_calls += 1
        try:
            with opener.open(req, timeout=timeout) as resp:
                raw = resp.read(8192).decode("utf-8", errors="replace")
                status = getattr(resp, "status", None) or resp.getcode()
                body = _parse_bounded_json(raw)
                return TransportResponse(
                    ok=200 <= int(status) < 300,
                    http_status=int(status),
                    body=body,
                    raw_body=None if body is not None else raw[:512],
                    simulated=False,
                    network_calls=1,
                    headers={},
                )
        except EndpointAllowlistError as exc:
            return TransportResponse(
                ok=False,
                error_class="UNEXPECTED_RESPONSE",
                error_detail=str(exc),
                simulated=False,
                network_calls=1,
            )
        except ssl.SSLError:
            return TransportResponse(
                ok=False,
                error_class="TLS_FAILURE",
                error_detail="tls failure",
                simulated=False,
                network_calls=1,
            )
        except socket.timeout:
            return TransportResponse(
                ok=False,
                error_class="READ_TIMEOUT_AMBIGUOUS",
                error_detail="read timeout after possible send",
                simulated=False,
                network_calls=1,
            )
        except urllib.error.HTTPError as exc:
            raw = ""
            try:
                raw = exc.read(8192).decode("utf-8", errors="replace")
            except Exception:  # noqa: BLE001
                raw = ""
            body = _parse_bounded_json(raw)
            status = int(exc.code)
            if status in {301, 302, 303, 307, 308}:
                return TransportResponse(
                    ok=False,
                    http_status=status,
                    error_class="UNEXPECTED_RESPONSE",
                    error_detail="redirect rejected",
                    simulated=False,
                    network_calls=1,
                )
            return TransportResponse(
                ok=False,
                http_status=status,
                body=body,
                raw_body=None if body is not None else raw[:512],
                simulated=False,
                network_calls=1,
            )
        except urllib.error.URLError as exc:
            reason = str(getattr(exc, "reason", exc))
            low = reason.lower()
            if "timed out" in low or "timeout" in low:
                ec = "READ_TIMEOUT_AMBIGUOUS"
            elif "name or service" in low or "getaddrinfo" in low or "nodename" in low:
                ec = "DNS_FAILURE"
            elif "ssl" in low or "certificate" in low:
                ec = "TLS_FAILURE"
            else:
                ec = "CONNECT_FAILURE"
            return TransportResponse(
                ok=False,
                error_class=ec,
                error_detail="network error",
                simulated=False,
                network_calls=1,
            )
        except OSError:
            return TransportResponse(
                ok=False,
                error_class="CONNECT_FAILURE",
                error_detail="os connect failure",
                simulated=False,
                network_calls=1,
            )


def create_d3_live_transport(
    *,
    profile: ProducerProfile,
    secrets: ProducerSecrets,
    authorization: D3LiveAuthorization,
) -> LiveHttpTransport:
    """Create live transport only after authorization gates pass."""
    authorization.assert_live_allowed()
    if not secrets.auth_secret_present:
        raise D3GateError("auth secret missing")
    secret = secrets.get_auth_secret() or ""
    if not secret:
        raise D3GateError("auth secret empty")
    endpoint = validate_and_allow_endpoint(profile)
    return LiveHttpTransport(
        endpoint=endpoint,
        auth_secret=secret,
        connect_timeout_s=profile.connect_timeout_ms / 1000.0,
        read_timeout_s=profile.request_timeout_ms / 1000.0,
        authorization=authorization,
    )


def create_d5_live_transport(
    *,
    profile: ProducerProfile,
    secrets: ProducerSecrets,
    authorization: D5LiveAuthorization,
) -> LiveHttpTransport:
    """Create D5 live transport — reuses D3 HTTPS allowlist/transport."""
    authorization.assert_live_allowed()
    if not secrets.auth_secret_present:
        raise D5GateError("auth secret missing")
    secret = secrets.get_auth_secret() or ""
    if not secret:
        raise D5GateError("auth secret empty")
    endpoint = validate_and_allow_endpoint(profile)
    return LiveHttpTransport(
        endpoint=endpoint,
        auth_secret=secret,
        connect_timeout_s=profile.connect_timeout_ms / 1000.0,
        read_timeout_s=profile.request_timeout_ms / 1000.0,
        authorization=authorization,
    )


def _parse_bounded_json(raw: str) -> Optional[dict[str, Any]]:
    if not raw:
        return None
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    # Bound to business fields only for producer classification
    allowed = {
        "result",
        "dedupe_result",
        "event_id",
        "message",
        "error",
        "hint",
        "status",
    }
    return {k: data[k] for k in data.keys() if k in allowed}


def assert_no_url_leak(text: str, url: str) -> bool:
    if not url:
        return True
    if url in text:
        return False
    # also reject host+path concatenation fragments beyond approved host alone
    parsed = urlparse(url)
    if parsed.path and len(parsed.path) > 8 and parsed.path in text:
        return False
    return True


# Re-export for clarity in evidence
__all__ = [
    "AllowedEndpoint",
    "EndpointAllowlistError",
    "LiveHttpTransport",
    "assert_no_url_leak",
    "compose_webhook_url",
    "create_d3_live_transport",
    "create_d5_live_transport",
    "validate_and_allow_endpoint",
    "NETWORK_DISPATCH_NOT_AUTHORIZED_D3",
]
