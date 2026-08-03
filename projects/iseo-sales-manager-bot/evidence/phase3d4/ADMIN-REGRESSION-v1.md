# ADMIN REGRESSION v1

**Phase:** 3D.4  
**Scope:** post-enrollment Admin command and allowlist regression

---

## 1. Allowlist counts (`/config` safe summary)

| Metric | Expected | Observed |
|--------|----------|----------|
| Administrators (`admin_user_ids`) | **1** | **1** |
| Managers with callback access (`manager_action_user_ids`) | **2** | **2** |
| Olya in admin list | **no** | **no** |
| Olya in manager list | **yes** | **yes** |

Manager list composition (hashes only):

| Hash | Role |
|------|------|
| 3FBE21323E22BFC1 | admin + manager (operator) |
| E6714550214106BA | manager only (Olya) |

---

## 2. Admin command regression matrix

| Command | Operator (admin) | Olya (manager only) |
|---------|------------------|---------------------|
| `/start` | Admin panel | Manager greeting (harness PASS; live PENDING) |
| `/help` | Full Admin list | Manager help (harness PASS; live PENDING) |
| `/status` | PASS | **deny** |
| `/config` | PASS | **deny** |
| `/leads` | PASS | **deny** |
| `/stats` | PASS | **deny** |
| `/health` | PASS | **deny** |
| `/ai_status` | PASS | **deny** |
| `/ai_on` | PASS (charter) | **deny** |
| `/ai_off` | PASS | **deny** |
| Callback processed | PASS | **PASS** (synthetic) |
| Callback spam | PASS | **PASS** (synthetic) |
| Callback unauthorized | deny | deny |

---

## 3. CONFIG keys unchanged (except enrollment)

| Key | Change this phase |
|-----|-------------------|
| `admin_user_ids` | **no change** (count stays 1) |
| `manager_action_user_ids` | **yes** — Olya added |
| `ai_enabled` | false (unchanged) |
| `environment` | production (unchanged) |
| `parser_version` | sm-parser-v3.2 |
| `message_format_version` | sm-msg-v2.1 |

---

## 4. Workflow regression

| Check | Result |
|-------|--------|
| Admin.dev active | PASS |
| Operational.dev active | PASS |
| Sales-Manager-v2 inactive | PASS |
| New workflows created | **0** |
| Admin node count | 42 (unchanged) |
| Operational node count | 36 (unchanged) |

---

## 5. Stats / error path

- `/stats` still excludes `SYNTHETIC_TEST`.
- `/last_error` no new open production errors from enrollment patch.
- AI calls during regression window: **0**.

---

*Related: ROLE-AUTHORIZATION-MODEL-v1 · OLYA-IDENTITY-RESOLUTION-v1 · PHASE3D4-ACCEPTANCE-RECEIPT-v1.md.*
