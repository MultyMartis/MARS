# REPEATED START ANTI-WIPE v1

**Phase:** 3G.2.3

---

## Contract

Repeated `/start` and `/my_status` must preserve:

- `reply_profile_number`
- `reply_sender_name`
- `reply_sender_enabled`
- `reply_company_name`
- no blanking of active profile fields
- no duplicate ACCESS_CONTROL rows

Mechanism (unchanged from 3G.2.2, reaffirmed):

- `rowFromSheet` includes reply-profile columns
- last_seen upsert uses `rehydrateReplyProfile` / `mergeRehydrateIntoUpsert`
- Upsert mapping includes all `reply_*` columns

---

## Offline proof

Harness checks #5–#6, #8–#10 **PASS** (`phase3g23-harness.mjs`).

Live window (sanitized): exec 24097 rehydrate-upsert restored MOD_A name; 24098 and 24100 read **Михаил** with no duplicate-row signal.

## Operator matrix (acceptance pending)

MOD_A: `/start` → `/start` → `/my_status` → `/my_reply_profile`  
ADMIN_A: `/start` → `/my_status` → `/my_reply_profile` → `/reply_profiles`
