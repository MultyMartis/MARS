# SITE-001 WF-V2-W3 PDP Layout Recomposition Write Charter v1

**Type:** Phase 2 write authorization charter — WF V2 Wave 3 Used PDP Layout Recomposition  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** WF-V2-W2A PDP Anatomy Rebuild live on TEST

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | Gap matrix · preservation map |
| [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W3-LAYOUT-RECOMPOSITION-ROLLBACK-PLAN-v1.md) | T1 rollback instance |

---

## 1. Operator mandate

**Composition wave — not cosmetic.** Geometry, structure, sizes, and DOM order only.

**MANDATORY:** If implementation adds colors, shadows, borders, radii, gradients, typography changes, or hover/focus effects → **FAIL**.

**Do NOT:** header, footer, homepage, catalog, modals, PHP, JS, DB, SEO, forms.

---

## 2. Allowed scope (WF-V2-W3)

| Category | Allowed | Channel |
|----------|---------|---------|
| **product.twig** | Offer column DOM reorder · `wfv2-layout-pdp` hook | FTP |
| **CSS** | WF-V2-W3 block in `main.css` + `media.css` — layout/geometry only atop W2A | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

**Backup (pre-write):** `pre-wfv2-w3-layout-recomposition-YYYYMMDD-HHMM`

Storage: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\`

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| Colors, shadows, borders, radii, typography, hover/focus | **FORBIDDEN** |
| PHP, JS, DB | **FORBIDDEN** |
| `header.twig`, `footer.twig`, `home.twig`, `category.twig` edits | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## 4. Task phases

| ID | Target |
|----|--------|
| **W3-01** | Hero split ~68/32 desktop — gallery dominates |
| **W3-02** | Widen Used PDP container (showroom layout, scoped) |
| **W3-03** | Offer column hierarchy: price → payment → CTA → specs → rest |
| **W3-04** | Characteristics below CTA group |
| **W3-05** | Equipment then Credit — vertical stack, not columns |
| **W3-06** | Reading path: car → price → CTA → equipment → credit → banks → similar |

---

## 5. Success criteria

1. Car visually dominates hero.
2. Price is second focal point.
3. CTA precedes characteristics.
4. Equipment and credit no longer compete horizontally.
5. PDP reads as showroom, not catalog card.
6. No new decorative elements.
7. No regressions on 8-URL matrix.

---

## 6. Rollback anchor

T1 restore from `pre-wfv2-w3-layout-recomposition-*`. Prior baseline: WF-V2-W2A (`pre-wfv2-w2a-pdp-anatomy-rebuild-20260610-0401`).
