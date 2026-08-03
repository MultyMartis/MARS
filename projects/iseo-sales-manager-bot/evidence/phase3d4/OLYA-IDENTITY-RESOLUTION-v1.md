# OLYA IDENTITY RESOLUTION v1

**Phase:** 3D.4  
**Date:** 2026-08-03  
**Classification:** operator-attested enrollment evidence (sanitized)

---

## 1. Purpose

Resolve the manager identity for PER-0010 (Оля) without printing raw Telegram identifiers in documentation or committed artifacts. The resolved identity is stored in CONFIG runtime only.

---

## 2. Resolution method

| Step | Action | Result |
|------|--------|--------|
| 1 | Olya sends `/start` to the Admin bot from a **private chat** | First observed update captured |
| 2 | Operator reviews n8n execution (Admin.dev) | Unique denied `/start` execution recorded |
| 3 | Identity hash computed from resolved `user_id` | **E6714550214106BA** |
| 4 | Compare against operator hash | **3FBE21323E22BFC1** — **distinct** |
| 5 | Enroll hash into CONFIG `manager_action_user_ids` only | Runtime write; not echoed in docs |

---

## 3. Evidence anchors (sanitized)

| Field | Value |
|-------|-------|
| Execution reference | Admin denied `/start` — exec **17177** (unique) |
| Chat type | private (not group/supergroup) |
| Olya identity hash | **E6714550214106BA** |
| Operator identity hash | **3FBE21323E22BFC1** |
| Same person? | **no** |
| Stored in CONFIG? | **yes** — `manager_action_user_ids` runtime only |
| Stored in git/docs? | **hash only** — no raw numeric ID |

---

## 4. Deny-before-enroll behavior

Before enrollment, Olya's `/start` correctly returned `Доступ запрещён.` — confirming:

- Trigger received the update;
- Authorization gate evaluated against `admin_user_ids` (not enrolled);
- No CONFIG leak of other identities;
- No Admin command surface exposed.

Post-enrollment, Olya remains **denied** for Admin text commands; only manager-action callbacks are authorized.

---

## 5. Constraints observed

- Raw Telegram `user_id` never printed in this pack or operator chat logs attached here.
- Enrollment did **not** add Olya to `admin_user_ids`.
- Identity resolution used operator-attested execution review, not client-side guesswork.

---

## 6. Pending human confirmation

Live Telegram confirmation from Olya for role-aware `/start` and `/help` (manager path) is **pending** — see `MANAGER-START-HELP-ACCEPTANCE-v1.md` and `PHASE3D4-ACCEPTANCE-RECEIPT-v1.md`.

---

*Related: ROLE-AUTHORIZATION-MODEL-v1 · ADMIN-REGRESSION-v1 · OLYA-MANAGER-ACTION-ACCEPTANCE-v1.*
