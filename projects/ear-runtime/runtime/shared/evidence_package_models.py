"""EAR Runtime R2.1 evidence package models — contract-aligned data structures only.

Maps to EAR-EVIDENCE-PACKAGE-v1 (logical fields). Standard library only.
No filesystem access. No network. No persistence. No validation logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Connector outcome at evidence boundary (not package_quality_level).
CONNECTOR_STATUS_SUCCESS = "success"
CONNECTOR_STATUS_PARTIAL = "partial"
CONNECTOR_STATUS_FAILED = "failed"

# Logical artifact classification (R2.3 — index entry taxonomy; not acquisition-specific).
ARTIFACT_TYPE_IDENTITY = "identity"
ARTIFACT_TYPE_MANIFEST = "manifest"
ARTIFACT_TYPE_CONNECTOR_OUTPUT = "connector-output"
ARTIFACT_TYPE_LOG = "log"
ARTIFACT_TYPE_METADATA = "metadata"
ARTIFACT_TYPE_SAFE_UNKNOWN = "safe-unknown"
ARTIFACT_TYPE_OTHER = "other"

# Per-artifact availability (distinct from EvidenceStatus.connector_status).
ARTIFACT_STATUS_PRESENT = "present"
ARTIFACT_STATUS_MISSING = "missing"
ARTIFACT_STATUS_PARTIAL = "partial"
ARTIFACT_STATUS_SKIPPED = "skipped"
ARTIFACT_STATUS_UNKNOWN = "unknown"


@dataclass(frozen=True)
class EvidenceIdentity:
    """Session identity — acquisition_id, site_ref, connector_class (no evidence_id)."""

    acquisition_id: str
    site_ref: str
    connector_class: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "acquisition_id": self.acquisition_id,
            "site_ref": self.site_ref,
            "connector_class": self.connector_class,
        }


@dataclass(frozen=True)
class EvidenceProvenance:
    """Provenance metadata — string timestamps only (no datetime parsing)."""

    channel: str
    started_at: str
    completed_at: str
    operator_approval_ref: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "channel": self.channel,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "operator_approval_ref": self.operator_approval_ref,
        }


@dataclass(frozen=True)
class EvidenceScopeEcho:
    """Approved vs attempted scope — lists of path/table labels."""

    approved_scope: tuple[str, ...] = field(default_factory=tuple)
    attempted_scope: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "approved_scope": list(self.approved_scope),
            "attempted_scope": list(self.attempted_scope),
        }


@dataclass(frozen=True)
class EvidenceArtifact:
    """Single logical artifact index entry.

    artifact_ref is an opaque logical or future storage pointer — never validated here.
    status is per-artifact availability, not package-level connector_status.
    """

    artifact_type: str
    artifact_ref: str
    status: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_type": self.artifact_type,
            "artifact_ref": self.artifact_ref,
            "status": self.status,
        }


@dataclass(frozen=True)
class EvidenceArtifactIndex:
    """Logical artifact index — count plus ordered entries (not a filesystem listing)."""

    artifact_count: int
    artifacts: tuple[EvidenceArtifact, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_count": self.artifact_count,
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
        }


@dataclass(frozen=True)
class EvidenceStatus:
    """Connector-level acquisition outcome at evidence boundary."""

    connector_status: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "connector_status": self.connector_status,
        }


@dataclass(frozen=True)
class EvidencePackage:
    """Contract-aligned evidence package aggregate (R2.1 model layer only)."""

    identity: EvidenceIdentity
    provenance: EvidenceProvenance
    scope_echo: EvidenceScopeEcho
    artifact_index: EvidenceArtifactIndex
    status: EvidenceStatus
    warnings: tuple[str, ...] = field(default_factory=tuple)
    errors: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "identity": self.identity.to_dict(),
            "provenance": self.provenance.to_dict(),
            "scope_echo": self.scope_echo.to_dict(),
            "artifact_index": self.artifact_index.to_dict(),
            "status": self.status.to_dict(),
            "warnings": list(self.warnings),
            "errors": list(self.errors),
        }
