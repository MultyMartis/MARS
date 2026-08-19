# REPORT — FP-0002 PROD-P18E Cookie Consent / Privacy Controls Design

## 1. Status

**PASS**

Design/specification wave complete. No frontend cookie banner was implemented. No consent runtime was deployed. No Yandex Metrika runtime was changed. No production legal text was mutated. Indexing remains closed.

## 2. Current Tracker Reality

**P18E CURRENT PRODUCTION PRIVACY / TRACKER REALITY VERIFIED**

Fresh read-only intake confirmed:

- public site is `https://shpigovsky.ru/`;
- live homepage currently loads **Yandex Metrika counter `98284776`** directly on page load;
- current Metrika owner of truth is existing SEO/integration settings;
- form success logic already follows backend-confirmed success before optional Metrika goal attempt;
- public frontend also stores UTM values in `sessionStorage['fp02_utm']`;
- live legal pages exist at `policy`, `cookie-files-policy`, and `consent-personal-data`;
- current cookie policy is still generic/demo and itself states that a dedicated consent banner/panel is not implemented.

## 3. Russian Legal Basis

**RUSSIAN COOKIE / ANALYTICS COMPLIANCE BASIS VERIFIED**

Separated inputs:

- **Law:** `152-FZ` Article 9 supports explicit, informed, separable consent and a form that allows confirmation of receipt where consent is the legal basis.
- **Roskomnadzor enforcement/guidance signal:** current bounded evidence supports treating cookie/analytics disclosures and actual tracker behavior as a practical compliance surface; unresolved points are marked for legal review rather than guessed.
- **Yandex provider requirements/capabilities:** official docs support deferred loading, pre-init opt-out, and confirm that Metrika uses cookies plus browser storage.
- **Design recommendations:** for FP-0002 the safest compact model is Necessary vs Analytics, with Metrika blocked until analytics consent allows it.

Exact matrix: `REPORTS/evidence/prod-p18e-cookie-design/RU-LEGAL-BASIS-MATRIX.md`

## 4. Actual Inventory

**ACTUAL COOKIE / STORAGE / TRACKER INVENTORY COMPLETED**

Confirmed public-scope technologies:

- Yandex Metrika JS + noscript watch pixel
- Yandex Metrika cookies/localStorage/sessionStorage families as documented by Yandex
- FP-0002 first-party `sessionStorage['fp02_utm']`
- form security/nonce/hidden fields
- current form personal-data consent checkbox
- conditional Yandex map embed capability on contacts pages

No live GA/GTM/Facebook Pixel/Cookiebot/OneTrust/calltracking stack was confirmed on the inspected homepage.

Exact inventory: `REPORTS/evidence/prod-p18e-cookie-design/TRACKER-STORAGE-INVENTORY.md`

## 5. Consent Model

**MINIMUM JUSTIFIED CONSENT CATEGORIES DEFINED**

P18E v1 category set:

1. `Necessary`
2. `Analytics`

`Necessary` does not include Yandex Metrika.  
`Analytics` includes Metrika loading, storage, and goal firing.

## 6. Frontend UX

First notice:

- compact bottom card;
- small, theme-integrated, mobile-safe;
- no fullscreen blocker, no manipulative accept-only design.

Buttons:

- `Принять`
- `Только необходимые`
- `Настроить`

Settings:

- `Необходимые` -> always on
- `Аналитика` -> on/off
- provider named: `Яндекс.Метрика`
- primary action: `Сохранить выбор`

Withdrawal:

- persistent footer link `Настройки cookie`
- settings can be reopened at any time

## 7. State / Storage

States:

- `UNDECIDED`
- `NECESSARY_ONLY`
- `ANALYTICS_ALLOWED`

Stored record:

- one minimal first-party consent record, candidate key `fp02_cookie_consent`
- includes `version`, `necessary`, `analytics`, `decided_at`
- excludes name/email/phone/fingerprint/unnecessary identifiers

Versioning:

- `consent_version` required
- reprompt only on material technology/privacy model changes

Evidence assessment:

- browser-only model is technically easy but weaker as proof
- server-only model has stronger evidence but higher privacy/ops cost
- hybrid-ready architecture is recommended

**CONSENT EVIDENCE MODEL ASSESSED AGAINST RUSSIAN REQUIREMENTS**

`LEGAL REVIEW REQUIRED BEFORE IMPLEMENTATION`

## 8. Yandex Metrika

Required outcome:

- no Metrika load before analytics allowance
- no “banner after already-tracked pageview” fake control
- same existing counter source of truth preserved in SEO/integrations

Withdrawal:

- future collection must stop when analytics becomes OFF
- pre-init disable flag may be used
- first-party analytics cookies can be deleted on best effort
- reload is acceptable if honestly required

## 9. Forms / Goals

**FORM ANALYTICS RESPECTS COOKIE CONSENT STATE**

Target rule:

- backend-confirmed success
- if analytics allowed -> attempt Metrika goal
- if analytics not allowed -> do nothing
- form success must remain unaffected

**FORM PERSONAL-DATA CONSENT AND ANALYTICS CONSENT REMAIN SEPARATE**

The current form checkbox remains the personal-data consent for submitted lead data, not an analytics opt-in.

## 10. Cookie Policy

Required future factual content:

- actual categories used
- actual providers
- actual storage/tracker inventory
- purpose and disclosure
- choice and withdrawal path
- browser deletion guidance
- relation to privacy policy

Current gaps:

- live `cookie-files-policy` contains generic/demo language
- includes a placeholder for analytics provider listing
- states no dedicated consent UI is implemented
- does not factually describe the future versioned consent model

Final legal copy remains:

- `DRAFT / LEGAL REVIEW REQUIRED`

## 11. Admin

Future path:

`Настройки сайта -> Cookie и конфиденциальность`

Minimal fields:

- banner enabled/title/description/policy link/version
- necessary fixed active
- analytics description/toggle availability
- integration mapping `Yandex Metrika -> Analytics`
- state summary: enabled/version/detected integrations/policy status

Editors may adjust explanatory text, but category semantics and technical gating ownership must remain controlled.

## 12. Accessibility / Mobile / Performance

Architecture decisions:

- keyboard complete
- visible focus
- sensible tab order
- 320px+ safe
- 200% zoom safe
- reduced-motion safe
- iOS safe-area support
- no focus trap in simple notice mode
- no analytics race before consent state resolves
- no giant third-party CMP payload

## 13. Olya / Editorial Safety

**COOKIE IMPLEMENTATION MUST PRESERVE CURRENT EDITORIAL PRODUCTION TRUTH**

Future implementation must not overwrite:

- current legal copy except the explicitly approved cookie/privacy update scope;
- current SEO settings;
- current Metrika counter owner;
- current form configuration;
- footer/menu/legal/admin edits made by Olya/Admin.

## 14. WP Forge Module

Reusable boundary proposed:

- `PrivacyConsent / CookieConsent`

Reusable parts:

- consent state
- categories
- versioning
- gating API
- Metrika adapter
- admin owner
- reopen link pattern

Maturity:

- `THEORY / SPECIFICATION`

## 15. WP Forge Knowledge

The following reusable standards were codified for WP Forge:

- `PRIVACY-001` inventory-first truth
- `PRIVACY-002` UI without gating is not consent control
- `PRIVACY-003` analytics must not load before allowed
- `PRIVACY-004` form consent and analytics consent are separate
- `PRIVACY-005` withdrawal must remain available
- `PRIVACY-006` necessary is not a tracking loophole
- `PRIVACY-007` legal text must match actual technology
- `PRIVACY-008` Russian-law basis, not copied GDPR mechanics
- `PRIVACY-009` editorial/admin truth remains production truth
- `PRIVACY-010` Metrika goals respect analytics consent and must not carry identifying form values by default

## 16. Implementation Plan

Future phases defined:

- `P18E-A` privacy/tracker re-intake + implementation charter
- `P18E-B` core consent state + admin owner
- `P18E-C` frontend notice/settings UX
- `P18E-D` conditional Yandex Metrika loading
- `P18E-E` form goal consent integration
- `P18E-F` cookie policy + withdrawal surfaces
- `P18E-G` accessibility/mobile/cache/performance QA
- `P18E-H` deployment + evidence + dashboard sync

Plan file:

`PLANS/FP-0002-P18E-IMPLEMENTATION-PLAN.md`

No implementation performed in this wave.

## 17. Indexing

**INDEXING REMAINS CLOSED**

No indexing-open action is part of this design wave.

## 18. Git

- work performed in a clean worktree from `origin/mars/canonical-post-recovery`
- dirty main left untouched
- scope limited to design/docs/knowledge
- secret scan and commit/push handled after document package completion

## 19. Remaining Legal Decisions

Points that still require operator/legal review:

1. final legal basis posture for analytics in the operator's documents;
2. whether browser-only consent state is sufficient evidence;
3. whether a minimal server-side consent event store is required;
4. exact consent lifetime / retention policy;
5. final cookie/privacy wording and provider disclosures;
6. whether maps or any future CAPTCHA become consent-category-relevant in a later wave.

## 20. Acceptance

**FP-0002 P18E DESIGN COMPLETE — ACTUAL SITE TRACKERS / COOKIES / STORAGE HAVE BEEN INVENTORIED — RUSSIAN LEGAL / ROSKOMNADZOR / YANDEX REQUIREMENTS HAVE BEEN SEPARATED FROM PRODUCT RECOMMENDATIONS — A SMALL FIRST-PARTY CONSENT MODEL IS SPECIFIED — NECESSARY AND ANALYTICS ARE DISTINCT — YANDEX METRIKA WILL BE CONSENT-GATED — FORM GOALS WILL RESPECT ANALYTICS CONSENT — CONSENT CAN BE WITHDRAWN — COOKIE POLICY REQUIREMENTS ARE DEFINED FROM ACTUAL TECHNOLOGY — OLYA'S CURRENT ADMIN/EDITORIAL STATE REMAINS PRODUCTION TRUTH — IMPLEMENTATION IS PLANNED BUT NOT YET AUTHORIZED — INDEXING REMAINS CLOSED**

Final design principle:

```text
DO NOT BUILD A DECORATIVE COOKIE BANNER.

BUILD A SMALL PRIVACY CONTROL THAT ACTUALLY CONTROLS
NON-ESSENTIAL ANALYTICS.

DO NOT COPY GDPR MECHANICALLY.

GROUND THE RUSSIAN PRODUCTION IMPLEMENTATION IN CURRENT
152-FZ / ROSKOMNADZOR-EVIDENCE / YANDEX CAPABILITIES
AND ACTUAL DEPLOYED TECHNOLOGY.

DO NOT INVENT LEGAL FACTS OR THIRD-PARTY SERVICES.

DO NOT OVERWRITE CURRENT EDITORIAL WORK.
```
