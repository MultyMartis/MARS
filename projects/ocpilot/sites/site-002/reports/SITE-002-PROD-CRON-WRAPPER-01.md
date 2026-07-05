# REPORT — SITE-002 Parallel 1C Import Cron Wrapper

**OCPilot run:** 4.178  
**Operation ID:** `SITE-002-PROD-CRON-WRAPPER-01`  
**Date:** 2026-07-06  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Baseline before:** `SITE-002-STABLE-PROD-SORT-MENU-ORDER-01`  
**Checkpoint after:** `SITE-002-STABLE-PROD-CRON-WRAPPER-01`

---

## 1. Scope

Prepare a **parallel** MARS 1C import cron wrapper on Production without modifying, replacing, or disabling Sergey legacy import flow.

**Allowed:** FTP read; legacy source download; new isolated MARS wrapper upload; dry-run/status HTTP verification.  
**Forbidden (compliance):** real import execution; DB mutation; Beget cron activation; legacy file edits.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS\` — **PASS** |
| Volume | `X:` label `AI WS` — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD (start) | `2f144335f4e7e83c48561258006b8a232970425c` |
| Staged files before task | **Empty** — **PASS** |
| Foreign WIP | Present elsewhere in monorepo — **not staged, not touched** |

---

## 3. Sergey legacy import preservation

| Rule | Status |
|------|--------|
| Legacy files edited | **0** |
| Legacy files deleted | **0** |
| Legacy files renamed | **0** |
| Legacy route replaced | **No** |
| Legacy Beget cron touched | **No** |
| `index.php?route=common/cronjob` invoked | **No** |

All existing import/cron implementation treated as **SERGEY LEGACY IMPORT — PRESERVE**.

---

## 4. Legacy import map

Full map: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-WRAPPER-01\legacy-map\`

| Component | Production evidence |
|-----------|---------------------|
| Route | `common/cronjob` → `catalog/controller/common/cronjob.php` |
| Model | `catalog/model/catalog/cronjob.php` — queries table `cron` |
| Catalog import | `import_1C.php` — `1c_incoming/webdata/import0_*.xml` |
| Offers import | `import_1C_offers.php` — `offers0_*.xml` + `refreshPriceIndex()` (**confirmed on Production**) |
| Process helper | `import_1C_process.php` |
| Manual reindex | `reindex_prices.php` |
| XML directory | `/public_html/1c_incoming/webdata/` — `import0_1.xml` present; no `offers0_*.xml` at capture |
| Lock in legacy | **None found** |
| Logs in legacy | OpenCart log writes only — no dedicated cron log file |

Production legacy files downloaded to `source/legacy/` with SHA-256 recorded in `sergey-legacy-import-files.json`.

---

## 5. Wrapper design

| Aspect | Design |
|--------|--------|
| Namespace | `/storage/mars-tools/cron/` (CLI primary) + HTTP gateway under `/public_html/mars-tools/cron/` |
| Legacy interaction | Run mode orchestrates Sergey flow via `cron.active` toggles + HTTP call to existing `common/cronjob` route |
| Modes | `dry-run` · `status` · `run` (gated) |
| Lock | `/storage/mars-tools/cron/mars_1c_import.lock` with stale lock handling (3600s) |
| Logs | `/storage/mars-tools/cron/logs/mars_1c_import_YYYYMMDD.log` |
| Max runtime | 2700s wrapper timeout for cronjob HTTP steps |
| Sequence | Step 1 `1c` → on success Step 2 `1c_offers`; offers skipped if catalog fails |
| PHP compatibility | PHP 7.x safe (no `never`, no `str_contains`) |
| Default on deploy | **dry-run safe** — run blocked without local config / token |

---

## 6. DB toggle strategy

**Recommended: Strategy A** — wrapper bootstraps OpenCart via `public_html/config.php`, sets `cron.active` flags, invokes legacy route twice, deactivates after each step.

| Strategy | Verdict |
|----------|---------|
| A — DB toggle + legacy route | **Recommended** — matches operator manual sequence; implemented in run mode |
| B — Direct include without toggles | **Not viable** — `getTasks()` requires `active=1` |
| C — Operator pre-sets flags | **Fallback only** — error-prone for daily cron |

**This operation:** Strategy A **designed and coded** in run mode — **not executed**. No DB reads/writes performed.

---

## 7. Files prepared

| File | Location |
|------|----------|
| `mars_1c_import_wrapper.php` | Storage deployment `prepared/` |
| `mars_1c_http_gateway.php` | Storage deployment `prepared/` |
| `index.html` (listing guard) | Storage deployment `prepared/` |
| `README-MARS-1C-CRON-WRAPPER.md` | Storage deployment `prepared/` |
| `site-002-prod-cron-wrapper-01.py` | `projects/ocpilot/sites/site-002/tools/` |

---

## 8. Upload / no-upload result

| Remote path | Action | SHA-256 (final) |
|-------------|--------|-----------------|
| `/storage/mars-tools/cron/mars_1c_import_wrapper.php` | **Uploaded** (+ PHP7 fix replace) | `17ebf7d2a262e5dc1e6c69a62a293ff8f94c20fa6fb1558780bb11da2e98ba61` |
| `/public_html/mars-tools/cron/mars_1c_http_gateway.php` | **Uploaded** | `59dced94134d71ba386bfba3b3cf3dc05ae677ac210c6186c4ea0b13a4095ffc` |
| `/storage/mars-tools/index.html` | **Uploaded** | listing guard |
| `/storage/mars-tools/cron/index.html` | **Uploaded** | listing guard |
| `/public_html/mars-tools/index.html` | **Uploaded** | listing guard |
| `/public_html/mars-tools/cron/index.html` | **Uploaded** | listing guard |

**Legacy Sergey paths:** untouched.

---

## 9. Verification

| Check | Result |
|-------|--------|
| Legacy file SHA at download | Recorded — no post-upload legacy re-download (read-only policy) |
| Wrapper FTP hash match | **PASS** |
| HTTP `?mode=dry-run` | **200** — `mutation: false`, legacy files exist, config.php exists |
| HTTP `?mode=status` | **200** — lock not held |
| HTTP `?mode=run` (no token) | **403** — `mutation: false` |
| Real import / cronjob route | **Not invoked** |

**Hosting path confirmed (dry-run):** `/home/a/assum/bzpm.ru/` — used for Beget cron command template below.

---

## 10. Beget cron plan (NOT ENABLED)

**Activation gate:** operator review + separate charter `SITE-002-PROD-CRON-BEGET-ACTIVATE-01`.

**Preferred CLI command:**

```bash
/usr/bin/php /home/a/assum/bzpm.ru/storage/mars-tools/cron/mars_1c_import_wrapper.php --run
```

Before first run, create `/storage/mars-tools/cron/mars_1c_wrapper.local.php` with `run_token` and optionally `MARS_1C_WRAPPER_ALLOW_CLI_RUN=1`.

**HTTP fallback (only if CLI unavailable):**

```bash
wget -q -O - "https://bzpm.ru/mars-tools/cron/mars_1c_http_gateway.php?mode=run&token=TOKEN"
```

Requires `allow_http_run => true` in local config.

**Disable:** remove Beget cron row for MARS wrapper only — leave Sergey legacy flow intact.

---

## 11. Timezone handling

**Target:** 12:00 Barnaul (UTC+7)

| Beget panel timezone | Schedule |
|----------------------|----------|
| Moscow (UTC+3) | `0 8 * * *` |
| UTC | `0 5 * * *` |
| Account/server local | **SAFE UNKNOWN** — verify in Beget panel |

---

## 12. Rollback / disable plan

1. Delete MARS wrapper files under `/storage/mars-tools/` and `/public_html/mars-tools/cron/` (gateway + index guards).
2. Remove Beget cron entry when/if created.
3. **Do not** delete or modify Sergey `cronjob` / `import_1C*` files.
4. Optional: remove `mars_1c_wrapper.local.php` if created later.

---

## 13. Remote mutation summary

| Metric | Count |
|--------|------:|
| Remote uploads | **6** (2 PHP + 4 index.html) |
| Remote overwrites | **1** (wrapper PHP7 compatibility fix — same operation) |
| Remote deletes | **0** |
| Remote renames | **0** |
| Legacy Sergey files edited | **0** |
| Database operations | **0** |
| Import executions | **0** |
| Beget cron changes | **0** |
| Admin saves | **0** |
| Cache clears | **0** |

---

## 14. Storage artefacts

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-WRAPPER-01\
  manifests\operation.json
  legacy-map\sergey-legacy-import-map.md
  legacy-map\sergey-legacy-import-files.json
  source\legacy\  (6 Sergey files)
  prepared\       (wrapper + README)
  verification\   (HTTP checks)
  logs\
```

Checkpoint storage:

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\baselines\SITE-002-STABLE-PROD-CRON-WRAPPER-01\
```

---

## 15. Authority updates

| Document | Updated |
|----------|---------|
| `OPERATIONAL-INDEX.md` | Run 4.178 |
| `OCPILOT-STATE.md` | SITE-002 cron wrapper state |
| `production-profile.md` | MARS wrapper + checkpoint |
| `site-passport.md` | Parallel cron wrapper note |
| `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` | §2 + Production checkpoint |
| `baselines/SITE-002-STABLE-PROD-CRON-WRAPPER-01.md` | **Issued** |
| `tools/README.md` | New script entry |

---

## 16. Git status

Scoped commit planned for OCPilot docs/tools/report/baseline only. Storage artefacts and downloaded legacy PHP **not** in git.

---

## 17. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Beget cron panel timezone | **SAFE UNKNOWN** |
| Production `cron` table rows (`duration`, `lastrun`, ids) | **SAFE UNKNOWN** — DB not read |
| Parser URL auth / IP restriction | **SAFE UNKNOWN** |
| Exact `/usr/bin/php` on Beget | **Assumed standard** — verify in panel |
| 1C XML drop time vs 12:00 Barnaul | **Operator confirmation required** |
| First real-run duration / timeout tuning | **Pending** maintenance-window dry-run |

**Blockers for cron activation (future):**

1. Operator creates `mars_1c_wrapper.local.php` with token.
2. Operator confirms Beget timezone → schedule mapping.
3. Operator authorizes DB read of `cron` table.
4. Operator approves one manual `--run` in maintenance window.
5. Separate charter for Beget cron row creation.

---

## 18. Final verdict

**SITE-002 MARS 1C CRON WRAPPER PREPARED — LEGACY IMPORT PRESERVED**

Parallel MARS wrapper deployed under isolated `mars-tools` paths. Dry-run and status verified over HTTP. Run mode gated (403 without config). Sergey legacy import untouched. **Beget cron activation pending operator approval.**

**Superseded by Run 4.179:** wrapper v1.1.0 adds human-readable TXT reports per run — see [SITE-002-PROD-CRON-RUN-REPORTS-01.md](SITE-002-PROD-CRON-RUN-REPORTS-01.md) · checkpoint `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-01`.
