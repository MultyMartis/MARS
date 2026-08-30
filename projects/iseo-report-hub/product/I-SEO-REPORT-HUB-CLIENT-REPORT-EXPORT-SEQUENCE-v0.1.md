# I-SEO Report Hub — Client Report Export Sequence v0.1

**Status:** CHARTER / SEQUENCE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-20  
**Wave:** Client Report Export HTML Alignment Charter 01

Supersedes the export/PDF portion of visual sequence for forward planning. Preview visual Impl 01 remains complete.

---

## Sequence

| Order | Wave | Intent | Mutates exports/shares? |
|------:|------|--------|-------------------------|
| 1 | **Client Report Export HTML Alignment Implementation 01** | Non-mutating client-document HTML renderer + Storage evidence; keep renderer dual-path; freeze export 4 | **No** |
| 2 | **Client Report PDF Regeneration Proof 01** | Create **new** PDF (and prerequisite HTML) export ids from client HTML; evidence; never overwrite export **4** | **Yes — new rows only** |
| 3 | **Client Report Share Handoff Update 01** | Only after operator approves new export/PDF; new share or explicit cutover; keep tokens secret | **Yes — only if approved** |
| 4 | Metrics / results model | Separate; no fake KPI in template waves | Per that charter |
| 5 | Screenshot QA all pages | When operator provides shots; not a gate for step 1 | No (docs/evidence) |

Parallel tracks (unchanged): Production Environment Operator Decision 01; optional Local Share QA Cleanup.

---

## Step 1 detail (next)

See:

- Options → Option B  
- Scope → Implementation 01  
- Acceptance → HTML Acceptance v0.1  
- Immutability → Policy v0.1  

Next prompt name for operators/agents:

**`I-SEO Report Hub — Client Report Export HTML Alignment Implementation 01`**

---

## Explicit skips

- Do not merge step 1 with PDF regeneration.
- Do not attach a new PDF to the current active share inside step 1 or 2 without step 3.
- Do not restyle public share into dynamic HTML unless a separate product charter appears (today: PDF stream only).
