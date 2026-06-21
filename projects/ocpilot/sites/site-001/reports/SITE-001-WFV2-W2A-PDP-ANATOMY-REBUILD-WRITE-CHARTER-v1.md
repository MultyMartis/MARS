# SITE-001 WF-V2-W2A PDP Anatomy Rebuild Write Charter v1

**Type:** Phase 2 write authorization charter — WF V2 Wave 2-A Used PDP Anatomy Rebuild  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** WF-V2-W1 Hybrid Header live · WF-V2-W2 Flat PDP live · WF-V2-W2S Clean Stabilization live

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](SITE-001-WF-V2-GAP-ANALYSIS-v1.md) | Gap matrix · preservation map |
| SITE-001 PDP Composition Audit *(operator brief)* | C-01, C-03, C-08, C-09, C-10, C-11 scope |
| `projects/ocpilot/sites/site-001/design/wf-v2-concept/01-sibcar-v2-concept.png` | Used PDP showroom composition |
| [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-CHANGE-REQUEST-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-ROLLBACK-PLAN-v1.md](SITE-001-WFV2-W2A-PDP-ANATOMY-REBUILD-ROLLBACK-PLAN-v1.md) | T1 rollback instance |

---

## 1. Operator mandate

**Architectural wave — not cosmetic.** Stop all new visual polish / color passes.

**Goal:** Full PDP composition rebuild — structure and DOM order, not style tokens.

**MANDATORY:** If implementation adds colors, shadows, borders, radii, typography changes, or hover/focus effects → **FAIL**.

**Do NOT:** header, footer, homepage, catalog, modals, PHP, JS, DB.

---

## 2. Allowed scope (WF-V2-W2A)

| Category | Allowed | Channel |
|----------|---------|---------|
| **product.twig** | DOM reorder · commercial stage anatomy · layer 3 grid · reviews position · lcd_display relocation · credit image removal | FTP |
| **CSS** | WF-V2-W2A block in `main.css` + `media.css` — grid/flex layout only atop W2/W2S | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

**Backup (pre-write):** `pre-wfv2-w2a-pdp-anatomy-rebuild-YYYYMMDD-HHMM`

| File | Remote path |
|------|-------------|
| `header.twig` | `catalog/view/theme/auto/template/common/header.twig` |
| `product.twig` | `catalog/view/theme/auto/template/product/product.twig` |
| `main.css` | `css/main.css` |
| `media.css` | `css/media.css` |

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

## 4. Task phases (composition audit items)

| ID | Target |
|----|--------|
| **C-01** | H1 inside commercial stage; single title; no identity gap above hero |
| **C-03** | Commercial stage = Identity Row + Hero Split + Trust Line only |
| **C-08** | Remove `lcd_display.product` from hero→equipment path; relocate below fold |
| **C-09** | Layer 3: Equipment ≈60% + Credit ≈40% desktop; stack mobile |
| **C-10** | Reviews after Equipment + Credit zone |
| **C-11** | Remove duplicate car photo from credit section |

---

## 5. Success criteria

1. Commercial stage reads as one object  
2. H1 no longer isolated above stage  
3. Trust is part of the scene  
4. Equipment + Credit form one zone  
5. Reviews no longer split Equipment/Credit  
6. No duplicate hero photo in credit  
7. PDP closer to showroom page than OC product card  

---

## 6. Verification matrix

| URL | Expect |
|-----|--------|
| `/audi-a1-2012-s-probegom-149-000-km-799` | `wfv2-anatomy-pdp` + W2/W2S markers preserved |
| `/`, `/about`, `/contact/` | No W2A leak; header unchanged |
| `/cars/`, `/cars/bmw/` | No W2A leak |
| `/auto/`, `/auto/haval/` | No W2A leak |

**Gate:** 8/8 HTTP 200 · markers · before/after screenshots (desktop, tablet, mobile).

---

## 7. CSS marker

Block marker: `WF-V2-W2A PDP Anatomy Rebuild`  
End anchor: `/* END WF-V2-W2A PDP Anatomy Rebuild — main */`

Rollback: remove WF-V2-W2A block; restore product.twig from backup.

*SITE-001 WF-V2-W2A PDP Anatomy Rebuild Write Charter v1 — TEST only.*
