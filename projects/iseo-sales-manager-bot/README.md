# i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Classification:** External operational product (documentation-first) — n8n + Gmail + Google Sheets + Telegram  
**Logical owner:** OPS  
**Supporting systems:** ATLAS · MetaBOT SEO Content Agent patterns · MetaBOT Programmer / Developer · MARS Survivability / GitGuard  
**Status:** Phase 3A implementation package **documented**; JSON baseline generation **blocked** pending source drop; registry **planned**; runtime / n8n implementation **not started**

---

## Purpose

Human-supervised sales lead intake and manager assist for **i-SEO** (ORG-0003):

- intake lead emails from Gmail;
- immutable RAW evidence logging;
- deterministic (and optional AI) enrichment;
- CLEAN manager-facing lead state;
- Telegram card for managers (copy-ready first reply only — **never** auto-send to clients);
- Admin Telegram surface for AI mode, health, stats, and config.

---

## Two-workflow target (v1)

| Workflow | Role |
|----------|------|
| **i-SEO Sales Manager - Operational.dev** | Scheduled Gmail intake → parse → RAW → process → CLEAN → Telegram manager card → Gmail labels |
| **i-SEO Sales Manager - Admin.dev** | Telegram admin entry → auth → commands → CONFIG / health / stats / synthetic test |

**No third workflow for v1.** Do not clone MetaBOT Intake/Worker/Admin as three copies. Maximum later live copies: one Operational.dev + one Admin.dev if required.

---

## Authority split

| Layer | Role |
|-------|------|
| **n8n** | Execution truth (external) |
| **Google Sheets** | Durable RAW / CLEAN / CONFIG / diagnostics |
| **Telegram** | Manager cards + admin commands |
| **MARS (`projects/iseo-sales-manager-bot/`)** | Architecture, contracts, change plans, implementation specs, evidence — **does not execute** the bot |

---

## Document map

| Area | Path |
|------|------|
| Operational index | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) |
| Architecture | [architecture/](architecture/) |
| Plans | [plans/](plans/) |
| Baselines / source gap | [baselines/](baselines/) |
| MetaBOT Programmer implementation package | [implementation/](implementation/) |
| Reports | [reports/](reports/) |
| ATLAS recommendation | [atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md](atlas/ATLAS-REGISTRATION-RECOMMENDATION-v1.md) |

---

## Hard constraints (operator-attested)

1. Exactly **two** target workflows (Operational + Admin).
2. AI processing is **optional**; default **AI OFF**.
3. AI OFF: no OpenRouter call; zero AI tokens; fully operational.
4. AI ON: preferably **one** structured AI call per lead; deterministic validation; automatic fallback to AI OFF.
5. First replies are for **manual manager copy only**.
6. **Never** send replies automatically to real clients.
7. Do not discuss or embed OpenRouter credentials in docs or exports.
8. Preserve foreign WIP; selective staging only when explicitly chartered.
9. Phase 3A: no live n8n, no workflow copies, no Sheets/Gmail/Telegram mutation.

---

## Not claimed

- Live n8n parity with Sales-Manager-v2 (**SAFE UNKNOWN** without fresh live attestation).
- Sanitized Sales-Manager-v1/v2 JSON baselines (**blocked** — source drop required).
- Implemented runtime inside MARS.
- Full CRM / OPS-as-CRM.
- Auto-reply to clients.
- Created `.dev` workflow copies, Sheets v2 tabs, or live Admin/Operational graphs.

---

## Next gate

**PHASE 3B — LIVE READ-ONLY AUDIT AND DEV WORKFLOW CREATION** — only after [implementation/SANDBOX-APPLY-GATE-v1.md](implementation/SANDBOX-APPLY-GATE-v1.md) operator confirmations.

Operator source drop path: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\raw\`

---

*Phase 2 charter: ISEO-SALES-MANAGER-BOT — PHASE 2 ARCHITECTURE AND DATA MODEL (2026-07-30).*  
*Phase 2R: project registration + documentation checkpoint (2026-07-30).*  
*Phase 3A: sanitized baseline gate + MetaBOT Programmer implementation package (2026-07-30).*
