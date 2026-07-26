# I-SEO Report Hub — Report Export / PDF Validation Plan v0.1

**Status:** PLANNING ONLY — no smoke executed against export (layer does not exist yet)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export / PDF Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Preflight (every future export wave)

| Check | Expected |
|-------|----------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` label `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| i-SEO WIP | clean before start (or charter-allowed paths only) |
| Staged | no `projects/iseo-report-hub/` unless intended; foreign-only → clean worktree |
| DB | `iseo_report_hub_dev` @ `127.0.0.1` only |
| Baseline | Snapshot Implementation complete; snapshot id 1 `active` |
| Restrictions | no push/fetch/pull/reset/clean/stash; no secrets printed |

---

## 2. DB-08 schema validation

After DB-08 Apply:

- `schema_migrations` count +1 (expected **7** if starting from **6**).
- tables +1 (expected **15** if starting from **14**).
- table `report_exports` exists; **0** rows.
- FKs / UNIQUE `export_key` / CHECKs for format/status present as designed.
- No change to: report_snapshots, monthly_report_contents, report_blocks, weekly_checkpoints, reporting_periods counts/content.
- Snapshot id 1 checksum unchanged.

---

## 3. Storage path validation

- Exports root resolves under runtime `storage/exports/reports/` (not `public/`).
- Path traversal attempts rejected.
- Directory layout `monthly-{id}/snapshot-{id}/` created only on generate.
- No files under Active Brain Git paths.

---

## 4. HTML export generation smoke

Recommended future HTML implementation smoke:

1. Confirm snapshot id **1** `active`; key `monthly-1-v1`; checksum `0d0c863c…` (full match).
2. Auth as generate-capable role; POST `/report-snapshots/1/exports/html` (CSRF).
3. Verify `report_exports` row created (`format=html`, `status=ready`).
4. Verify file exists at expected storage path outside public webroot.
5. Verify filename `monthly-1-v1.html`; export_key `snapshot-1-html-v1`.
6. Verify HTML contains snapshot key/version/checksum and escaped block content.
7. Verify no `<script>` / no external CDN / no secrets.

---

## 5. Idempotency smoke

1. Repeat POST HTML export for same snapshot.
2. Expect same export id / export_key; no duplicate ready row for same checksum+format.
3. Audit `report_export.idempotent_hit`.
4. File unchanged (or bit-identical regenerate policy documented).

---

## 6. Authenticated download smoke

1. GET `/report-exports/{id}` → 200 for allowed roles; metadata visible.
2. GET `/report-exports/{id}/download` → 200; correct Content-Type; body matches file.
3. Unauthenticated → redirect/401/403 per app auth pattern.
4. `client_viewer` → denied.

---

## 7. No public access validation

- No route under `/public-exports` or static alias.
- Direct URL guess to `/exports/…` or filesystem path → not served.
- No token query param download in MVP.

---

## 8. File checksum validation

- Metadata `checksum_sha256` equals SHA-256 of file bytes.
- `source_snapshot_checksum_sha256` equals snapshot `checksum_sha256`.
- Tamper test (optional): alter file → download/integrity check fails closed.

---

## 9. Snapshot unchanged validation

Before/after HTML export:

| Entity | Expectation |
|--------|-------------|
| report_snapshots id 1 | unchanged row / checksum |
| monthly_report_contents id 1 | still `finalized`; no field drift |
| report_blocks | still 6 `reviewed` |
| reporting_periods / weekly_checkpoints | counts unchanged |

---

## 10. DB mutation boundaries

| Allowed (HTML wave) | Forbidden |
|---------------------|-----------|
| Insert/update `report_exports` | Mutate snapshots/monthly/blocks/periods/weekly |
| Audit events for export | Admin password/hash changes |
| | `.env` secret changes without charter |

DB-08: schema + migrations bookkeeping only.

---

## 11. Regression smoke

- Snapshot GET/POST still works; idempotent snapshot hit still OK.
- Preview + print still 200 for auth.
- Finalization locks still hold (monthly/block edit denied while finalized).
- Auth login/logout unaffected.

---

## 12. No-PDF validation for HTML wave

- No PDF routes registered.
- No `.pdf` files created.
- `format=pdf` not insertable via HTML UI (or rejected).
- No PDF engine binaries installed by the wave.

---

## 13. Data policy

- Fixture-only content (`LOCAL_FIXTURE_ONLY`) acceptable.
- No real client production data.
- No credentials in HTML or logs.
- No Nikita credential sheet material.

---

## 14. STOP conditions

STOP and report if:

- wrong DB/host;
- snapshot id 1 missing or checksum drifted unexpectedly before start;
- export written to `public/` or Git;
- PDF generated in HTML wave;
- business rows mutated;
- public/unauth download succeeds;
- staged list includes non-allowlisted paths;
- push attempted without charter.

Token: `STOP — I-SEO REPORT EXPORT / PDF SAFETY CONDITION FAILED`
