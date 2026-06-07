"""EAR Runtime persistence contract — constants and validation helpers only.

Single source of truth for store states and mock persist defaults.
Standard library only. No IO. No network.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

# Store lifecycle states (Store stage only — not Publish)
STORE_STATE_STORED = "stored"
STORE_STATE_UNPUBLISHED = "stored_unpublished"

ALLOWED_STORE_STATES: frozenset[str] = frozenset(
    {STORE_STATE_STORED, STORE_STATE_UNPUBLISHED}
)

# Mock pipeline defaults
DEFAULT_SNAPSHOT_SOURCE = "mock"
DEFAULT_CREATED_FROM = "mock_evidence_package"

# OpenCart contract identity (enriched at persist boundary per R1.8B)
SNAPSHOT_CONTRACT = "ear-opencart-snapshot-v1"
PARENT_CONTRACT = "ear-snapshot-v1"
DEFAULT_CONSUMER_TARGET = "ocpilot"
DEFAULT_PACKAGE_QUALITY_LEVEL_MOCK = 0

# Chartered EAR bulk root (R1.8C PC-03)
EAR_BULK_ROOT = Path(r"C:\AI MARS STORAGE\ear")

# OpenCart sections not populated by mock pipeline (R1.8B mock persist honesty)
MOCK_UNPOPULATED_SECTIONS: tuple[str, ...] = (
    "file-manifest",
    "theme-info",
    "extension-inventory",
    "ocmod-inventory",
    "database-metadata",
    "seo-structure",
)


def build_mock_acquisition_id(site_id: str, source: str) -> str:
    """Deterministic mock acquisition id — dry-run / mock persist only."""
    return f"acq-mock-{site_id}-{source}"


def is_valid_store_state(value: Any) -> bool:
    """Return True if value is an allowed store state string."""
    return isinstance(value, str) and value in ALLOWED_STORE_STATES


def find_store_state_violation(store_state: Any) -> str | None:
    """Return an error message if store_state is invalid, else None."""
    if not isinstance(store_state, str) or not store_state.strip():
        return "store_state must be a non-empty string"
    if store_state not in ALLOWED_STORE_STATES:
        allowed = ", ".join(sorted(ALLOWED_STORE_STATES))
        return f"store_state must be one of: {allowed}"
    return None


def output_root_under_ear_bulk(output_root: Path) -> bool:
    """Return True if resolved output_root is under the chartered EAR bulk root."""
    try:
        resolved = output_root.resolve()
        ear_root = EAR_BULK_ROOT.resolve()
        resolved.relative_to(ear_root)
        return True
    except (OSError, ValueError):
        return False
