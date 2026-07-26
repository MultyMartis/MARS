# REPORT — I-SEO REPORT HUB REPORT EXPORT / PDF CHARTER 01

**Status:** COMPLETE (docs/policy only)  
**project_id:** `iseo-report-hub`  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Export / PDF Charter 01  
**Primary commit:** `5cf2239128a7440afa98cab11de9c415230f5fd0`  
**Hash-record commit:** `PENDING_HASH_RECORD`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `7c3dbf1cabb119f645bfa94553087bfe40d412ea` |
| Staged/index before (main) | **non-empty foreign** (`projects/client-ops-reporting-bridge/**` staged deletes/changes) — **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-export-pdf-charter-01\repo` (detached at `7c3dbf1c`) |
| i-SEO WIP before | **clean** (`projects/iseo-report-hub/` no modified/untracked on main) |
| Foreign WIP | **preserved** (main index untouched; no unstage/restore of foreign paths) |
| Write scope | Active Brain docs only under allowlisted `product/` + `reports/` + `OPERATIONAL-INDEX.md` in clean worktree |

HEAD matched Snapshot closeout-hashes `7c3dbf1c`. No STOP.

---

## 2. Baseline Reviewed

| Item | Value |
|------|-------|
| Snapshot primary | `7d19979183947a25510915a7d36da9655c370673` — `feat(iseo-report-hub): add report snapshot workflow` |
| Snapshot hash-record | `040586fe96db91868704ed448402f640f438cb02` |
| Snapshot clarify | `c6b5d84161a751c594444a93510b159eb4c73a17` |
| Snapshot closeout-hashes | `7c3dbf1cabb119f645bfa94553087bfe40d412ea` |
| Smoke (snapshot) | **64/64 PASS** |
| Push (snapshot) | **no** |
| DB-07 primary | `eb1d0ce544f42876a99ea4393a98ffa780bb6f1f` |
| DB-07 hash-record / clarify | `e290a29c…` / `a9b3c8e8…` |
| DB (read-only this wave) | `iseo_report_hub_dev` @ `127.0.0.1` |
| Counts | schema_migrations **6**; tables **14**; users **1**; roles **6**; clients/projects/sites **1/1/1**; reporting_periods **2**; weekly_checkpoints **4**; monthly_report_contents **1**; report_blocks **6** (all `reviewed`); report_snapshots **1** |
| Snapshot id 1 | key `monthly-1-v1`; version **1**; status `active`; render_mode `blocks_primary`; checksum `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38`; rendered_text present; rendered_html null |
| Monthly id 1 | status `finalized`; `finalized_at` non-null |
| Current limitation | **No** export model; **no** PDF; **no** export storage; **no** `report_exports`; **no** export routes; **no** public/share/client portal |

This charter wave did not mutate DB.

---

## 3. Charter Output

Created/updated:

- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md`
- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-report-export-pdf-charter-01.md` (this file)
- `OPERATIONAL-INDEX.md` — Report Export / PDF Charter status; baseline on Snapshot Implementation; recommended DB-08 `report_exports`; next = DB-08 Migration Apply 01; no code/runtime/DB in charter

---

## 4. Export Design Summary

| Area | Design |
|------|--------|
| Source of truth | `report_snapshots` only (not live monthly/blocks) |
| MVP format | **HTML** artifact first |
| PDF | **Deferred** (engine charter later) |
| Storage root | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\` |
| Layout | `monthly-{id}/snapshot-{id}/{snapshot_key}.html` |
| Filename | e.g. `monthly-1-v1.html` |
| Export key | e.g. `snapshot-1-html-v1` |
| Metadata table | Recommended `report_exports` (DB-08) |
| Routes (future) | GET exports list; POST html; GET detail; GET download |
| Access | generate: admin_owner + seo_lead_reviewer; view/download: internal roles; client_viewer none |
| Audit | `report_export.created` / `idempotent_hit` / optional `downloaded` / `creation_failed` |
| No-public / no-PDF | No public/token routes; no PDF in first HTML wave |

---

## 5. Storage Plan

| Item | Policy |
|------|--------|
| Root | Localhost runtime `storage/exports/reports/` |
| Layout | `monthly-{monthly_id}/snapshot-{snapshot_id}/` |
| No Git | Artifacts never committed |
| No public webroot | No `public/exports`; auth stream only |
| Checksums | Snapshot checksum copied; separate file SHA-256 |
| Cleanup | Soft archive later; no auto-delete; physical delete only via destructive charter |

---

## 6. Validation Plan

Covers: DB-08 schema; storage path; HTML generate; idempotency; file checksum; authenticated download; no public access; snapshot unchanged; regression; no-PDF for HTML wave; data policy; STOP conditions.

---

## 7. Restrictions Confirmed

- no app-source edits;
- no runtime edits;
- no DB mutation;
- no SQL/migration creation/edit;
- no report_snapshots / report_blocks / monthly_report_contents / weekly_checkpoint / reporting_period row changes;
- no admin/password/hash changes;
- no env changes;
- no source sync;
- no service restart;
- no file/PDF generation;
- no push/fetch/pull/reset/clean/stash;
- no broad git add;
- foreign WIP preserved on main.

---

## 8. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted docs only (in clean worktree) |
| Commit message | `docs(iseo-report-hub): add report export pdf charter` |
| Primary commit hash | `5cf2239128a7440afa98cab11de9c415230f5fd0` |
| Hash-record message | `docs(iseo-report-hub): record report export pdf charter commit hash` |
| Hash-record hash | `PENDING_HASH_RECORD` |
| Push | **no** |

---

## 9. SAFE UNKNOWN

- Exact future migration filename for DB-08 (suggested `2026_07_27_000007_create_report_exports_table.sql`) — finalize in DB-08 apply wave.
- Whether operator will override to HTML-without-table (not recommended) — unknown until explicit decision.
- PDF engine choice — deferred; unknown until PDF Engine Charter.
- Whether download audit will be enabled by default (noise) — decide in HTML implementation.

---

## 10. Recommended Next Action

**I-SEO Report Hub — Report Export DB-08 Migration Apply 01**

---

## 11. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-CHARTER-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-DESIGN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-STORAGE-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-IMPLEMENTATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-PDF-VALIDATION-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-export-pdf-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 12. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | **yes** (allowlisted docs in worktree) |
| commit (primary + hash-record) | **yes** (see §8) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout/update-ref | **yes** — worktree detached at `7c3dbf1c`; after commits, `git update-ref refs/heads/mars/canonical-post-recovery` from worktree HEAD if safe; scoped restore on main for i-SEO docs if needed |
| reset | **no** |
| restore (destructive broad) | **no** — scoped i-SEO restore on main only if needed for alignment |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-export-pdf-charter-01\repo` used for commits |
