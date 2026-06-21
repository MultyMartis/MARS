# AG-WP-001 — Forge WordPress Boundaries

**Agent ID:** AG-WP-001  
**Status:** SEED  
**Date:** 2026-06-11  

---

## Purpose

Зафиксировать границы **направления** Forge WordPress на стадии SEED — без расширения scope и без production claims.

---

## Forge WordPress делает (намерение SEED)

| Boundary | Meaning |
|----------|---------|
| **WordPress production direction** | Определяет **будущую** роль перевода Frontend-результата Factory в WordPress |
| **Learning accumulation** | Принимает знания **только** из реальных Factory-проектов по [AG-WP-001-LEARNING-PROTOCOL.md](AG-WP-001-LEARNING-PROTOCOL.md) |
| **Expertise framing** | Держит производственную дисциплину WordPress как **направление**, не как инструмент |
| **Companion alignment** | Согласуется с WPilot как инструментальным мостом — см. [AG-WP-001-WPILOT-CONNECTION.md](AG-WP-001-WPILOT-CONNECTION.md) |

---

## Forge WordPress не делает

| Exclusion | Why |
|-----------|-----|
| **Не заменяет Frontend Production** | Gulp / Forge frontend lanes остаются canonical для статического Frontend; WordPress — **downstream** направление |
| **Не заменяет Website Factory** | Factory — родительская система координации; Forge WordPress — **одно внутреннее направление** |
| **Не заменяет разработчика** | Human-operated execution; нет автономных mutation claims |
| **Не заменяет WPilot** | WPilot — инструмент inspection/safe-change; Forge WordPress — экспертное производственное знание |
| **Не создаёт runtime** | Нет dispatcher, orchestrator, agent service |
| **Не создаёт правила без evidence** | Production / ACF / Theme rules запрещены на стадии SEED |
| **Не является отдельным проектом MARS** | Живёт в Factory operations zone, не в `projects/` как standalone system |
| **Не владеет hosting, DNS, deploy** | Внешние системы; Factory terminal ≠ go-live |

---

## Boundary pairs (critical)

```text
  Website Factory          Forge WordPress (SEED)
  ─────────────────        ──────────────────────
  coordination + layers    WordPress production direction (future)
  multi-agent story        single internal seed — not registered agent

  Frontend Production      Forge WordPress
  ─────────────────        ─────────────────
  static Gulp/Forge output  WordPress implementation (future handoff consumer)

  WPilot                   Forge WordPress
  ──────                   ───────────────
  tool / bridge            expertise / production discipline
  safe scoped changes      what to build and how (from evidence later)
```

---

## Interaction with FP-0002

FP-0002 — **First Learning Project**, не production authority для Forge WordPress.

| Rule | Meaning |
|------|---------|
| Delivery first | Клиентский проект важнее system learning |
| No speculative rules | Паттерны фиксируются post-hoc — см. [WORDPRESS-PRODUCTION-LEARNING-CHARTER.md](../../FP-0002-SHPIGOVSKY/WORDPRESS-PRODUCTION-LEARNING-CHARTER.md) |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Точная граница «Frontend handoff complete» → «WordPress start» | **SAFE UNKNOWN** |
| Совместное использование WPilot на FP-0002 | **SAFE UNKNOWN** — future production evidence |

---

*Seed boundaries only. No enforcement product. No runtime.*
