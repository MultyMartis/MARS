# I-SEO Report Hub — Summary Assembly Apply UI Cleanup 01 Result v0.1

**Status:** IMPLEMENTED (local UI cleanup; no DB write)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply UI Cleanup 01  
**Verdict:** `SUMMARY ASSEMBLY APPLY UI CLEANUP PASS`

Operator screenshot of `/monthly-reports/1/assembly-preview` showed a correct locked apply state that looked like a debug failure: repeated red warnings, fixture/current markers in the open comparison, and draft text competing with technical panes. This wave cleans the manager-facing layout. Apply protection is unchanged.

---

## 1. Operator issue

| Item | Before |
|------|--------|
| Apply protection | Correct — report 1 finalized, apply disabled, POST refused |
| Visual | Too many red banners; per-block overwrite warnings looked like errors |
| Comparison | `Сейчас в отчете` and draft panes open; `LOCAL_FIXTURE_ONLY` / local markers too visible |
| Hierarchy | Future client text was not the primary card content |

---

## 2. UI cleanup

| Area | Change |
|------|--------|
| Top warning | One amber banner: report finalized, apply blocked, reopen/update/finalize/export needed |
| Per-block red | Removed. Optional muted hint only: `Применение недоступно: отчет финализирован.` |
| Draft | Primary heading `Будущий текст блока` + yellow draft box |
| Current body | `Показать текущий текст отчета` collapsed by default |
| Sources | `Показать источники работ` collapsed by default; ids/categories only inside |
| Local markers | Not shown in the normal card; nested technical current text if expanded |
| Manual blocks | Unchanged role; current text collapsed; no apply controls |
| Bottom apply | Calm locked copy; disabled confirm/button; no working POST form |

Apply service, routes, repository writes, and finalized POST refusal are unchanged.

---

## 3. Files

| Path | Role |
|------|------|
| `app-source/app/Views/pages/monthly-reports/assembly-preview.php` | Manager layout |
| `app-source/public/assets/css/app.css` | Amber locked state, primary draft box, collapsed details |

JS not changed. No `.env`, storage, export, PDF, vendor, DB, or WordPress files.

---

## 4. Validation

PHP lint OK. GET routes 200. UI assertions PASS. POST `/monthly-reports/1/assembly-apply` → **302** to assembly preview. DB counts unchanged (periods 2, monthly 2, fixture marker rows 0, report 1 blocks 6 / entries 7, report 5 0/0, exports 4, shares 7 / active 1 / revoked 6, export 4 prefix `a8c4d61c6216e8d70b19`). Block body SHA and `updated_at` max unchanged.

---

## 5. Remaining debt

- Client Report Template Visual Alignment  
- Metrics model for `results_summary`  
- Screenshot QA of all pages when the operator sends shots  
- Optional operator click-through of apply on a non-finalized report  

---

## 6. SAFE UNKNOWN

- Whether a later charter will add a simple/technical toggle beyond native `<details>`.
