# REPORT — WEBSITE FACTORY PRODUCTION MODES

**Date:** 2026-06-17  
**Scope:** Architecture and contracts design only — **no implementation**, **no workflow edits**, **no governance expansion**.  
**Evidence base:** `projects/mars-website-factory/`, `workspaces/website-factory-reference-v1/`, `workspaces/website-factory-operations/` (LOC-ZONE), `agents/`, `reports/website-factory-architecture-alignment-v1.md`, `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md`, execution workspaces (FP-0002, Triumph).  
**External reference:** AI Website Factory Research — compared via alignment report summary only; **not** imported as repo truth.

**Honesty boundary:** Website Factory in MARS is **documentation-first, human-operated methodology**. Production Modes described here are **architectural contracts** — not runtime flags, not orchestration products, not automated routers unless a future charter explicitly implements them.

---

## Executive Summary

Website Factory уже **неявно** работает в двух производственных сценариях: (1) воспроизведение готового дизайна (практика pixel-perfect в client workspaces + FP-0002) и (2) сборка из требований и библиотеки блоков (foundation adoption, block registry, Triumph-подобные пути). Формального **Production Mode contract** нет — это главный архитектурный пробел, подтверждённый FP-0002 (false-green build при отсутствии режимного QA fork).

**Вердикт Part 1:** `PIXEL_PERFECT` и `TEMPLATE_ART` — **правильные и достаточные** как два первичных архитектурных режима Website Factory при условии:

- явного **Mode Selection Gate** на intake;
- ортогональности к **Forge mode** (Lite/Standard/Critical) и **Operational Modes Model** (governance density);
- фиксации режима в **LOC-ZONE passport**;
- mode-specific QA router и vocabulary `BUILT` / `VERIFIED` / `PRODUCTION PASS`.

Третий постоянный режим **не требуется** на v1: гибриды (дизайн + новые секции из брифа) оформляются как **scoped sub-cycle** с явным primary mode + transition record, не как отдельный pipeline.

**Priority A (mandatory):** blocking intake gate · passport field · QA fork · anti-generative-fill для PIXEL_PERFECT · STOP при unknown mode.

---

## Production Modes Overview

### Canonical mode tokens

| Token | Working name | One-line contract |
|-------|--------------|-------------------|
| `PIXEL_PERFECT` | Pixel-perfect mode | Approved visual design is **SSOT**; frontend must **reproduce** layout, typography, spacing, assets, and copy fidelity — not reinterpret. |
| `TEMPLATE_ART` | Template-art mode | Requirements, IA, content, and block registry are **SSOT**; visual design is **produced** within Factory foundations and quality tiers — not extracted from FIG hash. |

### Orthogonal dimensions (must not be conflated)

| Dimension | What it controls | Documents |
|-----------|------------------|-----------|
| **Production mode** (`PIXEL_PERFECT` \| `TEMPLATE_ART`) | Fidelity contract, SSOT hierarchy, QA fork, extract vs generate | *This report* (future: `PRODUCTION-MODE-CHARTER-v1.md`) |
| **Forge mode** (Lite / Standard / Critical) | Task risk, checklist depth, freeze posture | `agents/mars-forge/forge-operational-modes-v1.md` |
| **Operational modes** (Lite → Critical → Freeze-validation …) | Governance density, report compression, escalation | `projects/mars-website-factory/operational-modes-model.md` |
| **Source Discovery** (Phase A0) | Inventory of **all** incoming materials | `website-factory-source-discovery-v1.md` — **both** modes |

```text
INTAKE
  └─► PRODUCTION MODE SELECTION  ◄── blocking gate (NEW)
         ├─ PIXEL_PERFECT  → extract + lock + diff + PF audit chain
         └─ TEMPLATE_ART   → blueprint + blocks + content SSOT + semantic QA

Per task / slice:
  └─► FORGE MODE (Lite default) × OPERATIONAL MODE (as risk dictates)
```

### Completeness, overlap, conflict assessment

| Question | Assessment |
|----------|------------|
| **Полнота двух режимов** | Покрывает наблюдаемые factory paths: FP-0002 (pixel) и Triumph / foundation adoption (template-art). Edge: «дизайн только для shell, остальное из брифа» → primary mode + scoped waiver, не третий режим. |
| **Пересечения** | Source Discovery, Block Registry, Site Type, Blueprint QA, Operator Visual Approval, Brand Asset rules — **общие**, но с разной строгостью. |
| **Конфликты** | (1) Client `AGENTS.md` pixel-perfect vs Factory pack без mode token. (2) Onboarding Path B запускает pixel chain без вопроса о режиме. (3) Generative fill при неполном extract в pixel-проекте (FP-0002). (4) `npm run build` PASS трактуется как production-ready. |
| **Достаточность** | Двух режимов достаточно для v1; **hybrid** и **migration-only** cycles описываются через **Mode Transition Rules**, не через расширение enum. |

---

## Pixel-perfect Mode

**Token:** `PIXEL_PERFECT`  
**When:** Client supplies approved visual design (FIG, PNG, JPG, PDF, screenshot pack, or mixed design pack) and delivery contract requires **maximum visual reproduction fidelity**.

### Source Of Truth

| Rank | Authority | Role |
|------|-----------|------|
| **1** | **Approved visual design source** (per `design-source-to-frontend-mapping-governance-v1.md` priority: Figma → PNG/PDF → …) | Primary evidence for layout, composition, assets, copy |
| **2** | **Project Production Standards** (post-approval) | Numeric SSOT after Mapping QA + Standards Approval |
| **3** | **Layout Spec + Group Decomposition + Assembly Spec** (approved) | Composition chain before HTML |
| **4** | **section-NN.lock.json** (recommended machine SSOT per FP-0002) | Per-section text/image/order lock |
| **5** | Operator Laws + Factory precision (OL-*, WF-GRID, WF-LAYOUT) | Normalization only — **never** override approved design |

**Non-SSOT in this mode:** starter template aesthetics, agent aesthetic judgment, block library defaults without explicit mapping record, generative paraphrase of missing copy.

### Allowed Inputs

| Category | Allowed | Notes |
|----------|---------|-------|
| Visual | Figma, PNG, JPG, PDF, WebP, screenshot pack, mixed design pack | Mandatory visual SSOT registration in Source Discovery |
| Structural | XLSX IA, briefs, sitemap, URL strategy | Governs IA/navigation — must not silently override visual order without ASSEMBLY DECISION |
| Content | Copy deck, legal micro-copy | May **supplement** FIG text when FIG extract incomplete — triggers HITL, not auto-fill |
| Technical | Production Standards Draft, numeric rules, layout specs | Factory-generated from design |
| **Forbidden as silent substitute** | Block library hero «as default», invented card copy, first-image-as-logo heuristic | FP-0002 failure classes |

### Creativity Rules

| Area | Allowed creativity | Forbidden |
|------|-------------------|-----------|
| Layout / spacing / type | **None** beyond documented OL-01 mapping to nearest approved row | «Looks cleaner», beautification drift |
| Copy | **None** — lock FIG/copy-deck strings | Paraphrase, hallucinated reviews/cards (FAIL-002, FAIL-003) |
| Assets | Select **only** from approved extract + brand detection chain | Positional heuristics without brand confirmation |
| Responsive | Implement per design exports; infer **only** with documented SAFE UNKNOWN + HITL | Invent alternate layouts |
| Interactions | Minimal stubs per charter (FAIL-010) or explicit KNOWN NON-GOALS | Fake functional forms/video without charter |
| Build staging | 2–3 sections per agent run (FP-0002 memory analysis) | Full-page generative pass in one context |

**Creativity level:** **0 — reproduction only.** Any creative gap → `UNKNOWN` + HITL, not fill.

### QA Rules

| Gate | Mandatory | Automation |
|------|-----------|------------|
| Source Discovery A0 | Yes — all sources READ | Human-operated |
| Design → Frontend Mapping QA | Yes | Human |
| Group Decomposition → Layout Spec → Assembly Spec | Yes | Human |
| Brand Asset Detection chain | Yes before logo wire | Documented; not in-repo engine |
| Design Calibration + Foundation QA | Yes (greenfield chain) | Human |
| Block-by-block operator approval | Yes (per client AGENTS.md pattern) | Human |
| Pixel Fidelity Audit (PF-*) | Yes | Human DevTools + side-by-side |
| Frontend Design QA Matrix | Yes | Human |
| Render Diff (FIG extract ↔ dist) | **Required for VERIFIED** — manual or project-scripted | Absent in Factory today |
| Text lock diff | Required per section | Absent — **NEW DOC NEEDED** at implementation |
| `BUILT` vs `VERIFIED` vs `PRODUCTION PASS` | `npm run build` = **BUILT** only | Addresses FAIL-001 |

**Forge mode:** typically **Standard** minimum for section slices; **Critical** for freeze/unfreeze, brand disputes, full-page stress.

### Acceptance Rules

Production slice/page may be declared **complete** only when **all** hold:

1. `production_mode: PIXEL_PERFECT` recorded in passport (no UNKNOWN).
2. Visual SSOT locked and referenced in Production Standards Approval.
3. All mandatory gates **PASS** or **PASS WITH NOTES** per `frontend-qa-reporting-standard-v1.md` — including PF-* where applicable.
4. State is **VERIFIED** (mode-appropriate checklist + render/text diff) — not merely **BUILT**.
5. **OPERATOR VISUAL ACCEPT** recorded (`operator-visual-approval-law-v1.md`) — TECHNICAL PASS ≠ approval.
6. No open Critical failure class: `ASSET_IDENTITY_COLLISION`, generative fill, false-green log.
7. Scoped KNOWN NON-GOALS (interactions, backend) documented if out of contract.

### SAFE UNKNOWN

| Situation | Required behavior |
|-----------|-------------------|
| No visual design source | **STOP** — mode mismatch; reclassify to `TEMPLATE_ART` or park |
| Visual source partial (mobile missing) | Document scope; **UNKNOWN** on uncovered viewports; HITL before PASS |
| FIG text not machine-exportable | **UNKNOWN** + HITL — **forbid** generative fill |
| Pixel spacing/type not measured | PF gate **UNKNOWN** — not PASS (`pixel-fidelity-audit-rules-v1.md` §0.3) |
| Assembly order conflict (bounds.y vs layer index) | **ASSEMBLY DECISION** record required (FAIL-007) — silent default forbidden |
| Render diff tooling absent | **SAFE UNKNOWN** on automated diff; mandatory human side-by-side + checklist |
| INSTANCE subtree invisible in flat extract | **STOP** section build until Group Register / Instance Resolver pass |

---

## Template-art Mode

**Token:** `TEMPLATE_ART`  
**When:** No approved pixel design; delivery driven by brief, SEO structure, blueprint, content deck, commercial requirements, wireframe/prototype, or blueprint-only charter.

### Source Of Truth

| Rank | Authority | Role |
|------|-----------|------|
| **1** | **Intake + approved blueprint / page architecture** | IA, page list, URL logic, block requirements |
| **2** | **Content contract** (copy deck, approved texts) | Copy SSOT — not FIG extract |
| **3** | **Site Type Registry + Block Registry** | `site_type_id`, `block_id`, compatibility, quality tiers |
| **4** | **Foundation adoption + reference tokens** | `foundation-adoption-charter-v1.md`, `_tokens.scss` brand layer |
| **5** | **Strategy / SEO artifacts** | Messaging, keyword structure, CTA narrative |
| **6** | Wireframe / prototype (if present) | Structural intent — not pixel measurement |

**Non-SSOT in this mode:** FIG hash diff, pixel-perfect PF-* against nonexistent design export, starter demo copy as final content.

**Explicit non-goals:** FIG extract requirements, Render Diff against design, Group Decomposition for non-imported visuals (unless wireframe SSOT exists).

### Allowed Inputs

| Category | Allowed | Notes |
|----------|---------|-------|
| Requirements | ТЗ, brief, commercial requirements, compliance flags | Intake SSOT |
| Architecture | Sitemap, blueprint, page-block validation, SEO structure | Upstream of frontend |
| Content | Copy deck, product data, legal | Mandatory before page build |
| Visual direction | Mood boards, brand guidelines, token tables | Inform `_tokens.scss` — not pixel lock |
| Prototype | Low-fi wireframe, clickable prototype | Structure reference |
| Library | `curated-library-index-v1.md`, reference-v1 blocks, foundation adoption | **Provenance required** (`block_id`) |
| Optional later | Approved section screenshots from library extracts | Triumph-style extraction — not pixel contract |

### Creativity Rules

| Area | Allowed creativity | Constraints |
|------|-------------------|-------------|
| Visual design | **High** within Factory foundations | Must respect `block_id`, quality tiers, ru-landing presets if commercial RU |
| Layout composition | Select LP-* patterns, registry blocks | No ad-hoc column math outside WF-GRID/WF-LAYOUT |
| Copy | Write from content contract + strategy | No lorem; no keyword stuffing; realistic commercial copy |
| Imagery | Brand-appropriate assets, library art, generated placeholders **only** if charter allows | Asset identity still applies for logos |
| Responsive | Factory breakpoint discipline | `foundation-adoption-charter-v1.md` patterns |
| New sections | Compose from registry + foundations | Extract-to-library optional post-delivery |

**Creativity level:** **High for design synthesis; low for architecture drift** — blueprint and block registry bound creativity.

### QA Rules

| Gate | Mandatory | Waived vs PIXEL_PERFECT |
|------|-----------|-------------------------|
| Source Discovery A0 | Yes (brief, content, brand — not FIG) | Same |
| Site Type + Blueprint QA | **Primary** | Stronger weight |
| Content contract completeness | Yes before page build | N/A in pixel (FIG-led) |
| Foundation adoption validation | Yes | Same |
| Design → Frontend Mapping QA | **Reduced** — token/brand mapping, not full extract | No full L-07 FIG extract |
| Group Decomposition / Layout Spec | When wireframe SSOT exists | Optional for pure library assembly |
| Pixel Fidelity Audit (PF-*) | **N/A** or **PASS WITH NOTES** on brand/semantic only | Explicit waiver |
| Render Diff | **Waived** | Non-goal |
| Frontend Design QA Matrix | Yes — semantic, responsive, a11y, enforcement | No FIG hash checks |
| `ru-landing-qa-preset-v1.md` | If RU commercial | Same |
| Block provenance audit | `block_id` traceable to registry | **Template-art specific** |

**Forge mode:** **Lite** viable for local token/section edits; **Standard** for new section from handoff; **Critical** for freeze/delivery.

### Acceptance Rules

1. `production_mode: TEMPLATE_ART` in passport.
2. Blueprint + content contract approved (HITL G1/G2 equivalent).
3. All pages trace to `site_type_id` + `block_id` set.
4. Foundation adoption QA **PASS**.
5. Frontend Design QA Matrix **PASS** / **PASS WITH NOTES** — PF-* marked **N/A** with charter reference.
6. No claim of pixel-perfect fidelity in REPORT or client comms.
7. OPERATOR VISUAL ACCEPT on brand/UX intent — not measurement diff.
8. **VERIFIED** = semantic + responsive + enforcement gates — not render diff.

### SAFE UNKNOWN

| Situation | Required behavior |
|-----------|-------------------|
| Blueprint incomplete | **STOP** frontend page build — park at architecture stage |
| Content deck missing | **STOP** — no invented long-form copy at scale |
| Brand tokens undefined | **UNKNOWN** on color/type; HITL before freeze |
| Block not in registry | **STRUCTURE CHANGE** or registry update — no silent custom block without record |
| Client later supplies FIG | **Mode transition** required — see below; do not implicit pixel QA |
| «Good enough» without operator sign-off | **STOP** — OPERATOR VISUAL ACCEPT mandatory |

---

## Mode Selection Gate

Website Factory **обязана запрашивать / фиксировать** production mode at the following lifecycle points.

### Gate matrix

| Lifecycle event | Mode action | If absent / ambiguous |
|-----------------|-------------|------------------------|
| **Новый проект** | **Mandatory declare** at `WF_V0_S01_INTAKE` (before site type classification affects QA emphasis) | **STOP** — no `WF_V0_S10` handoff, no LOC-ZONE passport finalize without field |
| **Новый production cycle** | **Confirm** mode still valid; record in cycle charter | **STOP** if charter contradicts passport mode without transition record |
| **Новый frontend cycle** | **Read** passport mode; route QA per mode | **STOP** if passport missing mode — run intake gate retroactively |
| **Новый дизайн поверх старого проекта** | **Evaluate transition** — likely `TEMPLATE_ART → PIXEL_PERFECT` | **STOP** until visual SSOT registered + transition approved |
| **Перезапуск проекта** | **Re-declare** mode; do not inherit from chat memory | **STOP** — reconstruction mode until passport rewritten |
| **Unknown state** | Treat as **UNDECLARED** | **STOP** all frontend production (HTML/SCSS), including scaffold, until resolved |

### Blocking surfaces (STOP triggers)

Frontend work **must not start** (including Shell, Production Standards Draft that assumes extract depth) when:

```text
production_mode ∈ { UNDECLARED, UNKNOWN, CONFLICT }
OR
(PIXEL_PERFECT ∧ no visual SSOT registered in Source Discovery)
OR
(TEMPLATE_ART ∧ no approved blueprint/content path)
```

**Minimum record at gate:**

| Field | Location (proposed) |
|-------|---------------------|
| `production_mode` | `FP-XXXX-PROJECT-PASSPORT.md` |
| `mode_declared_at` | passport metadata |
| `mode_declared_by` | operator / coordinator ID |
| `mode_rationale` | 1–3 sentences + source evidence pointer |
| `mode_waivers` | optional — scoped PF N/A, interaction stubs |

### Relationship to existing gates

| Existing gate | Enhancement (design only) |
|---------------|---------------------------|
| `onboarding-flow-v1.md` Path B step 1 | Add **step 0: production mode** before charter slug |
| `website-factory-source-discovery-v1.md` A0 | Branch checklist by mode after A0.5 |
| `operational-qa-entry-v1.md` | Mode router at top — **NEW** pointer row |
| `OPERATIONAL-INDEX.md` Core Run | Mode before frontend packs |

---

## Mode Transition Rules

### Permitted transitions

| From | To | Permitted? | Typical trigger |
|------|-----|------------|-----------------|
| `TEMPLATE_ART` | `PIXEL_PERFECT` | **Yes** | Client delivers approved FIG/PDF; retrofit existing site to design |
| `PIXEL_PERFECT` | `TEMPLATE_ART` | **Yes, rare** | Design contract cancelled; maintain IA, rebuild visually from library |
| Same → Same | — | **Yes** | New cycle, new pages — confirm only |
| Any | **Hybrid scope** | **Via primary mode + waiver** | e.g. PIXEL shell + TEMPLATE_ART inner pages — document per-page mode map |

### Forbidden implicit transitions

- Running PF-* audit on template-art without transition record.
- Applying generative fill after pixel mode declared.
- Treating foundation adoption as pixel-perfect because «it looks similar to reference».

### Transition protocol (design)

```text
1. Operator files MODE TRANSITION REQUEST in REPORT
2. HITL approves (coordinator + lead)
3. Update passport production_mode + transition_log[]
4. Re-run affected gates:
   PIXEL_PERFECT ← TEMPLATE_ART: Source Discovery visual, Mapping QA, Standards, PF baseline
   TEMPLATE_ART ← PIXEL_PERFECT: waive PF, lock content/blueprint SSOT, archive FIG locks
5. Freeze impact assessment — may require Critical Forge mode
```

### Storage locations

| Artifact | Field / section |
|----------|-----------------|
| **LOC-ZONE passport** | `production_mode`, `mode_history[]` |
| **MOC-01 manifest** (when enrolled) | `factory.production_mode` |
| **Project Production Standards** | `mode_binding` clause — ranks with SSOT |
| **REPORT header** | `Production mode: PIXEL_PERFECT \| TEMPLATE_ART` |
| **Future agent contracts** | `required_production_mode` in task envelope |
| **Per-page override** (hybrid only) | `page_mode_map` in blueprint — not a third global mode |

---

## Workflow Impact Analysis

Impact on Factory layers — **what changes by mode**.

### Intake

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Primary question | What visual SSOT exists? Design approval chain? | What business/SEO/content requirements exist? |
| Artifacts | Design pack inventory, approval status | Brief, blueprint readiness, content deck status |
| Gate | Visual SSOT **required** before frontend | Blueprint + content path **required** |

### Discovery

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Source Discovery A0 | **Full** — visual + structural | **Full** — structural + content; visual optional |
| Authority | Visual source = Critical for layout | Brief/IA = Critical |
| FP-0002 lesson | Register FIG anomalies early | Register content gaps early |

### Strategy

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Weight | Secondary to design reproduction | **Primary** — positioning, funnel, SEO narrative |
| Agents (planned) | Marketing/SEO inform copy gaps only | Marketing/SEO **drive** block selection |
| Drift risk | Strategy overrides visual | Strategy fabrications without evidence |

### Blueprint

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Role | Confirms page list vs design pages; block inventory from design | **SSOT** for pages, blocks, URLs |
| QA | Consistency design ↔ blueprint | `page-blueprint-qa-checklist-v0.md` **blocking** |
| Block registry | Maps design sections → `block_id` | Selects `block_id` from palette |

### Design

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Activity | Audit + extract + calibration | Wireframe / direction / token choice / library composition |
| Outputs | Production Standards, Layout Spec, Group Register | Token table, wireframes, block wire-ups |
| Agents | Design Governance, extract discipline | AI Designer / Wireframe (planned) — **generative allowed** |
| Stop rule | Missing extract → HITL | Missing blueprint → STOP |

### Frontend

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Chain | A0 → Mapping QA → Shell → block-by-block → PF audit | Adoption → sections from library → semantic QA |
| Gulp agent behavior | Text lock, no paraphrase, staged sections | Content-driven, `block_id` provenance |
| AGENTS.md pixel-perfect | **Active** in client workspace | **Inactive** — replace with template-art charter |
| FP-0002 pipeline | Canonical stress path | Not applicable |

### QA

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Entry | `operational-qa-entry-v1.md` → **pixel router** | → **template router** |
| PF-* | Mandatory | N/A (waived) |
| Render diff | Required for VERIFIED | Waived |
| Enforcement pack | Full EG gates | Full EG gates (no pixel claims) |
| Verdict vocabulary | BUILT / VERIFIED / PRODUCTION PASS | Same — VERIFIED = semantic chain |

### Release

| Aspect | PIXEL_PERFECT | TEMPLATE_ART |
|--------|---------------|--------------|
| Operator approval | Visual side-by-side vs SSOT | Brand/UX acceptance vs requirements |
| Client comms | «Reproduces approved design» | «Meets blueprint and content contract» |
| Regression | Visual regression workflow **mandatory** on visual changes | Responsive + semantic regression |
| Hosting/deploy | SAFE UNKNOWN per project | SAFE UNKNOWN per project |

---

## Future Layer Mapping

Mapping FP-0002 / alignment research layers to production modes.

| Layer | PIXEL_PERFECT | TEMPLATE_ART | Notes |
|-------|---------------|--------------|-------|
| **Instance Resolver Layer** | **Primary** — mandatory before INSTANCE-heavy sections | **Optional** — only if importing componentized wireframes | FAIL-006, FAIL-008 root cause |
| **Asset Identity Layer** | **Primary** — brand detection, hash dedup, manifest | **Shared** — logos/favicons still require brand chain | `ASSET_IDENTITY_COLLISION` applies to both |
| **Visual Ordering Layer** | **Primary** — bounds.y assembly, ASSEMBLY DECISION | **Low** — DOM order from blueprint, not FIG | FAIL-007 |
| **Frontend QA Layer** | **Shared** — mode-specific checklists | **Shared** — semantic/responsive emphasis | False-green fix applies to both |
| **Render Diff Layer** | **Primary** — FIG↔HTML, screenshot diff | **Waived** — explicit non-goal | Absent today; project-local scripts possible |

### Additional research layers (alignment v1 crosswalk)

| Layer | PIXEL_PERFECT | TEMPLATE_ART |
|-------|---------------|--------------|
| Structure Extraction | **Primary** | Partial (IA only) |
| Component Detection | **Primary** | Optional |
| Layout Measurement | **Primary** | Token-level only |
| Screenshot Layer | **Primary** | Smoke only |
| Visual Diff Layer | **Primary** (human or scripted) | Waived |
| Pixel QA Layer | **Primary** | Waived |
| Text Lock / anti-paraphrase | **Primary** | Content deck diff only |

---

## Cross-surface representation

How production modes should appear across Factory surfaces (**design targets** — not implemented).

### Website Factory (methodology pack)

| Surface | Representation |
|---------|----------------|
| `OPERATIONAL-INDEX.md` | Row: «Production mode router» → charter + passport field |
| `onboarding-flow-v1.md` | Step 0 mode selection (both paths) |
| `website-factory-workflow-v0.md` | `WF_V0_S01` output: `production_mode` artifact |
| `website-factory-source-discovery-v1.md` | A0 checklist fork |
| `operational-qa-entry-v1.md` | Top-level mode router |
| `frontend-qa-reporting-standard-v1.md` | REPORT header field; PF N/A rule for TEMPLATE_ART |
| Future `PRODUCTION-MODE-CHARTER-v1.md` | Canonical definitions |

### LOC-ZONE

| Surface | Representation |
|---------|----------------|
| `FP-XXXX-PROJECT-PASSPORT.md` | `production_mode`, `mode_history[]`, `mode_waivers` |
| MOC-01 manifest | `factory.production_mode` |
| SOC surfaces | Mode-aware status (e.g. «PIXEL — Mapping QA pending») |
| ROC catalog | Filterable by mode (optional) |

### Project Intake

| Surface | Representation |
|---------|----------------|
| Intake summary template | Checkbox / enum: PIXEL_PERFECT \| TEMPLATE_ART |
| Task envelope (future) | `required_production_mode` |
| Handoff contracts | Mode-scoped QA_requirements |

### Future Agent Contracts

| Agent | Mode binding |
|-------|--------------|
| `gulp_frontend_agent` | Read passport mode; PIXEL → text lock + staged build; TEMPLATE → block_id + content SSOT |
| `mars_forge_frontend_agent` | Orthogonal Forge mode; cite both in REPORT |
| `frontend_qa_agent` (planned) | Mode-specific checklist matrix |
| Planned design agents | TEMPLATE_ART primary; PIXEL → extract-only |

### Future Frontend QA

| Mechanism | Mode behavior |
|-----------|---------------|
| Gate rollup | PF-* required vs N/A |
| VERIFIED definition | Render diff vs semantic chain |
| Failure attribution | Mode-aware expected gates |
| Operator Visual Approval | Side-by-side vs requirements review |

---

## Risks

| Risk | Severity | Mitigation (architecture) |
|------|----------|---------------------------|
| **False-green production** | Critical | `BUILT` ≠ `VERIFIED`; mode-specific checklists (FP-0002 FAIL-001) |
| **Wrong path without gate** | High | Blocking intake gate; STOP on UNDECLARED |
| **Mode / Forge conflation** | High | Orthogonal vocabulary in charter + REPORT |
| **Implicit hybrid** | High | Per-page `page_mode_map`; primary mode in passport |
| **Generative fill in PIXEL_PERFECT** | Critical | Text lock + UNKNOWN policy |
| **Template-art claimed as pixel** | Medium | PF N/A + explicit non-claims in REPORT |
| **Doctrine vs operations drift** | Medium | Passport as LOC-ZONE SoT; reference-v1 mode matrix (future) |
| **Transition without re-gate** | High | Transition protocol + freeze assessment |
| **Agent mythology** | Medium | Mode in task envelope; honesty boundary on automation |
| **Research doc not in repo** | Low | Attach full research or keep SAFE UNKNOWN |

---

## SAFE UNKNOWN

| Item | Status | What would verify |
|------|--------|-------------------|
| Full AI Website Factory Research text | **SAFE UNKNOWN** | Canonical copy in repo |
| Hybrid per-page mode taxonomy | **Design proposal only** | Pilot on mixed FP project |
| Automated Render Diff adoption | **SAFE UNKNOWN** | Project CI charter |
| OCPilot SITE-001 ↔ WF mode mapping | **SAFE UNKNOWN** | Crosswalk doc |
| Third mode (e.g. «migration-only») | **Not required v1** | Charter if recurring pattern emerges |
| Runtime mode router implementation | **Not claimed** | Explicit implementation charter |
| FP-0002 ROC enrollment | **Pending operator decision** | LOC-ZONE catalog update |

---

## Recommended Architecture

### Priority A — mandatory

1. **Production Mode Selection gate** at `WF_V0_S01` + onboarding step 0 — blocking before frontend.
2. **Passport field** `production_mode: PIXEL_PERFECT | TEMPLATE_ART` in all FP-* passports.
3. **QA mode router** in `operational-qa-entry-v1.md` (design pointer — fork PF vs semantic).
4. **Vocabulary** `BUILT` / `VERIFIED` / `PRODUCTION PASS` — end false-green.
5. **PIXEL_PERFECT anti-generative-fill policy** — missing text → UNKNOWN + HITL.
6. **STOP rules** on UNDECLARED mode and mode/source mismatch.
7. **Orthogonality declaration** — production_mode × forge_mode × operational_mode.

### Priority B — desirable

1. **`PRODUCTION-MODE-CHARTER-v1.md`** — canonical definitions, non-goals, checklists.
2. **Mode transition protocol** + `mode_history[]` in passport.
3. **Layer checklist** for PIXEL_PERFECT mapped to existing docs + gaps.
4. **Template-art charter** linked to foundation adoption + block registry.
5. **`frontend_qa_agent` operational pack** with mode matrices.
6. **Visual Y ordering / ASSEMBLY DECISION** policy for PIXEL_PERFECT.
7. **`section-NN.lock.json` SSOT** pattern standardized.
8. **Crosswalk** existing packs to mode columns (alignment v1 §10 Phase 0 item 4).

### Priority C — defer

1. Automated vision / CV layer.
2. Factory engine runtime / LangGraph mode router.
3. Third global production mode enum.
4. Percy/Chromatic SaaS unless project charters.
5. ROC enrollment automation.
6. Governance expansion beyond mode charter + passport field.

---

## Appendix — Evidence index

| Artifact | Role in this report |
|----------|---------------------|
| `reports/website-factory-architecture-alignment-v1.md` | Industry comparison, gap analysis, mode fork P0 |
| `reports/FP-0002-STRESS-TEST-FORENSIC-v1.md` | False-green, generative fill, layer lessons |
| `projects/mars-website-factory/onboarding-flow-v1.md` | Missing mode gate at Path B |
| `projects/mars-website-factory/website-factory-source-discovery-v1.md` | Phase A0 — shared |
| `projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md` | PIXEL extract chain |
| `projects/mars-website-factory/foundation-adoption-charter-v1.md` | TEMPLATE_ART path |
| `projects/mars-website-factory/pixel-fidelity-audit-rules-v1.md` | PIXEL QA |
| `projects/mars-website-factory/operational-qa-entry-v1.md` | QA router target |
| `projects/mars-website-factory/frontend-qa-reporting-standard-v1.md` | Verdict vocabulary |
| `projects/mars-website-factory/group-decomposition-law-v1.md` | PIXEL composition |
| `projects/mars-website-factory/failures/asset-identity-collision-v1.md` | Shared asset layer |
| `agents/mars-forge/forge-operational-modes-v1.md` | Orthogonal Forge dimension |
| `projects/mars-website-factory/operational-modes-model.md` | Orthogonal governance dimension |
| `workspaces/website-factory-operations/README.md` | LOC-ZONE |
| `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PROJECT-PASSPORT.md` | Passport without mode field today |
| `agents/cards/gulp-frontend-agent-v0.md` | Future mode binding |

---

*End of report — architecture and contracts design only. No implementation. No refactoring. No governance expansion.*
