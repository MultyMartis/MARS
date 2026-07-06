# FP-0002 V9-06E10 Remediation Plan v1

**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/remediation-plan.json`

## Phase plan (no repair in E10)

| Phase | Goal | Notes |
|-------|------|-------|
| **E11** | Full static-to-WP page contract inventory | Every V9 route: static source, WP route, expected vs current section stack, content status, repair action |
| **E12** | One-page-at-a-time strict V9 replacement | Start: `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`; replace inner markup from static partials; fork home partials where needed |
| **E13** | Stable checkpoint refresh | Only after screenshot parity all required routes; E3 remains invalidated |

## Explicitly forbidden

- Broad blind refactor across all templates
- Probe-only PASS
- ACF/content seed without static trace
- Repair without pre-published section map

## Backup reference

Pre-audit backup: `X:\AI MARS STORAGE\backups\fp-0002-shpigovsky\v9-06e10-root-cause-pre-audit-20260706-212334\`
