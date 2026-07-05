# FP-0002 V9-06D9Q Reviews Requirements and Constraints v1

**Date:** 2026-07-06

Evidence: `validation/v9-06d9q-reviews-include-planning/reviews-requirements-constraints.json`

---

## Requirements

| ID | Requirement | Decision |
|----|-------------|----------|
| REQ-01 | Shared across pages | **Required** — one pool for Home + `/otzyvy/` |
| REQ-02 | Not on Home edit screen | **Required** — remove card management from Home #4 |
| REQ-03 | Editor-friendly | **Required** — under «Настройки сайта» |
| REQ-04 | Future reviews page | **Required** — shared include reusable |
| REQ-05 | Production migration safe | **Required** — Git JSON + options export |
| REQ-06 | Static demo fallback | **Required** — preserve V9 cards when empty |
| REQ-07 | No Home save blockers | **Required** — no Home-bound reviews repeater |
| REQ-08 | Disable/hide support | **Required** — master toggle + row visibility |
| REQ-09 | Replaceable later | **Required** — CPT escalation path reserved |
| REQ-10 | No unreviewed production claims | **Required** — demo labeled; D9-S/U gates |

---

## Hard constraints

- ACF Pro required; Flexible Content forbidden.
- `home_reviews_teaser` model rejected by operator.
- Max 50 review rows (matches existing FG-REVIEWS bound).
- Home slider display limit: 10 cards.
- D9-Q: zero DB/source writes.
- D9-R: no CPT registration in first wave.

---

## Operator decision captured

Reviews should **not** be managed as a required Home page ACF block. Shared include architecture is the approved direction.
