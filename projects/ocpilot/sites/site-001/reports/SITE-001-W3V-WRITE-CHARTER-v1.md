# SITE-001 W3-V Write Charter v1

**Type:** Phase 2 write authorization charter — W3-V Visual Layer Refresh  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)** · active theme **`auto`**  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W3-V — Visual Layer Refresh (CSS-only)

**Supersedes for W3-V writes:** structural/footer scope in [SITE-001-W2-WRITE-CHARTER-v1.md](SITE-001-W2-WRITE-CHARTER-v1.md) W3-C section — **W3-C ROLLED BACK**; W3-V is a **revised Phase 2 approach** (visual-only, no markup changes).

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | Visual goals, tokens (adapted for W3-V radius targets) |
| [SITE-001-W3V-CHANGE-REQUEST-v1.md](SITE-001-W3V-CHANGE-REQUEST-v1.md) | Formal change request |
| [SITE-001-W3V-ROLLBACK-PLAN-v1.md](SITE-001-W3V-ROLLBACK-PLAN-v1.md) | T1 rollback instance |
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

## 2. Allowed execution scope (W3-V)

Human-supervised writes permitted **only** on TEST, **only** within W3-V visual layer:

| Category | Allowed | Access channel |
|----------|---------|----------------|
| **CSS tokens** | `:root` custom properties; spacing, radius, shadow tokens | FTP |
| **CSS overrides** | Buttons, forms, cards, shadows, hover states, visual hierarchy | FTP |
| **Responsive CSS** | Matching overrides in `media.css` where breakpoints require | FTP |
| **Cache** | System + modification cache clear after CSS upload | Admin |

**W3-V file allow-list:**

- `css/main.css`
- `css/media.css`

**Explicitly NOT in scope:**

- Any `.twig` template
- Header / footer structure
- Navigation
- Content, texts, block order
- OpenCart business logic, forms logic, DB

---

## 3. Forbidden scope

| Category | Forbidden |
|----------|-----------|
| **Structure** | Header/footer markup; block add/remove/reorder |
| **Content** | Text changes; link removal; legal content edits |
| **Environment** | Production, DNS, SSL, `robots.txt` |
| **Catalog / DB** | Product import, category edits, destructive SQL |
| **Extensions** | Install/uninstall modules |
| **Third-party widgets** | Callibri, SmartWidgets, DMP removal |
| **W3-C repeat** | Footer structural reduction; legal collapse markup |

---

## 4. Operator authority

| Role | Authority |
|------|-----------|
| Write approver | **Андрей** (per access brief) |
| Session operator | Executes FTP/admin under approver authorization |
| Agent | Prepare diffs, run verification, document — **no autonomous production writes** |

---

## 5. Success criteria (W3-V)

1. Border radius modernized: **8px** small elements, **12px** large blocks, **8–10px** buttons.
2. Soft restrained shadows applied to cards and CTAs — no heavy glassmorphism.
3. Button height, padding, hover improved — **brand colors preserved**.
4. Form inputs/textarea/submit spacing and focus improved — **fields unchanged**.
5. Catalog, advantage, bank, information cards: spacing, radius, shadow, hover improved.
6. Price and CTA visual hierarchy strengthened — **no layout shift**.
7. Verification PASS on `/`, `/about`, `/contact/`, `/cars/`, `/auto/`, used PDP, new PDP.
8. Per-wave backup + rollback path documented.

---

## 6. Authorization record

| Field | Value |
|-------|-------|
| Charter status | **ACTIVE** — W3-V Visual Layer Refresh |
| Approver | **Андрей** |
| Date | 2026-06-09 |
| Change request | CR-SITE-001-W3V-2026-06-09 |
| Prior wave lesson | W3-C structural/footer changes **rejected** — W3-V is CSS-only |
