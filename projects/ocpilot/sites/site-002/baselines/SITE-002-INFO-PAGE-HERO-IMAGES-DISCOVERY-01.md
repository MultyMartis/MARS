# SITE-002 — Info Page Hero Images Discovery 01 (baseline)

**Baseline name:** `SITE-002-INFO-PAGE-HERO-IMAGES-DISCOVERY-01`  
**Site:** SITE-002 · ЗПМ · `https://bzpm.ru/`  
**Registered:** 2026-07-12  
**Mode:** read-only discovery (0 Production mutations)  
**Status:** **COMPLETE — PARTIAL** (restore executed in Run 4.263)

---

## 1. Authority

| Item | Value |
|------|--------|
| Operation | `SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01` |
| Report | [SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01.md](../reports/SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01.md) |
| Pattern parent | `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01` (TEST-era) |
| Follow-on restore | `SITE-002-PROD-INFO-PAGE-HERO-IMAGES-RESTORE-01` (Run 4.263) |

---

## 2. Discovery facts (frozen)

| URL | Intro markup at discovery | Asset HTTP |
|-----|---------------------------|------------|
| `/custom-equipment` | present | 200 |
| `/payment-methods` | present | 200 |
| `/delivery` | **absent** (text-only lead) | 200 (`delivery-intro.jpg` unused) |
| `/dealers` | present | 200 |
| `/guarantee` | present | 200 |

| Asset | Production |
|-------|------------|
| Path | `/assets/img/corporate/delivery-intro.jpg` |
| HTTP | 200 · `image/jpeg` · 1672×941 |
| SHA256 | `c89bb396cc2b1f6dbfb969a2700cab5bfe84eb2824ff82daec308cf743702afa` |

| CSS | Production |
|-----|------------|
| Marker | `SITE-002 — Corporate intro image blocks (zpm-corp-intro)` **present** |
| Layout | desktop `1fr 2fr`; ≤1024 stacked |

**Cause:** delivery-summary restyle left text-only lead; CSS and asset remained.

**Recommended restore:** Option A — selective twig lead restore only (no asset/CSS upload).

---

## 3. Post-discovery disposition

Restore Run **4.263** closed the `/delivery` markup gap. This baseline remains the discovery evidence record; it is **not** a new Production stability checkpoint.
