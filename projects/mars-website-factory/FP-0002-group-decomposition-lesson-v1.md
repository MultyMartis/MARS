# FP-0002 — Group Decomposition Lesson v1

**ID:** `FP-0002-GROUP-DECOMPOSITION-LESSON`  
**Status:** **documented** — Factory lesson from FP-0002 Shpigovsky.ru JPG analysis test.  
**Not:** retroactive fix of FP-0002 header code; **not** modification of FP-0002 workspace artefacts.

**Date:** 2026-06-15  
**Authority:** [group-decomposition-law-v1.md](group-decomposition-law-v1.md) — canonical law promoted from this incident.

**Read-only FP-0002 references:** [FP-0002-FULL-jpg-ANALYSIS-TEST-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-FULL-jpg-ANALYSIS-TEST-v1.md) · [FP-0002-HEADER-LAYOUT-SPEC-v2.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HEADER-LAYOUT-SPEC-v2.md) (correct downstream decomposition — **not** produced in JPG test path).

---

## 1. What happened

During FP-0002 **FULL PAGE JPG ANALYSIS TEST** (2026-06-15), the agent analyzed header structure from `HOME-PAGE-FULL-MOCKUP.jpg` **without** Layout Spec, Design Audit, or intermediate composition artefacts.

The agent **correctly** identified **two horizontal rows** in the header.

The agent **incorrectly** grouped elements **inside ROW 1** into abstract aggregates.

---

## 2. Evidence — row correct, groups wrong

### 2.1 What the JPG test produced

From [FP-0002-FULL-jpg-ANALYSIS-TEST-v1.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-FULL-jpg-ANALYSIS-TEST-v1.md) §2–§3:

| Dimension | Agent output |
|-----------|--------------|
| **Row count** | **2 rows** — correct band split |
| **ROW 1 summary** | `logo \| contact \| CTA` |
| **ROW 1 center** | **«Контактный блок»** — address + phone merged |
| **ROW 2** | Menu (6 links) + search icon |
| **Missing decomposition** | Schedule, separate phone cluster, messengers not named as discrete groups |

### 2.2 What faithful decomposition requires

For the same visual band, Group Decomposition must register **discrete groups**, not one contact blob:

**ROW-01**

| GROUP-ID | Group |
|----------|-------|
| GROUP-01 | Logo |
| GROUP-02 | Address |
| GROUP-03 | Schedule |
| GROUP-04 | Phones |
| GROUP-05 | Messengers |
| GROUP-06 | CTA |

**ROW-02**

| GROUP-ID | Group |
|----------|-------|
| GROUP-07 | Menu |
| GROUP-08 | Search |

### 2.3 Failure shape

```text
Actual layout (many groups)  →  Agent summary (few abstractions)

LOGO · ADDRESS · SCHEDULE · PHONES · MESSENGERS · CTA
                          ↓
                    LOGO · CONTACT BLOCK · CTA
```

**Result:** Even at **analysis-only** stage, future Layout Spec and HTML inherit **wrong grouping** — flex bands, markup wrappers, and visual hierarchy compress before code starts.

---

## 3. Root cause (systemic)

| Factor | Detail |
|--------|--------|
| **Missing artifact** | No **Group Decomposition** register between Visual SSOT and Layout Spec |
| **Partial success trap** | Correct **row count** masked wrong **group count** |
| **Not the cause** | JPG quality, PDF absence, Layout Spec absence alone, Visual Scale |
| **Aggregation habit** | Agent defaulted to **CONTACT BLOCK**-class labels familiar from generic headers |

---

## 4. Why prior gates did not catch it

| Gate / artefact | Why grouping error survived |
|-----------------|----------------------------|
| **Layout Spec Law** | Assumes Layout Spec exists; JPG test **skipped** Layout Spec entirely |
| **Layout Spec content** | Can **inherit** upstream aggregates if Group Decomposition skipped |
| **Design Audit** | Page/block inventory — not per-group register |
| **Row-level verbal summary** | «Two rows» treated as sufficient understanding |
| **Operator visual review** | Post-implementation — JPG test caught error in **analysis REPORT**, not build |

**Discovery mechanism:** Operator review of JPG analysis REPORT — grouping visible before HTML in this test; in production path, same error would surface at Layout Spec or first markup.

---

## 5. Correct capture point

**Group Decomposition Gate** — immediately **after** Visual SSOT approval, **before** Layout Spec.

```text
Visual SSOT (JPG / PDF / Figma — format irrelevant)
    ↓
Group Decomposition — ROW register + GROUP-ID register + relationships
    ↓
Operator APPROVED
    ↓
Layout Spec (inherits GROUP-IDs — no re-aggregation)
    ↓
Assembly Spec → Visual Scale Spec → HTML
```

---

## 6. Lesson (normative for Factory)

1. **Row count ≠ group decomposition.** Two rows correct with six groups merged into one **CONTACT BLOCK** is still a **composition failure**.
2. **Abstract labels are stop signals.** CONTACT BLOCK · INFO AREA · UTILITY GROUP without GROUP-IDs = **GROUP AGGREGATION BEFORE DECOMPOSITION**.
3. **JPG is sufficient SSOT for decomposition duty.** Format did not cause the failure; **skipping Group Decomposition** did.
4. **Layout Spec cannot fix upstream aggregation** unless operator forces REVISE back to Group Decomposition.

---

## 7. v1 Factory response

| Action | Document |
|--------|----------|
| Canonical law | [group-decomposition-law-v1.md](group-decomposition-law-v1.md) |
| Roadmap integration | [website-factory-production-roadmap-v2-draft.md](website-factory-production-roadmap-v2-draft.md) — pointer |
| Layout Spec integration | [layout-spec-law-v1.md](layout-spec-law-v1.md) — authority chain pointer |
| Failure attribution | [frontend-failure-attribution-model-v1.md](frontend-failure-attribution-model-v1.md) — **GROUP AGGREGATION BEFORE DECOMPOSITION** |

---

## 8. Changelog

| Date | Change |
|------|--------|
| 2026-06-15 | v1 — lesson filed from FP-0002 JPG test; promotes Group Decomposition Law. |
