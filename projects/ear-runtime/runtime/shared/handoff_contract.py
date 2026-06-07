"""EAR Runtime R3.5 handoff contract — R2 → R3 boundary helpers only.

Authoritative helpers per R2.6, R3.2, R3.3, R3.4. Standard library only.
No I/O. No persistence. No filesystem. No network. Contract only.
"""

from __future__ import annotations

from typing import Any

from shared.evidence_package_models import (
    CONNECTOR_STATUS_FAILED,
    CONNECTOR_STATUS_PARTIAL,
    CONNECTOR_STATUS_SUCCESS,
    EvidenceIdentity,
    EvidencePackage,
)
from shared.snapshot_package_models import (
    PARENT_CONTRACT,
    SNAPSHOT_CONTRACT,
    SnapshotIdentity,
)

# Candidate quality — R3 assembly default; R5 certifies possession.
CANDIDATE_PACKAGE_QUALITY_LEVEL = 0

# Production snapshot_id algorithm — not implemented at R3.5.
PRODUCTION_SNAPSHOT_ID_ALGORITHM = "SAFE_UNKNOWN"

# Mock snapshot_id prefix — dry-run / --contract-snapshot only (ID-R3-14).
MOCK_SNAPSHOT_ID_PREFIX = "snap-mock-"

# Canonical safe-unknown topics (R3.4 registry).
TOPIC_ACQUISITION_OUTCOME = "acquisition_outcome"
TOPIC_PARTIAL_ACQUISITION = "partial_acquisition"
TOPIC_FILE_MANIFEST = "file-manifest"
TOPIC_THEME_INFO = "theme-info"
TOPIC_DATABASE_METADATA = "database-metadata"
TOPIC_SEO_STRUCTURE = "seo-structure"
TOPIC_EXTENSION_INVENTORY = "extension-inventory"
TOPIC_OCMOD_INVENTORY = "ocmod-inventory"
TOPIC_SCOPE_DELTA = "scope_delta"
TOPIC_SCOPE_ECHO = "scope_echo"
TOPIC_ENVIRONMENT = "environment"
TOPIC_LIVE_VERSION_PROOF = "live_version_proof"
TOPIC_METADATA_EAR_MODE = "metadata.ear_mode"
TOPIC_METADATA_PLATFORM = "metadata.platform"
TOPIC_ACQUISITION_LOG = "acquisition-log"

# Safe-unknown category slugs for reason prefixes (SU-CAT-*).
CAT_MISSING_EVIDENCE = "missing-evidence"
CAT_PARTIAL_ACQUISITION = "partial-acquisition"
CAT_FAILED_ACQUISITION = "failed-acquisition"
CAT_DEFERRED_EXPANSION = "deferred-expansion"
CAT_SCOPE_LIMITATION = "scope-limitation"
CAT_UNSUPPORTED_CAPABILITY = "unsupported-capability"
CAT_CONTRACT_GAP = "contract-gap"

_ALLOWED_CONNECTOR_STATUSES: frozenset[str] = frozenset(
    {
        CONNECTOR_STATUS_SUCCESS,
        CONNECTOR_STATUS_PARTIAL,
        CONNECTOR_STATUS_FAILED,
    }
)

_REQUIRED_IDENTITY_FIELDS: tuple[str, ...] = (
    "acquisition_id",
    "site_ref",
    "connector_class",
)


def build_mock_snapshot_id(site_id: str, connector_class: str) -> str:
    """Deterministic mock snapshot_id for candidate generation only.

    Format: ``snap-mock-{site_id}-{connector_class}`` per R3.5 mock path.
    Forbidden in production Store or Publish paths (ID-R3-14).
    """
    return f"{MOCK_SNAPSHOT_ID_PREFIX}{site_id}-{connector_class}"


def transform_site_ref_to_site_id(site_ref: str) -> str:
    """R2 ``site_ref`` → R3 ``site_id`` — 1:1 value rename (ID-CONT-02)."""
    return site_ref


def build_snapshot_identity(
    evidence_identity: EvidenceIdentity,
    snapshot_id: str,
) -> SnapshotIdentity:
    """Create R3 SnapshotIdentity from evidence identity + new snapshot_id."""
    return SnapshotIdentity(
        snapshot_id=snapshot_id,
        acquisition_id=evidence_identity.acquisition_id,
        site_id=transform_site_ref_to_site_id(evidence_identity.site_ref),
        snapshot_contract=SNAPSHOT_CONTRACT,
    )


def check_identity_continuity(
    evidence_identity: EvidenceIdentity,
    snapshot_identity: SnapshotIdentity,
) -> list[str]:
    """Verify ID-CONT-01/02 invariants between evidence and snapshot identity."""
    errors: list[str] = []

    if snapshot_identity.acquisition_id != evidence_identity.acquisition_id:
        errors.append(
            "identity continuity: acquisition_id must equal evidence acquisition_id"
        )

    expected_site_id = transform_site_ref_to_site_id(evidence_identity.site_ref)
    if snapshot_identity.site_id != expected_site_id:
        errors.append(
            "identity continuity: site_id must equal evidence site_ref value"
        )

    if snapshot_identity.snapshot_contract != SNAPSHOT_CONTRACT:
        errors.append(
            f"identity continuity: snapshot_contract must be {SNAPSHOT_CONTRACT!r}"
        )

    if not snapshot_identity.snapshot_id.strip():
        errors.append("identity continuity: snapshot_id must be non-empty")

    if snapshot_identity.snapshot_id == evidence_identity.acquisition_id:
        errors.append(
            "identity continuity: snapshot_id must not equal acquisition_id"
        )

    return errors


def is_handoff_eligible(
    package: EvidencePackage,
    r2_validation: dict[str, Any] | None = None,
) -> tuple[bool, list[str]]:
    """Check R2 → R3 handoff eligibility (HO-INV-13).

    Requires non-empty evidence identity fields and R2 structural pass when
    ``r2_validation`` is supplied.
    """
    errors: list[str] = []
    identity = package.identity

    for field_name in _REQUIRED_IDENTITY_FIELDS:
        value = getattr(identity, field_name, "")
        if not isinstance(value, str) or not value.strip():
            errors.append(f"handoff eligibility: identity.{field_name} required")

    connector_status = package.status.connector_status
    if connector_status not in _ALLOWED_CONNECTOR_STATUSES:
        errors.append(
            "handoff eligibility: status.connector_status must be "
            "success, partial, or failed"
        )

    if r2_validation is not None:
        if not r2_validation.get("valid", False):
            r2_errors = r2_validation.get("errors", [])
            if isinstance(r2_errors, list) and r2_errors:
                errors.append(
                    f"handoff eligibility: R2 validation failed — {r2_errors[0]}"
                )
            else:
                errors.append("handoff eligibility: R2 validation failed")

    return len(errors) == 0, errors


def build_identity_continuity_record(
    evidence_identity: EvidenceIdentity,
    snapshot_id: str,
) -> dict[str, str]:
    """Identity Continuity Record — minimal correlation map (H-OUT-04)."""
    return {
        "acquisition_id": evidence_identity.acquisition_id,
        "snapshot_id": snapshot_id,
        "site_ref": evidence_identity.site_ref,
        "site_id": transform_site_ref_to_site_id(evidence_identity.site_ref),
        "connector_class": evidence_identity.connector_class,
    }


def metadata_parent_contract() -> str:
    """Constant parent contract for metadata section."""
    return PARENT_CONTRACT
