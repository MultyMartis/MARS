# REPORT — Corvonero Commander CT-4 Operator Approval and Cleanup v1

Generated: 2026-06-29T19:17:53.625Z

## Preflight

| Check | Result |
|-------|--------|
| Drive | X: |
| Volume label | AI WS |
| Repository | X:\\AI MARS\\ |
| Branch | mars/canonical-post-recovery |
| Write scope | projects/mars-search-ppc-production/ |

## Part 1 — Technical copy validation

| Ad group | H1 (≤56) | H2 (≤30) | Text (≤81) | Path (≤20) |
|----------|----------|----------|------------|------------|
| ca-01-find-hire-specialist | 21 PASS | 26 PASS | 74 PASS | 14 PASS |
| ca-01-remote-freelance-specialist | 23 PASS | 21 PASS | 73 PASS | 14 PASS |
| ca-01-specialist-by-product | 30 PASS | 21 PASS | 76 PASS | 14 PASS |
| ca-01-specialist-extended | 32 PASS | 23 PASS | 80 PASS | 14 PASS |
| ca-05-chestny-znak-service | 29 PASS | 26 PASS | 73 PASS | 13 PASS |
| ca-05-marking-codes | 20 PASS | 24 PASS | 61 PASS | 13 PASS |
| ca-05-marking-setup | 25 PASS | 19 PASS | 73 PASS | 13 PASS |



## Part 2 — Phrase cleanup

| Phrase | Verdict | Final destination | Reason |
|--------|---------|-------------------|--------|
| найти работу программистом 1с | REJECT | — / — | employment_job_seeker_intent — seeker looking for work as programmer, not service purchase |
| требуется программист 1с | REJECT | — / — | hiring_staff_vacancy_intent without service-purchase evidence — vacancy-style employer query |
| ищу программист 1с | KEEP | CA-01 / ca-01-find-hire-specialist | commercial_find_hire_intent — employer seeking contracted 1C programmer for task |
| подработка 1с программист удаленно | REJECT | — / — | employment_part_time_job_seeker_intent — side-job / part-time work query |
| программа программист 1с | REJECT | — / — | malformed_unclear_informational — software/program query, not service purchase |
| бухгалтерия для программиста 1с | REJECT | — / — | malformed_unclear_informational — misaligned product/education query, not deployable service intent |
| тестирование доработок 1с | MOVE_TO_OTHER_CAMPAIGN | CA-03 / ca-03-modification | generic_1c_modification_intent — modification/testing intent belongs in CA-03, not marking |
| продажа доработок 1с | REJECT | — / — | seller_intent_not_service_purchase — selling modifications, not buying setup service |

## Part 5 — Count reconciliation

| Metric | Value |
|--------|-------|
| Original pre-CT4 | 895 |
| CT-4 rejected before operator cleanup | 56 |
| Additional rejected (operator cleanup) | 6 |
| Additional moved within campaign | 0 |
| Additional moved to other campaign | 1 |
| **Total rejected** | **62** |
| Before operator cleanup deployable | 839 |
| **Final deployable** | **833** |
| Reconciled (895 − rejected = deployable) | YES |

## Verdict

```
CORVONERO COMMANDER CT-4:
PASS — FINAL AUTHORITY APPROVED

Groups over 200: 0
Final deployable phrases: 833
Operator-approved derived ads: 7
Unapproved ads: 0
Technical ad limits: PASS
CT-5 generation: READY FOR SEPARATE AUTHORIZATION
```

## CT-4 authority manifest

`X:/AI MARS/projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-CT4-AUTHORITY-MANIFEST-v1.json`
