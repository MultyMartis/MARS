# REPORT — iSEO Sales Manager Bot Google Sheets 429 Repair v1

Generated: 2026-09-01T07:36:00Z  
Target: VEESP-N8N-01 (`https://n8n.ai-metacode.com`) · n8n 2.14.2  
Prior diagnostic: [REPORT-iseo-sales-manager-bot-google-sheets-degraded-diagnostic-v1.md](./REPORT-iseo-sales-manager-bot-google-sheets-degraded-diagnostic-v1.md)

## 1. Verdict

**PARTIAL — QUOTA PRESSURE REDUCED BUT 429 REMAINS**

Workflow-side repairs deployed to **Operational.dev** only reduced specific read sources and stopped error-path Gmail re-intake amplification. Natural post-fix observation still shows **HTTP 429** on every execution in the final observation window. **PASS** (`post-fix 429 = 0`) is **not** claimed.

Preferred full PASS verdict was **not** achieved:

> `GOOGLE SHEETS 429 REPAIR PASS — REQUEST PRESSURE NORMALIZED — PRODUCTION HEALTHY`

## 2. Pre-fix quota state

| Signal | Value |
|--------|------:|
| Google error | HTTP **429** |
| Quota metric | `Read requests per minute per user` |
| Service | `sheets.googleapis.com` |
| Consumer | `project_number:173364893180` |
| Credential | `nRfNJVn6SEziII8k` (Multy Martis) |
| Forensic window | 45 min (`2026-09-01T06:04:26Z` → observe end) |
| Operational.dev executions | 90 (~2.0/min) |
| Operational.dev approx reads/min | **~10.49** (sampled node runs) |
| Operational.dev 429 sampled | **80** |
| Empty Gmail polls (lead route) | **0** |
| Execution success (Operational.dev) | **0** in degraded window |

Evidence: `evidence/current-stabilization/google-sheets-429-repair/pressure-summary.json`, prior diagnostic §5.

## 3. Active workflow request-pressure inventory

**Active workflows sharing credential `nRfNJVn6SEziII8k`:** **5**

| Workflow | Active | Exec/min | Read nodes / exec (design) | Approx reads/min | 429 sampled | Credential |
|---|---:|---:|---:|---:|---:|---|
| i-SEO Sales Manager - Operational.dev | yes | ~2.0 | 12 nodes (4 explicit read) | **~10.49** | **80** | nRfNJVn6SEziII8k |
| SEO Content Agent Beta.v14 - Admin | yes | ~0.16 | 5 | ~0.27 | 0 | nRfNJVn6SEziII8k |
| i-SEO Sales Manager - Admin.dev | yes | ~0.13 | 27 | ~0.27 | 0 | nRfNJVn6SEziII8k |
| SEO Content Agent Beta.v14 - Worker | yes | 0 | 9 | 0 | 0 | nRfNJVn6SEziII8k |
| SEO Content Agent Beta.v14 - Intake | yes | ~0.16 | 3 | 0 | 0 | nRfNJVn6SEziII8k |

**Conclusion:** Pressure is dominated by **Operational.dev** under stuck-lead re-intake, not inactive workflow inventory. Admin.dev and other active workflows are negligible contributors in the same window.

Evidence: `pressure-summary.json`, `active-workflows-with-credential.json`.

## 4. Operational.dev call graph

Forensic classification of 90 consecutive Operational.dev executions (same 45 min window):

| Route | Count | Typical Sheets nodes | Pattern |
|---|---:|---:|---|
| Lead (Gmail work present) | **90** | 2 or 11 | Alternating early vs full path |
| Empty poll | **0** | — | Not observed in window |

**Answers (with node-path evidence):**

1. **Does `Read CONFIG` run every cron/poll?**  
   **Yes** pre-fix on every classified lead execution (`readConfig: true` on all 90 rows). Post-fix Wave 2+: skipped when 5-minute workflow static cache is fresh.

2. **Does it run when Gmail returns no new lead?**  
   **Not testable in window** — zero empty polls. All 90 executions were **lead route** (same stuck message re-polled).

3. **Sheets read requests on a normal empty poll?**  
   **N/A** (0 empty polls). Pre-fix design would still hit CONFIG + early append path when lead mail exists.

4. **Sheets requests on one actual lead?**  
   - **Early fail path:** ~**2** node runs (`Append RAW v2` + `Read CONFIG`), often stopping at CONFIG 429 (`sheetsNodeCount: 2`, `readConfig429: true`).  
   - **Full path:** ~**11** node runs through DEDUP/CLEAN/ACCESS/RAW before downstream 429 (`sheetsNodeCount: 11`).

5. **Can CONFIG be read only when needed?**  
   **Partially yes** — deployed **CONFIG Route Prep** + **CONFIG Cache IF** (5 min TTL) skips `Read CONFIG` when cache fresh. CONFIG is still required for lead processing semantics; deferral does not remove lead-path reads.

6. **Repeated sheet reads within one execution?**  
   **Yes** on full path: `Lookup DEDUP_INDEX`, `Read ACCESS_CONTROL`, `Read LEAD_DELIVERIES`, multiple append/appendOrUpdate nodes — each n8n Google Sheets node consumes read quota (see §5).

7. **Error handlers causing retry/re-intake amplification?**  
   **Yes (proven).** When `Append ERRORS` returned 429, execution failed before Gmail ERROR labeling → same lead re-intake on next 30s poll. Wave 3 (`onError: continueRegularOutput` on `Append ERRORS`) restored `Add Gmail ERROR` on quota failure.

Evidence: `route-classification.json`, `operational-dev-node-runs-sample.json`, `post-patch-observe*.json`.

## 5. Why append nodes consumed / read quota

Diagnostic and node-run sampling establish that **write-labeled nodes still count against Read quota** in n8n's Google Sheets integration.

| Node | Requested op | Observed behavior | Read quota |
|---|---|---|---|
| `Append RAW v2` | append | Can **succeed** while separate `Read CONFIG` **429** in same execution | append path performs metadata/sheet resolution (read-class API calls) |
| `Append ERRORS` | append | Pre-fix: 429 blocked error labeling | Same append-internal read pattern |
| `Apply Runtime State CONFIG` | appendOrUpdate | Pre-fix post-hotfix: 429 failed execution after labels applied | appendOrUpdate read/metadata before write |

Sample proof (`operational-dev-node-runs-sample.json`): same execution shows `Append RAW v2` `status: success`, `is429: false` while `Read CONFIG` `is429: true`. Pressure table counts **472 read-quota runs** across explicit and write nodes for Operational.dev.

**Not guessed:** classification comes from execution node-run metadata (`op`, `is429`, status) aggregated in forensic scripts.

## 6. Rate budget

| Metric | Value |
|---|---:|
| Google limit (per user) | **60** read requests / minute |
| Pre-fix Operational.dev avg | **~10.5** reads/min (sampled) |
| Pre-fix burst (full lead path) | **~9–11** reads per execution × **~2** exec/min ⇒ rolling-minute peaks can exceed 60 when quota already hot |
| Target (design preference) | Sustained **<40** reads/min with burst headroom |
| Post-fix Wave 4 window (20 min) | **39** exec, **171** successful Sheets ops + **39** terminal 429; CONFIG reads skipped **39/39** |
| Post-fix estimated reads/min | Still **~10–11** node-scale (CONFIG savings ~**1** read/exec ≈ **~2**/min at 2 exec/min) — **insufficient** vs rolling saturation |

Safety margin after partial repair: **negative** while stuck-lead re-intake continues under quota.

## 7. Exact root cause

**Primary:** Operational.dev **re-processes the same Gmail lead every ~30s** because Sheets failures prevent consistent Gmail label transitions (processed/error). Each poll consumes multiple Google Sheets read-quota calls.

**Secondary amplifiers:**

- Full lead path ~**11** read-quota node runs per poll when DEDUP path progresses.
- Early path still hits **`Append RAW v2`** (read-backed append) + **`Read CONFIG`** pre-cache.
- **`Append ERRORS` 429** (pre Wave 3) prevented ERROR labeling → re-intake loop.
- **`Apply Runtime State CONFIG` 429** (pre Wave 4) failed executions after partial progress.

**Ruled out as primary cause in this window:**

- Empty-poll CONFIG reads (**0** empty polls observed).
- OAuth/credential mismatch, Docker, nginx, firewall (per prior diagnostic; not re-challenged).
- Admin.dev read pressure (negligible).

## 8. Repair design

Applied **smallest safe** workflow changes in priority order:

| Priority | Action | Status |
|---|---|---|
| A | Eliminate unnecessary CONFIG reads | **Deployed** — 5 min cache gate (Route Prep + IF + Normalize CONFIG persist) |
| B | Execution-local dedupe | **Partial** — CONFIG cached in workflow static data |
| C | Short safe cache | **Deployed** — 5 min TTL (derived from poll cadence + CONFIG change tolerance) |
| D | Retry discipline | **No change** — 0 retry storms observed; no unlimited retry added |
| Error path | Stop re-intake on ERRORS/runtime telemetry 429 | **Deployed** — `onError: continueRegularOutput` on non-semantic nodes |

**Explicitly not deployed** (business semantics risk):

- `onError` on `Lookup DEDUP_INDEX`
- `onError` on `Append RAW v2`
- OAuth rotation, quota increase, Docker/nginx changes

Patch sources: `implementation/patches/ConfigRoutePrep.google-sheets-429-repair.js`, `NormalizeCONFIG.google-sheets-429-repair.js` (deprecated broken `ConfigCacheGate.*` retained for audit only).

## 9. Modified nodes

**Workflow:** Operational.dev (`xSnXPy8cEHoZw6xG`) only. **Admin.dev unchanged.**

| Wave | Stamp (UTC) | Nodes / connections |
|---|---|---|
| 1 | 2026-09-01T06:58:17Z | `Read CONFIG` onError; `Normalize CONFIG` cache; `Update Last Success / Runtime State` empty-poll throttle; broken `CONFIG Cache Gate` (removed in Wave 2) |
| 2 | 2026-09-01T07:02:37Z | **Added** `CONFIG Route Prep`, `CONFIG Cache IF`; **Removed** `CONFIG Cache Gate`; rewired Parse Lead → cache branch |
| 3 | 2026-09-01T07:21:38Z | `Append ERRORS` → `onError: continueRegularOutput` |
| 4 | 2026-09-01T07:26:44Z | `Apply Runtime State CONFIG` → `onError: continueRegularOutput` |

Private PRE/POST workflow JSON backups: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\google-sheets-429-repair-20260901-134643-local\backups\` (not in git).

## 10. Deployment

| Check | Result |
|---|---|
| Operational.dev active post-deploy | **yes** |
| Admin.dev active / unchanged | **yes** |
| Protected prod workflow inactive | **yes** (`h8I2Tl2yl4uzhUnB`) |
| PRE backups | **yes** per wave (Storage path above) |
| POST backups | **yes** per wave |
| Telegram / ACCESS / AI | **untouched** |
| Synthetic tests | **none** |

Deploy receipts: `evidence/.../deploy-receipt.json`, `hotfix-deploy-receipt.json`, `append-errors-deploy-receipt.json`, `runtime-state-deploy-receipt.json`.

## 11. Post-fix natural execution evidence

Observation used **natural cron only** (no synthetic leads, no Telegram).

| Window | Since (UTC) | Exec | Any 429 | Success exec | Read CONFIG skip | Top 429 nodes |
|---|---|---:|---:|---:|---:|---|
| Post hotfix (Wave 2) | 07:02:37 | 29 | 29 | 0 | 28/29 | Lookup DEDUP_INDEX, Append ERRORS |
| Post Wave 3 | 07:21:38 | 6 | 6 | 0 | 6/6 | Lookup DEDUP_INDEX; Append ERRORS cleared |
| Post Wave 4 (final, 20 min) | 07:26:44 | **39** | **39** | **0** | **39/39** | **Lookup DEDUP_INDEX (20), Append RAW v2 (19)** |

Wave 4 highlights (`post-patch-observe-wave4.json`, `07:27:20Z` → `07:47:36Z`):

- `add_gmail_error_ok`: **19** (Wave 3 fix working)
- `add_gmail_processed_ok`: **0**
- `remove_gmail_incoming_ok`: **0**
- `successful_sheets_ops`: **171** (partial path progress before terminal 429)
- `retry_events`: **0**

**Progress proven:** CONFIG read pressure eliminated in observation; ERRORS/runtime telemetry no longer terminal on 429.

**Still failing:** Every observed execution ends in error with 429 at DEDUP lookup or RAW append while rolling quota remains saturated.

## 12. Google Sheets 429 before/after

| Metric | Pre-fix (45 min) | Post-fix Wave 4 (20 min) |
|---|---:|---:|
| Executions with any 429 | 90/90 (Operational.dev degraded) | **39/39** |
| `Read CONFIG` 429 | 80 (top node) | **0** (skipped via cache) |
| `Append ERRORS` 429 | 80 (top node pre-fix) | **0** |
| `Apply Runtime State CONFIG` 429 | present pre Wave 4 | **0** |
| `Lookup DEDUP_INDEX` 429 | 39 sampled | **20** (final window) |
| `Append RAW v2` 429 | 80 sampled | **19** (final window) |
| Execution `success` | 0 | **0** |

**Hard target `post-fix 429 = 0`:** **FAIL**

## 13. Direct spreadsheet ID

Production spreadsheet ID (sanitized reference only): `1aeIWHeaqHwgJSKLCFZP8M4qG5y9qmOcPt6rvSWs`

**DIRECT SPREADSHEET ID = NOT PROVEN POST-FIX**

No post-fix execution completed a full production success path demonstrating stable read against this spreadsheet after quota normalization. Partial successful node ops occurred, but terminal 429 persists.

## 14. OAuth/credential invariants

| Item | Status |
|---|---|
| Credential ID | `nRfNJVn6SEziII8k` (unchanged) |
| OAuth reauthorization | **not performed** |
| Credential rotation | **none** |
| Sharing / permissions | **unchanged** |
| Google Cloud project | **unchanged** (`173364893180`) |

## 15. Runtime/server invariants

| Layer | Mutations |
|---|---:|
| Docker / Compose | 0 |
| nginx | 0 |
| firewall | 0 |
| n8n upgrade | 0 |
| Container env | 0 (matches prior diagnostic) |

## 16. Telegram/ACCESS invariants

| Item | Status |
|---|---|
| Telegram synthetic messages | **0** |
| Olya test messages | **0** |
| AI calls | **0** |
| ACCESS workflow/config | **unchanged** |
| Moderator notifications semantics | **unchanged** (delivery not validated via synthetic send) |

## 17. UI list/search status

**UI LIST/SEARCH = UNKNOWN**

Not re-tested in this repair. No Drive/OAuth picker changes made.

## 18. Quota increase recommendation

**QUOTA INCREASE MAY STILL BE USEFUL**

Optimization reduced CONFIG and error-path waste but legitimate stuck-lead re-intake still drives multi-read executions exceeding rolling quota recovery. Quota increase was **not** requested (per charter). If operator approves later, treat as **fallback** after semantic-safe workflow options are exhausted.

Classification: **not** `QUOTA INCREASE NOT NEEDED`, **not** `QUOTA INCREASE REQUIRED AFTER OPTIMIZATION` (optimization incomplete).

## 19. Git

| Item | Path / state |
|---|---|
| Canonical repo | `X:\AI MARS` (not dirty-mutated beyond allowlisted repair artifacts) |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-sm-google-sheets-429-repair-20260901-143414\repo` |
| Worktree branch | `iseo-sm-gs429-repair-20260901` (tracks `origin/mars/canonical-post-recovery`) |
| Report | `projects/iseo-sales-manager-bot/reports/REPORT-iseo-sales-manager-bot-google-sheets-429-repair-v1.md` |
| Evidence | `projects/iseo-sales-manager-bot/evidence/current-stabilization/google-sheets-429-repair/` |
| Patches | `projects/iseo-sales-manager-bot/implementation/patches/*429-repair*.js` |
| Commit / push | **none** (default) |

## 20. Next gate

1. **STOP** further production mutation without operator charter (remaining 429 at DEDUP/RAW touch dedupe/RAW semantics).
2. Allow **natural quota recovery** + extended observation (≥15–20 min at 2 polls/min) before reassessing PASS.
3. If 429 persists after recovery: operator choice between **semantic-safe dedupe optimizations** vs **Google quota increase**.
4. **Do not** start final 48h bot soak until `post-fix 429 = 0` on stable window.
5. UI picker listing remains optional separate diagnostic.

---

## 21. Required counters

### Safety (expected 0)

| Counter | Value |
|---|---:|
| credential mutations | 0 |
| Google project mutations | 0 |
| Docker mutations | 0 |
| nginx mutations | 0 |
| firewall mutations | 0 |
| ACCESS mutations | 0 |
| Telegram synthetic messages | 0 |
| Olya test messages | 0 |
| AI calls | 0 |

### Functional / forensic

| Counter | Value |
|---|---:|
| active workflows sharing credential | 5 |
| observed pre-fix Sheets reads/min (Operational.dev) | 10.49 |
| estimated post-fix Sheets reads/min (Wave 4 window) | ~10–11 (CONFIG −~2/min) |
| empty polls observed (pre-fix window) | 0 |
| Sheets reads per empty poll before | N/A |
| Sheets reads per empty poll after | N/A |
| post-fix executions observed (Wave 4 final window, 20 min) | 39 |
| successful Sheets node operations (Wave 4) | 171 |
| post-fix 429 (executions with any 429, Wave 4) | **39** |
| retry events (Wave 4) | 0 |
| real leads observed (stuck re-intake) | yes |
| real leads lost | 0 (no duplicate/create anomaly proven) |
| duplicate logical leads | 0 |
| workflow mutations (deploy waves) | 4 |
| workflow files touched | Operational.dev only |

---

**Evidence pack:** `projects/iseo-sales-manager-bot/evidence/current-stabilization/google-sheets-429-repair/`  
**Private backups (Storage only):** `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\google-sheets-429-repair-20260901-134643-local\backups\`
