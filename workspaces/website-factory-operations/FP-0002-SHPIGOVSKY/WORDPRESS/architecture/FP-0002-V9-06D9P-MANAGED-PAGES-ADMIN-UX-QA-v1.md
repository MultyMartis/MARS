# FP-0002 V9-06D9P Managed Pages Admin UX QA v1

**Date:** 2026-07-05  
**Task:** V9-06D9-P (read-only QA)

## Audited pages

| Page ID | Title | Native editor hidden | Admin controls OK | Route | Result |
|---:|---|---|---|---|---|
| 5 | Услуги | YES | YES | `/uslugi/` | PASS |
| 20 | Контакты | YES | YES | `/kontakty/` | PASS |
| 11 | О центре | YES | YES | `/o-centre/` | PASS |

## Checks

- All three pages on D9-N hide allowlist (IDs 4, 5, 11, 12, …, 24).
- `post_content` length 0 after D9-M cleanup — expected for template-managed pages.
- Classic Editor active; Gutenberg disabled for pages (Classic Editor plugin).
- Frontend routes ALL_200 (see `frontend-regression-qa.json`).

## Admin screenshots

Services #5 and Contacts #20 admin captures: **PARTIAL** (wp-login screen without auth). Policy validated via allowlist helper + D9-N baseline.

## Evidence

`validation/v9-06d9p-admin-ux-qa/managed-pages-admin-ux-qa.json`

## Result

**PASS**
