# REPORT — SITE-002 STABLE CHECKPOINT M9.13 ABOUT COMPANY RESTORED 01

**Project:** SITE-002 (ЗПМ / BZPM)  
**Date:** 2026-06-23  
**Prior authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**New authority:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`  
**Mode:** Stable checkpoint registration — documentation only (no deploy, no FTP)

---

## 1. Authority state

| Field | Value |
|-------|--------|
| **Authority** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| **Supersedes** | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| **Environment** | TEST — https://zpm.new-site.space/ |
| **Manual UI policy** | **CANONICAL** — operator CSS/Twig/JS/UX edits on live TEST override pass reports and work copies |
| **Restoration type** | **Operator-approved restoration** — **not** a rollback failure |

---

## 2. Registered lifecycle — M9.13 About Company Redesign

| Stage | Status | Reference |
|-------|--------|-----------|
| Design | Complete | Corporate Pages Program · M9.13 charter |
| Implementation | **IMPLEMENTED** | [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md) |
| Redesign QA | **QA PASSED** | Redesign report |
| Polish | **IMPLEMENTED** | [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md) |
| Polish QA | **QA PASSED** | Polish report |
| Operator review | **REJECTED BY OPERATOR** | Visual evaluation — redesign not accepted |
| Restoration | **RESTORED** | [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md) |
| Restoration QA | **QA PASSED** | Restore report §5 |

**Current canonical About state:** restored pre-M9.13 version on live TEST `/about`.

---

## 3. Stable scope

### Carried forward (unchanged)

Full catalog UX cluster from `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`:

- Filter recovery (06D–06M)
- Filter UX (04–08A)
- Wishlist / Compare tooltips (01)
- Commercial Trust (03B/03C + operator polish)
- Catalog state persistence (09A–09C)
- Hub cleanup (10)
- M9.8.1 / M9.8.2 / M9.8.5 + operator manual PLP polish

### New in this checkpoint

- M9.13 About Company lifecycle registered end-to-end
- About page restoration documented as intentional operator decision
- Knowledge Map **§17 About Page History** added
- About-page PRE-TASK rule for future redesign work

---

## 4. Knowledge map updates

**File:** [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)

| Change | Content |
|--------|---------|
| **§17 About Page History** | **Added** — original page, M9.13 redesign, polish, operator review, restoration, current canonical state |
| **§1 Authority** | Updated to `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| **§13 PRE-TASK RULE** | Updated checkpoint reference; added domain-specific rule for About page tasks |

---

## 5. Operational rules

### General (unchanged)

Before **any** SITE-002 task: read Knowledge Map + latest stable checkpoint; verify authority state.

### About page — new mandatory rule

Before **any** new About page redesign or structural change:

1. Read [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md)
2. Read [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md)
3. Read [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md)
4. Read Knowledge Map **§17 About Page History**
5. Treat **restored version** on live TEST as **source of truth**

Registered in Knowledge Map §13 and baseline §9.1.

---

## 6. Files updated

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md` | **created** |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | §17 + authority + PRE-TASK update |
| `site-passport.md` | authority, status, About restoration scope |
| `README.md` | authority, active checkpoint |
| `../../OCPILOT-STATE.md` | SITE-002 state |
| `../../OPERATIONAL-INDEX.md` | Run **4.146** |
| `reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md` | **created** — this report |

---

## 7. Git result

| Item | Value |
|------|--------|
| Commit | **requested** — checkpoint registration commit |
| Push | **requested** |
| Live changes | **NONE** — documentation only |

---

## 8. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Twig cache clear after restore | **SAFE UNKNOWN** — empty FTP listing; operator manual clear if stale render |
| M9.8.9-09C browser QA Q1–Q6 | **PENDING operator** |
| ocStore / OpenCart exact version | **SAFE UNKNOWN** |
| M10 scope and authorization | **not authorized** |
| Future About redesign charter | **not authorized** until operator approves new pass |

---

*Documentation only — no runtime claimed.*
