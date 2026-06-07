"""EAR Runtime R5.3 Quality Possession models — certification concepts only.

Authoritative L0–L3 possession level registry distinct from R3 candidate assembly,
R5 Validate Engine, R5-V-* rules, and R4 Publish.
Standard library only. No scoring. No thresholds. No certification algorithms.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Canonical quality level identifiers — not enums; align with package_quality_level 0–3.
QUALITY_LEVEL_L0 = 0
QUALITY_LEVEL_L1 = 1
QUALITY_LEVEL_L2 = 2
QUALITY_LEVEL_L3 = 3

CANONICAL_QUALITY_LEVEL_IDS: tuple[int, ...] = (
    QUALITY_LEVEL_L0,
    QUALITY_LEVEL_L1,
    QUALITY_LEVEL_L2,
    QUALITY_LEVEL_L3,
)

# Claim stage — distinguishes R3 candidate placeholder from R5 certified possession.
QUALITY_CLAIM_STAGE_CANDIDATE = "candidate"
QUALITY_CLAIM_STAGE_CERTIFIED = "certified"

QUALITY_POSSESSION_OWNER_R5 = "R5"

# R3 candidate default — honest placeholder; NOT R5 certified L0 (VB-R3-06; Q-INV-R5-01).
CANDIDATE_PACKAGE_QUALITY_LEVEL = 0


@dataclass(frozen=True)
class QualityPossessionDescription:
    """Human-facing level title and purpose — no certification logic."""

    title: str
    purpose: str

    def to_dict(self) -> dict[str, Any]:
        return {"title": self.title, "purpose": self.purpose}


@dataclass(frozen=True)
class QualityPossessionReference:
    """Lightweight level pointer for assessments, findings, and registry lookup."""

    level_id: int

    def to_dict(self) -> dict[str, Any]:
        return {"level_id": self.level_id}


@dataclass(frozen=True)
class QualityPossessionLevel:
    """Single L0–L3 certification concept — ownership contract, not a validator."""

    level_id: int
    description: QualityPossessionDescription
    ownership: tuple[str, ...] = field(default_factory=tuple)
    non_goals: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "level_id": self.level_id,
            "description": self.description.to_dict(),
            "ownership": list(self.ownership),
            "non_goals": list(self.non_goals),
        }

    def to_reference(self) -> QualityPossessionReference:
        return QualityPossessionReference(level_id=self.level_id)


@dataclass(frozen=True)
class QualityPossessionAssessment:
    """Conceptual possession assessment record — no scoring or certification algorithms.

    claim_stage distinguishes R3 candidate placeholder from R5 certified possession.
    Same numeric level_id may carry different semantic meaning per stage (VB-R3-06).
    """

    assessment_id: str
    claim_stage: str
    level: QualityPossessionReference
    target_level: QualityPossessionReference | None = None
    summary: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "assessment_id": self.assessment_id,
            "claim_stage": self.claim_stage,
            "level": self.level.to_dict(),
            "target_level": (
                self.target_level.to_dict()
                if self.target_level is not None
                else None
            ),
            "summary": self.summary,
        }


@dataclass(frozen=True)
class QualityPossessionRegistry:
    """Canonical registry of all R5 quality possession levels L0–L3."""

    levels: tuple[QualityPossessionLevel, ...] = field(default_factory=tuple)

    def get(self, level_id: int) -> QualityPossessionLevel | None:
        for level in self.levels:
            if level.level_id == level_id:
                return level
        return None

    def level_ids(self) -> tuple[int, ...]:
        return tuple(level.level_id for level in self.levels)

    def to_dict(self) -> dict[str, Any]:
        return {
            "levels": [level.to_dict() for level in self.levels],
        }


def _build_l0_level() -> QualityPossessionLevel:
    return QualityPossessionLevel(
        level_id=QUALITY_LEVEL_L0,
        description=QualityPossessionDescription(
            title="Identity only",
            purpose=(
                "Minimum honest identity and audit trail; all non-acquired sections "
                "listed in safe-unknown; no structural or extension claims."
            ),
        ),
        ownership=(
            f"{QUALITY_POSSESSION_OWNER_R5} certifies site and package identity",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies environment class or explicit UNKNOWN",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies acquisition-log minimum audit fields",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies safe-unknown honesty for all gaps",
        ),
        non_goals=(
            "baseline diff capability",
            "structural file proof",
            "extension or ocMod analysis",
            "scoring formulas or percentages",
            "R3 candidate placeholder semantics",
        ),
    )


def _build_l1_level() -> QualityPossessionLevel:
    return QualityPossessionLevel(
        level_id=QUALITY_LEVEL_L1,
        description=QualityPossessionDescription(
            title="Identity + structure",
            purpose=(
                "Level 0 plus version proof, file-manifest subset, database-metadata, "
                "seo-structure, and theme-info adequacy or honest section-level safe-unknown."
            ),
        ),
        ownership=(
            f"{QUALITY_POSSESSION_OWNER_R5} certifies version proof or explicit safe-unknown",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies file-manifest subset adequacy",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies database-metadata or section safe-unknown",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies seo-structure or section safe-unknown",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies theme-info or section safe-unknown",
        ),
        non_goals=(
            "extension-inventory possession",
            "ocmod-inventory possession",
            "comprehensive manifest",
            "weighted quality indexes",
            "R3 section population rules",
        ),
    )


def _build_l2_level() -> QualityPossessionLevel:
    return QualityPossessionLevel(
        level_id=QUALITY_LEVEL_L2,
        description=QualityPossessionDescription(
            title="Identity + structure + extensions",
            purpose=(
                "Level 1 plus extension-inventory and ocmod-inventory adequacy "
                "or honest section-level safe-unknown for extension domains."
            ),
        ),
        ownership=(
            f"{QUALITY_POSSESSION_OWNER_R5} certifies extension-inventory adequacy",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies ocmod-inventory or section safe-unknown",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies corroboration where architecture mandates",
        ),
        non_goals=(
            "comprehensive path manifest",
            "residual-only safe-unknown at L3",
            "full file contents in published package",
            "certification algorithms",
        ),
    )


def _build_l3_level() -> QualityPossessionLevel:
    return QualityPossessionLevel(
        level_id=QUALITY_LEVEL_L3,
        description=QualityPossessionDescription(
            title="Full read-only audit",
            purpose=(
                "Level 2 plus comprehensive file-manifest per acquisition scope policy, "
                "populated extension and ocmod inventories, DB baseline indicators, "
                "and safe-unknown limited to genuinely residual unknowns."
            ),
        ),
        ownership=(
            f"{QUALITY_POSSESSION_OWNER_R5} certifies comprehensive manifest adequacy",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies extension and integration indicators",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies ocmod classification where possible",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies database-metadata baseline indicators",
            f"{QUALITY_POSSESSION_OWNER_R5} certifies safe-unknown is residual-only",
        ),
        non_goals=(
            "full file contents inside published package",
            "database row data in package",
            "live connector after Publish",
            "numeric completeness thresholds",
            "Publish level freeze",
        ),
    )


CANONICAL_QUALITY_POSSESSION_REGISTRY = QualityPossessionRegistry(
    levels=(
        _build_l0_level(),
        _build_l1_level(),
        _build_l2_level(),
        _build_l3_level(),
    ),
)
