# REPORT — I-SEO REPORT HUB REPORT DELIVERY PUBLIC SHARE HARDENING 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `8d148df52653d09135ed26eae9b041e4e126f2a7` |
| Staged/index state | Foreign staged WIP present (client-ops); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-delivery-public-share-hardening-01\repo` (for commit) |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** |
| Write scope | allowlisted i-SEO app-source + docs; exact runtime sync; DB share create/revoke/access via smoke only |

## 2. Preflight

| Item | Value |
|------|-------|
| PHP | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migrations | **9** |
| Tables | **16** |
| report_exports before | **4** |
| report_export_shares before | **2** |
| Active shares before | **0** |
| Existing share status before | both **revoked**, export id **4** |
| Export ids 1–4 | ready; id **4** shareable; ids **1–3** not |
| Artifact checksums before | v1/v2 HTML/PDF match expected; PDFs `%PDF` |
| Runtime `.env.local` | present (contents redacted; not printed; not committed) |

## 3. Source Hardening

| Area | Change |
|------|--------|
| Token helper | `SafeToken`: exact 64-hex gate; `hashPublicToken()`; generate self-check |
| Repository | Access UPDATE requires active + `expires_at > NOW()` + max_access headroom |
| Service | Format-before-hash resolve; deferred access record; UI sanitization of hash/IP fields |
| Controllers | Public stream headers + access after preflight; deny headers aligned |
| Routes | `/share/report/{64hex}` only; malformed `/share/report/*` → 404 |
| UI | once-URL autocomplete/spellcheck off |
| README | Hardening status note |

## 4. Runtime Sync

Copied exact allowlisted mirrors only. `.env.local` untouched. No broad sync. No artifact sync.

## 5. Token / Public Route Hardening

| Topic | Result |
|-------|--------|
| Token format | 64 hex only |
| Malformed denial | 404 (`nothex`, short, path, encoded sep) |
| Invalid 64-hex | 404 |
| Revoked | 410 |
| Path/checksum/PDF | via `validateReadyArtifact` |
| Headers | required + Pragma/Expires/Referrer-Policy |
| Plaintext redaction | not in DB; not in report; once UI only |

## 6. Eligibility / UI

| Export | Shareable |
|--------|-----------|
| id 1 | no (HTML + legacy) |
| id 2 | no (legacy PDF) |
| id 3 | no (HTML) |
| id 4 | yes (styled PDF v2) |

One-time URL shown once; no token_hash/path in share UI.

## 7. DB Validation

| Metric | After |
|--------|-------|
| Shares | **3** revoked (ids 1–2 preserved; id 3 hardening smoke revoked) |
| Active | **0** |
| Access on hardening share | **1** after successful GET; unchanged on denials/revoke GET |
| Plaintext token in DB | **no** (hash only) |
| Business / report_exports | **unchanged** |
| DELETE/DROP/TRUNCATE | **none** |

## 8. Artifact Validation

| Artifact | SHA-256 | Magic |
|----------|---------|-------|
| v1 HTML | `c194c62b…626fadc4` | n/a |
| v1 PDF | `707e72d6…880d0320` | `%PDF` |
| v2 HTML | `27a6eee6…95f6ffe` | n/a |
| v2 PDF | `a8c4d61c…41a56b6b` | `%PDF` |

No new artifacts. No public artifact files.

## 9. HTTP / Regression

| Item | Value |
|------|-------|
| Server | PHP `-S 127.0.0.1:8092` + `-d session.save_path` Laragon tmp |
| Auth | session injection (no password/session/token printed) |
| Summary | **66/66 PASS** (65 on first full run + 1 UI-hash assertion recheck after excluding CSRF false positive; token unit **9/9**) |
| Public token | **[REDACTED]** — created, streamed, revoked |
| `/share` | 404 |
| `/r/test` | 404 |

## 10. Restrictions Confirmed

All charter restrictions confirmed: no production/remote DB; no real data beyond fixture; no credentials/password/hash/session/plaintext token in report; no `.env` commit; no source `.env.local`; no schema/migration/db-migrate; no auth/health/fixture-tool edits; no business/export row mutation; no artifact overwrite; no public webroot artifact writes; no prune of existing revoked rows; no active long-lived share left; no DELETE/DROP/TRUNCATE; no package install; no vhost/hosts/service restart; no demo/registry; no push/fetch/pull/reset/clean/stash; no broad git add.

## 11. Documentation

- Result: `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md`
- OPERATIONAL-INDEX updated
- This closeout report

## 12. Commit

| Field | Value |
|-------|-------|
| Exact-path git add | yes (allowlist only) |
| Staged list | see post-commit verification |
| Primary commit | `a453ecd0138febe4cf2fa2d90ff86e8cd450e940` — `fix(iseo-report-hub): harden public report share links` |
| Hash-record commit | `60b3ffcc169fffcdd5ed80261459aa755bb8dfa3` — `docs(iseo-report-hub): record public report share hardening commit hash` |
| HEAD verification | after commits |
| Push | **no** |

## 13. SAFE UNKNOWN

- Apache `:80` / Laragon vhost state during `:8092` smoke not re-probed.
- Revoked smoke rows (now 3) not pruned; needs separate DB charter.

## 14. Recommended Next Action

I-SEO Report Hub — Report Delivery Public Share Visual QA 01

## 15. Files Changed

**Git (Active Brain):**

- `projects/iseo-report-hub/app-source/app/Support/SafeToken.php`
- `projects/iseo-report-hub/app-source/app/Services/ReportExportShareService.php`
- `projects/iseo-report-hub/app-source/app/Repositories/ReportExportShareRepository.php`
- `projects/iseo-report-hub/app-source/app/Controllers/PublicReportShareController.php`
- `projects/iseo-report-hub/app-source/app/routes.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-export-shares/index.php`
- `projects/iseo-report-hub/app-source/README.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-PUBLIC-SHARE-HARDENING-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-delivery-public-share-hardening-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

**Runtime (not Git):** mirrors of the seven app-source files above under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`.

**DB:** +1 `report_export_shares` row (id 3, revoked); access_count=1 on that row.

## 16. Git Actions

| Action | Done? |
|--------|-------|
| Exact-path git add | yes (worktree) |
| Commit | yes (primary + hash-record) |
| Push | **no** |
| Fetch / pull | **no** |
| Checkout / update-ref | yes if needed for worktree→main alignment |
| Reset / restore / clean / stash | **no** (except scoped restore if required for i-SEO alignment) |
| Broad git add | **no** |
| Clean temporary worktree | used for commit |
