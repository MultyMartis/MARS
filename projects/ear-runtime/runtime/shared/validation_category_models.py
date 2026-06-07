"""EAR Runtime R5.2 Validation Category models — ownership contracts only.

Authoritative R5 validation category registry distinct from R2 structural validation,
R3 assembly eligibility, Validate Engine, and R5-V-* rules.
Standard library only. No validation logic. No scoring. No Publish.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# R5 canonical category identifiers — not enums; align with validation_result_models.
VALIDATION_CATEGORY_IDENTITY = "identity"
VALIDATION_CATEGORY_STRUCTURE = "structure"
VALIDATION_CATEGORY_POSSESSION = "possession"
VALIDATION_CATEGORY_QUALITY = "quality"
VALIDATION_CATEGORY_REDACTION = "redaction"
VALIDATION_CATEGORY_READINESS = "readiness"
VALIDATION_CATEGORY_CONSISTENCY = "consistency"

VALIDATION_CATEGORY_OWNER_R5 = "R5"

CANONICAL_VALIDATION_CATEGORY_IDS: tuple[str, ...] = (
    VALIDATION_CATEGORY_IDENTITY,
    VALIDATION_CATEGORY_STRUCTURE,
    VALIDATION_CATEGORY_POSSESSION,
    VALIDATION_CATEGORY_QUALITY,
    VALIDATION_CATEGORY_REDACTION,
    VALIDATION_CATEGORY_READINESS,
    VALIDATION_CATEGORY_CONSISTENCY,
)


@dataclass(frozen=True)
class ValidationCategoryDescription:
    """Human-facing category title and purpose — no rule logic."""

    title: str
    purpose: str

    def to_dict(self) -> dict[str, Any]:
        return {"title": self.title, "purpose": self.purpose}


@dataclass(frozen=True)
class ValidationCategoryOwnership:
    """What R5 owns and explicitly excludes for a category."""

    owner: str
    owns: tuple[str, ...] = field(default_factory=tuple)
    does_not_own: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "owner": self.owner,
            "owns": list(self.owns),
            "does_not_own": list(self.does_not_own),
        }


@dataclass(frozen=True)
class ValidationCategoryScope:
    """Primary inputs and boundary notes — conceptual refs only."""

    primary_inputs: tuple[str, ...] = field(default_factory=tuple)
    r5_owns_certification: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "primary_inputs": list(self.primary_inputs),
            "r5_owns_certification": self.r5_owns_certification,
        }


@dataclass(frozen=True)
class ValidationCategoryReference:
    """Lightweight category pointer for findings, reports, and registry lookup."""

    category_id: str

    def to_dict(self) -> dict[str, Any]:
        return {"category_id": self.category_id}


@dataclass(frozen=True)
class ValidationCategory:
    """Single R5 validation category — ownership contract, not a validator."""

    category_id: str
    description: ValidationCategoryDescription
    ownership: ValidationCategoryOwnership
    scope: ValidationCategoryScope
    non_goals: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "category_id": self.category_id,
            "description": self.description.to_dict(),
            "ownership": self.ownership.to_dict(),
            "scope": self.scope.to_dict(),
            "non_goals": list(self.non_goals),
        }

    def to_reference(self) -> ValidationCategoryReference:
        return ValidationCategoryReference(category_id=self.category_id)


@dataclass(frozen=True)
class ValidationCategoryRegistry:
    """Canonical registry of all R5 validation categories."""

    categories: tuple[ValidationCategory, ...] = field(default_factory=tuple)

    def get(self, category_id: str) -> ValidationCategory | None:
        for category in self.categories:
            if category.category_id == category_id:
                return category
        return None

    def category_ids(self) -> tuple[str, ...]:
        return tuple(category.category_id for category in self.categories)

    def to_dict(self) -> dict[str, Any]:
        return {
            "categories": [category.to_dict() for category in self.categories],
        }


def _build_identity_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_IDENTITY,
        description=ValidationCategoryDescription(
            title="Identity",
            purpose=(
                "Snapshot and site identity integrity; contract version adequacy; "
                "acquisition correlation beyond R3 presence checks."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "snapshot identity certification",
                "contract identity consistency",
                "snapshot_id and acquisition_id correlation review",
                "site_id and contract id adequacy at Validate",
            ),
            does_not_own=(
                "snapshot creation",
                "snapshot_id generation",
                "section assembly",
                "evidence identity structural gate",
                "publish",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "snapshot identity block",
                "metadata parent_contract",
                "acquisition-log correlation",
                "identity continuity record",
            ),
        ),
        non_goals=(
            "R5-V-* rule implementation",
            "snapshot_id creation",
            "R3 assembly eligibility duplication",
        ),
    )


def _build_structure_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_STRUCTURE,
        description=ValidationCategoryDescription(
            title="Structure",
            purpose=(
                "OpenCart section tree adequacy vs spec skeleton; forbidden field absence; "
                "contract structure beyond R3 skeleton presence."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "contract structure adequacy",
                "section presence adequacy for certification target",
                "forbidden snapshot field absence review",
            ),
            does_not_own=(
                "section assembly",
                "section population",
                "candidate skeleton enforcement",
                "publish",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "SnapshotPackage aggregate section tree",
                "OpenCart snapshot spec skeleton",
                "serialized forbidden-key scan",
            ),
        ),
        non_goals=(
            "R3-V-* assembly rules",
            "section content population",
            "Validate Engine dispatch",
        ),
    )


def _build_possession_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_POSSESSION,
        description=ValidationCategoryDescription(
            title="Possession",
            purpose=(
                "Section content adequacy for target certify level; corroboration where "
                "required; gap honesty vs safe-unknown at Validate."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "section-level possession adequacy for target level",
                "safe-unknown completeness review for certify level",
                "corroboration requirements where architecture mandates",
            ),
            does_not_own=(
                "section assembly and population",
                "L0-L3 level assignment",
                "candidate package_quality_level default",
                "publish",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "section payloads",
                "safe-unknown entries",
                "target certify level declaration",
            ),
        ),
        non_goals=(
            "quality level mapping formulas",
            "R3 gap propagation rules",
            "scoring or weighting",
        ),
    )


def _build_quality_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_QUALITY,
        description=ValidationCategoryDescription(
            title="Quality",
            purpose=(
                "Map possession assessment to certified L0-L3; downgrade paths; "
                "inflation detection — certification concept only."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "certified package_quality_level assignment on Validate pass",
                "L0-L3 certification mapping",
                "downgrade policy application",
                "quality inflation detection",
            ),
            does_not_own=(
                "section assembly",
                "section possession adequacy checks",
                "candidate quality placeholder",
                "published quality freeze",
                "publish",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "possession assessment outcomes",
                "EAR-OPENCART-QUALITY-MAPPING concepts",
                "target certify level",
            ),
        ),
        non_goals=(
            "scoring formulas",
            "weighted quality indexes",
            "percentages",
            "R3 candidate default enforcement",
        ),
    )


def _build_redaction_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_REDACTION,
        description=ValidationCategoryDescription(
            title="Redaction",
            purpose=(
                "Secret, credential, and unsafe-publication review on candidate snapshot "
                "serializations bound for consumer paths."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "candidate redaction review",
                "secret exposure findings",
                "credential leakage findings",
                "unsafe publication blockers",
            ),
            does_not_own=(
                "evidence quarantine policy",
                "R2 evidence serialization policy checks",
                "assembly copy-avoidance rules",
                "automated redaction engine product",
                "publish",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "candidate snapshot serialization",
                "section payloads",
                "bulk refs and metadata fields",
            ),
        ),
        non_goals=(
            "redaction scanners",
            "heuristic secret detection algorithms",
            "evidence quarantine mutation",
        ),
    )


def _build_readiness_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_READINESS,
        description=ValidationCategoryDescription(
            title="Readiness",
            purpose=(
                "Gate G2-G4 checklist semantics; Publish Eligibility Recommendation "
                "inputs — advisory only."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "readiness gate G2-G4 semantic mapping",
                "Publish Eligibility Recommendation inputs",
                "precondition status aggregation for operator report",
            ),
            does_not_own=(
                "Publish execution",
                "consumer delivery",
                "operator HITL workflow product",
                "validated Store state marker persist",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "ValidationResult aggregate outcome",
                "category findings across Identity-Consistency",
                "EAR-READINESS-GATES definitions",
                "R2/R3 precondition flags when supplied",
            ),
        ),
        non_goals=(
            "Publish metadata assignment",
            "readiness algorithms beyond gate mapping",
            "automatic Publish without HITL",
        ),
    )


def _build_consistency_category() -> ValidationCategory:
    return ValidationCategory(
        category_id=VALIDATION_CATEGORY_CONSISTENCY,
        description=ValidationCategoryDescription(
            title="Consistency",
            purpose=(
                "Evidence-to-snapshot provenance alignment; identity continuity; "
                "read-only evidence use — not R2 structural re-run."
            ),
        ),
        ownership=ValidationCategoryOwnership(
            owner=VALIDATION_CATEGORY_OWNER_R5,
            owns=(
                "evidence-to-snapshot provenance alignment",
                "identity continuity cross-check",
                "acquisition-log correlation with evidence chain",
            ),
            does_not_own=(
                "R2 structural validation re-implementation",
                "evidence generation",
                "evidence quarantine writes",
                "snapshot assembly",
                "publish",
            ),
        ),
        scope=ValidationCategoryScope(
            primary_inputs=(
                "Evidence Package read-only",
                "Identity Continuity Record",
                "acquisition-log section",
                "snapshot identity block",
            ),
        ),
        non_goals=(
            "R2-V-* rule duplication as certification",
            "evidence Package mutation",
            "full evidence re-validation",
        ),
    )


CANONICAL_VALIDATION_CATEGORY_REGISTRY = ValidationCategoryRegistry(
    categories=(
        _build_identity_category(),
        _build_structure_category(),
        _build_possession_category(),
        _build_quality_category(),
        _build_redaction_category(),
        _build_readiness_category(),
        _build_consistency_category(),
    ),
)
