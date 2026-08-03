# OLYA MANAGER ACTION ACCEPTANCE v1

**Phase:** 3D.4  
**Subject:** Olya (hash **E6714550214106BA**) inline callback authorization

---

## 1. Enrollment confirmation

| Field | Value |
|-------|-------|
| CONFIG key | `manager_action_user_ids` |
| Olya enrolled | **yes** |
| Olya in `admin_user_ids` | **no** |
| Operator also on manager list | **yes** (hash **3FBE21323E22BFC1**) |
| CONFIG write | runtime enrollment **ok** |

---

## 2. Synthetic callback acceptance (harness)

Synthetic lead rows only — `SYNTHETIC_TEST` marker; no production business lead mutated for acceptance.

| Case | Actor hash | Transition | Outcome | Sheets | LEAD_EVENTS |
|------|------------|------------|---------|--------|-------------|
| Processed apply | E6714550214106BA | pending→processed | applied | mutate | `manager_marked_processed` |
| Processed idempotent | E6714550214106BA | repeat processed | idempotent | no duplicate | no duplicate row |
| Spam apply | E6714550214106BA | pending→spam | applied | mutate | `manager_marked_spam` |
| Conflict | E6714550214106BA | processed→spam | conflict | no change | conflict recorded |
| Unauthorized | (unknown) | any | unauthorized | no change | deny answer |

**Harness result:** synthetic callback matrix **PASS**.

---

## 3. Production stats exclusion

- All synthetic acceptance rows carry `SYNTHETIC_TEST` / harness fixture ids.
- `/stats` production rollup **excludes** synthetic rows (unchanged policy).
- No production `lifecycle_status` change attributed to Olya acceptance runs.

---

## 4. Live human checks (pending)

| Check | Status |
|-------|--------|
| Olya taps **✅ Отметить обработанным** on a real pending card | **PENDING** — operator to confirm after Olya reads manager `/start` |
| Olya taps **🚫 Отметить как спам** on a test card (if chartered) | **PENDING** |
| Olya live `/start` manager greeting | **PENDING** |
| Olya live `/help` manager help | **PENDING** |

Synthetic harness proves authorization wiring; human Telegram confirmation closes the handoff gate.

---

## 5. Expected live behavior (when Olya taps)

1. Callback answer toast confirms outcome (Russian).
2. Card message edited — keyboard cleared, lifecycle line shows ✅ or 🚫.
3. `lead_clean_v2` row updated (`lifecycle_status`, `manager_action_user_id` stamp).
4. `LEAD_EVENTS` append with actor reference (runtime only — not printed here).
5. No Gmail mutation, no client message, no Admin command side effects.

---

## 6. Forbidden during acceptance

- No real client lead used as a test without explicit charter.
- No enrollment of Olya into `admin_user_ids`.
- No automatic reply to clients triggered by callback.

---

*Related: OLYA-IDENTITY-RESOLUTION-v1 · PROCESSED-ACTION-ACCEPTANCE (phase3d3) · SPAM-ACTION-ACCEPTANCE (phase3d3).*
