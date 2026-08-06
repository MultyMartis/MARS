<!-- Phase 3H.5 final pre-AI soak T+0 observation 2026-08-06 -->
## Phase 3H.5 T+0 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.5 — Final pre-AI soak observation checkpoint T+0 |
| **Verdict** | `SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION` |
| **Executed** | **2026-08-06 19:52 Europe/Moscow** (~3h 32m after final T+0 16:20) |
| **STOP** | MOD_C identity reactivated after T+0 · lead card delivered (4-recipient fanout) |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI **OFF** · heartbeat OK · reminders armed |
| **Next mark** | T+6 06.08.2026 22:20 Europe/Moscow (calendar only; not PASS) |
| **Evidence** | [evidence/pre-ai-soak/](evidence/pre-ai-soak/) |
| **Report** | [REPORT-iseo-sales-manager-bot-final-pre-ai-soak-t0-v1.md](reports/REPORT-iseo-sales-manager-bot-final-pre-ai-soak-t0-v1.md) |
| **Gate** | Phase 3I.1 blocked |

<!-- Phase 3H.4.1 last processed status readback repair 2026-08-06 -->
## Phase 3H.4.1 (additive; prior)

| Field | Value |
|-------|-------|
| **Phase** | 3H.4.1 — Last production processed status readback repair |
| **Verdict** | `PHASE 3H.4.1 COMPLETE — STATUS READBACK REPAIRED; FINAL 48-HOUR SOAK RESTARTED` |
| **Root cause** | Empty CONFIG `last_production_processed_*` cache after 3H.4 backfill; Status fail-closed to `нет данных` |
| **Repair** | Admin Status `iseo-last-production-processed-v1.0` + CONFIG cache from LEADS |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI **OFF** · reminders **ON** |
| **Soak** | Attempt 2 interrupted · Final T+0 **2026-08-06 16:20 Europe/Moscow** · earliest PASS **2026-08-08 16:20 Europe/Moscow** |
| **Evidence** | [evidence/phase3h4-1/](evidence/phase3h4-1/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h4-1-last-processed-status-repair-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h4-1-last-processed-status-repair-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS |
<!-- Phase 3H.4 soak observability repair 2026-08-06 -->
## Phase 3H.4 (current)

| Field | Value |
|-------|-------|
| **Phase** | 3H.4 — Soak observability repair + soak restart |
| **Verdict** | `PHASE 3H.4 COMPLETE — SOAK OBSERVABILITY REPAIRED; 48-HOUR SOAK RESTARTED` |
| **Repairs** | `/reminder_status` SyntaxError · empty-poll heartbeat · `/status` production lead truth · health/status separation |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI **OFF** · reminders **ON** |
| **Soak T+0** | **2026-08-06 19:15 Europe/Moscow** · earliest PASS **2026-08-08 19:15 Europe/Moscow** |
| **Soak attempt 1** | 06.08.2026 14:20 МСК — **INVALIDATED** (observability repair) |
| **Evidence** | [evidence/phase3h4/](evidence/phase3h4/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h4-soak-observability-repair-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h4-soak-observability-repair-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS |

<!-- Phase 3H production hardening + pre-AI soak 2026-08-06 -->
## Phase 3H (additive; historical)

| Field | Value |
|-------|-------|
| **Phase** | 3H — Production hardening, Olya onboarding, reminders, pre-AI soak |
| **Verdict** | `PHASE 3H IMPLEMENTATION COMPLETE — 48-HOUR SOAK STARTED` |
| **3H.1** | Cleanup + reporting MANUAL truth + three-profile renderer PASS |
| **3H.2** | Olya restored (Оля, active, cards) · three-recipient Telegram 3/3 PASS |
| **3H.3** | Reminders ON 10:00 Europe/Moscow · source LEADS · zero-pending armed |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI **OFF** · reminders **ON** |
| **Recipients** | 3 — Андрей, Оля, Михаил · Никита revoked |
| **Reporting** | manual (`только вручную`) · tests/archive excluded |
| **Soak start** | 06.08.2026 14:20 МСК · earliest PASS 08.08.2026 14:20 МСК |
| **Evidence** | [evidence/phase3h1/](evidence/phase3h1/) · [phase3h2/](evidence/phase3h2/) · [phase3h3/](evidence/phase3h3/) · [pre-ai-soak/](evidence/pre-ai-soak/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3h-production-hardening-and-pre-ai-soak-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h-production-hardening-and-pre-ai-soak-v1.md) |
| **Gate** | Phase 3I.1 blocked until soak PASS + explicit operator approval |

<!-- Phase 3G.2.3 moderator start read-after-rehydrate 2026-08-06 -->
## Phase 3G.2.3 (additive; historical)

| Field | Value |
|-------|-------|
| **Phase** | 3G.2.3 — Moderator `/start` read-after-rehydrate repair |
| **Verdict** | `COMPLETE — MODERATOR START PROFILE REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Root cause** | Start Reply read pre-rehydrate `Read ACCESS_CONTROL` while Auth `access_upsert` already held Михаил (exec 24097) |
| **Fix** | Admin.dev Start prefers `j.access_upsert.reply_sender_name`; sheet fallback; same ID · 85 nodes · hash `7E0A13DB067254EF` |
| **Invariant** | Single-execution consistency: `/start` must not rely on the next command |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI OFF · reminders OFF |
| **Harness** | `phase3g23-harness.mjs` **30/30 PASS** |
| **Evidence** | [evidence/phase3g2-3/](evidence/phase3g2-3/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3g2-3-moderator-start-profile-repair-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3g2-3-moderator-start-profile-repair-v1.md) |
| **Operator gate** | MOD_A `/start` ×2 + `/my_reply_profile`; ADMIN_A `/start` + `/reply_profiles` |

<!-- Phase 3G.2.2 unified resolver + config truth repair 2026-08-06 -->
## Phase 3G.2.2 (additive; historical)

| Field | Value |
|-------|-------|
| **Phase** | 3G.2.2 — Unified reply profile resolver + config truth repair |
| **Verdict** | `COMPLETE — PROFILE RESOLVER UNIFIED; MODERATOR START READ-AFTER-REHYDRATE REPAIR PENDING` → closed by **3G.2.3** |
| **Root cause** | `Check User Authorization` `rowFromSheet()` stripped `reply_profile_*` fields; `/start`/`/my_status` last-seen upsert wrote ACCESS_CONTROL without those fields, wiping ADMIN_A and MOD_A on routine authenticated traffic |
| **Fix** | Anti-wipe projection allowlist + auto-rehydrate on same Admin.dev workflow; unified resolver `iseo-reply-profile-resolver-v1.0` backs all 8 profile read paths |
| **Storage** | Single authoritative `ACCESS_CONTROL` store confirmed; 4 profile rows, 0 duplicates, 0 renumbering |
| **Config truth** | Stale `sm-parser-v3.2` CONFIG key corrected to live `sm-parser-v3.3`; reporting sync display corrected to honest «выключена»; resolver version + active-recipient count (2) added to `/config` |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI OFF · reminders OFF |
| **Harness** | `phase3g22-harness.mjs` **53/53 PASS**; regression `phase3g2-harness.mjs` **42/42 PASS** |
| **Evidence** | [evidence/phase3g2-2/](evidence/phase3g2-2/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3g2-2-profile-resolver-and-config-truth-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3g2-2-profile-resolver-and-config-truth-v1.md) |
| **Follow-up** | Start stale-read closed in **3G.2.3** |

<!-- Phase 3G.2.1 silent help/start/config repair 2026-08-06 -->
## Phase 3G.2.1 (additive; historical)

| Field | Value |
|-------|-------|
| **Phase** | 3G.2.1 — Silent `/help` `/start` `/config` repair + response guard |
| **Verdict** | `COMPLETE — SILENT COMMANDS REPAIRED; OPERATOR ACCEPTANCE PENDING` |
| **Root causes** | Help/Start: corrupted `startReply` splice (`Unexpected token ')'`); Config: literal `\\n` in array (`Invalid or unexpected token`) |
| **Repair** | Admin.dev same ID; Help/Start/Config/Capture patched; no-silent recognized-command guard |
| **Runtime** | Ops **45** active · Admin **85** active · v2 inactive · AI OFF · reminders OFF |
| **Profiles** | unchanged 1–4 (Михаил №3 enabled) |
| **Evidence** | [evidence/phase3g2-1/](evidence/phase3g2-1/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3g2-1-silent-command-repair-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3g2-1-silent-command-repair-v1.md) |
| **Operator gate** | Visual `/help` `/start` `/config` as Admin + moderator `/help` `/start` `/my_reply_profile` |

<!-- Phase 3G.2 number-based profiles + text contract 2026-08-06 -->
## Phase 3G.2 (additive; historical)

| Field | Value |
|-------|-------|
| **Phase** | 3G.2 — Reply profile numbers + Telegram text / help / command docs |
| **Numbers** | 1 ADMIN_A Андрей enabled · 2 MOD_B_REVOKED Оля disabled · 3 MOD_A Михаил enabled · 4 MOD_C_REVOKED Никита disabled |
| **Commands** | Number-based `/reply_profile N` family; moderator `/my_reply_profile` only |
| **Text** | [TELEGRAM-TEXT-CONTRACT-v2.md](architecture/TELEGRAM-TEXT-CONTRACT-v2.md) · [TELEGRAM-COMMAND-REFERENCE-v1.md](guides/TELEGRAM-COMMAND-REFERENCE-v1.md) |
| **Help** | [ROLE-AWARE-HELP-BUILDER-v2.md](implementation/ROLE-AWARE-HELP-BUILDER-v2.md) — explicit templates, no substring patch |
| **Runtime** | Ops 45 active · Admin **85** after 3G.2.1 · v2 inactive · Parser 3.3 · LEADS / LEAD_EVENTS · epoch 05.08.2026 MSK · AI OFF · reminders OFF |
| **Evidence** | [evidence/phase3g2/](evidence/phase3g2/) |
| **Follow-up** | Silent `/help`/`/start`/`/config` repaired in **3G.2.1** |

## Phase 3G.1.1 (additive; historical seed)

| Field | Value |
|-------|-------|
| **Phase** | 3G.1.1 — Live reply profile seed + T1/T3 personalized template acceptance |
| **Verdict** | `COMPLETE — LIVE PROFILES SEEDED; OPERATOR TEMPLATE ACCEPTANCE PENDING` |
| **Profiles** | ACCESS_CONTROL Q–V seeded; ADMIN_A→Андрей; MOD_A→Михаил; revoked prepared disabled |
| **Acceptance inject** | T1 + T3 · 4 Telegram successes · 0 duplicates · `Мопс`=0 |
| **Harness** | Fail-closed band **9/9 PASS**; Phase 3G.1 baseline 100/100 retained |
| **Runtime** | Ops 45 active · Admin **84** active · v2 inactive · AI OFF · reminders OFF |
| **Evidence** | [evidence/phase3g1-1/](evidence/phase3g1-1/) |
| **Report** | [REPORT-iseo-sales-manager-bot-phase3g1-1-live-profile-and-template-acceptance-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3g1-1-live-profile-and-template-acceptance-v1.md) |
| **Operator gate** | Visual accept latest T1/T3 cards; ignore earlier empty-copy exploratory batches |

<!-- Phase 3G.1 INTLSEO first-contact 2026-08-06 -->
## Phase 3G.1 (additive)

| Field | Value |
|-------|-------|
| **Phase** | 3G.1 — INTLSEO approved first-contact + personalized manager assist |
| **Harness** | `phase3g1-harness.mjs` **100/100 PASS** |
| **Reply standard** | `iseo-first-contact-v1.0` (live cutover pending) |
| **AI** | OFF; assist contract exists, not globally enabled |
| **Evidence** | [evidence/phase3g1/](evidence/phase3g1/) |
| **Architecture** | [INTLSEO-FIRST-CONTACT-STANDARD-v1.md](architecture/INTLSEO-FIRST-CONTACT-STANDARD-v1.md) · [RECIPIENT-PERSONALIZED-REPLIES-v1.md](architecture/RECIPIENT-PERSONALIZED-REPLIES-v1.md) · [AI-MANAGER-ASSIST-v1.md](architecture/AI-MANAGER-ASSIST-v1.md) · [REPLY-PROFILE-CONTRACT-v1.md](architecture/REPLY-PROFILE-CONTRACT-v1.md) · **3G.2:** [REPLY-PROFILE-NUMBERING-v1.md](architecture/REPLY-PROFILE-NUMBERING-v1.md) · [TELEGRAM-TEXT-CONTRACT-v2.md](architecture/TELEGRAM-TEXT-CONTRACT-v2.md) |
| **Live patch** | applied (3G.1); profile seed repair **3G.1.1 complete**; number addressing **3G.2** |

<!-- Phase 3F.2 clean ledger active 2026-08-05; reminders OFF; reporting private -->
# i-SEO Sales Manager Bot — Operational Index

**project_id:** `iseo-sales-manager-bot`  
**Process line:** ISEO-SALES-MANAGER-BOT  
**Primary logical owner:** OPS  
**Domain root:** [README.md](README.md)

---

## Current status

| Field | Value |
|-------|-------|
| **Status** | **Phase 3G.2.2** — unified reply profile resolver + config truth repair; operator Telegram acceptance pending |
| **Active stage** | `sm-parser-v3.3` / INTLSEO first-contact + `iseo-recipient-name-v1.1` / `sm-msg-v2.4` / `iseo-reply-profile-resolver-v1.0` / AI OFF / reminders OFF |
| **Runtime** | External n8n — Operational.dev **active** (45 nodes); Admin.dev **active (85 nodes, same workflow patched in 3G.2.2)**; Sales-Manager-v2 inactive |
| **Phase 3F.2** | Clean production ledger + reporting workbook; callbacks v2; reminders OFF |
| **Live parity vs Sales-Manager-v2** | **CUT OVER** — Operational.dev replaced v2 for intake; v2 preserved inactive; filter \`labelIds\` parity confirmed |
| **JSON baselines v1/v2** | **PRESENT** — Phase 3A.1 baselines + Phase 3B sanitized .dev exports; Phase 3C–3D.3 evidence under `evidence/phase3*` |
| **Registry** | status **planned** unchanged — promotion to active requires **separate governance gate** (`REGISTRY_STATUS_PROMOTION_PENDING`) |
| **ATLAS** | Recommendation only — ORG-0003 / PER-0001 / PER-0010 / PER-0011; **no** new IDs |
| **Next** | Operator visual confirm /help + /lead_history 1 after 3F.2.2; reminders stay OFF until explicit activation |
| **AI** | **OFF** — `ai_enabled=false`; no AI ON claim in Phase 3F.1 |
| **Product layer** | [product/](product/) |
| **Evidence 3F.2.2** | [evidence/phase3f2-2/](evidence/phase3f2-2/) — human event labels + Admin help rebuild |
| **Evidence 3F.1** | [evidence/phase3f1/](evidence/phase3f1/) — pending commands + reminder engine, harness 73/73 PASS |
| **Evidence 3E.2.3** | [evidence/phase3e2-3/](evidence/phase3e2-3/) — exactly-once + five-poll live proof PASS |
| **Evidence 3E.2.2** | [evidence/phase3e2-2/](evidence/phase3e2-2/) · [reports/REPORT-iseo-sales-manager-bot-phase3e2-2-final-acceptance-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3e2-2-final-acceptance-v1.md) |
| **Evidence 3E.2.1** | [evidence/phase3e2-1/](evidence/phase3e2-1/) |
| **Evidence 3E.2** | [evidence/phase3e2/](evidence/phase3e2/) |
| **Evidence 3E.1** | [evidence/phase3e1/](evidence/phase3e1/) · closed — operator visual A–F PASS |
| **Architecture 3F.1** | [PENDING-LEADS-VIEW-v1.md](architecture/PENDING-LEADS-VIEW-v1.md) · [PENDING-REMINDER-v1.md](architecture/PENDING-REMINDER-v1.md) · [REMINDER-DELIVERY-IDEMPOTENCY-v1.md](architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md) |
| **Architecture 3E.2.1** | [HUMAN-REPLY-STYLE-v1.md](architecture/HUMAN-REPLY-STYLE-v1.md) · [MEANINGFUL-COMMENT-BRANCHING-v1.md](architecture/MEANINGFUL-COMMENT-BRANCHING-v1.md) · [FIRST-REPLY-QUALITY-LINTER-v1.md](architecture/FIRST-REPLY-QUALITY-LINTER-v1.md) · [DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md](architecture/DELIVERY-FAIL-CLOSED-RECONCILIATION-v1.md) |
| **Architecture 3E.2** | [FIRST-REPLY-ENGINE-v2.md](architecture/FIRST-REPLY-ENGINE-v2.md) · [KNOWN-INFORMATION-GUARD-v1.md](architecture/KNOWN-INFORMATION-GUARD-v1.md) · [MANAGER-CARD-v2.4-CONTRACT-v1.md](architecture/MANAGER-CARD-v2.4-CONTRACT-v1.md) |
| **Architecture 3E.1** | [LEAD-SEMANTIC-MODEL-v1.md](architecture/LEAD-SEMANTIC-MODEL-v1.md) · [PARSER-3.3-CONTRACT-v1.md](architecture/PARSER-3.3-CONTRACT-v1.md) · [FIRST-REPLY-RULES-v1.md](architecture/FIRST-REPLY-RULES-v1.md) |
| **Evidence 3D.8.3** | [evidence/phase3d8-3/](evidence/phase3d8-3/) · [reports/REPORT-iseo-sales-manager-bot-phase3d8-3-button-label-polish-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d8-3-button-label-polish-v1.md) |
| **Evidence 3D.8.2** | [evidence/phase3d8-2/](evidence/phase3d8-2/) · [reports/REPORT-iseo-sales-manager-bot-phase3d8-2-actor-attribution-and-revoked-moderators-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d8-2-actor-attribution-and-revoked-moderators-v1.md) |
| **Evidence 3D.8.1** | [evidence/phase3d8-1/](evidence/phase3d8-1/) · [reports/REPORT-iseo-sales-manager-bot-phase3d8-1-live-callback-repair-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d8-1-live-callback-repair-v1.md) |
| **Evidence 3D.8** | [evidence/phase3d8/](evidence/phase3d8/) · [reports/REPORT-iseo-sales-manager-bot-phase3d8-product-baseline-backup-and-buttons-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d8-product-baseline-backup-and-buttons-v1.md) |
| **Evidence 3D.7.1** | [evidence/phase3d7-1/](evidence/phase3d7-1/) · [reports/REPORT-iseo-sales-manager-bot-phase3d7-1-duplicate-delivery-containment-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d7-1-duplicate-delivery-containment-v1.md) |
| **Evidence 3D.7** | [evidence/phase3d7/](evidence/phase3d7/) · [reports/REPORT-iseo-sales-manager-bot-phase3d7-multi-recipient-lead-delivery-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d7-multi-recipient-lead-delivery-v1.md) |
| **Evidence 3D.6** | [evidence/phase3d6/](evidence/phase3d6/) · [reports/REPORT-iseo-sales-manager-bot-phase3d6-personal-status-and-role-notifications-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d6-personal-status-and-role-notifications-v1.md) |
| **Evidence 3D.5.2** | [evidence/phase3d52/](evidence/phase3d52/) · [reports/REPORT-iseo-sales-manager-bot-phase3d52-admin-silence-incident-recovery-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d52-admin-silence-incident-recovery-v1.md) |
| **Evidence 3D.5.1** | [evidence/phase3d51/](evidence/phase3d51/) |
| **Evidence 3D.5** | [evidence/phase3d5/](evidence/phase3d5/) |
| **Evidence 3D.4** | [evidence/phase3d4/](evidence/phase3d4/)
| **Evidence 3D.3.1** | [evidence/phase3d31/](evidence/phase3d31/) |

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
| 5 | [architecture/TELEGRAM-UX-CONTRACT-v1.md](architecture/TELEGRAM-UX-CONTRACT-v1.md) | Phase 2 (+ **text →** [TELEGRAM-TEXT-CONTRACT-v2.md](architecture/TELEGRAM-TEXT-CONTRACT-v2.md) in 3G.2) |
| 6 | [architecture/ADMIN-COMMAND-CONTRACT-v1.md](architecture/ADMIN-COMMAND-CONTRACT-v1.md) | Phase 2 |
| 7 | [architecture/HEALTHCHECK-CONTRACT-v1.md](architecture/HEALTHCHECK-CONTRACT-v1.md) | Phase 2 (+ 3C.1 live query wording) |
| 7a | [architecture/GMAIL-INTAKE-FILTER-CONTRACT-v1.md](architecture/GMAIL-INTAKE-FILTER-CONTRACT-v1.md) | Phase 3C.2 |
| 8 | [architecture/AI-OFF-ON-CONTRACT-v1.md](architecture/AI-OFF-ON-CONTRACT-v1.md) | Phase 2 |
| 8a | [architecture/LEAD-SEMANTIC-MODEL-v1.md](architecture/LEAD-SEMANTIC-MODEL-v1.md) | Phase 3E.1 |
| 8b | [architecture/PARSER-3.3-CONTRACT-v1.md](architecture/PARSER-3.3-CONTRACT-v1.md) | Phase 3E.1 |
| 8c | [architecture/FIRST-REPLY-RULES-v1.md](architecture/FIRST-REPLY-RULES-v1.md) | Phase 3E.1 |

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
| 37 | [reports/REPORT-iseo-sales-manager-bot-phase3c1-first-real-lead-intake-diagnosis-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3c1-first-real-lead-intake-diagnosis-v1.md) | Phase 3C.1 |
| 38 | [evidence/phase3c1/](evidence/phase3c1/) | Phase 3C.1 evidence |
| 39 | [reports/REPORT-iseo-sales-manager-bot-phase3c2-gmail-routing-and-first-lead-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3c2-gmail-routing-and-first-lead-v1.md) | Phase 3C.2 |
| 40 | [evidence/phase3c2/](evidence/phase3c2/) | Phase 3C.2 evidence |
| 41 | [reports/REPORT-iseo-sales-manager-bot-phase3d-production-stabilization-and-olya-handoff-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d-production-stabilization-and-olya-handoff-v1.md) | Phase 3D |
| 42 | [evidence/phase3d/](evidence/phase3d/) | Phase 3D evidence |
| 43 | [guides/OLYA-LEAD-WORK-GUIDE-v1.md](guides/OLYA-LEAD-WORK-GUIDE-v1.md) | Olya handoff |
| 44 | [guides/OPERATOR-RUNBOOK-v1.md](guides/OPERATOR-RUNBOOK-v1.md) | Operator runbook |
| 45 | [reports/REPORT-iseo-sales-manager-bot-phase3d2-production-closeout-and-olya-handoff-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d2-production-closeout-and-olya-handoff-v1.md) | Phase 3D.2 |
| 46 | [evidence/phase3d2/](evidence/phase3d2/) | Phase 3D.2 evidence |
| 47 | [reports/REPORT-iseo-sales-manager-bot-phase3d21-admin-reply-and-runtime-closeout-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d21-admin-reply-and-runtime-closeout-v1.md) | Phase 3D.2.1 |
| 48 | [evidence/phase3d21/](evidence/phase3d21/) | Phase 3D.2.1 evidence |
| 49 | [reports/REPORT-iseo-sales-manager-bot-phase3d3-manager-ux-actions-and-history-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d3-manager-ux-actions-and-history-v1.md) | Phase 3D.3 |
| 50 | [evidence/phase3d3/](evidence/phase3d3/) | Phase 3D.3 evidence (16 docs) |
| 51 | [reports/REPORT-iseo-sales-manager-bot-phase3d31-archive-recovery-and-sheets-safety-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d31-archive-recovery-and-sheets-safety-v1.md) | Phase 3D.3.1 |
| 52 | [evidence/phase3d31/](evidence/phase3d31/) | Phase 3D.3.1 evidence |
| 53 | [knowledge/WEBSITE-FORM-FORMATS-v1.md](knowledge/WEBSITE-FORM-FORMATS-v1.md) | Website form registry |
| 54 | [reports/REPORT-iseo-sales-manager-bot-phase3d4-manager-enrollment-and-form-semantics-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3d4-manager-enrollment-and-form-semantics-v1.md) | Phase 3D.4 |
| 55 | [evidence/phase3d4/](evidence/phase3d4/) | Phase 3D.4 evidence (14 docs: identity, roles, start/help, Olya callbacks, emoji v2.1, parser v3.2 semantics, supplied form, multi-form plan, admin regression, workflow state, receipt) |

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
| **Phase 3C** | Operational production cutover (AI OFF) | **DONE** |
| Phase 3C.1 | First real lead observation / eligibility diagnosis | **DONE** |
| **Phase 3C.2** | Gmail routing audit + first real lead acceptance | **DONE** |
| **Phase 3D** | Production stabilization / Olya handoff | **DONE** (technical) |
| **Phase 3D.1** | Real-form parser + clean lead | **DONE** |
| **Phase 3D.2** | Production closeout / Olya handoff docs | **DONE** (typed Trigger pending) |
| **Phase 3D.2.1** | Admin duplicate reply + runtime lead stamp | **DONE** (harness; typed Trigger pending) |
| **Phase 3D.3** | Manager UX (`sm-msg-v2`), inline lead actions, `/leads`, lifecycle Sheets model | **DONE** |
| **Phase 3D.3.1** | `/leads` multi-card + Sheets phone RAW safety | **DONE** |
| **Phase 3D.4** | Olya manager enrollment, sm-parser-v3.2 / sm-msg-v2.1, form registry | **DONE** — Olya live Telegram **pending** |
| **Phase 3D.6** | `/my_status`, role notifications, 3d6b Code-mode hotfix, live non-Admin status acceptance | **COMPLETE — personal status ready; notification delivery SAFE UNKNOWN** |
| **Phase 3D.8** | Product baseline, recovery receipts, button forensic/repair contract, Parser 3.3 research | **COMPLETE** (buttons/attribution/labels); research superseded by 3E.1 |
| **Phase 3D.8.1–3** | Live callbacks, actor attribution, short button labels | **COMPLETE** |
| **Phase 3E.1** | Parser 3.3 + Lead Semantic Model + `sm-msg-v2.3` | **HARNESS COMPLETE (46/46); live semantic PENDING** |
| **Phase 3E.2** | First Reply Engine v2 (`sm-reply-v2.0`) | Engine implemented; umbrella Phase 3E.2 **NOT COMPLETE** pending 3E.2.3 gates |
| **Phase 3E.2.1** | Human Reply Style v1 + meaningful comment branching + quality linter + delivery fail-closed reconciliation | **OPERATOR-ACCEPTED; no redesign in 3E.2.3** |
| **Phase 3E.2.2** | Quota diagnosis and acceptance preparation | **ATTENTION; superseded by 3E.2.3 optimization gate** |
| **Phase 3E.2.3** | Sheets call-budget, bounded reads/retries, single-flight, final exactly-once proof | **COMPLETE — proof delivered; operator visual confirmation pending** |
| **Phase 3F.1** | Pending-lead commands (`/pending_count`, `/pending_leads`, `/pending_leads_test`) + daily reminder engine (`sm-pending-reminder-v1.0`) | **COMPLETE — COMMANDS AND REMINDER ENGINE READY; OPERATOR ACTIVATION PENDING** |
| **Phase 3G.2.2** | Unified reply profile resolver (anti-wipe + auto-rehydrate) + config truth repair | **COMPLETE — PROFILE RESOLVER UNIFIED; OPERATOR ACCEPTANCE PENDING** |
| Next form iteration | Per `MULTI-FORM-TEST-PLAN-v1` | **not opened** |
| Live rename | After clean-lead acceptance | **deferred** |
| Registry promotion | Separate governance charter | **not opened** |
| Reminder production activation | Operator sets `pending_reminders_enabled=true` | **not opened** |

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

*Last updated: 2026-08-05 — Phase 3E.2.3 Sheets call-budget optimization, inactive quiet window.*


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.

## Phase 3D.5.2 — Admin silence incident recovery

- Root causes: n8n-disallowed `require('crypto')` in Admin Code nodes; CONFIG row fan-out multiplying ACCESS_CONTROL reads (Sheets rate limit); error paths with no Telegram reply.
- Repair: pure-JS SHA-256; **Collapse Authorization Context** (one command-context item); Sheets `onError=continueRegularOutput`; guaranteed one reply; Admin bootstrap recovery-only command set.
- Evidence: `evidence/phase3d52/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d52-admin-silence-incident-recovery-v1.md`.

*Last updated: 2026-08-04 — Phase 3D.6.1 live `/my_status` acceptance closeout and 3d6b hotfix canonicalization.*

## Phase 3E.2.3 architecture set

- `architecture/SHEETS-CALL-BUDGET-v1.md`
- `architecture/OPERATIONAL-SINGLE-FLIGHT-v1.md`
- `architecture/SHEETS-BACKOFF-POLICY-v1.md`
- `implementation/ACCESS-CONTROL-SNAPSHOT-v1.md`
- `implementation/BOUNDED-DELIVERY-LEDGER-READ-v1.md`

## Phase 3F.1 — pending leads + daily reminder engine

- Admin.dev same ID `wLrLp4WQHm1VJmxz`: 59 → 79 nodes.
- New commands: `/pending_count`, `/pending_leads`, `/pending_leads_test`, `/reminder_status`, `/reminder_on`, `/reminder_off`, `/reminder_time`, `/reminder_timezone`, `/reminder_min`.
- Internal 15-minute Schedule Trigger inside Admin.dev — **not** a new workflow.
- Pending rule: `manager_status` primary, `lifecycle_status` secondary, legacy rows default to pending unless closed; excludes processed/spam/technical-retry/invalid; deduped by business key; probable tests excluded by default; oldest-first.
- Reminder CONFIG: `enabled=false` default, `10:00` `Europe/Moscow`, version `sm-pending-reminder-v1.0`; new additive `REMINDER_DELIVERIES` ledger tab.
- Offline harness `73/73 PASS` (`evidence/phase3f1/HARNESS-RESULTS-v1.md`).
- Controlled reminder live exercise reached ACCESS_CONTROL and correctly failed closed under Sheets quota; production reminders remain OFF.
- Operational.dev unchanged (45 nodes); access unchanged; AI OFF; workflows created=0; destructive migrations=0.
- Architecture: `architecture/PENDING-LEADS-VIEW-v1.md` · `architecture/PENDING-REMINDER-v1.md` · `architecture/REMINDER-DELIVERY-IDEMPOTENCY-v1.md`.
- Implementation: `implementation/PENDING-COMMANDS-v1.md` · `implementation/REMINDER-CONFIG-COMMANDS-v1.md`.
- Evidence: `evidence/phase3f1/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3f1-pending-leads-and-reminders-v1.md`.



### Phase 3F.2.1
- Status: view/reporting repair applied; operator acceptance pending
- Evidence: `evidence/phase3f2-1/`
- Report: `reports/REPORT-iseo-sales-manager-bot-phase3f2-1-view-and-reporting-repair-v1.md`

