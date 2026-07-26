# METALLKA — WPilot Gate E Retry Charter v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4C-R0 — Gate E Retry Charter preparation  
**Date:** 2026-07-26  
**Production:** `https://metallka.ru/`  
**Status:** **PREPARED — RETRY NOT AUTHORIZED**  
**Execution phase:** PHASE 4C-R1 — **NOT STARTED**  
**Semantics authority:** [METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md](METALLKA-WPILOT-PRODUCTION-CONFIRMATION-SEMANTICS-v1.md)

```text
No tokens, credentials, Authorization / X-WPilot-Token values, or plaintext secrets are recorded here.
```

---

## 1. Why original Gate E blocked

Original approval:

```text
APPROVE METALLKA WPILOT GATE E — BRIDGE AND READ-ONLY REST SMOKE
```

RC6 `WPilot_Environment::operational_readiness()` requires **`dev_confirmed=true`** in addition to `bridge_enabled=true` for authenticated reads. Gate E text did **not** authorize toggling `dev_confirmed`. Admin save also forces `bridge = confirmation && bridge_checkbox`, so a bridge-only save cannot create a live bridge.

**Outcome:** STOP before mutation. Production unchanged. Authenticated REST = **0**.

---

## 2. `dev_confirmed` source semantics (summary)

| Item | Finding |
|------|---------|
| Functional role | Operator confirmation gate for authenticated operational REST |
| Not | Automatic “is development host” detector |
| Admin label | “I confirm this is a DEV/test WordPress site, not production.” |
| Production notice | Bridge/writes stay off on production-like sites **until a separate operational charter authorizes them** |
| Production verdict | **SAFE WITH CONDITIONS** (see semantics doc) |

Naming is historically misleading; **do not** reset the flag after successful smoke merely because of the name.

---

## 3. Operational readiness truth table

| dev | bridge | write | Token mgmt | Auth reads | Content writes | Posture |
|-----|--------|-------|------------|------------|----------------|---------|
| F | F | F | YES | NO | NO | Current / rollback target |
| T | F | F | YES | NO | NO | Confirmation only |
| T | T | F | YES | YES | NO | **Retry read-smoke target** |
| T | T | T | YES | YES | YES | Write-ready — **forbidden** |

Public `/ping` works in all rows (presence only).

---

## 4. Public `/ping` 200 explanation

Public `GET /wp-json/wpilot/v1/ping` uses `__return_true`, returns limited non-secret status, and does **not** prove token auth or operational readiness. Phase 4C public ping 200 only proved plugin presence while flags were off.

Retry must not treat public ping 200 as authenticated connectivity proof. Auth proof = successful authenticated GETs below.

---

## 5. Exact future settings mutation (4C-R1 only, after approval)

### BEFORE (current)

| Flag | Value |
|------|-------|
| `dev_confirmed` | `false` |
| `bridge_enabled` | `false` |
| `write_enabled` | `false` |
| token | **preserved** |

### READ-SMOKE STATE (intended)

| Flag | Value |
|------|-------|
| `dev_confirmed` | `true` |
| `bridge_enabled` | `true` |
| `write_enabled` | `false` |
| token | **preserved** (no create / rotate / revoke) |

### Supported mutation path

**ONE** WP Admin WPilot `Save Bridge State` (`save_bridge`):

1. Check **DEV confirmation** checkbox (`dev_confirmed`)
2. Check **Enable authenticated REST bridge**
3. Leave **write readiness** unchecked
4. Submit once

Minimum save count: **1**. No other settings delta.

---

## 6. Authenticated REST scope (maximum)

Confirmed from `WPilot_REST_Controller::register_routes()` — GET only:

| Method | Path | Auth gate |
|--------|------|-----------|
| GET | `/wp-json/wpilot/v1/ping` | Public (state snapshot; optional in smoke) |
| GET | `/wp-json/wpilot/v1/site-info` | `require_read_access` |
| GET | `/wp-json/wpilot/v1/themes` | `require_read_access` |
| GET | `/wp-json/wpilot/v1/plugins` | `require_read_access` |
| GET | `/wp-json/wpilot/v1/pages` | `require_read_access` |

**Forbidden:** POST / PUT / PATCH / DELETE; backup; dry-run; scoped-replace; rollback; any write endpoint; page mutation; token regeneration; guessed routes (including `/pages/{id}` and `/indexing-state` unless a later charter expands GET allowlist).

Header for authenticated GETs: `X-WPilot-Token` (existing local metallka token only).

---

## 7. Data minimization (evidence)

| Endpoint | Persist only |
|----------|--------------|
| ping | status / readiness fields |
| site-info | operational metadata (URLs, versions, flags) |
| themes | name / status / version (active theme fields) |
| plugins | name / status / version |
| pages | minimal inventory (id, title, status, modified, link, has_wpbakery) — **no `post_content`** |

Do not export private data. Do not expose token. Do not commit secrets.

---

## 8. Expected connection / audit side effects

| Effect | Expected on auth GET success? | Classification |
|--------|-------------------------------|----------------|
| `last_token_used_at` | YES | Inherent operational metadata |
| Connection status / success / authorized timestamps / endpoint label | YES | Inherent operational metadata |
| Auth failure fields | Only on auth failure | Inherent operational metadata |
| Audit table rows | **NO** for listed GETs | N/A |
| Persisted IP / UA | **NO** (response meta strips; tracker does not store them) | N/A |
| Content / unrelated options | **NO** | Forbidden if observed |

These metadata updates may be explicitly authorized as side effects of read connectivity. They are **not** site content writes.

---

## 9. Write isolation reminder

`write_enabled=false` blocks dry-run / rollback / scoped-replace content paths.  
**Backup is not write-gated** — still **forbidden** in this retry.

---

## 10. Preferred final state after successful read smoke

**MODEL A — persistent read-connected state**

| Flag | Value |
|------|-------|
| `dev_confirmed` | `true` |
| `bridge_enabled` | `true` |
| `write_enabled` | `false` |

**Rationale:** Confirmation is a durable operational prerequisite (not a one-shot env claim). Bridge remains the intended agent connectivity path while writes stay independently disabled. Resetting confirmation solely due to the `dev_*` name would fight product design and programme intent.

**MODEL B** (conservative reset all three to false) is **not** preferred after success; use only as **failure rollback**.

Do **not** execute final-state policy in 4C-R0.

---

## 11. Failure rollback

If retry fails after settings mutation:

Restore:

| Flag | Value |
|------|-------|
| `dev_confirmed` | `false` |
| `bridge_enabled` | `false` |
| `write_enabled` | `false` |

Preserve: plugin installed, plugin active, existing metallka token.

Do **not** uninstall WPilot for read-smoke failure alone unless the plugin itself causes site regression.

Validate after rollback: frontend, WP Admin, token existence, safe flags.

---

## 12. Retry success conditions

COMPLETE only if all hold:

1. `dev_confirmed` semantics explicitly accepted (SAFE WITH CONDITIONS).
2. Minimum settings mutation applied (confirmation + bridge; write false).
3. `write_enabled` remains false throughout.
4. Token preserved (no regenerate).
5. Authenticated `site-info`, `themes`, `plugins`, `pages` succeed.
6. Public or token-bearing `/ping` may be used for state snapshot only — auth proof is the four authenticated GETs.
7. No write / backup / dry-run / scoped-replace / rollback requests.
8. No content changes.
9. Only expected connection/token-used metadata side effects.
10. Frontend / admin healthy.
11. Final state matches **MODEL A**.

---

## 13. Required approval (future 4C-R1)

Verdict permits defining this string. **Not yet granted.**

```text
APPROVE METALLKA WPILOT GATE E RETRY — SET PRODUCTION CONFIRMED + BRIDGE / READ-ONLY REST ONLY
```

### Authorizes

- Exact minimum supported settings mutation to read readiness
- `dev_confirmed=true` as operator confirmation gate (despite DEV/test label)
- `bridge_enabled=true`
- `write_enabled` remains false
- Existing token only
- Authenticated GET smoke (allowlist above)
- Inherent connection / `last_token_used_at` metadata side effects
- Rollback of those flags if required

### Does **not** authorize

- `write_enabled`
- Write endpoints, backup, dry-run, scoped replace, rollback endpoint
- Content changes
- Token regeneration
- Unrelated settings changes
- Auto-start of Phase 4D writes

---

## 14. Phase sequencing

| Phase | Status |
|-------|--------|
| 4C Gate E | **BLOCKED** (historical) |
| **4C-R0** this charter | **COMPLETE — PREPARED / RETRY NOT AUTHORIZED** |
| 4C-R1 execution | **NOT STARTED** — waits for approval string |
| 4D writes | **BLOCKED** |

---

*Gate E Retry Charter v1 · PREPARED — RETRY NOT AUTHORIZED · no production mutation.*
