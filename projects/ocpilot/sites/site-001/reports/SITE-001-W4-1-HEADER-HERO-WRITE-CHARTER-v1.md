# SITE-001 W4.1 Header & Hero Authority Write Charter v1

**Type:** Phase 2 write authorization charter — W4.1 Header & Hero Authority  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** W4 Used PDP baseline accepted · `pre-w4-1-stable-*`

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md) | Pre-implementation spec |
| [SITE-001-W4-1-HEADER-HERO-CHANGE-REQUEST-v1.md](SITE-001-W4-1-HEADER-HERO-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md](SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Parent rollback tiers T1–T3 |

---

## 1. Operator direction (2026-06-09)

W4 Used PDP accepted as working baseline. Create stable checkpoint, then W4.1 — make first screen look more modern and authoritative without undoing W4.

---

## 2. Allowed scope (W4.1)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Header twig** | Class additions on header, toolbar, nav | FTP |
| **Used PDP twig** | Promo class + PDP top wrapper | FTP |
| **CSS** | W4.1 block in `main.css` + `media.css` | FTP |
| **Visual** | Header shell, red discipline, promo integration, PDP top | FTP |
| **Cache** | System + modification cache clear | Admin |

**File allow-list:**

1. `catalog/view/theme/auto/template/common/header.twig`
2. `catalog/view/theme/auto/template/product/product.twig`
3. `css/main.css`
4. `css/media.css`

**Backup includes (not modified unless regression):** `footer.twig`

---

## 3. Forbidden scope

| Category | Status |
|----------|--------|
| PHP, JS, DB | **FORBIDDEN** |
| SEO / content / URLs / menu items | **FORBIDDEN** |
| `footer.twig` edits | **FORBIDDEN** unless regression-safe color only |
| W4 Used PDP rollback / hero rework | **FORBIDDEN** |
| Production deployment | **NOT AUTHORIZED** |

---

## 4. Success criteria (visual)

Operator opens homepage and used PDP and **immediately** sees:

1. Header looks more modern  
2. Top area feels less like old OpenCart  
3. Red accents feel more controlled  
4. PDP W4 improvements preserved  
5. No content/structure regression  

**Target:** **7/10** first-screen impact. If not obvious → W4.1 FAIL → T1 rollback recommended.

---

## 5. Status

**ACTIVE** — W4.1 execution authorized on TEST per operator task brief 2026-06-09.
