# REPORT — FP-0002 SERVICE STAGES REUSABLE-BLOCK FALLBACK REPAIR 01

**Date:** 2026-09-14  
**Verdict:** **PASS**  
**Production URL (primary QA):** `https://shpigovsky.ru/uslugi/genotipirovenie/`  
**Canonical origin at wave start:** `99860fd2ae1a1c238d4ba56fb5f7b8ebd61105e0`

---

## 1. Verdict

**PASS**

Reusable Comfort Requirements content now renders on genotyping when the section stages block is ON and local section fields are empty. Local override and OFF semantics preserved. Pending multi-image child-card production delta untouched.

---

## 2. Current source-state topology

| Surface | State |
|--------|--------|
| `origin/mars/canonical-post-recovery` (fetched) | `99860fd2` at wave start |
| This repair worktree | `X:\AI MARS STORAGE\worktrees\fp0002-service-stages-reusable-fallback-01` |
| This repair branch | `wave/fp0002-service-stages-reusable-fallback-01` |
| Pending multi-image worktree | `X:\AI MARS STORAGE\worktrees\fp0002-service-child-cards-multi-image-02` — **PRESERVED** |
| Pending multi-image branch | `wave/fp0002-service-child-cards-multi-image-02` — **PRESERVED** |
| Production deltas not on origin | `child-services.php` + `service-child-services.css` (multi-image wave) |

---

## 3. Fresh production intake

Layer-B baselines:  
`X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-maint-service-stages-reusable-fallback-01\prod-before\`

Confirmed before edit:

- Theme helpers/templates for stages path matched origin (safe edit base).
- `ServiceSectionParity.php` matched origin (Admin notice patch OK).
- `ServiceGeneralParity.php` **DIFFERS** from origin → **not mutated** (avoid overwriting live plugin drift).
- Child-card files: production == multi-image worktree (`1d3e6e1fbd11` / `c43df6f43af2`); origin differs — left alone.

---

## 4. Root cause

1. Live genotyping (`#1889`, slug `genotipirovenie`) uses layout **`subdivision`**.
2. Admin block **«6. Этапы / что нужно для лечения»** is **section** ACF (`section_stages_*`), owned by `ServiceSectionParity` — not `service_general_stages_*`.
3. Operator-visible post ID `1898` is a **revision** of a child service, not the genotyping parent. Live parent ID = **1889**.
4. Subdivision render path:
   - `subdivision-stack.php` gates on `section_stages_visible`
   - `stages.php` loaded section fields via `shpigovsky_get_section_stages_items()` / section scalars
   - Empty local → early return; fallback only to legacy Structured `stages` repeater, **never** to reusable Comfort Requirements (`rehab_requirements_*` / `fp02-block-comfort-requirements`)
5. Separately, service-general path (`shpigovsky_get_general_stages_copy`) also lacked reusable fallback (alcohol emergency only). Fixed in the same wave for completeness.

---

## 5. Local block data owner (genotyping `#1889`)

| Field label | Meta / field name | Current genotyping value |
|-------------|-------------------|--------------------------|
| Показывать блок этапов | `section_stages_visible` | `1` (ON) |
| Заголовок этапов | `section_stages_heading` | empty |
| Лид этапов | `section_stages_lead` | empty |
| Этапы (repeater) | `section_stages_items` | empty (0 rows) |
| Заголовок поддержки | `section_stages_support_heading` | empty |
| Пункты поддержки | `section_stages_support_items` | empty (0 rows) |

Evidence: `REPORTS/evidence/prod-maint-service-stages-reusable-fallback-01/resolver-probe-section.json`

---

## 6. Reusable block owner

| Item | Value |
|------|--------|
| Admin | `Настройки сайта → Повторяемые блоки → Comfort Requirements` |
| Page slug | `admin.php?page=fp02-block-comfort-requirements` |
| Options context | `fp02-block-comfort` (`shpigovsky_get_comfort_block_context()`) |
| Fields | `rehab_requirements_heading`, `rehab_requirements_intro`, `rehab_requirements_steps` (`step_title`/`step_text`), `rehab_requirements_support_heading`, `rehab_requirements_support_items`, plus CTA/photo fields used on home |
| Helpers | `shpigovsky_get_rehab_requirements_*` in `inc/reusable-blocks-helpers.php` |
| New bridge | `shpigovsky_get_stages_copy_from_reusable_requirements()` |

---

## 7. Semantic mapping

| Local (section / general) | Reusable / default | Frontend model |
|---------------------------|--------------------|----------------|
| `*_stages_heading` | `rehab_requirements_heading` | `heading` |
| `*_stages_lead` | `rehab_requirements_intro` | `lead` |
| `*_stages_items` | `rehab_requirements_steps` | `steps[]` (`title`/`text`) |
| `*_stages_support_heading` | `rehab_requirements_support_heading` | `support_heading` |
| `*_stages_support_items` | `rehab_requirements_support_items` | `support_items[]` |
| Guest Visit CTA (service templates) | *(not remapped; stays guest CTA band)* | CTA component |
| Photo | home-only `rehab_requirements_photo*` | not used on service stages template |

Fallback mode: **block-level** when local empty; **field-level fill from reusable** when local has some meaningful values.

---

## 8. Final precedence

```text
OFF (section_stages_visible / service_general_stages_visible = 0)
  → render nothing (no reusable fallback)

ON + local meaningful content
  → local owner (empty fields may fill from reusable)

ON + local empty
  → reusable Comfort Requirements

(last resort) alcohol-only theme emergency remains behind reusable on service-general path only
```

---

## 9. Implementation

| File | Change |
|------|--------|
| `theme/.../inc/service-general-helpers.php` | `shpigovsky_get_stages_copy_from_reusable_requirements()` + reusable fallback in `shpigovsky_get_general_stages_copy()` |
| `theme/.../inc/service-section-helpers.php` | `shpigovsky_get_section_stages_copy()`; reusable step in `shpigovsky_get_section_stages_items()` |
| `theme/.../template-parts/service/stages.php` | Subdivision branch renders resolved section model |
| `plugins/.../Fields/ServiceSectionParity.php` | Admin notice documents OFF / local / reusable precedence |

Not touched: child-card files, SEO/OG/Schema, robots, indexing.

---

## 10. Genotyping QA

- Local section fields remain empty (probe).
- Frontend shows reusable heading/steps/support (`service-subdivision-stages`).
- Source = `reusable_requirements`.
- URL note: live slug is `genotipirovenie` (not `genotipirovanie`).

---

## 11. Local override QA

- Request-scoped `acf/pre_load_value` on genotyping → `source=local`, heading/lead/support = QA strings (no DB write).
- Live alcohol service `#74` → `shpigovsky_get_general_stages_copy` `source=local`; FE leaf stages present.
- No live subdivision currently has filled `section_stages_items` (fixture unavailable); section local override proven via non-persistent filter.

---

## 12. OFF-toggle QA

- Live fixture with `section_stages_visible=0` **not found**.
- Proven by code: `subdivision-stack.php` skips `stages` when `shpigovsky_section_block_enabled(..., 'section_stages_visible')` is false; helper treats meta `0` as OFF. OFF does not call reusable resolver.

---

## 13. Cross-service QA

| Service | Path | Result |
|---------|------|--------|
| Genotyping `#1889` | subdivision ON + empty local | reusable renders |
| Alcohol `#74` | service-general + local | local wins |
| Home | reusable block | still renders requirements |

---

## 14. Regression QA

- Child-card production hashes still match multi-image worktree — **UNTOUCHED**
- SEO robots meta / OG / Schema present on geno page after fix
- `/robots.txt` Olya policy unchanged (read-only capture)
- Indexing remains OPEN (no mutation)
- Mobile (390px): stages block present, 4 steps, support visible

---

## 15. Production parity

Exact deployed files MATCH worktree source (SHA):

- `service-general-helpers.php` `3b64286bfc1c…`
- `service-section-helpers.php` `567d7c7d0647…`
- `stages.php` `1b79eba7be3a…`
- `ServiceSectionParity.php` `20b1f26cc34c…`

---

## 16. Backup / rollback

- Layer-B before: `...\prod-maint-service-stages-reusable-fallback-01\prod-before\`
- Layer-B after: `...\prod-maint-service-stages-reusable-fallback-01\prod-after\`
- Rollback = exact-file restore of the four files from `prod-before` (theme/plugin only). **No DB rollback.**

---

## 17. Robots / indexing

- Robots: Olya-owned physical file unchanged (read-only evidence).
- Indexing: OPEN — no mutation.

---

## 18. Git

- Commit: `39e9cd4e1bf930e5858ea0e9665e23e8b5a0cb7c`
- Pushed to: `origin/mars/canonical-post-recovery`
- Message: `fix(fp0002): restore stages reusable Comfort Requirements fallback`
- Staged paths: this repair’s theme/plugin files + report/handoff/PROJECT-STATUS + evidence JSON/PNG only
- Pending multi-image files **not** staged

---

## 19. Active pending wave preservation

```text
MULTI-IMAGE WORKTREE = PRESERVED
MULTI-IMAGE BRANCH = PRESERVED
MULTI-IMAGE UNCOMMITTED CHANGES = PRESERVED
PRODUCTION MULTI-IMAGE DELTA = UNTOUCHED
```

---

## 20. Documentation / agent knowledge

Precedence rule recorded in this report, `PROJECT-STATUS.md`, and `FP-0002-NEXT-WEBGPT-HANDOFF.md`.

**Future-agent rule:**

```text
SERVICE STAGES BLOCK
OFF → hidden
ON + local meaningful → local
ON + local empty → reusable Comfort Requirements (fp02-block-comfort-requirements)
```

Subdivision Admin label «6. Этапы…» = `section_stages_*`.  
Service-general Admin stages = `service_general_stages_*`.

---

## 21. Residuals

- No live OFF fixture for section stages.
- No live subdivision with filled local stages (override proven via request-scoped filter).
- `ServiceGeneralParity.php` production drift left intact (notice text there not updated).
- Pending multi-image wave still uncommitted (by design).

---

## 22. Mutation statement

**Production files changed:**

1. `wp-content/themes/shpigovsky/inc/service-general-helpers.php`
2. `wp-content/themes/shpigovsky/inc/service-section-helpers.php`
3. `wp-content/themes/shpigovsky/template-parts/service/stages.php`
4. `wp-content/plugins/shpigovsky-core/src/Fields/ServiceSectionParity.php` (Admin help text only)

```text
NO SERVICE EDITORIAL CONTENT DUPLICATED.
NO ROBOTS/INDEXING MUTATION.
NO CHILD-CARD WAVE MUTATION.
FOREIGN WIP PRESERVED.
```
