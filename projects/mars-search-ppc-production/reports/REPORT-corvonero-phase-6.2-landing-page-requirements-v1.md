# REPORT — CORVONERO PHASE 6.2 LANDING PAGE REQUIREMENTS V1

**Generated:** 2026-06-29  
**Branch:** `mars/canonical-post-recovery`  
**Scope:** Landing-page requirements pack only — no website changes, no ad creation

---

## 1. Safety and Authorization

| Check | Status |
|-------|--------|
| External model API (OpenRouter) | **NONE** |
| Website modification | **NONE** — read-only Phase 6.1 audit reused |
| Semantic registries modified | **NONE** |
| Campaign architecture sources modified | **NONE** |
| Commander / Yandex import | **NOT AUTHORIZED** |
| Ad copy / minus-word deployment | **NOT AUTHORIZED** |

Task executed with local Cursor reasoning only against committed Phase 6.1 and Phase 5.2 authority artefacts.

---

## 2. Git Preflight

| Item | Result |
|------|--------|
| Branch | `mars/canonical-post-recovery` |
| HEAD | `09e6e8ea` — descends from checkpoint `88facdb7` |
| Phase 6.1 artefacts | **Present** (17 files) |
| Campaign family ACCEPT total | **935** (404+155+71+48+220+37) |
| Ad groups | **21** |
| Group phrase reconciliation | **935 unique IDs, 0 duplicates, 0 missing** |
| Provider calls | **NONE** |
| Commit / push | **Not performed** (per git policy) |

---

## 3. Input Authority

| Artefact | Role |
|----------|------|
| `CORVONERO-PHASE-6.1-CAMPAIGN-FAMILIES-v2.json` | Six CA families, phrase counts, LP gap flags |
| `CORVONERO-PHASE-6.1-AD-GROUP-ARCHITECTURE-v2.json` | 21 groups, intents, representative phrases |
| `CORVONERO-PHASE-6.1-PHRASE-ALLOCATION-v2.json` | 935 ACCEPT manifest |
| `CORVONERO-PHASE-6.1-WEBSITE-PAGE-INVENTORY-v1.json` | lk.corvonero.ru homepage + /products crawl |
| `CORVONERO-PHASE-6.1-LANDING-PAGE-AUDIT-v1.*` | Suitability classes per campaign |
| `CORVONERO-PHASE-6.1-LANDING-PAGE-MATRIX-v2.json` | Group-level LP readiness |
| `CORVONERO-PHASE-6.1-EXCLUSION-BOUNDARIES-v2.json` | Intent exclusion families |
| `CORVONERO-PHASE-6.1-READINESS-MATRIX-v1.*` | Pre-6.2 readiness baseline |
| `CORVONERO-PHASE-6.1-RESULT-v1.*` | Phase 6.1 reconciliation proof |
| Phase 5.2 final registries | Semantic authority boundary (1599/2368, 67.5%) |

Partial semantic authority unchanged: **935 ACCEPT / 368 REJECT / 296 ABSTAIN / 769 backlog**.

---

## 4. Operator Decisions

Recorded in `CORVONERO-PHASE-6.2-OPERATOR-DECISIONS-v1.json`:

| ID | Decision |
|----|----------|
| **RD-01** | `corvonero.ru` **PROHIBITED** as LP; `lk.corvonero.ru` **temporary generic fallback only**; dedicated service LPs **required before normal ad launch** |
| **RD-02** | P1 must not launch to one homepage; **LP-01..LP-05 required** |
| **RD-03** | **LP-06 P2** — required before CA-06; not in automatic initial launch |
| **RD-04** | Product resale **SAFE UNKNOWN**; `/products` **NOT APPROVED** for service campaigns; product-plus-service **HOLD** |
| **RD-05** | Primary geo **Новосибирск + Новосибирская область**; expansion **NOT AUTHORIZED** until primary-launch evidence |

---

## 5. Existing Homepage Evidence

Source: Phase 6.1 audit of `https://lk.corvonero.ru/`

**Reusable (with verification):**

- Phone **+7 (383) 390-29-28** (CONFIRMED on homepage)
- Brand «Корво Неро», meta «Центр автоматизации 1с»
- Generic proposition: внедрение, настройка, обновление, сопровождение 1С
- Menu anchors: Услуги, Цены, О нас, Контакты
- Partial trust signal: clients/cases (not service-specific)

**Missing or inadequate for all LP-01..LP-06:**

- Dedicated URL per service family
- Service-specific H1 and first-screen message match
- Explicit geography statement for campaign targeting
- Service-specific CTA copy
- Verified pricing, SLA, certifications, case studies

**Must not reuse without verification:**

- Цены anchor rates; partner badges; `/products` catalog pricing; Russia-wide claims

**corvonero.ru:** IIS default — **LP_NOT_SUITABLE**, prohibited per RD-01.

Full map: `CORVONERO-PHASE-6.2-EXISTING-CONTENT-EVIDENCE-MAP-v1.json`

---

## 6. Required Landing Pages

| LP | Campaign | Phrases | Groups | Priority |
|----|----------|---------|--------|----------|
| LP-01 | CA-01 Программист / специалист 1С | 404 | 3 | P1 |
| LP-02 | CA-02 Сопровождение | 155 | 6 | P1 |
| LP-03 | CA-03 Доработка и разработка | 71 | 3 | P1 |
| LP-04 | CA-04 Интеграции | 48 | 1 | P1 |
| LP-05 | CA-05 Маркировка / Честный знак | 220 | 5 | P1 |
| LP-06 | CA-06 Отчёты и обработки | 37 | 3 | P2 |

---

## 7–12. LP Requirements Summary

Each LP has paired `.md` + `.json` with sections A–H (commercial purpose, intent coverage, content blocks, message evidence, conversion, ad alignment, geography, SEO/technical).

| LP | Recommended slug | H1 direction (planning) |
|----|------------------|-------------------------|
| LP-01 | `programmist-1s` | Программист 1С в Новосибирске — услуги специалиста |
| LP-02 | `soprovozhdenie-1s` | Сопровождение и обслуживание 1С в Новосибирске |
| LP-03 | `dorabotka-razrabotka-1s` | Доработка и разработка 1С под задачи бизнеса |
| LP-04 | `integracii-1s` | Интеграция 1С с сайтом, Bitrix и внешними системами |
| LP-05 | `markirovka-chestny-znak` | Маркировка и Честный знак в 1С — настройка и сопровождение |
| LP-06 | `otchety-obrabotki-1s` | Разработка отчётов и обработок 1С |

Message evidence default classifications across all LPs: phone CONFIRMED; hourly rates and SLA **PROHIBITED_UNSUPPORTED**; partner status and remote scope **NEEDS_CLIENT_CONFIRMATION**.

---

## 13. Group-to-Page Mapping

`CORVONERO-PHASE-6.2-GROUP-TO-LP-MAP-v1.json`

| Rule | All 21 groups → exactly one LP-01..LP-06 by campaign family |
|------|---------------------------------------------------------------|

**Reconciliation:**

```text
935 ACCEPT = 935 page-mapped IDs + 0 HOLD
duplicates: 0 | missing ACCEPT: 0
REJECT allocated: 0 | ABSTAIN allocated: 0 | backlog allocated: 0
PASS: true
```

Product-scope HOLD IDs: **0** (product demand excluded at Phase 6.1 allocation per OD-03).

---

## 14. Content Evidence Requirements

`CORVONERO-PHASE-6.2-CONTENT-EVIDENCE-REQUIREMENTS-v1.json`

**UNKNOWN_BLOCKING (12 fields):** exact service scope, supported configurations, response times, pricing model, subscription terms, NDS/VAT, certificates/partner status, project examples, remote scope, on-site boundary, and related.

**PARTIALLY_KNOWN:** typical tasks, integration systems, marking/TS ПИОТ, geography, staff expertise, testimonials.

**SAFE UNKNOWN:** product/license sales scope (RD-04).

---

## 15. Production Priority

`CORVONERO-PHASE-6.2-LP-PRODUCTION-PRIORITY-v1.json`

```text
1. LP-01 — Программист (404 phrases, highest volume)
2. LP-02 — Сопровождение (155, closest homepage match)
3. LP-05 — Маркировка (220, distinct intent cluster)
4. LP-03 — Доработка (71)
5. LP-04 — Интеграции (48)
6. LP-06 — Отчёты (37, P2 — defer from initial wave per RD-03)
```

---

## 16. Interim Homepage Policy

`CORVONERO-PHASE-6.2-INTERIM-HOMEPAGE-POLICY-v1.*`

| Campaign | Classification |
|----------|----------------|
| CA-01, CA-03, CA-04, CA-05 | INTERIM_FALLBACK_HIGH_RISK |
| CA-02 | INTERIM_FALLBACK_POSSIBLE (still not authorized) |
| CA-06 | INTERIM_FALLBACK_PROHIBITED |

**No launch authorized.** Minimum changes before any fallback test: dedicated section/URL, service H1, geo statement, service CTA, separation from `/products`.

---

## 17. Website Implementation Handoff

`CORVONERO-PHASE-6.2-WEBSITE-IMPLEMENTATION-HANDOFF-v1.*`

Standalone handoff for website development: six pages on `lk.corvonero.ru`, acceptance criteria, evidence gaps, technical constraints, prohibited assumptions. CMS not prescribed.

---

## 18. Campaign Readiness Matrix

`CORVONERO-PHASE-6.2-CAMPAIGN-READINESS-MATRIX-v2.*`

| Dimension | CA-01..CA-06 |
|-----------|--------------|
| Semantic | READY (within 67.5% partial authority) |
| Architecture | READY (CONSOLIDATED_V2) |
| LP specification | READY (Phase 6.2 pack) |
| Content evidence | NOT READY |
| Current website | LP_GENERIC_FALLBACK or LP_PARTIAL_MATCH |
| Ad design | NOT READY |
| **Final state** | **READY_FOR_LP_PRODUCTION** |

`READY_FOR_AD-DESIGN` **not used** — no approved dedicated LP exists.

---

## 19. Operator Decision Packet

`CORVONERO-PHASE-6.2-OPERATOR-DECISION-PACKET-v3.*`

**11 open decisions (ODP-01..ODP-11):** configurations, remote scope, on-site boundary, product sales, NDS/VAT, pricing disclosure, response times, cases/reviews, certificates, production platform, LP-06 first-wave timing.

No fabricated answers.

---

## 20. Phase 6.2 Verdict

```text
PHASE 6.2:
PASS — LANDING PAGE REQUIREMENTS READY FOR OPERATOR REVIEW

Campaign Architecture:
APPROVED FOR LP REQUIREMENTS

Landing pages:
NOT BUILT

Ad creation:
NOT AUTHORIZED
```

---

## 21. Outputs Created

**28 artefacts** under `projects/mars-search-ppc-production/pilots/corvonero/`:

- `CORVONERO-PHASE-6.2-OPERATOR-DECISIONS-v1.json`
- `CORVONERO-PHASE-6.2-EXISTING-CONTENT-EVIDENCE-MAP-v1.json`
- `CORVONERO-PHASE-6.2-LP-01-PROGRAMMER-REQUIREMENTS-v1.md/json`
- `CORVONERO-PHASE-6.2-LP-02-SUPPORT-REQUIREMENTS-v1.md/json`
- `CORVONERO-PHASE-6.2-LP-03-DEVELOPMENT-REQUIREMENTS-v1.md/json`
- `CORVONERO-PHASE-6.2-LP-04-INTEGRATIONS-REQUIREMENTS-v1.md/json`
- `CORVONERO-PHASE-6.2-LP-05-MARKING-REQUIREMENTS-v1.md/json`
- `CORVONERO-PHASE-6.2-LP-06-REPORTS-REQUIREMENTS-v1.md/json`
- `CORVONERO-PHASE-6.2-GROUP-TO-LP-MAP-v1.json`
- `CORVONERO-PHASE-6.2-CONTENT-EVIDENCE-REQUIREMENTS-v1.json`
- `CORVONERO-PHASE-6.2-LP-PRODUCTION-PRIORITY-v1.json`
- `CORVONERO-PHASE-6.2-INTERIM-HOMEPAGE-POLICY-v1.md/json`
- `CORVONERO-PHASE-6.2-WEBSITE-IMPLEMENTATION-HANDOFF-v1.md/json`
- `CORVONERO-PHASE-6.2-CAMPAIGN-READINESS-MATRIX-v2.md/json`
- `CORVONERO-PHASE-6.2-OPERATOR-DECISION-PACKET-v3.md/json`
- `CORVONERO-PHASE-6.2-RESULT-v1.md/json`
- `CORVONERO-PHASE-7-NEXT-TASK-PARTIAL-v3.md`

**Report:** `projects/mars-search-ppc-production/reports/REPORT-corvonero-phase-6.2-landing-page-requirements-v1.md`

---

## 22. Files Changed

**Created (Phase 6.2 only):** 28 new files listed above.  
**Modified:** None (source Phase 6.1 artefacts untouched).  
**Websites:** Unchanged.

---

## 23. Git Status

All Phase 6.2 outputs are **untracked** (`??`). No commit, no push, no broad staging.

---

## 24. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Product/license resale in PPC scope | SAFE UNKNOWN (RD-04) |
| Exact office address / on-site boundary | Not in audit — operator/client required |
| Messenger channels (WhatsApp/Telegram) | Not confirmed in crawl |
| Homepage Цены section exact rates | Not independently verified |
| Email address text | Flagged visible in audit but address string not extracted |
| 769-phrase backlog future allocation | Out of scope — not processed |
| CMS/platform for new LPs | Tilda inferred from footer — not prescribed as authority |

---

## 25. Exact Next Task

**Phase 7 (partial v3):** Operator resolves **Decision Packet v3 (ODP-01..ODP-11)**, supplies blocking client evidence, then authorizes **LP-01 production** as first page per production priority.

See: `CORVONERO-PHASE-7-NEXT-TASK-PARTIAL-v3.md`

---

## 26. Stop Condition

**STOPPED** after landing-page requirements, implementation handoff, and operator decision packet.

Not performed: page design/build, website edits, ad copy, minus-word deployment, Commander, campaign import/launch.
