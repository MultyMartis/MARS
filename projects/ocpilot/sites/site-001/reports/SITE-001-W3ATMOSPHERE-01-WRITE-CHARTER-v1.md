# SITE-001 W3ATMOSPHERE-01 Write Charter v1

**Type:** Phase 2 write authorization charter — W3ATMOSPHERE-01 Global Atmosphere Refresh  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W3ATMOSPHERE-01 — Atmosphere-only CSS layer

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W3COLOR-01-DISCOVERY-v1.md](SITE-001-W3COLOR-01-DISCOVERY-v1.md) | Palette, surface, depth discovery |
| [SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md) | Operator visual preview |
| [SITE-001-W3ATMOSPHERE-01-CHANGE-REQUEST-v1.md](SITE-001-W3ATMOSPHERE-01-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W3ATMOSPHERE-01-ROLLBACK-PLAN-v1.md](SITE-001-W3ATMOSPHERE-01-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Parent rollback tiers T1–T3 |

---

## 1. Allowed scope (W3ATMOSPHERE-01)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Canvas / surfaces** | `background-color`, gradients, surface tokens | FTP |
| **Depth** | `box-shadow`, inset highlights, `backdrop-filter` | FTP |
| **Borders** | `border-color`, `border-radius` (atmosphere seams only) | FTP |
| **Color** | `color`, `opacity`, brand/graphite neutrals | FTP |
| **Tokens** | `:root` `--w3color-*` + W3V2 bridge | FTP |
| **Responsive CSS** | Atmosphere parity block in `media.css` | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:** `css/main.css`, `css/media.css`

**Explicitly NOT in scope:** twig, PHP, JS, DB, SEO, routes, content, structure, layout, spacing, typography scale, PDP hierarchy, CTA hierarchy, navigation changes.

---

## 2. Success criteria (visual)

Operator must immediately notice (≥3/5):

1. Header looks more premium  
2. Footer looks more premium  
3. Cards no longer look like default OpenCart cards  
4. Site background becomes a distinct surface  
5. Forms feel part of one design language  

---

## 3. Operator authority

Operator task brief 2026-06-09 — W3ATMOSPHERE-01 execution on TEST authorized per this charter and linked CR.

---

## 4. Status

**ACTIVE** — execution authorized on TEST.
