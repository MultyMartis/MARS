# Forge WordPress — Cookie Consent and Privacy Controls Standard v1

**ID:** FW-S-33  
**Status:** ACTIVE — PRODUCTION-INFORMED / SPECIFICATION-FIRST  
**Date:** 2026-08-19  
**Evidence:** FP-0002 PROD-P18E design; FP-0002 live Metrika/forms/legal reality  
**Companions:** [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) · [SITE-SETTINGS](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) · [GLOBAL-SETTINGS-OWNERSHIP](FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md) · [ADMIN-IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md)

---

## 1. Core rule

```text
DO NOT SHIP A DECORATIVE COOKIE BANNER.

IF THE UI CLAIMS TO CONTROL ANALYTICS,
THE RUNTIME MUST ACTUALLY GATE ANALYTICS.
```

For Russian production sites, privacy/cookie design must be based on:

- actual deployed trackers/storage;
- current operator/legal documents;
- provider capabilities;
- Russian legal/regulator evidence actually verified for the case.

Do **not** copy GDPR-style mechanics blindly when the repo evidence does not justify them.

---

## 2. Minimum default model

For small first-party WordPress sites with one confirmed analytics provider and no ad stack:

- `Necessary`
- `Analytics`

Do **not** add `Marketing`, `Personalization`, or “functional cookies” by reflex. Add categories only when the verified runtime actually needs them.

---

## 3. Inventory first

Before any consent UI design or implementation:

1. inspect live frontend HTML;
2. inspect actual theme/plugin output paths;
3. inspect current legal pages;
4. list actual cookies, localStorage/sessionStorage, embeds, analytics, maps, forms, and injected scripts;
5. classify each observed item:
   - owner
   - purpose
   - public page-load timing
   - external transmission
   - necessity
   - feasible consent category
   - current disclosure state

If the inventory is missing, the consent design is incomplete.

**PRIVACY-001:** cookie notice must reflect actual tracker/storage inventory.

---

## 4. Runtime gating

If analytics consent is modeled, non-essential analytics must not load before it is allowed.

Required semantics:

```text
UNDECIDED         -> analytics absent
NECESSARY_ONLY    -> analytics absent
ANALYTICS_ALLOWED -> analytics may load
```

The following are insufficient:

- banner shown after analytics already initialized;
- CSS-hidden banner only;
- “we have a policy page” without script gating;
- goal suppression while the counter still loads freely.

**PRIVACY-002:** consent UI without runtime gating is not consent control.  
**PRIVACY-003:** analytics must not load before the selected model allows it.

---

## 5. Yandex Metrika rule

If Yandex Metrika is used:

1. keep one counter owner of truth;
2. do not duplicate the counter id in multiple settings owners;
3. defer loading until analytics consent permits it;
4. treat both JS bootstrap and noscript image/watch path as gating scope;
5. use provider-supported pre-init disable behavior for withdrawal where appropriate;
6. keep forms fully functional if Metrika is absent.

Metrika goals:

- fire only after backend-confirmed success;
- do not send identifying form values by default.

**PRIVACY-010:** Metrika goals must respect analytics consent and never carry identifying form values without an explicitly supported/legal mechanism.

---

## 6. Forms are separate

Form personal-data consent and analytics consent are different controls.

Never:

- merge them into one checkbox;
- phrase analytics acceptance as blanket form-processing consent;
- silently opt a submitter into analytics by checking the form consent box.

**PRIVACY-004:** form personal-data consent and analytics consent are separate.

---

## 7. Withdrawal

Visitors must be able to reopen settings after the first choice.

Minimum pattern:

- footer link `Настройки cookie`;
- current state visible when reopened;
- analytics can change from ON to OFF;
- future analytics collection stops after withdrawal.

Be honest about technical limits; do not promise deletion of already-transmitted third-party data the site cannot control.

**PRIVACY-005:** consent withdrawal must remain accessible after first choice.

---

## 8. Necessary category discipline

Necessary means technically required for:

- requested site operation;
- security;
- a visitor-requested action;
- consent-state persistence itself.

Not necessary:

- analytics the business wants for reporting;
- heatmaps/replay;
- vendor scripts loaded “just in case”.

**PRIVACY-006:** necessary must not become a dumping ground for tracking.

---

## 9. Legal documents must match reality

Privacy policy / cookie policy must describe actual deployed technology, not a generic vendor template and not a future-state assumption.

At minimum they must align on:

- actual providers;
- actual categories;
- actual purposes;
- actual choice/withdrawal mechanism;
- relationship between form consent and analytics consent.

**PRIVACY-007:** legal text must describe actual deployed technology, not generic template vendors.

---

## 10. Russian-law boundary

For Russian sites:

- use Russian legal/regulator/provider evidence verified for the case;
- do not state that every cookie always requires a GDPR-style consent workflow unless the evidence for that exact claim is present;
- when legal certainty is insufficient, mark the decision for operator/legal review rather than inventing a universal rule.

**PRIVACY-008:** Russian-site cookie/privacy design must be based on Russian-law/regulator evidence, not blindly copied GDPR UX.

---

## 11. Editorial truth

Production privacy implementation must preserve legitimate editor/Admin changes as current truth.

Do not overwrite:

- legal pages;
- SEO/integration settings;
- current analytics counter source of truth;
- forms configuration;
- footer/menu content;
- operator-approved runtime settings

without a fresh intake and explicit implementation charter.

**PRIVACY-009:** Admin/editorial changes remain production truth through privacy waves.

---

## 12. Admin owner

Recommended path:

```text
Настройки сайта
→ Cookie и конфиденциальность
```

Keep it minimal:

- banner text/link/version
- category descriptions
- integration mapping
- state summary

Editors may change explanatory copy, but must not reclassify analytics as necessary through ordinary text fields.

---

## 13. Reusable module boundary

Candidate reusable WP Forge module:

```text
PrivacyConsent / CookieConsent
```

Reusable concerns:

- consent state
- categories
- versioning
- early runtime gate
- events
- integration registry
- Yandex Metrika adapter
- footer reopen link

Project-specific concerns:

- styling
- legal copy
- actual provider inventory

---

## 14. Anti-pattern linkage

Related anti-patterns:

- AP-031 — decorative cookie banner without gating
- AP-032 — analytics loads before consent state resolves
- AP-033 — cookie analytics consent merged with form personal-data consent
- AP-034 — privacy policy names generic/demo vendors instead of actual runtime

---

## 15. Reusable standards extracted

- `PRIVACY-001` inventory-first truth
- `PRIVACY-002` UI without gating is not consent control
- `PRIVACY-003` analytics must not load before allowed
- `PRIVACY-004` form consent and analytics consent are separate
- `PRIVACY-005` withdrawal remains accessible
- `PRIVACY-006` necessary is not a tracking loophole
- `PRIVACY-007` legal text must match actual deployed technology
- `PRIVACY-008` Russian-law/regulator evidence over copied GDPR assumptions
- `PRIVACY-009` editorial/Admin truth preserved
- `PRIVACY-010` Metrika goals respect analytics consent and avoid identifying payloads by default

---

*FW-S-33 v1 — first WP Forge privacy/cookie controls standard derived from FP-0002 P18E.*
