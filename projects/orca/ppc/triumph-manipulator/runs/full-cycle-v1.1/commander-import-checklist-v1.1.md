# Commander Import Checklist v1.1

Use after opening `triumph-sheet1-patch-full-cycle-v1.1.xlsx` in Yandex Direct Commander (or web import flow).

## Pre-import

- [ ] Validation report shows `export_allowed: true`
- [ ] File opens in Excel without repair prompt
- [ ] Row count ends at **123** (no stale rows 124+)
- [ ] Groups **11** and **12** visible with correct display paths: `kray`, `zakaz-manip`

## Post-import spot checks

| Group | Check |
|-------|--------|
| 11 | Landing `…/manipulyator-krasnodarskiy-kray/`, display `kray`, region Краснодарский край |
| 12 | Landing `https://manipulator-triumph.ru/`, display `zakaz-manip`, commercial ads present |

## HITL

- [ ] Operator approves `human_review.approved_for_commander_import`
- [ ] Live URLs for krai page and homepage verified on production
- [ ] No unintended broad match expansion beyond phrase policies in JSON

**Not** automated launch · **not** runtime orchestration.
