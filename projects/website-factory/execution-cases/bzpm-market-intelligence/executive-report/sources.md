# Источники authority — BZPM Executive Presentation Package v2.1 RU

Все материалы Executive Package основаны **только** на утверждённых authority-документах. Новые выводы не изобретались.

**Источники используются как утверждённая база исследования; новые данные при формировании v2.1 не добавлялись.**

**Версия:** v2.1 RU  
**Дата:** 2026-07-02  
**Изменение:** Russian localization + client-facing commentary pass  

---

## Первичные источники (обязательные)

| Документ | Путь | Использование в пакете |
| --- | --- | --- |
| **BZPM Competitor Registry v2** | `../BZPM-COMPETITOR-REGISTRY-v2.md` | 126 сущностей, таксономия tier/status, merge table, benchmark IDs, статистика SERP |
| **BZPM Market Intelligence Master Report v1** | `../BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md` | Итоги discovery, география, распределение tier, региональное покрытие, лидеры SERP, история программы, готовность W4 |
| **BZPM Operator Insights v1** | `../BZPM-OPERATOR-INSIGHTS-v1.md` | UX-паттерны, Native Benchmark Group, FIM markers, operator highlights — основа Word-выводов |

---

## Вторичные источники (контекст)

| Документ | Путь | Использование |
| --- | --- | --- |
| **Presentation Pack README** | `../presentation-pack/README.md` | Описание отличий operational vs executive layer |
| **Presentation Pack Export Report** | `../presentation-pack/EXPORT-REPORT.md` | Валидация counts, структура operational pack |
| **Presentation Pack Generator** | `../presentation-pack/generate_bzpm_pack.py` | Паттерны парсинга registry, валидация chart data |

---

## Authority волн (встроено в Master Report / Registry)

| Волна | Название | Ключевые outputs (из authority) |
| --- | --- | --- |
| W1 | Картирование рынка | Позиционирование + buyer journey baseline |
| W2 | Поиск конкурентов | Пул 80 кандидатов |
| W2.5 | Приоритизация | 46 Approved; 34 отложено |
| W3 | Реестр конкурентов | COMP-BZPM-001…046; 13 review flags |
| W3R | Региональное усиление | 38 региональных строк; пулы Barnaul/Siberia/Ural/FE/KZ/BY |
| W3S | Поисковая видимость (SERP) | Матрица 20 запросов; 40 доменов; 27 новых кандидатов |
| W3X | Консолидация реестра | Registry v2 + Master Report v1 |
| W3Y | Операторские наблюдения | Operator Insights v1 |

---

## Трассируемость метрик

| Метрика | Значение | Authority |
| --- | ---: | --- |
| Канонические сущности | 126 | Registry v2, Master Report §1 |
| Утверждённый реестр (Approved) | 46 | Registry v2, Master Report §1 |
| Strong expansion | 21 | Registry v2, Master Report §1 |
| Possible expansion | 22 | Registry v2, Master Report §1 |
| Отложено (Deferred) | 26 | Registry v2, Master Report §1 |
| Исключено (Excluded) | 11 | Registry v2, Master Report §1 |
| Пул W2 discovery | 80 | Master Report §1 |
| Региональные строки W3R | 38 | Registry v2, Master Report §1 |
| Новые SERP-домены W3S | 27 | Registry v2, Master Report §1 |
| Доменов в SERP | 40 | Master Report Statistics |
| Матрица SERP-запросов | 20 | Master Report §8 (W3S) |
| Review Required flags | 13 | Master Report §9 |
| Operator highlights | 7 | Operator Insights §Operator Highlight Registry |
| Observed patterns | 10 | Operator Insights §Observed Pattern Registry |
| Benchmark group | 6 | Operator Insights §Native Benchmark Group |
| FIM markers | 7 | Operator Insights §Future Investigation Markers |

---

## Явно НЕ использовались как authority

| Материал | Причина |
| --- | --- |
| `bzpm-catalog-redesign/*` | Operator Insights v1 §Program Impact: отдельно от W3Y capture; cross-reference допустим, слияние не предполагается |
| Session transcripts / `.recovery-temp` | Не закоммиченные артефакты |
| BZPM MI Methodology v1 | SAFE UNKNOWN — не найден в репозитории (Registry v2, Master Report §9) |
| W1 Market Mapping Report | SAFE UNKNOWN — не найден в репозитории |
| Operator Manual Review Notes (verbatim) | SAFE UNKNOWN — не закоммичены в репозитории; только формализованные W3Y highlights |

---

## Цепочка регенерации

```
BZPM-COMPETITOR-REGISTRY-v2.md
BZPM-MARKET-INTELLIGENCE-MASTER-REPORT-v1.md
BZPM-OPERATOR-INSIGHTS-v1.md
        ↓
generate_executive_report.py
        ↓
BZPM Market Research.xlsx
BZPM Research Conclusions.docx
```
