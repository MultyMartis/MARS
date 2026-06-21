# FP-0002 v2 — Design System Snapshot v1

**Document type:** Design System Snapshot (audit-only — **no code implementation**)  
**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-22  
**Sources:** FIG variables + component instances + PDF numeric sampling + Production Standards v3 (reference)

**Purpose:** Single-page SSOT snapshot for Discovery / token wiring later. **Not** wired to `fp-0002-shpigovsky-v2/src/scss/`.

---

## 1. Colors

### 1.1 FIG variable names (presence confirmed)

`Colors` collection · `Color text` · `Backgrounds/Primary` · `Color / Primary 1` · `red` · `white` · `Back1` · `Back2` · `Red blank`

### 1.2 Sampled / documented values

| Token (snapshot) | FIG/PDF sample | Production v3 | Snapshot status |
|------------------|----------------|---------------|-----------------|
| `accent-primary` | `#B3261D` (PDF scan) | `#B3261E` | **CONFIRMED** presence · Δ1 hex — use operator tier |
| `text-primary` | `#3B3D3D` (PDF) | `#475371` | **CONFLICT** — coordinator vs PDF |
| `text-muted` | `#8D9097` | — | **ESTIMATED** |
| `bg-page-wash` | `#E3EAF2` / `#E4EBF3` | `rgba(218,229,240,0.7)` | **CONFLICT** — layer vs solid |
| `bg-base` | white nodes in FIG | `#FFFFFF` | **CONFIRMED** |
| `chrome-dark` | `#455069` footer sampling | — | **ESTIMATED** |
| `border-card` | `#CBD4E0` | — | **ESTIMATED** |
| `border-subtle` | `#C6CEDA` | — | **ESTIMATED** |
| `text-on-accent` | — | `#FFFFFF` | **ESTIMATED** |

---

## 2. Radius

| Element | PDF numeric v2 | FIG instance sampling | Production v3 | Snapshot |
|---------|----------------|----------------------|---------------|----------|
| Primary button | 6 px ESTIMATED | rounded rects on `Кнопка` | **30 px** | **CONFLICT** |
| Card | 8 px ESTIMATED | — | **30 px** default | **CONFLICT** |
| Input | 6 px | `Поле ввода` | **10 px** | **CONFLICT** |
| Pill / avatar | 50% | circular crops | **999 px** | **ALIGNED** (intent) |
| FAQ panel | 8 px | — | 30 / 10 TBD | **ESTIMATED** |

**Snapshot rule for v2 Discovery:** Production Standards v3 wins for **implementation** unless operator overrides with FIG-measured proof per component.

---

## 3. Buttons

| Pattern | FIG instance | H×W (est.) | Notes |
|---------|--------------|------------|-------|
| Primary CTA | `Кнопка` | **44** px height · ~324 px hero width | Red fill; label 16 px |
| Header CTA | `Кнопка` in `Хедер` | compact | «Записаться на консультацию» |
| Text / inline | `Кнопка` | auto width | BLK-025 family |
| Pagination | square cells | **40×40** | BLK-017 |
| Mobile sticky (×3) | chrome | equal thirds | BLK-004 — height **SAFE UNKNOWN** |

**States (hover/focus/disabled):** **SAFE UNKNOWN** — not in static PDF/FIG export.

---

## 4. Inputs (BLK-035)

| Field | Height | Padding (est.) | Border | Layout |
|-------|--------|----------------|--------|--------|
| text / tel / email | **48 px** | 16×12 | 1 px | 2-col desktop · 1-col mobile |
| textarea | **~120 px** | 16 | 1 px | full width |
| submit | **44 px** | — | — | primary button |

---

## 5. Cards

| Type | Columns D/M | Gap | Border | Image |
|------|-------------|-----|--------|-------|
| UTP / Feature | 3 → 1 | 24 px est. | 1 px | — |
| Service | 3–4 → 1 | 24 px | 1 px | 16:10 est. |
| Specialist | 4 → 1 | 24 px | — | portrait |
| Review | 3 → 1 | 24 px | — | — |
| Article | 3 → 1 | 24 px | — | landscape |

**Shadow:** flat / none — **ESTIMATED CONFIRMED**

---

## 6. Containers & spacing

| Parameter | FIG artboard | PDF median | Production v3 | Snapshot |
|-----------|--------------|------------|---------------|----------|
| Desktop artboard | **1437 px** | **1437 px** | ref only | **CONFIRMED** |
| Mobile artboard | **380 px** (390 About mob) | **380/390** | ref only | **CONFIRMED** |
| Container max | inner frames **1170 px** (`Хедер`) | ~1020 content | **1170 px** | **ALIGNED** |
| Page padding desktop | — | 172 median / 133 Contacts | **40 px** | **CONFLICT** |
| Page padding mobile | — | 41 px text bbox | **20 px** | **CONFLICT** |
| Section gap | — | 72 / 56 / 250 clusters | Factory 4px scale | **ESTIMATED** |
| Grid gutter | — | 24 px | 24 px | **ESTIMATED** |

**CSS breakpoint:** Production **`min-width: 1024px`** — **not** measured from FIG artboards (380 vs 1437 only).

---

## 7. Components (FIG symbol library)

| Symbol / INSTANCE | Count hint | Role |
|-----------------|------------|------|
| `Кнопка` | 954 instances total file | Button |
| `Подвал` | footer | Footer |
| `Поле ввода` | forms | Input |
| `Расскрытие вопроса` / `Вопрос скрыт` | FAQ | Accordion |
| `отзыв` | reviews | Card |
| `Врач` | specialists | Card |
| `Статья` | articles | Card |
| `search` | header | Icon button |
| `этап` / `Цифра` | steps / program | Numbered tiles |

**76 SYMBOL** · **954 INSTANCE** — design system **exists in FIG** (`Internal Only Canvas`).

---

## 8. Implementation status

| Item | Status |
|------|--------|
| Tokens in v2 workspace | **NOT STARTED** — placeholder `_tokens.scss` only |
| This snapshot | **AUDIT ARTIFACT ONLY** |

---

## Document control

| Field | Value |
|-------|-------|
| Version | v1 (v2 audit pass) |
| Next | Discovery token binding charter |
