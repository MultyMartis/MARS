# METALLKA — WPilot Gate E Read Smoke Evidence v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4C — WPilot Gate E bridge + read-only REST smoke  
**Date:** 2026-07-26  
**Production:** `https://metallka.ru/`  
**Status:** **BLOCKED — CURRENT RC6 READ GATE REQUIRES DEV_CONFIRMATION NOT AUTHORIZED BY GATE E**

```text
No tokens, credentials, Authorization / X-WPilot-Token header values, or plaintext secrets are recorded here.
```

---

## 1. Operator authorization received

Exact string:

```text
APPROVE METALLKA WPILOT GATE E — BRIDGE AND READ-ONLY REST SMOKE
```

Scope of approval (as chartered): first controlled production WPilot REST connectivity / **read-only** smoke.  
**Does not** authorize WPilot write operations, token regeneration, or casual `dev_confirmed` toggle.

---

## 2. Preflight (session)

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume `X:` label | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `f6cae2e8111617420f3395ebe2459be0783e7eaa` |
| `origin/mars/canonical-post-recovery` | `dc1fa5c48255efd8819b1947408d82f67bf020ca` (local HEAD ahead; no commit/push in this task) |
| Staged | **empty** |
| Foreign WIP | Present elsewhere — **untouched** |
| Token file exists | **YES** — `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` |
| Token gitignored | **YES** — `.gitignore` rule `/local/` |

---

## 3. Source-level gate review (RC6 authority)

Source root inspected: `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` (accepted as byte-identical to metallka / i-seo RC6).

### 3.1 Authenticated read gate

`WPilot_Auth::require_read_access()` → `WPilot_Environment::operational_readiness()`.

`operational_readiness()` requires **all** of:

1. environment option keys present;
2. `emergency_disabled` = false;
3. `bridge_enabled` = true;
4. **`dev_confirmed` = true**.

If `dev_confirmed` is false while bridge is on, response is **`DEV_NOT_CONFIRMED`** (HTTP **403**) via `WPilot_Errors::dev_not_confirmed()`.

**Verdict:** `bridge_enabled=true` **alone is NOT sufficient** for authenticated read REST.

### 3.2 Admin settings surface (supported mutation path)

`WPilot_Admin_Page` action `save_bridge`:

```php
$options['bridge_enabled'] = $dev_confirmed && $bridge_enabled;
$options['write_enabled']  = $dev_confirmed && $bridge_enabled && $write_enabled;
```

Therefore, enabling **only** the bridge checkbox with `dev_confirmed` unchecked persists **`bridge_enabled=false`**.  
A supported “bridge-only” save that leaves `dev_confirmed=false` **cannot** produce a live bridge for REST.

### 3.3 Write gate (not exercised)

Write / dry-run / backup / rollback / scoped-replace paths additionally require `write_enabled` (and readiness).  
Gate E **did not** call any write endpoint. `write_enabled` remained **false** by design; write capability execution = **NOT TESTED**.

### 3.4 Public `/ping` (unauthenticated)

`GET /wp-json/wpilot/v1/ping` uses `permission_callback` `__return_true` and does **not** require token / bridge / `dev_confirmed`. It exposes non-secret bridge snapshot fields only.

### 3.5 Connection metadata side effects (source)

Authenticated successful reads update `last_token_used_at` and connection tracker fields.  
**Not observed** in this Gate E wave because authenticated REST was **not** executed.

### 3.6 Programme / WPilot precedent

WPilot token-gating remediation reports explicitly record:

> REST still requires `dev_confirmed` after bridge enable — Intentional; production bridge enable charter must address DEV semantics separately.

`dev_confirmed` remains a literal **DEV/test** assertion — **not** reinterpreted as generic production confirmation without a separate charter.

---

## 4. STOP decision

Per Gate E charter §5:

> If source requires `dev_confirmed=true` for read connectivity, STOP before production mutation and report:  
> **BLOCKED — CURRENT RC6 READ GATE REQUIRES DEV_CONFIRMATION NOT AUTHORIZED BY GATE E**  
> Do NOT infer authorization to toggle `dev_confirmed`.

**Action taken:** **STOP before any bridge / settings mutation.**

| Intended Gate E mutation | Executed? |
|--------------------------|-----------|
| `bridge_enabled` false → true | **NO** |
| `dev_confirmed` false → true | **NO** (not authorized) |
| `write_enabled` change | **NO** |
| Token create/regenerate | **NO** |
| Authenticated REST GETs | **NO** |
| Write REST | **NO** |

---

## 5. Pre-bridge production revalidation (read-only; no settings change)

### 5.1 Public frontend

| URL | HTTP |
|-----|------|
| `/` | **200** |
| `/about/` | **200** |
| `/services/` | **200** |
| `/services/tokarnye-raboty/` | **200** |
| `/contacts/` | **200** |
| `/wp-json/` | **200** |

### 5.2 Public WPilot `/ping` (no token; no mutation)

Captured: `X:\AI MARS STORAGE\wpilot\evidence\metallka-ru-site-ops\phase-4c-gate-e\public-ping-no-token.json`

Sanitized summary:

| Field | Value |
|-------|-------|
| HTTP | **200** |
| `data.plugin` | `metacode-wpilot` |
| `data.status` | `installed` |
| `data.bridge_enabled` | **false** |
| `data.write_enabled` | **false** |
| `data.state` | `disabled` |
| `meta.auth_state` | `not-required` |
| `meta.bridge_state_snapshot.dev_confirmed` | **false** |
| `meta.bridge_state_snapshot.emergency_disabled` | **false** |

### 5.3 REST namespace registration (index only)

`GET /wp-json/wpilot/v1` → **200**; routes present include `/ping`, `/site-info`, `/themes`, `/plugins`, `/pages` (and write routes registered but **not called**).

### 5.4 Consistency with Phase 4B / FIX01 baseline

| Field | Expected | Observed (public) |
|-------|----------|-------------------|
| WPilot installed/active | YES | YES (ping + namespace) |
| bridge | false | false |
| write | false | false |
| `dev_confirmed` | false | false |
| Token file local | YES | YES (path only; value not read into evidence) |

No unexpected baseline drift requiring STOP-for-anomaly beyond the structural `dev_confirmed` gate block.

---

## 6. Authenticated smoke — NOT EXECUTED

| Endpoint | Status |
|----------|--------|
| `GET /wpilot/v1/ping` with `X-WPilot-Token` | **NOT RUN** |
| `GET /wpilot/v1/site-info` | **NOT RUN** |
| `GET /wpilot/v1/themes` | **NOT RUN** |
| `GET /wpilot/v1/plugins` | **NOT RUN** |
| `GET /wpilot/v1/pages` | **NOT RUN** |

| Proof claim | Result |
|-------------|--------|
| Token authentication | **NOT PROVEN** |
| Read-only REST smoke | **NOT PROVEN** |
| Connection tracking | **NOT OBSERVED** |
| WPilot writes | **BLOCKED** (unchanged) |

---

## 7. Final bridge posture

**OFF** — no enable attempted (structural Gate E block).

Preferred post-smoke ON/OFF choice **N/A** (smoke not reached).

---

## 8. Counters

| Counter | Count |
|---------|-------|
| Bridge enable operations | **0** |
| Bridge disable operations | **0** |
| Token generations | **0** |
| Token modifications | **0** |
| Authenticated REST GET | **0** |
| Public unauthenticated `/ping` | **1** (state revalidation only) |
| REST namespace index GET | **1** (route confirmation only) |
| REST non-GET | **0** |
| WPilot write requests | **0** |
| Content mutations | **0** |
| DB direct writes | **0** |
| Filesystem production writes | **0** |
| Cache purges | **0** |
| Plugin/theme/core changes | **0** |
| Git staged | **0** |
| Secrets in tracked evidence | **0** |

---

## 9. What Gate E proved / did not prove

**Proven this wave:**

- RC6 source read gate requires `dev_confirmed` **in addition to** bridge.
- Supported admin save cannot enable bridge without `dev_confirmed`.
- Gate E approval string alone does **not** authorize `dev_confirmed`.
- Public metallka WPilot remains installed; safe defaults still OFF.

**Still not proven:**

- Token authentication on metallka  
- Authenticated `/ping` / site-info / themes / plugins / pages  
- Production bridge connectivity  
- Write paths, backup, dry-run, scoped-replace, rollback  

---

## 10. Recommended next human charter (not started)

A future charter must **explicitly** decide production semantics for `dev_confirmed` (or a successor production-confirmation model), then authorize the exact settings toggles required for read smoke. Do **not** silently reinterpret DEV/test as production approval.

Suggested follow-up labels (operator-owned):

1. **PHASE 4C-R / Gate E-R** — charter for production confirmation semantics + bridge enable + read smoke; **or**  
2. WPilot product change — production readiness flag separate from DEV/test label (out of metallka ops scope unless separately chartered).

---

*Gate E evidence v1 · BLOCKED before production bridge mutation · 2026-07-26.*
