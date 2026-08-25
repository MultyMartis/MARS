# Knowledge Inventory

## Start Here

1. [FINAL-HANDOFF.md](../FINAL-HANDOFF.md)
2. [PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md)
3. [CURRENT-PRODUCTION-ARCHITECTURE.md](../architecture/CURRENT-PRODUCTION-ARCHITECTURE.md)
4. [OPERATIONAL-RUNBOOKS.md](../runbooks/OPERATIONAL-RUNBOOKS.md)
5. [RECOVERY-GUIDE.md](../recovery/RECOVERY-GUIDE.md)

## Canonical Stable Baselines

- `baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md`
- `baselines/PRODUCTION-STABLE-ACCEPTANCE-MATRIX-2026-08-17.md`
- `baselines/PRODUCTION-STABLE-KNOWN-STATE-2026-08-17.md`
- `evidence/stable-baseline-20260817/`

These are the canonical live truth for the stable contour.

## Current Architecture Pack

- `architecture/CURRENT-PRODUCTION-ARCHITECTURE.md`
- `architecture/DATA-STATE-MODEL.md`
- `architecture/LEAD-LIFECYCLE-CURRENT.md`
- `architecture/GMAIL-INTAKE-CONTRACT.md`
- `architecture/TELEGRAM-PRODUCT-CONTRACT.md`
- `architecture/REMINDER-CONTRACT.md`
- `architecture/ADMIN-OPERATOR-CONTRACT.md`
- `architecture/SHEETS-DEPENDENCY-MAP.md`

## Operator Pack

- `runbooks/OPERATIONAL-RUNBOOKS.md`
- `recovery/RECOVERY-GUIDE.md`
- `checklists/PRE-PRODUCTION-CHECKLIST.md`
- `checklists/CUTOVER-CHECKLIST.md`
- `checklists/TELEGRAM-UX-ACCEPTANCE-CHECKLIST.md`
- `checklists/RAW-SOURCE-ACCEPTANCE-CHECKLIST.md`
- `checklists/REMINDER-NATURAL-ACCEPTANCE-CHECKLIST.md`
- `checklists/STABLE-FREEZE-CHECKLIST.md`
- `checklists/INCIDENT-FORENSIC-CHECKLIST.md`

## Reproduction And Roadmap Pack

- `playbooks/REPRODUCE-SALES-MANAGER-FOR-NEW-PROJECT.md`
- `roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md`
- `roadmap/DB-FIRST-MIGRATION-ROADMAP.md`
- `roadmap/DEFERRED-PRODUCT-ROADMAP.md`
- `roadmap/DEEP-RESEARCH-BACKLOG.md`
- `roadmap/PROJECT-NEUTRAL-TEMPLATE.md`

## Historical Material

- `architecture/*-v1.md` Phase 2 architecture documents are historical where they conflict with the stable baseline.
- `implementation/SHEETS-MIGRATION-SPEC-v1.md` describes historical sheet layout work, not the preferred successor architecture.
- `reports/` and `evidence/` contain forensic and phase evidence. Treat them as support unless promoted by baseline docs.

## Current Truth Summary

Production is stable on Sales Manager v2 baseline. n8n executes the bot. AI is off. Google Sheets are current persistence. Natural Monday reminder live acceptance remains pending observation unless superseded by later evidence.

