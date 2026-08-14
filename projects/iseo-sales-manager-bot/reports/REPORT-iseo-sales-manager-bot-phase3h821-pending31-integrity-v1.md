# REPORT — ISEO-SALES-MANAGER-BOT PHASE 3H.8.2.1 PRE-WINDOW PENDING-31 INTEGRITY

**Process-line:** `ISEO-SALES-MANAGER-BOT — PHASE 3H.8.2.1 PRE-WINDOW PENDING-31 INTEGRITY CHECK`  
**Captured:** 2026-08-14 12:32 Europe/Moscow  
**Mode:** READ-ONLY (no status writes, no reminder send, no AI, no soak restart)

---

## 1. Verdict

`STOP — REMINDER PENDING SELECTOR INTEGRITY DEFECT`

Phase 3H.8.2 `current eligible pending = 31` is **not** 31 unique current business leads.

Live `lead_clean_v2` (12:32 MSK) under the **exact** Admin `Reminder Build Claims` selector:

| Measure | Count |
|---|---|
| CLEAN rows | 129 |
| `life()=pending` (incl. tests) | 112 |
| Naive pending ∩ not-test (3H.8.2-style row count) | **30** |
| Unique eligible business keys (what tomorrow’s reminder will use) | **10** |
| Extra duplicate CLEAN rows inside the naive 30 | **20** |

The live reminder node **does** dedupe by `lead_id` / `stable_lead_ref` / `source_message_id` (first row wins). The 31 figure came from a **non-deduped** CLEAN filter in 3H.8.2 prep (`life==pending && !isTest`), not from `pending_count` emitted by `Reminder Build Claims`.

No production patch in this checkpoint.

---

## 2. Reported pending count

| Source | Value |
|---|---|
| Phase 3H.8.2 claimed | 31 |
| Live naive pending ∩ not-test | 30 |
| Live **selector** unique `pending_count` | **10** |
| Delta 31 → 10 | 20 duplicate CLEAN rows + 1 extra row that full `isTest()` now excludes |

3H.8.2 prep used a weaker test heuristic (lead_id/name only). Live reminder `isTest()` also uses `is_probable_test`, `PHASE_3` markers, `source=synthetic`, and summary/name testish signals. That accounts for 31 vs 30. Neither 31 nor 30 is the reminder `pending_count`.

---

## 3. Dataset used by reminder

Authoritative reminder dataset (live Admin.dev, 92 nodes):

| Node | Sheet | Range |
|---|---|---|
| `Read CLEAN for Reminder` | `lead_clean_v2` | `A1:ZZ500` |

`Reminder Build Claims` does **not** read `LEADS`, `LEAD_EVENTS`, or archive columns.

Admin node `Read LEADS for History` also targets **`lead_clean_v2`**, not a separate `LEADS` tab. CLEAN `manager_status` **is** current-state for this product.

Selector (live copy, archive/close_reason **absent**):

1. `manager_status` ∈ {processed, spam} else `lifecycle_status` ∈ {processed, spam} else **pending** (including `new`).
2. Drop probable tests unless `include_tests`.
3. Require a business key; keep **first** row per key (sheet order).
4. `pending_count = unique keys`.

Live CLEAN snapshot: ephemeral read 2026-08-14 12:32:55 Europe/Moscow. Admin/Ops untouched (92 / 45). Follow-up ACCESS/ledger/CONFIG read hit quota (`No item to return was found`). Events sheet this run: HTTP error item (`events_err=1`).

---

## 4. Unique business leads

**10** unique reminder-eligible keys.

Two duplicate groups inside the naive 30:

| Alias | Duplicate CLEAN rows | Status on every copy |
|---|---|---|
| `LEAD_F4C9D9693444` | 6 | `new` → selector pending |
| `LEAD_C3EF8E536C35` | 16 | `pending` |

20 extra rows. Not separate business leads. Not separate Telegram cards in the selector — same `lead_id` repeated on CLEAN (Gmail re-ingest / historical copies).

---

## 5. Valid current pending

Among the **10 unique** selector rows: **10 × `VALID_CURRENT_PENDING`** on CLEAN current-state.

That is the count tomorrow’s reminder will report **if nothing changes**. It is **not** 31.

`REMINDER_ACCEPTANCE_LEAD_2` is one of the 10, once.

---

## 6. Stale projections

**0** unique rows where CLEAN says pending while a later CLEAN Spam/Processed field exists.

`LEAD_EVENTS` live read failed (quota). Stale-event proof is therefore **CLEAN + callback executions + reopen record**, not a full events replay:

- Non-reopened recent spam rows stay `manager_status=spam` and are **not** selector-eligible.
- Selector does not keep an old pending copy when a later CLEAN row for the same key is spam: it filters `life!==pending` **before** first-wins. All 6+16 duplicate copies are pending, so first-wins does not hide a later terminal row **in this snapshot**.

`SAFE_UNKNOWN` for a later Spam event that did not update CLEAN.

---

## 7. Terminal-state leakage

**0** terminal CLEAN rows in the selector set.

Recent genuine Spam (still spam, not eligible):

| Alias | CLEAN status | Last action | Updated (UTC) |
|---|---|---|---|
| `LEAD_F9361746E171` | spam | `marked_spam` | 2026-08-13T09:02:31Z |
| `LEAD_C8D974B3429F` | spam | `marked_spam` | 2026-08-13T09:02:14Z |

Admin callback execs `30042` / `30041` (13 Aug 12:02 MSK) wrote those Spam updates. They do **not** remain reminder-eligible.

`REMINDER_ACCEPTANCE_LEAD_2` was spam at 10:15 MSK (exec `30821`); after reopen it is pending (see §11). That is intended, not leakage.

---

## 8. Test/archive leakage

| Check | Result |
|---|---|
| Test rows in unique selector set | **0** |
| Archive column on CLEAN | **absent** (`is_archived` / `archive_state` not in schema) |
| CONFIG `pending_reminder_include_archive=false` | displayed by `/reminder_status`; **not applied** in `Reminder Build Claims` |
| Archive leak | **0** (nothing to leak) |

Tests remain on CLEAN (`lead_synth_*`, `lead_msg_synth_*`, harness rows). They inflate `life=pending` (112) but are excluded by reminder `isTest()`. Unique 10 are non-test.

---

## 9. Duplicate analysis

**Defect:** treating CLEAN pending∩not-test **row count** as `pending_count`.

| Item | Value |
|---|---|
| Duplicate business identities | **2** |
| Extra rows | **20** |
| Naive 30 − extras | 10 unique |

`LEAD_C3EF8E536C35`: 16 CLEAN rows, same Gmail `lead_id`, timestamps ~30s apart on 2026-08-04 (re-poll copies).  
`LEAD_F4C9D9693444`: 6 CLEAN rows, `manager_status=new`, empty received timestamps.

Reminder first-wins collapses each group to 1. `/pending_count` (`Pending View Handler`) also dedupes (prefers latest). 3H.8.2’s 31 did **not**.

---

## 10. Age distribution

Unique valid pending (10), age from received/created, as of 12:32 MSK 2026-08-14:

| Bucket | Count |
|---|---|
| today | 0 |
| 1 day | 2 (`REMINDER_ACCEPTANCE_LEAD_1`, `REMINDER_ACCEPTANCE_LEAD_2`) |
| 2–7 days | 1 (`LEAD_08C4CF248F93`) |
| 8–30 days | 6 |
| older than 30 days | 0 |
| unknown | 1 (`LEAD_F4C9D9693444`, no timestamp) |

Old pending is **not** classified invalid merely by age. 10 unique is a plausible real backlog; 31 is not.

---

## 11. Acceptance lead

`REMINDER_ACCEPTANCE_LEAD_2` = Phase 3H.8.2 `LEAD_A6A0FB0DBFF6` (suffix `…74b4d095`).

| Check | Result |
|---|---|
| Same stable lead ID as 3H.8.2 | **yes** |
| CLEAN `manager_status` | `pending` |
| `last_manager_action` | `reopened` @ 2026-08-14T08:51:38.304Z |
| `manager_status_source` | `phase3h82_acceptance_reopen` |
| `spam_at` preserved | 2026-08-13T07:40:36.921Z |
| `close_reason` after reopen | empty |
| test / archive | false / false |
| Reminder eligible | **yes** |
| Times in unique 10 | **exactly once** |
| New CLEAN row | no (still 129 rows) |
| Card resurface | no (3H.8.2 reopen TMP) |

`REMINDER_ACCEPTANCE_LEAD_1` (`LEAD_3990BF2451B7`) remains pending from Phase 3H.8 reopen; also in the 10, once.

---

## 12. Recent Spam/Processed reconciliation

| Alias | CLEAN now | Selector | Notes |
|---|---|---|---|
| `LEAD_F9361746E171` | spam | excluded | callback spam 13 Aug 12:02 MSK |
| `LEAD_C8D974B3429F` | spam | excluded | callback spam 13 Aug 12:02 MSK |
| `REMINDER_ACCEPTANCE_LEAD_2` before reopen | spam (10:15 snapshot exec `30821`) | was excluded | |
| `REMINDER_ACCEPTANCE_LEAD_2` now | pending via reopen | included | latest action `reopened`; spam history kept |
| Other historical spam / processed / synth closed | terminal on CLEAN | excluded | not returned by pending-first-wins |

Ordinary spam that was **not** reopened does **not** re-enter pending because an older mental model of “CLEAN once said pending”. Current `manager_status` is spam.

`LEAD_EVENTS` sheet: **SAFE_UNKNOWN** this run (quota). Callback execs `29992` (LEAD_2 original spam 13 Aug 10:40 MSK) and reopen record `manager_reopened` still corroborate CLEAN.

---

## 13. Reminder count expected tomorrow

If the 10 unique leads stay pending, **2026-08-15 10:00 Europe/Moscow** `Reminder Build Claims` will set:

`pending_count_snapshot = 10`

Message shape (`pending_count > 1`, existing contract — not sent here):

```
⏰ Напоминание о заявках

Необработанных заявок: 10
Старше суток: <n>
Самая старая: <age>

Посмотреть список: /pending_leads
```

- Count + optional age summary + `/pending_leads` pointer.
- **Not** a per-lead list in the reminder.
- **Not** one reminder per lead.
- One reminder per **recipient**; expected **4** claims / 4 Telegram attempts if ACCESS still has 4 active staff.

---

## 14. Next-window readiness

| Condition | Status |
|---|---|
| ≥1 genuine current pending | **yes** (10 unique) |
| `REMINDER_ACCEPTANCE_LEAD_2` pending | **yes** |
| Selector count truthful vs claimed 31 | **no** |
| Selector count truthful vs unique keys | **yes (10)** |
| Reminder recipients = 4 | **last proven yes** (CONFIG `pending_reminder_active_recipients_count=4` @ 12:00 MSK; 3H.8.2 ACCESS=4). Live ACCESS this checkpoint **quota-failed**. |
| No production sent-claim for `2026-08-15` | **last proven yes** (`pending_reminder_last_window` empty @ 12:00 MSK; `last_success` empty). Live ledger this checkpoint **quota-failed**. |

The real 10:00 window can still **send** (pending ≥ 1, lead 2 pending, day not stamped). It must **not** be scored against a pending_count of 31.

---

## 15. Soak state

`INTERRUPTED — REAL REMINDER WINDOW FAILED ON SHEETS 429`  
**Not restarted.**

---

## 16. Phase 3I.1 gate

**Blocked.** AI remains OFF. No soak. No reminder sent. No production status mutation.

---

## Sanitized matrices

### A. Unique selector set (tomorrow’s `pending_count`)

| # | Alias | Hash | Received (MSK) | CLEAN status | Last action | Last action at (UTC) | Test | Archive | Eligible | Class |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `LEAD_E57863B5A6A4` | E57863B5A6A4 | 2026-08-03 06:25 | pending | — | — | n | n | y | VALID_CURRENT_PENDING |
| 2 | `LEAD_A3F351F95AA7` | A3F351F95AA7 | 2026-08-03 11:52 | pending | — | — | n | n | y | VALID_CURRENT_PENDING |
| 3 | `LEAD_EA1CB88926DF` | EA1CB88926DF | 2026-08-04 10:50 | pending | — | — | n | n | y | VALID_CURRENT_PENDING |
| 4 | `LEAD_C3EF8E536C35` | C3EF8E536C35 | 2026-08-04 16:05 | pending | — | — | n | n | y | VALID_CURRENT_PENDING |
| 5 | `LEAD_791F70A6A4CF` | 791F70A6A4CF | 2026-08-04 17:06 | pending | — | — | n | n | y | VALID_CURRENT_PENDING |
| 6 | `LEAD_CFF5D644ED63` | CFF5D644ED63 | 2026-08-04 17:55 | pending | — | — | n | n | y | VALID_CURRENT_PENDING |
| 7 | `LEAD_08C4CF248F93` | 08C4CF248F93 | 2026-08-10 11:56 | pending | reopened | 2026-08-10T09:04:11Z | n | n | y | VALID_CURRENT_PENDING |
| 8 | `REMINDER_ACCEPTANCE_LEAD_2` | A6A0FB0DBFF6 | 2026-08-12 13:04 | pending | reopened | 2026-08-14T08:51:38Z | n | n | y | VALID_CURRENT_PENDING |
| 9 | `REMINDER_ACCEPTANCE_LEAD_1` | 3990BF2451B7 | 2026-08-12 22:30 | pending | reopened | 2026-08-13T10:22:23Z | n | n | y | VALID_CURRENT_PENDING |
| 10 | `LEAD_F4C9D9693444` | F4C9D9693444 | unknown | new→pending | — | — | n | n | y | VALID_CURRENT_PENDING |

Row 7 has historical `spam_at` (2026-08-10T09:03:00Z) then reopen; latest CLEAN action is reopen → pending is current, not stale spam.

### B. Naive 30 CLEAN rows (3H.8.2-style; inflated)

Same 10 identities; `LEAD_F4C9D9693444` ×6 (rows 29–34); `LEAD_C3EF8E536C35` ×16 (rows 45–60); plus eight singleton pending rows (39, 40, 44, 61, 62, 125, 129, 130).

---

## Counters

| Counter | Value |
|---|---|
| raw reminder candidate rows | 30 (naive pending∩not-test); 31 was the 3H.8.2 claim |
| unique business leads | 10 |
| valid current pending | 10 |
| stale pending projections | 0 (on CLEAN; events sheet unread) |
| terminal rows incorrectly eligible | 0 |
| test rows incorrectly eligible | 0 (unique set) |
| archive rows incorrectly eligible | 0 |
| duplicate business identities | 2 (20 extra CLEAN rows) |
| safe unknown | live `LEAD_EVENTS` + live ACCESS/ledger this snap (quota) |
| acceptance lead eligible | 1 (`REMINDER_ACCEPTANCE_LEAD_2`) |
| reminder recipients | 4 (last proven; live ACCESS unread) |
| next-date production claims | 0 (last proven; `last_window` empty) |
| mutations | 0 |
| reminders sent | 0 |
| AI state | OFF |

---

## System invariants (unchanged)

Ops 45 active · Admin 92 active · v2 inactive · reminder 10:00 Europe/Moscow · reporting manual · OpenRouter/customer auto-send not enabled this check · workflows created for production = 0.

Ephemeral TMP readers used for sheet GET were created and deleted; Admin.dev was not patched.

---

## Defect (do not patch in this checkpoint)

**`REPORTED_PENDING_31_IS_NOT_UNIQUE_BUSINESS_LEADS`**

- 3H.8.2 counted CLEAN pending∩not-test **rows**.
- Production `Reminder Build Claims` counts **unique keys** → **10**.
- Inflation is duplicate CLEAN representations, not stale Spam/Processed leakage.

Stop condition for this checkpoint: met. No selector patch, no extra reopens, no manual reminder.
