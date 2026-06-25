# FP-0002 V7 Intro Content Map

**Figma group:** `2 - Дом - вступление` (`1:927`)  
**Frontend partial:** `src/partials/sections/home-recovery-intro.html`  
**DOM policy:** text replacement only — **PRESERVED**

| Figma visible node | Current HTML element | Current text (before) | Required text (Figma) | Action |
| ------------------ | -------------------- | --------------------- | --------------------- | ------ |
| `1:929` TEXT | `.home-recovery-intro__heading` | Шпиговский дом — восстановление с уважением к личности | Same | NO CHANGE |
| `1:931` TEXT | `.home-recovery-intro__lead` | …в «Шпиговский Дом»… | Same | NO CHANGE |
| `1:933` INSTANCE override | `.home-recovery-intro__benefits-item` ×1 | высокий уровень комфорта; | Same | NO CHANGE |
| `1:934` INSTANCE override | `.home-recovery-intro__benefits-item` ×2 | анонимное лечение зависимостей; | Same | NO CHANGE |
| `1:935` INSTANCE override | `.home-recovery-intro__benefits-item` ×3 | психотерапевтическая реабилитация; | Same | NO CHANGE |
| `1:936` INSTANCE override | `.home-recovery-intro__benefits-item` ×4 | лечение зависимости без потери личности, статуса и связи с жизнью. | Same | NO CHANGE |
| `1:944`/`13:4502` TEXT | `.home-recovery-intro__card-title` | Реабилитация без изоляции | Same | NO CHANGE |
| `1:945`/`13:4503` TEXT | `.home-recovery-intro__card-text` (card 1) | …договорённости… «выпадать из жизни» | …договоренности… “выпадать из жизни” | REPLACE |
| `1:950`/`13:4508` TEXT | `.home-recovery-intro__card-title` | Участие семьи и близких | Same | NO CHANGE |
| `1:951`/`13:4509` TEXT | `.home-recovery-intro__card-text` (card 2) | Same | Same | NO CHANGE |
| `1:956`/`13:4514` TEXT | `.home-recovery-intro__card-title` | Выявление и устранение причины зависимости | Same | NO CHANGE |
| `1:957`/`13:4515` TEXT | `.home-recovery-intro__card-text` (card 3) | …её причины… | …ее причины… | REPLACE |

## Desktop/mobile text differences

Mobile heading `1:4038` contains a line break after em dash; treated as responsive wrap only — **single semantic HTML** retained.

## Verdict

`INTRO CONTENT REPLACEMENT` — **PASS** (2 card body fields updated; DOM/SCSS unchanged)
