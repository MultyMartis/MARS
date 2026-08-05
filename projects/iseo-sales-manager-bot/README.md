<!-- Phase 3G.2 documentation + number-based reply profiles 2026-08-06 -->

## Phase 3G.2 — Reply profile numbers + Telegram text contract

**Status:** **DOCUMENTATION PACKAGE + NUMBER CONTRACT**; live Admin patch / acceptance evidence under `evidence/phase3g2/` (stubs → fill).

- Immutable `reply_profile_number` 1–4: ADMIN_A→Андрей enabled; MOD_B_REVOKED→Оля disabled; MOD_A→Михаил enabled; MOD_C_REVOKED→Никита disabled
- Admin commands by **number only**: `/reply_profiles`, `/reply_profile N`, `/reply_name_set N name`, `/reply_name_enable N`, `/reply_name_disable N`; moderators: `/my_reply_profile`
- Client name **only** from `reply_sender_name`; access roles unchanged by name commands
- Text authority: [TELEGRAM-TEXT-CONTRACT-v2.md](architecture/TELEGRAM-TEXT-CONTRACT-v2.md) · commands: [TELEGRAM-COMMAND-REFERENCE-v1.md](guides/TELEGRAM-COMMAND-REFERENCE-v1.md)
- Help: explicit Admin/moderator templates ([ROLE-AWARE-HELP-BUILDER-v2.md](implementation/ROLE-AWARE-HELP-BUILDER-v2.md)) — no substring patch
- Contour: Ops **45** active · Admin **~84+** after patch · Sales-Manager-v2 inactive · Parser 3.3 · `LEADS` / `LEAD_EVENTS` · stats epoch **05.08.2026** Europe/Moscow · AI OFF · reminders OFF · no auto-send
- Evidence: [evidence/phase3g2/](evidence/phase3g2/)

## Phase 3G.1.1 — Live reply profile seed + T1/T3 template acceptance

**Status:** **LIVE PROFILES SEEDED**; **OPERATOR TEMPLATE ACCEPTANCE PENDING**; Admin **84** nodes; profiles seeded on ACCESS_CONTROL Q–V.

- Defect closed: sidecar ok but columns missing → headers + 24 cells seeded; Admin Upsert schema aligned
- Live readback: ADMIN_A→Андрей enabled; MOD_A→Михаил enabled; revoked prepared disabled
- T1/T3 acceptance inject: 4 Telegram successes; 0 duplicates; `Мопс`=0 in client copy
- Fail-closed harness band: **9/9 PASS**; Phase 3G.1 baseline **100/100 PASS** retained
- AI OFF; reminders OFF; Ops 45 active; Sales-Manager-v2 inactive
- Evidence: [evidence/phase3g1-1/](evidence/phase3g1-1/) · Report: [REPORT-iseo-sales-manager-bot-phase3g1-1-live-profile-and-template-acceptance-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3g1-1-live-profile-and-template-acceptance-v1.md)

## Phase 3G.1 — INTLSEO first-contact + personalized manager assist

**Status:** offline libs + harness **100/100 PASS**; live workflow patch **applied**; profile seed repair in **3G.1.1**.

- Standard `iseo-first-contact-v1.0` · templates `iseo-template-set-v1.0` · policy `iseo-sales-policy-v1.0` · assist `iseo-manager-assist-v1.0` · personalization `iseo-recipient-name-v1.0`
- Five templates; precedence **T5 > T4 > T3 > T1 > T2**; legacy `sm-reply-v2.1` rollback stamp only
- One business lead → multiple personalized drafts (ADMIN_A→Андрей, MOD_A→Михаил; Мопс never in client copy)
- AI OFF default; constrained AI assist contract not globally enabled; **no auto-send** to customers
- Prefer `RECIPIENT_REPLIES` or `LEAD_DELIVERIES` extension; reporting = shared template id only
- Contour baseline: Ops 45 active · Admin **84** active · Sales-Manager-v2 inactive · reminders OFF · stats 1/1/0/0 epoch 05.08.2026
- Evidence: [evidence/phase3g1/](evidence/phase3g1/) · [evidence/phase3g1-1/](evidence/phase3g1-1/) · Architecture: [INTLSEO-FIRST-CONTACT-STANDARD-v1.md](architecture/INTLSEO-FIRST-CONTACT-STANDARD-v1.md)

# i-SEO Sales Manager Bot

**project_id:** `iseo-sales-manager-bot`  
**Classification:** External operational product (documentation-first) — n8n + Gmail + Google Sheets + Telegram  
**Logical owner:** OPS  
**Supporting systems:** ATLAS · MetaBOT SEO Content Agent patterns · MetaBOT Programmer / Developer · MARS Survivability / GitGuard  
**Status:** Phase 3F.2.2 — COMPLETE — FINAL ADMIN POLISH READY; OPERATOR CONFIRMATION PENDING; AI OFF; reminders OFF

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
| Sheets budget / concurrency (3E.2.3) | [architecture/SHEETS-CALL-BUDGET-v1.md](architecture/SHEETS-CALL-BUDGET-v1.md) · [architecture/OPERATIONAL-SINGLE-FLIGHT-v1.md](architecture/OPERATIONAL-SINGLE-FLIGHT-v1.md) · [architecture/SHEETS-BACKOFF-POLICY-v1.md](architecture/SHEETS-BACKOFF-POLICY-v1.md) |
| Pending leads view + reminders (3F.1) | [architecture/PENDING-LEADS-VIEW-v1.md](architecture/PENDING-LEADS-VIEW-v1.md) · [architecture/PENDING-REMINDER-v1.md](architecture/PENDING-REMINDER-v1.md) · [architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md](architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md) |
| Phase 3G.1 INTLSEO first-contact | [architecture/INTLSEO-FIRST-CONTACT-STANDARD-v1.md](architecture/INTLSEO-FIRST-CONTACT-STANDARD-v1.md) · [architecture/RECIPIENT-PERSONALIZED-REPLIES-v1.md](architecture/RECIPIENT-PERSONALIZED-REPLIES-v1.md) · [architecture/AI-MANAGER-ASSIST-v1.md](architecture/AI-MANAGER-ASSIST-v1.md) · [architecture/REPLY-PROFILE-CONTRACT-v1.md](architecture/REPLY-PROFILE-CONTRACT-v1.md) |
| Phase 3G.2 text + numbers | [architecture/TELEGRAM-TEXT-CONTRACT-v2.md](architecture/TELEGRAM-TEXT-CONTRACT-v2.md) · [architecture/REPLY-PROFILE-NUMBERING-v1.md](architecture/REPLY-PROFILE-NUMBERING-v1.md) · [guides/TELEGRAM-COMMAND-REFERENCE-v1.md](guides/TELEGRAM-COMMAND-REFERENCE-v1.md) · [implementation/REPLY-PROFILE-ADMIN-COMMANDS-v2.md](implementation/REPLY-PROFILE-ADMIN-COMMANDS-v2.md) · [implementation/ROLE-AWARE-HELP-BUILDER-v2.md](implementation/ROLE-AWARE-HELP-BUILDER-v2.md) · [implementation/USER-VISIBLE-TEXT-REGISTRY-v1.md](implementation/USER-VISIBLE-TEXT-REGISTRY-v1.md) |
| Phase 3G.1 evidence | [evidence/phase3g1/](evidence/phase3g1/) — harness 100/100 PASS |
| Phase 3G.1.1 evidence | [evidence/phase3g1-1/](evidence/phase3g1-1/) — live profiles seeded; operator template acceptance pending |
| Phase 3G.2 evidence | [evidence/phase3g2/](evidence/phase3g2/) — stubs for acceptance fill |
| Parser 3.3 research (implemented) | [research/parser-3.3/](research/parser-3.3/) |
| Phase 3F.1 evidence | [evidence/phase3f1/](evidence/phase3f1/) |
| Phase 3E.2 evidence | [evidence/phase3e2/](evidence/phase3e2/) |
| Phase 3E.2.3 evidence | [evidence/phase3e2-3/](evidence/phase3e2-3/) |
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
- Pending-lead reminders **enabled** in production — the engine is implemented and live-command-accepted but `pending_reminders_enabled=false` until the operator explicitly activates it.
- A full live dual-recipient reminder Telegram send under normal (non-quota) conditions — the controlled live window reached ACCESS_CONTROL and failed closed on a Sheets quota condition (see `evidence/phase3f1/CONTROLLED-REMINDER-LIVE-ACCEPTANCE-v1.md`).

**Resolved in Phase 3A.1:** sanitized Sales-Manager-v1/v2 JSON baselines and XLSX-derived schema baselines are present under `baselines/`.  
**Resolved in Phase 3C:** Operational.dev is the active production intake (AI OFF); Sales-Manager-v2 preserved inactive as rollback source; Admin.dev remains active.  
**Resolved in Phase 3C.2:** Gmail filters audited (no Trash rules); OPS field-loss/chat_id/messageId repaired; first real website-form lead accepted end-to-end.  
**Resolved in Phase 3D.3:** manager UX upgraded to `sm-msg-v2` (emoji lead/lifecycle indicators, copy-friendly `<code>` contact fields, single `<pre>` client-reply block); inline lifecycle buttons with idempotent + conflict-safe callback handling; `/leads 3|5|10` (admin allowlist only); CLEAN 65 headers with lifecycle columns.  
**Resolved in Phase 3D.4:** Olya enrolled in `ACCESS_CONTROL moderator (legacy CONFIG fallback retained) (hash **E6714550214106BA**, not admin); role-aware manager `/start`/`/help`; parser **`sm-parser-v3.2`** (messenger/site split, contact inference, comment «в тг», source page normalization); formatter **`sm-msg-v2.1`** (reduced emoji density); `knowledge/WEBSITE-FORM-FORMATS-v1.md` with free-audit record; synthetic callback acceptance PASS — **live Olya `/start`/`/help` pending**.
**Resolved in Phase 3D.6 / 3D.6.1:** `/my_status` for public/pending/moderator/Admin/revoked/blocked; grant/revoke Telegram notification branch with ACCESS_EVENTS delivery events and non-rollback failure boundary. Live hotfix `3d6b-my-status-code-mode` fixed Code-node mode (`runOnceForAllItems`). Real non-Admin `/my_status` accepted by operator. Direct grant/revoke notification delivery remains SAFE UNKNOWN without independent visual proof. Harness **31/31 PASS**.
**Phase 3D.8.x:** product/recovery baseline; action buttons + actor attribution + short labels COMPLETE.  
**Phase 3E.2.3:** First Reply Engine **v2.1** + **Human Reply Style v1** remain unchanged and operator-accepted; current work only reduces Sheets request amplification and adds bounded concurrency/retry controls. Operational.dev is active after the quiet-window proof; exactly-once delivery and five-poll zero-resend are proven.
**Phase 3E.2 closeout:** operator visual confirmation received — final verdict `PHASE 3E.2 COMPLETE — HUMAN FIRST REPLY ENGINE READY` (see `evidence/phase3f1/PHASE3E2-FINAL-CLOSEOUT-v1.md`).
**Phase 3F.1:** Admin.dev gained pending-lead commands (`/pending_count`, `/pending_leads`, `/pending_leads_test`) and a daily reminder engine (`sm-pending-reminder-v1.0`, internal 15-minute schedule trigger, additive `REMINDER_DELIVERIES` ledger). Node count 59→79. Offline harness 73/73 PASS; live command acceptance PASS; a controlled reminder live exercise reached ACCESS_CONTROL and correctly failed closed under Sheets quota. Reminders remain `enabled=false` in production — AI ON pilot and reusable fleet deployment remain **not implemented**.

---

## Guides

| Guide | Path |
|-------|------|
| Оля — работа с лидами | [guides/OLYA-LEAD-WORK-GUIDE-v1.md](guides/OLYA-LEAD-WORK-GUIDE-v1.md) |
| Operator runbook (Андрей) | [guides/OPERATOR-RUNBOOK-v1.md](guides/OPERATOR-RUNBOOK-v1.md) |
| Telegram command reference | [guides/TELEGRAM-COMMAND-REFERENCE-v1.md](guides/TELEGRAM-COMMAND-REFERENCE-v1.md) |

## Next gate

**Current gate:** `COMPLETE — EXACTLY-ONCE PROOF DELIVERED; OPERATOR VISUAL CONFIRMATION PENDING`.
**Proven:** harness 83/83; zero-write empty polls; safe real-lead recount; two claims/two sends/two stamps; five polls with zero resend; two CONFIG guards reconciled without resend.
**Pre-visual maximum verdict:** `COMPLETE — EXACTLY-ONCE PROOF DELIVERED; OPERATOR VISUAL CONFIRMATION PENDING`. Do not claim PHASE 3E.2 COMPLETE yet.

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

## Phase 3E.2.3 — Sheets call-budget optimization

Empty polls have live proof of zero Sheets writes. Final schedule is `minutesInterval=2`; `secondsInterval=120` was rejected by n8n as an invalid interval. Intake Gate uses a 4-minute single-flight TTL. ACCESS_CONTROL and bounded LEAD_DELIVERIES snapshots are read once with bounded retries; exactly-once proof and five-poll zero-resend passed. See `evidence/phase3e2-3/`.

## Phase 3F.1 — Pending leads commands + daily reminder engine

Admin.dev (same ID, 59→79 nodes) gained a read-only pending-lead view (`/pending_count`, `/pending_leads`, `/pending_leads_test`) and a daily reminder engine (`/reminder_status`, `/reminder_on`, `/reminder_off`, `/reminder_time`, `/reminder_timezone`, `/reminder_min`; internal 15-minute schedule trigger). Pending resolution is `manager_status` primary / `lifecycle_status` secondary / legacy-defaults-to-pending. `REMINDER_DELIVERIES` is a new additive Sheets tab. Offline harness 73/73 PASS; live command acceptance PASS across admin/moderator/revoked; a controlled reminder live exercise reached ACCESS_CONTROL and failed closed under Sheets quota (zero sends, correct behavior). Production reminders remain `enabled=false`. Operational.dev, access state, and AI OFF are unchanged. See `evidence/phase3f1/` and `reports/REPORT-iseo-sales-manager-bot-phase3f1-pending-leads-and-reminders-v1.md`.


## Phase 3F.2

Clean production ledger (`LEADS`), immutable lead events, stats epoch 05.08.2026, callback lookup v2, private external reporting workbook. Reminders remain OFF until explicit operator activation.



## Phase 3F.2.2 (final Admin polish)

Human event labels for `/lead_history` (including `telegram_sent`) and rebuilt Admin/moderator `/help`.
Evidence: `evidence/phase3f2-2/`. Report: `reports/REPORT-iseo-sales-manager-bot-phase3f2-2-final-admin-polish-v1.md`.

## Phase 3F.2.1 (view & reporting repair)

Repaired `/leads` LEADS field mapping, connected `/lead_history`, keyed reporting mapper, human source `Сайт i-seo.su`. See `reports/REPORT-iseo-sales-manager-bot-phase3f2-1-view-and-reporting-repair-v1.md`.

## Phase 3G.1 — INTLSEO first-contact standard (additive)

Approved five-template corpus + recipient personalization + manager assist contract. Offline harness **100/100 PASS**. AI OFF; no auto-send; Мопс never in client copy (Михаил for MOD_A). Live n8n patch applied. Profile seed repair: **Phase 3G.1.1** — LIVE PROFILES SEEDED; operator T1/T3 visual acceptance pending. Evidence: `evidence/phase3g1/` · `evidence/phase3g1-1/`.

## Phase 3G.1.1 — Live reply profile seed (additive)

ACCESS_CONTROL columns Q–V created and seeded. T1/T3 acceptance inject 4/4 Telegram; fail-closed harness 9/9 PASS. Admin 84 active. Report: `reports/REPORT-iseo-sales-manager-bot-phase3g1-1-live-profile-and-template-acceptance-v1.md`.
