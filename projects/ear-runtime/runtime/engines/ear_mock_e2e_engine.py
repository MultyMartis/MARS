"""EAR Runtime Mock E2E Flow — in-memory orchestration only.

Wires existing R2 contract evidence, R3 candidate snapshot, R5 Validate Engine,
and R4 Publish Engine skeletons into a single mock end-to-end path.
Standard library only. No network. No Store writes. No SFTP execution.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_RUNTIME_ROOT = Path(__file__).resolve().parent.parent
if str(_RUNTIME_ROOT) not in sys.path:
    sys.path.insert(0, str(_RUNTIME_ROOT))

from builders.evidence_package_builder import build_contract_evidence_package
from builders.manifest_builder import build_manifest
from builders.snapshot_package_builder import build_candidate_snapshot_package
from engines.ear_publish_engine import PublishEngineOutput, run_publish
from engines.ear_validate_engine import ValidateEngineOutput, run_validate
from shared.config_loader import ConfigValidationError, load_config
from shared.evidence_package_models import EvidencePackage
from shared.mock_listing import build_mock_listing
from shared.publish_eligibility_models import PUBLISH_ELIGIBILITY_ELIGIBLE
from shared.publish_result_models import PUBLISH_RESULT_SUCCESS
from shared.snapshot_package_models import SnapshotPackage
from shared.validation_result_models import VALIDATION_STATUS_PASS
from validators.evidence_package_validator import validate_contract_evidence_package
from shared.listing_validator import validate_listing_result
from validators.manifest_validator import validate_manifest
from validators.snapshot_package_validator import validate_candidate_snapshot_package

ENGINE_VERSION = "ear-mock-e2e-engine-v1"


@dataclass(frozen=True)
class E2EFlowSummary:
    """Lightweight mock E2E outcome summary — orchestration record only."""

    flow_id: str
    engine_version: str
    site_id: str
    acquisition_id: str
    snapshot_id: str
    validation_status: str
    publish_result_state: str
    ids_linked: bool
    id_linkage_notes: tuple[str, ...] = field(default_factory=tuple)
    r2_structural_pass: bool = False
    r3_assembly_pass: bool = False
    safe_unknown_count: int = 0
    in_memory_only: bool = True
    network_access: bool = False
    store_writes: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "flow_id": self.flow_id,
            "engine_version": self.engine_version,
            "site_id": self.site_id,
            "acquisition_id": self.acquisition_id,
            "snapshot_id": self.snapshot_id,
            "validation_status": self.validation_status,
            "publish_result_state": self.publish_result_state,
            "ids_linked": self.ids_linked,
            "id_linkage_notes": list(self.id_linkage_notes),
            "r2_structural_pass": self.r2_structural_pass,
            "r3_assembly_pass": self.r3_assembly_pass,
            "safe_unknown_count": self.safe_unknown_count,
            "in_memory_only": self.in_memory_only,
            "network_access": self.network_access,
            "store_writes": self.store_writes,
        }


@dataclass(frozen=True)
class E2EMockBundle:
    """Authoritative mock E2E output bundle — no persistence."""

    config: dict[str, Any]
    evidence_package: EvidencePackage
    snapshot_package: SnapshotPackage
    validate_output: ValidateEngineOutput
    publish_output: PublishEngineOutput
    summary: E2EFlowSummary

    def to_dict(self) -> dict[str, Any]:
        return {
            "config": {
                "site_id": self.config.get("site_id"),
                "pilot_id": self.config.get("pilot_id"),
                "connector": self.config.get("connector"),
                "mode": self.config.get("mode"),
                "snapshot_target": self.config.get("snapshot_target"),
                "dry_run": self.config.get("dry_run"),
            },
            "evidence_package": self.evidence_package.to_dict(),
            "snapshot_package": self.snapshot_package.to_dict(),
            "validate_output": self.validate_output.to_dict(),
            "publish_output": self.publish_output.to_dict(),
            "summary": self.summary.to_dict(),
        }


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _resolve_config(config: dict[str, Any] | str | Path) -> dict[str, Any]:
    if isinstance(config, dict):
        return dict(config)
    return load_config(config)


def _parse_target_certify_level(config: dict[str, Any]) -> int | None:
    target = config.get("snapshot_target", "")
    if isinstance(target, str) and target.startswith("level_"):
        suffix = target.split("_", 1)[1]
        if suffix.isdigit():
            return int(suffix)
    return None


def _operator_ref(config: dict[str, Any]) -> str:
    pilot_id = config.get("pilot_id", "")
    if isinstance(pilot_id, str) and pilot_id.strip():
        return f"operator:{pilot_id.strip()}"
    return "operator:mock-e2e"


def _build_contract_upstream(
    config: dict[str, Any],
) -> tuple[EvidencePackage, SnapshotPackage, bool, bool]:
    """Build R2 evidence and R3 candidate snapshot via mock listing path only."""
    listing = build_mock_listing()
    listing_validation = validate_listing_result(listing)
    if not listing_validation["valid"]:
        raise ValueError(
            "mock listing validation failed: "
            + "; ".join(listing_validation.get("errors", ()))
        )

    manifest = build_manifest(listing)
    manifest_validation = validate_manifest(manifest)
    if not manifest_validation["valid"]:
        raise ValueError(
            "mock manifest validation failed: "
            + "; ".join(manifest_validation.get("errors", ()))
        )

    connector_metadata = {"connector_status": "success"}
    evidence = build_contract_evidence_package(
        manifest,
        config,
        connector_metadata,
    )
    evidence_validation = validate_contract_evidence_package(evidence)
    r2_pass = bool(evidence_validation["valid"])
    if not r2_pass:
        raise ValueError(
            "R2 contract evidence validation failed: "
            + "; ".join(evidence_validation.get("errors", ()))
        )

    snapshot = build_candidate_snapshot_package(
        evidence,
        config,
        r2_validation=evidence_validation,
    )
    snapshot_validation = validate_candidate_snapshot_package(snapshot, evidence)
    r3_pass = bool(snapshot_validation["valid"])
    if not r3_pass:
        raise ValueError(
            "R3 candidate snapshot validation failed: "
            + "; ".join(snapshot_validation.get("errors", ()))
        )

    return evidence, snapshot, r2_pass, r3_pass


def _verify_id_linkage(
    evidence: EvidencePackage,
    snapshot: SnapshotPackage,
    validate_output: ValidateEngineOutput,
    publish_output: PublishEngineOutput,
) -> tuple[bool, tuple[str, ...]]:
    notes: list[str] = []
    snapshot_id = snapshot.identity.snapshot_id
    acquisition_id = snapshot.identity.acquisition_id

    if evidence.identity.acquisition_id != acquisition_id:
        notes.append("evidence.acquisition_id != snapshot.acquisition_id")

    validation_result = validate_output.validation_result
    if validation_result.audit.validated_snapshot_id != snapshot_id:
        notes.append("validation_result.validated_snapshot_id mismatch")

    report = validate_output.validate_report
    if report.summary.snapshot_id != snapshot_id:
        notes.append("validate_report.snapshot_id mismatch")
    if report.result_ref != validation_result.result_id:
        notes.append("validate_report.result_ref mismatch")

    recommendation = validate_output.publish_eligibility_recommendation
    if recommendation.snapshot_id != snapshot_id:
        notes.append("publish_eligibility.snapshot_id mismatch")
    if recommendation.validation_result_ref != validation_result.result_id:
        notes.append("publish_eligibility.validation_result_ref mismatch")
    if recommendation.validate_report_ref != report.report_id:
        notes.append("publish_eligibility.validate_report_ref mismatch")

    publish_result = publish_output.publish_result
    if publish_result.snapshot_id != snapshot_id:
        notes.append("publish_result.snapshot_id mismatch")
    if publish_result.validation_result_ref != validation_result.result_id:
        notes.append("publish_result.validation_result_ref mismatch")
    if publish_result.publish_recommendation_ref != recommendation.recommendation_id:
        notes.append("publish_result.publish_recommendation_ref mismatch")

    if publish_output.published_snapshot is not None:
        if publish_output.published_snapshot.identity.snapshot_id != snapshot_id:
            notes.append("published_snapshot.snapshot_id mismatch")
        if (
            publish_output.published_snapshot.publication.validation_result_ref
            != validation_result.result_id
        ):
            notes.append("published_snapshot.validation_result_ref mismatch")

    return not notes, tuple(notes)


def run_mock_e2e_flow(
    config: dict[str, Any] | str | Path,
    *,
    hitl_approved: bool = True,
    operator_publish_approval_ref: str = "hitl:mock-e2e-approve-001",
    consumer_target: str = "ocpilot",
    validate_sign_off_ref: str = "validate:mock-e2e-signoff-001",
    run_at: str | None = None,
) -> E2EMockBundle:
    """Run mock E2E flow: Config → Evidence → Snapshot → Validate → Publish.

    Accepts a config dict or path to a validated runtime config JSON.
    Raises ConfigValidationError, ValueError on precondition failures.
    Does not write filesystem state or access network.
    """
    resolved = _resolve_config(config)
    timestamp = run_at or _utc_now_iso()
    operator = _operator_ref(resolved)
    target_level = _parse_target_certify_level(resolved)

    evidence, snapshot, r2_pass, r3_pass = _build_contract_upstream(resolved)

    validate_output = run_validate(
        snapshot,
        target_certify_level=target_level,
        operator_ref=operator,
        validated_at=timestamp,
        r2_structural_pass=r2_pass,
        r3_assembly_pass=r3_pass,
    )

    publish_output = run_publish(
        snapshot,
        validation_result=validate_output.validation_result,
        validate_report=validate_output.validate_report,
        publish_eligibility=validate_output.publish_eligibility_recommendation,
        hitl_approved=hitl_approved,
        operator_publish_approval_ref=operator_publish_approval_ref,
        consumer_target=consumer_target,
        published_by=operator,
        published_at=timestamp,
        validate_sign_off_ref=validate_sign_off_ref,
        in_memory_path=True,
        store_placement_confirmed=False,
    )

    ids_linked, linkage_notes = _verify_id_linkage(
        evidence,
        snapshot,
        validate_output,
        publish_output,
    )

    flow_id = f"e2e-mock-{snapshot.identity.snapshot_id}-{timestamp.replace(':', '').replace('+', '')}"
    summary = E2EFlowSummary(
        flow_id=flow_id,
        engine_version=ENGINE_VERSION,
        site_id=snapshot.identity.site_id,
        acquisition_id=snapshot.identity.acquisition_id,
        snapshot_id=snapshot.identity.snapshot_id,
        validation_status=validate_output.validation_result.summary.status.value,
        publish_result_state=publish_output.publish_result.publish_result_state,
        ids_linked=ids_linked,
        id_linkage_notes=linkage_notes,
        r2_structural_pass=r2_pass,
        r3_assembly_pass=r3_pass,
        safe_unknown_count=len(snapshot.safe_unknown.entries),
        in_memory_only=True,
        network_access=False,
        store_writes=False,
    )

    return E2EMockBundle(
        config=resolved,
        evidence_package=evidence,
        snapshot_package=snapshot,
        validate_output=validate_output,
        publish_output=publish_output,
        summary=summary,
    )


def _default_sample_config_path() -> Path:
    return Path(__file__).resolve().parent.parent / "configs" / "sample-r1-site-001.json"


def _run_verification() -> None:
    config_path = _default_sample_config_path()
    bundle = run_mock_e2e_flow(config_path)

    assert bundle.evidence_package is not None
    assert bundle.snapshot_package is not None
    assert (
        bundle.validate_output.validation_result.summary.status.value
        == VALIDATION_STATUS_PASS
    )
    assert (
        bundle.validate_output.publish_eligibility_recommendation.recommendation_state
        == PUBLISH_ELIGIBILITY_ELIGIBLE
    )
    assert (
        bundle.publish_output.publish_result.publish_result_state
        == PUBLISH_RESULT_SUCCESS
    )
    assert bundle.summary.ids_linked is True
    assert bundle.summary.in_memory_only is True
    assert bundle.summary.network_access is False
    assert bundle.summary.store_writes is False
    assert bundle.snapshot_package.identity.snapshot_id.startswith("snap-mock-")

    print("ear_mock_e2e_engine verification: PASS")
    print(f"  config: {config_path}")
    print(f"  snapshot_id: {bundle.summary.snapshot_id}")
    print(f"  acquisition_id: {bundle.summary.acquisition_id}")
    print(f"  validation_status: {bundle.summary.validation_status}")
    print(f"  publish_result_state: {bundle.summary.publish_result_state}")
    print(f"  ids_linked: {bundle.summary.ids_linked}")
    print(f"  safe_unknown_count: {bundle.summary.safe_unknown_count}")


if __name__ == "__main__":
    _run_verification()
