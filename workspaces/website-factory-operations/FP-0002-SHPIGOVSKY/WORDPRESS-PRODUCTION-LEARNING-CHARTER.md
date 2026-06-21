# FP-0002 — WordPress Production Learning Charter

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-11  
**Status:** **documented** — learning intent only; no knowledge captured yet  

---

## Purpose

Fix the learning contract between **this client delivery project** and **MARS / Website Factory system evolution**.

This charter is **not** a knowledge base. It defines **how** real project work may later feed system learning — without delaying delivery.

---

## Goal

Use the Shpigovsky.ru project as the **first real production source** for learning in:

| Learning domain | Container |
|-----------------|-----------|
| WordPress Production Agent patterns | [KNOWLEDGE-EXTRACTION/wp-patterns/](KNOWLEDGE-EXTRACTION/wp-patterns/) |
| ACF patterns | [KNOWLEDGE-EXTRACTION/acf-patterns/](KNOWLEDGE-EXTRACTION/acf-patterns/) |
| Theme architecture patterns | [KNOWLEDGE-EXTRACTION/theme-patterns/](KNOWLEDGE-EXTRACTION/theme-patterns/) |
| Deployment patterns | [KNOWLEDGE-EXTRACTION/deployment-patterns/](KNOWLEDGE-EXTRACTION/deployment-patterns/) |
| WPilot evolution inputs | [KNOWLEDGE-EXTRACTION/wpilot-improvements/](KNOWLEDGE-EXTRACTION/wpilot-improvements/) |

Extraction happens **after** relevant production work — not during foundation.

---

## Priority rule

```text
  PROJECT DELIVERY  ──always──▶  priority 1
  SYSTEM LEARNING   ──only when──▶  delivery not blocked
```

| Rule | Meaning |
|------|---------|
| **Project first** | Client delivery timelines and quality take precedence over system documentation |
| **Learn from reality** | Patterns are extracted from **actual** decisions and implementations on this project |
| **No speculative patterns** | Do not pre-fill learning containers before production evidence exists |
| **No delivery delay** | System learning must **not** block or slow project milestones |

---

## Boundaries

| This charter **is** | This charter **is not** |
|---------------------|-------------------------|
| A discipline for post-hoc learning capture | A WordPress architecture spec |
| A container routing policy | An agent runtime or automation mandate |
| A guard against system-work crowding out delivery | Permission to expand project scope for “research” |

---

## Activation

Learning extraction containers become **active** only when:

1. Relevant production lane has **started** (see [PROJECT-STATUS.md](PROJECT-STATUS.md))
2. Operator identifies a **repeatable pattern** worth recording
3. Recording does **not** delay the current delivery task

Until then, all KNOWLEDGE-EXTRACTION/ folders remain **empty by design**.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Whether ACF will be used | **SAFE UNKNOWN** — scope not attested |
| WordPress theme approach | **SAFE UNKNOWN** — awaiting design intake |
| WPilot integration points | **SAFE UNKNOWN** — future production evidence |

---

*Human-operated learning charter. Not a knowledge product.*
