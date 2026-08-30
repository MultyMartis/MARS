# I-SEO Report Hub — Report Delivery Client Handoff UX Visual QA Result v0.1

## 1. Status

| Field | Value |
|-------|-------|
| Verdict | **PASS** |
| Evidence folder | `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-handoff-ux-visual-qa-01\` (STORAGE only; not Git) |
| Final DB share state | `report_export_shares` **6** (ids **1–5** prior revoked preserved + id **6** visual-qa smoke revoked) |
| Active share count | **0** |
| Artifact checksums unchanged | **yes** |
| Smoke result | **129/129 PASS** (`127.0.0.1:8092`; session injection; no plaintext token printed) |

## 2. Scope

| Area | Covered |
|------|---------|
| Screens / routes | Export list; export detail ids **1–4**; shares page id **4**; handoff readiness panel; create once-URL + RU copy pack; revisit; revoke; auth downloads **1–4** |
| Copy pack | Short messenger / formal email subject+body / internal note — once with public URL; redacted in evidence |
| Public route | `GET /share/report/{token}` success stream; revoked **410**; malformed/invalid **404**; `/share` **404**; `/r/test` **404** |
| Token redaction | Plaintext token never printed in smoke log/docs; evidence uses `[REDACTED_64HEX_TOKEN]`; evidence not committed |
| Prior Visual QA minors | `UI-REL-STORAGE-PATH` and `UI-LIST-SHARE-LABEL` re-checked as resolved |

## 3. Internal UI Findings

| Screen | Result |
|--------|--------|
| Export list | Ids **1–3** show **Not shareable** (not ambiguous **No**); id **4** shows **Shareable** |
| Export id **1** | **Not shareable**; reason: Only styled PDF exports can be shared; handoff panel present; not delivery ready; no copy pack |
| Export id **2** | **Not shareable**; reason: Template metadata is required; legacy PDF; not delivery ready; no copy pack |
| Export id **3** | **Not shareable**; reason: Only styled PDF exports can be shared; not delivery ready; no copy pack |
| Export id **4** | **Shareable**; handoff readiness panel + checklist (report finalized / snapshot / styled PDF / shareable / active share / once URL / no bad link); relative storage path only under technical `<details>`; no path in handoff/copy areas |
| Shares page | Handoff panel visible; revoked rows readable; create CTA **Create share for handoff** when no active share; no `token_hash` / IP-UA hashes / absolute path |
| Create once-URL | Shown once; RU copy pack visible; readonly + autocomplete=off + spellcheck=false; copy buttons present |
| Copy pack | Short / email / internal contain redacted public URL; internal note references export/share status; no token_hash; no storage path |
| Revisit | once URL + copy pack gone; RU revoke+recreate guidance (`handoff-once-gone`) visible while active share exists |
| Revoke | Status → revoked; create CTA returns; active count **0**; public URL **410** |
| Leak checks | No `token_hash`, no IP/UA hashes, no absolute path, no relative storage path in client/handoff/copy areas |

## 4. Public Route Findings

| Case | Result |
|------|--------|
| Valid token stream | **200**; body starts `%PDF`; no HTML landing/wrapper; no storage path |
| Headers | Content-Type PDF; Content-Disposition attachment; Content-Length; nosniff; private/no-store; noindex/nofollow; Pragma; Expires; Referrer-Policy |
| Malformed tokens | `nothex`, short hex, path-like, encoded separator → **404** |
| Invalid 64-hex | **404** |
| Revoked token | **410**; no token/export/path detail leak |
| `/share` | **404** |
| `/r/test` | **404** |

## 5. Evidence

STORAGE-only under `X:\AI MARS STORAGE\incoming\iseo-report-hub\client-handoff-ux-visual-qa-01\`:

- `ui-exports-list.html`
- `ui-export-detail-1.html` … `ui-export-detail-4.html`
- `ui-export-detail-4-handoff-panel.html`
- `ui-shares-id4-before-create.html`
- `ui-shares-id4-handoff-panel-before.html`
- `ui-shares-id4-once-url-REDACTED.html`
- `ui-copy-pack-REDACTED.html`
- `copy-pack-short-REDACTED.txt`
- `copy-pack-email-REDACTED.txt`
- `copy-pack-internal-REDACTED.txt`
- `ui-shares-id4-after-access-no-once.html`
- `ui-shares-id4-after-revoke.html`
- `public-token-200-headers-REDACTED.txt`
- `public-token-200-pdf-magic.txt`
- `public-revoked-410-REDACTED.txt`
- `public-malformed-nothex-404.txt`
- `public-invalid-64hex-404.txt`
- `public-share-root-404.txt`
- `public-r-test-404.txt`
- `db-final-validation.json`
- `db-after-validation.json`
- `issues-summary.json`
- `http-visual-qa-results.txt`
- `http-visual-qa-results-full.txt`
- `http-visual-qa-smoke.php` (harness; outside Git)

No plaintext token in evidence filenames or committed docs. Browser PNG screenshots not captured (no browser install in charter); HTML/header/body captures used as visual evidence.

## 6. DB / Artifact Validation

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 9 | 9 |
| tables | 16 | 16 |
| report_exports | 4 | 4 |
| report_export_shares | 5 | 6 |
| active shares | 0 | 0 |
| revoked shares | 5 | 6 |
| business counts | unchanged | unchanged |

Artifacts: v1/v2 HTML/PDF checksums match expected; PDFs begin `%PDF`; no public artifact files; no new artifacts.

## 7. Issues

No BLOCKER / MAJOR / MINOR found.

Prior Public Share Visual QA minors re-validated as resolved:

| Prior ID | Status | Notes |
|----------|--------|-------|
| UI-REL-STORAGE-PATH | **resolved** | Relative path only inside technical `<details>` summary; absent from handoff/copy/client-facing areas |
| UI-LIST-SHARE-LABEL | **resolved** | List badge wording is **Not shareable** (aligned with detail) |

**BLOCKER:** 0 · **MAJOR:** 0 · **MINOR:** 0

## 8. Restrictions

- No production/remote DB
- No real client data beyond existing LOCAL_FIXTURE_ONLY exports
- No plaintext token in DB/report
- No absolute/raw storage path in public response or client copy
- No public artifact files
- No `report_exports` / business row mutation
- No artifact regeneration/overwrite
- No app-source / runtime code edits
- No package install; no secrets in Git
- No prune of existing revoked rows; no long-lived active share left
- No public landing / client portal / email automation / DB-11

## 9. Next Phase

**I-SEO Report Hub — Report Delivery Production Readiness Charter 01**

## 10. SAFE UNKNOWN

- Apache `:80` / Laragon vhost state during `:8092` Visual QA smoke not re-probed.
- Six revoked smoke rows remain (ids 1–6); pruning needs a separate DB charter.
- Pixel PNG browser screenshots not produced in this wave (HTML evidence only).
