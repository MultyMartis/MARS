# METALLKA — WPilot RC6 Installation Evidence v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4B — production install / activate / token  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Status:** **COMPLETE — WPILOT RC6 INSTALLED / ACTIVE / TOKEN CREATED / REST NOT RUN**

```text
Token plaintext is NEVER recorded in this artefact.
```

### Historical / baseline note (Phase 4B-FIX01 — 2026-07-26)

This artefact remains the **immutable Phase 4B install evidence**. It is **not failed** and is **not rewritten**.

Phase 4B-FIX01 re-checked live `i-seo.su` WPilot CODE and found production identity **`0.3.0-RC6`**, byte-identical to this same accepted package and to metallka’s installed tree. Operator concern that RC6 was a stale baseline vs a newer i-seo build was **not confirmed** by production files. See [METALLKA-WPILOT-CURRENT-BASELINE-RECONCILIATION-v1.md](METALLKA-WPILOT-CURRENT-BASELINE-RECONCILIATION-v1.md) and [METALLKA-WPILOT-FIX01-UPDATE-EVIDENCE-v1.md](METALLKA-WPILOT-FIX01-UPDATE-EVIDENCE-v1.md).

As a **deployment-baseline assumption**, “RC6 because Phase 4B chose it” is superseded by “RC6 because i-seo production currently runs it (FIX01-proven)”. The install event itself stays historically complete.

---

## 1. Operator authorization

| Confirmation | Received |
|--------------|----------|
| `CONFIRM METALLKA FRESH BEGET BACKUP FOR WPILOT INSTALL` | **YES** |
| `APPROVE METALLKA WPILOT INSTALL — RC6 INSTALL ACTIVATE TOKEN ONLY` | **YES** |

Backup posture: operator-attested fresh Beget full backup. No agent panel restore/create performed.

---

## 2. Package

| Field | Value |
|-------|-------|
| Filename | `metacode-wpilot-v0.3.0-rc6.zip` |
| Path | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| Expected SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Actual SHA-256 (Phase 4B recheck) | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Match | **YES** |
| Remediation commit (accepted) | `27dfe624eec8b10b73e34c4a5f6df323258ecd1b` |

---

## 3. Pre-install WPilot state

| Check | Result |
|-------|--------|
| Production host | `metallka.ru` / admin site name «МЕТАЛЛКА» |
| WP Admin login | **OK** |
| Plugins page lists WPilot | **NO** |
| Plugin directory `metacode-wpilot` (SSH) | **ABSENT** |
| Ghost `*wpilot*` plugin paths | **NONE** |
| Active WPilot plugin | **ABSENT** |
| Option `wpilot_options` | **ABSENT** |
| WPilot tables | **ABSENT** |
| Public `/wp-json/` namespace `wpilot/v1` | **ABSENT** |

---

## 4. Installation / activation

| Field | Value |
|-------|--------|
| Surface | WP Admin → Plugins → Upload Plugin |
| Install timestamp (UTC) | `2026-07-26T14:38:49Z` |
| Activation timestamp (UTC) | `2026-07-26T14:38:54Z` |
| Plugin directory | `wp-content/plugins/metacode-wpilot/` |
| Active | **YES** |
| Version header | **0.3.0** |
| Schema (admin overview) | **0.2.0** |
| RC identity | Accepted RC6 package SHA + source constants `0.3.0-RC6` / `RC6` (localized overview did not echo English RC string; package+version+schema establish identity) |
| Installations | **1** |
| Activations | **1** |
| SSH/FTP fallback | **NOT USED** |

---

## 5. Safe defaults

### Before token

| Key | Observed |
|-----|----------|
| `bridge_enabled` | **false** (checkbox unchecked) |
| `write_enabled` | **false** (checkbox unchecked) |
| `dev_confirmed` | **false** (checkbox unchecked) |

### After token

| Key | Observed |
|-----|----------|
| `bridge_enabled` | **false** |
| `write_enabled` | **false** |
| `dev_confirmed` | **false** |

Automatic bridge/write/dev enable: **NOT observed**.

---

## 6. Token (metadata only)

| Field | Value |
|-------|-------|
| Token created | **YES** |
| Tokens created count | **1** |
| Persisted local-only | **YES** |
| Path | `X:\AI MARS\local\tokens\wpilot-prod-metallka-ru.token` |
| Gitignored | **YES** (`.gitignore` `/local/`) |
| Token leaked to tracked evidence | **NO** |
| REST authentication test | **NOT RUN** |

See [METALLKA-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md](METALLKA-WPILOT-TOKEN-CREATION-EVIDENCE-v1.md).

---

## 7. REST boundary

| Item | Value |
|------|-------|
| `/wp-json/wpilot/v1/*` requests | **0** |
| Bridge enable operations | **0** |
| Write enable operations | **0** |
| WPilot content writes | **0** |

Public `/wp-json/` index was read **once pre-install** for namespace absence only (not a WPilot endpoint call).

---

## 8. Regression smoke

### Frontend

| URL | HTTP | Fatal | Pass |
|-----|------|-------|------|
| `https://metallka.ru/` | 200 | NO | **PASS** |
| `https://metallka.ru/about/` | 200 | NO | **PASS** |
| `https://metallka.ru/services/remont-otverstij/` | 200 | NO | **PASS** |
| `https://metallka.ru/contacts/` | 200 | NO | **PASS** |

### WP Admin

| Surface | Result |
|---------|--------|
| Dashboard | **PASS** |
| Plugins (WPilot active) | **PASS** |
| WPilot admin page | **PASS** |
| Page ID 52 editor + WPBakery UI | **PASS** (no save) |

---

## 9. Rollback

| Field | Value |
|-------|-------|
| Required | **NO** |
| Executed | **NO** |
| Case | n/a |

---

## 10. Raw evidence (sanitized)

`X:\AI MARS STORAGE\wpilot\evidence\metallka-ru-site-ops\phase-4b-wpilot-rc6-install\`

- `execution-result.json` (no token plaintext)
- `preinstall-ssh.json`
- `post-install.png`
- `phase4b_wpilot_rc6_install.py`

---

*METALLKA WPilot RC6 Installation Evidence v1 · Phase 4B COMPLETE.*
