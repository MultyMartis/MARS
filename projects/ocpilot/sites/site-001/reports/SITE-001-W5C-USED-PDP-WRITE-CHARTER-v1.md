# SITE-001 W5-C Used PDP Write Charter v1

**Type:** Phase 2 write authorization charter — W5-C Used PDP Commercial Stage  
**Date:** 2026-06-10  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `pre-w5c-commercial-stage-20260610-0002`  
**Phase:** W5-C — Commercial offer scene (used PDP only)

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md](SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md) | Block plan, safety gate |
| [SITE-001-W5C-USED-PDP-CHANGE-REQUEST-v1.md](SITE-001-W5C-USED-PDP-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W5C-USED-PDP-ROLLBACK-PLAN-v1.md](SITE-001-W5C-USED-PDP-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
| [SITE-001-W5-STABLE-BACKUP-v1.md](SITE-001-W5-STABLE-BACKUP-v1.md) | Pre-write backup report |

---

## 1. Operator direction (2026-06-10)

Create stable backup, then advance used PDP from W4 structural slice to **W5-C commercial stage** — unified vehicle offer per Concept B mandate.

**Target URL:** `https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799`

---

## 2. Allowed scope (W5-C)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Used PDP twig** | Wrapper div, class additions only | FTP |
| **CSS** | W5-C block in `main.css` + `media.css` | FTP |
| **Modal styling** | `body.used_car_page` scoped CSS (footer popups untouched) | FTP |
| **Cache** | System + modification cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/product/product.twig`
2. `css/main.css`
3. `css/media.css`

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP logic | **FORBIDDEN** |
| JS logic | **FORBIDDEN** |
| DB changes | **FORBIDDEN** |
| SEO / meta / text rewrites | **FORBIDDEN** |
| `header.twig`, `footer.twig` | **FORBIDDEN** (header regression fixes only if explicitly authorized) |
| Homepage, catalog, new PDP | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |

---

## 4. Success criteria

Target **≥7/10** visual impact on used PDP — see design plan §9. Subtle change = FAIL → rollback recommended.

Regression: W5-A header stable on all 8 verification URLs; no W5-C marker leak to non-used pages.

---

## 5. Status

**ACTIVE** — W5-C execution authorized on TEST per operator task brief 2026-06-10.

*SITE-001 W5-C Used PDP Write Charter v1 — TEST only; no commit; no push.*
