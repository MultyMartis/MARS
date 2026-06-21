# REPORT — WEBSITE FACTORY VL3 VALIDATION DOMAINS

**Date:** 2026-06-18  
**Scope:** Architecture design only — **no implementation**, **no governance edits**, **no runtime**.  
**Task:** WF-A02 Pass 02 prerequisite — internal architecture of **VL3 Composition & Extract Validation**  
**Authority chain:** [website-factory-validation-architecture-charter-v1.md](../projects/mars-website-factory/website-factory-validation-architecture-charter-v1.md) (WF-A02 Pass 01)  
**Evidence base:** [website-factory-validation-architecture-audit-v1.md](website-factory-validation-architecture-audit-v1.md) · [website-factory-validation-architecture-design-v1.md](website-factory-validation-architecture-design-v1.md) · [website-factory-validation-architecture-implementation-pass-01.md](website-factory-validation-architecture-implementation-pass-01.md) · [FP-0002-STRESS-TEST-FORENSIC-v1.md](FP-0002-STRESS-TEST-FORENSIC-v1.md)

**Honesty boundary:** VL3 validation domains described here are **documented, human-operated contracts**. No Instance Resolver product, Asset Identity Registry engine, or automated ordering diff is claimed in-repo. Project-local scripts may later satisfy evidence classes; Factory does **not** claim global automation in this pass.

---

## Executive Summary

**VL3 — Composition & Extract Validation** — критический слой Validation Architecture. FP-0002 доказал, что **большинство критических дефектов** (12 PARTIAL + 2 FAIL forensic при 15/15 build PASS) возникают **до и во время generation**, внутри composition/extract, а не на этапе compile.

Pass 01 канонизировал VL3 как единый слой с пятью sub-layers (VL3a–VL3e). **Pass 02 проектирует внутреннюю архитектуру** — шесть validation domains, границы ответственности, проверки, failure classes и интеграцию с VL2/VL4/VL5.

**Ключевые архитектурные решения v1:**

| Decision | Choice |
|----------|--------|
| **VL3 internal map** | **6 domains** — VL3e (foundation) → VL3a → VL3b ∥ VL3d → VL3c → VL3f |
| **Component Extraction** | Sub-contract внутри **VL3a Instance Resolver** — не отдельный слой |
| **Text Extraction** | Upstream contract внутри **VL3d Text Lock** — extract quality gate до lock |
| **Mapping** | **VL2 boundary** — VL3 consumes Mapping QA output; не дублирует VL2 |
| **Assembly Decision** | Отдельный domain **VL3f** — governance gate перед generation |
| **Pre-build blocking** | VL3b Asset Identity + VL3a Instance Resolver — **STOP before wire** |
| **PIXEL_PERFECT** | Full VL3 stack mandatory; PARTIAL на Critical entity blocks VERIFIED |
| **Failure registry** | Prefix codes: **IR-** · **AI-** · **VO-** · **TL-** · **AD-** · **GL-** |

**Вердикт:** VL3 — **partially documented, not gated as unified layer** (audit). Этот документ — **design target для WF-A02 Pass 02** (documentation integration, not runtime).

---

## VL3 Structure

### Position in Validation Architecture

```text
VL2 — Design Contract Validated
         │
         │  handoff: Mapping QA record, Standards APPROVED,
         │           FIG extract, component type inventory
         ▼
┌────────────────────────────────────────────────────────────────┐
│  VL3 — COMPOSITION & EXTRACT VALIDATION                        │
│                                                                │
│  VL3e  Composition Foundation (Group / Layout Spec)            │
│    └─► VL3a  Instance Resolver (+ Component Extraction)      │
│           ├─► VL3b  Asset Identity                             │
│           └─► VL3d  Text Lock (+ Text Extraction contract)     │
│                 └─► VL3c  Visual Ordering                      │
│                       └─► VL3f  Assembly Decision              │
│                             └─► COMPOSITION_VALIDATED          │
└────────────────────────────────────────────────────────────────┘
         │
         ▼
    [GENERATION] ──► VL4 (BUILT) ──► VL5 (VERIFIED) ──► VL6
```

### Domain registry

| ID | Domain | Charter alias | Primary question |
|----|--------|---------------|------------------|
| **VL3e** | Composition Foundation | Group / Layout Spec | Are discrete groups registered and Layout Spec APPROVED? |
| **VL3a** | Instance Resolver | Instance Resolver | Are FIG INSTANCE subtrees enumerated and bound to HTML slots? |
| **VL3b** | Asset Identity | Asset Identity | Is every wired asset uniquely identified and collision-free? |
| **VL3d** | Text Lock | Text Lock | Is all in-scope copy locked, partial, or explicitly forbidden to generate? |
| **VL3c** | Visual Ordering | Visual Ordering | Does planned DOM order match visual SSOT contract? |
| **VL3f** | Assembly Decision | *(new — charter gap)* | May Factory auto-assemble, escalate, or must stop? |

### Cross-cutting concepts (not separate domains)

| Concept | Owner domain | Rationale |
|---------|--------------|-----------|
| **Component Extraction** | VL3a | Extraction is means; validation target is **instance truth** |
| **Text Extraction** | VL3d (upstream) | Flat TEXT extract quality gate precedes lock/diff |
| **Mapping** | VL2 → VL3 handoff | Design → Frontend Mapping QA completes at VL2; VL3 consumes artifacts |
| **Group Register** | VL3e | GROUP-ID register is prerequisite for VL3a instance walk |

### Execution order (validation, not necessarily agent turn order)

| Phase | Domains | Blocking rule |
|-------|---------|---------------|
| **P0 — Foundation** | VL3e | No VL3a–VL3f without APPROVED Layout Spec (PIXEL) |
| **P1 — Structure truth** | VL3a | INSTANCE-heavy sections: instance walk before assets/text |
| **P2 — Slot binding** | VL3b, VL3d | Parallel validation; both must PASS or explicit PARTIAL disposition |
| **P3 — Page composition** | VL3c | Section order contract before cross-section assembly |
| **P4 — Build authorization** | VL3f | COMPOSITION_VALIDATED emitted only when P0–P3 satisfied or escalated |

### VL3 exit state

| Field | Definition |
|-------|------------|
| **State token** | `COMPOSITION_VALIDATED` |
| **Minimum artifacts** | Group Register · APPROVED Layout Spec · Instance enumeration record (where applicable) · Asset manifest · Text lock manifest · Visual order record · Assembly Decision record (if conflict) |
| **Lifecycle** | **No BUILT claim** at VL3 — generation authorized, not verified |
| **Mode fork** | PIXEL: full stack · TEMPLATE: VL3e optional; VL3b brand-only; VL3a/VL3c reduced |

### Sub-layer evolution (Pass 01 → Pass 02)

| Pass 01 (charter) | Pass 02 (this doc) | Change |
|-------------------|--------------------|--------|
| VL3a–VL3e flat list | Ordered dependency graph | Adds execution semantics |
| Assembly Decision in VL3c notes | **VL3f** separate domain | Separates **order contract** from **build authorization** |
| Component Extraction implicit | Explicit VL3a sub-contract | Names extraction as input gate |
| Text Extraction implicit | VL3d upstream gate | Anti-paraphrase requires extract completeness check |

---

## Instance Resolver Domain

**ID:** VL3a  
**Failure prefix:** `IR-`  
**Charter:** VL3a Instance Resolver Validation

### Purpose

Ensure **FIG component instances** (`INSTANCE` nodes, typed symbols) are **enumerated, counted, and bound** to planned HTML slots **before** generation — replacing flat TEXT extract blindness (FAIL-006).

### What counts as an instance

| Instance class | Definition | FIG signals | HTML target |
|----------------|------------|-------------|-------------|
| **Component instance** | `INSTANCE` node referencing a `COMPONENT` symbol | `type: INSTANCE`, `componentId`, symbol name | Card, row, accordion item, review block |
| **Repeating visual unit** | Same symbol repeated N times in section frame | Enumeration in Group Register | N sibling elements with distinct content |
| **Named symbol match** | Symbol name matches Factory component vocabulary | `отзыв`, `Врач`, `Статья`, `Пункт услуги`, `этап`, `Расскрытие вопроса` | Section-specific slot map |
| **NOT an instance** | Frame-level export blob, decorative GROUP without symbol, single TEXT node | FRAME export, unnamed GROUP | — |

**Instance identity key (normative):**

```text
instance_key = section_id + ":" + fig_node_id + ":" + symbol_name + ":" + instance_index
```

### Component Extraction sub-contract (VL3a.1)

| Check | Validation | Failure if |
|-------|------------|------------|
| **CE-01** Symbol visibility | INSTANCE subtree reachable in extract | Flat extract has 0 instances but Discovery flagged components → **STOP** |
| **CE-02** Per-instance TEXT walk | Each instance has text leaf inventory | Body text missing for card-type instance → **PARTIAL** or **STOP** (PIXEL) |
| **CE-03** Per-instance IMAGE walk | Each instance has image leaf inventory | Image slot empty → **PARTIAL** (PIXEL Critical for hero/card) |
| **CE-04** Instance count | `fig_instance_count == planned_html_slot_count` | Mismatch → **FAIL** (`IR-001`) |
| **CE-05** Instance uniqueness | No duplicate `instance_key` in register | Collision → **FAIL** (`IR-002`) |

### Validations (VL3a checklist)

| ID | Check | PIXEL | TEMPLATE | Signal |
|----|-------|:-----:|:--------:|--------|
| IR-V01 | Group Register lists INSTANCE-heavy groups | M | Opt | STOP if missing |
| IR-V02 | Instance enumeration complete per section | M | Opt | STOP if invisible |
| IR-V03 | Instance count ↔ slot count | M | Opt | FAIL |
| IR-V04 | Per-instance text inventory | M | Opt | PARTIAL / STOP |
| IR-V05 | Per-instance image inventory | M | Opt | PARTIAL |
| IR-V06 | Symbol name ↔ Factory vocabulary | M | Opt | SAFE UNKNOWN |
| IR-V07 | Generic placeholder detection | M | — | FAIL if «Специалист центра» pattern |

### Failure classes

| Code | Title | Severity | Trigger | Pipeline effect |
|------|-------|----------|---------|-----------------|
| **IR-001** | Instance count mismatch | Critical | FIG N instances ≠ HTML N slots | **STOP** section build (PIXEL) |
| **IR-002** | Duplicate instance key | Major | Two instances map to same slot | **FAIL** |
| **IR-003** | INSTANCE subtree invisible | Critical | Flat extract; no Group Register pass | **STOP** (charter) |
| **IR-004** | Component text not extracted | Critical | Card shell without body text in extract | **STOP** generative fill (PIXEL) |
| **IR-005** | Generic placeholder substitution | Critical | Human-readable generic label where FIG has named instance | **FAIL** |
| **IR-006** | Symbol vocabulary unknown | Major | Symbol not in vocabulary | **SAFE UNKNOWN** → HITL |
| **IR-007** | Cross-instance content bleed | Major | Same text/hash bound to multiple instances incorrectly | **FAIL** |

### Evidence

| Class | Artifact |
|-------|----------|
| E2 | Instance enumeration record per section |
| E2 | Group Register with GROUP-IDs |
| E1 | `instance_key → slot_id` mapping table |
| E3 | Instance text inventory ↔ planned HTML strings |

---

### FP-0002 — Instance Resolver mapping

#### Specialists (SECTION-12) — FAIL

| Field | Value |
|-------|-------|
| **Forensic** | FAIL-008 — «Специалист центра» ×3; same photo ×3 |
| **Root cause** | `Врач` component instances not enumerated; names/photos not extracted per instance |
| **Would trigger** | IR-001 (count may match 3 but content identical), IR-005, IR-004 |
| **Required fix path** | Enumerate `Врач` instances; map unique image hashes per card |

#### Reviews (SECTION-05) — PARTIAL

| Field | Value |
|-------|-------|
| **Forensic** | FAIL-002 — review bodies hallucinated; FIG has 5 text nodes (title, meta, disclaimer) — no review bodies |
| **Root cause** | `отзыв` component text not extracted; generator filled generic copy |
| **Would trigger** | IR-004, IR-003; TL-003 (generative fill) |
| **Required fix path** | Component-instance text walker for `отзыв`; forbid generative fill |

#### Articles (SECTION-13) — FAIL

| Field | Value |
|-------|-------|
| **Forensic** | FAIL-009 — invented titles; CSS gradient placeholders |
| **Root cause** | `Статья` component images not extracted/linked |
| **Would trigger** | IR-004, IR-005; AI-006 (unconnected export) |
| **Required fix path** | Per-article asset extraction from component symbol |

#### FAQ (SECTION-14) — PARTIAL

| Field | Value |
|-------|-------|
| **Forensic** | Form shell OK; accordion Q&A invented; sidebar image missing |
| **Root cause** | `Расскрытие вопроса` instances not walked |
| **Would trigger** | IR-004, IR-001 (accordion item count) |
| **Required fix path** | Walk `Расскрытие вопроса` instances; bind sidebar image |

#### Cards (cross-section) — PARTIAL / FAIL pattern

| Section | Component | Forensic | IR codes |
|---------|-----------|----------|----------|
| S03 Services | `Пункт услуги` / `Услуга` | FAIL-015 — invented links + cards | IR-001, IR-004 |
| S07 Program | `этап` | FAIL-014 — invented card bodies | IR-004 |
| S04 Why-us | stat pairs | FAIL-012 — descriptions dropped | IR-004 (adjacent TEXT pairing) |
| S09 Advantages | card bodies | Generated titles/bodies | IR-004, IR-005 |

---

## Asset Identity Domain

**ID:** VL3b  
**Failure prefix:** `AI-`  
**Charter:** VL3b Asset Identity Validation  
**Existing foundation:** [failures/asset-identity-collision-v1.md](../projects/mars-website-factory/failures/asset-identity-collision-v1.md) — `ASSET_IDENTITY_COLLISION`

### Purpose

Ensure every raster/SVG wired to HTML is **uniquely identified**, **correctly scoped**, and **bound** via manifest — before assembly. Forbid frame-export pollution, hash collisions, orphan exports, and unconnected assets.

### Asset identity record (normative shape)

```text
asset_record {
  section_id      : string
  slot_id         : string          // logical HTML slot (logo, card-2-photo, hero)
  fig_node_id     : string
  export_hash     : string          // content hash
  file_path       : string          // src/img/...
  node_class      : LEAF_IMAGE | BRAND_MARK | ICON | DECORATIVE
  binding_status  : BOUND | ORPHAN | UNCONNECTED | COLLISION
}
```

### Pre-build validations (must pass before wire)

| ID | Check | Description | Signal |
|----|-------|-------------|--------|
| AI-V01 | **No frame-level export as slot image** | FRAME bounds export forbidden as content image | **STOP** (`AI-001`) |
| AI-V02 | **Hash uniqueness per slot** | Same hash in >1 slot without explicit reuse approval | **FAIL** (`AI-002`) |
| AI-V03 | **Brand chain** | Logo/favicon: nodeId + hash + brand text association | **STOP** (`AI-003`) |
| AI-V04 | **Leaf selection by area** | Prefer largest-area IMAGE leaf, not first traversal | **FAIL** if wrong leaf |
| AI-V05 | **Orphan export ratio** | `orphan_count / export_count` within threshold | **PARTIAL** if >50% (FP-0002: 56%) |
| AI-V06 | **Manifest completeness** | Every `src` in planned HTML has manifest row | **FAIL** |
| AI-V07 | **Unconnected export** | Export exists but no slot binding | **PARTIAL** (PIXEL) / note (TEMPLATE) |
| AI-V08 | **Collision registry** | Known collision hashes blocklisted | **STOP** |

### Failure classes

| Code | Title | Severity | FP-0002 | Pipeline effect |
|------|-------|----------|---------|-----------------|
| **AI-001** | Frame-export pollution | Critical | FAIL-004 `d3ac7d00` | **STOP** before wire |
| **AI-002** | Hash collision across slots | Critical | FAIL-004 — same hash 10+ sections | **STOP** or **FAIL** |
| **AI-003** | Brand identity collision | Blocker | FAIL-017 — Skinerica vs Shpigovsky | **STOP** before wire |
| **AI-004** | First-image-as-logo heuristic | Critical | FAIL-017 root cause | **STOP** |
| **AI-005** | Orphan asset majority | Major | FAIL-005 — 56% unused | **PARTIAL** → blocks VERIFIED |
| **AI-006** | Unconnected export | Major | FAIL-009 — article thumbnails | **FAIL** (Critical slot) |
| **AI-007** | Missing manifest row | Major | No `section → nodeId → src` | **FAIL** |
| **AI-008** | Duplicate file, distinct slots | Major | Same file wired 3× (specialists photo) | **FAIL** |
| **AI-009** | Export without reference | Medium | Intro image exported, unused | **PARTIAL** |

### d3ac7d00 collision — dissected

| Field | Value |
|-------|-------|
| **Symptom** | `genotyping-d3ac7d00.jpg` in HTML; hash in S02,S03,S04,S06,S07,S08,S09,S11,S12,S14 |
| **Mechanism** | FIG parser exports section **FRAME** as image; identical hash across sections |
| **Detection** | AI-V01: `node_class == FRAME` → reject · AI-V02: hash appears >N sections → **STOP** |
| **Remediation** | Exclude FRAME-level exports; rank leaf IMAGE by area; maintain hash dedup registry |
| **Pre-build gate** | AI-V08 blocklist entry for known frame-export pattern |

### Duplicate / orphan / unconnected taxonomy

| Term | Definition | Validation | FP-0002 example |
|------|------------|------------|-----------------|
| **Duplicate assets** | Same `export_hash` bound to multiple unrelated slots | AI-V02, AI-V08 | Specialists photo ×3 |
| **Orphan assets** | File on disk, not referenced in planned HTML | AI-V05 | ~19 of 36 files |
| **Unconnected exports** | Export in manifest without `slot_id` binding | AI-V06, AI-V07 | Article thumbnails never wired |

### Evidence

| Class | Artifact |
|-------|----------|
| E1 | Asset manifest JSON — full `asset_record` set |
| E2 | Brand chain checklist (nodeId, hash, brand text) |
| E1 | Hash dedup registry / blocklist |
| E3 | Manifest ↔ planned HTML `src` diff |

---

## Visual Ordering Domain

**ID:** VL3c  
**Failure prefix:** `VO-`  
**Charter:** VL3c Visual Ordering Validation

### Purpose

Define and validate **section and in-section visual order contract** — resolving conflicts between FIG layer child index, visual Y position, and planned DOM order. FP-0002 SECTION-10 is the canonical failure.

### Ordering dimensions (three-axis model)

| Axis | Source | Scope | Primary use |
|------|--------|-------|-------------|
| **Visual Y** | `bounds.y` (FIG absolute coordinates) | Cross-section page flow | **Primary** for PIXEL page assembly |
| **Layer Order** | FIG layer child index | Sibling order within parent | **Fallback**; tie-breaker |
| **DOM Order** | Planned HTML `<section>` sequence | Rendered document flow | **Output contract** — must match resolved order |

### Order contract (normative)

```text
RESOLVED_ORDER = sort(sections, key=visual_y, stable_tie=layer_index)

IF exists(section_pair) WHERE abs(y_a - y_b) > Y_THRESHOLD
   AND layer_index_order != visual_y_order
THEN conflict = TRUE
     REQUIRE assembly_decision_record (VL3f)
     FORBID silent layer-index default (PIXEL)
```

| Parameter | Default | Notes |
|-----------|---------|-------|
| `Y_THRESHOLD` | Project-scoped (e.g. 100px) | Tunable per FIG coordinate space |
| `stable_tie` | Layer index ascending | When \|Δy\| ≤ threshold |

### SECTION-10 FAIL — dissected

| Field | Value |
|-------|-------|
| **Section** | SECTION-10 `Слово спецу` (SPECIALIST-WORD) |
| **Visual Y** | `y=2389` — between S02 (`y=1029`) and S03 (`y=3000`) |
| **Layer index** | After S09 in FIG children |
| **DOM (dist)** | After S09 — follows layer index |
| **Verdict** | **Visual order drift** — wrong page position |
| **Would trigger** | VO-001 conflict · AD-001 unresolved |

### Validations

| ID | Check | PIXEL | Signal |
|----|-------|:-----:|--------|
| VO-V01 | Compute `RESOLVED_ORDER` from visual Y | M | — |
| VO-V02 | Compare vs layer-index-only order | M | Conflict detection |
| VO-V03 | Compare vs planned DOM order | M | FAIL if mismatch |
| VO-V04 | Discovery anomaly flags reconciled | M | STOP if open |
| VO-V05 | In-section element order (GROUP-IDs) | M | PARTIAL if wrong |
| VO-V06 | Structural IA override documented | M | Requires AD record |

### Failure classes

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **VO-001** | Y vs layer-index conflict | High | Requires VL3f decision |
| **VO-002** | DOM order ≠ resolved order | Critical | **FAIL** |
| **VO-003** | Silent layer-index default | Critical | **STOP** (PIXEL) — FAIL-007 class |
| **VO-004** | Discovery anomaly unresolved | High | **STOP** |
| **VO-005** | In-section visual order drift | Major | **PARTIAL** |
| **VO-006** | IA override without record | Major | **STOP** |

### Evidence

| Class | Artifact |
|-------|----------|
| E1 | Ordered section list: `section_id, visual_y, layer_index, dom_index` |
| E2 | Conflict flag report |
| E2 | Cross-ref to Assembly Decision record (VL3f) |

---

## Text Lock Domain

**ID:** VL3d  
**Failure prefix:** `TL-`  
**Charter:** VL3d Text Lock Validation

### Purpose

Define **text state** per string slot before generation; forbid generative paraphrase in PIXEL_PERFECT; gate Text Extraction quality upstream.

### Text Extraction sub-contract (VL3d.0)

Text Lock cannot validate what Text Extraction did not surface.

| Gate | Check | Failure |
|------|-------|---------|
| TE-01 | Flat extract vs INSTANCE walk coverage | INSTANCE text missing → **STOP** walk first |
| TE-02 | Section-scoped binding | Cross-section text bleed → **FAIL** (FAIL-016) |
| TE-03 | Multi-paragraph preservation | `\n` splits preserved → blocks truncation (FAIL-013) |
| TE-04 | Adjacent node pairing | Stat NUMBER + DESCRIPTION paired (FAIL-012) |

### Text state machine

| State | Definition | PIXEL allowed action | HTML generation |
|-------|------------|----------------------|-----------------|
| **LOCKED** | String in extract/manifest with node provenance | Use verbatim | Required exact match |
| **PARTIAL** | Heading present; body incomplete or truncated | **STOP** or HITL — no paraphrase | Forbidden auto-fill |
| **UNKNOWN** | Slot identified; no extract string | **STOP** + HITL | Forbidden generate |
| **FORBIDDEN TO GENERATE** | Policy — PIXEL mode | Never invent copy | **STOP** if attempted |
| **SUPPLEMENT** | TEMPLATE_ART only — content deck fills gap | Allowed in bounds | With provenance |

**PIXEL_PERFECT rule:**

```text
IF text_state(slot) NOT IN { LOCKED }
AND production_mode == PIXEL_PERFECT
THEN generation_action = FORBIDDEN
     signal = STOP (TL-003)
```

### State assignment rules

| Condition | State |
|-----------|-------|
| FIG nodeId + exact string in extract | **LOCKED** |
| Heading LOCKED; body missing from extract | **PARTIAL** |
| Slot in Layout Spec; no extract entry | **UNKNOWN** |
| Agent attempts paraphrase / generic filler | **FORBIDDEN TO GENERATE** (violation) |
| TEMPLATE + approved content deck string | **SUPPLEMENT** (not PIXEL) |

### Validations

| ID | Check | PIXEL | Signal |
|----|-------|:-----:|--------|
| TL-V01 | All Critical slots have state assigned | M | STOP if UNKNOWN |
| TL-V02 | LOCKED strings have node provenance | M | FAIL |
| TL-V03 | No generative fill on UNKNOWN/PARTIAL | M | **STOP** |
| TL-V04 | `section-NN.lock.json` present (recommended) | Rec | PASS aid |
| TL-V05 | Section-scoped text binding | M | FAIL on bleed |
| TL-V06 | Multi-paragraph blocks complete | M | PARTIAL |
| TL-V07 | Disclaimer / meta text rendered | M | PARTIAL |

### Failure classes

| Code | Title | Severity | FP-0002 |
|------|-------|----------|---------|
| **TL-001** | Paraphrase drift | High | FAIL-003 intro |
| **TL-002** | Invented body copy | Critical | FAIL-002, 007, 014, 015 |
| **TL-003** | Generative fill on missing extract | Critical | Charter §7 |
| **TL-004** | Text truncation | Major | FAIL-013 quote |
| **TL-005** | Adjacent pair loss | Major | FAIL-012 stats |
| **TL-006** | Section scope bleed | Medium | FAIL-016 disclaimer |
| **TL-007** | UNKNOWN slot unescalated | Critical | — |
| **TL-008** | Lock file / extract mismatch | Major | — |

### Evidence

| Class | Artifact |
|-------|----------|
| E1 | `section-NN.lock.json` or text lock manifest |
| E3 | FIG string ↔ planned HTML diff |
| E2 | Anti-generative-fill attestation |
| E2 | Per-slot state table |

---

## Assembly Decision Domain

**ID:** VL3f  
**Failure prefix:** `AD-`  
**Charter gap:** Partially in VL3c / charter ASSEMBLY DECISION — **elevated to domain** in Pass 02

### Purpose

Govern **when Factory may auto-assemble**, **when it must escalate (HITL)**, and **when it must stop** — converting composition conflicts into explicit decisions, not silent defaults.

### Decision outcomes

| Outcome | Definition | When allowed |
|---------|------------|--------------|
| **AUTO_ASSEMBLE** | Proceed to generation without HITL | All VL3 domains PASS; no VO conflict; no SAFE UNKNOWN |
| **ESCALATE** | HITL required; decision record before generation | VO-001 conflict; IR-006 unknown symbol; ambiguous IA |
| **STOP_ASSEMBLY** | No generation until resolved | STOP triggers; brand collision; generative fill attempt; unresolved conflict |

### Decision matrix

| Condition | Outcome | Record required |
|-----------|---------|-----------------|
| All VL3a–VL3e PASS; VO no conflict | **AUTO_ASSEMBLE** | Composition validation summary |
| VO-001 Y vs layer conflict | **ESCALATE** | Assembly Decision Record |
| IR-003 INSTANCE invisible | **STOP_ASSEMBLY** | — |
| AI-003 brand collision | **STOP_ASSEMBLY** | — |
| TL-003 generative fill attempted | **STOP_ASSEMBLY** | — |
| IR-006 symbol unknown | **ESCALATE** | HITL vocabulary decision |
| Structural IA overrides visual Y | **ESCALATE** | AD record + Lead ack |
| TEMPLATE_ART + blueprint order | **AUTO_ASSEMBLE** | Blueprint reference |
| Exception Registry waiver | **ESCALATE** | Waiver ID in E0 |

### Assembly Decision Record (shape)

```text
assembly_decision_record {
  decision_id       : string
  conflict_type     : VISUAL_ORDER | IA_OVERRIDE | INSTANCE_UNKNOWN | ...
  sections_affected : string[]
  visual_y_order    : string[]
  layer_index_order : string[]
  chosen_dom_order  : string[]
  rationale         : string
  decided_by        : HITL | AUTO_POLICY
  timestamp         : ISO-8601
}
```

### Failure classes

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **AD-001** | Unresolved order conflict | Critical | **STOP** — FAIL-007 |
| **AD-002** | Silent default applied | Critical | **STOP** |
| **AD-003** | Missing decision record | Major | **STOP** generation |
| **AD-004** | IA override without authority | Major | **STOP** |
| **AD-005** | AUTO_ASSEMBLE with open SAFE UNKNOWN | Major | **STOP** |
| **AD-006** | ESCALATE not completed | Major | **STOP** |

### Evidence

| Class | Artifact |
|-------|----------|
| E2 | Assembly Decision Record (when ESCALATE) |
| E2 | AUTO_ASSEMBLE attestation checklist |
| E0 | HITL sign-off on conflict resolution |

---

## Validation Signals

Per-domain signal semantics. Cross-ref charter §4.

### Signal applicability matrix

| Signal | VL3e | VL3a | VL3b | VL3d | VL3c | VL3f | Blocks GEN | Blocks VERIFIED |
|--------|:----:|:----:|:----:|:----:|:----:|:----:|:----------:|:---------------:|
| **PASS** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | contributes |
| **PARTIAL** | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ PIXEL Critical |
| **FAIL** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ context | ✓ |
| **STOP** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **SAFE UNKNOWN** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ until resolved |

### Per-domain PASS criteria (summary)

| Domain | PASS means |
|--------|------------|
| **VL3e** | Group Register complete; Layout Spec APPROVED |
| **VL3a** | Instance enumeration complete; count match; no placeholders |
| **VL3b** | Manifest bound; no collisions; brand chain OK; orphan ratio acceptable |
| **VL3d** | All Critical slots LOCKED or waived; no UNKNOWN unescalated |
| **VL3c** | DOM order = resolved order; no open conflicts |
| **VL3f** | AUTO_ASSEMBLE authorized or ESCALATE completed with record |

### Per-domain STOP triggers (canonical)

| Domain | STOP when |
|--------|-----------|
| **VL3e** | Layout Spec missing (PIXEL) |
| **VL3a** | INSTANCE invisible; generative placeholder |
| **VL3b** | Frame export; brand collision; blocklisted hash |
| **VL3d** | UNKNOWN slot; generative fill attempt (PIXEL) |
| **VL3c** | Silent layer-index default; open Discovery anomaly |
| **VL3f** | Unresolved conflict; AUTO with open UNKNOWN |

### COMPOSITION_VALIDATED rollup

```text
COMPOSITION_VALIDATED =
  VL3e PASS
  AND VL3a PASS (or N/A TEMPLATE non-instance section)
  AND VL3b PASS
  AND VL3d PASS (no UNKNOWN Critical; no FORBIDDEN violation)
  AND VL3c PASS
  AND VL3f ∈ { AUTO_ASSEMBLE, ESCALATE completed }
```

---

## Failure Registry

### Code system

| Prefix | Domain | Range | Charter cross-ref |
|--------|--------|-------|---------------------|
| **GL-** | VL3e Group/Layout | GL-001–GL-099 | `group-decomposition-law-v1.md` |
| **IR-** | VL3a Instance Resolver | IR-001–IR-099 | VL3a |
| **AI-** | VL3b Asset Identity | AI-001–AI-099 | `ASSET_IDENTITY_COLLISION` |
| **TL-** | VL3d Text Lock | TL-001–TL-099 | Anti-generative-fill |
| **VO-** | VL3c Visual Ordering | VO-001–VO-099 | VL3c |
| **AD-** | VL3f Assembly Decision | AD-001–AD-099 | ASSEMBLY DECISION |

**GL- prefix** chosen over generic GP- to align with Group/Layout Spec vocabulary.

### GL- failure classes (VL3e foundation)

| Code | Title | Severity |
|------|-------|----------|
| **GL-001** | Layout Spec skipped | Critical |
| **GL-002** | Group aggregation before decomposition | Major |
| **GL-003** | GROUP-ID missing for visual group | Major |
| **GL-004** | Layout Spec not APPROVED | Critical |
| **GL-005** | Group Register / Layout Spec inconsistency | Major |

### Registry token mapping (existing → new)

| Legacy token | New code |
|--------------|----------|
| `ASSET_IDENTITY_COLLISION` | AI-003, AI-004 |
| `GROUP AGGREGATION BEFORE DECOMPOSITION` | GL-002 |
| FAIL-001 … FAIL-018 | See FP-0002 Mapping section |

### Severity → pipeline effect

| Severity | GENERATION | VERIFIED (PIXEL) | PRODUCTION PASS |
|----------|:----------:|:----------------:|:---------------:|
| Critical | STOP | Blocked | Blocked |
| Blocker | STOP | Blocked | Blocked |
| Major | FAIL section / ESCALATE | Blocked | Blocked |
| Medium | PARTIAL | May block if Critical entity | Investigate |
| Low | PASS WITH NOTES | — | — |

---

## Layer Integration

### VL3 ← VL2 (inputs)

| VL2 output | VL3 consumer |
|------------|--------------|
| Mapping QA PASS record | Scope boundary for sections/slots |
| APPROVED Production Standards | Token/brand constraints for VL3b |
| FIG extract (full/reduced) | VL3a, VL3d upstream |
| Design Audit conflict list | VL3c, VL3f escalation inputs |
| Component type inventory | VL3a symbol vocabulary |

**Boundary rule:** Mapping QA completes at VL2. VL3 does **not** re-run mapping — it validates **composition truth** against mapping artifacts.

### VL3 → VL4 (outputs)

| VL3 artifact | VL4 use |
|--------------|---------|
| `COMPOSITION_VALIDATED` | Generation authorization |
| Instance enumeration | Builder consumes slot map |
| Asset manifest | `src` wiring source of truth |
| Text lock manifest | Verbatim copy injection |
| Visual order record | Section partial sequence |
| Assembly Decision Record | Order override authority |

**Boundary rule:** VL4 **BUILT** does not re-validate VL3. Stale VL3 artifacts after source change invalidate VERIFIED (charter §5.5).

### VL3 → VL5 (verification handoff)

| VL3 domain | VL5 verification |
|------------|------------------|
| VL3a | Entity completeness — instance cards (Layer C) |
| VL3b | DQ-08 Assets; PF-07; manifest ↔ dist diff |
| VL3d | E3 text lock diff — FIG ↔ HTML |
| VL3c | Section order in dist vs order record |
| VL3f | Assembly Decision cited in REPORT |
| All | VL5 re-runs E3 diffs; VL3 PASS is **necessary not sufficient** for VERIFIED |

**FP-0002 retroactive:** BUILT at VL4; VL3 gates absent → VL5 would yield **NOT VERIFIED**.

### Integration diagram

```text
VL2 ──mapping, standards, extract──► VL3 ──composition artifacts──► GEN
                                      │                              │
                                      │                              ▼
                                      └──────────────────────► VL4 BUILT
                                                                   │
                                      VL3 evidence reviewed ◄──────┤
                                      in VL5 E2/E3 bundle            ▼
                                                              VL5 VERIFIED
```

---

## FP-0002 Mapping

Complete forensic failure register → VL3 domain → failure code → would-have-blocked.

| FAIL ID | Title | Domain | Code(s) | Block point |
|---------|-------|--------|---------|-------------|
| FAIL-001 | False-green build log | VL4/VL5 | — | VERIFIED |
| FAIL-002 | Review hallucination | VL3a, VL3d | IR-004, TL-002 | STOP / VERIFIED |
| FAIL-003 | Intro text drift | VL3d | TL-001 | VERIFIED |
| FAIL-004 | Image hash collision d3ac7d00 | VL3b | AI-001, AI-002 | STOP |
| FAIL-005 | Asset orphans 56% | VL3b | AI-005 | VERIFIED |
| FAIL-006 | Component instance blindness | VL3a | IR-003 | STOP |
| FAIL-007 | SECTION-10 visual order | VL3c, VL3f | VO-001, AD-001 | VERIFIED |
| FAIL-008 | Specialists placeholders | VL3a, VL3b | IR-005, AI-008 | VERIFIED |
| FAIL-009 | Articles missing assets | VL3a, VL3b | IR-004, AI-006 | VERIFIED |
| FAIL-010 | Interaction stubs | VL5/VL6 | — | PRODUCTION PASS scoped |
| FAIL-011 | Empty alt | VL5 | — | VERIFIED |
| FAIL-012 | Stat description loss | VL3d | TL-005 | VERIFIED |
| FAIL-013 | Quote truncation | VL3d | TL-004 | VERIFIED |
| FAIL-014 | Program cards invented | VL3a | IR-004 | VERIFIED |
| FAIL-015 | Services invented | VL3a | IR-001, IR-004 | VERIFIED |
| FAIL-016 | Disclaimer leak | VL3d | TL-006 | VERIFIED |
| FAIL-017 | Logo collision | VL3b | AI-003, AI-004 | STOP |
| FAIL-018 | No post-build FIG diff | VL5 | — | VERIFIED |

### Domain failure density (FP-0002)

| Domain | FAIL count | % of addressable |
|--------|:----------:|:----------------:|
| VL3a Instance Resolver | 6 | 35% |
| VL3d Text Lock | 6 | 35% |
| VL3b Asset Identity | 5 | 29% |
| VL3c / VL3f Visual Order | 1 | 6% |
| VL3e Foundation | 0 direct | — |

**Lesson:** ~70% of FP-0002 composition failures split between **Instance Resolver** and **Text Lock** — VL3a + VL3d are Priority A for Pass 02 operationalization.

---

## Risks

| Risk | Severity | Mitigation in this architecture |
|------|----------|--------------------------------|
| VL3 domains remain human-only | Critical | Explicit checklists + failure codes; evidence model |
| GL- / IR- / AI- code proliferation without adoption | Medium | Single registry; map to existing FAIL-* and tokens |
| Y_THRESHOLD tuning disputes | Medium | Project-scoped parameter in Assembly Decision Record |
| Text Lock without extract fix | Critical | TE-0* gates explicitly precede lock |
| VL3f ignored; silent defaults persist | Critical | AD-002 STOP; VO-003 STOP |
| Orphan threshold too lenient | Medium | AI-V05 default 50% → PARTIAL blocks VERIFIED |
| TEMPLATE_ART path under-specified | Medium | Mode fork table per domain |
| Pass 02 scope creep into WF-A03 automation | High | Explicit non-goals preserved |
| Governance fatigue (6 domains × checklists) | Medium | Rollup to COMPOSITION_VALIDATED; staged sections |
| Instance vocabulary drift | Medium | IR-006 SAFE UNKNOWN + HITL |

---

## SAFE UNKNOWN

| Item | Status | What would verify |
|------|--------|-------------------|
| Optimal `Y_THRESHOLD` for FIG coordinate spaces | **SAFE UNKNOWN** | Pilot on 2+ PIXEL projects |
| Machine-readable `composition_manifest.json` adoption | **SAFE UNKNOWN** | First Pass 02 pilot project |
| Component symbol vocabulary completeness | **SAFE UNKNOWN** | Registry harvest from FP-0002 + FP-0001 |
| Whether VL3f warrants charter §3 amendment | **Design only** | Pass 02 implementation review |
| Automated instance walk scripts | **Per-project** | WF-A03 or project-local charter |
| In-section VO-V05 enforcement depth | **SAFE UNKNOWN** | Layout Spec granularity audit |
| Orphan ratio threshold (50%) | **Proposed default** | Forensic calibration on next stress test |
| TE-03 multi-paragraph rules across FIG export versions | **SAFE UNKNOWN** | Extract pipeline version matrix |

---

## Recommended WF-A02 Pass 02 Scope

Architecture design for VL3 domains complete. **Pass 02 implementation** = documentation integration only — not runtime.

### Priority A — mandatory

1. **Amend charter §3 VL3** — add VL3f Assembly Decision; ordered domain graph; reference this doc.
2. **VL3 PIXEL_PERFECT operator checklist** — IR/AI/VO/TL/AD/GL validations as routable human checklist.
3. **`composition_manifest.json` SSOT spec** — unify instance, asset, text lock, order records (design from this doc).
4. **Failure registry doc** — `GL-`/`IR-`/`AI-`/`TL-`/`VO-`/`AD-` codes with FP-0002 crosswalk.
5. **Anti-generative-fill operationalization** — TL state machine in charter-adjacent gate doc.
6. **Asset Identity pre-wire gate spec** — AI-V01–V08 as blocking checklist (extends `asset-identity-collision-v1.md`).
7. **Assembly Decision Record template** — AD record shape + VO conflict policy.

### Priority B — desirable

1. **INSTANCE-heavy section playbook** — specialists, reviews, articles, FAQ, cards (from FP-0002 mapping).
2. **`section-NN.lock.json` spec** — align with TL-V04; per-section text state export.
3. **Component symbol vocabulary registry** — seed from FP-0002 FIG symbols.
4. **Text Extraction quality gate doc** — TE-01–TE-04 as VL3d.0 upstream.
5. **Orphan asset threshold policy** — formalize AI-V05 default.
6. **TEMPLATE_ART VL3 reduced checklist** — brand-only VL3b path.
7. **OPERATIONAL-INDEX row** — pointer to VL3 domains architecture.

### Priority C — defer (WF-A03 or project-local)

1. Automated Instance Resolver walker.
2. Hash dedup registry engine.
3. Visual Y auto-sort script.
4. Text lock diff automation.
5. CI integration of composition_manifest.
6. Computer vision ordering validation.

---

**STOP AFTER REPORT** — No implementation. No governance edits. No runtime. No WF-A03.

*End of VL3 Validation Domains Architecture v1 — WF-A02 Pass 02 design deliverable.*
