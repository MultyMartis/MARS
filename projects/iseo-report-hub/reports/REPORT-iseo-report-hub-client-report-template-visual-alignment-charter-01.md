# REPORT — I-SEO REPORT HUB CLIENT REPORT TEMPLATE VISUAL ALIGNMENT CHARTER 01

**Date:** 2026-08-17  
**project_id:** `iseo-report-hub`  
**Wave:** Client Report Template Visual Alignment Charter 01  
**Verdict:** `CLIENT REPORT VISUAL CHARTER COMPLETE`

Docs / architecture / UX / safety only. No app-source, runtime, DB, share, export, or PDF mutation. No push.

Primary: `d92215458f38db264191474421d9d540218321d9`. Hash-record / tip: this docs commit.

---

## 1. Verdict

`CLIENT REPORT VISUAL CHARTER COMPLETE`

Option B: dedicated client report document template. Implementation 01 restyles live internal preview only. Issued PDF 4 and the active share stay frozen.

---

## 2. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` / `AI WS` |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `62ca9acbc1efe14da10a1b6a86e452c0b8d61c6b` |
| Clean worktree used | **Yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-hub-client-report-template-visual-alignment-charter-01\repo` on `feat/iseo-report-hub-client-report-template-visual-alignment-charter-01` |
| Foreign WIP preserved | **Yes** (main staged foreign index untouched during edits) |
| app-source / runtime / DB writes | **No** |
| HTTP (unauth) | `/health` **200**; `/monthly-reports/1/preview` **302**; `/report-exports/4` **302**; share URL not fetched |

---

## 3. Current Surface Audit

| Surface | Class |
|---------|-------|
| `/monthly-reports/{id}/preview` | Internal admin preview today; **first client-document canvas** |
| `/report-exports/{id}` | Internal delivery ops — not client-safe |
| `/share/report/{token}` | PDF **attachment stream**; no HTML view |
| HTML v2 / PDF v2 | `ReportTemplateRenderer`; still “internal export”; **frozen** |

Canonical client document = new Option B template. Current client-delivered file = PDF export **4**.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-SURFACE-AUDIT-v0.1.md`

---

## 4. Target Client Report IA

Order: cover → `executive_summary` → `results_summary` → `work_completed` → `key_findings` → `risks_and_blockers` → `next_month_plan` → footer.

Empty: calm notes on preview; no fake KPI. Hide ids, keys, checksums, weekly dumps, `LOCAL_FIXTURE_ONLY`.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-TARGET-IA-v0.1.md`

---

## 5. Visual Direction

Light paper on `#f5f6f8`; ink `#18181B`; accent `#facc15`; no dark sidebar; Manrope/system sans; A4 print; red not default.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-DIRECTION-v0.1.md`

---

## 6. Template Architecture

A in-place restyle — rejected as primary.  
B dedicated reusable document — **recommended**.  
C split web/PDF templates — defer.

Target: `layout-client-report.php` + `partials/client-report/document.php` + client CSS + optional view mapper. Routes unchanged. Renderer/PDF files untouched in Impl 01.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-ARCHITECTURE-v0.1.md`

---

## 7. PDF / Export / Share Safety

Export 4 checksum unchanged. No regen, no new export row, no share create/revoke, no token print. Public share is static PDF. Future regen = new export id + `Client Report PDF Regeneration Proof 01`.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-PDF-EXPORT-SHARE-SAFETY-v0.1.md`

---

## 8. Implementation Sequence

**Next:** `I-SEO Report Hub — Client Report Template Visual Alignment Implementation 01` (preview document only).

Later: export HTML alignment → PDF regeneration proof. Public HTML share alignment **skipped** unless delivery model changes. Screenshot QA of all pages remains deferred.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-IMPLEMENTATION-SEQUENCE-v0.1.md`

---

## 9. Acceptance Criteria

Preview 200; no sidebar; no edit/apply/ids; six RU sections in IA order; calm empties; DB/export/share/PDF unchanged.

Doc: `product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-ACCEPTANCE-v0.1.md`

---

## 10. Docs Created

See §14.

---

## 11. Restrictions Confirmed

No app-source/runtime/DB/share/export/PDF mutation. No production. No push. No secrets/tokens printed.

---

## 12. Commit

| Field | Value |
|-------|--------|
| Primary | `d92215458f38db264191474421d9d540218321d9` |
| Hash-record | this docs commit |
| Tip HEAD | this docs commit |
| Push | **no** |

---

## 13. SAFE UNKNOWN

- Active share id/label not re-queried (context: id **7** / `test-first-link`).
- Whether a later wave will bump `iseo_default_v1` version when first regenerating PDF.
- Origin of monthly id **5** (untouched).

---

## 14. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-SURFACE-AUDIT-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-TARGET-IA-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-DIRECTION-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-TEMPLATE-ARCHITECTURE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-PDF-EXPORT-SHARE-SAFETY-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-IMPLEMENTATION-SEQUENCE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-CLIENT-REPORT-VISUAL-ACCEPTANCE-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-client-report-template-visual-alignment-charter-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

---

## 15. Git Actions

Clean worktree exact-path commits; `update-ref` canonical; scoped restore of i-SEO docs paths on main; foreign WIP preserved; **no push**.
