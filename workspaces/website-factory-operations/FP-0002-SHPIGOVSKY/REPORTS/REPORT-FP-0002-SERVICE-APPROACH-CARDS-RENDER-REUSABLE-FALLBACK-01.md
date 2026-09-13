# REPORT — FP-0002 SERVICE APPROACH CARDS RENDER + REUSABLE FALLBACK 01

**Date:** 2026-09-14  
**Verdict:** **PASS_WITH_RESIDUALS**  
**Production URL (primary QA):** `https://shpigovsky.ru/uslugi/genotipirovenie/`  
**Canonical origin at wave start:** `d0ab990d1eb728faf6e0d907a405a4de56920653`

---

## 1. Verdict

**PASS_WITH_RESIDUALS**

Card-level reusable fallback for «Карточки подхода» is live. Genotyping local cards remain unchanged and render (`source=local`). Global reusable cards seeded with meaningful non-placeholder copy. Stages fallback and pending multi-image child-card delta preserved.

Residual: services with layout **Заглушка / placeholder** still show approach Admin fields (Service General parity) but frontend intentionally does not render the approach block — Admin content on those stubs remains non-FE. Documented; not auto-promoted to full service layout.

---

## 2. Current source-state topology

| Surface | State |
|--------|--------|
| `origin/mars/canonical-post-recovery` (fetched) | `d0ab990d` at wave start |
| This repair worktree | `X:\AI MARS STORAGE\worktrees\fp0002-service-approach-cards-reusable-fallback-01` |
| This repair branch | `wave/fp0002-service-approach-cards-reusable-fallback-01` |
| Pending multi-image worktree | `X:\AI MARS STORAGE\worktrees\fp0002-service-child-cards-multi-image-02` — **PRESERVED** |
| Pending multi-image branch | `wave/fp0002-service-child-cards-multi-image-02` — **PRESERVED** |
| Production deltas not on origin | `child-services.php` + `service-child-services.css` (multi-image wave) |

---

## 3. Fresh production intake

Layer-B baselines:  
`X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-service-approach-cards-reusable-fallback-01\prod-before\`

Confirmed before edit:

- Theme helpers/templates for approach/stages matched origin (safe edit base) except pending child-card files.
- Child-card files: production == multi-image worktree (`1d3e6e1fbd11` / `c43df6f43af2`); **not mutated**.
- Live geno `#1889` layout=`subdivision`; approach visible ON; 4 local cards present and already rendered on FE before this wave’s deploy.

Evidence: `REPORTS/evidence/prod-maint-service-approach-cards-reusable-fallback-01/prod-intake-parity.json`

---

## 4. Root cause

### A. Operator “Admin filled / FE empty” on some pages

1. Many services use editor role **`placeholder` (Заглушка)**.
2. Field-group filter still loads **Service General** parity Admin (including «7. Наш подход» + `service_general_approach_cards`) for `service` **and** `placeholder`.
3. Frontend `placeholder-stack` renders header/nav/H1/footer only — **no approach section**.
4. Result: Admin shows populated карточки (often DEMO seed), FE ignores them by layout design.

### B. Live subdivision / service-general (including genotyping)

At wave intake, local cards **already rendered** via `shpigovsky_get_section_approach_cards()` (with orphan-meta recovery). Genotyping FE titles/texts matched DB.

### C. Architectural gap fixed this wave

When section/block is **ON** and local approach cards are **empty**, frontend previously rendered the section chrome without cards (subdivision) or fell through to legacy/emergency paths (leaf) — **no reusable Admin owner**, unlike stages → Comfort Requirements.

---

## 5. Local data owner

| Field label | Field / meta | Type | Genotyping `#1889` |
|-------------|--------------|------|--------------------|
| Показывать блок «Наш подход» | `section_approach_visible` | true_false | `1` |
| Заголовок подхода | `section_approach_heading` | text | present |
| Выделенный абзац | `section_approach_highlight` | textarea | present |
| Intro | `section_approach_intro` | textarea | present |
| Карточки подхода | `section_approach_cards` (+ `_N_title` / `_N_text`) | repeater title/text | **4 rows** |
| (Услуга path) | `service_general_approach_*` | parallel general fields | used on leaf/service-general |

---

## 6. Current local-content inventory

Classification for published services (probe):

| Class | Meaning | Count (approx) |
|-------|---------|----------------|
| LOCAL_FILLED | subdivision/service-general with local cards; FE renders | 8 active layouts |
| PLACEHOLDER_ADMIN_ONLY | placeholder layout; Admin cards exist; FE no approach | 24 |
| LOCAL_EMPTY | ON + empty local cards | **0** at intake |
| SECTION_OFF | approach toggle OFF | **0** found |

Representative:

| service | URL | section enabled | local cards | frontend before | source after |
|---------|-----|-----------------|-------------|-----------------|--------------|
| Генотипирование `#1889` | `/uslugi/genotipirovenie/` | ON | 4 | 4 cards | **local** |
| Зависимости `#73` | `/uslugi/zavisimosti/` | ON | 4 | 4 cards | local |
| Алкоголь `#74` | `.../lechenie-alkogolnoy-zavisimosti/` | ON | 4 | 4 cards | local |
| Профилактический анализ `#75` | geno child | Admin ON | 4 DEMO | **0** (placeholder) | n/a (layout) |

Evidence: `inventory-readable.json`, `resolver-probe.json`, `frontend-before.json`, `frontend-after.json`

---

## 7. Reusable/global owner

| Item | Value |
|------|--------|
| Admin | `Настройки сайта → Подход к лечению — карточки` |
| Page slug | `admin.php?page=fp02-block-approach-cards` |
| Options context | `fp02-block-approach-cards` |
| Field group | `group_fp02_block_approach_cards` |
| Repeater | `reusable_approach_cards` (`title`, `text`) |
| Helper | `shpigovsky_get_reusable_approach_cards()` |
| Resolver | `shpigovsky_get_effective_service_approach_cards( $post_id, 'section'\|'general' )` |

Separate from Comfort Requirements / stages owner.

---

## 8. Reusable card content

### Card 1

**Title:** Индивидуальный план  

**Text:** Работа начинается с вашей ситуации, а не с общей схемы. План строится с учётом состояния человека, целей обращения и того, какая форма помощи сейчас уместна — от консультации и диагностики до программы восстановления.

**Source/context:** Program / service intros emphasizing individualized route (not a copy of local service cards).

### Card 2

**Title:** Понятная диагностика  

**Text:** Мы помогаем разобраться, что происходит на уровне состояния и возможных биологических особенностей, чтобы дальше опираться на факты, а не на догадки. Диагностика — инструмент понимания, а не приговор.

**Source/context:** Genotyping + diagnostics editorial language on live site (restrained medical tone).

### Card 3

**Title:** Работа с причинами  

**Text:** В процессе учитываем не только внешние проявления, но и то, что стоит за запросом: тревогу, привычные реакции, триггеры и контекст жизни. Цель — устойчивые изменения, а не только краткий перерыв в симптомах.

**Source/context:** Site themes around causes/triggers / psychocorrection without cure guarantees.

### Card 4

**Title:** Команда специалистов  

**Text:** В центре рядом работают специалисты разных профилей. Маршрут согласовывается спокойно и без осуждения, чтобы человеку и близким было понятно, кто за что отвечает и как строится поддержка.

**Source/context:** Multidisciplinary approach copy used across approach sections.

### Card 5

**Title:** Поддержка на всём пути  

**Text:** Помогаем выстроить сопровождение на разных этапах — от первого разговора до восстановления в повседневной жизни. При согласии человека близкие могут получить понятные ориентиры, как помогать без давления.

**Source/context:** Support / family involvement themes already present in project content.

---

## 9. Final precedence

```text
APPROACH CARDS:

SECTION / BLOCK OFF
  → hidden (no reusable override)

SECTION / BLOCK ON + LOCAL CARDS NON-EMPTY
  → local cards exactly

SECTION / BLOCK ON + LOCAL CARDS EMPTY
  → reusable/global approach cards

LOCAL EDITORIAL VALUES ARE NEVER AUTOMATICALLY OVERWRITTEN BY GLOBAL DEFAULTS.
```

Card-level only — heading/lead/media stay local-owned.

---

## 10. Implementation

| File | Change |
|------|--------|
| `plugins/.../Admin/OptionsPage.php` | New reusable subpage `fp02-block-approach-cards` |
| `plugins/.../Fields/FieldGroups.php` | `block_approach_cards()` field group |
| `plugins/.../Fields/ServiceSectionParity.php` | Admin notices / card instructions |
| `plugins/.../Fields/ServiceGeneralParity.php` | Admin notices / card instructions |
| `theme/.../inc/reusable-blocks-helpers.php` | `shpigovsky_get_reusable_approach_cards()` |
| `theme/.../inc/service-section-helpers.php` | `shpigovsky_get_effective_service_approach_cards()` + normalize helper |
| `theme/.../inc/service-general-helpers.php` | Card-level reusable integration in `shpigovsky_get_general_approach_copy()` |
| `theme/.../template-parts/service/team-stats.php` | Uses effective resolver |

Not touched: child-card PHP/CSS, stages Comfort Requirements owner, SEO/OG/Schema/robots/indexing.

---

## 11. Genotyping QA

- Local 4 cards unchanged (titles: Диагностические инструменты / Психиатрия / Функциональная терапия / Комплементарная терапия).
- Effective `source=local`; FE titles match before/after.
- Global reusable not mixed in while local exists.
- Evidence: `seed-report.json`, `frontend-after.json`, `qa-summary.json`

---

## 12. Reusable fallback QA

- Reusable options: 5 cards seeded (`after_count=5`).
- Precedence simulation: empty local → `source=reusable` with global titles (`fallback-off-qa.json`).
- No live LOCAL_EMPTY fixture existed; non-persistent composition proof used (no DB wipe of local cards).

---

## 13. OFF-toggle QA

- Live OFF fixture for approach: **not found**.
- Code: `subdivision-stack.php` loads `team-stats` only when `shpigovsky_section_block_enabled(..., 'section_approach_visible')`; helper treats meta `0` as OFF. OFF does not invoke reusable as a visibility bypass.

---

## 14. Responsive QA

- Desktop HTML: 4 approach cards present on geno.
- Mobile (~390): approach region present in a11y tree with card titles/texts; long card paragraphs wrap without empty giant cells / duplicate blocks.
- No visual redesign performed.

---

## 15. Regression QA

| Area | Result |
|------|--------|
| Stages reusable fallback | `source=reusable_requirements` on geno — healthy |
| Child-card multi-image files | **UNTOUCHED** (prod still matches multi worktree) |
| SEO / OG / Schema | Present on geno after deploy |
| Robots | Read-only capture; unchanged |
| Indexing | OPEN — no mutation |

---

## 16. Olya/editorial preservation

- No local `section_approach_cards` / `service_general_approach_cards` writes.
- Only new options field `reusable_approach_cards` written.
- Genotyping local titles/texts preserved.

---

## 17. Production parity

Exact deployed files MATCH worktree source (SHA) — see `deploy-report.json`.

---

## 18. Backup / rollback

- Layer-B before: `...\prod-maint-service-approach-cards-reusable-fallback-01\prod-before\`
- Layer-B after: `...\prod-maint-service-approach-cards-reusable-fallback-01\prod-after\`
- Options pre-state: `options-pre-state.json` (`reusable_approach_cards: null`)
- Options after: `options-after-state.json`
- Rollback = exact-file restore of 8 files + restore options field to empty/null. **No broad DB restore.**

---

## 19. Robots / indexing

- Robots: Olya-owned physical file — read-only evidence only.
- Indexing: OPEN — no mutation.

---

## 20. Git

Selective paths only (this wave). Pending multi-image theme files **NOT staged**.

---

## 21. Active pending wave preservation

```text
MULTI-IMAGE WORKTREE = PRESERVED
MULTI-IMAGE BRANCH = PRESERVED
MULTI-IMAGE UNCOMMITTED DELTA = PRESERVED
```

---

## 22. Documentation / agent knowledge

- This report
- `PROJECT-STATUS.md` updated
- `FP-0002-NEXT-WEBGPT-HANDOFF.md` updated
- Forge: stages wave already documents global default + local override + explicit OFF — **NO NEW HARVEST**

---

## 23. Residuals

1. Placeholder-layout services still expose approach Admin fields without FE render — UX clarity residual (documented in Admin helper text).
2. No live LOCAL_EMPTY / SECTION_OFF fixtures; proven via code + non-persistent composition.
3. Pending multi-image composition remains uncommitted (by design).

---

## 24. Mutation statement

- **Production files changed:** 8 theme/plugin files listed in §10.
- **Reusable/global option values written:** `reusable_approach_cards` (5 cards) on `fp02-block-approach-cards`.
- **Local service `Карточки подхода` records NOT overwritten.**
- **No robots/indexing mutation.**
- **Pending child-card wave untouched.**
