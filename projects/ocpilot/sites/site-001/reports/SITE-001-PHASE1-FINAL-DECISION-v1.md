# SITE-001 — Phase 1 Final Decision v1

**Type:** Phase 1 brand replacement — final acceptance gate decision  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Inputs:** [SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) · [SITE-001-W1G-SEO-DB-CLEANUP-v1.md](SITE-001-W1G-SEO-DB-CLEANUP-v1.md) · [SITE-001-PHASE1-FINAL-AUDIT-v1.md](SITE-001-PHASE1-FINAL-AUDIT-v1.md) · [SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md)

---

## Decision

# **PHASE 1 ACCEPTED WITH NOTES**

---

## Rationale

### Why not PHASE 1 ACCEPTED (unqualified)

1. **Product detail pages** — used-car and new-car PDP URLs are **not HTTP-verifiable** on TEST (zero discoverable product links; new-car direct probe 404). W1G confirms DB remediation for 203 new-car meta rows, but live PDP `<title>` sign-off remains **open**.
2. **Mail identity legacy** — `config_mail_smtp_username` and `anketa.php` punycode sender remain **deferred W1F-D** (CRITICAL for production mail).
3. **Inactive backup artefacts** — `backup_yml/` copies and backup templates remain **deferred W1F-E** (LOW public risk; activation risk if not cleaned before prod).
4. **Production deployment** — **NOT AUTHORIZED**; TEST-only evidence.

### Why not PHASE 1 NOT ACCEPTED

1. All authorized execution waves **W1A through W1G completed successfully** on TEST.
2. Final acceptance HTTP scan: **13/13 required URLs CLEAN** for forbidden legacy dictionary (2026-06-09).
3. Prior interim audit **FAIL** on `/auto/` is **remediated** by W1G — title and meta description now show **СИБКАР**.
4. Visible **СИБКАР** branding confirmed on homepage, header, legal pages, category surfaces, logos, favicon.
5. Remaining gaps cluster in **documented deferred items** (mail, backups, PDP HTTP gap) — not widespread visible body branding failure.
6. Rollback path documented; no production writes occurred.

### Why PHASE 1 ACCEPTED WITH NOTES (selected)

Matches expected gate when:

- Phase 1 **operational rebrand objectives** on TEST are met for scoped public surfaces
- **W1G closes** the last public HTML legacy hit (`/auto/`)
- Residual items are **bounded, deferred, and non-blocking** for Phase 1 documentation closure
- Operator can proceed to **W1F-D / W1F-E** and Phase 2 planning in parallel

*Note: This decision supersedes the interim label **PHASE 1 COMPLETE WITH NOTES** in [SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md) after W1G execution and final acceptance re-verification.*

---

## Decision matrix

| Criterion | Assessment | Impact |
|-----------|------------|--------|
| W1A–W1G waves executed | **YES** | Supports ACCEPTED |
| 13/13 required URLs legacy-clean | **YES** | Supports ACCEPTED |
| `/auto/` legacy in title/meta | **NO** — remediated W1G | Supports ACCEPTED |
| Visible СИБКАР on primary surfaces | **YES** | Supports ACCEPTED |
| Product detail HTTP verified | **NO** | Notes |
| SMTP / `anketa.php` legacy | **YES — deferred W1F-D** | Notes |
| `backup_yml` inactive copies | **YES — deferred W1F-E** | Notes |
| Production deployment ready | **NO** | Notes |

---

## Conditions for unqualified Phase 1 acceptance

Before declaring **PHASE 1 ACCEPTED** without notes:

1. HTTP-verify at least one used-car and one new-car product detail page — expect **0** legacy dictionary hits
2. Execute **W1F-D** — SMTP username + `anketa.php` sender
3. Execute **W1F-E** — backup YML, backup templates, orphan assets
4. Operator HITL sign-off (**Андрей**) on acceptance record
5. Re-run legacy dictionary on expanded URL set including PDP samples

SMTP may remain a **separate production mail gate** if outbound mail is not in Phase 1 scope — but it blocks **production cutover**, not documentation closure with notes.

---

## Recommended next phase

| Priority | Wave / activity | Scope |
|----------|-----------------|-------|
| **1** | **W1F-D** | `config_mail_smtp_username` · `anketa.php` sender · mail identity verification |
| **2** | **W1F-E** | `backup_yml/` · `productnew_Backup.twig` · orphan legacy assets |
| **3** | **PDP spot-check** | When TEST inventory routable — one used + one new car product URL |
| **4** | **Phase 2 planning** | Parallel documentation — production cutover checklist, DNS, prod URL policy |

**Inspection rule (active):** [OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](../../knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md)

---

## Authorization status

| Action | Status |
|--------|--------|
| Phase 1 TEST rebrand (W1A–W1G) | **EXECUTED** — acceptance recorded |
| W1F-D remediation | **NOT AUTHORIZED** — requires change request |
| W1F-E remediation | **NOT AUTHORIZED** — requires change request |
| Production deployment | **NOT AUTHORIZED** |
| Phase 2 planning | **ALLOWED** — documentation only |

---

## Sign-off

| Role | Name | Status |
|------|------|--------|
| OCPilot acceptance | Agent documentation | **DECISION RECORDED** 2026-06-09 |
| Write approver (HITL) | **Андрей** | **PENDING** — operator acceptance of WITH NOTES gate |

*SITE-001 Phase 1 Final Decision v1 — documentation only; no commit.*
