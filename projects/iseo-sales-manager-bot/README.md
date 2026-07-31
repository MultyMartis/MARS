# i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Classification:** External operational product (documentation-first) — n8n + Gmail + Google Sheets + Telegram  
**Logical owner:** OPS  
**Supporting systems:** ATLAS · MetaBOT SEO Content Agent patterns · MetaBOT Programmer / Developer · MARS Survivability / GitGuard  
**Status:** Phase 3D.2.1 — Admin reply / runtime-state closeout; duplicate `/start` classified as harness overlap; n8n attribution off; `/status` lead stamp backfilled; Update Runtime State fixed; Admin.dev **active**; Operational.dev **active** (AI OFF); Sales-Manager-v2 **inactive**; Olya destination visibility **pending**; registry status promotion **pending**

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
| Baselines / sanitized sources | [baselines/](baselines/) |
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
9. Phase 3A / 3A.1: no live n8n, no workflow copies, no Sheets/Gmail/Telegram mutation.

---

## Not claimed

- Implemented runtime inside MARS (execution remains external n8n).
- Full CRM / OPS-as-CRM.
- Auto-reply to clients.
- AI ON in production (remains OFF until explicit charter).
- Explained historical Trash actor for unlabeled incident mail (SAFE UNKNOWN; not a Gmail filter).

**Resolved in Phase 3A.1:** sanitized Sales-Manager-v1/v2 JSON baselines and XLSX-derived schema baselines are present under `baselines/`.  
**Resolved in Phase 3C:** Operational.dev is the active production intake (AI OFF); Sales-Manager-v2 preserved inactive as rollback source; Admin.dev remains active.  
**Resolved in Phase 3C.2:** Gmail filters audited (no Trash rules); OPS field-loss/chat_id/messageId repaired; first real website-form lead accepted end-to-end.

---

## Guides

| Guide | Path |
|-------|------|
| Оля — работа с лидами | [guides/OLYA-LEAD-WORK-GUIDE-v1.md](guides/OLYA-LEAD-WORK-GUIDE-v1.md) |
| Operator runbook (Андрей) | [guides/OPERATOR-RUNBOOK-v1.md](guides/OPERATOR-RUNBOOK-v1.md) |

## Next gate

**Operator:** submit one clean valid-contact website test lead (readiness notice already sent).  
**Then:** confirm exactly-once card + optional `.dev` rename.  
**Later (separate approval):** PHASE 3E — controlled AI ON pilot.

Do not enable AI or reactivate Sales-Manager-v2 without explicit charter. Do not add Оля to Admin allowlist without approval.

Operator source drop path (raw retained): `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\raw\`

---

*Phase 2 charter: ISEO-SALES-MANAGER-BOT — PHASE 2 ARCHITECTURE AND DATA MODEL (2026-07-30).*  
*Phase 2R: project registration + documentation checkpoint (2026-07-30).*  
*Phase 3A: sanitized baseline gate + MetaBOT Programmer implementation package (2026-07-30).*  
*Phase 3A.1: source ingest + sanitized baselines (2026-07-30).*  
*Phase 3C: operational production cutover AI OFF (2026-07-31).*  
*Phase 3C.2: Gmail routing audit + first real lead acceptance (2026-07-31).*  
*Phase 3D: production stabilization + Olya handoff pack (2026-07-31).*
