# REPORT — FOUNDRY CAPABILITY GAP AUDIT

**Дата:** 2026-06-19  
**Режим:** аудит только — исходные документы **не изменялись**  
**Область:** реальные **производственные способности** Website Factory / FOUNDRY (не оценка качества документации как таковой)  
**База:** [foundry-registry-layer-audit-v1.md](foundry-registry-layer-audit-v1.md) · [foundry-system-wide-layer-audit-v1.md](foundry-system-wide-layer-audit-v1.md) · execution cases · workspaces · LOC-ZONE · WF-A01/A02 charters

**Терминология:** строка **FOUNDRY** в репозитории **не найдена** как отдельный продукт или путь. В этом отчёте **FOUNDRY** = **Website Factory** — human-operated методология + governance + ограниченный набор реальных build workspaces. См. SAFE UNKNOWN.

**Честная граница:** Phase 1 MARS — documentation-first, Cursor-assisted execution. **Нет** factory runtime, orchestration engine, autonomous agents, machine-enforced validation в repo. Оценка **Production Readiness** отражает способность **доставить реальный сайт** при текущей дисциплине оператора, а не наличие автоматизации.

---

## Executive Summary

FOUNDRY сегодня — **рабочая human-operated фабрика для узкого класса задач** (коммерческие **LANDING** / service landing, frontend production в Gulp-workspaces, PIXEL_PERFECT под жёстким VL3), а **не** универсальный генератор сайтов по Site Type Registry.

| Паттерн | Факт |
|---------|------|
| **Сильнейшие capabilities** | Landing Sites (live evidence), Frontend Production (methodology + Triumph v6), Validation governance (WF-A02), Blueprint planning (Core 5 doc) |
| **Слабейшие capabilities** | Corporate / Catalog / Manufacturer / Auto как **Factory-pipeline**; Blueprint Generation (automation); Validation (enforcement); Template-Art beyond LANDING subset |
| **Главный разрыв doc ↔ reality** | Registry/Blueprint **ACCEPTED** при **~31%** reference block implementation (9/29 partials) и **dual v0↔v1 canon** |
| **Главный разрыв build ↔ quality** | FP-0002 forensic: build log **15/15 PASS**, forensic **1 PASS / 12 PARTIAL / 2 FAIL** — методология QA сильна, **исполнение под давлением** ломается без VL3 |

**Сводный вердикт:** FOUNDRY **production-capable** для **LANDING / service landing** и **PIXEL_PERFECT frontend** при experienced operator + HITL. Для **CATALOG / CORPORATE / manufacturer / auto-dealer** классов — **ad-hoc delivery** (OCPilot, OpenCart) **опережает** Factory pipeline; канон v1 **не замыкает** end-to-end production без structural registry expansion и operational binding.

---

## Capability Matrix

Шкала **Current Maturity:** 1 = concept only · 4 = partial human-operated · 7 = repeatable production with HITL · 9 = production-scale with minimal gaps  
**Production Readiness:** `NR` Not Ready · `HP` Human-operated Pilot · `LP` Limited Production · `PR-HITL` Production-ready with mandatory HITL · `PS` Production-scale (automated or broad portfolio)

| # | Capability | Current Maturity | Production Readiness | Main Dependencies | Critical Gaps |
|---|------------|------------------|----------------------|-------------------|---------------|
| **01** | **Landing Sites** | **7 / 10** | **PR-HITL** | `LANDING` site type · LANDING-BLUEPRINT-v1 · 9 reference partials · Triumph v6 workspace · RU landing QA preset · `gulp_frontend_agent` / Forge | v0↔v1 ID drift in ops Wave 4–6; reference covers ~subset of 29 blocks; no machine blueprint instance |
| **02** | **Corporate Sites** | **4 / 10** | **HP** | CORPORATE-BLUEPRINT-v1 · PAGE-TYPE-REGISTRY · Legal v2 · hybrid IA rules | No reference workspace; shallow CORPORATE partials; custom integrations per charter only; no battle-tested corporate case in Factory lane |
| **03** | **Catalog Sites** | **4 / 10** | **HP** (ad-hoc **LP** via OCPilot) | CATALOG-BLUEPRINT-v1 · SITE-002 BZPM TEST · OpenCart stack | **HEADER_NAV, FILTERS, SEARCH** absent from Block Registry v1; no Factory workspace for BZPM; faceted SEO FUTURE; manual UI = canonical on SITE-002 |
| **04** | **Manufacturer Sites** | **3 / 10** | **NR** (Factory) / **HP** (OCPilot) | Maps to `CATALOG` + `CORPORATE` composition; BZPM as industry proxy | **No** dedicated site_type or vertical playbook; RFQ/dealer/spec-table blocks undocumented in reference code; Factory method not proven for B2B manufacturer IA |
| **05** | **Service Business Sites** | **6 / 10** | **PR-HITL** | `LANDING` / `PROMO` · Triumph (manipulator/cargo) · `scroll_process_timeline` pattern · service_landing v0 legacy | v0 `service_landing` not mapped 1:1 to v1; PROMO multi-page subset unimplemented in reference; strategy/CTA pattern catalog ~5% |
| **06** | **Auto Industry Sites** | **4 / 10** | **HP** | OCPilot SITE-001 (Автосалон СИБКАР) · used-catalog / PDP work · WF visual direction CSS-only | **No** auto vertical in Site Type Registry; OpenCart theme path outside reference-v1; SITE-001 Factory binding **не verified**; catalog blocks missing in canon implementation |
| **07** | **Template-Art Production** | **4 / 10** | **HP** (LANDING-only effective) | WF-A01 `TEMPLATE_ART` mode · Block Registry SSOT · Blueprint QA · Design System architecture | Registry **31%** implemented; CATALOG/CORPORATE Template-Art **blocked** without structural blocks; design tokens DG-01–04 OPEN; UX/wireframe SSOT missing |
| **08** | **Pixel-Perfect Production** | **5 / 10** | **HP → PR-HITL** (if VL3 enforced) | WF-A01 `PIXEL_PERFECT` · VL3 domains charter · Group Decomposition / Layout Spec laws · FP-0002 forensic lessons | WF-A03 **DEFERRED** (Vision, Visual Diff); FP-0002 false-green + generative fill + asset collision; no automated FIG↔HTML gate |
| **09** | **Blueprint Generation** | **5 / 10** (planning) / **2 / 10** (generation) | **HP** | 5 Core Blueprints ACCEPTED · PAGE-TYPE-REGISTRY · page-block-validation matrices · page_blueprint_agent card (planned) | **No** `project.blueprint.yaml` machine schema; agent **planned**; Extended types without blueprints; human markdown-only instances |
| **10** | **Frontend Production** | **7 / 10** | **PR-HITL** (LANDING) / **HP** (full registry) | Gulp workspaces · Waves 1–6 governance · Shell-first protocol · Triumph v6 · ISBD · fp-0002-shpigovsky | 9/29 block partials; curated library v0 naming; CATALOG/ECOMMERCE commerce chain absent in reference |
| **11** | **Validation** | **6 / 10** (governance) / **2 / 10** (enforcement) | **HP** | WF-A02 VL0–VL6 · VL3a–f domains · Production Modes router · operational-qa-entry · FP-0002 failure taxonomy | **Not** runtime/CI; compact pass vs PRODUCTION PASS confusion; SEO/Conversion/Design QA agents **planned**; adoption on Triumph/ISBD **SAFE UNKNOWN** |
| **12** | **Project Operations** | **5 / 10** | **HP** | LOC-ZONE · FP passport fields · ROC-01 catalog · onboarding-flow · execution-cases-registry | Only **FP-0001** ROC-enrolled; FP-0002 visibility-only; OCPilot/Triumph v6 **parallel** to LOC-ZONE; BZPM no Factory workspace; portfolio visibility fragmented |

---

## Capability Detail Notes

### 01 — Landing Sites

**Evidence (real production, not docs):**

- `workspaces/triumph-manipulator-landing-v6/` — extensive live client workspace (multi-page PPC variants, backend, dist build path).
- `workspaces/website-factory-reference-v1/` — 9 section partials aligned to LANDING block vocabulary.
- `workspaces/isbd-care-landing/` — client delivery case #2.
- Reference case artifact chain (Triumph doc simulation) + LOC FP-0001 partial closeout.

**Honest ceiling:** Repeatable **human-operated** landing production. **Not** one-click or agent-automated landing factory.

### 02 — Corporate Sites

**Evidence:** CORPORATE-BLUEPRINT-v1 **ACCEPTED**; **no** dedicated corporate reference workspace or enrolled execution case completing Factory CORPORATE track.

**Honest ceiling:** IA/legal **planning** possible; **build** requires project-local invention + heavy HITL per route group.

### 03 — Catalog Sites

**Evidence:** SITE-002 (BZPM) — live TEST catalog (`zpm.new-site.space`), M9.x phases, filters, megamenu — **OCPilot/OpenCart path**, operator manual UI canonical. Factory execution case `bzpm-catalog-redesign` — research complete, **no Factory workspace**.

**Honest ceiling:** Catalog **delivery** proven **outside** Factory canon; Factory **method** for catalog **not production-ready** until structural blocks + reference PLP/PDP.

### 04 — Manufacturer Sites

**Evidence:** BZPM (food equipment) is closest vertical proxy — classified operationally as catalog/manufacturer commerce, not as Factory `site_type_code`. No manufacturer-specific block set, SEO profile, or blueprint extension in v1.

**Honest ceiling:** **Concept / ad-hoc** — compose from CATALOG + CORPORATE charters per project; **no** vertical SSOT.

### 05 — Service Business Sites

**Evidence:** Triumph manipulator/cargo taxi — highest Factory-adjacent live evidence; `scroll_process_timeline` DEV-validated; v0 `service_landing` taxonomy richer than v1 explicit type.

**Honest ceiling:** **Strong** for single/multi-section commercial service **landing**; **weak** for full PROMO service hub sites without reference expansion.

### 06 — Auto Industry Sites

**Evidence:** OCPilot SITE-001 (СИБКАР) — auto dealership TEST, WF CSS visual direction, PDP/catalog stabilization waves; **not** enrolled in LOC-ZONE; production mode/registry binding unverified in this audit.

**Honest ceiling:** **Project-local** delivery competence; **Factory vertical capability** essentially **absent**.

### 07 — Template-Art Production

**Evidence:** WF-A01 charter operational; OCPilot Site-001 trajectory cited in prior audits as TEMPLATE_ART direction; reference implementation supports **LANDING block subset only**.

**Honest ceiling:** **Honest** only for LANDING-shaped Template-Art with operator accepting Factory visual defaults / design-system architecture without token kit.

### 08 — Pixel-Perfect Production

**Evidence:** FP-0002 Shpigovsky — full stress test, Design Governance Pack, Group/Layout laws, forensic failure register; `workspaces/fp-0002-shpigovsky-frontend/` build exists.

**Honest ceiling:** **Methodology production-grade**; **default execution** proven **unsafe** without mandatory VL3 composition gates and operator visual approval law.

### 09 — Blueprint Generation

**Evidence:** Core 5 blueprints + PAGE-BLOCK-VALIDATION matrices; Triumph `page-blueprint-v0.md` as case artifact; `page_blueprint_agent` status **planned**; BLUEPRINT-GAPS G6 machine schema **not queued**.

**Honest ceiling:** **Planning & QA** human-operated; **not** generation product.

### 10 — Frontend Production

**Evidence:** Operational doc packs (`gulp_frontend_agent`, `mars_forge_frontend_agent`); multiple workspaces with working Gulp builds; strongest governance stack (Waves 1–6, shell-first, compliance decision model).

**Honest ceiling:** **High** for static frontend craft; **low** for registry-complete multi-type assembly.

### 11 — Validation

**Evidence:** WF-A02 Complete; VL3 domains Pass 02; FP-0002 spawned failure classes (false-green, asset collision, generative fill); RU landing preset.

**Honest ceiling:** **Excellent operator playbook**; **no** enforcement layer — discipline-dependent.

### 12 — Project Operations

**Evidence:** LOC-ZONE C2–C7 proven on FP-0001; passport contract with `production_mode`; FP-0002 rich artifacts but not catalog-enrolled; execution-cases-registry 3 rows vs broader live portfolio.

**Honest ceiling:** **Substrate proven** for enrolled projects; **portfolio-wide** operations **immature**.

---

## Top Capability Gaps

| Rank | Gap | Capabilities affected | Severity | Why it limits production |
|------|-----|----------------------|----------|--------------------------|
| **1** | **Registry implementation cliff** — 29 `block_id`, 9 reference partials (~31%) | 03, 04, 07, 10, 02 | **Critical** | Blueprints and site types **promise** blocks that **cannot** be assembled from Factory reference; catalog/corp/ecommerce **blocked** at composition layer |
| **2** | **v0 ↔ v1 dual canon** — snake_case vs UPPER_SNAKE, 10 vs 8 site types, ops Wave 4–6 on v0 | All | **Critical** | Agents/operators mix IDs → **false compatibility** and wrong block stacks on v1 blueprints |
| **3** | **Missing structural blocks** — HEADER_NAV, FILTERS, SEARCH, breadcrumbs, pagination | 03, 04, 06, 07 | **Critical** | CATALOG/auto/manufacturer surfaces **require** navigation/filter/search; validation matrices **assume** roles without canonical `block_id` |
| **4** | **Validation not enforced** — human VL chain only; FP-0002 false-green | 08, 11, All | **Critical** | Build can **ship** with generative fill, wrong assets, invented copy while logs claim PASS |
| **5** | **UX / Wireframe layer absent** — no wireframe SSOT; Group/Layout Spec only for PIXEL | 07, 08, 02, 05 | **High** | Gap between blueprint and design **un governed** for Template-Art; drift default without Layout Spec |
| **6** | **SEO content layer missing** — architecture v2 strong; no title/meta/schema templates | 01–06, 09 | **High** | Planning-ready but **no** repeatable meta/H1/schema production; faceted SEO FUTURE for catalog |
| **7** | **Commercial / conversion pattern catalog minimal** (~1 pattern) | 01, 05, 07, 09 | **High** | Strategy → blueprint → frontend **weak** on reusable `pattern_id`; CTA/analytics contracts absent |
| **8** | **Agent layer mostly planned** — 2/18 operational doc packs | 09, 11, All upstream | **High** | Intake → Strategy → IA → Blueprint → UX → Design **thin**; human carries full upstream load |
| **9** | **Catalog / vertical delivery outside Factory canon** — BZPM, Sibcar on OCPilot/OpenCart | 03, 04, 06 | **High** | Real production **exists** but **does not feed** registry/reference loop — lessons trapped in project silos |
| **10** | **Project operations fragmentation** — LOC-ZONE partial enrollment; parallel Triumph/OCPilot tracks | 12, All | **Medium–High** | Passports, visibility, and lesson capture **uneven**; operator must reconcile 3 visibility surfaces |

---

## Main Bottleneck

**Primary limiter: Registry** (registry architecture **plus** reference implementation **plus** v0→v1 operational binding — treated as one bottleneck class).

**Обоснование:**

1. **Composition truth** — Site Type Registry, Block Registry, and Page Blueprints define **what** FOUNDRY can produce. At **~31%** block implementation and **missing structural IDs**, the registry **overstates** capability for 4 of 5 Core types. This is the **widest** gap between **claimed** and **buildable** surface.

2. **Multi-capability gate** — Registry gaps **directly block** Catalog (03), Manufacturer (04), Auto (06), Template-Art beyond LANDING (07), and full-spectrum Frontend (10). Strategy, UX, and Agents are **upstream**, but even perfect upstream work **cannot assemble** FILTERS/SEARCH/HEADER_NAV that **do not exist** in canon.

3. **Drift multiplier** — v0↔v1 dual canon (Registry Audit XD-01) **corrupts** the registry layer under operational load — the highest **systemic** failure mode across agents, ops docs, and curated library.

**Secondary limiter (operational, not architectural): Validation adoption** — WF-A02 documentation is strong, but FP-0002 proves **PIXEL_PERFECT** fails without VL3 discipline. This limits **08** more than **01** when operators follow gates.

**Not primary bottleneck (at current maturity stage):**

| Candidate | Why not #1 now |
|-----------|----------------|
| **Pixel Factory (WF-A03)** | Correctly **DEFERRED**; fixes visual **verification**, not missing catalog blocks or dual canon |
| **Agents** | Symptom of human-operated Phase 1; expanding agents **before** registry truth **amplifies** false-green |
| **Strategy** | Weak (3/10) but **LANDING** still ships via Triumph without strategy automation |
| **Operations** | Partial LOC-ZONE hurts **visibility**, not root **composition** capacity |

---

## Development Order

Recommended sequence for **6–12 months** — capability-outcome oriented, **human-operated** charters only (no runtime claims).

### Phase 1 — Months 1–2: Registry truth & binding (unblock 03, 07, 10)

| # | Work item | Target capabilities | Outcome |
|---|-----------|---------------------|---------|
| 1.1 | **v0 → v1 operational binding charter** — single canonical `site_type_code` / `block_id` for new work | All | Stops ID drift; agents/ops cite one namespace |
| 1.2 | **Registry v1.1 — structural blocks** — HEADER_NAV, FILTERS, SEARCH (+ breadcrumb/pagination policy) | 03, 04, 06, 07 | Catalog/auto/manufacturer **honest** in block vocabulary |
| 1.3 | **Explicit policy:** Template-Art **LANDING-only** until reference expansion **or** PROMO money-page subset charter | 07, 01, 05 | Ends false multi-type Template-Art claims |
| 1.4 | **BLOCK-REGISTRY hygiene** — full BLOCK-CONTRACT on 29 entries; TRUST/TESTIMONIALS disposition | 10, 07 | Registry doc matches operator expectations |

### Phase 2 — Months 2–4: Reference implementation & validation adoption (lift 01, 08, 10, 11)

| # | Work item | Target capabilities | Outcome |
|---|-----------|---------------------|---------|
| 2.1 | **Reference partials expansion** — minimum PROMO subset (SERVICES, PROCESS, TEAM) **or** LANDING policy reaffirmed | 05, 02, 10 | Factory can **assemble** multi-page service sites beyond hero/form |
| 2.2 | **VL3 mandatory adoption** on PIXEL_PERFECT greenfield — Group → Layout → Instance/Asset/Text before generation | 08, 11 | FP-0002-class failures prevented by **process** |
| 2.3 | **False-green closure discipline** — BUILT ≠ VERIFIED; build logs require diff evidence for section PASS | 08, 11 | Validation governance **bites** in practice |
| 2.4 | **Commercial Pattern catalog v0** — pattern_id file (lead-form-v1, rfq-v1, scroll_process_timeline) | 05, 09, 01 | Reusable conversion semantics |

### Phase 3 — Months 4–6: Catalog corridor & blueprint machine layer (lift 03, 04, 09)

| # | Work item | Target capabilities | Outcome |
|---|-----------|---------------------|---------|
| 3.1 | **CATALOG reference scaffold** — PLP/PDP/filter partials bound to new structural `block_id` | 03, 04, 10 | First **Factory-native** catalog assembly path |
| 3.2 | **`project.blueprint.yaml` machine schema** (documentation) | 09, 07 | Blueprint instances become **checkable** artifacts |
| 3.3 | **SEO content pattern slice** — title/description formulas per `page_type` | 01–06, 09 | SEO moves from planning-only to **repeatable copy rules** |
| 3.4 | **Execution case → layer lesson index** — normalize Triumph, FP-0002, BZPM, Sibcar feeds | 12, All | Project silos **feed** canon |

### Phase 4 — Months 6–9: Vertical pilots & operations (lift 04, 06, 12)

| # | Work item | Target capabilities | Outcome |
|---|-----------|---------------------|---------|
| 4.1 | **Manufacturer vertical pilot** — BZPM W3 blueprint **or** new charter using CATALOG reference | 03, 04 | One **enrolled** catalog/manufacturer Factory track |
| 4.2 | **Auto vertical pilot charter** — SITE-001/Sibcar binding to v1 registry + production_mode in passport | 06, 12 | Auto dealer **inside** Factory visibility, not parallel-only |
| 4.3 | **FP-0002 LOC enrollment decision** — enroll vs learning-only | 12, 08 | Forensic lessons **institutionalized** |
| 4.4 | **Wireframe artifact contract v1** — markdown section map for Template-Art | 07, 02, 05 | Closes blueprint→design cliff for non-PIXEL |

### Phase 5 — Months 9–12: Corporate depth & selective automation prep (lift 02, 08, 11)

| # | Work item | Target capabilities | Outcome |
|---|-----------|---------------------|---------|
| 5.1 | **CORPORATE reference slice** — hub + about + contact route group | 02, 10 | First **honest** corporate assembly evidence |
| 5.2 | **Strategy memo contract v1** — bind to blueprint `conversion_requirements` | 02, 05, 09 | Upstream strategy **artifact**, not governance-only |
| 5.3 | **Design token charter DG-01** — documentation bind to `_tokens.scss` pattern | 07, 08 | Template-Art visual consistency **without** full Figma kit |
| 5.4 | **WF-A03 Research Pass decision** — start Pixel Factory **only if** visual verification dominates backlog | 08, 11 | Avoid premature pixel automation before composition truth |
| 5.5 | **Agent operational honesty matrix** — planned vs human-executed per workflow stage | 09, 11, 12 | Stops **implicit** agent automation assumptions |

**Explicitly deferred beyond 12 months unless charter:** ECOMMERCE Legal Extension E1–E4 · Extended Type blueprints (SAAS, MARKETPLACE) · Registry JSON Schema export · MARS factory runtime phases 6–7.

---

## Risks

| Risk | Severity | Capabilities | Mitigation (documentation / discipline) |
|------|----------|--------------|----------------------------------------|
| False «Factory complete» from ACCEPTED labels | **Critical** | All | Treat ACCEPTED as **architecture**; capability audit = **implementation** |
| TEMPLATE_ART on CATALOG without structural blocks | **Critical** | 03, 07 | HITL + OPEN gap; no pretend PLP completeness |
| PIXEL_PERFECT without VL3 composition gates | **Critical** | 08, 11 | FP-0002 lesson mandatory on greenfield |
| v0 `block_id` on v1 blueprint | **Critical** | All | Binding charter; STOP on mixed IDs |
| OCPilot delivery **never** feeds Factory reference | **High** | 03, 04, 06, 12 | Execution case lesson index; explicit enrollment |
| Compact QA mistaken for PRODUCTION PASS | **High** | 11, 08 | operational-qa-entry router |
| BZPM/Sibcar production **misread** as Factory catalog/auto readiness | **High** | 03, 06 | Separate **delivery evidence** from **canon pipeline** |
| WF-A03 started without Research Pass | **Medium** | 08 | roadmap DEFERRED marker |
| Governance bloat slows operators | **Medium** | 12 | OPERATIONAL-INDEX Core Run single row |
| Extended site type misclassified as Core | **Medium** | 02, 03 | SITE-TYPE-REGISTRY Extended section |

---

## SAFE UNKNOWN

- **FOUNDRY** как именованный продукт/путь в tree — **не обнаружен**; аудит = Website Factory ecosystem.
- **OCPilot SITE-001** `production_mode` и registry v1 binding — **не verified** в этом pass.
- **VL3 adoption rate** на Triumph v6 и ISBD — **не аудирован** (нет per-project VL REPORT sweep).
- **BZPM W3 blueprint** delivery date и Factory workspace registration — **UNKNOWN**.
- Единый owner миграции v0→v1 для live projects — **не зафиксирован**.
- Will Triumph v6 become **PROMO** reference standard — **UNKNOWN** (BLUEPRINT-GAPS).
- Machine registry export (JSON Schema) — **not defined**.
- **Manufacturer** and **Auto** as future Extended types vs v1 composition rules — **undecided**.
- Revenue/throughput metrics for Factory portfolio — **no evidence** in repo.
- Agent runtime / Control Plane timeline — **future**, no repo proof.

---

**STOP — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме создания этого отчёта)**

---

*Audit artifact: `reports/foundry-capability-gap-audit-v1.md`*  
*Evidence base: foundry-registry-layer-audit-v1.md, foundry-system-wide-layer-audit-v1.md, execution-cases-registry-v1.md, SITE-TYPE-REGISTRY-v1, BLOCK-REGISTRY-v1, blueprints/, WF-A01/A02 charters, FP-0002 forensic, Triumph v6 workspace, OCPilot SITE-001/002 reports, LOC-ZONE README, agent-map.md, agents/registry.md.*
