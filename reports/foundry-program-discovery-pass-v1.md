# REPORT — FOUNDRY PROGRAM DISCOVERY PASS

**Дата:** 2026-06-19  
**Режим:** discovery only — исходные документы **не изменялись**  
**Область:** Website Factory / FOUNDRY — поиск скрытых программ уровня WF-R01 перед стартом WF-R01.1  
**Контекст:** WF-A01 ✅ · WF-A02 ✅ · WF-R01 **CHARTERED** · WF-R01.1 **PROPOSAL** · WF-A03 **DEFERRED**

**Терминология:** строка **FOUNDRY** в репозитории **не найдена** как отдельный продукт или путь. **FOUNDRY** = **Website Factory** ecosystem (`projects/mars-website-factory/`, `workspaces/website-factory-reference-v1/`, `workspaces/website-factory-operations/`). См. SAFE UNKNOWN.

**Honesty boundary:** Phase 1 MARS — documentation-first, human-operated Cursor execution. **Нет** factory runtime, orchestration engine, autonomous agents, machine-enforced validation в repo.

---

## Executive Summary

Discovery pass **не обнаружил** скрытых программ развития **сопоставимого масштаба с WF-R01**, которые уже фактически присутствуют в документации, имеют собственную область ответственности и **требуют отдельного roadmap-track до WF-R01.1**.

| Классификация | Количество | Примеры |
|---------------|------------|---------|
| **Уже зарегистрированные программы / architecture items** | 4 | WF-A01 (Complete), WF-A02 (Complete), WF-R01 (CHARTERED), WF-A03 (DEFERRED) |
| **Подпрограммы WF-R01** (не отдельные программы) | 8 + R01.X | R01.1–R01.8 — scope в program design |
| **SEED / CHARTER_CANDIDATE** (gap без program design) | 3 | UX/Wireframe, Strategy artifact slice, LOC-ZONE portfolio ops |
| **Скрытые PROGRAM уровня WF-R01** | **0** | — |

**Главный вывод:** крупные «скрытые» направления либо **уже канонизированы** (WF-A01/A02/A03), либо **вложены в WF-R01** как подпрограммы (Template-Art, Commercial Pattern, SEO slice, Execution Case feed), либо остаются на уровне **governance SEED** без program authority pass.

**Рекомендация:** **Option A** — дополнительная программа уровня WF-R01 **не требуется**; можно переходить к **WF-R01.1**.

---

## Existing Programs

Официально зарегистрированные Factory architecture items (`roadmap.md` § Factory architecture items, `OPERATIONAL-INDEX.md` Core Run):

| ID | Name | Status | Scope | Roadmap | OPERATIONAL-INDEX |
|----|------|--------|-------|---------|-------------------|
| **WF-A01** | Production Modes Contract | **Complete (Pass 01)** | `PIXEL_PERFECT` \| `TEMPLATE_ART`; intake gate; passport fields; QA router; BUILT/VERIFIED/PRODUCTION PASS | ✅ | ✅ |
| **WF-A02** | Validation Architecture | **Complete (Pass 01 + Pass 02)** | VL0–VL6; VL3a–f domains; signals; evidence; false-green closure | ✅ | ✅ |
| **WF-R01** | Registry Expansion Program | **CHARTERED** (execution not started) | v0→v1 binding; structural blocks; reference expansion; pattern/SEO slices; Template-Art policy; case feed | ✅ | ✅ |
| **WF-A03** | Pixel Factory Expansion | **DEFERRED** | Vision Layer, Visual Diff, Pixel QA Runtime, Screenshot Engine, Agent Runtime | ✅ | ✅ (via deferred marker) |

**Authority chain (канон после Charter Pass 2026-06-19):**

```text
WF-A01  Production Modes          ✅ Complete
WF-A02  Validation Architecture     ✅ Complete (+ VL3 Pass 02)
   ↓
WF-R01  Registry Expansion          ◆ CHARTERED (≠ ACTIVE)
   ↓
WF-A03  Pixel Factory               ⏸ DEFERRED (recommended R01 Gate 2+ precondition)
```

**WF-R01 subprograms** (scope SoT: `foundry-registry-expansion-program-design-v1.md`) — **не** отдельные roadmap programs:

| Subprogram | Name | Status |
|------------|------|--------|
| WF-R01.1 | v0 → v1 Operational Binding Charter | **PROPOSAL** (design complete) |
| WF-R01.2 | Registry v1.1 — Structural Blocks | Not authorized |
| WF-R01.3 | Reference Implementation Expansion | Not authorized |
| WF-R01.4 | Commercial Pattern Library v0 | Not authorized |
| WF-R01.5 | SEO Content Pattern Slice | Not authorized |
| WF-R01.6 | Blueprint & Registry Hygiene Pass | Not authorized |
| WF-R01.7 | Template-Art Multi-Site-Type Charter | Not authorized |
| WF-R01.8 | Execution Case → Registry Vocabulary Feed | Not authorized |
| WF-R01.X | Metrics, Gates & Roadmap Registration | Cross-cutting |

---

## Program Candidates

Кандидаты, проверенные по запросу (Parts 1–8):

| # | Candidate area | Question | Verdict |
|---|----------------|----------|---------|
| 1 | Production Modes | Самостоятельная программа или завершённое направление? | **Завершённое направление** — WF-A01 Complete |
| 2 | Validation Architecture | Самостоятельная программа или завершённое направление? | **Завершённое направление** — WF-A02 Complete |
| 3 | Strategy Layer | Отдельная программа (Framework / Commercial / Conversion)? | **SEED** — governance only; частично R01.4 |
| 4 | UX / Wireframe Layer | UX Expansion / Wireframe / Conversion Architecture Program? | **SEED** — workflow stage без SSOT; не program |
| 5 | Template-Art Layer | Часть WF-R01 или отдельная программа? | **Подпрограмма WF-R01.7** + mode WF-A01 |
| 6 | Agent Layer | Agent Expansion / Operationalization / Runtime Prep? | **SEED** — deferred to WF-A03 |
| 7 | Execution Cases Layer | Case Harvesting / Vocabulary / Reference Site Program? | **Подпрограмма WF-R01.8** + registry v1 |
| 8 | LOC-ZONE / Operations | Отдельная программа Project Operations? | **SEED** — substrate complete; enrollment partial |

---

## Candidate Classification

| Candidate | Status | Evidence | Comparable to WF-R01? | Separate roadmap track needed? |
|-----------|--------|----------|-------------------------|-------------------------------|
| **Production Modes (WF-A01)** | **PROGRAM** (Complete) | Charter + Pass 01; roadmap; OPERATIONAL-INDEX | Was architecture item, now **closed** | **No** — already registered and complete |
| **Validation Architecture (WF-A02)** | **PROGRAM** (Complete) | Charter + Pass 01/02; VL3 domains; roadmap | Was architecture item, now **closed** | **No** — already registered and complete |
| **Pixel Factory (WF-A03)** | **PROGRAM** (DEFERRED) | roadmap § WF-A03 deferred marker; explicit non-goals | **Yes** — registered deferred program | **No** — already on roadmap; not hidden |
| **Registry Expansion (WF-R01)** | **PROGRAM** (CHARTERED) | Program charter; program design; authority pass | **Yes** — reference program | **No** — current active program track |
| **Strategy Framework / Commercial Architecture** | **SEED** | `strategic-intent-governance.md`, commercial-density, cta-philosophy; Marketing Strategy Agent **planned**; maturity **3/10** (system audit) | **No** — governance pack, not program design | **No before R01.1** — Priority B slice; R01.4 covers conversion patterns |
| **Conversion System Program** | **SEED** | Commercial Pattern Library ~1 pattern; BLUEPRINT-GAPS G5 NOT queued | **No** | **No** — absorbed into **WF-R01.4** |
| **UX Expansion Program** | **SEED** | `design-layer-model.md`; UX Structure Agent **planned**; maturity **2/10** | **No** | **No before R01.1** — Priority C post-R01 |
| **Wireframe Program** | **SEED** | Workflow stage exists; format **TBD**; no wireframe SSOT | **No** | **No before R01.1** — explicit exclusion from WF-R01 core |
| **Conversion Architecture Program (UX-adjacent)** | **NONE** | No dedicated program artifact; conversion in blueprints + WF-A01 modes | **No** | **No** |
| **Template-Art Expansion** | **PROPOSAL** (within R01) | WF-A01 defines mode; WF-R01.7 designs multi-site-type charter | **Partial** — subprogram scope | **No** — **WF-R01.7**, not parallel program |
| **Agent Expansion / Operationalization** | **SEED** | 2/18 agents operational_doc_pack; Agent Runtime in WF-A03 non-goals | **No** — deferred | **No before R01.1** — WF-A03 or post-R01 honesty matrix (Priority B) |
| **Agent Runtime Preparation** | **PROPOSAL** (within A03) | WF-A03 explicit scope; forbidden until chartered | **Yes** when A03 starts | **No** — already WF-A03 |
| **Case Harvesting / Vocabulary Feed** | **PROPOSAL** (within R01) | `execution-cases-registry-v1.md`; WF-R01.8 in program design | **Partial** — subprogram | **No** — **WF-R01.8** |
| **Reference Site Program** | **SEED** | Triumph reference case + FP-0001 LOC; no program charter | **No** | **No** — case registry + R01.8 |
| **LOC-ZONE / Project Operations Program** | **SEED** | Waves 1–3 complete; FP-0001 enrolled; FP-0002 visibility-only | **No** — operational substrate, not expansion program | **No before R01.1** — enrollment decisions Priority B |
| **SEO Pattern / Content Program** | **PROPOSAL** (within R01) | SEO Architecture v2 ACCEPTED; content templates absent | **Partial** — subprogram | **No** — **WF-R01.5** |
| **Design Token / Design System Program** | **SEED** | DG-01–04 OPEN; explicitly **outside** WF-R01 core | **No** | **No before R01.1** — parallel Priority B |

**Status legend:**

| Status | Meaning in this pass |
|--------|----------------------|
| **NONE** | No program-like structure beyond scattered docs |
| **SEED** | Governance gap or operational need visible; no program design / charter pass |
| **PROPOSAL** | Scoped in an existing program design (WF-R01 subprogram or WF-A03) |
| **CHARTER_CANDIDATE** | Could warrant future program pass; **not** evidenced as hidden existing program |
| **PROGRAM** | Registered in roadmap with explicit status |

---

## Top Program Candidates

Рейтинг кандидатов **по приоритету регистрации** (если бы потребовалась **новая** программа уровня WF-R01). Фактически **ни один не блокирует WF-R01.1**:

| Rank | Candidate | Status | Priority rationale | Blocks WF-R01.1? |
|------|-----------|--------|--------------------|------------------|
| — | *(none at WF-R01 scale, unregistered)* | — | All major tracks already on roadmap or inside R01 | **No** |
| 1 | **WF-A03 Pixel Factory** | PROGRAM (DEFERRED) | Already registered; largest **future** program after R01 | **No** — explicitly downstream |
| 2 | **UX / Wireframe artifact program** | SEED → CHARTER_CANDIDATE | Layer maturity 2/10; blueprint→design cliff | **No** — post-R01 Priority C in audits |
| 3 | **Strategy artifact program** | SEED | strategy-memo-contract; upstream thin | **No** — Priority B; overlaps R01.4 |
| 4 | **LOC-ZONE portfolio operations program** | SEED | Partial enrollment; 3 visibility surfaces | **No** — operational hygiene, not registry cliff |
| 5 | **Agent operationalization program** | SEED | 16/18 planned; honesty matrix sufficient short-term | **No** — WF-A03 scope when deferred lifts |

**Active execution priority (не новая программа):** **WF-R01.1** remains the correct next step per authority chain.

---

## Hidden Program Analysis

### PART 1 — Production Modes

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **PROGRAM — Complete** (WF-A01) |
| **Evidence** | `website-factory-production-modes-charter-v1.md`; `reports/website-factory-production-modes-implementation-pass-01.md`; roadmap row **Complete (Pass 01)** |
| **Verdict** | **Завершённое направление**, не ongoing program. Intake gate, passport `production_mode`, QA router — **operational**. Не требует отдельного track. |

### PART 2 — Validation Architecture

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **PROGRAM — Complete** (WF-A02) |
| **Evidence** | `website-factory-validation-architecture-charter-v1.md`; `website-factory-vl3-domains-charter-v1.md`; Pass 01 + Pass 02 reports |
| **Verdict** | **Завершённое направление**. VL0–VL6 + VL3 domains — **documentation complete**; enforcement remains human-operated. Adoption gap ≠ hidden program. WF-A03 explicitly **excludes** duplicating WF-A02 automation scope until chartered. |

### PART 3 — Strategy Layer

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **SEED** |
| **Evidence** | `strategic-intent-governance.md`, `commercial-density-governance.md`, `commercial-landing-pressure-model.md`, `cta-philosophy-governance.md`; Marketing Strategy Agent **planned**; system audit maturity **3/10** |
| **Sub-candidates** | Strategy Framework — governance only. Commercial Architecture — policy docs, no `pattern_id` catalog (→ **WF-R01.4**). Conversion System — ~1 documented pattern (`scroll_process_timeline`) |
| **Verdict** | **Нет отдельной программы**. Gap acknowledged in audits as Priority B `strategy-memo-contract-v1` — **documentation slice**, not WF-R01-scale program. Commercial/conversion expansion **already scoped** under WF-R01.4. |

### PART 4 — UX / Wireframe Layer

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **SEED** (CHARTER_CANDIDATE for **future**, not hidden **existing**) |
| **Evidence** | `layer-map.md` §4; `design-layer-model.md`; Wireframe Generator / UX Structure agents **planned**; system audit **2/10**; FP-0002 uses Group Decomposition / Layout Spec as **PIXEL substitute**, not universal UX SSOT |
| **Sub-candidates** | UX Expansion Program — **NONE**. Wireframe Program — **NONE**. Conversion Architecture Program — **NONE** as named program |
| **Verdict** | **Существенный layer gap**, но **не оформлен** как program. WF-R01 program design **explicitly excludes** wireframe contract from core (`foundry-registry-expansion-program-design-v1.md` exclusions: «Wireframe artifact contract v1 — Phase 4 tail or post-R01»). Future program pass **возможен после R01**, не параллельно скрытый. |

### PART 5 — Template-Art Layer

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **PROPOSAL** — subprogram **WF-R01.7** |
| **Evidence** | WF-A01 defines `TEMPLATE_ART` mode (Complete). WF-R01.7 «Template-Art Multi-Site-Type Charter» in program design. Capability audit: effective scope **LANDING-only** until structural blocks + reference expansion |
| **Verdict** | **Часть WF-R01**, не отдельная программа. Mode contract = WF-A01; expansion policy = WF-R01.7. |

### PART 6 — Agent Layer

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **SEED** (runtime scope → **WF-A03 PROPOSAL**) |
| **Evidence** | `agent-map.md`; `agents/registry.md` §4.1 — 18 cards, **2** operational_doc_pack (`gulp_frontend_agent`, `mars_forge_frontend_agent`); WF-A03 non-goals include **Agent Runtime** |
| **Sub-candidates** | Agent Expansion — **SEED**. Agent Operationalization — Priority B honesty matrix in audits, not program. Agent Runtime Preparation — **WF-A03** when DEFERRED lifts |
| **Verdict** | **Нет скрытой программы**. Upstream agents **planned** by design; expansion **explicitly deferred** to WF-A03, not parallel hidden track. |

### PART 7 — Execution Cases Layer

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **PROPOSAL** — subprogram **WF-R01.8** + operational registry |
| **Evidence** | `execution-cases-registry-v1.md` (3 cases); WF-R01.8 «Execution Case → Registry Vocabulary Feed»; Triumph, ISBD, BZPM, FP-0001/0002 lessons |
| **Sub-candidates** | Case Harvesting — **R01.8**. Vocabulary Harvest — **R01.8 + R01.1 binding**. Reference Site Program — Triumph/FP-0001 exist; **no** separate program charter |
| **Verdict** | Case normalization **внутри WF-R01.8**; registry v1 **operational**, не program. BZPM/Sibcar enrollment — **HITL decisions**, not new program. |

### PART 8 — LOC-ZONE / Operations Layer

| Field | Assessment |
|-------|------------|
| **Hidden program?** | **No** |
| **Status** | **SEED** |
| **Evidence** | `workspaces/website-factory-operations/README.md` — Waves 1–3 **complete**; FP-0001 ROC-enrolled; FP-0002 visibility-only; passport fields from WF-A01/A02 |
| **Verdict** | **Substrate proven** (C2–C7 on FP-0001). Portfolio-wide operations **immature** but **not** a hidden WF-R01-scale program — enrollment/enrollment policy = Priority B hygiene, optionally post-R01 Gate 2. |

### Cross-check — already visible «large» programs not in Parts 1–8

| Item | Hidden? | Notes |
|------|---------|-------|
| **WF-A03 Pixel Factory** | **No** — roadmap DEFERRED | Vision, Visual Diff, Pixel QA, Screenshot Engine, Agent Runtime |
| **Frontend Waves 1–6 / Evolution Packs** | **No** | Operational governance packs; integrated into OPERATIONAL-INDEX, not separate programs |
| **Physical Artifact Waves (LOC-ZONE C2–C7)** | **No** | Complete substrate; not ongoing expansion program |
| **WPilot / WordPress bridge** | **No** | Planned integration; `AG-WP-001` internal seed only |

---

## Risks

| Risk | Severity | If ignored before WF-R01.1 |
|------|----------|----------------------------|
| **False discovery narrative** — inventing parallel programs and delaying R01.1 | **High** | Registry cliff persists; dual canon (XD-01) continues |
| **Confusing SEED gaps with hidden PROGRAM** | **Medium** | Program sprawl; governance bloat |
| **Starting WF-A03** believing UX/Agent gaps require parallel program | **Medium** | Pixel automation without composition truth (audits reconfirm) |
| **TEMPLATE_ART on CATALOG** before R01.2 structural blocks | **Critical** | False completeness — mitigated by pending R01.7, not new program |
| **Treating CHARTERED WF-R01 as ACTIVE** | **Critical** | Unauthorized registry edits — mitigated by R01.1 gate |
| **LOC-ZONE / case silos** without R01.8 | **Medium** | Lessons trapped in OCPilot/BZPM — **R01.8 scope**, not new program |

---

## SAFE UNKNOWN

- **FOUNDRY** как именованный продукт/путь в tree — **не обнаружен**.
- Будет ли **UX/Wireframe** когда-либо оформлен как отдельная WF-Axx/Rxx program — **не зафиксировано**; сегодня только audit Priority C recommendation.
- Единый owner **Strategy artifact slice** vs **WF-R01.4** boundary — **не formalized** beyond program design exclusions.
- **VL3 adoption rate** на Triumph v6 / ISBD — **не аудирован** в этом pass.
- **OCPilot Site-001** production_mode и registry binding — **не verified** here.
- **Operator waiver** для WF-A03 до WF-R01 Gate 2+ — **recommended**, not chartered.
- Formal **Program Authority Model** в `governance/` — **не обнаружен**; статусы **выведены** из WF-Axx precedent (authority pass).

---

## Final Verdict

### Option A — **Recommended**

**No additional program required. Proceed to WF-R01.1.**

**Обоснование:**

1. **Все программы уровня roadmap уже видимы:** WF-A01 ✅ · WF-A02 ✅ · WF-R01 CHARTERED · WF-A03 DEFERRED.
2. **Кандидаты, похожие на «скрытые программы»**, либо **завершены** (A01/A02), либо **отложены официально** (A03), либо **уже декомпозированы** в подпрограммы WF-R01 (R01.4 Commercial Pattern, R01.5 SEO slice, R01.7 Template-Art, R01.8 Execution Cases).
3. **Оставшиеся gaps** (Strategy memo, UX/wireframe SSOT, LOC-ZONE enrollment, Agent honesty matrix) — **SEED / Priority B–C** в system-wide audit; **не** имеют program design, charter pass, или scope сопоставимого с WF-R01 (8 subprograms + cross-cutting metrics + registry cliff closure).
4. **Блокер перед R01.1** — не отсутствие другой программы, а **неопубликованный ACCEPTED binding charter** (`wf-r01-1-v0-v1-binding-charter-v1.md`).

### Option B — **Not recommended**

~~Register program X before WF-R01.1~~

**Не применимо.** Ни один кандидат не удовлетворяет одновременно: (a) фактически присутствует как **скрытая** program-level структура, (b) имеет scope **сопоставимый с WF-R01**, (c) **не** покрыт существующим WF-R01 / WF-A03 / Complete A01/A02.

**Если оператор захочет post-R01 expansion:** наиболее вероятные **CHARTER_CANDIDATE** (не сейчас): UX/Wireframe artifact program (post Gate 2+) · WF-A03 execution (после Research Pass) · LOC-ZONE portfolio enrollment program (Priority B hygiene).

---

**STOP — NO IMPLEMENTATION — NO DOCUMENT CHANGES (кроме создания этого отчёта)**

---

*Discovery artifact: `reports/foundry-program-discovery-pass-v1.md`*  
*Evidence base: roadmap.md, OPERATIONAL-INDEX.md, foundry-registry-layer-audit-v1.md, foundry-system-wide-layer-audit-v1.md, foundry-capability-gap-audit-v1.md, foundry-registry-expansion-program-design-v1.md, wf-r01-registry-expansion-program-charter-v1.md, wf-r01-program-authority-pass-v1.md, wf-r01-charter-pass-design-v1.md, wf-r01-1-v0-v1-binding-charter-design-v1.md, website-factory-production-modes-charter-v1.md, website-factory-validation-architecture-charter-v1.md, website-factory-vl3-domains-charter-v1.md, layer-map.md, agent-map.md, execution-cases-registry-v1.md, site-type-registry-v0.md, block-registry-v0.md, LOC-ZONE README, strategic-intent-governance.md.*
