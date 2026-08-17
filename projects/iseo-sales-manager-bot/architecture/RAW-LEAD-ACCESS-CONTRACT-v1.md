# RAW LEAD ACCESS CONTRACT v1.0

**Contract id:** `iseo-raw-lead-access-v1.0`  
**Phase:** 3H.9  
**Status:** documented + Admin.dev patched (deny-text / failure-class distinction)

## Staff set (do not broaden)

Authorized **active** production staff may view the raw/original submission for production leads they are permitted to work with:

- ADMIN_A
- MOD_A
- MOD_B
- MOD_C

No per-card ownership restriction is part of this contract. The fact that a Telegram card instance was delivered to another recipient does **not** by itself make raw text inaccessible to otherwise authorized staff.

## Callback

- Action: `📄 Исходная заявка`
- `callback_data`: `sm:i:<action_token>`
- Lifecycle: **no status change**, no reminder claims, no pending-count mutation, no reminder window mark

## Operator-facing results

| Condition | Text |
|---|---|
| Unauthorized / inactive staff | `Недостаточно прав.` |
| Authorized; original payload record missing | `Исходная заявка для этого лида не найдена.` |
| Lead does not resolve in working registry | existing safe not-found wording |
| ACCESS/CONFIG registry read failed (quota, credentials, transport) | `Сервис временно недоступен. Попробуйте позже.` — **not** a permission deny |
| Transient RAW read failure | existing temporary-unavailable wording |
| Empty original body | may display empty; not itself a bot defect |

Do not leak internal IDs, sheet names, or OAuth details in Telegram.

## Explicit non-goals

- Do not change raw payload semantics (literal source).
- Do not fabricate missing source data.
- Do not treat missing payload as insufficient permissions.
