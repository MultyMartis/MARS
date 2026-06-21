# SITE-001 W5-A Header Shell Recomposition Write Charter v1

**Type:** Phase 2 write authorization charter — W5-A Header Shell  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** W4.1 deployed · Concept B · W5 Blueprint **APPROVED**

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) | Design authority — Concept B header architecture |
| [SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md](SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md) | Blueprint **APPROVED** |
| [SITE-001-W5A-HEADER-SHELL-CHANGE-REQUEST-v1.md](SITE-001-W5A-HEADER-SHELL-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md](SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md) | T1 rollback instance |

---

## 1. Operator direction (2026-06-09)

W5 Blueprint **APPROVED**. First implementation phase: **W5-A Header Shell Recomposition** — transform header from OpenCart three-band template to **modern dealership shell** (Concept B). **NOT** palette/atmosphere/shadow/radius wave.

---

## 2. Allowed scope (W5-A)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Header twig** | DOM regroup — contact rail + primary band + CTA cluster | FTP |
| **CSS** | W5-A block in `main.css` + `media.css` | FTP |
| **Architecture** | Static header; centered nav; inset promo (CSS sibling); CTA hierarchy | FTP |
| **Cache** | System + modification cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `css/main.css`
3. `css/media.css`

**Backup:** `pre-w5a-header-shell-YYYYMMDD-HHMM` — header.twig, main.css, media.css + manifest.

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP, JS, DB | **FORBIDDEN** |
| `product.twig`, `footer.twig`, homepage hero, catalog cards | **FORBIDDEN** |
| SEO / content / URLs / menu items / phone values | **FORBIDDEN** |
| Palette-only / atmosphere-only / shadow-only / radius-only | **FORBIDDEN** |
| W5-B / W5-C / W5-D | **FORBIDDEN** in this task |
| Production deployment | **NOT AUTHORIZED** |
| Commit / push | **NOT AUTHORIZED** |

---

## 4. Success criteria (visual)

Operator opens homepage and **immediately** sees:

1. **Sticky header gone** — header scrolls away  
2. **Header feels like one system** — not toolbar + nav + promo bands  
3. **Promo integrated** — inset row, not screaming third strip  
4. **CTA hierarchy clearer** — callback primary · phone secondary · WhatsApp supportive  
5. **Difference visible without A/B** — 3-second test

**Target:** Structural recomposition; if impact remains subtle → **W5-A FAIL** → T1 rollback recommended.

---

## 5. Verification matrix

| URL | Expect |
|-----|--------|
| `/` | W5-A shell; callback; no sticky |
| `/about` | Shell; no regression |
| `/contact/` | Forms present |
| `/cars/` · `/cars/bmw/` | Catalog + promo inset |
| `/auto/` · `/auto/haval/` | New catalog OK |
| `/audi-a1-2012-s-probegom-149-000-km-799` | W4 preserved; promo visible |

---

## 6. Status

**ACTIVE** — W5-A execution authorized on TEST per operator task brief 2026-06-09.
