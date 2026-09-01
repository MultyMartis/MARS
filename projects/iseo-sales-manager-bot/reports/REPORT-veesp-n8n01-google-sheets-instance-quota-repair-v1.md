# REPORT — VEESP-N8N-01 Google Sheets Instance Quota Repair v1

Generated: 2026-09-01T09:00:00Z  
Target: VEESP-N8N-01 (`https://n8n.ai-metacode.com`) · n8n 2.14.2  
Process line: `VEESP-N8N-01 — SHARED GOOGLE SHEETS PER-USER QUOTA SATURATION — INSTANCE-WIDE ACTIVE-CONSUMER FORENSIC + MINIMAL REPAIR`  
Prior iSEO-only repair: [REPORT-iseo-sales-manager-bot-google-sheets-429-repair-v1.md](./REPORT-iseo-sales-manager-bot-google-sheets-429-repair-v1.md)

## 1. Verdict

**PARTIAL — CROSS-WORKFLOW QUOTA SATURATION REMAINS**

Instance-wide Phase A confirms **Operational.dev** dominates active shared-credential read pressure under a **confirmed re-intake loop**. Waves 1–5 (Operational.dev only) eliminated CONFIG/DEDUP read hammer and reduced DEDUP 429 to zero in post-Wave-5 observation, but **HTTP 429 persists** on RAW/CLEAN and downstream nodes. **PASS** criterion (`new Sheets 429 = 0` during adequate natural observation) is **not** met.

Not achieved:

> `INSTANCE-WIDE GOOGLE SHEETS QUOTA REPAIR PASS — SHARED REQUEST PRESSURE NORMALIZED`

## 2. Current production impact

| Surface | Status | Evidence |
|---|---|---|
| iSEO Operational.dev lead intake | **Degraded** — executions alternate success/error; **0** leads marked `gmail_processed` in Wave-5 observe window | `post-patch-observe-wave5.json` |
| iSEO Admin.dev reminder group navigation | **Blocked upstream** — callback reaches Sheets reads → 429 → `Сервис временно недоступен` | `admin-reminder-trace.json` exec **54217** |
| SEO Content Agent `/health` | **Intermittent** — operator-reported alternating 429 on `seo_active_jobs` vs `memory`; not dominant in forensic window | operator evidence + `instance-forensic-extended.json` §seoHealth |
| Shared credential | **Saturated** — rolling per-user read quota contention | HTTP 429 message below |

**Exact Google error (proven):**

`Quota exceeded for quota metric 'Read requests' and limit 'Read requests per minute per user' of service 'sheets.googleapis.com' for consumer 'project_number:173364893180'.`

## 3. Active Google consumer inventory

Forensic window: **45 minutes** (`pressure-summary-fresh.json`, generated `2026-09-01T08:26:58Z`). Only workflows with **actual executions** in window are counted.

| Workflow | Workflow ID | Active | Executions | Google node runs (sampled) | Est. read req/min | Peak/min | Purpose |
|---|---|---:|---:|---:|---:|---:|---|
| i-SEO Sales Manager - Operational.dev | `xSnXPy8cEHoZw6xG` | yes | 89 | 487 | **~10.64** | ~1.98 exec/min | Gmail lead intake / dedupe / RAW / CLEAN |
| i-SEO Sales Manager - Admin.dev | `wLrLp4WQHm1VJmxz` | yes | 3 | 8 | ~0.18 | ~0.07 | Admin bot + reminder callbacks |
| SEO Content Agent Beta.v14 - Admin | `AR6QxGt8ZKH0xG2T` | yes | 1 | 2 | ~0.04 | ~0.02 | Admin + `/health` |
| SEO Content Agent Beta.v14 - Worker | `p4mqb4VuPcemIDlC` | yes | 0 | 0 | 0 | 0 | Worker (idle in window) |
| SEO Content Agent Beta.v14 - Intake | `x8EbTGKNdlBprLvk` | yes | 1 | 0 | 0 | ~0.02 | Intake trigger (no Sheets runs sampled) |

**REAL ACTIVE CONSUMER SET:** 5 active credential-bound workflows; **3 executed** in window; **1 dominant** (Operational.dev).

**429 sampled in window:** 80 (all attributed to Operational.dev in pressure summary).

## 4. Shared credential/user evidence

| Field | Value |
|---|---|
| Credential ID | `nRfNJVn6SEziII8k` |
| Credential name | Google Sheets account (Multy Martis) |
| Type | `googleSheetsOAuth2Api` |
| Google project | `173364893180` |
| All active consumers in set | **Same credential** (hashed in evidence as `714B72146501A2F8`) |

**Mutations:** credential / OAuth / project / permissions = **0** (invariant preserved).

## 5. Total rate budget

| Component | Pre-fix baseline (45m forensic) | Post-Wave-5 observe (21m) |
|---|---:|---:|
| Operational.dev | ~**10.64** reads/min sampled; ~1.98 exec/min | ~2.05 exec/min; CONFIG reads **skipped** (cache); DEDUP 429 **0** |
| Admin.dev | ~0.18 reads/min | not re-measured (low volume) |
| SEO Content Agent (all) | ~0.04 reads/min | not re-measured |
| Retry / re-intake amplification | **High** — 2 stuck Gmail IDs → 100 exec / 60 min (~1.67/min) | **Persists** — ~2 exec/min; 72% executions with ≥1 Sheets 429 |
| **TOTAL BASELINE READ RPM (sampled)** | **~11** (Operational-dominated) | **UNKNOWN** exact reads/min post-cache; pressure still exceeds quota |
| **TOTAL PEAK READ RPM** | Driven by full lead path (~11 Sheets nodes) × ~2 exec/min | Alternating full (~14 nodes) / partial (~4 nodes) every ~30s |
| **Google per-user read limit (numeric)** | **UNKNOWN** — not extractable from API metadata in this task |
| **Observed rejection rate** | 80/487 sampled node runs ≈ **16%** 429 (Operational only) | **31/43** executions ≈ **72%** with Sheets 429 |

Interpretation: even after CONFIG/DEDUP optimizations, **stuck-lead polling** keeps aggregate demand in the rolling quota envelope; Admin/SEO failures correlate with saturation, not separate credentials.

## 6. Top quota consumers

1. **i-SEO Sales Manager - Operational.dev** — ~10.64 reads/min; 80×429 sampled  
   - `RE-INTAKE LOOP` / `STUCK-ITEM_REPROCESS` / `RETRY_AMPLIFICATION`  
   - Full path: DEDUP, ACCESS, DELIVERIES, RAW, CLEAN, ERRORS, runtime CONFIG writes  
   - Pre-fix: redundant CONFIG every poll → **fixed** (cache)  
   - Pre-fix: DEDUP hammer → **reduced post-Wave-5** (0 DEDUP 429 in observe)

2. **i-SEO Sales Manager - Admin.dev** — ~0.18 reads/min; reminder callbacks **BUSINESS_REQUIRED** but fail when quota saturated  
   - Classification: `BUSINESS_REQUIRED` + `HEALTHCHECK_OVERREAD` (none) — failure is **contention**, not design dominance

3. **SEO Content Agent Admin** — ~0.04 reads/min; `/health` ≈ **4 reads** per invocation  
   - Classification: `HEALTHCHECK_OVERREAD` (moderate); `BUSINESS_REQUIRED` for production jobs  
   - **Not modified** in this wave (read-only inspect)

No other active consumers material in window. Inactive workflows with Google nodes **excluded** per charter.

## 7. iSEO re-intake loop

**Classification: RE-INTAKE LOOP CONFIRMED**

| Signal | Value |
|---|---|
| Window | 60 min (`instance-forensic-extended.json` §reIntake) |
| Operational executions | 100 |
| Unique stuck Gmail message IDs | **2** (hashed) |
| Repeat counts | 69 + 31 executions per message |
| Amplification | **~1.67 exec/min** |
| `gmail_processed` | Remains **false** when RAW/dedupe path blocked |
| First failing nodes (pre-Wave-5) | `Lookup DEDUP_INDEX`, `Append RAW v2` |
| Gmail error label | Applied inconsistently on error path |

**Causal chain:** Gmail poll re-delivers same message → Operational.dev runs lead path → Sheets 429 on integrity gate → hard stop → message not marked processed → **~30s** poll repeats → quota amplification.

**Wave-5 mitigation:** defer gate (5 min per message), DEDUP retry/backoff, error bridge sets defer timestamp. **Partial effect:** DEDUP 429 cleared; loop cadence unchanged; RAW/CLEAN 429 remain.

**dedupe bypass = 0** · **RAW bypass = 0**

## 8. iSEO Admin reminder failure

**IS CURRENT REMINDER FAILURE CAUSED BY SAME SHEETS 429? → YES**

| Field | Value |
|---|---|
| Workflow | i-SEO Sales Manager - Admin.dev (`wLrLp4WQHm1VJmxz`) |
| Execution ID | **54217** |
| Mode | webhook (Telegram callback) |
| Path | Operator `reminder` → group button (`Аудит 13` / `SEO 2` class callbacks) |
| UI | `Открываю группу` → **`Сервис временно недоступен. Попробуйте позже.`** |
| Failing Sheets nodes | `Read CLEAN for Callback`, `Read LEAD_DELIVERIES for Sync` |
| Error | HTTP **429** (same quota metric) |
| Before canonical card? | **Yes** — failure before card/sync completion |

Additional Admin executions in 180m trace: **12** Sheets 429 samples; **3** match reminder failure pattern (`admin-reminder-trace.json`).

## 9. SEO Content Agent evidence

| Field | Value |
|---|---|
| Admin workflow | `AR6QxGt8ZKH0xG2T` |
| Same credential? | **YES** |
| Health nodes | `Health Check Active Jobs`, `Health Check Memory` |
| Reads per `/health` (estimate) | **~4** |
| Forensic sample exec | **54322** — both health reads **success** (window not saturated at instant) |
| Worker / Intake | Active; negligible/zero pressure in window |
| Mutations | **0** (read-only inspect) |

Operator alternating 429 pattern is **consistent with shared rolling quota**, not a separate Google user.

## 10. Retry amplification

| Mechanism | Pre-fix | Post-Wave-5 |
|---|---|---|
| Stuck-message re-poll (~30s) | ~2 exec/min × multi-node path | **Unchanged cadence** |
| DEDUP immediate re-read | High 429 count | **0** DEDUP 429 in observe |
| n8n `retryOnFail` on DEDUP/RAW | N/A | maxTries=4, wait 15s — **bounded** |
| Error-path Gmail re-intake (Append ERRORS) | Prior issue | **continueRegularOutput** — no Gmail loop from ERRORS |
| Defer gate skip | N/A | Deployed; **not separately counted** in observe script — effectiveness **partial** |

## 11. Exact repair design

### Decision matrix (deployed)

| Workflow | Node/pattern | Reads before (est.) | Reads after (est.) | Semantic risk | Modify? |
|---|---|---:|---:|---|---|
| Operational.dev | Read CONFIG every poll | 1/poll | 0 when cache fresh (5m TTL) | Low — TTL bounded | **Yes** (Waves 1–2) |
| Operational.dev | Append ERRORS → stop execution | N/A (amplification) | continue on error | Low — error ledger best-effort | **Yes** (Wave 3) |
| Operational.dev | Apply Runtime State CONFIG on empty poll | 1/empty poll | throttled skip | Low | **Yes** (Wave 4) |
| Operational.dev | Sheets Quota Defer Gate | 0 | skips full path 5m after defer | Medium — delayed retry | **Yes** (Wave 5) |
| Operational.dev | DEDUP retry + error output → bridge | immediate fail | 4×15s retry + defer stamp | Low — **no bypass** | **Yes** (Wave 5) |
| Operational.dev | RAW retryOnFail only | immediate fail | 4×15s retry | Low — **no bypass** | **Yes** (Wave 5) |
| Admin.dev | — | — | — | — | **No** |
| SEO Content Agent | — | — | — | — | **No** |

### Wave 5 architecture (live 2026-09-01T08:31:58Z)

1. `Sheets Quota Defer Gate` after `Parse Lead` — static-data defer per `gmail_message_id`  
2. `IF Sheets Quota Deferred` → `Sheets Quota Defer Skip` (terminal, **zero** Sheets reads)  
3. `Lookup DEDUP_INDEX` — `retryOnFail`, `onError: continueErrorOutput` → `Sheets Quota Error Bridge` → `Error Handler`  
4. `Append RAW v2` — `retryOnFail` only (**no** permissive onError)  
5. Enhanced quota-aware `Error Handler` + defer timestamp on 429  

Deploy receipt: `evidence/.../wave5-deploy-receipt.json`  
PRE/POST backups: `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\google-sheets-429-repair-20260901-134643-local\backups\`

## 12. Modified workflows/nodes

**Production mutations:** Operational.dev only (`xSnXPy8cEHoZw6xG`).

| Wave | Nodes added/modified |
|---|---|
| 1–2 | CONFIG Route Prep, CONFIG Cache IF, Normalize CONFIG |
| 3 | Append ERRORS (onError) |
| 4 | Apply Runtime State CONFIG (onError + empty-poll throttle) |
| 5 | Sheets Quota Defer Gate, IF Sheets Quota Deferred, Sheets Quota Defer Skip, Sheets Quota Error Bridge; Error Handler; Lookup DEDUP_INDEX; Append RAW v2 |

**Patch sources:** `projects/iseo-sales-manager-bot/implementation/patches/*.google-sheets-429-repair.js`

## 13. DEDUP/RAW integrity proof

| Invariant | Status |
|---|---|
| `Lookup DEDUP_INDEX` remains authoritative | **Yes** — still executed before lifecycle advance; no skip-on-fail |
| `Append RAW v2` required before processed state | **Yes** — no `continueRegularOutput` on RAW |
| dedupe bypass | **0** |
| RAW bypass | **0** |
| Post-Wave-5 DEDUP 429 count | **0** (21m observe) |
| Post-Wave-5 RAW 429 count | **9** (still failing; not bypassed) |

## 14. Pre/post request pressure

| Metric | Pre-fix (45m) | Post-Wave-5 (21m) |
|---|---:|---:|
| Operational exec/min | ~1.98 | ~2.05 |
| CONFIG Read 429 | 0 (after Wave 2 in prior report) | **skipped** — cache hit all 43 exec |
| DEDUP 429 | 8 (prior partial window) | **0** |
| RAW 429 | 7 (prior) | **9** |
| CLEAN append/update 429 | present | **22** node-level |
| Executions with any Sheets 429 | ~100% in degraded periods | **31/43 (72%)** |
| Leads fully processed | 0 | **0** |

## 15. Post-fix natural observation

| Field | Value |
|---|---|
| Window | `2026-09-01T08:31:58Z` → `2026-09-01T08:54:07Z` (**21 min**) |
| Method | Natural production traffic only; **no** synthetic Telegram |
| Executions | 43 |
| Success rate | 12/43 (28%) |
| Sheets 429 executions | **31** |
| PASS threshold (≥20 min, 429=0) | **NOT MET** |

Evidence: `evidence/current-stabilization/google-sheets-instance-quota-repair/post-patch-observe-wave5.json`

## 16. Sheets 429 before/after

| Scope | Before instance repair | After Wave 5 (21m) |
|---|---:|---:|
| Instance sampled 429 (45m forensic) | 80 | — |
| Operational DEDUP 429 | 8 (prior wave window) | **0** |
| Operational RAW 429 | 7 (prior) | **9** |
| Operational any-429 executions | ~100% in saturation | **72%** |
| Admin reminder callback 429 | proven (54217) | **not re-tested** post-fix (blocked while saturation persists) |

## 17. OAuth/credential invariants

| Counter | Value |
|---|---:|
| Google credential mutations | **0** |
| OAuth reauthorization | **0** |
| Credential rotation | **0** |
| Spreadsheet permission changes | **0** |
| Google project changes | **0** |

## 18. Server/runtime invariants

| Counter | Value |
|---|---:|
| Docker mutations | **0** |
| nginx mutations | **0** |
| firewall mutations | **0** |
| n8n upgrade | **0** |
| ACCESS workflow mutations | **0** |
| AI calls | **0** |

## 19. /health resilience status

iSEO `/health` producing no Telegram response when Sheets fails: **documented as likely dependency** (workflow terminates before summary reply). **Not implemented** in this wave — scope deferred (charter §16).

SEO `/health`: 4 reads per check; failures are **quota contention**, not separate breakage.

## 20. Reminder card confirmation status

**CARD LIVE CONFIRMATION BLOCKED BY GOOGLE SHEETS QUOTA**

Natural reminder actionable-card patch **not judged** while group navigation fails upstream on Sheets 429. Next natural reminder after quota normalization may resume pending live confirmation.

## 21. Quota increase recommendation

**QUOTA INCREASE RECOMMENDED AS ADDITIONAL HEADROOM**

Rationale: after removing CONFIG/DEDUP waste, **legitimate stuck-lead recovery** still requires multi-read/write paths; baseline may sit near per-user ceiling under 2 stuck messages. Exact ceiling **UNKNOWN** — recommend Google Cloud quota review for `Read requests per minute per user` on project `173364893180`. **No quota change performed** in this task.

## 22. Git canonicalization

| Item | Path / SHA |
|---|---|
| Repair worktree | `X:\AI MARS STORAGE\git-sync-iseo-sm-google-sheets-429-repair-20260901-143414\repo` |
| Branch | `iseo-sm-gs429-repair-20260901` |
| Base (pre-repair) | `4a304a29facd500892f32f5203b00ec9831de973` (= `origin/mars/canonical-post-recovery` at task start) |
| Charter anchor cited | `ef662992ab3146abfcdb0c10e3a025720a597bbb` — **superseded** by later canonical |
| Live production | **Ahead of** prior partial git state; Wave 5 live **2026-09-01T08:31:58Z** |
| Repair worktree commit | `395ff51271be47e2f9c6b0527a07ea318984dc91` (`iseo-sm-gs429-repair-20260901`) |
| Canonical commit (main repo) | `2359b4ea9087e2d29d68afc6341aa35a4c04fc6c` — selective stage of 28 allowlisted paths |
| Push | **STOP — REMOTE/HEAD MISMATCH** — `git push origin mars/canonical-post-recovery` rejected (non-fast-forward); remote @ `4a304a29`; local ahead with repair commit + prior unpushed foreign commits. Operator pull/rebase/merge required before push. |

**Allowlisted artifacts:** instance report, iSEO 429 repair report, evidence folders `google-sheets-429-repair` + `google-sheets-instance-quota-repair`, patches `*.google-sheets-429-repair.js`.

## 23. Remaining risks

1. **Stuck Gmail messages** continue ~30s polling until RAW/CLEAN succeed — quota amplification persists.  
2. **Admin reminder navigation** remains blocked during saturation windows.  
3. **SEO `/health`** may alternate 429 for operators during same windows.  
4. **Defer gate** may not cover RAW/CLEAN 429 paths comprehensively — defer skip not proven in telemetry.  
5. **Zero leads processed** in observe window — production backlog risk for stuck leads.  
6. **Exact Google quota numeric limit** unknown — sizing headroom requires Cloud Console.

## 24. Next gate

1. **Wave 6 design (Operational.dev only):** extend defer stamping to **any** Sheets 429 on RAW/CLEAN/error bridge; optionally lengthen defer TTL; verify defer-skip executions in n8n UI; **never** bypass DEDUP/RAW.  
2. **Re-observe ≥20 min** natural traffic; require **Sheets 429 = 0** for PASS.  
3. **Natural Admin reminder** retry (`Аудит 13` / `SEO 2`) after PASS — confirm card live path.  
4. **Optional:** SEO health read collapse (2 reads → 1 cached) — separate charter if Operational PASS insufficient.  
5. **Quota increase request** to Google if post-waste baseline still ≥ limit.  
6. **Merge** repair branch → `mars/canonical-post-recovery` after operator review.

---

## Safety counters (task closeout)

| Counter | Value |
|---|---:|
| Google credential mutations | 0 |
| Google project mutations | 0 |
| Docker / nginx / firewall | 0 |
| ACCESS mutations | 0 |
| Olya / customer synthetic messages | 0 |
| AI calls | 0 |
| dedupe bypasses | 0 |
| RAW bypasses | 0 |
| real leads lost | **UNKNOWN** (0 processed; stuck not abandoned) |
| duplicate logical leads caused | 0 |

## Evidence index

`projects/iseo-sales-manager-bot/evidence/current-stabilization/google-sheets-instance-quota-repair/`

- `pressure-summary-fresh.json` — active consumer table  
- `route-classification.json` — Operational.dev route stats  
- `instance-forensic-extended.json` — re-intake + SEO health  
- `admin-reminder-trace.json` — callback 429 trace  
- `wave5-deploy-receipt.json` — live deploy proof  
- `post-patch-observe-wave5.json` — 21m post-fix observation  
- `*.live.sanitized.json` — workflow structure snapshots (no secrets)

Prior wave evidence: `.../google-sheets-429-repair/`

Private backups (not in git): `X:\AI MARS STORAGE\incoming\iseo-sales-manager-bot\google-sheets-429-repair-20260901-134643-local\backups\`
