"""Offline CLI for Phase 1A exporter core.

Modes:
  validate-only   — normalize; print sanitized result; no envelope write
  build-envelope  — write distributable envelope to an approved local path

No network, Storage publication, n8n, Telegram, or production access.
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
from .security_validator import redact_for_diagnostics

# Approved output roots for Phase 1A (resolved at runtime).
_PROJECT_ROOT = Path(__file__).resolve().parents[2]


def _is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def assert_safe_output_path(output: Path) -> Path:
    """Refuse paths outside project locus or system temp.

    Approved:
    - under ``projects/client-ops-reporting-bridge/``
    - under the process temporary directory
    """
    resolved = output.resolve()
    tmp_root = Path(tempfile.gettempdir()).resolve()
    if _is_under(resolved, _PROJECT_ROOT) or _is_under(resolved, tmp_root):
        # Deny writing into fixtures source trees accidentally replacing inputs
        fixtures = (_PROJECT_ROOT / "fixtures").resolve()
        if _is_under(resolved, fixtures) and resolved.parent == fixtures:
            raise UnsafeOutputPathError(
                "refusing to write envelope directly into fixtures root"
            )
        # Allow fixtures/*/out/ or project test-output/
        return resolved
    raise UnsafeOutputPathError(
        "output path outside approved Phase 1A boundaries "
        "(project locus or system temp)"
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="client_ops_reporting_bridge",
        description=(
            "Phase 1A offline exporter core — fixture validate / build only"
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
        raise UsageError(f"unknown command: {args.command}")
    except UsageError as exc:
        sys.stderr.write(f"usage error: {exc}\n")
        return EXIT_USAGE
    except UnsafeOutputPathError as exc:
        sys.stderr.write(f"unsafe output path: {exc}\n")
        return EXIT_UNSAFE_OUTPUT_PATH
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
