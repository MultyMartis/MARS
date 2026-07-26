# I-SEO Report Hub — Report Snapshot Design v0.1

**Status:** DESIGN / PLANNING ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-SCHEMA-PLAN-v0.1.md)

---

## 1. Snapshot definition

A **report snapshot** is the frozen internal representation of a finalized monthly report at a specific moment.

It is:

- internal-only;
- created from a finalized monthly report;
- read-only after creation;
- based on preview/render composition;
- intended as future source for export/PDF/share layers;
- **not** itself a PDF;
- **not** public;
- **not** client portal;
- **not** external delivery.

It preserves:

- report metadata;
- period / client / project / site context;
- monthly report content status / title / finalized_at;
- render mode;
- ordered block payload;
- source weekly checkpoint references;
- diagnostics / render checksum;
- generated_at / snapshot_created_at (column; not in checksum identity by default);
- actor user id;
- version number.

---

## 2. Data sources

| Source | Role in snapshot |
|--------|------------------|
| `monthly_report_contents` | Parent identity, title, status, finalized_at, flat fields, source weekly ids |
| `reporting_periods` | Period key/dates/status |
| `clients` / `projects` / `sites` | Context metadata (ids + safe display fields) |
| `report_blocks` | Ordered non-archived block content for `blocks_primary` |
| `weekly_checkpoints` | Resolve / embed weekly source refs |
| `ReportPreviewService` composition | Canonical render mode + ordered sections + diagnostics |
| Actor / auth session | `created_by` |

Live mutable rows remain editable only after reopen; snapshot rows never mutate content fields after insert (status transitions only: active → superseded / archived).

---

## 3. Payload design

`payload_json` (JSON NOT NULL) structure:

```json
{
  "metadata": {},
  "period": {},
  "client": {},
  "project": {},
  "site": {},
  "monthly_report": {},
  "blocks": [],
  "weekly_sources": [],
  "diagnostics": {},
  "render": {}
}
```

### Recommended field content

| Section | Include |
|---------|---------|
| `metadata` | snapshot schema version string (e.g. `1`); monthly_report_content_id; reporting_period_id |
| `period` | id, period_key, date range, status |
| `client` / `project` / `site` | id, name/slug/safe labels only — no secrets |
| `monthly_report` | id, title, status, finalized_at, flat DB-05 fields used by flat_fallback, source_weekly_checkpoint_ids |
| `blocks` | ordered array: id, block_key, block_type, status, title, body, summary, source ids, sort_order |
| `weekly_sources` | resolved refs: id, week_key, status (and safe labels) |
| `diagnostics` | render_mode, block_count, missing required keys (if any at capture time), composition notes |
| `render` | optional normalized plain-text outline; **not** required to duplicate full HTML |

### Rendered columns

| Column | MVP policy |
|--------|------------|
| `rendered_text` | Optional; may store plain-text composition from trusted renderer |
| `rendered_html` | Prefer **null** in first implementation; if set later, only escaped/trusted renderer output — no raw user HTML |

Do not store huge unused HTML.

---

## 4. Checksum design

- Algorithm: **SHA-256** hex (`checksum_sha256` CHAR(64)).
- Input: canonical normalized JSON of checksum-relevant payload.
- Canonical JSON order defined by `ReportSnapshotService` (stable key sort / stable block order by sort_order then id).
- Include enough to detect rendered content changes:
  - monthly id;
  - reporting period id/key/dates;
  - report title/status/finalized_at;
  - ordered blocks id/key/type/status/title/body/summary/source ids/sort_order;
  - weekly refs.
- **Exclude** volatile `snapshot_created_at` / `generated_at` from checksum unless intentionally part of identity (MVP: exclude).
- Store `created_at` separately on row.

Purpose: idempotency + later source-vs-snapshot drift comparison.

---

## 5. Versioning

| Rule | Policy |
|------|--------|
| First snapshot for monthly | `version = 1` |
| After reopen + re-finalize + new snapshot | `version = N+1` |
| Unique | `(monthly_report_content_id, version)` |
| Active cardinality | App enforces **one** `active` per monthly; prior active → `superseded` |
| Snapshot key | `monthly-{monthly_report_content_id}-v{version}` (unique, slug-safe) |

Alternative key `{period_key}-monthly-report-v{version}` allowed if uniqueness still guaranteed; preferred MVP: id-based key to avoid period_key collisions across projects if multi-tenant expands.

---

## 6. Lifecycle

Statuses: `active` | `superseded` | `archived`

| Transition | When |
|------------|------|
| → `active` | on create (new version) |
| `active` → `superseded` | when newer active version created |
| `active`/`superseded` → `archived` | admin archive (not MVP-required) |

All rows immutable for payload/checksum/title/render fields after insert. No hard delete. No rebuild-in-place of same version — create new version instead.

---

## 7. Routes (future implementation)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/monthly-reports/{id}/snapshot` | Show active snapshot or “no snapshot yet” |
| POST | `/monthly-reports/{id}/snapshot` | Create snapshot from finalized report |
| GET | `/report-snapshots/{id}` | View snapshot detail |
| GET | `/report-snapshots/{id}/compare-source` | Optional later hardening only |

No public route. No PDF/export route. No delete route. Auth + CSRF on POST.

---

## 8. Services / repositories

| Component | Responsibility |
|-----------|----------------|
| `ReportSnapshotService` | Gates; build payload; checksum; version resolve; idempotency; supersede; audit |
| `ReportSnapshotRepository` | Persist/retrieve by id, monthly, active version |
| `ReportPreviewService` | Composition source for payload |
| Finalization / monthly status checks | Gate: must be finalized |

Audit events recommended:

- `report_snapshot.created`
- `report_snapshot.idempotent_hit`
- `report_snapshot.superseded`
- `report_snapshot.archived`
- `report_snapshot.creation_failed`

Payload: snapshot_id; monthly_report_content_id; reporting_period_id; version; checksum_sha256; actor user id; gate failures if any; **no secrets**.

---

## 9. UI integration

### Monthly report detail

Snapshot card:

- status: no snapshot / active snapshot exists;
- version; checksum short; created_at; created_by;
- **Create snapshot** if finalized and no active for current checksum;
- if not finalized: blocked reason.

### Preview page

Snapshot state cue: no snapshot / active exists / (later) source differs from snapshot.

### Snapshot detail

Immutable view: metadata; rendered text/html; ordered blocks; source refs; checksum; version; links back to monthly report / preview.

---

## 10. Access model

| Role | Create | View | Archive (later) |
|------|--------|------|-----------------|
| `admin_owner` | yes | yes | yes |
| `seo_lead_reviewer` | yes (after finalized) | yes | no (unless later charter) |
| `seo_specialist` | no | yes | no |
| `account_client_manager` | no | yes (internal MVP) | no |
| `internal_viewer` | no | yes | no |
| `client_viewer` | no | no | no |

---

## 11. Idempotency

Recommended MVP:

1. Build payload + checksum for current finalized state.
2. If active snapshot exists with same checksum → return it; audit `idempotent_hit`; no new row.
3. If active exists with different checksum → refuse unless explicit new-version after reopen/re-finalize path (preferred: require finalized state that differs; create vN+1 and supersede).
4. If no active → create v1 or next version.

Do not create duplicate rows for identical checksum.

---

## 12. No-public / no-PDF policy

- Snapshot is **not** client delivery.
- Snapshot is **not** PDF binary.
- Future export/PDF must depend on snapshot (or explicit later charter), not live draft tables.
- Public/token publish remains governed by separate publishing model — out of this MVP snapshot layer.
- Print route (`/preview/print`) remains browser print of live preview; not snapshot export.
