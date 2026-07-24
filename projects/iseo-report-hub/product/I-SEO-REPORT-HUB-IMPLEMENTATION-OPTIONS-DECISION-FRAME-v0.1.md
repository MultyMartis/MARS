# I-SEO Report Hub — Implementation Options Decision Frame v0.1

**Status:** PLANNING — decision support (Layer 02); **no final forced choice**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED**

---

## 1. Status

This frame compares implementation options for MVP **after** demo v0.4 and report content architecture. It extends [I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md](I-SEO-REPORT-HUB-PLATFORM-OPTIONS-v0.1.md) with Layer 02 product clarity (roles, lifecycle, snapshots, modules).

**Final platform choice is not forced** unless evidence later supports it. Recommended frame below; MVP technical brief still required.

---

## 2. Option A — WordPress Module on i-seo.su

### Description

Report Hub as WordPress custom module/plugin on existing i-seo.su: CPT/meta or custom tables, wp-admin or custom admin screens, client pages on same site.

### Advantages

- Existing hosting and domain trust
- Possible reuse of WP auth/users
- Precedent: web commercial proposals on i-seo.su
- Branding alignment with marketing site

### Risks

- Complex entities (periods, blocks, snapshots, evidence) fight CPT/meta patterns
- Specialist workspace UX may fight wp-admin chrome
- Plugin/theme update coupling
- Permission model finer than WP roles needs custom caps

### Fit assessment

| Concern | Fit |
|---------|-----|
| Specialist workspace | Medium — doable but awkward |
| Report publishing | Good — pages on i-seo.su |
| Permissions | Medium — custom capabilities required |
| File/evidence storage | Good — WP media |
| Future Topvisor/API imports | Medium — WP cron/plugins |
| Operations/security | Coupled to WP hardening |

### Migration path

If WP proves insufficient: extract custom tables / app later; client URLs may need redirect plan.

### Recommendation for MVP

Viable if **speed** and **existing WP auth/admin** dominate and entity complexity stays manageable. Not automatically preferred after Layer 02.

---

## 3. Option B — Custom PHP + MySQL App

### Description

Purpose-built PHP application + MySQL schema for Report Hub entities, custom admin UI, custom client renderer. Deployed on i-SEO hosting (same server, subdirectory, or subdomain — TBD).

### Advantages

- Clean mapping to Layer 02 data model and lifecycle
- Direct UX for specialist workspace and review queue
- Clear snapshot/publish boundaries
- Easier testing of permissions and validation gates

### Risks

- Auth, CSRF, backups, deploy ownership all custom
- Branding integration with i-seo.su must be designed
- Build capacity / Anton skill mix — **SAFE UNKNOWN**
- No WP plugin ecosystem for free admin/media features

### Fit assessment

| Concern | Fit |
|---------|-----|
| Specialist workspace | Strong |
| Report publishing | Strong (own renderer) |
| Permissions | Strong |
| File/evidence storage | Strong if designed |
| Future Topvisor/API imports | Strong |
| Operations/security | Requires disciplined ops |

### Migration path

Can later embed or reverse-proxy under i-seo.su; optional WP as marketing shell only.

### Recommendation for MVP

**Strong candidate** when product clarity, DB, permissions, and future imports matter most.

---

## 4. Option C — Hybrid (Custom App + WordPress Published Pages / Embedding)

### Description

Custom PHP+MySQL owns SoT (entities, workflow, snapshots). WordPress on i-seo.su hosts or visually embeds **published** client report presentation (theme shell, path, or proxy). Admin workspace remains in the custom app.

### Advantages

- Best of both: clean product core + trusted public site surface
- Snapshot renderer can still live in app while WP provides brand chrome
- Separates marketing CMS from operational reporting

### Risks

- Two surfaces to operate (app + WP)
- Auth and URL routing complexity
- Embedding/iframe policy risks if misused
- Higher integration design cost

### Fit assessment

| Concern | Fit |
|---------|-----|
| Specialist workspace | Strong (app) |
| Report publishing | Strong if public face on i-seo.su matters |
| Permissions | Strong (app) |
| File/evidence storage | Strong (app) |
| Future imports | Strong (app) |
| Operations/security | Dual-surface care |

### Migration path

Start as B, add WP presentation layer when publish UX needs i-seo.su shell — or design C from day one if domain unity is mandatory.

### Recommendation for MVP

**Strong if** public report rendering on i-seo.su is a hard requirement while admin remains custom.

---

## 5. Option D — External No-code / Low-code Prototype

### Description

Airtable/Notion/Glide/similar for ops prototype.

### Advantages

- Fast experiments

### Risks

- Not suitable as production SoT for client reports
- Weak permissions/snapshots/audit for SEO reporting
- Vendor lock and data export pain

### Fit

Poor for production MVP. Acceptable only as disposable internal experiment — **not recommended for production**.

### Recommendation for MVP

**Do not** choose for production Report Hub.

---

## 6. Decision Frame (How to Choose)

| If priority is… | Lean toward… |
|-----------------|--------------|
| Speed + existing WP auth/admin on i-seo.su | **Option A** — WordPress module |
| Clean product, DB, permissions, future imports | **Option B** — custom PHP + MySQL |
| Public report rendering on i-seo.su + clean admin core | **Option C** — hybrid |
| Disposable experiment only | **Option D** — then throw away |

Gates before commitment (carry forward from Platform Options):

1. Structure + Layer 02 reviewed by operator  
2. Security model for client URLs clarified  
3. Hosting/deploy constraints known  
4. Build ownership (Anton / capacity) clear  
5. SEO feedback still **deferred** — not a blocker for architecture commit, but remains a later gate before declaring UX final

---

## 7. Current Likely Recommendation

**Custom PHP + MySQL (B) or Hybrid (C) appear stronger for product clarity** after Layer 02 (roles, lifecycle, snapshots, modules). WordPress (A) remains a valid speed path if constraints demand it.

**Final decision should wait** until an **MVP technical brief** (hosting, auth, ownership, timeline). This document does **not** lock the platform.

---

## 8. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Final choice A/B/C | **UNKNOWN** |
| Hosting PHP/MySQL constraints | **UNKNOWN** |
| Subdomain policy | **UNKNOWN** |
| Anton preference WP vs custom | **UNKNOWN** |
| Cost/time comparison | **UNKNOWN** |

---

## Document control

- **Created:** 2026-07-24  
- **Does not claim:** any platform implemented  
- **Supersedes assumption:** WordPress as sole path — still reopened
