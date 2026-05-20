# QA Workflow v0

## Goal

Review the ORCA output package before a human uses it in Yandex.Direct, Google Ads, or related PPC tools.

## Steps

1. Confirm all expected artifacts are present.
2. Check project brief alignment.
3. Review SERP observations and source limitations.
4. Check keyword relevance, duplicates, clusters, and negatives.
5. Review campaign structure, naming, targeting, and landing page mapping.
6. Review ad copy for unsupported claims and policy risk.
7. Check export package completeness.
8. Produce blockers, warnings, SAFE UNKNOWN items, and human approval checklist.

## Inputs

- Project input contract.
- SERP research output contract.
- Semantic cluster contract.
- Campaign structure contract.
- Export package contract.
- Human constraints and approvals.

## Outputs

- QA report.
- Blocker list.
- Warning list.
- SAFE UNKNOWN register.
- Final human approval checklist.

## Human Checkpoints

- Decide whether blockers require rework.
- Accept or reject warnings.
- Approve final platform use.
- Confirm no automatic upload or optimization is expected.

## Failure Risks

- Missing data is hidden instead of marked.
- Unsupported claims reach ad copy.
- Export package is treated as approved by default.
- Human approval is assumed but not recorded.

## REPORT Expectations

The report must include pass/fail status by artifact, blockers, warnings, unresolved SAFE UNKNOWN items, and final human action required.

QA can mark a package review-ready, but only the human can approve platform use.
