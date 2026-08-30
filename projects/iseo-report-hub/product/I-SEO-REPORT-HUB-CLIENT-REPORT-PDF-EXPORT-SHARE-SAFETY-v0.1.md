# I-SEO Report Hub — Client Report PDF / Export / Share Safety v0.1

**Status:** CHARTER / SAFETY POLICY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01

---

## 1. Issued artifacts (frozen)

| Export id | Key | Format | Policy |
|-----------|-----|--------|--------|
| 1 | `snapshot-1-html-v1` | html | Do not rewrite |
| 2 | `snapshot-1-pdf-v1` | pdf | Do not rewrite |
| 3 | `snapshot-1-html-v2` | html | Do not rewrite |
| 4 | `snapshot-1-pdf-v2` | pdf | Do not rewrite; checksum prefix `a8c4d61c6216e8d70b19` must stay |

No new export rows in Implementation 01. No artifact file edits. No Edge PDF run.

---

## 2. Shares

| Rule | Value |
|------|--------|
| Create | **Forbidden** in this charter and in Impl 01 |
| Revoke | **Forbidden** |
| Token print | **Forbidden** |
| Active share | Must remain active (context: 1 active / 6 revoked / 7 total; likely id **7**) |
| Public route | Keep streaming the **existing** PDF file for the current share |

Public share is **not** a live template. Template/preview CSS changes cannot break the binary PDF. They also **cannot** update what the client already downloads.

---

## 3. Dynamic vs static

| Surface | Class | Restyle in Impl 01? | Affects active share? |
|---------|-------|---------------------|------------------------|
| `/monthly-reports/{id}/preview` | Dynamic, auth | **Yes** (target) | No |
| `/preview/print` | Dynamic, auth | Yes (same template) | No |
| Export detail / shares UI | Dynamic, admin | No | No |
| Assembly preview | Dynamic, admin | No | No |
| HTML/PDF files 1–4 | Static artifacts | **No** | Share uses PDF 4 |
| `/share/report/{token}` | Static file stream | **No** | Unchanged bytes |

If a future wave adds a **dynamic HTML public view**, that would affect the live share URL behaviour and needs its own safety + visual smoke. That view **does not exist** today.

---

## 4. Implementation 01 hard gates

Forbidden:

- PDF regeneration;
- `POST` export HTML/PDF/styled routes;
- share create/revoke;
- DB writes to `report_exports`, `report_export_shares`, `report_snapshots`, `report_blocks`, `monthly_report_contents`, work entries;
- `.env` edits;
- runtime sync **unless** an explicit later implementation charter copies preview templates (this charter: **no runtime sync**);
- production ops;
- token/secret printing.

Allowed in Impl 01 (when that wave starts): app-source view/css/service for preview document only + validation GET.

---

## 5. Future PDF regeneration proof

Required separate wave, suggested name:

**`I-SEO Report Hub — Client Report PDF Regeneration Proof 01`**

Rules:

- backup/evidence under Storage, not git;
- create a **new** test export (next version key, new id);
- **do not overwrite** export **4**;
- new checksum is expected for the **new** row only;
- export **4** checksum remains the baseline for the current active share;
- do not attach the new PDF to the existing active share unless an explicit share-cutover charter says so;
- prefer leaving share **7** on PDF **4** until operator accepts the new visual PDF.

---

## 6. Preview visual smoke (Impl 01)

GET-only after login:

- `/health` 200;
- `/monthly-reports/1/preview` 200;
- no DB count change;
- export 4 checksum unchanged;
- share counts unchanged.

Do not fetch `/share/report/{token}` in a way that prints the token. Optional HEAD/GET with a token from a **local secret store** is operator-only; agents must not log it.

---

## 7. Rollback

Impl 01 is view/css. Rollback = revert those app-source files. Issued PDF/share rows are untouched, so delivery rollback is unnecessary if gates hold.
