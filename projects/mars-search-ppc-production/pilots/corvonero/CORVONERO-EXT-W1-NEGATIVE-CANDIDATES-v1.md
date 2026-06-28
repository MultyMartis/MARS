# CORVONERO-EXT-W1 — Negative Keyword Candidates v1

**Status:** NOT DEPLOYED — operator approval required.

## account_shared

| Term | Match | Source | Status | Risk |
|------|-------|--------|--------|------|
| вакансия | word | EX-CAREER-JOBS | APPROVED_CANDIDATE | LOW |
| работа программистом | phrase | EX-CAREER-JOBS | APPROVED_CANDIDATE | LOW |
| резюме | word | EX-RESUME-INTERVIEWS | APPROVED_CANDIDATE | LOW |
| обучение | word | EX-EDUCATION-COURSES | REVIEW_REQUIRED | MEDIUM |
| курс | word | EX-EDUCATION-COURSES | REVIEW_REQUIRED | MEDIUM |
| курсы | word | EX-EDUCATION-COURSES | REVIEW_REQUIRED | MEDIUM |
| сертификация | word | EX-CERTIFICATION-EXAMS | APPROVED_CANDIDATE | LOW |
| скачать | word | EX-FREE-DOWNLOADS | REVIEW_REQUIRED | MEDIUM |
| кряк | word | EX-FREE-DOWNLOADS | APPROVED_CANDIDATE | LOW |
| зарплата | word | EX-SALARY | APPROVED_CANDIDATE | LOW |
| стань программистом | phrase | CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json S1 | APPROVED_CANDIDATE | LOW |
| становится программистом | phrase | CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json | APPROVED_CANDIDATE | LOW |

## campaign

| Term | Match | Source | Status | Risk |
|------|-------|--------|--------|------|
| купить 1с | phrase | EX-PRODUCT-LICENSE-ONLY | REVIEW_REQUIRED | MEDIUM |
| лицензия 1с | phrase | EX-PRODUCT-LICENSE-ONLY | REVIEW_REQUIRED | MEDIUM |
| инструкция | word | EX-SELF-SERVICE-MANUALS | DO_NOT_DEPLOY | HIGH |
| как сделать самому | phrase | EX-SELF-SERVICE-MANUALS | REVIEW_REQUIRED | HIGH |
| заказать коды маркировки | phrase | CORVONERO-AD-WAVE-1-EXCLUDED-GROUPS-v1.json ca-05-specialist-search | REVIEW_REQUIRED | HIGH |
| трактир | word | CORVONERO-AD-WAVE-1-SEMANTIC-RECONCILIATION-v1.json S2 ABSTAIN | DO_NOT_DEPLOY | HIGH |
| erp | word | CORVONERO-PHASE-6-ABSTAIN-HOLDOUT-v1.json GENERIC_PLATFORM_OR_ERP | REVIEW_REQUIRED | MEDIUM |

## group_cross

| Term | Match | Source | Status | Risk |
|------|-------|--------|--------|------|
| маркировка | undefined | CA-01 | DO_NOT_DEPLOY | HIGH |
| честный знак | undefined | CA-01 | REVIEW_REQUIRED | MEDIUM |
| интеграция | undefined | CA-01 | DO_NOT_DEPLOY | HIGH |
| сопровождение | undefined | CA-01 | DO_NOT_DEPLOY | HIGH |
| доработка | undefined | CA-01 | DO_NOT_DEPLOY | HIGH |
| программист | undefined | CA-02 | DO_NOT_DEPLOY | CRITICAL |
| коды маркировки | undefined | CA-05 | DO_NOT_DEPLOY | CRITICAL |

