"""Offline CLI for Phase 1A exporter core + Phase 1B-D2/D3 producer.

Modes:
  validate-only         — normalize; print sanitized result; no envelope write
  build-envelope        — write distributable envelope to an approved local path
  producer-dry-run      — offline producer with mock/fixture/disabled transport
  producer-fixture-test — run a named mock classification once
  site002-adapter-dry-run — D4 real-source adapter → producer offline only
  push-webhook          — ALWAYS blocked (use producer-d3-controlled-live)
  producer-d3-controlled-live — D3-gated real HTTPS (exact phrases + --apply)

Ordinary dry-run never reaches network. Import causes no network.
D4 real-source live dispatch is always blocked.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import traceback
from pathlib import Path
from typing import Optional, Sequence

from .constants import (
    EXIT_INTERNAL,
    EXIT_SOURCE_BLOCKED,
    EXIT_SUCCESS,
    EXIT_UNSAFE_OUTPUT_PATH,
    EXIT_USAGE,
)
from .errors import UnsafeOutputPathError, UsageError
from .pipeline import process_fixture_dir
from .producer_config import (
    ProducerConfigError,
    default_profile_path,
    default_secrets_path,
    load_producer_profile,
    load_producer_secrets,
    offline_default_profile,
)
from .producer_constants import (
    D3_ENABLE_PHRASE,
    D3_SEND_FIRST_PHRASE,
    D3_SEND_REPLAY_PHRASE,
    D5_ENABLE_PHRASE,
    D5_SEND_PHRASE,
    D5_SOURCE_PROVENANCE,
    EXIT_CONCURRENCY_REJECTED,
    EXIT_CONFIG_INVALID,
    EXIT_NETWORK_NOT_AUTHORIZED,
    MOCK_FIXTURE_NAMES,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
    TRANSPORT_DISABLED,
    TRANSPORT_MOCK,
)
from .site002_adapter import (
    RealSourceLiveDispatchNotAuthorized,
    run_site002_adapter_dry_run,
)
from .site002_adapter_constants import (
    REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
    SOURCE_CONTRACT_VERSION,
)
from .producer_d3 import run_producer_d3_controlled
from .producer_d3_gates import build_authorization, default_d3_runs_dir
from .producer_d5 import (
    assess_preview_for_live,
    build_source_preview,
    d3_charter_is_consumed,
    run_producer_d5_controlled,
)
from .producer_d5_gates import (
    build_authorization as build_d5_authorization,
    default_d5_runs_dir,
    load_charter_state as load_d5_charter_state,
    reject_forbidden_discovery_flags,
    validate_explicit_source_path,
)
from .producer_dispatch_guard import SequentialDispatchError
from .producer_pipeline import run_producer_offline
from .security_validator import redact_for_diagnostics

# Approved output roots for Phase 1A/D2 (resolved at runtime).
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_REPO_ROOT = Path(__file__).resolve().parents[4]


def _is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def assert_safe_output_path(output: Path) -> Path:
    """Refuse paths outside approved offline boundaries.

    Approved:
    - under ``projects/client-ops-reporting-bridge/``
    - under the process temporary directory
    - under ``local/client-ops-reporting-bridge/`` (ignored local evidence/runs)
    """
    resolved = output.resolve()
    tmp_root = Path(tempfile.gettempdir()).resolve()
    local_client_ops = (_REPO_ROOT / "local" / "client-ops-reporting-bridge").resolve()
    if (
        _is_under(resolved, _PROJECT_ROOT)
        or _is_under(resolved, tmp_root)
        or _is_under(resolved, local_client_ops)
    ):
        # Deny writing into fixtures source trees accidentally replacing inputs
        fixtures = (_PROJECT_ROOT / "fixtures").resolve()
        if _is_under(resolved, fixtures) and resolved.parent == fixtures:
            raise UnsafeOutputPathError(
                "refusing to write envelope directly into fixtures root"
            )
        # Allow fixtures/*/out/ or project test-output/ or ignored local runs/
        return resolved
    raise UnsafeOutputPathError(
        "output path outside approved offline boundaries "
        "(project locus, ignored local client-ops, or system temp)"
    )


def _print_result(result_dict: dict, *, stream=None) -> None:
    stream = stream or sys.stdout
    stream.write(json.dumps(result_dict, ensure_ascii=False, indent=2))
    stream.write("\n")


def cmd_validate_only(fixture: Path, *, debug: bool = False) -> int:
    if not fixture.is_dir():
        raise UsageError(f"fixture path is not a directory: {fixture}")
    result = process_fixture_dir(fixture, build_envelope=True)
    payload = result.to_sanitized_dict()
    if result.envelope is not None and result.distributable:
        payload["event_id"] = result.envelope.get("event_id")
    if debug and result.issues:
        payload["issues"] = [
            {
                "code": i.code,
                "message": redact_for_diagnostics(i.message),
                "artifact": i.artifact,
                "field": i.field,
            }
            for i in result.issues
        ]
    _print_result(payload)
    if result.security_rejected:
        return EXIT_SOURCE_BLOCKED
    if result.normalized_status == "BLOCKED":
        return EXIT_SOURCE_BLOCKED
    if result.normalized_status == "FAILED":
        # Failed is a valid normalized site status with distributable envelope
        return EXIT_SUCCESS if result.distributable else EXIT_SOURCE_BLOCKED
    if result.normalized_status in {"OK", "ATTENTION"} and result.distributable:
        return EXIT_SUCCESS
    if result.normalized_status in {"OK", "ATTENTION"}:
        return EXIT_SOURCE_BLOCKED
    return EXIT_SOURCE_BLOCKED


def cmd_build_envelope(
    fixture: Path,
    output: Path,
    *,
    debug: bool = False,
) -> int:
    if not fixture.is_dir():
        raise UsageError(f"fixture path is not a directory: {fixture}")
    safe_out = assert_safe_output_path(output)
    result = process_fixture_dir(fixture, build_envelope=True)

    if result.security_rejected or not result.distributable or result.envelope is None:
        payload = result.to_sanitized_dict()
        if debug and result.issues:
            payload["issues"] = [
                {
                    "code": i.code,
                    "message": redact_for_diagnostics(i.message),
                    "artifact": i.artifact,
                    "field": i.field,
                }
                for i in result.issues
            ]
        _print_result(payload)
        return EXIT_SOURCE_BLOCKED

    safe_out.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result.envelope, ensure_ascii=False, indent=2) + "\n"
    safe_out.write_text(text, encoding="utf-8")
    summary = result.to_sanitized_dict()
    summary["event_id"] = result.envelope["event_id"]
    summary["output"] = str(safe_out.name)
    _print_result(summary)
    return EXIT_SUCCESS


def _load_profile_optional(path: Optional[Path]):
    if path is None:
        default = default_profile_path(_REPO_ROOT)
        if default.is_file():
            return load_producer_profile(default)
        return offline_default_profile()
    return load_producer_profile(path)


def cmd_producer_dry_run(
    fixture: Path,
    *,
    transport: str = TRANSPORT_MOCK,
    mock_response: str = "202_accepted",
    evidence_dir: Optional[Path] = None,
    profile_path: Optional[Path] = None,
    concurrency: int = 1,
    live: bool = False,
    apply: bool = False,
    with_auth: bool = False,
) -> int:
    from .site002_adapter import is_real_source_fixture

    if live or apply or transport.strip().lower() == "http":
        # Real-source fixtures must not piggyback on generic live attempts
        if is_real_source_fixture(fixture):
            _print_result(
                {
                    "ok": False,
                    "final_state": REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
                    "network_calls": 0,
                    "transport_mode": transport,
                }
            )
            return EXIT_NETWORK_NOT_AUTHORIZED
        _print_result(
            {
                "ok": False,
                "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
                "network_calls": 0,
                "transport_mode": transport,
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    if concurrency != 1:
        _print_result(
            {
                "ok": False,
                "final_state": "CONCURRENCY_REJECTED",
                "network_calls": 0,
            }
        )
        return EXIT_CONCURRENCY_REJECTED

    try:
        profile = _load_profile_optional(profile_path)
    except ProducerConfigError as exc:
        _print_result(
            {
                "ok": False,
                "final_state": "CONFIG_INVALID",
                "error": redact_for_diagnostics(str(exc)),
                "network_calls": 0,
            }
        )
        return EXIT_CONFIG_INVALID

    secrets = None
    if with_auth:
        secrets = load_producer_secrets(default_secrets_path(_REPO_ROOT))

    safe_evidence = None
    if evidence_dir is not None:
        safe_evidence = assert_safe_output_path(evidence_dir)

    result = run_producer_offline(
        fixture_dir=fixture,
        profile=profile,
        secrets=secrets,
        transport_mode=transport,
        mock_fixture=mock_response,
        concurrency=concurrency,
        evidence_dir=safe_evidence,
        require_auth=False,
    )
    payload = result.to_sanitized_dict()
    payload["ok"] = result.final_state not in {
        NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
        "CONCURRENCY_REJECTED",
        "SOURCE_BLOCKED",
        "CONFIG_INVALID",
    }
    _print_result(payload)
    if result.final_state == NETWORK_DISPATCH_NOT_AUTHORIZED_D2:
        return EXIT_NETWORK_NOT_AUTHORIZED
    if result.final_state == "CONCURRENCY_REJECTED":
        return EXIT_CONCURRENCY_REJECTED
    if result.final_state == "SOURCE_BLOCKED":
        return EXIT_SOURCE_BLOCKED
    return EXIT_SUCCESS


def cmd_site002_adapter_dry_run(
    source: Path,
    *,
    transport: str = TRANSPORT_MOCK,
    mock_response: str = "202_accepted",
    evidence_dir: Optional[Path] = None,
    live: bool = False,
    apply: bool = False,
    confirm_enable: Optional[str] = None,
    confirm_send: Optional[str] = None,
) -> int:
    """D4 real-source adapter offline dry-run (never HTTP)."""
    d3_phrase = confirm_enable or confirm_send
    try:
        safe_evidence = (
            assert_safe_output_path(evidence_dir) if evidence_dir is not None else None
        )
        result = run_site002_adapter_dry_run(
            source,
            transport=transport,
            mock_response=mock_response,
            live=live,
            apply=apply,
            d3_phrase=d3_phrase,
            evidence_dir=safe_evidence,
        )
    except RealSourceLiveDispatchNotAuthorized as exc:
        _print_result(
            {
                "ok": False,
                "final_state": REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
                "network_calls": 0,
                "error": redact_for_diagnostics(str(exc.detail)),
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    payload = result.to_sanitized_dict()
    payload["ok"] = result.final_state not in {
        REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
        "ADAPTER_FIREWALL_REJECTED",
        "ADAPTER_SOURCE_REJECTED",
        "SOURCE_BLOCKED",
        "CONCURRENCY_REJECTED",
    }
    # Always expose producer_input identity fields for offline evidence
    if result.producer_input is not None:
        payload["producer_input"] = {
            k: result.producer_input.get(k)
            for k in (
                "run_id",
                "observed_at",
                "normalized_status",
                "source_status",
                "summary_code",
                "action_code",
                "reason_codes",
                "metrics",
            )
            if k in result.producer_input
        }
    _print_result(payload)
    if result.final_state == REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4:
        return EXIT_NETWORK_NOT_AUTHORIZED
    if result.final_state in {
        "ADAPTER_FIREWALL_REJECTED",
        "ADAPTER_SOURCE_REJECTED",
        "SOURCE_BLOCKED",
    }:
        return EXIT_SOURCE_BLOCKED
    return EXIT_SUCCESS


def cmd_producer_fixture_test(mock_response: str, fixture: Path) -> int:
    if mock_response not in MOCK_FIXTURE_NAMES:
        raise UsageError(f"unknown mock response: {mock_response}")
    return cmd_producer_dry_run(
        fixture,
        transport=TRANSPORT_MOCK,
        mock_response=mock_response,
    )


def cmd_push_webhook(*_args, **_kwargs) -> int:
    """Generic live POST — remains blocked; use producer-d3-controlled-live."""
    _print_result(
        {
            "ok": False,
            "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
            "network_calls": 0,
            "message": (
                "push-webhook remains blocked; use producer-d3-controlled-live "
                "with exact D3 confirmation phrases"
            ),
        }
    )
    return EXIT_NETWORK_NOT_AUTHORIZED


def cmd_producer_d3_controlled_live(
    *,
    fixture: Optional[Path],
    mode: str,
    apply: bool,
    dry_run: bool,
    confirm_enable: Optional[str],
    confirm_send: Optional[str],
    profile_path: Optional[Path],
    evidence_dir: Optional[Path],
    concurrency: int,
    max_retries: int,
) -> int:
    """D3-gated controlled live producer POST (or dry-run readiness)."""
    if concurrency != 1:
        _print_result({"ok": False, "final_state": "CONCURRENCY_REJECTED", "network_calls": 0})
        return EXIT_CONCURRENCY_REJECTED
    if max_retries != 0:
        _print_result(
            {
                "ok": False,
                "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
                "network_calls": 0,
                "error": "max_retries must be 0",
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    try:
        profile = _load_profile_optional(profile_path)
    except ProducerConfigError as exc:
        _print_result(
            {
                "ok": False,
                "final_state": "CONFIG_INVALID",
                "error": redact_for_diagnostics(str(exc)),
                "network_calls": 0,
            }
        )
        return EXIT_CONFIG_INVALID

    secrets_path = default_secrets_path(_REPO_ROOT)
    secrets = load_producer_secrets(secrets_path)
    profile_ok = bool(profile.webhook_base and profile.webhook_route)
    auth = build_authorization(
        enable_phrase=confirm_enable,
        send_phrase=confirm_send,
        mode=mode,
        apply=apply,
        dry_run=dry_run,
        environment=profile.environment,
        concurrency=concurrency,
        max_retries=max_retries,
        producer_marker_present=True,  # applied inside pipeline for live/dry
        profile_present=profile_ok,
        secret_present=secrets.auth_secret_present,
    )

    safe_evidence = assert_safe_output_path(evidence_dir) if evidence_dir else None
    runs_dir = default_d3_runs_dir(_REPO_ROOT)

    if dry_run:
        # Prove readiness without network
        ready = (
            profile_ok
            and secrets.auth_secret_present
            and concurrency == 1
            and max_retries == 0
            and profile.environment in {"sandbox", "sandbox_controlled"}
        )
        _print_result(
            {
                "ok": ready,
                "final_state": "D3_DRY_RUN_READY" if ready else "NOT_READY",
                "network_calls": 0,
                "dispatch_attempted": False,
                "real_network": False,
                "profile_present": profile_ok,
                "secret_present": secrets.auth_secret_present,
                "environment": profile.environment,
                "concurrency": concurrency,
                "max_retries": max_retries,
                "mode": mode,
                "enable_phrase_expected": D3_ENABLE_PHRASE,
                "send_phrase_expected": (
                    D3_SEND_FIRST_PHRASE if mode == "first_seen" else D3_SEND_REPLAY_PHRASE
                ),
            }
        )
        return EXIT_SUCCESS if ready else EXIT_CONFIG_INVALID

    if not apply:
        _print_result(
            {
                "ok": False,
                "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
                "network_calls": 0,
                "error": "missing --apply",
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    result = run_producer_d3_controlled(
        authorization=auth,
        profile=profile,
        secrets=secrets,
        fixture_dir=fixture,
        mode=mode,
        concurrency=concurrency,
        evidence_dir=safe_evidence,
        runs_dir=runs_dir,
        repo_root=_REPO_ROOT,
    )
    payload = result.to_sanitized_dict()
    payload["ok"] = result.final_state not in {
        NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
        NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
        "CONCURRENCY_REJECTED",
        "SOURCE_BLOCKED",
        "CONFIG_INVALID",
    }
    _print_result(payload)
    if result.final_state in {
        NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
        NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
    }:
        return EXIT_NETWORK_NOT_AUTHORIZED
    if result.final_state == "CONCURRENCY_REJECTED":
        return EXIT_CONCURRENCY_REJECTED
    return EXIT_SUCCESS


def cmd_site002_controlled_live(
    *,
    source: Optional[Path],
    apply: bool,
    dry_run: bool,
    preview_only: bool,
    confirm_enable: Optional[str],
    confirm_send: Optional[str],
    environment: str,
    profile_path: Optional[Path],
    evidence_dir: Optional[Path],
    concurrency: int,
    max_retries: int,
    event_unseen: bool,
    preview_approved: bool,
    latest: bool = False,
    watch: bool = False,
) -> int:
    """D5-gated one manual SITE-002 real-source controlled live POST."""
    try:
        reject_forbidden_discovery_flags(latest=latest, watch=watch)
    except Exception as exc:  # noqa: BLE001
        _print_result(
            {
                "ok": False,
                "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
                "network_calls": 0,
                "error": redact_for_diagnostics(str(exc)),
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    if concurrency != 1:
        _print_result({"ok": False, "final_state": "CONCURRENCY_REJECTED", "network_calls": 0})
        return EXIT_CONCURRENCY_REJECTED
    if max_retries != 0:
        _print_result(
            {
                "ok": False,
                "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
                "network_calls": 0,
                "error": "max_retries must be 0",
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    if source is None:
        raise UsageError("--source required (explicit completed SITE-002 run directory)")

    try:
        profile = _load_profile_optional(profile_path)
    except ProducerConfigError as exc:
        _print_result(
            {
                "ok": False,
                "final_state": "CONFIG_INVALID",
                "error": redact_for_diagnostics(str(exc)),
                "network_calls": 0,
            }
        )
        return EXIT_CONFIG_INVALID

    secrets_path = default_secrets_path(_REPO_ROOT)
    secrets = load_producer_secrets(secrets_path)
    profile_ok = bool(profile.webhook_base and profile.webhook_route)
    runs_dir = default_d5_runs_dir(_REPO_ROOT)
    safe_evidence = assert_safe_output_path(evidence_dir) if evidence_dir else None

    source_path_ok = False
    try:
        validated = validate_explicit_source_path(Path(source))
        source_path_ok = True
    except Exception as exc:  # noqa: BLE001
        if not (dry_run or preview_only):
            _print_result(
                {
                    "ok": False,
                    "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
                    "network_calls": 0,
                    "error": redact_for_diagnostics(str(exc)),
                }
            )
            return EXIT_NETWORK_NOT_AUTHORIZED
        validated = Path(source)

    if preview_only or dry_run:
        preview = build_source_preview(validated) if source_path_ok else {}
        decision = assess_preview_for_live(preview) if preview else {
            "verdict": "REAL_SOURCE_PREVIEW_NOT_APPROVED_FOR_LIVE_POST",
            "reason": "source path invalid",
            "approved": False,
            "network_calls": 0,
        }
        charter = load_d5_charter_state(runs_dir)
        _print_result(
            {
                "ok": bool(source_path_ok and decision.get("approved")),
                "final_state": (
                    "D5_PREVIEW_READY" if decision.get("approved") else "D5_PREVIEW_BLOCKED"
                ),
                "network_calls": 0,
                "dispatch_attempted": False,
                "real_network": False,
                "profile_present": profile_ok,
                "secret_present": secrets.auth_secret_present,
                "environment_requested": environment,
                "concurrency": concurrency,
                "max_retries": max_retries,
                "automatic_retry": False,
                "d3_charter_consumed": d3_charter_is_consumed(_REPO_ROOT),
                "d4_live_blocked": True,
                "d5_charter_consumed": bool(charter.get("charter_consumed")),
                "enable_phrase_expected": D5_ENABLE_PHRASE,
                "send_phrase_expected": D5_SEND_PHRASE,
                "source_preview": preview,
                "source_preview_decision": decision,
            }
        )
        return EXIT_SUCCESS if source_path_ok else EXIT_CONFIG_INVALID

    if not apply:
        _print_result(
            {
                "ok": False,
                "final_state": NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
                "network_calls": 0,
                "error": "missing --apply",
            }
        )
        return EXIT_NETWORK_NOT_AUTHORIZED

    auth = build_d5_authorization(
        enable_phrase=confirm_enable,
        send_phrase=confirm_send,
        apply=apply,
        dry_run=False,
        environment=environment,
        site_id="SITE-002",
        domain="bzpm.ru",
        source_contract=SOURCE_CONTRACT_VERSION,
        source_provenance=D5_SOURCE_PROVENANCE,
        concurrency=concurrency,
        max_retries=max_retries,
        automatic_retry=False,
        producer_marker_present=True,
        profile_present=profile_ok,
        secret_present=secrets.auth_secret_present,
        source_path_ok=source_path_ok,
        preview_approved=preview_approved,
        event_unseen=event_unseen,
        d3_charter_consumed=d3_charter_is_consumed(_REPO_ROOT),
        d4_live_blocked=True,
    )

    result = run_producer_d5_controlled(
        authorization=auth,
        profile=profile,
        secrets=secrets,
        source_dir=validated,
        concurrency=concurrency,
        evidence_dir=safe_evidence,
        runs_dir=runs_dir,
        repo_root=_REPO_ROOT,
        event_unseen_confirmed=event_unseen,
    )
    payload = result.to_sanitized_dict()
    payload["ok"] = result.final_state not in {
        NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
        NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
        NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
        REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
        "CONCURRENCY_REJECTED",
        "SOURCE_BLOCKED",
        "CONFIG_INVALID",
        "D5_REAL_SOURCE_CHARTER_CONSUMED",
    }
    _print_result(payload)
    if result.final_state in {
        NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
        NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
        NETWORK_DISPATCH_NOT_AUTHORIZED_D5,
        REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
        "D5_REAL_SOURCE_CHARTER_CONSUMED",
    }:
        return EXIT_NETWORK_NOT_AUTHORIZED
    if result.final_state == "CONCURRENCY_REJECTED":
        return EXIT_CONCURRENCY_REJECTED
    return EXIT_SUCCESS


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="client_ops_reporting_bridge",
        description=(
            "Phase 1A offline exporter + Phase 1B-D2 offline sequential producer"
        ),
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="include redacted issue details (no raw secrets)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_val = sub.add_parser(
        "validate-only",
        help="validate and normalize fixture; do not write envelope",
    )
    p_val.add_argument(
        "--fixture",
        required=True,
        type=Path,
        help="path to local fixture directory",
    )

    p_build = sub.add_parser(
        "build-envelope",
        help="build distributable envelope to an approved local path",
    )
    p_build.add_argument(
        "--fixture",
        required=True,
        type=Path,
        help="path to local fixture directory",
    )
    p_build.add_argument(
        "--output",
        required=True,
        type=Path,
        help="output JSON path under project locus or temp",
    )

    p_dry = sub.add_parser(
        "producer-dry-run",
        help="offline producer dry-run (mock/fixture/disabled; never live POST)",
    )
    p_dry.add_argument("--fixture", required=True, type=Path)
    p_dry.add_argument(
        "--transport",
        default=TRANSPORT_MOCK,
        choices=["disabled", "fixture", "mock"],
        help="D2-allowed transports only (http absent)",
    )
    p_dry.add_argument(
        "--mock-response",
        default="202_accepted",
        help="mock fixture name when --transport=mock",
    )
    p_dry.add_argument("--evidence-dir", type=Path, default=None)
    p_dry.add_argument("--profile", type=Path, default=None)
    p_dry.add_argument("--concurrency", type=int, default=1)
    p_dry.add_argument("--with-auth", action="store_true")
    p_dry.add_argument("--live", action="store_true", help="blocked in D2")
    p_dry.add_argument("--apply", action="store_true", help="blocked in D2")

    p_fix = sub.add_parser(
        "producer-fixture-test",
        help="run one named mock classification against a fixture",
    )
    p_fix.add_argument("--fixture", required=True, type=Path)
    p_fix.add_argument(
        "--mock-response",
        required=True,
        choices=sorted(MOCK_FIXTURE_NAMES.keys()),
    )

    p_d4 = sub.add_parser(
        "site002-adapter-dry-run",
        help=(
            "D4 SITE-002 real-source adapter offline dry-run "
            "(explicit source path; never live HTTP)"
        ),
    )
    p_d4.add_argument(
        "--source",
        required=True,
        type=Path,
        help="explicit SITE-002 fixture/artifact directory (no --latest)",
    )
    p_d4.add_argument(
        "--transport",
        default=TRANSPORT_MOCK,
        choices=["disabled", "fixture", "mock"],
        help="D4-allowed transports only (http absent)",
    )
    p_d4.add_argument("--mock-response", default="202_accepted")
    p_d4.add_argument("--evidence-dir", type=Path, default=None)
    p_d4.add_argument("--live", action="store_true", help="blocked in D4")
    p_d4.add_argument("--apply", action="store_true", help="blocked in D4")
    p_d4.add_argument("--confirm-enable", type=str, default=None)
    p_d4.add_argument("--confirm-send", type=str, default=None)
    p_d4.add_argument(
        "--latest",
        action="store_true",
        help="forbidden — auto-discovery not authorized",
    )
    p_d4.add_argument(
        "--watch",
        action="store_true",
        help="forbidden — watch mode not authorized",
    )

    p_push = sub.add_parser(
        "push-webhook",
        help="BLOCKED — use producer-d3-controlled-live instead",
    )
    p_push.add_argument("--fixture", type=Path, default=None)
    p_push.add_argument("--live", action="store_true")
    p_push.add_argument("--apply", action="store_true")
    p_push.add_argument("--transport", default="http")

    p_d3 = sub.add_parser(
        "producer-d3-controlled-live",
        help="D3-gated controlled live HTTPS producer POST (exact phrases required)",
    )
    p_d3.add_argument("--fixture", type=Path, default=None)
    p_d3.add_argument(
        "--mode",
        choices=["first_seen", "exact_replay"],
        default="first_seen",
    )
    p_d3.add_argument("--apply", action="store_true")
    p_d3.add_argument(
        "--dry-run",
        action="store_true",
        help="validate readiness only; never open network",
    )
    p_d3.add_argument("--confirm-enable", type=str, default=None)
    p_d3.add_argument("--confirm-send", type=str, default=None)
    p_d3.add_argument("--profile", type=Path, default=None)
    p_d3.add_argument("--evidence-dir", type=Path, default=None)
    p_d3.add_argument("--concurrency", type=int, default=1)
    p_d3.add_argument("--max-retries", type=int, default=0)

    p_d5 = sub.add_parser(
        "site002-controlled-live",
        help=(
            "D5-gated one manual SITE-002 real-source controlled live POST "
            "(explicit source; exact phrases; max 1 HTTP)"
        ),
    )
    p_d5.add_argument(
        "--source",
        type=Path,
        required=True,
        help="explicit completed SITE-002 run directory under approved root",
    )
    p_d5.add_argument("--apply", action="store_true")
    p_d5.add_argument(
        "--dry-run",
        action="store_true",
        help="preview/readiness only; never open network",
    )
    p_d5.add_argument(
        "--preview-only",
        action="store_true",
        help="emit sanitized source preview; never open network",
    )
    p_d5.add_argument("--confirm-enable", type=str, default=None)
    p_d5.add_argument("--confirm-send", type=str, default=None)
    p_d5.add_argument(
        "--environment",
        type=str,
        default="manual_real_source_controlled",
    )
    p_d5.add_argument("--profile", type=Path, default=None)
    p_d5.add_argument("--evidence-dir", type=Path, default=None)
    p_d5.add_argument("--concurrency", type=int, default=1)
    p_d5.add_argument("--max-retries", type=int, default=0)
    p_d5.add_argument(
        "--event-unseen",
        action="store_true",
        help="operator confirms Data Table precheck: event_id rows=0",
    )
    p_d5.add_argument(
        "--preview-approved",
        action="store_true",
        help="operator confirms REAL_SOURCE_PREVIEW_APPROVED_FOR_ONE_LIVE_POST",
    )
    p_d5.add_argument("--latest", action="store_true", help="forbidden")
    p_d5.add_argument("--watch", action="store_true", help="forbidden")

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(list(argv) if argv is not None else None)
    except SystemExit as exc:
        # argparse already printed usage
        code = exc.code
        if code is None:
            return EXIT_SUCCESS
        return int(code) if int(code) != 2 else EXIT_USAGE

    try:
        if args.command == "validate-only":
            return cmd_validate_only(args.fixture, debug=args.debug)
        if args.command == "build-envelope":
            return cmd_build_envelope(
                args.fixture, args.output, debug=args.debug
            )
        if args.command == "producer-dry-run":
            return cmd_producer_dry_run(
                args.fixture,
                transport=args.transport,
                mock_response=args.mock_response,
                evidence_dir=args.evidence_dir,
                profile_path=args.profile,
                concurrency=args.concurrency,
                live=args.live,
                apply=args.apply,
                with_auth=args.with_auth,
            )
        if args.command == "producer-fixture-test":
            return cmd_producer_fixture_test(args.mock_response, args.fixture)
        if args.command == "site002-adapter-dry-run":
            if getattr(args, "latest", False) or getattr(args, "watch", False):
                _print_result(
                    {
                        "ok": False,
                        "final_state": REAL_SOURCE_LIVE_DISPATCH_NOT_AUTHORIZED_D4,
                        "network_calls": 0,
                        "error": "auto-discovery/watch modes forbidden in D4",
                    }
                )
                return EXIT_NETWORK_NOT_AUTHORIZED
            return cmd_site002_adapter_dry_run(
                args.source,
                transport=args.transport,
                mock_response=args.mock_response,
                evidence_dir=args.evidence_dir,
                live=args.live,
                apply=args.apply,
                confirm_enable=args.confirm_enable,
                confirm_send=args.confirm_send,
            )
        if args.command == "push-webhook":
            return cmd_push_webhook()
        if args.command == "producer-d3-controlled-live":
            if (
                not args.dry_run
                and args.apply
                and args.mode == "first_seen"
                and args.fixture is None
            ):
                raise UsageError("--fixture required for FIRST_SEEN live apply")
            return cmd_producer_d3_controlled_live(
                fixture=args.fixture,
                mode=args.mode,
                apply=args.apply,
                dry_run=args.dry_run,
                confirm_enable=args.confirm_enable,
                confirm_send=args.confirm_send,
                profile_path=args.profile,
                evidence_dir=args.evidence_dir,
                concurrency=args.concurrency,
                max_retries=args.max_retries,
            )
        if args.command == "site002-controlled-live":
            return cmd_site002_controlled_live(
                source=args.source,
                apply=args.apply,
                dry_run=args.dry_run,
                preview_only=args.preview_only,
                confirm_enable=args.confirm_enable,
                confirm_send=args.confirm_send,
                environment=args.environment,
                profile_path=args.profile,
                evidence_dir=args.evidence_dir,
                concurrency=args.concurrency,
                max_retries=args.max_retries,
                event_unseen=args.event_unseen,
                preview_approved=args.preview_approved,
                latest=args.latest,
                watch=args.watch,
            )
        raise UsageError(f"unknown command: {args.command}")
    except UsageError as exc:
        sys.stderr.write(f"usage error: {exc}\n")
        return EXIT_USAGE
    except UnsafeOutputPathError as exc:
        sys.stderr.write(f"unsafe output path: {exc}\n")
        return EXIT_UNSAFE_OUTPUT_PATH
    except SequentialDispatchError as exc:
        sys.stderr.write(f"sequential guard: {exc}\n")
        return EXIT_CONCURRENCY_REJECTED
    except ProducerConfigError as exc:
        sys.stderr.write(f"config error: {redact_for_diagnostics(str(exc))}\n")
        return EXIT_CONFIG_INVALID
    except Exception as exc:  # noqa: BLE001 — map to exit 5 without stack by default
        sys.stderr.write(
            f"internal error: {redact_for_diagnostics(type(exc).__name__)}\n"
        )
        if getattr(args, "debug", False):
            sys.stderr.write(redact_for_diagnostics(traceback.format_exc(), 2000))
            sys.stderr.write("\n")
        return EXIT_INTERNAL


if __name__ == "__main__":
    raise SystemExit(main())
