# MIG MVP Validation Freeze v1

**Status:** **FROZEN** — evidence-only snapshot of proven MVP capabilities  
**Date:** 2026-06-05  
**Lane:** A (MIG MVP Validation)  
**Scope:** One validated market — **Грузотакси / Краснодар / проект Триумф**  
**Not in scope:** redesign, new capabilities, Wordstat, Deep Research, ORCA integration, new runtime

---

## Purpose

Record what MIG has **actually proven** on a real market through human-supervised pilot sessions. This document is the canonical **MVP validation freeze** — reality as it exists today, not planned architecture.

**Groundtruth rule:** MIG acquires reality; ORCA interprets reality. Nothing here authorizes strategy synthesis or automated ORCA handoff.

---

## Validated sessions

| Session ID | Role | Path / reference |
| --- | --- | --- |
| `mig-20260604-61b585` | Pilot #1 — single-query groundtruth run | `projects/mig/sessions/mig-20260604-61b585/` (local; gitignored) · outcome: `incoming/mig/completed/request-triumph-gruzotaxi-krasnodar-v1.outcome.json` · SERP evidence: `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-20260604/` |
| `mig-20260604-mqgt01` | Multi-query SERP groundtruth (8/11 queries) | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260604-mqgt01/` |
| `mig-20260605-mlint01` | Market-leader intelligence + stabilization pass | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260605-mlint01/` |
| `mig-20260605-gtrgt01` | Groundtruth regression test (fresh acquisition) | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260605-gtrgt01/` |

**Pilot package:** `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/`

**Regression report:** `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/REPORT-mig-groundtruth-regression-test.md`

**Stabilization report:** `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260605-mlint01/REPORT-mig-stabilization-pass-v1.md`

---

## Validation Matrix

| Layer | Status | Evidence | Known limitations | Confidence |
| --- | --- | --- | --- | --- |
| **SERP Acquisition** | **Proven (manual + Playwright)** | Pilot #1: real Yandex mobile SERP for `грузотакси краснодар` — `evidence/serp-20260604/capture-notes.md`, screenshots, `capture-raw.json`. Multi-query: 8 captures in `evidence/serp-multi-20260604/`, normalized to `session-mig-20260604-mqgt01/serp_index.json`, `serp_results/q*.json`. | Manual/operator-invoked only; no live SERP provider API. q05–q07 not captured. Headless Playwright ≠ logged-in human phone; personalization unknown. Regression run (`gtrgt01`) copied SERP — did not re-capture SERP variability. | **B** — real captures exist; partial query set; variability across re-runs not measured in regression |
| **Competitor Discovery** | **Proven (MVP)** | Pilot #1: 9 competitors from single SERP — `outcome.json` → `competitors.json`. Multi-query: 22 entities, 12 repeated domains — `session-mig-20260604-mqgt01/competitors.json`, `competitor-frequency-table.md`. Deterministic re-derivation from same SERP in `gtrgt01`. | Single-query Pilot #1: `rule_repeated_domain` inert. Aggregator/marketplace classification requires human review. yabs promo hrefs may omit destination URL. | **B** — repeatable from fixed SERP bundle; frequency ranking stable when input identical |
| **Multi-Query Discovery** | **Proven (partial coverage)** | 11-query set declared in `multi-query-market-query-set-v1.md`; 8 executed (q01–q04, q08–q11) — `session-mig-20260604-mqgt01/session_manifest.json` `queries_executed`. Cross-query recurrence surfaced market leaders (e.g. `krasnodar.gruzovichkof.ru` on 7 distinct queries). | q05 (`перевозка мебели`), q06 (`квартирный переезд`), q07 (`вызов газели`) — `execution_status: failed`; entities from those intents absent. | **B−** — multi-query value proven on 8/11; incomplete market surface |
| **Website Acquisition** | **Proven (MVP, single URL/domain)** | mlint01: 5/5 HTTP 200, `success` — `REPORT-top-repeated-domains-intelligence-pass.md`. gtrgt01 fresh fetch: 4/5 success, 1 timeout (`city-mobil.ru`) — `website-acquisition-summary.json`, `snapshots/sites/`. Pilot #1: website pass executed per outcome.json. | One URL per domain (homepage or SERP landing). No multi-page crawl. `city-mobil.ru` timeout on regression (was success in mlint01). Capture timing affects dynamic blocks. | **B** — reliable for 4/5 market leaders; acquisition failures recorded honestly |
| **Landing Analysis v2** | **Proven** | Phase `landing_analysis_v2` on all 5 shortlist domains — `landing_observations.json`, per-landing JSON under `landings/`. Families: OFFERS, PRICING, DELIVERY_PROMISE, CTA, CONTACT_MODEL, TRUST, etc. Pilot #1 session is design SoT per contracts. | App-first surfaces (taximaxim) → many SAFE UNKNOWN columns. Verbatim blobs may embed tel fragments in pricing/marketing copy. | **B** — structured observations emitted; semantic gaps flagged as SAFE UNKNOWN |
| **Research Pack** | **Proven (draft)** | `research_pack.draft.md` generated in all full-stack sessions (61b585, mqgt01, mlint01, gtrgt01). Rebuilt after stabilization pass. | No `research_pack.approved.md` in freeze evidence — human approval not recorded. Not ORCA-ready without Approved By. | **B** — draft generation reliable; approval workflow not implemented |
| **Comparison Matrix** | **Proven (repaired)** | `market-leader-comparison-matrix.md` + `.json` in mlint01 and gtrgt01. Columns: Primary Offer, Pricing, Delivery Promise, Trust, Lead Capture, Contact Model, Geo Awareness, Page Structure, Evidence refs. Regression: 4/5 domains stable offers/pricing at similarity 100%. | Truncated cells in markdown export. city-mobil.ru → SAFE UNKNOWN after timeout in gtrgt01. | **B** — comparative structure repeatable; row completeness depends on acquisition success |
| **Geo Awareness** | **Proven (flag-only)** | `geo-awareness.js` — compares `session_manifest.scope.city` to visible city tokens. **gruzovichec.ru** flagged: `research_target: Краснодар; observed: пензе` — matrix in gtrgt01, stabilization report. | Flags mismatch; does not correct URL routing. Lexicon pilot-scoped (Krasnodar, Penza, Moscow, SPb); other cities → SAFE UNKNOWN. Root cause: capture hit `https://gruzovichec.ru/` (Penza homepage), not regional landing. | **B** — detection works; remediation not in MVP |
| **Phone Presence** | **Proven** | Stabilization pass: raw numbers removed from matrix/pack contact sections; emits `phone_present`, `phone_prominent`, `contact_model` enum. CTAs redacted to `Phone CTA → tel:[present]`. Raw numbers remain in `website_snapshot.json`, `page.html`, `_legacy`. | Marketing/pricing blobs may still contain embedded tel fragments. | **B+** — contact_model intelligence reliable in comparison layer |
| **Delivery Promise** | **Proven (repaired)** | `delivery-promise-rules.js` routes time-token segments from trust/pricing/meta to DELIVERY_PROMISE. Verified: triumph «20 минут», gruzovichkof «15 минут», gruzovichec «20 минут» — stabilization report + gtrgt01 regression (`similarity: 1` on delivery fields). | Negative rules and segment extraction pilot-tuned; edge cases in dynamic/app copy → SAFE UNKNOWN. | **B+** — primary promises extracted and stable across mlint vs fresh |

---

## Proven Capabilities

Evidence-backed findings only.

### Market discovery

- **Same market leaders found repeatedly** across multi-query SERP: 5 SERVICE_BRAND domains in shortlist — `gruzotaxi-triumph.ru`, `gruzovichec.ru`, `krasnodar.gruzovichkof.ru`, `krasnodar.taximaxim.ru`, `city-mobil.ru` — `session-mig-20260605-mlint01/market-leader-shortlist.json`.
- **Cross-session shortlist stability:** identical 5-domain shortlist reproduced in `gtrgt01` from copied SERP bundle — regression report §Stable domains.
- **Multi-query expands surface vs single query:** 22 entities (multi-query) vs 9 (Pilot #1) — `REPORT-mig-multi-query-groundtruth-pilot.md`.
- **Core organic brands recur:** `krasnodar.gruzovichkof.ru` (7 distinct queries), `gruzovichec.ru` (6), `gruzotaxi-triumph.ru` (2), `krasnodar.taximaxim.ru` (3), `city-mobil.ru` (3).

### Landing intelligence

- **Pricing reproduced** at 100% text similarity (mlint vs fresh) for: `gruzotaxi-triumph.ru` (от 960 ₽/час, от 1260 ₽/час…), `gruzovichec.ru` (от 690 руб.), `krasnodar.gruzovichkof.ru`, `krasnodar.taximaxim.ru` — `regression-comparison.json`.
- **Delivery promises reproduced:** triumph «Автомобиль будет подан, через 20 минут или быстрее!»; gruzovichkof «подача за 15 минут»; gruzovichec «от 20 минут» — stable across mlint and gtrgt01.
- **Comparison matrix repaired:** DELIVERY_PROMISE column populated (was misclassified in trust/pricing) — `REPORT-mig-stabilization-pass-v1.md`.
- **Contact model without raw PII** in operator-facing matrix: `phone_present`, `phone_prominent`, `contact_model: mixed|app_first|…`.

### Geo and acquisition honesty

- **Geo mismatch detected:** `gruzovichec.ru` — research target Краснодар, page shows Penza — flagged in matrix, not silently corrected.
- **Acquisition failures recorded:** `city-mobil.ru` timeout in gtrgt01 → SAFE UNKNOWN rows; not fabricated.

### Runtime spine (human-supervised)

- Task File Adapter intake → `runMigSession` → manifest v0.2 → artifact chain — Pilot #1 outcome `status: completed`, `stage: partial_complete`.
- End-to-end stack through comparison matrix + research pack draft on market-leader shortlist — mlint01, gtrgt01 manifests `capture_profile`: serp, discovery, website, landing = true.

---

## Known Limitations

No solutions — reality only.

| Limitation | Evidence |
| --- | --- |
| **city-mobil.ru timeout** | gtrgt01: HTTP —, `timeout`; all matrix columns SAFE UNKNOWN for that row. mlint01 had success at `https://city-mobil.ru/krasnodar/gruz-taxi`. |
| **Regional routing anomalies** | `gruzovichec.ru` resolves to Penza homepage despite Krasnodar SERP recurrence; geo_mismatch flagged, not fixed. |
| **Partial query coverage (q05–q07)** | `session_manifest.json`: q05, q06, q07 `execution_status: failed`; furniture move / apartment move / dispatch wording intents not in groundtruth. |
| **Single-domain acquisition depth** | One URL per domain; no multi-page crawl — stated in intelligence pass and regression reports. |
| **SERP variability untested in regression** | gtrgt01 copied SERP from mqgt01; true re-capture drift not measured. |
| **Pilot #1 session folder gitignored** | Local path `projects/mig/sessions/mig-20260604-61b585/`; regression uses outcome + backtest references. |
| **No keyword pass** | `keyword_pass: false` in all manifests — Wordstat not started (per freeze rules). |
| **No deep research pass** | `deep_research_pass: false` — synthesis memo not implemented. |
| **No ORCA automation** | No approved pack, no transport API — handoff contract not exercised end-to-end. |
| **Dynamic / app-first pricing** | taximaxim: «окончательная стоимость появится на экране приложения» — page-visible SAFE UNKNOWN for fixed price. |
| **Verbatim price string drift** | Confidence **C** for verbatim strings without fixed snapshot fixtures — regression confidence assessment. |

---

## Readiness Assessment

### What MIG can reliably do today

1. **Accept** a groundtruth Research Request via Task File Adapter (human-invoked).
2. **Normalize** manual or Playwright-captured Yandex mobile SERP into session artifacts.
3. **Discover** competitors from SERP URLs with multi-query frequency ranking and entity typing.
4. **Shortlist** repeated SERVICE_BRAND market leaders with evidence refs.
5. **Acquire** one page per domain via HTTP fetch; record success/timeout/failure.
6. **Extract** landing observations v2 (offers, pricing, delivery promise, trust, CTA, contact model).
7. **Generate** facts-only comparison matrix and draft research pack with SAFE UNKNOWN for gaps.
8. **Flag** geo mismatch and redact phone CTAs in operator-facing intelligence layers.
9. **Reproduce** discovery and comparative structure from identical SERP input (regression proven).

**Validated market:** Грузотакси Краснодар only. Generalization to other niches/regions is **not proven** in this freeze.

### What MIG cannot reliably do today

1. **Fully automated** unattended research sessions (human-supervised operator workflow).
2. **Complete query-set coverage** when capture fails (3/11 queries missing).
3. **Guaranteed acquisition** of every shortlist domain (city-mobil.ru demonstrated timeout).
4. **Correct regional landing** selection when SERP URL routing is ambiguous.
5. **Verbatim-stable pricing strings** across live re-fetches without fixed fixtures.
6. **Multi-page** or deep site crawl intelligence.
7. **Keyword volumes**, ads surface analysis, or Wordstat integration.
8. **Deep research synthesis** or strategic interpretation.
9. **ORCA-ready approved handoff** without human approval step.
10. **Production n8n deployment** or approval automation.

### Confidence summary

| Area | Level | Basis |
| --- | --- | --- |
| Discovery from fixed SERP | B | Deterministic re-derivation in gtrgt01 |
| Comparative matrix structure | B | 4/5 leaders stable; columns include repaired layers |
| Verbatim pricing strings | C | Live capture drift; city-mobil regression failure |
| Single-market pilot | B | Four sessions, one niche/geo; not multi-market |

---

## SAFE UNKNOWN

Items **not provable** from freeze evidence:

- SERP ranking drift if queries re-captured on a different day or device profile.
- Logged-in Yandex personalization effects on competitor visibility.
- Actual dispatch price at order time (only page-visible text captured).
- Conversion performance, ad spend, fleet size, operational capacity.
- Whether entities visible only on q05–q07 would change market-leader shortlist.
- Repeatability on markets other than Грузотакси / Краснодар.
- Production runtime uptime, scaling, or unattended error recovery.
- ORCA consumption quality of draft packs (no approved handoff in evidence).

---

## Freeze boundaries

**Included:** MVP session spine, manual/Playwright SERP, competitor discovery, website acquisition, landing analysis v2, comparison matrix, geo awareness, phone presence model, delivery promise rules, research pack draft — as evidenced in four sessions above.

**Explicitly excluded from this freeze (not started / not proven):**

- Wordstat / keyword intelligence pass
- Deep Research synthesis pass
- ORCA integration / automated handoff
- Multi-page website acquisition
- Live SERP provider API
- New capabilities or architecture redesign

---

## Evidence index (quick links)

| Report | Path |
| --- | --- |
| Multi-query pilot | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/REPORT-mig-multi-query-groundtruth-pilot.md` |
| Intelligence pass | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/REPORT-top-repeated-domains-intelligence-pass.md` |
| Stabilization pass | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260605-mlint01/REPORT-mig-stabilization-pass-v1.md` |
| Regression test | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/REPORT-mig-groundtruth-regression-test.md` |
| Comparison matrix (latest) | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260605-gtrgt01/market-leader-comparison-matrix.md` |
| Pilot #1 outcome | `incoming/mig/completed/request-triumph-gruzotaxi-krasnodar-v1.outcome.json` |

---

*MIG MVP Validation Freeze v1 · 2026-06-05 · evidence only · no redesign*
