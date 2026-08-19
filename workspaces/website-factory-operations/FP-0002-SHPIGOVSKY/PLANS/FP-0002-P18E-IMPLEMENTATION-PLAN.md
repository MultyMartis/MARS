# FP-0002 P18E Implementation Plan

**Status:** planning only  
**Wave:** prepared by PROD-P18E design; implementation not authorized

## Objective

Turn the P18E cookie/privacy design into a bounded production rollout without breaking current forms, Metrika ownership, legal pages, or Olya/Admin editorial truth.

## Gate conditions before any implementation

1. Fresh production intake on the day of implementation.
2. Olya/Admin content truth treated as canonical DB truth.
3. Current tracker/storage inventory re-verified.
4. Current legal pages re-verified before any wording mutation.
5. Indexing remains closed.
6. Existing Yandex Metrika counter source of truth preserved.
7. No second analytics owner introduced.

## Recommended phases

### P18E-A — Privacy / tracker re-intake and implementation charter

Deliverables:

- fresh runtime tracker/storage inventory;
- fresh legal page gap review;
- implementation charter with exact editable scope;
- no frontend mutation yet.

Gate:

- operator confirms current production truth preserved.

### P18E-B — Core consent state + Admin owner

Deliverables:

- `PrivacyConsent` / `CookieConsent` module skeleton;
- consent version model;
- `Настройки сайта -> Cookie и конфиденциальность`;
- integration registry mapping `Yandex Metrika -> analytics`.

Gate:

- source review confirms no duplicate counter-id source;
- admin discoverability proof.

### P18E-C — Frontend notice + settings UX

Deliverables:

- compact bottom notice;
- direct `Принять` and `Только необходимые`;
- settings panel;
- accessibility states and focus behavior.

Gate:

- keyboard/mobile review;
- no dark-pattern regression.

### P18E-D — Conditional Yandex Metrika loading

Deliverables:

- unconditional `wp_footer` Metrika path retired;
- consent-gated Metrika adapter;
- no pre-consent JS or noscript tracking.

Gate:

- view-source and network proof:
  - undecided: no Metrika load
  - necessary only: no Metrika load
  - analytics allowed: Metrika loads

### P18E-E — Form goal consent integration

Deliverables:

- `reachGoal` guarded by analytics consent;
- backend-confirmed success semantics preserved;
- no impact on lead persistence or SMTP.

Gate:

- with analytics off: submit works, no goal
- with analytics on: backend success then goal attempt

### P18E-F — Cookie policy and withdrawal surfaces

Deliverables:

- factual cookie-policy update or dedicated approved page;
- footer `Настройки cookie` reopen link;
- settings reopen from any page.

Gate:

- operator/legal copy approval for factual legal text.

### P18E-G — Accessibility / mobile / cache / performance QA

Deliverables:

- 320px/mobile QA;
- zoom/reduced-motion QA;
- cache safety confirmation;
- no analytics race before consent resolution.

Gate:

- acceptance matrix PASS.

### P18E-H — Deployment + evidence + dashboard sync + canonical sync

Deliverables:

- deployment record;
- if chosen, consent evidence store validation;
- Dashboard status note;
- canonical Git sync;
- post-deploy report.

Gate:

- no indexing change as deploy side effect;
- operator confirms production state.

## Non-goals

- no third-party CMP by default;
- no Yandex Metrika runtime redesign beyond consent gating;
- no legal-text invention without approval;
- no broad privacy-database creation by default.

## Required test matrix

- first visit undecided
- accept
- necessary only
- reload persistence
- multi-page persistence
- reopen settings
- revoke analytics
- forms with analytics off
- forms with analytics on
- consent version bump
- browser cookies blocked
- mobile 320px
- keyboard-only
- shared cache safety

## Implementation warnings

1. Do not trust browser consent state for privileged server actions.
2. Do not log visitor cookie choices into Activity Log.
3. Do not classify Metrika as necessary.
4. Do not keep Metrika noscript image active before consent.
5. Do not merge form personal-data consent with analytics consent.

## End state

At the end of a successful P18E implementation:

- visitor gets a real choice;
- analytics does not load before permission;
- forms still work;
- Metrika goals remain backend-confirmed;
- withdrawal is accessible;
- current editorial/admin production truth remains preserved.
