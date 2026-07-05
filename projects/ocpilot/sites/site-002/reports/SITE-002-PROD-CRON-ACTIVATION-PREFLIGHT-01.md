# REPORT — SITE-002 1C Cron Activation Preflight

**OCPilot run:** 4.180  
**Operation ID:** `SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01`  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-01`  
**Checkpoint after:** *(none — manual run not executed)*

---

## 1. Scope

Prepare MARS 1C import wrapper for first controlled manual run and future Beget cron activation.

**Allowed (compliance):** FTP read; upload one new local wrapper config; HTTP dry-run/status; read-only DB check; manual run plan; conditional single `--run` through wrapper only.  
**Forbidden (compliance):** Beget cron activation; legacy Sergey file edits; automatic import without passing all gates.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS\` — **PASS** |
| Volume | `X:` label `AI WS` — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD (start) | `d0518fb686c5bddfc0175a6501081ad5ce55ab50` |
| Staged files before task | **Empty** — **PASS** |
| Foreign WIP | Present elsewhere — **not staged, not touched** |

---

## 3. Legacy Sergey import preservation

| Rule | Status |
|------|--------|
| Legacy files edited | **0** |
| Legacy files deleted | **0** |
| Legacy files renamed | **0** |
| Legacy route replaced | **No** |
| Legacy Beget cron touched | **No** |
| `index.php?route=common/cronjob` invoked manually | **No** |

All existing import/cron implementation treated as **SERGEY LEGACY IMPORT — PRESERVE**.

---

## 4. Wrapper status

| Field | Value |
|-------|-------|
| Remote wrapper | `/storage/mars-tools/cron/mars_1c_import_wrapper.php` |
| Remote gateway | `/public_html/mars-tools/cron/mars_1c_http_gateway.php` |
| Version (HTTP dry-run) | **1.1.0** |
| SHA-256 (wrapper download) | `e991afb2b0202f622c7e6f1cbd627826f4cdef79fedc45b9e3054d337ae28b62` |
| SHA-256 (gateway download) | `59dced94134d71ba386bfba3b3cf3dc05ae677ac210c6186c4ea0b13a4095ffc` |
| Modes | dry-run · status · run (gated) |
| Hosting absolute root (dry-run) | `/home/a/assum/bzpm.ru/` |
| Server timezone (Run 4.179) | `Europe/Moscow` |

### HTTP verification

| Check | HTTP | mutation | Result |
|-------|------|----------|--------|
| dry-run | **200** | **false** | **PASS** |
| status | **200** | **false** | **PASS** |
| run (no token) | **403** | **false** | **PASS** |

Dry-run confirms: legacy files exist; `config.php` exists; lock not held; `run_token_configured: true`; `http_run_allowed: true`; catalog and offers XML present.

---

## 5. Local token config

| Field | Value |
|-------|-------|
| Remote path | `/storage/mars-tools/cron/mars_1c_wrapper.local.php` |
| State before operation | **Missing** |
| Action | **Created and uploaded** (first preflight pass) |
| Overwrite on re-check | **No** — EXISTS policy |
| Size on server | 445 bytes |
| Token in Git | **No** |
| Token in report | **No** — fingerprint only |
| Token fingerprint (SHA-256 prefix) | `7f113d` |
| Wrapper detects config | **Yes** (`run_token_configured: true` in dry-run) |
| `allow_http_run` | **true** (enables gated HTTP manual run for operator) |

Artefacts: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01\prepared\mars_1c_wrapper.local.php` (Storage only — **not committed**).

---

## 6. Read-only DB check

| Field | Value |
|-------|--------|
| Method attempted | SSH ephemeral PHP probe under `/storage/mars-tools/cron/` (SELECT only) |
| SSH from operator environment | **Reachable on second pass** (first local probe failed — network) |
| PHP CLI on SSH | **Failed** — `/usr/bin/php`, `/usr/bin/php7.4`, `/usr/bin/php8.1`, `/usr/bin/php8.2` all returned `PHP7.3+ Required` from OpenCart `startup.php` |
| Wrapper dry-run/status DB read | **Not available** — non-mutating modes do not query `cron` table |
| Live cron table state | **SAFE UNKNOWN** |

**Operator follow-up:** verify via Beget phpMyAdmin or SSH with PHP binary matching the site’s web PHP version (Beget panel → PHP settings). Required query pattern:

```sql
SELECT command, active, duration, lastrun FROM cron WHERE command IN ('1c', '1c_offers');
```

Expected before manual run: both rows exist; `active = 0` for each.

---

## 7. Input file check

| Pattern | Count | Files | Size (bytes) |
|---------|-------|-------|--------------|
| `import0_*.xml` | **1** | `import0_1.xml` | 7 422 785 |
| `offers0_*.xml` | **1** | `offers0_1.xml` | 3 532 791 |

Directory: `/public_html/1c_incoming/webdata/`  
XML contents: **not read** (metadata only).

**Note:** Run 4.178 recorded offers XML absent; Production now has `offers0_1.xml` — gate G8 **PASS**.

---

## 8. Manual run gates

| Gate | Description | Result |
|------|-------------|--------|
| G1 | Wrapper dry-run PASS | **PASS** |
| G2 | Wrapper status PASS | **PASS** |
| G3 | Run without token blocked | **PASS** |
| G4 | Local token config detected | **PASS** |
| G5 | DB cron rows known | **FAIL** — SAFE UNKNOWN |
| G6 | No `active=1` before run | **FAIL** — cannot verify without G5 |
| G7 | Catalog XML exists | **PASS** |
| G8 | Offers XML exists or safe skip | **PASS** (offers present) |
| G9 | Lock absent or stale | **PASS** |
| G10 | Reports/logs writable | **PASS** |
| G11 | No Beget cron change in this task | **PASS** |
| G12 | Maintenance window acceptable | **PASS** |

**Overall:** **FAIL** — manual run **not executed**.

**Verdict:** `MANUAL RUN BLOCKED — NO IMPORT EXECUTED`

---

## 9. Manual run result

| Field | Value |
|-------|-------|
| Import executions | **0** |
| Reason | Gates G5/G6 failed — live `cron` table state not verified |
| Retry | **Not attempted** (per charter) |

### Operator manual run plan (after DB verification)

1. Confirm `cron` rows for `1c` and `1c_offers` exist with `active = 0`.
2. Confirm no stale lock at `/storage/mars-tools/cron/mars_1c_import.lock`.
3. **Preferred:** Beget SSH with site PHP binary (confirm path in panel — default `/usr/bin/php` on SSH is **too old**):

```bash
/usr/bin/php /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php --run
```

4. **Alternative:** HTTP gateway with token (do not log full URL):

```text
https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php?mode=run&token=<run_token from mars_1c_wrapper.local.php>
```

5. Verify TXT report under `/storage/mars-tools/cron/reports/` and site HTTP 200.
6. Only then consider Beget cron activation (separate charter).

---

## 10. TXT report verification

| Field | Value |
|-------|-------|
| Run-mode TXT report | **N/A** — no manual run |
| Dry-run/status reports this session | **Created** (wrapper v1.1.0 behaviour confirmed) |
| Latest dry-run report (HTTP) | `mars_1c_import_dry_run_2026-07-05_205117.txt` |

---

## 11. HTTP/site verification

| URL | Status | Notes |
|-----|--------|-------|
| https://bzpm.ru/ | **200** | No fatal errors observed |
| https://bzpm.ru/katalog/ | **200** | Catalog reachable |
| Wrapper dry-run | **200** | mutation false |
| Wrapper status | **200** | mutation false |

---

## 12. Beget cron plan (NOT ENABLED)

| Field | Value |
|-------|-------|
| Activation | **Forbidden in this operation** |
| Server timezone | `Europe/Moscow` |
| Target business time | 12:00 Barnaul (UTC+7) |
| Recommended cron schedule (Moscow) | `0 8 * * *` |
| Preferred command | `/usr/bin/php /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php --run` |
| PHP CLI path on SSH | **SAFE UNKNOWN** — verify in Beget panel; web PHP meets 7.3+ |
| Log append variant | `... >> /home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_cron_stdout.log 2>&1` |
| Token in cron command | **Not required** — token in `mars_1c_wrapper.local.php` |
| Activation gate | Successful manual run + operator confirmation |

---

## 13. Rollback / disable plan

| Scenario | Action |
|----------|--------|
| Token config only (this run) | Leave config in place; or disable by removing/renaming `mars_1c_wrapper.local.php` **only with operator approval** |
| Future Beget cron | Disable row in Beget panel — do not delete Sergey legacy files or MARS wrapper |
| Manual run failure (future) | Use TXT report + `/storage/mars-tools/cron/logs/` — no automatic DB rollback |

---

## 14. Remote mutation summary

| Metric | Count |
|--------|------:|
| Remote uploads | **1** |
| Remote overwrites | **0** |
| Remote deletes | **0** |
| Remote renames | **0** |
| Remote directories created | **0** |
| Legacy Sergey files edited | **0** |
| Database SELECT operations | **0** (live state SAFE UNKNOWN) |
| Database write operations outside wrapper run | **0** |
| Import executions | **0** |
| Beget cron changes | **0** |
| Admin saves | **0** |
| Cache clears | **0** |

Ephemeral SSH probe file: uploaded and **removed** during DB check attempt (not counted as persistent remote change).

---

## 15. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01\`

| Subfolder | Contents |
|-----------|----------|
| `source/` | Downloaded wrapper + gateway |
| `prepared/` | `mars_1c_wrapper.local.php` (secrets — Storage only) |
| `manifests/` | operation.json, http-checks, gates, local-config, input-xml, token-meta |
| `db-readonly/` | Probe script + cron-table-readonly.json |
| `verification/` | *(no run report — import not executed)* |
| `manual-run/` | *(empty — blocked)* |

---

## 16. Authority updates

| Document | Updated |
|----------|---------|
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Run 4.180 entry |
| `projects/ocpilot/OCPILOT-STATE.md` | Run 4.180 summary |
| `projects/ocpilot/sites/site-002/production-profile.md` | Token config + pending manual run |
| `projects/ocpilot/sites/site-002/site-passport.md` | Token config status |
| `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | Activation preflight section |
| `projects/ocpilot/sites/site-002/tools/site-002-prod-cron-activation-preflight-01.py` | New helper |
| `projects/ocpilot/sites/site-002/tools/README.md` | Script index |

No new Production checkpoint (manual run not verified).

---

## 17. Git status

Scoped commit planned for repository docs/tools/report only. Storage artefacts and token config excluded.

---

## 18. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Live `cron` table `active` / `lastrun` | **SAFE UNKNOWN** — SSH PHP CLI too old for OpenCart bootstrap |
| Beget SSH PHP binary for CLI `--run` | **SAFE UNKNOWN** — confirm in hosting panel |
| Beget cron panel current state | **SAFE UNKNOWN** — not inspected (forbidden) |

**Blocker for manual run:** G5/G6 require live DB read — operator must verify via phpMyAdmin or correct PHP CLI before first `--run`.

---

## 19. Final verdict

**SITE-002 1C CRON ACTIVATION PREFLIGHT COMPLETE — TOKEN CONFIG READY / MANUAL RUN PENDING**

Token config deployed and verified. Wrapper gates G1–G4 and G7–G12 pass. Manual import **not executed** — blocked on live read-only DB verification (G5/G6). Beget cron **not activated**. Sergey legacy import **preserved**.
