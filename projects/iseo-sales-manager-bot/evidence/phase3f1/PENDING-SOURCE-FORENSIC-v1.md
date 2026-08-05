# PENDING SOURCE FORENSIC v1

**Question:** what field(s) in `lead_clean_v2` are the authoritative source of "pending" for a business lead, given the CLEAN schema carries both a Phase 3D.3 `lifecycle_status` column and later manager-facing `manager_status` usage?

## Finding

Live callback/lifecycle mutation (`Update CLEAN Lifecycle`, per `implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md` §Phase 3D.3) writes `manager_status` on the CLEAN row as the current operational field managers and Admin/Bot read. `lifecycle_status` (added in the Phase 3D.3 65-column migration, see `implementation/SHEETS-MIGRATION-SPEC-v1.md` §3.1) remains present as a secondary/compatibility field on rows written by that generation of the schema.

## Authoritative rule (adopted)

1. Primary: `manager_status` — `pending` \| `processed` \| `spam`.
2. Secondary: `lifecycle_status` — read only when `manager_status` is absent/blank.
3. `close_reason` — treated as a tertiary signal (`spam` / `processed`) for rows predating both columns.
4. Legacy rows with **none** of the above populated are treated as **pending** (they represent leads Olya has not yet closed) unless a close signal is present.

This mirrors `resolveLifecycle()` in `implementation/runtime-libs/pending-leads-lib.mjs`:

```js
export function resolveLifecycle(r) {
  const primary = String(r.manager_status || '').trim().toLowerCase();
  const secondary = String(r.lifecycle_status || '').trim().toLowerCase();
  const close = String(r.close_reason || '').trim().toLowerCase();
  for (const raw of [primary, secondary]) {
    if (raw === 'processed' || raw === 'spam') return raw;
  }
  if (close === 'spam') return 'spam';
  if (close === 'processed') return 'processed';
  return 'pending';
}
```

## Exclusions before a row counts as a pending business lead

| Exclusion | Rule | Rationale |
|---|---|---|
| Technical retry rows | `row_kind`/`record_kind`/`entry_type` = `technical_retry`/`retry_only`/`tech_retry`, or `technical_retry`/`is_technical_retry` flag | Not a business lead — infrastructure artifact |
| Probable invalid/empty shell rows | No business key **and** no name/site/summary/phone/email | Malformed row, not a real lead |
| Probable test rows | `is_probable_test`/`probable_test` flag, `SYNTHETIC_TEST` marker, `PHASE_3*` phase marker, or name/summary containing test/synthetic/stabilization signals (reuses the Phase 3E.2.2 probable-test exemption logic) | Keeps operator/harness fixtures out of the business count by default |
| Processed/spam | per `resolveLifecycle()` above | Already closed by a manager |

## Harness coverage

Checks 1–7, 43–44 in `implementation/harness/phase3f1-harness.mjs` (Pending lifecycle included, Processed excluded, Spam excluded, Test excluded by default, Legacy compatibility pending, Missing timestamp safe, Processed/Spam lead disappears from the view after lifecycle change).

*Related: [PENDING-VIEW-CONTRACT-v1.md](PENDING-VIEW-CONTRACT-v1.md), [../../architecture/PENDING-LEADS-VIEW-v1.md](../../architecture/PENDING-LEADS-VIEW-v1.md).*
