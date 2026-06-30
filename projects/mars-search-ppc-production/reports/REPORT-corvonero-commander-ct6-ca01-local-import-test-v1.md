# REPORT — Corvonero Commander CT-6 CA-01 Local Import Test v1

**Date:** 2026-06-30  
**Programme:** [mars-search-ppc-production](../README.md)  
**Scope:** CA-01 v5 local Commander import test — operator-assisted reconciliation  
**Branch:** `mars/canonical-post-recovery` @ `880ca442d7dd25a74ed2c1fd83e4a11fecee8dc1`

---

## Executive summary

CA-01 v5 local Commander import **PASS**. Operator preview and local import match final authority workbook: 1 campaign, 7 groups, 339 phrases, 7 ads, 0 unparsed rows, 0 preview/import/callout/region/organization errors. No server upload, synchronization, or campaign launch occurred.

---

## Preflight results

| Check | Status |
|-------|--------|
| Drive X: / volume `AI WS` | PASS |
| Repository `X:\AI MARS\` | PASS |
| Binding XLSX exists | PASS |
| SHA-256 recalculation | PASS — `80e62d262b33e154c86a6a2642c84d4c8a37c263f7464ac9fffc13e082702210` |
| CT-4 authority checkpoint | `8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86` |
| CT-5 generation checkpoint | `880ca442d7dd25a74ed2c1fd83e4a11fecee8dc1` |

---

## CA-01 v5 binding verification

| Metric | Expected | Workbook authority | Operator import |
|--------|----------|-------------------|-----------------|
| Campaigns | 1 | 1 | 1 |
| Groups | 7 | 7 | 7 |
| Phrases | 339 | 339 | 339 |
| Ads | 7 | 7 | 7 |
| Groups over 200 | 0 | 0 (max 144) | — |
| Callouts | valid | valid | 0 errors |
| URLs | clean, no UTM | clean | 0 errors |
| Region | Новосибирская область | PASS | 0 errors |
| Organization | blank | PASS | 0 errors |
| Bid policy | CORVONERO_BALANCED_CYCLIC_10_RUB_V1 | PASS (10 distinct bids) | — |
| Unparsed rows | 0 | — | 0 |
| Preview errors | 0 | — | 0 |

---

## Operator result

| Item | Value |
|------|-------|
| Binding version | v5 |
| Preview | PASS |
| Local import | COMPLETED |
| Operator confirmation | Everything is good |
| Server upload | NOT PERFORMED |
| Synchronization | NOT PERFORMED |
| Launch | NOT PERFORMED |

**Detailed field inspection:** OPERATOR CONFIRMED GENERALLY — DETAILED FIELD-BY-FIELD INSPECTION NOT RECORDED

---

## Commander transport tooling

| Capability | Status |
|------------|--------|
| Row extension | present |
| Metadata translation | present |
| Fastlink clearing | present |
| Organization blanking | present |
| Callout serialization (`||`) | present |
| Clean URL policy | present |
| Explicit bid-policy selection | present |
| Triumph policy preserved | present |
| Corvonero balanced cyclic bid policy | present |
| Unit tests | 64 / 64 PASS |

---

## Artifacts

| Artifact | Path |
|----------|------|
| Import protocol | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-IMPORT-PROTOCOL-v1.md` / `.json` |
| Preview receipt | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-IMPORT-PREVIEW-v1.md` / `.json` |
| Local result receipt | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-LOCAL-RESULT-v1.md` / `.json` |
| Forensic comparison | `pilots/corvonero/CORVONERO-COMMANDER-CT6-CA01-FORENSIC-COMPARISON-v1.md` / `.json` |
| CT-5R3 authority receipt | `pilots/corvonero/CORVONERO-COMMANDER-CT5R3-RESULT-v1.json` |
| Generated XLSX (Storage) | `X:\AI MARS STORAGE\exports\corvonero\CORVONERO-COMMANDER-CT5R3-FINAL-2026-06-30\` |
| This report | `reports/REPORT-corvonero-commander-ct6-ca01-local-import-test-v1.md` |

---

## Verdict

```
CORVONERO COMMANDER CT-6 CA-01:
PASS — LOCAL IMPORT MATCHES FINAL AUTHORITY

Campaigns:
1

Groups:
7

Phrases:
339

Ads:
7

Preview errors:
0

Unparsed rows:
0

Server upload:
NOT PERFORMED

CA-02–CA-05 local import:
READY FOR SEPARATE AUTHORIZATION
```

---

## UNKNOWN

- Commander version on operator workstation: **UNKNOWN** (not recorded in operator evidence).
- Group-negative and campaign-negative field-by-field Commander display: **OPERATOR CONFIRMED GENERALLY — DETAILED FIELD-BY-FIELD INSPECTION NOT RECORDED**.

---

## SECURITY RISK

None identified. No server upload, Yandex Direct access, or campaign launch occurred in this task scope.
