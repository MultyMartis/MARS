# I-SEO Report Hub — i-SEO Brand Style Discovery v0.1

**Status:** DISCOVERY ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-07  
**Wave:** UI Screenshot QA, Brand Style and Nikita Templates Discovery 01  
**Live site (read-only):** `https://i-seo.su`

---

## 1. Sources inspected

| Source | Path / URL | Result |
|--------|------------|--------|
| Site-ops programme | `X:\AI MARS\projects\iseo-su-site-ops\` | Theme `iseoblog`; shared `css/`; WPilot binding docs; **no** dedicated Report Hub palette file |
| Local CSS scratch (prod copy) | `projects/iseo-su-site-ops/_glossary-scratch/layout-fix/prod-css__main.css` (+ `prod-css__media.css`) | **Usable token extraction** |
| Theme baseline CSS | `projects/iseo-su-site-ops/_glossary-scratch/theme-baseline/style.css` | Partial WP theme CSS; yellow accent cues |
| WP inventory | `ISEO-SU-WORDPRESS-INVENTORY-v1.md` | Theme **iseoblog**; site title INTLSEO Studio |
| Remote FS inventory | `ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md` | Shared assets `css/`, `js/`, theme path |
| Demo Report Hub CSS | `workspaces/website-factory-operations/iseo-report-hub-prototype/assets/css/styles.css` | Current hub inspiration: red `#c8102e` |
| Live Report Hub CSS | `projects/iseo-report-hub/app-source/public/assets/css/app.css` | Same red shell tokens post-Impl 02 |
| Live public site | `https://i-seo.su/` + `css/main.css` + `css/media.css` | Read-only fetch; confirmed yellow/dark system |
| `X:\AI MARS\local\sites\iseo-su-production` | — | Present in tree listing earlier; **contents not readable here** (ignore/filter) — treat as SAFE UNKNOWN for this wave |
| WPilot project | `projects/wpilot/` | Binding/ops docs; **not** a brand token store |

**Not done:** WordPress Admin login, theme file mutation, SFTP download beyond existing scratch, production writes.

---

## 2. Brand identity (public)

| Signal | Value |
|--------|-------|
| Public brand | INTLSEO / i-seo.su |
| Marketing site model | Custom dark landing + shared CSS (`css/main.css`), WordPress `iseoblog` for content routes |
| Typography | **Manrope** (Google Fonts `family=Manrope:wght@200..800`) |
| Visual mood | Dark UI, high-contrast yellow CTA, pill buttons |

---

## 3. Extracted tokens (practical)

### 3.1 Colors

| Token role | Live i-seo.su evidence | Report Hub today (Impl 02) | Gap |
|------------|------------------------|----------------------------|-----|
| **Primary / CTA accent** | `#facc15` / `#FACC15` (also `#ffcc00`, rating `#FDCD3E`) | `#c8102e` / `#a00d25` | **Mismatch** — hub red ≠ site yellow |
| **Accent soft** | Yellow on dark (no soft pink) | `#fff0f2` | Replace when retokening |
| **Page / dark surface** | `#181818`, `#18181B`, `#1A1A1D`, `#212121`, `#212123`, `#27272A`, `#282828` | Sidebar `#1f2a3a`; main `#f5f6f8` | Hub is light-main admin shell; site is dark marketing |
| **Text on dark** | `#fff` | `#e2e8f0` / `#fff` in sidebar | Close enough |
| **Text on light / on yellow CTA** | `#000` on `#facc15` buttons | Dark text on light panels | Keep light panels for hub readability |
| **Muted** | `#666` / `#666666` / `#777` | `#374151` | Align optionally |
| **Border** | White/light borders on dark; yellow `#ffcc00` accents | `#e5e7eb` | Keep light borders for hub cards |
| **Danger / alert** | `#f77` appears | `#dc2626` | Keep hub semantic status colors |

### 3.2 Typography

| Item | Value |
|------|-------|
| Primary font | `"Manrope", sans-serif` |
| Hub today | System stack (Segoe UI / Roboto / Arial) |
| Recommendation | Load Manrope for hub UI (CDN or self-host later); do **not** import full WP CSS |

### 3.3 Components

| Pattern | i-seo.su | Hub today | Recommendation |
|---------|----------|-----------|----------------|
| Primary button | `#facc15` bg, `#000` text, **pill** `border-radius: 100px` | Red fill, radius ~8px | Adopt yellow CTA + darker hover; optional pill or 999px for primary only |
| Cards / panels | Often `border-radius: 16px` on dark surfaces | 8px white cards | Increase to 12–16px; keep white cards for admin density |
| Sidebar | N/A (marketing top chrome) | Dark slate + red active | Keep sidebar IA; retoken accent to yellow; optional darker `#18181B` |
| Section numbers | Marketing numbered blocks | Demo-like `01` headings | Keep; retoken accent |
| Shadows | Subtle / flat dark UI | `--shadow-sm/md` | Keep light shadows for white cards |

---

## 4. Recommendation

1. **Do not import** full `css/main.css` / WordPress theme CSS into Report Hub.  
2. **Create a dedicated Report Hub brand layer** in `app.css` `:root` tokens mapped from i-seo.su.  
3. **Replace** demo red `#c8102e` with **i-seo yellow `#facc15`** as primary accent for buttons, active nav, links (with accessible dark text on yellow buttons).  
4. **Keep** light main content + dark sidebar shell (admin UX), even though marketing site is mostly dark — do not force a full dark admin theme in Impl 03 unless operator insists.  
5. **Optional:** darken sidebar toward `#18181B` to feel closer to i-seo.su without losing readability.  
6. **Adopt Manrope** for headings + UI text.  
7. Treat `#c8102e` as **legacy demo accent**, not live brand truth.

### Decision summary

| Option | Verdict |
|--------|---------|
| Use exact i-seo colors for accent/font | **Yes** (yellow + Manrope) |
| Keep demo shell layout | **Yes** (sidebar + light main) |
| Import full WordPress CSS | **No** |
| Dedicated brand layer | **Yes** — Impl 03 |

---

## 5. Suggested `:root` draft (for Impl 03 — not applied now)

```css
--color-accent: #facc15;
--color-accent-hover: #eab308; /* SAFE UNKNOWN exact hover — derive in Impl 03 */
--color-accent-ink: #000000;   /* text on yellow CTA */
--color-accent-soft: #fef9c3;
--sidebar-bg: #18181b;
--color-bg: #f5f6f8;           /* keep light admin canvas */
--font: "Manrope", system-ui, sans-serif;
--radius: 12px;
--radius-pill: 100px;
```

Hover yellow exact value: **SAFE UNKNOWN** until Impl 03 samples hover states from live CSS/JS.

---

## 6. SAFE UNKNOWN

- Exact hover/focus yellow variants and all button class names on live site.  
- Whether operator wants **full dark admin** vs **light admin + yellow accent** (recommended: latter).  
- Fonts licensing / self-host vs Google Fonts CDN for production later.  
- Local production mirror CSS under `local/sites/iseo-su-production` (path filtered / not inspected this wave).  
- Whether INTLSEO logo mark asset should replace text `INTLSEO` in sidebar (asset path not extracted).
