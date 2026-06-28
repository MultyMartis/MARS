# SITE-002 — CORPORATE INTRO BLOCKS 01

**Task:** SITE-002 — Corporate intro image blocks implementation  
**Branch:** `mars/canonical-post-recovery`  
**Authority:** `SITE-002-STABLE-LIVE-UNIVERSAL-CORPORATE-CTA-01`  
**Live TEST:** https://zpm.new-site.space/  
**Deploy pass:** `site-002-corporate-intro-blocks-01`  
**Timestamp (UTC):** 2026-06-28T22:41:22Z  
**Verdict:** **FAIL** — markup/CSS/deploy **PASS** on 6 pages; **`delivery-intro.jpg` asset missing** (HTTP 404)

---

## 1. Safety

| Step | Result |
|------|--------|
| `git status` + `git rev-parse HEAD` | Pre: `7f5d7f23` |
| Checkpoint commit | `c658d560` — `checkpoint(site-002): before corporate intro image blocks implementation` |
| Production | **NOT TOUCHED** |
| Controllers / `main.js` | **NOT TOUCHED** |
| CTA / timelines / FAQ / forms | **NOT TOUCHED** |

---

## 2. Backups

Suffix: `.pre-site-002-corp-intro-blocks-01.bak`  
Directory: `projects/ocpilot/sites/site-002/backups/`

| Remote | Backup |
|--------|--------|
| `assets/css/style.css` | `assets__css__style.css.pre-site-002-corp-intro-blocks-01.bak` |
| `catalog/view/theme/default/template/information/about.twig` | `catalog__view__theme__default__template__information__about.twig.pre-site-002-corp-intro-blocks-01.bak` |
| `catalog/view/theme/default/template/information/delivery.twig` | `catalog__view__theme__default__template__information__delivery.twig.pre-site-002-corp-intro-blocks-01.bak` |
| `catalog/view/theme/default/template/information/payment.twig` | `catalog__view__theme__default__template__information__payment.twig.pre-site-002-corp-intro-blocks-01.bak` |
| `catalog/view/theme/default/template/information/guarantee.twig` | `catalog__view__theme__default__template__information__guarantee.twig.pre-site-002-corp-intro-blocks-01.bak` |
| `catalog/view/theme/default/template/information/dealers.twig` | `catalog__view__theme__default__template__information__dealers.twig.pre-site-002-corp-intro-blocks-01.bak` |
| `catalog/view/theme/default/template/information/custom_equipment.twig` | `catalog__view__theme__default__template__information__custom_equipment.twig.pre-site-002-corp-intro-blocks-01.bak` |

Preflight: [corporate-intro-blocks-work/preflight-manifest.json](corporate-intro-blocks-work/preflight-manifest.json)  
SHA256: [corporate-intro-blocks-work/deploy-sha256.json](corporate-intro-blocks-work/deploy-sha256.json)

---

## 3. Assets uploaded

| Asset | Local before deploy | FTP upload | HTTP QA |
|-------|---------------------|------------|---------|
| `about-intro.jpg` | Synced from TEST (1 003 429 B) | Re-uploaded | **200** |
| `delivery-intro.jpg` | **MISSING locally and on FTP** | **Skipped** | **404** |
| `payment-intro.jpg` | Synced (962 586 B) | Re-uploaded | **200** |
| `warranty-intro.jpg` | Synced (861 186 B) | Re-uploaded | **200** |
| `dealers-intro.jpg` | Synced (903 056 B) | Re-uploaded | **200** |
| `custom-intro.jpg` | Synced (1 021 xxx B) | Re-uploaded | **200** |

Local staging: `reports/corporate-intro-blocks-work/assets/img/corporate/`

---

## 4. Failed previous path swaps fixed

| Issue | Fix |
|-------|-----|
| About hero used `/assets/img/corporate/about-intro.jpg` | Restored hero to `/assets/img/about-page-img.jpg` |
| Custom OEM `.zpm-custom-oem__media` used `custom-intro.jpg` | Restored to `/assets/img/about-page-img.jpg` |
| Delivery/Payment/Warranty/Dealers had text-only lead | Converted to `.zpm-corp-intro` media+text grid |

---

## 5. Files changed (live TEST)

| Remote | pre → post SHA256 (trunc.) |
|--------|----------------------------|
| `about.twig` | `ee4af4df…` → `0b822807…` |
| `delivery.twig` | `dd966884…` → `1d3ba241…` |
| `payment.twig` | `1e507319…` → `058cfaa4…` |
| `guarantee.twig` | `e353f274…` → `f10dedc1…` |
| `dealers.twig` | `873f6f9e…` → `5b46fed2…` |
| `custom_equipment.twig` | `ed0c4075…` → `2c43e2e8…` |
| `style.css` | `5069589f…` → `d0da1d23…` |

---

## 6. Markup implemented

Pattern on M9.14–M9.18 + About:

```html
<section class="zpm-corp-page-lead zpm-corp-intro" aria-label="Вводная информация">
  <div class="container">
    <div class="zpm-corp-intro__grid">
      <div class="zpm-corp-intro__media">
        <img src="/assets/img/corporate/{page}-intro.jpg" alt="…" loading="lazy">
      </div>
      <div class="zpm-corp-intro__body zpm-corp-page-lead__body">…</div>
    </div>
  </div>
</section>
```

**About:** intro block inserted after hero; body = moved `zpm-about-company__text` paragraph (copy unchanged). Hero retains lead + trust + `about-page-img.jpg`.

**Other pages:** `{{ page_lead|raw }}` moved into intro body unchanged.

---

## 7. CSS added

Append block in `assets/css/style.css`: marker `SITE-002 — Corporate intro image blocks (zpm-corp-intro)`  
Source: [corporate-intro-blocks-work/zpm-corp-intro.css](corporate-intro-blocks-work/zpm-corp-intro.css)

- Desktop: grid `1fr 2fr`, gap `var(--pad-gap)`, radius `var(--radius-main)`, `object-fit: cover`
- Mobile ≤1024px: single column, image above text

---

## 8. QA

| Page | HTTP | `.zpm-corp-intro` | aria-label | Image path in HTML | Image HTTP |
|------|------|-------------------|------------|-------------------|------------|
| `/about` | 200 | ✓ | ✓ | `about-intro.jpg` | 200 |
| `/delivery` | 200 | ✓ | ✓ | `delivery-intro.jpg` | **404** |
| `/payment-methods` | 200 | ✓ | ✓ | `payment-intro.jpg` | 200 |
| `/guarantee` | 200 | ✓ | ✓ | `warranty-intro.jpg` | 200 |
| `/dealers` | 200 | ✓ | ✓ | `dealers-intro.jpg` | 200 |
| `/custom-equipment` | 200 | ✓ | ✓ | `custom-intro.jpg` | 200 |

Restoration checks: About hero **not** using `about-intro.jpg`; Custom OEM **not** using `custom-intro.jpg` — **PASS**.

Manifest: [corporate-intro-blocks-work/deploy-manifest.json](corporate-intro-blocks-work/deploy-manifest.json)

---

## 9. Rollback

`python projects/ocpilot/sites/site-002/reports/corporate-intro-blocks-work/site-002-corp-intro-blocks-rollback.py`

Restores all 6 Twig files + `style.css` from `.pre-site-002-corp-intro-blocks-01.bak`.

---

## 10. Stable checkpoint

**Name:** `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01`  
**Baseline:** [baselines/SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01.md)  
**Status:** **PARTIAL** — pending operator upload of `delivery-intro.jpg`

---

## 11. Git

| Step | Commit |
|------|--------|
| Pre | `c658d560` checkpoint |
| Post | *(this commit)* implementation + docs |

Push: `origin/mars/canonical-post-recovery`

---

## 12. Remaining HITL

1. **Operator:** place `delivery-intro.jpg` at `assets/img/corporate/` on TEST (local source was **not found** in repo or operator paths searched).
2. Re-run asset upload only or full deploy script after file is available.
3. Visual sign-off on 6 intro blocks (desktop 1440 / mobile 390).
4. Confirm About intro text placement (company paragraph moved from §02 head) — acceptable or adjust copy location only via explicit charter.

---

**Final verdict: FAIL** (single blocking asset: `delivery-intro.jpg`)
