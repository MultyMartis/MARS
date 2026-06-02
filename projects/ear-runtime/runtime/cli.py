"""EAR Runtime CLI — skeleton and config validation only. No connector or live access."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_RUNTIME_ROOT = Path(__file__).resolve().parent
if str(_RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(_RUNTIME_ROOT))

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


def main() -> int:
    parser = argparse.ArgumentParser(description="EAR Runtime CLI")
    parser.add_argument(
        "--config",
        metavar="PATH",
        help="Path to runtime config JSON (validation only; no live access)",
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

    _print_loaded_config(config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
