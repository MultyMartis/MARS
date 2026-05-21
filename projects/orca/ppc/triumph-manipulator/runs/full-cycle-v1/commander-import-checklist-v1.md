# Commander Import Checklist v1

Use after opening `triumph-sheet1-patch-full-cycle-v1.xlsx` in Yandex Direct Commander (or web import flow).

## Pre-import

- [ ] Validation report `export_allowed: true` for `triumph-manipulator-krd-search-full-cycle-v1`
- [ ] Human review gate: operator accepts draft copy and URLs
- [ ] Backup existing campaign in Direct if re-importing
- [ ] Confirm template version matches `assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` lineage

## Post-import spot checks

- [ ] Campaign type / structure readable (no corrupt sheet1)
- [ ] **Region** = Краснодарский край (not «Все», not multi-line)
- [ ] **Ad type** = Текстово-графическое on ad rows
- [ ] **Display URL** = short latin paths only (≤20 chars), no `manipulator-triumph.ru/` in display field
- [ ] **Final URL** = `https://manipulator-triumph.ru/.../` per group
- [ ] Fastlinks present and deduplicated per ad
- [ ] No image URL cells populated
- [ ] Keywords and negatives imported as expected (phrase match)
- [ ] Manual CPC / bids set by operator (not auto-optimized in this pass)

## Landing continuity (HITL)

- [ ] Group 01 → `/manipulyator-5-tonn/` hero matches 5 т / стрела / вылет
- [ ] Group 06 → `/perevozka-oborudovaniya/` — **verify live page** (SAFE UNKNOWN until confirmed)
- [ ] Remaining slugs match production site navigation

## After import

- [ ] Set `human_review.approved_for_commander_import` in JSON only after successful smoke import
- [ ] Do **not** enable launch without separate launch approval
- [ ] Log friction in OPERATIONAL-INDEX / run notes if Commander rejects rows

## References

- `tools/exporter-cli/commander-import-observations-v0.md`
- `tools/exporter-cli/commander-region-fix-v0.6.md`
- `validation/commercial-validation-rules-v1.md`
