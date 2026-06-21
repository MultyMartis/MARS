# SITE-001 WF-V2-W1 Hybrid Header Write Charter v1

**Type:** Phase 2 write authorization charter — WF V2 Wave 1 Hybrid Header  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** Visual Baseline V1 (W5-A/S + W5-C) · WF V2 GAP + Implementation Plan **APPROVED**

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | Gap matrix · preservation map |
| [SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md) | Wave sequence · W1 scope |
| `01-sibcar-v2-concept.png` | Hybrid header visual authority (light rail + dark band + light promo) |
| [SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md) | T1 rollback instance |

---

## 1. Operator direction (HITL 2026-06-10)

**Do NOT** implement pure light header from spec `02`.  
**Do NOT** retain current graphite W5-A header surface.

**Target:** **WF V2 Hybrid Header**

1. Contact rail — **light**
2. Primary band — **dark** (automotive dealership)
3. Promo strip — **light / neutral**

Matches approved visual direction from concept mock `01`.

---

## 2. Allowed scope (WF-V2-W1)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Header twig** | Remove phone/WA from primary band CTA cluster; restore original logo asset; add WF V2 class hooks | FTP |
| **CSS** | WF-V2-W1 block in `main.css` + `media.css` — override W5-A graphite surfaces | FTP |
| **Visual** | Contact rail flat info line; dark primary band; light promo strip; de-noise borders/shadows | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `css/main.css`
3. `css/media.css`

**Backup:** `pre-wfv2-w1-header-YYYYMMDD-HHMM` — header.twig, main.css, media.css + manifest.

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP, JS, DB | **FORBIDDEN** |
| `product.twig`, `home.twig`, `category.twig`, `footer.twig` | **FORBIDDEN** |
| SEO / content / URLs / menu labels / phone values | **FORBIDDEN** |
| W5-C PDP surface changes | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## 4. Success criteria (visual)

Operator opens site and **immediately** sees:

1. Header visually close to V2 concept mock (hybrid three-zone system)
2. Cleaner than Baseline V1 — fewer layers, no card-in-card
3. Phone/WhatsApp **only** in contact rail (desktop primary band)
4. Contact rail = intentional info line, not UI cards
5. Promo strip light, compact, no overlap
6. Original logo visible (no invert filter)
7. Static header (no sticky)

**Target:** If difference not visually obvious → **WF-V2-W1 FAIL** → T1 rollback recommended.

---

## 5. Verification matrix

| URL | Expect |
|-----|--------|
| `/` | Hybrid header; callback in primary band; promo visible |
| `/about` | Same shell; no regression |
| `/contact/` | Forms present |
| `/cars/` · `/cars/bmw/` | Catalog + light promo |
| `/auto/` · `/auto/haval/` | New cars shell |
| `/audi-a1-2012-s-probegom-149-000-km-799` | W5-C PDP unchanged; header hybrid |

Functional: dropdown «Услуги» · dropdown «Ещё» · mobile offcanvas · callback modal hook.

---

## 6. CSS marker

Block marker: `WF-V2-W1 Hybrid Header System`  
End anchor: `/* END WF-V2-W1 Hybrid Header System — main */`

Rollback: remove WF-V2-W1 block from main.css + media.css; restore header.twig from backup.
