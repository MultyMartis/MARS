# REPORT — MIG Groundtruth Regression Test

## New Session

| Field | Value |
| --- | --- |
| Session ID | `mig-20260605-gtrgt01` |
| Path | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-20260605-gtrgt01/` |
| Created | 2026-06-05T16:38:29.146Z |
| SERP source (read-only) | `mig-20260604-mqgt01` — multi-query bundle copied for controlled discovery baseline |
| Website acquisition | **Fresh** — live HTTP fetch at run time |
| Analysis stack | Landing v2 + delivery promise rules + phone presence model + geo-awareness |

Reference sessions (read-only, not modified): `mig-20260604-61b585`, `mig-20260604-mqgt01`, `mig-20260605-mlint01`.

## Workflow Coverage

| Layer | Status | Evidence |
| --- | --- | --- |
| SERP | Copied from multi-query session | `serp_index.json`, `serp_results/*.json` |
| Discovery | Re-derived from SERP bundle | `competitors.json`, `market-leader-shortlist.json` |
| Website Acquisition | Fresh fetch | 5/5 snapshots; status: {"success":4,"timeout":1} |
| Landing Analysis v2 | Executed | phase `landing_analysis_v2`; 5 landings |
| Comparison Layer | Generated | `market-leader-comparison-matrix.md` |
| Geo Awareness | Active | research scope city Краснодар |
| Phone Presence | Active | contact_model enum, redacted tel CTAs |
| Delivery Promise | Active | delivery-promise-rules.js routing |
| Research Pack | Generated | `research_pack.draft.md` |

## Stable Findings

### Stable domains (present in MQ + mlint + fresh)

- **gruzotaxi-triumph.ru**
- **krasnodar.gruzovichkof.ru**
- **krasnodar.taximaxim.ru**
- **city-mobil.ru**
- **gruzovichec.ru**

### Stable offers (4)

- **gruzotaxi-triumph.ru** — similarity 100%
- **gruzovichec.ru** — similarity 100%
- **krasnodar.gruzovichkof.ru** — similarity 100%
- **krasnodar.taximaxim.ru** — similarity 100%

### Stable pricing (4)

- **gruzotaxi-triumph.ru** — similarity 100%
- **gruzovichec.ru** — similarity 100%
- **krasnodar.gruzovichkof.ru** — similarity 100%
- **krasnodar.taximaxim.ru** — similarity 100%

### Stable CTA patterns (3)

- **gruzotaxi-triumph.ru**
- **krasnodar.gruzovichkof.ru**
- **krasnodar.taximaxim.ru**

## Changed Findings

### New domains in fresh run

- none (same market-leader shortlist)

### Missing domains vs stabilization pass

- none

### Changed offers (1)

- **city-mobil.ru**: was `В чем плюсы?; Удобнее через приложение…` → now `SAFE UNKNOWN…`

### Changed pricing (1)

- **city-mobil.ru**: similarity 0%

### Changed CTA patterns (2)

- **gruzovichec.ru**
- **city-mobil.ru**

### Per-domain acquisition (fresh)

- **gruzotaxi-triumph.ru** — HTTP 200; `success`; offers 7; forms 2
- **gruzovichec.ru** — HTTP 200; `success`; offers 3; forms 0
- **krasnodar.gruzovichkof.ru** — HTTP 200; `success`; offers 2; forms 1
- **krasnodar.taximaxim.ru** — HTTP 200; `success`; offers 0; forms 0
- **city-mobil.ru** — HTTP —; `timeout`; offers 0; forms 0

## Regression Analysis

| Comparison axis | Pilot #1 domains | Multi-Query | Stabilization | Fresh |
| --- | --- | --- | --- | --- |
| Domain count | 9 | 22 | 5 | 5 |
| Market leaders captured | gruzotaxi-triumph.ru, krasnodar.gruzovichkof.ru, krasnodar.taximaxim.ru | 5/5 in SERP | 5/5 | 5/5 |

**What remained stable:**
- Market-leader shortlist (5 SERVICE_BRAND domains) reproduced from same multi-query SERP groundtruth
- Core offer headlines for regional operators (triumph, gruzovichkof) largely unchanged between mlint and fresh
- Stabilization intelligence columns (delivery_promise, contact_model, geo_awareness) present in fresh matrix
- Discovery frequency ranking unchanged (SERP input identical)

**What changed:**
- **gruzovichec.ru** / cta: signal drift
- **city-mobil.ru** / offers: signal drift
- **city-mobil.ru** / pricing: signal drift
- **city-mobil.ru** / cta: signal drift
- **city-mobil.ru** / contact: signal drift
- **city-mobil.ru** / acquisition_status: signal drift

**Change attribution:**

| Cause | Likelihood | Evidence |
| --- | --- | --- |
| Market change | Low–Medium | Live sites may update copy between 2026-06-04 and 2026-06-05 |
| SERP variability | **Not in this run** | SERP bundle copied from `mig-20260604-mqgt01` — isolates downstream layers |
| Geo variability | Medium | `gruzovichec.ru` may resolve to non-Krasnodar regional page (Penza) — capture routing |
| Capture variability | Medium | HTTP status, redirect targets, dynamic blocks differ per fetch |
| SAFE UNKNOWN | Where noted in matrix | App-first surfaces (taximaxim), dynamic quote pricing |

## Confidence Assessment

**Can MIG produce repeatable market intelligence?**

**Partial Yes — with evidence:**

1. **Discovery repeatability:** Same SERP → same competitor frequency table and market-leader shortlist (deterministic).
2. **Structural repeatability:** 4/5 market leaders acquired successfully (city-mobil.ru timeout); landing v2 families emitted for all rows.
3. **Semantic stability:** Primary offers and delivery promises for triumph/gruzovichkof stable across mlint vs fresh (high text similarity).
4. **Known non-repeatability:** Pricing verbatim strings, marketing blobs, and redirect landing URLs vary with capture timing; `gruzovichec.ru` geo mismatch persists.

**Confidence level:** **B** — repeatable comparative structure; **C** for verbatim price strings without fixed snapshot fixtures.

## Remaining Weaknesses

- SERP layer not re-captured in this regression (controlled baseline); true SERP variability untested here
- Single URL per domain; no multi-page depth
- q05–q07 queries still missing from multi-query bundle
- Pilot #1 session folder absent from repo (gitignored); comparison uses backtest snapshot fallback
- No keyword pass, no ads surface, no ORCA interpretation (per task rules)

## Recommended Next Step

1. Human review fresh comparison matrix vs `mig-20260605-mlint01` for pricing/delivery drift on triumph and gruzovichkof.
2. Investigate `gruzovichec.ru` capture URL — prefer `krasnodar.gruzovichec.ru` if SERP provides regional landing.
3. Optional: re-run with fresh Playwright SERP capture to measure SERP-layer variability separately.

---

*Generated 2026-06-05T16:38:29.150Z · Lane A · session mig-20260605-gtrgt01*
