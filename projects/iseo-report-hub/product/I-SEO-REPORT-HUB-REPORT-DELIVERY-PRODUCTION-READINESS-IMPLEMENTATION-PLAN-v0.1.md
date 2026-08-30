# I-SEO Report Hub — Report Delivery Production Readiness Implementation Plan v0.1

**Status:** PLAN ONLY — this wave is documentation; no production implementation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Report Delivery Production Readiness Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-VALIDATION-PLAN-v0.1.md)

---

## 1. Nature of this wave

**No-code.** Production Readiness Charter 01 creates policy docs only.

Forbidden in this and any future wave unless separately chartered and operator-approved:

- production deployment;
- push;
- inventing hosting/domain without operator decision;
- DB mutation on prod or local without charter;
- silent `.env` changes.

---

## 2. Recommended next wave

### Selected: `I-SEO Report Hub — Production Environment Charter 01`

**Goal:** Operator-facing decision package for hosting / domain / HTTPS / runtime / DB / deploy topology — still docs/policy first; **no** provisioned infra unless a later apply charter says so.

**Must cover:**

| Topic | Content |
|-------|---------|
| Options | A local-only pilot; B shared hosting; C VPS; D containers — compare with constraints |
| Recommendation discussion | Prefer operator choice between **B** and **C** |
| Domain + HTTPS | Stable public hostname; TLS required for share URLs |
| Runtime | PHP version pin; MySQL; webserver; docroot=`public/` |
| PDF | Edge/headless compatibility probe plan on candidate host |
| Storage | Artifacts/logs outside public webroot |
| Deploy model | Model A source → runtime; release hash; allowlist sync |
| Secrets contour | Production env file location (not Git) |
| STOP | No deploy until Environment Charter accepted **and** subsequent deploy charter approved |

---

## 3. Alternative waves (not immediate)

| Wave | When |
|------|------|
| `Report Delivery DB-11 Delivery Events Charter 01` | Only if operator confirms durable delivery tracking need |
| `Real Client Data Model Charter 01` | After or parallel to Environment Charter when moving off fixtures |
| `Production Backup/Restore Charter 01` | After environment chosen; before first real deploy |
| `Report Delivery Production Readiness Implementation 01` | **Not recommended yet** — would be premature checklist tooling without environment decision |

---

## 4. Minimum production checklist (for future deploy charter)

Use as gate list — not executed now:

1. Branch / release hash recorded (`mars/canonical-post-recovery` or tagged release).
2. `APP_ENV=production`; display_errors off; debug off.
3. HTTPS `APP_URL` / public base URL for share links.
4. Session/cookie secure settings.
5. Production DB + least-privilege user; migrations dry-run then backup-gated apply.
6. Fixture data absent or clearly segregated from real clients.
7. Storage + logs + exports outside `public/`.
8. Public share route smoke over HTTPS (create once → download → revoke → 410).
9. Auth/CSRF smoke on internal share create/revoke.
10. Backup dump + restore drill attested.
11. `/health` reachable; error logging verified.
12. Rate limiting / webserver throttling plan for token route documented.
13. Access-log privacy policy for share URLs accepted.
14. Explicit operator approval to deploy; **no** push/deploy by default agent habit.

---

## 5. Deployment strategy requirements (future)

| Requirement | Rule |
|-------------|------|
| Source of truth | Active Brain `app-source/` (Model A) |
| Release identity | Exact Git hash / tag |
| Build artifacts | Prefer source sync; no hand-edit of runtime after sync |
| `.env.production` | Local secret contour only — **never** commit |
| Migrations | Dry-run → backup → apply → verify `schema_migrations` |
| Rollback | Code hash rollback; DB rollback policy; revoke active shares if delivery affected |
| Docroot | Points only to `public/` |
| Public share | HTTPS only |

---

## 6. STOP conditions for future production work

STOP and report if:

- environment / domain / HTTPS not selected;
- production DB target unclear or equals `iseo_report_hub_dev`;
- secrets would be written into Git;
- backup/restore not tested when charter requires it;
- fixture data would be exposed on production domain;
- foreign WIP / staged index blocks safe scoped commit;
- operator has not approved deploy charter;
- request implies push without explicit approval.

Tokens:

- `STOP — PRODUCTION ENVIRONMENT NOT SELECTED`
- `STOP — PRODUCTION SECRETS / ENV CONTOUR UNDEFINED`
- `STOP — BACKUP RESTORE NOT ATTESTED`
- `STOP — FIXTURE DATA ON PRODUCTION PATH`
- `STOP — DEPLOY NOT OPERATOR-APPROVED`

---

## 7. Sequence recommendation

```text
Production Readiness Charter 01 (this wave — docs)
    → Production Environment Charter 01 (docs/decision)
        → Backup/Restore Charter + Real Client Data Model (as needed)
            → Production Deploy / Apply Charter (operator-approved only)
```

DB-11 / portal / email remain off this critical path unless operator inserts them.
