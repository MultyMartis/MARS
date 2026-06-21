# SITE-001 W3-C Discovery v1

**Type:** Pre-execution discovery — read-only + FTP inventory  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** W3-C — Footer Reduction

---

## Executive summary

Footer dominates viewport due to **stacked 50px vertical gaps**, **six always-visible legal blocks**, **26px catalog column titles**, and **6-column manufacturer link layout**. Popup forms (6) live below `</footer>` and are **not** visible footer weight — consolidation deferred to W3-D.

**Evidence (local, not git):** `.recovery-temp/site-001-w3c-work/discovery-meta.json` · backup `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3c-20260609-0259\`

---

## 1. File inventory

| File | Remote path | Lines | Bytes | Role |
|------|-------------|-------|-------|------|
| **footer.twig** | `catalog/view/theme/auto/template/common/footer.twig` | 410 | 20 078 | Markup, legal blocks, popups, scripts |
| **main.css** | `css/main.css` | 6 784 | 104 417 | Footer layout tokens (§6497–6672) |
| **media.css** | `css/media.css` | 2 192 | 30 330 | Responsive footer overrides |
| **common.js** | `js/common.js` | — | — | Referenced from footer; **out of W3-C scope** |

**Footer-related JS in footer.twig:** inline AJAX handler for `.actionform`; third-party Callibri, SmartWidgets, Yandex Metrika — **defer** (no removal).

---

## 2. Current footer sections

| Section | Class / marker | Content |
|---------|----------------|---------|
| Brand + CTAs | `.footer_top__wrap` | Logo, callback modal trigger, phone, WhatsApp, address |
| Catalog links | `.footer_menu__auto`, `.footer_menu__catalog` | Manufacturer lists (new + used) via `manufactures_new` / `manufactures` |
| Legal stack | `.footer_bottom > div` × **7** | Credit terms, penalties, entity, pricing disclaimer, PD consent, admin rights, policy links, copyright |
| Popups (post-footer) | `#callback__FORM_popup`, credit, trade-in, etc. | 6 forms — hidden until modal |

---

## 3. Duplication and noise

| Issue | Detail |
|-------|--------|
| **Legal block spacing** | Each `.footer_bottom > div` had `padding-top: 50px` — **~350px padding alone** across 7 blocks |
| **Footer shell padding** | `footer { padding: 50px 0 }` + `border-top/bottom: 10px` |
| **Menu spacing** | `.footer_menu { padding-top: 50px }`; title `font-size: 26px`; link `margin: 10px 0` |
| **Inline styles** | **8** hits in footer.twig (loan-terms link flex inline style) |
| **Catalog density** | Manufacturer lists in **6 CSS columns** (desktop) |
| **Popup forms** | 6 duplicate AJAX embed patterns — **not visible** in footer; W3-D scope |

---

## 4. Current height proxy (HTTP, pre-change)

| URL | Footer HTML bytes | Links | Forms in footer |
|-----|-------------------|-------|-----------------|
| `/` | 11 080 | 89 | 0 |
| `/about` | 11 080 | 89 | 0 |
| `/contact/` | 11 080 | 89 | 0 |
| `/cars/` | 11 080 | 89 | 0 |
| `/auto/` | 11 080 | 89 | 0 |

**Rendered text chars (footer):** ~5 305 (all legal paragraphs expanded).

---

## 5. Preserved elements (must keep)

- Logo `/img/logo_white.svg` alt **СИБКАР**
- Phone `+7 (383) 388-55-23`
- WhatsApp `wa.me/79539979910`
- Address Новосибирск, ул. Богдана Хмельницкого 101
- Callback CTA → `#callback__FORM_popup`
- Entity block OOO СибКар + INN/OGRN + bank/insurance partners
- Policy links `/privacy-policy/`, `/user-agreement/`, `/cookie-files-policy/`
- Loan terms link `/loan-terms`
- All manufacturer SEO links in both columns
- Copyright `© ООО «СибКар»`

---

## 6. Planned reduction (W3-C)

| Rule | Action |
|------|--------|
| Compress vertical spacing | Reduce footer/menu/legal padding tokens |
| Compress legal area | Collapse long paragraphs into `<details>` expander; entity + links stay visible |
| Compress catalog blocks | Columns 6→4 desktop; tighter link margins and title size |
| Compress contact area | Keep single CTA row; no duplicate phone strip added |
| Preserve SEO | No link removal |

**Target:** 40–60% visible footer height reduction (CSS + collapsed legal default).

---

## 7. Risk notes

| Risk | Mitigation |
|------|------------|
| Legal accessibility | All text retained in DOM; expander + `/loan-terms` |
| Modification cache | Admin cache clear + modification refresh after twig edit |
| Popup form regression | Popups untouched in W3-C |

---

## 8. Authorization prerequisites

| Artefact | Status |
|----------|--------|
| Phase 2 write charter | [SITE-001-W2-WRITE-CHARTER-v1.md](SITE-001-W2-WRITE-CHARTER-v1.md) — **ACTIVE** |
| Change request | CR-SITE-001-W3C-2026-06-09 — **READY** |
| Rollback plan | [SITE-001-W3C-ROLLBACK-PLAN-v1.md](SITE-001-W3C-ROLLBACK-PLAN-v1.md) |
| Pre-write backup | `pre-w3c-20260609-0259` — **DONE** |
