# REPORT — I-SEO REPORT HUB CLIENT REPORT EXPORT HTML ALIGNMENT CHARTER 01

**Date:** 2026-08-20  
**project_id:** `iseo-report-hub`  
**Wave:** Client Report Export HTML Alignment Charter 01  
**Verdict:** `CLIENT REPORT EXPORT HTML CHARTER COMPLETE`

Documentation / architecture / safety charter only. No app-source, runtime, DB, export, share, or PDF mutation. No push.

Primary: `6dbcdce069f4819b1d771695f194a025a052946a`. Hash-record / tip: `a113ab36d7691743cc7e6a27c12a63d893777db4`.

---

## 1. Verdict

`CLIENT REPORT EXPORT HTML CHARTER COMPLETE`

---

## 2. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` / `AI WS` |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `444d8a458b44fca994261c8eee52083308e6628f` (later than visual Impl tip `b7b1144e…`; ancestor OK) |
| Clean worktree used | **Yes** — detached then `feat/iseo-report-hub-client-report-export-html-alignment-charter-01` at `X:\AI MARS STORAGE\git-sync-iseo-report-hub-client-report-export-html-alignment-charter-01\repo` |
| Foreign WIP preserved | **Yes** |
| i-SEO WIP before start | **None** |
| Staged i-SEO | **None** |
| App-source / runtime / DB | **Unchanged** |
| Optional HTTP `/health` | Connection failed (runtime not answering) — SAFE UNKNOWN for live smoke; charter did not require runtime |

---

## 3. Export Pipeline Audit

| Area | Finding |
|------|---------|
| HTML export | `ReportExportService` → `ReportTemplateRenderer` string HTML from **snapshot payload**; embedded CSS; disk under `storage/exports/reports/…` |
| PDF | Edge/Chrome headless `--print-to-pdf` from **HTML artifact file**; no separate PDF template; no `ReportPdfService` class |
| Storage / DB | Immutable ready files + `report_exports` checksum metadata; versioned paths `monthly-{id}-v{N}` |
| `/report-exports/{id}` | Internal metadata/handoff UI; download streams file |
| Public share | Static PDF attachment stream; not dynamic HTML |

Detail: [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md)

---

## 4. Alignment Options

| Option | Summary |
|--------|---------|
| A | Rewrite `ReportTemplateRenderer` onto client document — high blast radius |
| B | New client export HTML renderer; keep old renderer — **recommended** |
| C | Docs-only until PDF wave — too little progress |

Detail: [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md)

---

## 5. Recommended Implementation Scope

**Next:** `I-SEO Report Hub — Client Report Export HTML Alignment Implementation 01`

- Snapshot→`ClientReportDocument` adapter + export-safe HTML with **embedded** CSS  
- Non-mutating dry-render / optional tool  
- Evidence only under Storage incoming  
- No export rows, no PDF, no share mutation  

Detail: [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md)

---

## 6. Data / CSS / PDF Safety

- Reuse client DTO; export-safe mode turns **off** local demo banner  
- Embed CSS for future PDF; do not claim PDF readiness in Impl 01  
- Strip fixture markers; no technical ids; honest empties; no fake KPI  
- `/preview/print` is visual reference only — exports stay snapshot-based  

Detail: [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md)

---

## 7. Artifact Immutability

Export **4** frozen; future visual = new id; shares stay on old PDF until handoff charter; Storage evidence ≠ product export.

Detail: [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md)

---

## 8. Acceptance Criteria

See [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md)

---

## 9. Sequence

1. Export HTML Alignment Implementation 01 (non-mutating)  
2. PDF Regeneration Proof 01 (new export id)  
3. Share Handoff Update 01 (operator-approved)  
4. Metrics model  
5. Screenshot QA all pages  

Detail: [I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md](../product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md)

---

## 10. Docs Created

- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-PIPELINE-AUDIT-v0.1.md`
- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-ALIGNMENT-OPTIONS-v0.1.md`
- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-IMPLEMENTATION-SCOPE-v0.1.md`
- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-DATA-CSS-PDF-SAFETY-v0.1.md`
- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-IMMUTABILITY-POLICY-v0.1.md`
- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-HTML-ACCEPTANCE-v0.1.md`
- `product/I-SEO-REPORT-HUB-CLIENT-REPORT-EXPORT-SEQUENCE-v0.1.md`
- `reports/REPORT-iseo-report-hub-client-report-export-html-alignment-charter-01.md`
- `OPERATIONAL-INDEX.md` (updated)

---

## 11. Restrictions Confirmed

No code edits; no runtime edits; no DB mutation; no share/export/PDF mutation; no production; no push; no secrets/token printing.

---

## 12. Commit

- Primary: `6dbcdce069f4819b1d771695f194a025a052946a`
- Hash-record: `a113ab36d7691743cc7e6a27c12a63d893777db4`
- Tip HEAD: `a113ab36d7691743cc7e6a27c12a63d893777db4`
- Push: **no**

---

## 13. SAFE UNKNOWN

- Live local HTTP smoke for preview/export pages in this charter wave (runtime `/health` unreachable during optional check).
- Whether operator prefers CLI tool vs service-only dry-render in Impl 01 (both allowed; service method required).
- Exact active share id/token values not re-probed here (prior checkpoint: id **7** / `test-first-link` context; token not printed).

---

## 14. Files Changed

Exact allowlisted docs under `projects/iseo-report-hub/` listed in §10.

---

## 15. Git Actions

Clean worktree branch commit(s); scoped restore into main canonical branch; foreign WIP preserved; **no push**.
