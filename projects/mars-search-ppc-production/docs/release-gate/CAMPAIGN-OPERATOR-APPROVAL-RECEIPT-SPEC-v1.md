# Campaign Operator Approval Receipt Spec v1

**Status:** IMPLEMENTED  
**Module:** `tools/commander-transport/src/operator-approval-receipt.mjs`  
**Schema:** `tools/commander-transport/contracts/campaign-operator-approval-receipt-schema-v1.json`

## Required fields

- `project_id`, `campaign_program`, `release_version`
- `authority_artifact_paths`, `authority_hashes`
- `phrase_count`, `keep_count`, `reject_count`, `move_count`, `hold_count`
- `campaign_count`, `group_count`, `ad_count`
- `geo_policy`, `negative_policy`
- `approval_timestamp`, `operator_identity_label` (when approved)
- `status`: `READY_FOR_OPERATOR_APPROVAL` | `OPERATOR_SEMANTIC_APPROVED`

## Rules

- `generateApprovalReceiptForReview()` sets `generated_for_review_only: true` — **never self-approves**
- Release gate requires `OPERATOR_SEMANTIC_APPROVED` with timestamp and identity
- `hold_count > 0` blocks approval
- Cursor task reports do **not** constitute operator approval
