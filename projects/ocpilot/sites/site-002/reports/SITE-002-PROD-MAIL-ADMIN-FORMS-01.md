# REPORT — SITE-002 Mail Admin Forms

**Operation ID:** SITE-002-PROD-MAIL-ADMIN-FORMS-01
**OCPilot Run:** 4.224 — SITE-002 Mail Admin Forms
**Date:** 2026-07-08
**Environment:** PRODUCTION (`https://bzpm.ru/`)
**Baseline before:** SITE-002-STABLE-PROD-MAIL-DESIGN-SYSTEM-01
**Checkpoint after:** SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01

---

## 1. Scope

Controlled production implementation: connect shared `ZpmMailRenderer` to admin emails from `checkout/anketa.php` and add service info block.

- Admin form emails in unified ЗПМ style
- Service info: IP, device, browser, User-Agent, referrer, page URL, date/time, dialog, UTM (if present), city = unknown
- Preserve `config_mail_alert_email` recipients
- Fix JSON success-before-send
- No customer copy; no standard OpenCart mail changes; no SMTP/admin/DB changes

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` @ `6c36d6ba` |
| Staged changes before task | **None** scoped to this operation |
| Foreign WIP | Present elsewhere — **not staged** |
| STOP tokens | **None** |

---

## 3. Source authority confirmation

FTP read-only + `source-before/` downloads.

| Path | Exists | Mod overlay | Touch |
|------|--------|-------------|-------|
| `/public_html/catalog/controller/checkout/anketa.php` | yes | no | **yes** |
| `/public_html/system/library/zpm/mail_renderer.php` | yes | no | compatibility |
| `/storage/modification/catalog/controller/checkout/anketa.php` | no | — | no |
| `/storage/modification/system/library/zpm/mail_renderer.php` | no | — | no |

**Confirmed:** anketa is live route; no modification overlay; renderer exists; recipients from `config_mail_alert_email`; dialogs 1/2/3/5/7; JSON success was echoed before send (fixed).

Storage: `manifests/source-authority-map.{csv,json,md}`

---

## 4. Live before snapshot

HTTP GET only — no submits.

| URL | HTTP | zpm-forms | CSRF | reCAPTCHA |
|-----|------|-----------|------|-----------|
| `/` | 200 | yes | yes | yes |
| `/katalog` | 200 | yes | yes | yes |
| `/katalog/.../stoly` | 200 | yes | yes | yes |
| PDP sample | 200 | yes | yes | yes |

Storage: `http-before/form-pages-before.{md,json}`

---

## 5. Implementation design

- Load `ZpmMailRenderer` via `require_once(DIR_SYSTEM . 'library/zpm/mail_renderer.php')`
- `renderAdminForm()` for HTML + text
- Subject: `ЗПМ: новая заявка — {dialog_label}`
- Service info via `zpmBuildServiceInfo()` + local UA parser (no external API)
- City: `unknown` (no GeoIP)
- JSON `ok: true` only after mail send attempt
- Graceful fallback to minimal HTML if renderer missing

Storage: `manifests/implementation-design.{md,json}`

---

## 6. Patch plan and rollback

| File | SHA before (remote) | Action | Rollback |
|------|---------------------|--------|----------|
| `checkout/anketa.php` | captured in `source-before/` | overwrite | re-upload `source-before` |
| `mail_renderer.php` | captured | service-info field map extension | re-upload `source-before` |

Storage: `rollback/rollback-plan.md`, `rollback/remote-before-manifest.json`

---

## 7. Local patch summary

| File | Change |
|------|--------|
| `tools/checkout_anketa_mail_admin_forms.php` | Patched anketa source (repo) |
| `tools/mail_renderer.php` | Extended `componentServiceInfo` map (browser, device, OS, proxy headers) |
| `tools/site-002-prod-mail-admin-forms-01.py` | Operation orchestrator |

Static checks: renderer integration, service info, JSON-after-send, no customer copy, no БЗПМ, no GeoIP — **PASS**

Storage: `patch/patch-summary.md`, `patch/diff-anketa.diff`, `patch/diff-mail-renderer.diff`

---

## 8. Local mail preview QA

**PASS**

| Check | Result |
|-------|--------|
| HTML + text generated | yes |
| ЗПМ present | yes |
| БЗПМ absent | yes |
| Service info block | yes |
| city = unknown | yes |

Storage: `mail-after/admin-form-mail-preview.{html,txt,json}`, `verification/local-mail-preview-qa.{md,json}`

---

## 9. Dry-run gates

**All 12 gates PASS** (G1–G12)

Storage: `manifests/dry-run.{md,json}`

---

## 10. Controlled deploy

**UPLOADED AND VERIFIED**

| Remote path | Local SHA = Remote SHA |
|-------------|------------------------|
| `/public_html/catalog/controller/checkout/anketa.php` | `f1a0714e…` verified |
| `/public_html/system/library/zpm/mail_renderer.php` | `e8d24944…` verified |

Storage: `verification/upload-manifest.{csv,json}`, `verification/remote-after-sha.json`

---

## 11. Controlled test submit

**PASS (application-side)**

| Item | Value |
|------|-------|
| Method | Playwright browser-context `fetch` to `checkout/anketa` with live CSRF + reCAPTCHA v3 |
| Dialog | 2 (обратный звонок) |
| Marker | `MARS TEST MAIL ADMIN FORMS 01` |
| Phone | `+7 000 000-00-00` |
| HTTP status | 200 |
| Response | `{"ok": true, "message": "Заявка отправлена"}` |
| Submits | **1** (charter limit) |

**Mailbox delivery:** **SAFE UNKNOWN** — operator visual confirmation of admin inbox pending.

Storage: `test-submit/test-submit-{request-redacted,response,summary}.{json,md}`

---

## 12. Live verification after

**PASS**

| URL | HTTP | Notes |
|-----|------|-------|
| `/` | 200 | no public БЗПМ |
| `/katalog` | 200 | OK |
| neutral hub | 200 | OK |
| `/stoly` | 200 | Load More present |
| PDP sample | 200 | extra-info present |
| `/llms.txt` | 200 | UTF-8 BOM; ЗПМ |
| `/robots.txt` | 200 | OK |
| `/sitemap.xml` | 200 | URL count recorded |

Storage: `verification/live-sanity.{md,json}`

---

## 13. Mail behavior summary

| Aspect | After |
|--------|-------|
| Handler | `checkout/anketa.php` |
| Body | `ZpmMailRenderer::renderAdminForm()` HTML + text fallback |
| Subject | `ЗПМ: новая заявка — {dialog}` |
| Recipients | `config_mail_alert_email` loop (unchanged) |
| Customer copy | none |
| JSON timing | success after send attempt |

---

## 14. Service info summary

Fields in admin email service block:

- IP / REMOTE_ADDR
- X-Forwarded-For, X-Real-IP, CF-Connecting-IP (when present)
- User-Agent, browser, device, OS (local parser)
- Referrer, page URL
- submitted_at, dialog ID
- UTM (from POST or referrer query)
- city: **unknown**

---

## 15. Privacy / security notes

- No SMTP/DB credentials in artifacts
- No recipient addresses printed
- Test data uses `test@example.invalid` and explicit marker
- Service info admin-only (renderer customer methods unchanged)
- reCAPTCHA + CSRF preserved

---

## 16. Brand regression check

| Check | Result |
|-------|--------|
| Admin subject uses ЗПМ | yes |
| Public БЗПМ introduced | **no** |
| Preview / mail HTML БЗПМ | **no** |

---

## 17. Rollback status

**Not required** — deploy and test submit passed.

Rollback bundle ready: re-upload `source-before/` exact files.

---

## 18. Production mutation summary

| Metric | Value |
|--------|------:|
| Remote uploads | 2 |
| Remote overwrites | 2 |
| Remote deletes | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Mail sends | 1 (controlled test) |
| Form submits | 1 |
| SMTP config changes | 0 |
| Live mail trigger changes | `checkout/anketa.php` only |
| Shared helper changes | `mail_renderer.php` (service-info fields) |
| Customer copy changes | 0 |
| Standard OpenCart mail changes | 0 |
| Header/footer/Yandex changes | 0 |
| Sitemap/robots/llms changes | 0 |
| Cache clears | 0 |
| External GeoIP/API calls | 0 |
| public БЗПМ introduced | no |

---

## 19. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-MAIL-ADMIN-FORMS-01\`

Checkpoint copy: `production/baselines/SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01\`

---

## 20. Authority updates

- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) — Run 4.224
- [OCPILOT-STATE.md](../../OCPILOT-STATE.md)
- [production-profile.md](../production-profile.md)
- [site-passport.md](../site-passport.md)
- [SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](../knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
- [tools/README.md](../tools/README.md)
- [SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01.md](../baselines/SITE-002-STABLE-PROD-MAIL-ADMIN-FORMS-01.md)

---

## 21. Git status

Selective commit planned for repo docs/tools only. Storage artefacts not committed.

---

## 22. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Admin mailbox visual confirmation of styled email | **SAFE UNKNOWN** |
| PHP CLI syntax lint on operator workstation | **SAFE UNKNOWN** (static inspection clean) |
| SMTP transport error surfacing to visitor | suppressed by design |

---

## 23. Final verdict

**SITE-002 MAIL ADMIN FORMS PARTIAL — DEPLOYED, MAILBOX DELIVERY CONFIRMATION PENDING**

Application path verified: renderer integration live, controlled test submit `ok: true`, live sanity PASS. Operator should confirm admin inbox shows ЗПМ-styled email with service info block.

---

## 24. Next task recommendation

**SITE-002-PROD-MAIL-CUSTOMER-FORMS-01** — optional customer confirmation emails for forms (no service info in customer copy).

Then: account transactional → order transactional mail redesign stages.

---

## Addendum — Operator inbox confirmation

**Date:** 2026-07-08
**Follow-up operation:** SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01 (OCPilot Run 4.225)

**Confirmation:** Mailbox delivery, email design, service info block, and admin-side data confirmed by operator after controlled test submit from Run 4.224 (marker `MARS TEST MAIL ADMIN FORMS 01`). No issues reported.

**Updated operational interpretation:** Run 4.224 is now treated as **operator-verified complete** for admin form mail redesign. Original §23 verdict at report time remains accurate historical record (mailbox was pending then).

**Follow-up report:** [SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01.md](SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01.md)

