# ISEO-SU FORM HMAC SECRET ROTATION EVIDENCE v1

## 1. Security Risk

Tracked current source previously contained active HMAC secret material in `production-source/forms/iseo-form-config.php`. Because the value entered Git, it was treated as potentially compromised even without proof of active abuse.

## 2. Previous Architecture

Before remediation, the shared form config stored recipients, thresholds, `test_mode`, and the active HMAC secret literal together in tracked source. Shared server logic in `iseo-form-security.php` consumed that value for timing-token signing/validation, IP hashing, and duplicate fingerprints.

## 3. Secret Usage Map

| File | Role | SECRET_REFERENCE_PRESENT | TRACKED / UNTRACKED | RUNTIME / SOURCE |
|------|------|--------------------------|---------------------|------------------|
| `production-source/forms/iseo-form-config.php` | tracked config / loader path | YES (pre-rotation), NO active literal after remediation | TRACKED | SOURCE |
| `production-source/forms/iseo-form-security.php` | shared server validation / HMAC consumer | YES (symbol reference only) | TRACKED | SOURCE |
| `production-source/forms/iseo-form-token.php` | token endpoint | indirect via shared server helper | TRACKED | SOURCE |
| `js/common.js` | client token fetch + hidden field inject | NO secret literal; receives only signed `{t,s,id}` token payload | TRACKED | SOURCE |
| `.iseo-form-runtime/iseo-form-secrets.local.php` | active HMAC authority | YES | UNTRACKED | RUNTIME |

## 4. New Secret Authority

Active HMAC authority moved to production-local PHP file:

- runtime path: `.iseo-form-runtime/iseo-form-secrets.local.php`
- protection: `.iseo-form-runtime/.htaccess` with deny rule
- tracked config behavior: `hmac_secret => null` plus `local_secret_path`
- fail policy: if local secret file is missing/unreadable, token issuance and HMAC-protected submission behavior fail closed

## 5. Rotation

- New HMAC secret generated from a cryptographically secure local generator (`token_hex(32)`).
- New value was written directly to local build artifact and deployed to the production-local authority file.
- Old tracked secret was not reused, derived, or printed.

## 6. Current Tracked Source State

- `production-source/forms/iseo-form-config.php` no longer contains active HMAC secret material.
- `production-source/forms/iseo-form-security.php` loads the local authority and validates presence before issuing/verifying tokens.
- `production-source/forms/iseo-form-token.php` returns `503 {"error":"unavailable"}` if the secret authority is unavailable.
- `production-source/forms/iseo-form-secrets.example.php` contains placeholder-only syntax (`null`), not a working secret.

## 7. Production Deployment

Scoped production mutation set:

1. `iseo-form-config.php`
2. `iseo-form-security.php`
3. `iseo-form-token.php`
4. `.iseo-form-runtime/.htaccess`
5. `.iseo-form-runtime/iseo-form-secrets.local.php`

Each file was uploaded with post-upload readback/checksum verification. Scoped rollback receipts and backup copies were stored under `X:\AI MARS\local\sites\iseo-su-production\_hmac-rotation-01\`.

## 8. Positive Form Test

- isolated `test_mode`: ON
- effective test recipient: `im.work@mail.ru` only
- representative valid submission: `callback__FORM.php`
- result: accepted (`true`)
- production recipient during the isolated positive test: **not used**

## 9. Negative HMAC Test

- representative stale/invalid signature test: `callback__FORM.php`
- result: rejected (`false`)
- mail expected: 0
- observed accepted send count from invalid HMAC test: 0

## 10. Recipient Isolation

During isolated validation:

- `test_mode` routed only to `im.work@mail.ru`
- normal production recipient set was not active for test sends
- `im.work@nail.ru` remained absent
- no CC/BCC path exists in the shared send helper

## 11. Production Recipient Restoration

Final production config state after test-mode disable:

- `test_mode`: OFF
- production recipient set: `nikel007i33@yandex.ru` only
- operator test mailbox present in production recipients: NO

## 12. Secret Exposure Checks

- active HMAC secret in current tracked source: NO
- active HMAC secret in `js/common.js`: NO
- token endpoint public payload: signed `{t,s,id}` only
- local secret file web access: blocked (expected deny behavior)
- current tracked forms source high-entropy literal scan: no active HMAC literal found

## 13. Git History Assessment

OLD SECRET MATERIAL IN HISTORY: YES

Risk classification:

- the old value was historically tracked, so repository history still contains revoked secret material
- the secret is no longer active after rotation
- no history rewrite was performed in this task
- immediate operational safety is restored by rotation + removal from current tracked source

## 14. Rollback

Rollback authority:

- scoped local backup/receipt set: `X:\AI MARS\local\sites\iseo-su-production\_hmac-rotation-01\backups\`
- deploy/verify receipts: `prepare-build-receipt.json`, `remote-baseline.json`, `deploy-rotation-receipt.json`, test-mode receipts, validation receipt

Rollback method:

1. restore backed-up production files from the scoped receipt set
2. restore prior runtime secret file only if intentionally rolling back the whole security wave
3. verify `test_mode=false` and recipient set

## 15. Final Security Decision

- ACTIVE SECRET ROTATED: YES
- ACTIVE SECRET IN TRACKED SOURCE: NO
- PRODUCTION SECRET AUTHORITY: LOCAL-ONLY
- HMAC VALIDATION: PASS
- FORM VALID SUBMISSION: PASS
- INVALID HMAC MAIL COUNT: 0
- TEST MODE: OFF
- PRODUCTION RECIPIENT: `nikel007i33@yandex.ru` only
