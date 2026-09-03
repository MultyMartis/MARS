# REPORT — ISEO-SU SITE OPS SEO TEAM TASK PACK REGISTRATION 01

**Task ID:** `ISEO-SU-SITE-OPS-SEO-TEAM-TASK-PACK-REGISTRATION-01`  
**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-09-03  
**Mode:** DOCUMENTATION / ROADMAP ONLY  
**Canonical branch:** `mars/canonical-post-recovery`

---

## 1. Scope

Зафиксировать в MARS утверждённый пакет задач SEO-команды по `i-seo.su`, сформировать каноническую карту действий (3 waves) и сохранить историю принятого решения.

**В scope:** documentation registration, roadmap, index/register updates, scoped Git persistence + remote sync.

**Out of scope:** любая production implementation (forms, pages, sitemap, menu, canonical, robots, DB, CSS/JS/PHP production-source mutations).

---

## 2. Source Task Pack

Источник: SEO-team requirements / content package (2026-09).

Canonical planning authorities created:

- `ISEO-SU-SEO-TEAM-NEW-TASK-PACK-2026-09-v1.md`
- `ISEO-SU-IMPLEMENTATION-ROADMAP-2026-09-v1.md`

User-upload / temporary chat paths не сохранены как SoT.

---

## 3. Approved Workstreams

| Wave | Name | Status |
|------|------|--------|
| 1 | Form Consent | **NEXT** |
| 2 | City SEO pages ×5 | **QUEUED** |
| 3 | USA / UAE draft pages ×2 | **QUEUED / OPEN DECISIONS** |

Order locked: 1 → 2 → 3.

---

## 4. WAVE 1

Form Consent: обязательный checkbox согласия на ПДн на контактных формах; client + server validation; сохранить HMAC / antispam / recipient / `test_mode` OFF.

Privacy policy URL: **OPEN** (кандидат `https://i-seo.su/privacy-policy.html`).

---

## 5. WAVE 2

5 city pages clone from `b-regionakh.html`; SEO content only; hub linking; self-canonical на новых URL; sitemap allowlist + regenerate; CANON-MISSING backlog не трогать; Advego/Turgenev = SEO-side residual.

---

## 6. WAVE 3

2 draft pages clone from `zarubezhnye.html`; no menu; no sitemap; open indexability + title brand decisions; case URL verify только в implementation wave.

---

## 7. Open Decisions

| ID | Status |
|----|--------|
| Exact privacy policy URL (WAVE 1) | **UNRESOLVED** (candidate: `/privacy-policy.html`) |
| USA/UAE PRE-APPROVAL INDEXABILITY | **UNRESOLVED** |
| USA/UAE TITLE BRAND SUFFIX (`itlseo` / `itlseo.su` vs `i-seo.su`) | **UNRESOLVED** |

---

## 8. Current Protected State

Не изменены: HMAC, antispam layers, recipient routing, forms security architecture, sitemap generator ownership, SEO review backlog statuses.

SEO review contour (CANON-*/TITLE-*/META-*/ORPHAN/ALT/OG/H1) **не** закрыт и **не** смешан с этим pack.

---

## 9. Files Created / Updated

**Created:**

- `projects/iseo-su-site-ops/ISEO-SU-SEO-TEAM-NEW-TASK-PACK-2026-09-v1.md`
- `projects/iseo-su-site-ops/ISEO-SU-IMPLEMENTATION-ROADMAP-2026-09-v1.md`
- `projects/iseo-su-site-ops/reports/REPORT-ISEO-SU-SITE-OPS-SEO-TEAM-TASK-PACK-REGISTRATION-01.md`

**Updated:**

- `projects/iseo-su-site-ops/ISEO-SU-CURRENT-STATE-v1.md` — section **Approved Upcoming Work**
- `projects/iseo-su-site-ops/OPERATIONAL-INDEX.md` — links + open work + next action
- `projects/iseo-su-site-ops/ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md` — register new docs

---

## 10. Production Mutations

**0**

No pages, forms, sitemap, menu, canonical, robots, DB, or production-source implementation edits.

---

## 11. Git Persistence

Main working tree was **dirty / divergent** (`ahead` foreign report-hub history, `behind` origin tip, large foreign WIP).

Scoped commit performed via clean sync worktree:

`X:\AI MARS STORAGE\git-sync-iseo-su-seo-task-pack-registration-01\repo`

Allowlisted paths only (documentation listed in §9).  
Foreign WIP on main: **untouched**.

Commit message:

`docs(iseo-su): register seo team implementation roadmap`

*(SHA filled after commit.)*

---

## 12. Remote Sync

Target: `origin/mars/canonical-post-recovery`  
Force push: **NO**

*(Result filled after push.)*

---

## 13. Final Decision

**COMPLETE — ISEO-SU SEO TEAM TASK PACK REGISTERED / IMPLEMENTATION ROADMAP CANONICAL / WAVE 1 NEXT**

Do **not** auto-start WAVE 1. Separate charter required after privacy URL confirmation.

---

## Final hard check

```text
TASK PACK REGISTERED: YES
ROADMAP CREATED: YES
CURRENT STATE UPDATED: YES
OPERATIONAL INDEX UPDATED: YES
ARTIFACT REGISTER UPDATED: YES

WAVE 1 STATUS: NEXT
WAVE 2 STATUS: QUEUED
WAVE 3 STATUS: QUEUED / OPEN DECISIONS

OPEN DECISION — PRIVACY POLICY URL: UNRESOLVED (candidate https://i-seo.su/privacy-policy.html)
OPEN DECISION — USA/UAE INDEXABILITY: UNRESOLVED
OPEN DECISION — USA/UAE TITLE BRAND: UNRESOLVED

SEO REVIEW BACKLOG MODIFIED: NO
PRODUCTION MUTATIONS: 0
IMPLEMENTATION STARTED: NO

PROJECT-OWNED UNCOMMITTED: (post-sync)
FOREIGN WIP PRESERVED: YES
REMOTE SYNC: (post-sync)
```
