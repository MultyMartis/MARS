# SITE-001 W3UX-C1 Write Charter v1

**Type:** Phase 2 write authorization charter — W3UX-C1 Used Catalog Card Density  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)** · active theme **`auto`**  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W3UX-C1 — Used Cars Catalog Card Density (CSS-only)

**Supersedes for W3UX-C1 writes:** general Phase 2 scope in [SITE-001-W2-WRITE-CHARTER-v1.md](SITE-001-W2-WRITE-CHARTER-v1.md) — **this charter narrows to used catalog cards only**.

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W3UX-DENSITY-AUDIT-v1.md](SITE-001-W3UX-DENSITY-AUDIT-v1.md) | Discovery baseline · U-01–U-11 change map |
| [SITE-001-W3UX-DENSITY-DECISION-v1.md](SITE-001-W3UX-DENSITY-DECISION-v1.md) | Roadmap gate · W3UX-C1 authorized as wave 1 |
| [SITE-001-W3UX-C1-CHANGE-REQUEST-v1.md](SITE-001-W3UX-C1-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Parent rollback tiers T1–T3 |
| [SITE-001-W1-BACKUP-PROCEDURE-v1.md](SITE-001-W1-BACKUP-PROCEDURE-v1.md) | Pre-write backup checklist |
| [SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md) | Recovery baseline |

---

## 1. Environment

| Field | Value |
|-------|-------|
| **Authorized environment** | **TEST only** |
| **TEST URL** | `https://sibcar.new-site.space/` |
| **Production** | **FORBIDDEN** |
| **store_id** | **0** |

Any session that cannot confirm TEST host is **halted** (T3).

---

## 2. Allowed execution scope (W3UX-C1)

Human-supervised writes permitted **only** on TEST, **only** within W3UX-C1 density scope:

| Category | Allowed | Access channel |
|----------|---------|----------------|
| **CSS density overrides** | Used catalog cards only — `.used_catalog` scoped | FTP |
| **Responsive CSS** | Matching overrides in `media.css` where breakpoints require | FTP |
| **Cache** | System + modification cache clear after CSS upload | Admin |

**W3UX-C1 file allow-list:**

- `css/main.css`
- `css/media.css`

**Route family (verification):**

- `/cars/`
- `/cars/*` (e.g. `/cars/bmw/`, `/cars/audi/`)

**Explicitly NOT in scope:**

- Any `.twig` template (including `category.twig` — read-only for discovery)
- Header / footer structure
- New catalog (`/auto/`) — deferred to W3UX-C2
- PDP, homepage — deferred to later W3UX waves
- Content, texts, block order
- OpenCart business logic, forms logic, DB

---

## 3. Forbidden scope

| Category | Forbidden |
|----------|-----------|
| **Structure** | HTML/Twig markup changes; block add/remove/reorder |
| **Scripts** | JS changes |
| **PHP** | Controllers, models |
| **Templates** | `header.twig`, `footer.twig`, `product.twig`, `productnew.twig`, `categorynew.twig` |
| **Content** | Text changes; link removal |
| **Environment** | Production, DNS, SSL |
| **Catalog / DB** | Product import, category edits, destructive SQL |
| **Visual redesign** | Color palette, radius, shadow refresh — W3-V layer preserved |

---

## 4. Operator authority

| Role | Authority |
|------|-----------|
| Write approver | **Андрей** (per access brief) |
| Session operator | Executes FTP/admin under approver authorization |
| Agent | Prepare diffs, run verification, document — **no autonomous production writes** |

---

## 5. Success criteria (W3UX-C1)

1. Used catalog card height reduced **15–20%** without layout break.
2. Price visually dominant; title and specs hierarchy improved.
3. Credit block compressed vertically — functionality unchanged.
4. Image dead space reduced — no broken images.
5. CTA buttons unchanged in location and function.
6. Verification PASS on `/cars/`, `/cars/bmw/`, `/cars/audi/` — desktop, tablet, mobile.
7. No regression on `/auto/`, `/`, header, footer.
8. Per-wave backup + T1 rollback path documented.

---

## 6. Authorization record

| Field | Value |
|-------|-------|
| Charter status | **ACTIVE** — W3UX-C1 Used Catalog Card Density |
| Approver | **Андрей** |
| Date | 2026-06-09 |
| Change request | CR-SITE-001-W3UX-C1-2026-06 |
| Prior context | W3-UX discovery complete; W3-V cosmetic pass insufficient; W3-C **ROLLED BACK** |
