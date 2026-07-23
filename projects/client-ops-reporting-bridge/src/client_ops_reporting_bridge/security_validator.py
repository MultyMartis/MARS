"""Deterministic security validation for distributable envelopes."""

from __future__ import annotations

import re
from typing import Any, Iterable, Optional

from .constants import FORBIDDEN_ENVELOPE_TOP_LEVEL_KEYS
from .errors import ValidationIssue

# Patterns that must never appear in distributable string fields.
_WINDOWS_ABS = re.compile(r"[A-Za-z]:\\")
_UNC = re.compile(r"\\\\[^\s\\/]+\\")
_URI_CREDS = re.compile(r"[a-zA-Z][a-zA-Z0-9+.-]*://[^/\s]*:[^/\s]*@")
_TOKENISH = re.compile(
    r"(?i)(\b(api[_-]?key|bot[_-]?token|access[_-]?token|secret[_-]?key|"
    r"bearer\s+[A-Za-z0-9\-._~+/]+=*)\b|"
    r"\b\d{8,10}:[A-Za-z0-9_-]{30,}\b)"  # telegram-like token shape (synthetic)
)
_STACK = re.compile(r"(?m)^(Traceback \(most recent call last\):|\s+File \".+\", line \d+)")
_RAW_LOG_BLOCK = re.compile(r"(?i)-----BEGIN (RSA |OPENSSH )?PRIVATE KEY-----")


def redact_for_diagnostics(text: str, max_len: int = 80) -> str:
    """Redact potentially sensitive substrings for test/CLI diagnostics."""
    cleaned = _WINDOWS_ABS.sub("<REDACTED_PATH>", text)
    cleaned = _UNC.sub(r"<REDACTED_UNC>", cleaned)
    cleaned = _URI_CREDS.sub("<REDACTED_URI>", cleaned)
    cleaned = _TOKENISH.sub("<REDACTED_TOKEN>", cleaned)
    if len(cleaned) > max_len:
        return cleaned[: max_len - 3] + "..."
    return cleaned


def _iter_strings(value: Any, prefix: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield prefix, value
    elif isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            yield from _iter_strings(child, path)
    elif isinstance(value, list):
        for idx, child in enumerate(value):
            yield from _iter_strings(child, f"{prefix}[{idx}]")


def validate_envelope_security(
    envelope: dict[str, Any],
) -> list[ValidationIssue]:
    """Return issues if envelope must not be distributed.

    Does not echo rejected sensitive content into issue messages.
    """
    issues: list[ValidationIssue] = []

    for key in envelope.keys():
        if str(key).lower() in FORBIDDEN_ENVELOPE_TOP_LEVEL_KEYS:
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_SECRET_MARKER_DETECTED",
                    message="unexpected sensitive top-level key",
                    field=str(key),
                )
            )

    security = envelope.get("security")
    if not isinstance(security, dict):
        issues.append(
            ValidationIssue(
                code="SECURITY_FLAGS_INVALID",
                message="security block missing",
            )
        )
    else:
        if security.get("contains_secrets") is not False:
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_SECRET_MARKER_DETECTED",
                    message="contains_secrets must be false",
                    field="security.contains_secrets",
                )
            )
        if security.get("redacted") is not True:
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_NOT_REDACTED",
                    message="redacted must be true",
                    field="security.redacted",
                )
            )

    for path, text in _iter_strings(envelope):
        if _WINDOWS_ABS.search(text) or _UNC.search(text):
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_PATH_DETECTED",
                    message="absolute or UNC path detected",
                    field=path,
                )
            )
        if _URI_CREDS.search(text):
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_SECRET_MARKER_DETECTED",
                    message="credential URI detected",
                    field=path,
                )
            )
        if _TOKENISH.search(text):
            issues.append(
                ValidationIssue(
                    code="ENVELOPE_SECRET_MARKER_DETECTED",
                    message="token-like marker detected",
                    field=path,
                )
            )
        if _STACK.search(text):
            issues.append(
                ValidationIssue(
                    code="RAW_LOG_DETECTED",
                    message="stack trace pattern detected",
                    field=path,
                )
            )
        if _RAW_LOG_BLOCK.search(text):
            issues.append(
                ValidationIssue(
                    code="RAW_LOG_DETECTED",
                    message="raw secret block detected",
                    field=path,
                )
            )

    # Deduplicate by (code, field)
    seen: set[tuple[str, Optional[str]]] = set()
    unique: list[ValidationIssue] = []
    for issue in issues:
        key = (issue.code, issue.field)
        if key in seen:
            continue
        seen.add(key)
        unique.append(issue)
    return unique


def is_distributable(envelope: dict[str, Any]) -> bool:
    return not validate_envelope_security(envelope)
