# SITE-001 W3V2 Write Charter v1

**Type:** Phase 2 write authorization charter — W3V2 Visual Identity Refresh  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W3V2 — Visual Identity Refresh (CSS-only)

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | Visual goals, token policy |
| [SITE-001-W3V2-CHANGE-REQUEST-v1.md](SITE-001-W3V2-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W3V2-ROLLBACK-PLAN-v1.md](SITE-001-W3V2-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Parent rollback tiers T1–T3 |

---

## 1. Allowed scope (W3V2)

| Category | Allowed | Channel |
|----------|---------|---------|
| **Color tokens** | `:root` `--w3v2-*` custom properties | FTP |
| **Depth tokens** | Shadow system sm/md/lg | FTP |
| **CSS overrides** | Cards, buttons, forms, header/footer visuals | FTP |
| **W3-V bridge** | Remap `--w3v-shadow-*` to W3V2 depth | FTP |
| **Responsive CSS** | W3V2 block in `media.css` | FTP |
| **Cache** | System + modification + image cache clear | Admin |

**File allow-list:** `css/main.css`, `css/media.css`

**Explicitly NOT in scope:** twig, PHP, JS, DB, SEO, routes, content, structure.

---

## 2. Operator authority

Operator decision (2026-06-09): density optimization (W3UX-C1) **remains active**; next priority is **visual identity**, not structure.

---

## 3. Status

**ACTIVE** — execution authorized on TEST per operator W3V2 brief.
