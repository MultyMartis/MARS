# REPORT — FP-0002 P18E-E/F Form Goal + Policy Integration

## 1. Status

PASS

P18E-E/F is functionally complete on production. Final legal approval remains pending and indexing remains closed.

## 2. Olya/Admin Intake

Required: P18E-E/F CURRENT OLYA / ADMIN PRODUCTION TRUTH VERIFIED

Fresh read-only intake was captured before mutation in `REPORTS/evidence/prod-p18e-ef-form-goal-policy-integration/01-olya-admin-intake.json`.

Verified current production truth included:

- `blog_public=0` and indexing still closed;
- Cookie Policy owner = live page `#24`;
- Yandex Metrika counter owner remains current SEO/Admin settings (`98284776`);
- current Admin/privacy/dashboard truth lagged behind runtime before this wave;
- recent Activity Log confirmed live editorial/admin movement and was treated as canonical DB truth.

## 3. Form Goal Reality

Required: CURRENT FORM GOAL RUNTIME PATH PROVEN

Proven runtime path before/after final patch:

1. frontend submit posts AJAX lead request;
2. backend validates, persists lead, attempts mail, returns accepted success;
3. frontend success handler in `WORDPRESS/theme/shpigovsky/assets/js/v9-shell.js` receives success payload;
4. `fireMetrikaGoal()` runs only after accepted success;
5. goal/counter source of truth remains existing form/settings ownership;
6. no personal form payload is intentionally attached to `reachGoal`.

## 4. Consent Integration

Required: FORM GOAL EXECUTION IS CONSENT-GATED AFTER BACKEND SUCCESS  
Required: FORM ANALYTICS USES CANONICAL PRIVACYCONSENT STATE  
Required: NO METRIKA FORM GOAL WITHOUT ANALYTICS CONSENT

Implemented:

- `v9-shell.js` now gates form-goal attempts through `FP02PrivacyConsent.isAllowed('analytics')`;
- missing `window.ym`, blank goal, blank counter, or revoked analytics produce a no-op;
- form success UX remains successful regardless of analytics availability.

## 5. Idempotency

Required: FORM GOAL ATTEMPT IS IDEMPOTENT PER ACCEPTED SUBMISSION

Implemented with per-submission token dedupe in the form success path. One accepted frontend submission can produce at most one goal attempt.

## 6. Goal Payload

Required: METRIKA GOAL PAYLOAD CONTAINS NO IDENTIFYING FORM DATA

Confirmed source path sends only `counter` + `goal` through `ym(counter, 'reachGoal', goal)`. No name, phone, email, message, or lead identifier is intentionally passed from the form runtime.

Note: live Yandex network traffic may still contain provider-side instrumentation outside our explicit goal payload. This wave did not add personal fields to the goal call itself.

## 7. Consent Separation

Required: FORM PERSONAL-DATA CONSENT REMAINS INDEPENDENT FROM ANALYTICS CONSENT

Preserved. The form consent checkbox remains required for form submission, while analytics consent remains a separate browser privacy choice owned by `PrivacyConsent`.

## 8. Reopen Entry

Required: VISITOR CAN REOPEN COOKIE SETTINGS AFTER INITIAL DECISION  
Required: COOKIE SETTINGS REOPEN ADDED WITHOUT OVERWRITING OLYA FOOTER CONTENT

Implemented a permanent visitor-facing footer button `Настройки cookie` in the technical footer template. It reopens the existing consent settings UI and does not overwrite editor-owned menu DB state.

## 9. Change / Withdrawal

Required: REOPENED SETTINGS CAN CHANGE CONSENT EFFECTIVELY  
Required: WITHDRAWAL BLOCKS BOTH FUTURE METRIKA AND FUTURE FORM GOALS  
Required: RE-GRANT RESTORES ANALYTICS WITHOUT DUPLICATE INITIALIZATION

Verified by live QA:

- necessary-only reopen reflects analytics toggle OFF;
- analytics ON -> OFF saves `fp02_cookie_consent` with `analytics=false`;
- future page analytics and future form-goal attempts are blocked after withdrawal;
- re-grant restores one consent-gated Metrika loader without duplicate script injection.

## 10. Cookie Policy

Required: CURRENT COOKIE POLICY OWNER AND STATUS PROVEN  
Required: CONSENT UI AND FOOTER POINT TO ONE CURRENT COOKIE POLICY

Current owner/page was proven by fresh intake and updated in place. Evidence:

- before: `cookie-policy-before.json`
- after content source: `cookie-policy-after.html`
- deploy proof: `02-deploy-snapshot.json`

Updated policy content now factually describes:

- `fp02_cookie_consent`;
- Yandex Metrika;
- consent-gated analytics behavior;
- how to reopen settings via `Настройки cookie`;
- how to withdraw analytics consent later;
- `sessionStorage['fp02_utm']` disclosure boundary;
- relationship to privacy/personal-data documents.

Policy status remains: CURRENT / NEEDS LEGAL REVIEW.

## 11. Legal UX

Required: COOKIE ANALYTICS CONSENT AND FORM PERSONAL-DATA CONSENT REMAIN DISTINCT IN LEGAL UX

Preserved. Cookie/analytics consent stays in the consent UI and Cookie Policy. Form processing consent remains part of the form/legal processing path and was not merged into analytics consent.

## 12. Necessary-Only Form QA

Required: FORM SUBMIT PASSES WITHOUT ANALYTICS AND WITHOUT GOAL

Live QA PASS. Evidence in `03-live-qa.json`:

- success text returned;
- `ymCalls=[]`;
- `metrikaRequests=[]`;
- `pageErrors=[]`.

## 13. Analytics-Allowed Form QA

Required: FORM GOAL ATTEMPT OCCURS ONLY AFTER BACKEND SUCCESS AND ANALYTICS CONSENT

Live QA PASS. Evidence in `03-live-qa.json`:

- form success text preserved;
- consent-gated Metrika network activity present only with analytics allowed;
- no page errors;
- one Metrika script tag present.

## 14. Analytics Failure

Required: ANALYTICS FAILURE DOES NOT BREAK FORM SUCCESS

Live QA PASS. With analytics allowed but `mc.yandex.ru` aborted, the form still returned success text and no page error was recorded.

## 15. Goal SoT

Required: METRIKA GOAL SOURCE OF TRUTH REMAINS SINGLE

Preserved. Privacy code gates permission only; the goal identifier remains owned by the existing form/settings/Admin structure.

## 16. Evidence Model

Required: NO UNAPPROVED SERVER-SIDE CONSENT TRACKING INTRODUCED

PASS. No server-side consent evidence table or visitor-consent database was added in this wave.

## 17. Mobile / Accessibility

Required: COOKIE SETTINGS REOPEN MOBILE / ACCESSIBILITY QA PASS

Live QA PASS at `320`, `360`, `393`, `1280`:

- footer reopen entry reachable;
- settings panel opens;
- no horizontal overflow detected;
- desktop keyboard close returns focus to `Настройки cookie`.

## 18. Dashboard

Required: DASHBOARD REFLECTS FULL CURRENT PRIVACY RUNTIME TRUTH

Updated:

- Cookie consent = ACTIVE
- Metrika = CONSENT-GATED
- Form goal integration = CONSENT-GATED
- Cookie settings reopen = ACTIVE
- Cookie Policy = CURRENT / NEEDS LEGAL REVIEW
- Latest wave = P18E-E/F
- Indexing remains closed and waiting for Olya approval

## 19. Olya Safety

Required: OLYA CURRENT EDITORIAL STATE PRESERVED THROUGH P18E-E/F

PASS. Fresh intake was taken immediately before mutation. Footer/menu DB ownership, SEO settings, Metrika counter source, form settings, contacts content, and legal/editorial truth were preserved.

## 20. Indexing

Required: INDEXING REMAINS CLOSED

PASS. No indexing change was introduced in this wave.

## 21. Parity

Required: CODE PARITY PASS / EDITORIAL TRUTH PRESERVED

PASS for touched source-owned runtime files via exact deploy snapshot in `02-deploy-snapshot.json`. Editorial/legal page content remains canonical production truth and was updated only through the bounded Cookie Policy mutation in this charter.

## 22. Legal Review Remaining

- final Cookie Policy approval;
- browser-only evidence model sufficiency;
- consent lifetime/retention policy;
- final wording treatment for `sessionStorage['fp02_utm']`.

## 23. WP Forge Knowledge

Proven lessons confirmed by this wave:

- analytics-dependent conversion goals must obey the same consent state as analytics loading;
- form/business success must not depend on analytics availability;
- cookie settings must remain reopenable after the first decision;
- withdrawal must block both future analytics collection and future analytics goals;
- legal disclosure must follow actual runtime inventory and current consent behavior;
- technical privacy links should not require overwriting editor-owned footer content.

## 24. Git

- dirty main untouched;
- clean worktree used for implementation;
- exact staging required for commit/push;
- secret/privacy scan still required in final git wave.

## 25. Remaining Work

Expected if technical PASS:

- legal/operator review of final Cookie Policy wording;
- Olya indexing approval;
- sitemap submissions;
- final crawl.

## 26. Acceptance

FP-0002 P18E-E/F COMPLETE — FORM METRIKA GOALS NOW RESPECT THE SAME ANALYTICS CONSENT STATE AS YANDEX METRIKA LOADING — FORM SUCCESS REMAINS INDEPENDENT OF ANALYTICS — VISITORS CAN REOPEN COOKIE SETTINGS AFTER THEIR FIRST DECISION — WITHDRAWAL BLOCKS FUTURE METRIKA AND FUTURE FORM GOALS — RE-GRANT RESTORES ANALYTICS SAFELY — COOKIE POLICY LINKS AND RUNTIME DISCLOSURE ARE ALIGNED WITH ACTUAL DEPLOYED TECHNOLOGY — FORM PERSONAL-DATA CONSENT REMAINS SEPARATE FROM ANALYTICS CONSENT — OLYA'S CURRENT EDITORIAL WORK IS PRESERVED — SOURCE/PRODUCTION PARITY IS CONFIRMED — INDEXING REMAINS CLOSED
