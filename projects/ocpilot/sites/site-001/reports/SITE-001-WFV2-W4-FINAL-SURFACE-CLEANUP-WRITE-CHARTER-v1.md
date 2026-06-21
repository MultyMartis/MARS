# SITE-001 WF-V2-W4 Final Surface Cleanup Write Charter v1

**Type:** Phase 2 write authorization charter — WF V2 Wave 4 Used PDP Final Surface Cleanup  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** WF-V2-W3 Layout Recomposition live on TEST

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | Gap matrix · preservation map |
| [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W4-FINAL-SURFACE-CLEANUP-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/01-sibcar-v2-concept.png` | Used PDP — clean white showroom reference |

---

## 1. Operator mandate

**Surface cleanup wave — not layout rebuild, not new design.**

WF-V2-W3 geometry is correct; page still looks visually dirty from layered backgrounds, borders, shadows, grey panels, nested surfaces, and section boxes accumulated across W5-C / W2 / W2S waves.

Goal: **clean white showroom page** — minimum chrome, strong car + price + CTA.

**MANDATORY:** If result still looks like boxed OpenCart → **WF-V2-W4 FAIL**.

**Do NOT:** header, footer, homepage, catalog, PHP, JS, DB, SEO, forms logic.

---

## 2. Allowed scope (WF-V2-W4)

| Category | Allowed | Channel |
|----------|---------|---------|
| **product.twig** | Add `wfv2-surface-pdp` hook on commercial stage wrapper | FTP |
| **CSS** | WF-V2-W4 block in `main.css` + `media.css` — subtractive surface override atop W3 | FTP |
| **Visual** | Remove excess backgrounds/borders/shadows; clean hero, offer column, equipment, credit | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

**Backup (pre-write):** `pre-wfv2-w4-final-surface-cleanup-YYYYMMDD-HHMM`

Storage: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\`

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| Layout rebuild / DOM restructure beyond class hook | **FORBIDDEN** |
| PHP, JS, DB | **FORBIDDEN** |
| `header.twig`, `footer.twig`, `home.twig`, `category.twig` edits | **FORBIDDEN** |
| New decorative elements / new design language | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## 4. Task phases

| ID | Target |
|----|--------|
| **W4-01** | Remove excess PDP backgrounds — white showroom, no grey stage |
| **W4-02** | Hero — one unified showroom area |
| **W4-03** | Offer column — calm composition, no mini-cards |
| **W4-04** | Specs — clean facts list, no boxed grid |
| **W4-05** | CTA — keep red commercial focus, flat chrome |
| **W4-06** | Trust strip — light divider only |
| **W4-07** | Equipment — specification sheet, no box rows |
| **W4-08** | Credit — connected section, no floating widget |
| **W4-09** | Layer 3 — sequential sections, minimal chrome |

---

## 5. Success criteria

Operator opens Used PDP and **immediately** notices:

1. Fewer boxes  
2. Fewer grey panels  
3. Fewer borders  
4. Fewer shadows  
5. Cleaner showroom look  
6. Closer to WF V2 reference  
7. Red CTA and commercial focus preserved  

If result still looks like boxed OpenCart → **WF-V2-W4 FAIL** → T1 rollback recommended.

---

## 6. Verification matrix

| URL | Expect |
|-----|--------|
| Used PDP | `wfv2-surface-pdp` + W3/W2A markers preserved |
| `/`, `/about`, `/contact/` | No W4 leak; hybrid header unchanged |
| `/cars/`, `/cars/bmw/` | No W4 leak |
| `/auto/`, `/auto/haval/` | No W4 leak |

Functional: modal · form · responsive · no Twig/PHP errors.

---

## 7. CSS marker

Block marker: `WF-V2-W4 Final Surface Cleanup`  
End anchor: `/* END WF-V2-W4 Final Surface Cleanup — main */`

Rollback: remove WF-V2-W4 block from main.css + media.css; restore product.twig from backup.

Prior baseline: WF-V2-W3 (`pre-wfv2-w3-layout-recomposition-20260610-0413`).
