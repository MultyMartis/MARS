# ORCA Semantic Review Status v1

**Taxonomy ID:** `orca-semantic-review-status`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-review-status-v1.json`](orca-semantic-review-status-v1.json)

---

## Purpose

`review.workflow_status` tracks **pipeline and human workflow** — not commercial eligibility.

> **Rule:** Workflow status must never replace semantic eligibility.

---

## Distinction from eligibility

| Axis | Field | Question answered |
|------|-------|-------------------|
| Semantic eligibility | `commercial_eligibility.decision` | ACCEPT / REJECT / ABSTAIN for PPC gate |
| Workflow | `review.workflow_status` | Where is this record in human/operator pipeline? |

Examples:

- `commercial_eligibility.decision: ABSTAIN` + `workflow_status: ABSTAIN_PENDING_REVIEW` — consistent
- `commercial_eligibility.decision: ACCEPT` + `workflow_status: REJECTED_FROM_CORE` — possible after human veto
- **Invalid:** using `APPROVED_FOR_CORE` as substitute for `decision: ACCEPT` without eligibility field

---

## Workflow statuses

| Status | Description |
|--------|-------------|
| `UNPROCESSED` | Запись создана, автоматическая оценка не начата. |
| `AUTO_SCREENED` | Пройден автоматический скрининг без финального core promotion. |
| `AUTO_ACCEPT_CANDIDATE` | Автоматика предлагает ACCEPT; ожидает review если required. |
| `AUTO_REJECT_CANDIDATE` | Автоматика предлагает REJECT. |
| `ABSTAIN_PENDING_REVIEW` | ABSTAIN; ожидает человека или оператора. |
| `HUMAN_REVIEWED` | Человек просмотрел; решение может совпадать или отличаться от авто. |
| `ADJUDICATED` | Конфликт assessors разрешён назначенным adjudicator. |
| `OPERATOR_OVERRIDE` | Оператор изменил решение; prior decision в audit. |
| `APPROVED_FOR_CORE` | Разрешено включение в approved Semantic Core. |
| `REJECTED_FROM_CORE` | Исключено из core после review. |
| `SUPERSEDED` | Заменено новой версией записи; остаётся auditable. |

---

## Typical transitions

```
UNPROCESSED → AUTO_SCREENED → AUTO_ACCEPT_CANDIDATE | AUTO_REJECT_CANDIDATE | ABSTAIN_PENDING_REVIEW
AUTO_ACCEPT_CANDIDATE → HUMAN_REVIEWED → APPROVED_FOR_CORE | REJECTED_FROM_CORE
ABSTAIN_PENDING_REVIEW → HUMAN_REVIEWED | ADJUDICATED → APPROVED_FOR_CORE | REJECTED_FROM_CORE
any → OPERATOR_OVERRIDE (audit retains prior)
any → SUPERSEDED (new record_version)
```

---

## Review object fields

| Field | Description |
|-------|-------------|
| `workflow_status` | **Required.** One of statuses above |
| `automated_assessors` | IDs of rule/model/llm assessors |
| `human_reviewers` | Reviewer identities |
| `adjudicator` | Conflict resolver |
| `operator_override` | true if operator changed automated output |
| `review_notes` | Free-text notes (no sentinels) |

---

## Related documents

- [`ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md)
- [`../schemas/ORCA-SEMANTIC-DECISION-TRACE-v1.md`](../schemas/ORCA-SEMANTIC-DECISION-TRACE-v1.md)
