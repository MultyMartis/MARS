"""SITE-002-specific source firewall (before generic producer firewall)."""

from __future__ import annotations

from typing import Any, Mapping

from .site002_adapter_constants import (
    ALWAYS_STRIP_KEYS,
    ARTIFACT_ALLOWLISTS,
    REJECT_KEY_FRAGMENTS,
)


class Site002AdapterFirewallError(ValueError):
    """Raised when SITE-002 source violates the adapter firewall."""


def _is_reject_key(key: str) -> bool:
    lk = str(key).lower()
    if lk in ALWAYS_STRIP_KEYS:
        return False
    for frag in REJECT_KEY_FRAGMENTS:
        if frag in lk:
            return True
    # Absolute path carriers beyond allowlist
    if lk.endswith("_path") or lk.endswith("_paths") or lk == "path":
        return True
    return False


def firewall_artifact_document(
    artifact_name: str,
    document: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Allowlist + reject/strip SITE-002 artifact keys.

    Returns ``(cleaned_document, redaction_result)``.
    Never returns raw path/credential fields.
    """
    if not isinstance(document, Mapping):
        raise Site002AdapterFirewallError(
            f"{artifact_name}: artifact must be a JSON object"
        )

    allow = ARTIFACT_ALLOWLISTS.get(artifact_name)
    if allow is None:
        raise Site002AdapterFirewallError(
            f"unsupported artifact for adapter firewall: {artifact_name}"
        )

    stripped: list[str] = []
    rejected: list[str] = []
    cleaned: dict[str, Any] = {}

    for key, value in document.items():
        sk = str(key)
        lk = sk.lower()

        if lk in ALWAYS_STRIP_KEYS or sk in ALWAYS_STRIP_KEYS:
            stripped.append(sk)
            continue

        if _is_reject_key(sk):
            # Security-sensitive unexpected field → fail closed
            rejected.append(sk)
            continue

        if sk not in allow:
            # Harmless unknown presentation metadata → strip
            stripped.append(sk)
            continue

        if isinstance(value, dict):
            # Nested objects only allowed for added_page_types counts
            if sk == "added_page_types":
                nested: dict[str, Any] = {}
                for nk, nv in value.items():
                    if _is_reject_key(str(nk)):
                        rejected.append(f"{sk}.{nk}")
                        continue
                    if isinstance(nv, (int, float, str)) and not isinstance(nv, bool):
                        nested[str(nk)] = nv
                    else:
                        stripped.append(f"{sk}.{nk}")
                cleaned[sk] = nested
            else:
                stripped.append(sk)
            continue

        if isinstance(value, list):
            # No list propagation into adapter contract (URLs/logs)
            stripped.append(sk)
            continue

        cleaned[sk] = value

    if rejected:
        raise Site002AdapterFirewallError(
            f"{artifact_name}: rejected security-sensitive keys: "
            + ",".join(sorted(rejected))
        )

    redaction = {
        "artifact": artifact_name,
        "stripped_keys": sorted(stripped),
        "rejected_keys": [],
        "allowlist_size": len(allow),
        "output_keys": sorted(cleaned.keys()),
    }
    return cleaned, redaction


def assert_no_raw_passthrough(producer_input: Mapping[str, Any]) -> None:
    """Fail if producer input still carries raw source / path / secret markers."""
    blob = str(producer_input).lower()
    forbidden_snippets = (
        "artifact_paths",
        "x:\\ai mars storage",
        "password",
        "authorization:",
        "begin private key",
        "api.telegram.org/bot",
    )
    for snip in forbidden_snippets:
        if snip in blob:
            raise Site002AdapterFirewallError(
                f"raw source leakage detected in producer input ({snip})"
            )
