# i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Classification:** External operational product (documentation-first) — n8n + Gmail + Google Sheets + Telegram  
**Logical owner:** OPS  
**Supporting systems:** ATLAS · MetaBOT SEO Content Agent patterns · MetaBOT Programmer / Developer · MARS Survivability / GitGuard  
**Status:** Phase 3E.2.1 — First Reply Engine **`sm-reply-v2.1`** + Human Reply Style **`sm-human-v1.0`** + manager card **`sm-msg-v2.4`**; Parser **`sm-parser-v3.3`** (3E.1 COMPLETE); harness 64/64 PASS; AI OFF; drafts are manager-copy only; operator copy acceptance **ATTENTION**

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
| **i-SEO Sales Manager - Operational.dev** | Scheduled Gmail intake → parse → RAW → process → CLEAN → **multi-recipient** Telegram cards (active Admin+moderators) → Gmail labels |
| **i-SEO Sales Manager - Admin.dev** | Telegram entry → ACCESS_CONTROL auth → commands / callbacks (early `answerCallbackQuery`) → **multi-copy lifecycle sync via LEAD_DELIVERIES** · `/delivery_status` · `/delivery_users` |

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
| Product manual layer | [product/](product/) |
| Parser 3.3 architecture | [architecture/PARSER-3.3-CONTRACT-v1.md](architecture/PARSER-3.3-CONTRACT-v1.md) · [LEAD-SEMANTIC-MODEL-v1.md](architecture/LEAD-SEMANTIC-MODEL-v1.md) · [FIRST-REPLY-RULES-v1.md](architecture/FIRST-REPLY-RULES-v1.md) |
| First Reply Engine v2.1 + Human Reply Style v1 | [architecture/FIRST-REPLY-ENGINE-v2.md](architecture/FIRST-REPLY-ENGINE-v2.md) · [architecture/HUMAN-REPLY-STYLE-v1.md](architecture/HUMAN-REPLY-STYLE-v1.md) · [architecture/MEANINGFUL-COMMENT-BRANCHING-v1.md](architecture/MEANINGFUL-COMMENT-BRANCHING-v1.md) · [architecture/FIRST-REPLY-QUALITY-LINTER-v1.md](architecture/FIRST-REPLY-QUALITY-LINTER-v1.md) · [architecture/KNOWN-INFORMATION-GUARD-v1.md](architecture/KNOWN-INFORMATION-GUARD-v1.md) · [architecture/MANAGER-CARD-v2.4-CONTRACT-v1.md](architecture/MANAGER-CARD-v2.4-CONTRACT-v1.md) |
| Delivery fail-closed (3E.2.1) | [architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md) |
| Parser 3.3 research (implemented) | [research/parser-3.3/](research/parser-3.3/) |
| Phase 3E.2 evidence | [evidence/phase3e2/](evidence/phase3e2/) |
| Phase 3E.2.1 evidence | [evidence/phase3e2-1/](evidence/phase3e2-1/) |
| Phase 3E.1 evidence | [evidence/phase3e1/](evidence/phase3e1/) |
| Phase 3D.8 evidence | [evidence/phase3d8/](evidence/phase3d8/) |
| Phase 3D.8.1 evidence | [evidence/phase3d8-1/](evidence/phase3d8-1/) |
| Phase 3D.8.2 evidence | [evidence/phase3d8-2/](evidence/phase3d8-2/) |
| Phase 3D.8.3 evidence | [evidence/phase3d8-3/](evidence/phase3d8-3/) |
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
**Resolved in Phase 3D.3:** manager UX upgraded to `sm-msg-v2` (emoji lead/lifecycle indicators, copy-friendly `<code>` contact fields, single `<pre>` client-reply block); inline lifecycle buttons with idempotent + conflict-safe callback handling; `/leads 3|5|10` (admin allowlist only); CLEAN 65 headers with lifecycle columns.  
**Resolved in Phase 3D.4:** Olya enrolled in `ACCESS_CONTROL moderator (legacy CONFIG fallback retained) (hash **E6714550214106BA**, not admin); role-aware manager `/start`/`/help`; parser **`sm-parser-v3.2`** (messenger/site split, contact inference, comment «в тг», source page normalization); formatter **`sm-msg-v2.1`** (reduced emoji density); `knowledge/WEBSITE-FORM-FORMATS-v1.md` with free-audit record; synthetic callback acceptance PASS — **live Olya `/start`/`/help` pending**.
**Resolved in Phase 3D.6 / 3D.6.1:** `/my_status` for public/pending/moderator/Admin/revoked/blocked; grant/revoke Telegram notification branch with ACCESS_EVENTS delivery events and non-rollback failure boundary. Live hotfix `3d6b-my-status-code-mode` fixed Code-node mode (`runOnceForAllItems`). Real non-Admin `/my_status` accepted by operator. Direct grant/revoke notification delivery remains SAFE UNKNOWN without independent visual proof. Harness **31/31 PASS**.
**Phase 3D.8.x:** product/recovery baseline; action buttons + actor attribution + short labels COMPLETE.  
**Phase 3E.2 / 3E.2.1:** First Reply Engine **v2.1** + **Human Reply Style v1** (`sm-human-v1.0`) — natural Оля drafts, silent known-info guard, meaningful comment branching, quality linter; delivery fail-closed reconciliation; local harness **64/64 PASS**; operator copy acceptance **ATTENTION**. Reminders, AI ON pilot and reusable fleet deployment remain **not implemented**.

---

## Guides

| Guide | Path |
|-------|------|
| Оля — работа с лидами | [guides/OLYA-LEAD-WORK-GUIDE-v1.md](guides/OLYA-LEAD-WORK-GUIDE-v1.md) |
| Operator runbook (Андрей) | [guides/OPERATOR-RUNBOOK-v1.md](guides/OPERATOR-RUNBOOK-v1.md) |

## Next gate

**Current closeout:** **COMPLETE — STATUS READY, LIVE NOTIFICATION CONFIRMATION PENDING.**
**Next:** operator performs Telegram grant/revoke delivery confirmation → next website form per `MULTI-FORM-TEST-PLAN-v1` (one form per iteration).
**Later (separate approval):** PHASE 3E — controlled AI ON pilot; optional `.dev` rename; registry promotion.

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
*Phase 3D.2.1: Admin duplicate reply + runtime-state closeout (2026-08-01).*  
*Phase 3D.3: manager UX sm-msg-v2, inline lead actions, `/leads`, lifecycle Sheets model — AI OFF (2026-08-01).*  
*Phase 3D.4: Olya manager enrollment, sm-parser-v3.2 / sm-msg-v2.1 form semantics, website form registry — AI OFF (2026-08-03).*
*Phase 3D.6: personal `/my_status` and role-notification contracts — AI OFF (2026-08-04).*  
*Phase 3D.6.1: live non-Admin `/my_status` acceptance + 3d6b Code-mode hotfix canonicalization — AI OFF (2026-08-04).*


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.
