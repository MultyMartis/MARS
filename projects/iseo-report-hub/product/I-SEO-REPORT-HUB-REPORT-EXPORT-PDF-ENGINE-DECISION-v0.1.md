# I-SEO Report Hub — Report Export PDF Engine Decision v0.1

**Status:** DECISION / POLICY — no PDF implementation; no engine install  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md), [I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md](I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md)

---

## 1. Chosen direction

| Decision | Value |
|----------|-------|
| Implement server PDF now? | **No** |
| Next wave | **I-SEO Report Hub — Report Export PDF Engine Probe 01** (read-only / no install) |
| Preferred PDF input source | Existing ready **HTML export artifact** (checksum-aligned to snapshot) |
| Preferred engine candidate after probe | **Headless / controlled local browser** (Edge/Chrome) **only if already available** |
| Fallback if no controllable browser | **STOP** for operator approval before any install (wkhtmltopdf / Composer / browser download) |
| Temporary operator path | Manual browser print from HTML download (not product PDF metadata path) |

---

## 2. Why not direct PDF implementation yet

1. HTML export storage/auth/idempotency just landed; PDF adds process/binary/font risk.
2. No validated local engine inventory yet (Edge/Chrome/wkhtmltopdf/composer presence unknown as product evidence).
3. Composer and binary installs are **denied by default** in this programme without explicit approval.
4. Wrong engine choice now creates rework of routes/service/audit and storage smoke.
5. Probe is cheaper and reversible: docs + environment capture, no DB/PDF mutation.

---

## 3. Preferred source: HTML artifact

Recommended generation chain:

```
report_snapshots (immutable)
  → report_exports HTML (ready, checksum match)
    → PDF bytes
      → report_exports PDF row + storage file
```

Rules:

- Use HTML export only if `status=ready` and `source_snapshot_checksum_sha256` matches snapshot checksum.
- If HTML missing or checksum mismatch: require HTML export first (or fail safely) — do not silently render from live monthly/blocks.
- Alternative (later): render PDF directly from snapshot payload with same content contract — only if HTML path is insufficient; still keep snapshot checksum reference.

Rationale: reuses existing renderer output; reduces duplicate layout code; ties PDF to proven artifact.

---

## 4. Preferred candidate engine after probe

**Headless Chromium / local browser automation** — preferred **if**:

- probe finds a known browser executable (Edge/Chrome preferred);
- path is controllable via allowlist;
- print-to-PDF can be invoked without network fetch of secrets;
- no new npm package install required for MVP path;
- Cyrillic glyphs render with available fonts.

**Not preferred yet:** Dompdf / mPDF (Composer), wkhtmltopdf (unless already present), downloading Chromium via package managers.

---

## 5. Fallback policy

| Probe result | Action |
|--------------|--------|
| Controllable local browser found | Charter PDF Implementation using that executable allowlist |
| wkhtmltopdf already on PATH/known path | May propose wkhtmltopdf as alternative after fidelity smoke charter |
| Only Composer available, no browser/binary | **STOP** — request operator approval for Dompdf or mPDF |
| Nothing suitable | **STOP** — operator must approve install path before implementation |
| Manual print only | Document as interim ops workaround; no PDF `report_exports` automation |

---

## 6. Dependency approval policy

Denied without separate explicit operator charter:

- `composer require` / vendor commit;
- `npm install` / browser downloaders;
- Chromium / Edge / Chrome installer runs by agent;
- wkhtmltopdf installer;
- copying binaries into Active Brain Git;
- enabling unrestricted `proc_open` to arbitrary paths.

Allowed after probe docs (still no install unless approved):

- read-only path existence checks;
- `where.exe` / Test-Path style discovery;
- documenting absolute candidate paths (no secrets).

Any install wave must state: exact package/binary, path, checksum if applicable, rollback, and no public exposure.

---

## 7. Storage / metadata decision (future implementation)

| Field | Planned value (fixture snapshot-1) |
|-------|-------------------------------------|
| Absolute file | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.pdf` |
| Relative `storage_path` | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` |
| `export_key` | `snapshot-1-pdf-v1` |
| `format` | `pdf` |
| `status` | `ready` |
| `mime_type` | `application/pdf` |
| `filename` | `monthly-1-v1.pdf` |
| Checksums | file SHA-256 + copy of snapshot checksum |
| Public / Git / Desktop | **forbidden** |

---

## 8. Access / audit decision (future implementation)

Access (same as HTML):

- create PDF: `admin_owner`, `seo_lead_reviewer`;
- view/download: internal roles except `client_viewer`;
- `client_viewer`: none.

Audit events (recommended):

- `report_export.pdf_created`
- `report_export.pdf_idempotent_hit`
- `report_export.pdf_creation_failed`

Payload: export_id; report_snapshot_id; source_html_export_id; checksums; engine name/version; actor user id; avoid absolute paths; no secrets.

---

## 9. STOP conditions

STOP before PDF implementation if:

- probe not completed;
- no approved engine after probe;
- proposed path requires install without operator approval;
- HTML export missing / checksum mismatch for target snapshot;
- DB target not `iseo_report_hub_dev` @ `127.0.0.1`;
- public/share/token route proposed;
- foreign WIP remediation required to proceed;
- scoped commit cannot be guaranteed.

STOP token for unsafe preflight:  
`STOP — I-SEO REPORT HUB REPORT EXPORT PDF ENGINE CHARTER SAFETY CONDITION FAILED`  
(or probe-specific STOP from Probe 01 charter).
