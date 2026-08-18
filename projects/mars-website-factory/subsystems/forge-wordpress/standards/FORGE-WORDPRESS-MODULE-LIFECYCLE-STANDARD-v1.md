# Forge WordPress — Module lifecycle standard v1

**ID:** FW-S-33  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Evidence:** FP-0002 `ModuleRegistry` + `ModuleInterface`; INC-04 `mars-runtime` mutating GET; leftover importers

---

## 1. Purpose

A module is a bounded unit of project functionality with one responsibility. It is not “a PHP class that also fixes unrelated Admin bugs.”

---

## 2. Required identity card (every module)

| Field | Required |
|-------|----------|
| **ID** | Stable string (`settings.site`, `forms.consultation`) |
| **Responsibility** | One sentence; no “and also” |
| **Owner** | Functionality plugin / theme / MU / third-party |
| **Dependencies** | Other module IDs, ACF, WP core APIs |
| **Storage** | options / postmeta / custom table / none |
| **Admin entry** | menu slug or “none” |
| **Frontend consumers** | templates/helpers or “none” |
| **Hooks** | `init`, `wp_ajax_*`, `rest_api_init`, cron hooks |
| **REST/AJAX endpoints** | exact routes/actions |
| **Assets** | CSS/JS handles enqueued by this module |
| **Health/state** | how Dashboard or operator sees it |
| **Uninstall / deactivation** | keep data / drop / no-op |

FP-0002 `ModuleRegistry` is **evidence of the pattern**, not a required class name. Site #2 may use a simpler array in the plugin bootstrap if the identity card exists in docs + code comments.

---

## 3. Lifecycle states

```text
REGISTERED → ENABLED → DISABLED → DEPRECATED → REMOVED
```

| State | Meaning | Runtime |
|-------|---------|---------|
| **REGISTERED** | Known in the catalog; may be off | No hooks unless ENABLED |
| **ENABLED** | `is_enabled()` true for current phase | Hooks, Admin, endpoints as declared |
| **DISABLED** | Intentionally off (phase or WAD) | **No** executable path |
| **DEPRECATED** | Will be removed; still documented | Same constraints as DISABLED unless a sunset window is explicit |
| **REMOVED** | Gone from code and catalog | No residue |

REJECTED (FP-0002 taxonomies) maps to **REGISTERED + never ENABLED** with a written reason — then **REMOVED** from the next site’s catalog if still unused.

---

## 4. Disabled / deprecated must not leave

A DISABLED or DEPRECATED module must not leave:

- executable runners (HTTP PHP, WP-CLI that mutates by default)
- orphan Admin menu
- public REST/AJAX endpoint
- cron event
- stale enqueue
- public temp files
- hidden mutation path (`admin-post`, anonymous GET)

If any of these remain, the module is **not** disabled. It is a **defect**.

Evidence: leftover public `mars-runtime` populate scripts created pages/menus on GET ([INC-04](../knowledge/FORGE-WORDPRESS-PRODUCTION-INCIDENT-LESSONS-v1.md)).

---

## 5. Boundary rule

A module must not mutate unrelated responsibilities.

| Bad | Better |
|-----|--------|
| “Permalink UX” also rewrites SEO titles | Split modules |
| “Dashboard” also registers CPTs | Split |
| “Importer” also changes `blog_public` | Split |

Shared helpers (escaping, capability) are **utils**, not a license to merge domains.

---

## 6. Module retirement checklist

Before marking REMOVED or shipping DISABLED to production:

1. [ ] Identity card updated (`REMOVE WHEN` / successor)  
2. [ ] `is_enabled()` false in all production phases  
3. [ ] No `add_action` / `add_filter` / `register_rest_route` / `wp_ajax` / cron from this module  
4. [ ] Admin menu and capability checks gone  
5. [ ] Enqueued handles gone (front and Admin)  
6. [ ] Rewrite rules flushed if the module owned them  
7. [ ] Public files deleted from **webroot** (not only Git) — [HYGIENE](FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md)  
8. [ ] Temp directories empty; no world-writable leftovers  
9. [ ] Cron unscheduled (`wp_clear_scheduled_hook`)  
10. [ ] Data retention decision recorded (keep table vs drop)  
11. [ ] Dashboard / dependency register no longer claims it is live  
12. [ ] Environment flags / temporary-tool register row closed  
13. [ ] Smoke: route 404 or auth-fail; Admin menu absent; no JS console 404 for its assets  

---

## 7. Temporary tools (importers, QA helpers, debug MU)

Every temporary production tool needs:

| Field | |
|-------|--|
| OWNER | named operator/role |
| PURPOSE | one sentence |
| CREATED | date |
| REMOVE WHEN | event (SMTP PASS, cutover PASS, wave close) |
| REMOVAL GATE | checklist item that proves absence |

Use [TEMPORARY-TOOL-REGISTER](../templates/FORGE-WORDPRESS-TEMPORARY-TOOL-REGISTER-TEMPLATE-v1.md).

**Temporary infrastructure without removal conditions is a defect.**

---

*FW-S-33 v1.*
