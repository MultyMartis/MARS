# REPORT — HOME COMMERCIAL TRUST REPLACEMENT

**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` · `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` · `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`  
**Checkpoint:** `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01`  
**Date:** 2026-06-29  
**Branch:** `mars/canonical-post-recovery` @ `e3146922` (pre-deploy checkpoint) → post-task commits pending operator review  
**Commit / push:** **NO** (per default git rules)

---

## 1. Preflight

| Step | Result |
|------|--------|
| Branch | `mars/canonical-post-recovery` ✓ |
| HEAD (pre-task checkpoint) | `e3146922d40847cd9ea3d8f3747456255e4100f7` |
| Git checkpoint | `checkpoint: pre SITE-002 home commercial trust replacement (preflight work dir)` |
| FTP backups | Suffix `.pre-home-commercial-trust-01.bak` in `backups/` |
| Manifest | [deploy-manifest-20260628-193640.json](home-commercial-trust-work/deploy-manifest-20260628-193640.json) · [fix-manifest-20260628-193747.json](home-commercial-trust-work/fix-manifest-20260628-193747.json) |
| SHA256 | [deploy-sha256-20260628-193640.json](home-commercial-trust-work/deploy-sha256-20260628-193640.json) · fix manifest per-file hashes |

---

## 2. HTML replaced

| Location | Before | After |
|----------|--------|-------|
| **Home** CTA slot (`{{ blockdealersform }}` via `home.php`) | `<section class="zpm-dealers" data-dealers>` — 2-col universal grid, bare form, «Дилерам и оптовикам» | `<section class="zpm-commercial-trust zpm-dealers" data-commercial-trust data-dealers>` — catalog Commercial Trust card (cert podium + 3 benefits + form wrap) |
| **`/katalog`** | Unchanged — still `sections/blockdealersform.twig` legacy dealers block |

**Live files (final):**

| Remote | Role |
|--------|------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust_home.twig` | **NEW delivery partial** — Home-only markup (same `zpm-commercial-trust` structure as PLP first section; no PLP FAQ grid) |
| `catalog/controller/common/home.php` | Loads `blockcommercialtrust_home` into `blockdealersform` variable |
| `catalog/view/theme/default/template/sections/blockdealersform.twig` | **Restored** legacy dealers markup for `/katalog` |

**Repo work copies:** [home-commercial-trust-work/](home-commercial-trust-work/)

---

## 3. CSS reused (no new CSS file / rules)

All presentation from existing `assets/css/style.css` (Operator Manual Polish 01 authority):

| Class family | Reuse |
|--------------|-------|
| `.zpm-commercial-trust` | Section shell, card, wrap, header, lead |
| `.zpm-commercial-trust__main` | Cert column + benefits grid |
| `.zpm-commercial-trust__cert-*` | Certificate podium (unchanged asset paths) |
| `.zpm-commercial-trust__benefits-grid` / `__benefit*` | 3 OEM benefit rows |
| `.zpm-commercial-trust__form-wrap` / `__form-card` | Form card + decor logo |
| `.zpm-decoration-with-logo` | Background contours |
| `.zpm-form__*` | Form grid, fields, agree, submit |
| `.zpm-dealers` | **Dual hook only** — `position: relative`; enables existing JS selector |

**New CSS classes created:** **none**

**Legacy Home CSS no longer hit on Home:** `.zpm-dealers__grid`, `.zpm-dealers__text`, `.zpm-universal__grid` (dealers layout) — still present in CSS for `/katalog`.

---

## 4. JS / form behaviour

| Item | Value |
|------|-------|
| Handler | Existing IIFE — `formSelector: '.zpm-dealers[data-dealers] .zpm-form'` |
| Hook | Dual class `zpm-commercial-trust zpm-dealers` + `data-dealers` on Home section |
| Endpoint | `POST /index.php?route=checkout/anketa` · `dialog=7` |
| Fields | name, phone, email, message, agree — **unchanged count/names** |
| JS file | **Not modified** |

---

## 5. Adapted texts (Home vs catalog)

| Element | Home copy |
|---------|-----------|
| Label | Связаться с заводом |
| H2 | Получите прайс-лист, консультацию или условия сотрудничества |
| Lead | Предприятия + дилеры/опт; подбор, расчёт, КП, документы для закупки |
| Benefit 1 | Собственное производство — Барнаул, без посредников |
| Benefit 2 | Документы для закупки |
| Benefit 3 | Дилерам и оптовикам — ссылка `/dealers` |
| Form title | Получить прайс-лист |
| Form note | Актуальный прайс + подбор под предприятие/проект |

Catalog PLP wording («Поможем с выбором», category H2, FAQ grid) **not used** on Home.

---

## 6. Legacy dealers files still in use

| File | Status on Home | Status elsewhere |
|------|----------------|------------------|
| `sections/blockdealersform.twig` | **No longer rendered** on Home | **Active** on `/katalog` |
| `.zpm-dealers__*` layout CSS | Not used on Home markup | Applies on `/katalog` legacy block |

---

## 7. Backups

| Backup local | Remote |
|--------------|--------|
| `backups/catalog__view__theme__default__template__sections__blockdealersform.twig.pre-home-commercial-trust-01.bak` | `sections/blockdealersform.twig` |
| `backups/catalog__controller__common__home.php.pre-home-commercial-trust-01.bak` | `controller/common/home.php` |
| `backups/catalog__controller__product__katalog.php.pre-home-commercial-trust-01.bak` | `controller/product/katalog.php` (capture only — not modified) |
| `backups/catalog__view__theme__default__template__common__home.twig.pre-home-commercial-trust-01.bak` | `common/home.twig` (capture only — not modified) |

---

## 8. SHA256 (final live targets)

| Artifact | SHA256 | Bytes |
|----------|--------|-------|
| `blockcommercialtrust_home.twig` | `69b4daad5621dbe0fe7140159466e4c70a56f226f0faa0f14b83fb5b23f06386` | 9160 |
| `home.php` | `8e68ab0866f7822c6530b37dd0c4544c22b86b4895f32035def7fe338e098fb9` | 3852 |
| `blockdealersform.twig` (restored) | `5abad9f2d27e3f575f6d79b4d50bd877c0fb6844645aff6af4f2f8b2bb9bbe99` | 4375 |

---

## 9. Git

| Item | Value |
|------|--------|
| Pre-deploy checkpoint | `e3146922` — work dir + deploy scripts |
| Post-task | Documentation + work artefacts staged; **no push** |
| **GIT CHECKPOINT NEEDED** | **Omit** — scoped Home CTA swap; operator HITL gate applies |

---

## 10. QA (automated probe)

| URL | HTTP | Commercial Trust | Legacy dealers grid | Notes |
|-----|------|------------------|---------------------|-------|
| `/` | 200 ✓ | ✓ | ✗ | `data-dealers` + `dialog=7` present |
| `/katalog` | 200 ✓ | ✗ | legacy `zpm-dealers` section ✓ | Isolation fix verified |

**Manual HITL still required:** Desktop / tablet / mobile visual pass · console · overflow · form submit · spacing vs adjacent Home sections.

**Console / overflow:** **SAFE UNKNOWN** — not instrumented in automated probe.

---

## 11. Rollback

```bash
python projects/ocpilot/sites/site-002/reports/home-commercial-trust-work/site-002-home-commercial-trust-rollback.py
```

Restores pre-change `blockdealersform.twig` + `home.php`; deletes `blockcommercialtrust_home.twig`; clears Twig cache.

---

## 12. Checkpoint

**Registered:** [baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](../baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md)

---

## 13. Scope compliance

| Rule | Status |
|------|--------|
| Hero · Categories · Advantages · Catalog PLP · Reviews · Footer · Header · FAQ · Corp pages | **Untouched** ✓ |
| No new design system / CSS file | ✓ |
| Certificate block as in catalog component | ✓ |
| Existing FA icons only | ✓ |

**Note:** `blockcommercialtrust_home.twig` is a **delivery partial** (Home wiring), not a new visual component — same `zpm-commercial-trust` markup family as PLP.

---

## 14. UNKNOWN / SECURITY

| Signal | Detail |
|--------|--------|
| **UNKNOWN** | Manual responsive/console QA not run in agent session |
| **SECURITY RISK** | FTP credentials in deploy scripts — operator-local pattern; not for public commit beyond existing SITE-002 work copies |

---

**STOP — awaiting operator HITL.**
