# I-SEO Report Hub — Client Report Visual Acceptance v0.1

**Status:** CHARTER / ACCEPTANCE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Client Report Template Visual Alignment Charter 01  
**Applies to:** Client Report Template Visual Alignment Implementation 01

---

## 1. Route / page

| Check | Pass if |
|-------|---------|
| `GET /health` | 200 |
| `GET /monthly-reports/1/preview` | 200 (authenticated internal) |
| `GET /monthly-reports/1/preview/print` | 200 |
| Routes unchanged | No new public share route required |

---

## 2. Client document (preview)

| Check | Pass if |
|-------|---------|
| Admin sidebar / topbar | Absent (not merely `display:none` on screen) |
| Edit / apply / assembly / snapshot / block-CRUD controls | Absent from the document |
| Technical ids | No visible monthly/snapshot/export/block ids, `block_key`, checksums |
| Weekly source dump / diagnostics `<details>` | Absent from client document |
| Six shells | Present as RU headings in Target IA order: резюме → результаты → что сделали → выводы → риски → план |
| Empty/manual | Calm empty note; no red error banners; no fake KPI |
| Fixture markers | No raw `LOCAL_FIXTURE_ONLY` in the document |
| Brand | Light paper, ink `#18181B`, yellow accent `#facc15`, no dark admin chrome |
| Print CSS | `@media print` and/or `@page` present; operator strip `.no-print` |
| Optional operator strip | At most back-to-monthly (+ print); `no-print` |

---

## 3. Safety

| Check | Pass if |
|-------|---------|
| DB counts | Unchanged vs pre-wave baseline (periods 2; monthly 2; report 1: 6 blocks / 7 entries; report 5: 0/0; fixture marker rows 0; exports 4; shares 7 / active 1 / revoked 6) |
| Export 4 checksum | Prefix `a8c4d61c6216e8d70b19` unchanged (full hash unchanged) |
| PDF bytes | Unchanged |
| Share rows | No create/revoke; active share still active |
| New export rows | 0 |
| Secrets / tokens | None in diffs, docs, logs |

---

## 4. Out of scope (do not fail Impl 01)

- Pixel match of issued PDF 4 (it will still look like the old export).  
- Public share HTML restyle.  
- Metrics widgets.  
- Full admin screenshot QA.  
- Manrope loaded if no local font yet (system sans + tokens is acceptable).  

---

## 5. Verdict language

Implementation 01 closeout should use one of:

- `CLIENT REPORT VISUAL ALIGNMENT IMPLEMENTATION PASS`
- `CLIENT REPORT VISUAL ALIGNMENT IMPLEMENTATION PASS_WITH_MINOR_ISSUES`
- `CLIENT REPORT VISUAL ALIGNMENT IMPLEMENTATION ATTENTION`
- `STOPPED`
