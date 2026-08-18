# CORVONERO — РСЯ URL / UTM draft v0.1

**Status:** DRAFT_APPROVAL_REQUIRED  
**Landing split:** SAME_URL_FOR_LOCAL_AND_REMOTE  
**Landing URL status:** OPERATOR_PREVIOUSLY_REPORTED_CREATED / NOT_RESCANNED_IN_THIS_TASK  
**Search UTM policy:** NOT MODIFIED (see `CORVONERO-EXT-W1-UTM-POLICY-v2.md`)

Do **not** treat these as final import URLs. Do not overwrite Search package conventions.

Search production slugs (`corv_programmist_1s`, `ca-01-specialist-search`, …) stay on Search. RSY draft uses **distinct** `campaign_code` values so analytics are not mixed.

---

## Draft UTM pattern

```
utm_source=yandex
utm_medium=cpc
utm_campaign={campaign_code}
utm_content={group_code}
utm_term={targeting_or_auto}
```

`utm_term={targeting_or_auto}` is a **placeholder**. Exact Direct Networks macro (if any) is **SAFE UNKNOWN / DIRECT_CONFIRMATION_REQUIRED**. Search `{keyword}` is not assumed to exist for RSY.

---

## Primary structure URL candidates

| campaign_code | group_code | landing_url | utm_url_candidate | status | notes |
| --- | --- | --- | --- | --- | --- |
| CORVONERO-RSY-LOCAL | 01-LOCAL-PROGRAMMIST-1S | https://lk.corvonero.ru/programmist-1s/ | https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-LOCAL&utm_content=01-LOCAL-PROGRAMMIST-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=01-LOCAL-PROGRAMMIST-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-LOCAL | 02-LOCAL-SOPROVOZHDENIE-1S | https://lk.corvonero.ru/soprovozhdenie-1s/ | https://lk.corvonero.ru/soprovozhdenie-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-LOCAL&utm_content=02-LOCAL-SOPROVOZHDENIE-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/soprovozhdenie-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=02-LOCAL-SOPROVOZHDENIE-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-LOCAL | 03-LOCAL-DORABOTKA-1S | https://lk.corvonero.ru/dorabotka-razrabotka-1s/ | https://lk.corvonero.ru/dorabotka-razrabotka-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-LOCAL&utm_content=03-LOCAL-DORABOTKA-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/dorabotka-razrabotka-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=03-LOCAL-DORABOTKA-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-LOCAL | 04-LOCAL-INTEGRACII-1S | https://lk.corvonero.ru/integracii-1s/ | https://lk.corvonero.ru/integracii-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-LOCAL&utm_content=04-LOCAL-INTEGRACII-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/integracii-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=04-LOCAL-INTEGRACII-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-LOCAL | 05-LOCAL-MARKIROVKA-CHESTNY-ZNAK | https://lk.corvonero.ru/markirovka-chestny-znak/ | https://lk.corvonero.ru/markirovka-chestny-znak/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-LOCAL&utm_content=05-LOCAL-MARKIROVKA-CHESTNY-ZNAK&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/markirovka-chestny-znak/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=05-LOCAL-MARKIROVKA-CHESTNY-ZNAK&utm_term={targeting_or_auto} |
| CORVONERO-RSY-REMOTE | 01-REMOTE-PROGRAMMIST-1S | https://lk.corvonero.ru/programmist-1s/ | https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-REMOTE&utm_content=01-REMOTE-PROGRAMMIST-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=01-REMOTE-PROGRAMMIST-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-REMOTE | 02-REMOTE-SOPROVOZHDENIE-1S | https://lk.corvonero.ru/soprovozhdenie-1s/ | https://lk.corvonero.ru/soprovozhdenie-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-REMOTE&utm_content=02-REMOTE-SOPROVOZHDENIE-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/soprovozhdenie-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=02-REMOTE-SOPROVOZHDENIE-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-REMOTE | 03-REMOTE-DORABOTKA-1S | https://lk.corvonero.ru/dorabotka-razrabotka-1s/ | https://lk.corvonero.ru/dorabotka-razrabotka-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-REMOTE&utm_content=03-REMOTE-DORABOTKA-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/dorabotka-razrabotka-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=03-REMOTE-DORABOTKA-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-REMOTE | 04-REMOTE-INTEGRACII-1S | https://lk.corvonero.ru/integracii-1s/ | https://lk.corvonero.ru/integracii-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-REMOTE&utm_content=04-REMOTE-INTEGRACII-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/integracii-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=04-REMOTE-INTEGRACII-1S&utm_term={targeting_or_auto} |
| CORVONERO-RSY-REMOTE | 05-REMOTE-MARKIROVKA-CHESTNY-ZNAK | https://lk.corvonero.ru/markirovka-chestny-znak/ | https://lk.corvonero.ru/markirovka-chestny-znak/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY-REMOTE&utm_content=05-REMOTE-MARKIROVKA-CHESTNY-ZNAK&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Fallback candidate: https://lk.corvonero.ru/markirovka-chestny-znak/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=05-REMOTE-MARKIROVKA-CHESTNY-ZNAK&utm_term={targeting_or_auto} |

---

## Fallback one-campaign URL note

If `CORVONERO-RSY` is chosen, replace `utm_campaign` with `CORVONERO-RSY` and keep `utm_content={group_code}` for the 10-group mapping.

Compact 5-group mapping (weaker isolation):

| campaign_code | group_code | landing_url | utm_url_candidate | status | notes |
| --- | --- | --- | --- | --- | --- |
| CORVONERO-RSY | 01-PROGRAMMIST-1S | https://lk.corvonero.ru/programmist-1s/ | https://lk.corvonero.ru/programmist-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=01-PROGRAMMIST-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Compact fallback only; utm_content would lose LOCAL/REMOTE unless extra parameter added later |
| CORVONERO-RSY | 02-SOPROVOZHDENIE-1S | https://lk.corvonero.ru/soprovozhdenie-1s/ | https://lk.corvonero.ru/soprovozhdenie-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=02-SOPROVOZHDENIE-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Compact fallback only; utm_content would lose LOCAL/REMOTE unless extra parameter added later |
| CORVONERO-RSY | 03-DORABOTKA-1S | https://lk.corvonero.ru/dorabotka-razrabotka-1s/ | https://lk.corvonero.ru/dorabotka-razrabotka-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=03-DORABOTKA-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Compact fallback only; utm_content would lose LOCAL/REMOTE unless extra parameter added later |
| CORVONERO-RSY | 04-INTEGRACII-1S | https://lk.corvonero.ru/integracii-1s/ | https://lk.corvonero.ru/integracii-1s/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=04-INTEGRACII-1S&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Compact fallback only; utm_content would lose LOCAL/REMOTE unless extra parameter added later |
| CORVONERO-RSY | 05-MARKIROVKA-CHESTNY-ZNAK | https://lk.corvonero.ru/markirovka-chestny-znak/ | https://lk.corvonero.ru/markirovka-chestny-znak/?utm_source=yandex&utm_medium=cpc&utm_campaign=CORVONERO-RSY&utm_content=05-MARKIROVKA-CHESTNY-ZNAK&utm_term={targeting_or_auto} | DRAFT_APPROVAL_REQUIRED | Compact fallback only; utm_content would lose LOCAL/REMOTE unless extra parameter added later |

---

## Notes

- Live HTTP status of landings was **not** rescanned in this task.
- Legal/form URLs were **not** live-checked.
- LP-06 remains historical/deferred; not used.
- Operator must approve the RSY pattern before any import package.
