# I-SEO Report Hub — Report Delivery / Public Share Implementation Plan v0.1

**Status:** PLAN ONLY — no code / migration / tokens in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Delivery / Public Share Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-DESIGN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md)

---

## 1. Recommended next wave

**I-SEO Report Hub — Report Delivery Public Share DB-10 Migration Apply 01**

Split rationale:

1. **DB-10 first** — create `report_export_shares` with empty table; validate schema only; no tokens; no public route.
2. **Implementation second** — service/UI/routes after schema is durable.

Optional intermediate naming if operator wants a separate schema charter:  
`Report Delivery Public Share DB-10 Charter / Migration Apply 01` — **not required** if this pack is accepted as sufficient policy.

---

## 2. DB-10 table plan

Table: `report_export_shares`

| Column | Notes |
|--------|-------|
| `id` | PK |
| `report_export_id` | FK → `report_exports(id)` **RESTRICT** |
| `token_hash` | unique; plaintext never stored |
| `token_label` | nullable |
| `status` | `active` / `revoked` / `expired` |
| `expires_at` | required for MVP |
| `revoked_at` | nullable |
| `revoked_by` | FK → `users(id)` **SET NULL** |
| `created_by` | FK → `users(id)` **SET NULL** |
| `created_at` | required |
| `last_accessed_at` | nullable |
| `access_count` | default 0 |
| `max_access_count` | nullable (unused in MVP enforcement) |
| `last_access_ip_hash` | nullable |
| `last_user_agent_hash` | nullable |
| `metadata_json` | nullable |

Indexes:

- unique `token_hash`
- `(report_export_id, status)`
- `(expires_at, status)`
- `created_by`
- `revoked_by`

DB-10 wave constraints:

- local DB `iseo_report_hub_dev` @ `127.0.0.1` only;
- **no** share rows seeded;
- **no** public route;
- **no** artifact / `report_exports` row mutation beyond schema FK target existence;
- expected after apply: migrations **9**, tables **16** (policy expectation — confirm in DB-10 wave).

---

## 3. Follow-up implementation wave

**I-SEO Report Hub — Report Delivery Public Share Implementation 01**

Deliver:

- share service / repository / controller;
- token create + revoke;
- public stream route;
- internal UI cards;
- smoke + security checks per validation plan.

---

## 4. Source areas (future implementation)

Expected Model A touch points (not modified in this charter):

| Area | Likely paths |
|------|----------------|
| Routes | `app-source/app/routes.php` |
| Controllers | new share controller and/or extend `ReportExportController.php` |
| Services | new `ReportExportShareService` (+ reuse export path/checksum helpers from `ReportExportService.php`) |
| Repositories | new `ReportExportShareRepository` (+ read `ReportExportRepository`) |
| Views | `report-exports/show.php` (+ optional list / snapshot / monthly badges) |
| Migrations | new DB-10 SQL under `app-source/database/migrations/` |
| README | status / next stage notes |

Runtime sync: exact-path source → Localhost only under implementation / migration charters.

---

## 5. Routes (implementation target)

Internal:

- `GET /report-exports/{id}/shares`
- `POST /report-exports/{id}/shares`
- `POST /report-export-shares/{id}/revoke`

Public:

- `GET /share/report/{token}`

Deferred:

- `GET /r/{token}`

Auth download unchanged:

- `GET /report-exports/{id}/download`

---

## 6. Services / repositories

| Component | Responsibility |
|-----------|----------------|
| Share repository | CRUD/list by export; find by token hash; revoke; access counters |
| Share service | Eligibility; token mint (hash store); expiry; revoke; public resolve; audit hooks |
| Export service reuse | Path hardening, checksum, MIME/PDF gates |
| Auth/RBAC | Role gates for create/revoke; public route bypasses session |

---

## 7. UI (implementation target)

- Export detail share card: status, expiry, create, revoke, one-time copy link.
- Eligibility-gated create button (PDF styled ready only).
- Optional: export list badge; snapshot/monthly “shareable PDF available”.
- No portal; no email UI; no public HTML preview.

---

## 8. Smoke (implementation target)

Minimum smoke themes:

- create share for export id **4**;
- public token download succeeds once;
- revoke → denial;
- expired → denial (fixture or clock stub per wave);
- legacy id **2** / HTML id **3** create denied;
- checksum / missing artifact denied;
- auth downloads still pass;
- `/share` without token remains non-listing;
- headers present on success.

Exact case counts defined in implementation / validation execution reports.

---

## 9. STOP conditions

STOP implementation / migration waves if:

- wrong DB host/name;
- foreign i-SEO WIP / unsafe staged index for i-SEO paths;
- attempt to put artifacts in public docroot;
- plaintext tokens persisted;
- export id embedded as sole public capability;
- HTML share enabled without new charter;
- package install required without charter;
- push requested without operator authorization.
