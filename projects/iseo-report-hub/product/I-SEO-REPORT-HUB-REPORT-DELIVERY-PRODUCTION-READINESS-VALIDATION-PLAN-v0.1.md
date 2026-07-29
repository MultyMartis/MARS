# I-SEO Report Hub — Report Delivery Production Readiness Validation Plan v0.1

**Status:** VALIDATION PLAN ONLY — not executed in this charter wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Report Delivery Production Readiness Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Purpose

Define validation checks that must pass **before** calling a production deploy “ready”. This plan is for future Environment / Backup / Deploy charters — **not** run in Production Readiness Charter 01.

---

## 2. Validation suites

### 2.1 Source / repo validation

| Check | Pass criteria |
|-------|---------------|
| Branch | Approved release branch / tag |
| Hash | Exact commit hash recorded in deploy evidence |
| Scope | Only allowlisted paths synced; no foreign WIP in release package |
| App-source integrity | No accidental runtime-only drift without import charter |

### 2.2 Environment validation

| Check | Pass criteria |
|-------|---------------|
| Hosting option | Operator-selected and documented |
| PHP / MySQL versions | Match charter pins |
| Docroot | `public/` only |
| Storage / logs / exports | Outside public webroot; writable by app; not listable |
| HTTPS | TLS valid for public domain |
| PDF engine | Probe result documented (available / unavailable + fallback) |

### 2.3 Production `.env` validation

| Check | Pass criteria |
|-------|---------------|
| Not in Git | Confirmed absent from repo |
| `APP_ENV` | `production` |
| Debug / display_errors | off |
| `APP_URL` | HTTPS production base |
| DB target | Production DB name — **not** `iseo_report_hub_dev` |
| Session cookies | Secure / HttpOnly / SameSite per policy |

Do **not** print secret values in reports.

### 2.4 DB migration dry-run

| Check | Pass criteria |
|-------|---------------|
| Dry-run | Migrations apply cleanly on clone/staging |
| Count | Expected `schema_migrations` after apply |
| Tables | Expected table set including `report_export_shares` |
| No fixture bleed | Prod DB not cloned from local fixture without scrub |

### 2.5 DB backup / restore

| Check | Pass criteria |
|-------|---------------|
| Pre-change dump | Exists, access-restricted, not in Git |
| Restore drill | Restored to scratch DB; smoke query OK |
| Rollback policy | Documented for failed migration |

### 2.6 Artifact storage / public webroot

| Check | Pass criteria |
|-------|---------------|
| No public artifacts | No export PDF/HTML under `public/` |
| Path hardening | `..` / absolute / symlink escape rejected |
| Checksums | Match DB before stream |

### 2.7 HTTPS / domain

| Check | Pass criteria |
|-------|---------------|
| Share URL host | Production HTTPS domain |
| HTTP redirect / deny | No production share over plain HTTP |
| Certificate | Valid chain; hostname match |

### 2.8 Public share route

| Check | Pass criteria |
|-------|---------------|
| Valid token | **200** PDF stream; `%PDF`; hardened headers |
| Malformed / invalid | **404** |
| Revoked / expired / max_access | **410** |
| Once URL | Shown once; not reconstructible from DB |
| Token format | Exact 64-hex |
| No landing | No HTML wrapper for success |

### 2.9 Auth / CSRF

| Check | Pass criteria |
|-------|---------------|
| Unauth internal | Redirect / deny |
| Create / revoke | CSRF required |
| Roles | Only allowed roles create/revoke |

### 2.10 Error / log validation

| Check | Pass criteria |
|-------|---------------|
| No stack traces to clients | Production errors generic |
| App error log | Writable; sample error captured in drill |
| Access logs | Token URL sensitivity acknowledged; retention set |
| `/health` | Returns healthy without leaking secrets |

### 2.11 Real data validation

| Check | Pass criteria |
|-------|---------------|
| No fixture labels to clients | Demo / LOCAL_FIXTURE_ONLY absent from client-facing content |
| Client/project/period | Real entities verified |
| Handoff readiness panel | Shows delivery-ready only for intended export |
| Wrong-link drill | Revoke + recreate works |

### 2.12 Rollback validation

| Check | Pass criteria |
|-------|---------------|
| Code rollback | Prior hash restorable |
| DB rollback | Policy executed on scratch or documented irreversible steps |
| Share revoke | Active shares revoked if delivery compromised |

### 2.13 Post-deploy smoke

Minimum suite after first production deploy charter:

1. Login as production admin.
2. Open eligible styled PDF export.
3. Create share (once URL — redact in evidence).
4. Public HTTPS download **200** PDF.
5. Revoke → public **410**.
6. Handoff panel / copy pack visible rules still hold (no path/token_hash leak).
7. `/health` OK.
8. DB counts / migration version recorded.
9. Backup timestamp recorded.

---

## 3. Evidence rules

- Store evidence under `X:\AI MARS STORAGE\incoming\iseo-report-hub\` (or approved prod evidence root) — **not** Git unless explicitly chartered.
- Redact tokens: `[REDACTED_64HEX_TOKEN]`.
- Never commit live tokens, passwords, or full `.env`.

---

## 4. What this charter validates now

Production Readiness Charter 01 validates **only**:

- docs package completeness;
- gates/risks/plans committed;
- no app-source/runtime/DB mutation;
- next action = Production Environment Charter 01.

It does **not** execute suites 2.2–2.13 against production (production does not exist yet).
