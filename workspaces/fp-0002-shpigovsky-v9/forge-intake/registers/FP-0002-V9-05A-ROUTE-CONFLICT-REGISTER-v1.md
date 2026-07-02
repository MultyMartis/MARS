# FP-0002 V9-05A — Route Conflict Register v1

**Project:** FP-0002 Shpigovsky.ru  
**Phase:** V9-05A  
**Date:** 2026-07-02  
**Authority:** V9 canonical manifest (31 routes) vs FW-06A page registry  
**Gate:** [FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md](../validation/FP-0002-V9-05A-APPROVED-FRONTEND-INTAKE-GATE-v1.md)

This register records known route/object conflicts **without changing them**. It authorizes **planning only**.

Destructive retirement later requires: exact object identity, backup, dry-run, route impact check, operator approval.

---

## Summary

| Metric | Value |
|--------|-------|
| V9 required routes | 31 |
| Foundation pages (FW-06A registry) | 22 |
| Missing required V9 objects | 14 |
| Extra foundation-only routes | 4 |
| Forbidden V9 route | 1 (`/uslugi/genotipirovanie/`) |

---

## Extra foundation objects (not in V9)

| Object / route | Current state | Required future action | Destructive |
|----------------|---------------|------------------------|-------------|
| `/uslugi/genotipirovanie/` | Page exists; slug `genotipirovanie` under `uslugi` | **RETIRE** — must not publish | **YES** |
| `/specyalisty/` (top-level) | Page `specyalisty`; Primary menu | **RETIRE** or **REVIEW** redirect to V9 equivalent | **YES** |
| `/o-centre/intervyu-i-smi/` | Page `intervyu-i-smi` under `o-centre` | **RETIRE** or **REVIEW** | **YES** |
| `/pravovaya-informaciya-pilzovatelyu/` | Legal menu page | **RETIRE** or **REVIEW** — V9 uses discrete legal slugs | **YES** |

---

## Hierarchy and naming conflicts

| Object / route | Current state | Required future action | Destructive |
|----------------|---------------|------------------------|-------------|
| `/o-centre/specialistam/` vs `/uslugi/zavisimosti/specialistam/` | Foundation has o-centre child only; V9 requires service-leaf under zavisimosti | **CREATE** zavisimosti child; **REVIEW** o-centre page role | **NO** (create) |
| Home page slug `glavnaya` | WP record; static front at `/` | **REVIEW** — preserve WP record; ensure permalink `/` | **NO** |
| `privacy-policy` | Exists; V9 legal DEMO tokens | **UPDATE** content; **REVIEW** publication (`PUBLISH` blocked until legal approval) | **NO** |
| `user-agreement` | Exists; DEMO tokens | **UPDATE**; **REVIEW** publication | **NO** |
| `consent-personal-data` | Exists; DEMO tokens | **UPDATE**; **REVIEW** publication | **NO** |
| `cookie-files-policy` | Exists; DEMO tokens | **UPDATE**; **REVIEW** publication | **NO** |

---

## Missing required V9 routes (14)

| Route | V9 template | Required future action | Destructive |
|-------|-------------|------------------------|-------------|
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/zavisimosti/profilakticheskiy-analiz/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/zavisimosti/specialistam/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/psihicheskoe-zdorovie/depressiya/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/psihicheskoe-zdorovie/ptrs/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/psihicheskoe-zdorovie/emocionalnoe-vygoranie/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/psihicheskoe-zdorovie/trevozhnye-rasstroystva/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/psihicheskoe-zdorovie/rasstroystva-sna/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/psihicheskoe-zdorovie/travma/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/rasstroystva-pischevogo-povedeniya/nervnaya-bulimiya/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/uslugi/rasstroystva-pischevogo-povedeniya/kompulsivnoe-pereedanie/` | TPL-SERVICE-LEAF | **CREATE** | **NO** |
| `/blog/nazvanie-stati/` | TPL-BLOG-SINGLE (post) | **CREATE** fixture post | **NO** |
| `/` front-page template assignment | Foundation default | **UPDATE** assign TPL-FRONT-PAGE when templates exist | **NO** |

*Note: `/blog/` posts page exists; missing item is the fixture **post** and full blog templates.*

---

## Blog fixture

| Object | Current state | Required future action | Destructive |
|--------|---------------|------------------------|-------------|
| Blog archive `/blog/` | Posts page assigned | **UPDATE** template to TPL-BLOG-ARCHIVE | **NO** |
| Fixture post `/blog/nazvanie-stati/` | **Missing** | **CREATE** with V9 fixture content | **NO** |
| `home.php` | Not present in theme | **CREATE** in implementation | **NO** |

---

## Menu reconciliation (planning)

| Menu area | Current state | Required future action | Destructive |
|-----------|---------------|------------------------|-------------|
| Primary | Includes `specyalisty`; missing service leaves | **UPDATE** per V9 menus contract | **NO** |
| Footer | Partial o-centre links | **UPDATE** | **NO** |
| Legal | Includes `pravovaya-informaciya-pilzovatelyu` | **UPDATE** to V9 legal slugs only | **NO** |

---

## Forbidden route invariant

```text
/uslugi/genotipirovanie/ — MUST NOT be published or admitted to V9 route map.
```

V9 frontend: `NOT_PUBLISHED_IN_FRONTEND`. WordPress foundation page must be **RETIRE**d in controlled reconciliation — not in this gate.

---

*Route conflict register — planning authority only.*
