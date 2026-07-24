"""Producer configuration loading (ignored local boundaries only)."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Optional

from .producer_constants import (
    DEFAULT_CONNECT_TIMEOUT_MS,
    DEFAULT_ENVIRONMENT,
    DEFAULT_HOST_CLASS,
    DEFAULT_MAX_RETRIES,
    DEFAULT_REQUEST_TIMEOUT_MS,
    LOCAL_SITE_REL,
    MAX_TIMEOUT_MS,
    MIN_TIMEOUT_MS,
    PRODUCER_PROFILE_FILENAME,
    SECRET_KEY_WEBHOOK_AUTH,
    SECRETS_FILENAME,
)


class ProducerConfigError(ValueError):
    """Invalid producer configuration (sanitized messages only)."""


@dataclass(frozen=True)
class ProducerProfile:
    """Non-secret producer profile (safe to log after sanitization)."""

    webhook_base: str
    webhook_route: str
    request_timeout_ms: int
    connect_timeout_ms: int
    environment: str
    site_id: str
    max_retries: int
    concurrency: int
    host_class: str
    profile_path: Optional[str] = None

    def sanitized_dict(self) -> dict[str, Any]:
        return {
            "host_class": self.host_class,
            "route_configured": bool(self.webhook_route),
            "base_configured": bool(self.webhook_base),
            "request_timeout_ms": self.request_timeout_ms,
            "connect_timeout_ms": self.connect_timeout_ms,
            "environment": self.environment,
            "site_id": self.site_id,
            "max_retries": self.max_retries,
            "concurrency": self.concurrency,
            # Never expose full URL
            "endpoint_identity": {
                "host_class": self.host_class,
                "route_configured": bool(self.webhook_route),
            },
        }


@dataclass(frozen=True)
class ProducerSecrets:
    """Secret material — never log or serialize values."""

    auth_secret_present: bool
    # Internal only; callers must not print.
    _auth_secret: Optional[str] = None

    def get_auth_secret(self) -> Optional[str]:
        return self._auth_secret


def default_local_site_dir(repo_root: Path) -> Path:
    return Path(repo_root) / "local" / LOCAL_SITE_REL


def default_secrets_path(repo_root: Path) -> Path:
    return default_local_site_dir(repo_root) / SECRETS_FILENAME


def default_profile_path(repo_root: Path) -> Path:
    return default_local_site_dir(repo_root) / PRODUCER_PROFILE_FILENAME


def _parse_timeout(value: Any, *, field: str, default: int) -> int:
    if value is None:
        return default
    try:
        n = int(value)
    except (TypeError, ValueError) as exc:
        raise ProducerConfigError(f"invalid {field}: not an integer") from exc
    if n <= 0:
        raise ProducerConfigError(f"invalid {field}: must be positive")
    if n < MIN_TIMEOUT_MS or n > MAX_TIMEOUT_MS:
        raise ProducerConfigError(
            f"invalid {field}: must be within {MIN_TIMEOUT_MS}..{MAX_TIMEOUT_MS}"
        )
    return n


def parse_producer_profile(
    raw: Mapping[str, Any],
    *,
    profile_path: Optional[str] = None,
) -> ProducerProfile:
    """Parse and validate a producer.local.json object."""
    base = str(raw.get("webhook_base") or raw.get("CLIENT_OPS_WEBHOOK_BASE") or "").strip()
    route = str(
        raw.get("webhook_route") or raw.get("CLIENT_OPS_WEBHOOK_ROUTE") or ""
    ).strip()
    # Reject accidental full-URL-only config that embeds query secrets
    if "://" in route or "?" in route:
        raise ProducerConfigError("webhook_route must be a path segment, not a URL")
    if base and ("?" in base or "#" in base):
        raise ProducerConfigError("webhook_base must not include query or fragment")

    env = str(
        raw.get("environment") or raw.get("CLIENT_OPS_ENVIRONMENT") or DEFAULT_ENVIRONMENT
    ).strip()
    if env not in {"sandbox", "staging", "production"}:
        raise ProducerConfigError("invalid environment")

    site_id = str(raw.get("site_id") or raw.get("CLIENT_OPS_SITE_ID") or "SITE-002").strip()
    host_class = str(raw.get("host_class") or DEFAULT_HOST_CLASS).strip() or DEFAULT_HOST_CLASS

    max_retries = raw.get("max_retries", raw.get("CLIENT_OPS_RETRY_MAX", DEFAULT_MAX_RETRIES))
    try:
        max_retries_i = int(max_retries)
    except (TypeError, ValueError) as exc:
        raise ProducerConfigError("invalid max_retries") from exc
    if max_retries_i < 0 or max_retries_i > 10:
        raise ProducerConfigError("invalid max_retries bounds")
    # D2 policy: automatic retries remain disabled even if profile sets >0
    # (enforced at dispatch; profile may store future value).

    concurrency = raw.get("concurrency", 1)
    try:
        concurrency_i = int(concurrency)
    except (TypeError, ValueError) as exc:
        raise ProducerConfigError("invalid concurrency") from exc
    if concurrency_i != 1:
        raise ProducerConfigError("concurrency must be 1 (sequential only)")

    req_to = _parse_timeout(
        raw.get("request_timeout_ms", raw.get("CLIENT_OPS_REQUEST_TIMEOUT_MS")),
        field="request_timeout_ms",
        default=DEFAULT_REQUEST_TIMEOUT_MS,
    )
    conn_to = _parse_timeout(
        raw.get("connect_timeout_ms", raw.get("CLIENT_OPS_CONNECT_TIMEOUT_MS")),
        field="connect_timeout_ms",
        default=DEFAULT_CONNECT_TIMEOUT_MS,
    )
    if conn_to > req_to:
        raise ProducerConfigError("connect_timeout_ms must not exceed request_timeout_ms")

    return ProducerProfile(
        webhook_base=base,
        webhook_route=route,
        request_timeout_ms=req_to,
        connect_timeout_ms=conn_to,
        environment=env,
        site_id=site_id,
        max_retries=max_retries_i,
        concurrency=concurrency_i,
        host_class=host_class,
        profile_path=profile_path,
    )


def load_producer_profile(path: Path) -> ProducerProfile:
    if not path.is_file():
        raise ProducerConfigError("producer profile missing")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ProducerConfigError("producer profile malformed JSON") from exc
    if not isinstance(raw, dict):
        raise ProducerConfigError("producer profile must be an object")
    return parse_producer_profile(raw, profile_path=str(path.name))


def load_env_file(path: Path) -> dict[str, str]:
    """Parse KEY=VALUE env file; values are returned but must not be printed."""
    if not path.is_file():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        trimmed = line.strip()
        if not trimmed or trimmed.startswith("#"):
            continue
        if "=" not in trimmed:
            continue
        key, _, value = trimmed.partition("=")
        key = key.strip()
        value = value.strip()
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        out[key] = value
    return out


def load_producer_secrets(path: Path) -> ProducerSecrets:
    env = load_env_file(path)
    secret = env.get(SECRET_KEY_WEBHOOK_AUTH) or os.environ.get(SECRET_KEY_WEBHOOK_AUTH)
    present = bool(secret)
    return ProducerSecrets(auth_secret_present=present, _auth_secret=secret if present else None)


def offline_default_profile() -> ProducerProfile:
    """Deterministic in-memory profile for dry-run without local files."""
    return ProducerProfile(
        webhook_base="",
        webhook_route="/webhook/client-ops-sandbox",
        request_timeout_ms=DEFAULT_REQUEST_TIMEOUT_MS,
        connect_timeout_ms=DEFAULT_CONNECT_TIMEOUT_MS,
        environment=DEFAULT_ENVIRONMENT,
        site_id="SITE-002",
        max_retries=DEFAULT_MAX_RETRIES,
        concurrency=1,
        host_class=DEFAULT_HOST_CLASS,
        profile_path=None,
    )
