# REPORT — I-SEO REPORT HUB REPORT DELIVERY PUBLIC SHARE VISUAL QA 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `17a10da3b66803acdc204532adb1b825a40cbe3e` |
| Staged/index state | Foreign staged WIP present (client-ops); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-delivery-public-share-visual-qa-01\repo` (for docs commit) |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** |
| Write scope | allowlisted i-SEO docs only; evidence under STORAGE; DB share create/revoke/access via QA smoke only |

## 2. Preflight

| Item | Value |
|------|-------|
| PHP | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migrations | **9** |
| Tables | **16** |
| report_exports before | **4** |
| report_export_shares before | **3** |
| Active shares before | **0** |
| Existing share status before | all **revoked**, export id **4** |
| Export ids 1–4 | ready; id **4** shareable; ids **1–3** not |
| Artifact checksums before | v1/v2 HTML/PDF match expected; PDFs `%PDF` |
| Runtime `.env.local` | present (contents redacted; not printed; not committed) |

## 3. QA Method

| Item | Value |
|------|--------|
| Server | PHP `-S 127.0.0.1:8092` + `-d session.save_path` Laragon tmp |
| Auth | session injection (no password/session/token printed) |
| Evidence folder | `X:\AI MARS STORAGE\incoming\iseo-report-hub\public-share-visual-qa-01\` |
| Capture method | HTML main extracts + HTTP header/body text captures (no browser install) |
| Token redaction | once-URL evidence uses `[REDACTED_64HEX_TOKEN]`; docs never include plaintext token |

## 4. Internal UI QA

| Check | Result |
|-------|--------|
| Export list | Shareable for id **4**; blocked badge for ids **1–3** |
| Id 1 | Not shareable — Only PDF exports are shareable |
| Id 2 | Not shareable — Template metadata is required |
| Id 3 | Not shareable — Only PDF exports are shareable |
| Id 4 | Shareable PDF / Eligible; Manage shares CTA |
| Shares page | Revoked rows readable; create CTA when no active share |
| Create once-URL | Shown once; autocomplete off; spellcheck false; Copy button |
| Revisit | once-box gone; plaintext not recoverable |
| Revoke | revoked status; create CTA returns |
| Leak checks | no `token_hash` / IP-UA hashes / absolute path |

## 5. Public Route QA

| Check | Result |
|-------|--------|
| Valid token stream | **200** PDF; magic `%PDF`; no HTML wrapper; no path |
| Headers | Content-Type application/pdf; attachment; Content-Length; nosniff; private/no-store; noindex/nofollow; Pragma no-cache; Expires 0; Referrer-Policy no-referrer |
| Malformed tokens | **404** |
| Invalid 64-hex | **404** |
| Revoked token | **410**; no detail leak |
| `/share` | **404** |
| `/r/test` | **404** |

## 6. DB Validation

| Check | Result |
|-------|--------|
| Shares before/after | **3** → **4** |
| Final statuses | all **revoked** (ids 1–4) |
| Active final | **0** |
| Access count | incremented to **1** on successful public stream for QA row |
| Plaintext token in DB | **no** (hash only; 64 hex) |
| Business counts | unchanged |
| report_exports mutation | **no** |
| DELETE/DROP/TRUNCATE | **no** |

## 7. Artifact Validation

| Check | Result |
|-------|--------|
| v1 HTML | `c194c62b…6fadc4` unchanged |
| v1 PDF | `707e72d6…0d0320` unchanged; `%PDF` |
| v2 HTML | `27a6eee6…95f6ffe` unchanged |
| v2 PDF | `a8c4d61c…1a56b6b` unchanged; `%PDF` |
| New artifacts | **no** |
| Public artifact files | **no** |

## 8. Visual Verdict

| Field | Value |
|-------|-------|
| Verdict | **PASS_WITH_MINOR_ISSUES** |
| BLOCKER | **0** |
| MAJOR | **0** |
| MINOR | **2** |

| ID | Severity | Finding |
|----|----------|---------|
| UI-REL-STORAGE-PATH | MINOR | Auth export detail shows relative `storage/exports/...` path |
| UI-LIST-SHARE-LABEL | MINOR | List badge **No** vs detail **Not shareable** |

Smoke: **86/86 PASS**.

## 9. Restrictions Confirmed

All charter restrictions confirmed: no production/remote DB; no real data beyond fixture; no credentials/password/hash/session/plaintext token in report; no `.env` commit; no source `.env.local`; no schema/migration/db-migrate; no app-source/runtime/auth/health/fixture-tool edits; no business/export row mutation; no artifact overwrite; no public webroot artifact writes; no prune of existing revoked rows; no active long-lived share left; no DELETE/DROP/TRUNCATE; no package install; no vhost/hosts/service restart; no demo/registry; no push/fetch/pull/reset/clean/stash; no broad git add.

## 10. Documentation

- Result: `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md`
- OPERATIONAL-INDEX updated
- This closeout report

## 11. Commit

| Field | Value |
|-------|-------|
| Exact-path git add | yes (allowlist docs only; clean worktree) |
| Staged list (primary) | VISUAL-QA-RESULT; REPORT; OPERATIONAL-INDEX |
| Primary commit | `9e9101879904b4a981cf58a5e04aeac64cd3baf2` — `docs(iseo-report-hub): add public share visual qa` |
| Hash-record commit | (this commit) — `docs(iseo-report-hub): record public share visual qa commit hash` |
| HEAD verification | filled after hash-record |
| Push | **no** |

## 12. SAFE UNKNOWN

- Apache `:80` / Laragon vhost state during `:8092` Visual QA smoke not re-probed.
- Four revoked smoke rows remain; pruning needs a separate DB charter.
- Pixel PNG browser screenshots not produced (HTML/header evidence only).

## 13. Recommended Next Action

I-SEO Report Hub — Report Delivery Client Handoff UX Charter 01

## 14. Files Changed

**Git (Active Brain):**

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-VISUAL-QA-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-delivery-public-share-visual-qa-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

**STORAGE (not Git):** evidence under `X:\AI MARS STORAGE\incoming\iseo-report-hub\public-share-visual-qa-01\`

**DB:** +1 `report_export_shares` row (id **4**, revoked after QA); access_count=1 on that row; ids **1–3** preserved.

**App-source / runtime code:** unchanged.

## 15. Git Actions

| Action | Done? |
|--------|-------|
| Exact-path git add | yes (worktree) |
| Commit | yes (primary + hash-record) |
| Push | **no** |
| Fetch / pull | **no** |
| Checkout / update-ref | yes for worktree→main branch alignment |
| Reset / restore / clean / stash | scoped restore of i-SEO docs on main if needed |
| Broad git add | **no** |
| Clean temporary worktree | used for commit |
