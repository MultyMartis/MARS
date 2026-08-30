# I-SEO Report Hub — Report Delivery / Public Share Design v0.1

**Status:** DESIGN / POLICY ONLY — no implementation in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Delivery / Public Share Charter 01  
**Related:**
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-SECURITY-MODEL-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-IMPLEMENTATION-PLAN-v0.1.md)
- [I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VALIDATION-PLAN-v0.1.md)

---

## 1. Purpose

Описать product/design модель tokenized public share для finalized report exports: lifecycle, eligibility, roles, routes, streaming, audit, UI — без client portal и без email в MVP.

---

## 2. Share lifecycle

```
eligible export (ready styled PDF)
        │
        ▼
 create share (internal role)
   · generate opaque token
   · store token_hash only
   · set expires_at (default +30d)
   · status = active
   · show plaintext URL once
        │
        ├──────────────┬──────────────────┐
        ▼              ▼                  ▼
   public access    revoke             expire
   (token route)    (internal)         (time)
        │              │                  │
        ▼              ▼                  ▼
 stream PDF if     status=revoked     treat as denied
 still valid       public denial      public denial
 audit access      audit revoke       audit deny
```

States:

| Status | Meaning |
|--------|---------|
| `active` | Valid until expiry / revoke / max access (if later enabled) |
| `revoked` | Operator disabled; public denial |
| `expired` | Past `expires_at` (may be stored or computed at read time) |

MVP: no one-time consume requirement. Optional later: `max_access_count`.

---

## 3. Export eligibility rules

### Shareable (MVP)

All must hold:

- `report_exports.status = ready`
- `format = pdf`
- `template_id IS NOT NULL` (styled / recorded metadata)
- `render_target = pdf_export`
- artifact exists under export storage root
- storage path passes existing hardening (no absolute path escape, inside exports root)
- checksum validates before delivery
- parent snapshot / monthly report still traceable (finalized / active snapshot lineage)

First local target: export id **4** (`snapshot-1-pdf-v2`, `iseo_default_v1 v1`, source HTML id **3**).

Later styled PDFs with the same metadata shape are shareable under the same policy.

### Not shareable (MVP)

- draft / incomplete / non-ready exports;
- archived exports;
- missing artifact or checksum mismatch;
- HTML exports (including styled id **3**);
- legacy v1 without template metadata (ids **1–2**);
- raw storage files / public webroot copies;
- direct public path URLs.

---

## 4. Role / access rules

| Action | Who |
|--------|-----|
| Create share | `admin_owner`, `seo_lead_reviewer` |
| Revoke share | `admin_owner`, `seo_lead_reviewer` |
| View internal share management | internal roles only (same admin surfaces) |
| Public token access | **no login** — opaque token only |

Auth-only download routes (`/report-exports/{id}/download`) remain unchanged and internal.

---

## 5. Data model (design summary)

Recommended table: **`report_export_shares`** (DB-10).

Candidate fields:

- `id`
- `report_export_id`
- `token_hash` (unique)
- `token_label` nullable
- `status` (`active` / `revoked` / `expired`)
- `expires_at`
- `revoked_at`, `revoked_by`
- `created_by`, `created_at`
- `last_accessed_at`, `access_count`
- `max_access_count` nullable (deferred use)
- `last_access_ip_hash`, `last_user_agent_hash` nullable
- `metadata_json` nullable

Not recommended: share columns on `report_exports` (mixes artifact and link lifecycle; one-link limitation).  
Deferred: generic `public_tokens` abstraction.

---

## 6. Internal routes

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/report-exports/{id}/shares` | List / manage shares for export |
| POST | `/report-exports/{id}/shares` | Create share (CSRF; role gate) |
| POST | `/report-export-shares/{id}/revoke` | Revoke share (CSRF; role gate) |

Internal only. No plaintext token re-display after creation response.

---

## 7. Public token route

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/share/report/{token}` | Validate token + stream PDF |

Preferred: opaque token only — **no export id in URL**.

Alternative short route `GET /r/{token}` — **deferred** unless operator requests shorter client URLs.

MVP behavior:

- no public landing / preview HTML page;
- token route downloads/streams PDF directly on success;
- denials return generic **404** or **410** without reason detail.

Validation order (conceptual):

1. resolve share by token hash;
2. status / expiry / revoke / max_access;
3. export ready + PDF eligibility;
4. artifact path / MIME / size / checksum;
5. stream bytes;
6. audit + access_count increment.

---

## 8. Streaming behavior

- Serve through application controller/service — **never** expose storage absolute path;
- use existing export storage root + relative path resolution / hardening;
- validate checksum before stream;
- `Content-Type: application/pdf` (for PDF MVP);
- `Content-Disposition: attachment; filename="…"` (safe basename only);
- conservative cache / nosniff / noindex headers (see security model);
- no directory listing;
- no public docroot writes.

---

## 9. Audit events

| Event | When |
|-------|------|
| `share_created` | Internal create success |
| `share_revoked` | Internal revoke |
| `share_accessed` | Successful public download |
| `share_denied_expired` | Expired token |
| `share_denied_revoked` | Revoked token |
| `share_denied_missing_artifact` | Artifact missing |
| `share_denied_checksum_mismatch` | Checksum fail |
| access_count increment | On successful access |

Do not log plaintext token. Prefer hashed IP / UA if stored.

---

## 10. UI cards

### Export detail (`report-exports/show`)

- share status card (active / revoked / expired counts or latest state);
- create share button **only** for eligible exports;
- expiry display;
- revoke controls for active shares;
- copy link **only** immediately after creation (one-time plaintext).

### Export list (optional MVP+)

- share badge / active count — optional, not required for first implementation.

### Snapshot / monthly show

- indicator: “shareable PDF available” when eligible PDF exists (e.g. id **4**).

No client portal screens. No email compose UI.

---

## 11. Explicit MVP non-goals

- **no** client portal login;
- **no** email sending of PDF/link;
- **no** one-time link requirement;
- **no** HTML public share / public preview page;
- **no** public listing of shares or exports;
- **no** raw storage path or absolute path exposure;
- **no** public webroot artifact placement.

---

## 12. Deferred

- client portal;
- email delivery;
- one-time / max-download enforcement UX;
- short `/r/{token}` route;
- HTML share policy;
- multi-template / multi-client branding of share pages;
- generic public token platform.
