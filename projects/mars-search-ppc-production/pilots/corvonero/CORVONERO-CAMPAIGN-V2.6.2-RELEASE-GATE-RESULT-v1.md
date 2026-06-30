# Corvonero Campaign V2.6.2 — Release Gate Result v1

**Status:** `RELEASE_GATE_PASS`  
**Evaluated:** 2026-06-30T17:01:33Z  
**Semantic authority:** V2.6 (unchanged)  
**Deployable package:** V2.6.2

## Phrase-slot reconciliation

| Metric | Value |
|--------|------:|
| Authority phrase slots | 926 |
| Artifact phrase slots | 926 |
| Delta | 0 |
| Missing | 0 |
| Unexpected | 0 |
| Duplicates | 0 |
| Pass | true |

## Gate command

```powershell
cd projects/mars-search-ppc-production/tools/commander-transport
$env:MARS_SKIP_VOLUME_CHECK='1'
node src/release-gate-cli.mjs --project corvonero `
  --package "X:\AI MARS STORAGE\exports\corvonero\CORVONERO-CAMPAIGN-V2.6.2-FINAL-2026-06-30" `
  --authority "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-RELEASE-STATE-v1.json" `
  --receipt "X:\AI MARS\projects\mars-search-ppc-production\pilots\corvonero\CORVONERO-CAMPAIGN-V2.6-OPERATOR-SEMANTIC-APPROVAL-v1.json" `
  --json
```

**Commander import:** NOT PERFORMED  
**Yandex Direct launch:** NOT APPROVED

Machine-readable: `CORVONERO-CAMPAIGN-V2.6.2-RELEASE-GATE-RESULT-v1.json`
