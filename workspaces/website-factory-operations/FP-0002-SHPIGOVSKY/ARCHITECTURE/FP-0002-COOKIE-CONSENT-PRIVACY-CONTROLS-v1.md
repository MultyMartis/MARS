# FP-0002 Cookie Consent / Privacy Controls v1

**Project:** FP-0002 "Шпиговский дом"  
**Wave:** PROD-P18E design/specification only  
**Status:** implementation-ready specification; not implemented  
**Date:** 2026-08-19

## 1. Intent

Build a **small first-party privacy control**, not a decorative banner and not a full CMP.

The subsystem must:

1. expose a real first-visit choice;
2. keep genuinely necessary mechanisms separate from analytics;
3. prevent Yandex Metrika from loading before analytics consent allows it;
4. preserve backend-confirmed form success semantics;
5. let the visitor reopen and change the choice later;
6. remain manageable through WordPress Admin;
7. preserve current editor/Admin production truth.

## 2. Current production truth

### Verified runtime

- public site: `https://shpigovsky.ru/`
- indexing: **closed**
- current Yandex Metrika counter: **`98284776`**
- current Metrika owner of truth: SEO/integration settings
- current forms owner: `ConsultationHandler` + `MailOps`
- current live legal pages:
  - `https://shpigovsky.ru/policy`
  - `https://shpigovsky.ru/cookie-files-policy/`
  - `https://shpigovsky.ru/consent-personal-data/`

### Verified behavioral gap

Current theme/runtime loads Metrika directly in `wp_footer`, which means:

```text
current state = analytics active before any cookie choice
```

Therefore:

```text
banner without runtime gating = non-compliant product behavior for this design goal
```

## 3. Legal/compliance posture

This specification is grounded in:

- current `152-FZ` consent requirements as a design input;
- Yandex Metrika official deferred-loading and opt-out capabilities;
- actual FP-0002 technology inventory;
- current live legal/documentation gaps.

It does **not** claim that Russian law mechanically equals GDPR/ePrivacy for every cookie.

### Legal decision boundary

The architecture is designed around the safer bounded model:

```text
analytics = consent-gated
necessary = always on if genuinely required
```

Unresolved legal-policy decisions remain:

- exact evidentiary model for consent records;
- final legal copy;
- exact consent lifetime;
- whether any future non-analytics category becomes justified.

Mark all of these:

```text
LEGAL REVIEW REQUIRED BEFORE IMPLEMENTATION
```

## 4. Product model

### Categories

P18E v1 uses the minimum justified category set:

1. `necessary`
2. `analytics`

No `marketing`, `personalization`, or `functional` category is introduced now because the current verified runtime does not justify them.

### Category rules

#### Necessary

Allowed:

- consent-state persistence;
- server-side form security/integrity required for a requested action;
- any truly required anonymous visitor technical mechanism later re-verified during implementation intake.

Not allowed:

- Yandex Metrika;
- analytics identifiers;
- analytics goals;
- future “we want metrics” loopholes.

#### Analytics

Includes:

- Yandex Metrika counter loading;
- Metrika cookies and browser storage;
- `reachGoal` after backend-confirmed form success.

## 5. First-visit UX

### Notice shape

- Desktop: compact floating bottom card, approx. `420–520px` wide, theme-integrated
- Mobile: near-full-width bottom card with safe margins and iOS safe-area support
- No full-screen modal
- No forced dark patterns

### Canonical copy concept

Title:

```text
Мы используем файлы cookie
```

Short text concept:

```text
Необходимые технологии помогают сайту работать корректно.
Аналитика используется только в соответствии с вашим выбором.
```

Policy link:

```text
Политика использования cookie
```

Primary actions, first level:

1. `Принять`
2. `Только необходимые`
3. `Настроить`

Requirement:

```text
ACCEPT AND NECESSARY-ONLY ARE BOTH DIRECTLY AVAILABLE
```

## 6. Settings UX

`Настроить` opens a compact settings panel.

### Structure

- `Необходимые` — state text: `Всегда включены`
- `Аналитика` — toggle on/off
- Description names the actual provider:
  - `Яндекс.Метрика`

Primary action:

```text
Сохранить выбор
```

### Accessibility behavior

- visible focus styles;
- keyboard reachable controls;
- screen-reader labels for switches/buttons;
- if modal presentation is used, focus moves into the panel and returns to the opener on close;
- `Escape` closes settings only when it behaves as a modal;
- simple notice mode must not trap focus.

## 7. State model

Internal state is machine-driven, not label-driven.

### Canonical states

- `UNDECIDED`
- `NECESSARY_ONLY`
- `ANALYTICS_ALLOWED`

### Stored record

Candidate first-party record name:

```json
{
  "key": "fp02_cookie_consent",
  "version": "v1",
  "necessary": true,
  "analytics": false,
  "decided_at": "ISO-8601 timestamp"
}
```

Rules:

- one minimal first-party consent record;
- no name/email/phone/IP/fingerprint inside the consent object;
- browser state is advisory for client-side gating, not an authentication artifact.

## 8. Consent versioning

The architecture must support:

```text
consent_version = v1
```

Reprompt only when the privacy model materially changes, such as:

- a new third-party analytics or tracking provider;
- a new consent-sensitive purpose/category;
- materially different processing behavior.

Do **not** reprompt for cosmetic wording edits alone.

## 9. Evidence model

Three models were assessed.

### A. Browser-only record

Pros:

- minimal data;
- low operational burden;
- easiest implementation.

Cons:

- weak evidence if the visitor clears storage;
- difficult for the operator to prove received consent later.

Use:

- technically viable for client-side gating;
- weaker for a consent-evidence posture.

### B. Server-side consent event record

Pros:

- strongest demonstrability;
- supports version/audit history.

Cons:

- creates a new data-processing surface;
- requires retention rules and minimization discipline.

Use:

- only if legal/operator review decides stronger evidence is needed.

### C. Hybrid

- browser record controls runtime immediately;
- server record stores a minimized event only if the operator chooses stronger evidence.

### Recommended direction

For P18E design:

```text
RECOMMENDED: HYBRID-READY ARCHITECTURE
DEFAULT IMPLEMENTATION START: browser record for runtime gating
SERVER EVIDENCE: legal/operator decision gate
```

Requirement:

```text
CONSENT EVIDENCE MODEL ASSESSED AGAINST RUSSIAN REQUIREMENTS
LEGAL REVIEW REQUIRED BEFORE IMPLEMENTATION
```

## 10. Yandex Metrika architecture

### Single source of truth

The current Metrika counter remains owned by existing SEO/integration settings.

Do not create:

- a duplicate counter id option;
- a second Metrika configuration owner;
- template-scattered conditional snippets.

### Required runtime semantics

```text
UNDECIDED         -> Metrika not loaded
NECESSARY_ONLY    -> Metrika not loaded
ANALYTICS_ALLOWED -> Metrika may load
```

### Required implementation shape

1. remove direct unconditional Metrika output from the always-run path;
2. move output behind one privacy/consent owner;
3. load the existing counter only after consent state allows analytics;
4. suppress both the JS tag bootstrap and the noscript watch pixel while analytics is disallowed.

Requirement:

```text
YANDEX METRIKA MUST NOT BE MERELY HIDDEN AFTER IT ALREADY TRACKED
```

## 11. Withdrawal behavior

Permanent footer link:

```text
Настройки cookie
```

If analytics changes from ON to OFF:

1. future Metrika loading must stop;
2. pre-init disable flag may be set:
   - `window['disableYaCounter98284776'] = true`
3. first-party analytics cookies under site control may be deleted on a best-effort basis;
4. a page reload may be required and should be explained honestly if used.

Do not promise deletion of data the site cannot technically control after prior transmission.

Requirement:

```text
CONSENT CAN BE WITHDRAWN THROUGH NORMAL SITE UI
```

## 12. Forms and goals

Current accepted semantic contract remains:

```text
BACKEND CONFIRMED FORM SUCCESS
-> optionally fire Metrika goal
```

P18E refines it to:

```text
BACKEND CONFIRMED FORM SUCCESS
-> analytics allowed?
   yes -> attempt ym(reachGoal)
   no  -> do nothing
-> form success remains unaffected
```

Rules:

- no goal on click;
- no goal before backend success;
- no analytics failure may break the form;
- no personal identifying form values in Metrika goal params unless separately proven allowed and intentionally designed.

Requirements:

```text
FORM ANALYTICS RESPECTS COOKIE CONSENT STATE
FORM PERSONAL-DATA CONSENT AND ANALYTICS CONSENT REMAIN SEPARATE
```

## 13. Storage and lifetime

### Browser storage choice

Preferred first implementation storage:

- first-party cookie **or** localStorage under one controlled consent owner.

Recommendation:

- use a first-party cookie for the actual consent state because it is easy to read early for gating;
- optionally mirror to JS memory after early bootstrap;
- do not rely on sessionStorage because the choice must persist across visits.

### Lifetime

No precise statutory consent lifetime was confirmed in bounded research.

Therefore:

```text
PRODUCT / LEGAL POLICY DECISION
```

Implementation recommendation:

- `6–12 months` practical lifetime;
- default recommendation for FP-0002: `12 months`, subject to legal approval.

## 14. Frontend technical owner

Create one privacy owner rather than scattering checks:

```text
PrivacyConsent / CookieConsent
```

### Responsibilities

- read/write consent state;
- expose `is_allowed('analytics')`;
- handle consent version comparison;
- render notice/settings UI;
- dispatch lifecycle events.

### Events

- `consent_ready`
- `analytics_granted`
- `analytics_revoked`

### Registry concept

```yaml
necessary:
  - consent_state
analytics:
  - yandex_metrika
```

Integrations register against categories; templates do not hand-roll privacy logic.

## 15. Admin information architecture

Future path:

```text
Настройки сайта
→ Cookie и конфиденциальность
```

### Minimal admin model

#### Баннер

- enabled
- title
- short description
- policy page/link
- consent version

#### Категории

- Necessary: fixed active, non-editable classification
- Analytics: enabled/disabled category, editor-visible description

#### Интеграции

- `Yandex Metrika -> Analytics`
- future discovered integrations listed read-only or selectively mapped

#### State

- consent system enabled/disabled
- current version
- detected integrations
- policy page status

### Ownership rule

Editor may change explanatory copy, but may **not** reclassify Metrika as necessary through ordinary content fields.

## 16. Policy page model

Candidate route:

```text
/cookie-policy/
```

Do not create it in this wave.

The approved future cookie policy must factually describe:

- what cookies/browser storage are;
- operator identity;
- categories used on the site;
- actual technologies and providers;
- purpose;
- approximate/known retention where factual;
- data recipients/providers;
- choice and withdrawal mechanism;
- browser deletion guidance;
- relation to privacy policy;
- current Yandex Metrika usage if deployed.

Current FP-0002 gap:

- live `cookie-files-policy` is production-owned but still generic/demo and not sufficient as final factual privacy control documentation.

All future legal copy remains:

```text
DRAFT / LEGAL REVIEW REQUIRED
```

## 17. Security and cache compatibility

### Security

- treat browser consent state as user-controlled input;
- validate `version` and categories;
- ignore unknown categories;
- never use browser consent state for privileged server authorization;
- sanitize all admin-editable strings.

### Cache

- full-page cache must remain shared;
- consent variation must be client-side only;
- no per-visitor cache variants are required for v1.

## 18. Accessibility, mobile, performance

### Accessibility

- semantic region for notice, dialog semantics for modal settings if used;
- visible focus;
- keyboard complete;
- 320px+ width;
- 200% zoom safe;
- reduced-motion safe;
- contrast aligned with site design.

### Mobile

- must not block primary CTA, menu, browser controls, or fixed header;
- safe-area padding on iOS;
- vertical button stack allowed on small screens.

### Performance

- read consent early;
- keep frontend bundle small;
- no analytics flash/race before state resolution;
- no giant third-party CMP by default.

## 19. Reusable module classification

Candidate reusable WP Forge module:

```text
PrivacyConsent / CookieConsent
```

Reusable boundaries:

- consent state;
- consent versioning;
- category registry;
- settings UI framework;
- integration gating API;
- Metrika adapter;
- admin settings skeleton;
- footer reopen link.

Project-specific boundaries:

- styling;
- copy;
- actual legal pages;
- actual provider inventory.

Maturity:

```text
THEORY / SPECIFICATION
NOT production-ready until P18E implementation passes
```

## 20. Acceptance matrix

Future implementation must pass at least:

- first visit: banner appears, Metrika absent
- accept: state saved, Metrika loads, banner hides
- necessary only: state saved, Metrika absent, forms still work
- reload/new page: choice persists
- settings reopen: current choice visible
- withdraw analytics: future analytics stops
- form without analytics consent: submission works, no goal
- form with analytics consent: submission works, backend success then goal attempt
- version change: reprompt only on material model change
- cookies disabled: site reasonably usable
- mobile 320px: no overflow or blocked CTA
- keyboard: all controls usable
- cache: one visitor choice does not leak to another

## 21. Implementation gate

Before any future P18E implementation:

1. fresh production intake again;
2. preserve Olya/Admin truth;
3. re-verify actual trackers and storage;
4. re-verify legal texts and slugs;
5. do not open indexing;
6. do not overwrite current SEO/Metrika settings;
7. do not mutate legal copy without explicit approved content wave.

## 22. Final principle

```text
DO NOT BUILD A DECORATIVE COOKIE BANNER.

BUILD A SMALL PRIVACY CONTROL THAT ACTUALLY CONTROLS
NON-ESSENTIAL ANALYTICS.
```
