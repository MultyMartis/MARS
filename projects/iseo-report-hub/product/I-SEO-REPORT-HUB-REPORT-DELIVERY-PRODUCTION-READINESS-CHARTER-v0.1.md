# I-SEO Report Hub — Report Delivery Production Readiness Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation; no SQL/migration; no share token; no public route change; no artifact regeneration; no production deployment  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Authority:** Operator I-SEO Report Hub Report Delivery Production Readiness Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-GATES-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-RISK-REGISTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-RISK-REGISTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PRODUCTION-READINESS-VALIDATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-IMPLEMENTATION-RESULT-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md)

---

## 1. Purpose

Определить, что означает **production readiness** для слоя Report Delivery в i-SEO Report Hub после завершения Public Share + Client Handoff UX MVP.

Эта волна — **docs/policy only**. Она **не** является production deployment и **не** внедряет инфраструктуру.

Charter фиксирует:

1. Что уже готово к **условному** local / controlled-pilot readiness.
2. Что **нельзя** считать production-ready.
3. Обязательные gates перед production deployment.
4. Риски и ограничения.
5. Проверки security / data / DB / runtime / deployment / backup / access.
6. Следующую implementation/validation волну после charter.

**Production readiness ≠ production deployment.**  
Readiness — документированная готовность к контролируемому production pilot при выполнении gates.  
Deployment — отдельная operator-approved волна после выбора среды.

---

## 2. Current Local MVP Baseline

### Client Handoff UX Visual QA 01

| Item | Value |
|------|-------|
| Primary | `1431192bdfe27562d64ccc2d8d4f35ae9b4a382c` |
| Hash-record | `9720ed5f350ef5a8aa8813d9f23b964970e22fdd` |
| Tip HEAD (charter start) | `ae5589ae8c49afd199235a8f84c60cc01ce4ae7c` |
| Verdict | **PASS** |
| Smoke | **129/129 PASS** |
| BLOCKER / MAJOR / MINOR | **0** / **0** / **0** |
| Prior minors resolved | `UI-REL-STORAGE-PATH`, `UI-LIST-SHARE-LABEL` |
| Evidence | `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-handoff-ux-visual-qa-01\` |

### Client Handoff UX Implementation 01

| Item | Value |
|------|-------|
| Status | **COMPLETE** |
| Implemented | readiness panel; RU copy pack (short / email / internal); once URL; revoke+recreate guidance |
| Explicitly not done | DB tracking; DB-11; public landing; client portal; email automation |
| Smoke | **115/115 PASS** |

### Public Share stack

| Item | Value |
|------|-------|
| DB-10 | applied (`report_export_shares`) |
| Implementation / Hardening / Visual QA | complete |
| Public route | `GET /share/report/{token}` — direct PDF stream only |
| Token | hash only in DB; plaintext URL once; exact 64-hex |
| Denials | malformed/invalid **404**; revoked/expired/max_access **410** |
| Not present | public landing; `/r/{token}`; email; client portal |

### Export / PDF

| Item | Value |
|------|-------|
| Styled PDF v2 | export id **4** shareable |
| Artifacts | v1/v2 HTML/PDF checksums attested unchanged in last QA |
| Storage | outside public webroot (local MVP) |

### Expected local DB state (from last Visual QA; not re-mutated)

| Metric | Expected |
|--------|----------|
| schema_migrations | **9** |
| tables | **16** |
| report_exports | **4** |
| report_export_shares | **6** revoked; active **0** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **6** |
| report_snapshots | **1** |

Data classification: **LOCAL_FIXTURE_ONLY** / demo fixture — **not** production client data.

### Capability summary (local MVP)

- Monthly report workflow: fixture client/project/site/period → finalized monthly → blocks reviewed → snapshot → HTML/PDF exports → styled PDF v2 → public share → client handoff UX → Visual QA **PASS**.
- Public share: direct PDF stream; token hash only; once URL; revoke; expiry/max_access support.
- Client handoff: internal panel; copy pack; revoke+recreate guidance; **no** DB delivery tracking yet.

---

## 3. Production Readiness Definition

Для Report Delivery **production readiness** означает:

| Criterion | Meaning |
|-----------|---------|
| Functional completeness | Workflow достаточен для controlled production pilot (не обязательно full product vision) |
| Security boundaries known | Token model, auth, CSRF, headers, storage/public webroot boundaries documented and locally proven |
| Runtime prerequisites documented | Hosting/domain/HTTPS/PHP/MySQL/storage/.env contour defined **before** deploy |
| DB / data strategy defined | Migration dry-run, fixture segregation, real-client import path |
| Backup / rollback defined | Pre-deploy dump, restore test, code rollback, share revoke on rollback |
| Monitoring / access defined | Logs, minimal share audit, `/health`, manual audit until automation |
| No hidden local-only assumptions | Localhost, fixture data, Edge PDF, Laragon vhost must not be silently treated as production |

**Not** claimed by this charter:

- production hosting selected;
- production domain/HTTPS live;
- production DB created;
- real client data imported;
- email / portal / DB-11;
- automated monitoring/alerting product.

---

## 4. Non-Production Facts

These are **not** all blockers for local MVP, but **are** gates for production:

| Fact | Status |
|------|--------|
| App is local/dev only (Laragon / Localhost) | true |
| DB is local `iseo_report_hub_dev` @ `127.0.0.1` | true |
| Data is fixture / `LOCAL_FIXTURE_ONLY` | true |
| No production hosting selected | true |
| No production domain selected | true |
| No production HTTPS configured | true |
| No production `.env` / secrets contour defined | true |
| No production DB created | true |
| No production backup/restore tested | true |
| No production deployment pipeline | true |
| No user/password policy hardening beyond local MVP | true |
| No production mail delivery | true |
| No client portal | true |
| No DB delivery audit events (DB-11) | true |
| No production monitoring/alerting | true |
| No formal retention/pruning policy for revoked share rows | true |
| No full browser pixel PNG Visual QA for last handoff wave | true (HTML evidence only) |
| Apache `:80` / Laragon vhost state not re-probed in latest QA | SAFE UNKNOWN (smoke used `:8092`) |

---

## 5. Production Gates

Summarize gates A–N (detail in Gates doc):

| Gate | Topic | Status |
|------|-------|--------|
| A | Functional report flow | **PASS** (local MVP) |
| B | Export integrity | **PASS** (local MVP) |
| C | Public share security | **PASS** (local MVP) |
| D | Client handoff UX | **PASS** (local MVP) |
| E | Production environment | **REQUIRED_BEFORE_PRODUCTION** |
| F | Secrets / env | **REQUIRED_BEFORE_PRODUCTION** |
| G | Production DB / migration | **REQUIRED_BEFORE_PRODUCTION** |
| H | Backup / rollback | **REQUIRED_BEFORE_PRODUCTION** |
| I | Access control / users | **REQUIRED_BEFORE_PRODUCTION** |
| J | Monitoring / logs | **REQUIRED_BEFORE_PRODUCTION** |
| K | Data import / real clients | **REQUIRED_BEFORE_PRODUCTION** |
| L | Retention / pruning | **READY_FOR_PLAN** |
| M | Delivery audit DB-11 | **DEFERRED** |
| N | Public landing / portal / email | **DEFERRED** |

**Local MVP readiness:** Gates A–D **PASS**.  
**Production deployment:** blocked until E–K are operator-satisfied; L planned separately; M/N deferred unless explicitly chartered.

---

## 6. Recommended Next Action

**I-SEO Report Hub — Production Environment Charter 01**

Reason:

- Product MVP (export → share → handoff) passed local Visual QA.
- Before any production implementation or deploy, operator must choose hosting / domain / HTTPS / runtime / DB / deploy topology.
- Do **not** invent production infra in this or the next wave without explicit operator decision.

Alternatives (not selected as immediate next):

- Real Client Data Model Charter 01
- Production Backup/Restore Charter 01
- DB-11 Delivery Events Charter 01 (only if operator confirms need)

Environment options to evaluate in next charter (no decision here):

| Option | Summary |
|--------|---------|
| A | Keep local-only / internal workstation pilot |
| B | Shared hosting PHP + MySQL |
| C | VPS PHP-FPM/Nginx/MySQL |
| D | Containerized VPS |

Recommendation for next charter discussion: choose between **B** and **C**; verify Edge/headless PDF compatibility on chosen host; do not decide without operator.

---

## 7. Out of Scope

This charter explicitly excludes:

- app-source / runtime implementation;
- production deployment;
- DB mutation / SQL / migration create-edit;
- share token creation;
- public route changes;
- new infra provisioning;
- domain / hosting decision (deferred to Production Environment Charter);
- DB-11 delivery events;
- client portal;
- email automation;
- public landing page;
- fixture pruning / revoked-row cleanup;
- real client data import;
- push / fetch / pull.

---

## 8. Minimum production prerequisites (policy)

Before any production deploy charter may proceed:

1. Operator-approved environment (domain, HTTPS, PHP/MySQL topology).
2. Production `.env` secret contour **outside Git** (`APP_ENV=production`; debug/display errors off).
3. Production DB created; migrations dry-run; backup before apply; least-privilege DB user.
4. Storage / logs / artifacts **outside** public docroot; docroot = `public/` only.
5. Fixture data segregated or absent; real clients/projects/users defined.
6. Backup + restore test completed and attested.
7. Public share only over **HTTPS** on stable domain.
8. Access control / password policy / admin inventory reviewed.
9. Logging / `/health` / share access_count audit plan accepted.
10. Explicit operator approval for deploy wave (separate charter); **no** push/deploy by default.

---

## 9. Security / data boundaries (carry-forward)

| Boundary | Requirement |
|----------|-------------|
| Auth | Internal routes require auth; CSRF on share create/revoke |
| Token | Hash-only storage; 64-hex; once URL; no reconstruction from DB |
| Public | PDF stream only; no landing; hardened headers; robots noindex/nofollow |
| Paths | Reject traversal; no absolute path in UI/client copy; no public artifact files |
| Integrity | Checksum validation before stream |
| Secrets | No `.env` in Git; no token/hash/secret display |
| Logs | Avoid logging plaintext token / full share URL; treat access logs as sensitive if URLs appear |
| HTTPS | Mandatory for production public share |

---

## 10. SAFE UNKNOWN (at charter time)

- Live re-probe of `iseo_report_hub_dev` during this charter: MySQL connection refused at attempt time — baseline taken from Client Handoff Visual QA 01 docs (expected state above).
- Apache `:80` / Laragon vhost state during `:8092` smoke not re-probed.
- STORAGE smoke script retention preference.
- Whether operator will require DB-11.
- Production hosting/domain choice (operator pending).
- Pixel PNG browser screenshots not produced for last QA (HTML evidence only).
