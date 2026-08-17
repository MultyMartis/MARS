> **Phase 3H.9.2 (2026-08-17):** ACCESS live drifted to 3 after an incomplete 2026-08-16 `/moderator_remove`/`/moderator_add` cycle left MOD_A revoked. Classified `UNAUTHORIZED_STATE_DRIFT`. Restored MOD_A via existing `/moderator_add` (same profile_no 3). Live ACCESS=4 · CONFIG=4 · Operational resolver=4 · reminder resolver=4. Next natural 10:00: **2026-08-18 Europe/Moscow**. Soak not restarted. Phase 3I.1 blocked. AI OFF. No four-recipient test sends.

> **Phase 3H.9 (2026-08-17):** False «Недостаточно прав» on raw lead was ACCESS/CONFIG Google Sheets `invalid_grant` mislabeled as a permission deny. Reminder 10:00 windows 15–17 Aug failed at CONFIG read with the same credential error before evaluation; 429 retry path was not applicable. Admin deny text + Sheets error classifier patched. Live Sheets OAuth reconnect by operator is still required before ADMIN_A raw retest and the next natural 4-recipient 10:00. Soak not restarted. Phase 3I.1 blocked. AI OFF.

# i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Classification:** External operational product — n8n + Gmail + Google Sheets + Telegram  
**Logical owner:** OPS  
**Supporting systems:** ATLAS · MetaBOT SEO Content Agent patterns · MetaBOT Programmer / Developer · MARS Survivability / GitGuard  

**STATUS:** PRODUCTION STABLE  
**Stable designation:** [Sales Manager v2 — Production Stable Baseline 2026-08-17](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)

Older “Phase 3A / planned / runtime not started” statements below the historical document map are **superseded** for production status. Phase 2/3A packs remain architecture history.

---

## Purpose

Human-supervised sales lead intake and manager assist for **i-SEO** (ORG-0003):

- intake lead emails from Gmail (full-source mode);
- durable RAW / full source logging;
- CLEAN normalized manager-facing lead state;
- Telegram card for managers (copy-ready first reply only — **never** auto-send to clients);
- Admin Telegram surface for lifecycle actions, raw source view, reminders, AI mode, health, stats, and config.

---

## Production workflows (stable)

| Workflow | Role | State |
|----------|------|-------|
| **i-SEO Sales Manager - Operational.dev** | Scheduled Gmail intake → parse → RAW → process → CLEAN → Telegram manager card → Gmail labels | **active** |
| **i-SEO Sales Manager - Admin.dev** | Telegram admin + callbacks (processed / spam / raw source) + reminders | **active** |
| **Sales-Manager-v2** | Inactive reference | **inactive** |

**No workflow copies.** AI default/current: **OFF**. Reminders: **Mon–Fri 10:00 Europe/Moscow**.

Production model: `Gmail → durable RAW/full source → CLEAN → Telegram manager card`.

---

## Authority split

| Layer | Role |
|-------|------|
| **n8n** | Execution truth (external) |
| **Google Sheets** | Durable RAW / CLEAN / CONFIG / diagnostics |
| **Telegram** | Manager cards + admin commands |
| **MARS (`projects/iseo-sales-manager-bot/`)** | Architecture, contracts, baselines, evidence — **does not execute** the bot |

---

## Document map

| Area | Path |
|------|------|
| **Canonical stable baseline** | [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) |
| Acceptance matrix | [baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md](baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md) |
| Known non-blockers | [baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md](baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md) |
| Freeze evidence | [evidence/stable-baseline-20260817/](evidence/stable-baseline-20260817/) |
| Operational index | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) |
| Architecture (historical Phase 2) | [architecture/](architecture/) |
| Plans | [plans/](plans/) |
| Implementation package (Phase 3A) | [implementation/](implementation/) |
| Reports | [reports/](reports/) |

---

## Hard constraints (operator-attested / freeze)

1. Exactly **two** active production workflows (Operational.dev + Admin.dev); v2 remains inactive reference.
2. AI processing is **optional**; current stable state **AI OFF**.
3. AI OFF: no OpenRouter call; zero AI tokens; fully operational.
4. First replies are for **manual manager copy only**.
5. **Never** send replies automatically to real clients.
6. `📄 Исходная заявка` shows literal source (not field reconstruction, not CLEAN substitute).
7. Do not discuss or embed OpenRouter / Gmail / Telegram credentials in docs or exports.
8. Preserve foreign WIP; selective staging only when explicitly chartered.
9. Any post-freeze behavior change = **new explicit phase**.

---

## Not claimed

- Implemented multi-agent runtime inside MARS.
- Full CRM / OPS-as-CRM.
- Auto-reply to clients.
- Natural Monday reminder live acceptance **before** its first natural window (pending observation at freeze if not yet occurred).

---

## Next

Treat [PRODUCTION-STABLE-BASELINE-2026-08-17.md](baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md) as stable. Observe the first natural Monday 10:00 MSK reminder if not yet accepted. Do not begin another Sales Manager behavior phase automatically.

---

*Stable freeze: 2026-08-17.*  
*Historical: Phase 2 / 2R / 3A documentation packs (2026-07-30).*
