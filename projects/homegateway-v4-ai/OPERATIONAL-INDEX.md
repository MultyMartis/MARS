# HomeGateway v4.ai — operational index

**Статус:** **DRAFT** · **PLANNING** · Phase 2 active (Phase 1 foundation complete)  
**Классификация (Wave 1A):** Program **`planned`** · Workspace **UI Prototype** · Documentation **Operational Documentation Pack** (см. [registry/project-registry.md](../../registry/project-registry.md) — «operational» = дисциплина док-пака, не зрелость продукта)  
**Назначение:** одна короткая карта для оператора и агента — куда идти в сессии, без полного каталога governance.

**Не является:** runtime-индексом, API-каталогом, реестром деплоя.

**Идентичность пакета:** [README.md](README.md) · **project_id:** `homegateway-v4-ai`

---

## Canonical entry

- **[README.md](README.md)** — границы, честность, карта документов v0.1.

---

## Phase 1 pack (UX discovery foundation)

Использовать при работе в **Phase 1** (до wireframes). Полный набор:

| Doc | Role |
|-----|------|
| [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) | JTBD, сценарии, pain points |
| [screen-map-v0.1.md](screen-map-v0.1.md) | Экраны и static MVP checklist |
| [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) | Типы и размеры block-screen |
| [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md) | Зоны shell (non-binding layout) |
| [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md) | Admin entry + admin-aware static prep |

---

## Core Run (default session)

Открывать **одну строку** за сессию, если задача не требует соседних фаз явно.

| # | Concern | Purpose | Entry file | When to use | Output expected |
|---|---------|---------|------------|-------------|-----------------|
| 1 | **Project architecture** | Роль HG в MARS, block-screen, границы MVP | [cockpit-architecture-blueprint-v0.1.md](cockpit-architecture-blueprint-v0.1.md), [product-positioning-v0.1.md](product-positioning-v0.1.md) | Новый участник; scope gate | Модель кокпита; non-goals |
| 2a | **UX discovery notes** | Задачи оператора, сценарии дня, приоритеты | [ux-discovery-notes-v0.1.md](ux-discovery-notes-v0.1.md) | Старт Phase 1; перед screen map | JTBD table; open questions list |
| 2b | **Screen map** | Инвентарь экранов, static MVP screen checklist | [screen-map-v0.1.md](screen-map-v0.1.md) | После 2a; перед wireframes | Согласованный screen inventory |
| 2c | **Block-screen taxonomy** | Типы, размеры, разметка admin-aware | [block-screen-taxonomy-v0.1.md](block-screen-taxonomy-v0.1.md) | Параллельно 2b; перед layout | Taxonomy + markup conventions |
| 2d | **Layout zones** | Shell zones; variants = mode tendencies | [cockpit-layout-zones-v0.1.md](cockpit-layout-zones-v0.1.md), [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) | Phase 2 | Zone catalog + A–D reframe |
| 2e | **Admin-aware static prep** | Entry point + CRUD entity map для static HTML | [admin-entry-and-future-crud-notes-v0.1.md](admin-entry-and-future-crud-notes-v0.1.md), [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md) | До Phase 4 static | Admin entry spec + data-structure checklist |
| **2f** | **Multi-view cockpit system** | HG как connected views, не one dashboard | [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) | Phase 2 start | Canonical multi-view model |
| **2g** | **Operational modes** | Modes A–H: purpose, density, risks | [operational-modes-v0.1.md](operational-modes-v0.1.md) | После 2f | Mode spec table |
| **2h** | **Navigation hierarchy** | L1/L2/L3, overlays, mode switch | [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) | После 2g | Navigation model |
| **2i** | **Cockpit ergonomics** | Density, cognitive load, overload risks | [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) | Параллельно wireframes | Density guidelines |
| **2j** | **Cockpit OS concept** | Conceptual environment direction only | [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md) | On demand | Terminology guardrails |
| **2k** | **Spatial cockpit architecture** | Tri-focus zones, post–prototype canon | [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) | After prototype review; before Phase 3–4 HTML | Zone catalog + anti-dashboard |
| **2l** | **Tactical signal philosophy** | `info_area` role, levels, anti-fatigue | [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) | With 2k | Signal psychology + persistence |
| **2m** | **Surface + motion + depth** | Interaction states, timing, z-layers | [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md), [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md), [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) | Phase 3–4 prep | UX doctrine for implementation |
| **2n** | **Viewport + scroll** | No page scroll, internal regions | [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md), **[desktop-viewport-shell-rule-v0.1.md](desktop-viewport-shell-rule-v0.1.md)** | With 2k; **before MVP HTML shell work** | Viewport-first rules + **2560×1440 / 1920px centered shell** |
| **2o** | **Information priority** | P0–P3 attention model | [information-priority-model-v0.1.md](information-priority-model-v0.1.md) | With 2l | Anti-overload mapping |
| **2p** | **Visual language direction** | Tactical calm, anti-SaaS/gamer | [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) | Phase 3 entry | Visual charter |
| **2s** | **Visual direction exploration pack** | DNA, materials, atmosphere, anti-patterns | [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) | Lane B; after 2k–2p | Visual crystallization v0.1 |
| **2t** | **Atmospheric visual exploration pack** | Probes, mood studies, prompt library, evaluation | [atmospheric-visual-exploration-pack-v0.1.md](atmospheric-visual-exploration-pack-v0.1.md) | Lane B; after 2s | Atmospheric probes v0.1 (no auto-gen in-repo) |
| **2q** | **Focus state model** | Overlay, focus, critical behaviors | [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md) | With 2k, 3f | Dimming + context preservation |
| **2r** | **Loading + empty states** | Skeleton, calm emptiness | [loading-and-empty-state-philosophy-v0.1.md](loading-and-empty-state-philosophy-v0.1.md) | Phase 4 prep | No layout jumps |
| 3 | **Wireframes** | HTML-oriented exploration pack | [wireframes/README.md](wireframes/README.md), [wireframes/wireframe-exploration-pack-v0.1.md](wireframes/wireframe-exploration-pack-v0.1.md) | После 2f–2h | Wireframe docs (no HTML yet) |
| **3a** | **Main cockpit wireframe** | Mode D composition | [wireframes/main-cockpit-wireframe-v0.1.md](wireframes/main-cockpit-wireframe-v0.1.md) | Row 3 | ASCII layout + blocks |
| **3b** | **Systems monitor wireframe** | Mode B grid | [wireframes/systems-monitor-wireframe-v0.1.md](wireframes/systems-monitor-wireframe-v0.1.md) | Row 3 | Status grid spec |
| **3c** | **Focus workspace wireframe** | Mode C minimal | [wireframes/focus-workspace-wireframe-v0.1.md](wireframes/focus-workspace-wireframe-v0.1.md) | Row 3 | Low-noise layout |
| **3d** | **Tactical signals wireframe** | Urgency + filters | [wireframes/tactical-signals-wireframe-v0.1.md](wireframes/tactical-signals-wireframe-v0.1.md) | Row 3 | Signal display rules |
| **3e** | **Navigation shell** | L1/L2/L3 | [wireframes/navigation-shell-wireframe-v0.1.md](wireframes/navigation-shell-wireframe-v0.1.md) | Row 3 | Shell + mode indicator |
| **3f** | **Overlay behavior** | L3 panels | [wireframes/overlay-and-popup-behavior-v0.1.md](wireframes/overlay-and-popup-behavior-v0.1.md) | Row 3 | Overlay types + stack rules |
| **3g** | **Static prototype readiness** | Phase 4 HTML prep | [wireframes/static-prototype-readiness-checklist-v0.1.md](wireframes/static-prototype-readiness-checklist-v0.1.md) | Before workspace | Checklist gate |
| 4 | **Visual direction** | Dark/light cockpit, glass, signals | [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md), [theme-system-draft-v0.1.md](theme-system-draft-v0.1.md) | Перед static MVP | Token groups approved for Phase 3 |
| 5 | **Static frontend MVP** | Mock login, cockpit, samples, admin stub | [screen-map-v0.1.md](screen-map-v0.1.md) § Static MVP · [README.md](README.md) | Phase 4 only | Static prototype; **no** backend |
| 6 | **Admin layer (future CRUD)** | Полный CRUD после static | [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md) | Phase 5–6 | Admin IA + entity forms |
| 7 | **Future integrations** | MARS/n8n/bots/leads | [roadmap-v0.1.md](roadmap-v0.1.md) Phase 7, [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) | После static MVP | FUTURE-INTEGRATION backlog |

**Phase 1 exit criteria:** docs 2a–2e согласованы ✓ (2026-05-20).

**Phase 2 exit criteria (draft):** 2f–2h + layout variants analysis ✓; wireframe pack (row 3, 3a–3g) ✓ (2026-05-20); wireframe **docs** complete — static HTML в workspace MVP v1 (см. ниже), Phase 4 gate ещё не закрыт.

**Post–Prototype v0.1 spatial formalization (2026-05-24):** Lane B — spatial cockpit architecture pack ✓ (docs 2k–2t below). Dashboard-grid reading **deprecated**; canonical phrase: *spatial operational cockpit environment with layered tactical awareness*.

---

## Wireframe pack (HTML-first, Phase 2)

| Doc | Role |
|-----|------|
| [wireframes/README.md](wireframes/README.md) | Folder entry |
| [wireframes/wireframe-exploration-pack-v0.1.md](wireframes/wireframe-exploration-pack-v0.1.md) | Master pack + density experiments |
| [wireframes/main-cockpit-wireframe-v0.1.md](wireframes/main-cockpit-wireframe-v0.1.md) | Default home (D) |
| [wireframes/systems-monitor-wireframe-v0.1.md](wireframes/systems-monitor-wireframe-v0.1.md) | Systems (B) |
| [wireframes/focus-workspace-wireframe-v0.1.md](wireframes/focus-workspace-wireframe-v0.1.md) | Focus (C) |
| [wireframes/tactical-signals-wireframe-v0.1.md](wireframes/tactical-signals-wireframe-v0.1.md) | Tactical / rail hybrid |
| [wireframes/navigation-shell-wireframe-v0.1.md](wireframes/navigation-shell-wireframe-v0.1.md) | Shell L1–L3 |
| [wireframes/overlay-and-popup-behavior-v0.1.md](wireframes/overlay-and-popup-behavior-v0.1.md) | Overlays |
| [wireframes/static-prototype-readiness-checklist-v0.1.md](wireframes/static-prototype-readiness-checklist-v0.1.md) | Phase 4 gate |

**Decision:** HTML wireframe prototype preferred over Figma-first.

---

## Phase 2 pack (multi-view cockpit UX)

| Doc | Role |
|-----|------|
| [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md) | Why multi-view; view inventory |
| [operational-modes-v0.1.md](operational-modes-v0.1.md) | Modes A–H specification |
| [navigation-hierarchy-v0.1.md](navigation-hierarchy-v0.1.md) | L1/L2/L3 navigation |
| [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) | A–D reframe + SaaS anti-patterns |
| [cognitive-load-and-density-notes-v0.1.md](cognitive-load-and-density-notes-v0.1.md) | Density scaling, risks |
| [cockpit-os-concept-notes-v0.1.md](cockpit-os-concept-notes-v0.1.md) | Cockpit OS concept (not real OS) |

---

## Spatial cockpit architecture pack (post–Prototype v0.1)

| Doc | Role |
|-----|------|
| [cockpit-spatial-architecture-v0.1.md](cockpit-spatial-architecture-v0.1.md) | **Canonical** tri-focus zones (`top_bar`, `main_area`, `info_area`, …) |
| [tactical-signal-philosophy-v0.1.md](tactical-signal-philosophy-v0.1.md) | `info_area` = tactical awareness, not inbox |
| [surface-behavior-system-v0.1.md](surface-behavior-system-v0.1.md) | hover / selected / critical / overlay-open |
| [motion-and-transition-charter-v0.1.md](motion-and-transition-charter-v0.1.md) | fast / base / slow · easing |
| [depth-and-z-layer-system-v0.1.md](depth-and-z-layer-system-v0.1.md) | Z-layer stack · anti chaos |
| [information-priority-model-v0.1.md](information-priority-model-v0.1.md) | P0–P3 |
| [viewport-and-scroll-philosophy-v0.1.md](viewport-and-scroll-philosophy-v0.1.md) | Viewport-first · no page scroll |
| [desktop-viewport-shell-rule-v0.1.md](desktop-viewport-shell-rule-v0.1.md) | **Desktop shell geometry** · 2560×1440 · centered 1920px wrapper |
| [ui-semantics-and-interaction-system-v0.1.md](ui-semantics-and-interaction-system-v0.1.md) | **Canonical UI semantics** · tabs, indicators, favorites, `#main_area` behavior |
| [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) | Tactical calm · anti-SaaS/gamer |
| [operational-focus-state-model-v0.1.md](operational-focus-state-model-v0.1.md) | Focus / overlay / critical states |
| [loading-and-empty-state-philosophy-v0.1.md](loading-and-empty-state-philosophy-v0.1.md) | Skeleton · calm emptiness |

**Entry for architecture gate:** [cockpit-architecture-blueprint-v0.1.md](cockpit-architecture-blueprint-v0.1.md) (updated diagram + links).

---

## Visual Direction Exploration Pack v0.1 (Lane B)

| Doc | Role |
|-----|------|
| [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) | **Master** — pillars, psychology, pack index |
| [visual-dna-and-identity-v0.1.md](visual-dna-and-identity-v0.1.md) | Emotional DNA, operator identity |
| [surface-material-language-v0.1.md](surface-material-language-v0.1.md) | Surface taxonomy, glass, borders |
| [background-and-environment-philosophy-v0.1.md](background-and-environment-philosophy-v0.1.md) | Atmospheric environment — not wallpaper |
| [lighting-and-depth-atmosphere-v0.1.md](lighting-and-depth-atmosphere-v0.1.md) | Ambient / focus / signal light |
| [color-behavior-and-accent-philosophy-v0.1.md](color-behavior-and-accent-philosophy-v0.1.md) | Operational color zones |
| [typography-atmosphere-v0.1.md](typography-atmosphere-v0.1.md) | Exo 2 operational typography |
| [motion-atmosphere-v0.1.md](motion-atmosphere-v0.1.md) | Motion mood (charter = timing) |
| [visual-anti-patterns-v0.1.md](visual-anti-patterns-v0.1.md) | Visual danger doctrine |
| [reference-analysis-and-visual-boundaries-v0.1.md](reference-analysis-and-visual-boundaries-v0.1.md) | Reference filter rules |

**Entry:** [visual-language-direction-v0.1.md](visual-language-direction-v0.1.md) (summary charter) → pack for Phase 3 depth.

---

## Atmospheric Visual Exploration Pack v0.1 (Lane B)

| Doc | Role |
|-----|------|
| [atmospheric-visual-exploration-pack-v0.1.md](atmospheric-visual-exploration-pack-v0.1.md) | **Master** — probes, mood discovery, operator calibration |
| [visual-probe-methodology-v0.1.md](visual-probe-methodology-v0.1.md) | Generate, compare, filter probes |
| [visual-probe-evaluation-framework-v0.1.md](visual-probe-evaluation-framework-v0.1.md) | Pass/fail checklist |
| [image-generation-prompt-library-v0.1.md](image-generation-prompt-library-v0.1.md) | Structured prompts (external tools) |
| [tactical-darkness-study-v0.1.md](tactical-darkness-study-v0.1.md) | Cockpit darkness, volumetric depth |
| [overlay-material-study-v0.1.md](overlay-material-study-v0.1.md) | Glass, overlays, immersion |
| [tactical-rail-atmosphere-study-v0.1.md](tactical-rail-atmosphere-study-v0.1.md) | `info_area` peripheral mood |
| [main-workspace-atmosphere-study-v0.1.md](main-workspace-atmosphere-study-v0.1.md) | `main_area` focus environment |
| [light-theme-tactical-environment-study-v0.1.md](light-theme-tactical-environment-study-v0.1.md) | Tactical light theme — anti-SaaS/CRM |
| [environmental-depth-study-v0.1.md](environmental-depth-study-v0.1.md) | Background as atmospheric layer |

**Entry:** [visual-direction-exploration-pack-v0.1.md](visual-direction-exploration-pack-v0.1.md) → atmospheric pack when running mood probes.

**Не claim:** generated images in-repo, final UI approval, Figma, frontend.

---

## Supporting docs (on demand)

| Concern | Entry |
|---------|--------|
| Module inventory | [module-registry-draft-v0.1.md](module-registry-draft-v0.1.md) |
| Signals & deadlines | [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) |
| Phases 0–8 | [roadmap-v0.1.md](roadmap-v0.1.md) |
| Registry row | [registry/project-registry.md](../../registry/project-registry.md) |

---

## Session discipline

1. **Один Core Run row** — Phase 1: последовательность 2a → 2e или одна строка за сессию.
2. **STATIC-FIRST** — не проектировать backend в Phase 1.
3. **FUTURE-INTEGRATION** — live MARS/n8n/bots только planned.
4. **STOP** — после screen map + zones достаточно для wireframes; не уходить в Phase 4 code.

---

## Workspace (UI prototype)

| Layer | Path | Maturity |
|-------|------|----------|
| **UI Prototype** | `workspaces/homegateway-v4-ai/v1/` | Static Gulp skeleton (MVP v1 init 2026-05-25) — **not** shippable product MVP |
| Init report | [reports/mvp-v1-initialization-report.md](reports/mvp-v1-initialization-report.md) | Build verified at bootstrap |
| Tools | `tools/bootstrap-mvp-v1.ps1`, `verify-mvp-v1-shell.mjs` | Experimental draft tooling |

---

## SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Wireframes location | `projects/homegateway-v4-ai/wireframes/` (docs); static HTML in `workspaces/homegateway-v4-ai/v1/` |
| Workspace folder | `workspaces/homegateway-v4-ai/v1/` — UI prototype active |
| Leads dedicated mode vs Main block | Wireframes |
| Static MVP minimum view count | Likely Main + 1 specialized |

---

*Last updated: 2026-05-25 — UI semantics doc added to spatial cockpit pack; MVP v1 workspace active.*
