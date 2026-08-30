# i-SEO Report Hub — Screenshot QA Checklist v0.1

**project_id:** `iseo-report-hub`  
**Wave:** App Pages Visual QA Preparation 01  
**Operator route:** [I-SEO-REPORT-HUB-MANUAL-VISUAL-QA-ROUTE-v0.1.md](I-SEO-REPORT-HUB-MANUAL-VISUAL-QA-ROUTE-v0.1.md)

---

## Filename format

```
iseo-hub-YYYYMMDD-##_page-name.png
```

Пример для даты 2026-08-21:

| # | Filename | Page |
|---|----------|------|
| 01 | `iseo-hub-20260821-01-login.png` | Login |
| 02 | `iseo-hub-20260821-02-dashboard.png` | Dashboard |
| 03 | `iseo-hub-20260821-03-reporting-periods.png` | Periods list |
| 04 | `iseo-hub-20260821-04-monthly-report-1.png` | Monthly report 1 |
| 05 | `iseo-hub-20260821-05-work-entries-1.png` | Work entries section |
| 06 | `iseo-hub-20260821-06-work-entry-create.png` | Create form |
| 07 | `iseo-hub-20260821-07-work-entry-edit.png` | Edit form |
| 08 | `iseo-hub-20260821-08-assembly-preview.png` | Assembly preview |
| 09 | `iseo-hub-20260821-09-client-preview.png` | Client preview |
| 10 | `iseo-hub-20260821-10-client-preview-print.png` | Print preview |
| 11 | `iseo-hub-20260821-11-exports-list.png` | Exports list |
| 12 | `iseo-hub-20260821-12-export-4.png` | Export detail 4 |
| 13 | `iseo-hub-20260821-13-export-shares.png` | Shares |
| 14 | `iseo-hub-20260821-14-monthly-report-5-empty.png` | Draft empty (P1) |
| 15 | `iseo-hub-20260821-15-preview-5-empty.png` | Preview empty (P1) |
| 16 | `iseo-hub-20260821-16-not-found.png` | 404 (P2) |

Если дата другая — замени `YYYYMMDD`. Номера `##` сохраняй по порядку прохода.

---

## Viewport

| Rule | Value |
|------|-------|
| Desktop | ≈ **1440px** width или полный экран |
| Mobile | **не обязателен** в этой волне |
| Include | topbar + sidebar, если они есть на странице |
| Zoom | 100% |

---

## Full-page vs first screen

| Page | Capture |
|------|---------|
| Большинство внутренних | **Первый экран** (above the fold) |
| Work entries на `/monthly-reports/1` | Секция работ (можно отдельный скрин после скролла) |
| `/assembly-preview` | **Полная страница**, если получается |
| `/preview` и `/preview/print` | **Полный документ**, если получается |
| Длинные таблицы exports/shares | Первый экран достаточно |

---

## Notes under each file

В том же чате / текстовом файле рядом со скрином:

```
Файл: iseo-hub-YYYYMMDD-##_….png
Что не нравится:
Что непонятно:
Что надо поправить:
Приоритет: low / medium / high
```

Несколько замечаний на один экран — ок (нумеруй 1, 2, 3).

---

## Do not capture / redact

- пароли;
- полные share tokens;
- длинные checksum / hash (если мешают — обрежь или не копируй в текст);
- чужие production URL / секреты.

---

## Done when

- [ ] Все **P0** файлы 01–13 сняты  
- [ ] Замечания написаны хотя бы для проблемных экранов  
- [ ] Опасные кнопки не нажимались  
- [ ] PDF / новый export не создавались
