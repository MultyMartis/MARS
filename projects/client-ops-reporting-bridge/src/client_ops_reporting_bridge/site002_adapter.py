"""Phase 1B-D4 SITE-002 real-source adapter (offline / read-only).

SITE-002 monitor/report artifacts
  → SITE-002 adapter parser + firewall
  → SITE002MonitorResult
  → Client Ops producer input
  → existing producer offline transport (mock/fixture/disabled)

No monitor execution. No network. No scheduler. No live POST.
"""

from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .artifact_loader import load_fixture_meta, sha256_file
from .constants import REQUIRED_ARTIFACTS, SITE_ID
from .envelope_builder import attach_envelope_with_security
from .models import FixtureMeta, ParsedArtifacts
from .normalizer import normalize
from .producer_config import ProducerProfile, offline_default_profile
from .producer_constants import TRANSPORT_MOCK
from .producer_firewall import normalize_producer_input
from .producer_pipeline import run_producer_offline
from .producer_result import ProducerResult, new_producer_run_id
from .simple_formatter import format_simple
from .site002_adapter_constants import (
    D4_ALLOWED_TRANSPORTS,
    D4_REAL_SOURCE_ORIGIN_MARKERS,
    REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
    SOURCE_CONTRACT_VERSION,
    STATUS_MAPPING,
)
from .site002_adapter_firewall import (
    Site002AdapterFirewallError,
    assert_no_raw_passthrough,
    firewall_artifact_document,
)


class Site002AdapterError(ValueError):
    """Adapter validation / gate failure."""


class RealSourceLiveDispatchNotAuthorized(RuntimeError):
    """D4 hard-block for any real-source live dispatch attempt."""

    def __init__(self, detail: str = "live dispatch blocked in D4") -> None:
        super().__init__(f"{REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4}: {detail}")
        self.code = REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4
        self.detail = detail


@dataclass
class AdapterResult:
    """Sanitized adapter outcome (never includes raw source)."""

    adapter_run_id: str
    source_contract_version: str
    source_run_id: str
    source_observed_at: Optional[str]
    source_status: str
    client_ops_status: str
    event_id: Optional[str]
    source_contract_fingerprint: str
    validation_result: str
    redaction_result: dict[str, Any]
    producer_build_result: str
    transport_mode: str
    network_calls: int
    final_state: str
    safe_unknowns: list[str] = field(default_factory=list)
    summary_code: str = ""
    action_code: str = ""
    reason_codes: list[str] = field(default_factory=list)
    metrics: Optional[dict[str, Any]] = None
    producer_input: Optional[dict[str, Any]] = None
    message_preview: Optional[str] = None
    intake_accepted: bool = False
    telegram_delivery_known: bool = False
    automatic_retry: bool = False
    business_result: str = "NOT_DISPATCHED"
    dedupe_result: str = "NA"
    retry_decision: str = "NONE"
    producer_result: Optional[dict[str, Any]] = None

    def to_sanitized_dict(self) -> dict[str, Any]:
        return {
            "adapter_run_id": self.adapter_run_id,
            "source_contract_version": self.source_contract_version,
            "source_run_id": self.source_run_id,
            "source_observed_at": self.source_observed_at,
            "source_status": self.source_status,
            "client_ops_status": self.client_ops_status,
            "event_id": self.event_id,
            "source_contract_fingerprint": self.source_contract_fingerprint,
            "validation_result": self.validation_result,
            "redaction_result": self.redaction_result,
            "producer_build_result": self.producer_build_result,
            "transport_mode": self.transport_mode,
            "network_calls": self.network_calls,
            "final_state": self.final_state,
            "safe_unknowns": list(self.safe_unknowns),
            "summary_code": self.summary_code,
            "action_code": self.action_code,
            "reason_codes": list(self.reason_codes),
            "metrics": self.metrics,
            "message_preview": self.message_preview,
            "intake_accepted": self.intake_accepted,
            "telegram_delivery_known": self.telegram_delivery_known,
            "automatic_retry": self.automatic_retry,
            "business_result": self.business_result,
            "dedupe_result": self.dedupe_result,
            "retry_decision": self.retry_decision,
        }


def read_fixture_meta_raw(source_dir: Path) -> dict[str, Any]:
    path = Path(source_dir) / "fixture-meta.json"
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise Site002AdapterError("fixture-meta.json must be an object")
    return data


def is_real_source_fixture(source_dir: Path) -> bool:
    """True when fixture-meta marks SITE-002 real-source / D4 adapter input."""
    meta = read_fixture_meta_raw(source_dir)
    origin = str(meta.get("source_origin") or meta.get("d4_source_marker") or "")
    if origin in D4_REAL_SOURCE_ORIGIN_MARKERS:
        return True
    if meta.get("real_source_adapter") is True:
        return True
    if str(meta.get("adapter_phase") or "") == "1B-D4":
        return True
    # Path heuristic for committed D4 fixture tree
    parts = {p.lower() for p in Path(source_dir).parts}
    if "site-002-real-source-adapter" in parts:
        return True
    return False


def assert_live_dispatch_blocked(
    *,
    live: bool = False,
    apply: bool = False,
    transport: str = TRANSPORT_MOCK,
    d3_phrase: Optional[str] = None,
) -> None:
    """Hard-block any real-source live / HTTP / apply attempt."""
    transport_l = str(transport or "").strip().lower()
    if live or apply or transport_l == "http":
        raise RealSourceLiveDispatchNotAuthorized(
            "live|apply|transport=http not authorized for real-source D4"
        )
    if d3_phrase:
        raise RealSourceLiveDispatchNotAuthorized(
            "D3 confirmation phrases cannot authorize D4 real-source live"
        )
    if transport_l not in D4_ALLOWED_TRANSPORTS:
        raise RealSourceLiveDispatchNotAuthorized(
            f"transport={transport_l} not allowed in D4"
        )


def reject_d3_real_source_usage(source_dir: Path) -> None:
    """D3 synthetic charter must refuse D4 real-source fixtures."""
    if is_real_source_fixture(source_dir):
        raise RealSourceLiveDispatchNotAuthorized(
            "D3 consumed synthetic charter cannot authorize D4 real-source fixture"
        )


def parse_source(source_dir: Path) -> tuple[ParsedArtifacts, dict[str, Any]]:
    """Parse required SITE-002 artifacts through the SITE-002 firewall."""
    source_dir = Path(source_dir).resolve()
    if not source_dir.is_dir():
        raise Site002AdapterError(f"source path is not a directory: {source_dir}")

    # Forbidden discovery modes
    name = source_dir.name.lower()
    if name in {"latest", "watch", "continuous"}:
        raise Site002AdapterError("auto-discovery source names are forbidden")

    result = ParsedArtifacts()
    redaction_records: list[dict[str, Any]] = []

    for artifact_name in REQUIRED_ARTIFACTS:
        path = source_dir / artifact_name
        if not path.is_file():
            result.missing.append(artifact_name)
            continue
        result.raw_hashes[artifact_name] = sha256_file(path)
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            result.malformed.append(artifact_name)
            continue
        if not isinstance(data, dict):
            result.malformed.append(artifact_name)
            continue
        cleaned, redaction = firewall_artifact_document(artifact_name, data)
        redaction_records.append(redaction)
        if artifact_name == "monitor-classification.json":
            result.monitor_classification = cleaned
        elif artifact_name == "changed-summary.json":
            result.changed_summary = cleaned
        elif artifact_name == "run-summary.json":
            result.run_summary = cleaned

    # run.log is evidence/debug only — never load into adapter contract
    redaction_result = {
        "policy": "site002-adapter-allowlist-v1",
        "artifacts": redaction_records,
        "run_log_loaded": False,
    }
    return result, redaction_result


def compute_source_contract_fingerprint(artifacts: ParsedArtifacts) -> str:
    """Hash only sanitized canonical source fields (not secrets/raw logs)."""
    canonical = {
        "monitor_classification": artifacts.monitor_classification or {},
        "changed_summary": artifacts.changed_summary or {},
        "run_summary": {
            k: v
            for k, v in (artifacts.run_summary or {}).items()
            if k
            in {
                "run_id",
                "classification",
                "started_at",
                "finished_at",
                "exit_code",
                "added_count",
                "onboarding_needs_count",
                "baseline_url_count",
                "current_url_count",
                "removed_count",
            }
        },
        "contract": SOURCE_CONTRACT_VERSION,
    }
    blob = json.dumps(
        canonical, ensure_ascii=False, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def validate_source(artifacts: ParsedArtifacts) -> None:
    """Fail-closed completeness gate (no silent OK)."""
    if artifacts.missing:
        raise Site002AdapterError(
            "incomplete source: missing " + ",".join(artifacts.missing)
        )
    if artifacts.malformed:
        raise Site002AdapterError(
            "malformed source: " + ",".join(artifacts.malformed)
        )


def normalize_status(source_status: str) -> str:
    """Map SITE-002 classification vocabulary; unknown → raise."""
    if source_status not in STATUS_MAPPING:
        raise Site002AdapterError(f"unsupported source status: {source_status}")
    return STATUS_MAPPING[source_status]


def derive_run_identity(artifacts: ParsedArtifacts) -> str:
    """Prefer run-summary.run_id (scheduled folder name)."""
    run = artifacts.run_summary or {}
    run_id = run.get("run_id") or run.get("id")
    if isinstance(run_id, str) and run_id.strip():
        return run_id.strip()
    raise Site002AdapterError("stable source run_id missing")


def to_producer_input(process_result: Any) -> dict[str, Any]:
    """Build allowlisted producer input from normalized ProcessResult."""
    raw = {
        "site_id": SITE_ID,
        "domain": "bzpm.ru",
        "event_type": "site.post_1c_monitor",
        "run_id": process_result.run_id,
        "observed_at": process_result.observed_at,
        "status": process_result.normalized_status,
        "normalized_status": process_result.normalized_status,
        "source_status": process_result.source_status,
        "summary_code": process_result.summary_code,
        "reason_codes": list(process_result.reason_codes),
        "action_code": process_result.action_code,
        "action_required": process_result.action_required,
        "action_text": process_result.action_text,
        "metrics": process_result.metrics,
        "freshness": {
            "age_seconds": process_result.age_seconds,
            "stale": process_result.stale,
        },
    }
    cleaned = normalize_producer_input(raw)
    assert_no_raw_passthrough(cleaned)
    return cleaned


def adapt_source_dir(
    source_dir: Path,
    *,
    meta: Optional[FixtureMeta] = None,
    now_utc: Optional[datetime] = None,
    build_envelope: bool = True,
) -> tuple[Any, dict[str, Any], str]:
    """Parse → firewall → normalize → optional envelope.

    Returns ``(ProcessResult, redaction_result, fingerprint)``.
    """
    artifacts, redaction = parse_source(source_dir)
    validate_source(artifacts)
    fingerprint = compute_source_contract_fingerprint(artifacts)
    loaded_meta = meta or load_fixture_meta(Path(source_dir))
    proc = normalize(artifacts, now_utc=now_utc, meta=loaded_meta)
    if build_envelope:
        proc = attach_envelope_with_security(proc, meta=loaded_meta)
        if proc.envelope is not None and proc.distributable:
            tz = loaded_meta.display_timezone
            proc.simple_text = format_simple(proc.envelope, tz_name=tz)
    return proc, redaction, fingerprint


def run_site002_adapter_dry_run(
    source_dir: Path,
    *,
    transport: str = TRANSPORT_MOCK,
    mock_response: str = "202_accepted",
    live: bool = False,
    apply: bool = False,
    d3_phrase: Optional[str] = None,
    profile: Optional[ProducerProfile] = None,
    evidence_dir: Optional[Path] = None,
    adapter_run_id: Optional[str] = None,
) -> AdapterResult:
    """Manual offline adapter → producer mock/fixture/disabled path."""
    assert_live_dispatch_blocked(
        live=live,
        apply=apply,
        transport=transport,
        d3_phrase=d3_phrase,
    )

    run_id = adapter_run_id or new_producer_run_id()
    source_dir = Path(source_dir)
    safe_unknowns: list[str] = []

    try:
        proc, redaction, fingerprint = adapt_source_dir(source_dir)
    except Site002AdapterFirewallError as exc:
        return AdapterResult(
            adapter_run_id=run_id,
            source_contract_version=SOURCE_CONTRACT_VERSION,
            source_run_id="",
            source_observed_at=None,
            source_status="",
            client_ops_status="BLOCKED",
            event_id=None,
            source_contract_fingerprint="",
            validation_result="FIREWALL_REJECTED",
            redaction_result={"error": str(exc)},
            producer_build_result="NOT_ATTEMPTED",
            transport_mode=transport,
            network_calls=0,
            final_state="ADAPTER_FIREWALL_REJECTED",
            safe_unknowns=safe_unknowns,
        )
    except Site002AdapterError as exc:
        return AdapterResult(
            adapter_run_id=run_id,
            source_contract_version=SOURCE_CONTRACT_VERSION,
            source_run_id="",
            source_observed_at=None,
            source_status="",
            client_ops_status="BLOCKED",
            event_id=None,
            source_contract_fingerprint="",
            validation_result="SOURCE_REJECTED",
            redaction_result={"error": str(exc)},
            producer_build_result="NOT_ATTEMPTED",
            transport_mode=transport,
            network_calls=0,
            final_state="ADAPTER_SOURCE_REJECTED",
            safe_unknowns=safe_unknowns,
        )

    producer_input = to_producer_input(proc)
    event_id = None
    if proc.envelope is not None:
        event_id = str(proc.envelope.get("event_id") or "") or None

    producer_build = "BUILT" if proc.distributable and proc.envelope else "NOT_DISTRIBUTABLE"
    validation = "PASS" if not proc.security_rejected else "SECURITY_REJECTED"

    # Offline producer only when envelope distributable
    producer_sanitized: Optional[dict[str, Any]] = None
    business = "NOT_DISPATCHED"
    dedupe = "NA"
    retry = "NONE"
    intake = False
    final_state = proc.normalized_status
    if proc.distributable and proc.envelope is not None:
        prod: ProducerResult = run_producer_offline(
            envelope=proc.envelope,
            profile=profile or offline_default_profile(),
            transport_mode=transport,
            mock_fixture=mock_response,
            evidence_dir=evidence_dir,
            producer_run_id=run_id,
        )
        if prod.network_calls != 0:
            raise RealSourceLiveDispatchNotAuthorized("network_calls must remain 0")
        producer_sanitized = prod.to_sanitized_dict()
        business = prod.business_result
        dedupe = prod.dedupe_result
        retry = prod.retry_decision
        intake = prod.intake_accepted
        final_state = prod.final_state
        event_id = prod.event_id or event_id
    else:
        final_state = "SOURCE_BLOCKED"
        producer_build = "NOT_DISTRIBUTABLE"

    return AdapterResult(
        adapter_run_id=run_id,
        source_contract_version=SOURCE_CONTRACT_VERSION,
        source_run_id=proc.run_id,
        source_observed_at=proc.observed_at,
        source_status=proc.source_status,
        client_ops_status=proc.normalized_status,
        event_id=event_id,
        source_contract_fingerprint=fingerprint,
        validation_result=validation,
        redaction_result=redaction,
        producer_build_result=producer_build,
        transport_mode=transport,
        network_calls=0,
        final_state=final_state,
        safe_unknowns=safe_unknowns,
        summary_code=proc.summary_code,
        action_code=proc.action_code,
        reason_codes=list(proc.reason_codes),
        metrics=proc.metrics,
        producer_input=producer_input,
        message_preview=proc.simple_text,
        intake_accepted=intake,
        telegram_delivery_known=False,
        automatic_retry=False,
        business_result=business,
        dedupe_result=dedupe,
        retry_decision=retry,
        producer_result=producer_sanitized,
    )


def new_adapter_run_id() -> str:
    return str(uuid.uuid4())
