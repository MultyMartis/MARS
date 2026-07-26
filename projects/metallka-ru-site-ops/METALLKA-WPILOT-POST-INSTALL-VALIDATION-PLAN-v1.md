# METALLKA — WPilot Post-Install Validation Plan v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4A — documentation only  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Related charter:** [METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md](METALLKA-WPILOT-INSTALLATION-ONBOARDING-CHARTER-v1.md)

```text
No validation against production is performed in Phase 4A.
Phase 4B validation must NOT call any WPilot REST endpoint.
```

---

## 1. Validation stages (Phase 4B order)

1. Pre-install absence + package SHA + backup posture  
2. Post-install / post-activation identity + safe defaults  
3. Post-token safe defaults + local token presence (metadata only in reports)  
4. Frontend smoke  
5. Admin smoke  
6. REST boundary confirmation (requests = 0)  
7. STOP  

---

## 2. Identity checks (after activation)

| Check | Expected |
|-------|----------|
| Plugin active | YES |
| Plugin Name | MetaCODE WPilot |
| Version header | `0.3.0` |
| RC evidence | `0.3.0-RC6` / RC6 visible in admin overview |
| Schema | `0.2.0` (admin schema valid expected) |
| Option `wpilot_options` | Present |
| Tables | `{prefix}wpilot_backups`, `{prefix}wpilot_audit_log` expected after activation |
| Automatic bridge enable | NO |
| Automatic write enable | NO |

---

## 3. Safe defaults

### After activation (before token)

| Key | Required |
|-----|----------|
| `bridge_enabled` | false |
| `write_enabled` | false |
| `dev_confirmed` | false |

Failure → **STOP** · no token · rollback Case C.

### After token creation

Same three must remain **false**.  
Token exists (admin + local file) = YES.  
REST calls = 0.

Failure → rollback Case E.

---

## 4. Frontend smoke (bounded)

| URL | Expect |
|-----|--------|
| `https://metallka.ru/` | HTTP 200; no visible fatal/warning; header/footer intact |
| `https://metallka.ru/about/` | HTTP 200; no fatal; content readable (CHANGE 0001 page) |
| Representative service page e.g. `https://metallka.ru/services/remont-otverstij/` | HTTP 200; no fatal |
| `https://metallka.ru/contacts/` | HTTP 200; no fatal |

Do **not**: submit forms · purge cache · edit content · open WPilot REST.

---

## 5. WP Admin smoke (bounded)

| Surface | Expect |
|---------|--------|
| Dashboard | Loads; no fatal |
| Plugins page | Loads; MetaCODE WPilot listed active |
| Page **52** editor / WPBakery | Opens; no fatal; no forced migration/setup |
| WPilot settings/admin | Opens read-only for validation if needed |

Do **not**: edit page content · submit unrelated settings · enable bridge/write · generate extra tokens.

---

## 6. REST boundary checklist

Confirm and record:

| Item | Required |
|------|----------|
| `/wp-json/wpilot/v1/ping` | **NOT CALLED** |
| Other `wpilot/v1` endpoints | **NOT CALLED** |
| Token auth test | **NOT PERFORMED** |
| Public namespace may appear after activation | Observation only — **do not** exercise |

---

## 7. Success / fail labels

| Result | Label |
|--------|-------|
| All checks pass | Phase 4B success per installation charter |
| Safe default failure | `ROLLED BACK — WPILOT SAFE DEFAULT FAILURE` |
| Post-token default failure | `ROLLED BACK — WPILOT POST-TOKEN SAFE DEFAULT FAILURE` |
| Frontend/admin regression | Rollback Case F |

---

## 8. Explicitly deferred to Gate E

- Bridge enable  
- Authenticated reads  
- Connection tracking via REST  
- Any write / backup / dry-run / scoped-replace / rollback endpoint  

Future approval (not this wave):

```text
APPROVE METALLKA WPILOT GATE E — BRIDGE AND READ-ONLY REST SMOKE
```

---

*METALLKA WPilot Post-Install Validation Plan v1 · Phase 4A preparation only.*
