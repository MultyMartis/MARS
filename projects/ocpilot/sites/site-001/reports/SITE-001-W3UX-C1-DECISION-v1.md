# SITE-001 W3UX-C1 Decision v1

**Type:** Post-execution decision — W3UX-C1 Used Catalog Card Density  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Change request:** CR-SITE-001-W3UX-C1-2026-06  
**Checkpoint:** `site-001-phase1-stable-2026-06`

**Inputs:** [SITE-001-W3UX-C1-DISCOVERY-v1.md](SITE-001-W3UX-C1-DISCOVERY-v1.md) · [SITE-001-W3UX-C1-EXECUTION-v1.md](SITE-001-W3UX-C1-EXECUTION-v1.md)

---

## Verdict

### **PASS WITH NOTES**

W3UX-C1 meets density targets on desktop and tablet, preserves layout and scope boundaries, and passes all route verification. Mobile card height increased slightly (+7%) — noted for operator review; does not block wave acceptance.

---

## Decision criteria evaluation

| Criterion | Result | Evidence |
|-----------|--------|----------|
| Card height reduced | **PASS** (desktop/tablet) · **NOTE** (mobile) | −24% desktop · −24% tablet · +7% mobile |
| Layout intact | **PASS** | 5/5 URLs HTTP 200; no automated overflow flags |
| All routes pass | **PASS** | `/cars/`, `/cars/bmw/`, `/cars/audi/` verified |
| CSS only | **PASS** | No twig/JS/PHP/DB changes |
| Scope respected | **PASS** | `.used_catalog` only; `/auto/` and `/` controls unchanged |
| No content add/remove | **PASS** | Spacing/hierarchy only |
| Rollback ready | **PASS** | `pre-w3ux-c1-20260609-0416` |

---

## Measured outcomes

| Metric | Target | Actual |
|--------|--------|--------|
| Desktop card height reduction | 15–20% | **24.0%** (530→403 px) |
| Tablet card height reduction | 15–20% | **24.3%** (573→434 px) |
| Mobile card height reduction | 15–20% | **−7.3%** (451→484 px) — **miss** |
| URL verification | All pass | **5/5 PASS** |
| New catalog regression | No change | **PASS** |

---

## Operator notes

| ID | Severity | Note | Action |
|----|----------|------|--------|
| N-W3UX-C1-01 | Low | Sparse `/cars/` inventory on TEST | Spot-check on `/cars/audi/` with full grid |
| N-W3UX-C1-02 | Medium | Mobile card taller than baseline | Browser review on 390px viewport; optional W3UX-C1b mobile tune |
| N-W3UX-C1-03 | Info | Operator browser sign-off pending | Visual hierarchy/price dominance review |

---

## Rollback status

| Field | Value |
|-------|-------|
| Rollback executed | **NO** |
| T1 package | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3ux-c1-20260609-0416\` |
| Restore procedure | FTP STOR 2 CSS files + cache clear |

---

## Next steps (not authorized in this wave)

| Wave | Scope | Status |
|------|-------|--------|
| W3UX-C2 | New catalog card density | **NOT AUTHORIZED** |
| W3UX-PDP-U | Used PDP compaction | **NOT AUTHORIZED** |
| W3UX-QA | Full matrix gate | After C1–C2 waves |

---

## Authorization record

| Role | Decision | Date |
|------|----------|------|
| Automated verification | **PASS WITH NOTES** | 2026-06-09 |
| Operator (**Андрей**) | Browser sign-off **PENDING** | — |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — W3UX-C1 decision **PASS WITH NOTES** |
