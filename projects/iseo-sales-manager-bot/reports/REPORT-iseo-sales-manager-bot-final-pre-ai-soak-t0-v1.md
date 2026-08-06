# REPORT — ISEO SALES MANAGER BOT FINAL PRE-AI SOAK T+0 CHECKPOINT

## 1. Verdict

`SOAK T+0 STOP — PRODUCTION INVARIANT VIOLATION`

Primary STOP causes: **MOD_C_REVOKED identity reactivated after T+0** and **lead card delivered to that identity** (4-recipient fanout vs baseline 3).

## 2. Checkpoint time

**2026-08-06 19:52 Europe/Moscow** (observation window ~19:43–19:52 МСК).

Final soak T+0 charter: **2026-08-06 16:20 Europe/Moscow**. Checkpoint is after T+0 and before T+6 (22:20 МСК). No future checkpoint evidence fabricated.

## 3. Soak elapsed

**~3h 32m** since final T+0.

## 4. Next checkpoint

Calendar next: **T+6 @ 2026-08-06 22:20 Europe/Moscow**.  
Operational next: **operator remediation** of access/delivery STOP before any PASS-path soak continuation decision. Earliest valid T+48 completion time remains **2026-08-08 16:20 Europe/Moscow** only if a valid soak is later re-armed by explicit charter — **not claimed here**.

## 5. Canonical baseline

| Item | Result |
|---|---|
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-sm-soak-t0-20260806-234132\repo` |
| Base | `origin/mars/canonical-post-recovery` @ `0d29cc24` |
| Ancestors | `63385c13`, `610500fd`, `0d29cc24` present |
| Dirty `X:\AI MARS` | not used for commit |

## 6. Workflow states

| Workflow | ID | Active | Nodes |
|---|---|---:|---:|
| Operational.dev | `xSnXPy8cEHoZw6xG` | true | 45 |
| Admin.dev | `wLrLp4WQHm1VJmxz` | true | 85 |
| Sales-Manager-v2 | `h8I2Tl2yl4uzhUnB` | false | 19 |

No ID replacement. No new i-SEO Sales Manager workflows. Sole Gmail **intake** = Operational Fetch Leads.

## 7. Gmail schedule

Schedule Trigger `minutesInterval=2`. Recent scheduled gaps **120s**. Empty polls succeed.

## 8. Gmail heartbeat

Contract `iseo-gmail-poll-heartbeat-v1.0` advancing on empty scheduled polls. Stale heartbeat incidents: **0**. `/health` not used as poll proof.

## 9. Production lead counts

| Counter | Value |
|---|---:|
| scheduled polls inspected | ≥15 detailed (+ census 106 listed) |
| successful scheduled polls | 106/106 listed since T+0 |
| stale heartbeat incidents | 0 |
| production leads received (inferred cumulative) | ≥3 |
| production leads pending | SAFE UNKNOWN |
| production leads processed | ≥1 (PROD_LEAD_1); PROD_LEAD_2 unknown |
| production leads spam | ≥1 (PROD_LEAD_3) |
| production leads lost | 0 |
| production leads duplicated | 0 |
| recipient delivery duplicates | 0 (per recipient on PROD_LEAD_2); PROD_LEAD_3 = illegal 4th recipient |
| revoked deliveries | **1** (PROD_LEAD_3 → MOD_C) |
| active profiles (desired) | 3 |
| revoked profiles (desired) | 1 |
| profile wipes | 0 |
| blank active profile names / numbers | **1** blank profile_no on MOD_C row |
| reminder claims after T+0 | 0 |
| reminder sends after T+0 | 0 |
| reminder duplicates | 0 |
| production reporting mode | manual |
| active errors (execution) | 0 |
| OpenRouter calls | 0 |
| customer auto-messages | 0 |
| workflows created | 0 |
| Gmail intake workflows | 1 |
| access changes | **1** |
| Phase 3I.1 started | 0 |

## 10. Production lead integrity

Two genuine post-T+0 ingestions (PROD_LEAD_2, PROD_LEAD_3), `duplicate=new`, parser `sm-parser-v3.3`, no synthetic markers on inspected parse path. PROD_LEAD_3 later marked spam via Admin callback. No manufactured leads.

## 11. Delivery integrity

- PROD_LEAD_2: **3/3** eligible recipients; MOD_C revoked at that moment — OK.
- PROD_LEAD_3: **4** successful card sends including MOD_C identity — **STOP**.
- Customer auto-send: none.
- No Telegram delivery loop observed.

## 12. Profile integrity

Baseline four-row model broken in spirit: MOD_C identity **active**, blank `profile_no`. Access change after T+0 = 1.

## 13. Reminder state

Enabled 10:00 Europe/Moscow; min 1; tests/archives excluded; once-per-business-date; CONFIG recipients count still 3 (stale vs live access). No sends/claims after T+0. Next window 07.08.2026 10:00 not elapsed.

## 14. Reporting state

`reporting_sync_mode=manual`; sync enabled false; tests/archive excluded. Manual reporting limitation accepted baseline — not a soak defect.

## 15. Command observability

No native Telegram `/status`…`/reply_profiles` packet executed **after** final T+0 in Admin execution history. Pre-T+0 post-repair acceptance packet exists historically but is **not** reused as T+0 command proof. Reminder CONFIG reads substitute for AI/reminder/reporting gates. **Operator visual acceptance still recommended** for the nine read-only commands after remediation.

## 16. Active errors

No Ops execution failures since T+0. Invariant STOP is policy/state, not crash.

## 17. Capacity and retries

No quota/rate-limit storm. Poll cadence stable. Duplicate spam callback pair = ATTENTION only.

## 18. AI gate

AI OFF. OpenRouter 0. Phase 3I.1 not started.

## 19. Customer auto-send gate

OFF. No outbound customer messages observed.

## 20. Production invariants

| Invariant | Result |
|---|---|
| Workflows/schedule healthy | PASS |
| Fresh Gmail heartbeat | PASS |
| No lead loss/duplication | PASS (for observed ingestions) |
| No profile wipe | PASS (rows remain) |
| No revoked delivery | **FAIL** |
| Reminder config intact | PASS (armed) |
| No duplicate reminder | PASS |
| Reporting truth unchanged | PASS |
| AI OFF / customer auto-send OFF | PASS |
| Access frozen except emergency revoke | **FAIL** (reactivation) |

## 21. Watch items

1. Reminder CONFIG `pending_reminder_active_recipients_count=3` vs live 4-capable access after reactivation.
2. Ops overwrites `last_production_processed_*` on delivery success — may desync `/status` from human lifecycle semantics (3H.4.1 intent).
3. Dual spam callbacks on same lead alias.
4. Missing post-T+0 Admin command packet.

## 22. SAFE UNKNOWN

- Exact Sheets LEADS row census / pending count without mutation or operator `/stats`.
- PROD_LEAD_2 final lifecycle status.
- Whether operator intentionally approved MOD_C reactivation (effect still violates soak charter).

## 23. Evidence

- `evidence/pre-ai-soak/FINAL-SOAK-CHECKPOINT-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-LIVE-WORKFLOW-STATE-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-GMAIL-HEARTBEAT-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-PRODUCTION-COUNTERS-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-PROFILE-INTEGRITY-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-REMINDER-STATE-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-ERROR-SUMMARY-T0-v1.md`
- `evidence/pre-ai-soak/FINAL-SOAK-AI-GATE-T0-v1.md`

## 24. Files changed

Evidence above + `guides/PRE-AI-SOAK-RUNBOOK-v1.md` + `product/PRODUCTION-BASELINE-PRE-AI-SOAK-v1.md` + `product/CURRENT-PRODUCTION-BASELINE-v1.md` + `OPERATIONAL-INDEX.md` + `product/PRODUCT-ROADMAP-v1.md` + this report.

## 25. Security validation

Committed text sanitized: no customer names/phones/domains, no Telegram/chat IDs, no workbook IDs, no raw payloads/exports/credentials/screenshots. Runtime forensic JSON stays under Storage worktree `runtime/out/` (not committed).

## 26. Commit

`691fc347` — `docs(iseo-sales-manager-bot): record final pre-ai soak t0 checkpoint`  
Scope: `projects/iseo-sales-manager-bot/**` only (clean worktree).

## 27. Push

Pushed without force to `origin/mars/canonical-post-recovery` (`0d29cc24..691fc347`).

## 28. Phase 3I.1 gate

**Blocked.** AI OFF. No pilot start.

## 29. Stop condition

Checkpoint complete: live state inspected; invariants classified **STOP**; sanitized evidence written; report committed/pushed from clean worktree; next calendar checkpoint identified without fabrication; Phase 3I.1 remains blocked. **No workflow patch. No soak cosmetic restart. No AI enablement. No profile restore/revoke performed by this agent.**
