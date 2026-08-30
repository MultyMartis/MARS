# I-SEO Report Hub — Report Delivery Public Share Hardening Result v0.1

## 1. Status

| Field | Value |
|-------|-------|
| Status | **complete** |
| Hardening applied | **yes** |
| DB final state | schema_migrations **9**; tables **16**; `report_exports` **4** unchanged; `report_export_shares` **3** revoked (ids 1–2 preserved + id 3 hardening smoke) |
| Active shares final | **0** |
| Artifact checksums unchanged | **yes** |
| Smoke result | **66/66 PASS** (HTTP regression + token unit + fixed UI hash assertion recheck) |

## 2. Source Changes

| Path | Change |
|------|--------|
| `app-source/app/Support/SafeToken.php` | Exact 64-hex public token gate; `hashPublicToken()` only after validation |
| `app-source/app/Services/ReportExportShareService.php` | Strict token resolve; access record deferred; UI row sanitization (no hash/IP fields) |
| `app-source/app/Repositories/ReportExportShareRepository.php` | Access UPDATE guards: active + not expired + max_access |
| `app-source/app/Controllers/PublicReportShareController.php` | Stream headers hardened; access record after preflight; optional cache/referrer headers |
| `app-source/app/routes.php` | Public route matches exactly 64 hex; malformed `/share/report/*` → generic 404 |
| `app-source/app/Views/pages/report-export-shares/index.php` | Once-URL input `autocomplete=off` / `spellcheck=false` |
| `app-source/README.md` | Hardening status note |

## 3. Runtime Sync

Exact allowlist mirrors under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`:

- `app/Support/SafeToken.php`
- `app/Services/ReportExportShareService.php`
- `app/Repositories/ReportExportShareRepository.php`
- `app/Controllers/PublicReportShareController.php`
- `app/routes.php`
- `app/Views/pages/report-export-shares/index.php`
- `README.md`

`.env.local` untouched. No broad sync. No artifact sync.

## 4. Token Validation Hardening

| Rule | Policy |
|------|--------|
| Format | Exactly **64** `[a-fA-F0-9]` chars (`bin2hex(random_bytes(32))`) |
| Reject | empty; wrong length; non-hex; `/` `\` `.` `%`; null bytes; path-like |
| Hash timing | Hash only after `isValidPublicToken` / via `hashPublicToken()` |
| Malformed denial | **404** (route catch-all or service gate) |
| Plaintext | Never stored; shown once via session once-URL; redacted in reports |

## 5. Public Route Hardening

| Topic | Policy |
|-------|--------|
| Active | `status=active` and `expires_at > now` |
| Revoked / expired / max_access | **410** |
| Invalid / missing / ineligible / artifact fail | **404** |
| Artifact | Existing `validateReadyArtifact` (relative `storage/exports/reports`, checksum, `%PDF`, MIME) |
| Access count | Increments only after successful stream preflight (`recordSuccessfulPublicAccess`) |
| Headers | `Content-Type: application/pdf`; `Content-Disposition: attachment`; `Content-Length`; `X-Content-Type-Options: nosniff`; `Cache-Control: private, no-store`; `X-Robots-Tag: noindex, nofollow`; `Pragma: no-cache`; `Expires: 0`; `Referrer-Policy: no-referrer` |
| Path leak | Absolute path never in public response |

## 6. Internal UI Hardening

| Rule | Result |
|------|--------|
| No `token_hash` in UI | Sanitized share rows + smoke recheck |
| No raw storage path in share UI | Shares page does not show storage path |
| One-time plaintext URL | Session once-box; consumed on next GET |
| Active share | Create form hidden; revoke available; no plaintext regeneration |
| Revoked rows | Status badge visible |
| Eligibility | Ids 1–3 blocked with reason; id 4 eligible |
| CSRF | Remains on create/revoke POST |

## 7. DB / Artifact Validation

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 9 | 9 |
| tables | 16 | 16 |
| report_exports | 4 | 4 |
| report_export_shares | 2 revoked | **3** revoked |
| active shares | 0 | **0** |
| business counts | unchanged | unchanged |

Artifacts (SHA-256) unchanged; PDFs begin `%PDF`; no public artifact files.

## 8. HTTP Smoke

Server: PHP `-S 127.0.0.1:8092` with `-d session.save_path=…` (Laragon tmp). Auth: session injection (no password/session/token printed).

Assertions covered: health/login/404; export details 1–4 eligibility; shares list; create once-URL; public PDF stream + headers; malformed/invalid tokens 404; access_count exactly 1 then unchanged on denials; revoke → 410; deny create id 2/3; `/share` + `/r/test` 404; auth downloads 1–4; final active 0.

Token value: **[REDACTED]**.

## 9. Restrictions

Confirmed: no production/remote DB; no real data beyond fixture; no raw token in DB/report; no raw path in public response; no public files; no export/business mutation; no artifact changes; no package install; no secrets in Git.

## 10. What Still Does Not Exist

- client portal
- email delivery
- short `/r/{token}` route
- one-time token UX (beyond once-display)
- dedicated audit table
- rate limiter
- revoked smoke-row pruning
- production deployment

## 11. Next Phase

**Report Delivery Public Share Visual QA 01**

## 12. SAFE UNKNOWN

- Apache `:80` / Laragon vhost state during `:8092` smoke not re-probed.
- Two original revoked smoke rows remain (plus one hardening revoked row); pruning needs a separate DB charter.
