# REPORT — FP-0002 V9-06E25A SERVICE DUPLICATE ACTION VISIBILITY REPAIR

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: aa1a6997c9e823984f30063eedb3452f24c23b0a
- Local short HEAD: aa1a6997
- Remote HEAD: aa1a6997c9e823984f30063eedb3452f24c23b0a
- Remote short HEAD: aa1a6997
- Ahead: 0
- Behind: 0
- Foreign WIP: extensive outside E25A scope — preserved unstaged
- Pre-existing staged files: none
- E25 baseline ancestor check: PASS (`aa1a6997` is ancestor of HEAD; HEAD equals E25 tip)
- Result: **PASS**

## 2. Authorization and scope

- Operator authorization: V9-06E25A Service Duplicate Action Visibility Repair — GRANTED
- Task mode: WordPress admin UI corrective repair (visibility only)
- DB checkpoint: YES
- Fresh DB dump: YES
- DB writes: 0
- Source/theme changes: 0 theme / 2 plugin
- Project plugin changes: 2 files
- Third-party plugin changes: 0
- ACF JSON changes: 0
- Runtime delivery: YES
- Source service writes: 0
- Existing service content writes: 0
- Published service creation: 0
- Media file duplication: 0
- Attachment file writes: 0
- Page delete/trash/draft changes: 0
- Blog/other pages porting: NO
- Obsolete page cleanup: NO
- Global hero settings: NO
- `Настройки сайта → Герои`: NO (absent)
- Hero CTA changes: NO (copy logic preserved)
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- Rewrite/permalink changes: NO
- Plugin install/update/delete: 0
- OCPilot writes: 0
- Documentation/evidence writes: YES
- Result: **PASS**

## 3. DB checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Fresh mysqldump | PASS | `v9-06e25a-service-duplicate-action-visibility-repair-pre-20260708T181800Z/mars_wp_fp0002.sql` |
| SHA256 | PASS | `28050E4EF55A07D6BE562B6FAE46CC1DC8FE9051BC354D90B0DE9C4ACF587277` |
| Service posts snapshot | PASS | 19 services |
| Draft duplicate 746 snapshot | PASS | draft preserved |
| E24 hero CTA snapshot | PASS | `hero_cta_label` on 73/74 |
| Global hero options | PASS | 0 entries |
| Restore instructions | PASS | `validation/v9-06e25a-service-duplicate-action-visibility-repair/db-checkpoint.json` |

## 4. Baseline visibility audit

| Area | Finding | Root cause | Result |
|---|---|---|---|
| Module load | PASS | `ServiceDuplicate` in `ModuleRegistry` | PASS |
| Runtime delivery (pre-fix) | PASS | E25 files present at runtime | PASS |
| List table hook | FAIL (E25) | Only `post_row_actions` hooked | PASS (identified) |
| Hierarchical CPT | CONFIRMED | `service` uses `page_row_actions` | PASS |
| Capability gate | FAIL (E25) | Literal `create_posts` false for admins | PASS (identified) |
| Edit screen button | FAIL (E25) | No meta box | PASS (identified) |
| Copy logic | PASS | Draft 746 exists from E25 | PASS |

## 5. Corrective plan

| Component | Decision | Reason | Safety |
|---|---|---|---|
| `page_row_actions` | add hook | hierarchical list table | service guard |
| `post_row_actions` | keep hook | non-hierarchical safety | dedupe key |
| Capability | CPT-mapped create cap | unblocks UI for admins | minimal change |
| Edit meta box | side `Дублирование` | visible second entry | existing posts only |
| Copy handler | preserve E25 | operator requirement | no publish |

## 6. Correction result

| Component | Before | After | Result | Notes |
|---|---|---|---|---|
| Row action hook | `post_row_actions` only | + `page_row_actions` | PASS | post 73 eval shows `fp02_duplicate` |
| Capability | `create_posts` literal | `user_can_duplicate()` mapped | PASS | admin user 1 passes |
| Edit meta box | absent | `Дублирование` + button | PASS | visible without hover |
| Nonce URL | E25 handler | preserved | PASS | `_wpnonce` in link |
| Copy logic | E25 | unchanged | PASS | `duplicate_service()` intact |

## 7. Runtime delivery

| File | Delivered | Result | Notes |
|---|---:|---|---|
| `shpigovsky-core.php` | YES | PASS | `0.3.3-v9-06e25a-source` |
| `src/Admin/ServiceDuplicate.php` | YES | PASS | visibility + capability fix |

## 8. Post-correction admin validation

| Admin context | Result | Notes |
|---|---|---|
| Hooks registered | PASS | page_row, post_row, meta_box, admin_post |
| List row action | PASS | `fp02_duplicate` on post 73 via `page_row_actions` |
| Edit screen button | PASS | `Дублировать услугу` in meta box |
| Nonce in URL | PASS | `_wpnonce` present |
| Service-only scope | PASS | guards on post type |
| No new duplicate | PASS | 0 DB writes this wave |
| Draft 746 state | PASS | still draft |

## 9. Frontend regression validation

| Route/check | Result | Notes |
|---|---|---|
| `/` | PASS | HTTP 200 |
| `/uslugi/` | PASS | HTTP 200 |
| `/uslugi/zavisimosti/` | PASS | HTTP 200 |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | PASS | HTTP 200 |
| `/kontakty/` | PASS | HTTP 200 |
| `/otzyvy/` | PASS | HTTP 200 |
| `/privacy-policy/` | PASS | HTTP 200 |
| Draft 746 public route | PASS | not promoted |

## 10. Screenshots / evidence

| Evidence | Captured | Result | Notes |
|---|---:|---|---|
| `admin-services-list-duplicate-action-visible-e25a.png` | YES | PASS | headless Chrome |
| `admin-service-edit-duplicate-metabox-visible-e25a.png` | YES | PASS | meta box |
| `admin-duplicate-action-url-nonce-e25a.png` | YES | PASS | edit screen |
| PHP hook eval fallback | YES | PASS | row + meta HTML proof |

## 11. Final E25A visibility contract

| Item | Final state | Notes |
|---|---|---|
| List row action | visible | `Дублировать` via `page_row_actions` |
| Edit screen control | visible | meta box `Дублирование` |
| Handler | preserved | `admin_post_fp02_duplicate_service` |
| Copy semantics | preserved | E25 draft copy unchanged |

## 12. No-scope-drift

- DB writes: 0
- Source service writes: 0
- Existing service content writes: 0
- Published service creation: 0
- Media file duplication: 0
- Attachment file writes: 0
- Nav/menu writes: 0
- Privacy writes: 0
- Rewrite flush: NO
- Source/theme changes: 0
- Project plugin changes: 2
- Third-party plugin changes: 0
- ACF JSON changes: 0
- Runtime delivery: YES (bounded)
- Blog/other pages porting: NO
- Obsolete page cleanup: NO
- Batch 3 implementation: NO
- Global hero settings: NO
- `Настройки сайта → Герои`: NO
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- OCPilot writes: 0
- Production migration: NO
- V9 src/dist changes: 0
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Helpers/temp staged: NO
- Secrets/API keys: NO
- Result: **PASS**

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E25A-SERVICE-DUPLICATE-ACTION-VISIBILITY-REPAIR-REPORT-v1.md` | created | task report |
| `architecture/FP-0002-V9-06E25A-*.md` | created | wave docs |
| `validation/v9-06e25a-service-duplicate-action-visibility-repair/*.json` | created | evidence |
| `validation/.../*.png` | created | admin screenshots |
| `WORDPRESS/README.md` | updated | status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | authority |
| `PROJECT-STATUS.md` | updated | project status |

## 14. Git checkpoint

- Exact staged files: E25A plugin + docs + validation only
- Staged list inspected: YES
- Theme source files staged: NO
- Project plugin files staged: YES
- Third-party plugin files staged: NO
- ACF JSON staged: NO
- Runtime files staged: NO
- OCPilot files staged: NO
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Uploaded media files staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Commit: pending
- Commit hash: pending
- Push: pending
- Local HEAD: aa1a6997 (pre-commit)
- Remote HEAD: aa1a6997
- Result: pending

## 15. Final verdict

PASS

V9-06E25A Service Duplicate Action Visibility Repair:
COMPLETE

DB checkpoint:
PASS

Fresh DB dump:
PASS

Root cause identified:
PASS

List row action visible:
PASS

Edit screen duplicate button visible:
PASS

Nonce/capability safety:
PASS

Copy logic preserved:
PASS

No unwanted duplicate created:
PASS

Frontend regression:
PASS

Global hero settings absent:
PASS

`Настройки сайта → Герои` absent:
PASS

Reviews alias remains removed:
PASS

Top-level Reviews preserved:
PASS

No-scope-drift:
PASS

Recommended next phase:
CREATE_V9_06E25_OPERATOR_SERVICE_DUPLICATE_QA_TASK

## 16. Recommended next action

CREATE_V9_06E25_OPERATOR_SERVICE_DUPLICATE_QA_TASK

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E25A Service Duplicate Action Visibility Repair performed:
YES

DB checkpoint:
YES

Fresh DB dump:
YES

DB writes:
0

Source service writes:
0

Existing service content writes:
0

Published service creation:
0

Media file duplication:
0

Attachment file writes:
0

Nav/menu writes:
0

Privacy writes:
0

Rewrite flush performed:
NO

Source/theme changes:
0

Project plugin changes:
2

Third-party plugin changes:
0

ACF JSON changes:
0

Runtime delivery:
YES

Blog/other pages porting:
NO

Obsolete page cleanup:
NO

Batch 3 implementation:
NO

Global hero settings:
NO

Настройки сайта → Герои:
NO

Reviews alias restore:
NO

Reviews data writes:
0

Legal text writes:
0

OCPilot writes:
0

Production migration performed:
NO

V9 source changed:
NO

V9 dist changed:
NO

DB dump committed:
NO

Backup payload committed:
NO

Runtime snapshot committed:
NO

Helper/temp committed:
NO

Secrets committed:
0
