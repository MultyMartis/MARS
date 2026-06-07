"""EAR Runtime SFTP connector skeleton — plan and status only.

Standard library only. No paramiko. No network access. No credential resolution.
"""

from __future__ import annotations

from typing import Any

from shared.connector_contract import (
    CONNECTOR_CLASS,
    CONNECTOR_VERSION,
    EXECUTION_MODE_PLAN,
    IMPLEMENTATION_STATE,
    NETWORK_ACCESS,
    find_enum_violations,
    find_missing_required_fields,
)
from builders.evidence_builder import build_evidence_package
from builders.evidence_package_builder import build_contract_evidence_package
from builders.manifest_builder import build_manifest
from builders.snapshot_package_builder import build_candidate_snapshot_package
from builders.persistence_layout_builder import build_persistence_layout
from builders.snapshot_builder import build_snapshot_package
from persistence.snapshot_store import PersistenceError, persist_mock_snapshot
from shared.listing_validator import validate_listing_result
from shared.mock_listing import build_mock_listing
from validators.evidence_validator import validate_evidence_package
from validators.evidence_package_validator import validate_contract_evidence_package
from validators.manifest_validator import validate_manifest
from validators.persistence_validator import validate_persistence_layout
from validators.snapshot_package_validator import validate_candidate_snapshot_package
from validators.snapshot_validator import validate_snapshot_package


class SFTPConnector:
    """Connector skeleton for SFTP read-only acquisition planning."""

    def __init__(self, config: dict[str, Any]) -> None:
        self._config = config

    def validate_config(self) -> dict[str, Any]:
        """Check required fields and contract enums. No access attempts."""
        errors: list[str] = []
        missing = find_missing_required_fields(self._config)
        if missing:
            errors.append(
                f"Missing required field(s): {', '.join(missing)}"
            )
        errors.extend(find_enum_violations(self._config))
        return {
            "valid": len(errors) == 0,
            "errors": errors,
        }

    def build_connection_plan(self) -> dict[str, Any]:
        """Build a local connection plan. No credentials, host, or connection."""
        excluded_paths = self._config.get("excluded_paths", [])
        excluded_count = len(excluded_paths) if isinstance(excluded_paths, list) else 0
        return {
            "site_id": self._config.get("site_id"),
            "pilot_id": self._config.get("pilot_id"),
            "environment": self._config.get("environment"),
            "connector": self._config.get("connector"),
            "mode": self._config.get("mode"),
            "remote_root": self._config.get("remote_root"),
            "excluded_paths_count": excluded_count,
            "dry_run": self._config.get("dry_run"),
        }

    def get_connector_status(self) -> dict[str, str]:
        """Return connector capability metadata. Network access is disabled."""
        return {
            "connector_class": CONNECTOR_CLASS,
            "connector_version": CONNECTOR_VERSION,
            "execution_mode": EXECUTION_MODE_PLAN,
            "network_access": NETWORK_ACCESS,
            "implementation_state": IMPLEMENTATION_STATE,
        }

    def build_mock_listing(self) -> dict[str, Any]:
        """Build and validate a mock listing. No remote access or network."""
        listing = build_mock_listing()
        validation = validate_listing_result(listing)
        preview_limit = 5
        return {
            "source": listing.source,
            "entry_count": listing.entry_count,
            "excluded_count": listing.excluded_count,
            "preview_paths": [entry.path for entry in listing.entries[:preview_limit]],
            "validation": validation,
        }

    def build_mock_manifest(self) -> dict[str, Any]:
        """Build mock listing, manifest, and validate. No remote access or network."""
        listing = build_mock_listing()
        listing_validation = validate_listing_result(listing)
        if not listing_validation["valid"]:
            return {
                "source": listing.source,
                "entry_count": listing.entry_count,
                "excluded_count": listing.excluded_count,
                "preview_paths": [],
                "validation": listing_validation,
            }

        manifest = build_manifest(listing)
        validation = validate_manifest(manifest)
        preview_limit = 5
        return {
            "source": manifest.source,
            "entry_count": manifest.entry_count,
            "excluded_count": manifest.excluded_count,
            "preview_paths": [entry.path for entry in manifest.entries[:preview_limit]],
            "validation": validation,
        }

    def build_contract_snapshot_package(self) -> dict[str, Any]:
        """Build R2 evidence → R3 candidate snapshot in memory. No network or writes."""
        listing = build_mock_listing()
        listing_validation = validate_listing_result(listing)
        if not listing_validation["valid"]:
            return {
                "snapshot_id": None,
                "acquisition_id": None,
                "site_id": self._config.get("site_id"),
                "safe_unknown_count": 0,
                "validation": listing_validation,
            }

        manifest = build_manifest(listing)
        manifest_validation = validate_manifest(manifest)
        if not manifest_validation["valid"]:
            return {
                "snapshot_id": None,
                "acquisition_id": None,
                "site_id": self._config.get("site_id"),
                "safe_unknown_count": 0,
                "validation": manifest_validation,
            }

        connector_metadata = {
            "connector_status": "success",
            **self.get_connector_status(),
        }
        evidence = build_contract_evidence_package(
            manifest,
            self._config,
            connector_metadata,
        )
        evidence_validation = validate_contract_evidence_package(evidence)
        if not evidence_validation["valid"]:
            return {
                "snapshot_id": None,
                "acquisition_id": evidence.identity.acquisition_id,
                "site_id": evidence.identity.site_ref,
                "safe_unknown_count": 0,
                "validation": evidence_validation,
            }

        snapshot = build_candidate_snapshot_package(
            evidence,
            self._config,
            r2_validation=evidence_validation,
        )
        validation = validate_candidate_snapshot_package(snapshot, evidence)
        return {
            "snapshot_id": snapshot.identity.snapshot_id,
            "acquisition_id": snapshot.identity.acquisition_id,
            "site_id": snapshot.identity.site_id,
            "safe_unknown_count": len(snapshot.safe_unknown.entries),
            "package_quality_level": snapshot.metadata.package_quality_level,
            "validation": validation,
        }

    def build_contract_evidence_package(self) -> dict[str, Any]:
        """Build R2 contract-shaped evidence package in memory. No network or writes."""
        listing = build_mock_listing()
        listing_validation = validate_listing_result(listing)
        if not listing_validation["valid"]:
            return {
                "acquisition_id": None,
                "site_ref": self._config.get("site_id"),
                "connector_class": self._config.get("connector"),
                "artifact_count": 0,
                "connector_status": None,
                "validation": listing_validation,
            }

        manifest = build_manifest(listing)
        manifest_validation = validate_manifest(manifest)
        if not manifest_validation["valid"]:
            return {
                "acquisition_id": None,
                "site_ref": self._config.get("site_id"),
                "connector_class": self._config.get("connector"),
                "artifact_count": 0,
                "connector_status": None,
                "validation": manifest_validation,
            }

        connector_metadata = {
            "connector_status": "success",
            **self.get_connector_status(),
        }
        package = build_contract_evidence_package(
            manifest,
            self._config,
            connector_metadata,
        )
        validation = validate_contract_evidence_package(package)
        return {
            "acquisition_id": package.identity.acquisition_id,
            "site_ref": package.identity.site_ref,
            "connector_class": package.identity.connector_class,
            "artifact_count": package.artifact_index.artifact_count,
            "connector_status": package.status.connector_status,
            "warnings": list(package.warnings),
            "validation": validation,
        }

    def build_mock_evidence_package(self) -> dict[str, Any]:
        """Build mock listing through evidence package and validate. No network or writes."""
        listing = build_mock_listing()
        listing_validation = validate_listing_result(listing)
        if not listing_validation["valid"]:
            return {
                "site_id": self._config.get("site_id"),
                "connector": self._config.get("connector"),
                "entry_count": listing.entry_count,
                "excluded_count": listing.excluded_count,
                "quality_level": "mock",
                "validation": listing_validation,
            }

        manifest = build_manifest(listing)
        manifest_validation = validate_manifest(manifest)
        if not manifest_validation["valid"]:
            return {
                "site_id": self._config.get("site_id"),
                "connector": self._config.get("connector"),
                "entry_count": manifest.entry_count,
                "excluded_count": manifest.excluded_count,
                "quality_level": "mock",
                "validation": manifest_validation,
            }

        evidence = build_evidence_package(manifest, self._config)
        validation = validate_evidence_package(evidence)
        return {
            "site_id": evidence.site_id,
            "connector": evidence.connector,
            "entry_count": evidence.manifest_entry_count,
            "excluded_count": evidence.manifest_excluded_count,
            "quality_level": evidence.quality_level,
            "validation": validation,
        }

    def build_mock_snapshot_package(self) -> dict[str, Any]:
        """Build mock listing through snapshot package and validate. No network or writes."""
        listing = build_mock_listing()
        listing_validation = validate_listing_result(listing)
        if not listing_validation["valid"]:
            return {
                "site_id": self._config.get("site_id"),
                "connector": self._config.get("connector"),
                "entry_count": listing.entry_count,
                "excluded_count": listing.excluded_count,
                "quality_level": "mock",
                "validation": listing_validation,
            }

        manifest = build_manifest(listing)
        manifest_validation = validate_manifest(manifest)
        if not manifest_validation["valid"]:
            return {
                "site_id": self._config.get("site_id"),
                "connector": self._config.get("connector"),
                "entry_count": manifest.entry_count,
                "excluded_count": manifest.excluded_count,
                "quality_level": "mock",
                "validation": manifest_validation,
            }

        evidence = build_evidence_package(manifest, self._config)
        evidence_validation = validate_evidence_package(evidence)
        if not evidence_validation["valid"]:
            return {
                "site_id": evidence.site_id,
                "connector": evidence.connector,
                "entry_count": evidence.manifest_entry_count,
                "excluded_count": evidence.manifest_excluded_count,
                "quality_level": evidence.quality_level,
                "validation": evidence_validation,
            }

        snapshot = build_snapshot_package(evidence)
        validation = validate_snapshot_package(snapshot)
        return {
            "snapshot_id": snapshot.snapshot_id,
            "site_id": snapshot.site_id,
            "connector": snapshot.connector,
            "quality_level": snapshot.quality_level,
            "entry_count": snapshot.entry_count,
            "excluded_count": snapshot.excluded_count,
            "validation": validation,
        }

    def persist_mock_snapshot_package(self) -> dict[str, Any]:
        """Mock listing through Store persist. No network or acquisition."""
        listing = build_mock_listing()
        listing_validation = validate_listing_result(listing)
        if not listing_validation["valid"]:
            return {
                "site_id": self._config.get("site_id"),
                "connector": self._config.get("connector"),
                "validation": listing_validation,
            }

        manifest = build_manifest(listing)
        manifest_validation = validate_manifest(manifest)
        if not manifest_validation["valid"]:
            return {
                "site_id": self._config.get("site_id"),
                "connector": self._config.get("connector"),
                "validation": manifest_validation,
            }

        evidence = build_evidence_package(manifest, self._config)
        evidence_validation = validate_evidence_package(evidence)
        if not evidence_validation["valid"]:
            return {
                "site_id": evidence.site_id,
                "connector": evidence.connector,
                "validation": evidence_validation,
            }

        snapshot = build_snapshot_package(evidence)
        snapshot_validation = validate_snapshot_package(snapshot)
        if not snapshot_validation["valid"]:
            return {
                "snapshot_id": snapshot.snapshot_id,
                "site_id": snapshot.site_id,
                "validation": snapshot_validation,
            }

        layout = build_persistence_layout(snapshot, self._config)
        persistence_validation = validate_persistence_layout(layout, self._config)
        if not persistence_validation["valid"]:
            return {
                "snapshot_id": snapshot.snapshot_id,
                "acquisition_id": layout.get("acquisition_id"),
                "output_root": self._config.get("output_root"),
                "validation": persistence_validation,
            }

        try:
            persist_result = persist_mock_snapshot(snapshot, self._config)
        except PersistenceError as exc:
            return {
                "snapshot_id": snapshot.snapshot_id,
                "acquisition_id": layout.get("acquisition_id"),
                "output_root": self._config.get("output_root"),
                "validation": {
                    "valid": False,
                    "errors": [str(exc)],
                },
            }

        return {
            "snapshot_id": persist_result["snapshot_id"],
            "acquisition_id": persist_result["acquisition_id"],
            "output_root": persist_result["output_root"],
            "store_state": persist_result["store_state"],
            "paths": persist_result["paths"],
            "written_files": persist_result["written_files"],
            "validation": persist_result["validation"],
        }
