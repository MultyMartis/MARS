# FP-0002 — NEXT WEB-GPT HANDOFF

## Project
- name: **FP-0002 / Шпиговский**
- production domain: `https://shpigovsky.ru/`
- phase: **PRODUCTION / MAINTENANCE — STABLE**

## Current Production State
- runtime/core: WordPress; recent maintenance includes stages reusable-fallback repair (2026-09-14)
- structured data: **JSON-LD LIVE** — `shpigovsky-core` module `structured-data.schema-org`
- open graph: **LIVE** — `shpigovsky-core` module `open-graph.meta`
- specialists hub: Page `#1030` `/specialisty/` uses `Specialists Hub` template
- indexing: **OPEN — human-approved**; P18G guard active; watchdog active
- robots: **Olya-approved robots policy active**; physical `/robots.txt` is editorial/SEO-owned
- forms / SMTP / anti-spam / privacy / Metrika: active as previously established

## Critical active pending wave (NOT this repair)
- **FP-0002 SERVICE CHILD-CARDS MULTI-IMAGE ADAPTIVE COMPOSITION 02**
- worktree: `X:\AI MARS STORAGE\worktrees\fp0002-service-child-cards-multi-image-02`
- branch: `wave/fp0002-service-child-cards-multi-image-02`
- uncommitted production delta still live in:
  - `template-parts/service/child-services.php`
  - `assets/css/service-child-services.css`
- **DO NOT** overwrite from origin, delete worktree/branch, or fold into unrelated commits until separately approved.

## Service stages / reusable-block precedence (MANDATORY)
Applies to subdivision Admin block **«6. Этапы / что нужно для лечения»** (`section_stages_*`) and service-general stages (`service_general_stages_*`):

```text
OFF  → hide block entirely (no reusable fallback)
ON + local meaningful content → local service content wins
ON + local empty → reusable Comfort Requirements
                 (Настройки сайта → Повторяемые блоки → fp02-block-comfort-requirements)
```

- Reusable helpers: `rehab_requirements_*` via `shpigovsky_get_rehab_requirements_*`
- Resolvers: `shpigovsky_get_section_stages_copy()`, `shpigovsky_get_general_stages_copy()`, bridge `shpigovsky_get_stages_copy_from_reusable_requirements()`
- Do **not** “fix” empty services by duplicating reusable copy into local ACF
- Genotyping fixture: `#1889` `/uslugi/genotipirovenie/` (slug spelling `genotipirovenie`); keep local empty to exercise fallback
- Report: `REPORTS/REPORT-FP-0002-SERVICE-STAGES-REUSABLE-BLOCK-FALLBACK-REPAIR-01.md`

## Authority Rules
- canonical Git truth: `origin/mars/canonical-post-recovery`
- production DB/editorial truth: current production admin/editorial state
- Olya robots truth: do not replace Olya robots with generic templates
- human indexability: do not auto-close indexing; explicit human command only
- dirty-main safety: no broad git cleanup on shared dirty main; future work should start from a fresh clean worktree
- while multi-image delta is pending: origin alone is **not** complete live source truth for child-card files

## Canonical Paths
- FP-0002 project locus: `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`
- open items: `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
- baseline: `REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
- robots ownership: `DOCS/OPERATIONS-INDEXING-ROBOTS-OWNERSHIP-v1.md`
- source/runtime authority: `WORDPRESS/SOURCE-AUTHORITY.md`

## Mandatory Maintenance Workflow
fresh intake → bounded task → exact deploy → validation → parity check → selective Git checkpoint

## Important Safeguards
- never overwrite Olya editorial DB state
- never replace Olya robots policy
- never auto-close indexing
- no broad dirty-main git operations
- preserve pending multi-image production delta until its own closeout
- structured data / OG must derive from Admin-owned fields

## Known Non-Blocking Items
- Google Search Console sitemap submission
- Yandex Webmaster sitemap submission
- optional authenticated Yandex structured-data validator pass
- optional external Facebook/Meta OG debugger pass
- optional legal sign-off on Cookie Policy
- optional `lead_retention_days=730` policy alignment
- optional anti-spam tuning only from real spam evidence
- commit/push of pending multi-image child-card wave (separate operator approval)

## Where To Read First
1. `PROJECT-STATUS.md`
2. `REPORTS/REPORT-FP-0002-SERVICE-STAGES-REUSABLE-BLOCK-FALLBACK-REPAIR-01.md`
3. `REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md`
4. `REPORTS/BASELINE-FP-0002-PRODUCTION-MAINTENANCE-STABLE.md`
