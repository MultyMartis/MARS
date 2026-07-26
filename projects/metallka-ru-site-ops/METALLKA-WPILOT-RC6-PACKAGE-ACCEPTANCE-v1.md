# METALLKA — WPilot RC6 Package Acceptance v1

**Programme:** METALLKA-RU-SITE-OPS  
**Phase:** 4A acceptance · **4B revalidated at install**  
**Date:** 2026-07-26  
**Site:** `https://metallka.ru/`  
**Decision:** **ACCEPTED — SHA MATCH / SOURCE IDENTITY CONFIRMED** · **DEPLOYED ON METALLKA (Phase 4B)**

Phase 4A: no production contact / no package rebuild / no token.  
Phase 4B: SHA recheck **MATCH**; package installed via WP Admin upload.

---

## 1. Package identity

| Field | Value |
|-------|-------|
| Package path | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.0-rc6.zip` |
| Expected SHA-256 | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Actual SHA-256 (Phase 4A) | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Actual SHA-256 (Phase 4B recheck) | `4a0b929cee34e8c6188a10991b0c120bb1e8ffdd09674418a32d920c2aa16bf6` |
| Match | **YES** (4A and 4B) |
| Plugin header Version | **0.3.0** |
| RC label | **0.3.0-RC6** |
| Schema | **0.2.0** |
| REST namespace | `wpilot/v1` |
| Auth header | `X-WPilot-Token` |
| Accepted remediation commit | `27dfe624eec8b10b73e34c4a5f6df323258ecd1b` |
| Remediation commit ancestor of HEAD | **YES** |

---

## 2. ZIP structure

| Check | Result |
|-------|--------|
| Single root | **YES** — `metacode-wpilot/` only |
| File count | **27** |
| Nested duplicate plugin root | **NONE** |
| Path traversal / absolute paths | **NONE observed** |
| Unexpected executables | **NONE** |
| Secret / `.env` / local debris | **NONE** |
| Main bootstrap | `metacode-wpilot/metacode-wpilot.php` present |

### Inventory (27)

```text
metacode-wpilot/metacode-wpilot.php
metacode-wpilot/README.md
metacode-wpilot/admin/class-wpilot-admin-page.php
metacode-wpilot/admin/class-wpilot-admin-ui-model.php
metacode-wpilot/includes/class-wpilot-audit-service.php
metacode-wpilot/includes/class-wpilot-auth.php
metacode-wpilot/includes/class-wpilot-backup-service.php
metacode-wpilot/includes/class-wpilot-checksum.php
metacode-wpilot/includes/class-wpilot-connection-tracker.php
metacode-wpilot/includes/class-wpilot-constants.php
metacode-wpilot/includes/class-wpilot-dry-run.php
metacode-wpilot/includes/class-wpilot-environment.php
metacode-wpilot/includes/class-wpilot-errors.php
metacode-wpilot/includes/class-wpilot-operation-id.php
metacode-wpilot/includes/class-wpilot-plugin.php
metacode-wpilot/includes/class-wpilot-request-context.php
metacode-wpilot/includes/class-wpilot-response.php
metacode-wpilot/includes/class-wpilot-rest-controller.php
metacode-wpilot/includes/class-wpilot-rollback-service.php
metacode-wpilot/includes/class-wpilot-schema.php
metacode-wpilot/includes/class-wpilot-scoped-replace-service.php
metacode-wpilot/includes/class-wpilot-settings.php
metacode-wpilot/includes/class-wpilot-site-reader.php
metacode-wpilot/includes/class-wpilot-wpbakery-detector.php
metacode-wpilot/languages/metacode-wpilot-ru_RU.mo
metacode-wpilot/languages/metacode-wpilot-ru_RU.po
metacode-wpilot/languages/metacode-wpilot.pot
```

Matches accepted i-seo.su RC6 evidence file count (**27**).

---

## 3. Canonical source relationship

| Field | Value |
|-------|-------|
| Canonical source | `X:\AI MARS\projects\wpilot\plugin\metacode-wpilot\` |
| Source Version | **0.3.0** |
| Source RC | **0.3.0-RC6** (`WPilot_Constants::RELEASE_LABEL`) |
| Source schema | **0.2.0** |
| Byte identity vs ZIP | **27 / 27 exact SHA-256 match**; **0** source-only; **0** package-only |
| Rebuild required | **NO** |

Do **not** silently re-package under the RC6 filename/hash if source later diverges. Any material source change requires a new package release decision.

---

## 4. RC6 token-gating remediation evidence (source)

Confirmed in canonical source (and therefore in accepted ZIP):

| Behavior | Evidence |
|----------|----------|
| Token admin gate | `WPilot_Environment::can_manage_token()` — requires `manage_options`, valid environment, not emergency; **does not** require `dev_confirmed` / `bridge_enabled` / `write_enabled` |
| Admin handler | `generate_token` uses `can_manage_token()`, not `is_operationally_ready()` |
| Token persistence | `WPilot_Settings::generate_token()` updates only token-related fields |
| Activation defaults | `bridge_enabled=false`, `write_enabled=false`, `dev_confirmed=false` |

Programme references:

- `projects/wpilot/reports/REPORT-WPILOT-PRODUCTION-TOKEN-GATING-REMEDIATION.md`
- `projects/wpilot/reports/REPORT-WPILOT-PRODUCTION-TOKEN-GATING-REMEDIATION-PERSISTENCE.md`
- i-seo.su RC6 update + token-creation evidence (precedent only; not metallka proof)

---

## 5. Baseline policy

| Item | Rule |
|------|------|
| RC5 | Frozen proven DEV / historical production reference only — **not** metallka deployment baseline |
| RC6 | **Current accepted reusable deployment baseline** for metallka onboarding |
| Stale / mismatched ZIP | **STOP** — `BLOCKED — WPILOT RC6 PACKAGE HASH MISMATCH` |

---

## 6. Phase 4B revalidation requirement

Immediately before any production install, recompute SHA-256 of the same package path. If mismatch: **STOP** — do not install.

**Phase 4B result:** SHA recheck **MATCH**; package **INSTALLED** on metallka.ru (see installation evidence).

---

*METALLKA WPilot RC6 Package Acceptance v1 · ACCEPTED · Phase 4B DEPLOYED.*
