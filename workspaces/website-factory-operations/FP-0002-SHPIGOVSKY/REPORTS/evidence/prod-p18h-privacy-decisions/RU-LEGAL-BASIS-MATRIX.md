# RU Legal Basis Matrix — FP-0002 PROD-P18H

**Retrieval date:** 2026-08-19  
**Scope:** Privacy/cookie/consent/retention decisions for `https://shpigovsky.ru/`  
**Status:** bounded recheck; not legal advice

## Classification legend

| Tag | Meaning |
|-----|---------|
| **LAW** | Current statutory text (152-FZ) |
| **REGULATOR** | Roskomnadzor guidance / enforcement signal |
| **PROVIDER** | Official Yandex Metrika documentation |
| **RECOMMENDATION** | Product/implementation choice when law does not fix an exact value |

## Sources verified

| Source | Tag | Finding | Design consequence |
|--------|-----|---------|-------------------|
| 152-FZ Art. 5 p.7 (Mintrud mirror, ConsultantPlus podborki, retrieved 2026-08-19) | **LAW** | Storage must not exceed purposes; destroy/anonymize when purpose ends unless law/contract sets another term | Lead retention must be purpose-bound; indefinite storage requires documented purpose — not a neutral default |
| 152-FZ Art. 9 (P18E matrix + current recheck) | **LAW** | Consent must be explicit, separable, informed; operator must be able to confirm receipt when consent is the basis | Separate form consent vs analytics consent; versioned browser record acceptable as technical evidence, but legal sufficiency of evidence posture is operator/legal review |
| 152-FZ Art. 14 (subject rights) | **LAW** | Subject may withdraw consent; operator must stop processing and destroy within statutory window when applicable | Withdrawal via cookie settings + email path; form consent withdrawal separate |
| Roskomnadzor operator guidance (secondary commentary via GramotaIB/Klerk synthesis, 2026-08-19) | **REGULATOR** | No universal “X days for all websites”; documented purpose required; excessive/indefinite periods risk enforcement | Privacy Policy “неограничен” conflicts with purpose-limitation principle — **LEGAL REVIEW NEEDED** for final Privacy Policy retention wording |
| Yandex Metrika cookie/storage docs (P18E verified) | **PROVIDER** | Deferred tag load supported; cookies + localStorage on site domain | Consent must gate tag load, not banner-only |
| Yandex Metrika user opt-out (`disableYaCounter`) | **PROVIDER** | Pre-init disable blocks collection | Withdrawal architecture aligned |

## Not proven as mandatory for this site

1. Exact cookie-consent lifetime in days (365 / 730 / etc.) — **RECOMMENDATION**
2. Mandatory server-side consent event database for analytics — **not established**; browser record + policy disclosure is the bounded minimum
3. GDPR-style “every cookie requires consent” universal rule for all Russian sites — **not established** in bounded primary-source review

## P18H legal recheck result

**P18H RUSSIAN PRIVACY / COOKIE LEGAL BASIS RECHECKED**

Statutory requirements are separated from product recommendations in `DECISION-MATRIX.md`.
