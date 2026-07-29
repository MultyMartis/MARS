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
| **Active stage** | **Phase 2R complete** — architecture pack + MARS project registration |
| **Runtime** | External n8n — **not** executed from MARS; implementation **not started** |
| **Live parity vs Sales-Manager-v2** | **SAFE UNKNOWN** (no live n8n inspection this phase) |
| **Registry** | **REGISTERED** — `project_id` **iseo-sales-manager-bot** · status **planned** (2026-07-30) |
| **ATLAS** | Recommendation only — ORG-0003 / PER-0001 / PER-0010 / PER-0011; **no** new IDs |
| **Next** | **PHASE 3A** — sanitized baseline + MetaBOT Programmer implementation package (operator gate before live n8n) |

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
| **Phase 2R** | Project registration + documentation checkpoint | **DONE (this pass)** |
| Phase 3A | Sanitized baseline + MetaBOT Programmer implementation package | **NEXT** (explicit operator gate before live n8n) |
| Phase 3B+ | Sandbox Operational.dev / Admin.dev build · tests · promote | Not started |
| Live | At most one Operational.dev + one Admin.dev; target-only diff | Forbidden until chartered |

---

## Forbidden in documentation sessions (unless separately chartered)

- Live n8n access or patch
- Workflow JSON creation/edit
- Google Sheets mutation
- Telegram send / Gmail process
- Credential discussion (including OpenRouter keys)
- Broad git staging / commit / push / clean / restore

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

*Last updated: 2026-07-30 — Phase 2R registration + documentation checkpoint.*
