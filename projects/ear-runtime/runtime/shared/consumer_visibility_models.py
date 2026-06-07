"""EAR Runtime R4.3 Consumer Visibility models — visibility semantics only.

Authoritative R4 consumer visibility registry distinct from R3 snapshot content,
R5 Validate certification, R1.8 Store placement, publish_state lifecycle (R4.2),
consumer registry implementation, and access control enforcement.
Standard library only. No Publish Engine. No persistence. No access control implementation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .publish_state_models import (
    PUBLISH_STATE_ARCHIVED,
    PUBLISH_STATE_PUBLISHED,
    PUBLISH_STATE_STORED_UNPUBLISHED,
    PUBLISH_STATE_SUPERSEDED,
)

# Canonical R4 consumer visibility state identifiers — orthogonal to publish_state.
VISIBILITY_STATE_NOT_VISIBLE = "not_visible"
VISIBILITY_STATE_VISIBLE = "visible"
VISIBILITY_STATE_RESTRICTED = "restricted"
VISIBILITY_STATE_HISTORICAL = "historical"

CANONICAL_VISIBILITY_STATE_IDS: tuple[str, ...] = (
    VISIBILITY_STATE_NOT_VISIBLE,
    VISIBILITY_STATE_VISIBLE,
    VISIBILITY_STATE_RESTRICTED,
    VISIBILITY_STATE_HISTORICAL,
)

# R4.1 PublishedSnapshotConsumerVisibility grant markers — mapped to canonical states.
VISIBILITY_GRANT_NONE = "none"
VISIBILITY_GRANT_GRANTED = "granted"

# Audience and target markers — semantics only; registry implementation deferred.
AUDIENCE_OPERATOR = "operator"
AUDIENCE_EAR = "ear"
AUDIENCE_REGISTERED_CONSUMER = "registered_consumer"
AUDIENCE_CONSUMER_PROGRAM = "consumer_program"

# Rule outcome markers — enforcement deferred to R4.7 / consumer programs.
RULE_OUTCOME_REQUIRED = "required"
RULE_OUTCOME_FORBIDDEN = "forbidden"
RULE_OUTCOME_POLICY_DEPENDENT = "policy_dependent"

VISIBILITY_OWNER_R4 = "R4"
VISIBILITY_OWNER_OPERATOR = "operator"
VISIBILITY_OWNER_CONSUMER = "consumer_program"


@dataclass(frozen=True)
class ConsumerVisibilityReference:
    """Lightweight visibility-state pointer for PublishedSnapshot and audit citations."""

    visibility_state_id: str
    snapshot_id: str = ""
    consumer_target: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "visibility_state_id": self.visibility_state_id,
            "snapshot_id": self.snapshot_id,
            "consumer_target": self.consumer_target,
        }


@dataclass(frozen=True)
class ConsumerVisibilityState:
    """Single canonical consumer visibility state — R4 semantics, not access control."""

    state_id: str
    title: str
    meaning: str
    owner: str
    publish_state_binding: tuple[str, ...]
    intake_permitted: bool
    active_default_permitted: bool
    currentness_implied: bool
    quality_implied: bool
    summary: str = ""
    non_goals: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "state_id": self.state_id,
            "title": self.title,
            "meaning": self.meaning,
            "owner": self.owner,
            "publish_state_binding": list(self.publish_state_binding),
            "intake_permitted": self.intake_permitted,
            "active_default_permitted": self.active_default_permitted,
            "currentness_implied": self.currentness_implied,
            "quality_implied": self.quality_implied,
            "summary": self.summary,
            "non_goals": list(self.non_goals),
        }

    def to_reference(self, snapshot_id: str = "", consumer_target: str = "") -> ConsumerVisibilityReference:
        return ConsumerVisibilityReference(
            visibility_state_id=self.state_id,
            snapshot_id=snapshot_id,
            consumer_target=consumer_target,
        )


@dataclass(frozen=True)
class ConsumerVisibilityRule:
    """Consumer boundary rule — CB-R4-* and supporting visibility invariants."""

    rule_id: str
    title: str
    statement: str
    outcome: str
    owner: str
    applies_to_visibility_states: tuple[str, ...]
    publish_dependency: str
    authority: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "title": self.title,
            "statement": self.statement,
            "outcome": self.outcome,
            "owner": self.owner,
            "applies_to_visibility_states": list(self.applies_to_visibility_states),
            "publish_dependency": self.publish_dependency,
            "authority": self.authority,
        }


@dataclass(frozen=True)
class ConsumerVisibilityTarget:
    """Registered consumer audience — logical visibility grant recipient, not credential holder."""

    target_id: str
    title: str
    audience: str
    intake_owner: str
    visibility_grant_source: str
    allowed_when_visible: tuple[str, ...]
    forbidden_always: tuple[str, ...]
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "target_id": self.target_id,
            "title": self.title,
            "audience": self.audience,
            "intake_owner": self.intake_owner,
            "visibility_grant_source": self.visibility_grant_source,
            "allowed_when_visible": list(self.allowed_when_visible),
            "forbidden_always": list(self.forbidden_always),
            "notes": self.notes,
        }


@dataclass(frozen=True)
class ConsumerVisibilityRegistry:
    """Canonical registry of R4 consumer visibility states, rules, and targets."""

    visibility_states: tuple[ConsumerVisibilityState, ...] = field(default_factory=tuple)
    visibility_rules: tuple[ConsumerVisibilityRule, ...] = field(default_factory=tuple)
    visibility_targets: tuple[ConsumerVisibilityTarget, ...] = field(default_factory=tuple)

    def get_state(self, state_id: str) -> ConsumerVisibilityState | None:
        for state in self.visibility_states:
            if state.state_id == state_id:
                return state
        return None

    def get_rule(self, rule_id: str) -> ConsumerVisibilityRule | None:
        for rule in self.visibility_rules:
            if rule.rule_id == rule_id:
                return rule
        return None

    def get_target(self, target_id: str) -> ConsumerVisibilityTarget | None:
        for target in self.visibility_targets:
            if target.target_id == target_id:
                return target
        return None

    def rules_for_state(self, state_id: str) -> tuple[ConsumerVisibilityRule, ...]:
        return tuple(
            rule
            for rule in self.visibility_rules
            if state_id in rule.applies_to_visibility_states or not rule.applies_to_visibility_states
        )

    def visibility_state_for_publish_state(self, publish_state_id: str) -> str:
        """Map R4.2 publish_state to canonical visibility state — semantics only."""
        mapping = {
            PUBLISH_STATE_STORED_UNPUBLISHED: VISIBILITY_STATE_NOT_VISIBLE,
            PUBLISH_STATE_PUBLISHED: VISIBILITY_STATE_VISIBLE,
            PUBLISH_STATE_SUPERSEDED: VISIBILITY_STATE_HISTORICAL,
            PUBLISH_STATE_ARCHIVED: VISIBILITY_STATE_RESTRICTED,
        }
        return mapping.get(publish_state_id, VISIBILITY_STATE_NOT_VISIBLE)

    def grant_to_visibility_state(self, grant_state: str) -> str:
        """Map R4.1 PublishedSnapshotConsumerVisibility.visibility_state grant marker."""
        if grant_state == VISIBILITY_GRANT_GRANTED:
            return VISIBILITY_STATE_VISIBLE
        return VISIBILITY_STATE_NOT_VISIBLE

    def to_dict(self) -> dict[str, Any]:
        return {
            "visibility_states": [state.to_dict() for state in self.visibility_states],
            "visibility_rules": [rule.to_dict() for rule in self.visibility_rules],
            "visibility_targets": [target.to_dict() for target in self.visibility_targets],
        }


def _build_not_visible_state() -> ConsumerVisibilityState:
    return ConsumerVisibilityState(
        state_id=VISIBILITY_STATE_NOT_VISIBLE,
        title="Not visible",
        meaning=(
            "Snapshot has no consumer visibility grant — pre-Publish lifecycle stages "
            "(candidate, validated, stored_unpublished) or never-published archived trees."
        ),
        owner=VISIBILITY_OWNER_R4,
        publish_state_binding=(PUBLISH_STATE_STORED_UNPUBLISHED,),
        intake_permitted=False,
        active_default_permitted=False,
        currentness_implied=False,
        quality_implied=False,
        summary="Default pre-Publish visibility — Store audience only",
        non_goals=(
            "consumer registry active pointer",
            "credential handoff",
            "quality certification",
            "Validate execution",
            "section content access for registered consumers",
        ),
    )


def _build_visible_state() -> ConsumerVisibilityState:
    return ConsumerVisibilityState(
        state_id=VISIBILITY_STATE_VISIBLE,
        title="Visible",
        meaning=(
            "R4 Publish gate executed; visibility grant issued for registered consumer_target; "
            "registered consumers may begin Consume via published snapshot_id citation."
        ),
        owner=VISIBILITY_OWNER_R4,
        publish_state_binding=(PUBLISH_STATE_PUBLISHED,),
        intake_permitted=True,
        active_default_permitted=True,
        currentness_implied=False,
        quality_implied=False,
        summary="Active consumer visibility after Publish — G4 satisfied",
        non_goals=(
            "automatic quality upgrade",
            "Validate re-certification",
            "consumer intake execution",
            "credential issuance",
            "evidence quarantine exposure",
        ),
    )


def _build_restricted_state() -> ConsumerVisibilityState:
    return ConsumerVisibilityState(
        state_id=VISIBILITY_STATE_RESTRICTED,
        title="Restricted",
        meaning=(
            "Visibility limited by operator retention policy, consumer_target mismatch, "
            "archive tier, or governance — not active default intake; access policy-dependent."
        ),
        owner=VISIBILITY_OWNER_OPERATOR,
        publish_state_binding=(PUBLISH_STATE_ARCHIVED,),
        intake_permitted=False,
        active_default_permitted=False,
        currentness_implied=False,
        quality_implied=False,
        summary="Policy-governed limited visibility — not active default",
        non_goals=(
            "active consumer default pointer",
            "deletion semantics",
            "quality reassessment",
            "access control implementation",
        ),
    )


def _build_historical_state() -> ConsumerVisibilityState:
    return ConsumerVisibilityState(
        state_id=VISIBILITY_STATE_HISTORICAL,
        title="Historical",
        meaning=(
            "Previously published snapshot superseded by newer R4 Publish for same site; "
            "historical citation permitted; not active default intake target."
        ),
        owner=VISIBILITY_OWNER_R4,
        publish_state_binding=(PUBLISH_STATE_SUPERSEDED,),
        intake_permitted=False,
        active_default_permitted=False,
        currentness_implied=False,
        quality_implied=False,
        summary="Superseded published snapshot — cite-only when policy permits",
        non_goals=(
            "active registry default",
            "invalidation of snapshot_id",
            "tree deletion",
            "automatic supersession without R4 Publish record",
        ),
    )


def _build_canonical_rules() -> tuple[ConsumerVisibilityRule, ...]:
    return (
        ConsumerVisibilityRule(
            rule_id="CB-R4-01",
            title="Published snapshot_id citation required",
            statement="Consumer intake must reference published snapshot_id — not acquisition_id alone.",
            outcome=RULE_OUTCOME_REQUIRED,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(VISIBILITY_STATE_VISIBLE,),
            publish_dependency="Requires publish_state published and visibility grant",
            authority="R4-CHARTER § Consumer Boundary",
        ),
        ConsumerVisibilityRule(
            rule_id="CB-R4-02",
            title="Unpublished stored snapshot not active consumer target",
            statement=(
                "Unpublished stored snapshot must not appear in consumer registry as active intake target."
            ),
            outcome=RULE_OUTCOME_FORBIDDEN,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(VISIBILITY_STATE_NOT_VISIBLE,),
            publish_dependency="Publish not executed — stored_unpublished",
            authority="R4-CHARTER § Consumer Boundary; R1.8B § Store vs Publish",
        ),
        ConsumerVisibilityRule(
            rule_id="CB-R4-03",
            title="Secrets paths forbidden at Publish",
            statement="Publish must not expose operator secrets/ paths or live credentials to consumers.",
            outcome=RULE_OUTCOME_FORBIDDEN,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(
                VISIBILITY_STATE_VISIBLE,
                VISIBILITY_STATE_RESTRICTED,
                VISIBILITY_STATE_HISTORICAL,
            ),
            publish_dependency="Applies at Publish grant emission — R4 confirms gate",
            authority="R4-CHARTER § Consumer Boundary",
        ),
        ConsumerVisibilityRule(
            rule_id="CB-R4-04",
            title="Consumer-side validation distinct from EAR Validate",
            statement=(
                "Consumer-side contract validation on intake is distinct from R5 EAR Validate — "
                "visibility grant does not substitute certification."
            ),
            outcome=RULE_OUTCOME_REQUIRED,
            owner=VISIBILITY_OWNER_CONSUMER,
            applies_to_visibility_states=(VISIBILITY_STATE_VISIBLE,),
            publish_dependency="After Publish — consumer programs own intake validation",
            authority="R4-CHARTER § Consumer Boundary",
        ),
        ConsumerVisibilityRule(
            rule_id="CB-R4-05",
            title="Re-acquisition requires new Request cycle",
            statement="Re-acquisition requires new Request cycle — consumer does not pull live SITE.",
            outcome=RULE_OUTCOME_FORBIDDEN,
            owner=VISIBILITY_OWNER_CONSUMER,
            applies_to_visibility_states=(
                VISIBILITY_STATE_VISIBLE,
                VISIBILITY_STATE_HISTORICAL,
                VISIBILITY_STATE_RESTRICTED,
            ),
            publish_dependency="Independent of publish_state — consumer program boundary",
            authority="R4-CHARTER § Consumer Boundary",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-01",
            title="Visibility begins only after Publish",
            statement=(
                "No consumer path write, registry pointer, or intake automation before R4 Publish "
                "completes with operator approval."
            ),
            outcome=RULE_OUTCOME_FORBIDDEN,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(VISIBILITY_STATE_NOT_VISIBLE,),
            publish_dependency="stored_unpublished and all pre-Publish stages",
            authority="R4-IMPLEMENTATION-CHARTER § Mandatory questions",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-02",
            title="Visibility does not imply currentness",
            statement=(
                "Visible or historical visibility does not assert snapshot is the active default "
                "for site — supersession may apply."
            ),
            outcome=RULE_OUTCOME_REQUIRED,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(
                VISIBILITY_STATE_VISIBLE,
                VISIBILITY_STATE_HISTORICAL,
            ),
            publish_dependency="published vs superseded distinction",
            authority="R4.2 publish_state model",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-03",
            title="Visibility does not imply quality",
            statement=(
                "Visibility grant permits consumer intake reference only — does not certify, "
                "upgrade, or reassess package_quality_level."
            ),
            outcome=RULE_OUTCOME_REQUIRED,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(VISIBILITY_STATE_VISIBLE,),
            publish_dependency="Quality frozen at Publish from R5 certified level",
            authority="R5.3; R4-CHARTER § Why R4 does not own quality",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-04",
            title="Evidence quarantine never consumer-visible",
            statement="Evidence Package quarantine bulk is never a consumer visibility target.",
            outcome=RULE_OUTCOME_FORBIDDEN,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(),
            publish_dependency="Independent of Publish — R2 internal only",
            authority="R2 ownership; R4-CHARTER § Consumer Boundary",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-05",
            title="Registered consumer_target required for visible grant",
            statement=(
                "Visibility grant applies to declared consumer_target only — other consumers "
                "remain not_visible unless separately granted."
            ),
            outcome=RULE_OUTCOME_REQUIRED,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(VISIBILITY_STATE_VISIBLE,),
            publish_dependency="consumer_target set at Publish",
            authority="R4.1 PublishedSnapshotMetadata",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-06",
            title="Superseded not active default",
            statement=(
                "Superseded published snapshot must not appear as active consumer registry "
                "default for site — historical cite only."
            ),
            outcome=RULE_OUTCOME_FORBIDDEN,
            owner=VISIBILITY_OWNER_R4,
            applies_to_visibility_states=(VISIBILITY_STATE_HISTORICAL,),
            publish_dependency="publish_state superseded after newer Publish",
            authority="R4.2 PST-R4-02; CB-R4-02 extension",
        ),
        ConsumerVisibilityRule(
            rule_id="CV-R4-07",
            title="Archived access policy-dependent",
            statement=(
                "Archived snapshot visibility is restricted — operator retention policy governs "
                "whether historical cite is permitted."
            ),
            outcome=RULE_OUTCOME_POLICY_DEPENDENT,
            owner=VISIBILITY_OWNER_OPERATOR,
            applies_to_visibility_states=(VISIBILITY_STATE_RESTRICTED,),
            publish_dependency="publish_state archived",
            authority="R1.8B § Archive implications; R4.2 archived state",
        ),
    )


def _build_canonical_targets() -> tuple[ConsumerVisibilityTarget, ...]:
    return (
        ConsumerVisibilityTarget(
            target_id="operator",
            title="Operator / EAR",
            audience=AUDIENCE_OPERATOR,
            intake_owner=VISIBILITY_OWNER_OPERATOR,
            visibility_grant_source="Store placement — not R4 consumer grant",
            allowed_when_visible=(
                "stored_unpublished tree read",
                "validated snapshot inspection",
                "publish decision context",
                "quarantine inspection",
            ),
            forbidden_always=(
                "consumer registry impersonation",
            ),
            notes="Store audience — visibility independent of R4 Publish for operator read paths",
        ),
        ConsumerVisibilityTarget(
            target_id="ocpilot",
            title="OCPilot consumer program",
            audience=AUDIENCE_CONSUMER_PROGRAM,
            intake_owner=VISIBILITY_OWNER_CONSUMER,
            visibility_grant_source="R4 Publish visibility grant — consumer_target declaration",
            allowed_when_visible=(
                "published snapshot_id citation",
                "OpenCart section tree intake",
                "published package_quality_level read",
                "safe-unknown honesty block",
                "bulk_root opaque reference",
                "acquisition-log audit",
            ),
            forbidden_always=(
                "evidence quarantine",
                "live SITE credentials",
                "candidate snapshot without Publish",
                "stored_unpublished as active intake",
                "Validate report as certification substitute",
                "acquisition initiation",
            ),
            notes="Default consumer_target per R1.8B — Run 5 execution not R4 deliverable",
        ),
        ConsumerVisibilityTarget(
            target_id="registered_consumer",
            title="Future registered consumer",
            audience=AUDIENCE_REGISTERED_CONSUMER,
            intake_owner=VISIBILITY_OWNER_CONSUMER,
            visibility_grant_source="R4 Publish visibility grant — explicit consumer_target match",
            allowed_when_visible=(
                "published snapshot reference",
                "frozen quality claim read",
            ),
            forbidden_always=(
                "pre-Publish snapshot intake",
                "quarantine bulk",
                "secrets paths",
            ),
            notes="Registry implementation SAFE UNKNOWN — R4.7 / consumer programs",
        ),
    )


CANONICAL_CONSUMER_VISIBILITY_REGISTRY = ConsumerVisibilityRegistry(
    visibility_states=(
        _build_not_visible_state(),
        _build_visible_state(),
        _build_restricted_state(),
        _build_historical_state(),
    ),
    visibility_rules=_build_canonical_rules(),
    visibility_targets=_build_canonical_targets(),
)
