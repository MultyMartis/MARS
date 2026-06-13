# Triumph — Legal Entity Lesson Learned v1

**Версия:** v1  
**Дата:** 2026-05-30  
**Статус:** post-mortem documentation — **no Triumph workspace modifications**  
**Связанные артефакты:**

| Документ | Роль |
|----------|------|
| [../legal/pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md](../legal/pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md) | Gap audit |
| [../legal/pilots/TRIUMPH-LEGAL-PILOT-EXECUTION-v1.md](../legal/pilots/TRIUMPH-LEGAL-PILOT-EXECUTION-v1.md) | Execution STOP |
| [../legal/examples/TRIUMPH-LEGAL-INPUT-SAMPLE-v1.md](../legal/examples/TRIUMPH-LEGAL-INPUT-SAMPLE-v1.md) | UNKNOWN fields sample |

---

## Что произошло

Triumph Legal Pilot достиг фазы preparation/execution, но **не прошёл readiness** для генерации Core Legal Pack L1–L4.

**Блокеры (documented):**

| Field | Status | Impact |
|-------|--------|--------|
| `company_name` | `UNKNOWN` | **STOP GENERATION** |
| `legal_name` | `UNKNOWN` | **STOP GENERATION** |

**Причина:** оператор не подтвердил канонические строки наименования, хотя в workspace присутствовали **конфликтующие неподтверждённые сигналы**:

- Footer: «ООО «ТРИУМФ»» (`confidence` medium)
- Legal footer variant: «Триумф» без ОПФ
- ИНН/ОГРН в footer — high confidence, но **не заменяют** legal name

См. [TRIUMPH-LEGAL-GAP-REPORT-v1.md §1.2](../legal/pilots/TRIUMPH-LEGAL-GAP-REPORT-v1.md).

---

## Структурная проблема Website Factory

До Legal Entity Discovery System v1 фабрика имела:

| Слой | Статус |
|------|--------|
| Legal Templates | ✓ |
| Legal Input Sheets | ✓ |
| Legal Generation Contracts | ✓ |
| **Legal Entity Discovery** | ✗ отсутствовал |

Discovery выполнялся **неявно**: агент/оператор читал footer, partials, scattered notes — без приоритетов, без card, без conflict reports.

---

## Как Legal Entity Discovery System v1 предотвратил бы сбой

### 1. Обязательный `project-input/legal-entity/`

Оператор запросил бы у клиента ЕГРЮЛ/реквизиты **до** legal generation. Pilot не зависел бы от footer как primary source.

### 2. Legal Entity Card до Input Sheet

```text
egrul.pdf (P1)
    ↓ extraction
LEGAL-ENTITY-CARD: legal_name = <from EGRUL>, company_name = PENDING
    ↓ conflict: footer «Триумф» vs EGRUL (P4 vs P1)
CONFLICT REPORT — not merged
    ↓ P6 operator
company_name + legal_name VERIFIED
    ↓
Legal Input Sheet (copied from card)
    ↓
Generation UNBLOCKED
```

### 3. Priority rules

Footer (P4) **не смог бы** перезаписать `legal_name` из ЕГРЮЛ (P1). Конфликт «Триумф» vs «ООО «ТРИУМФ»» был бы виден в conflict report, не скрыт в UNKNOWN Input Sheet.

### 4. `card_status = NOT_READY`

Pilot execution остановился бы на **Step 4–5** workflow с явным артефактом «что не хватает», а не на смешанном audit footer/content.

### 5. Запрет прямого discovery в Input Sheet

[LEGAL-INPUT-SHEET-v1.md](../legal/LEGAL-INPUT-SHEET-v1.md) после интеграции v1: identity fields **только** из verified card — нельзя «заполнить из gap report sample» без operator_verified card.

---

## Уроки для оператора

| # | Lesson |
|---|--------|
| 1 | ИНН/ОГРН в footer ≠ подтверждённое `legal_name` |
| 2 | Маркетинговое имя ≠ юридическое наименование без explicit P6 |
| 3 | Legal generation без card = повторение Triumph drift risk |
| 4 | Triumph unblock path: P1 docs + card + operator verify → Input Sheet → generation |

---

## Что **не** меняет этот урок

| Item | Status |
|------|--------|
| Triumph workspace files | **Unchanged** by this task |
| Legal page generation | **Not performed** |
| New site types / factories | **None** |

---

## SAFE UNKNOWN

- Whether Triumph operator will supply EGRUL to `project-input/legal-entity/` — **pending human action**.
- Exact canonical `company_name` string — **still requires operator**; system does not invent it.

---

*Lesson version: v1. Canonical location: `workspaces/website-factory-reference-v1/legal-entity/`.*
