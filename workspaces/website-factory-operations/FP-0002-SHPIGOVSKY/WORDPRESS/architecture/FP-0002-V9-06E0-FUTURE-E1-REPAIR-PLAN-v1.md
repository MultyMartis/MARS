# FP-0002 V9-06E0 — Future E1 Repair Plan v1

**Phase:** V9-06E0 (plan only — **no repair in E0**)  
**Date:** 2026-07-06  
**Evidence:** `validation/v9-06e0-legal-native-content-review/future-e1-repair-plan.json`

---

## Recommended wave sequence

### 1. OPERATOR_DECISION_REQUIRED (gate)

Operator must:

- Provide approved Shpigovsky legal texts **or** authorize reference-template generation with entity data fill-in.
- Decide fate of legacy pages **#21** and **#25**.
- Approve interim empty/placeholder legal state vs block publish until full copy ready.

### 2. CREATE_V9_06E1_LEGAL_ROUTE_AND_PRIVACY_SETTING_REPAIR_TASK

**Pages:** 3, 21, 25  
**Writes:** `wp_page_for_privacy_policy`, legal menu items, optional menu order  
**Safety:** DB checkpoint mandatory; no page deletion

### 3. CREATE_V9_06E1_LEGAL_PAGE_CLEAR_AND_PLACEHOLDER_TASK

**Pages:** 3 (garbled clear); optional 6–10, 17, 19, 21, 25 (native clear)  
**Writes:** `post_content` only on allowlisted IDs  
**Safety:** Preserve page objects; no ACF/home/services/reviews mutation

### 4. CREATE_V9_06E1_AUTHORITATIVE_LEGAL_COPY_SEED_TASK

**Pages:** 3, 22, 23, 24  
**Writes:** `post_content`, legal ACF fields, `post_status` for #3 when approved  
**Requires:** Operator copy package  
**Validation:** Frontend route audit; no garbled markers; privacy setting = 3

---

## Do not touch in E1 (unless explicitly chartered)

- Template-managed clean pages: 4, 5, 11–16, 18, 20
- Service CPT objects and Reviews OPTIONS
- Theme source, ACF JSON, plugins

---

## Validation plan (E1 closeout)

1. Re-run E0 inventory probes  
2. Confirm privacy setting alignment  
3. Screenshot four footer legal routes + admin privacy screen (authenticated if possible)  
4. No-scope-drift gate  

---

## Verdict

**PLANNED** — bounded E1 waves defined; execution blocked on operator decision.
