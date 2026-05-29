# Bid Management Rules v1

**Scope:** Triumph Manipulator Search PPC — manual bids in Direct Commander  
**Freeze:** PPC Exporter Production Baseline v1  
**Date:** 2026-05-29  
**Authority:** Human operator in Commander — ORCA documents reproducible rules; **not** an autobid engine

---

## DEFAULT SEARCH BID RANGE

| Parameter | Value |
|-----------|-------|
| **Default group anchor bid** | **400–600 ₽** per search click (manual CPC) |
| **Use** | Starting range for primary commercial groups after import |
| **Excluded** | **0 ₽** — never use zero bids |

Operator may adjust per group after Human QA; this range is the **documented production default**.

---

## Within-group bid variation

| Parameter | Value |
|-----------|-------|
| **Spread between phrases in same group** | **10–90 ₽** difference between highest and lowest phrase bid |
| **Purpose** | Priority routing inside group without flat bidding |

---

## Rules (mandatory)

| # | Rule |
|---|------|
| 1 | **Do not use 0** — zero bids break priority semantics and Commander hygiene |
| 2 | **Do not use identical bids for all phrases in a group** — flat bidding hides intent priority |
| 3 | **Primary query gets maximum bid in the group** — highest commercial intent phrase = top of range |
| 4 | **Secondary phrases bid lower by priority** — descending by intent tier within group |
| 5 | **Range must be reproducible automatically** — exporter/operator scripts should be able to regenerate the same spread from priority metadata (see examples) |

---

## Priority model (for automation)

Map each phrase to `priority_rank` (1 = highest):

```
phrase_bid = group_max_bid - (priority_rank - 1) * step
```

Where:

- `group_max_bid` ∈ [400, 600] ₽ (operator picks once per group)  
- `step` chosen so `(phrase_count - 1) * step` ≤ 90 ₽ and each step ≥ 10 ₽ when possible  
- `group_min_bid` = `group_max_bid - (phrase_count - 1) * step` ≥ `group_max_bid - 90`

**Constraint:** `group_max_bid - group_min_bid` ≤ **90 ₽** and ≥ **10 ₽** when group has 2+ phrases.

---

## Examples

### Example A — 3 phrases, zakaz group (illustrative)

| Phrase (priority) | priority_rank | Bid (₽) | Notes |
|-------------------|---------------|---------|-------|
| манипулятор краснодар заказать | 1 | **580** | Primary — max in group |
| заказать манипулятор краснодар | 2 | **550** | step 30 |
| манипулятор на заказ краснодар | 3 | **520** | spread 60 ₽ |

- Anchor max: 580 ∈ [400, 600]  
- Spread max−min: 60 ₽ ∈ [10, 90]  
- No zero · no flat 580 on all three

### Example B — 5 phrases, 5-tonn capability group

| priority_rank | Bid (₽) |
|---------------|---------|
| 1 | **600** |
| 2 | **580** |
| 3 | **560** |
| 4 | **540** |
| 5 | **520** |

- step = 20 ₽ · spread = 80 ₽  
- Primary at range ceiling

### Example C — 2 phrases, narrow group

| priority_rank | Bid (₽) |
|---------------|---------|
| 1 | **450** |
| 2 | **440** |

- Minimum spread 10 ₽ — valid when only two phrases

### Example D — forbidden patterns

| Pattern | Why forbidden |
|---------|---------------|
| All phrases **500 ₽** | Flat bidding — violates rule 2 |
| Any phrase **0 ₽** | Zero bid — violates rule 1 |
| Primary **400 ₽**, secondary **520 ₽** | Inverted priority — violates rule 3 |
| spread **120 ₽** on 4 phrases | Exceeds 90 ₽ cap — violates variation band |

---

## Exporter relationship

| Topic | Rule |
|-------|------|
| Exporter v1.2 | May emit bid cells from JSON if present; must not invent campaign logic |
| JSON instance | Should carry `priority_rank` or equivalent for reproducible spread |
| Commander import | Operator verifies bids post-import — [COMMANDER-CALIBRATION-FINDINGS-v1.md](COMMANDER-CALIBRATION-FINDINGS-v1.md) |
| Launch | Bid rules ≠ launch approval |

---

## SAFE UNKNOWN

- Market CPC shifts in live auction — operator may recalibrate outside this doc.  
- Whether JSON instance currently encodes all `priority_rank` fields — verify per export run.
