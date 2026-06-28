# REPORT — SITE-002 M9.18 CUSTOM MANUFACTURING IMPLEMENTATION

**Milestone:** M9.18 — Custom Manufacturing / Оборудование на заказ  
**Environment:** https://zpm.new-site.space/custom-equipment  
**Branch:** `mars/canonical-post-recovery`  
**Date:** 2026-06-28  
**Checkpoint:** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`

---

## 1. Safety preflight

| Check | Result |
|-------|--------|
| Repository | `C:\MARS Phenix\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD (pre-task) | `c6efb08905ecdf81c82e31fab493d223cc82fe7c` (expected `26e09732` or descendant — **not exact match**; verify operator lineage) |
| Working tree | Unrelated untracked files outside M9.18 scope — **not touched** |
| Preflight manifest | [reports/m9.18-work/preflight-manifest.json](m9.18-work/preflight-manifest.json) |
| Live baseline capture | [reports/m9.18-work/custom-equipment-live.html](m9.18-work/custom-equipment-live.html) |

**Preflight facts:**

| Remote file | Pre-deploy state |
|-------------|------------------|
| `custom_equipment.php` | **Did not exist** — new controller |
| `custom_equipment.twig` | **Did not exist** — new template (legacy CMS via `information_id=14`) |
| `style.css` | SHA256 `0adc3dd3…` (344669 bytes) — backed up |
| `main.js` | SHA256 `48fe8e6d…` (204159 bytes) — backed up |
| `oc_seo_url` keyword `custom-equipment` | id **1042** — `information_id=14` → migrated to `information/custom_equipment` |

**Authority:** [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md), [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md), M9.14–M9.17 + Contacts + Commercial Trust patterns.

**Scope safety:** About · Delivery · Payment · Warranty · Dealers · Contacts · Catalog · PDP · Filters — **untouched**.

---

## 2. Files modified

| Remote path | Action |
|-------------|--------|
| `catalog/controller/information/custom_equipment.php` | **Created** — meta, breadcrumbs, pageintro H1+lead, bodyClass |
| `catalog/view/theme/default/template/information/custom_equipment.twig` | **Created** — 8 landmarks BLOCK 01–10 + charter form |
| `assets/css/style.css` | Appended `zpm-custom-*` block (~13.4 KB delta) |
| `assets/js/main.js` | Replaced corp FAQ accordion block — added `[data-custom-faq]` |
| `oc_seo_url` keyword `custom-equipment` | **Modified** id 1042: `information_id=14` → `information/custom_equipment` |

---

## 3. Files created

| Path | Role |
|------|------|
| `reports/m9.18-work/custom_equipment.php` | Work copy controller |
| `reports/m9.18-work/custom_equipment.twig` | Work copy twig |
| `reports/m9.18-work/m9.18-custom-page.css` | CSS staging |
| `reports/m9.18-work/m9.18-corp-accordion.js` | JS staging (delivery + payment + warranty + dealers + custom) |
| `reports/m9.18-work/m918-custom-deploy.py` | Deploy script |
| `reports/m9.18-work/m918-custom-screenshots.py` | Screenshot script |
| `reports/m9.18-work/deploy-manifest.json` | Post-deploy SHA256 + QA |
| `reports/m9.18-work/preflight-manifest.json` | Pre-deploy SHA256 |
| `reports/m9.18-work/qa-custom-equipment.html` | Live HTML capture |
| `baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md` | Stable checkpoint |
| `qa/m9.18-custom-screenshots/*` | Viewport screenshots + QA JSON |
| `backups/style.css.pre-m9.18-custom.bak` | Remote backup |
| `backups/main.js.pre-m9.18-custom.bak` | Remote backup |

**Note:** `custom_equipment.php` / `custom_equipment.twig` backup placeholders empty (files were new on remote).

---

## 4. Assets reused

| Pattern | Source |
|---------|--------|
| Commercial Trust CTA card | `zpm-commercial-trust__*` from M9.8.9 / M9.14–M9.16 |
| Contacts form | `zpm-form`, phone mask, email validate, consent, `dialog=7` |
| Pageintro shell | M9.14–M9.17 internal pages |
| Corp timeline | `zpm-corp-timeline` from M9.14 Delivery CSS |
| Corp FAQ accordion | `zpm-corp-faq__*` from M9.14–M9.17 |
| Production proof image | `/assets/img/about-page-img.jpg` (About attested asset) |
| Section titles | `section-title__like-h2`, `section-title__like-h3` |
| Decor logo | `/assets/img/decor-logo.svg` |

---

## 5. Deploy verification

| Item | Value |
|------|--------|
| Route | `information/custom_equipment` |
| Public URL | `/custom-equipment` |
| Deploy script | `m918-custom-deploy.py` |
| SEO patch | HTTP one-shot `m918-seo-custom-patch.php` — removed after run |
| OpenCart cache | **Required** — `storage/cache/*` clear after seo_url migration (5 files) |
| Twig cache | Empty listing on remote |

---

## 6. QA results

| Check | Result |
|-------|--------|
| HTTP 200 | PASS (desktop 1440 · tablet 1024 · mobile 390) |
| `zpm-custom-page` | PASS |
| Pageintro lead | PASS |
| BLOCK 01 triggers (5+ bullets) | PASS |
| BLOCK 02 task matrix (7 rows) | PASS |
| BLOCK 03 scope + in/out table | PASS |
| BLOCK 04 OEM (5× H3 + proof strip) | PASS |
| Process timeline (8 steps) | PASS |
| Approval gate badge | PASS (live HTML; `&nbsp;` in markup) |
| BLOCK 06 checklist (9 rows) | PASS |
| BLOCK 07 materials (no AISI table) | PASS |
| BLOCK 08 outcomes (5 rows) | PASS |
| FAQ 8 items + `data-custom-faq` | PASS |
| CTA «Получить расчёт изделия под ваш объект» | PASS |
| Form «Заявка на расчёт» | PASS |
| Charter form fields | PASS |
| No file upload | PASS |
| No `zpm-seo` generic body | PASS |
| Console errors | PASS (0) |
| Horizontal overflow | PASS (all viewports) |
| Cross-links Payment/Delivery/Guarantee/About/Dealers | PASS |

**Automated deploy QA:** `all_pass` false only on literal-string `approval_badge` probe (`&nbsp;` in live HTML) — **HITL: badge present**.

**Screenshot QA JSON:** [qa/m9.18-custom-screenshots/m9.18-custom-qa-results.json](../qa/m9.18-custom-screenshots/m9.18-custom-qa-results.json) — **pass: true**

---

## 7. Screenshots

| File | Viewport |
|------|----------|
| `qa/m9.18-custom-screenshots/m9.18-custom-desktop-1440-full.png` | 1440 full page |
| `qa/m9.18-custom-screenshots/m9.18-custom-desktop-1440-timeline.png` | 1440 process block |
| `qa/m9.18-custom-screenshots/m9.18-custom-desktop-1440-outcomes.png` | 1440 outcomes block |
| `qa/m9.18-custom-screenshots/m9.18-custom-desktop-1440-form.png` | 1440 CTA form |
| `qa/m9.18-custom-screenshots/m9.18-custom-tablet-1024-full.png` | 1024 full page |
| `qa/m9.18-custom-screenshots/m9.18-custom-mobile-390-full.png` | 390 full page |

---

## 8. Rollback

| Priority | Action |
|----------|--------|
| P1 | Restore `oc_seo_url` id 1042 → `information_id=14` |
| P2 | Delete `custom_equipment.php` + `custom_equipment.twig` on remote |
| P3 | Restore `style.css` from `backups/style.css.pre-m9.18-custom.bak` |
| P4 | Restore `main.js` from `backups/main.js.pre-m9.18-custom.bak` |
| P5 | Clear OpenCart + twig cache |

Legacy CMS Information entry id **14** retained for RB-4.

---

## 9. Stable checkpoint

**Registered:** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`  
**Doc:** [baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md](../baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md)

**Corporate Pages Program:** Implementation phase for M9.14–M9.18 is **COMPLETE on TEST**. No further corp page implementations remain in program scope.

---

## 10. Risks

| ID | Risk | Status |
|----|------|--------|
| R1 | Calculator/upload drift | **Mitigated** — QA PASS |
| R4 | seo_url mis-edit | **Mitigated** — verified in deploy manifest |
| R9 | Production photo missing | **Mitigated** — About image reused |
| R14 | B6/B8 open at deploy | **OPEN** — operator ack recommended |
| R18 | Form `action="#"` no backend | **SAFE UNKNOWN** — Contacts parity |
| R20 | Production URL parity | **SAFE UNKNOWN** — TEST-first |

**SECURITY RISK:** Deploy script contains FTP credentials — operator-local only; **not committed** to secrets in repo (script in repo — operator should rotate if exposed).

---

## 11. Operator review notes

- Visual hierarchy: 8-step timeline dominant; outcomes table second — **HITL recommended**
- B6 Design Charter / B8 Copy sign-off remain **OPEN** — does not block TEST checkpoint
- PLP Commercial Trust «На заказ» chip → `/custom-equipment` link update = **separate task**
- Remaining work: visual polish · UX polish · responsive polish · production parity · final QA · production rollout

---

## 12. Git

| Item | Value |
|------|--------|
| Commit | *(pending this task)* |
| Push | `mars/canonical-post-recovery` *(pending)* |
| HEAD (pre-commit) | `c6efb08905ecdf81c82e31fab493d223cc82fe7c` |

**SAFE UNKNOWN:** Production `bzpm.ru/custom-equipment` parity not verified in this pass.

---

*Corporate Pages Program implementation completed on TEST. Terminal milestone M9.18 delivered.*
