# SITE-001 W2 Write Charter v1

**Type:** Phase 2 write authorization charter — **documentation only** in authoring; execution requires operator session  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Platform:** ocStore / OpenCart **3.0.3.8 (rs.2)** · active theme **`auto`**  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Phase:** W2 / W3 — Visual refresh (incremental reduction waves)

**Supersedes for Phase 2 writes:** read-only limits in [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) **only** for scoped waves below, **after** operator confirms this charter and pre-write backup.

**Binding specifications:**

| Document | Role |
|----------|------|
| [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](SITE-001-W2-VISUAL-SPECIFICATION-v1.md) | Visual goals, tokens, footer §9 |
| [SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md](SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md) | W3-A…F sequence |
| [SITE-001-W2-CHANGE-REQUEST-v1.md](SITE-001-W2-CHANGE-REQUEST-v1.md) | Phase 2 formal change request |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | Rollback tiers T1–T3 (extended per wave) |
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

## 2. Allowed execution scope (Phase 2)

Human-supervised writes permitted **only** on TEST, **only** within authorized W3 waves:

| Wave | Allowed operations | Access channel |
|------|-------------------|----------------|
| **W3-C** | Footer reduction — spacing compression, legal collapse markup, catalog link density, footer CSS tokens; **no** removal of legal text or SEO links | FTP/SFTP |
| **W3-A…B, D…F** | **NOT AUTHORIZED** in this charter instance — separate CR required |

**W3-C file allow-list:**

- `catalog/view/theme/auto/template/common/footer.twig`
- `css/main.css`
- `css/media.css`

**Supporting actions:** theme/modification cache clear; modification refresh after twig edits; HTTP verification.

---

## 3. Forbidden scope

| Category | Forbidden without new charter |
|----------|------------------------------|
| **Environment** | Production, DNS, SSL, `robots.txt` Host/Sitemap |
| **Catalog / DB** | Product import, category edits, destructive SQL |
| **Extensions** | Install/uninstall modules |
| **Third-party widgets** | Callibri, SmartWidgets, DMP removal |
| **Legal content removal** | Deleting compliance paragraphs or policy links |
| **Popup form removal** | AJAX popup handlers in footer.twig (W3-D scope) |
| **Manufacturer list removal** | SEO crawlable manufacturer links must remain |

---

## 4. Operator authority

| Role | Authority |
|------|-----------|
| Write approver | **Андрей** (per access brief) |
| Session operator | Executes FTP/admin under approver authorization |
| Agent | Prepare diffs, run verification, document — **no autonomous production writes** |

---

## 5. Success criteria (W3-C)

1. Footer visual height reduced **40–60%** on probed pages (collapsed legal default).
2. Logo, phone, WhatsApp, address, callback CTA preserved.
3. All legal text and policy links present (collapsed or visible).
4. Manufacturer SEO links preserved in both catalog columns.
5. No layout breakage on `/`, `/about`, `/contact/`, `/cars/`, `/auto/`, sample PDPs.
6. Per-wave backup + rollback path documented.

---

## 6. Authorization record

| Field | Value |
|-------|-------|
| Charter status | **ACTIVE** — W3-C first Phase 2 write |
| Approver | **Андрей** |
| Date | 2026-06-09 |
| Change request | CR-SITE-001-W3C-2026-06-09 |
