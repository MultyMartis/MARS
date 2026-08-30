# I-SEO Report Hub — Report Delivery Public Share Visual QA Result v0.1

## 1. Status

| Field | Value |
|-------|-------|
| Verdict | **PASS_WITH_MINOR_ISSUES** |
| Evidence folder | `X:\AI MARS STORAGE\incoming\iseo-report-hub\public-share-visual-qa-01\` (STORAGE only; not Git) |
| Final DB share state | `report_export_shares` **4** (ids **1–3** prior revoked preserved + id **4** visual-qa smoke revoked) |
| Active share count | **0** |
| Artifact checksums unchanged | **yes** |
| Smoke result | **86/86 PASS** (`127.0.0.1:8092`; session injection; no plaintext token printed) |

## 2. Scope

| Area | Covered |
|------|---------|
| Screens / routes | Export list; export detail ids **1–4**; shares page id **4**; create once-URL; revisit; revoke; auth downloads **1–4** |
| Public route | `GET /share/report/{token}` success stream; revoked **410**; malformed/invalid **404**; `/share` **404**; `/r/test` **404** |
| Public headers | Content-Type PDF; Content-Disposition attachment; Content-Length; nosniff; private/no-store; noindex/nofollow; Pragma; Expires; Referrer-Policy |
| Token redaction | Plaintext token never printed in smoke log/docs; once-URL evidence saved only with `[REDACTED_64HEX_TOKEN]`; evidence not committed |

## 3. Internal UI Findings

| Screen | Result |
|--------|--------|
| Export list | Id **4** shows **Shareable**; ids **1–3** show blocked badge (**No**); Shares links present |
| Export id **1** | **Not shareable**; reason: Only PDF exports are shareable (HTML + legacy) |
| Export id **2** | **Not shareable**; reason: Template metadata is required (legacy PDF metadata NULL) |
| Export id **3** | **Not shareable**; reason: Only PDF exports are shareable (HTML) |
| Export id **4** | **Shareable PDF** / Eligible; create CTA when no active share; active count readable |
| Shares page | Revoked rows visible (status/created/access_count/expires); no `token_hash` / IP-UA hashes; no absolute path |
| Create once-URL | Shown once; `autocomplete=off`; `spellcheck=false`; Copy button present |
| Revoke | Status → revoked; create CTA returns; active count **0**; public URL **410** |
| Leak checks | No `token_hash`, no absolute storage path, no IP/UA hashes in share UI |

## 4. Public Route Findings

| Case | Result |
|------|--------|
| Valid token stream | **200**; body starts `%PDF`; no HTML wrapper; no storage path |
| Headers | All required hardening headers present (see smoke) |
| Malformed tokens | `nothex`, short hex, path-like, encoded separator → **404** |
| Invalid 64-hex | **404** |
| Revoked token | **410**; no token/export/path detail leak |
| `/share` | **404** |
| `/r/test` | **404** |

## 5. Evidence

STORAGE-only under `X:\AI MARS STORAGE\incoming\iseo-report-hub\public-share-visual-qa-01\`:

- `ui-exports-list.html`
- `ui-export-detail-1.html` … `ui-export-detail-4.html`
- `ui-shares-id4-before-create.html`
- `ui-shares-id4-once-url-REDACTED.html`
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
- `issues-summary.json`
- `http-visual-qa-results-full.txt`
- `http-visual-qa-smoke.php` (harness; outside Git)

No plaintext token in evidence filenames or committed docs. Browser PNG screenshots not captured (no browser install in charter); HTML/header/body captures used as visual evidence.

## 6. DB / Artifact Validation

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 9 | 9 |
| tables | 16 | 16 |
| report_exports | 4 | 4 |
| report_export_shares | 3 | 4 |
| active shares | 0 | 0 |
| revoked shares | 3 | 4 |
| business counts | unchanged | unchanged |

Artifacts: v1/v2 HTML/PDF checksums match expected; PDFs begin `%PDF`; no public artifact files; no new artifacts.

## 7. Issues

| ID | Severity | Finding | Evidence | Recommendation |
|----|----------|---------|----------|----------------|
| UI-REL-STORAGE-PATH | MINOR | Authenticated export detail shows **relative** `storage/exports/...` path (not absolute; not on public route; not on shares page) | `ui-export-detail-*.html` | Optional later UX: hide relative path from operator detail or label as internal-only relative key |
| UI-LIST-SHARE-LABEL | MINOR | Export list blocked badge wording is **No** while detail uses **Not shareable** | `ui-exports-list.html` | Align list badge copy with detail for operator clarity |

**BLOCKER:** 0 · **MAJOR:** 0 · **MINOR:** 2 (unique issue classes; relative-path observation repeated across ids 1–4)

## 8. Restrictions

- No production/remote DB
- No real client data beyond existing LOCAL_FIXTURE_ONLY exports
- No plaintext token in DB/report
- No absolute raw storage path in public response
- No public artifact files
- No `report_exports` / business row mutation
- No artifact regeneration/overwrite
- No package install; no secrets in Git
- No prune of existing revoked rows; no long-lived active share left

## 9. Next Phase

**I-SEO Report Hub — Report Delivery Client Handoff UX Charter 01**

## 10. SAFE UNKNOWN

- Apache `:80` / Laragon vhost state during `:8092` Visual QA smoke not re-probed.
- Four revoked smoke rows remain (ids 1–4); pruning needs a separate DB charter.
- Pixel PNG browser screenshots not produced in this wave (HTML evidence only).
