# I-SEO Report Hub — Client Report Export HTML Acceptance v0.1

**Status:** CHARTER / ACCEPTANCE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

Applies to:

**`I-SEO Report Hub — Client Report Export HTML Alignment Implementation 01`**

---

## 1. Hard gates (must PASS)

| Gate | Criterion |
|------|-----------|
| DB mutation | None (no content/export/share/snapshot/block/work-entry writes for product state) |
| Export count | Unchanged (local baseline **4**) |
| Share count | Unchanged (baseline **7** total / **1** active / **6** revoked unless operator changed outside this track — re-probe and record) |
| Export 4 | Checksum prefix `a8c4d61c6216e8d70b19` and size `117055` unchanged; file SHA matches DB |
| `/report-exports/4` | Still 200 (auth) |
| `/report-exports/4/shares` | Still 200 (auth) |
| `/monthly-reports/1/preview` | Still 200 (auth); client document intact |
| PDF | No regeneration |
| Production | No production ops |
| Secrets | No share token / password / `.env` values printed |

---

## 2. Evidence HTML gates (must PASS)

Generated Storage evidence HTML must show:

| Check | Criterion |
|-------|-----------|
| Style | Client document composition (cover + IA sections + footer) |
| Admin chrome | No sidebar / top admin shell |
| Technical leakage | No ids/keys/checksums/tokens/snapshot diagnostics |
| Markers | No `LOCAL_FIXTURE_ONLY` / `MARS_FIXTURE` |
| IA order | Target six sections in order |
| CSS | Embedded CSS suitable as future PDF source |
| Local demo banner | Off in export-safe mode |
| Fake KPI | Absent |
| Empty sections | Honest empty states |

---

## 3. Code gates

| Check | Criterion |
|-------|-----------|
| `ReportTemplateRenderer` | Left intact for existing create behavior |
| Create routes | Not required to switch default in Impl 01 |
| Writes under `storage/exports/` | Forbidden |
| New export row | Forbidden |

---

## 4. Explicit non-claims

Impl 01 success does **not** mean:

- client PDF is ready;
- public share looks new;
- styled create UI produces client HTML by default.

Those require later PDF Proof + optional wiring + share handoff.
