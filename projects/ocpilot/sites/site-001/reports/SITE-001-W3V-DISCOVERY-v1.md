# SITE-001 W3-V Discovery v1

**Type:** Pre-execution discovery — read-only + FTP inventory + backup  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3-V — Visual Layer Refresh (CSS-only)

---

## Executive summary

Primary visual system lives in **`css/main.css`** (6 784 lines, 104 KB) and **`css/media.css`** (2 192 lines, 30 KB). Styles are **not tokenized** — dominant `border-radius: 4px` (68 hits in main.css), minimal shadows (20 rules), hardcoded brand reds. W3-V will apply **CSS-only** token layer and override block — **no twig/markup changes**.

**Evidence (local, not git):** `.recovery-temp/site-001-w3v-discovery.json` · backup `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3v-20260609-0327\`

---

## 1. File inventory

| File | Remote path | Lines | Bytes | Role |
|------|-------------|-------|-------|------|
| **main.css** | `css/main.css` | 6 784 | 104 417 | Global layout, buttons, forms, cards, PDP, homepage |
| **media.css** | `css/media.css` | 2 192 | 30 330 | Responsive breakpoint overrides |

**Out of W3-V scope:** all `.twig` templates, `footer.twig`, header structure, JS, third-party widgets.

---

## 2. Visual style groups (pre-change baseline)

### 2.1 Border radius

| Metric | main.css | media.css |
|--------|----------|-----------|
| `border-radius: 4px` | **68** | 0 |
| `border-radius: 12px` | 0 | 0 |

**Assessment:** Legacy sharp/compact look — uniform 4px dominant.

### 2.2 Shadows

| Metric | main.css | media.css |
|--------|----------|-----------|
| `box-shadow` rules | **20** | 1 |

**Assessment:** Minimal elevation; red-tinted glow on form focus/hover (`0 0 10px rgb(170,3,3)`).

### 2.3 Component selector map

| Group | Key selectors | Rule hits (approx) |
|-------|---------------|-------------------|
| **Buttons** | `.callback_btn`, `.home_slider_btn`, `.phone_btn`, `.whatsapp_btn`, `.car_main_info__btns > a` | 5+ callback; 44 total button family |
| **Forms** | `input[type="text"]`, `textarea`, `.form_item`, `.popup__FORM_wrap` | 28 input rules |
| **Catalog cards** | `.catalog_item`, `.catalog_item__price_main` | 71 catalog_item hits |
| **Advantage cards** | `.new_car_bonus__item` | Bonus blocks on new-car surfaces |
| **Bank cards** | `.partner_banks__item` | Partner bank slider |
| **Information cards** | `.fancy_two_blocks__item`, `.reviews__item > .inner` | About/info/reviews |
| **Price hierarchy** | `.catalog_item__price_main`, `.car_main_info__price_main` | 20px / default PDP price |

---

## 3. W3-V planned changes (CSS-only)

| Target | Pre-change | W3-V target |
|--------|------------|-------------|
| Small elements radius | 4px | **8px** (`--w3v-radius-sm`) |
| Large blocks radius | 4px | **12px** (`--w3v-radius-lg`) |
| Buttons radius | 4px | **8–10px** (`--w3v-radius-md`) |
| Shadows | Minimal / red glow | Soft restrained (`--w3v-shadow-sm/md/cta`) |
| Button sizing | 50px height, tight padding | 48px height, 24px horizontal padding |
| Form focus | Heavy red glow | Focus ring `--w3v-shadow-focus` |
| Card hover | Light shadow | `--w3v-shadow-hover` + subtle translate |
| Price hierarchy | 20px catalog price | **22px/600** catalog; **34px/600** PDP |

**Implementation method:** Extend `:root` with W3-V tokens; append marked override block at end of `main.css` + responsive block in `media.css`.

---

## 4. HTTP pre-check (read-only)

| URL | HTTP | Forms | CTA present |
|-----|------|-------|-------------|
| `/` | 200 | YES | YES |
| `/about` | 200 | YES | YES |
| `/contact/` | 200 | YES | YES |
| `/cars/` | 200 | YES | YES |
| `/auto/` | 200 | YES | YES |

---

## 5. Preserved elements (must not change)

- All HTML structure, block order, texts, navigation
- Footer/header markup (post-W3-C rollback baseline)
- Brand colors: primary `rgb(170, 3, 3)`, hover `rgb(200, 0, 0)`
- WhatsApp green accent
- Form fields and business logic
- OpenCart functionality

---

## 6. Risk notes

| Risk | Mitigation |
|------|------------|
| Layout shift from hover translate | `translateY(-2px)` on cards only; disabled on mobile |
| Specificity conflicts | End-of-file override block; marked for rollback |
| W3-C lesson — structural rejection | **Zero twig edits** in W3-V |
| Cache stale CSS | Admin system + modification cache clear post-upload |

---

## 7. Authorization prerequisites

| Artefact | Status |
|----------|--------|
| W3-V write charter | [SITE-001-W3V-WRITE-CHARTER-v1.md](SITE-001-W3V-WRITE-CHARTER-v1.md) — **ACTIVE** |
| Change request | CR-SITE-001-W3V-2026-06-09 — **READY** |
| Rollback plan | [SITE-001-W3V-ROLLBACK-PLAN-v1.md](SITE-001-W3V-ROLLBACK-PLAN-v1.md) |
| Pre-write backup | `pre-w3v-20260609-0327` — **DONE** |
