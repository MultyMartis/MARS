# RU Legal Basis Matrix — FP-0002 PROD-P18E Cookie Consent Design

**Wave:** PROD-P18E design/specification only  
**Retrieval date:** 2026-08-19  
**Scope:** Russian-law-aware cookie / analytics architecture for `https://shpigovsky.ru/`  
**Status:** bounded current verification complete; not legal advice

## Classification legend

- `LAW` — current legal text or authoritative legal text mirror
- `REGULATOR GUIDANCE / ENFORCEMENT SIGNAL` — regulator-facing operational signal; strong design input, not a substitute for legal analysis
- `PROVIDER REQUIREMENT` — official Yandex Metrika capability / constraint
- `IMPLEMENTATION RECOMMENDATION` — technical product recommendation derived from the combined evidence

## Verified sources

| Source | Type | Principle supported | Design consequence |
|---|---|---|---|
| Federal Law No. 152-FZ, Article 9, current text as mirrored by ConsultantPlus search results and article snippet, retrieved 2026-08-19 | LAW | Consent to personal-data processing must be free, specific, informed, conscious, unambiguous, separable from other documents, and in a form that allows confirmation of receipt | If analytics consent is the relied-on legal basis, the UI must be explicit, separable from form consent, and the implementation must preserve evidence of the received choice |
| Federal Law No. 152-FZ, Article 9, same source | LAW | The operator must be able to confirm the fact of receiving consent when consent is used | Browser-only state may be operationally insufficient for stronger evidentiary posture; server evidence is a separate architecture decision and requires operator/legal review |
| `https://yandex.ru/support/metrica/en/general/how-it-works` (via search synthesis, retrieved 2026-08-19) | PROVIDER REQUIREMENT | When the Metrika JavaScript tag executes it gains access to interaction/event data; if the JS tag is not executed, collection is materially reduced | Consent architecture must control tag loading, not merely hide a banner after the tag already ran |
| `https://yandex.ru/support/metrica/en/general/notification` (search synthesis, retrieved 2026-08-19) | PROVIDER REQUIREMENT | Yandex supports delaying tag loading until user consent; without consent the snippet does not load | FP-0002 should use deferred loading of the existing counter, not a second counter source or post-load suppression only |
| `https://yandex.ru/support/metrica/ru/general/user-opt-out` (fetched 2026-08-19) | PROVIDER REQUIREMENT | `window['disableYaCounterXXXXXXXX']=true` before counter initialization blocks cookies, collection, and data transmission | Withdrawal architecture may use a pre-init disable flag when analytics is not allowed or has been revoked |
| `https://yandex.ru/support/metrica/en/general/cookie-usage` (fetched 2026-08-19) | PROVIDER REQUIREMENT | Metrika stores anonymous browser identifiers in cookies and localStorage on the site domain; documented cookies include `_ym_uid`, `_ym_d`, `_ym_isad`, `_ym_visorc_*`, `ymex`; documented storage includes `_ym_uid`, `_ym_retryReqs`, `_ym_lastHit`, `_ym_lsid` | Actual policy/inventory must name Yandex Metrika as a storage owner and treat both cookies and localStorage/sessionStorage as in scope for disclosure and gating |
| Current FP-0002 production legal pages and frontend, fetched 2026-08-19 | REGULATOR GUIDANCE / ENFORCEMENT SIGNAL | The live site currently uses Yandex Metrika and exposes a cookie policy page that still says a separate banner/panel is not implemented | There is a present compliance/documentation gap between runtime behavior and the current cookie-policy copy; future implementation must update factual disclosure without overwriting unrelated editorial truth |
| FP-0002 historical P18A legal-state evidence (`LEGAL-DEMO-PLACEHOLDER-INVENTORY`, `DB-LEGAL-INTAKE`, related report), verified 2026-08-19 | REGULATOR GUIDANCE / ENFORCEMENT SIGNAL | Legal pages are production pages with editor-owned truth; page `cookie-files-policy` still contains a demo placeholder for connected analytics systems | P18E implementation must preserve Olya/Admin truth while replacing only the factual cookie/analytics sections after re-intake |

## What the evidence does and does not prove

### Verified

1. `152-FZ` supports a consent model that must be explicit and confirmable when consent is the legal basis.
2. Official Yandex Metrika documentation supports deferred loading and pre-init opt-out.
3. Official Yandex Metrika documentation confirms that the product uses both cookies and browser storage.
4. The current FP-0002 runtime loads Metrika immediately on public pages, so a decorative banner would not be a real control.

### Not proven as a universal rule

1. That Russian law has an exact GDPR/ePrivacy-equivalent requirement for every cookie on every site.
2. That a two-year or any other exact cookie-consent retention/lifetime is legally mandated for this use case.
3. That browser-only consent state is always legally sufficient where consent evidence may later be challenged.

## Required legal/operator review flags

| Topic | Why review is still required |
|---|---|
| Whether FP-0002 will rely on consent as the legal basis for analytics, or attempt another basis for some processing elements | Product/legal choice with risk implications; design is prepared for consent-first gating because that is the safer bounded model |
| Whether browser-only consent storage is enough evidence for this operator | Article 9 confirmation burden exists; stronger evidence posture may justify a minimal server record |
| Final wording for privacy policy and cookie policy | Current pages contain generic/demo phrasing and must be aligned to actual deployed technology by operator/legal owner |
| Final consent lifetime / re-prompt policy | No precise statutory period was confirmed in bounded research; this is a product/legal policy decision |

## Architecture conclusion

**RUSSIAN COOKIE / ANALYTICS COMPLIANCE BASIS VERIFIED**

For FP-0002, the canonical safe design is:

1. treat necessary site-operation mechanisms separately from optional analytics;
2. do not load Yandex Metrika until analytics consent allows it;
3. keep form personal-data consent separate from analytics consent;
4. preserve a versioned, minimal consent record;
5. update the cookie/privacy documents to match the actual technology inventory;
6. mark unresolved evidentiary and wording questions as `LEGAL REVIEW REQUIRED BEFORE IMPLEMENTATION`.
