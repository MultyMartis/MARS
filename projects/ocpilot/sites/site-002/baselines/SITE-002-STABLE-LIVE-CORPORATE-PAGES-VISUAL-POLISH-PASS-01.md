# SITE-002 — Stable Live Corporate Pages Visual Polish Pass 01

**Baseline name:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-28  
**Mode:** Stable live checkpoint — CSS-only corporate pages visual polish (Pass 1)  
**Status (2026-06-28):** **REJECTED BY OPERATOR** — rolled back on TEST; **not** active visual authority

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01` — **historical only**

**Current visual authority:** **Pre-Pass-1** — live TEST `assets/css/style.css` restored from [backups/style.css.pre-site-002-corp-visual-polish-pass1.bak](../backups/style.css.pre-site-002-corp-visual-polish-pass1.bak)

**Rollback report:** [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01-ROLLBACK.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01-ROLLBACK.md)

**Next task:** Visual Polish Pass 1.1 — rules in [Knowledge Map §24](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#24-corporate-pages-visual-polish-pass-11--operator-rules)

**Scope:** Corporate pages M9.14–M9.18 only — `/delivery`, `/payment-methods`, `/guarantee`, `/dealers`, `/custom-equipment`. Does **not** supersede page-specific implementation checkpoints (M9.14–M9.18) or site-wide M9.13 About authority.

**Rejection reason:** global `padding-top: 0` on corporate sections (VP-01) removed vertical rhythm.

**Audit source:** [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md) — Priority 1 + Priority 2 implemented; Priority 3 deferred.

---

## 2. Live surface

| Item | Value |
|------|--------|
| **Modified file** | `assets/css/style.css` |
| **CSS block** | `SITE-002 — Corporate Pages Visual Polish Pass 1 (VP-01–VP-10)` |
| **pre_sha256** | `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` |
| **post_sha256** | `d4303c40d972135c092f5b8803b148b37e80881ac6f6db9e76a220995115ca42` |
| **main.js** | Unchanged |

---

## 3. Rollback

| Priority | Action |
|----------|--------|
| P1 | Restore `assets/css/style.css` from `backups/style.css.pre-site-002-corp-visual-polish-pass1.bak` |
| P2 | Or remove appended block `SITE-002 — Corporate Pages Visual Polish Pass 1` from live CSS |

**Rollback order:** FTP restore style.css → verify corp URLs HTTP 200 → operator visual HITL optional.

---

## 4. Evidence

| Artifact | Path |
|----------|------|
| Implementation report | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md) |
| Audit | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md) |
| Preflight | [site-002-visual-polish-pass1-work/preflight-manifest.json](../reports/site-002-visual-polish-pass1-work/preflight-manifest.json) |
| Deploy manifest | [site-002-visual-polish-pass1-work/deploy-manifest.json](../reports/site-002-visual-polish-pass1-work/deploy-manifest.json) |
| Patch source | [site-002-visual-polish-pass1-work/site-002-corp-visual-polish-pass1.css](../reports/site-002-visual-polish-pass1-work/site-002-corp-visual-polish-pass1.css) |
| Backup | [backups/style.css.pre-site-002-corp-visual-polish-pass1.bak](../backups/style.css.pre-site-002-corp-visual-polish-pass1.bak) |
