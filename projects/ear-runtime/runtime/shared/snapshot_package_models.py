"""EAR Runtime R3.1 OpenCart Snapshot Package models — contract-aligned data structures only.

Maps to EAR-OPENCART-SNAPSHOT-SPEC-v1 logical section tree. Standard library only.
No filesystem access. No network. No persistence. No validation logic. No assembly logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Contract identifiers (normative per EAR-OPENCART-SNAPSHOT-SPEC-v1).
SNAPSHOT_CONTRACT = "ear-opencart-snapshot-v1"
PARENT_CONTRACT = "ear-snapshot-v1"

# Environment class enum (normative per OpenCart spec § environment).
ENVIRONMENT_TEST = "TEST"
ENVIRONMENT_DEV = "DEV"
ENVIRONMENT_STAGING = "STAGING"
ENVIRONMENT_PRODUCTION = "PRODUCTION"
ENVIRONMENT_UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class SnapshotIdentity:
    """R3 snapshot identity — distinct from evidence identity (no snapshot_id on evidence).

    snapshot_id is created by R3 at Store boundary. acquisition_id survives from R2.
    site_id is the OpenCart contract name for evidence site_ref.
    """

    snapshot_id: str
    acquisition_id: str
    site_id: str
    snapshot_contract: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "acquisition_id": self.acquisition_id,
            "site_id": self.site_id,
            "snapshot_contract": self.snapshot_contract,
        }


@dataclass(frozen=True)
class SnapshotMetadata:
    """metadata/ section — platform, acquisition context, contract links.

    package_quality_level is candidate default only (L0); R5 certifies possession.
    No publish metadata (published_at, published_by) — R4 future concern.
    """

    parent_contract: str
    created_at: str
    ear_mode: str
    operator_approval: str
    package_quality_level: int
    platform: str = ""
    version: str = ""
    detected_version: str = ""
    site_display_name: str = ""
    acquisition_date: str = ""
    acquisition_scope: str = ""
    baseline_candidate: str = ""
    baseline_approved: str = ""
    consumer_target: str = ""
    bulk_root: str = ""
    prior_snapshot_ref: str = ""
    snapshot_sequence: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "parent_contract": self.parent_contract,
            "created_at": self.created_at,
            "ear_mode": self.ear_mode,
            "operator_approval": self.operator_approval,
            "package_quality_level": self.package_quality_level,
            "platform": self.platform,
            "version": self.version,
            "detected_version": self.detected_version,
            "site_display_name": self.site_display_name,
            "acquisition_date": self.acquisition_date,
            "acquisition_scope": self.acquisition_scope,
            "baseline_candidate": self.baseline_candidate,
            "baseline_approved": self.baseline_approved,
            "consumer_target": self.consumer_target,
            "bulk_root": self.bulk_root,
            "prior_snapshot_ref": self.prior_snapshot_ref,
            "snapshot_sequence": self.snapshot_sequence,
        }


@dataclass(frozen=True)
class SnapshotEnvironment:
    """environment/ section — deployment class for consumer safety rules."""

    environment_class: str
    operator_assertion: str = ""
    weak_signals: tuple[str, ...] = field(default_factory=tuple)
    multi_store_note: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "environment_class": self.environment_class,
            "operator_assertion": self.operator_assertion,
            "weak_signals": list(self.weak_signals),
            "multi_store_note": self.multi_store_note,
        }


@dataclass(frozen=True)
class SnapshotManifestPathEntry:
    """Single relative path entry within file-manifest/."""

    relative_path: str
    size_bytes: int | None = None
    hash_value: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "relative_path": self.relative_path,
            "size_bytes": self.size_bytes,
            "hash_value": self.hash_value,
        }


@dataclass(frozen=True)
class SnapshotFileCount:
    """Per-folder file count summary within file-manifest/."""

    folder: str
    count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "folder": self.folder,
            "count": self.count,
        }


@dataclass(frozen=True)
class SnapshotFileManifest:
    """file-manifest/ section — structural inventory for baseline diff."""

    root_folders: tuple[str, ...] = field(default_factory=tuple)
    path_entries: tuple[SnapshotManifestPathEntry, ...] = field(default_factory=tuple)
    file_counts: tuple[SnapshotFileCount, ...] = field(default_factory=tuple)
    version_proof_files: tuple[str, ...] = field(default_factory=tuple)
    custom_folders: tuple[str, ...] = field(default_factory=tuple)
    missing_baseline_paths: tuple[str, ...] = field(default_factory=tuple)
    modified_core_indicators: tuple[str, ...] = field(default_factory=tuple)
    external_manifest_ref: str = ""
    upload_cache_exclusions: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "root_folders": list(self.root_folders),
            "path_entries": [entry.to_dict() for entry in self.path_entries],
            "file_counts": [count.to_dict() for count in self.file_counts],
            "version_proof_files": list(self.version_proof_files),
            "custom_folders": list(self.custom_folders),
            "missing_baseline_paths": list(self.missing_baseline_paths),
            "modified_core_indicators": list(self.modified_core_indicators),
            "external_manifest_ref": self.external_manifest_ref,
            "upload_cache_exclusions": list(self.upload_cache_exclusions),
        }


@dataclass(frozen=True)
class SnapshotThemeInfo:
    """theme-info/ section — active and installed theme surface."""

    active_storefront_theme: str = ""
    installed_themes: tuple[str, ...] = field(default_factory=tuple)
    theme_version_markers: tuple[str, ...] = field(default_factory=tuple)
    admin_theme: str = ""
    override_indicators: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "active_storefront_theme": self.active_storefront_theme,
            "installed_themes": list(self.installed_themes),
            "theme_version_markers": list(self.theme_version_markers),
            "admin_theme": self.admin_theme,
            "override_indicators": list(self.override_indicators),
        }


@dataclass(frozen=True)
class SnapshotExtensionEntry:
    """Single extension row within extension-inventory/."""

    extension_type: str
    code: str
    title: str = ""
    enabled: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "extension_type": self.extension_type,
            "code": self.code,
            "title": self.title,
            "enabled": self.enabled,
        }


@dataclass(frozen=True)
class SnapshotExtensionInventory:
    """extension-inventory/ section — L2+ target; placeholder at R3 L1."""

    installed_extensions: tuple[SnapshotExtensionEntry, ...] = field(default_factory=tuple)
    detected_modules: tuple[str, ...] = field(default_factory=tuple)
    detected_integrations: tuple[str, ...] = field(default_factory=tuple)
    unknown_extensions: tuple[str, ...] = field(default_factory=tuple)
    third_party_indicators: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "installed_extensions": [
                entry.to_dict() for entry in self.installed_extensions
            ],
            "detected_modules": list(self.detected_modules),
            "detected_integrations": list(self.detected_integrations),
            "unknown_extensions": list(self.unknown_extensions),
            "third_party_indicators": list(self.third_party_indicators),
        }


@dataclass(frozen=True)
class SnapshotOcmodEntry:
    """Single modification row within ocmod-inventory/."""

    mod_name: str
    enabled: str = ""
    mod_id: str = ""
    source: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "mod_name": self.mod_name,
            "enabled": self.enabled,
            "mod_id": self.mod_id,
            "source": self.source,
        }


@dataclass(frozen=True)
class SnapshotOcmodInventory:
    """ocmod-inventory/ section — L2+ target; placeholder at R3 L1."""

    modifications: tuple[SnapshotOcmodEntry, ...] = field(default_factory=tuple)
    unknown_modifications: tuple[str, ...] = field(default_factory=tuple)
    conflict_indicators: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "modifications": [entry.to_dict() for entry in self.modifications],
            "unknown_modifications": list(self.unknown_modifications),
            "conflict_indicators": list(self.conflict_indicators),
        }


@dataclass(frozen=True)
class SnapshotDatabaseMetadata:
    """database-metadata/ section — schema-level facts without row data."""

    database_engine: str = ""
    table_prefix: str = ""
    table_count: int | None = None
    table_list: tuple[str, ...] = field(default_factory=tuple)
    extra_tables: tuple[str, ...] = field(default_factory=tuple)
    missing_tables: tuple[str, ...] = field(default_factory=tuple)
    collation_summary: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "database_engine": self.database_engine,
            "table_prefix": self.table_prefix,
            "table_count": self.table_count,
            "table_list": list(self.table_list),
            "extra_tables": list(self.extra_tables),
            "missing_tables": list(self.missing_tables),
            "collation_summary": self.collation_summary,
        }


@dataclass(frozen=True)
class SnapshotSeoStructure:
    """seo-structure/ section — SEO and routing indicators at metadata level."""

    seo_urls_enabled: str = ""
    rewrite_indicators: tuple[str, ...] = field(default_factory=tuple)
    url_patterns: tuple[str, ...] = field(default_factory=tuple)
    custom_routing_indicators: tuple[str, ...] = field(default_factory=tuple)
    seo_extensions: tuple[str, ...] = field(default_factory=tuple)
    canonical_robots_indicators: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "seo_urls_enabled": self.seo_urls_enabled,
            "rewrite_indicators": list(self.rewrite_indicators),
            "url_patterns": list(self.url_patterns),
            "custom_routing_indicators": list(self.custom_routing_indicators),
            "seo_extensions": list(self.seo_extensions),
            "canonical_robots_indicators": list(self.canonical_robots_indicators),
        }


@dataclass(frozen=True)
class SnapshotSafeUnknownEntry:
    """Single honesty carrier within safe-unknown/."""

    topic: str
    reason: str
    impact: str
    unblock_hint: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "topic": self.topic,
            "reason": self.reason,
            "impact": self.impact,
            "unblock_hint": self.unblock_hint,
        }


@dataclass(frozen=True)
class SnapshotSafeUnknown:
    """safe-unknown/ section — explicit gaps; required on every candidate package."""

    entries: tuple[SnapshotSafeUnknownEntry, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "entries": [entry.to_dict() for entry in self.entries],
        }


@dataclass(frozen=True)
class SnapshotAcquisitionLog:
    """acquisition-log/ section — how evidence was obtained (not publish log).

    No published_by / published_at — publish metadata is R4 future concern.
    """

    approved_by: str = ""
    approved_at: str = ""
    ear_mode: str = ""
    channel: str = ""
    connector_class: str = ""
    started_at: str = ""
    completed_at: str = ""
    scope_approved: tuple[str, ...] = field(default_factory=tuple)
    scope_attempted: tuple[str, ...] = field(default_factory=tuple)
    partial_run: str = ""
    hitl_reference: str = ""
    tooling_note: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "approved_by": self.approved_by,
            "approved_at": self.approved_at,
            "ear_mode": self.ear_mode,
            "channel": self.channel,
            "connector_class": self.connector_class,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "scope_approved": list(self.scope_approved),
            "scope_attempted": list(self.scope_attempted),
            "partial_run": self.partial_run,
            "hitl_reference": self.hitl_reference,
            "tooling_note": self.tooling_note,
        }


@dataclass(frozen=True)
class SnapshotPackage:
    """OpenCart Snapshot Package aggregate (R3.1 model layer only).

    Authoritative at R3 assembly boundary; supersedes R1.7 flat SnapshotPackage
    for contract-shaped candidate output. Population deferred to R3.3–R3.5.
    """

    identity: SnapshotIdentity
    metadata: SnapshotMetadata
    environment: SnapshotEnvironment
    file_manifest: SnapshotFileManifest
    theme_info: SnapshotThemeInfo
    extension_inventory: SnapshotExtensionInventory
    ocmod_inventory: SnapshotOcmodInventory
    database_metadata: SnapshotDatabaseMetadata
    seo_structure: SnapshotSeoStructure
    safe_unknown: SnapshotSafeUnknown
    acquisition_log: SnapshotAcquisitionLog

    def to_dict(self) -> dict[str, Any]:
        return {
            "identity": self.identity.to_dict(),
            "metadata": self.metadata.to_dict(),
            "environment": self.environment.to_dict(),
            "file_manifest": self.file_manifest.to_dict(),
            "theme_info": self.theme_info.to_dict(),
            "extension_inventory": self.extension_inventory.to_dict(),
            "ocmod_inventory": self.ocmod_inventory.to_dict(),
            "database_metadata": self.database_metadata.to_dict(),
            "seo_structure": self.seo_structure.to_dict(),
            "safe_unknown": self.safe_unknown.to_dict(),
            "acquisition_log": self.acquisition_log.to_dict(),
        }
