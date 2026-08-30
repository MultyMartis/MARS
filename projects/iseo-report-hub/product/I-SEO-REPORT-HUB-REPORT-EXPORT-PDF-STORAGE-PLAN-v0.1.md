# I-SEO Report Hub — Report Export / PDF Storage Plan v0.1

**Status:** PLANNING ONLY — no files created; no runtime edits; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export / PDF Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md)

---

## 1. Storage root

**Canonical local runtime storage root for exports:**

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\`

Notes:

- Under Localhost runtime project, **outside** `public/` docroot.
- Not under Active Brain Git tree (`X:\AI MARS\projects\iseo-report-hub\`).
- App config should resolve via runtime-relative path (e.g. `storage/exports/reports`) — absolute X: path is the operator-facing canonical location.

---

## 2. Directory layout

```
storage/exports/reports/
  monthly-{monthly_report_content_id}/
    snapshot-{snapshot_id}/
      {snapshot_key}.html
      {snapshot_key}.pdf          # future only
```

Example (fixture):

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html`

Create parent directories on demand during generation. Do not pre-seed empty trees in Git.

---

## 3. File naming

| Rule | Value |
|------|-------|
| Pattern | `{snapshot_key}.{ext}` |
| HTML example | `monthly-1-v1.html` |
| PDF example (later) | `monthly-1-v1.pdf` |
| Charset | ASCII / kebab-safe |
| Forbidden | Cyrillic; spaces; client names; raw report titles; user free-text |

`snapshot_key` is already deterministic (`monthly-{id}-v{n}`).

---

## 4. No-Git policy

- Export artifacts **must not** be committed to `X:\AI MARS`.
- Do not place exports under `projects/iseo-report-hub/app-source/`.
- Do not add export binaries/HTML to monorepo ignore workarounds that encourage commit.
- Runtime `storage/` remains Localhost-only (outside versioned SoT).

If an agent accidentally writes exports into Active Brain: STOP; do not stage; report path.

---

## 5. No-public-webroot policy

Forbidden write/serve locations:

- `public/exports`
- `public/**` any export dump
- desktop/downloads as system SoT
- Active Brain paths
- source repo paths

Serving must **not** rely on Apache alias to storage without auth. Default: no direct URL to storage filesystem.

---

## 6. Authenticated serving

1. Client requests `GET /report-exports/{id}/download` (auth required).
2. Controller loads metadata; checks role.
3. Resolves path from metadata `storage_path` under allowed root only (path traversal reject).
4. Streams file with correct `Content-Type` / `Content-Disposition`.
5. Optional audit `report_export.downloaded`.

No tokenized public download in MVP.

---

## 7. File checksum

| Checksum | Scope |
|----------|-------|
| `source_snapshot_checksum_sha256` | Copied from snapshot row — proves export bound to snapshot identity |
| `checksum_sha256` (file) | SHA-256 of artifact bytes on disk |

On download/smoke: recompute file hash and compare to metadata when status `ready`.

Mismatch → treat as integrity failure (fail closed; do not serve as valid; mark failed / regenerate per policy).

---

## 8. Metadata

Recommended DB table `report_exports` (see Implementation Plan / DB-08):

- stores relative `storage_path`, `filename`, `mime_type`, sizes, checksums, status, actor, timestamps;
- unique `export_key`;
- FK to `report_snapshots` and `monthly_report_contents`.

Minimal alternative (not recommended): filesystem-only without DB — weaker lifecycle/audit; rejected for MVP given snapshot DB precedent.

---

## 9. Cleanup / archive policy

MVP:

- no automatic deletion;
- no `git clean` of storage;
- status `archived` + `archived_at` for soft lifecycle later;
- physical delete only via explicit destructive charter.

Dev fixture notes: exports may accumulate under `monthly-1/snapshot-1/`; operators may wipe Localhost storage manually outside Git — not an agent default action.

---

## 10. Local/dev vs future production

| Concern | Local (now) | Future production |
|---------|-------------|-------------------|
| Disk | Localhost `storage/exports` | Separate durable disk / object store charter |
| Serving | Auth PHP stream | Same auth principle; CDN/public only by explicit publish charter |
| Secrets | No secrets in files | Same |
| Git | Never | Never |

Object storage (S3/Drive) is **out of scope** until separate charter.

---

## 11. Secrets / data policy

- No credentials, tokens, `.env`, or password hashes in export HTML/PDF.
- Corpus credential sheet remains excluded (programme security exclusion).
- Fixture markers `LOCAL_FIXTURE_ONLY` may appear (demo data) — not real client secrets.
- Audit payloads: relative paths only; no absolute path with user home if avoidable; no secrets.
- Do not export real client production data in local MVP without separate data charter.
