# I-SEO Report Hub — Implementation Brief v0.1

**Status:** PLANNING DRAFT — **not a build task**  
**Audience:** Anton (developer), implementation planning, operator HITL charter  
**Implementation:** **NOT STARTED**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10

---

## 1. Status

This brief summarizes **what must eventually be built** on WordPress/i-seo.su. It is a handoff document from product architecture planning to a future implementation charter.

| Fact | State |
|------|-------|
| WordPress plugin/module | **Does not exist** |
| MARS runtime | **Documentation only** |
| n8n workflows | **Do not exist** |
| Website Factory prototype | **Not created** |

Do not treat this document as authorization to deploy code without explicit operator implementation charter.

---

## 2. Product Summary

Build an **internal Report Hub** on existing i-seo.su WordPress that:

1. Manages i-SEO clients and SEO projects with type profiles.
2. Runs **monthly reporting cycles** (3 weekly checkpoints + 1 monthly final).
3. Lets assigned SEO specialists enter data manually, select standardized works, attach evidence, and link Topvisor reports.
4. Routes reports through **review and approval**.
5. Publishes **approved client web reports** on i-seo.su via controlled private links.
6. Emits **notification events** for future n8n automation (reminders, AI draft assist, delivery).

WordPress is **source of truth**. n8n is external helper only. MARS holds docs. Website Factory may prototype UI separately.

---

## 3. MVP Modules

| # | Module | MVP deliverable |
|---|--------|-----------------|
| 1 | **Client / project management** | CRUD clients, projects, profiles, assignments |
| 2 | **User roles and project assignment** | Specialist scoped access; reviewer; admin |
| 3 | **Reporting cycle** | Auto or manual open cycle per project/month |
| 4 | **Weekly checkpoints** | 3 editors per cycle |
| 5 | **Monthly final reports** | Full block-based monthly editor |
| 6 | **Work dictionary** | Selectable canonical works (sanitized corpus) |
| 7 | **Block library** | Required/optional/profile blocks |
| 8 | **Manual metrics** | Entry + display in cards/charts |
| 9 | **Evidence / external links** | Files, URLs, Topvisor link + optional screenshot |
| 10 | **Review / approval** | Submit → review → revision → approve |
| 11 | **Web report renderer** | Client page from Published Version |
| 12 | **Basic notification events** | Logged events; webhook optional stub |

---

## 4. Suggested Technical Direction

Product-level guidance only — **not code specification**:

| Area | Likely direction |
|------|------------------|
| **Packaging** | WordPress custom plugin or site-specific module on i-seo.su |
| **Storage** | **Hybrid:** CPTs for major objects; custom tables for metrics, blocks, works, events |
| **Admin UI** | Custom admin screens (may extend wp-admin); exact approach **SAFE UNKNOWN** |
| **Client render** | Dedicated template/route reading immutable published snapshot |
| **Private links** | Opaque token URL; security detail in separate gate |
| **API** | **Not required** in MVP — manual entry + external links |
| **n8n** | Outbound webhooks or REST read endpoints later; human approval gates remain |
| **Media** | WP Media Library for evidence files |
| **Charts** | Client-side chart library from snapshot data — library TBD |
| **AI** | Post-MVP via n8n; draft endpoints with clear marking |

Reference docs for Anton:

- [I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md)
- [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md)
- [I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md](I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md)
- [I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md)

**Forge WordPress / WPilot:** May assist local experimentation — **not** automatic production path. Production target is i-seo.su external hosting.

---

## 5. Open Technical Decisions

| Decision | Status |
|----------|--------|
| CPT vs custom tables per entity | **OPEN** — hybrid recommended; spike needed |
| Frontend framework vs classic WP admin | **OPEN** |
| Chart library (admin + client) | **OPEN** |
| PDF/export engine | **DEFERRED** post-MVP |
| File storage limits and retention | **OPEN** — hosting review |
| Private link security (token, expiry, revoke) | **OPEN** — security gate |
| n8n webhook design and authentication | **OPEN** |
| API credentials storage layer | **OPEN** — must be separate from reports |
| Performance/caching for client reports | **OPEN** |
| Backup/versioning of published snapshots | **OPEN** |
| Plugin conflicts on i-seo.su (existing proposal generator) | **OPEN** — site audit needed |
| Multisite vs single-site | **SAFE UNKNOWN** |

---

## 6. Website Factory / Prototype Hand-off

### Prototype candidates (optional, pre-implementation)

| Screen | Value |
|--------|-------|
| Admin dashboard | Deadline UX validation |
| Weekly checkpoint editor | Form density |
| Monthly report editor | Multi-block layout |
| Client web report page | **Highest priority** — client-facing design |

### Clarification

- Website Factory prototype is **optional** before implementation.
- Requires **separate operator charter** — no workspace from documentation tasks alone.
- Prototype output is **not** deployed Report Hub.
- Prototype informs UX; Anton implements on WordPress.

---

## 7. MVP Acceptance Boundaries

MVP is accepted when all are true:

1. Specialist can view and manage **assigned projects** only.
2. Specialist can open/create **monthly reporting cycle** for a project.
3. Specialist can complete **3 weekly checkpoints** and **1 monthly final**.
4. Specialist can **select work dictionary items** in completed works blocks.
5. Specialist can **enter metrics manually** and see them in report preview.
6. Specialist can **attach evidence** (link + screenshot) and **Topvisor URL**.
7. Specialist can **submit monthly for review**.
8. Reviewer can **approve** or **request revision**.
9. Approved monthly report **publishes as client web page** on i-seo.su.
10. Operator can **view published link** and publish history.
11. **No secrets** storable in report fields by design.
12. **Notification events** defined and logged (n8n wiring optional).

---

## 8. Non-goals

Repeat of MVP exclusions:

- Full client portal with login
- Automatic API import (Topvisor, Metrika, GSC, GA4)
- Autonomous AI publication to clients
- Full n8n automation suite in MVP
- BI/data warehouse
- Live Topvisor iframe/embed as requirement
- PDF as primary delivery format
- Public unrestricted report URLs
- MARS as runtime orchestrator
- Credential storage in report database

---

## 9. Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **WordPress complexity** | Schedule slip | Phased MVP; hybrid storage spike first |
| **Data model sprawl** | Unmaintainable schema | Strict entity list; custom tables for repeats |
| **Weak access model** | Data leak between projects | Project-scoped caps from day one |
| **Report URL security** | Unauthorized client access | Dedicated security gate before publish MVP |
| **Too early automation** | n8n bypasses human review | Events only; approval gates in WP |
| **Unsanitized work dictionary** | Wrong or sensitive content in reports | Dictionary extraction gate before populate |
| **Credentials mixed with reports** | Security incident | Separate integration layer; validation rules |
| **Specialist adoption** | Low usage | Preserve flexibility within blocks; training |
| **i-seo.su hosting limits** | Custom tables/plugin blocked | Hosting review before charter |

---

## 10. Next Build Gate

Before any implementation work:

| # | Gate | Owner |
|---|------|-------|
| 1 | **Operator approval** of planning docs v0.1 | Андрей / Никита |
| 2 | **Decide data storage strategy** (hybrid confirmation) | Anton spike + operator |
| 3 | **Decide first screen prototypes** (Website Factory charter or skip) | Operator |
| 4 | **Decide URL security approach** | Operator + Anton |
| 5 | **Sanitize work dictionary** from Nikita materials (exclude credential sheet) | Operator task |
| 6 | **Define minimal project profile fields** | Product |
| 7 | **Explicit implementation charter (HITL)** for i-seo.su deployment | Operator |

**No build until gates 1 and 7 are satisfied.**

---

## Document control

- **Audience:** Anton, operator, future implementation agent
- **Does not authorize:** deployment, plugin install, or production changes
- **MARS role:** documentation locus only
