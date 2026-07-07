# FP-0002 V9-06E16 — Obsolete Pages Cleanup Audit

**Evidence:** `validation/v9-06e16-operator-qa-closure-reusable-blocks-clone-cleanup-audit/obsolete-pages-cleanup-audit.json`

## Privacy verification (PASS)

| Item | Value |
|------|-------|
| `wp_page_for_privacy_policy` | **3** |
| Canonical route | `/privacy-policy/` (ID 3, publish, `legal.php`) |
| Footer/legal fallback | `/privacy-policy/` |
| Legal menu item | object_id **3** |

**ID 25** (`privacy-policy-page`) is **not** the WordPress privacy page.

## Cleanup candidates (future E20 only)

| Candidate | ID | Status | Route HTTP | Action |
|-----------|---:|--------|------------|--------|
| `/uslugi/genotipirovanie/` | 9 | publish page | 404 | trash |
| `/privacy-policy-page/` | 25 | publish page | 200 duplicate | trash |
| Правовая информация | 21 | draft | n/a | trash |

## Must not touch

- **ID 3** `/privacy-policy/` — canonical privacy and legal content.

## Notes

- Page 9 is legacy child of hub page 5; service CPT rewrite owns `/uslugi/*`; no service slug `genotipirovanie` in CPT.
- Hub helpers still contain DEMO genotipirovanie maps — separate source cleanup after page trash.

**No delete/trash in E16.**
