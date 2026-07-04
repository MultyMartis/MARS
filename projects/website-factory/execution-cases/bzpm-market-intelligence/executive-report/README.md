# BZPM Executive Presentation Package v2.1 RU

**Программа:** BZPM Market Intelligence  
**Стадия:** Executive Presentation Layer  
**Статус:** W3X + W3Y Approved  
**Версия:** v2.1 RU  
**Дата генерации:** 2026-07-02  
**Изменение:** Russian localization + client-facing commentary pass  

---

## Назначение

Executive Presentation Package — **презентационная версия** исследования рынка ЗПМ. Документы в этом пакете предназначены для:

- показа клиенту, руководству или новому сотруднику через год и более;
- полного понимания методологии, масштаба, данных и выводов исследования;
- обоснования решений при разработке нового сайта ЗПМ.

Это **не** рабочая таблица и **не** обновление существующих Excel из Presentation Pack.

---

## Состав пакета

| # | Файл | Назначение |
| --- | --- | --- |
| 01 | `BZPM Market Research.xlsx` | Презентационный Excel — 12 листов: обложка, цели, методология, KPI, география, классификация, диаграммы, benchmark, SERP, изученные поверхности, факты, приложение |
| 02 | `BZPM Research Conclusions.docx` | Аналитический Word — 14 разделов выводов (не дублирует Excel и реестр) |
| 03 | `README.md` | Этот файл — описание пакета |
| 04 | `sources.md` | Перечень authority-документов |
| — | `generate_executive_report.py` | Генератор пакета из authority markdown |

---

## Что открыть клиенту

| Задача | Файл |
| --- | --- |
| **Презентация и обзор данных** | `BZPM Market Research.xlsx` |
| **Выводы и рекомендации для сайта** | `BZPM Research Conclusions.docx` |
| **Проверка источников** | `sources.md` |

Клиенту для первого знакомства: **Excel** (дашборд и диаграммы) + **Word** (выводы). Рабочие таблицы и полный реестр — не в этом пакете.

---

## Чем отличается от Presentation Pack

| Аспект | Presentation Pack | Executive Report |
| --- | --- | --- |
| **Формат** | 6 рабочих Excel-файлов | 1 презентационный Excel + 1 Word с выводами |
| **Аудитория** | Оператор, аналитик, Website Factory | Клиент, руководство, новый участник проекта |
| **Содержание** | Полные таблицы, чеклисты, фильтры | KPI-карточки, диаграммы, narrative, выводы |
| **Выводы** | Нет — только данные | Word-документ с аналитикой |
| **Стиль** | Рабочий/операционный | Консалтинговый презентационный |
| **Язык (v2.1 RU)** | Операционный | Полностью клиентский русский + пояснения |
| **Обновление** | `presentation-pack/generate_bzpm_pack.py` | `executive-report/generate_executive_report.py` |

**Presentation Pack не изменяется** при создании Executive Report.

---

## Аналитическая основа

Для углублённой работы и верификации данных используйте authority markdown в родительской папке:

- `../BZPM-COMPETITOR-REGISTRY-v2.md` — полный реестр 126 сущностей
- `../BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md` — master report
- `../BZPM-OPERATOR-INSIGHTS-v1.md` — операторские UX-наблюдения

Executive Package — **презентационный слой** поверх этих документов, без новых данных.

---

## Регенерация

```powershell
cd "X:\AI MARS\projects\website-factory\execution-cases\bzpm-market-intelligence"
python executive-report/generate_executive_report.py
```

Парсит authority markdown из родительской папки `bzpm-market-intelligence/`. Не изменяет authority и Presentation Pack. Повторная генерация создаёт русскую версию v2.1 RU.

---

## Границы scope

- **In scope:** Презентационное оформление, выводы из утверждённых данных, диаграммы, narrative, клиентские пояснения
- **Out of scope:** Новое исследование, изменение registry, W4 intelligence, UX audit scoring

---

## Связанные материалы

- Presentation Pack: `../presentation-pack/`
- Registry authority: `../BZPM-COMPETITOR-REGISTRY-v2.md`
- Master Report: `../BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md`
- Operator Insights: `../BZPM-OPERATOR-INSIGHTS-v1.md`
