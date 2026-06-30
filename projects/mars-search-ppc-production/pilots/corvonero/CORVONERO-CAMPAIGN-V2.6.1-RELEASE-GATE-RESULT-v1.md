# Corvonero Campaign V2.6.1 — Release Gate Result v1

> **SUPERSEDED / INVALIDATED** — see `CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-CORRECTION-v1.json`

**Original status:** `RELEASE_GATE_PASS` (false — phrase-slot reconciliation not enforced)  
**Superseded result:** `INVALIDATED`  
**Reason:** `MULTI_CAMPAIGN_PHRASE_SLOT_TOTAL_NOT_ENFORCED`  
**Authority phrase slots:** 926 | **Artifact phrase slots:** 924 | **Operator import ready:** false

**Evaluated:** 2026-06-30T16:38:05Z  **Semantic authority:** V2.6  
**Deployable package:** V2.6.1

## Verdict

**CORVONERO V2.6 / V2.6.1 RELEASE GATE: PASS — OPERATOR SEMANTIC APPROVAL RECORDED AND PACKAGE READY FOR COMMANDER IMPORT**

## Gate invocation

```powershell
cd projects/mars-search-ppc-production/tools/commander-transport
$env:MARS_SKIP_VOLUME_CHECK='1'
npm run campaign:release-gate -- --project corvonero `
  --package "X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.1-FINAL-2026-06-30" `
  --authority "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json" `
  --receipt "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json" `
  --json
```

## Summary

| Check | Result |
|-------|--------|
| Operator semantic approval | PASS |
| Authority frozen | PASS |
| Template contract | PASS |
| XLSX validation | 10/10 PASS |
| E9 embedded negatives blank | 10/10 PASS |
| Organization blank | 10/10 PASS |
| URLs without UTM | 10/10 PASS |
| TXT negatives | 10 PASS |
| Checksums | PASS (27/27) |
| Foreign-client contamination | 0 |

## Package totals (from actual XLSX)

| Metric | Value |
|--------|------:|
| Groups | 71 |
| Ads | 71 |
| Keyword rows | 924 |

Operator-approved semantic authority phrase slots: **926** (see reconciliation note in JSON result).

## Remaining operator actions

1. Import 10 XLSX into Commander
2. Reconcile counts after import
3. Manually import 10 campaign-negative TXT files
4. Manually exclude Novosibirsk and NSO from REMOTE campaigns
5. Separately authorize Yandex Direct launch

**Commander import:** NOT PERFORMED  
**Yandex Direct launch:** NOT APPROVED

Machine-readable full result: `CORVONERO-CAMPAIGN-V2.6.1-RELEASE-GATE-RESULT-v1.json`
