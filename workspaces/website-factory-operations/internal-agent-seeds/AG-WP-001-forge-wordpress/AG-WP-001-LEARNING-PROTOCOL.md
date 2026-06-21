# AG-WP-001 — Forge WordPress Learning Protocol

**Agent ID:** AG-WP-001  
**Status:** SEED  
**Date:** 2026-06-11  

---

## Purpose

Зафиксировать **единственно допустимый** путь накопления знаний для Forge WordPress: **только реальные проекты**, без выдуманных правил.

---

## Knowledge source rule

```text
  REAL PROJECT WORK  ──only──▶  Forge WordPress knowledge
  SPECULATION        ──never──▶  Forge WordPress rules
```

| Rule ID | Rule |
|---------|------|
| **LP-01** | Знания извлекаются **после** производственных решений на реальном кейсе |
| **LP-02** | Запрещено создавать Production / ACF / Theme rules **без evidence** |
| **LP-03** | Запрещено выдумывать паттерны «на будущее» в пустые контейнеры |
| **LP-04** | Delivery проекта **всегда** приоритетнее system learning |
| **LP-05** | Каждая запись должна ссылаться на **конкретный** проект и контекст решения |

---

## Primary sources

### FP-0002 — Shpigovsky.ru (First Learning Project)

| Item | Location |
|------|----------|
| Project passport | [FP-0002-PROJECT-PASSPORT.md](../../FP-0002-SHPIGOVSKY/FP-0002-PROJECT-PASSPORT.md) |
| Learning charter | [WORDPRESS-PRODUCTION-LEARNING-CHARTER.md](../../FP-0002-SHPIGOVSKY/WORDPRESS-PRODUCTION-LEARNING-CHARTER.md) |
| Extraction root | [KNOWLEDGE-EXTRACTION/](../../FP-0002-SHPIGOVSKY/KNOWLEDGE-EXTRACTION/) |
| Forge-specific sink | [KNOWLEDGE-EXTRACTION/wordpress-agent/](../../FP-0002-SHPIGOVSKY/KNOWLEDGE-EXTRACTION/wordpress-agent/) |

**Activation:** контейнеры активны только когда production lane стартовал и operator фиксирует repeatable pattern **без задержки delivery**.

### Future Factory projects

| Rule | Meaning |
|------|---------|
| **Same protocol** | Каждый новый Factory project с WordPress lane — потенциальный learning source |
| **No pre-registration** | Новые источники добавляются **по факту** charter/project init, не speculatively |
| **Cross-project synthesis** | Обобщение в Forge rules — **только** после повторяемости на 2+ кейсах или explicit human charter |

---

## What may be captured (when evidence exists)

| Category | Allowed when | Container (FP-0002) |
|----------|--------------|---------------------|
| WordPress implementation choices | Documented on project | `wp-patterns/`, `wordpress-agent/` |
| ACF usage patterns | ACF actually used | `acf-patterns/` |
| Theme architecture decisions | Theme work started | `theme-patterns/` |
| Deployment/release patterns | Deploy evidence | `deployment-patterns/` |
| WPilot tool gaps/wins | Operator notes with evidence | `wpilot-improvements/` (feeds WPilot, not Forge rules directly) |

---

## What is forbidden at SEED stage

| Forbidden | Reason |
|-----------|--------|
| WordPress Production Rules document | No evidence pack |
| ACF Rules document | No evidence pack |
| Theme Rules document | No evidence pack |
| AGENT.md / workflow.md operational pack | SEED ≠ agent |
| Registry enrollment | Not chartered |
| «Best practices» without project anchor | Violates LP-01 |

---

## Extraction workflow (human-operated)

```text
  1. Production task completes on Factory project
  2. Operator identifies repeatable pattern (optional)
  3. If recording does NOT delay delivery:
       → write to appropriate KNOWLEDGE-EXTRACTION container
       → reference project ID, date, decision context
  4. Forge WordPress SEED consumes refs — does NOT auto-promote to rules
```

---

## Promotion criteria (SAFE UNKNOWN detail)

Переход SEED → richer documentation (e.g. operational doc pack) **не определён** в этом charter.

**Minimum future evidence (indicative, not normative):**

- ≥1 completed WordPress production cycle on Factory project
- Human charter for scope expansion
- Explicit decision on `agent_id` registration — if ever

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Whether FP-0002 uses ACF | **SAFE UNKNOWN** |
| WordPress theme approach on FP-0002 | **SAFE UNKNOWN** |
| Timeline of first knowledge capture | **SAFE UNKNOWN** — depends on production lane start |

---

*Learning protocol only. Not a knowledge base. Not enforcement.*
