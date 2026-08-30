# I-SEO Report Hub — Field Help Question Icon Design v0.1

**Status:** UX/design planning — **no code in this wave**  
**Date:** 2026-08-21  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01  
**Recommended first implementation:** Field Help Question Icon Implementation 01 (render/UI only, no DB)

---

## Goal

SEO specialists see a small **`?`** control next to important field/section labels.  
Click (and keyboard) opens a short Russian hint; where useful, an **example** of good fill.  
Interface stays calm — no tooltip spam, no modal stacks, no external packages.

---

## UX rules

| Rule | Detail |
|------|--------|
| Control | Compact circular/`?` button beside label text |
| Default | Help panel **collapsed / hidden** |
| Open | Click or Enter/Space on focused control |
| Close | Second click, Esc, or click outside (if JS present) |
| Progressive enhancement | Prefer `<details>`/`<summary>` or `popover`/checkbox hack **without** heavy JS; optional tiny toggle script only if needed |
| A11y | `button` or summary with accessible name, e.g. `Подсказка: Кратко для клиента`; `aria-expanded` if custom JS |
| Density | One help control per field/section — not per every helper sentence already on screen |
| Existing `field-hint` | Keep short static hints; `?` carries deeper “what to write” + example |
| Client preview | **No** `?` on client-facing preview/print (internal forms only) |

---

## Visual sketch (CSS intent)

- Size ~18–20px hit target; visually ~14–16px
- Neutral border; no purple/glow; match existing `app.css` buttons
- Panel: light surface, 12–16px padding, max-width ~28–36rem, below label
- Example block: muted background, label «Пример:»
- `prefers-reduced-motion`: no animated bounce

---

## Where to add first (priority)

### A. Work entry form  
`app/Views/pages/monthly-report-work-entries/form.php`

| Field | Help |
|-------|------|
| Категория | yes |
| Работа из каталога | yes |
| Название | yes |
| Описание | yes |
| Статус | yes |
| Роль в периоде | yes |
| Видимость для клиента | yes |
| Кратко для клиента | yes (high) |
| Внутренняя заметка | yes (high) |
| Заметка по доказательствам | yes (high) |
| Порядок | brief |

### B. Report block form  
`app/Views/pages/report-blocks/form.php`

| Field | Help |
|-------|------|
| Ключ блока | yes |
| Тип блока | yes |
| Название | yes |
| Кратко (`summary`) | yes |
| Текст (`body`) | yes |
| Статус | yes |
| `data_json` | yes (warn: advanced) |
| `source_metric_refs` | yes (warn: demo/fictional care) |
| Owner/reviewer | optional brief |

### C. Monthly report content form  
`app/Views/pages/monthly-reports/form.php` — all `UiLabels::blockKeyMap()` textareas:

- Краткое резюме  
- Что сделали  
- Результаты  
- Ключевые выводы  
- Риски и блокеры  
- План на следующий месяц  
- Заметки для клиента  
- Внутренние заметки  

Plus title + status if space allows.

### D. Not first pass

- Health page  
- Login  
- Export/share admin panels  
- Client preview document chrome  

---

## Reusable implementation idea (no DB migration)

1. **Help copy map** — PHP array/config, e.g. `app/Support/FieldHelpCopy.php` or `config/field-help.php`  
   Keys: `work_entry.client_summary`, `monthly.risks_and_blockers`, …
2. **Partial** — `app/Views/partials/field-help.php`  
   Params: `key`, optional override title  
   Renders: label adornment + collapsed help + example
3. **CSS** — scoped in `public/assets/css/app.css` (`.field-help`, `.field-help__btn`, `.field-help__panel`)
4. **JS** — optional minimal module only if `<details>` insufficient; no npm packages
5. **Helper** — `field_help('work_entry.client_summary')` in `helpers.php`

Static copy is enough for pass 01 — **no DB table** for help text.

---

## Copy source

Authoritative draft pack:  
[I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md](I-SEO-REPORT-HUB-FIELD-HELP-COPY-PACK-v0.1.md)

---

## Acceptance for design doc

- `?` + click/keyboard behavior defined  
- Priority surfaces listed  
- Reusable partial/config approach without DB  
- Client preview excluded  
