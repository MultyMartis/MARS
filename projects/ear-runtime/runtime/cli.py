"""EAR Runtime CLI — skeleton and config validation only. No connector or live access."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_RUNTIME_ROOT = Path(__file__).resolve().parent
if str(_RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(_RUNTIME_ROOT))

from connectors.sftp_connector import SFTPConnector
from shared.config_loader import ConfigValidationError, load_config


def _print_skeleton_banner() -> None:
    print("EAR Runtime")
    print()
    print("EAR Runtime v1")
    print("Skeleton Build")
    print()
    print("Runtime state: FOUNDATION ONLY")
    print("Implemented: NONE")
    print("Execution: NOT AUTHORIZED")
    print("Live access: FORBIDDEN")


def _print_loaded_config(config: dict) -> None:
    print("Config loaded:")
    print(f"  site_id: {config['site_id']}")
    print(f"  pilot_id: {config['pilot_id']}")
    print(f"  connector: {config['connector']}")
    print(f"  mode: {config['mode']}")
    print(f"  snapshot_target: {config['snapshot_target']}")
    print(f"  dry_run: {config['dry_run']}")
    print("  credential_ref: REDACTED")


def _print_connection_plan(plan: dict) -> None:
    print("Connection plan:")
    for key, value in plan.items():
        print(f"  {key}: {value}")


def _print_mock_listing_summary(summary: dict) -> None:
    print("Mock listing summary:")
    print(f"  source: {summary['source']}")
    print(f"  entry_count: {summary['entry_count']}")
    print(f"  excluded_count: {summary['excluded_count']}")
    print("  preview_paths:")
    for path in summary["preview_paths"]:
        print(f"    - {path}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def _print_mock_manifest_summary(summary: dict) -> None:
    print("Mock manifest summary:")
    print(f"  source: {summary['source']}")
    print(f"  entry_count: {summary['entry_count']}")
    print(f"  excluded_count: {summary['excluded_count']}")
    print("  preview_paths:")
    for path in summary["preview_paths"]:
        print(f"    - {path}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def _print_contract_snapshot_summary(summary: dict) -> None:
    print("Contract snapshot package summary:")
    print(f"  snapshot_id: {summary['snapshot_id']}")
    print(f"  acquisition_id: {summary['acquisition_id']}")
    print(f"  site_id: {summary['site_id']}")
    print(f"  safe_unknown_count: {summary['safe_unknown_count']}")
    if "package_quality_level" in summary:
        print(f"  package_quality_level: {summary['package_quality_level']}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def _print_contract_evidence_summary(summary: dict) -> None:
    print("Contract evidence package summary:")
    print(f"  acquisition_id: {summary['acquisition_id']}")
    print(f"  site_ref: {summary['site_ref']}")
    print(f"  connector_class: {summary['connector_class']}")
    print(f"  artifact_count: {summary['artifact_count']}")
    print(f"  connector_status: {summary['connector_status']}")
    if summary.get("warnings"):
        print("  warnings:")
        for warning in summary["warnings"]:
            print(f"    - {warning}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def _print_mock_evidence_summary(summary: dict) -> None:
    print("Mock evidence package summary:")
    print(f"  site_id: {summary['site_id']}")
    print(f"  connector: {summary['connector']}")
    print(f"  entry_count: {summary['entry_count']}")
    print(f"  excluded_count: {summary['excluded_count']}")
    print(f"  quality_level: {summary['quality_level']}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def _print_mock_snapshot_summary(summary: dict) -> None:
    print("Mock snapshot package summary:")
    if "snapshot_id" in summary:
        print(f"  snapshot_id: {summary['snapshot_id']}")
    print(f"  site_id: {summary['site_id']}")
    print(f"  connector: {summary['connector']}")
    print(f"  entry_count: {summary['entry_count']}")
    print(f"  excluded_count: {summary['excluded_count']}")
    print(f"  quality_level: {summary['quality_level']}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def _print_persist_mock_snapshot_summary(summary: dict) -> None:
    print("Mock snapshot persist summary:")
    if "snapshot_id" in summary:
        print(f"  snapshot_id: {summary['snapshot_id']}")
    if "acquisition_id" in summary:
        print(f"  acquisition_id: {summary['acquisition_id']}")
    if "output_root" in summary:
        print(f"  output_root: {summary['output_root']}")
    if "store_state" in summary:
        print(f"  store_state: {summary['store_state']}")
    if summary.get("written_files"):
        print("  persisted paths:")
        for name, path in summary["written_files"].items():
            print(f"    {name}: {path}")
    elif summary.get("paths"):
        print("  layout paths:")
        for key, path in summary["paths"].items():
            print(f"    {key}: {path}")
    validation = summary["validation"]
    status = "PASS" if validation["valid"] else "FAIL"
    print(f"  validation: {status}")
    if validation["errors"]:
        for error in validation["errors"]:
            print(f"    error: {error}")


def main() -> int:
    parser = argparse.ArgumentParser(description="EAR Runtime CLI")
    parser.add_argument(
        "--config",
        metavar="PATH",
        help="Path to runtime config JSON (validation only; no live access)",
    )
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Build and print a local connection plan (no network access)",
    )
    parser.add_argument(
        "--mock-listing",
        action="store_true",
        help="Build and print a mock remote listing (no network access)",
    )
    parser.add_argument(
        "--mock-manifest",
        action="store_true",
        help="Build and print a mock manifest from mock listing (no network access)",
    )
    parser.add_argument(
        "--mock-evidence",
        action="store_true",
        help="Build and print a mock evidence package (no network access)",
    )
    parser.add_argument(
        "--contract-evidence",
        action="store_true",
        help="Build and print R2 contract-shaped evidence package (no network access)",
    )
    parser.add_argument(
        "--contract-snapshot",
        action="store_true",
        help="Build R2 evidence → R3 candidate snapshot package (no network access)",
    )
    parser.add_argument(
        "--mock-snapshot",
        action="store_true",
        help="Build and print a mock snapshot package (no network access)",
    )
    parser.add_argument(
        "--persist-mock-snapshot",
        action="store_true",
        help="Build mock snapshot and persist to EAR Store under output_root (no network)",
    )
    args = parser.parse_args()

    if args.config is None:
        _print_skeleton_banner()
        return 0

    try:
        config = load_config(args.config)
    except ConfigValidationError as exc:
        print(f"Config validation failed: {exc}", file=sys.stderr)
        return 1

    connector = SFTPConnector(config)

    if (
        args.plan
        or args.mock_listing
        or args.mock_manifest
        or args.mock_evidence
        or args.contract_evidence
        or args.contract_snapshot
        or args.mock_snapshot
        or args.persist_mock_snapshot
    ):
        validation = connector.validate_config()
        if not validation["valid"]:
            print(
                f"Config validation failed: {validation['errors'][0]}",
                file=sys.stderr,
            )
            return 1

    if args.plan:
        _print_connection_plan(connector.build_connection_plan())
        return 0

    if args.mock_listing:
        summary = connector.build_mock_listing()
        _print_mock_listing_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    if args.mock_manifest:
        summary = connector.build_mock_manifest()
        _print_mock_manifest_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    if args.mock_evidence:
        summary = connector.build_mock_evidence_package()
        _print_mock_evidence_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    if args.contract_evidence:
        summary = connector.build_contract_evidence_package()
        _print_contract_evidence_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    if args.contract_snapshot:
        summary = connector.build_contract_snapshot_package()
        _print_contract_snapshot_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    if args.mock_snapshot:
        summary = connector.build_mock_snapshot_package()
        _print_mock_snapshot_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    if args.persist_mock_snapshot:
        summary = connector.persist_mock_snapshot_package()
        _print_persist_mock_snapshot_summary(summary)
        if not summary["validation"]["valid"]:
            return 1
        return 0

    _print_loaded_config(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
