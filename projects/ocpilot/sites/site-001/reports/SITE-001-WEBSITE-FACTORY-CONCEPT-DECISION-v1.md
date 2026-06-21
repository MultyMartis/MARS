# SITE-001 — Website Factory Concept Decision v1

**Type:** Design direction decision — Website Factory  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Workshop input:** [SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md)

**Mode:** **DESIGN ONLY** — no implementation · no CSS · no code

---

## Decision

# **CONCEPT B — «Современный Дилер 2026» (Modern Dealer)**

Website Factory выбирает **Concept B** как единственное авторитетное визуальное направление для first impression (header · homepage first screen · used PDP first screen).

**Rejected for direction:**

| Concept | Verdict |
|---------|---------|
| **A — Региональный Про** | **REJECTED** — повторяет failure mode W3/W4.1; 3-second test **FAIL**; operator feedback «слишком мало» гарантирован |
| **C — Премиум Шоурум** | **REJECTED** — 3-second test PASS как premium, но **brand mismatch** для регионального салона пробега; риск «не мы» |

---

## Rationale

### Why Concept B

| Gate | Assessment |
|------|------------|
| **3-second test** | **PASS** — visitor reads «modern dealership», not OC template, without logo |
| **Operator mandate** | «Изменения должны быть заметны без A/B» — B delivers **+4** impact (3→7/10) |
| **Brand fit** | Сохраняет красный СИБКАР, dealer clarity, акции — не luxury masquerade |
| **Technical path** | Умеренные Twig + CSS changes на существующем `auto` theme — **реалистично** для OCPilot charter |
| **W4 asset reuse** | `w4-used-*` wrappers **re-skin** inside magazine PDP stage — не выбрасываем W4 работу |
| **Sticky header** | **Explicit NO** — B uses static scroll-away header |
| **Failure audit alignment** | Root cause = «changes too weak» — B меняет **композицию**, не atmosphere tokens |

### Why not Concept A

- Тот же силуэт (3-band header + carousel) = **тот же 3/10 perception class**  
- W4.1 Visual Proof Pack доказал: polish header **не меняет** homepage first screen для visitor  
- Operator уже отверг инкрементальный подход в Visual Change Failure Audit  
- Score 5/10 **ниже** mandate воркшопа  

### Why not Concept C

- СИБКАР — **региональный дилер пробега**, не import luxury brand  
- Убирание красного и promo с first screen = **конфликт** с Phase 1 brand identity  
- Operator risk: «красиво, но клиенты испугаются цен»  
- Higher Twig/DOM churn при слабой связи с бизнес-моделью  

---

## Authorized design direction (summary)

### Header — «Dealer shell»

- Ultra-compact contact rail + **single immersive graphite nav band**  
- Centered navigation · inset promo (not third strip)  
- **Static header — NO sticky**  
- One red primary CTA; phone/WhatsApp cluster right  

### Homepage first screen — «Showroom entry»

- Hero 85vh with **large typography** (not promo micro-text)  
- **Floating search card** overlapping hero — primary entry  
- Featured vehicles horizontal peek below fold edge  
- Cool stone canvas; dark-to-light hero gradient  

### Used PDP first screen — «Magazine PDP»

- Dark graphite **stage band**; gallery 70% edge-bleed  
- H1 on gallery overlay (white)  
- **Floating offer card** overlapping gallery  
- W4 hero grouping preserved inside stage  
- Light trust strip below stage  

---

## What this decision supersedes

| Prior artifact | Status |
|----------------|--------|
| [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) «Graphite Salon» | **SUPERSEDED** for first-impression scope — atmosphere tokens may inform future waves, not drive direction |
| [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-DECISION-v1.md) READY FOR W3WF-01 | **SUPERSEDED** — W3WF-01 remains **ON HOLD** |
| W4.1 sticky header direction | **REJECTED** — do not extend; rollback consideration remains operator choice |

---

## What stays frozen until implementation charter

| Item | Status |
|------|--------|
| Phase 1 branding, copy, URLs | **Frozen** |
| Menu items, phone, WhatsApp | **Frozen** |
| W3UX-C1 catalog density | **Preserve** |
| Footer, forms, credit, SEO | **Out of scope** |
| Production deployment | **NOT AUTHORIZED** |
| OCPilot implementation | **NOT AUTHORIZED** — awaits separate implementation charter |

---

## Implementation gate (future — not this document)

Website Factory **не** авторизует OCPilot execution в этом decision.

**Before any write:**

1. Operator sign-off on Concept B direction (this document)  
2. Separate **W5 First Impression** implementation charter — Twig allow-list + CSS scope + rollback  
3. Hard-refresh QA protocol (cache risk per audit 4.127)  
4. 3-second test verification on TEST with logo hidden  

**Estimated implementation waves (planning only):**

| Wave | Scope |
|------|-------|
| W5-A | Header shell recomposition (header.twig + CSS) |
| W5-B | Homepage hero + search card (home.twig + CSS) |
| W5-C | Used PDP magazine stage (product.twig + CSS; W4 preserve) |

---

## Expected outcomes (post-implementation — target)

| Stakeholder | Expected reaction |
|-------------|-------------------|
| **Operator** | «Сайт наконец выглядит современно — узнаём СИБКАР» |
| **Customer** | «Удобный современный автосалон» за 3 сек |
| **Visual impact** | **7/10** (from baseline 3/10) |

---

## Operator next action

1. Review [SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md) — all three concepts  
2. Confirm or override Concept B selection in this document  
3. If confirmed → authorize Website Factory to draft **W5 First Impression charter** (separate task)  
4. W4.1 rollback remains **operator option** if sticky/polish unwanted on live TEST  

---

## Authorization status

| Action | Status |
|--------|--------|
| Design direction (Concept B) | **SELECTED** by Website Factory |
| Operator HITL | **PENDING** |
| OCPilot implementation | **NOT AUTHORIZED** |
| Commit | **NOT AUTHORIZED** |
| Push | **NOT AUTHORIZED** |
| Production | **NOT AUTHORIZED** |

*SITE-001 Website Factory Concept Decision v1 — design documentation only*
