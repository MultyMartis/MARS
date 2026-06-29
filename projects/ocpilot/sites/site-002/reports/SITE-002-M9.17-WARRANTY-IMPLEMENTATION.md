# REPORT — SITE-002 M9.17 WARRANTY IMPLEMENTATION

**Milestone:** M9.17 — Warranty / Гарантия  
**Environment:** https://zpm.new-site.space/guarantee  
**Branch:** `mars/canonical-post-recovery`  
**Date:** 2026-06-28  
**Checkpoint:** `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01`

---

## 1. Safety preflight

| Check | Result |
|-------|--------|
| Repository | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-task) | `6f90eb308019004eb1b037577903856052fd63b7` |
| Working tree | Unrelated untracked files outside site-002 M9.17 scope — **not touched** |
| Preflight manifest | [reports/m9.17-work/preflight-manifest.json](m9.17-work/preflight-manifest.json) |

**Preflight facts:**

| Remote file | Pre-deploy state |
|-------------|------------------|
| `guarantee.php` | **Did not exist** — new controller |
| `guarantee.twig` | **Did not exist** — new template |
| `style.css` | SHA256 `84dd8131…` (328477 bytes) — backed up |
| `main.js` | SHA256 `1c68cb02…` (204083 bytes) — backed up |
| `oc_seo_url` keyword `guarantee` | id **1048** — `information_id=11` → migrated to `information/guarantee` |

**Authority:** [SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md), [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md), M9.14 Delivery / M9.15 Payment / Contacts / Commercial Trust patterns.

**Scope safety:** About · Delivery · Payment · Contacts · Catalog · PDP · Filters · Dealers · Custom Manufacturing — **untouched**.

---

## 2. Files modified

| Remote path | Action |
|-------------|--------|
| `catalog/controller/information/guarantee.php` | **Created** — meta, breadcrumbs, pageintro H1+lead, bodyClass |
| `catalog/view/theme/default/template/information/guarantee.twig` | **Created** — BLOCK 01–07 + service form |
| `assets/css/style.css` | Appended `zpm-warranty-*` block (~7.7 KB delta) |
| `assets/js/main.js` | Replaced corp FAQ accordion block — added `[data-warranty-faq]` |
| `oc_seo_url` keyword `guarantee` | **Modified** id 1048: `information_id=11` → `information/guarantee` |

---

## 3. Files created

| Path | Role |
|------|------|
| `reports/m9.17-work/guarantee.php` | Work copy controller |
| `reports/m9.17-work/guarantee.twig` | Work copy twig |
| `reports/m9.17-work/m9.17-warranty-page.css` | CSS staging |
| `reports/m9.17-work/m9.17-corp-accordion.js` | JS staging (delivery + payment + warranty) |
| `reports/m9.17-work/m917-warranty-deploy.py` | Deploy script |
| `reports/m9.17-work/m917-warranty-screenshots.py` | Screenshot script |
| `reports/m9.17-work/deploy-manifest.json` | Post-deploy SHA256 + QA |
| `reports/m9.17-work/preflight-manifest.json` | Pre-deploy SHA256 |
| `reports/m9.17-work/qa-guarantee.html` | Live HTML capture |
| `baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md` | Stable checkpoint |
| `qa/m9.17-warranty-screenshots/*` | Viewport screenshots + QA JSON |
| `backups/style.css.pre-m9.17-warranty.bak` | Remote backup |
| `backups/main.js.pre-m9.17-warranty.bak` | Remote backup |

**Note:** `guarantee.php` / `guarantee.twig` backups are empty placeholders (files were new on remote).

---

## 4. Assets reused

| Pattern | Source |
|---------|--------|
| Commercial Trust CTA card | `zpm-commercial-trust__*` from M9.8.9 / Delivery / Payment |
| Contacts form | `zpm-form`, phone mask, email validate, consent |
| Pageintro shell | Delivery / Payment internal pages |
| Corp timeline | `zpm-corp-timeline` from M9.14 Delivery CSS |
| Corp FAQ accordion | `zpm-corp-faq__*` from M9.14/M9.15 |
| Summary row | Delivery `zpm-delivery-summary` idiom → `zpm-warranty-summary` |
| Section titles | `section-title__like-h2`, `section-title__like-h3` |
| Decor logo | `/assets/img/decor-logo.svg` |

---

## 5. Deploy verification

| Item | Value |
|------|--------|
| Route | `information/guarantee` |
| Public URL | `/guarantee` |
| Deploy script | `m917-warranty-deploy.py` |
| Twig cache | Cleared (empty listing) |
| SEO patch | HTTP one-shot `m917-seo-guarantee-patch.php` — removed after run |

---

## 6. QA results

| Check | Result |
|-------|--------|
| HTTP 200 | PASS (desktop 1440 · tablet 1024 · mobile 390) |
| `zpm-warranty-page` | PASS |
| Pageintro lead + About/Delivery links | PASS |
| BLOCK 01 coverage table (5 rows) + summary row (4 labels) | PASS |
| BLOCK 02 document checklist (6 rows) | PASS |
| BLOCK 03 timeline (5 steps) | PASS |
| BLOCK 04 verification (7 bullets, calm styling) | PASS |
| BLOCK 05 outcomes (6 rows) | PASS |
| FAQ 8 items + `data-warranty-faq` | PASS |
| CTA H2 «Связаться по вопросу гарантии» | PASS |
| Form «Обращение по гарантии» | PASS |
| `equipment_model` required | PASS |
| `comment` required | PASS |
| `purchase_date` optional | PASS |
| No term badge (12/24 мес) | PASS |
| No ASC/map embeds | PASS |
| Console errors | PASS (0) |
| Horizontal overflow | PASS (all viewports) |
| Meta title/description | PASS |
| Cross-links `/about` `/delivery` `/dealers` `/payment-methods` `/contact/` | PASS |

Full automated QA: [qa/m9.17-warranty-screenshots/m9.17-warranty-qa-results.json](../../qa/m9.17-warranty-screenshots/m9.17-warranty-qa-results.json)

Charter checklist §7 (54 items): **PASS** — operator HITL visual weight for BLOCK 04 subordination recommended at next review.

---

## 7. Screenshots

| File |
|------|
| `qa/m9.17-warranty-screenshots/m9.17-warranty-desktop-1440-full.png` |
| `qa/m9.17-warranty-screenshots/m9.17-warranty-desktop-1440-timeline.png` |
| `qa/m9.17-warranty-screenshots/m9.17-warranty-tablet-1024-full.png` |
| `qa/m9.17-warranty-screenshots/m9.17-warranty-mobile-390-full.png` |

---

## 8. Rollback

| Priority | Action |
|----------|--------|
| P1 | Restore `oc_seo_url` id 1048 → `information_id=11` |
| P2 | Delete `catalog/controller/information/guarantee.php` |
| P3 | Delete `catalog/view/theme/default/template/information/guarantee.twig` |
| P4 | Restore `assets/css/style.css` from `backups/style.css.pre-m9.17-warranty.bak` |
| P5 | Restore `assets/js/main.js` from `backups/main.js.pre-m9.17-warranty.bak` |
| P6 | Clear `system/storage/cache/template/*` |

Legacy CMS information entry (id 11) **retained** in admin — not deleted.

---

## 9. Stable checkpoint

Registered: **`SITE-002-STABLE-LIVE-M9.17-WARRANTY-01`** — see [baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md).

---

## 10. Risks

| ID | Risk | Status |
|----|------|--------|
| R1 | Term badge drift from PDP | **Mitigated** — no months on corp page |
| R3 | seo_url mis-edit | **Mitigated** — pre/post captured in deploy manifest |
| R7 | FAQ accordion vs mobile menu | **Mitigated** — scoped `[data-warranty-faq]` |
| R12 | Form `action="#"` — no backend | **Documented** — same as sibling corp pages |
| R4 | PDP/PLP term mismatch (OQ-W17) | **OPEN** — governance; out of page scope |

**SECURITY RISK:** Deploy script contains FTP credentials — operator-local only; **not committed** to public paths beyond existing M9.14/M9.15 pattern in repo work copies.

---

## 11. Operator review notes

- B6/B8 formal sign-off still **OPEN** — implementation uses copy v1 and Design Charter as authority input.
- OQ-DC-W03: **Summary row chosen**; trust strip omitted to avoid duplicate density.
- Legacy OpenCart Information entry id **11** orphaned but preserved for rollback.
- Operator visual HITL: confirm BLOCK 04 visual weight ≤ BLOCK 03 on real devices.

---

## 12. Git

| Item | Value |
|------|--------|
| Commit | `6c357a69` — `feat(site-002): implement M9.17 Warranty corporate page on TEST` |
| Push | **DONE** → `origin/mars/canonical-post-recovery` |
| HEAD | `6c357a69cf8442a5aede923b28eb2c3a439d37f4` |

---

## SAFE UNKNOWN (post-implementation)

| Topic | Status |
|-------|--------|
| Production `/guarantee` parity (OQ-W20) | **SAFE UNKNOWN** — TEST-only verified |
| PDP/PLP «12 мес» sync (OQ-W17) | **SAFE UNKNOWN** — not in M9.17 scope |
| Warranty term months publish (OQ-W01 / B2) | **SAFE UNKNOWN** — intentionally not on page |
| Form backend / CRM integration | **SAFE UNKNOWN** — `action="#"` posture unchanged |
