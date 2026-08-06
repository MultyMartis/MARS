"""Phase 1B-D5 confirmation gates and one-time real-source charter state.

No network on import. Live HTTP requires every gate below.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from .producer_constants import (
    D5_ALLOWED_ENVIRONMENTS,
    D5_CHARTER_STATE_FILENAME,
    D5_ENABLE_PHRASE,
    D5_MAX_REAL_REQUESTS,
    D5_PRODUCER_MARKER,
    D5_REAL_SOURCE_CHARTER_CONSUMED,
    D5_RUNS_REL,
    D5_SEND_PHRASE,
    D5_SOURCE_PROVENANCE,
    LOCAL_SITE_REL,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
    SECOND_REAL_SOURCE_POST_NOT_AUTHORIZED,
)
from .site002_adapter_constants import SOURCE_CONTRACT_VERSION


class D5GateError(RuntimeError):
    """D5 live gate rejected."""

    def __init__(self, detail: str, *, code: Optional[str] = None) -> None:
        resolved = code or NETWORK_DISPATCH_NOT_AUTHORIZED_D5
        super().__init__(f"{resolved}: {detail}")
        self.code = resolved
        self.detail = detail


@dataclass(frozen=True)
class D5LiveAuthorization:
    """Proven authorization bundle for one controlled real-source live dispatch."""

    enable_phrase_ok: bool
    apply: bool
    send_phrase: str
    environment: str
    site_id: str
    domain: str
    source_contract: str
    source_provenance: str
    concurrency: int
    max_retries: int
    automatic_retry: bool
    producer_marker_present: bool
    profile_present: bool
    secret_present: bool
    dry_run: bool
    source_path_ok: bool
    preview_approved: bool
    event_unseen: bool
    d3_charter_consumed: bool
    d4_live_blocked: bool

    def assert_live_allowed(self) -> None:
        if self.dry_run:
            raise D5GateError("dry_run cannot reach live HTTP")
        if not self.apply:
            raise D5GateError("missing --apply")
        if not self.enable_phrase_ok:
            raise D5GateError("enable confirmation phrase mismatch")
        if self.send_phrase != D5_SEND_PHRASE:
            raise D5GateError("send confirmation phrase mismatch")
        if self.environment not in D5_ALLOWED_ENVIRONMENTS:
            raise D5GateError("environment not manual_real_source_controlled")
        if self.site_id != "SITE-002":
            raise D5GateError("site_id must be SITE-002")
        if self.domain != "bzpm.ru":
            raise D5GateError("domain must be bzpm.ru")
        if self.source_contract != SOURCE_CONTRACT_VERSION:
            raise D5GateError("source contract mismatch")
        if self.source_provenance != D5_SOURCE_PROVENANCE:
            raise D5GateError("source provenance mismatch")
        if self.concurrency != 1:
            raise D5GateError("concurrency must be 1")
        if self.max_retries != 0:
            raise D5GateError("max_retries must be 0")
        if self.automatic_retry:
            raise D5GateError("automatic_retry must be false")
        if not self.producer_marker_present:
            raise D5GateError("D5 producer marker missing")
        if not self.profile_present:
            raise D5GateError("producer profile missing")
        if not self.secret_present:
            raise D5GateError("auth secret missing")
        if not self.source_path_ok:
            raise D5GateError("source path not approved")
        if not self.preview_approved:
            raise D5GateError("source preview not approved")
        if not self.event_unseen:
            raise D5GateError("event_id already present in Data Table")
        if not self.d3_charter_consumed:
            raise D5GateError("D3 charter must remain consumed")
        if not self.d4_live_blocked:
            raise D5GateError("D4 live mode must remain blocked")


_RUN_DIR_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$")


def default_d5_runs_dir(repo_root: Path) -> Path:
    return Path(repo_root) / "local" / LOCAL_SITE_REL / D5_RUNS_REL


def charter_state_path(runs_dir: Path) -> Path:
    return Path(runs_dir) / D5_CHARTER_STATE_FILENAME


def load_charter_state(runs_dir: Path) -> dict[str, Any]:
    path = charter_state_path(runs_dir)
    if not path.is_file():
        return {
            "phase": "1B-D5",
            "charter_created": False,
            "charter_consumed": False,
            "real_http_requests": 0,
            "event_id": None,
            "source_label": None,
            "source_preview_verdict": None,
            "workflow_activation_status": "inactive",
        }
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise D5GateError("charter state malformed")
    return raw


def save_charter_state(runs_dir: Path, state: dict[str, Any]) -> None:
    runs_dir = Path(runs_dir)
    runs_dir.mkdir(parents=True, exist_ok=True)
    path = charter_state_path(runs_dir)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def assert_request_budget(state: dict[str, Any]) -> None:
    used = int(state.get("real_http_requests") or 0)
    if state.get("charter_consumed"):
        raise D5GateError(
            SECOND_REAL_SOURCE_POST_NOT_AUTHORIZED,
            code=D5_REAL_SOURCE_CHARTER_CONSUMED,
        )
    if used >= D5_MAX_REAL_REQUESTS:
        raise D5GateError(
            SECOND_REAL_SOURCE_POST_NOT_AUTHORIZED,
            code=D5_REAL_SOURCE_CHARTER_CONSUMED,
        )


def record_successful_request(state: dict[str, Any], *, event_id: str) -> dict[str, Any]:
    out = dict(state)
    out["real_http_requests"] = int(out.get("real_http_requests") or 0) + 1
    out["event_id"] = event_id
    out["charter_consumed"] = True
    return out


def record_attempted_request(state: dict[str, Any], *, event_id: Optional[str]) -> dict[str, Any]:
    """Consume charter after any live attempt (no retry / no second POST)."""
    out = dict(state)
    out["real_http_requests"] = int(out.get("real_http_requests") or 0) + 1
    if event_id:
        out["event_id"] = event_id
    out["charter_consumed"] = True
    return out


def sanitize_source_label(source_dir: Path) -> str:
    """Sanitized label only — never absolute Storage path."""
    name = Path(source_dir).name
    if _RUN_DIR_RE.match(name):
        return f"site002-post-1c-run/{name}"
    return "site002-post-1c-run/<redacted>"


def resolve_approved_source_root() -> Path:
    """Canonical SITE-002 scheduled-monitor artifact root on X: Storage."""
    return Path(r"X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c")


def validate_explicit_source_path(source_dir: Path) -> Path:
    """Accept exactly one explicit completed run directory under approved root."""
    if source_dir is None:
        raise D5GateError("explicit source path required")
    raw = Path(source_dir)
    text = str(raw)
    if "*" in text or "?" in text:
        raise D5GateError("glob/wildcard source paths forbidden")
    if ".." in raw.parts:
        raise D5GateError("path traversal forbidden")
    name = raw.name.lower()
    if name in {"latest", "watch", "continuous"}:
        raise D5GateError("auto-discovery source names forbidden")
    if not _RUN_DIR_RE.match(raw.name):
        raise D5GateError("source must be an explicit completed run directory name")

    resolved = raw.resolve()
    root = resolve_approved_source_root().resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise D5GateError("source path outside approved SITE-002 monitor artifact root") from exc
    if resolved == root:
        raise D5GateError("source must be a single run directory, not the root")
    if not resolved.is_dir():
        raise D5GateError("source path is not a directory")
    # Reject sanitized fixture trees
    parts_l = {p.lower() for p in resolved.parts}
    if "site-002-real-source-adapter" in parts_l or (
        "fixtures" in parts_l and "client-ops-reporting-bridge" in parts_l
    ):
        raise D5GateError("sanitized fixture cannot authorize D5 real-source live")
    return resolved


def reject_forbidden_discovery_flags(*, latest: bool = False, watch: bool = False) -> None:
    if latest or watch:
        raise D5GateError("latest/watch/auto-discovery forbidden in D5")


def envelope_has_d5_marker(envelope: dict[str, Any]) -> bool:
    producer = envelope.get("producer") if isinstance(envelope.get("producer"), dict) else {}
    name = str(producer.get("name") or "")
    return name == D5_PRODUCER_MARKER


def build_authorization(
    *,
    enable_phrase: Optional[str],
    send_phrase: Optional[str],
    apply: bool,
    dry_run: bool,
    environment: str,
    site_id: str,
    domain: str,
    source_contract: str,
    source_provenance: str,
    concurrency: int,
    max_retries: int,
    automatic_retry: bool,
    producer_marker_present: bool,
    profile_present: bool,
    secret_present: bool,
    source_path_ok: bool,
    preview_approved: bool,
    event_unseen: bool,
    d3_charter_consumed: bool = True,
    d4_live_blocked: bool = True,
) -> D5LiveAuthorization:
    return D5LiveAuthorization(
        enable_phrase_ok=(enable_phrase == D5_ENABLE_PHRASE),
        apply=apply,
        send_phrase=send_phrase or "",
        environment=environment,
        site_id=site_id,
        domain=domain,
        source_contract=source_contract,
        source_provenance=source_provenance,
        concurrency=concurrency,
        max_retries=max_retries,
        automatic_retry=automatic_retry,
        producer_marker_present=producer_marker_present,
        profile_present=profile_present,
        secret_present=secret_present,
        dry_run=dry_run,
        source_path_ok=source_path_ok,
        preview_approved=preview_approved,
        event_unseen=event_unseen,
        d3_charter_consumed=d3_charter_consumed,
        d4_live_blocked=d4_live_blocked,
    )
