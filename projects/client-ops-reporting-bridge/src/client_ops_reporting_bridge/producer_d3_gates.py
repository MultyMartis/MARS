"""Phase 1B-D3 confirmation gates and one-time charter state.

No network on import. Live HTTP requires every gate below.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from .producer_constants import (
    D3_ALLOWED_ENVIRONMENTS,
    D3_CHARTER_STATE_FILENAME,
    D3_ENABLE_PHRASE,
    D3_MAX_REAL_REQUESTS,
    D3_PRODUCER_MARKER,
    D3_RUNS_REL,
    D3_SEND_FIRST_PHRASE,
    D3_SEND_REPLAY_PHRASE,
    LOCAL_SITE_REL,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
)


class D3GateError(RuntimeError):
    """D3 live gate rejected."""

    def __init__(self, detail: str) -> None:
        super().__init__(f"{NETWORK_DISPATCH_NOT_AUTHORIZED_D3}: {detail}")
        self.code = NETWORK_DISPATCH_NOT_AUTHORIZED_D3
        self.detail = detail


@dataclass(frozen=True)
class D3LiveAuthorization:
    """Proven authorization bundle for one controlled live dispatch."""

    enable_phrase_ok: bool
    apply: bool
    send_phrase: str
    mode: str  # first_seen | exact_replay
    environment: str
    concurrency: int
    max_retries: int
    producer_marker_present: bool
    profile_present: bool
    secret_present: bool
    dry_run: bool

    def assert_live_allowed(self) -> None:
        if self.dry_run:
            raise D3GateError("dry_run cannot reach live HTTP")
        if not self.apply:
            raise D3GateError("missing --apply")
        if not self.enable_phrase_ok:
            raise D3GateError("enable confirmation phrase mismatch")
        if self.mode == "first_seen" and self.send_phrase != D3_SEND_FIRST_PHRASE:
            raise D3GateError("FIRST_SEEN confirmation phrase mismatch")
        if self.mode == "exact_replay" and self.send_phrase != D3_SEND_REPLAY_PHRASE:
            raise D3GateError("exact replay confirmation phrase mismatch")
        if self.mode not in {"first_seen", "exact_replay"}:
            raise D3GateError("invalid D3 mode")
        if self.environment not in D3_ALLOWED_ENVIRONMENTS:
            raise D3GateError("environment not sandbox_controlled/equivalent")
        if self.concurrency != 1:
            raise D3GateError("concurrency must be 1")
        if self.max_retries != 0:
            raise D3GateError("max_retries must be 0")
        if not self.producer_marker_present:
            raise D3GateError("D3 producer marker missing")
        if not self.profile_present:
            raise D3GateError("producer profile missing")
        if not self.secret_present:
            raise D3GateError("auth secret missing")


def default_d3_runs_dir(repo_root: Path) -> Path:
    return Path(repo_root) / "local" / LOCAL_SITE_REL / D3_RUNS_REL


def charter_state_path(runs_dir: Path) -> Path:
    return Path(runs_dir) / D3_CHARTER_STATE_FILENAME


def load_charter_state(runs_dir: Path) -> dict[str, Any]:
    path = charter_state_path(runs_dir)
    if not path.is_file():
        return {
            "phase": "1B-D3",
            "real_http_requests": 0,
            "first_seen_consumed": False,
            "exact_replay_consumed": False,
            "charter_consumed": False,
            "event_id": None,
        }
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise D3GateError("charter state malformed")
    return raw


def save_charter_state(runs_dir: Path, state: dict[str, Any]) -> None:
    runs_dir = Path(runs_dir)
    runs_dir.mkdir(parents=True, exist_ok=True)
    path = charter_state_path(runs_dir)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def assert_request_budget(state: dict[str, Any], *, mode: str) -> None:
    used = int(state.get("real_http_requests") or 0)
    if used >= D3_MAX_REAL_REQUESTS:
        raise D3GateError("max real HTTP requests already consumed")
    if mode == "first_seen":
        if state.get("first_seen_consumed"):
            raise D3GateError("FIRST_SEEN already consumed")
        if used != 0:
            raise D3GateError("FIRST_SEEN requires zero prior real requests")
    elif mode == "exact_replay":
        if not state.get("first_seen_consumed"):
            raise D3GateError("exact replay requires successful FIRST_SEEN")
        if state.get("exact_replay_consumed"):
            raise D3GateError("exact replay already consumed")
        if used != 1:
            raise D3GateError("exact replay requires exactly one prior real request")
    else:
        raise D3GateError("invalid mode for request budget")


def record_successful_request(state: dict[str, Any], *, mode: str, event_id: str) -> dict[str, Any]:
    out = dict(state)
    out["real_http_requests"] = int(out.get("real_http_requests") or 0) + 1
    out["event_id"] = event_id
    if mode == "first_seen":
        out["first_seen_consumed"] = True
    elif mode == "exact_replay":
        out["exact_replay_consumed"] = True
        out["charter_consumed"] = True
    if int(out["real_http_requests"]) >= D3_MAX_REAL_REQUESTS:
        out["charter_consumed"] = True
    return out


def invalidate_charter_state(runs_dir: Path) -> None:
    """Remove reusable one-time authorization after test."""
    path = charter_state_path(runs_dir)
    if path.is_file():
        # Mark consumed rather than leaving a reusable auth token file.
        state = load_charter_state(runs_dir)
        state["charter_consumed"] = True
        state["invalidated"] = True
        save_charter_state(runs_dir, state)


def envelope_has_d3_marker(envelope: dict[str, Any]) -> bool:
    producer = envelope.get("producer") if isinstance(envelope.get("producer"), dict) else {}
    name = str(producer.get("name") or "")
    return name == D3_PRODUCER_MARKER


def build_authorization(
    *,
    enable_phrase: Optional[str],
    send_phrase: Optional[str],
    mode: str,
    apply: bool,
    dry_run: bool,
    environment: str,
    concurrency: int,
    max_retries: int,
    producer_marker_present: bool,
    profile_present: bool,
    secret_present: bool,
) -> D3LiveAuthorization:
    return D3LiveAuthorization(
        enable_phrase_ok=(enable_phrase == D3_ENABLE_PHRASE),
        apply=apply,
        send_phrase=send_phrase or "",
        mode=mode,
        environment=environment,
        concurrency=concurrency,
        max_retries=max_retries,
        producer_marker_present=producer_marker_present,
        profile_present=profile_present,
        secret_present=secret_present,
        dry_run=dry_run,
    )
