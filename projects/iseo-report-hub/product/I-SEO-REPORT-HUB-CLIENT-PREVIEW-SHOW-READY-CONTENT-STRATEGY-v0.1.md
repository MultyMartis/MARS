# I-SEO Report Hub — Client Preview Show-ready Content Strategy v0.1

**Status:** strategy decision (docs only)  
**Date:** 2026-08-21  
**Next wave name:** `I-SEO Report Hub — Client Preview Show-ready Content Implementation 01`

---

## 1. Goal definition — what “show-ready client preview” means (MVP)

For local MVP demo, **show-ready** means:

1. `/monthly-reports/1/preview` and `/monthly-reports/1/preview/print` read as a **credible finished SEO monthly report** for a client.
2. All **six** client sections show useful, client-safe Russian copy (not “will be filled later” placeholders).
3. Copy is **modest and honest**: work done, conclusions, blockers, next plan — **no fake traffic / positions / leads**.
4. Layout/chrome remain as accepted; polish is content-first.
5. Report **5** empty draft stays calm empty (no demo fill).
6. Frozen export/share/PDF surfaces stay untouched.

Show-ready is **demo credibility**, not production content-editor completeness and not PDF parity.

---

## 2. Options evaluated

### Option A — Render-layer show-ready local demo fallback

**Recommended for Implementation 01.**

Mechanism (implementation later):

- When assembling the client document for preview/print, if a section body is empty/junk after sanitizer **and** environment is local/demo (`app.env === local` and/or existing `local_demo` flag), inject polished demo text for report 1 (or equivalent gated demo finalized report).
- Prefer live work-entry-derived text for auto sections when available without DB write; use static demo fallback for manual empties.
- No `report_blocks` / `monthly_report_contents` UPDATE.
- Export/PDF/share pipelines remain on current DB/snapshot path — unchanged.

| Pros | Cons |
|------|------|
| No DB mutation | Preview text may differ from DB block bodies |
| No immutable export/share impact | Must gate carefully (local/demo only) |
| Fast and reversible | Not a long-term CMS content solution |
| Keeps export 4 frozen | Operators must understand “demo overlay” |
| Aligns with current `ClientReportDocument` preview-only role | Future editor wave still needed for real persistence |

### Option B — Local-only DB update of report 1 blocks

**Deferred** — separate future charter if operator requests true persistence.

| Pros | Cons |
|------|------|
| Preview equals DB | Report 1 is finalized/issued |
| Closer to real workflow | Requires backup + reopen or guarded direct update |
| | Export 4 mismatch remains until PDF regen (deferred) |
| | Higher safety / confusion risk |

If pursued later: **local-only DB content wave** with backup, explicit reopen/finalize policy, and still **no** export 4 mutation until PDF wave is approved.

### Option C — Separate show-ready demo report

**Deferred.**

| Pros | Cons |
|------|------|
| Clean demo object | DB seed/mutation |
| Does not touch report 1 | Larger scope; distracts from current MVP demo object |
| | Still needs preview/export policy clarity |

---

## 3. Decision

| Item | Decision |
|------|----------|
| **Implementation 01** | **Option A** |
| Option B | Deferred — needs separate local DB content charter + backup |
| Option C | Deferred — needs separate demo-report seed charter |
| PDF/export/share | Remain frozen / deferred |
| Metrics / KPI fill | Not in scope — honest “metrics not automated” copy only |

---

## 4. Content source policy (for Option A)

Priority when rendering report 1 client preview in local/demo:

1. **Real sanitized block body/summary** if non-empty and not junk.
2. Else for auto-capable sections: **assembly-from-work-entries text** (read-only, in-memory) if entries exist.
3. Else: **static show-ready demo copy** from the Report 1 Demo Copy pack.
4. Report 5 / true empty drafts: keep **calm empty** messages — **do not** apply show-ready demo pack.

Labeling:

- Existing “Локальная демо-среда” cover/footer note is sufficient for MVP.
- Optional small section-level “демо-текст” label is **not required** if the whole page is already local-demo marked; avoid clutter.

---

## 5. What remains deferred

- Persistent block editor UX polish for client narrative.
- True DB content fill for report 1 (Option B).
- New demo report seed (Option C).
- Metrics model / automated results numbers.
- PDF regeneration and export HTML alignment (export 4 frozen).
- Share mutation / public share demo content refresh.
- Production content.

---

## 6. Why Option A is the safe show path now

- Report 1 finalized + apply blocked → DB fill is the high-risk path.
- Export 4 already issued → any DB content change without PDF regen increases drift.
- Operator already deferred PDF until UI/content polish completes.
- Render-layer overlay finishes the **demo story** without breaking freezes.
