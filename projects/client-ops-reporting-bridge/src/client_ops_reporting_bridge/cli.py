"""Offline CLI for Phase 1A exporter core + Phase 1B-D2/D3 producer.

Modes:
  validate-only         — normalize; print sanitized result; no envelope write
  build-envelope        — write distributable envelope to an approved local path
  producer-dry-run      — offline producer with mock/fixture/disabled transport
  producer-fixture-test — run a named mock classification once
  push-webhook          — ALWAYS blocked (use producer-d3-controlled-live)
  producer-d3-controlled-live — D3-gated real HTTPS (exact phrases + --apply)

Ordinary dry-run never reaches network. Import causes no network.
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
    EXIT_CONCURRENCY_REJECTED,
    EXIT_CONFIG_INVALID,
    EXIT_NETWORK_NOT_AUTHORIZED,
    MOCK_FIXTURE_NAMES,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D2,
    NETWORK_DISPATCH_NOT_AUTHORIZED_D3,
    TRANSPORT_DISABLED,
    TRANSPORT_MOCK,
)
from .producer_d3 import run_producer_d3_controlled
from .producer_d3_gates import build_authorization, default_d3_runs_dir
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
    if live or apply or transport.strip().lower() == "http":
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
