# ORCA Operational Index — Корво Неро

## Fast navigation

| Need | Document |
|------|----------|
| Project summary | [PROJECT.md](PROJECT.md) |
| **Operator scope correction** | [strategy/operator-scope-correction-v1.md](strategy/operator-scope-correction-v1.md) |
| **Full-service charter** | [strategy/full-service-campaign-charter-v1.md](strategy/full-service-campaign-charter-v1.md) |
| **Stage 2A report** | [artifacts/REPORT-orca-stage-2a-v1.md](artifacts/REPORT-orca-stage-2a-v1.md) |
| Stage 1 report | [artifacts/REPORT-orca-stage-1-v1.md](artifacts/REPORT-orca-stage-1-v1.md) |
| Campaign architecture | [production/campaign-architecture-v1.md](production/campaign-architecture-v1.md) |
| Ad group registry | [production/ad-group-registry-v1.json](production/ad-group-registry-v1.json) |
| Service inventory | [production/service-to-cluster-inventory-v1.md](production/service-to-cluster-inventory-v1.md) |
| Keyword production | [production/keyword-production-registry-v1.md](production/keyword-production-registry-v1.md) |
| Negative architecture | [production/negative-keyword-architecture-v1.md](production/negative-keyword-architecture-v1.md) |
| Conflict matrix | [production/conflict-negative-matrix-v1.md](production/conflict-negative-matrix-v1.md) |
| Bidding model | [production/bidding-model-v1.md](production/bidding-model-v1.md) |
| URL / landing map | [production/url-landing-map-v1.md](production/url-landing-map-v1.md) |
| Commander format | [production/direct-commander-format-contract-v1.md](production/direct-commander-format-contract-v1.md) |
| Triumph pattern audit | [production/triumph-production-pattern-audit-v1.md](production/triumph-production-pattern-audit-v1.md) |
| Ad production contract | [production/ad-production-contract-v1.md](production/ad-production-contract-v1.md) |
| Landing document contract | [production/landing-document-contract-v1.md](production/landing-document-contract-v1.md) |
| Production plan | [production/production-plan-v1.md](production/production-plan-v1.md) |
| Stage 1 (historical) | [strategy/strategic-model-comparison-v1.md](strategy/strategic-model-comparison-v1.md) |
| Stage status | [approvals/stage-1-status-v1.md](approvals/stage-1-status-v1.md) · [approvals/stage-2a-status-v1.md](approvals/stage-2a-status-v1.md) |

## MIG source (read-only)

```
incoming/mig/pilots/corvonero/session-mig-20260622-corv01/
```

## Current gate

**v7 contract gate FINAL — AUTHORITY SYNCHRONIZED; ACTUAL XLSX REVIEW AND COMMANDER DRY-RUN AUTHORIZED** (operator approval still required after external XLSX review).

| Artefact | Path |
|----------|------|
| Contract audit JSON | [production/validation/orca-production-contract-audit-v7.json](production/validation/orca-production-contract-audit-v7.json) |
| Pre-sync audit evidence | [production/validation/orca-production-contract-audit-v7-pre-sync.json](production/validation/orca-production-contract-audit-v7-pre-sync.json) |
| Contract audit report | [production/validation/orca-production-contract-audit-v7.md](production/validation/orca-production-contract-audit-v7.md) |
| Authority sync audit | [production/audit/operator-scope-authority-sync-v7.json](production/audit/operator-scope-authority-sync-v7.json) |
| Triumph contract workbook (original) | [exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT.xlsx](exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT.xlsx) |
| Triumph contract workbook (FINAL) | [exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT-FINAL.xlsx](exports/CORVONERO-V7-TRIUMPH-CONTRACT-AUDIT-FINAL.xlsx) |
| Commander v7 XLSX | [exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx](exports/CORVONERO-YANDEX-DIRECT-COMMANDER-v7.xlsx) |
| v7 production report | [artifacts/REPORT-orca-commander-v7-production.md](artifacts/REPORT-orca-commander-v7-production.md) |
| Authority sync task report | [artifacts/REPORT-corvonero-v7-authority-sync-and-final-contract-gate.md](artifacts/REPORT-corvonero-v7-authority-sync-and-final-contract-gate.md) |

**Operator scope authority:** SYNCHRONIZED — 6 stale HOLD records corrected; 31/31 families; 41/41 seeds; 0 critical; 0 high.

**Next gate:** upload and independent review of actual v7 Commander and Review XLSX files. Commander local dry-run follows only after operator review of actual files.

## Explicitly not authorized

- Campaign launch
- Client questionnaire to Roman
- Fake import-ready XLSX without Stage 2B–2C production
