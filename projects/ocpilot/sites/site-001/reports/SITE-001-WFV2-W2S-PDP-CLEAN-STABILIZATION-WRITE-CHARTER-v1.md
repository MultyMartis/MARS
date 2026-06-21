# SITE-001 WF-V2-W2S PDP Clean Stabilization Write Charter v1

**Type:** Phase 2 write authorization charter — WF V2 Wave 2-S Used PDP Clean Stabilization  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** WF-V2-W1 Hybrid Header **APPROVED** · WF-V2-W2 Flat PDP live

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | Gap matrix · preservation map |
| [SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md) | Wave 2-S stabilization scope |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/01-sibcar-v2-concept.png` | Used PDP composition — clean showroom stage |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/02-sibcar-v2-specification.png` | Subtractive / minimal surface principles |
| [SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W2S-PDP-CLEAN-STABILIZATION-ROLLBACK-PLAN-v1.md) | T1 rollback instance |

**Design reference gate:** `01-sibcar-v2-concept.png` and `02-sibcar-v2-specification.png` — **VERIFIED PRESENT** (2026-06-10).

---

## 1. Operator mandate

**Stabilization wave — not a new design wave.** WF-V2-W2 direction is correct; result is still not clean. Goal: **cleaner composition**, not more decoration.

**MANDATORY:** If implementation adds extra borders, shadows, cards, or decorative blocks → **FAIL**.

**Do NOT:** redesign header/footer/homepage/catalog; touch PHP/JS/DB/SEO/forms/modal logic; introduce new visual language.

---

## 2. Allowed scope (WF-V2-W2S)

| Category | Allowed | Channel |
|----------|---------|---------|
| **product.twig** | Add `wfv2-clean-pdp` hook on commercial stage wrapper | FTP |
| **CSS** | WF-V2-W2S block in `main.css` + `media.css` — composition override atop W2 | FTP |
| **Visual** | Hero composition, price hierarchy, specs grid, trust strip, equipment, credit, noise purge — W2S-A through W2S-G | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

**Backup:** `pre-wfv2-w2s-pdp-clean-YYYYMMDD-HHMM` — product.twig, main.css, media.css + manifest.

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP, JS, DB | **FORBIDDEN** |
| `header.twig`, `footer.twig`, `home.twig`, `category.twig`, `productnew.twig` | **FORBIDDEN** |
| SEO / content / URLs / menu / phone values | **FORBIDDEN** |
| W5-A navigation / dropdown logic | **FORBIDDEN** |
| Forms logic / modal logic (DOM/JS) | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## 4. Task phases

| Phase | Target |
|-------|--------|
| W2S-A | Hero composition — one showroom stage; align gallery + offer; remove empty zones |
| W2S-B | Price / offer — price anchor; eye path Price → monthly → discounts → CTA |
| W2S-C | Specs grid — clean vehicle facts grid; reduce fragmentation |
| W2S-D | Trust strip — one calm proof line; even statuses; VIN in row |
| W2S-E | Equipment — spec sheet scan; reduce line noise; keep columns |
| W2S-F | Credit block — connected section; reduce black-box heaviness |
| W2S-G | Noise purge — borders, dividers, nested layers, red micro-noise |

---

## 5. Success criteria

Operator opens Used PDP and **immediately** notices:

1. Cleaner composition  
2. Fewer visual fragments  
3. Price area is clearer  
4. Trust strip is calmer  
5. Equipment is easier to scan  
6. Page feels designed, not just flattened  
7. No extra decoration added  

If result is only «less decorated» but not cleaner → **WF-V2-W2S FAIL** → T1 rollback recommended.

---

## 6. Verification matrix

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | `wfv2-clean-pdp` + `wfv2-flat-pdp` + W5-C/W4 markers preserved |
| `/`, `/about`, `/contact/` | No W2S leak; hybrid header unchanged |
| `/cars/`, `/cars/bmw/` | No W2S leak |
| `/auto/`, `/auto/haval/` | No W2S leak |

Functional: modals · dropdowns · responsive · no Twig/JS errors.

---

## 7. CSS marker

Block marker: `WF-V2-W2S Clean Used PDP Stabilization`  
End anchor: `/* END WF-V2-W2S Clean Used PDP Stabilization — main */`

Rollback: remove WF-V2-W2S block from main.css + media.css; restore product.twig from backup.
