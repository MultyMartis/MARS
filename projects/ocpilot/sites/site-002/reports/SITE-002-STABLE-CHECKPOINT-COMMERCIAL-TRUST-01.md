# REPORT — SITE-002 STABLE CHECKPOINT COMMERCIAL TRUST 01

**Project:** SITE-002 (ЗПМ / BZPM)  
**Date:** 2026-06-21  
**Prior authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`  
**New authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`  
**Mode:** Stable checkpoint registration — FTP live capture + documentation

---

## 1. New Authority State

| Field | Value |
|-------|--------|
| **Authority** | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| **Supersedes** | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| **Environment** | TEST — https://zpm.new-site.space/ |
| **Manual UI policy** | **CANONICAL** — operator CSS/Twig/UX edits on live TEST override pass reports and work copies |

---

## 2. Live Capture Summary

FTP read-only capture from `polygonws.beget.tech` at **2026-06-21T10:09:31Z**:

| File | Remote path | SHA256 |
|------|-------------|--------|
| `blockcommercialtrust.twig` | `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | `6bd6475e924ccc84a3591a91213b59cb4605de274f7bdf8fb18b3bec4ff855b9` |
| `style.css` | `assets/css/style.css` | `60f5bb61be84afabf5d2342944617e390a7a6a4e13bed22831e0fa29b79acd6d` |
| `category.php` | `catalog/controller/product/category.php` | `b4594c74dfc726c96df0cd222e161b6b9c06a702c8f819f6057af530d7049036` |

**Capture location:** [m9.8.9-commercial-trust-checkpoint-work/live-capture/](m9.8.9-commercial-trust-checkpoint-work/live-capture/)

**Findings vs M9.8.9-03C deploy report:**

| File | vs 03C deploy |
|------|---------------|
| `blockcommercialtrust.twig` | **Changed** — operator manual polish (podium cert, 3 OEM benefits, FAQ section split, decor logo, updated copy) |
| `style.css` | **Changed** — operator CSS polish (podium, enlarged cert, form card, FAQ grid, logo contours) |
| `category.php` | **Unchanged** — SHA256 identical to 03C post-deploy |

---

## 3. Registered Manual Changes

Live TEST Commercial Trust block (category PLP) — **canonical**:

| Area | Registered state |
|------|------------------|
| **Certificate** | Enlarged (`max-width: 250px`); displayed on podium base (`sert-base.jpg`); single visible slide; Fancybox on cert click |
| **Composition** | Two-column wrap: info column (header + cert + benefits) + form column; FAQ in separate `zpm-catalog-faq` section |
| **OEM benefits** | 3 items with `fad` icons in 110px circles — собственное производство · документы для закупки · российское производство / «Сделано в России» |
| **Lead copy** | Updated lead paragraph — подбор, расчёт стоимости, КП, комплектация проекта |
| **Form** | Title «Получить прайс-лист»; `dialog=7`; backdrop-blur card; `zpm-decoration-with-logo` with `decor-logo.svg` background contours |
| **FAQ grid** | 8 service cards (4×2 desktop, 2×4 ≤1024px) under «Частые вопросы» |
| **Dynamic H2** | From `category.php` → `commercial_trust_heading` (5 mapped categories + fallback) |
| **Visual balance** | Operator spacing, icon hover states, form shadow, cert-col padding — manual CSS polish |

**Out of scope (unchanged):** homepage certificates slider, `/katalog`, PDP, filters, product grid, 1C, price logic, `main.js`.

---

## 4. Knowledge Map Updates

**File:** [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)

| Change | Content |
|--------|---------|
| **§14 Commercial Trust Block** | **Added** — purpose, structure, files, dynamic headings, certificate, form, FAQ grid, change rules |
| **§1 Authority** | Updated to `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| **§8 Live Files** | Extended with commercial-trust files |
| **§13 PRE-TASK RULE** | Added domain-specific rule for trust block / certificates / dealers form / category CTA |

---

## 5. Updated Files

| File | Change |
|------|--------|
| `baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md` | **created** |
| `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | §14 + authority + PRE-TASK update |
| `site-passport.md` | authority, status, commercial trust scope |
| `README.md` | authority, active checkpoint |
| `../../OCPILOT-STATE.md` | SITE-002 state |
| `../../OPERATIONAL-INDEX.md` | Run **4.144** |
| `reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/*` | **created** — FTP capture |
| `reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md` | **created** — this report |

---

## 6. Stable Baseline Contents

Registered as part of authority state:

- Filter Recovery (06D–06M)
- Filter UX (04–08A)
- Wishlist Tooltips (01)
- M9.8.1 / M9.8.2 / M9.8.5
- Commercial Trust redesign (03B design · 03C deploy)
- **Operator manual Commercial Trust polish** (post 03C — live canonical)

---

## 7. Operational Rules Updates

**PRE-TASK RULE (new domain):** Before any task touching **trust block**, **certificates**, **dealers form**, or **category CTA**:

1. Read Knowledge Map **§14 Commercial Trust Block**
2. Read latest stable checkpoint — `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`
3. Live-capture `blockcommercialtrust.twig`, `style.css`, `category.php` before deploy

**Explicitly not addressed in this registration:**

- limit + filter persistence
- page-intro__description

---

## 8. Git Result

Commit and push requested — see git output in task closeout.

---

## 9. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact date of each operator manual edit post 03C | **SAFE UNKNOWN** — live capture proves current state only |
| Fancybox group completeness (hidden certificat_01) | **Removed from live twig** — single cert link only; verify if multi-cert gallery needed |
| Form POST end-to-end on live | **Not auto-tested** in this registration |
| `data-dealers` / `zpm-dealers` hooks | **Removed from main section** on live — verify JS dependencies if dealers form behaviour regresses |
| Full certificate inventory on FTP | **SAFE UNKNOWN** — see BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH |

---

*Registration complete — awaiting next task.*
