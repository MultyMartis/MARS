# REPORT — SITE-002 STABLE CHECKPOINT OPERATOR MANUAL POLISH 01

**Project:** SITE-002 (ЗПМ / BZPM)  
**Task:** SITE-002 — Operator Manual Polish Canonical Checkpoint  
**Environment:** TEST only — https://zpm.new-site.space/  
**Date:** 2026-06-29  
**Mode:** Read-only capture + documentation — **no** live deploy · **no** visual changes · **no** code edits on TEST  
**Prior checkpoint:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2`  
**New authority:** `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01`

---

## 1. Safety

| Item | Value |
|------|--------|
| **Repository** | `C:\MARS Phenix\AI MARS` |
| **Branch** | `mars/canonical-post-recovery` |
| **HEAD (pre-work)** | `f696beeed57eba9ea0f72ec03159fed7c0860bd7` |
| **Pre-work checkpoint commit** | `8ffe77d7` — `checkpoint(site-002): before operator manual polish canonical checkpoint 01` |
| **Operator Beget backup** | **CONFIRMED** |
| **Production** | **NOT TOUCHED** |
| **Live TEST writes** | **NONE** — FTP read-only capture only |

---

## 2. Authority registration

Starting from this checkpoint:

| Rule | Value |
|------|--------|
| Operator manual CSS | **Authority** |
| Operator manual HTML/Twig | **Authority** |
| Operator manual JS | **Authority** |
| **Forbidden reference** | Pass 1.2 CSS/HTML/JS as baseline for future tasks |
| **Sole baseline** | `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` |

No correctness analysis performed on operator edits.

---

## 3. FTP capture

**Script:** [site-002-operator-manual-polish-capture.py](site-002-operator-manual-polish-01-work/site-002-operator-manual-polish-capture.py)  
**Manifest:** [capture-manifest.json](site-002-operator-manual-polish-01-work/capture-manifest.json)  
**Live capture dir:** [live-capture/](site-002-operator-manual-polish-01-work/live-capture/)  
**Captured at (UTC):** 2026-06-28T18:40:54.796410+00:00

### 3.1 Files captured (19)

| Remote path | SHA256 | Bytes |
|-------------|--------|-------|
| `assets/css/style.css` | `1d190d97953cfaab17bb1f9948e0eecafb777710d7c1ba613a35181b28e88a86` | 379934 |
| `assets/js/main.js` | `17cb1fffe8831d4ac633d5bd41e047c31b4fd478a0e1cfa67c8667c42ab539e8` | 204187 |
| `catalog/controller/information/about.php` | `77ac5ea35be5863f5c729c996743a8f8cd18af3e9afca328d4dcde7585b5fa8a` | 1687 |
| `catalog/view/theme/default/template/information/about.twig` | `998321d3b3ea0a119b0aa688d9c6ebbcdc31431ced75110450026d24458202f8` | 3443 |
| `catalog/controller/information/delivery.php` | `df48a823bdea367b4deb7042e5b46cc6349a1c295caf637cf84fbb7038b383c1` | 3237 |
| `catalog/view/theme/default/template/information/delivery.twig` | `6db8da22c7e449a2fe8fdd5aa121f403808bd5a3099dc164f9b1962fe80ed234` | 51331 |
| `catalog/controller/information/payment.php` | `44516f1ebd21778b7ba14d8d517f4e8b24451c8b6997e484291b7b5d1633ff8a` | 3441 |
| `catalog/view/theme/default/template/information/payment.twig` | `d878062c675f9e76a65d3ab0db25483bee4af959d117b37f318061df600cb1c7` | 33699 |
| `catalog/controller/information/guarantee.php` | `4e525e71c666d2f87595019c3e72572135806eb548b814e4edea20ea76f3cb3e` | 3794 |
| `catalog/view/theme/default/template/information/guarantee.twig` | `cc9dd9863aadf7e6ea386eda0b2837a13a9462a9176281d264131936b79e8365` | 44953 |
| `catalog/controller/information/dealers.php` | `b8988dd740859f2dc56ae53b44ea32c83d9851b5dcb2c22364cf1b8829ed96f7` | 3164 |
| `catalog/view/theme/default/template/information/dealers.twig` | `ecc6dc8b06faa8f9691edb02b6c10cee6eec22982d7d34275e163c3cd7370b5c` | 45886 |
| `catalog/controller/information/custom_equipment.php` | `e4fdffc8e3f5caf6a023d7eb2920b0fd5b736179353a5db2e566b237ffff41e5` | 3431 |
| `catalog/view/theme/default/template/information/custom_equipment.twig` | `59fcaca9f319dfe9301ce9190e898883f0854cd47a8c00e3ebc2cf92e26616a5` | 66791 |
| `catalog/view/theme/default/template/product/producthero.twig` | `2ac446502f53d758556c727ae505f2154c20d70b816de544b3087fcfe821e7d5` | 12178 |
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | `6bd6475e924ccc84a3591a91213b59cb4605de274f7bdf8fb18b3bec4ff855b9` | 13276 |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | `05550c752dfabd616ce4d02be8188dac34caf39c60c3e97c7c5aed1f696a040a` | 19158 |
| `catalog/controller/product/category.php` | `05bf86805989471c411a27d07fdc7bd5216a090b0592c5e4407d8aedd0040db2` | 23067 |
| `catalog/model/catalog/product.php` | `66ad19e4e0211973214d72dcb8aef6af3cd4a9be2e343b5e5e9ecd27e7168d00` | 59651 |

---

## 4. Delta vs Pass 1.2

Pass 1.2 deployed **CSS only** — post-deploy SHA256 `243d6d5e2a1ad00c06c450f4b90dc72adb1671b64a681f266675abdbd9330252` ([Pass 1.2 baseline](../baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md)).

| File | Pass 1.2 state | Live TEST (this checkpoint) | Operator manual change |
|------|----------------|----------------------------|------------------------|
| `assets/css/style.css` | `243d6d5e…` (378470 B) | `1d190d97…` (379934 B) | **YES** |
| `catalog/view/theme/default/template/information/dealers.twig` | `e2a7edb4…` (Pass 1.1 deploy snapshot) | `ecc6dc8b…` | **YES** |
| `assets/js/main.js` | Not deployed in Pass 1.2 | `17cb1fff…` | Captured as authority — Pass 1.2 did not track JS |
| All other captured corp twig/php | Same as Pass 1.1 deploy snapshots | Unchanged at capture | **NO** (vs deploy snapshots) |

**Repo sync:** live `style.css` → `reports/site-002-visual-polish-pass1.2-work/style.css`; live `dealers.twig` → `reports/site-002-visual-polish-pass1.1-work/dealers.twig`.

Diff evidence: [diff-vs-pass12.json](site-002-operator-manual-polish-01-work/diff-vs-pass12.json)

---

## 5. Backups created

All files saved under `projects/ocpilot/sites/site-002/backups/` with suffix `.pre-site-002-operator-manual-polish-01.bak`:

| Backup file |
|-------------|
| `assets__css__style.css.pre-site-002-operator-manual-polish-01.bak` |
| `assets__js__main.js.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__information__about.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__information__about.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__information__delivery.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__information__delivery.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__information__payment.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__information__payment.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__information__guarantee.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__information__guarantee.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__information__dealers.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__information__dealers.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__information__custom_equipment.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__information__custom_equipment.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__product__producthero.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__sections__blockcommercialtrust.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__view__theme__default__template__sections__filterssidebar.twig.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__controller__product__category.php.pre-site-002-operator-manual-polish-01.bak` |
| `catalog__model__catalog__product.php.pre-site-002-operator-manual-polish-01.bak` |

---

## 6. Page verification (HTTP)

| Page | URL | Status |
|------|-----|--------|
| Home | https://zpm.new-site.space/ | **200 PASS** |
| About | https://zpm.new-site.space/about | **200 PASS** |
| Delivery | https://zpm.new-site.space/delivery | **200 PASS** |
| Payment | https://zpm.new-site.space/payment-methods | **200 PASS** |
| Warranty | https://zpm.new-site.space/guarantee | **200 PASS** |
| Dealers | https://zpm.new-site.space/dealers | **200 PASS** |
| Custom Manufacturing | https://zpm.new-site.space/custom-equipment | **200 PASS** |
| Catalog | https://zpm.new-site.space/katalog/ | **200 PASS** |
| PDP (sample) | https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-standart/stoly-standart-600-s-polkoy-reshetkoy/stol-proizvodstvennyy-spb-s-17-6-1700h600h850 | **200 PASS** |

---

## 7. Documentation updated

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md` | **created** — new stable baseline |
| `baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md` | **SUPERSEDED** marker |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | §1 authority + **§26 Operator Manual Polish 01** |
| `site-passport.md` | authority checkpoint |
| `README.md` | active checkpoint |
| `../../OCPILOT-STATE.md` | SITE-002 focus |
| `../../OPERATIONAL-INDEX.md` | Run **4.161** |
| `reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md` | **created** — this report |

---

## 8. Stable checkpoint

**Registered:** `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01`

All future SITE-002 tasks (local fonts, new About, CTA, intro blocks, Home, PDP body classes, etc.) **must** start from this checkpoint only.

---

## 9. Git

| Item | Value |
|------|--------|
| Pre-work checkpoint | `8ffe77d7` |
| Final commit | `989ba31e` — `feat(site-002): register operator manual polish canonical checkpoint 01` |
| Push | **DONE** — `origin/mars/canonical-post-recovery` |
| Live TEST changes | **NONE** |

---

## 10. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Pixel-level HITL / screenshots | **SAFE UNKNOWN** — HTTP-only verification |
| Console errors | **SAFE UNKNOWN** |
| Exact operator edit timestamps per file | **SAFE UNKNOWN** — forensic diff only |
| Which main.js edits belong to this polish session vs earlier operator passes | **SAFE UNKNOWN** — live state registered as authority without session attribution |

---

## 11. SECURITY RISK

FTP credentials exist in operator-local capture scripts (`site-002-operator-manual-polish-capture.py`) — same pattern as prior M9.x deploy work copies. **Not** for public redistribution.

---

*Read-only capture — live TEST unchanged. Operator manual edits registered as canonical authority.*
