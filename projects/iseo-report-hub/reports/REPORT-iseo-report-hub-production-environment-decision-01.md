# REPORT — I-SEO REPORT HUB PRODUCTION ENVIRONMENT DECISION 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `976ead719361557888c79d725ef702aa890d3c2f` |
| Staged/index state (main) | Foreign staged WIP present (`projects/client-ops-reporting-bridge/` and related; **299** staged paths); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-hub-production-environment-decision-01\repo` (detached HEAD for docs commit) |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** — main index untouched |
| Write scope | allowlisted i-SEO docs only |

## 2. Baseline Reviewed

| Baseline | Result |
|----------|--------|
| Production Environment Charter 01 | COMPLETE; primary `b2b0c3af…`; hash-record `50650dd9…`; tip `976ead71…`; docs/policy; recommended candidate Option C; production **not** selected |
| Production Readiness Charter 01 | COMPLETE; primary `fd99ce7d…`; hash-record `677d07fa…`; tip `07505b97…`; local MVP gates **A–D PASS**; production **E–K** REQUIRED_BEFORE_PRODUCTION |
| Client Handoff UX Visual QA 01 | COMPLETE; primary `1431192b…`; hash-record `9720ed5f…`; tip `ae5589ae…`; verdict **PASS**; smoke **129/129**; BLOCKER/MAJOR/MINOR **0**; shares **6** revoked / active **0**; `report_exports` **4** unchanged |
| Public Share stack | DB-10 + implementation + hardening + Visual QA complete; `GET /share/report/{token}` direct PDF stream; hash-only; 64-hex; 404/410; no portal/email/landing/`/r/{token}` |
| Expected DB baseline (attested) | migrations **9**; tables **16**; exports **4**; shares **6** revoked; active **0**; users/roles **1/6**; clients/projects/sites **1/1/1**; periods **2**; weekly **4**; monthly **1**; blocks **6**; snapshots **1** |
| Live DB check (this decision wave) | Optional read-only probe: TCP `127.0.0.1:3306` **refused**; mysql CLI absent; **no** mutation; baseline from Visual QA docs (**SAFE UNKNOWN** live counts) |

## 3. Decision Output

Created/updated:

- `product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md`
- `product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-MATRIX-v0.1.md`
- `product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md`
- `product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md`
- `OPERATIONAL-INDEX.md` updated (active stage, Decision 01 section, next stages, boundaries)
- This closeout report

| Topic | Value |
|-------|-------|
| Decision state | **`RECOMMENDATION_READY`** |
| `APPROVED_FOR_IMPLEMENTATION` | **No** |
| `PRODUCTION_SELECTED` | **No** |

## 4. Recommendation

| Item | Value |
|------|-------|
| Recommended default | **Option C — VPS PHP-FPM/Nginx/MySQL** |
| Webserver | Nginx preferred; Apache acceptable |
| PHP / DB | PHP **8.3** preferred; MySQL **8.x** preferred |
| Docroot / storage | `/public` only; storage/logs outside public |
| HTTPS | Stable domain + TLS required for client-facing shares |
| PDF | Validate headless on VPS; fallback pre-generated / serve-only |
| Deploy | Release-hash exact sync or Git-based — after operator choice; **no deploy now** |

**Rationale:** best fit for custom PHP + MySQL + headless PDF + public share; stronger control than shared hosting; lower first-pilot complexity than mandatory containers/managed platforms.

**Non-negotiable:** HTTPS; stable domain; docroot `/public`; storage/logs outside public; secrets outside Git; backup/restore; no fixture data to clients; token logs sensitive; production DB ≠ `iseo_report_hub_dev`.

## 5. Operator Decisions Needed

All **pending** (no invented server/domain):

1. Environment option (A–E)
2. Provider / server / OS
3. Domain / subdomain (exact hostname)
4. HTTPS method
5. DB engine / version
6. PHP version
7. PDF mode
8. Deployment method
9. Backup policy (locations, retention, restore test)
10. Access model
11. Logging policy
12. Real data mode
13. DB-11 before pilot (yes/no/defer)
14. Production implementation approved (yes/no)

## 6. Next Wave Logic

| Operator outcome | Next wave |
|------------------|-----------|
| VPS approved **with** server + domain details | **Production Environment Validation 01** |
| VPS direction only (no details) | **Production Environment Decision Follow-up 01** |
| Shared hosting | **Shared Hosting Compatibility Validation 01** |
| Local-only demo | **Local Demo Hardening Charter 01** |
| DB-11 required before pilot | **Report Delivery DB-11 Delivery Events Charter 01** |

**Immediate recommended next (now):** `I-SEO Report Hub — Production Environment Operator Decision 01`

## 7. Boundaries Confirmed

- no server access;
- no deployment;
- no DNS / HTTPS setup;
- no DB mutation;
- no app-source / runtime changes;
- no secrets creation / commit;
- no production claim.

## 8. Restrictions Confirmed

Confirmed for this wave:

- no app-source edits;
- no runtime edits;
- no DB mutation;
- no SQL/migration creation/edit;
- no share token creation;
- no public route changes;
- no report_exports / report_export_shares / report_snapshots / report_blocks / monthly / weekly / period row changes;
- no artifact regeneration;
- no new export rows;
- no package install/download;
- no production deployment;
- no domain/DNS/HTTPS/server operations;
- no push / fetch / pull / reset / clean / stash;
- no broad git add;
- no foreign WIP remediation.

## 9. Commit

| Item | Value |
|------|-------|
| Exact-path git add | allowlisted Decision 01 docs only (see §12) |
| Primary commit message | `docs(iseo-report-hub): add production environment decision package` |
| Primary commit hash | `114abef1a451d50aa9c893bdb85508bb96197523` |
| Hash-record commit message | `docs(iseo-report-hub): record production environment decision commit hash` |
| Hash-record commit hash | `fc304a62bd681ba2113f18cbe822374631d4cee2` |
| Tip after wave | `fc304a62bd681ba2113f18cbe822374631d4cee2` |
| Push | **no** |

## 10. SAFE UNKNOWN

| Item | Note |
|------|------|
| Live local MySQL state | TCP 3306 refused this wave; same as Production Readiness Charter 01 and Production Environment Charter 01; counts not re-attested live |
| Production host / domain / HTTPS | Not selected; not invented |
| Operator checklist answers 1–14 | All pending |
| Whether Validation 01 can run | Unknown until Operator Decision 01 supplies (or withholds) server/domain |

Before any implementation/deploy work that needs local DB evidence: re-check `iseo_report_hub_dev` @ `127.0.0.1`.

## 11. Recommended Next Action

**I-SEO Report Hub — Production Environment Operator Decision 01**

## 12. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-BRIEF-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-DECISION-MATRIX-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-OPERATOR-APPROVAL-CHECKLIST-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PRODUCTION-ENVIRONMENT-NEXT-WAVE-PLAN-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-production-environment-decision-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

## 13. Git Actions

| Action | Result |
|--------|--------|
| Exact-path git add | **yes** — allowlisted docs only |
| Commit | **yes** — primary + hash-record (worktree) |
| Push | **no** |
| Fetch | **no** |
| Pull | **no** |
| Checkout / update-ref | worktree detached at pre-wave HEAD; after commits: `git update-ref refs/heads/mars/canonical-post-recovery <tip>` if safe |
| Reset | **no** |
| Restore | scoped restore on main for changed i-SEO docs only if needed to align working tree |
| Clean | **no** |
| Stash | **no** |
| Broad git add | **no** |
| Clean temporary worktree | used: `X:\AI MARS STORAGE\git-sync-iseo-report-hub-production-environment-decision-01\repo` |
