# REPORT — MIG Demand Surface — Корво Неро

> **Update 2026-06-22:** Wordstat Pass A **COMPLETE** via MARS Storage ingestion correction — see `REPORT-mig-wordstat-storage-ingestion-correction-v1.md`. Nationwide semantic discovery layer now populated (2399 rows). Regional demand and SERP grade C limitations remain.

**Session:** `mig-20260622-corv01`  
**Request:** `corvonero-yandex-direct-v1`  
**Date:** 2026-06-22  
**Lane:** A — MIG evidence acquisition  
**Boundary:** Demand Surface deposited — Wordstat two-pass policy corrected — Pass A IN PROGRESS — Research Pack **not approved** — ORCA **blocked**

**Policy note (2026-06-22):** Wordstat collection model updated to two-pass (Pass A semantic / Pass B regional). Superseded Wordstat sections in this report — see `REPORT-mig-wordstat-policy-and-serp-capability-audit-v1.md`.

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | `19b9d7f` |
| Canonical session | **`mig-20260622-corv01`** — no newer Corvonero session |
| Newer Demand Surface | **None** — this pass is canonical |
| Wordstat matrix | **Approved** — status updated to `attempted_blocked` |
| Operator approvals in scope | Wordstat matrix, manual collection mandate, competitor shortlist, bounded R1 SERP |
| Out of scope | ORCA, campaigns, landing, Research Pack, commit, push |
| Unrelated WIP | Not modified |

Contracts read: `OPERATIONAL-INDEX.md`, `MIG-KEYWORD-REGISTRY-MODEL-v1.md`, `MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md`, `MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md`, `MIG-REALITY-ACQUISITION-MODEL-v1.md`, Triumph `pilot-serp-capture-checklist.md`, manual Wordstat pilot precedent (`session-mig-20260606-kwrd01`).

---

## 2. Wordstat Collection Method

| Parameter | Value |
|-----------|-------|
| Provider | Yandex Wordstat — manual operator export |
| Primary region | **Новосибирск + Новосибирская область** |
| Matrix | `corvonero-wordstat-collection-matrix-v1.json` — 20 queries (P1: 8, P2: 7, P3: 5) |
| Syntax | Exact phrase in quotes per matrix `operator_syntax` |
| Broad/exact comparison | Planned per matrix `broad_compare` flag — **not executed** |
| Nationwide reference | Separate reference only — **not collected** |
| Evidence requirement | Screenshot or export per query_id + date + geo visible |

**Execution outcome:** Acquisition **blocked** (af-006). Wordstat landing page accessible; authenticated query UI and regional frequency export require human operator session not available in Cursor agent environment. **Zero frequencies recorded. No values estimated.**

---

## 3. Wordstat Evidence Collected

| Priority | Queries | Collected | Grade |
|----------|---------|-----------|-------|
| P1 | 8 | **0** | X_not_collected |
| P2 | 7 | **0** | X_not_collected |
| P3 | 5 | **0** | X_not_collected |
| **Total** | **20** | **0** | **X_not_collected** |

**Artifacts (structure only):**

- `wordstat-export-manual-20260622-corv01.md` — placeholder table, all NOT COLLECTED
- `wordstat_snapshot.cap-20260622-corv01.json` — 20 rows, `frequency_status: not_captured`
- `wordstat-collection-normalized.json` — full record schema per query
- `evidence/wordstat/acquisition-blocked-20260622.md` — failure log

**Task scope notes:**

- «услуги программиста 1С» — task P1 item; SERP covered (lq02); not separate matrix row
- «маркировка строительных материалов 1С» — task P3 item; **deferred** (matrix caps P3 at 5 rows)
- «ТС ПИОТ» without «1С» — matrix uses ws-p3-004 «ТС ПИОТ 1С» only

---

## 4. Exact and Broad Comparison

**Status:** `not_executed` — artifact `wordstat-broad-exact-comparison.json`

| Comparison type | Status |
|-----------------|--------|
| Broad phrase frequency | not_captured |
| Quoted exact phrase | not_captured |
| Fixed word form / order | not_applicable without UI |
| Regional (NSO primary) | not_captured |
| Nationwide reference | not_collected (separate) |
| Commercially relevant subset | unknown |

**Interpretation rule preserved:** Broad Wordstat frequency must **not** be presented as expected advertising traffic. No conflation performed because no numbers exist.

---

## 5. R1 SERP Capture

**Checklist:** Triumph `pilot-serp-capture-checklist.md`  
**Device scope:** mobile  
**Region:** Новосибирск (lr=65)

| # | Query | r1_id | R1 result | Fallback (grade C) |
|---|-------|-------|-----------|-------------------|
| 1 | программист 1С Новосибирск | r1q01 | **captcha blocked** | lq01 |
| 2 | сопровождение 1С Новосибирск | r1q02 | **captcha blocked** | lq04 |
| 3 | доработка 1С Новосибирск | r1q03 | **captcha blocked** | lq03 |
| 4 | доработка отчёта 1С Новосибирск | r1q04 | **captcha blocked** | lq09 |
| 5 | интеграция 1С с сайтом Новосибирск | r1q05 | **captcha blocked** | lq13 |
| 6 | интеграция 1С Битрикс Новосибирск | r1q06 | **captcha blocked** | lq14 |
| 7 | маркировка в 1С Новосибирск | r1q07 | **captcha blocked** | lq17 |
| 8 | Честный знак 1С Новосибирск | r1q08 | **captcha blocked** | lq19 |
| 9 | настройка ТС ПИОТ | r1q09 | **captcha blocked** | lq21 |
| 10 | программа 1С не работает Новосибирск | r1q10 | **captcha blocked** | lq06 |

**Pass summary:** 0/10 R1 successes. Failure **af-004** (Yandex captcha). **Grade not upgraded** — remains **C**. No screenshots. Ads/maps counts → SAFE UNKNOWN.

**Index:** `serp_r1_index.json` + `serp_results_r1/r1q01.json` … `r1q10.json`

---

## 6. Query Cleaning and Noise Classes

**Artifact:** `query_cleaning_noise_registry.json`  
**Purpose:** Groundtruth classification only — **not** final ORCA negative-keyword list.

### Frequent irrelevant patterns identified

| Noise class | Examples | Observed in |
|-------------|----------|-------------|
| job-seeking | вакансии, работа программистом, hh.ru | lq05, ws-p2-006 |
| educational | курсы 1С, обучение | seed matrix |
| software-download | скачать, бесплатно, демо | seed matrix |
| informational | инструкция, как настроить, форум, документация | lq20, lq21, lq06 |
| regulatory | гос. требования без запроса услуги | lq17, lq21 |
| equipment_without_service | сканер/оборудование без внедрения | seed matrix |
| operator_marking | оператор маркировки без 1С услуги | seed matrix |
| platform_self_update | обновление платформы своими руками | seed matrix |

### Intent classification summary (matrix phrases)

| Intent class | Query count (approx.) | Clusters |
|--------------|----------------------|----------|
| direct-commercial | 11 | broad, modification, reports, forms, integrations |
| commercial-mixed | 4 | support, labeling |
| troubleshooting | 2 | urgent |
| regulatory | 1 | TS PIOT |
| informational dominance (SERP) | — | TS PIOT setup, Честный знак how-to variants |

---

## 7. Demand Surface Findings

**Artifact:** `demand_surface.json`  
**Overall status:** `partial_serp_only` — grade **C_partial**

### Cluster evidence summary

| Cluster | Regional demand (SERP) | Intent | Noise | ORCA readiness |
|---------|------------------------|--------|-------|----------------|
| **Broad 1C services** | commercial demand observed (lq01–04) | commercial | low–moderate vacancy on urgent variants | conditional — volume unknown |
| **Reports and forms** | commercial demand observed (lq09–12) | direct-commercial | low | conditional |
| **Integrations** | strong — web studios dominate (lq13–16) | direct-commercial | low–moderate | conditional — segment distinct |
| **Labeling / ЧЗ** | moderate commercial + informational mix (lq17–20) | commercial-mixed | high informational | conditional — narrow landing path evidence |
| **TS PIOT** | weak commercial — informational-heavy (lq21–22) | regulatory | high informational | defer volume decisions |
| **Product labeling sample** | moderate (lq23–26) | commercial-mixed | moderate on pharma | sample only — not full catalog |
| **Troubleshooting / urgent** | mixed (lq05–08) | troubleshooting | **high vacancy** on «срочно» | needs review — noise risk |

**Neutral language used:** commercial demand observed; broad phrase dominated by informational intent (TS PIOT); evidence insufficient for volume claims.

---

## 8. Keyword Registry

**Artifact:** `keyword_registry.json`  
**State:** `draft_pending_operator_review`  
**Entries:** 20  
**keyword_pass:** `false` — status `partial`

### Review status distribution

| Status | Count | Notes |
|--------|-------|-------|
| accepted for evidence | 10 | High commercial SERP signal — volumes still unknown |
| needs review | 7 | Mixed or unmapped SERP |
| informational-only | 1 | ws-p3-004 TS PIOT |
| weak demand | 1 | ws-p2-006 срочно |
| rejected | 0 | — |

**Not labeled as final advertising keywords.** ORCA handoff eligibility: mostly `eligible_with_volume_unknown` or `needs_review` / `defer`.

---

## 9. Cluster Review

### Broad 1C services (programmer, support, modification, setup)

| Question | Evidence answer |
|----------|-----------------|
| Observable regional demand? | **Yes in SERP** (grade C) — local firms + franchisees visible |
| Commercial / mixed / informational? | **Commercial** on head terms; support mixed with ITS/info |
| Distinct formulations? | **Yes** — seed matrix + lq01–04 |
| Geo wording required? | **Yes** for head programmer cluster per matrix geo notes |
| Direct service providers in SERP? | **Yes** — Shift, Avanta, ITsVsem, Vigyana patterns |
| Ready for ORCA review? | **Conditional** — qualitative yes; volumes unknown |
| Unknown | Wordstat volumes, ad density, exact rank order |

### Reports and forms

| Question | Evidence answer |
|----------|-----------------|
| Regional demand? | **SERP yes** — Vigyana, ITLlekt, Avanta on report query |
| Intent? | **Direct-commercial** |
| Formulations? | **Yes** — reports, forms, RMK variants in matrix |
| Geo required? | **Moderate** — works without geo per matrix |
| Service providers? | **Yes** — local 1C companies |
| ORCA ready? | **Conditional** |
| Unknown | Volumes; cost-calculation / payment-calendar phrases not SERP-tested |

### Integrations (website, Bitrix, sync)

| Question | Evidence answer |
|----------|-----------------|
| Regional demand? | **SERP yes** |
| Intent? | **Direct-commercial** |
| Formulations? | **Yes** |
| Geo? | **Optional** per matrix |
| Providers? | **Web studios** (YAL, Direct Line, Studio Expert) — segment distinct from pure 1C |
| ORCA ready? | **Conditional** — segment separation evidence strong |
| Unknown | Volumes; cash-register integration not in live SERP subset |

### Labeling (generic, Честный знак, setup)

| Question | Evidence answer |
|----------|-----------------|
| Regional demand? | **Moderate in SERP** |
| Intent? | **Commercial-mixed** — AB OnlineKassa commercial; blogs/regulatory info present |
| Formulations? | **Yes** |
| Geo? | **Moderate** |
| Providers? | **Labeling/kassa specialists** + universal 1C catalogs |
| ORCA ready? | **Conditional** — high informational noise on setup phrases |
| Unknown | Volumes; hardware upsell vs pure 1C service boundary |

### Product-specific labeling (beer, water, medicines, auto parts)

| Question | Evidence answer |
|----------|-----------------|
| Regional demand? | **Moderate sample in SERP** (lq23–26) |
| Intent? | **Commercial-mixed** |
| Formulations? | **Bounded sample only** (5 matrix P3) |
| Geo? | **Low sensitivity observed** |
| Providers? | AB OnlineKassa, Vigyana price lines |
| ORCA ready? | **Defer expansion** — construction materials not in matrix |
| Unknown | Volumes per product; pharma informational risk |

### Troubleshooting (not working, errors, urgent)

| Question | Evidence answer |
|----------|-----------------|
| Regional demand? | **Mixed** |
| Intent? | **Troubleshooting** — commercial on «не работает»; vacancy on «срочно» |
| Formulations? | **Yes** |
| Geo? | **Useful but not mandatory** |
| Providers? | **Partial** — Mikos, Avanta; vacancy aggregators on urgent |
| ORCA ready? | **Needs review** — high noise on urgent lane |
| Unknown | Volumes; DIY informational share |

---

## 10. Business Context Risks

**Context (evidence only — no economics calculated):**

| Factor | Value |
|--------|-------|
| Budget | 100 000 RUB/month |
| Minimum order | 6 000 RUB |
| Historical ads | none |
| Target CPL | SAFE UNKNOWN |
| Case package | none systematic |

### Evidence risks identified

| Risk | Evidence basis |
|------|----------------|
| **Demand fragmentation** | Many distinct clusters (1C broad, reports, integrations, labeling, urgent) — SERP shows segment separation |
| **Low regional volume** | **SAFE UNKNOWN** — Wordstat not collected; cannot confirm |
| **High informational noise** | TS PIOT, Честный знак setup, urgent «срочно» vacancy pollution |
| **Strong franchise competition** | Avanta Pro, ITLlekt in multiple SERP groups |
| **Weak proof on current site** | website-corvonero-intelligence — no cases/certs/reviews vs competitors |
| **Broad phrases exceeding scope** | Head «программист 1С» competes with franchisees; single Tilda page vs narrow competitor landings |
| **Budget vs unknown CPL** | Cannot assess fit — CPL unknown |

---

## 11. Evidence Grades and Failures

| Artifact | Grade | Failure |
|----------|-------|---------|
| Wordstat snapshot | **X_not_collected** | af-006 |
| Wordstat broad/exact | **X_not_collected** | af-006 |
| R1 priority SERP | **C** | af-004 captcha — no upgrade |
| Stage 2 live SERP (fallback) | **C** | af-004 |
| Demand Surface | **C_partial** | SERP-only |
| Keyword Registry | **C_partial** | volumes missing |
| Query cleaning | **C** | SERP/matrix inference |
| Competitor shortlist | **B** | unchanged |
| Website / Landing | **B** | unchanged |

**Grade upgrade blocked:** No valid R1 screenshots; no Wordstat export.

---

## 12. Files Created or Changed

### Created

| Path |
|------|
| `wordstat-export-manual-20260622-corv01.md` |
| `wordstat_snapshot.cap-20260622-corv01.json` |
| `wordstat-collection-normalized.json` |
| `wordstat-broad-exact-comparison.json` |
| `evidence/wordstat/acquisition-blocked-20260622.md` |
| `serp_r1_index.json` |
| `serp_results_r1/r1q01.json` … `r1q10.json` |
| `demand_surface.json` |
| `keyword_registry.json` |
| `query_cleaning_noise_registry.json` |
| `REPORT-mig-demand-surface-v1.md` |
| `tools/generate-demand-surface-artifacts.mjs` |

### Modified

| Path |
|------|
| `corvonero-wordstat-collection-matrix-v1.json` (status → attempted_blocked) |
| `session_manifest.json` |
| `evidence/source-registry.json` |
| `evidence/review.md` |

### Not modified

- Stage 1/2 SERP files (preserved)
- ORCA / ATLAS / Research Pack
- Unrelated pilots and WIP

---

## 13. Validation

| Rule | Pass |
|------|------|
| Wordstat values from collected evidence only | **Yes** — zero invented |
| Regional / nationwide separated | **Yes** — nationwide not merged |
| Broad / exact not conflated | **Yes** — comparison not executed |
| Wordstat ≠ forecast traffic | **Yes** |
| SERP grade upgraded only with evidence | **Yes** — **no upgrade** |
| Keyword Registry = groundtruth not campaign | **Yes** |
| No final negative-keyword list | **Yes** |
| No ORCA / landing / Research Pack | **Yes** |
| No commit / push | **Yes** |

---

## 14. Git Status

Modified/new files under `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/`. Repository has extensive unrelated untracked WIP outside scope.

---

## 15. Recommended Selective Git Scope

When operator chooses to commit (not in this task):

```
incoming/mig/pilots/corvonero/session-mig-20260622-corv01/
```

---

## 16. Next Gate

**OPERATOR REVIEW OF MIG DEMAND SURFACE**

Operator decisions:

1. Execute manual Wordstat (20 queries + screenshots) — close af-006
2. Execute R1 mobile SERP (10 priority queries + screenshots) — upgrade path to grade B
3. Review Demand Surface cluster assessments and Keyword Registry statuses
4. Authorize or defer ORCA interpretation (future gate — not this task)

---

## 17. Stop Condition

**STOPPED** per Demand Surface charter.

**Not executed:** Research Pack assembly, ORCA handoff, campaign architecture, advertising forecast, landing architecture, landing copy, commit, push.

---

## Demand Surface Report — Review Questions (Task 9)

1. **Measurable regional demand clusters?** Broad 1C, reports/forms, integrations — **SERP commercial signal** (grade C). Volumes **unknown**.

2. **Nationwide / informational dependence?** TS PIOT, Честный знак setup phrases — **informational-heavy in SERP**. Nationwide Wordstat **not collected**.

3. **Direct commercial intent phrases?** программист 1С, доработка 1С, доработка отчёта, интеграция 1С с сайтом/Битрикс — **SERP commercial**.

4. **Noise-dominated phrases?** срочно программист 1С (**vacancy**); настройка ТС ПИОТ / подключение ЧЗ (**informational**).

5. **Product-labeling hypotheses with sufficient evidence?** Beer, water, auto parts — **moderate SERP sample**; medicines — informational risk; construction materials — **not in matrix**.

6. **Reject or defer?** Defer TS PIOT as primary commercial lane; defer urgent «срочно» without negative-class review; defer construction-materials labeling.

7. **Ready for ORCA interpretation?** **Conditional** — qualitative cluster separation supported; **volume-based prioritization not supported**.

8. **Further manual evidence?** **Wordstat (mandatory)**; **R1 SERP screenshots (mandatory for grade B)**.

9. **Common noise classes?** Vacancy, informational/how-to, regulatory, educational, software-download — see §6.

10. **Sufficiently broad for ORCA without profitability claim?** **Qualitatively yes** — multiple distinct service clusters observed. **Quantitatively unknown** — cannot claim budget adequacy or lead economics.

---

*MIG acquires reality. ORCA interprets reality.*
