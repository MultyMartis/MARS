# SITE-001 W3V2 Discovery v1

**Type:** Pre-execution discovery — read-only + HTTP inventory + backup  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3V2 — Visual Identity Refresh (CSS-only)

---

## Executive summary

Primary visual system remains in **`css/main.css`** (7 146 lines, 112 KB post-W3UX-C1) and **`css/media.css`** (2 229 lines, 31 KB). Prior waves **W3-V** (radius/shadow/spacing) and **W3UX-C1** (used catalog density) are active. W3V2 adds a **unified color + depth identity layer** — graphite surfaces, richer brand red, soft neutral backgrounds — **without** twig/markup/structure changes.

**Evidence (local, not git):** `.recovery-temp/site-001-w3v2-discovery.json` · backup `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3v2-20260609-0451\`

---

## 1. File inventory

| File | Remote path | Lines | Bytes | Role |
|------|-------------|-------|-------|------|
| **main.css** | `css/main.css` | 7 146 | 112 140 | Global layout, buttons, forms, cards, PDP, homepage + W3-V + W3UX-C1 blocks |
| **media.css** | `css/media.css` | 2 229 | 31 145 | Responsive overrides + W3-V + W3UX-C1 blocks |

**Out of W3V2 scope:** all `.twig`, PHP, JS, DB, SEO, routes, forms logic, header/footer structure.

---

## 2. Active token layers (pre-W3V2)

### 2.1 W3-V tokens (`:root`)

| Token | Value |
|-------|-------|
| `--w3v-space-xs` … `--w3v-space-xl` | 8–32px spacing scale |
| `--w3v-radius-sm/md/lg` | 8 / 10 / 12px |
| `--w3v-shadow-sm/md/hover/cta/focus` | Soft neutral + red-tinted shadows |
| `--swiper-theme-color` | `rgb(170, 3, 3)` |

### 2.2 W3UX-C1 tokens (`:root`)

| Token | Value |
|-------|-------|
| `--w3ux-space-xs` … `--w3ux-space-lg` | Density spacing |
| `--w3ux-card-img-max-h` | `180px` |

---

## 3. Color token map (baseline)

### 3.1 Top literals in `main.css`

| Color | Hits | Role |
|-------|------|------|
| `rgb(255, 255, 255)` | **73** | Card/surface white |
| `rgb(170, 3, 3)` | **56** | Brand red primary |
| `rgb(33, 36, 43)` | **48** | Dark sections (`#21242B`) |
| `rgb(200, 0, 0)` | **30** | Brand red hover / links |
| `rgb(208, 208, 208)` | **24** | Card borders |
| `rgb(246, 248, 250)` | **11** | Tag/badge surfaces |
| `rgb(14, 15, 16)` | **3** | Footer harsh borders |
| `#aa0303` | **1** | Credit slider accent |

### 3.2 Red accents (all variants)

| Color | Hits |
|-------|------|
| `rgb(170, 3, 3)` | 56 |
| `rgb(200, 0, 0)` | 30 |
| `rgba(170, 3, 3, …)` | 4 |
| `#aa0303` | 1 |

**Assessment:** Brand red is recognizable but flat; hover red is bright. W3V2 target: slightly richer/deeper primary.

### 3.3 Dark backgrounds

| Color | Hits | Usage |
|-------|------|-------|
| `rgb(33, 36, 43)` | **48** | Footer, nav, contacts, credit blocks, carousel chrome |
| `#21242b` | 2 | Marquee gradient |
| `rgb(14, 15, 16)` | 3 | Footer top/bottom borders (near-black) |
| `rgba(33, 36, 43, …)` | 6 | Overlays |

**Assessment:** Harsh black-adjacent feeling — W3V2 shifts large surfaces to **premium graphite** `#2B2F38`.

### 3.4 Card surfaces

| Selector family | Rest surface | Border | Shadow (post-W3-V) |
|-----------------|-------------|--------|-------------------|
| `.catalog_item > a/div` | `#fff` | `rgb(208,208,208)` | `--w3v-shadow-sm` |
| `.partner_banks__item` | `#fff` | none | `--w3v-shadow-sm` |
| `.new_car_bonus__item` | `#fff` | none | `--w3v-shadow-sm` |
| `.fancy_two_blocks__item` | `#fff` | none | `--w3v-shadow-sm` |
| `.reviews__item > .inner` | `#fff` | none | `--w3v-shadow-sm` |

### 3.5 Borders

| Pattern | Hits | Notes |
|---------|------|-------|
| `border-radius: 4px` (legacy) | **68** | Pre-W3-V base rules |
| `1px solid rgb(208, 208, 208)` | ~24 | Catalog card borders — flat grey |
| Footer `border-top/bottom: 10px solid rgb(14,15,16)` | 2 | Heavy near-black separation |

### 3.6 Shadows

| Metric | main.css | media.css |
|--------|----------|-----------|
| `box-shadow` rules | **38** | 1 |
| W3-V token shadows | 5 tokens | responsive hover disable |

**Assessment:** W3-V added soft shadows; W3V2 refines to layered graphite-tinted depth.

### 3.7 Button styles

| Class family | Fill | Hover | Radius (W3-V) |
|--------------|------|-------|---------------|
| `.callback_btn`, `.home_slider_btn` | `rgb(170,3,3)` | `rgb(200,0,0)` | `--w3v-radius-md` |
| `.phone_btn` | primary red | CTA shadow | `--w3v-radius-md` |
| `.whatsapp_btn` | green accent | preserved | `--w3v-radius-md` |
| `.form_item > .submit` | primary red | CTA shadow | `--w3v-radius-md` |

### 3.8 Hover states

| Area | Current |
|------|---------|
| Links | `rgb(200,0,0)` on hover |
| Cards | `--w3v-shadow-hover` + `translateY(-2px)` |
| Buttons | Background brighten + `--w3v-shadow-cta` |
| Forms | Red border + `--w3v-shadow-focus` |

---

## 4. W3V2 planned token system

| Token | Pre-change | W3V2 target |
|-------|------------|-------------|
| Brand Red | `rgb(170, 3, 3)` | `rgb(158, 2, 2)` — richer, deeper |
| Brand Red Hover | `rgb(200, 0, 0)` | `rgb(186, 0, 0)` |
| Dark Main | `rgb(33, 36, 43)` | `#2B2F38` graphite |
| Dark Secondary | — | `#363B46` |
| Surface | `#fff` / default | `#F7F8FA` body; `#FFFFFF` cards |
| Surface Alt | `rgb(246,248,250)` | `#EFF1F4` |
| Border | `rgb(208,208,208)` | `#D5DAE2` / `rgba(43,47,56,0.10)` |
| Text Main | `rgb(18,18,43)` / `rgb(33,36,43)` | `#2B2F38` |
| Text Secondary | ad-hoc | `#5C6370` |
| Shadow Small/Med/Large | W3-V neutral | Layered graphite depth |

**Implementation:** Extend `:root` with `--w3v2-*` tokens; append marked override block; bridge `--w3v-shadow-*` → `--w3v2-shadow-*`.

---

## 5. HTTP pre-check (read-only)

| URL | HTTP | Forms | CTA |
|-----|------|-------|-----|
| `/` | 200 | YES | YES |
| `/about` | 200 | YES | YES |
| `/contact/` | 200 | YES | YES |
| `/cars/` | 200 | YES | YES |
| `/auto/` | 200 | YES | YES |
| `/cars/bmw/` | 200 | YES | YES |
| `/auto/haval/` | 200 | YES | YES |

---

## 6. Preserved elements

- Twig/HTML structure, block order, texts, navigation
- W3UX-C1 density rules (`.used_catalog` scoped)
- W3-V radius/spacing tokens
- WhatsApp green accent
- Form fields and business logic
- OpenCart functionality

---

## 7. Authorization prerequisites

| Artefact | Status |
|----------|--------|
| W3V2 write charter | [SITE-001-W3V2-WRITE-CHARTER-v1.md](SITE-001-W3V2-WRITE-CHARTER-v1.md) — **ACTIVE** |
| Change request | CR-SITE-001-W3V2-2026-06-09 — **READY** |
| Rollback plan | [SITE-001-W3V2-ROLLBACK-PLAN-v1.md](SITE-001-W3V2-ROLLBACK-PLAN-v1.md) |
| Pre-write backup | `pre-w3v2-20260609-0451` — **DONE** |
