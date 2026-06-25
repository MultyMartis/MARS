# V6 Repair Package Side Effects

**Generated:** 2026-06-22T05:54:01.264Z

## Root causes

1. **Commercial seed exclusion** — 41 direct commercial phrases excluded via `semantic_status_changes`.
2. **Group-empty HOLD** — 8 operator-scope groups auto-held when keyword_count reached 0.
3. **Generic controlled-test hypotheses** — 15 unrelated phrases received TS PIOT/marking template.
4. **Informational leakage** — active v6 phrases with verification/regulatory year signals retained.

## Held groups

- **CORV-G07-04** (Восстановление работы 1С): 1 exclusions, seeds: восстановление работы 1с
- **CORV-G05-06** (Перенос данных в 1С): 2 exclusions, seeds: миграция данных 1с, перенос данных в 1с
- **CORV-G04-01** (Расчёт себестоимости в 1С): 2 exclusions, seeds: расчет себестоимости 1с, себестоимость в 1с
- **CORV-G04-02** (Планирование закупок 1С): 1 exclusions, seeds: планирование закупок 1с
- **CORV-G04-03** (Платёжный календарь 1С): 1 exclusions, seeds: платежный календарь 1с
- **CORV-G01-02** (Программист 1С Новосибирск): 2 exclusions, seeds: —
- **CORV-G01-06** (Обслуживание 1С): 3 exclusions, seeds: обслуживание 1с для организации
- **CORV-G01-04** (Внедрение 1С): 2 exclusions, seeds: внедрение 1с
