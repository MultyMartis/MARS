# HomeGateway v4.ai — operational modes v0.1

**Статус:** **DRAFT** · **PLANNING** · Phase 2  
**Назначение:** спецификация **cockpit modes / operational views** — purpose, density, navigation, risks.

**Родительская модель:** [multi-view-cockpit-system-v0.1.md](multi-view-cockpit-system-v0.1.md)

**Layout tendencies:** [layout-variants-analysis-v0.1.md](layout-variants-analysis-v0.1.md) (A/B/C/D)

---

## Легенда полей

| Поле | Шкала / смысл |
|------|----------------|
| **Density** | low · medium · high |
| **Signal intensity** | ambient · moderate · high · critical-focused |
| **Cognitive load** | low · medium · high (ожидаемая нагрузка на оператора) |
| **Layout tendency** | A / B / C / D / hybrid |

---

## A. Main Cockpit

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-main-cockpit` |
| **Purpose** | General operational overview; default «home»; hybrid balance |
| **Density** | medium |
| **Signal intensity** | moderate — deadlines visible, not dominant |
| **Cognitive load** | medium |
| **Layout tendency** | **D** Hybrid Operational Cockpit (elements of A + selective B blocks) |
| **Likely layout** | Full shell: left nav, central canvas (mixed block-screens), right signal rail, bottom quick strip |
| **Navigation behavior** | Layer 1–2 hub; overlays for project detail; shortcuts to other modes |
| **Ideal scenario** | Start of day; return between tasks; «где я в целом» |
| **Risks** | Становится «ещё одним dashboard» если все блоки равноправны; перегруз карточками |
| **Mitigation** | Signal hierarchy; не все module groups на canvas одновременно; progressive disclosure |

---

## B. Systems Monitor

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-systems-monitor` |
| **Purpose** | Status-heavy: bots, MARS, workflows, uptime/state |
| **Density** | high |
| **Signal intensity** | moderate–high (health, attention states) |
| **Cognitive load** | medium–high (много индикаторов, scan grid) |
| **Layout tendency** | **B** Modular Monitoring Grid |
| **Likely layout** | Grid-oriented block-screens; reduced narrative content; optional collapse of client blocks |
| **Navigation behavior** | Enter from Layer 2; deep panel for single system detail; **display-only** v0.1 |
| **Ideal scenario** | «Всё ли живо» перед релизом; после сбоя automation; weekly health check |
| **Risks** | NOC-dashboard aesthetic; table overload; false precision на mock data |
| **Mitigation** | Group by system family; signal colors restrained; no fake real-time animation |

**Maps to screens:** `scr-mars-monitor`, `scr-bots-systems` (+ aggregated status blocks).

---

## C. Focus Workspace

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-focus-workspace` |
| **Purpose** | Active project/task; lower noise; higher concentration |
| **Density** | low–medium |
| **Signal intensity** | low ambient; project-critical signals only |
| **Cognitive load** | low–medium |
| **Layout tendency** | **C** Tactical Focus Workspace |
| **Likely layout** | Reduced rails; enlarged central canvas; signal rail hidden or minimized; optional single-project lock |
| **Navigation behavior** | Enter with project context; exit returns to Main; minimal Layer 3 popups |
| **Ideal scenario** | 1–2 часа работы по одному клиенту; правки, ссылки, handoff |
| **Risks** | Слишком пустой экран → потеря situational awareness; сложно вернуть global signals |
| **Mitigation** | Compact persistent alert chip; one-click «expand signals» |

**Maps to screens:** `scr-project-detail` as primary; may subsume Focus mode.

---

## D. Tactical Signals

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-tactical-signals` |
| **Purpose** | Deadlines, warnings, recurring tasks, urgency |
| **Density** | medium–high |
| **Signal intensity** | high · critical-focused |
| **Cognitive load** | medium–high (time pressure) |
| **Layout tendency** | **C** + signal rail emphasis (vertical priority list) |
| **Likely layout** | Dominant deadline/recurring blocks; chronological or severity sort; reduced link hubs |
| **Navigation behavior** | Fast entry from signal rail anywhere; item click → overlay or Project View |
| **Ideal scenario** | Перед созвоном; конец дня; monthly recurring wave |
| **Risks** | Alarm fatigue; everything red; anxiety UX |
| **Mitigation** | [signal-system-draft-v0.1.md](signal-system-draft-v0.1.md) levels; calm overdue vs danger |

**Maps to screens:** `scr-signals-deadlines`.

---

## E. Project View

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-project` |
| **Purpose** | Client/project-centric operational screen |
| **Density** | medium |
| **Signal intensity** | moderate (project-scoped deadlines) |
| **Cognitive load** | medium |
| **Layout tendency** | **A** Centralized Command (project as command center) + **D** hybrid |
| **Likely layout** | Project header zone; related links grid; status; nested quick actions |
| **Navigation behavior** | From Clients list or search; breadcrumb client → project; overlay optional |
| **Ideal scenario** | Onboarding нового этапа; подготовка к демо клиенту |
| **Risks** | CRM clone; duplicate Focus Workspace |
| **Mitigation** | Project View = **structure + links + status**; Focus = **work session chrome** |

**Maps to screens:** `scr-clients-projects`, `scr-project-detail`.

---

## F. Quick Actions Mode

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-quick-actions` |
| **Purpose** | Fast launch, clipboard, utility interactions |
| **Density** | low |
| **Signal intensity** | low |
| **Cognitive load** | low |
| **Layout tendency** | Strip-first; may be **mode** or **persistent zone** (`zone-strip-bottom`) |
| **Likely layout** | Large action tiles; clipboard blocks; minimal chrome |
| **Navigation behavior** | Overlay or dedicated thin view; keyboard-friendly future |
| **Ideal scenario** | Между звонками; копирование handoff; open staging |
| **Risks** | Launcher app feeling; duplicate bottom strip on every view |
| **Mitigation** | Phase 4: bottom strip global + optional expanded Quick Actions mode |

**Maps to screens:** `scr-quick-actions`.

---

## G. Admin Mode

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-admin` |
| **Purpose** | Future CRUD / data management |
| **Density** | medium (forms) · high (lists) — **FUTURE** |
| **Signal intensity** | low operational; validation errors local |
| **Cognitive load** | medium–high |
| **Layout tendency** | Separate from cockpit chrome; **avoid** full SaaS admin shell |
| **Likely layout** | Simpler than enterprise admin; table restraint; link back to cockpit |
| **Navigation behavior** | `scr-admin-entry` → `scr-admin-area`; clear exit to Main Cockpit |
| **Ideal scenario** | Редактирование клиентов/дедлайнов после Phase 5–6 |
| **Risks** | Generic admin panel; breaks cockpit atmosphere |
| **Mitigation** | [admin-layer-plan-v0.1.md](admin-layer-plan-v0.1.md); shared tokens, lighter chrome |

**Status:** **FUTURE** — not static MVP.

---

## H. Settings / Personalization

| Attribute | Value |
|-----------|-------|
| **view_id** | `view-settings` |
| **Purpose** | Themes, layout preferences, cockpit behavior |
| **Density** | low |
| **Signal intensity** | none operational |
| **Cognitive load** | low |
| **Layout tendency** | Panel or side sheet; not full dashboard |
| **Likely layout** | Theme toggle; density preference (future); default view (future) |
| **Navigation behavior** | Layer 2; rarely visited; from top bar or nav |
| **Ideal scenario** | Первый визит; смена dark/light; настройка default mode |
| **Risks** | Settings bloat; too many toggles early |
| **Mitigation** | Phase 4: theme only; defer advanced prefs |

**Maps to screens:** `scr-settings`.

---

## Mode combination matrix (draft)

| Combination | Valid? | Notes |
|-------------|--------|-------|
| Main + Tactical rail visible | ✓ | Default hybrid |
| Focus + full Systems grid | ✗ | Conflicting goals |
| Project View + Tactical overlay | ✓ | Project deadlines drill-down |
| Quick Actions as global strip + any view | ✓ | Recommended |
| Admin inside Main canvas | ✗ | Separate mode |

---

## Mode switching principles

1. **Explicit over magic** — оператор выбирает mode; no autonomous switching.
2. **Preserve context** — при возврате в Main не сбрасывать scroll/project selection без причины (implementation TBD).
3. **One primary signal domain per view** — не смешивать «все дедлайны мира» и «все боты» на одном экране без hybrid intent.
4. **Fast escape** — из любого mode один жест/klick «Home» → Main Cockpit.

---

## SAFE UNKNOWN

- Exact pixel layouts per mode — wireframes Phase 2.
- Whether Leads monitor is standalone view or block on Main — operator validation.
- Pinning a mode as startup default — Settings Phase 4+.

---

*Last updated: 2026-05-20 — Phase 2 operational modes.*
