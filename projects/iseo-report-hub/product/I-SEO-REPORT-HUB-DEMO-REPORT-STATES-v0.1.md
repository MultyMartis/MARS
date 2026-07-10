# I-SEO Report Hub — Demo Report States v0.1

**Status:** PLANNING — demo data state model for static demo v0.3  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10  
**Implementation:** **NOT STARTED** — not real reports

---

## 1. Status

| Fact | State |
|------|-------|
| Purpose | Define **staged reporting lifecycle** for static demo v0.3 |
| Data | Fake/sanitized only — extends [I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md](I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md) |
| Audience | Operator review **before** SEO specialist feedback |
| HTML demo | **Not modified in this task** — spec for future v0.3 build |

**Key change from demo v0.2:** v0.2 showed three projects at similar monthly maturity (review/draft/approved). v0.3 must show **different reporting stages** — complete final, Week 3 active, Week 1 active.

---

## 2. Required Demo Scenario

Static demo v0.3 must show three projects at **different lifecycle stages**, not only different project types.

### Project A — Complete Final Report

| Field | Value |
|-------|-------|
| **Demo name** | Регион Сервис |
| **Client** | Демо-клиент «Регион Сервис» |
| **Site** | region-service-demo.example |
| **Project type** | Local / Regional |
| **Period** | Июль 2026 |
| **Specialist** | SEO-специалист Demo |
| **Overall status** | Final monthly report **approved / published** |

**Must include:**

| Stage | State |
|-------|-------|
| Week 1 | Completed |
| Week 2 | Completed |
| Week 3 | Completed |
| Final monthly report | Completed — all Required blocks filled |
| Client-facing report | **Available** |
| Internal notes | Hidden from client view |

---

### Project B — Week 3 In Progress

| Field | Value |
|-------|-------|
| **Demo name** | Industrial Tools |
| **Client** | Демо-клиент «Industrial Tools» |
| **Site** | demo-tools.example |
| **Project type** | E-commerce |
| **Period** | Июль 2026 |
| **Specialist** | Илья Demo |
| **Overall status** | Week 3 **active**; monthly **draft** |

**Must include:**

| Stage | State |
|-------|-------|
| Week 1 | Completed |
| Week 2 | Completed |
| Week 3 | In progress / needs review |
| Final monthly report | Draft / incomplete |
| Missing blocks | Visible in completeness panel |
| Client-facing report | **Not ready** |

---

### Project C — Week 1 In Progress

| Field | Value |
|-------|-------|
| **Demo name** | Инжиниринг Сервис |
| **Client** | Демо-клиент «Инжиниринг Сервис» |
| **Site** | engineering-demo.example |
| **Project type** | Service / Corporate |
| **Period** | Июль 2026 |
| **Specialist** | Денис Demo |
| **Overall status** | Week 1 **active**; early reporting period |

**Must include:**

| Stage | State |
|-------|-------|
| Week 1 | In progress |
| Week 2 | Not started |
| Week 3 | Not started |
| Final monthly report | Shell created — mostly empty |
| Blocks | Many **pending / empty** |
| Client-facing report | **Not ready** |

---

## 3. Data Density Rules

### Project A (complete final)

| Dimension | Density |
|-----------|---------|
| Monthly content | **Full** — all Local/Regional Required blocks with interpretation |
| Weekly summaries | All 3 weeks — condensed rollup on client report |
| KPI snapshot | 5–6 cards with deltas and notes |
| Evidence appendix | Populated — Topvisor link, SERP screenshots, schema examples |
| Executive summary | 3–4 paragraphs — wins, limits, plan preview |
| Block status | All Required → `approved` or `published` |
| Client report | Full render; no internal/reviewer fields |

### Project B (Week 3 in progress)

| Dimension | Density |
|-----------|---------|
| Monthly content | **Partial** — executive summary draft, KPI partial, works accumulated from W1–W2 |
| Week 1–2 | Full weekly blocks |
| Week 3 | Partial — works in progress, blockers updated, review flag set |
| Missing | Traffic interpretation incomplete; some Product Pages block draft |
| KPI | Present but Week 3 observations pending |
| Client report | Blocked — show reason banner |

### Project C (Week 1 in progress)

| Dimension | Density |
|-----------|---------|
| Monthly content | **Minimal** — meta shell, empty executive summary, KPI placeholders |
| Week 1 | Preliminary technical + semantic notes only |
| Week 2–3 | Empty / not started |
| KPI | 1–2 preliminary metrics if any |
| Plan | Draft bullets for week 2 |
| Client report | Blocked — «недостаточно данных за отчётный период» |

---

## 4. UI Requirements for Demo v0.3

Demo screens should communicate **lifecycle state**, not only content.

| UI element | Requirement |
|------------|-------------|
| **Project type selector** | Visible badge + filter; 5 types documented |
| **Reporting stage selector** | W1 / W2 / W3 / Final — show active stage per project |
| **Progress strip** | W1 ✓ · W2 ✓ · W3 ◐ · Final ○ (varies by project) |
| **Block completeness** | Per-block empty/draft/approved chips on monthly editor |
| **Client report availability** | Green «доступен» only Project A; amber/red for B and C with reason |
| **Not-ready reason** | Explicit text: incomplete period, draft status, missing Required blocks |
| **Dashboard** | Three cards at visibly different stages |

**Not in scope for v0.3 spec:** backend persistence, real auth, chart API.

---

## 5. Demo Project Assignment

| ID | Project | Type | Stage | Client report |
|----|---------|------|-------|---------------|
| **A** | Регион Сервис | Local / Regional | Complete final | Yes |
| **B** | Industrial Tools | E-commerce | Week 3 active | No |
| **C** | Инжиниринг Сервис | Service / Corporate | Week 1 active | No |

**Note:** Project assignment **reorders lifecycle vs v0.2 demo** (where all three had substantial monthly content). v0.3 prioritizes **staged lifecycle demonstration** over uniform monthly maturity.

---

## 6. Content Requirements Per State

### Project A — Регион Сервис (complete)

#### Weekly content

| Week | Required content |
|------|------------------|
| W1 | Regional landing drafts; LocalBusiness schema pilot; blocker: requisites pending |
| W2 | Published Tolyatti; updated Samara; FAQ + service area map; +4 geo TOP-10 |
| W3 | Zhigulevsk update; requisites on Samara; internal links; monthly submitted |

#### Monthly block fill state

| Block group | State |
|-------------|-------|
| Universal Required | 100% filled |
| Local profile blocks | 100% filled |
| Data Quality Notes | Internal — tracking regional attribution gap noted |
| Review | Approved |
| Publish | Published v1 |

#### Client visibility

All Required client blocks visible; internal notes stripped.

#### Missing data

None blocking publication (demo narrative).

#### Next action (demo)

Archive period; start August cycle (out of demo scope).

---

### Project B — Industrial Tools (Week 3)

#### Weekly content

| Week | Required content |
|------|------------------|
| W1 | Filter noindex batch; meta for 4 categories; 140 OOS SKUs flagged |
| W2 | Category texts + FAQ; 30 SKU descriptions; Topvisor +4 TOP-10 |
| W3 | Canonical on sort pages; 15 more SKUs; **in progress** — monthly exec summary draft |

#### Monthly block fill state

| Block group | State |
|-------------|-------|
| Meta, Work Completed | Draft — good coverage |
| Category/Product Pages | Draft |
| Indexing, Filters | Draft |
| Traffic / Behavior | **Empty / needs interpretation** |
| Orders / Leads | Draft with CRM caveat |
| Executive Summary | Draft |
| Review | Not submitted |

#### Client visibility

Not published — preview disabled or watermarked DRAFT only.

#### Missing data

- Traffic block interpretation
- Product Pages block completion
- Week 3 final evidence links

#### Next action

Complete Week 3 → fill traffic interpretation → submit monthly for review.

---

### Project C — Инжиниринг Сервис (Week 1)

#### Weekly content

| Week | Required content |
|------|------------------|
| W1 | **In progress** — redirects/canonical on priority services; meta rewrite started; blocker: certificates list |
| W2 | Not started |
| W3 | Not started |

#### Monthly block fill state

| Block group | State |
|-------------|-------|
| Meta | Shell only |
| Executive Summary | Empty |
| KPI Snapshot | Placeholder / partial |
| Service Pages, Leads, Commercial | Empty or stub |
| Work Completed | Empty (W1 not rolled up) |
| Plan | Week 2 draft bullets in weekly only |

#### Client visibility

Not available — period incomplete.

#### Missing data

Almost all monthly Required blocks; Weeks 2–3; KPI baselines; lead tracking status.

#### Next action

Finish Week 1 → start Week 2 service meta and commercial factors.

---

## 7. Review Questions for Operator

After static demo v0.3 build, operator should answer:

1. **Is the staged reporting lifecycle clear?** Can you tell at a glance which project is finished vs mid-month vs early month?
2. **Is it obvious why some reports are not client-ready?** Do not-ready banners and missing-block lists make sense?
3. **Does each project type show different SEO logic?** Local vs E-commerce vs Service blocks feel distinct?
4. **Is the final report (Project A) useful enough for client review?** Would you send this shape to a real client (content-wise, not data-wise)?
5. **Are there too many blocks?** Which blocks should merge or drop before SEO feedback?
6. **What should be simplified before SEO feedback?** Weekly vs monthly overlap, KPI count, profile-specific block count?

**SEO specialist feedback remains deferred** until operator approves v0.3 for feedback charter.

---

## 8. Mapping to Demo Pages (v0.3 build reference)

| Screen | Project A | Project B | Project C |
|--------|-----------|-----------|-----------|
| Dashboard | «Опубликован» badge | «Неделя 3» badge | «Неделя 1» badge |
| Project / Cycle | All stages ✓ | W1–2 ✓, W3 active | W1 active only |
| Weekly editor | Read-only complete weeks | W3 editable | W1 editable |
| Monthly editor | All blocks complete | Partial + missing alerts | Mostly empty |
| Review queue | Optional «published» row or archive | Primary row — needs review | Not in queue |
| Client report | Default showcase | Not ready message | Not ready message |

---

## 9. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact copy for not-ready banners | **UNKNOWN** — v0.3 build |
| Whether Week 1 project appears in review queue | **UNKNOWN** — recommend no |
| Chart placeholders for partial projects | **UNKNOWN** |

---

## Document control

- **Created:** 2026-07-10
- **Upstream:** Demo Content Pack v0.1, Report Content Architecture v0.1, Block Matrix v0.1
- **Does not claim:** demo v0.3 HTML exists
