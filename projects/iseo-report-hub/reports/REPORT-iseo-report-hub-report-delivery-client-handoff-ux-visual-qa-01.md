# REPORT — I-SEO REPORT HUB REPORT DELIVERY CLIENT HANDOFF UX VISUAL QA 01

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `2f7b1ed2a0e48f7826ab55943f2f0365dcb41658` |
| Staged/index state | Foreign staged WIP present (client-ops); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree | **yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-delivery-client-handoff-ux-visual-qa-01\repo` (for docs commit) |
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
| report_export_shares before | **5** |
| Active shares before | **0** |
| Existing share status before | all **revoked**, export id **4** (ids 1–5) |
| Export ids 1–4 | ready; id **4** shareable; ids **1–3** not |
| Artifact checksums before | v1/v2 HTML/PDF match expected; PDFs `%PDF` |
| Runtime `.env.local` | present (contents redacted; not printed; not committed) |

## 3. QA Method

| Item | Value |
|------|--------|
| Server | PHP built-in `-S 127.0.0.1:8092 -t public` |
| Auth | session injection (no password/session/token printed) |
| Evidence folder | `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-handoff-ux-visual-qa-01\` |
| Capture method | HTML main/panel extracts + HTTP header/body text captures (no browser install) |
| Token redaction | once-URL / copy-pack evidence uses `[REDACTED_64HEX_TOKEN]`; docs never include plaintext token |

## 4. Internal UI QA

| Check | Result |
|-------|--------|
| Export list | **Not shareable** for ids **1–3**; **Shareable** for id **4**; prior ambiguous **No** badge gone |
| Id 1 | Not shareable — Only styled PDF exports can be shared; handoff panel; not delivery ready; no copy pack |
| Id 2 | Not shareable — Template metadata is required; not delivery ready; no copy pack |
| Id 3 | Not shareable — Only styled PDF exports can be shared; not delivery ready; no copy pack |
| Id 4 | Shareable; readiness checklist visible; storage path only under technical `<details>` |
| Shares page | Handoff panel; revoked rows readable; create CTA **Create share for handoff** |
| Once URL | Shown once after create; readonly; autocomplete=off; spellcheck=false; Copy button |
| Copy pack | RU short / email / internal; URL present once; no token_hash; no storage path |
| Revisit | once URL + copy pack gone; revoke+recreate guidance visible |
| Revoke | revoked status; create CTA returns; active **0** |
| Leak checks | no `token_hash` / IP-UA hashes / absolute path / path in handoff-copy areas |

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
| Landing/portal | **none** — direct PDF stream unchanged |

## 6. DB Validation

| Check | Result |
|-------|--------|
| Shares before/after | **5** → **6** |
| Final statuses | all **revoked** (ids 1–6) |
| Active final | **0** |
| Access count | incremented to **1** on successful public stream for QA row id **6** |
| Plaintext token in DB | **no** (hash only; 64 hex) |
| Existing ids 1–5 | preserved revoked |
| Business counts | unchanged (users/clients/projects/sites/snapshots/monthly/blocks/periods/weekly) |
| report_exports mutation | **none** |
| DELETE/DROP/TRUNCATE | **none** |

## 7. Artifact Validation

| Check | Result |
|-------|--------|
| v1 HTML | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` unchanged |
| v1 PDF | `707e72d65f253de17070980e2be36b91f59c4e6faf4352e73d3b1849880d0320` unchanged; `%PDF` |
| v2 HTML | `27a6eee6f6729f5a081865a24aa1e4ca1f94554ff38d4a1278682f16f95f6ffe` unchanged |
| v2 PDF | `a8c4d61c6216e8d70b193115faeab345c0c61ed25ee97a96b740f5f041a56b6b` unchanged; `%PDF` |
| New artifacts | **none** |
| Public artifact files | **none** |

## 8. Visual Verdict

| Field | Value |
|-------|-------|
| Verdict | **PASS** |
| Smoke | **129/129 PASS** |
| BLOCKER | **0** |
| MAJOR | **0** |
| MINOR | **0** |
| Prior minors | `UI-REL-STORAGE-PATH` + `UI-LIST-SHARE-LABEL` **resolved** (re-validated) |

Issue table: none.

## 9. Restrictions Confirmed

No production/remote DB; no real data beyond fixture; no credentials/password/hash/session/token in report; no `.env` committed; no source `.env.local`; no schema/SQL/migration/DB-11/delivery events; no db-migrate; no app-source/runtime/auth/health/fixture edits; no business/export/artifact mutation; no public webroot writes; no public landing/portal/email; no long-lived active share; no DELETE/DROP/TRUNCATE; no dump; no WP; no Composer/npm/package install; no vhost/hosts/restart; no demo/registry; no push/fetch/pull/reset/clean/stash; no broad git add.

## 10. Documentation

- Result: `product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md`
- OPERATIONAL-INDEX updated
- This closeout report

## 11. Commit

| Field | Value |
|-------|-------|
| Message | `docs(iseo-report-hub): add client handoff visual qa` |
| Staging | exact-path only (allowlisted) |
| Primary commit | `1431192bdfe27562d64ccc2d8d4f35ae9b4a382c` |
| Hash-record | `ef64f0226a03106f3d46282833d053b8800972bb` — `docs(iseo-report-hub): record client handoff visual qa commit hash` |
| Tip HEAD | `ef64f0226a03106f3d46282833d053b8800972bb` |
| Push | **no** |

## 12. SAFE UNKNOWN

- Apache `:80` state during `:8092` smoke
- STORAGE smoke script retention preference
- Six revoked smoke rows remain; pruning needs separate DB charter
- Pixel PNG browser screenshots not produced (HTML evidence only)

## 13. Recommended Next Action

**I-SEO Report Hub — Report Delivery Production Readiness Charter 01**

## 14. Files Changed

### Git (Active Brain)

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-DELIVERY-CLIENT-HANDOFF-UX-VISUAL-QA-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-delivery-client-handoff-ux-visual-qa-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

### STORAGE evidence (not Git)

- `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-handoff-ux-visual-qa-01\`

### DB / files summary

- DB: +1 revoked share smoke row (id **6**); active **0**; existing 5 revoked preserved
- Artifacts unchanged; no app-source/runtime code changes

## 15. Git Actions

| Action | Done? |
|--------|-------|
| exact-path git add | yes (worktree) |
| commit | yes (primary + hash-record) |
| push | **no** |
| fetch/pull | no |
| checkout/update-ref | yes if worktree path used |
| reset/restore/clean/stash | no |
| broad git add | no |
| clean temporary worktree | used for commit |
