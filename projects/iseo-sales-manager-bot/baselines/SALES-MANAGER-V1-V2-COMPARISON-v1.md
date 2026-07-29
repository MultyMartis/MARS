# SALES MANAGER V1/V2 COMPARISON v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A.1  
**Evidence class:** Exact sanitized export diff (`Sales-Manager-v1.sanitized.json` · `Sales-Manager-v2.sanitized.json`)  
**Authority:** operator source drop 2026-07-30

---

## 1. Workflow metadata

| Field | V1 | V2 | Classification |
|-------|----|----|----------------|
| `name` | `Sales-Manager-v1` | `Sales-Manager-v2` | **NEUTRAL** |
| `active` (export) | `false` | `false` | **SAFE UNKNOWN** live parity |
| Node count | 19 | 19 | **NEUTRAL** |
| Connection edges | 18 | 18 (identical) | **NEUTRAL** |
| Settings | `executionOrder=v1`, `binaryMode=separate` | same | **NEUTRAL** |
| HTTP AI calls | 2 | 2 | **DEFECT** |

Sanitized SHA256: v1 `A1C9FD0607E9D7F6866CF491EFF7673070DC3BD3AE2703E6E65EF1212A915EB5` · v2 `AD90715FD14B6F8EF568BCBD69CC0F123D41FF024296AD3E54D3B9FD11AB821C`

---

## 2. Node inventory delta

| Change | Result |
|--------|--------|
| Added in v2 | none |
| Removed in v2 | none |
| Shared names | all 19 identical |

- `Schedule Trigger`
- `Get many messages`
- `Add label PROCESSED`
- `Add label ERROR`
- `Remove label LEADS_ISEO`
- `Lead-Mail-Parser`
- `Prepare-OpenRouter-Request`
- `Normalize-AI-Result`
- `Normalize-Clean-Lead`
- `message v2`
- `Prepare-AI-Normalizer-Request`
- `HTTP Request (AI #1)`
- `AI-Normalizer (AI #2)`
- `Запись лида (RAW)`
- `Осмысленные лиды (CLEAN)`
- `IF - Bad Quality`
- `Remove label LEADS_ISEO2`
- `Find Duplicate Lead`
- `Mark-Duplicate-Status`

---

## 3. Connection graph

Connections are **identical** v1↔v2.

Critical topology:

1. `Lead-Mail-Parser` fans out to `Запись лида (RAW)` **and** `Prepare-OpenRouter-Request` — RAW parallel write. **DEFECT**
2. Dual AI: `HTTP Request (AI #1)` → … → `AI-Normalizer (AI #2)`. **DEFECT**
3. `Запись лида (RAW)` has no downstream.
4. Success: `Осмысленные лиды (CLEAN)` → `message v2` → PROCESSED → remove incoming.
5. Quality fail: ERROR → remove incoming (`LEADS_ISEO2`).
6. No Telegram failure branch before PROCESSED. **DEFECT** vs operator policy.

---

## 4. Code-node changes

| Node | V1 chars | V2 chars | Identical | Classification |
|------|----------|----------|-----------|----------------|
| `Lead-Mail-Parser` | 2059 | 5939 | no | **IMPROVEMENT** + residual **DEFECT** (empty `ai_reply` / AI placeholders) |
| `Prepare-OpenRouter-Request` | 875 | 1372 | no | **IMPROVEMENT** (richer prompt) / dual-AI prelude remains |
| `Normalize-AI-Result` | 587 | 587 | yes | **NEUTRAL**; **DEFECT** discards first-AI quality fields |
| `Prepare-AI-Normalizer-Request` | 1165 | 1637 | no | **REGRESSION** driver (second AI retained) |
| `Normalize-Clean-Lead` | 2032 | 2447 | no | **IMPROVEMENT** signals + **DEFECT** optimistic quality risk |
| `Mark-Duplicate-Status` | 2137 | 2137 | yes | **NEUTRAL** / weak dedupe **DEFECT** |

---

## 5. AI / sheets / telegram / dedupe

| Topic | Evidence | Class |
|-------|----------|-------|
| AI OFF path | Absent | **DEFECT** |
| AI call count | 2 HTTP nodes | **DEFECT** |
| Discarded AI #1 quality | `Normalize-AI-Result` keeps summary/service/priority/reply | **DEFECT** |
| RAW AI columns mapped | 4 AI keys on RAW append | **DEFECT** |
| CLEAN missing reply/priority/AI meta | 14 mapped keys only | **DEFECT** |
| Find Duplicate | full `lead-base-processed` read | **DEFECT** |
| Telegram fail gate | missing | **DEFECT** |
| Gmail `returnAll` | `true` | **DEFECT** |
| Active state | both false in export | **SAFE UNKNOWN** |

---

## 6. Remaining bugs for Operational.dev

1. Dual AI calls  
2. No AI OFF path  
3. RAW parallel AI-column writes  
4. Discarded AI #1 quality fields  
5. CLEAN omits first reply / priority / AI metadata  
6. Optimistic quality dominance in historical CLEAN  
7. Full-table duplicate lookup  
8. Telegram failure does not ERROR/preserve incoming  
9. Parser overflow / `#ERROR!` contacts  
10. No Admin/CONFIG in these exports  

---

*Supersedes Phase 3A logical-only comparison.*
