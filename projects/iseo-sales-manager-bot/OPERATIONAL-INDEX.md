# i-SEO Sales Manager Bot — Operational Index

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT  
**Primary logical owner:** OPS  
**Domain root:** [README.md](README.md)

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | planned / documentation |
| **Active stage** | **Phase 3A complete** — implementation package + source-gap baseline (**READY WITH SOURCE DROP REQUIRED**) |
| **Runtime** | External n8n — **not** executed from MARS; workflow JSON / live copies **not** created |
| **Live parity vs Sales-Manager-v2** | **SAFE UNKNOWN** (no live n8n this phase) |
| **JSON baselines v1/v2** | **BLOCKED** — exports absent from approved drop paths |
| **Registry** | **REGISTERED** — `project_id` **iseo-sales-manager-bot** · status **planned** (unchanged; no implementation start) |
| **ATLAS** | Recommendation only — ORG-0003 / PER-0001 / PER-0010 / PER-0011; **no** new IDs |
| **Next** | **PHASE 3B** — live read-only audit + .dev workflow creation — **only after** sandbox apply gate confirmations |

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

## Core Run — Phase 3A baselines

| # | Document | Status |
|---|----------|--------|
| 13 | [baselines/SOURCE-GAP-MANIFEST-v1.md](baselines/SOURCE-GAP-MANIFEST-v1.md) | Source drop required |
| 14 | [baselines/SOURCE-SANITIZATION-MANIFEST-v1.md](baselines/SOURCE-SANITIZATION-MANIFEST-v1.md) | Contract defined; exec blocked |
| 15 | [baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md](baselines/SALES-MANAGER-V1-V2-COMPARISON-v1.md) | Logical comparison only |

## Core Run — Phase 3A implementation package

| # | Document | Status |
|---|----------|--------|
| 16 | [implementation/METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1.md](implementation/METABOT-PROGRAMMER-IMPLEMENTATION-BRIEF-v1.md) | Phase 3A |
| 17 | [implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md](implementation/OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.md) | Phase 3A |
| 18 | [implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md](implementation/ADMIN-WORKFLOW-PATCH-SPEC-v1.md) | Phase 3A |
| 19 | [implementation/ADMIN-SOURCE-SELECTION-v1.md](implementation/ADMIN-SOURCE-SELECTION-v1.md) | Phase 3A |
| 20 | [implementation/SHEETS-MIGRATION-SPEC-v1.md](implementation/SHEETS-MIGRATION-SPEC-v1.md) | Phase 3A |
| 21 | [implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md](implementation/DEDUP-IMPLEMENTATION-SPEC-v1.md) | Phase 3A |
| 22 | [implementation/TELEGRAM-FORMATTER-SPEC-v1.md](implementation/TELEGRAM-FORMATTER-SPEC-v1.md) | Phase 3A |
| 23 | [implementation/TEST-HARNESS-SPEC-v1.md](implementation/TEST-HARNESS-SPEC-v1.md) | Phase 3A |
| 24 | [implementation/SANDBOX-APPLY-GATE-v1.md](implementation/SANDBOX-APPLY-GATE-v1.md) | Gate closed pending operator |

## Reports

| # | Document | Status |
|---|----------|--------|
| 25 | [reports/REPORT-iseo-sales-manager-bot-phase3a-sanitized-baseline-and-implementation-package-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3a-sanitized-baseline-and-implementation-package-v1.md) | Phase 3A |

---

## Known baseline (operator-provided; not live-verified this phase)

**Sales-Manager-v2 logical stages:** Schedule Trigger → Gmail get many (incoming leads label) → Lead-Mail-Parser → RAW append → Prepare OpenRouter → AI #1 → Normalize → Prepare normalizer → AI #2 → Normalize Clean Lead → Find Duplicate → Mark Duplicate → IF Bad Quality → CLEAN append → Telegram → Gmail PROCESSED + remove incoming · error label branch.

**Known defects (design drivers):** dual AI calls; empty `ai_reply`; RAW AI columns pre-AI; CLEAN missing reply/AI/priority fields; optimistic quality; weak dedupe; no manager lifecycle; Telegram enums/ISO noise; no admin/config surface.

---

## Phase gates

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | Discovery / problem framing | Assumed prior / operator pack |
| **Phase 2** | Architecture + data model + contracts + plans | **DONE** |
| **Phase 2R** | Project registration + documentation checkpoint | **DONE** |
| **Phase 3A** | Sanitized baseline + MetaBOT Programmer implementation package | **DONE** (source drop still required for JSON baselines) |
| Phase 3B | Live read-only audit + Operational.dev / Admin.dev creation | **NEXT** — explicit operator gate |
| Live | At most one Operational + one Admin; target-only diff | Forbidden until chartered |

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

*Last updated: 2026-07-30 — Phase 3A sanitized baseline gate + implementation package.*
