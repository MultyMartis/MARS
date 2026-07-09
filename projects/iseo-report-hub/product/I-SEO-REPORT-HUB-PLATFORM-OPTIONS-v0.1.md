# I-SEO Report Hub — Platform Options v0.1

**Status:** PLANNING — platform options analysis  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10  
**Implementation:** **NOT STARTED** — no platform decision yet

---

## 1. Status

This document records **platform options** for i-SEO Report Hub after operator review of static demo v0.1.

| Fact | State |
|------|-------|
| Document type | Planning / decision support |
| Platform decision | **Not made** |
| WordPress as sole assumption | **Reopened** — no longer hard-bound |
| PHP + MySQL custom system | **Accepted candidate** |
| Runtime / code | **Does not exist** |

Earlier product docs (charter v0.1, WordPress architecture v0.1) assumed WordPress on i-seo.su as the approved production platform. This document **does not revoke** those docs but **supersedes the assumption** that WordPress is the only viable path until a later decision gate.

---

## 2. Why Platform Is Reopened

Operator review of localized static demo v0.1 (2026-07-10) established:

1. **Workflow mechanics are validated.** The demo successfully shows admin-to-report flow, weekly/monthly/check/review/client-page concepts, and useful product movement for internal discussion.

2. **Report structure is not yet validated.** Current demo fields and admin report content are generic placeholders. They do not reflect the intended SEO reporting structure derived from Denis/Ilya corpus patterns and operator direction.

3. **Custom UX scope is significant.** Report Hub requires block-based report composition, weekly checkpoints, monthly final synthesis, internal vs client-facing field separation, review workflow, and project-type profiles. This is closer to a **custom reporting application** than a typical WordPress content workflow.

4. **WordPress binding may add friction.** WP custom post types, meta fields, admin UI constraints, and plugin/theme boundaries can become awkward when the product needs a highly tailored report builder and admin experience.

5. **Custom PHP + MySQL may fit better.** i-SEO can potentially build a standalone or subdirectory web application with a cleaner entity model, direct UX control, and faster iteration for this specific use case — without fighting CMS conventions.

**Conclusion:** Platform choice should follow report structure stabilization, demo v0.2 review, and SEO specialist feedback — not precede them.

---

## 3. Option A — WordPress / i-seo.su Module

### Description

Report Hub implemented as a WordPress-based module on the existing i-seo.su site:

- Uses existing i-seo.su hosting and environment
- May reuse WordPress admin auth, user roles, and site context
- Client web report pages live under i-seo.su (controlled URLs)
- Data stored in WP custom post types, taxonomies, and post meta (per data model v0.1 planning)
- Admin UX embedded in or adjacent to WP admin shell

### Pros

| Advantage | Detail |
|-----------|--------|
| Existing site | i-seo.su already operational on WordPress |
| Existing hosting | No new deployment surface unless subdomain chosen |
| Familiar CMS | Team may know WP admin patterns |
| Commercial proposal precedent | i-seo.su already has web generator for commercial proposals — similar delivery pattern |
| Possible asset reuse | Branding, theme elements, existing i-seo.su visual identity |
| Single domain | Client reports on same trusted domain as i-SEO |

### Cons

| Disadvantage | Detail |
|--------------|--------|
| WP data model complexity | Cycles, checkpoints, block library, published versions, evidence — awkward in CPT/meta alone |
| Custom admin UX friction | Report builder, review queue, dictionary management may fight WP admin UX |
| Plugin/theme boundary risks | Updates, conflicts, maintenance coupling to WP stack |
| Performance/scaling | Heavy meta queries, admin list screens for complex entities |
| Developer specialization | Anton scoped as WP developer — custom app may need different skill mix |
| Highly custom product in CMS shell | Report Hub may be simpler as purpose-built app than as WP plugin |

---

## 4. Option B — Custom PHP + MySQL Report Hub

### Description

Standalone or subdirectory/subdomain web application:

- Custom PHP application (framework choice deferred — not decided in this doc)
- MySQL database with purpose-built tables/entities for projects, cycles, checkpoints, reports, blocks, evidence, dictionary
- Custom admin UI for SEO specialists and reviewers
- Custom client web report renderer (HTML pages from approved published versions)
- Deployed on i-SEO-controlled hosting (same server or separate vhost — **SAFE UNKNOWN**)

### Pros

| Advantage | Detail |
|-----------|--------|
| Cleaner data model | Entities map directly to reporting domain without CPT/meta workarounds |
| Simpler custom report blocks | Block library, profiles, and field visibility are first-class design concerns |
| Direct UX control | Admin screens built exactly for weekly/monthly/review workflows |
| Faster iteration for this use case | No WP admin constraints, plugin API limits, or theme coupling |
| Clear separation | Reporting product isolated from i-seo.su marketing site CMS concerns |
| Easier testing | Application boundaries clearer for MVP scope |

### Cons

| Disadvantage | Detail |
|--------------|--------|
| Auth/security design required | Login, roles, session management, CSRF, report URL tokens — all custom |
| Deployment/maintenance ownership | Hosting, backups, updates, PHP version, SSL — i-SEO responsibility |
| Backup/versioning needed | DB + file storage discipline required |
| More custom engineering | Full stack ownership; no WP ecosystem plugins for admin/media |
| Integration with i-seo.su | Visual/branding integration requires explicit design |
| Team capacity | Anton/build ownership and timeline — **SAFE UNKNOWN** |

---

## 5. Option C — Hybrid

### Description

Combined approach:

- **Core:** Custom PHP + MySQL application owns report entities, workflow, admin UX, and published version snapshots
- **Public/client layer:** Client report pages may be visually integrated with i-seo.su (shared header/footer, brand assets) via:
  - subdomain (e.g. `reports.i-seo.su`) with matched styling, or
  - reverse proxy/path on i-seo.su pointing to app, or
  - standalone styled pages linked from i-seo.su
- **Optional WP embedding:** Later, WP pages could link to or iframe report URLs if policy allows — not MVP assumption
- **n8n:** Remains external helper in all variants; not source of truth

### When hybrid makes sense

- Report logic and admin need custom app quality
- Client-facing delivery should feel "on i-SEO" brand-wise
- WordPress site remains marketing/content CMS; Report Hub is operational subsystem

---

## 6. Current Recommendation

**Remain platform-neutral through demo v0.2 and SEO feedback stage.**

| Stage | Action |
|-------|--------|
| Now | Model report structure and admin/report UX independently of platform |
| Demo v0.2 | Inject real report blocks and 3 demo projects into static HTML prototype |
| After v0.2 | Operator review + SEO specialist feedback on **structure and UX**, not platform |
| Then | Choose WordPress vs PHP+MySQL vs hybrid with evidence from structure complexity, security needs, and build ownership |

**Do not** block report structure work on platform decision.  
**Do not** assume WordPress implementation brief v0.1 is the only path forward — treat it as one option's planning artifact.

---

## 7. Decision Gates

Platform decision requires passing these gates:

| Gate | Criterion |
|------|-----------|
| **Report structure stabilized** | Universal monthly blocks, weekly checkpoints, project type variants documented and reflected in demo v0.2 |
| **Demo v0.2 operator review** | Static prototype shows realistic structure for 3 project types |
| **SEO feedback collected** | Specialists reviewed demo v0.2 structure (not v0.1 mechanics-only demo) |
| **Security model clarified** | Client report URL strategy, auth for admin, role model — at planning level |
| **Hosting/deployment constraints known** | i-seo.su hosting capabilities, subdomain policy, PHP/MySQL availability |
| **Anton/build ownership clear** | Who builds, on what timeline, WP vs custom app skill fit |

Until all gates relevant to the decision are addressed, **no platform commitment**.

---

## 8. Non-goals

This document explicitly excludes:

- Implementation of any platform option
- Database schema finalization
- Deployment plan or hosting procurement
- Migration plan from current manual reporting to Report Hub
- Authentication design finalization
- WordPress plugin scaffold
- PHP application scaffold
- API or n8n wiring

---

## 9. Relationship to Existing Docs

| Document | Relationship |
|----------|--------------|
| [I-SEO-REPORT-HUB-PRODUCT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-PRODUCT-CHARTER-v0.1.md) | §4 WordPress direction remains historical approved persist; platform reopened per operator pivot 2026-07-10 |
| [I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md) | Valid as **Option A** planning artifact |
| [I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md) | Valid as Option A data model sketch; may inform Option B entity design |
| [I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md](I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md) | WP-focused brief; **not** exclusive implementation path until platform gate |

---

## 10. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Final platform choice | **UNKNOWN** |
| i-seo.su hosting PHP/MySQL app constraints | **UNKNOWN** |
| Subdomain availability for reports | **UNKNOWN** |
| Anton preference and capacity for custom app vs WP | **UNKNOWN** |
| Cost/complexity comparison (WP plugin vs custom app MVP) | **UNKNOWN** |
| ATLAS/OPS integration impact on platform choice | **UNKNOWN** |

---

## Document control

- **Created:** 2026-07-10 (platform pivot modeling task 01)
- **Does not claim:** any runtime, plugin, PHP app, or deployment exists
- **Authority:** operator review of static demo v0.1 + platform pivot decision
