# REPORT — FP-0002 PROD-P18E-CD Cookie UI + Metrika Gating

**Date:** 2026-08-19  
**Evidence:** `REPORTS/evidence/prod-p18e-cd-cookie-ui-metrika-gating/`

## 1. Status

**PASS**

P18E-C/D shipped the first real public cookie notice/settings UI together with genuine consent-gated Yandex Metrika runtime.

## 2. Fresh production/Admin truth

**CURRENT OLYA / ADMIN TRUTH PRESERVED**

- Current WP/Admin DB state was treated as canonical truth.
- No old DB snapshot was restored.
- No legal/editorial page text was rewritten in this wave.
- Fresh intake reconfirmed current cookie/legal pages last modified on 2026-08-18.

## 3. Live pre-mutation tracker reality

**DUPLICATE OWNER RISK PROVEN BEFORE MUTATION**

- Before deploy, public HTML still emitted Yandex Metrika immediately.
- Fresh bounded intake proved `options_custom_head_code` still contained a live Metrika snippet.
- Counter source of truth remained `options_yandex_metrica_counter_id` / `SEO и интеграции`.

## 4. Canonical owner

**ONE COOKIE CONSENT OWNER**

- Runtime owner: `Shpigovsky\Core\Privacy\PrivacyConsent`
- Scope now includes Admin settings, browser-state contract, frontend notice/settings UI, consent write path, and Metrika runtime gating.

## 5. Public UI

**PUBLIC VISITOR-FACING CONTROL LIVE**

- Compact public card with `Принять`, `Только необходимые`, `Настроить`
- Compact settings layer with `Необходимые` always on
- `Аналитика` toggle with `Яндекс Метрика` provider text
- Cookie-policy link preserved without rewriting policy content
- Mobile widths `320 / 360 / 390 / 768 / 1280` checked with no overflow in final QA

## 6. Consent record

- Cookie key: `fp02_cookie_consent`
- Schema: `version`, `necessary`, `analytics`, `decided_at`
- Cookie attributes: `Secure` on HTTPS, `SameSite=Lax`, `Path=/`, bounded `Max-Age`, `HttpOnly=false`
- Invalid/tampered payload => `UNDECIDED`
- Old version => re-decision required

## 7. Metrika gating

**REAL CONSENT GATING PROVEN**

- Unconditional theme Metrika bootstrap removed
- `custom_head_code` / `custom_body_open_code` / `custom_footer_code` are sanitized at render time to strip direct Metrika bypass snippets
- `noscript` Metrika bypass removed from the theme owner path
- Metrika now loads only from one idempotent frontend loader after explicit analytics consent
- Existing form-goal helper remains harmless when `window.ym` is absent

## 8. Contacts / Yandex map residual

**SECONDARY YANDEX TRACKING PATH CLOSED**

- Live QA exposed `mc.yandex.ru` requests on `/kontakty/` from auto-loaded Yandex map constructor embeds
- Those third-party embeds were replaced by a privacy-safe fallback block with explicit external opening instead of background auto-load
- After the fix, `necessary-only` navigation to `/kontakty/` produced `0` `mc.yandex.ru` requests

## 9. Live QA

Final browser-level evidence:

- undecided: banner visible, no consent cookie, `0` `mc.yandex.ru` requests
- accept: consent cookie `analytics=true`, banner closes, Metrika loads
- necessary-only: consent cookie `analytics=false`, banner closes, `0` requests
- custom on/off: both states persisted and matched expected request behavior
- tampered cookie: banner visible, `0` requests
- old version cookie: banner visible, `0` requests
- persistence: analytics allowed survives navigation; necessary-only stays analytics-free on navigation
- revoke: cookie flips back to `analytics=false`; post-revoke navigation remains analytics-free
- JS disabled: `0` active Metrika requests
- Escape closes settings layer

## 10. Admin / dashboard

- `Настройки сайта → Cookie и конфиденциальность` remains discoverable
- Dashboard now reports consent `ACTIVE`, categories `Necessary + Analytics`, and Metrika `CONSENT-GATED`
- Form-goal consent integration remains explicitly pending

## 11. Indexing / Olya safety

**INDEXING REMAINS CLOSED**

- `blog_public=0`
- no sitemap submission
- no indexing open
- no overwrite of Olya’s current editorial/Admin truth

## 12. Parity / deploy

**EXACT-FILE DEPLOY + PARITY PASS**

Touched runtime files matched source after deploy:

- `WORDPRESS/plugins/shpigovsky-core/shpigovsky-core.php`
- `WORDPRESS/plugins/shpigovsky-core/src/Admin/SystemDashboard.php`
- `WORDPRESS/plugins/shpigovsky-core/src/Privacy/PrivacyConsent.php`
- `WORDPRESS/plugins/shpigovsky-core/assets/css/privacy-consent.css`
- `WORDPRESS/plugins/shpigovsky-core/assets/js/privacy-consent.js`
- `WORDPRESS/theme/shpigovsky/assets/css/v9-style.css`
- `WORDPRESS/theme/shpigovsky/inc/seo-integrations.php`
- `WORDPRESS/theme/shpigovsky/template-parts/contacts/location-card.php`

Remote PHP lint: PASS for touched PHP files.

## 13. WP Forge knowledge

Promoted lessons:

- `PRIVACY-015` one canonical consent owner must also strip legacy/bypass analytics owners from operator code fields, not only replace the visible theme bootstrap
- `PRIVACY-016` browser-level QA must include other Yandex embeds (`map-widget` / constructor) because `mc.yandex.ru` traffic can survive after Metrika removal
- `PRIVACY-017` safe external-open fallback can preserve map access while eliminating silent third-party tracking before consent

## 14. Open items

- `P18E-E/F` form-goal consent gating + permanent footer/privacy reopen entry
- server-side consent evidence model
- final Cookie Policy legal review / text rewrite
- indexing approval by Olya/operator

## 15. Acceptance

**FP-0002 P18E-C/D COMPLETE — REAL PUBLIC COOKIE CONTROLS ARE LIVE — `UNDECIDED` AND `NECESSARY_ONLY` VISITORS REMAIN ANALYTICS-FREE — YANDEX METRIKA LOADS ONLY AFTER EXPLICIT ANALYTICS ALLOW — TAMPERED AND OLD-VERSION CONSENT FAIL CLOSED — REVOCATION RETURNS THE SITE TO ANALYTICS-FREE NAVIGATION — THE CONTACTS-PAGE YANDEX MAP TRACKING RESIDUAL IS CLOSED — FORMS CONTINUE TO WORK WITHOUT `window.ym` — OLYA’S CURRENT EDITORIAL/ADMIN STATE IS PRESERVED — EXACT-FILE SOURCE↔PRODUCTION PARITY IS VERIFIED — INDEXING REMAINS CLOSED**
