# REPORT — FOUNDRY SYSTEM-WIDE LAYER AUDIT

**Дата:** 2026-06-19  
**Режим:** аудит только — исходные документы **не изменялись**  
**Область:** Website Factory / FOUNDRY — все слои кроме детального re-audit Registry Layer (см. [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md))  
**Контекст:** WF-A01 и WF-A02 **Complete**; WF-A03 **DEFERRED**

**Терминология:** строка **FOUNDRY** в репозитории **не найдена** как отдельный продукт или путь. В этом отчёте **FOUNDRY** = **Website Factory** (`projects/mars-website-factory/`, `workspaces/website-factory-reference-v1/`, `workspaces/website-factory-operations/`). См. SAFE UNKNOWN.

**Честная граница:** Phase 1 MARS — **documentation-first**, human-operated Cursor execution. **Нет** factory runtime, orchestration engine, autonomous agents, machine-enforced validation в repo.

---

## Executive Summary

Website Factory / FOUNDRY — **зрелая документированная методология** с **сильным frontend production и validation governance**, **сильной registry/blueprint архитектурой** (Foundation v1 freeze), и **слабой implementation-зрелостью** на upstream-слоях (Strategy, UX/Wireframe, Design tokens) и **системным v0↔v1 drift**.

| Паттерн | Оценка |
|---------|--------|
| **Архитектурная глубина** | **Высокая** — layer-map, workflow v0, charters WF-A01/A02, reference-v1 foundation stack |
| **Операционная зрелость** | **Средняя** — Triumph v6, ISBD, reference workspace, FP-0001 LOC-ZONE; adoption неравномерен |
| **Implementation readiness** | **Низкая–средняя** — registry/blueprint опережают код (~31% block partials); upstream agents **planned** |
| **False confidence risk** | **Высокий** — ACCEPTED/Foundation labels читаются как «готово к production-scale»; FP-0002 forensic доказал false-green при BUILT |

**Главный системный вывод:** FOUNDRY — **operational methodology + governance spine**, **не** end-to-end automated website factory. Сильнейшие слои: **Frontend Production**, **Validation/QA (documentation)**, **Registry/Blueprint (architecture)**. Слабейшие: **UX/Wireframe**, **Commercial Pattern Library**, **SEO content layer**, **Agent runtime**.

**Приоритет после Registry Audit:** targeted **Registry Expansion + v0→v1 binding** и **VL3 adoption in live projects** важнее WF-A03, пока primary bottleneck — structural vocabulary и composition truth, а не pixel automation alone.

---

## Layer Maturity Matrix

| Layer | Maturity (0–10) | Doc depth | Operational readiness | Implementation readiness | Drift / conflict | Critical gap (one line) |
|-------|-----------------|-----------|----------------------|------------------------|------------------|-------------------------|
| Strategy | **3** | Medium–High (governance) | Low | Low | v0 site types in agent cards | No strategy artifact SSOT; Commercial Pattern ≈1 pattern |
| SEO | **5** | High (arch v2) / Absent (pattern lib) | Medium (planning) | Low | registries.md §4 vs seo-architecture v2 | No title/meta/schema templates; no SEO QA runtime |
| IA / Page Architecture | **7** | High (v1) | Medium–High | Medium | workflow v0 → v0 contracts | Extended types + ECOMMERCE utility pages shallow |
| UX / Wireframe | **2** | Low–Medium (governance only) | Very Low | Very Low | design-layer-model format TBD | No wireframe SSOT, no UX artifact library |
| Design | **6** | High (architecture) | Medium | Low | DS-R07: no visual tokens in canon | Architecture-only design system; gaps DG-01–DG-20 open |
| Frontend Production | **8** | Very High | High | Medium–High | v0 block names in ops Wave 4–6 | Registry 29 blocks vs 9 reference partials |
| Validation / QA | **7** | Very High | Medium–High | Low (human only) | Compact QA vs Production PASS confusion | No automated VL gates; WF-A03 deferred |
| Agent | **3** | High (cards) | Low (2 packs only) | Very Low | 16 planned vs 2 operational_doc_pack | No specialist agent execution path |
| Workflow | **6** | Very High | Medium–High | Low | workflow v0 cites v0 registries | Human-only; phases 6–7 unmet dependencies |
| LOC-ZONE / Operations | **5** | Medium–High | Medium | Medium | FP-0002 not ROC-enrolled | Passport adoption partial; not all cases in LOC-ZONE |
| Execution Cases | **5** | Medium | Medium | Mixed | BZPM no workspace | Cases feed lessons unevenly into canon |
| Knowledge / Source Pack | **7** | High | High | N/A | legacy web-gpt-sources vs sync pack | Project chats need manual lane add-ons |

---

## Strategy Layer

### Current maturity: **3 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Medium–High** для governance: [strategic-intent-governance.md](../projects/mars-website-factory/strategic-intent-governance.md), [commercial-density-governance.md](../projects/mars-website-factory/commercial-density-governance.md), [cta-philosophy-governance.md](../projects/mars-website-factory/cta-philosophy-governance.md), [business-intent-continuity-model.md](../projects/mars-website-factory/business-intent-continuity-model.md). **Низкая** для executable strategy artifacts (memo templates, CTA matrices per site type). |
| **Operational readiness** | **Low** — Forge [strategic-intent-checklist.md](../agents/mars-forge/strategic-intent-checklist.md) exists; **Marketing Strategy Agent** status **planned**; workflow stage `WF_V0_S03_STRATEGY` documented but **не** operationalized как обязательный artifact chain в live projects. |
| **Implementation readiness** | **Low** — нет strategy memo SSOT, нет conversion pattern catalog (см. Registry Audit: Commercial Pattern Library **~5%**). |
| **Drift / conflict** | Agent cards ссылаются на [site-type-registry-v0.md](../projects/mars-website-factory/site-type-registry-v0.md); канон v1 — `SITE-TYPE-REGISTRY-v1.md`. [registries.md](../projects/mars-website-factory/registries.md) §3 заявляет Commercial Pattern **delivered** при фактически **одном** `scroll_process_timeline`. |
| **Critical gaps** | Коммерческая стратегия и CTA logic **декларативны** в governance; segmentation и offer logic **не** привязаны к blueprint fields machine-readable; conversion QA **planned**. |

### Recommended action

**Priority B:** Strategy artifact slice — минимальный `strategy-memo-contract-v1` (documentation) с полями: positioning, primary CTA, proof hierarchy, segment notes; bind к Blueprint `conversion_requirements`. **Не** расширять governance wave без charter.

---

## SEO Layer

### Current maturity: **5 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **High** для architecture: `workspaces/website-factory-reference-v1/seo-architecture/` — SEO Architecture Layer v2 **ACCEPTED** (intent model, page contracts, matrices, implementation rules). **Absent** как отдельный модуль: **SEO Pattern Library** из [registries.md](../projects/mars-website-factory/registries.md) §4. |
| **Operational readiness** | **Medium** для planning — operator может заполнить PAGE-SEO-CONTRACT из v2 mapping; [ru-landing-qa-preset-v1.md](../projects/mars-website-factory/ru-landing-qa-preset-v1.md) для RU commercial QA. **SEO QA Agent** — **planned**. |
| **Implementation readiness** | **Low** — нет title/meta/H1 **templates** (SEO-ARCHITECTURE-GAPS); нет keyword architecture; faceted SEO **FUTURE**; automated schema validation **не evidenced**. |
| **Drift / conflict** | [seo-marketing-layer.md](../projects/mars-website-factory/seo-marketing-layer.md) всё ещё ссылается на **SEO Pattern Library**; [page-blueprint-contract-v0.md](../projects/mars-website-factory/page-blueprint-contract-v0.md) — «SEO Pattern Library (planned)». Канон фактический — **seo-architecture v2**. |
| **Critical gaps** | Meta/title/H1 logic **архитектурно** задана, **контентно** не доставлена; internal linking — intent-level only; page intent mapping **сильная** на уровне matrices, **слабая** на generation. |

### Recommended action

**Priority A (binding):** Обновить operational cross-links **только по explicit charter** — seo-marketing-layer и workflow должны указывать на seo-architecture v2, не на absent Pattern Library.  
**Priority B:** SEO content pattern slice — title/description formula templates per `page_type` (documentation only).

---

## IA / Page Architecture Layer

### Current maturity: **7 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **High** — `page-architecture/PAGE-TYPE-REGISTRY-v1.md` (10 types + ECOMMERCE utility), Core 5 Blueprints **ACCEPTED**, PAGE-BLOCK-VALIDATION, SITE-TYPE-PAGE-MATRIX. |
| **Operational readiness** | **Medium–High** — blueprint selection human-operable для Core 5; FP-0002 имеет PAGE-INVENTORY; Triumph V6 rollout plan. |
| **Implementation readiness** | **Medium** — LANDING battle-tested; PROMO/CATALOG/ECOMMERCE/CORPORATE **partial** (Registry Audit); нет `project.blueprint.yaml` machine schema. |
| **Drift / conflict** | [website-factory-workflow-v0.md](../projects/mars-website-factory/website-factory-workflow-v0.md) и [page-blueprint-contract-v0.md](../projects/mars-website-factory/page-blueprint-contract-v0.md) — **v0**, snake_case, v0 registries. Канон v1 — `website-factory-reference-v1/blueprints/`. |
| **Critical gaps** | Route/page type logic **документирована**, **не** автоматизирована; Extended site types без blueprints; HEADER_NAV/FILTERS/SEARCH missing from block registry (blocks IA completeness). |

### Recommended action

**Priority A:** v0→v1 operational binding для новых задач (см. Registry Audit).  
**Priority B:** Blueprint machine schema documentation (`project.blueprint.yaml`).

---

## UX / Wireframe Layer

### Current maturity: **2 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Low–Medium** — [design-layer-model.md](../projects/mars-website-factory/design-layer-model.md) описывает sub-stages; [interaction-intent-governance.md](../projects/mars-website-factory/interaction-intent-governance.md) богатая governance. **Нет** wireframe artifact standard, section sequencing contract, user journey maps SSOT. |
| **Operational readiness** | **Very Low** — Wireframe Generator / UX Structure agents **planned**; workflow-map включает Wireframe stage, но **формат TBD** (markdown/YAML/Figma export — SAFE UNKNOWN). |
| **Implementation readiness** | **Very Low** — нет wireframe library, нет interaction contracts per block_id, нет journey templates. FP-0002 использует Group Decomposition / Layout Spec как **замену** wireframe discipline для PIXEL_PERFECT — не универсальный UX слой. |
| **Drift / conflict** | Layer-map §4 объединяет UX+Design; validation charter VL2 потребляет FIG/wireframe SSOT без единого wireframe canon. |
| **Critical gaps** | **Implementation cliff** между blueprint и design — для TEMPLATE_ART нет обязательного wireframe gate; UX patterns **декларативны**. |

### Recommended action

**Priority C:** Wireframe artifact contract v1 (markdown-first section map + responsive intent notes) — **после** registry binding.  
**Не** запускать WF-A03 как substitute.

---

## Design Layer

### Current maturity: **6 / 10** (architecture) / **3 / 10** (visual implementation kit)

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **High** для architecture — `design-system/` ACCEPTED: DESIGN-SYSTEM-RULES, VISUAL-PATTERN-REGISTRY (~40 VF_* families), BLOCK-VISUAL-MAPPING, DESIGN-SYSTEM-GAPS. [design-governance-layer.md](../projects/mars-website-factory/design-governance-layer.md) + Canonical Implementation Pack. **DS-R07:** colors/typography/CSS **forbidden** in Design Layer v1 artifacts — architecture only. |
| **Operational readiness** | **Medium** — Production Standards Governance, Mapping QA, Design Calibration chain **operational** на FP-0002/Triumph path; Forge design checklists. |
| **Implementation readiness** | **Low** — DESIGN-SYSTEM-GAPS DG-01–DG-04 (tokens, color, typography, components) **OPEN**; нет Figma kit/CSS token export в canon; reference partials ≠ full pattern library. |
| **Drift / conflict** | [registries.md](../projects/mars-website-factory/registries.md) §5 Design System Rules — **planned** table; фактический канон — reference-v1 design-system. Visual Pattern Registry ≠ Commercial Pattern Library. |
| **Critical gaps** | Design system rules **сильные** как **constraints**; visual direction / brand consistency **project-local** (FP-0002 numeric rules); image/asset rules в Mapping Governance, не в central design tokens. |

### Recommended action

**Priority B:** Design token charter (DG-01) — documentation slice only, bind к `_tokens.scss` foundation pattern.  
**Priority A (PIXEL):** Продолжать Design Governance Pack path — уже operational; не смешивать с Template-Art block defaults.

---

## Frontend Production Layer

### Current maturity: **8 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Very High** — Waves 1–6, Enforcement Pack, Authority Order, Foundation systems, 30+ frontend governance docs; [OPERATIONAL-INDEX.md](../projects/mars-website-factory/OPERATIONAL-INDEX.md) routing mature. |
| **Operational readiness** | **High** — `gulp_frontend_agent` + `mars_forge_frontend_agent` **operational_doc_pack**; workspaces: reference-v1, triumph-manipulator-landing-v6, isbd-care-landing, _template-client-v1; onboarding-flow v1. |
| **Implementation readiness** | **Medium–High** для LANDING subset; **Low** для full registry coverage (9/29 partials). Build pipeline **exists** in workspaces (Gulp); **не** in mars-website-factory doc pack alone. |
| **Drift / conflict** | [curated-library-index-v1.md](../projects/mars-website-factory/curated-library-index-v1.md) / [block-quality-tiers-v1.md](../projects/mars-website-factory/block-quality-tiers-v1.md) — v0 `block_id`. workflow v0 → Frontend Handoff v0. |
| **Critical gaps** | Component implementation maturity **неравномерна**; production handoff **сильный** (charters, VL3, shell-first); CATALOG/ECOMMERCE structural blocks absent. |

### Recommended action

**Priority A:** Reference implementation expansion (минимум PROMO money-page subset) **или** explicit LANDING-only Template-Art policy.  
**Priority A:** Registry v1.1 structural blocks charter.

---

## Validation / QA Layer

### Current maturity: **7 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Very High** — WF-A01 Production Modes **Complete**; WF-A02 Validation Architecture + VL3 Domains **Complete**; operational-qa-entry, frontend-qa-reporting-standard, pixel-fidelity, compliance/failure attribution models. |
| **Operational readiness** | **Medium–High** — VL0–VL6 human chain documented; BUILT/VERIFIED/PRODUCTION PASS taxonomy; RU landing preset; FP-0002 spawned VL3 failure registry. **Adoption gap:** operators may use **compact pass** and claim green without Production PASS chain. |
| **Implementation readiness** | **Low** — **not** runtime, **not** CI, **not** Vision/Visual Diff (WF-A03 **DEFERRED**). Project-local scripts (FP-0002 `_fig_parse_temp`) — isolated, not Factory product. |
| **Drift / conflict** | [validation-runtime-overview-v0.md](../projects/mars-website-factory/validation-runtime-overview-v0.md) (Phase 4) vs WF-A02 charter — newer charter **supersedes** for Factory frontend; naming «runtime» misleading. Layer-map §6 QA agents **planned** vs rich human QA docs **operational**. |
| **Critical gaps** | False-green closure **documented** post-FP-0002; **не** machine-enforced. SEO QA / Conversion QA / Design QA agents **planned**. VL3 domains **strong on paper** — adoption in Triumph/ISBD **SAFE UNKNOWN** without per-project REPORT audit. |

### Recommended action

**Priority A:** Operator discipline — Production PASS requires full gate chain per mode; REPORT Layer F mandatory.  
**Priority C:** WF-A03 только после Research Pass **и** если bottleneck = visual verification, не composition.

---

## Agent Layer

### Current maturity: **3 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **High** — 18 cards in [agents/cards/](../agents/cards/); [agent-map.md](../projects/mars-website-factory/agent-map.md); registry §4.1 complete roster. |
| **Operational readiness** | **Low** — только **`gulp_frontend_agent`** и **`mars_forge_frontend_agent`** = **operational_doc_pack** (human + Cursor). Остальные 16 factory agents = **planned**. |
| **Implementation readiness** | **Very Low** — нет agent runtime, Control Plane routing, Task automation. Validator Agent integration **planned**. |
| **Drift / conflict** | Design Governance Agent vs AI Designer vs Full Design Generator — роли **перекрываются** на paper; Forge partially absorbs frontend QA sequencing. Duplicate naming: Gulp Frontend Agent (§4) vs `gulp_frontend_agent` (§4.1) — same role, different ids. |
| **Critical gaps** | Intake → Strategy → IA → Blueprint → Design agents **не детализированы** beyond v0 cards; **нет** operational playbooks per agent except frontend/forge. |

### Recommended action

**Priority B:** Agent operational status matrix — какие stages **сегодня** выполняет human under which card (honesty doc).  
**Не** создавать новые agent systems.

---

## Workflow Layer

### Current maturity: **6 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Very High** — [website-factory-workflow-v0.md](../projects/mars-website-factory/website-factory-workflow-v0.md) (10 stages), [workflow-map.md](../projects/mars-website-factory/workflow-map.md), [first-operational-runbook-v0.md](../projects/mars-website-factory/first-operational-runbook-v0.md), execution semantics Phase 4 stack, artifact bus, reference project layer. |
| **Operational readiness** | **Medium–High** — [onboarding-flow-v1.md](../projects/mars-website-factory/onboarding-flow-v1.md) paths A/B/C; handoff contracts v0; HITL gates G1–G7; Triumph reference case walkthrough. |
| **Implementation readiness** | **Low** — phases 6–7 roadmap (runtime-assisted, automation) **depend on unmet** MARS runtime. Cursor execution **operational** per [execution-model.md](../governance/execution-model.md). |
| **Drift / conflict** | Workflow v0 registry references **v0** site/block registries; OPERATIONAL-INDEX points to **v1** reference-v1 for architecture. Intake step 0 (production mode) **added** post WF-A01 — не все legacy runbooks обновлены inline. |
| **Critical gaps** | Handoff points **documented**; **не** machine-routed. Report closeout [reporting-standard-v0.md](../projects/mars-website-factory/reporting-standard-v0.md) operational; release/delivery **human**. |

### Recommended action

**Priority A:** Single workflow registry binding note — «new work uses reference-v1 canon» (charter, not silent edit).  
**Priority B:** Reference run sequence alignment check vs WF-A01/A02 gates.

---

## LOC-ZONE / Operations Layer

### Current maturity: **5 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Medium–High** — [workspaces/website-factory-operations/README.md](../workspaces/website-factory-operations/README.md), [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../workspaces/website-factory-operations/FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md), ROC-01 catalog, MOC/SOC manifest pattern, Waves 1–3 execution records. |
| **Operational readiness** | **Medium** — FP-0001 **ROC-enrolled**, FACTORY_TRACK_CLOSED_PARTIAL; FP-0002 **visibility-only**, rich artifacts but **not** catalog-enrolled; passport `production_mode` on FP-0002 **retroactive**. |
| **Implementation readiness** | **Medium** — physical artifact substrate proven (C2–C7 on FP-0001); **не** automated passport generator; validation fields **optional** in passport. |
| **Drift / conflict** | [execution-cases-registry-v1.md](../projects/mars-website-factory/execution-cases-registry-v1.md) cases ≠ all LOC-ZONE FP rows (ISBD, BZPM not FP-XXXX enrolled). Doctrine in reference-v1; records in LOC-ZONE — **correct split**, but operator confusion risk. |
| **Critical gaps** | Project records **partial** portfolio coverage; workspace relationship **documented** for FP-0001/0002; Triumph v6 **outside** LOC-ZONE enrollment. |

### Recommended action

**Priority B:** FP-0002 enrollment decision or explicit «learning-only» charter.  
**Priority B:** Align execution-cases-registry rows with LOC-ZONE visibility policy.

---

## Execution Cases Layer

### Current maturity: **5 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **Medium** — [execution-cases-registry-v1.md](../projects/mars-website-factory/execution-cases-registry-v1.md) (3 cases); reference case overviews; FP-0001/0002 LOC packs extensive. |
| **Operational readiness** | **Medium** — mixed evidence types. |
| **Implementation readiness** | **Mixed** by case. |

### Per-case assessment

| Case | Role | Feeds FOUNDRY? | Maturity notes |
|------|------|----------------|----------------|
| **Triumph** (`triumph-manipulator-landing`) | Reference case #1 + **active client** v6 workspace | **Да** — block extractions (faq, pricing, cases), scroll_process_timeline, RU QA preset, Forge battle-tests | **Highest** live implementation evidence; **не** full Factory pipeline automation |
| **ISBD** (`isbd-care-landing`) | Client delivery #2 | **Частично** — adoption/freeze pattern; WPilot follow-on planned | Workspace exists; Factory canon binding **lighter** than Triumph |
| **BZPM** (`bzpm-catalog-redesign`) | Client delivery #3, research complete | **Слабо** — audit consolidation only | Workspace **SAFE UNKNOWN**; W3 blueprint pending — **Concept / research** |
| **FP-0001** (Triumph LOC) | LOC-ZONE enrolled pilot | **Да** — manifest/MOC/SOC playbook | **FACTORY_TRACK_CLOSED_PARTIAL** — substrate proof, not full site generation |
| **FP-0002** (Shpigovsky) | PIXEL_PERFECT stress test | **Да — высокий** — VL3 domains, production modes, Group/Layout laws, failure classes, forensic lessons | **Negative evidence** valuable: false-green, generative fill, asset collision — **питает charters**, не success story |

### Critical gaps

Кейсы **не** нормализованы в единый «case → layer maturity» feed; BZPM не замыкает loop; Triumph v6 authority **parallel** to FP-0001 LOC home.

### Recommended action

**Priority B:** Execution case → layer lesson index (documentation table, no new system).  
**Priority A:** Apply FP-0002 lessons in next PIXEL_PERFECT runs (VL3 mandatory).

---

## Knowledge / Source Pack Layer

### Current maturity: **7 / 10**

| Dimension | Assessment |
|-----------|------------|
| **Documentation depth** | **High** — [web-gpt-sources/mars-v2-stable-baseline-2026-06-sync/](../web-gpt-sources/mars-v2-stable-baseline-2026-06-sync/) (12-file upload order), WEB-GPT-CHAT-SYNC-PACK, [08_SYSTEM_MATURITY_MAP.md](../web-gpt-sources/mars-v2-stable-baseline-2026-06-sync/08_SYSTEM_MATURITY_MAP.md). |
| **Operational readiness** | **High** for ecosystem bootstrap; OPERATIONAL-INDEX Tier 2 routing; lane-specific add-ons documented. |
| **Implementation readiness** | N/A (knowledge layer). |
| **Drift / conflict** | Legacy numbered `web-gpt-sources/01_*.md` — **historical**; sync pack supersedes for upload. Two baseline folders (2026-06 vs sync) — operator must pick **sync**. |
| **Critical gaps** | Project-specific chats require **manual** repo pulls (Factory LOC-ZONE, Triumph rules, etc.); Knowledge Center **out-of-git** — mirror refresh **optional** (SAFE UNKNOWN). |

### Recommended action

**Priority C:** Per-project chat bootstrap checklist (FP passport + OPERATIONAL-INDEX Core Run row + mode declaration).  
Maintain sync pack on awareness passes — **не** expand governance.

---

## Cross-Layer Drift

| Drift ID | Layers affected | Description | Severity |
|----------|-----------------|-------------|----------|
| **XD-01** | Registry, IA, Workflow, Frontend, Agents | **v0 ↔ v1 dual canon** — snake_case vs UPPER_SNAKE, 10 vs 8 site types, 16 vs 29 blocks | **Critical** |
| **XD-02** | Registry, Frontend, Design | **Registry ACCEPTED ≠ implementation** — 29 block_id, 9 partials, design patterns architecture-only | **Critical** |
| **XD-03** | SEO, IA, registries.md | **SEO Pattern Library (planned)** vs **seo-architecture v2 (ACCEPTED)** | **High** |
| **XD-04** | Strategy, Registry | **Commercial Pattern Library** name vs 1-pattern reality + VF_* visual registry | **High** |
| **XD-05** | Validation, Frontend | **BUILT vs VERIFIED vs PRODUCTION PASS** — documented but FP-0002 showed build log false-green | **High** |
| **XD-06** | UX, Design, Validation | **Wireframe stage** in workflow vs **Group/Layout Spec** as de-facto PIXEL substitute — no unified UX SSOT | **Medium** |
| **XD-07** | Operations, Execution Cases | **LOC-ZONE FP-XXXX** vs **execution-cases-registry** vs **live workspaces** — three visibility surfaces | **Medium** |
| **XD-08** | Roadmap, All | Phase 4 «done (doc)» read as product maturity; phases 6–7 **future** vs operator expectations | **Medium** |
| **XD-09** | Agent, QA | Specialist QA agents **planned** vs rich **human** QA docs — role confusion with Validator | **Medium** |
| **XD-10** | Knowledge, Governance | Web-GPT sync maturity map says Factory «operational methodology» — accurate, but **не** «operational engine» | **Low** (wording) |

---

## Critical Gaps

1. **v0↔v1 operational binding absent** — highest systemic risk (extends Registry Audit).
2. **Implementation cliff** — architecture layers (registry, blueprint, SEO, design patterns) **опережают** code и upstream artifacts.
3. **UX/Wireframe layer effectively missing** — workflow stage exists without SSOT.
4. **SEO content layer absent** — strong planning, no templates/generation.
5. **Commercial/Conversion pattern catalog minimal** — strategy→blueprint→frontend chain weak on reusable pattern_id.
6. **Agent layer mostly planned** — only frontend doc packs operational.
7. **Validation not automated** — WF-A02 closes **documentation**; FP-0002 proves discipline gap under pressure.
8. **LOC-ZONE partial enrollment** — not all delivery cases in records zone.
9. **False confidence from ACCEPTED/Foundation labels** — operators/agents may skip VL3/VL5 in PIXEL_PERFECT.
10. **WF-A03 deferred correctly** — but roadmap skimming may over-weight pixel automation vs registry/compose gaps.

---

## Roadmap Impact

### Phase table vs reality

| Roadmap phase | Claimed state | Honest layer impact |
|---------------|---------------|---------------------|
| **0–1** | Registration, registries v0 | **Done (doc)** — но v1 superseded partially; drift persists |
| **2–4** | Artifact/execution/semantic/bus/validation models | **Done (doc)** — rich vocabulary; **not** runtime; overlaps WF-A02 |
| **5** | Cursor-assisted production | **Operational** for frontend path; upstream stages **thin** |
| **6–7** | Runtime / automation | **Blocked** — no MARS factory engine evidenced |

### WF-Axx status

| ID | Status | Layer impact |
|----|--------|--------------|
| **WF-A01** | **Complete** | Production modes — **operational** for intake/QA routing |
| **WF-A02** | **Complete** (+ VL3 Pass 02) | Validation — **strong doc**; adoption **in progress** |
| **WF-A03** | **DEFERRED** | Would affect Validation/Design/Frontend QA **only** — **не** fixes registry/UX/strategy gaps |

### Registry Expansion vs WF-A03 (reconfirmed)

**Registry Expansion + v0→v1 binding + VL3 operational adoption** > **WF-A03** for near-term ROI when projects are TEMPLATE_ART or PIXEL_PERFECT with composition failures (OCPilot trajectory, FP-0002 class).

**roadmap.md** operator reminder: WF-A03 requires **separate Web-GPT Research Pass** — still valid.

---

## Recommended Next Work

### Priority A

1. **v0 → v1 operational binding charter** — single canonical `site_type_code` / `block_id` for new work; banner on v0 ops docs.
2. **Registry v1.1 structural blocks** — HEADER_NAV, FILTERS, SEARCH (+ breadcrumbs/pagination policy).
3. **Reference partials expansion** — PROMO subset **or** explicit LANDING-only Template-Art policy in passport.
4. **VL3 mandatory adoption** on PIXEL_PERFECT greenfield — Group Decomposition → Layout Spec → Instance/Asset/Text gates before generation (FP-0002 lesson).
5. **False-green closure discipline** — BUILT never cited as VERIFIED; build logs must not claim section PASS without diff evidence.

### Priority B

6. **SEO content pattern slice** — title/description templates per `page_type` (documentation).
7. **Strategy memo contract v1** — minimal fields binding to blueprint conversion requirements.
8. **Commercial Pattern catalog v0** — pattern_id file: lead-form-v1, rfq-v1, scroll_process_timeline.
9. **FP-0002 LOC enrollment decision** — enroll vs learning-only charter.
10. **Agent operational honesty matrix** — planned vs human-executed today per workflow stage.
11. **BLOCK-REGISTRY hygiene** — full BLOCK-CONTRACT on 29 entries (Registry Audit carryover).

### Priority C

12. **Wireframe artifact contract v1** — markdown section map (after A binding).
13. **Design token charter DG-01** — documentation bind to foundation `_tokens.scss`.
14. **Execution case → layer lesson index**.
15. **WF-A03 Pixel Factory** — only after Research Pass **and** visual verification dominates bottleneck.
16. **Extended type blueprints** — SAAS, MARKETPLACE charters.
17. **Registry JSON Schema export** — tooling readiness.

---

## Risks

| Risk | Severity | Layers | Mitigation (documentation-only) |
|------|----------|--------|-----------------------------------|
| False «Factory complete» narrative | **Critical** | All | Treat ACCEPTED as architecture; REPORT cites VL layer |
| v0 block_id on v1 blueprint | **Critical** | Registry, Frontend, Agents | Binding charter; STOP on mixed IDs |
| PIXEL_PERFECT without VL3 | **Critical** | Validation, Frontend | FP-0002 class failures; mandatory composition gates |
| TEMPLATE_ART on CATALOG without structural blocks | **High** | Registry, IA, Frontend | HITL; record OPEN gaps |
| Compact QA mistaken for Production PASS | **High** | Validation | operational-qa-entry router |
| SEO architecture without content templates | **High** | SEO | Planning-only claims; no auto meta |
| Wireframe skip → design drift | **Medium** | UX, Design | Layout Spec path for PIXEL; wireframe contract for TEMPLATE |
| LOC-ZONE / workspace desync | **Medium** | Operations | execution-cases-registry append rule |
| WF-A03 auto-start | **Medium** | Validation | roadmap DEFERRED marker |
| Governance bloat session load | **Medium** | Knowledge, Workflow | OPERATIONAL-INDEX Core Run single row |
| Extended type misclassified as Core | **Medium** | Registry, IA | SITE-TYPE-REGISTRY Extended section |

---

## SAFE UNKNOWN

- **FOUNDRY** как именованный продукт/путь в tree — **не обнаружен**; аудит = Website Factory ecosystem.
- Единый owner миграции v0→v1 для live projects (Triumph v6, OCPilot Site-001, ISBD) — **не зафиксирован**.
- VL3 domain adoption rate на Triumph v6 и ISBD workspaces — **не аудирован** в этом pass (нет per-project VL REPORT sweep).
- BZPM W3 blueprint delivery date — **UNKNOWN**.
- Machine registry export (JSON Schema) — **не defined**.
- Knowledge Center mirror freshness — **UNKNOWN** (out-of-git).
- Will Triumph workspace become PROMO reference standard — **UNKNOWN** (BLUEPRINT-GAPS).
- MetaBOT / Factory SEO bridge — **no integration contract**.
- OCPilot Site-001 production mode and registry binding — **не verified** in this audit scope.
- Agent runtime / Control Plane implementation timeline — **future**, no repo evidence.

---

**STOP — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме создания этого отчёта)**

---

*Audit artifact: `reports/foundry-system-wide-layer-audit-v1.md`*  
*Evidence base: foundry-registry-layer-audit-v1.md, OPERATIONAL-INDEX, roadmap.md, layer-map.md, workflow-map.md, execution-cases-registry-v1.md, WF-A01/A02 charters, VL3 domains charter, LOC-ZONE README + passport contract, agents/registry.md + cards/, reference-v1 foundation stack, FP-0002 forensic, web-gpt sync pack, system maturity map.*
