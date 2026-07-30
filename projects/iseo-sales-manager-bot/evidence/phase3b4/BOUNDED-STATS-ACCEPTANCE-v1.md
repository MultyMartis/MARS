# BOUNDED STATS ACCEPTANCE v1

## Verdict

**PASS** (harness path; bounded CLEAN read + SYNTHETIC_TEST filter)

## Output sample

```
Статистика за 7 дней

Всего заявок: 4
Новых: 2
Повторных: 0
Возможных повторов: 0
Повторных обработок: 0

Без ИИ: 4
С ИИ: 0
Fallback на шаблон: 0

Данных достаточно: 1
Нужно уточнение: 3
Недостаточно для связи: 0

Ошибок обработки: 0

Контур: разработка
В статистике учитываются только SYNTHETIC_TEST.
```

## Gates

- Default window 7 days
- Dev contour label present
- Only SYNTHETIC_TEST rows counted
- Missing categories shown as 0
- No AI / Gmail calls in stats path
