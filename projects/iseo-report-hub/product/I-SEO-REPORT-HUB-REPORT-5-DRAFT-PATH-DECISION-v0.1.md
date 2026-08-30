# i-SEO Report Hub — Report 5 Draft Path Product Decision v0.1

**Wave:** Report 5 Draft Path Cleanup Charter 01  
**Date:** 2026-08-21  
**Depends on:** [I-SEO-REPORT-HUB-REPORT-5-CURRENT-STATE-AUDIT-v0.1.md](I-SEO-REPORT-HUB-REPORT-5-CURRENT-STATE-AUDIT-v0.1.md)

---

## Decision question

What should report id **5** be in the local demo product story — without mutating DB in the next UX implementation wave?

---

## Options

### Option A — Keep report 5 as clean empty draft

**Pros**
- Tests empty-state UX honestly  
- No DB mutation  
- Safe for P0/P1 immutability  

**Cons**
- Less useful as a second “full” demo report  

### Option B — Hide / demote report 5 from main reporting periods surfaces

**Pros**
- Cleaner primary demo path (report 1 / period 2026-07)  

**Cons**
- May hide a useful empty-draft rehearsal path if fully hidden  

### Option C — Seed report 5 with demo blocks / work entries

**Pros**
- Stronger second demo  

**Cons**
- Requires DB mutation, backup, and a **separate data wave** — out of scope for next UX implementation  

### Option D — Delete report 5

**Rejected**

**Reason:** unnecessary mutation; risk of dangling references; not required for demo clarity.

---

## Recommendation (accepted for next implementation)

**Option A + light demotion (B-lite)**

| Rule | Choice |
|------|--------|
| Keep report 5 row | **Yes** — valid draft object |
| Auto-create blocks/entries | **No** |
| DB seed / SQL cleanup / delete | **No** in next UX wave |
| Empty-state UX on detail + preview | **Yes** — make emptiness intentional and calm |
| Period / list demotion label | **Yes** — mark as `Пустой черновик` / `Черновик без работ` |
| Primary demo path | Remains **report 1** (`2026-07` finalized) |
| PDF / export / share | Frozen; unchanged |

---

## Product roles

| Object | Role |
|--------|------|
| Report **1** | Primary manager + client demo (filled, finalized) |
| Report **5** | Secondary **empty draft** rehearsal object (0 blocks / 0 entries) |
| Period `2026-08` (archived) | Smoke/archive period hosting the empty draft — not primary demo |

---

## Deferred (explicit)

- Separate local-only **data** wave if operator later wants Option C seed  
- Deeper content pack for empty → filled demo transition  
- Any deletion or SQL hide  

---

## Decision statement

Next wave **`I-SEO Report Hub — Report 5 Draft Path Cleanup Implementation 01`** implements **render/UX-only** cleanup so report 5 reads as a **clean empty draft**, lightly demoted in period UI, without competing with report 1 and without any DB or delivery-artifact mutation.
