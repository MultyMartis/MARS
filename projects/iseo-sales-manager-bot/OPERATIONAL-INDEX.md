# i-SEO Sales Manager Bot — Operational Index

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT  
**Primary logical owner:** OPS  
**Domain root:** [README.md](README.md)

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned (registry unchanged) / **production cutover complete**; first real lead acceptance **PENDING** |
| **Active stage** | **Phase 3C COMPLETE — FIRST REAL LEAD ACCEPTANCE PENDING** — Operational.dev active (AI OFF); Sales-Manager-v2 inactive rollback source; Admin.dev active |
| **Runtime** | External n8n — Operational.dev **active** (sole Gmail intake); Admin.dev **active**; Sales-Manager-v2 **inactive** |
| **Live parity vs Sales-Manager-v2** | **CUT OVER** — Operational.dev replaced v2 for intake; v2 preserved inactive |
| **JSON baselines v1/v2** | **PRESENT** — Phase 3A.1 baselines + Phase 3B sanitized .dev exports; Phase 3C evidence under `evidence/phase3c/` |
| **Registry** | **REGISTERED** — `project_id` **iseo-sales-manager-bot** · status **planned** (unchanged; separate registry gate not opened) |
| **ATLAS** | Recommendation only — ORG-0003 / PER-0001 / PER-0010 / PER-0011; **no** new IDs |
| **Next** | **PHASE 3C.1 — FIRST REAL LEAD OBSERVATION AND PRODUCTION ACCEPTANCE** |

---

## Programme identity

| Field | Value |
|-------|-------|
| **Product name** | i-SEO Sales Manager Bot |
| **Slug** | `iseo-sales-manager-bot` |
| **Business org** | ORG-0003 i-SEO Studio |
| **Primary manager user (v1)** | PER-0010 Дягилева Ольга (Оля) |
| **Owner / ops architect** | PER-0001 Русецкий Андрей *(multi-hat; operator attestation required for product edge)* |
| **Business owner signal** | PER-0011 Шваков Никита |
| **Pattern source** | MetaBOT SEO Content Agent (Admin + Sheets + Telegram + OpenRouter validation patterns) — **reuse grammar, do not clone three workflows** |

---

## Core Run — architecture

| # | Document | Status |
|---|----------|--------|
| 1 | [architecture/TWO-WORKFLOW-ARCHITECTURE-v1.md](architecture/TWO-WORKFLOW-ARCHITECTURE-v1.md) | Phase 2 |
| 2 | [architecture/LEAD-DATA-MODEL-v1.md](architecture/LEAD-DATA-MODEL-v1.md) | Phase 2 |
| 3 | [architecture/LEAD-LIFECYCLE-v1.md](architecture/LEAD-LIFECYCLE-v1.md) | Phase 2 |
| 4 | [architecture/CONFIGURATION-MODEL-v1.md](architecture/CONFIGURATION-MODEL-v1.md) | Phase 2 |
| 5 | [architecture/TELEGRAM-UX-CONTRACT-v1.md](architecture/TELEGRAM-UX-CONTRACT-v1.md) | Phase 2 |
| 6 | [architecture/ADMIN-COMMAND-CONTRACT-v1.md](architecture/ADMIN-COMMAND-CONTRACT-v1.md) | Phase 2 |
| 7 | [architecture/HEALTHCHECK-CONTRACT-v1.md](architecture/HEALTHCHECK-CONTRACT-v1.md) | Phase 2 |
| 8 | [architecture/AI-OFF-ON-CONTRACT-v1.md](architecture/AI-OFF-ON-CONTRACT-v1.md) | Phase 2 |

## Core Run — plans

| # | Document | Status |
|---|----------|--------|
| 9 | [plans/N8N-CHANGE-PLAN-v1.md](plans/N8N-CHANGE-PLAN-v1.md) | Phase 2 |
| 10 | [plans/SANDBOX-TEST-PLAN-v1.md](plans/SANDBOX-TEST-PLAN-v1.md) | Phase 2 |
| 11 | [plans/ROLLBACK-PLAN-v1.md](plans/ROLLBACK-PLAN-v1.md) | Phase 2 |

## Core Run — ATLAS / registry

| # | Document | Status |
|---|----------|--------|
| 12 | [atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md](atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md) | Recommendation only |

## Core Run — Phase 3A / 3A.1 baselines

| # | Document | Status |
|---|----------|--------|
| 13 | [baselines/SOURCE-GAP-MANIFEST-v1.md](baselines/SOURCE-GAP-MANIFEST-v1.md) | **CLOSED** (Phase 3A.1) |
| 14 | [baselines/SOURCE-SANITIZATION-MANIFEST-v1.md](baselines/SOURCE-SANITIZATION-MANIFEST-v1.md) | **Executed** |
| 15 | [baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md](baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md) | Exact sanitized diff |
| 15a | [baselines/Sales-Manager-v1.sanitized.json](baselines/Sales-Manager-v1.sanitized.json) | Phase 3A.1 |
| 15b | [baselines/Sales-Manager-v2.sanitized.json](baselines/Sales-Manager-v2.sanitized.json) | Phase 3A.1 |
| 15c | [baselines/SALES-MANAGER-V2-NODE-INVENTORY-v1.md](baselines/SALES-MANAGER-V2-NODE-INVENTORY-v1.md) | Phase 3A.1 |
| 15d | [baselines/SALES-MANAGER-V2-CONNECTION-MAP-v1.md](baselines/SALES-MANAGER-V2-CONNECTION-MAP-v1.md) | Phase 3A.1 |
| 15e | [baselines/RAW-SHEET-SCHEMA-BASELINE-v1.md](baselines/RAW-SHEET-SCHEMA-BASELINE-v1.md) | Phase 3A.1 |
| 15f | [baselines/CLEAN-SHEET-SCHEMA-BASELINE-v1.md](baselines/CLEAN-SHEET-SCHEMA-BASELINE-v1.md) | Phase 3A.1 |
| 15g | [baselines/SHEET-DATA-QUALITY-FINDINGS-v1.md](baselines/SHEET-DATA-QUALITY-FINDINGS-v1.md) | Phase 3A.1 |

## Core Run — Phase 3A implementation package

| # | Document | Status |
|---|----------|--------|
| 16 | [implementation/METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1.md](implementation/METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1.md) | Phase 3A (+ 3A.1 notes) |
| 17 | [implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md](implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md) | Phase 3A (+ source-graph reconcile) |
| 18 | [implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md](implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md) | Phase 3A |
| 19 | [implementation/ADMIN-SOURCE-SELECTION-v1.md](implementation/ADMIN-SOURCE-SELECTION-v1.md) | Phase 3A |
| 20 | [implementation/SHEETS-MIGRATION-SPEC-v1.md](implementation/SHEETS-MIGRATION-SPEC-v1.md) | Phase 3A (+ historical header evidence) |
| 21 | [implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md](implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md) | Phase 3A (confirmed vs full-table v2 lookup) |
| 22 | [implementation/TELEGRAM-FORMATTER-SPEC-v1.md](implementation/TELEGRAM-FORMATTER-SPEC-v1.md) | Phase 3A |
| 23 | [implementation/TEST-HARNESS-SPEC-v1.md](implementation/TEST-HARNESS-SPEC-v1.md) | Phase 3A |
| 24 | [implementation/SANDBOX-APPLY-GATE-v1.md](implementation/SANDBOX-APPLY-GATE-v1.md) | Phase 3B.2 Telegram sandbox items closed; production gate remains closed |

## Reports

| # | Document | Status |
|---|----------|--------|
| 25 | [reports/REPORT-iseo-sales-manager-bot-phase3a-sanitized-baseline-and-implementation-package-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3a-sanitized-baseline-and-implementation-package-v1.md) | Phase 3A (historical) |
| 26 | [reports/REPORT-iseo-sales-manager-bot-phase3a1-source-ingest-and-sanitized-baselines-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3a1-source-ingest-and-sanitized-baselines-v1.md) | Phase 3A.1 |
| 27 | [reports/REPORT-iseo-sales-manager-bot-phase3b-live-audit-and-dev-contour-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3b-live-audit-and-dev-contour-v1.md) | Phase 3B |
| Phase 3B.4 | Real Admin Trigger + runtime state | **ATTENTION** — runtime/stats/error PASS; real Trigger NOT CONFIRMED |
| 28 | [evidence/phase3b/](evidence/phase3b/) | Phase 3B evidence |
| 29 | [reports/REPORT-iseo-sales-manager-bot-phase3b1-telegram-sandbox-and-dev-acceptance-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3b1-telegram-sandbox-and-dev-acceptance-v1.md) | Phase 3B.1 |
| 30 | [evidence/phase3b1/](evidence/phase3b1/) | Phase 3B.1 evidence |
| 31 | [reports/REPORT-iseo-sales-manager-bot-phase3b2-runtime-fixes-and-telegram-sandbox-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3b2-runtime-fixes-and-telegram-sandbox-v1.md) | Phase 3B.2 |
| 32 | [evidence/phase3b2/](evidence/phase3b2/) | Phase 3B.2 acceptance evidence |
| 33 | [reports/REPORT-iseo-sales-manager-bot-phase3b3-telegram-ux-final-acceptance-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3b3-telegram-ux-final-acceptance-v1.md) | Phase 3B.3 |
| 34 | [evidence/phase3b3/](evidence/phase3b3/) | Phase 3B.3 UX final acceptance evidence |
| 35 | [reports/REPORT-iseo-sales-manager-bot-phase3c-operational-production-cutover-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3c-operational-production-cutover-v1.md) | Phase 3C |
| 36 | [evidence/phase3c/](evidence/phase3c/) | Phase 3C cutover evidence |

---

## Known baseline (sanitized export evidence; not live-verified this phase)

**Sales-Manager-v2 exact stages:** Schedule Trigger → Get many messages → Lead-Mail-Parser → parallel `Запись лида (RAW)` + Prepare-OpenRouter-Request → HTTP Request (AI #1) → Normalize-AI-Result → Prepare-AI-Normalizer-Request → AI-Normalizer (AI #2) → Normalize-Clean-Lead → Find Duplicate Lead → Mark-Duplicate-Status → IF - Bad Quality → Осмысленные лиды (CLEAN) → message v2 → Add label PROCESSED → Remove label LEADS_ISEO · ERROR branch removes incoming via Remove label LEADS_ISEO2.

**Known defects (export-evidenced):** dual AI calls; empty/discarded `ai_reply` quality fields; RAW AI columns pre-AI; CLEAN missing reply/AI/priority fields; optimistic quality (CLEAN 19/19 `ok`); full-table dedupe; no Telegram fail gate; Gmail `returnAll=true`; no admin/config surface in these exports.

---

## Phase gates

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Discovery / problem framing | Assumed prior / operator pack |
| **Phase 2** | Architecture + data model + contracts + plans | **DONE** |
| **Phase 2R** | Project registration + documentation checkpoint | **DONE** |
| **Phase 3A** | Sanitized baseline gate + MetaBOT Programmer implementation package | **DONE** (historical: sources absent at that time) |
| **Phase 3A.1** | Source ingest + sanitized baselines + reconciliation | **DONE** |
| Phase 3B | Live read-only audit + Operational.dev / Admin.dev creation | **DONE** — inactive contour + v2 tabs; Telegram sandbox PENDING |
| Phase 3B.1 | Telegram destination / preliminary acceptance | **DONE** |
| Phase 3B.2 | Runtime fixes + Telegram sandbox acceptance | **DONE** |
| Phase 3B.3 | Telegram UX polish + final dev acceptance | **DONE** |
| Phase 3B.4 / 3B.4.1 / 3B.5 | Real Admin Trigger + polish + cutover readiness | **DONE** |
| **Phase 3C** | Operational production cutover (AI OFF) | **DONE** — first real lead **PENDING** |
| Phase 3C.1 | First real lead observation / production acceptance | **NEXT** |
| Live rename / Olya handoff | After first-real-lead acceptance | Forbidden until chartered |

---

## Forbidden in documentation / Phase 3A sessions (unless separately chartered)

- Live n8n access or patch
- Workflow JSON creation/edit / workflow copies
- Google Sheets mutation
- Telegram send / Gmail process
- Credential discussion (including OpenRouter keys)
- Broad git staging / clean / restore on dirty main worktree

---

## Related systems

| System | Relationship |
|--------|----------------|
| **OPS** | Logical owner of sales/ops assist contour |
| **MetaBOT SEO Content Agent** | Pattern source (Admin commands, Sheets state, AI JSON validation, sandbox patch protocol) |
| **ATLAS** | Business reality IDs only — recommendation in this pack |
| **mars-survivability / GitGuard** | Selective staging, foreign WIP, rollback evidence discipline |
| **iseo-report-hub** | Sibling i-SEO product locus — **distinct** `project_id` |

---

*Last updated: 2026-07-31 — Phase 3C operational production cutover (AI OFF; first real lead PENDING).*
