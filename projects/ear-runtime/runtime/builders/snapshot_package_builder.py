"""EAR Runtime R3.5 candidate snapshot package builder — in-memory transformation only.

Maps R2.1 EvidencePackage to R3.1 SnapshotPackage per R2.6 handoff, R3.2 identity,
R3.3 section assembly, and R3.4 safe-unknown propagation.
Standard library only. No filesystem. No network. No persistence. No writes.
"""

from __future__ import annotations

from typing import Any

from shared.evidence_package_models import (
    ARTIFACT_STATUS_MISSING,
    ARTIFACT_STATUS_UNKNOWN,
    ARTIFACT_TYPE_MANIFEST,
    ARTIFACT_TYPE_SAFE_UNKNOWN,
    CONNECTOR_STATUS_FAILED,
    CONNECTOR_STATUS_PARTIAL,
    EvidencePackage,
)
from shared.handoff_contract import (
    CANDIDATE_PACKAGE_QUALITY_LEVEL,
    CAT_CONTRACT_GAP,
    CAT_DEFERRED_EXPANSION,
    CAT_FAILED_ACQUISITION,
    CAT_MISSING_EVIDENCE,
    CAT_PARTIAL_ACQUISITION,
    CAT_SCOPE_LIMITATION,
    CAT_UNSUPPORTED_CAPABILITY,
    TOPIC_ACQUISITION_LOG,
    TOPIC_ACQUISITION_OUTCOME,
    TOPIC_DATABASE_METADATA,
    TOPIC_EXTENSION_INVENTORY,
    TOPIC_FILE_MANIFEST,
    TOPIC_METADATA_EAR_MODE,
    TOPIC_OCMOD_INVENTORY,
    TOPIC_PARTIAL_ACQUISITION,
    TOPIC_SCOPE_DELTA,
    TOPIC_SCOPE_ECHO,
    TOPIC_SEO_STRUCTURE,
    TOPIC_THEME_INFO,
    build_mock_snapshot_id,
    build_snapshot_identity,
    is_handoff_eligible,
    metadata_parent_contract,
    transform_site_ref_to_site_id,
)
from shared.snapshot_package_models import (
    ENVIRONMENT_UNKNOWN,
    SnapshotAcquisitionLog,
    SnapshotDatabaseMetadata,
    SnapshotEnvironment,
    SnapshotExtensionInventory,
    SnapshotFileManifest,
    SnapshotMetadata,
    SnapshotOcmodInventory,
    SnapshotPackage,
    SnapshotSafeUnknown,
    SnapshotSafeUnknownEntry,
    SnapshotSeoStructure,
    SnapshotThemeInfo,
)

# Fixed assembly timestamp echo — matches mock evidence convention; no datetime parsing.
_DEFAULT_CREATED_AT = "2026-06-04T12:00:01Z"

_CONFIG_ENVIRONMENT_MAP: dict[str, str] = {
    "test": "TEST",
    "dev": "DEV",
    "development": "DEV",
    "staging": "STAGING",
    "production": "PRODUCTION",
    "prod": "PRODUCTION",
}


def _normalize_environment_class(config: dict[str, Any]) -> str:
    raw = config.get("environment", "")
    if not isinstance(raw, str) or not raw.strip():
        return ENVIRONMENT_UNKNOWN
    normalized = raw.strip().upper()
    if normalized in {"TEST", "DEV", "STAGING", "PRODUCTION"}:
        return normalized
    lowered = raw.strip().lower()
    return _CONFIG_ENVIRONMENT_MAP.get(lowered, ENVIRONMENT_UNKNOWN)


def _resolve_ear_mode(config: dict[str, Any]) -> tuple[str, SnapshotSafeUnknownEntry | None]:
    ear_mode = config.get("ear_mode", "")
    if isinstance(ear_mode, str) and ear_mode.strip():
        return ear_mode.strip(), None
    mode = config.get("mode", "")
    if isinstance(mode, str) and mode.strip():
        return mode.strip(), None
    return "", SnapshotSafeUnknownEntry(
        topic=TOPIC_METADATA_EAR_MODE,
        reason=f"[{CAT_MISSING_EVIDENCE}] ear_mode not declared in config echo",
        impact="EAR mode traceability incomplete on candidate package",
        unblock_hint="config:ear_mode",
    )


def _scope_summary(scope: tuple[str, ...]) -> str:
    if not scope:
        return ""
    return ", ".join(scope)


def _build_metadata(
    evidence: EvidencePackage,
    identity_snapshot_id: str,
    config: dict[str, Any],
    ear_mode: str,
) -> SnapshotMetadata:
    provenance = evidence.provenance
    created_at = (
        provenance.completed_at.strip()
        if provenance.completed_at.strip()
        else provenance.started_at.strip() or _DEFAULT_CREATED_AT
    )
    acquisition_date = provenance.completed_at.strip() or provenance.started_at.strip()
    approved = evidence.scope_echo.approved_scope
    attempted = evidence.scope_echo.attempted_scope
    scope_parts: list[str] = []
    if approved:
        scope_parts.append(f"approved={_scope_summary(approved)}")
    if attempted:
        scope_parts.append(f"attempted={_scope_summary(attempted)}")
    acquisition_scope = "; ".join(scope_parts)

    return SnapshotMetadata(
        parent_contract=metadata_parent_contract(),
        created_at=created_at,
        ear_mode=ear_mode,
        operator_approval=provenance.operator_approval_ref,
        package_quality_level=CANDIDATE_PACKAGE_QUALITY_LEVEL,
        platform=config.get("platform", "") if isinstance(config.get("platform"), str) else "",
        version=config.get("version", "") if isinstance(config.get("version"), str) else "",
        detected_version="",
        site_display_name="",
        acquisition_date=acquisition_date,
        acquisition_scope=acquisition_scope,
        baseline_candidate="",
        baseline_approved="",
        consumer_target="",
        bulk_root="",
        prior_snapshot_ref="",
        snapshot_sequence="",
    )


def _build_environment(
    evidence: EvidencePackage,
    config: dict[str, Any],
) -> SnapshotEnvironment:
    environment_class = _normalize_environment_class(config)
    weak_signals: list[str] = []
    for warning in evidence.warnings:
        if isinstance(warning, str) and warning.strip():
            weak_signals.append(warning.strip())
    return SnapshotEnvironment(
        environment_class=environment_class,
        operator_assertion="",
        weak_signals=tuple(weak_signals),
        multi_store_note="",
    )


def _build_acquisition_log(
    evidence: EvidencePackage,
    ear_mode: str,
) -> SnapshotAcquisitionLog:
    provenance = evidence.provenance
    identity = evidence.identity
    connector_status = evidence.status.connector_status
    partial_run = "true" if connector_status in {CONNECTOR_STATUS_PARTIAL, CONNECTOR_STATUS_FAILED} else ""

    return SnapshotAcquisitionLog(
        approved_by=provenance.operator_approval_ref,
        approved_at=provenance.started_at,
        ear_mode=ear_mode,
        channel=provenance.channel,
        connector_class=identity.connector_class,
        started_at=provenance.started_at,
        completed_at=provenance.completed_at,
        scope_approved=evidence.scope_echo.approved_scope,
        scope_attempted=evidence.scope_echo.attempted_scope,
        partial_run=partial_run,
        hitl_reference=provenance.operator_approval_ref,
        tooling_note="R3.5 candidate assembly — no quarantine expansion",
    )


def _section_is_empty_file_manifest(section: SnapshotFileManifest) -> bool:
    return (
        not section.root_folders
        and not section.path_entries
        and not section.file_counts
        and not section.version_proof_files
    )


def _section_is_empty_theme_info(section: SnapshotThemeInfo) -> bool:
    return not section.active_storefront_theme and not section.installed_themes


def _section_is_empty_database_metadata(section: SnapshotDatabaseMetadata) -> bool:
    return (
        not section.database_engine
        and not section.table_prefix
        and section.table_count is None
        and not section.table_list
    )


def _section_is_empty_seo_structure(section: SnapshotSeoStructure) -> bool:
    return not section.seo_urls_enabled and not section.rewrite_indicators


def _section_is_empty_extension_inventory(section: SnapshotExtensionInventory) -> bool:
    return not section.installed_extensions and not section.detected_modules


def _section_is_empty_ocmod_inventory(section: SnapshotOcmodInventory) -> bool:
    return not section.modifications and not section.unknown_modifications


def _find_manifest_artifact(evidence: EvidencePackage):
    for artifact in evidence.artifact_index.artifacts:
        if artifact.artifact_type == ARTIFACT_TYPE_MANIFEST:
            return artifact
    return None


def _propagate_safe_unknown(
    evidence: EvidencePackage,
    sections: dict[str, Any],
    ear_mode_entry: SnapshotSafeUnknownEntry | None,
) -> SnapshotSafeUnknown:
    """Build safe-unknown entries per R3.4 propagation matrix — no fabrication."""
    entries: list[SnapshotSafeUnknownEntry] = []
    connector_status = evidence.status.connector_status

    if connector_status == CONNECTOR_STATUS_FAILED:
        summary = (
            evidence.errors[0]
            if evidence.errors
            else "connector session failed at evidence boundary"
        )
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_ACQUISITION_OUTCOME,
                reason=f"[{CAT_FAILED_ACQUISITION}] {summary}",
                impact="candidate L0 only; L1 sections require re-acquisition",
                unblock_hint="connector:retry-acquisition",
            )
        )
    elif connector_status == CONNECTOR_STATUS_PARTIAL:
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_PARTIAL_ACQUISITION,
                reason=(
                    f"[{CAT_PARTIAL_ACQUISITION}] connector_status partial — "
                    "scope or artifacts incomplete"
                ),
                impact="sections not fully acquired; baseline diff may be blocked",
                unblock_hint="connector:complete-scope",
            )
        )

    approved = set(evidence.scope_echo.approved_scope)
    attempted = set(evidence.scope_echo.attempted_scope)
    if attempted - approved:
        delta = ", ".join(sorted(attempted - approved))
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_SCOPE_DELTA,
                reason=f"[{CAT_SCOPE_LIMITATION}] attempted paths not in approved scope: {delta}",
                impact="affected sections may be incomplete or excluded",
                unblock_hint="operator:scope-approval",
            )
        )

    if not evidence.scope_echo.approved_scope and not evidence.scope_echo.attempted_scope:
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_SCOPE_ECHO,
                reason=f"[{CAT_SCOPE_LIMITATION}] scope echo empty — completeness unknown",
                impact="structural and inventory sections cannot be scope-verified",
                unblock_hint="config:allowed_paths",
            )
        )

    manifest_artifact = _find_manifest_artifact(evidence)
    file_manifest = sections["file_manifest"]
    if manifest_artifact is None:
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_FILE_MANIFEST,
                reason=f"[{CAT_MISSING_EVIDENCE}] no manifest-class artifact in evidence index",
                impact="no structural proof for baseline diff",
                unblock_hint="acquisition:manifest",
            )
        )
    elif manifest_artifact.status in {ARTIFACT_STATUS_MISSING, ARTIFACT_STATUS_UNKNOWN}:
        category = (
            CAT_CONTRACT_GAP
            if manifest_artifact.status == ARTIFACT_STATUS_UNKNOWN
            else CAT_MISSING_EVIDENCE
        )
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_FILE_MANIFEST,
                reason=(
                    f"[{category}] manifest artifact {manifest_artifact.artifact_ref!r} "
                    f"status={manifest_artifact.status}"
                ),
                impact="file-manifest section cannot be populated",
                unblock_hint="acquisition:manifest",
            )
        )
    elif _section_is_empty_file_manifest(file_manifest):
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_FILE_MANIFEST,
                reason=(
                    f"[{CAT_CONTRACT_GAP}] manifest ref present but expansion not performed "
                    "at R3.5 — no quarantine bulk read"
                ),
                impact="structural inventory absent on candidate package",
                unblock_hint="level:1-manifest-expansion",
            )
        )

    if _section_is_empty_theme_info(sections["theme_info"]):
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_THEME_INFO,
                reason=(
                    f"[{CAT_MISSING_EVIDENCE}] theme-info not populated — "
                    "no theme signals in evidence expansion"
                ),
                impact="theme-dependent consumer phases blocked",
                unblock_hint="acquisition:theme-metadata",
            )
        )

    if _section_is_empty_database_metadata(sections["database_metadata"]):
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_DATABASE_METADATA,
                reason=(
                    f"[{CAT_UNSUPPORTED_CAPABILITY}] database-metadata not populated — "
                    "SFTP-only mock path without DB read channel"
                ),
                impact="schema-level baseline diff blocked",
                unblock_hint="proc:db-readonly-pma",
            )
        )

    if _section_is_empty_seo_structure(sections["seo_structure"]):
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_SEO_STRUCTURE,
                reason=(
                    f"[{CAT_MISSING_EVIDENCE}] seo-structure not populated — "
                    "no SEO metadata artifact expansion"
                ),
                impact="SEO routing indicators unavailable",
                unblock_hint="acquisition:seo-metadata",
            )
        )

    if _section_is_empty_extension_inventory(sections["extension_inventory"]):
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_EXTENSION_INVENTORY,
                reason=(
                    f"[{CAT_DEFERRED_EXPANSION}] extension-inventory deferred — "
                    "L2+ section not in R3 L1 engineering scope"
                ),
                impact="extension risk phase blocked until Level 2 acquisition",
                unblock_hint="level:2-acquisition",
            )
        )

    if _section_is_empty_ocmod_inventory(sections["ocmod_inventory"]):
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_OCMOD_INVENTORY,
                reason=(
                    f"[{CAT_DEFERRED_EXPANSION}] ocmod-inventory deferred — "
                    "L2+ section not in R3 L1 engineering scope"
                ),
                impact="modification conflict analysis blocked until Level 2 acquisition",
                unblock_hint="level:2-acquisition",
            )
        )

    for artifact in evidence.artifact_index.artifacts:
        if artifact.artifact_type == ARTIFACT_TYPE_SAFE_UNKNOWN:
            entries.append(
                SnapshotSafeUnknownEntry(
                    topic=f"artifact:{artifact.artifact_ref}",
                    reason=(
                        f"[{CAT_CONTRACT_GAP}] evidence artifact_type safe-unknown "
                        f"for ref {artifact.artifact_ref!r}"
                    ),
                    impact="artifact class unresolved at evidence boundary",
                    unblock_hint="evidence:classify-artifact",
                )
            )

    for warning in evidence.warnings:
        if isinstance(warning, str) and warning.strip():
            entries.append(
                SnapshotSafeUnknownEntry(
                    topic=TOPIC_SCOPE_ECHO,
                    reason=f"[scope-limitation] evidence warning: {warning.strip()}",
                    impact="assembly completeness may be affected",
                    unblock_hint="",
                )
            )

    if not provenance_has_approved_at(evidence) and connector_status != CONNECTOR_STATUS_FAILED:
        entries.append(
            SnapshotSafeUnknownEntry(
                topic=TOPIC_ACQUISITION_LOG,
                reason=(
                    f"[scope-limitation] approved_at derived from started_at — "
                    "no dedicated evidence field"
                ),
                impact="audit timestamp precision limited on candidate",
                unblock_hint="",
            )
        )

    if ear_mode_entry is not None:
        entries.append(ear_mode_entry)

    return SnapshotSafeUnknown(entries=tuple(entries))


def provenance_has_approved_at(evidence: EvidencePackage) -> bool:
    """Evidence has no dedicated approved_at — always False at R3.5."""
    return False


def build_candidate_snapshot_package(
    evidence: EvidencePackage,
    config: dict[str, Any],
    *,
    r2_validation: dict[str, Any] | None = None,
    require_handoff_eligibility: bool = True,
) -> SnapshotPackage:
    """Transform R2 EvidencePackage into R3 candidate SnapshotPackage in memory only."""
    if require_handoff_eligibility:
        eligible, eligibility_errors = is_handoff_eligible(evidence, r2_validation)
        if not eligible:
            raise ValueError(
                "handoff not eligible: " + "; ".join(eligibility_errors)
            )

    snapshot_id = build_mock_snapshot_id(
        transform_site_ref_to_site_id(evidence.identity.site_ref),
        evidence.identity.connector_class,
    )
    identity = build_snapshot_identity(evidence.identity, snapshot_id)

    ear_mode, ear_mode_entry = _resolve_ear_mode(config)

    empty_sections = {
        "file_manifest": SnapshotFileManifest(),
        "theme_info": SnapshotThemeInfo(),
        "extension_inventory": SnapshotExtensionInventory(),
        "ocmod_inventory": SnapshotOcmodInventory(),
        "database_metadata": SnapshotDatabaseMetadata(),
        "seo_structure": SnapshotSeoStructure(),
    }

    safe_unknown = _propagate_safe_unknown(
        evidence,
        empty_sections,
        ear_mode_entry,
    )

    return SnapshotPackage(
        identity=identity,
        metadata=_build_metadata(evidence, snapshot_id, config, ear_mode),
        environment=_build_environment(evidence, config),
        file_manifest=empty_sections["file_manifest"],
        theme_info=empty_sections["theme_info"],
        extension_inventory=empty_sections["extension_inventory"],
        ocmod_inventory=empty_sections["ocmod_inventory"],
        database_metadata=empty_sections["database_metadata"],
        seo_structure=empty_sections["seo_structure"],
        safe_unknown=safe_unknown,
        acquisition_log=_build_acquisition_log(evidence, ear_mode),
    )

