# METALLKA — WPilot Production Confirmation Semantics v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4C-R0 — Gate E Retry Charter (documentation / source-semantics only)  
**Date:** 2026-07-26  
**Production:** `https://metallka.ru/`  
**Source root:** `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` (RC6 / 0.3.0 / schema 0.2.0)  
**Status:** **SOURCE-GROUNDED**  
**Production mutations this wave:** **NONE**  
**REST requests this wave:** **0**

```text
No tokens, credentials, Authorization / X-WPilot-Token values, or plaintext secrets are recorded here.
```

---

## 1. Verdict (production use of `dev_confirmed`)

**SAFE WITH CONDITIONS**

`dev_confirmed` is **not** an environment detector (“this host is development”).  
It is an **operator checkbox gate** required by `WPilot_Environment::operational_readiness()` for authenticated REST.

The admin label still asserts DEV/test / “not production”. That wording is **historical / misleading** for metallka production, but the **technical mechanism** is a durable confirmation prerequisite. A separate operational charter may authorize setting it on production for controlled read connectivity, with writes independently gated.

Exact conditions: see §10 and the Gate E Retry Charter.

---

## 2. Declaration, default, read, write

| Aspect | Source evidence |
|--------|-----------------|
| **Declared** | Option key `dev_confirmed` in `WPilot_Settings::defaults()` (`includes/class-wpilot-settings.php`) |
| **Default** | `false` |
| **Activation reset** | `WPilot_Settings::activate()` forces `dev_confirmed = false` (also bridge/write false) |
| **Deactivation** | Does **not** clear `dev_confirmed`; clears bridge/write only |
| **Read (boolean)** | `WPilot_Environment::dev_confirmed()` — `! empty( $options['dev_confirmed'] )` |
| **Read (readiness)** | `WPilot_Environment::operational_readiness()` fails with `dev_not_confirmed` if false |
| **Read (state label)** | `WPilot_Settings::get_state()` → `enabled-without-dev-confirmation` when bridge on and flag false |
| **Written** | Admin action `save_bridge` in `WPilot_Admin_Page` sets `$options['dev_confirmed']` from POST checkbox, then `WPilot_Settings::update_options( $options, true )` |
| **Sanitize** | `sanitize_options()` casts to bool; does **not** auto-clear `bridge_enabled` when confirmation is false (admin save path enforces coupling — see §6) |

Code comments / labels:

- `WPilot_Environment::dev_confirmed` docblock: *“operator confirmed DEV/test use”*
- `WPilot_Constants::DEV_LABEL` = `'DEV/test'`
- Plugin header Description: *“DEV/test WPilot bridge…”*

---

## 3. Admin control — exact operator-facing text

**Form:** Bridge Control → `wpilot_action=save_bridge`  
**Checkbox name:** `dev_confirmed`  
**Label (exact):**

> I confirm this is a DEV/test WordPress site, not production.

**Overview / status labels:**

- Column: `DEV Confirmation` / `DEV/test confirmed`
- Values via `WPilot_Admin_UI_Model::dev_confirmed_label()`: `confirmed` / `not confirmed`

**Adjacent production notice (exact intent):**

> Production prohibition: If this WordPress site is production or production-like, leave the bridge and writes disabled until a separate operational charter authorizes them. Token generation alone does not enable the bridge or writes.

That notice **explicitly contemplates** charter-authorized bridge use on production-like sites.

---

## 4. Semantic classification (A / B / C)

| Option | Meaning | Fits source? |
|--------|---------|--------------|
| **A** | “This is a development environment” (auto / factual) | **NO** — not detected from host; operator checkbox only |
| **B** | “Operator explicitly confirmed controlled WPilot operation on this site” | **YES functionally** — required confirmation gate for operational REST |
| **C** | Other | Partially — UI text frames confirmation as “DEV/test … not production” (naming debt) |

**Authoritative functional meaning for metallka programme:** **B**, with **historical naming/labeling from A**.

Do **not** infer meaning from the variable name alone. Do **not** treat checking the box as a factual claim that metallka.ru is non-production.

---

## 5. Operational readiness

### 5.1 `WPilot_Environment::operational_readiness()`

Requires, in order:

1. `environment_valid` — keys present: `bridge_enabled`, `dev_confirmed`, `emergency_disabled`, `write_enabled`
2. `emergency_disabled` = false
3. `bridge_enabled` = true
4. `dev_confirmed` = true

Returns `true` or a safe error envelope (`SAFE_UNKNOWN` / `EMERGENCY_DISABLED` / `BRIDGE_DISABLED` / `DEV_NOT_CONFIRMED`).

### 5.2 Related methods

| Method | Role |
|--------|------|
| `is_operationally_ready()` | Same boolean gates (no emergency + bridge + confirmation); for non-REST admin flows needing a live bridge |
| `can_manage_token()` | Admin + non-emergency + valid options; **does not** require confirmation, bridge, or write |
| `write_disabled()` | `empty( write_enabled )` |
| `snapshot()` | Exposes bridge/dev/emergency/write for response meta |

### 5.3 Capability matrix (compact)

| Concern | Requirements (RC6 source) |
|---------|---------------------------|
| REST route **registration** | Plugin active; routes always registered (no readiness gate at register time) |
| Public `/ping` | Always; `permission_callback` = `__return_true`; no token / bridge / confirmation |
| Authenticated **reads** | `operational_readiness` + valid token (`WPilot_Auth::require_read_access`) |
| Bridge “availability” for auth REST | Same as operational readiness |
| Write / dry-run / rollback / scoped-replace | Readiness + token + **`write_enabled`** (see write isolation) |
| Backup create | Readiness + schema + token; **does not** require `write_enabled` |
| Token generate / rotate / revoke | `can_manage_token` only |

### 5.4 Truth table — `dev_confirmed` / `bridge_enabled` / `write_enabled`

Assume `emergency_disabled=false`, options valid, token present where auth matters.

| # | dev | bridge | write | Token mgmt | Auth reads | Writes (content/dry-run/rollback/scoped) | Intended posture |
|---|-----|--------|-------|------------|------------|------------------------------------------|------------------|
| 1 | F | F | F | YES | NO | NO | Safe idle (metallka current) |
| 2 | T | F | F | YES | NO (`BRIDGE_DISABLED`) | NO | Confirmation only; bridge off |
| 3 | T | T | F | YES | YES (with token) | NO | **Read-connected** (Gate E retry target) |
| 4 | T | T | T | YES | YES | YES (plus endpoint-specific gates) | Write-ready (forbidden for Gate E retry) |

Notes:

- Admin `save_bridge` forces `bridge = dev && bridge_checkbox` and `write = dev && bridge && write_checkbox`. A bridge checkbox with `dev_confirmed` unchecked **persists bridge=false**.
- State `#2` is reachable if confirmation is saved without bridge checkbox.
- State with `dev=false` and `bridge=true` is **not** produced by the supported admin save path.

---

## 6. Admin persistence (`save_bridge`)

Exact RC6 logic:

```php
$options['dev_confirmed']  = $dev_confirmed;
$options['bridge_enabled'] = $dev_confirmed && $bridge_enabled;
$options['write_enabled']  = $dev_confirmed && $bridge_enabled && $write_enabled;
WPilot_Settings::update_options( $options, true );
```

| Question | Answer |
|----------|--------|
| Bridge checkbox alone while `dev_confirmed=false`? | Persists **`bridge_enabled=false`** |
| Enable confirmation + bridge in **one** save? | **YES** — check both; leave write unchecked |
| Two saves required? | **NO** for read-ready state |
| `write_enabled` independent? | Operator checkbox independent, but AND-gated with confirmation + bridge; `sanitize_options` also requires those for write=true |
| `allow_write_enable=true` on this save? | **YES** — so an accidental write checkbox **would** persist write readiness |
| Unrelated options / token? | `update_options` merges into current options; token hash and connection fields preserved unless overwritten |
| Connection metadata? | Preserved on bridge save (not cleared by this action) |

---

## 7. Public `/ping` HTTP 200

| Fact | Source |
|------|--------|
| Intentionally public | `permission_callback` => `__return_true` |
| No token required | Handler does not call `WPilot_Auth` |
| Limited status only | Returns plugin slug, `status=installed`, `bridge_enabled`, `write_enabled`, `state`; meta includes bridge snapshot without requiring auth |
| Differs from authenticated reads | Read routes use `read_permission_callback` returning true at WP level, but handlers call `guard_read()` → `require_read_access()` |
| HTTP 200 meaning | **Plugin present + route reachable** — **not** authenticated readiness |
| Connection metadata mutation on public ping? | **NONE** — read options only; no `Connection_Tracker`, no `last_token_used_at` |

**Programme rule:** Do not treat public `/ping` 200 as proof of authenticated WPilot connectivity.

**Note:** There is **no** separate authenticated `/ping` handler. Token proof for Gate E retry is the authenticated GET set (`site-info`, `themes`, `plugins`, `pages`). Calling `/ping` with a token header still uses the public handler.

---

## 8. Write isolation — read-only target state

Target: `dev_confirmed=true`, `bridge_enabled=true`, `write_enabled=false`.

| Gate | Behavior |
|------|----------|
| Dry-run | `require_dry_run_access` → `WRITE_DISABLED` if write false |
| Rollback / scoped-replace | `require_rollback_access` / `require_scoped_replace_access` → require write after backup access |
| Content mutation endpoints | Same write gate |
| **Backup** | `require_backup_access` — readiness + schema + token; **no `write_enabled` check** — can mutate **plugin backup storage** even when write is false |

**Therefore:** `write_enabled=false` **does not** authorize content writes, but **does not** by itself make backup safe to call. Gate E retry must **forbid** backup / dry-run / scoped-replace / rollback / all POST write routes.

Authenticated GET side effects (not content writes):

- `last_token_used_at`
- connection tracker: status / success_at / authorized_at / authorized_endpoint
- auth failure timestamps/reasons on failed auth

IP / user-agent: built in `WPilot_Request_Context::build()` but **stripped** from `response_meta()`; **not** persisted by connection tracker on reads. Audit table inserts occur on write/backup/dry-run style handlers — **not** on the read GET handlers listed for retry.

---

## 9. Variable naming — technical debt (upstream recommendation only)

| Issue | Detail |
|-------|--------|
| Name | `dev_confirmed` implies environment class |
| Admin label | Asserts “DEV/test … not production” |
| Product reality | Operator confirmation required for **any** authenticated operational REST, including intended production Site Ops |
| Recommendation (non-binding) | Rename flag/labels to operator confirmation (e.g. `operator_confirmed` / “I authorize controlled WPilot operation on this site”) in a future WPilot release; keep boolean gate semantics |

**This task does not modify WPilot source.**

---

## 10. Conditions for production authorization (SAFE WITH CONDITIONS)

1. Operator issues the exact Gate E retry approval string (see Retry Charter).
2. Operator explicitly accepts that checking `dev_confirmed` means **controlled WPilot operation confirmation**, not a claim that metallka is non-production.
3. Mutation limited to confirmation + bridge enable; **`write_enabled` remains false**.
4. Existing token preserved; no regenerate/revoke.
5. Authenticated smoke = GET allowlist only; no backup/write/dry-run/rollback/scoped-replace.
6. Evidence sanitized; no token/secrets in tracked docs.
7. Failure rollback restores confirmation + bridge + write to pre-retry false/false/false.

---

## 11. Cross-references

- [METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md](METALLKA-WPILOT-GATE-E-RETRY-CHARTER-v1.md)
- [METALLKA-WPILOT-GATE-E-READ-SMOKE-EVIDENCE-v1.md](METALLKA-WPILOT-GATE-E-READ-SMOKE-EVIDENCE-v1.md)
- [reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R0-GATE-E-RETRY-CHARTER.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-4C-R0-GATE-E-RETRY-CHARTER.md)

---

*Production Confirmation Semantics v1 · SAFE WITH CONDITIONS · documentation only · no production mutation.*
