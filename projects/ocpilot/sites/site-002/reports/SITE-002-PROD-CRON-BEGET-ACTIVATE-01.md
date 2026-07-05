# REPORT — SITE-002 Beget 1C Cron Activation

**OCPilot run:** 4.182  
**Operation ID:** `SITE-002-PROD-CRON-BEGET-ACTIVATE-01`  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01`  
**Checkpoint after:** *(none — Beget cron row not created in this operation)*

---

## 1. Scope

Final activation charter for daily Beget cron targeting the MARS 1C import wrapper via HTTP gateway.

**Allowed:** non-mutating wrapper HTTP checks; SSH timezone probe; FTP read for manual-run report metadata; cron command preparation (token in Storage only); operator panel instructions; scoped OCPilot docs.  
**Forbidden:** legacy Sergey file edits; manual import execution; direct legacy URL; Beget cron change without panel access; token exposure in Git/reports.

**Operator approval (this task):** activate Beget cron · MARS wrapper · HTTP gateway · preserve Sergey legacy · schedule 12:00 Barnaul.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS\` — **PASS** |
| Volume | `X:` label `AI WS` — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
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
| Direct `common/cronjob` outside wrapper | **No** |

All existing import/cron implementation remains **SERGEY LEGACY IMPORT — PRESERVE**.

---

## 4. Wrapper readiness recheck

| Check | HTTP | mutation | Result |
|-------|------|----------|--------|
| dry-run | **200** | **false** | **PASS** |
| status | **200** | **false** | **PASS** |
| run (no token) | **403** | **false** | **PASS** |

| Field | Value |
|-------|-------|
| Wrapper version | **1.1.0** |
| Local config detected | **Yes** (`run_token_configured: true`) |
| Token fingerprint | `7f113d` (no token value in report) |
| Lock held | **No** |
| Reports path writable | **Yes** (dry-run wrote report) |
| Logs path writable | **Yes** |
| Latest manual run report | **Yes** — `mars_1c_import_2026-07-05_205934.txt` |
| Legacy files changed | **0** |

---

## 5. Beget cron state inspection

| Method | Result |
|--------|--------|
| Beget control panel (cp.beget.com) | **Not accessible from Cursor** — panel login required |
| SSH `crontab -l` | **Unavailable** — `crontab: command not found` on shared hosting SSH |
| SSH timezone probe | **MSK +0300** · `/etc/timezone` → `Europe/Moscow` |

| Question | Answer |
|----------|--------|
| Existing bzpm.ru cron row visible via SSH? | **No** — crontab CLI absent |
| Row calling `common/cronjob`? | **SAFE UNKNOWN** (panel not inspected) |
| Row calling `import_1C.php` / `import_1C_offers.php`? | **SAFE UNKNOWN** |
| Row calling `mars_1c_http_gateway.php`? | **No** (SSH probe) · panel **SAFE UNKNOWN** |
| Panel timezone shown? | **SAFE UNKNOWN** — server timezone **Europe/Moscow** confirmed |
| Command format wget/curl/php accepted? | **Assumed yes** (Beget standard) — HTTP gateway proved in Run 4.181 |

**Note:** Beget panel cron is authoritative. Operator must inspect panel for any existing legacy import rows before saving the new MARS row.

---

## 6. Cron command preparation

**Sanitized template (for documentation):**

```text
wget -q -O - "https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php?mode=run&token=<TOKEN_FROM_LOCAL_CONFIG>" >> /home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_cron_stdout.log 2>&1
```

| Field | Value |
|-------|-------|
| Channel | HTTP gateway (proved in Run 4.181) |
| Token source | `/storage/mars-tools/cron/mars_1c_wrapper.local.php` |
| Token fingerprint | `7f113d` |
| Actual command with token | Storage only — `deployments/SITE-002-PROD-CRON-BEGET-ACTIVATE-01/cron-command/beget-cron-command.ACTUAL.SECRET.txt` |
| Committed to Git | **No** |

---

## 7. Cron schedule

| Field | Value |
|-------|-------|
| Target business time | **12:00 Barnaul** (UTC+7) |
| Server timezone (confirmed) | **Europe/Moscow** (MSK +0300) |
| Recommended Beget schedule | **`0 8 * * *`** |
| If panel uses UTC | `0 5 * * *` |
| If panel allows Asia/Barnaul | `0 12 * * *` |

Rationale: previous wrapper runs and SSH probe show **Europe/Moscow**; 08:00 Moscow = 12:00 Barnaul.

---

## 8. Activation gates

| Gate | Description | Result |
|------|-------------|--------|
| G1 | Wrapper readiness PASS | **PASS** |
| G2 | Local token config exists | **PASS** |
| G3 | Run without token blocked | **PASS** |
| G4 | Manual run Run 4.181 SUCCESS documented | **PASS** |
| G5 | No legacy cron conflict (SSH probe) | **PASS** · panel **SAFE UNKNOWN** |
| G6 | No duplicate MARS cron (SSH probe) | **PASS** · panel **SAFE UNKNOWN** |
| G7 | Schedule resolved | **PASS** |
| G8 | Command prepared; token not exposed | **PASS** |
| G9 | Operator approval recorded | **PASS** |
| G10 | Beget action path available | **PASS** (panel URL in secrets; operator HITL) |

**Overall gates:** **PASS** for activation readiness — **panel save not performed by agent**.

---

## 9. Beget cron activation

| Field | Value |
|-------|--------|
| Activation performed by agent | **No** — Beget panel not programmatically accessible |
| Cron rows created | **0** |
| Cron rows edited | **0** |
| Cron rows deleted | **0** |
| Import triggered | **0** |

### Operator panel steps (HITL required)

1. Open [Beget control panel](https://cp.beget.com/) → Cron for account/site **bzpm.ru**.
2. **Inspect** existing cron rows. If any row targets `common/cronjob`, `import_1C.php`, or `import_1C_offers.php` — **do not change automatically**; report to operator charter.
3. Create **exactly one** new row:
   - **Name/description:** `SITE-002 MARS 1C Import Wrapper`
   - **Schedule:** `0 8 * * *` (if panel uses Moscow/server time)
   - **Command:** copy from Storage `beget-cron-command.ACTUAL.SECRET.txt` (contains real token — **not in Git**)
4. **Skip** optional immediate test run if panel offers it (avoids duplicate import).
5. Save and proceed to post-activation verification below.

---

## 10. Post-activation verification

**Status in this operation:** **NOT PERFORMED** — cron row not created by agent.

### Operator verification checklist (after panel save)

1. Exactly **one** MARS cron row exists (or one verified if pre-existing exact match).
2. Schedule = `0 8 * * *` (Moscow) or equivalent for 12:00 Barnaul.
3. Command targets `mars_1c_http_gateway.php` — **not** `common/cronjob` / `import_1C.php` / `import_1C_offers.php`.
4. Command includes `token=` parameter (do not share token in tickets).
5. Stdout/stderr append: `/home/a/assum/bzpm.ru/storage/mars-tools/cron/logs/beget_cron_stdout.log`
6. Do **not** manually trigger import during verification.
7. After first natural scheduled run: check TXT report under `/storage/mars-tools/cron/reports/` and `beget_cron_stdout.log`.

---

## 11. Disable / rollback plan

| Scenario | Action |
|----------|--------|
| **Disable daily import** | Beget panel → disable or delete row **SITE-002 MARS 1C Import Wrapper** (gateway URL only) |
| **Do not delete** | MARS wrapper files · Sergey legacy import files · TXT reports/logs |
| **Emergency disable** | Duplicate runs · repeated FAIL reports · lock stuck · catalog errors after import · server load |

| Wrong row created | Remove **only** the operation-created wrong row in same panel session; document row removed; do not touch legacy rows |

No automatic rollback in this operation.

---

## 12. Remote / external mutation summary

| Metric | Count |
|--------|------:|
| Remote file uploads | **0** |
| Remote file overwrites | **0** |
| Remote deletes | **0** |
| Remote renames | **0** |
| Legacy Sergey files edited | **0** |
| Database operations | **0** |
| Import executions in this operation | **0** |
| Direct legacy URL executions | **0** |
| Beget cron rows created | **0** |
| Beget cron rows edited | **0** |
| Beget cron rows deleted | **0** |
| Admin saves | **0** |
| Cache clears | **0** |

---

## 13. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-BEGET-ACTIVATE-01\`

| Subfolder | Contents |
|-----------|----------|
| `manifests/` | operation.json, http-checks, activation-gates, operation-summary, ftp-roots |
| `beget/` | cron-state-inspection.json, operator-panel-instructions.json |
| `cron-command/` | TEMPLATE.txt, ACTUAL.SECRET.txt (token), token-fingerprint.json |
| `reports/` | manual-run-report-meta.json |
| `verification/` | *(pending post-operator panel save)* |

---

## 14. Checkpoint

**Not issued** — Beget cron active state not verified in this operation.

After operator completes panel save and verification, issue:

- `SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01`

---

## 15. Authority updates

| Document | Updated |
|----------|---------|
| `projects/ocpilot/OPERATIONAL-INDEX.md` | Run 4.182 entry |
| `projects/ocpilot/OCPILOT-STATE.md` | Activation ready summary |
| `projects/ocpilot/sites/site-002/production-profile.md` | Cron activation state |
| `projects/ocpilot/sites/site-002/site-passport.md` | Cron activation state |
| `projects/ocpilot/sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | § Beget activation |
| `projects/ocpilot/sites/site-002/tools/site-002-prod-cron-beget-activate-01.py` | New helper |
| `projects/ocpilot/sites/site-002/tools/README.md` | Script index |

---

## 16. Git status

Scoped commit for OCPilot docs/tools/report only. Storage artefacts, token, and actual cron command excluded.

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Beget panel existing cron rows | **SAFE UNKNOWN** — operator must inspect panel before save |
| Beget panel timezone label | **SAFE UNKNOWN** — use `0 8 * * *` if Moscow/server time |
| Cron activation via Cursor/API | **Blocked** — no programmatic Beget cron API |
| SSH crontab inspection | **Unavailable** — `crontab` not on shared hosting SSH |

**No blockers for operator panel activation** — all wrapper gates PASS; command and schedule prepared.

---

## 18. Final verdict

**SITE-002 BEGET 1C CRON ACTIVATION READY — OPERATOR PANEL ACTION REQUIRED**

Wrapper readiness recheck **PASS**. Manual run Run 4.181 **SUCCESS** confirmed. HTTP gateway command and schedule `0 8 * * *` (Moscow → 12:00 Barnaul) prepared with token fingerprint `7f113d`. Sergey legacy import **preserved**. No import executed in this operation. Beget cron row **not created** — operator must complete panel steps in §9 and verify per §10.
