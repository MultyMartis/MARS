"""EAR Runtime R4.2 Publish State models — lifecycle semantics only.

Authoritative R4 publish-state registry distinct from R3 candidate assembly,
R5 Validate certification markers, R1.8 Store placement, and Publish Engine execution.
Standard library only. No state transition implementation. No Store adapter. No persistence.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Canonical R4 publish state identifiers — align with R1.8B publish_state conceptual field.
PUBLISH_STATE_STORED_UNPUBLISHED = "stored_unpublished"
PUBLISH_STATE_PUBLISHED = "published"
PUBLISH_STATE_SUPERSEDED = "superseded"
PUBLISH_STATE_ARCHIVED = "archived"

CANONICAL_PUBLISH_STATE_IDS: tuple[str, ...] = (
    PUBLISH_STATE_STORED_UNPUBLISHED,
    PUBLISH_STATE_PUBLISHED,
    PUBLISH_STATE_SUPERSEDED,
    PUBLISH_STATE_ARCHIVED,
)

# Consumer access semantics per publish state — visibility rules deferred to R4.3.
CONSUMER_ACCESS_NONE = "none"
CONSUMER_ACCESS_ALLOWED = "allowed"
CONSUMER_ACCESS_HISTORICAL = "historical"
CONSUMER_ACCESS_POLICY_DEPENDENT = "policy_dependent"

# Transition permission markers — semantics only; enforcement deferred to R4.7.
TRANSITION_ALLOWED = "allowed"
TRANSITION_FORBIDDEN = "forbidden"
TRANSITION_OPERATOR_POLICY = "operator_policy"

PUBLISH_STATE_OWNER_R4 = "R4"
PUBLISH_STATE_OWNER_STORE = "R1.8"
PUBLISH_STATE_OWNER_OPERATOR = "operator"


@dataclass(frozen=True)
class PublishStateReference:
    """Lightweight publish-state pointer for citations on PublishedSnapshot and audit records."""

    state_id: str

    def to_dict(self) -> dict[str, Any]:
        return {"state_id": self.state_id}


@dataclass(frozen=True)
class PublishState:
    """Single canonical publish lifecycle state — R4 visibility semantics, not certification."""

    state_id: str
    title: str
    meaning: str
    owner: str
    consumer_access: str
    visibility_implication: str
    r4_role: str
    non_goals: tuple[str, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "state_id": self.state_id,
            "title": self.title,
            "meaning": self.meaning,
            "owner": self.owner,
            "consumer_access": self.consumer_access,
            "visibility_implication": self.visibility_implication,
            "r4_role": self.r4_role,
            "non_goals": list(self.non_goals),
        }

    def to_reference(self) -> PublishStateReference:
        return PublishStateReference(state_id=self.state_id)


@dataclass(frozen=True)
class PublishStateTransition:
    """Allowed or forbidden publish-state transition — requirements contract only."""

    transition_id: str
    from_state_id: str
    to_state_id: str
    permission: str
    requirements: tuple[str, ...]
    owner: str
    summary: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "transition_id": self.transition_id,
            "from_state_id": self.from_state_id,
            "to_state_id": self.to_state_id,
            "permission": self.permission,
            "requirements": list(self.requirements),
            "owner": self.owner,
            "summary": self.summary,
        }


@dataclass(frozen=True)
class PublishStateRegistry:
    """Canonical registry of R4 publish lifecycle states and transition requirements."""

    states: tuple[PublishState, ...] = field(default_factory=tuple)
    transitions: tuple[PublishStateTransition, ...] = field(default_factory=tuple)

    def get(self, state_id: str) -> PublishState | None:
        for state in self.states:
            if state.state_id == state_id:
                return state
        return None

    def state_ids(self) -> tuple[str, ...]:
        return tuple(state.state_id for state in self.states)

    def transitions_from(self, state_id: str) -> tuple[PublishStateTransition, ...]:
        return tuple(t for t in self.transitions if t.from_state_id == state_id)

    def to_dict(self) -> dict[str, Any]:
        return {
            "states": [state.to_dict() for state in self.states],
            "transitions": [transition.to_dict() for transition in self.transitions],
        }


def _build_stored_unpublished_state() -> PublishState:
    return PublishState(
        state_id=PUBLISH_STATE_STORED_UNPUBLISHED,
        title="Stored unpublished",
        meaning=(
            "Validated snapshot immutably placed in Store (R1.8 layout) with "
            "publish_state stored_unpublished — Validate complete; Publish gate not executed."
        ),
        owner=PUBLISH_STATE_OWNER_STORE,
        consumer_access=CONSUMER_ACCESS_NONE,
        visibility_implication=(
            "Operator and EAR may read stored tree; registered consumers must not intake "
            "or receive registry pointers as active targets (CB-R4-02)."
        ),
        r4_role="Precondition — G3 satisfied; R4 reads stored artefact before Publish",
        non_goals=(
            "consumer visibility grant",
            "publish metadata assignment",
            "quality certification",
            "Validate execution",
            "section mutation",
        ),
    )


def _build_published_state() -> PublishState:
    return PublishState(
        state_id=PUBLISH_STATE_PUBLISHED,
        title="Published",
        meaning=(
            "R4 Publish gate executed after operator HITL; publish metadata set; "
            "consumer visibility grant issued for registered consumer_target."
        ),
        owner=PUBLISH_STATE_OWNER_R4,
        consumer_access=CONSUMER_ACCESS_ALLOWED,
        visibility_implication=(
            "Registered consumers may begin Consume via published snapshot_id citation "
            "and PublishedSnapshotReference (G4 satisfied)."
        ),
        r4_role="R4 target state — assigns publish metadata; freezes R5 certified quality claim",
        non_goals=(
            "quality certification or upgrade",
            "Validate re-run",
            "section content mutation",
            "evidence inclusion",
            "automatic Publish without HITL",
        ),
    )


def _build_superseded_state() -> PublishState:
    return PublishState(
        state_id=PUBLISH_STATE_SUPERSEDED,
        title="Superseded",
        meaning=(
            "Previously published snapshot replaced as active consumer default by a newer "
            "R4 Publish for the same site; snapshot_id and immutable tree retained."
        ),
        owner=PUBLISH_STATE_OWNER_R4,
        consumer_access=CONSUMER_ACCESS_HISTORICAL,
        visibility_implication=(
            "Not the active default intake target; historical citation from reports and "
            "audit records remains valid when policy permits."
        ),
        r4_role="R4 records supersession marker when newer publish succeeds for site",
        non_goals=(
            "deletion of snapshot tree",
            "invalidation of historical snapshot_id citations",
            "automatic supersession without operator context",
            "consumer active-default pointer",
        ),
    )


def _build_archived_state() -> PublishState:
    return PublishState(
        state_id=PUBLISH_STATE_ARCHIVED,
        title="Archived",
        meaning=(
            "Retention tier — snapshot removed from active operator and consumer default "
            "paths per retention policy; physical tree may remain citeable or re-tiered."
        ),
        owner=PUBLISH_STATE_OWNER_OPERATOR,
        consumer_access=CONSUMER_ACCESS_POLICY_DEPENDENT,
        visibility_implication=(
            "Not an active publish or intake target; access governed by operator retention "
            "and governance policy — not deletion."
        ),
        r4_role="R4 may emit archived publish_state pointer; operator owns retention policy",
        non_goals=(
            "deletion semantics",
            "content mutation",
            "reactivation to published without new acquisition cycle",
            "Validate or quality reassessment",
        ),
    )


def _build_canonical_transitions() -> tuple[PublishStateTransition, ...]:
    return (
        PublishStateTransition(
            transition_id="PST-R4-01",
            from_state_id=PUBLISH_STATE_STORED_UNPUBLISHED,
            to_state_id=PUBLISH_STATE_PUBLISHED,
            permission=TRANSITION_ALLOWED,
            requirements=(
                "R5 ValidationResult PASS or PASS WITH NOTES",
                "R5 PublishEligibilityRecommendation ELIGIBLE or ELIGIBLE WITH NOTES (default path)",
                "Validated snapshot at R1.8 layout or equivalent in-memory bundle",
                "Operator Publish HITL approval — distinct from Validate sign-off",
                "R4 Publish execution assigns publish metadata and visibility grant",
                "Gate G4 (Publish → Consume) satisfied",
            ),
            owner=PUBLISH_STATE_OWNER_R4,
            summary="Primary R4 Publish transition — stored-unpublished to published",
        ),
        PublishStateTransition(
            transition_id="PST-R4-02",
            from_state_id=PUBLISH_STATE_PUBLISHED,
            to_state_id=PUBLISH_STATE_SUPERSEDED,
            permission=TRANSITION_ALLOWED,
            requirements=(
                "Newer R4 Publish for same site_id succeeds",
                "Prior published snapshot no longer active consumer default",
                "Supersession record emitted — automation detail SAFE UNKNOWN",
            ),
            owner=PUBLISH_STATE_OWNER_R4,
            summary="Newer publish replaces active default; prior moves to superseded",
        ),
        PublishStateTransition(
            transition_id="PST-R4-03",
            from_state_id=PUBLISH_STATE_PUBLISHED,
            to_state_id=PUBLISH_STATE_ARCHIVED,
            permission=TRANSITION_OPERATOR_POLICY,
            requirements=(
                "Operator retention or archive policy applied",
                "R4 may record archived publish_state marker",
            ),
            owner=PUBLISH_STATE_OWNER_OPERATOR,
            summary="Published snapshot archived per retention policy",
        ),
        PublishStateTransition(
            transition_id="PST-R4-04",
            from_state_id=PUBLISH_STATE_SUPERSEDED,
            to_state_id=PUBLISH_STATE_ARCHIVED,
            permission=TRANSITION_OPERATOR_POLICY,
            requirements=(
                "Operator retention policy moves superseded snapshot to archive tier",
                "snapshot_id retained for historical cite",
            ),
            owner=PUBLISH_STATE_OWNER_OPERATOR,
            summary="Superseded snapshot re-tiered to archive",
        ),
        PublishStateTransition(
            transition_id="PST-R4-05",
            from_state_id=PUBLISH_STATE_STORED_UNPUBLISHED,
            to_state_id=PUBLISH_STATE_ARCHIVED,
            permission=TRANSITION_OPERATOR_POLICY,
            requirements=(
                "Snapshot never published; operator archive or retention policy",
                "No consumer visibility ever granted",
            ),
            owner=PUBLISH_STATE_OWNER_OPERATOR,
            summary="Stored-never-published snapshot archived per operator policy",
        ),
        PublishStateTransition(
            transition_id="PST-R4-F01",
            from_state_id="candidate",
            to_state_id=PUBLISH_STATE_PUBLISHED,
            permission=TRANSITION_FORBIDDEN,
            requirements=(
                "FORBIDDEN — bypasses R5 Validate",
            ),
            owner="—",
            summary="Candidate to published bypass forbidden",
        ),
        PublishStateTransition(
            transition_id="PST-R4-F02",
            from_state_id=PUBLISH_STATE_STORED_UNPUBLISHED,
            to_state_id=PUBLISH_STATE_PUBLISHED,
            permission=TRANSITION_FORBIDDEN,
            requirements=(
                "FORBIDDEN when R5 PublishEligibilityRecommendation NOT_ELIGIBLE on default path",
                "Requires audited operator override and typically re-Validate",
            ),
            owner=PUBLISH_STATE_OWNER_R4,
            summary="NOT_ELIGIBLE default block — fail closed per R5.6",
        ),
        PublishStateTransition(
            transition_id="PST-R4-F03",
            from_state_id=PUBLISH_STATE_PUBLISHED,
            to_state_id=PUBLISH_STATE_STORED_UNPUBLISHED,
            permission=TRANSITION_FORBIDDEN,
            requirements=(
                "FORBIDDEN — publish gate is not reversible; immutability per snapshot_id",
            ),
            owner="—",
            summary="Published to stored-unpublished reverse forbidden",
        ),
        PublishStateTransition(
            transition_id="PST-R4-F04",
            from_state_id=PUBLISH_STATE_ARCHIVED,
            to_state_id=PUBLISH_STATE_PUBLISHED,
            permission=TRANSITION_FORBIDDEN,
            requirements=(
                "FORBIDDEN — reactivation requires new acquisition → new snapshot_id",
            ),
            owner="—",
            summary="Archived to published reactivation forbidden",
        ),
    )


CANONICAL_PUBLISH_STATE_REGISTRY = PublishStateRegistry(
    states=(
        _build_stored_unpublished_state(),
        _build_published_state(),
        _build_superseded_state(),
        _build_archived_state(),
    ),
    transitions=_build_canonical_transitions(),
)
