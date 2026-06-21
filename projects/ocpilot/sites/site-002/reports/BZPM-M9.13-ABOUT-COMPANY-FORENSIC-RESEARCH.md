# REPORT — BZPM M9.13 About Company Forensic Research

**Milestone:** M9.13 — About Company / О компании  
**Project:** SITE-002 / BZPM (ЗПМ)  
**Environment (read-only baseline):** https://zpm.new-site.space/  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Status:** **RESEARCH COMPLETE**  
**Source:** Operator forensic research — **chat approved**  
**Registration date:** 2026-06-22  
**Mode:** Research only — **no** design · **no** implementation · **no** deploy

**Registration note:** Forensic was completed and operator-approved in chat before repo export. This document is the **first markdown registration** of M9.13; it compiles corroborating repo evidence without re-running live forensic.

---

## 1. Executive summary

| Field | Value |
|-------|--------|
| **Page role** | Corporate narrative — «кто мы», производство, доверие, география |
| **Canonical URL (TEST)** | `/about` |
| **Nav label** | «О компании» |
| **Research verdict** | **RESEARCH COMPLETE** — architecture and cross-link role sufficient for next-phase design charter |
| **Implementation** | **Not started** · **not authorized** by this report |

### Key findings (repo-corroborated)

| # | Finding | Evidence |
|---|---------|----------|
| 1 | Dedicated **about-page** CSS namespace exists on live theme | `style.css` § «Страница О КОМПАНИИ» — `.about-page--*` classes |
| 2 | Page includes **video block** with scroll-to-next interaction | `main.js` — `[data-scroll-next]` init for «блока видео на странице О компании» |
| 3 | Layout blocks: hero media, main text+image split, video, certificate promo, geo promo | CSS class inventory §3 |
| 4 | Linked from **header top nav**, **footer**, **mobile menu** on all captured pages | `footer.twig` / `offcanvasmenu.twig` / contact QA captures |
| 5 | IA role: trust / OEM proof anchor — feeds catalog Commercial Trust and PDP buyer questions | `BZPM-BLUEPRINT-v1.md` · `BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` |
| 6 | Twig template path on live hosting — **not in MARS git tree** | Same pattern as M9.8.9-03 forensic — lives on TEST / bulk storage |

---

## 2. Scope

### In scope (forensic)

- URL and navigation placement
- CSS/Twig architecture signals from repo captures
- Cross-links from catalog / commercial surfaces
- IA role vs catalog-redesign blueprint
- Gaps and SAFE UNKNOWN for implementation planning

### Out of scope

- Visual redesign or wireframes
- Copy rewrite
- Twig/CSS/JS changes
- Deploy or TEST modifications
- Production (`bzpm.ru`) attestation

---

## 3. Live architecture signals (repo evidence)

### 3.1 URL and routing

| Field | Value |
|-------|--------|
| **Public URL** | `https://zpm.new-site.space/about` |
| **OpenCart route (expected)** | `information/information` with SEO alias `about` |
| **Route confirmation** | **SAFE UNKNOWN** — no `information/about.twig` in MARS git tree; inferred from URL pattern and nav |

### 3.2 Navigation placement

Present in global chrome (2026-06-21 captures):

| Surface | Link | Label |
|---------|------|-------|
| Header top bar | `/about` | О компании |
| Footer company links | `/about` | О компании |
| Mobile offcanvas menu | `/about` | О компании |

**Evidence:** `m7.1-launch-mode-work/catalog__view__theme__default__template__common__footer.twig` · `offcanvasmenu.twig` · `reports/contacts-polish-work/qa-contact-polish.html`

### 3.3 CSS block inventory (live `style.css` capture)

Source: `reports/contacts-redesign-work/live-capture/assets__css__style.css` (2026-06-21 FTP capture)

| Block / class root | Inferred section role |
|--------------------|----------------------|
| `.about-page--big-media-capture` | Full-width hero / top media |
| `.about-page--main-wrap` | Two-column main (text + image); stacks column ≤ breakpoint |
| `.about-page--main-text` | H2 + paragraph stack |
| `.about-page--main-img` | Supporting image column |
| `.about-page-video` | Video section container |
| `.about-page-video__media` | Video element (max-height 70vh, object-fit cover) |
| `.about-page-video__scroll-btn` | Scroll CTA overlay on video (`data-scroll-next` target) |
| `.about-page--sert-promo-wrap` | Certificate / trust promo block |
| `.about-page--geo-promo-wrap` | Geography / production footprint promo (text + image split) |
| `.about-adv__title` | Advantages-related typography hook (shared or section title) |

**Responsive:** `.about-page--main-wrap` → `flex-flow: column` at captured mobile breakpoint (≤11306 region in `style.css`).

### 3.4 JavaScript behaviour

| Hook | Behaviour | File evidence |
|------|-----------|---------------|
| `[data-scroll-next]` | Click scrolls to next block id from attribute | `m9.8.5-products-per-page-work/main.js` — comment «для блока видео на странице О компании» |

**Progressive enhancement:** scroll interaction is enhancement; static video block remains visible without JS.

### 3.5 Template location

| Item | Status |
|------|--------|
| Twig on live TEST | **Expected** `catalog/view/theme/default/template/information/information.twig` or custom about template |
| Twig in MARS git | **NOT PRESENT** — forensic markup not captured in dedicated HTML snapshot in-repo |
| Bulk storage | `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` — about-specific forensic export **not found** at registration pass |

---

## 4. Information architecture role

### 4.1 Buyer questions addressed (from catalog research cross-links)

| Persona / intent | Question | About page role |
|------------------|----------|-----------------|
| Owner / снабженец | «Кто вы? Можно ли доверять заводу?» | Primary trust narrative surface |
| Проектировщик | Производство, география, сертификация | Supports OEM proof; overlaps cert/geo blocks |
| Дилер | Канал vs прямой завод | Secondary — `/dealers` is dedicated surface (M9.16) |

**Cross-reference:** `BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` § persona objections; Techno-TT `/about` benchmark note.

### 4.2 Relationship to catalog surfaces

| Surface | Link to About |
|---------|---------------|
| Header / footer | Persistent `/about` |
| Commercial Trust FAQ | «Кто вы?» class objections — About is canonical deep link |
| Homepage advantages | Thematic overlap — **differentiation risk** if copy duplicates without page-specific depth |
| PDP / PLP | No inline full About block — trust deferred to header or post-grid CTA |

**Blueprint rule:** Single information owner per fact type (`BZPM-BLUEPRINT-v1.md` CP-01). About owns **entity narrative**; catalog owns **SKU evaluation**.

---

## 5. Forensic gaps and risks

| ID | Gap / risk | Severity | Notes |
|----|------------|----------|-------|
| G-01 | No dedicated about HTML snapshot in repo | Medium | CSS/JS evidence only; operator may supply live capture before implementation |
| G-02 | Twig source off-repo | Medium | Standard SITE-002 pattern — live-capture required before edits |
| G-03 | Content freshness vs operator manual UI | Low | MANUAL UI CANONICAL — any operator CSS/Twig on live overrides stale docs |
| G-04 | Certificate block duplication vs PLP Commercial Trust | Medium | M9.8.9-03B noted persona/copy overlap — About cert promo must not blindly duplicate PLP trust strip |
| G-05 | Video block accessibility / reduced motion | Low | `prefers-reduced-motion` posture not attested for about video scroll UX |

---

## 6. Research verdict

| Field | Value |
|-------|--------|
| **M9.13 status** | **RESEARCH COMPLETE** |
| **Ready for** | Operator design charter · implementation planning |
| **Not ready for** | Implementation without charter · deploy |
| **Next program step** | M9.15 Payment forensic (first research-not-started page) **or** operator charter to implement M9.13 if priority overridden |

---

## 7. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact `information_id` in OpenCart admin for `/about` | **SAFE UNKNOWN** |
| Full block order and copy on live `/about` at registration date | **SAFE UNKNOWN** — no in-repo HTML snapshot |
| Production `bzpm.ru/about` parity with TEST | **SAFE UNKNOWN** |
| Verbatim operator chat forensic transcript | Not committed — status registered per operator approval |

---

## 8. Evidence index

| Artifact | Role |
|----------|------|
| `reports/contacts-redesign-work/live-capture/assets__css__style.css` | About-page CSS inventory |
| `m9.8.5-products-per-page-work/main.js` | Video scroll-next behaviour |
| `m7.1-launch-mode-work/catalog__view__theme__default__template__common__footer.twig` | Nav/footer links |
| `projects/website-factory/execution-cases/bzpm-catalog-redesign/BZPM-BLUEPRINT-v1.md` | IA ownership rules |
| `reports/BZPM-M9.9-CTA-INTELLIGENCE-RESEARCH.md` | Persona / trust cross-links |
| `projects/website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md` | Program registry |

---

*M9.13 About Company — research registration only. No implementation authorized.*
