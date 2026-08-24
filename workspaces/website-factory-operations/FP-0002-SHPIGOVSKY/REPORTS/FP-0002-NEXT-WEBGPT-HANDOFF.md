# FP-0002 — NEXT WEB-GPT HANDOFF

## Project
- name: **FP-0002 / Шпиговский**
- production domain: `https://shpigovsky.ru/`
- phase: **PRODUCTION / MAINTENANCE — STABLE**

## Current Production State
- runtime/core: WordPress; current production status tracks core `0.3.25-olya-robots`
- indexing: **OPEN — human-approved**; P18G guard active; watchdog active
- robots: **Olya-approved robots policy active**; physical `/robots.txt` is editorial/SEO-owned and must stay separate from global indexing state
- forms: active
- SMTP: verified / active
- anti-spam: native first-party anti-spam active; **no external CAPTCHA**
- privacy: privacy/cookie consent active
- analytics: Yandex Metrika consent-gated; form goals consent-gated
- Dashboard: compact/current client-facing Dashboard UX active

## Authority Rules
- canonical Git truth: `origin/mars/canonical-post-recovery`
- production DB/editorial truth: current production admin/editorial state
- Olya robots truth: do not replace Olya robots with generic templates
- human indexability: do not auto-close indexing; explicit human command only
- local secrets: retain required local-only runtime/secret files; do not commit them
- dirty-main safety: no broad git cleanup on shared dirty main; future work should start from a fresh clean worktree

## Canonical Paths
- FP-0002 project locus:
  - `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`
- current open items:
  - `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
- current baseline:
  - `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
- robots ownership/runbook:
  - `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/DOCS/OPERATIONS-INDEXING-ROBOTS-OWNERSHIP-v1.md`
- source/runtime authority:
  - `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/SOURCE-AUTHORITY.md`

## Current Git Recovery Point
This handoff is finalized together with the local closeout wave. Read the matching closeout report for the exact final remote SHA:
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/REPORT-FP-0002-FINAL-LOCAL-MARS-CLOSEOUT.md`

## Mandatory Maintenance Workflow
fresh intake
→ bounded task
→ exact deploy
→ validation
→ parity check
→ selective Git checkpoint

## Important Safeguards
- never overwrite Olya editorial DB state
- never replace Olya robots policy
- never auto-close indexing
- no broad dirty-main git operations
- no external CAPTCHA currently
- spam filtering before lead persistence

## Known Non-Blocking Items
- Google Search Console sitemap submission
- Yandex Webmaster sitemap submission
- optional legal sign-off on Cookie Policy
- optional `lead_retention_days=730` policy alignment
- optional anti-spam tuning only from real spam evidence
- normal future SEO/content/feature work

## Where To Read First
1. `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md`
2. `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
3. `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
4. `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/REPORT-FP-0002-PROD-MAINT-OLYA-ROBOTS-RESTORATION.md`
5. `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/REPORT-FP-0002-FINAL-LOCAL-MARS-CLOSEOUT.md`

## Historical Evidence
Deep historical P07–P18 reports remain preserved in `REPORTS/` and `REPORTS/evidence/`.
Do not replay the full history for normal maintenance. Only drill into old reports when the current baseline/open-items/handoff files are insufficient for the specific task.

