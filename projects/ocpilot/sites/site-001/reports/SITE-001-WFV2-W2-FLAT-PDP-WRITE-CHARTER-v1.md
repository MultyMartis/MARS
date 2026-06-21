# SITE-001 WF-V2-W2 Flat PDP Write Charter v1

**Type:** Phase 2 write authorization charter — WF V2 Wave 2 Used PDP Flat Stage  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** WF-V2-W1 Hybrid Header **APPROVED** · W5-C Used PDP Commercial Stage live

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | Gap matrix · preservation map |
| [SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md) | Wave 2 scope |
| `01-sibcar-v2-concept.png` | Used PDP composition — flat showroom stage |
| `02-sibcar-v2-specification.png` | Subtractive / minimal surface principles |
| [SITE-001-WFV2-W2-FLAT-PDP-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W2-FLAT-PDP-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md) | T1 rollback instance |

---

## 1. Operator mandate

**Subtraction wave.** Move Used PDP from «styled OpenCart dealer card system» to «clean automotive showroom stage».

**MANDATORY:** If implementation adds extra borders, shadows, containers, or decorative blocks → **FAIL**.

**Do NOT:** redesign header/footer/homepage/catalog; touch PHP/JS/DB/SEO/forms/modal logic; introduce new visual language.

---

## 2. Allowed scope (WF-V2-W2)

| Category | Allowed | Channel |
|----------|---------|---------|
| **product.twig** | Add `wfv2-flat-pdp` hook on commercial stage wrapper only | FTP |
| **CSS** | WF-V2-W2 block in `main.css` + `media.css` — override W5-C card/shadow/border surfaces | FTP |
| **Visual** | Flatten hero, price authority, trust band, specs grid, equipment, credit — W2-A through W2-G | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

**Backup:** `pre-wfv2-w2-flat-pdp-YYYYMMDD-HHMM` — product.twig, main.css, media.css + manifest.

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP, JS, DB | **FORBIDDEN** |
| `header.twig`, `footer.twig`, `home.twig`, `category.twig` | **FORBIDDEN** |
| SEO / content / URLs / menu / phone values | **FORBIDDEN** |
| W5-A navigation / dropdown logic | **FORBIDDEN** |
| Forms logic / modal logic (DOM/JS) | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## 4. Task phases

| Phase | Target |
|-------|--------|
| W2-A | Hero flattening — one commercial stage; reduce nested card hierarchy |
| W2-B | Price authority — price anchor; demote discount/credit chrome |
| W2-C | Trust strip — single information band; preserve statuses + VIN CTA |
| W2-D | Specs de-cardification — information grid, not mini cards |
| W2-E | Equipment cleanup — scan-friendly sheet; keep columns/content |
| W2-F | Credit block — part of page; reduce nesting/framing |
| W2-G | Global PDP noise reduction — remove heavy borders/shadows/dividers |

---

## 5. Success criteria

Operator opens Used PDP and **immediately** notices:

1. Fewer boxes  
2. Fewer borders  
3. Cleaner composition  
4. Price dominates  
5. PDP feels more premium  
6. PDP feels less OpenCart  

If visual change is not obvious → **WF-V2-W2 FAIL** → T1 rollback recommended.

---

## 6. Verification matrix

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | `wfv2-flat-pdp` + W5-C/W4 markers preserved |
| `/`, `/about`, `/contact/` | No W2 leak; hybrid header unchanged |
| `/cars/`, `/cars/bmw/` | No W2 leak |
| `/auto/`, `/auto/haval/` | No W2 leak |

Functional: modals · dropdowns · responsive · no Twig/JS errors.

---

## 7. CSS marker

Block marker: `WF-V2-W2 Flat Used PDP Stage`  
End anchor: `/* END WF-V2-W2 Flat Used PDP Stage — main */`

Rollback: remove WF-V2-W2 block from main.css + media.css; restore product.twig from backup.
