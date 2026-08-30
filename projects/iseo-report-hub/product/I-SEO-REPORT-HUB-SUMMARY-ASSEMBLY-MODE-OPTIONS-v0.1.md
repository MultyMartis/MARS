# I-SEO Report Hub — Summary Assembly Mode Options v0.1

**Status:** CHARTER / OPTIONS — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Charter 01

---

## 1. Option A — Preview-only assembler (recommended now)

**Idea:** Generate client-section drafts from work entries and show them on a dedicated internal page. **Zero writes** to `report_blocks`, flat monthly columns, snapshots, exports, or shares.

| Dimension | Assessment |
|-----------|------------|
| DB mutation | None |
| Schema / migration | None |
| Fit for finalized report id 1 | Safe — live preview of a proposal, published PDF untouched |
| Operator value | Sees mapping quality on the real 7 entries |
| Overwrite risk | None |
| Implementation size | Small: service + GET route + view |
| PDF / share | Unchanged |

**Limit:** Specialist still copies text by hand (or waits for Option B) if they want shells updated.

---

## 2. Option B — Draft apply with overwrite protection

**Idea:** Same generator as A, plus POST apply to **selected** `report_blocks` keys. Skip blocks with existing manual text unless a confirm checkbox is set. Backup DB (or at least dump `report_blocks` for that monthly id) before first apply.

| Dimension | Assessment |
|-----------|------------|
| DB mutation | UPDATE `report_blocks.body` / `summary` / optional `data_json` |
| Parent finalized | Must **reopen** first (current lock) **or** refuse apply with a clear message |
| Snapshot / PDF | Still **not** auto-regenerated |
| Overwrite risk | Medium — mitigated by selection + confirm + backup |
| Complexity | Medium — CSRF, reopen policy, provenance JSON, evidence of old text |

**Do not** ship B in the same wave as the first preview. Report 1 is finalized and has an active share; writing shells now trains the wrong expectation (“I applied → client PDF changed”).

---

## 3. Option C — Full assembly workflow

**Idea:** Versioned drafts, diffs, per-block locks, dual draft/final columns, auto-sync flags, maybe snapshot bump.

| Dimension | Assessment |
|-----------|------------|
| Schema | Likely new columns/tables |
| Complexity | High |
| MVP safety | Poor as next bite |
| Value | Right later, after A then B are proven |

---

## 4. Comparison

| Criterion | A | B | C |
|-----------|---|---|---|
| Speed to learn mapping | ★★★★ | ★★★ | ★ |
| Safety vs report 1 PDF/share | ★★★★ | ★★ | ★★ |
| Usefulness for real monthly close | ★★ | ★★★★ | ★★★★ |
| Schema change | none | none (MVP) | likely |
| Recommended sequence | **Impl 01** | Apply charter / Impl 02 | Backlog |

---

## 5. Recommendation

**Implementation 01 = Option A only.**

Reasons:

1. Report id **1** is **finalized**; block writes are locked without reopen.  
2. Export **4** + active share exist; operators must not confuse live shells with the client PDF.  
3. Source rules need a visible trial on 7 fixture entries before any overwrite policy is trusted.  
4. No migration, no POST, no backup obligation beyond count checks.

**Implementation 02 / next charter = Option B** after operator reviews the preview: explicit apply, no overwrite unless selected, backup, still **no** PDF regen until a later export wave.

Option C stays out of scope until apply is boringly safe.

---

## 6. Compatibility rules

1. Do not change `REQUIRED_BLOCK_KEYS`.  
2. Do not regenerate PDF/shares in A or first B.  
3. Do not write `monthly_report_contents` flat columns in A or first B (blocks remain client SoT).  
4. Work entry editor remains the specialist SoT.

---

## 7. SAFE UNKNOWN

- Whether apply (B) should be allowed on finalized reports without reopen (default: **no**, reuse existing lock).  
- Whether first B should write only empty bodies (safer) vs selected overwrite (more useful).
