# SITE-002 — Stable Live Corporate Intro Blocks Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-29  
**Mode:** Corporate intro visual blocks — 6 pages  
**Status:** **PARTIAL** — `delivery-intro.jpg` **404** until operator upload

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01`

**Parent authority:** `SITE-002-STABLE-LIVE-UNIVERSAL-CORPORATE-CTA-01` (CTA blocks unchanged)

**Scope:** Intro media blocks on About + M9.14–M9.18 corporate pages only.

---

## 2. Live surfaces

| Page | URL | Intro image |
|------|-----|-------------|
| About | `/about` | `/assets/img/corporate/about-intro.jpg` |
| Delivery | `/delivery` | `/assets/img/corporate/delivery-intro.jpg` (**404 asset**) |
| Payment | `/payment-methods` | `/assets/img/corporate/payment-intro.jpg` |
| Warranty | `/guarantee` | `/assets/img/corporate/warranty-intro.jpg` |
| Dealers | `/dealers` | `/assets/img/corporate/dealers-intro.jpg` |
| Custom | `/custom-equipment` | `/assets/img/corporate/custom-intro.jpg` |

**Markup class:** `.zpm-corp-page-lead.zpm-corp-intro` + `.zpm-corp-intro__grid` / `__media` / `__body`  
**CSS:** `assets/css/style.css` — block `SITE-002 — Corporate intro image blocks (zpm-corp-intro)`

---

## 3. SHA256 (post-deploy)

See [reports/corporate-intro-blocks-work/deploy-sha256.json](../reports/corporate-intro-blocks-work/deploy-sha256.json).

| File | post SHA256 |
|------|-------------|
| `style.css` | `d0da1d23a1a1bd50429bd3f3fefc1b863bdebe9b48d529d70670e7bb2fb4c0ea` |
| `about.twig` | `0b82280799eb318243c415d8acd638f9c60c710941cfa118d6eca4ac24fa9aa0` |
| `delivery.twig` | `1d3ba241c489e61cbfa781073e4d99c06c75a4324a6b5ad98a3d4387a5e421a4` |

---

## 4. Asset registry (TEST FTP)

| File | SHA256 | Bytes | HTTP |
|------|--------|-------|------|
| `about-intro.jpg` | `0729c3a0fd27973825d9681841a859d2c324c613f5084ee20afac01d8d60f85d` | 1 003 429 | 200 |
| `delivery-intro.jpg` | — | — | **404** |
| `payment-intro.jpg` | `c89bb396cc2b1f6dbfb969a2700cab5bfe84eb2824ff82daec308cf743702afa` | 962 586 | 200 |
| `warranty-intro.jpg` | `9cba7c87f517011445ea65ccf5f93a2654eeee41eed2ee10f114e1d784df4683` | 861 186 | 200 |
| `dealers-intro.jpg` | *(see deploy-manifest)* | 903 056 | 200 |
| `custom-intro.jpg` | *(see deploy-manifest)* | ~1 021 000 | 200 |

Local mirror: `reports/corporate-intro-blocks-work/assets/img/corporate/`

---

## 5. Rollback

| Item | Path |
|------|------|
| Script | [site-002-corp-intro-blocks-rollback.py](../reports/corporate-intro-blocks-work/site-002-corp-intro-blocks-rollback.py) |
| Backups | `backups/*.{pre-site-002-corp-intro-blocks-01.bak}` |

---

## 6. Report

[reports/SITE-002-CORPORATE-INTRO-BLOCKS-01.md](../reports/SITE-002-CORPORATE-INTRO-BLOCKS-01.md)

---

*Documentation only — live TEST evidence in deploy manifest. Verdict FAIL until `delivery-intro.jpg` uploaded.*
