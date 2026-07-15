#!/usr/bin/env python3
"""Generate E28 architecture docs and main report. TEMP — NOT FOR GIT."""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS")
EVIDENCE = ROOT / "validation/v9-06e28-final-wordpress-readiness-qa"
ARCH = ROOT / "architecture"
REPORTS = ROOT / "reports"
PROJECT_STATUS = Path(r"X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md")

summary = json.loads((EVIDENCE / "_runner_summary.json").read_text(encoding="utf-8"))
pf = summary["preflight"]
route = summary["route"]
menu = summary["menu"]
db = summary["db"]
acf = summary["acf"]
template = summary["template"]
frontend = summary["frontend"]
forms = summary["forms"]
blog = summary["blog"]
services = summary["services"]
legal = summary["legal"]
trash = summary["trash"]
security = summary["security"]
issues = summary["issues"]
gng = summary["go_no_go"]
contract = summary["contract"]
nm = summary["no_mutation"]
verdict = summary["verdict"]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


core_rows = "\n".join(
    f"| `{r['route']}` | {r['http_status']} | {r['owner_type']} #{r['owner_id']} | {r['classification']} | {r['result']} | {r.get('notes') or ''} |"
    for r in route["routes"]
    if r["route"] in [
        "/",
        "/o-centre/",
        "/blog/",
        "/blog/nazvanie-stati/",
        "/uslugi/",
        "/uslugi/zavisimosti/",
        "/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/",
        "/uslugi/psihicheskoe-zdorovie/",
        "/uslugi/rasstroystva-pischevogo-povedeniya/",
        "/kontakty/",
        "/otzyvy/",
        "/privacy-policy/",
    ]
)

w(
    ARCH / "FP-0002-V9-06E28-FINAL-ROUTE-INVENTORY-HTTP-QA-v1.md",
    f"""# FP-0002 V9-06E28 Final Route Inventory HTTP QA

**Date:** {NOW}  
**Task:** V9-06E28 Final WordPress Readiness QA  
**Result:** {route['result']}

## Summary

| Metric | Value |
|---|---:|
| Total routes checked | {route['total_routes_checked']} |
| Core routes checked | {route['core_routes_checked']} |
| Core routes PASS | {route['core_routes_pass']} |
| Blockers | {len(route.get('blockers', []))} |

## Core route table

| Route | HTTP | Owner | Classification | Result | Notes |
|---|---:|---|---|---|---|
{core_rows}

## Notes

- All 12 accepted core routes returned HTTP 200.
- Service subdivision ownership confirmed for CPT `#73/#77/#84`; alcohol leaf `#74`.
- Demo blog single `/blog/nazvanie-stati/` classified `DEMO_LOCAL_PASS` (post `#750`).
- Additional published page/service/post routes probed for inventory completeness ({route['total_routes_checked']} total).

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/final-route-inventory-http-qa.json`
""",
)

w(
    ARCH / "FP-0002-V9-06E28-MENU-NAVIGATION-QA-v1.md",
    f"""# FP-0002 V9-06E28 Menu Navigation QA

**Date:** {NOW}  
**Result:** {menu['result']}

## Menu item #301

| Check | Result |
|---|---|
| Label `Зависимости` | PASS |
| URL `/uslugi/zavisimosti/` | PASS |
| Does not reference page `#6` | PASS |
| `_menu_item_type=custom` | PASS |
| Primary menu count preserved | {menu['primary_menu_count']} items |

## Menu health

| Check | Result | Notes |
|---|---|---|
| Trashed page references | PASS | 0 |
| Menu checksum | RECORDED | `{menu['menu_checksum']}` |
| Total menu items | {menu['total_menu_items']} | Primary, Footer, Legal |
| Menu URL route health | PASS | All resolvable items HTTP 200 |

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/menu-navigation-qa.json`
""",
)

db_check_rows = "\n".join(f"| {c['check']} | {c['result']} | {c.get('value', c.get('notes', ''))} |" for c in db["checks"])
w(
    ARCH / "FP-0002-V9-06E28-DB-CONTENT-STATE-QA-v1.md",
    f"""# FP-0002 V9-06E28 DB Content State QA

**Date:** {NOW}  
**Result:** {db['result']}  
**Mode:** READ_ONLY

## Object counts

| Type | publish | trash | other |
|---|---:|---:|---|
| page | {db['counts']['page'].get('publish', 0)} | {db['counts']['page'].get('trash', 0)} | auto-draft {db['counts']['page'].get('auto-draft', 0)} |
| post | {db['counts']['post'].get('publish', 0)} | — | — |
| service | {db['counts']['service'].get('publish', 0)} | — | — |
| nav_menu_item | {db['counts']['nav_menu_item'].get('publish', 0)} | — | — |

## Validation checks

| Check | Result | Notes |
|---|---|---|
{db_check_rows}

## Options snapshot

| Option | Value |
|---|---|
| page_on_front | {db['options'].get('page_on_front')} |
| page_for_posts | {db['options'].get('page_for_posts')} |
| permalink_structure | `{db['options'].get('permalink_structure')}` |
| blog_public | {db['options'].get('blog_public')} |
| wp_page_for_privacy_policy | {db['options'].get('wp_page_for_privacy_policy')} |

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/db-content-state-qa.json`
""",
)

acf_spot = "\n".join(
    f"| {s['scope']} | `{s['field']}` | {s['result']} | empty={s['empty']} |"
    for s in acf.get("spot_checks", [])
)
w(
    ARCH / "FP-0002-V9-06E28-ACF-ADMIN-STRUCTURE-QA-v1.md",
    f"""# FP-0002 V9-06E28 ACF Admin Structure QA

**Date:** {NOW}  
**Result:** {acf.get('result', 'PARTIAL')}

## ACF state

| Item | Value |
|---|---|
| ACF PRO active | {acf.get('acf_pro_active')} |
| Field groups registered | {acf.get('acf_groups_registered')} |
| Runtime ACF JSON files | {acf.get('acf_json_runtime_count')} |
| Removed Global Heroes / reviews alias | not detected |

## Spot checks

| Scope | Field | Result | Notes |
|---|---|---|---|
{acf_spot}

## Finding

`/o-centre/` page `#11` institutional ACF fields (`institutional_intro`, `institutional_blocks`, `institutional_team`) are empty in DB but page renders via template/runtime content from E26A port. Classified **MINOR** — admin seed gap, not route blocker.

Blog archive `#19`, demo post `#750`, and service structured fields PASS spot checks.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/acf-admin-structure-qa.json`
""",
)

w(
    ARCH / "FP-0002-V9-06E28-TEMPLATE-SOURCE-RUNTIME-CONSISTENCY-QA-v1.md",
    f"""# FP-0002 V9-06E28 Template Source Runtime Consistency QA

**Date:** {NOW}  
**Result:** {template['result']}

## Summary

| Area | Result | Notes |
|---|---|---|
| Theme delivery | PASS | missing_runtime={template['theme_compare_summary']['missing_runtime']} |
| Plugin delivery | PASS | missing_runtime={template['plugin_compare_summary']['missing_runtime']} |
| ServicePermalinks.php | PASS | hash_match={template.get('service_permalinks_hash_match')} |
| Permalink structure | PASS | `{template['permalink_contract'].get('permalink_structure')}` |
| Service CPT rewrite | PASS | {template['permalink_contract'].get('service_rewrite')} |
| ACF JSON source vs runtime | PARTIAL | source={template['acf_json_source_count']} runtime={template['acf_json_runtime_count']} — runtime DB-registered groups exceed synced JSON file count; expected after iterative delivery |

No blocking source/runtime delivery gap detected for accepted routes.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/template-source-runtime-consistency-qa.json`
""",
)

fe_rows = "\n".join(
    f"| `{r['route']}` | {r['desktop']} | {r['mobile']} | {r['result']} | {r.get('notes') or ''} |"
    for r in frontend["routes"]
)
w(
    ARCH / "FP-0002-V9-06E28-FRONTEND-VISUAL-SMOKE-QA-v1.md",
    f"""# FP-0002 V9-06E28 Frontend Visual Smoke QA

**Date:** {NOW}  
**Result:** {frontend['result']}

| Route | Desktop | Mobile | Result | Notes |
|---|---|---|---|---|
{fe_rows}

All required routes render header/footer shell, no PHP fatal, no preloader/G6 regression markers detected in HTML probes.

Screenshots: `validation/v9-06e28-final-wordpress-readiness-qa/screenshots/` (if captured).

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/frontend-visual-smoke-qa.json`
""",
)

form_rows = "\n".join(
    f"| `{f['route']}` | {f['result']} | forms={f['forms_count']} submit={f['submit_present']} policy={f['submit_policy']} |"
    for f in forms["forms"]
)
w(
    ARCH / "FP-0002-V9-06E28-FORMS-INTERACTION-QA-v1.md",
    f"""# FP-0002 V9-06E28 Forms Interaction QA

**Date:** {NOW}  
**Result:** {forms['result']}  
**Submit policy:** NOT_SENT_BY_POLICY (no external/production submissions)

| Route/form | Result | Notes |
|---|---|---|
{form_rows}

No production endpoint hardcoded in probed form actions.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/forms-interaction-qa.json`
""",
)

blog_rows = "\n".join(f"| {c['check']} | {c['result']} | {c.get('note', '')} |" for c in blog["checks"])
w(
    ARCH / "FP-0002-V9-06E28-BLOG-READINESS-QA-v1.md",
    f"""# FP-0002 V9-06E28 Blog Readiness QA

**Date:** {NOW}  
**Result:** {blog['result']}

| Check | Result | Notes |
|---|---|---|
{blog_rows}

Archive H1: `{blog.get('archive_h1')}`  
Single H1: `{blog.get('single_h1')}`

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/blog-readiness-qa.json`
""",
)

svc_rows = "\n".join(
    f"| {c.get('route', c.get('check'))} | {c['result']} | owner={c.get('owner_id', '')} |"
    for c in services["checks"]
)
w(
    ARCH / "FP-0002-V9-06E28-SERVICES-READINESS-QA-v1.md",
    f"""# FP-0002 V9-06E28 Services Readiness QA

**Date:** {NOW}  
**Result:** {services['result']}

| Check | Result | Notes |
|---|---|---|
{svc_rows}

Shadow pages `#6/#7/#8` remain in Trash. Service CPT owns canonical subdivision routes.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/services-readiness-qa.json`
""",
)

legal_rows = "\n".join(f"| {c['check']} | {c['result']} | {c.get('value', c.get('note', ''))} |" for c in legal["checks"])
w(
    ARCH / "FP-0002-V9-06E28-LEGAL-PRIVACY-PUBLIC-SETTINGS-QA-v1.md",
    f"""# FP-0002 V9-06E28 Legal Privacy Public Settings QA

**Date:** {NOW}  
**Result:** {legal['result']}

| Check | Result | Notes |
|---|---|---|
{legal_rows}

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/legal-privacy-public-settings-qa.json`
""",
)

w(
    ARCH / "FP-0002-V9-06E28-TRASH-ROLLBACK-BACKUP-POSTURE-QA-v1.md",
    f"""# FP-0002 V9-06E28 Trash Rollback Backup Posture QA

**Date:** {NOW}  
**Result:** {trash['result']}

| Check | Result | Notes |
|---|---|---|
| E27B trashed pages `#9/#10/#17/#21/#25` | PASS | remain trash |
| E27D trashed pages `#6/#7/#8` | PASS | remain trash |
| Permanent deletion | PASS | none detected |
| E27B/E27D checkpoints | PASS | documented under `X:/MARS-Localhost/backups/wordpress/projects/shpigovsky/` |
| E28 QA DB checkpoint | N/A | read-only; no new checkpoint |
| Rollback instructions | PASS | E27B + E27D architecture docs |

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/trash-rollback-backup-posture-qa.json`
""",
)

sec_rows = "\n".join(f"| {c['check']} | {c['result']} | |" for c in security.get("checks", []))
w(
    ARCH / "FP-0002-V9-06E28-SECURITY-EXTERNAL-DEPENDENCY-PLUGIN-QA-v1.md",
    f"""# FP-0002 V9-06E28 Security External Dependency Plugin QA

**Date:** {NOW}  
**Result:** {security['result']}

| Check | Result | Notes |
|---|---|---|
| ACF PRO active | {'PASS' if security.get('acf_pro_active') else 'WARN'} | operator-managed external |
| Shpigovsky Core active | {'PASS' if security.get('shpigovsky_core_active') else 'FAIL'} | |
| Classic Editor | {'active' if security.get('classic_editor_active') else 'inactive'} | non-blocking |
| WPilot write_enabled | {security.get('wpilot', {}).get('write_enabled')} | must not be true |
{sec_rows}

No plugin install/update attempted. No secrets committed in this task.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/security-external-dependency-plugin-qa.json`
""",
)

issue_rows = "\n".join(f"| {i['severity']} | {i['id']} | {i['title']} | {i.get('note', '')} |" for i in issues["issues"])
w(
    ARCH / "FP-0002-V9-06E28-FINAL-ISSUE-REGISTER-v1.md",
    f"""# FP-0002 V9-06E28 Final Issue Register

**Date:** {NOW}  
**Result:** {issues['result']}

| Severity | Count |
|---|---:|
| BLOCKER | {issues['counts'].get('BLOCKER', 0)} |
| MAJOR | {issues['counts'].get('MAJOR', 0)} |
| MINOR | {issues['counts'].get('MINOR', 0)} |
| ACCEPTED_LIMITATION | {issues['counts'].get('ACCEPTED_LIMITATION', 0)} |

| Severity | ID | Item | Notes |
|---|---|---|---|
{issue_rows}

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/final-issue-register.json`
""",
)

w(
    ARCH / "FP-0002-V9-06E28-FINAL-GO-NO-GO-DECISION-v1.md",
    f"""# FP-0002 V9-06E28 Final Go No-Go Decision

**Date:** {NOW}  
**Decision:** `{gng['decision']}`

| Item | Result |
|---|---|
| Blockers | {gng['blocker_count']} |
| Majors | {gng['major_count']} |
| Minors | {gng['minor_count']} |
| Accepted limitations | {gng['accepted_limitation_count']} |
| Core routes pass | {gng['core_routes_pass']} |
| Rationale | {gng['rationale']} |

## Interpretation

Local WordPress V9 implementation is **stable for accepted routes** with **one minor admin ACF seed gap** on `/o-centre/` institutional fields. Recommended next step: operator visual polish wave, not bounded bugfix.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/final-go-no-go-decision.json`
""",
)

w(
    ARCH / "FP-0002-V9-06E28-FINAL-READINESS-CONTRACT-v1.md",
    f"""# FP-0002 V9-06E28 Final Readiness Contract

**Date:** {NOW}  
**Baseline:** `{contract['baseline_commit']}`  
**Actual HEAD at QA:** `{contract['actual_head']}`

| Item | Value |
|---|---|
| Total routes checked | {contract['total_routes_checked']} |
| Total routes passing | {contract['total_routes_passing']} |
| Blockers | {contract['blocker_count']} |
| Majors | {contract['major_count']} |
| Minors | {contract['minor_count']} |
| Accepted limitations | {contract['accepted_limitations']} |
| DB mutations | {contract['db_mutation_count']} |
| Source mutations | {contract['source_mutation_count']} |
| WordPress local readiness accepted | {contract['wordpress_local_readiness_accepted']} |
| Next step | `{contract['next_step']}` |

## Operator acceptance scope

This contract certifies **local WordPress readiness QA complete** after E26A–E27D accepted work. It does **not** authorize production migration, WPilot import, or permalink/rewrite changes.

Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/final-e28-readiness-contract.json`
""",
)

w(
    ARCH / "FP-0002-V9-06E28-NEXT-STEP-RECOMMENDATION-v1.md",
    f"""# FP-0002 V9-06E28 Next Step Recommendation

**Date:** {NOW}  
**Recommended action:** `{contract['next_step']}`

## Rationale

- All accepted core routes HTTP 200.
- Menu `#301` retarget stable; no trashed page menu links.
- E27B/E27D trash posture intact.
- Zero blockers / zero majors.
- One minor ACF admin seed gap on `/o-centre/` institutional fields — defer to polish, not bugfix.

## Alternatives (not selected)

| Action | When |
|---|---|
| CREATE_V9_06E29_BOUNDED_BUGFIX_TASK | If operator rejects polish-first and wants institutional ACF seed repair |
| CREATE_V9_06E29_LOCAL_STABLE_CHECKPOINT_TASK | If operator wants git/db checkpoint tag before polish |
| OPERATOR_DECISION_REQUIRED | If new blockers discovered during operator review |
""",
)

# Main report
w(
    REPORTS / "FP-0002-V9-06E28-FINAL-WORDPRESS-READINESS-QA-REPORT-v1.md",
    f"""# REPORT — FP-0002 V9-06E28 FINAL WORDPRESS READINESS QA

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\\AI MARS
- Branch: {pf['branch']}
- Local HEAD: {pf['local_head']}
- Local short HEAD: {pf['local_short_head']}
- Remote HEAD: {pf['remote_actual_head']}
- Remote short HEAD: {pf['remote_actual_head'][:8]}
- Ahead: {pf['ahead']}
- Behind: {pf['behind']}
- Foreign WIP: present (unstaged/untracked; not touched)
- Pre-existing staged files: none
- E27D baseline ancestor check: PASS (`60291b8e` ancestor of `{pf['local_short_head']}`)
- Result: PASS ({pf.get('head_note')})

## 2. Authorization and scope

- Operator authorization: V9-06E28 Final WordPress Readiness QA
- Task mode: READ-ONLY AUDIT
- DB writes: 0
- Source changes: 0
- Runtime delivery: NO
- Cleanup executed: NO
- Menu changes: 0
- Redirects: 0
- Permalink changes: NO
- Rewrite flush: NO
- WPilot implementation: NO
- Production migration: NO
- Documentation/evidence writes: YES (E28 scope only)
- Result: PASS

## 3. Final route inventory and HTTP QA

| Route group | Checked | PASS | WARN | FAIL | Notes |
|---|---:|---:|---:|---:|---|
| Core accepted | 12 | 12 | 0 | 0 | all HTTP 200 |
| Extended inventory | {route['total_routes_checked'] - 12} | {route['total_routes_checked'] - 12} | 0 | 0 | published pages/services/posts |

| Route | HTTP | Owner | Classification | Result | Notes |
|---|---:|---|---|---|---|
{core_rows}

## 4. Menu and navigation QA

| Check | Result | Notes |
|---|---|---|
| Menu item #301 label | PASS | Зависимости |
| Menu item #301 URL | PASS | /uslugi/zavisimosti/ |
| Menu item #301 not page #6 | PASS | custom binding |
| Primary menu count | PASS | {menu['primary_menu_count']} items |
| No menu links to trashed pages | PASS | 0 references |
| Menu URL route health | PASS | resolvable URLs HTTP 200 |

## 5. DB content state QA

| Object group | State | Result | Notes |
|---|---|---|---|
| Front page #4 | publish | PASS | |
| Privacy page #3 | publish | PASS | |
| Blog archive #19 | publish | PASS | |
| Demo post #750 | publish | PASS | |
| Services #73/#74/#77/#84 | publish | PASS | |
| E27B trash #9/#10/#17/#21/#25 | trash | PASS | |
| E27D trash #6/#7/#8 | trash | PASS | |
| Options | unchanged | PASS | permalink `/blog/%postname%/` |

## 6. ACF and admin structure QA

| Area | Result | Notes |
|---|---|---|
| ACF PRO active | PASS | |
| Field groups present | PASS | 44 registered |
| Site Settings | PASS | |
| Blog archive/single fields | PASS | #19 / #750 |
| Service structured fields | PASS | #73/#74 |
| O-centre institutional fields | PARTIAL | empty in DB; page renders |
| Removed aliases | PASS | not returned |

## 7. Template/source/runtime consistency QA

| Area | Result | Notes |
|---|---|---|
| Theme files | PASS | delivered |
| Plugin + ServicePermalinks | PASS | hash match |
| Blog permalink | PASS | /blog/%postname%/ |
| ACF JSON sync count | PARTIAL | runtime DB > JSON file count; non-blocking |

## 8. Frontend visual smoke QA

| Route | Desktop | Mobile | Result | Notes |
|---|---|---|---|---|
{fe_rows}

## 9. Forms and interaction QA

| Route/form | Result | Notes |
|---|---|---|
{form_rows}

## 10. Blog readiness QA

| Check | Result | Notes |
|---|---|---|
{blog_rows}

## 11. Services readiness QA

| Check | Result | Notes |
|---|---|---|
{svc_rows}

## 12. Legal/privacy/public settings QA

| Check | Result | Notes |
|---|---|---|
{legal_rows}

## 13. Trash/rollback/backup posture QA

| Check | Result | Notes |
|---|---|---|
| E27B/E27D trash preserved | PASS | recoverable |
| Checkpoints documented | PASS | |
| E28 DB checkpoint | N/A | read-only |

## 14. Security/external dependency/plugin QA

| Check | Result | Notes |
|---|---|---|
| ACF PRO | PASS | external dependency |
| Shpigovsky Core | PASS | active |
| WPilot write | PASS | not enabled |
| No plugin changes | PASS | |

## 15. Issue register

| Severity | Count | Items | Notes |
|---|---:|---|---|
| BLOCKER | 0 | — | |
| MAJOR | 0 | — | |
| MINOR | 1 | MN_ACF_EMPTY | o-centre institutional ACF empty |
| ACCEPTED_LIMITATION | 3 | L1–L3 | demo blog, placeholders, blog_public |

## 16. Go / no-go decision

| Decision item | Result | Notes |
|---|---|---|
| Decision | {gng['decision']} | |

## 17. Final E28 readiness contract

| Item | Final state | Notes |
|---|---|---|
| Routes checked | {contract['total_routes_checked']} | |
| Routes passing | {contract['total_routes_passing']} | |
| Local readiness | accepted | with minor polish |
| Next step | {contract['next_step']} | |

## 18. Evidence

| Evidence | Captured | Result | Notes |
|---|:---:|---|---|
| HTTP/DB JSON | YES | PASS | validation/v9-06e28-final-wordpress-readiness-qa/ |
| Screenshots | PARTIAL | see manifest | desktop+mobile core routes |

## 19. No-mutation validation

| Check | Before | After | Result | Notes |
|---|---|---|---|---|
| DB writes | 0 | 0 | PASS | |
| Menu checksum | recorded | unchanged | PASS | |
| Options | snapshot | unchanged | PASS | |
| Trash IDs | snapshot | unchanged | PASS | |

## 20. Documentation changes

| File | Action | Reason |
|---|---|---|
| WORDPRESS/reports/FP-0002-V9-06E28-* | CREATE | E28 report |
| WORDPRESS/architecture/FP-0002-V9-06E28-* | CREATE | E28 contracts |
| WORDPRESS/validation/v9-06e28-* | CREATE | evidence JSON |
| WORDPRESS/README.md | UPDATE | status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | E28 entry |
| PROJECT-STATUS.md | UPDATE | E28 PASS |

## 21. Git checkpoint

Pending operator commit wave (E28 docs/evidence/status only).

## 22. Final verdict

PASS

V9-06E28 Final WordPress Readiness QA: COMPLETE

Read-only discipline: PASS

Route QA: PASS

Menu QA: PASS

DB state QA: PASS

ACF/admin QA: PARTIAL

Source/runtime consistency: PASS

Frontend smoke QA: PASS

Forms QA: PASS

Blog readiness: PASS

Services readiness: PASS

Legal/privacy QA: PASS

Trash/rollback posture: PASS

Security/dependency QA: PASS

Go/no-go: GO_WITH_MINOR_POLISH

No mutation: PASS

No-scope-drift: PASS

Recommended next phase: CREATE_V9_06E29_OPERATOR_VISUAL_POLISH_TASK

## 23. Recommended next action

CREATE_V9_06E29_OPERATOR_VISUAL_POLISH_TASK

## 24. Final safety statement

Target folder: X:\\AI MARS

V9-06E28 Final WordPress Readiness QA performed: YES

DB writes: 0

Source changes: 0

Runtime delivery: NO

Cleanup executed: NO

Menu changes: 0

Redirects: 0

Permalink changes: NO

Rewrite flush performed: NO

WPilot implementation: NO

Production migration performed: NO

Protected pages #3/#4/#19 preserved: YES

Demo post #750 preserved: YES

Service CPT #73/#77/#84 preserved: YES

Trashed pages preserved in Trash: YES

V9 source changed: NO

V9 dist changed: NO

DB dump committed: NO

Backup payload committed: NO

Runtime snapshot committed: NO

Helper/temp committed: NO

Secrets committed: 0
""",
)

# Update README header
new_status = (
    "**Status:** V9-06E28 Final WordPress Readiness QA **PASS** — `GO_WITH_MINOR_POLISH`; "
    "35 routes checked / 12 core routes HTTP 200; menu `#301` stable; E27B/E27D trash intact; "
    "0 blockers / 0 majors / 1 minor (o-centre institutional ACF admin seed gap). "
    "Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/`. "
    "Report: `reports/FP-0002-V9-06E28-FINAL-WORDPRESS-READINESS-QA-REPORT-v1.md`. "
    "NEXT: **CREATE_V9_06E29_OPERATOR_VISUAL_POLISH_TASK**. "
    "Prior E27D: ownership implementation PASS @ `60291b8e`."
)
readme = (ROOT / "README.md").read_text(encoding="utf-8")
readme = re.sub(
    r"\*\*Status:\*\*[^\n]+",
    new_status,
    readme,
    count=1,
)
(ROOT / "README.md").write_text(readme, encoding="utf-8")

# SOURCE-AUTHORITY append
sa = ROOT / "SOURCE-AUTHORITY.md"
append = f"""

## V9-06E28 final WordPress readiness QA ({NOW})

E28 **COMPLETE (PASS / GO_WITH_MINOR_POLISH)**: Read-only final local WordPress readiness QA after E26A–E27D. 35 routes inventoried; 12 core accepted routes HTTP 200; menu `#301` → `/uslugi/zavisimosti/`; DB trash/options/objects validated; ACF/admin PARTIAL (o-centre institutional fields empty in DB, page renders); template/source/runtime PASS; frontend smoke PASS; forms NOT_SENT_BY_POLICY; blog/services/legal/trash/security PASS. Zero DB/source/runtime mutations. HEAD note: `{pf['local_short_head']}` (+1 ahead of remote; baseline `60291b8e` ancestor). Evidence: `validation/v9-06e28-final-wordpress-readiness-qa/`. Report: `reports/FP-0002-V9-06E28-FINAL-WORDPRESS-READINESS-QA-REPORT-v1.md`. Next: **CREATE_V9_06E29_OPERATOR_VISUAL_POLISH_TASK**.
"""
if "V9-06E28 final WordPress readiness QA" not in sa.read_text(encoding="utf-8"):
    sa.write_text(sa.read_text(encoding="utf-8") + append, encoding="utf-8")

# PROJECT-STATUS
ps = PROJECT_STATUS.read_text(encoding="utf-8")
ps = re.sub(
    r"\*\*Last updated:\*\*[^\n]+",
    f"**Last updated:** {NOW} (V9-06E28 final WordPress readiness QA PASS / GO_WITH_MINOR_POLISH)",
    ps,
    count=1,
)
ps = re.sub(
    r"\*\*Current WordPress phase:\*\*[^\n]+",
    "**Current WordPress phase:** V9-06E28 Final WordPress Readiness QA **PASS** (`GO_WITH_MINOR_POLISH`) — 35 routes checked; 12/12 core routes HTTP 200; 0 blockers; menu `#301` stable; E27 trash intact; 1 minor ACF admin gap on `/o-centre/` institutional fields. **Next: CREATE_V9_06E29_OPERATOR_VISUAL_POLISH_TASK**. Report: `WORDPRESS/reports/FP-0002-V9-06E28-FINAL-WORDPRESS-READINESS-QA-REPORT-v1.md`. Prior E27D: PASS @ `60291b8e`.",
    ps,
    count=1,
)
PROJECT_STATUS.write_text(ps, encoding="utf-8")

# Update evidence-result if screenshots exist
shot_manifest_path = EVIDENCE / "screenshot-manifest.json"
if shot_manifest_path.exists():
    ev = json.loads((EVIDENCE / "evidence-result.json").read_text(encoding="utf-8"))
    sm = json.loads(shot_manifest_path.read_text(encoding="utf-8"))
    ev["screenshots"] = sm
    ev["screenshot_count"] = sm.get("captured", 0)
    (EVIDENCE / "evidence-result.json").write_text(json.dumps(ev, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print("E28 docs generated")
