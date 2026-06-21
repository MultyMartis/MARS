# SITE-001 W5-A Stabilization Pass Write Charter v1

**Type:** Phase 2 write authorization charter — W5-A-S Stabilization  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** W5-A deployed · operator review **PARTIAL PASS**

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md](SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md) | Parent W5-A charter |
| [SITE-001-W5A-HEADER-SHELL-DECISION-v1.md](SITE-001-W5A-HEADER-SHELL-DECISION-v1.md) | Prior decision — PASS WITH NOTES |
| [SITE-001-W5A-STABILIZATION-CHANGE-REQUEST-v1.md](SITE-001-W5A-STABILIZATION-CHANGE-REQUEST-v1.md) | Formal change request |

---

## 1. Operator direction (2026-06-09)

W5-A initial deploy **PARTIAL PASS**. Stabilization pass required before W5-B. **No redesign.** Fix promo overlap, dropdown regression, navigation density, responsive collisions. Preserve all routes, URLs, content, palette, atmosphere.

---

## 2. Allowed scope (W5-A-S)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Header twig** | Nav grouping — «Ещё» dropdown migration (routes preserved) | FTP |
| **CSS** | W5-A-S block in `main.css` + `media.css`; patch W5-A `overflow:hidden` on nav group | FTP |
| **Architecture** | Promo inset fix · dropdown z-index/overflow · density at 1280px | FTP |
| **Cache** | System + modification cache clear | Admin |
| **QA** | Responsive + interaction audits · before/after screenshots | Playwright |

**File allow-list:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `css/main.css`
3. `css/media.css`

**Backup:** `pre-w5a-stabilization-YYYYMMDD-HHMM` — header.twig, main.css, media.css + manifest.

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP, JS, DB | **FORBIDDEN** |
| `product.twig`, `footer.twig`, homepage hero, catalog cards, PDP | **FORBIDDEN** |
| SEO / route removal / content removal | **FORBIDDEN** |
| Palette / atmosphere / Concept C / Concept D | **FORBIDDEN** |
| W5-B / W5-C / W5-D | **FORBIDDEN** |
| Production · commit · push | **NOT AUTHORIZED** |

---

## 4. Success criteria

| Task | Criterion |
|------|-----------|
| A — Promo | No overlap · no clipping · promo visible on catalog/PDP |
| B — Dropdown | «Услуги» + «Ещё» hover/click functional desktop/tablet; offcanvas mobile |
| C — Nav density | Primary row breathes at 1280px; all routes reachable |
| D — Responsive | Audit 1920…390 documented; no header/promo collisions |
| E — Interaction | Logo · menu · phone · callback · WhatsApp · dropdowns work |

**Visual acceptance:** all five operator criteria met → W5-A eligible for COMPLETE sign-off.

---

## 5. Verification matrix

Same 8 URLs as W5-A charter. Screenshots: `sites/site-001/qa/w5a-stabilization-screenshots/`.

**Commit / push / production:** **NOT AUTHORIZED**
