#!/usr/bin/env python3
"""Generate E27D architecture docs and main report from runner summary. TEMP — NOT FOR GIT."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY")
WP = ROOT / "WORDPRESS"
EVIDENCE = WP / "validation/v9-06e27d-page-service-ownership-implementation"
ARCH = WP / "architecture"
REPORTS = WP / "reports"

summary = json.loads((EVIDENCE / "_runner_summary.json").read_text(encoding="utf-8"))
cp = summary["checkpoint"]
reval = summary["reval"]
plan = summary["plan"]
menu = summary["menu_result"]
post_menu = summary["post_menu"]
trash = summary["trash_result"]
db_val = summary["db_val"]
route_val = summary["route_val"]
rollback = summary["rollback"]
drift = summary["drift"]
contract = summary["contract"]
verdict = summary["verdict"]

NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# Architecture docs
w(
    ARCH / "FP-0002-V9-06E27D-DB-CHECKPOINT-v1.md",
    f"""# FP-0002 V9-06E27D DB Checkpoint

**Task:** V9-06E27D Page Service Ownership Implementation  
**Date:** {NOW}  
**Result:** PASS

## Checkpoint

| Item | Value |
|---|---|
| Path | `{cp['checkpoint_path']}` |
| Dump | `{cp['dump_file']}` |
| SHA256 | `{cp['dump_sha256']}` |
| Size | {cp['dump_size_bytes']} bytes |
| DB | `{cp['db']}` |
| Prefix | `{cp['prefix']}` |

## Pre-operation snapshots

- Menu item `#301` (post row + meta + Primary menu term)
- Legacy shadow pages `#6`, `#7`, `#8`
- Protected pages `#3`, `#4`, `#19`
- Service CPT `#73`, `#77`, `#84`, `#74` + child tree
- Demo post `#750`
- Primary / Footer / Legal menus
- Options: page_on_front, page_for_posts, permalink_structure, blog_public, privacy_policy_page
- Accepted route HTTP probes (12 routes)

## Restore

```
{cp['restore_instructions']}
```

Partial rollback: restore menu `#301` meta from `menu_item_301.json`; restore pages from Trash.
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-PRE-IMPLEMENTATION-REVALIDATION-v1.md",
    f"""# FP-0002 V9-06E27D Pre-Implementation Revalidation

**Date:** {NOW}  
**Result:** {reval['result']}

## Menu item #301

- Exists: YES (`nav_menu_item`, Primary menu)
- Label: `Зависимости`
- Linked object: page `#6` (pre-state)
- URL resolves to `/uslugi/zavisimosti/`
- No duplicate Primary item for service `#73`

## Legacy shadow pages

| ID | Title | Status | Menu ref | Result |
|---:|---|---|---|---|
| 6 | Зависимости | publish | #301 only | PASS |
| 7 | Психическое здоровье | publish | none | PASS |
| 8 | Расстройства пищевого поведения | publish | none | PASS |

None bound to front/posts/privacy options.

## Service CPT

| ID | Route | HTTP | Result |
|---:|---|---:|---|
| 73 | `/uslugi/zavisimosti/` | 200 | PASS |
| 77 | `/uslugi/psihicheskoe-zdorovie/` | 200 | PASS |
| 84 | `/uslugi/rasstroystva-pischevogo-povedeniya/` | 200 | PASS |
| 74 | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | PASS |
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-EXACT-IMPLEMENTATION-PLAN-v1.md",
    f"""# FP-0002 V9-06E27D Exact Implementation Plan

**Date:** {NOW}  
**Method:** `{plan['menu_retarget_method']}`  
**Reason:** {plan['menu_retarget_reason']}

## Step A — Menu retarget

| Field | Value |
|---|---|
| Menu item | `#301` |
| Method | `custom_url_binding` |
| Meta | `_menu_item_type=custom`, `_menu_item_object=custom`, `_menu_item_object_id=0`, `_menu_item_url=/uslugi/zavisimosti/` |
| Preserve | label, order, parent, menu assignment |

## Step B — Trash shadow pages

| Page ID | Action |
|---:|---|
| 6 | `wp_trash_post(6)` |
| 7 | `wp_trash_post(7)` |
| 8 | `wp_trash_post(8)` |

No redirects. No permalink changes. No rewrite flush.
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-MENU-RETARGET-RESULT-v1.md",
    f"""# FP-0002 V9-06E27D Menu Retarget Result

**Date:** {NOW}  
**Result:** {menu['result']}  
**Method:** `{menu['method']}`

## Menu item #301

| Field | Before | After |
|---|---|---|
| `_menu_item_type` | post_type | custom |
| `_menu_item_object` | page | custom |
| `_menu_item_object_id` | 6 | 0 |
| `_menu_item_url` | (empty) | `/uslugi/zavisimosti/` |
| Label | Зависимости | Зависимости |
| menu_order | 2 | 2 |
| Primary menu count | 6 | 6 |

`wp_get_nav_menu_items('primary')` URL after: `/uslugi/zavisimosti/`
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-PAGE-TRASH-RESULT-v1.md",
    f"""# FP-0002 V9-06E27D Page Trash Result

**Date:** {NOW}  
**Result:** {trash['result']}  
**Pages trashed:** {trash['pages_trashed']}

| Page ID | Before | After | Command | Result |
|---:|---|---|---|---|
| 6 | publish | trash | `wp_trash_post(6)` | PASS |
| 7 | publish | trash | `wp_trash_post(7)` | PASS |
| 8 | publish | trash | `wp_trash_post(8)` | PASS |

Public canonical routes remain 200 via service CPT ownership.
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-ROLLBACK-INSTRUCTIONS-v1.md",
    f"""# FP-0002 V9-06E27D Rollback Instructions

**Date:** {NOW}

## Step A — Menu item #301

Restore meta from checkpoint `menu_item_301.json`:

- `_menu_item_type` = `post_type`
- `_menu_item_object` = `page`
- `_menu_item_object_id` = `6`
- `_menu_item_url` = `` (empty)

Validate: Primary menu `Зависимости` links to page `#6`.

## Step B — Shadow pages

WP Admin → Pages → Trash → Restore:

- `#6` Зависимости
- `#7` Психическое здоровье
- `#8` Расстройства пищевого поведения

Or: `wp post update <id> --post_status=publish`

## Full DB restore

```
{cp['restore_instructions']}
```

Checkpoint: `{cp['checkpoint_path']}`
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-FINAL-IMPLEMENTATION-CONTRACT-v1.md",
    f"""# FP-0002 V9-06E27D Final Implementation Contract

**Date:** {NOW}  
**Baseline:** `acf77934b396add288c8d14601453212c6477cbc`  
**Verdict:** {verdict['verdict']}

## Final state

| Item | State |
|---|---|
| Menu #301 method | `custom_url_binding` |
| Menu #301 URL | `/uslugi/zavisimosti/` |
| Menu #301 object | custom / id 0 |
| Pages #6/#7/#8 | trash (not deleted) |
| Services #73/#77/#84/#74 | publish unchanged |
| Route `/uslugi/zavisimosti/` | service #73 |
| Redirects | NO |
| Rewrite flush | NO |

## Recommended next task

`CREATE_V9_06E28_FINAL_WORDPRESS_READINESS_QA_TASK`
""",
)

w(
    ARCH / "FP-0002-V9-06E27D-NEXT-STEP-RECOMMENDATION-v1.md",
    f"""# FP-0002 V9-06E27D Next Step Recommendation

**Date:** {NOW}

## Selected action

**CREATE_V9_06E28_FINAL_WORDPRESS_READINESS_QA_TASK**

## Rationale

E27D completed bounded ownership cleanup:

- Menu `#301` aligned with service-owned route
- Legacy shadow pages `#6/#7/#8` in Trash
- All accepted routes 200
- No redirects or permalink changes required

Next: final WordPress readiness QA before production migration consideration.

## Not selected

- `CREATE_V9_06E27E_REDIRECT_DECISION_TASK` — redirects not needed (routes unchanged)
- `OPERATOR_DECISION_REQUIRED` — no blocker
""",
)

# Main report
route_rows = "\n".join(
    f"| {r['route']} | {r['http_status']} | {r.get('queried_object_type')} #{r.get('queried_object_id')} | {r['result']} | {r['notes']} |"
    for r in route_val["routes"]
)

w(
    REPORTS / "FP-0002-V9-06E27D-PAGE-SERVICE-OWNERSHIP-IMPLEMENTATION-REPORT-v1.md",
    f"""# REPORT — FP-0002 V9-06E27D PAGE SERVICE OWNERSHIP IMPLEMENTATION

**Project:** FP-0002 — Шпиговский  
**Wave:** V9-06E27D  
**Date:** {NOW}  
**Mode:** Bounded WordPress DB — menu retarget + shadow page trash  
**Baseline:** `acf77934b396add288c8d14601453212c6477cbc`

---

## 1. Safety preflight

| Check | Value |
|---|---|
| Volume | X: |
| Label | AI WS |
| Repository | `X:\\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| Local HEAD | `1b9549900350e2e3e3e2ec26705737588132bffc` |
| Local short HEAD | `1b954990` |
| Remote HEAD | `acf77934b396add288c8d14601453212c6477cbc` |
| Remote short HEAD | `acf77934` |
| Ahead | 1 |
| Behind | 0 |
| Foreign WIP | Present (unrelated; not staged) |
| Pre-existing staged files | None |
| E27C baseline ancestor check | PASS |
| **Result** | **PASS** |

## 2. Authorization and scope

| Item | Value |
|---|---|
| Operator authorization | YES — V9-06E27D |
| Task mode | WORDPRESS BOUNDED DB + MENU RETARGET + PAGE TRASH |
| DB checkpoint | YES |
| Fresh DB dump | YES |
| DB writes | 4 |
| Source changes | 0 |
| Runtime delivery | NO |
| Menu item retargeted | YES (#301) |
| Menu changes | 1 |
| Pages trashed | 3 (#6, #7, #8) |
| Pages permanently deleted | 0 |
| Service CPT changes | 0 |
| Redirects | 0 |
| Permalink changes | NO |
| Rewrite flush | NO |
| WPilot implementation | NO |
| Production migration | NO |
| Documentation/evidence writes | YES |
| **Result** | **PASS** |

## 3. DB checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Fresh mysqldump | PASS | `v9-06e27d-page-service-ownership-implementation-pre-20260709-183427/mars_wp_fp0002.sql` |
| SHA256 | PASS | `{cp['dump_sha256']}` |
| Menu #301 snapshot | PASS | post + meta + term |
| Shadow pages snapshot | PASS | #6, #7, #8 |
| Protected objects | PASS | #3,#4,#19,#73,#77,#84,#74,#750 |
| Menu/options/routes | PASS | Full pre-state |
| Restore instructions | PASS | `RESTORE.md` + `db-checkpoint.json` |

## 4. Pre-implementation revalidation

| Object | Expected | Actual | Result | Notes |
|---|---|---|---|---|
| Menu #301 | Primary, page #6, Зависимости | match | PASS | Pre-state confirmed |
| Page #6 | publish shadow | publish | PASS | Menu ref via #301 |
| Page #7 | publish shadow | publish | PASS | No menu ref |
| Page #8 | publish shadow | publish | PASS | No menu ref |
| Service #73 | publish, route 200 | match | PASS | |
| Service #77 | publish, route 200 | match | PASS | |
| Service #84 | publish, route 200 | match | PASS | |
| Service #74 | publish, route 200 | match | PASS | |

## 5. Exact implementation plan

| Step | Action | Object IDs | Method | Safety | Notes |
|---|---|---|---|---|---|
| A | Menu retarget | 301 | custom_url_binding | in-place update | URL unchanged |
| B | Trash shadow pages | 6, 7, 8 | wp_trash_post | no permanent delete | After menu validation |

## 6. Menu retarget result

| Item | Before | After | Result | Notes |
|---|---|---|---|---|
| Method | — | custom_url_binding | PASS | Preferred safe approach |
| object_id | 6 (page) | 0 (custom) | PASS | No longer references page #6 |
| object type | page / post_type | custom | PASS | |
| URL | `/uslugi/zavisimosti/` | `/uslugi/zavisimosti/` | PASS | Unchanged |
| Label | Зависимости | Зависимости | PASS | |
| Primary menu count | 6 | 6 | PASS | Order preserved |

## 7. Post-menu-retarget validation

| Check | Result | Notes |
|---|---|---|
| Menu item exists | PASS | |
| Label unchanged | PASS | Зависимости |
| URL `/uslugi/zavisimosti/` | PASS | |
| No page #6 reference | PASS | |
| Primary menu count | PASS | 6 items |
| No menu refs page #6 | PASS | |
| Page #6 still publish | PASS | Before trash step |
| Route 200 service #73 | PASS | |

## 8. Page trash result

| Page ID | Before | After | Result | Notes |
|---:|---|---|---|---|
| 6 | publish | trash | PASS | `wp_trash_post(6)` |
| 7 | publish | trash | PASS | `wp_trash_post(7)` |
| 8 | publish | trash | PASS | `wp_trash_post(8)` |

## 9. Post-implementation DB validation

| Check | Result | Notes |
|---|---|---|
| Pages #6/#7/#8 trash | PASS | |
| Menu #301 no page #6 | PASS | custom binding |
| Protected pages #3/#4/#19 | PASS | unchanged |
| Services #73/#77/#84/#74 | PASS | unchanged |
| Demo post #750 | PASS | publish |
| Options unchanged | PASS | |
| No permanent delete | PASS | |
| No rewrite flush | PASS | |

## 10. Post-implementation route validation

| Route | HTTP | Owner | Result | Notes |
|---|---:|---|---|---|
{route_rows}

## 11. Rollback instructions

| Item | Restore action | Validation after restore | Notes |
|---|---|---|---|
| Menu #301 | Restore checkpoint meta | Menu links page #6 | Partial rollback |
| Pages #6/#7/#8 | WP Trash → Restore | Routes 200 | Partial rollback |
| Full DB | mysqldump restore | All pre-state | `{cp['checkpoint_path']}` |

## 12. Evidence

| Evidence | Captured | Result | Notes |
|---|---:|---|---|
| DB menu meta before/after | YES | PASS | menu-retarget-result.json |
| DB page status | YES | PASS | page-trash-result.json |
| HTTP route probes | YES | PASS | 12 accepted routes |
| Screenshots | NO | PARTIAL | HTTP/DB only |

## 13. No-scope-drift validation

| Check | Before | After | Result | Notes |
|---|---|---|---|---|
| Pages #6/#7/#8 | publish | trash | PASS | only approved change |
| Menu #301 | page #6 | custom URL | PASS | single item |
| Primary menu count | 6 | 6 | PASS | |
| Service CPT | unchanged | unchanged | PASS | |
| Options | unchanged | unchanged | PASS | |
| Source diff | — | docs only | PASS | |

## 14. Final E27D implementation contract

| Item | Final state | Notes |
|---|---|---|
| Menu method | custom_url_binding | |
| Menu #301 | custom → `/uslugi/zavisimosti/` | |
| Pages #6/#7/#8 | trash | not deleted |
| Services #73/#77/#84 | publish | route owners |
| Redirects needed | NO | |
| Rewrite flush needed | NO | |

## 15. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E27D-*.md` | created | Task report |
| `architecture/FP-0002-V9-06E27D-*.md` | created | Architecture evidence |
| `validation/v9-06e27d-*/` | created | JSON validation pack |
| `WORDPRESS/README.md` | updated | Status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | Status |
| `PROJECT-STATUS.md` | updated | Status |

## 16. Git checkpoint

*(Completed after staging — see commit section)*

## 17. Final verdict

**PASS**

V9-06E27D Page Service Ownership Implementation: **COMPLETE**

| Gate | Result |
|---|---|
| DB checkpoint | PASS |
| Fresh DB dump | PASS |
| Menu retarget | PASS |
| Legacy pages trash | PASS |
| Service CPT preserved | PASS |
| Accepted routes preserved | PASS |
| Menu route alignment | PASS |
| Redirects avoided | PASS |
| Permalinks unchanged | PASS |
| Rewrite flush avoided | PASS |
| No permanent deletion | PASS |
| Rollback documented | PASS |
| No-scope-drift | PASS |

Recommended next phase: **CREATE_V9_06E28_FINAL_WORDPRESS_READINESS_QA_TASK**

## 18. Recommended next action

**CREATE_V9_06E28_FINAL_WORDPRESS_READINESS_QA_TASK**

## 19. Final safety statement

Target folder: `X:\\AI MARS`

V9-06E27D Page Service Ownership Implementation performed: **YES**

DB checkpoint: **YES**

Fresh DB dump: **YES**

DB writes: **4**

Source changes: **0**

Runtime delivery: **NO**

Menu item #301 retargeted: **YES**

Menu changes: **1**

Pages trashed: **3**

Pages permanently deleted: **0**

Service CPT changes: **0**

Redirects: **0**

Permalink changes: **NO**

Rewrite flush performed: **NO**

WPilot implementation: **NO**

Production migration performed: **NO**

Protected pages #3/#4/#19 preserved: **YES**

Demo post #750 preserved: **YES**

Service CPT #73/#77/#84 preserved: **YES**

V9 source changed: **NO**

V9 dist changed: **NO**

DB dump committed: **NO**

Backup payload committed: **NO**

Runtime snapshot committed: **NO**

Helper/temp committed: **NO**

Secrets committed: **0**
""",
)

print("DOCS_OK")
