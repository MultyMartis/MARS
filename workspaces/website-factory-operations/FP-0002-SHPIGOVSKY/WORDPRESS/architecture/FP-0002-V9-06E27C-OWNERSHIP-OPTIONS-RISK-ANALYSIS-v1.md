# FP-0002 V9-06E27C — Ownership Options Risk Analysis

**Evidence:** `validation/v9-06e27c-page-service-ownership-decision/ownership-options-risk-analysis.json`

## Option A — Service CPT owns routes (**RECOMMENDED**)

| Aspect | Assessment |
|---|---|
| Description | Confirm `#73/#77/#84`; retarget menu `#301`; trash `#6/#7/#8` |
| Benefits | Matches architecture, static V9, runtime, ACF templates, child tree |
| Risks | Menu retarget must precede page `#6` trash |
| Redirects | Not needed (URLs unchanged) |
| Rewrite flush | Not needed |
| Verdict | **RECOMMENDED** |

## Option B — Page owns routes

| Aspect | Assessment |
|---|---|
| Description | Keep pages; demote/remove service CPT at same paths |
| Benefits | Avoids menu retarget |
| Risks | Breaks `#73` child tree (`#74` alcohol leaf), contradicts architecture, high regression |
| Verdict | **NOT_RECOMMENDED** |

## Option C — Keep both temporarily

| Aspect | Assessment |
|---|---|
| Description | No resolution |
| Benefits | Defers writes |
| Risks | Admin confusion, menu ambiguity, blocks E28 QA |
| Verdict | **NOT_RECOMMENDED** (acceptable only as interim before E27D) |
