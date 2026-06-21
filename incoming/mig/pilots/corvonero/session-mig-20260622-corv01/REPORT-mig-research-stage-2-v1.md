# REPORT — MIG Research Stage 2 — Корво Неро

**Session:** `mig-20260622-corv01`  
**Request:** `corvonero-yandex-direct-v1`  
**Date:** 2026-06-22  
**Lane:** A — MIG evidence acquisition  
**Boundary:** Stage 2 complete — Wordstat **not executed** — Research Pack **not approved** — ORCA **blocked**

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Git branch | `mars/post-cycle8-live-tests` |
| HEAD | `03941f7` |
| Canonical session | **`mig-20260622-corv01`** — no newer Corvonero session |
| Stage 2 structure | **Same session append** — no child run required per MIG pilot precedent |
| Research Request | Updated approval gates |
| Machine request | `operator_approval` + `stage_boundary` synchronized |
| Unrelated WIP | Not modified (Corvonero loci only) |

---

## 2. Approval State Synchronization

Synchronized across:

- `incoming/mig/pilots/corvonero/CORVONERO-MIG-RESEARCH-REQUEST-v1.md`
- `incoming/mig/requests/request-corvonero-yandex-direct-v1.json`
- `session-mig-20260622-corv01/session_manifest.json`

| Gate | Status |
|------|--------|
| Business Intake | **APPROVED** |
| ATLAS Registration | **APPROVED** |
| MIG Research Request | **APPROVED FOR EXECUTION** |
| Stage 1 | **COMPLETE** |
| Stage 2 | **AUTHORIZED** (artifacts deposited) |
| Research Pack | **NOT APPROVED** |
| ORCA handoff | **BLOCKED** until Research Pack approval |

Research scope **not rewritten**. Future stages **not** marked complete.

---

## 3. Live SERP Recapture

**Procedure:** Triumph manual SERP checklist (`pilot-serp-capture-checklist.md`) — target R1 human browser + screenshots.  
**Actual execution:** Bounded web search synthesis + failed direct Yandex fetch.

| Item | Value |
|------|-------|
| Device (declared scope) | **mobile** |
| Region | Новосибирск (lr=65 intent) |
| Collection date | 2026-06-22 |
| Pass locus | `serp_results_live/` + `serp_live_index.json` |
| Separation from Stage 1 | **Yes** — Stage 1 remains `serp_results/q01–q09` |
| Queries captured | **27** (lq01–lq27) |
| Evidence grade | **C** — **not upgraded** |

**Acquisition failure af-004:** Direct fetch to `https://yandex.ru/search/?text=…&lr=65` returned Yandex captcha («Please confirm that you are not a robot»). No R1/R2 live UI capture in this environment.

**Ads / maps:** `ads_blocks` and exact counts → **SAFE UNKNOWN** for all lq queries. Maps/local pack partially visible via synthesis (Yandex Uslugi, Maps org pages) — not verified as live SERP blocks.

### Query-group signal summary

| Group | Commercial signal | Noise |
|-------|-------------------|-------|
| Broad services (lq01–04) | **Strong** | Low |
| Urgent (lq05–08) | **Weak–moderate** | **High vacancy** on «срочно» |
| Reports/forms (lq09–12) | **Strong** | Low |
| Integrations (lq13–16) | **Strong** — web studios | Low–moderate |
| Labeling (lq17–22) | **Moderate** | **High informational** on TS PIOT / подключение |
| Product labeling sample (lq23–27) | **Moderate–weak** | Informational on pharma |

---

## 4. Query Matrix Expansion

Updated: `corvonero-seed-query-matrix-v1.json` → `stage_2_expansion`

Research labels added (not ORCA groups):

| Label | Use |
|-------|-----|
| commercial | Paid service intent |
| mixed | Blended SERP |
| informational-heavy | Blogs/regulatory |
| urgent | Failure/sрочно |
| integration | Site/Bitrix/kassa |
| regulated-labeling | ЧЗ / TS PIOT |
| product-specific | Cluster E sample |
| geo-sensitive | Novosibirsk modifier needed |
| low-confidence | Artificial stacks |

Also documented: geo-mandatory queries, natural no-geo queries, natural price/order modifiers, artificial combinations.

---

## 5. Confirmed Competitor Shortlist

**Artifact:** `competitors-shortlist-confirmed.json`  
**Count:** 9 (7 confirmed competitors + 2 pattern references)

| ID | Name | Class | Role |
|----|------|-------|------|
| corv-s001 | Shift Company | Local NSO | confirmed — SERP recurrence (fetch timeout) |
| corv-s002 | Profinfoservice | Local NSO | confirmed — support landing |
| corv-s003 | Vigyana | Local NSO | confirmed — universal price catalog |
| corv-s004 | Avanta Pro | Local franchisee | confirmed — partner claim + reviews |
| corv-s005 | ITLlekt | Local franchisee | confirmed — modification table |
| corv-s006 | AB OnlineKassa | Labeling NSO | confirmed — ЧЗ commercial |
| corv-s007 | Студия ЯЛ | Integration studio | confirmed |
| corv-s008 | Studio Expert | Integration | pattern reference |
| corv-s009 | LegaSoft SPb | Labeling federal | pattern reference (TS PIOT) |

Excluded: aggregators, MSB centers, official 1C docs, pure blogs.

---

## 6. Website Intelligence

**Artifact:** `website_intelligence.json`  
**Method:** Bounded HTTP fetch — 6/7 shortlist URLs captured (grade **B**)

### Cross-site patterns (observation only)

| Pattern | Prevalence |
|---------|------------|
| Hourly or line-item pricing | Common (Avanta 2200 ₽/h; Vigyana/ITLlekt from 1500–3200; AB SKU prices) |
| Official 1C partner claim | Avanta, ITLlekt — **claimed_by_competitor**, not externally verified here |
| SLA / 24-7 messaging | Profinfoservice, Vigyana, AB OnlineKassa |
| Reviews / cases | Avanta reviews; YAL portfolio; Corvonero **none** |
| Universal vs narrow pages | Vigyana = universal catalog; ITLlekt/YAL/AB = narrower; Avanta broad programmer page |

No conversion performance claims.

---

## 7. Landing Intelligence

**Artifact:** `landing_intelligence_v2.json`  
**Cards:** 5 (4 competitor + WEB-CORV-01)

| Page | Intent match | Narrow vs universal |
|------|--------------|---------------------|
| Avanta programmer | High broad | Medium specificity |
| ITLlekt dorabotka | High narrow | High — price table |
| YAL integration | High integration | Narrow segment |
| AB marking | High ЧЗ | Niche + hardware upsell |
| Corvonero lk | Low per-query | Single brochure — all services |

Evidence descriptions only — **not** landing architecture.

---

## 8. Corvonero Website Findings

**Artifact:** `website-corvonero-intelligence.json` (extends Stage 1 snapshot)

| Topic | Finding |
|-------|---------|
| Structure | Single Tilda page — anchors only |
| Services | Broad blocks incl. marking/integration/reports |
| Configurations | **Not named on site** vs intake list → **contradiction** |
| Pricing | 3000 ₽/h aligned with intake; min 6000 ₽ **not on site** |
| Trust | Process blocks only — **no cases/certs/partners/reviews** |
| Intake alignment | Proof gap **confirmed** — matches intake §4.5 |

---

## 9. Wordstat Collection Matrix

**Artifact:** `corvonero-wordstat-collection-matrix-v1.json`  
**Status:** **PREPARED — NOT EXECUTED**

| Priority | Count | Focus |
|----------|-------|-------|
| P1 | 8 | Broad commercial, support, modification, integration, marking |
| P2 | 7 | Reports, RMK, sync, urgent variants |
| P3 | 5 | Product marking sample, TS PIOT |

No invented frequencies. Reformulation candidates documented before collection.

---

## 10. Evidence Grades and Failures

| Artifact | Grade | Failure |
|----------|-------|---------|
| Stage 1 SERP | C | af-001 (unchanged) |
| Stage 2 live SERP | C | af-004 Yandex captcha |
| Shortlist | B | — |
| Website Intelligence | B | af-005 Shift timeout |
| Landing Intelligence | B | — |
| Corvonero site | B | — |
| Wordstat matrix | A (plan) | af-002 not collected |

**Grade upgrade blocked:** Without operator R1 manual SERP + screenshots, live pass remains **C**.

---

## 11. Stage 2 Findings (review questions)

1. **Market classes in SERP:** local 1C companies, franchisees, web/integration studios, labeling/kassa integrators, aggregators (Yandex Uslugi), informational/regulatory content, vacancy noise on urgent queries.

2. **Direct local competitors:** Shift, Profinfoservice, Vigyana, Avanta Pro, ITLlekt, AB OnlineKassa (marking), YAL (integration).

3. **Pattern references:** Studio Expert (Bitrix integration); LegaSoft (TS PIOT federal).

4. **Segment separation:** **Yes** — integrations dominated by web studios; marking by kassa/ЧЗ vendors + info content; broad 1C by franchisees/local firms.

5. **Narrow vs universal pages:** ITLlekt/AB/YAL narrow; Vigyana universal catalog; Corvonero single universal page.

6. **Common offers/trust:** hourly/table pricing, 24/7 or SLA claims, partner badges (competitors), reviews/portfolio (competitors) — **absent on Corvonero**.

7. **Claims Corvonero cannot use without proof:** client counts, cases, certificates, official partner status, SLA — market shows these patterns; client intake confirms proof gap.

8. **Separate landing categories:** **Evidence supports** distinct SERP/landing paths for integration and marking vs broad programmer — not a strategic verdict.

9. **Wordstat-ready clusters:** P1 broad/support/modification/integration/marking — **ready after operator approves matrix**.

10. **Reformulate before Wordstat:** urgent/vacancy queries; TS PIOT informational variants; verify geo on head terms.

11. **Sufficient for Demand Surface entry?** **Conditionally yes after operator review** — SERP + site intelligence adequate to **start manual Wordstat**; volumes still **SAFE UNKNOWN**.

---

## 12. Files Created or Changed

### Created

| Path |
|------|
| `session-mig-20260622-corv01/serp_live_index.json` |
| `session-mig-20260622-corv01/serp_results_live/lq01.json` … `lq27.json` |
| `session-mig-20260622-corv01/competitors-shortlist-confirmed.json` |
| `session-mig-20260622-corv01/website_intelligence.json` |
| `session-mig-20260622-corv01/landing_intelligence_v2.json` |
| `session-mig-20260622-corv01/website-corvonero-intelligence.json` |
| `session-mig-20260622-corv01/corvonero-wordstat-collection-matrix-v1.json` |
| `session-mig-20260622-corv01/REPORT-mig-research-stage-2-v1.md` |
| `session-mig-20260622-corv01/tools/generate-stage2-live-serp.mjs` |

### Modified

| Path |
|------|
| `CORVONERO-MIG-RESEARCH-REQUEST-v1.md` |
| `incoming/mig/requests/request-corvonero-yandex-direct-v1.json` |
| `corvonero-seed-query-matrix-v1.json` |
| `session-mig-20260622-corv01/session_manifest.json` |
| `session-mig-20260622-corv01/evidence/source-registry.json` |
| `session-mig-20260622-corv01/evidence/review.md` |

### Not modified

- Stage 1 SERP files (`serp_results/q01–q09`) — preserved
- ORCA / ATLAS / Business Intake
- Triumph / Makita pilots

---

## 13. Validation

| Rule | Pass |
|------|------|
| Approval states consistent | Yes |
| Stage 1 complete unchanged | Yes |
| Live SERP separated from Stage 1 | Yes |
| Grade upgraded only where justified | Yes — **no upgrade** (C retained) |
| Shortlist evidence-based | Yes |
| No conversion claims | Yes |
| Landing Intel ≠ architecture | Yes |
| Wordstat matrix without volumes | Yes |
| No ORCA / campaigns / copy | Yes |
| No Wordstat execution | Yes |
| No commit / push | Yes |

---

## 14. Git Status

New/modified untracked files under `incoming/mig/pilots/corvonero/` and `incoming/mig/requests/request-corvonero-yandex-direct-v1.json`. Repository has unrelated WIP outside scope.

---

## 15. Recommended Selective Git Scope

When operator chooses to commit (not in this task):

```
incoming/mig/pilots/corvonero/
incoming/mig/requests/request-corvonero-yandex-direct-v1.json
```

---

## 16. Next Gate

**OPERATOR REVIEW OF MIG RESEARCH STAGE 2 AND WORDSTAT MATRIX**

Operator decisions:

- Mandate R1 manual Yandex mobile SERP for priority queries (grade B path)
- Approve Wordstat matrix → authorize manual collection
- Confirm shortlist for Research Pack track
- Resolve Corvonero intake/site contradictions

---

## 17. Stop Condition

**STOPPED** per Stage 2 charter.

**Not executed:** Wordstat collection, Keyword Registry final, Research Pack assembly, ORCA strategy, campaign architecture, landing architecture, landing copy, commit, push.

---

*MIG acquires reality. ORCA interprets reality.*
