# SITE-001 — W5 First Impression Decision v1

**Type:** Blueprint gate decision — Website Factory  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Blueprint input:** [SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md)  
**Direction:** **Concept B — «Современный Дилер 2026»**

**Mode:** **DESIGN DECISION ONLY** — no implementation · no CSS · no code · no FTP

---

## Decision

# **BLUEPRINT APPROVED FOR OPERATOR HITL**

Website Factory утверждает **SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1** как авторитетную архитектуру first impression для Concept B.

**Implementation:** **NOT AUTHORIZED** — awaits operator sign-off on this decision + separate W5 implementation charter.

---

## Gate assessment

| Criterion | Result |
|-----------|--------|
| Scope compliance (header · homepage first screen · used PDP first screen only) | **PASS** |
| No styling/token/atmosphere proposals in blueprint | **PASS** |
| Architecture addresses root cause (composition, not polish) | **PASS** |
| Aligns with Concept B workshop decision | **PASS** |
| Preserves Phase 1 branding, menu, phone, URLs | **PASS** |
| Preserves W3UX-C1 catalog density | **PASS** |
| Preserves W4 `w4-used-*` as re-group asset | **PASS** |
| Rejects W4.1 sticky header direction | **PASS** |
| Implementation phases W5-A…D defined | **PASS** |
| 3-second test methodology documented | **PASS** |
| Operator HITL on blueprint | **PENDING** |

---

## Blueprint summary (authorized architecture)

### Header — «Dealer shell»

- 3-band stack → **1 shell** (contact rail + primary band + **inset** promo)  
- **Centered nav** · static scroll · single primary CTA (callback)  
- Phone secondary · WhatsApp supportive · logo left anchor  

### Homepage — «Showroom entry»

- Stable **large headline** + dominant vehicle visual  
- **Floating search card** as primary entry (overlapping hero)  
- Featured vehicles horizontal peek below fold edge  

### Used PDP — «Magazine PDP»

- **Stage band** — gallery 70% edge-dominant  
- **H1 on gallery overlay** · minimal breadcrumb strip above  
- **Floating offer card** overlapping gallery  
- W4 hero wrappers preserved inside stage  

### Implementation sequence (planning)

| Phase | Scope |
|-------|-------|
| W5-A | Header shell recomposition |
| W5-B | Homepage showroom entry |
| W5-C | Used PDP magazine stage |
| W5-D | Integration + 3-second HITL verification |

---

## What this decision supersedes

| Prior artifact | Status |
|----------------|--------|
| W4.1 header direction (sticky, polish-only) | **SUPERSEDED** for first impression — W5-A replaces; sticky **revert** in charter |
| W3WF-01 / atmosphere waves | **ON HOLD** — not first-impression driver |
| Incremental CSS-only expectation | **REJECTED** — blueprint requires Twig structural regroup |

---

## Operator next action

1. Review [SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) — all six sections  
2. Confirm or override blueprint architecture  
3. If confirmed → authorize Website Factory to draft **W5 implementation charter** (Twig allow-list + rollback + QA protocol)  
4. W4.1 rollback remains **operator option** on live TEST until W5-A deploys  

---

# FINAL DECISION

## Can Concept B realistically move perception from 3/10 to 7/10+ without full redesign?

# **YES**

### Explanation

**YES** — при условии реализации **архитектурных** изменений из blueprint (W5-A…C), а не очередной CSS-волны.

**Почему YES:**

1. **Каркас остаётся** — OpenCart `auto` theme, Phase 1 routes, menu, copy, W4 wrappers. Full redesign (новая CMS, новый DOM с нуля) **не требуется**.  
2. **Корневая причина 3/10 доказана** — Visual Change Failure Audit и W4.1 Visual Proof Pack: CSS/atmosphere меняют **отделку**, не **сцену**. Blueprint меняет **сцену** (band count, hero grammar, PDP geometry).  
3. **Три VERY HIGH impact changes** достаточны для смены класса восприятия за 3 секунды:  
   - Header: 3 bands → 1 shell + centered nav  
   - Homepage: carousel promo → search-first showroom entry  
   - Used PDP: 50/50 catalog → stage + floating offer  
4. **W4 — платформа, не потолок** — structural hero card уже поднял PDP до 6/10; Concept B regroup внутри stage доводит до 7/10 без выбрасывания W4 работы.  
5. **Workshop 3-second test** — Concept B **PASS** без logo; blueprint детализирует тот же structural read.  
6. **Реалистичный scope** — умеренные Twig regroups в `header.twig`, `home.twig`, `product.twig` — в рамках OCPilot charter practice (сравнимо с W4, но шире по first screen).

**Почему не автоматический YES без оговорок:**

- Достижение **7/10+** зависит от **дисциплинированной реализации** blueprint, не от частичного deploy (как W4.1: promo 8/10, homepage 3/10).  
- W5-D (integration HITL) обязателен — иначе риск повторения «PARTIAL SUCCESS».  
- **Full redesign** (Concept C luxury, новый brand category) **не нужен** и **не целевой** — B намеренно regional modern, не premium rebrand.

**Вердикт:** Concept B + W5 blueprint может поднять first impression с **3/10** до **7/10+** на том же OpenCart-каркасе — это **structural modernization**, не косметика и не полная перестройка продукта.

---

## Authorization status

| Action | Status |
|--------|--------|
| Blueprint architecture | **APPROVED** by Website Factory |
| Final YES/NO (3→7/10) | **YES** |
| Operator HITL on blueprint | **PENDING** |
| W5-A/B/C/D implementation | **NOT AUTHORIZED** |
| OCPilot writes | **NOT AUTHORIZED** |
| Commit | **NOT AUTHORIZED** |
| Push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

*SITE-001 W5 First Impression Decision v1 — design documentation only.*
