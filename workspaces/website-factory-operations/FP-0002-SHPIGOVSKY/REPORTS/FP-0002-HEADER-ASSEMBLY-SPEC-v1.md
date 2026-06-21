# FP-0002 HEADER ASSEMBLY SPEC v1

**Block ID / scope:** `FP-0002-BLK-001 + FP-0002-BLK-002` — Desktop Header (shell chrome)  
**Document type:** Assembly Spec (engineering assembly bridge — **not** Layout Spec, **not** implementation)  
**Status:** **DRAFT** — awaiting operator decision **APPROVED | REVISE**  
**Date:** 2026-06-14  
**Viewport:** Desktop **≥ 1024px** (Phase C.1 default)  
**Upstream Layout Spec:** [FP-0002-HEADER-LAYOUT-SPEC-v2.md](FP-0002-HEADER-LAYOUT-SPEC-v2.md)

**Purpose of this layer:** Закрыть разрыв между **Layout Spec** (что где лежит) и будущей **вёрсткой** (как это собирается). FP-0002 показал, что путь `Visual SSOT → Layout Spec → «агент понял» → HTML` ломается без явного слоя **сборки**.

**Authority applied:**

| Layer | Document | Role |
|-------|----------|------|
| A0 | [FP-0002-SOURCE-DISCOVERY-REPORT-v1.md](FP-0002-SOURCE-DISCOVERY-REPORT-v1.md) | SOURCE-ID register |
| A1 | [FP-0002-DESIGN-AUDIT-v1.md](FP-0002-DESIGN-AUDIT-v1.md) | Visual SSOT READ · header element inventory |
| Approval | [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md) | Operator decision matrix (D-001…D-022) |
| Blocks | [FP-0002-BLOCK-INVENTORY-v1.md](../FP-0002-BLOCK-INVENTORY-v1.md) | BLK-001 / BLK-002 scope |
| Layout Spec | [FP-0002-HEADER-LAYOUT-SPEC-v2.md](FP-0002-HEADER-LAYOUT-SPEC-v2.md) | Composition SSOT — rows · zones · groups · weight · alignment |
| Engineering | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) §8.7 | Container model · dual-row law — **not** assembly order SSOT |
| Factory law | [layout-spec-law-v1.md](../../../../projects/mars-website-factory/layout-spec-law-v1.md) | Layout Spec Gate — precedes Assembly Spec |
| Shell | [canonical-clean-shell-v1.md](../../../../projects/mars-website-factory/canonical-clean-shell-v1.md) | Pre-code empty shell |
| Visual gate | [operator-visual-approval-law-v1.md](../../../../projects/mars-website-factory/operator-visual-approval-law-v1.md) | Post-build operator review |
| Lesson | [FP-0002-layout-spec-lesson-v1.md](../../../../projects/mars-website-factory/FP-0002-layout-spec-lesson-v1.md) | SaaS-header failure provenance |

**Honesty note:** Assembly Spec описывает **логический порядок сборки** и **запреты слияния**. Он **не** заменяет Layout Spec v2 и **не** разрешает HTML/CSS/JS. Layout Spec v2 на момент создания этого документа — **DRAFT**; Assembly Spec **зависит** от operator **APPROVED** на Layout Spec v2 как обязательного upstream.

**Forbidden in this document (by charter):** HTML · SCSS · JS · DOM · классы · контейнеры как markup · grid · flex · размеры · токены · цвета · кнопки как UI · компоненты · адаптив · mobile · footer · hero.

---

## 1. Purpose

### 1.1 Что такое Assembly Spec

**Header Assembly Spec** — инженерный документ, который фиксирует **КАК ИМЕННО** одобренный Layout Spec должен быть **преобразован в будущую вёрстку**: порядок сборки, изоляция групп, запреты слияния, ловушки интерпретации.

Assembly Spec отвечает на вопрос: *«В каком логическом порядке и с какими границами агент собирает header, не переизобретая композицию?»*

### 1.2 Чем Assembly Spec **не** является

| Artifact | Что даёт | Почему не заменяет Assembly Spec |
|----------|----------|----------------------------------|
| **Design Audit (A1)** | Инвентарь элементов, блоков, источников, конфликтов | Подтверждает **наличие** phones/nav/logo — **не** порядок сборки и **не** запреты слияния |
| **Layout Spec v2** | Декомпозиция: rows · zones · groups · weight · alignment · frozen decisions | Фиксирует **что где** — **не** пошаговую инженерную сборку и **не** anti-trap checklist для агента перед кодом |
| **Operator Visual Review** | Приёмка **построенной** страницы | Работает **после** HTML — слишком поздно для предотвращения structural fantasy |
| **Production Standards v3** | Engineering tokens, container law | **Не** assembly order; **не** visual composition SSOT |
| **Block Inventory** | BLK-ID и reuse | Границы блоков — **не** intra-header assembly rules |

### 1.3 Зачем нужен отдельный слой

Доказанный FP-0002 failure path:

```text
Visual SSOT → Layout Spec → «агент понял» → HTML   ← ЛОМАЕТСЯ
```

Обязательный path после введения Assembly Spec:

```text
Visual SSOT → Layout Spec → Assembly Spec → Operator APPROVED → HTML → QA → Operator Review
```

Layout Spec без Assembly Spec оставляет агенту пространство для **инженерной интерпретации** (слияние nav+CTA, single-row collapse, SaaS re-layout) при формально «правильном» чтении зон.

---

## 2. Authority Chain

Строгая цепочка полномочий для header desktop ≥1024px:

```text
Visual SSOT (SOURCE-001 + matching PG-001…010 templates)
        ↓
Layout Spec (FP-0002-HEADER-LAYOUT-SPEC-v2 — composition decomposition)
        ↓
Assembly Spec (this document — assembly order · group isolation · failure traps)
        ↓
HTML (shell header markup — FORBIDDEN until Assembly Spec APPROVED)
        ↓
QA (technical build · structure checks)
        ↓
Operator Visual Review (live page — separate gate per operator-visual-approval-law-v1)
```

| Stage | Gate question | Who decides |
|-------|---------------|-------------|
| Visual SSOT | Есть ли одобренный визуальный источник? | Operator / A1 audit |
| Layout Spec | Верна ли декомпозиция rows/zones/groups? | Operator **APPROVED \| REVISE** on Layout Spec v2 |
| Assembly Spec | Достаточен ли порядок сборки и anti-trap rules? | Operator **APPROVED \| REVISE** on this document |
| HTML | Можно ли писать markup? | **Only after Assembly Spec APPROVED** |
| QA | Собирается ли проект? | Agent / technical QA |
| Operator Review | Совпадает ли built page с SSOT? | Operator **ACCEPT \| REVISE** |

**Rule:** Ни один downstream артеfact **не может** переопределить upstream composition truth. Production Standards **не** отменяют Visual SSOT composition. Starter patterns **не** отменяют dual-row law.

---

## 3. Assembly Order

**Definition:** Логический порядок **сборки header как единого chrome-объекта** — сверху вниз, внутри каждой строки слева направо. Это **не** CSS-порядок, **не** DOM-порядок как markup recipe — это **инженерная последовательность**, которую агент обязан соблюдать при будущей реализации.

### 3.1 Macro assembly (header stack)

| Step | Assemble | Block | Band role |
|------|----------|-------|-----------|
| **1** | Entire **Row 1 — TOP ROW** | FP-0002-BLK-001 | SECONDARY band — contact + utility meta |
| **2** | Entire **Row 2 — MAIN ROW** | FP-0002-BLK-002 | PRIMARY band — brand + IA + conversion |

**Rule:** Row 1 **полностью** собран и изолирован **до** того, как Row 2 получает содержимое MAIN ROW groups. **Запрещено** начинать Row 2, «компенсируя» незавершённую Row 1, или собирать обе строки как один undifferentiated band.

### 3.2 Row 1 assembly order (TOP ROW · BLK-001)

Строгая последовательность зон **слева направо**:

| Step | Zone | Group | Reading role |
|------|------|-------|--------------|
| **R1-1** | ZONE A | Region Group | Locale context — opens strip |
| **R1-2** | ZONE B | Hours Group | Schedule meta — supporting |
| **R1-3** | ZONE C | Utility Links Group | Secondary shortcuts |
| **R1-4** | ZONE D | Phone Group | Contact climax — closes strip right |

**Narrative intent:** where → when → secondary shortcuts → call now.

**Rule:** Каждая зона собирается **как отдельная assembly unit** внутри Row 1. **Запрещено** пропускать зону и «переносить» её содержимое в соседнюю зону для удобства.

### 3.3 Row 2 assembly order (MAIN ROW · BLK-002)

Строгая последовательность зон **слева направо**:

| Step | Zone | Group | Reading role |
|------|------|-------|--------------|
| **R2-1** | ZONE E | Logo Group | Brand anchor — opens main stage |
| **R2-2** | ZONE F | Primary Nav Group | Site IA spine — center band |
| **R2-3** | ZONE G | CTA Group | Conversion punctuation — closes main stage right |

**Narrative intent:** identity → wayfinding → callback action.

**Rule:** Logo Group **полностью** определён как brand unit **до** Primary Nav Group. CTA Group **собирается последним** в Row 2 — **изолированно**, не как продолжение nav list.

### 3.4 Cross-row assembly coupling

| Coupling | Rule |
|----------|------|
| Row 1 ↔ Row 2 | Row 2 **stacked below** Row 1 — **never merged** into single row |
| Left anchor | Region Group (R1) **visually aligns** with Logo Group (R2) left edge within shared inner width |
| Right anchor | Phone Group (R1) **visually aligns** with CTA Group (R2) right edge within shared inner width |
| Dominance | Row 2 assembly **must read dominant** over Row 1 when both complete |

### 3.5 Assembly order summary (reference strip)

```text
HEADER STACK
  STEP 1 — ROW 1 (BLK-001)
    R1-1  ZONE A  Region Group
    R1-2  ZONE B  Hours Group
    R1-3  ZONE C  Utility Links Group
    R1-4  ZONE D  Phone Group
  STEP 2 — ROW 2 (BLK-002)
    R2-1  ZONE E  Logo Group
    R2-2  ZONE F  Primary Nav Group
    R2-3  ZONE G  CTA Group
HEADER ENDS — next block is NOT header (Breadcrumbs or Page Hero)
```

---

## 4. Group Assembly

Для каждой из семи групп — роль, визуальная сила, запреты, запрет слияния.

### 4.1 Region Group (ZONE A · Row 1)

| Dimension | Rule |
|-----------|------|
| **Role** | Locale context — «где мы работаем»; **not** navigation |
| **Visual force** | **UTILITY** — lowest intentional presence in Row 1 except Hours |
| **Must not do** | Style as nav link · split labels to opposite ends of Row 1 · move to Row 2 · merge with Hours as one undifferentiated sentence · compete with Phone Group |
| **Must not merge with** | Hours Group (keep separate zones) · Phone Group · Primary Nav · Logo · CTA · Utility Links as single mega-cluster |

**Content (frozen):** «Москва,» · «Московская область» — **one paired locale cluster**.

---

### 4.2 Hours Group (ZONE B · Row 1)

| Dimension | Rule |
|-----------|------|
| **Role** | Operating schedule meta — supports contact context |
| **Visual force** | **SUPPORTING** — weakest intentional presence in entire header stack |
| **Must not do** | Match Phone Group prominence · move to RIGHT zone replacing phones · embed inside Phone Group · move to Row 2 · style as CTA or nav |
| **Must not merge with** | Phone Group · Region Group (as single typographic line) · Utility Links · any MAIN ROW group |

**Content (frozen):** Single hours cluster «пн-пт: 08:00-18:00, сб-вс 08:00-22:00» (exact string reconciliation — operator SU-06).

---

### 4.3 Utility Links Group (ZONE C · Row 1)

| Dimension | Rule |
|-----------|------|
| **Role** | Secondary IA shortcuts in top strip — **not** primary site menu |
| **Visual force** | **SECONDARY (weak)** within Row 1 — above meta, below phones, **far below** Primary Nav |
| **Must not do** | Promote to Primary Nav Group · move to Row 2 center · style equal to nav links · place after phones · demote to footnote meta |
| **Must not merge with** | Primary Nav Group · Phone Group · CTA Group · Region/Hours as undifferentiated utility blob |

**Content (frozen):** «Генотипирование» → `/uslugi/genotipirovanie/` · «Специалисты» → `/specyalisty/` — **adjacent pair**.

---

### 4.4 Phone Group (ZONE D · Row 1)

| Dimension | Rule |
|-----------|------|
| **Role** | Direct contact cluster — business phones at outer right of top strip |
| **Visual force** | **SECONDARY** — **strongest group in Row 1**; must remain readable contact objects |
| **Must not do** | Demote to utility microtext · move to Row 2 · center or left-align in Row 1 · split one number to MAIN ROW · match Logo/CTA scale · hide behind meta styling |
| **Must not merge with** | Utility Links (keep whitespace separation) · Hours · Primary Nav · CTA · Logo |

**Content (frozen):** +7 (925) 183-64-64 · +7 (995) 023-92-26 — **one contact cluster**.

---

### 4.5 Logo Group (ZONE E · Row 2)

| Dimension | Rule |
|-----------|------|
| **Role** | Brand home unit — institutional identity anchor |
| **Visual force** | **PRIMARY** — co-equal with Primary Nav; **visual brand object**, not decoration |
| **Must not do** | Center in MAIN ROW (SaaS pattern) · detach mark from text stack · treat as favicon placeholder · merge with nav list · move any part to Row 1 |
| **Must not merge with** | Primary Nav Group · CTA Group · Region Group · any TOP ROW group |

**Content (frozen):** Mark + «Центр профилактики и лечения зависимостей» + «(Шпиговский дом)» — **one brand unit** linking to `/`. Tagline «Лечение и профилактика» — placement SU-03 (does not change zone).

---

### 4.6 Primary Nav Group (ZONE F · Row 2)

| Dimension | Rule |
|-----------|------|
| **Role** | Primary site wayfinding — horizontal IA spine |
| **Visual force** | **PRIMARY** — five equal-weight text links |
| **Must not do** | Add 6th item «Заказать звонок» · absorb Utility Links from Row 1 · include phones/hours/region · flush entire nav to far right next to CTA only · break into multiple disconnected clusters |
| **Must not merge with** | CTA Group · Utility Links Group · Phone Group · Logo (as single flex blob) · top-bar meta |

**Content (frozen, exact order):** Услуги · О центре · Отзывы · Статьи · Контакты — **one list, five items only**.

---

### 4.7 CTA Group (ZONE G · Row 2)

| Dimension | Rule |
|-----------|------|
| **Role** | Isolated conversion control — callback entry point |
| **Visual force** | **PRIMARY** — strongest **action accent** in MAIN ROW at right edge |
| **Must not do** | Render as 6th nav text link · move to Row 1 · place left of logo · merge into nav list · demote to plain link · substitute generic engineering widget for design-intent control |
| **Must not merge with** | Primary Nav Group · Utility Links · Phone Group · any TOP ROW group |

**Content (frozen):** Single control «Заказать звонок» — **standalone**, not part of nav enumeration. Behavior (modal/tel) — SU-12; **does not change zone**.

---

## 5. Zone Assembly Rules

Для каждой зоны A–G: допустимое содержимое, запреты, anti-migration.

### ZONE A — Utility Left (Row 1)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| Region Group only: «Москва,» · «Московская область» | Hours · phones · utility links · nav · CTA · logo · search · breadcrumbs | Region labels **to** ZONE D, Row 2, or footer |

### ZONE B — Utility Center-Left (Row 1)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| Hours Group only: schedule string | Phones · utility links · nav · region labels · CTA | Hours **to** ZONE D (replacing phones) or Row 2 |

### ZONE C — Utility Right-Inner (Row 1)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| Utility Links Group: «Генотипирование» · «Специалисты» | Phones · primary nav items · CTA · hours · region | Either link **to** ZONE F Primary Nav or Row 2 |

### ZONE D — Utility Right-Outer (Row 1)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| Phone Group: two tel numbers as one cluster | Nav · CTA · logo · utility links mixed without separation | Phones **to** Row 2 · one phone split to MAIN ROW |

### ZONE E — Brand Anchor (Row 2)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| Logo Group: mark + brand title + subtitle stack | Nav links · CTA · phones · top-bar content | Brand parts **to** nav center · mark **to** Row 1 |

### ZONE F — Primary IA (Row 2)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| Primary Nav Group: exactly five named links | CTA · utility links · phones · hours · logo text · 6th nav item | Nav items **to** Row 1 · «Генотипирование»/«Специалисты» **into** this zone |

### ZONE G — Conversion (Row 2)

| Allowed inside | Forbidden inside | Must not migrate |
|----------------|------------------|------------------|
| CTA Group: «Заказать звонок» single control | Nav list items · utility links · phones | CTA **to** Row 1 · CTA **as** inline nav item in ZONE F |

---

## 6. Composition Rules

**Normative separation laws** — агент **не может** «оптимизировать» header, нарушая эти правила.

| Rule ID | Law | Meaning |
|---------|-----|---------|
| **CR-01** | **Logo ≠ Nav** | Logo Group (ZONE E) and Primary Nav Group (ZONE F) are **distinct assembly units**. Brand home is **not** a nav item; nav list **does not include** logo text stack. |
| **CR-02** | **Nav ≠ CTA** | Primary Nav Group (ZONE F) and CTA Group (ZONE G) are **distinct assembly units**. «Заказать звонок» is **not** the 6th nav link. |
| **CR-03** | **Phones ≠ Utility** | Phone Group (ZONE D) and Utility Links Group (ZONE C) are **distinct**. Phones are contact objects; utility links are secondary shortcuts — **different tiers, different zones**. |
| **CR-04** | **Utility ≠ Primary Nav** | Utility Links (ZONE C, Row 1) and Primary Nav (ZONE F, Row 2) are **different IA layers**. «Генотипирование» / «Специалисты» **never** join the five-item primary list. |
| **CR-05** | **Hero ≠ Header** | Page Hero (BLK-007) begins **immediately below** header bottom on Home. Hero content **never** assembled inside header stack. |
| **CR-06** | **Breadcrumbs ≠ Header** | Breadcrumbs (BLK-005) begin **immediately below** header on inner pages. Breadcrumb trail **never** inside BLK-001 or BLK-002. |
| **CR-07** | **CTA ≠ 6th nav item** | CTA Group is **conversion control**, not navigation enumeration. It **must not** appear in Primary Nav Group count or styling tier as a link sibling. |

**Corollaries:**

- Row 1 content **never** appears in Row 2 zones (FD-02 · FD-03).
- Row 2 content **never** appears in Row 1 zones.
- Search, hamburger (desktop ≥1024), messengers — **not in header** unless future SSOT + Layout Spec REVISE.
- Footer (BLK-003), Mobile Sticky CTA Bar (BLK-004), in-page anchors (BLK-006) — **outside** header assembly scope.

---

## 7. Failure Traps

Documented FP-0002 and Factory failure modes — что это, почему возникает, как ловить **до** HTML.

### FT-01 — HEADER BLOB

| Field | Content |
|-------|---------|
| **What** | Все группы header слиты в **один** undifferentiated chrome object без row/zone boundaries |
| **Why** | Agent optimizes for «simplest header partial»; starter patterns encourage monolithic `<header>` content |
| **How to catch** | Verify Assembly Order §3: two distinct row assembly steps; seven groups remain separable; ask «can I name ZONE A–G before coding?» — if no → **STOP** |

### FT-02 — SAAS HEADER

| Field | Content |
|-------|---------|
| **What** | Centered logo · nav+CTA clustered right · single dominant row — типичный app header |
| **Why** | Agent defaults to common SaaS template; Layout Spec read without alignment/weight enforcement |
| **How to catch** | Check CR-01 (logo left anchor) · Row 2 order Logo→Nav→CTA · dual-row macro step 1+2 · compare mentally to SOURCE-001 strip, not to gulp-starter |

### FT-03 — CENTERED LOGO REBUILD

| Field | Content |
|-------|---------|
| **What** | Logo Group moved to horizontal center of MAIN ROW; nav split to edges |
| **Why** | Misread «balance» as centered brand; triumph/starter residue |
| **How to catch** | ZONE E = LEFT only · Logo Group §4.5 «must not center» · Alignment Model in Layout Spec v2 §7.4 forbidden moves |

### FT-04 — UTILITY NAV SWAP

| Field | Content |
|-------|---------|
| **What** | «Генотипирование» / «Специалисты» promoted to Primary Nav; or primary nav items demoted to top bar |
| **Why** | Both are «links» — agent collapses IA layers |
| **How to catch** | CR-04 · Zone F allowed content = five items only · Zone C must stay Row 1 · §9.4 IS / IS NOT nav table in Layout Spec v2 |

### FT-05 — PHONE DEMOTION

| Field | Content |
|-------|---------|
| **What** | Phone numbers styled/read as smallest meta caption in top strip |
| **Why** | Agent treats all Row 1 as «utility bar» with uniform weak styling |
| **How to catch** | Phone Group = SECONDARY, strongest in Row 1 · CR-03 · Layout Spec LR-001 · ask «are phones the contact climax of Row 1?» |

### FT-06 — CTA DEMOTION

| Field | Content |
|-------|---------|
| **What** | «Заказать звонок» becomes plain text link inside nav or weak top-bar link |
| **Why** | Agent avoids «button» until design tokens ready; merges action with nav for simplicity |
| **How to catch** | CR-02 · CR-07 · CTA Group §4.7 isolated ZONE G · must remain PRIMARY action accent |

### FT-07 — SINGLE ROW COLLAPSE

| Field | Content |
|-------|---------|
| **What** | BLK-001 and BLK-002 merged into one horizontal band `[logo][meta][nav][CTA]` |
| **Why** | Single-row flex is easier to implement; FD-01 ignored |
| **How to catch** | Macro assembly Step 1 then Step 2 · FD-01 frozen · FT-01 blob variant · Block Inventory separates BLK-001 vs BLK-002 |

### FT-08 — VISUAL INTERPRETATION

| Field | Content |
|-------|---------|
| **What** | Agent implements from memory/chat summary without filed Layout Spec + Assembly Spec |
| **Why** | Skipped documentation gates; «I understood the PDF» |
| **How to catch** | Require citation: Layout Spec REF + Assembly Spec REF in implementation REPORT; layout-spec-law-v1 failure class |

### FT-09 — TRIUMPH REUSE

| Field | Content |
|-------|---------|
| **What** | Header patterns copied from unrelated project (Triumph Manipulator landing or other workspace) |
| **Why** | Prior workspace muscle memory; similar gulp-starter architecture |
| **How to catch** | Scope lock: SOURCE-001 composition only · CR rules · no cross-project partial reuse without explicit charter |

### FT-10 — STARTER RESIDUE

| Field | Content |
|-------|---------|
| **What** | Demo nav, placeholder logo, generic CTA, ui-demo chrome bleed into header |
| **Why** | Workspace not at Clean Shell; foundation demo invited wrong patterns |
| **How to catch** | canonical-clean-shell-v1: HEADER NOT STARTED until gates pass · no inherited starter header markup · FP-0002-clean-shell-lesson |

**Pre-code checklist (agent self-test):**

1. Two rows assembled in order?  
2. Seven groups isolated?  
3. All CR-01…CR-07 pass?  
4. No FT-01…FT-10 trigger?  
5. Assembly Spec APPROVED recorded?

If any **NO** → **STOP** — no HTML.

---

## 8. Assembly Acceptance

Assembly Spec считается **достаточным** для unlock HTML/CSS header scope **только когда** все условия ниже **YES**:

| # | Criterion | Status (this filing) |
|---|-----------|------------------------|
| A-01 | Layout Spec v2 operator **APPROVED** (upstream gate) | **PENDING** — Layout Spec v2 still DRAFT |
| A-02 | Assembly Order §3 documented for all 7 groups across 2 rows | **YES** |
| A-03 | Group Assembly §4 complete for all 7 groups | **YES** |
| A-04 | Zone Assembly Rules §5 complete for ZONE A–G | **YES** |
| A-05 | Composition Rules §6 CR-01…CR-07 explicit | **YES** |
| A-06 | Failure Traps §7 minimum set documented with catch methods | **YES** |
| A-07 | Authority chain §2 cites Visual SSOT → Layout → Assembly → HTML | **YES** |
| A-08 | No HTML/SCSS/JS/DOM in this document | **YES** |
| A-09 | Operator decision **APPROVED** on **this** Assembly Spec | **NO** — awaiting gate |
| A-10 | SAFE UNKNOWN from Layout Spec v2 §14 acknowledged — agent must not invent structure to fill | **YES** — gaps remain (SU-01…SU-18); assembly zones fixed, micro-layout open |

**Verdict:** Document **filed and structurally complete** — operator gate **not passed**. Assembly acceptance for implementation = **NO** until A-01 **and** A-09 are **YES**.

---

## 9. Implementation Readiness

**Question:** Может ли агент после этого документа создавать HTML?

**Answer: NO**

| Gate | Verdict | Notes |
|------|---------|-------|
| Assembly Spec filed | **YES** | This document v1 |
| Layout Spec v2 APPROVED | **NO** | Upstream composition gate — **STOP** |
| Assembly Spec operator APPROVED | **NO** | This document — **STOP** |
| HTML/CSS permitted | **NO** | Forbidden until **both** Layout Spec v2 **APPROVED** **and** Assembly Spec v1 **APPROVED** |
| Operator Visual Review | **N/A** | Runs after implementation — separate gate |

**Unlock sequence for future implementation:**

```text
1. Operator APPROVED — FP-0002-HEADER-LAYOUT-SPEC-v2.md
2. Operator APPROVED — FP-0002-HEADER-ASSEMBLY-SPEC-v1.md (this document)
3. THEN — Header HTML/CSS allowed (cite both REFs in REPORT)
4. THEN — Build → QA → Operator Visual Review
```

**Post-approval implementation must cite:**

```text
LAYOUT SPEC REF — FP-0002-HEADER-LAYOUT-SPEC-v2.md — APPROVED <date>
ASSEMBLY SPEC REF — FP-0002-HEADER-ASSEMBLY-SPEC-v1.md — APPROVED <date>
ASSEMBLY GATE — PASS (APPROVED)
```

---

## 10. Operator Decision

Проверьте Assembly Spec против [FP-0002-HEADER-LAYOUT-SPEC-v2.md](FP-0002-HEADER-LAYOUT-SPEC-v2.md) и Visual SSOT (SOURCE-001 + matching desktop templates PG-001…010).

**Требуется решение по этому документу:**

| Decision | Effect |
|----------|--------|
| **APPROVED** | Assembly layer accepted — **still requires** Layout Spec v2 APPROVED before HTML |
| **REVISE** | Fix Assembly Spec only — **do not** compensate with HTML patches |

```text
OPERATOR DECISION — FP-0002-HEADER-ASSEMBLY-SPEC-v1:

[ ] APPROVED
[ ] REVISE
```

**Верстка запрещена до APPROVED на Assembly Spec и до APPROVED на Layout Spec v2.**

---

## Document control

| Field | Value |
|-------|-------|
| Version | **v1** |
| Status | **DRAFT** |
| Related upstream | FP-0002-HEADER-LAYOUT-SPEC-v2.md |
| Related blocks | FP-0002-BLK-001 · FP-0002-BLK-002 |
| Commit / push | Not performed |
| Workspace touched | **NO** |

---

**Operator gate request:**

Header Assembly Spec v1 готов как мост **Layout Spec → будущая вёрстка** для desktop header (BLK-001 + BLK-002, ≥1024px).  
Проверьте порядок сборки, изоляцию групп, composition rules и failure traps против Layout Spec v2 и Visual SSOT.  
Требуется решение: **APPROVED** или **REVISE**.  
HTML/CSS/JS **запрещены** до APPROVED на Layout Spec v2 **и** на этом документе.
