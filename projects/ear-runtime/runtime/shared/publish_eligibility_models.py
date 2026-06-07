"""EAR Runtime R5.6 Publish Eligibility models — advisory gate contract only.

Narrow Publish consideration signal distinct from ValidationResult outcome authority
and ValidateReport operator audit layout.
Standard library only. No recommendation builder logic. No Publish execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# R5 canonical recommendation states — exactly three; no scores or percentages.
PUBLISH_ELIGIBILITY_ELIGIBLE = "ELIGIBLE"
PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES = "ELIGIBLE_WITH_NOTES"
PUBLISH_ELIGIBILITY_NOT_ELIGIBLE = "NOT_ELIGIBLE"

CANONICAL_PUBLISH_ELIGIBILITY_STATES: tuple[str, ...] = (
    PUBLISH_ELIGIBILITY_ELIGIBLE,
    PUBLISH_ELIGIBILITY_ELIGIBLE_WITH_NOTES,
    PUBLISH_ELIGIBILITY_NOT_ELIGIBLE,
)

# Fixed boundary text per R5.6 PE-INV-R5-01.
PUBLISH_ELIGIBILITY_BOUNDARY_DECLARATION = (
    "Publish Eligibility Recommendation is advisory only; no side effects."
)


@dataclass(frozen=True)
class PublishEligibilityRecommendation:
    """R5 advisory Publish gate input — recommendation != Publish; HITL mandatory.

    Must not execute Publish, certify quality, or mutate snapshot, evidence,
    quarantine, or Store. Does not replace ValidationResult or ValidateReport.
    """

    recommendation_id: str
    recommendation_state: str
    summary: str
    blocking_reasons: tuple[str, ...] = field(default_factory=tuple)
    notes: tuple[str, ...] = field(default_factory=tuple)
    required_operator_actions: tuple[str, ...] = field(default_factory=tuple)
    validation_result_ref: str = ""
    validate_report_ref: str = ""
    derived_from_status: str = ""
    snapshot_id: str = ""
    generated_at: str = ""
    boundary_declaration: str = PUBLISH_ELIGIBILITY_BOUNDARY_DECLARATION

    def to_dict(self) -> dict[str, Any]:
        return {
            "recommendation_id": self.recommendation_id,
            "recommendation_state": self.recommendation_state,
            "summary": self.summary,
            "blocking_reasons": list(self.blocking_reasons),
            "notes": list(self.notes),
            "required_operator_actions": list(self.required_operator_actions),
            "validation_result_ref": self.validation_result_ref,
            "validate_report_ref": self.validate_report_ref,
            "derived_from_status": self.derived_from_status,
            "snapshot_id": self.snapshot_id,
            "generated_at": self.generated_at,
            "boundary_declaration": self.boundary_declaration,
        }
