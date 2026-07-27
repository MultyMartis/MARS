# REPORT — I-SEO REPORT HUB REPORT EXPORT PDF ENGINE CHARTER 01

**Status:** COMPLETE (docs/policy only)  
**project_id:** `iseo-report-hub`  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export PDF Engine Charter 01  
**Primary commit:** `e16fc4149712e1770c7b6dd8c53109469347c018`  
**Hash-record commit:** `22f2f80eaa6fea18bc4a1b3f50a92f45ad74c5ed`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `ce1c095a7d67192e59b764d7b9ea64229e1c48ae` |
| Staged/index before (main) | **non-empty foreign** (`projects/client-ops-reporting-bridge/**` staged) — **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-pdf-engine-charter-01\repo` (detached at `ce1c095a`) |
| i-SEO WIP before | **clean** (`projects/iseo-report-hub/` no modified/untracked on main) |
| Foreign WIP | **preserved** (main index untouched; no unstage/restore of foreign paths) |
| Write scope | Active Brain docs only under allowlisted `product/` + `reports/` + `OPERATIONAL-INDEX.md` in clean worktree |

HEAD matched HTML export hash-record `ce1c095a`. No STOP.

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| HTML Export primary | `25cf8d4229c1e31bf1159ed2976bb320340bb336` — `feat(iseo-report-hub): add html report export workflow` |
| HTML Export hash-record | `ce1c095a7d67192e59b764d7b9ea64229e1c48ae` |
| DB-08 primary / hash-record / clarify | `7b059bb2…` / `e0a13795…` / `3b35673f…` |
| Snapshot primary / hash-record | `7d199791…` / `040586fe…` |
| DB (read-only this wave) | `iseo_report_hub_dev` @ `127.0.0.1` |
| Counts | schema_migrations **7**; tables **15**; report_snapshots **1**; report_exports **1** |
| Export id 1 | key `snapshot-1-html-v1`; format `html`; status `ready`; file checksum `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4`; size **5360**; path `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` |
| HTML artifact FS | **exists** outside public; PDF under exports **none**; PDF DB rows **0** |
| Current limitation | **No** PDF engine selected; **no** PDF route/artifact/dependency policy executed |

This charter wave did not mutate DB or filesystem artifacts.

---

## 3. Charter Output

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md`
- `reports/REPORT-iseo-report-hub-report-export-pdf-engine-charter-01.md` (this file)
- `OPERATIONAL-INDEX.md` — PDF Engine Charter status; baseline on HTML Artifact Implementation; next = PDF Engine Probe 01; note no code/runtime/DB/PDF in charter

---

## 4. Engine Comparison Summary

| Candidate | Summary |
|-----------|---------|
| Manual browser print | Lowest risk; not true server PDF; temporary fallback |
| Headless Chromium / local browser | Best HTML/CSS fidelity; preferred **if** already available and controllable |
| wkhtmltopdf | Simpler CLI; weaker modern CSS; needs binary if missing |
| Dompdf | PHP/Composer; CSS limits; Cyrillic fonts tricky; deferred |
| mPDF | PHP/Composer; often better multilingual text than Dompdf; deferred |
| Recommendation | Probe-first; prefer local browser without install; else STOP for operator approval |

---

## 5. Decision

- **No** direct PDF implementation in this wave.
- Next: **Report Export PDF Engine Probe 01** (read-only).
- Preferred source = existing ready **HTML artifact**.
- Preferred candidate = **headless/local browser** if available without install.
- Any Composer/binary install requires **explicit operator approval**.

---

## 6. Storage / Metadata Plan

| Item | Plan |
|------|------|
| Future PDF path | `…/storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.pdf` |
| DB | `report_exports` row `snapshot-1-pdf-v1`, `format=pdf`, relative `storage_path`, MIME `application/pdf`, checksums |
| Public / Git / Desktop | **forbidden** |

---

## 7. Validation Plan

- Probe: no install; no PDF (default); no DB mutation; inventory documented; engine or STOP.
- Future PDF: HTML checksum gate; `%PDF` magic; size > 0; DB checksum match; auth download; idempotent POST; no-public; no unapproved deps; HTML/snapshot regression intact.

---

## 8. Restrictions Confirmed

- no app-source edits;
- no runtime edits;
- no DB mutation;
- no SQL/migration creation/edit;
- no report_exports / report_snapshots / report_blocks / monthly_report_contents / weekly_checkpoint / reporting_period row changes;
- no admin/password/hash changes;
- no env changes;
- no source sync;
- no service restart;
- no file/PDF generation;
- no package install/download;
- no push/fetch/pull/reset/clean/stash.

---

## 9. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only (worktree) |
| Commit message | `docs(iseo-report-hub): add report export pdf engine charter` |
| Primary commit hash | `e16fc4149712e1770c7b6dd8c53109469347c018` |
| Hash-record message | `docs(iseo-report-hub): record report export pdf engine charter commit hash` |
| Hash-record commit hash | `22f2f80eaa6fea18bc4a1b3f50a92f45ad74c5ed` |
| Push | **no** |

---

## 10. SAFE UNKNOWN

- Whether Edge/Chrome/wkhtmltopdf/Composer are present on this machine in a form suitable for controlled PDF generation — **not inventoried in this docs wave**; deferred to Probe 01.
- Exact headless print-to-PDF CLI flags / reliability on Laragon Windows — **SAFE UNKNOWN** until probe/implementation smoke.
- Whether operator will approve any install if no local browser path is found — **SAFE UNKNOWN**.

---

## 11. Recommended Next Action

I-SEO Report Hub — Report Export PDF Engine Probe 01

---

## 12. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-COMPARISON-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-ENGINE-DECISION-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.2.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.2.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-export-pdf-engine-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 13. Git Actions

| Action | Done? |
|--------|-------|
| Exact-path git add | **yes** (allowlisted docs only in clean worktree) |
| Commit | **yes** (primary + hash-record) |
| Push | **no** |
| Fetch | **no** |
| Pull | **no** |
| Checkout / update-ref | worktree detached at HEAD; after commits: `git update-ref refs/heads/mars/canonical-post-recovery <new-tip>` if safe |
| Reset | **no** |
| Restore | scoped restore on main for changed i-SEO files only if needed to align working tree to HEAD |
| Clean | **no** |
| Stash | **no** |
| Broad git add | **no** |
| Clean temporary worktree | `X:\AI MARS STORAGE\git-sync-iseo-pdf-engine-charter-01\repo` used for commit |
