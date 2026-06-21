# REPORT — FP-0002 HERO ASSEMBLY SPEC v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-15  
**Phase:** HERO ASSEMBLY SPEC (engineering assembly bridge — **not** Layout Spec, **not** Visual Scale, **not** build)  
**Visual SSOT:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg`  
**Upstream Layout Spec:** [FP-0002-HERO-LAYOUT-SPEC-v1.md](FP-0002-HERO-LAYOUT-SPEC-v1.md)

**Purpose of this layer:** Закрыть разрыв между **Hero Layout Spec** (что где лежит) и будущей **вёрсткой** (как это собирается). Фиксирует порядок сборки, изоляцию групп, CTA relation, composition rules и failure traps **до** HTML.

**Authority chain applied (strict):**

| Priority | Document | Role |
|----------|----------|------|
| A0 | `HOME-PAGE-FULL-MOCKUP.jpg` | Visual SSOT |
| A1 | [FP-0002-HERO-LAYOUT-SPEC-v1.md](FP-0002-HERO-LAYOUT-SPEC-v1.md) | Composition SSOT — **supreme on conflict** |
| A2 | [FP-0002-HERO-GROUP-FORENSIC-v1.md](FP-0002-HERO-GROUP-FORENSIC-v1.md) | Group decomposition · Content Lock v2 |
| A3 | [FP-0002-HERO-DISCOVERY-v1.md](FP-0002-HERO-DISCOVERY-v1.md) | **Superseded** on grouping · copy · CTA relation |

**Rule:** LAYOUT SPEC > FORENSIC > DISCOVERY.

**Constraints respected:** HTML / SCSS / JS / Hero build / Hero Visual Scale Spec — **NOT created**. `desktop-shell.html` · `desktop-ui-demo.html` · header · footer · `dist` — **NOT touched**.

**Forbidden in this document (by charter):** HTML · SCSS · JS · DOM classes · grid · flex · px · tokens · colors · responsive breakpoints · build commands.

---

## 1. Assembly Order

**Definition:** Логический порядок **сборки Hero** — от **самого внешнего слоя к самому внутреннему**. Это **не** CSS z-index recipe и **не** markup recipe — это **инженерная последовательность**, которую агент обязан соблюдать при будущей реализации.

### 1.1 Macro assembly (Hero stack — outermost → innermost)

| Step | Assemble | GROUP-ID / layer | Role |
|------|----------|------------------|------|
| **S-01** | **Hero root** | Section band | Bounds · overflow · START/END of Hero; **не** header · **не** intro section |
| **S-02** | **Background layer** | GROUP-01 + GROUP-01C | Full-bleed photo + corner clip/mask по периметру Hero |
| **S-03** | **Background image overlay** | GROUP-01B | Global wash / desaturation поверх всего фонового фото |
| **S-04** | **Content wrapper** | Structural (не GROUP-ID) | Центрирование GROUP-02 + GROUP-05 как единой вертикальной композиции |
| **S-05** | **Overlay card container** | GROUP-02 | Aggregated shell: surface + inner content stack only |
| **S-06** | **Card surface** | GROUP-02A | Frosted glass panel — semi-transparent surface + backdrop blur + radius |
| **S-07** | **Card content stack** | GROUP-02B | Vertical layout entity внутри surface — **без** отдельной визуальной «коробки» |
| **S-08** | **Label** | GROUP-03 | Top of content stack — uppercase sans-serif line |
| **S-09** | **Main heading** | GROUP-04 | Middle of content stack — display serif title |
| **S-10** | **CTA primary** | GROUP-05 | **Sibling** of GROUP-02 — **после** завершения card assembly |

### 1.2 Assembly coupling rules

| Coupling | Rule |
|----------|------|
| Background ↔ overlay content | Background (S-02–S-03) **полностью** определён **до** content wrapper (S-04) |
| Card ↔ CTA | GROUP-02 (S-05–S-09) **полностью** собран **до** GROUP-05 (S-10) |
| Card surface ↔ content stack | GROUP-02A (S-06) **до** GROUP-02B (S-07) |
| Label ↔ heading | GROUP-03 (S-08) **до** GROUP-04 (S-09) внутри stack |
| Content wrapper | **Mandatory** parent assembly step для card + CTA — **не** пропускать S-04 |

### 1.3 Visual layer stack (composition reference — not CSS)

| Layer | Step | Content |
|-------|------|---------|
| L0 | S-01 | Hero root — section band, bounds, overflow |
| L1 | S-02 | GROUP-01 background image + GROUP-01C corner mask |
| L2 | S-03 | GROUP-01B image overlay (wash) |
| L3 | S-04 | Content wrapper — centers card + CTA stack |
| L4 | S-06 | GROUP-02A card surface |
| L5 | S-07–S-09 | GROUP-02B → GROUP-03 → GROUP-04 |
| L6 | S-10 | GROUP-05 CTA (under content wrapper; **sibling** of GROUP-02) |

### 1.4 Assembly order summary (reference strip)

```text
HERO STACK (outermost → innermost)
  S-01  Hero root (section band)
  S-02  GROUP-01 Background Media + GROUP-01C Corner Mask
  S-03  GROUP-01B Background Image Overlay (wash)
  S-04  Content Wrapper (structural — centers overlay stack)
  S-05  GROUP-02 Overlay Card Container
    S-06  GROUP-02A Card Surface (frosted panel)
    S-07  GROUP-02B Card Content Stack
      S-08  GROUP-03 Label
      S-09  GROUP-04 Main Heading
  S-10  GROUP-05 CTA Primary (sibling of GROUP-02 — NOT inside card)
HERO ENDS — next block is NOT Hero (white intro section)
```

**Порядок чтения (visual flow):** фон full bleed → центральная карточка (label → heading) → CTA под карточкой на фоне фото.

---

## 2. Group Assembly

Для каждого GROUP-ID — роль, родитель, дочерние элементы, порядок появления в assembly chain.

### 2.1 GROUP-01 — Hero Background Media

| Dimension | Rule |
|-----------|------|
| **Role** | Full-bleed photographic background — здание клиники (белая башня, кирпич, деревья, небо, газон) |
| **Parent** | Hero root (S-01) |
| **Children** | GROUP-01B (overlay wash) · GROUP-01C (corner mask) — sub-layers фона |
| **Assembly step** | S-02 (together with GROUP-01C clip) |
| **Must not do** | Treat as inline `<img>` content block inside card · crop to card width · move behind header |

**Content (frozen):** Visual asset — filename / crop / focal point: **UNKNOWN** (Layout Spec U-05).

---

### 2.2 GROUP-01B — Hero Background Image Overlay

| Dimension | Rule |
|-----------|------|
| **Role** | Global darkening / desaturation wash поверх **всего** фонового фото |
| **Parent** | GROUP-01 (background layer) |
| **Children** | — (atomic overlay sub-layer) |
| **Assembly step** | S-03 — **after** GROUP-01 image + GROUP-01C; **before** content wrapper |
| **Must not do** | Apply only behind card · duplicate as separate filter on card · skip wash and rely on card opacity alone |

**Implementation note (assembly only):** separate div vs pseudo-element — **UNKNOWN** (Layout Spec U-09); assembly tree allows both.

---

### 2.3 GROUP-01C — Hero Container Corner Mask

| Dimension | Rule |
|-----------|------|
| **Role** | Rounded corners hero-контейнера — clip/mask фото по периметру Hero bounds |
| **Parent** | GROUP-01 (background layer) |
| **Children** | — (clip property on background assembly) |
| **Assembly step** | S-02 — **with** GROUP-01 image |
| **Must not do** | Apply radius only to card · clip content wrapper · round entire page section below Hero |

---

### 2.4 Content Wrapper (structural — not GROUP-ID)

| Dimension | Rule |
|-----------|------|
| **Role** | Позиционирование и центрирование GROUP-02 + GROUP-05 как **единой вертикальной композиции** поверх background |
| **Parent** | Hero root (S-01) |
| **Children** | GROUP-02 (overlay card) · GROUP-05 (CTA) — **siblings** |
| **Assembly step** | S-04 — **before** card and CTA children |
| **Must not do** | Skip and position card/CTA independently · nest inside GROUP-02 · merge with background layer |

**Authority:** Layout Spec FD-07 · Forensic Frontend Developer Test — **mandatory**; absent in Discovery v1 tree.

---

### 2.5 GROUP-02 — Overlay Card Container

| Dimension | Rule |
|-----------|------|
| **Role** | Aggregated shell — объединяет card surface + inner content stack |
| **Parent** | Content wrapper |
| **Children** | GROUP-02A (card surface) · GROUP-02B (content stack) — **NOT** GROUP-05 |
| **Assembly step** | S-05 |
| **Must not do** | Include CTA inside container · treat as single text blob without 02A/02B split · merge with background |

**Verdict (Forensic):** **AGGREGATED** — contains GROUP-02A + GROUP-02B only.

---

### 2.6 GROUP-02A — Card Surface

| Dimension | Rule |
|-----------|------|
| **Role** | Frosted glass panel — semi-transparent surface + backdrop blur + border-radius |
| **Parent** | GROUP-02 |
| **Children** | GROUP-02B (content stack) — layout/content inside surface |
| **Assembly step** | S-06 — **before** GROUP-02B |
| **Must not do** | Add visible stroke/border/frame · opaque solid panel without blur · extend surface below heading to wrap CTA · readable shadow mass as primary separation |

**Visual:** Separation через opacity + blur — **not** decorative border (Forensic §2).

---

### 2.7 GROUP-02B — Card Content Stack

| Dimension | Rule |
|-----------|------|
| **Role** | Vertical stack label → heading **внутри** card surface; layout entity без отдельной визуальной «коробки» |
| **Parent** | GROUP-02A (visually inside surface) |
| **Children** | GROUP-03 (label) · GROUP-04 (heading) — **only** |
| **Assembly step** | S-07 — **after** GROUP-02A |
| **Must not do** | Include GROUP-05 CTA · add subtitle/description paragraph · add icon/badge row |

**Verdict (Forensic):** **AGGREGATED (layout)** — contains GROUP-03 + GROUP-04.

---

### 2.8 GROUP-03 — Label

| Dimension | Rule |
|-----------|------|
| **Role** | Uppercase sans-serif label — opens content stack |
| **Parent** | GROUP-02B |
| **Children** | — (atomic text node) |
| **Assembly step** | S-08 — **first** inside content stack |
| **Must not do** | Place outside card · below heading · merge with heading as one line · use Discovery v1 copy |

**Content (frozen — Content Lock v2):** `Центр профилактики и лечения зависимостей`  
**Rejected:** Discovery v1 `ЧАСТНАЯ ПСИХИАТРИЧЕСКАЯ КЛИНИКА` (Layout Spec FD-15).

---

### 2.9 GROUP-04 — Main Heading

| Dimension | Rule |
|-----------|------|
| **Role** | Display serif main title — visual climax of card |
| **Parent** | GROUP-02B |
| **Children** | — (atomic text node) |
| **Assembly step** | S-09 — **after** GROUP-03 |
| **Must not do** | Place outside card · add description below inside card · use Discovery v1 copy |

**Content (frozen — Content Lock v2):** `Шпиговский дом`  
**Rejected:** Discovery v1 `КОРСАКОВ` (Layout Spec FD-15).

---

### 2.10 GROUP-05 — CTA Primary

| Dimension | Rule |
|-----------|------|
| **Role** | Primary conversion control — red pill button on background photo |
| **Parent** | Content wrapper — **NOT** GROUP-02 / GROUP-02A / GROUP-02B |
| **Children** | — (atomic button control) |
| **Assembly step** | S-10 — **after** GROUP-02 assembly complete |
| **Must not do** | Nest inside card surface · stack as third row inside GROUP-02B · align to card left edge only · use header CTA copy |

**Content (frozen — Content Lock v2):** `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ`  
**Rejected:** Discovery v1 `ЗАПИСАТЬСЯ НА ПРИЕМ` (Layout Spec FD-15).

**Layer:** Sits on background photo (GROUP-01), **not** on frosted panel (Layout Spec §3 E-03).

---

### 2.11 Full assembly chain (parent chain per group)

```text
Hero root (S-01)
├─ GROUP-01 Background (+ GROUP-01C)     [S-02]
│  └─ GROUP-01B Overlay                  [S-03]
└─ Content Wrapper                       [S-04]
   ├─ GROUP-02 Overlay Card              [S-05]
   │  ├─ GROUP-02A Card Surface          [S-06]
   │  └─ GROUP-02B Content Stack          [S-07]
   │     ├─ GROUP-03 Label                [S-08]
   │     └─ GROUP-04 Main Heading         [S-09]
   └─ GROUP-05 CTA Primary               [S-10]  ← sibling of GROUP-02
```

---

## 3. Relation Audit

### 3.1 GROUP-05 CTA — mandatory relation question

**Вопрос:** GROUP-05 CTA — Child? Sibling? Independent?

| Option | Verdict |
|--------|---------|
| **Child of card (GROUP-02 / GROUP-02A)** | **NO** |
| **Sibling of card (GROUP-02)** | **YES** |
| **Independent (no shared parent with card)** | **NO** |

### 3.2 Answer

**GROUP-05 CTA = SIBLING OF CARD (GROUP-02)**

**Shared parent:** Content wrapper (structural layer S-04).

GROUP-05 is **not** independent — it shares content wrapper with GROUP-02 and participates in the **center-stack composition**. It is **not** a child of GROUP-02, GROUP-02A, or GROUP-02B.

### 3.3 Evidence summary (authority chain)

| # | Source | Finding |
|---|--------|---------|
| E-01 | Layout Spec §3 E-01 | Card surface **ends** below heading — does not wrap button |
| E-02 | Layout Spec §3 E-02 | CTA **below** GROUP-02 with visible vertical gap |
| E-03 | Layout Spec §3 E-03 | Button on background photo, not frosted panel |
| E-04 | Layout Spec §3 E-04 | Label · heading · CTA share **one center line** |
| E-05 | Layout Spec FD-03 | CTA relation = **B — sibling of card** — frozen |
| E-06 | Forensic v1 §1 | CTA — отдельный визуальный блок, sibling карточки |
| E-07 | Discovery v1 | CTA inside overlay — **rejected** |

### 3.4 DOM implication (assembly-only — not HTML)

GROUP-02 and GROUP-05 are **siblings** under content wrapper. GROUP-05 is **not** a descendant of GROUP-02.

---

## 4. Composition Rules

Нормативные separation laws — агент **не может** «оптимизировать» Hero, нарушая эти правила.

| Rule ID | Law | Meaning |
|---------|-----|---------|
| **CR-01** | **CTA outside card** | GROUP-05 **не** child GROUP-02 / GROUP-02A / GROUP-02B. CTA assembly step S-10 **after** card; visually below card surface with gap. |
| **CR-02** | **Heading inside card** | GROUP-04 **only** inside GROUP-02B → GROUP-02A. Heading **never** on background layer outside card. |
| **CR-03** | **Label inside card** | GROUP-03 **only** inside GROUP-02B → GROUP-02A. Label **never** outside card or below heading. |
| **CR-04** | **Center line** | GROUP-03 · GROUP-04 · GROUP-05 share **one vertical center axis** under content wrapper. |
| **CR-05** | **Hero hierarchy** | L0 background full bleed → L3–L5 center overlay stack → L6 CTA on photo. Background **dominates** area; text stack **dominates** reading order. |
| **CR-06** | **GROUP-02 boundary** | GROUP-02 aggregates **only** GROUP-02A + GROUP-02B — **not** GROUP-05. |
| **CR-07** | **GROUP-02B boundary** | GROUP-02B contains **only** GROUP-03 + GROUP-04 — vertical stack label → heading. **No** CTA row inside stack. |
| **CR-08** | **No inner description** | **No** subtitle / description paragraph between heading and card bottom (Layout Spec FD-11). |
| **CR-09** | **Card surface law** | GROUP-02A = frosted glass (semi-transparent + blur + radius). **No** visible decorative border/frame. **No** readable shadow mass as primary separation. |
| **CR-10** | **Hero ≠ Header** | Hero START = bottom of header nav-row. Hero content **never** assembled inside header stack. |
| **CR-11** | **Hero ≠ Intro section** | Hero END = top of white section «Шпиговский дом — восстановление с уважением к личности». Intro/features block **never** inside Hero assembly. |
| **CR-12** | **Background sub-layers** | GROUP-01B (wash) + GROUP-01C (corner mask) are **part of background assembly** (S-02–S-03), not card assembly. |
| **CR-13** | **Content wrapper mandatory** | Content wrapper (S-04) is **required** parent of GROUP-02 + GROUP-05 for center-stack positioning — **not** optional. |
| **CR-14** | **Card surface ≠ content stack** | GROUP-02A (visual shell) and GROUP-02B (layout stack) remain **distinct assembly units** inside GROUP-02. |
| **CR-15** | **Content Lock v2 only** | GROUP-03 / GROUP-04 / GROUP-05 copy from JPG Content Lock v2 — Discovery v1 strings **forbidden**. |
| **CR-16** | **Absent elements** | Secondary CTA · form · badges/icons row · breadcrumb · logo inside overlay — **not** assembled in Hero. |

**Corollaries:**

- Discovery v1 tree (CTA inside overlay card) — **invalid** assembly model.
- GROUP-01 background assembly **complete** before overlay content assembly begins.
- Mobile/tablet Hero assembly — **UNKNOWN** (Layout Spec U-06); desktop JPG authority only.

---

## 5. Failure Traps

Документированные failure modes — что это, почему возникает, как ловить **до** HTML.

### FT-01 — CTA INSIDE CARD

| Field | Content |
|-------|---------|
| **What** | GROUP-05 placed inside GROUP-02A surface or as third row in GROUP-02B stack |
| **Why** | Discovery v1 tree residue; vertical «card with everything centered» mental model |
| **How to catch** | CR-01 · Relation Audit §3 · ask «does frosted panel end below heading?» — if CTA inside panel → **STOP** |

### FT-02 — DISCOVERY V1 CONTENT RETURN

| Field | Content |
|-------|---------|
| **What** | Copy reverts to `ЧАСТНАЯ ПСИХИАТРИЧЕСКАЯ КЛИНИКА` / `КОРСАКОВ` / `ЗАПИСАТЬСЯ НА ПРИЕМ` |
| **Why** | Discovery v1 filed first; agent reads older doc or chat summary |
| **How to catch** | CR-15 · Content Lock v2 table §2.8–2.10 · cite Layout Spec FD-14 / FD-15 |

### FT-03 — GROUP COLLAPSE (HERO BLOB)

| Field | Content |
|-------|---------|
| **What** | All Hero groups merged into one undifferentiated overlay object without background / card / CTA boundaries |
| **Why** | Agent optimizes for «simplest hero partial»; starter demo patterns |
| **How to catch** | Assembly Order §1.4 — can you name S-01…S-10 and nine GROUP-IDs before coding? If no → **STOP** |

### FT-04 — BACKGROUND AS CONTENT

| Field | Content |
|-------|---------|
| **What** | Background photo treated as inline content `<img>` inside card or content wrapper instead of full-bleed background layer |
| **Why** | Default img-first markup habit; confusion with card media patterns |
| **How to catch** | CR-12 · GROUP-01 assembly at S-02 **before** S-04 · background covers full Hero band |

### FT-05 — CARD SURFACE LOSS

| Field | Content |
|-------|---------|
| **What** | GROUP-02A becomes opaque solid box, loses blur, loses radius, or gains heavy border/shadow as primary separation |
| **Why** | Token not ready; agent uses plain white `background` shortcut |
| **How to catch** | CR-09 · Forensic CARD SURFACE / CARD BACKDROP present · ask «is this frosted glass, not a bordered card component?» |

### FT-06 — SINGLE STACK INSIDE CARD (CTA ROW)

| Field | Content |
|-------|---------|
| **What** | Three-row vertical stack inside overlay: label → heading → **CTA** — Discovery v1 geometry |
| **Why** | Discovery v1 «ROW COUNT inside overlay = 3» residue |
| **How to catch** | CR-07 · GROUP-02B children = **two only** · FT-01 variant |

### FT-07 — CONTENT WRAPPER SKIP

| Field | Content |
|-------|---------|
| **What** | Card and CTA positioned as independent absolute elements without shared center-stack parent |
| **Why** | Agent skips «unnecessary wrapper div»; positions card and button separately |
| **How to catch** | CR-13 · CR-04 center line breaks · Forensic tree requires content wrapper |

### FT-08 — CENTER LINE BREAK

| Field | Content |
|-------|---------|
| **What** | Label / heading / CTA misaligned on different horizontal axes |
| **Why** | CTA positioned relative to card edge instead of shared wrapper; button width asymmetry |
| **How to catch** | CR-04 · Layout Spec §4 CENTER LINE · visual check against JPG center axis |

### FT-09 — DISCOVERY V1 TREE REUSE

| Field | Content |
|-------|---------|
| **What** | DOM tree copied from Discovery v1: `Hero → Background → Overlay Card → Label → Heading → CTA` (CTA nested in card) |
| **Why** | First filed discovery doc in folder; grep hits Discovery before Layout Spec |
| **How to catch** | Compare tree §6 to Discovery v1 rejected tree in Layout Spec §5 · Relation Audit §3 |

### FT-10 — CARD SURFACE / CONTENT STACK MERGE

| Field | Content |
|-------|---------|
| **What** | GROUP-02A and GROUP-02B collapsed — text placed directly on background without frosted shell distinction |
| **Why** | Forensic split seen as «over-engineering» |
| **How to catch** | CR-14 · Forensic GROUP-02 **AGGREGATED** verdict · card surface visually present in JPG |

### FT-11 — HEADER HERO MERGE

| Field | Content |
|-------|---------|
| **What** | Hero background or overlay content bleeds into header assembly; nav/logo treated as Hero layer |
| **Why** | Full-page mockup read as one chrome block |
| **How to catch** | CR-10 · Hero START below nav-row · header assembly scope separate |

### FT-12 — INTRO SECTION IN HERO

| Field | Content |
|-------|---------|
| **What** | Hero extended to include white intro section «Шпиговский дом — восстановление…» or Discovery END marker «МНОГОПРОФИЛЬНОЕ…» |
| **Why** | Wrong END boundary from Discovery v1 |
| **How to catch** | CR-11 · Layout Spec FD-02 · Forensic END boundary |

### FT-13 — SUBTITLE INVENTION

| Field | Content |
|-------|---------|
| **What** | Description paragraph added between heading and card bottom or between card and CTA |
| **Why** | Agent expects «hero subtitle» pattern from other landings |
| **How to catch** | CR-08 · Forensic «subtitle NOT PRESENT» · GROUP-02B = two children only |

### FT-14 — BACKGROUND OVERLAY SKIP

| Field | Content |
|-------|---------|
| **What** | GROUP-01B wash omitted — photo at full saturation/brightness without global overlay |
| **Why** | Sub-layer not in Discovery v1 register |
| **How to catch** | CR-12 · Forensic IMAGE OVERLAY **PRESENT** · assembly S-03 mandatory |

### FT-15 — CORNER MASK SKIP

| Field | Content |
|-------|---------|
| **What** | Hero container sharp corners — GROUP-01C not applied |
| **Why** | Mask treated as card-only radius |
| **How to catch** | GROUP-01C assembly S-02 · Forensic IMAGE MASK **PRESENT** on Hero bounds |

### FT-16 — VISUAL INTERPRETATION

| Field | Content |
|-------|---------|
| **What** | Hero implemented from memory / chat summary without filed Layout Spec + Assembly Spec |
| **Why** | Skipped documentation gates |
| **How to catch** | Require citation: Layout Spec REF + Assembly Spec REF in implementation REPORT |

### FT-17 — TRIUMPH / STARTER REUSE

| Field | Content |
|-------|---------|
| **What** | Hero patterns copied from Triumph Manipulator landing, gulp-starter demo, or unrelated workspace |
| **Why** | Prior workspace muscle memory; similar starter architecture |
| **How to catch** | Scope lock: HOME-PAGE-FULL-MOCKUP.jpg composition only · CR rules · no cross-project partial reuse |

**Pre-code checklist (agent self-test):**

1. Assembly Order S-01…S-10 followed?  
2. Nine GROUP-IDs + content wrapper remain separable?  
3. CTA = sibling of card (Relation Audit §3)?  
4. All CR-01…CR-16 pass?  
5. No FT-01…FT-17 trigger?  
6. Content Lock v2 strings locked?

If any **NO** → **STOP** — no Hero HTML.

---

## 6. Frontend Tree Final

Итоговое дерево — **достаточно** для начала Hero HTML markup planning. **Не** является HTML spec.

```text
Hero (section root)                         ← S-01 · Hero bounds · START/END
├─ Background Layer                         ← S-02 · GROUP-01 + GROUP-01C
│  └─ Background Image Overlay              ← S-03 · GROUP-01B (wash; div or pseudo — UNKNOWN)
└─ Content Wrapper                          ← S-04 · structural · centers vertical stack
   ├─ Overlay Card                          ← S-05 · GROUP-02
   │  ├─ Card Surface                       ← S-06 · GROUP-02A · frosted panel
   │  └─ Content Stack                      ← S-07 · GROUP-02B · layout entity
   │     ├─ Label                           ← S-08 · GROUP-03
   │     └─ Main Heading                    ← S-09 · GROUP-04
   └─ CTA Primary                           ← S-10 · GROUP-05 · SIBLING of Overlay Card
```

**Rejected tree (Discovery v1 — do not use):**

```text
Hero
├─ Background
└─ Overlay Card
   ├─ Label
   ├─ Heading
   └─ CTA          ← ERROR: CTA not inside card
```

**Structural block count (planning only):** Hero root · background · background-overlay · content wrapper · card surface · content stack (optional explicit wrapper) · CTA wrapper — **5–7** structural blocks. GROUP-01B may be pseudo — **UNKNOWN** (U-09).

**Text nodes:** GROUP-03 label · GROUP-04 heading · GROUP-05 button label — separate DOM text elements inside their assembly units.

**Content Lock v2 (frozen copy for HTML phase):**

| GROUP-ID | Locked string |
|----------|---------------|
| GROUP-03 | `Центр профилактики и лечения зависимостей` |
| GROUP-04 | `Шпиговский дом` |
| GROUP-05 | `ЗАПИСАТЬСЯ НА КОНСУЛЬТАЦИЮ` |

---

## 7. Implementation Readiness

| Gate | Answer |
|------|--------|
| **HERO ASSEMBLY SPEC COMPLETE** | **YES** |
| **CTA RELATION PRESERVED** | **YES** (GROUP-05 = sibling of GROUP-02 under content wrapper; FD-03 / Relation Audit §3) |
| **READY FOR HERO HTML** | **YES** (frontend tree §6 sufficient to begin markup planning; Visual Scale Spec still required for pixel build) |
| **READY FOR HERO BUILD** | **NO** |

**Not unlocked by this document:**

- Hero SCSS / visual tokens / px geometry (Layout Spec §7 Safe UNKNOWN U-01…U-10)  
- Hero Visual Scale Spec (separate future artifact)  
- Operator **APPROVED** gate on this Assembly Spec (awaiting decision)  
- Mobile/tablet Hero assembly (U-06)

**Unlock sequence for future implementation:**

```text
1. Operator APPROVED — FP-0002-HERO-LAYOUT-SPEC-v1.md (upstream)
2. Operator APPROVED — FP-0002-HERO-ASSEMBLY-SPEC-v1.md (this document)
3. THEN — Hero HTML allowed (cite both REFs in REPORT)
4. Hero Visual Scale Spec — before SCSS pixel build
5. THEN — Hero SCSS / build → QA → Operator Visual Review
```

---

## 8. Final Verdict

Hero Assembly Spec v1 фиксирует **порядок сборки S-01…S-10** от Hero root через background sub-layers (GROUP-01 / 01B / 01C) к content wrapper, затем **card assembly** (GROUP-02 → 02A → 02B → GROUP-03 → GROUP-04) и **CTA как sibling карточки** (GROUP-05).

**CTA relation B (sibling of card)** — подтверждён и сохранён. Discovery v1 grouping, tree и Content Lock — **отклонены**.

**Group Register v2** (9 IDs + content wrapper) — assembly chain полная.

Hero Assembly Spec завершён. **Hero HTML · Hero SCSS · Hero Build · Hero Visual Scale Spec — не создавать.** Ожидание решения оператора.

---

**STOP.**

---

## Git status

| Item | Value |
|------|-------|
| Commit / push | **Not performed** (default policy) |
| Changed files (this task) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-HERO-ASSEMBLY-SPEC-v1.md` (created) |
| Build workspace | **Not modified** |
| `desktop-shell.html` · `desktop-ui-demo.html` · header · footer · `dist` | **Not touched** |
