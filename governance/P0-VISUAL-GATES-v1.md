# REPORT — P0 VISUAL GATES

**Type:** Governance — P0 anti-regression gates (minimal deployment)  
**Date:** 2026-06-11  
**Status:** **Effective immediately** — human-operated; not automated enforcement  
**Source evidence:** [SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md](../projects/ocpilot/governance/SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md) · [SITE-001-LESSONS-INTEGRATION-PLAN-v1.md](SITE-001-LESSONS-INTEGRATION-PLAN-v1.md)

**Explicit scope:** Website Factory · OCPilot · Web-GPT · visual redesign workflows. **Not** a new process layer. **Not** a policy engine. **Not** runtime code.

**Website Factory canonical operator visual law:** [operator-visual-approval-law-v1.md](../projects/mars-website-factory/operator-visual-approval-law-v1.md) — P0-01 expression for Factory frontend; this doc remains cross-program P0 minimum.

---

## Purpose

Документ создан как **минимальное** внедрение пяти критических правил, выявленных в SITE-001 (Автосалон СИБКАР), без реформы MARS и без разрастания governance.

**Почему это необходимо:** В SITE-001 технический PASS (URLs 200, CSS markers, regression matrix) подменял продуктовый PASS. Pipeline авторизовал следующие волны при HITL PENDING, накапливал append-only CSS и принимал agent-estimated scores 7–8/10, пока Visual Proof Pack фиксировал homepage 3/10 и GAP 25–30/100. Эти пять правил блокируют повторение этой цепочки.

**Что документ не делает:** Не заменяет существующие governance-документы; не запускает WF-V3; не меняет SITE-001 артефакты; не создаёт новые процессы или системы. Операторы и агенты **обязаны** соблюдать правила при human-operated работе.

---

## Rule P0-01

### Technical PASS != Visual PASS

**Definition**

Два независимых вердикта на каждую волну с визуальным impact:

| Field | Meaning |
|-------|---------|
| `AUTOMATED_PASS` | yes/no — deploy hygiene: HTTP 200, markers present, byte match, regression matrix |
| `VISUAL_ACCEPT` | ACCEPT / REJECT / PENDING / WAIVED — perception outcome по target screens |

Единое поле «PASS WITH NOTES» **не** является основанием для авторизации следующей волны. `AUTOMATED_PASS = yes` при `VISUAL_ACCEPT = PENDING` означает: техника выполнена, продукт **не принят**.

**Enforcement**

- OCPilot decision reports **обязаны** содержать оба поля отдельно.
- Web-GPT authorization chain читает **только** `VISUAL_ACCEPT`.
- OPERATIONAL summaries и state **не** могут помечать волну как DONE без явного visual-статуса.
- Нарушение: авторизация следующей implementation-волны при `VISUAL_ACCEPT ≠ ACCEPT` (и без dated WAIVE) = **FAIL** governance.

**SITE-001 evidence:** F-01 — W5-A stabilization PASS WITH NOTES при criterion 5 PENDING; W5-C automated PASS при 7/7 visual HITL PENDING.

---

## Rule P0-02

### HITL Pending = Hard Stop

**Definition**

`HITL PENDING` (эквивалент `VISUAL_ACCEPT = PENDING` на закрывающей волне) — **жёсткая остановка** pipeline. Не optional human step, не deferrable indefinitely.

Допустимые выходы из PENDING:

1. Operator visual **ACCEPT** с датированной записью, или
2. Explicit **WAIVE** с ограничением scope и operator signature.

**Enforcement**

- Web-GPT: **не** авторизовать новый implementation prompt, пока предыдущая волна имеет `VISUAL_ACCEPT = PENDING`.
- OCPilot: **не** рекомендовать next wave при `VISUAL_ACCEPT = PENDING`.
- Cumulative rule: >1 волна с накопленным PENDING без escalation session → **HARD STOP** до operator review artifact.
- Нарушение: wave chaining с открытым HITL = **FAIL** governance.

**SITE-001 evidence:** F-02 — каждый decision doc: automated PASS + HITL PENDING → next charter authorized; W5-C выполнен без operator close W5-A.

---

## Rule P0-03

### Cosmetic Loop Cap

**Definition**

**Cosmetic loop** — последовательные волны одной стратегии (CSS append → cleanup → surface pass) на том же route family без изменения DOM/composition, при стагнации perception class.

**Trigger**

Два визуальных прохода **подряд** на target screen(s), и результат **ниже operator acceptance** (программный порог, по умолчанию <7/10 по Visual Proof Pack zone table или operator HITL score).

**Required action**

1. **STOP** append-only CSS на затронутом route family.
2. Обязательный **Architecture Review** или **Clean Room Review** (Website Factory + operator).
3. **Третий косметический проход запрещён** до письменного решения review: consolidation, twig restructure, или clean-room prototype charter.
4. Web-GPT **не** авторизует CSS-only «ещё один pass» на том же scope.

**SITE-001 evidence:** F-03 — 15+ visual passes W3-V through WF-V2-W4 после Proof Pack homepage 3/10; «cleanup after cleanup» без architecture pivot.

---

## Rule P0-04

### Clean Room Trigger

**Definition**

**Clean room** — изолированный prototype (отдельный twig/CSS bundle или `prototype-*` route), оцениваемый **до** merge в production theme. Противоположность append-only patches на legacy DOM.

**Trigger** (любой из):

| Trigger | Condition |
|---------|-----------|
| GAP alignment | <50/100 vs signed target concept |
| New visual class | Target perception class требует composition/DOM change, недостижимого CSS-only на текущем DOM |
| Concept conflict | Активный концепт **противоречит** текущей experimental branch (параллельные mandates без supersession) |

**Required action**

1. **STOP** append-only implementation на production TEST path.
2. **Prototype First** — authorize только design/prototype charter; не production TEST patches.
3. GAP response class обязателен: `clean-room` / `reversal` / `scope-reduction` — без READY без класса.
4. WF-V{n+1} planning **не** начинается, пока trigger active на WF-V{n}.

**SITE-001 evidence:** F-07 — GAP 25–30/100; WF-V2 patches продолжались на legacy DOM; W5 moved opposite to WF V2 target.

---

## Rule P0-05

### Agent Score Ban

**Definition**

Агенты (OCPilot, Web-GPT, Cursor) **не** оценивают perception numerically. Agent-estimated scores создавали ложное ощущение threshold met (7–8/10 в decision docs при Proof Pack 3–6/10).

**Allowed**

| Evidence type | Usage |
|---------------|-------|
| **Operator score** | Binding field: `operator score: PENDING` / `ACCEPT` / numeric с датой и screen ID |
| **Visual Proof Pack** | Zone table по шаблону W4.1: per-screen scores, before/after paths, verdict |

Агент может указать: `automated inconclusive for perception` — **без** числовой оценки.

**Forbidden**

```text
7/10
8/10
9/10
```

и эквиваленты: `agent est. 7–8/10`, `estimated visual impact 8/10`, `threshold met (agent)`, любой agent-generated perception score ≥6/10.

**Enforcement**

- Decision и execution reports: удалить/не публиковать agent scores; только operator score или Proof Pack zone table.
- Web-GPT **не** цитирует agent score как основание для authorization.
- Нарушение: decision doc с agent score используется для next-wave auth = **FAIL** governance.

**SITE-001 evidence:** F-08 — W5-C agent est. 7–8/10 vs Proof Pack homepage 3/10, header 5/10.

---

## Scope

| System | Application |
|--------|-------------|
| **Website Factory** | GAP trigger, clean-room declaration, architecture review при cosmetic loop cap |
| **OCPilot** | Dual-verdict decision reports; no agent scores; no next-wave recommendation при PENDING |
| **Web-GPT** | Authorization checklist: read `VISUAL_ACCEPT`; enforce hard stops |
| **Visual redesign workflows** | Все программы first-impression, WF-V*, W3–W5 chains с visual claims |

**Applies to:** SITE-001 future work (mandatory) · all OCPilot visual sites (recommended default until site charter says otherwise).

**Does not apply to:** Non-visual technical waves (config, SEO meta, backend) — unless wave claims visual impact.

---

## Final Decision

**Effective immediately** (2026-06-11).

Пять правил P0-01..P0-05 **обязательны** для human-operated работы в scope выше. Это **не** automated enforcement, **не** policy engine, **не** runtime gate product.

**WF-V3:** Не авторизован этим документом. Prerequisites без изменений: P0 knowledge docs, WF-V2 freeze artifact, clean-room plan, design assets in repo, operator visual review.

**Interim authority chain:**

```
P0-VISUAL-GATES-v1.md (this doc)     ← P0 gates, effective now
        ↓
operator-visual-approval-law-v1.md   ← Website Factory canonical operator visual law (2026-06-14)
        ↓
SITE-001-LESSONS-LEARNED-ANTI-REGRESSION-v1.md   ← full findings F-01..F-15
        ↓
SITE-001-LESSONS-INTEGRATION-PLAN-v1.md          ← future integration map (no auto-apply)
```

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Operator actual HITL scores (SITE-001) | **SAFE UNKNOWN** — all pending at source audit |
| Automated enforcement of P0 gates | **NOT PLANNED** — human-operated per MARS governance posture |
| WF-V3 planning report in repo | **MISSING** — Restore Registry intent only |

**SECURITY RISK:** None identified (governance documentation only).

---

*P0 Visual Gates v1 — minimal anti-regression deployment; no existing documents modified; no commit implied.*
