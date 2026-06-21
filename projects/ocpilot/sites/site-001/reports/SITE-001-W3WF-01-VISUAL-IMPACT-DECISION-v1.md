# SITE-001 W3WF-01 Visual Impact Decision v1

**Type:** Pre-execution decision — visual impact gate  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Checkpoint:** `site-001-phase1-stable-2026-06`  
**Wave:** **W3WF-01** — Website Factory Visual Direction Implementation (not yet executed)

**Inputs:**

- [SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md](SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md)
- [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md)
- [SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md)
- [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](SITE-001-WEBSITE-FACTORY-DECISION-v1.md)
- [SITE-001-W3ATMOSPHERE-01-DECISION-v1.md](SITE-001-W3ATMOSPHERE-01-DECISION-v1.md) — ACTIVE on TEST

---

## Decision

# **READY FOR W3WF-01 IMPLEMENTATION**

С оговоркой: решение основано на **ожидаемом визуальном impact относительно текущего TEST**, а не на полноте документации. W3WF-01 **не даст второй визуальный скачок** уровня W3ATMOSPHERE. Оно **закрывает governance gap** и **дожимает patchy-зоны** под единой спецификацией Website Factory.

---

## Rationale

### Why READY (not DESIGN TOO SUBTLE — REVISE FIRST)

| Gate | Assessment |
|------|------------|
| Направление «Graphite Salon» корректно | **PASS** — операторский язык (раскраска, тональность, дороже) совпадает с live TEST |
| Основная трансформация уже на TEST | **FACT** — W3ATMOSPHERE-01 PASS WITH NOTES; оператор уже видит ~70–80% цели |
| W3WF-01 добавляет измеримую ценность | **PASS** — Phase H legacy purge, `--wf-*` consolidation, four_blocks/new-catalog patch closure |
| Риск «косметика» | **ACKNOWLEDGED** — perceptual delta LOW–MEDIUM vs current TEST; это **finishing wave**, не redesign |
| Revise design first? | **NO** — проблема не в направлении, а в **фрагментированной реализации**; revise = structural/typography waves, которые **OUT OF SCOPE** |

### Why not DESIGN TOO SUBTLE — REVISE FIRST

- «Graphite Salon» как концепция **уже принят** Website Factory Decision v1.
- Субтильность W3WF-01 vs **текущий TEST** — ожидаема: atmosphere wave опередила authoritative spec.
- Revise **design** не увеличит impact без нарушения frozen constraints (no hero, no spacing, no structure).
- Оператору, которому мало текущего TEST, нужен **другой charter** (hierarchy/typography/structure) — не пересмотр palette.

### When operator should choose NO-GO

Оператор должен **остановить** W3WF-01 и запросить **новый design brief**, если ожидание:

1. «Сайт должен выглядеть **совсем иначе**» vs сегодняшний TEST.
2. «PDP hero и CTA должны измениться» — forbidden.
3. «Footer должен стать компактнее» — W3-C lesson, forbidden.
4. «Хочу 9/10 transformation без layout changes» — **недостижимо** в CSS-only atmosphere scope; cap ~6–7/10 уже достигнут в W3ATMOSPHERE.

---

## Expected visual impact summary

| Metric | Value |
|--------|-------|
| Perceptual delta vs **current TEST** | **LOW–MEDIUM** sitewide |
| Perceptual delta vs **Phase 1 checkpoint** | **MEDIUM–HIGH** — но этот скачок **уже случился** в W3ATMOSPHERE |
| Strongest W3WF-01 zones | Homepage blocks (four_blocks), new cars catalog, forms on interaction |
| Weakest W3WF-01 zones | Canvas, nav, PDP |
| Operator «без A/B» notice probability | **30–40%** casual · **60–70%** attentive operator on `/` and `/auto/` |
| «Это опять косметика» risk | **MEDIUM–HIGH** if expectation = second transformation |

---

## Reality check verdict

| Zone | Notice without A/B? |
|------|---------------------|
| Header | **Barely / maybe** |
| Footer | **Maybe** |
| Homepage | **Maybe (operator) / barely (casual)** |
| Catalog | **Maybe** |
| PDP | **Barely** |

**Honest aggregate:** W3WF-01 — **доводка**, не революция. Оператор, довольный текущим TEST atmosphere, может **не увидеть** разницу. Оператор, видевший patchy four_blocks или neon focus, **увидит** выравнивание.

---

## Design risk acceptance

| Risk ID | Severity | Accepted? |
|---------|----------|-----------|
| R-WF-01 Duplicate W3ATMOSPHERE with minimal delta | Medium | **YES** — value = governance + purge, not new look |
| R-WF-02 Legacy literals survive | Medium | **MITIGATED** by Phase H — operator checklist catches |
| R-WF-03 Operator expects full rebrand | Medium | **ACKNOWLEDGED** — preview sets ~3–6/10 delta vs TEST |
| R-WF-04 W3UX-C1 regression | High | **NO** — charter exclusion mandatory |
| R-WF-05 PDP scope creep | High | **NO** — brief forbidden list |

---

## Authorization matrix

| Action | Status | Owner |
|--------|--------|-------|
| W3WF-01 visual impact map | **DONE** | Website Factory / planning |
| W3WF-01 visual impact decision | **DONE** — this document | Website Factory / planning |
| Operator preview sign-off | **PENDING** | Operator |
| W3WF-01 write charter | **NOT AUTHORIZED** | OCPilot |
| W3WF-01 execution on TEST | **NOT AUTHORIZED** — pending charter + CR + backup | OCPilot |
| Production | **FORBIDDEN** | — |
| Git commit / push | **NOT AUTHORIZED** | — |

---

## Recommended operator action

1. Открыть TEST **сейчас** — зафиксировать mental baseline (W3ATMOSPHERE уже active).
2. Прочитать impact map §Reality check — согласиться с LOW–MEDIUM delta expectation.
3. Если baseline устраивает и нужна только **дожимка** — **authorize** OCPilot charter for W3WF-01.
4. Если baseline **не** устраивает — **не** запускать W3WF-01; запросить **новый design scope** (structural/hierarchy), не palette revise.

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Operator formal sign-off on W3ATMOSPHERE-01 live scroll | **PENDING** |
| Exact legacy bleed pages on live TEST without fresh probe | **SAFE UNKNOWN** — impact map based on W3ATMOSPHERE N-01 notes |
| PDP sample URLs on TEST | **SAFE UNKNOWN** — category shells suffice |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-09 | **CREATED** — Decision **READY FOR W3WF-01 IMPLEMENTATION** with LOW–MEDIUM perceptual delta caveat |

*SITE-001 W3WF-01 Visual Impact Decision v1 — documentation only; no implementation.*
