"""Sanitized local evidence writer (atomic replace when possible)."""

from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any, Mapping, Optional

from .producer_result import ProducerResult
from .security_validator import redact_for_diagnostics

_FORBIDDEN_EVIDENCE_KEYS = frozenset(
    {
        "authorization",
        "token",
        "secret",
        "password",
        "api_key",
        "cookie",
        "webhook_url",
        "full_url",
        "raw_monitor",
        "stack_trace",
        "env_dump",
    }
)

_ABS_PATH = re.compile(r"[A-Za-z]:\\")
_URL = re.compile(r"https?://[^\s\"']+", re.I)


class EvidenceSecurityError(ValueError):
    """Evidence payload failed sanitization gates."""


def _scan_strings(value: Any, path: str = "") -> list[str]:
    issues: list[str] = []
    if isinstance(value, dict):
        for k, v in value.items():
            lk = str(k).lower()
            # Allow documenting the Header Auth *name* when value is redacted.
            if lk == "x-mars-client-ops-token" and str(v) in {
                "<redacted>",
                "<absent>",
            }:
                continue
            if lk in _FORBIDDEN_EVIDENCE_KEYS or any(
                f in lk
                for f in (
                    "password",
                    "secret",
                    "authorization",
                    "api_key",
                    "webhook_url",
                    "full_url",
                )
            ):
                # "token" alone is too broad (header name contains Token)
                if lk.endswith("_token") or lk in {"token", "bot_token"}:
                    if str(v) not in {"<redacted>", "<absent>", "null", "None"}:
                        issues.append(
                            f"forbidden_key:{path}.{k}" if path else f"forbidden_key:{k}"
                        )
                elif "token" not in lk:
                    issues.append(
                        f"forbidden_key:{path}.{k}" if path else f"forbidden_key:{k}"
                    )
                elif str(v) not in {"<redacted>", "<absent>"}:
                    issues.append(
                        f"forbidden_key:{path}.{k}" if path else f"forbidden_key:{k}"
                    )
            issues.extend(_scan_strings(v, f"{path}.{k}" if path else str(k)))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            issues.extend(_scan_strings(v, f"{path}[{i}]"))
    elif isinstance(value, str):
        if _ABS_PATH.search(value):
            issues.append(f"path:{path}")
        if _URL.search(value) and "example" not in value.lower():
            # Allow only clearly placeholder hosts
            if not any(
                x in value.lower()
                for x in ("example.com", "localhost", "invalid.invalid")
            ):
                issues.append(f"url:{path}")
    return issues


def build_evidence_document(
    result: ProducerResult,
    *,
    phase: str = "1B-D2",
) -> dict[str, Any]:
    doc = {
        "phase": phase,
        "schema": "mars.client_ops.producer_evidence",
        "schema_version": "1.0",
        "result": result.to_sanitized_dict(),
        "redaction_status": "redacted",
        "notes": {
            "intake_vs_telegram": (
                "HTTP 202 / intake_accepted does not imply Telegram SENT"
            ),
            "n8n_execution_id": None,
            "telegram_message_id": None,
        },
    }
    issues = _scan_strings(doc)
    if issues:
        raise EvidenceSecurityError(
            "evidence sanitization failed: " + ",".join(issues[:5])
        )
    return doc


def write_evidence_atomic(
    path: Path,
    document: Mapping[str, Any],
) -> Path:
    """Write JSON evidence via temp file + replace."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    # Final scan on serialized text for absolute paths / obvious secrets shapes
    if _ABS_PATH.search(text):
        text = _ABS_PATH.sub("<REDACTED_PATH>", text)
    fd, tmp_name = tempfile.mkstemp(
        prefix=".producer-evidence-",
        suffix=".json.tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
    return path


def write_producer_evidence(
    result: ProducerResult,
    evidence_dir: Path,
    *,
    filename: Optional[str] = None,
) -> Path:
    doc = build_evidence_document(result)
    name = filename or f"{result.producer_run_id}.json"
    # Keep filenames basename-only
    name = Path(name).name
    out = Path(evidence_dir) / name
    return write_evidence_atomic(out, doc)


def sanitize_error_message(exc: BaseException, max_len: int = 120) -> str:
    return redact_for_diagnostics(f"{type(exc).__name__}: {exc}", max_len=max_len)
