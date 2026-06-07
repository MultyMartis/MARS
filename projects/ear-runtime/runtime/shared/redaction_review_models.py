"""EAR Runtime R5.4 Redaction Review models — publication safety representation only.

Authoritative R5 redaction review contract distinct from R2 evidence quarantine policy,
R3 assembly copy-avoidance, R4 Publish, secret storage, and automated scanners.
Standard library only. No scanning logic. No detection logic. No sensitive values in findings.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Canonical redaction category identifiers — not enums; align with R5 Redaction validation category.
REDACTION_CATEGORY_CREDENTIALS = "credentials"
REDACTION_CATEGORY_SECRETS = "secrets"
REDACTION_CATEGORY_PII = "pii"
REDACTION_CATEGORY_INTERNAL_PATHS = "internal_paths"
REDACTION_CATEGORY_UNSAFE_PUBLICATION = "unsafe_publication"
REDACTION_CATEGORY_QUARANTINE_LEAKAGE = "quarantine_leakage"
REDACTION_CATEGORY_OTHER = "other"

CANONICAL_REDACTION_CATEGORY_IDS: tuple[str, ...] = (
    REDACTION_CATEGORY_CREDENTIALS,
    REDACTION_CATEGORY_SECRETS,
    REDACTION_CATEGORY_PII,
    REDACTION_CATEGORY_INTERNAL_PATHS,
    REDACTION_CATEGORY_UNSAFE_PUBLICATION,
    REDACTION_CATEGORY_QUARANTINE_LEAKAGE,
    REDACTION_CATEGORY_OTHER,
)

# R5 redaction review statuses — not Publish statuses; not security incident statuses.
REDACTION_STATUS_CLEAR = "CLEAR"
REDACTION_STATUS_REVIEW_REQUIRED = "REVIEW_REQUIRED"
REDACTION_STATUS_BLOCKED = "BLOCKED"

CANONICAL_REDACTION_STATUSES: tuple[str, ...] = (
    REDACTION_STATUS_CLEAR,
    REDACTION_STATUS_REVIEW_REQUIRED,
    REDACTION_STATUS_BLOCKED,
)

# R5 redaction recommendations — feed R5 report only; not Publish decision; not security action.
REDACTION_RECOMMENDATION_NO_ACTION_REQUIRED = "NO_ACTION_REQUIRED"
REDACTION_RECOMMENDATION_REDACT_BEFORE_PUBLISH = "REDACT_BEFORE_PUBLISH"
REDACTION_RECOMMENDATION_OPERATOR_REVIEW_REQUIRED = "OPERATOR_REVIEW_REQUIRED"
REDACTION_RECOMMENDATION_NOT_PUBLISHABLE = "NOT_PUBLISHABLE"

CANONICAL_REDACTION_RECOMMENDATIONS: tuple[str, ...] = (
    REDACTION_RECOMMENDATION_NO_ACTION_REQUIRED,
    REDACTION_RECOMMENDATION_REDACT_BEFORE_PUBLISH,
    REDACTION_RECOMMENDATION_OPERATOR_REVIEW_REQUIRED,
    REDACTION_RECOMMENDATION_NOT_PUBLISHABLE,
)

REDACTION_OWNER_R5 = "R5"


@dataclass(frozen=True)
class RedactionStatus:
    """R5 redaction review status — distinct from ValidationStatus and Publish gate."""

    value: str

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


@dataclass(frozen=True)
class RedactionRecommendation:
    """R5 redaction recommendation — recommendation != Publish; != security incident action."""

    value: str

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


@dataclass(frozen=True)
class RedactionCategoryReference:
    """Lightweight redaction category pointer for findings and registry lookup."""

    category_id: str

    def to_dict(self) -> dict[str, Any]:
        return {"category_id": self.category_id}


@dataclass(frozen=True)
class RedactionCategory:
    """Single redaction risk category — ownership contract, not a scanner."""

    category_id: str
    title: str
    purpose: str
    ownership: tuple[str, ...] = field(default_factory=tuple)
    non_goals: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "category_id": self.category_id,
            "title": self.title,
            "purpose": self.purpose,
            "ownership": list(self.ownership),
            "non_goals": list(self.non_goals),
        }

    def to_reference(self) -> RedactionCategoryReference:
        return RedactionCategoryReference(category_id=self.category_id)


@dataclass(frozen=True)
class RedactionCategoryRegistry:
    """Canonical registry of all R5 redaction review categories."""

    categories: tuple[RedactionCategory, ...] = field(default_factory=tuple)

    def get(self, category_id: str) -> RedactionCategory | None:
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


@dataclass(frozen=True)
class RedactionFinding:
    """Single R5 redaction finding — operator-facing; never stores sensitive values.

    Must not contain raw credentials, passwords, tokens, API keys, PII values,
    or filesystem dumps. Represents risk only.
    """

    finding_id: str
    category: RedactionCategoryReference
    status: RedactionStatus
    title: str
    description: str
    recommendation: RedactionRecommendation

    def to_dict(self) -> dict[str, Any]:
        return {
            "finding_id": self.finding_id,
            "category": self.category.to_dict(),
            "status": self.status.to_dict(),
            "title": self.title,
            "description": self.description,
            "recommendation": self.recommendation.to_dict(),
        }


@dataclass(frozen=True)
class RedactionAudit:
    """R5 redaction review audit metadata — no implementation logic."""

    reviewer_version: str
    reviewed_at: str
    reviewed_snapshot_id: str
    operator_ref: str
    contract_ref: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "reviewer_version": self.reviewer_version,
            "reviewed_at": self.reviewed_at,
            "reviewed_snapshot_id": self.reviewed_snapshot_id,
            "operator_ref": self.operator_ref,
            "contract_ref": self.contract_ref,
        }


@dataclass(frozen=True)
class RedactionReviewSummary:
    """R5 redaction review aggregate outcome — no detection logic."""

    status: RedactionStatus
    finding_count: int
    blocked_count: int
    review_required_count: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.to_dict(),
            "finding_count": self.finding_count,
            "blocked_count": self.blocked_count,
            "review_required_count": self.review_required_count,
        }


@dataclass(frozen=True)
class RedactionReview:
    """Aggregate R5 redaction review output — publication safety review contract only.

    Must not represent evidence quarantine management, snapshot assembly,
    Publish execution, secret storage, or security incident response.
    """

    review_id: str
    summary: RedactionReviewSummary
    findings: tuple[RedactionFinding, ...] = field(default_factory=tuple)
    audit: RedactionAudit | None = None
    recommendation: RedactionRecommendation | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "review_id": self.review_id,
            "summary": self.summary.to_dict(),
            "findings": [finding.to_dict() for finding in self.findings],
            "audit": self.audit.to_dict() if self.audit is not None else None,
            "recommendation": (
                self.recommendation.to_dict()
                if self.recommendation is not None
                else None
            ),
        }


def _build_credentials_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_CREDENTIALS,
        title="Credentials",
        purpose=(
            "Review candidate snapshot serializations for credential-like exposure "
            "bound for consumer paths — usernames paired with secrets, live auth material."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} reviews credential exposure risk on candidate snapshot",
            f"{REDACTION_OWNER_R5} records credential findings without storing credential values",
            f"{REDACTION_OWNER_R5} fail-closed when mandatory credential exposure is confirmed",
        ),
        non_goals=(
            "credential storage or rotation",
            "secret vault management",
            "automated credential scanners",
            "evidence quarantine policy",
            "publish execution",
        ),
    )


def _build_secrets_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_SECRETS,
        title="Secrets",
        purpose=(
            "Review candidate snapshot for secret carriers — API keys, tokens, passwords, "
            "private keys — in section payloads and metadata fields."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} reviews secret exposure risk on candidate serialization",
            f"{REDACTION_OWNER_R5} classifies secret findings by category without storing values",
            f"{REDACTION_OWNER_R5} blocks Validate when mandatory secret exposure confirmed",
        ),
        non_goals=(
            "regex or heuristic secret detection libraries",
            "automated redaction engine product",
            "R2 evidence serialization policy enforcement",
            "security incident workflows",
        ),
    )


def _build_pii_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_PII,
        title="Personally identifiable information",
        purpose=(
            "Review candidate snapshot for PII that must not proceed to consumer-visible "
            "publication paths without operator review."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} reviews PII publication risk on candidate snapshot",
            f"{REDACTION_OWNER_R5} records PII findings without storing PII values",
            f"{REDACTION_OWNER_R5} recommends operator review or redaction before Publish",
        ),
        non_goals=(
            "PII detection algorithms",
            "GDPR or compliance workflow product",
            "evidence quarantine PII scrubbing",
            "consumer delivery policy",
        ),
    )


def _build_internal_paths_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_INTERNAL_PATHS,
        title="Internal paths",
        purpose=(
            "Review candidate snapshot for internal filesystem paths, quarantine roots, "
            "or operator-only storage references that must not appear in consumer paths."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} reviews internal path leakage in candidate sections",
            f"{REDACTION_OWNER_R5} flags path exposure without embedding path dumps in findings",
        ),
        non_goals=(
            "filesystem scanning implementation",
            "Store layout redesign",
            "R3 bulk_root vs quarantine assembly checks",
            "path normalization engines",
        ),
    )


def _build_unsafe_publication_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_UNSAFE_PUBLICATION,
        title="Unsafe publication",
        purpose=(
            "Review whether candidate carries pre-redaction bulk, raw exports, or content "
            "that must not proceed to R4 Publish recommendation or consumer paths."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} reviews unsafe publication risk on candidate snapshot",
            f"{REDACTION_OWNER_R5} determines publication safety for Validate report",
            f"{REDACTION_OWNER_R5} fail-closed on mandatory unsafe-publication blockers",
        ),
        non_goals=(
            "Publish execution",
            "consumer intake delivery",
            "R3 assembly copy-avoidance rules",
            "evidence quarantine writes",
        ),
    )


def _build_quarantine_leakage_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_QUARANTINE_LEAKAGE,
        title="Quarantine leakage",
        purpose=(
            "Review candidate snapshot for evidence quarantine content, bulk refs, or "
            "pre-redaction material inappropriately copied into snapshot sections."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} reviews quarantine leakage into candidate snapshot",
            f"{REDACTION_OWNER_R5} correlates bulk refs and section payloads for leakage risk",
        ),
        non_goals=(
            "evidence quarantine management",
            "quarantine layout policy",
            "R2 evidence Package mutation",
            "quarantine persistence implementation",
        ),
    )


def _build_other_category() -> RedactionCategory:
    return RedactionCategory(
        category_id=REDACTION_CATEGORY_OTHER,
        title="Other publication risk",
        purpose=(
            "Operator-facing bucket for redaction risks that do not fit canonical categories "
            "— requires explicit category reference and human review."
        ),
        ownership=(
            f"{REDACTION_OWNER_R5} records uncategorized publication risks with operator review",
        ),
        non_goals=(
            "catch-all without operator review",
            "automatic downgrade to CLEAR",
            "security incident classification",
        ),
    )


CANONICAL_REDACTION_CATEGORY_REGISTRY = RedactionCategoryRegistry(
    categories=(
        _build_credentials_category(),
        _build_secrets_category(),
        _build_pii_category(),
        _build_internal_paths_category(),
        _build_unsafe_publication_category(),
        _build_quarantine_leakage_category(),
        _build_other_category(),
    ),
)
