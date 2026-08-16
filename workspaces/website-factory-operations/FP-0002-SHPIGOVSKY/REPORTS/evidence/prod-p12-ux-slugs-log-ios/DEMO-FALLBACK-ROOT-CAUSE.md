# Dependence nature demo fallback — root cause

## Symptom

`/uslugi/zavisimosti/` § «Природа зависимости» showed demo-like blocks:

- Нейробиология
- Генотипирование
- Подробнее о генотипировании

while Admin repeater «Текстовые блоки» was empty.

## Root cause

1. Admin SoT repeater `section_nature_text_blocks` on post `#73` = **empty** (confirmed production meta).
2. Helper `shpigovsky_get_section_nature_text_blocks()` still **fell through to legacy pair metas**:
   - `section_nature_neurobiology_*`
   - `section_nature_genotyping_*`
3. Those legacy metas still held seeded demo headings/labels from earlier waves.
4. Legacy fields are **not** in current ACF Admin UI (only the repeater is) — so FE contradicted Admin.

Hardcoded PHP emergency `shpigovsky_get_section_nature_text_blocks_fallback()` was **not** on the normal FE path.

## Fix (canonical owner)

`inc/service-section-helpers.php` — resolver returns **only** normalized repeater rows.  
Empty repeater → empty FE (omit text-block subsections).  
Legacy metas left dormant in DB (not deleted; Olya content not mass-wiped).

DEPENDENCE NATURE TEXT BLOCKS = ADMIN DATA ONLY, NO DEMO FRONTEND FALLBACK

## QA

| Route | Result |
|-------|--------|
| `/uslugi/zavisimosti/` | nature subsection heads **[]**; no neurobiology/geno demo link |
| `/uslugi/psihicheskoe-zdorovie/` | real Admin nature rows still render |
| `/uslugi/lechenie-alkogolnoy-zavisimosti/` | no false nature demo inject |
