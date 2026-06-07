"""EAR Runtime R2.7 evidence package builder — contract-shaped in-memory assembly only.

Maps Manifest + Config + mock connector metadata to R2.1 EvidencePackage.
Standard library only. No filesystem access. No network. No persistence.
"""

from __future__ import annotations

from typing import Any

from shared.evidence_package_models import (
    ARTIFACT_STATUS_PRESENT,
    ARTIFACT_TYPE_MANIFEST,
    ARTIFACT_TYPE_METADATA,
    CONNECTOR_STATUS_SUCCESS,
    EvidenceArtifact,
    EvidenceArtifactIndex,
    EvidenceIdentity,
    EvidencePackage,
    EvidenceProvenance,
    EvidenceScopeEcho,
    EvidenceStatus,
)
from shared.manifest_models import Manifest
from shared.persistence_contract import build_mock_acquisition_id

# Fixed mock session timestamps — matches mock_listing convention; no datetime parsing.
_MOCK_STARTED_AT = "2026-06-04T12:00:00Z"
_MOCK_COMPLETED_AT = "2026-06-04T12:00:01Z"

# Logical artifact refs (opaque; no filesystem or quarantine paths).
_MANIFEST_ARTIFACT_REF = "manifest:primary"
_LISTING_SUMMARY_REF = "listing:summary"

_ALLOWED_CONNECTOR_STATUSES: frozenset[str] = frozenset(
    {"success", "partial", "failed"}
)


def build_mock_evidence_acquisition_id(site_id: str, manifest_source: str) -> str:
    """Deterministic mock acquisition_id — unified with mock persist layout (R-R2.2-04).

    Strategy: ``acq-mock-{site_id}-{manifest_source}`` via ``build_mock_acquisition_id``.
    No ``evidence_id`` — not in EAR-EVIDENCE-PACKAGE-v1.
    """
    return build_mock_acquisition_id(site_id, manifest_source)


def _build_identity(manifest: Manifest, config: dict[str, Any]) -> EvidenceIdentity:
    site_id = config["site_id"]
    return EvidenceIdentity(
        acquisition_id=build_mock_evidence_acquisition_id(site_id, manifest.source),
        site_ref=site_id,
        connector_class=config["connector"],
    )


def _build_provenance(config: dict[str, Any], manifest: Manifest) -> EvidenceProvenance:
    pilot_id = config.get("pilot_id", "")
    operator_ref = pilot_id if isinstance(pilot_id, str) and pilot_id.strip() else "mock-operator-approval"
    return EvidenceProvenance(
        channel=manifest.source,
        started_at=_MOCK_STARTED_AT,
        completed_at=_MOCK_COMPLETED_AT,
        operator_approval_ref=operator_ref,
    )


def _build_scope_echo(config: dict[str, Any]) -> tuple[EvidenceScopeEcho, tuple[str, ...]]:
    """Build scope echo from config. Returns (scope_echo, warnings).

    Config has ``allowed_paths`` / ``excluded_paths`` — not ``approved_scope`` /
    ``attempted_scope``. Mapping:
    - ``approved_scope`` ← ``allowed_paths`` when list
    - ``attempted_scope`` ← ``attempted_scope`` config key if present, else
      ``allowed_paths`` (mock assumes attempted equals approved when side missing)
    """
    warnings: list[str] = []
    allowed = config.get("allowed_paths", [])
    approved: tuple[str, ...] = tuple(allowed) if isinstance(allowed, list) else tuple()

    if "attempted_scope" in config and isinstance(config["attempted_scope"], list):
        attempted = tuple(str(item) for item in config["attempted_scope"])
    elif isinstance(allowed, list):
        attempted = tuple(allowed)
        if not attempted:
            warnings.append(
                "scope_echo: attempted_scope SAFE UNKNOWN — config lacks attempted_scope "
                "and allowed_paths is empty; emitted empty attempted_scope"
            )
    else:
        attempted = tuple()
        warnings.append(
            "scope_echo: attempted_scope SAFE UNKNOWN — config lacks attempted_scope "
            "and allowed_paths is not a list"
        )

    if "approved_scope" not in config:
        warnings.append(
            "scope_echo: approved_scope mapped from allowed_paths — "
            "config lacks explicit approved_scope field"
        )

    return EvidenceScopeEcho(approved_scope=approved, attempted_scope=attempted), tuple(warnings)


def _build_artifact_index(manifest: Manifest) -> EvidenceArtifactIndex:
    artifacts: list[EvidenceArtifact] = [
        EvidenceArtifact(
            artifact_type=ARTIFACT_TYPE_MANIFEST,
            artifact_ref=_MANIFEST_ARTIFACT_REF,
            status=ARTIFACT_STATUS_PRESENT,
        ),
        EvidenceArtifact(
            artifact_type=ARTIFACT_TYPE_METADATA,
            artifact_ref=_LISTING_SUMMARY_REF,
            status=ARTIFACT_STATUS_PRESENT,
        ),
    ]
    return EvidenceArtifactIndex(
        artifact_count=len(artifacts),
        artifacts=tuple(artifacts),
    )


def _resolve_connector_status(connector_metadata: dict[str, Any] | None) -> str:
    if connector_metadata and isinstance(connector_metadata.get("connector_status"), str):
        status = connector_metadata["connector_status"]
        if status in _ALLOWED_CONNECTOR_STATUSES:
            return status
    return CONNECTOR_STATUS_SUCCESS


def build_contract_evidence_package(
    manifest: Manifest,
    config: dict[str, Any],
    connector_metadata: dict[str, Any] | None = None,
) -> EvidencePackage:
    """Build an R2.1 contract-shaped EvidencePackage in memory only."""
    scope_echo, scope_warnings = _build_scope_echo(config)
    warnings = list(scope_warnings)

    connector_status = _resolve_connector_status(connector_metadata)
    errors: tuple[str, ...] = tuple()
    if connector_status == "failed":
        errors = ("connector session failed (mock metadata)",)

    return EvidencePackage(
        identity=_build_identity(manifest, config),
        provenance=_build_provenance(config, manifest),
        scope_echo=scope_echo,
        artifact_index=_build_artifact_index(manifest),
        status=EvidenceStatus(connector_status=connector_status),
        warnings=tuple(warnings),
        errors=errors,
    )
