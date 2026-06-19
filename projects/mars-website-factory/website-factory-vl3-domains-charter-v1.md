# Website Factory — VL3 Domains Charter v1

**Status:** **documented** — canonical SoT for **VL3 Composition & Extract Validation** internal domains (VL3a–VL3f).  
**Not:** Instance Resolver runtime, Asset Identity Registry engine, automated ordering diff, validator product, or CI gate.

**Date:** 2026-06-18  
**Implementation pass:** WF-A02 — Pass 02 (VL3 Domains Integration)  
**Authority chain:** [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) (WF-A02 Pass 01) · [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) (WF-A01)

**Evidence base:** [reports/website-factory-vl3-validation-domains-architecture-v1.md](../reports/website-factory-vl3-validation-domains-architecture-v1.md) · [reports/FP-0002-STRESS-TEST-FORENSIC-v1.md](../reports/FP-0002-STRESS-TEST-FORENSIC-v1.md) · [reports/website-factory-vl3-domains-implementation-pass-01.md](../reports/website-factory-vl3-domains-implementation-pass-01.md)

**Honesty boundary:** VL3 domains are **human-operated documentation contracts**. Project-local scripts may satisfy evidence classes; Factory does **not** claim global automation in WF-A02 Pass 02.

---

## 1. Purpose

This charter is the **single canonical source of truth** for VL3 internal architecture:

| Domain | Definition location |
|--------|---------------------|
| VL3 domain registry (VL3a–VL3f) | §2 |
| Per-domain contracts (Purpose, Inputs, Outputs, Exit Criteria, Failure Signals) | §3 |
| Execution order and dependency graph | §4 |
| Failure Registry (GL-, IR-, AI-, TL-, VO-, AD-) | §5 |
| FP-0002 forensic crosswalk | §6 |
| Production Mode integration | §7 |
| VL2 → VL3 → VL4 flow contract | §8 |
| COMPOSITION_VALIDATED rollup | §9 |

**Parent layer:** VL3 — Composition & Extract Validation — defined in [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) §3.

**Explicit non-goals (WF-A02 Pass 02):** Validator Runtime · Instance Resolver automation · Hash dedup engine · Visual Y auto-sort · Text lock diff automation · WF-A03 layers.

---

## 2. VL3 Domain Registry

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

### Domain summary

| ID | Domain | Failure prefix | Primary question |
|----|--------|----------------|------------------|
| **VL3e** | Composition Foundation | `GL-` | Are discrete groups registered and Layout Spec APPROVED? |
| **VL3a** | Instance Resolver | `IR-` | Are FIG INSTANCE subtrees enumerated and bound to HTML slots? |
| **VL3b** | Asset Identity | `AI-` | Is every wired asset uniquely identified and collision-free? |
| **VL3d** | Text Lock | `TL-` | Is all in-scope copy locked, partial, or explicitly forbidden to generate? |
| **VL3c** | Visual Ordering | `VO-` | Does planned DOM order match visual SSOT contract? |
| **VL3f** | Assembly Decision | `AD-` | May Factory auto-assemble, escalate, or must stop? |

### Cross-cutting concepts (not separate domains)

| Concept | Owner domain | Rationale |
|---------|--------------|-----------|
| **Component Extraction** | VL3a | Extraction is means; validation target is **instance truth** |
| **Text Extraction** | VL3d (upstream VL3d.0) | Flat TEXT extract quality gate precedes lock/diff |
| **Mapping** | VL2 → VL3 handoff | Design → Frontend Mapping QA completes at VL2; VL3 consumes artifacts |
| **Group Register** | VL3e | GROUP-ID register is prerequisite for VL3a instance walk |

**Primary authorities:** [group-decomposition-law-v1.md](group-decomposition-law-v1.md) · [layout-spec-law-v1.md](layout-spec-law-v1.md) · [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) · validation charter §7 anti-generative-fill.

---

## 3. Per-Domain Contracts

Each domain defines: **Purpose**, **Inputs**, **Outputs**, **Exit Criteria**, **Failure Signals** — per Validation Architecture IA-02 pattern.

---

### VL3e — Composition Foundation

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Ensure discrete visual groups are registered and Layout Spec is APPROVED before composition truth validation — prerequisite for INSTANCE walk and slot binding. |
| **Inputs** | Group Decomposition output; GROUP-ID register; Layout Spec draft; Design Audit group inventory; VL2 Mapping QA scope boundary. |
| **Outputs** | Complete Group Register; APPROVED Layout Spec (PIXEL); group ↔ section binding record; foundation attestation for downstream VL3 domains. |
| **Exit criteria** | All visual groups in scope have GROUP-IDs; Layout Spec status = APPROVED (PIXEL mandatory); no Group aggregation before decomposition violation; Group Register consistent with Layout Spec. |
| **Failure signals** | **STOP** — Layout Spec missing or not APPROVED (PIXEL); **FAIL** — GROUP-ID missing for visual group; **FAIL** — Group Register / Layout Spec inconsistency; **FAIL** — group aggregation before decomposition. |

**Failure prefix:** `GL-`  
**Primary authorities:** [group-decomposition-law-v1.md](group-decomposition-law-v1.md) · [layout-spec-law-v1.md](layout-spec-law-v1.md)

---

### VL3a — Instance Resolver

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Ensure FIG component instances (`INSTANCE` nodes, typed symbols) are **enumerated, counted, and bound** to planned HTML slots **before** generation — replacing flat TEXT extract blindness. |
| **Inputs** | Group Register (VL3e); FIG extract with INSTANCE visibility; component type inventory from VL2; planned HTML slot map; Factory component vocabulary. |
| **Outputs** | Instance enumeration record per section; `instance_key → slot_id` mapping table; per-instance text/image inventory; Component Extraction sub-contract attestation (CE-01–CE-05). |
| **Exit criteria** | INSTANCE-heavy sections: instance walk complete; `fig_instance_count == planned_html_slot_count`; no duplicate `instance_key`; no generic placeholder substitution; per-instance text inventory present (PIXEL Critical). |
| **Failure signals** | **STOP** — INSTANCE subtree invisible; generative placeholder detected; **FAIL** — instance count mismatch; duplicate instance key; cross-instance content bleed; **SAFE UNKNOWN** — symbol not in vocabulary → HITL. |

**Failure prefix:** `IR-`  
**Sub-contract:** Component Extraction (VL3a.1) — CE-01 through CE-05.

**Instance identity key (normative):**

```text
instance_key = section_id + ":" + fig_node_id + ":" + symbol_name + ":" + instance_index
```

---

### VL3b — Asset Identity

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Ensure every raster/SVG wired to HTML is **uniquely identified**, **correctly scoped**, and **bound** via manifest — before assembly. Forbid frame-export pollution, hash collisions, orphan exports, and unconnected assets. |
| **Inputs** | FIG export manifest; planned HTML `src` list; brand chain checklist; VL3a per-instance image inventory; hash dedup registry / blocklist. |
| **Outputs** | Asset manifest (`asset_record` set); brand chain attestation; hash dedup registry update; pre-wire gate checklist (AI-V01–AI-V08). |
| **Exit criteria** | No frame-level export as slot image; hash uniqueness per slot (or explicit reuse approval); brand chain verified; manifest completeness — every planned `src` has manifest row; orphan ratio within threshold; no blocklisted collision hash. |
| **Failure signals** | **STOP** — frame-export pollution; brand identity collision; blocklisted hash; first-image-as-logo heuristic; **FAIL** — hash collision across slots; missing manifest row; duplicate file in distinct slots; **PARTIAL** — orphan asset majority; unconnected export (PIXEL Critical slot). |

**Failure prefix:** `AI-`  
**Existing foundation:** [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) — registry token `ASSET_IDENTITY_COLLISION` maps to **AI-003**, **AI-004**.

**Asset identity record (normative shape):**

```text
asset_record {
  section_id      : string
  slot_id         : string
  fig_node_id     : string
  export_hash     : string
  file_path       : string
  node_class      : LEAF_IMAGE | BRAND_MARK | ICON | DECORATIVE
  binding_status  : BOUND | ORPHAN | UNCONNECTED | COLLISION
}
```

---

### VL3d — Text Lock

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Define **text state** per string slot before generation; forbid generative paraphrase in PIXEL_PERFECT; gate Text Extraction quality upstream. |
| **Inputs** | FIG TEXT extract; INSTANCE walk text inventory (VL3a); Layout Spec text block definitions; VL2 Mapping QA text scope; optional `section-NN.lock.json`. |
| **Outputs** | Text lock manifest; per-slot state table (LOCKED / PARTIAL / UNKNOWN / FORBIDDEN TO GENERATE / SUPPLEMENT); Text Extraction sub-contract attestation (TE-01–TE-04); anti-generative-fill attestation. |
| **Exit criteria** | All Critical slots have state assigned; LOCKED strings have node provenance; no generative fill on UNKNOWN/PARTIAL (PIXEL); section-scoped binding verified; multi-paragraph blocks complete where required. |
| **Failure signals** | **STOP** — UNKNOWN Critical slot unescalated; generative fill attempt (PIXEL); **FAIL** — paraphrase drift; invented body copy; section scope bleed; lock file / extract mismatch; **PARTIAL** — text truncation; adjacent pair loss. |

**Failure prefix:** `TL-`  
**Sub-contract:** Text Extraction (VL3d.0) — TE-01 through TE-04.

**PIXEL_PERFECT rule:**

```text
IF text_state(slot) NOT IN { LOCKED }
AND production_mode == PIXEL_PERFECT
THEN generation_action = FORBIDDEN
     signal = STOP (TL-003)
```

**Text state machine:**

| State | PIXEL allowed action |
|-------|---------------------|
| **LOCKED** | Use verbatim — required exact match |
| **PARTIAL** | **STOP** or HITL — no paraphrase |
| **UNKNOWN** | **STOP** + HITL — forbidden generate |
| **FORBIDDEN TO GENERATE** | **STOP** if attempted |
| **SUPPLEMENT** | TEMPLATE_ART only — content deck fills gap |

---

### VL3c — Visual Ordering

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Define and validate **section and in-section visual order contract** — resolving conflicts between FIG layer child index, visual Y position, and planned DOM order. |
| **Inputs** | Section bounds (`visual_y`, `layer_index`); Discovery anomaly flags; planned DOM order; Layout Spec section sequence; VL3e Group Register in-section order. |
| **Outputs** | Ordered section list (`section_id, visual_y, layer_index, dom_index`); conflict flag report; RESOLVED_ORDER computation; cross-ref to Assembly Decision record when conflict. |
| **Exit criteria** | `RESOLVED_ORDER` computed from visual Y (PIXEL); DOM order = resolved order; no open Discovery anomalies; in-section GROUP-ID order verified; IA override documented when applied. |
| **Failure signals** | **STOP** — silent layer-index default (PIXEL); open Discovery anomaly unresolved; IA override without record; **FAIL** — DOM order ≠ resolved order; **ESCALATE** — Y vs layer-index conflict → VL3f required. |

**Failure prefix:** `VO-`

**Order contract (normative):**

```text
RESOLVED_ORDER = sort(sections, key=visual_y, stable_tie=layer_index)

IF exists(section_pair) WHERE abs(y_a - y_b) > Y_THRESHOLD
   AND layer_index_order != visual_y_order
THEN conflict = TRUE
     REQUIRE assembly_decision_record (VL3f)
     FORBID silent layer-index default (PIXEL)
```

---

### VL3f — Assembly Decision

| Attribute | Definition |
|-----------|------------|
| **Purpose** | Govern **when Factory may auto-assemble**, **when it must escalate (HITL)**, and **when it must stop** — converting composition conflicts into explicit decisions, not silent defaults. |
| **Inputs** | VL3a–VL3e validation results; VO conflict flags; SAFE UNKNOWN dispositions; Exception Registry waivers; structural IA override requests. |
| **Outputs** | Assembly Decision Record (when ESCALATE); AUTO_ASSEMBLE attestation checklist; `COMPOSITION_VALIDATED` authorization token. |
| **Exit criteria** | Outcome ∈ { **AUTO_ASSEMBLE**, **ESCALATE completed with record** }; no unresolved conflicts; no STOP triggers from upstream domains; no AUTO_ASSEMBLE with open SAFE UNKNOWN. |
| **Failure signals** | **STOP** — unresolved order conflict; silent default applied; missing decision record; IA override without authority; AUTO_ASSEMBLE with open SAFE UNKNOWN; ESCALATE not completed. |

**Failure prefix:** `AD-`

**Decision outcomes:**

| Outcome | When allowed |
|---------|--------------|
| **AUTO_ASSEMBLE** | All VL3 domains PASS; no VO conflict; no SAFE UNKNOWN |
| **ESCALATE** | VO-001 conflict; IR-006 unknown symbol; ambiguous IA |
| **STOP_ASSEMBLY** | STOP triggers; brand collision; generative fill attempt; unresolved conflict |

---

## 4. Execution Order

| Phase | Domains | Blocking rule |
|-------|---------|---------------|
| **P0 — Foundation** | VL3e | No VL3a–VL3f without APPROVED Layout Spec (PIXEL) |
| **P1 — Structure truth** | VL3a | INSTANCE-heavy sections: instance walk before assets/text |
| **P2 — Slot binding** | VL3b, VL3d | Parallel validation; both must PASS or explicit PARTIAL disposition |
| **P3 — Page composition** | VL3c | Section order contract before cross-section assembly |
| **P4 — Build authorization** | VL3f | COMPOSITION_VALIDATED emitted only when P0–P3 satisfied or escalated |

---

## 5. Failure Registry

### 5.1 Code system

| Prefix | Domain | Range | Ownership | Scope |
|--------|--------|-------|-----------|-------|
| **GL-** | VL3e Composition Foundation | GL-001–GL-099 | Group Decomposition / Layout Spec operators | GROUP-ID register, Layout Spec approval, decomposition order |
| **IR-** | VL3a Instance Resolver | IR-001–IR-099 | Composition / extract operators | INSTANCE enumeration, slot binding, component extraction |
| **AI-** | VL3b Asset Identity | AI-001–AI-099 | Asset / brand operators | Manifest binding, hash dedup, brand chain — extends `ASSET_IDENTITY_COLLISION` |
| **TL-** | VL3d Text Lock | TL-001–TL-099 | Text / content operators | Text state, anti-generative-fill, extract quality |
| **VO-** | VL3c Visual Ordering | VO-001–VO-099 | Assembly / IA operators | Section order, visual Y vs layer index |
| **AD-** | VL3f Assembly Decision | AD-001–AD-099 | Lead / HITL operators | Build authorization, conflict resolution |

**Ownership rule:** Each prefix is **human-maintained** in Factory documentation. No automated registry engine is claimed. Operators cite codes in REPORT Layer C entity findings and Layer D SAFE UNKNOWN escalations.

### 5.2 GL- failure classes (VL3e)

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **GL-001** | Layout Spec skipped | Critical | **STOP** (PIXEL) |
| **GL-002** | Group aggregation before decomposition | Major | **FAIL** |
| **GL-003** | GROUP-ID missing for visual group | Major | **FAIL** |
| **GL-004** | Layout Spec not APPROVED | Critical | **STOP** (PIXEL) |
| **GL-005** | Group Register / Layout Spec inconsistency | Major | **FAIL** |

### 5.3 IR- failure classes (VL3a)

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **IR-001** | Instance count mismatch | Critical | **STOP** section build (PIXEL) |
| **IR-002** | Duplicate instance key | Major | **FAIL** |
| **IR-003** | INSTANCE subtree invisible | Critical | **STOP** |
| **IR-004** | Component text not extracted | Critical | **STOP** generative fill (PIXEL) |
| **IR-005** | Generic placeholder substitution | Critical | **FAIL** |
| **IR-006** | Symbol vocabulary unknown | Major | **SAFE UNKNOWN** → HITL |
| **IR-007** | Cross-instance content bleed | Major | **FAIL** |

**Example (FP-0002):** FAIL-008 Specialists — `Врач` instances not enumerated → **IR-005**, **IR-004**. Operator cites `IR-005` in Layer C for SECTION-12; blocks VERIFIED until instance walk complete.

### 5.4 AI- failure classes (VL3b)

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **AI-001** | Frame-export pollution | Critical | **STOP** before wire |
| **AI-002** | Hash collision across slots | Critical | **STOP** or **FAIL** |
| **AI-003** | Brand identity collision | Blocker | **STOP** before wire |
| **AI-004** | First-image-as-logo heuristic | Critical | **STOP** |
| **AI-005** | Orphan asset majority | Major | **PARTIAL** → blocks VERIFIED |
| **AI-006** | Unconnected export | Major | **FAIL** (Critical slot) |
| **AI-007** | Missing manifest row | Major | **FAIL** |
| **AI-008** | Duplicate file, distinct slots | Major | **FAIL** |
| **AI-009** | Export without reference | Medium | **PARTIAL** |

**Example (FP-0002):** FAIL-004 hash `d3ac7d00` → **AI-001**, **AI-002**. Operator runs AI-V01 pre-wire checklist; **STOP** before HTML wire when frame-export detected.

**Legacy mapping:** `ASSET_IDENTITY_COLLISION` → **AI-003**, **AI-004**.

### 5.5 TL- failure classes (VL3d)

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **TL-001** | Paraphrase drift | High | Blocks VERIFIED |
| **TL-002** | Invented body copy | Critical | **STOP** / blocks VERIFIED |
| **TL-003** | Generative fill on missing extract | Critical | **STOP** |
| **TL-004** | Text truncation | Major | **PARTIAL** |
| **TL-005** | Adjacent pair loss | Major | **PARTIAL** |
| **TL-006** | Section scope bleed | Medium | **PARTIAL** |
| **TL-007** | UNKNOWN slot unescalated | Critical | **STOP** |
| **TL-008** | Lock file / extract mismatch | Major | **FAIL** |

**Example (FP-0002):** FAIL-002 Review hallucination → **IR-004**, **TL-002**. Text state for review bodies = UNKNOWN; generation forbidden under PIXEL_PERFECT.

### 5.6 VO- failure classes (VL3c)

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **VO-001** | Y vs layer-index conflict | High | Requires VL3f decision |
| **VO-002** | DOM order ≠ resolved order | Critical | **FAIL** |
| **VO-003** | Silent layer-index default | Critical | **STOP** (PIXEL) |
| **VO-004** | Discovery anomaly unresolved | High | **STOP** |
| **VO-005** | In-section visual order drift | Major | **PARTIAL** |
| **VO-006** | IA override without record | Major | **STOP** |

**Example (FP-0002):** FAIL-007 SECTION-10 → **VO-001**, escalates to **AD-001** if unresolved.

### 5.7 AD- failure classes (VL3f)

| Code | Title | Severity | Pipeline effect |
|------|-------|----------|-----------------|
| **AD-001** | Unresolved order conflict | Critical | **STOP** |
| **AD-002** | Silent default applied | Critical | **STOP** |
| **AD-003** | Missing decision record | Major | **STOP** generation |
| **AD-004** | IA override without authority | Major | **STOP** |
| **AD-005** | AUTO_ASSEMBLE with open SAFE UNKNOWN | Major | **STOP** |
| **AD-006** | ESCALATE not completed | Major | **STOP** |

**Example (FP-0002):** SECTION-10 visual Y conflict → operator creates Assembly Decision Record citing **VO-001**; Lead ack required before **AUTO_ASSEMBLE**.

### 5.8 Severity → pipeline effect

| Severity | GENERATION | VERIFIED (PIXEL) | PRODUCTION PASS |
|----------|:----------:|:----------------:|:---------------:|
| Critical | STOP | Blocked | Blocked |
| Blocker | STOP | Blocked | Blocked |
| Major | FAIL section / ESCALATE | Blocked | Blocked |
| Medium | PARTIAL | May block if Critical entity | Investigate |
| Low | PASS WITH NOTES | — | — |

---

## 6. FP-0002 Mapping

Retroactive forensic register → VL3 domain → failure class.

| FAIL ID | Title | VL3 Domain | Failure Class | Would block |
|---------|-------|------------|---------------|-------------|
| FAIL-001 | False-green build log | — (VL4/VL5) | — | VERIFIED |
| FAIL-002 | Review hallucination | VL3a, VL3d | IR-004, TL-002 | STOP / VERIFIED |
| FAIL-003 | Intro text drift | VL3d | TL-001 | VERIFIED |
| FAIL-004 | Image hash collision d3ac7d00 | VL3b | AI-001, AI-002 | STOP |
| FAIL-005 | Asset orphans 56% | VL3b | AI-005 | VERIFIED |
| FAIL-006 | Component instance blindness | VL3a | IR-003 | STOP |
| FAIL-007 | SECTION-10 visual order | VL3c, VL3f | VO-001, AD-001 | VERIFIED |
| FAIL-008 | Specialists placeholders | VL3a, VL3b | IR-005, AI-008 | VERIFIED |
| FAIL-009 | Articles missing assets | VL3a, VL3b | IR-004, AI-006 | VERIFIED |
| FAIL-010 | Interaction stubs | — (VL5/VL6) | — | PRODUCTION PASS scoped |
| FAIL-011 | Empty alt | — (VL5) | — | VERIFIED |
| FAIL-012 | Stat description loss | VL3d | TL-005 | VERIFIED |
| FAIL-013 | Quote truncation | VL3d | TL-004 | VERIFIED |
| FAIL-014 | Program cards invented | VL3a | IR-004 | VERIFIED |
| FAIL-015 | Services invented | VL3a | IR-001, IR-004 | VERIFIED |
| FAIL-016 | Disclaimer leak | VL3d | TL-006 | VERIFIED |
| FAIL-017 | Logo collision | VL3b | AI-003, AI-004 | STOP |
| FAIL-018 | No post-build FIG diff | — (VL5) | — | VERIFIED |

### Domain failure density (FP-0002 addressable)

| Domain | FAIL count | % of addressable |
|--------|:----------:|:----------------:|
| VL3a Instance Resolver | 6 | 35% |
| VL3d Text Lock | 6 | 35% |
| VL3b Asset Identity | 5 | 29% |
| VL3c / VL3f Visual Order | 1 | 6% |
| VL3e Foundation | 0 direct | — |

---

## 7. Production Mode Integration

Per-domain mandatory checks by production mode.

| Domain | PIXEL_PERFECT | TEMPLATE_ART |
|--------|:-------------:|:------------:|
| **VL3e** Composition Foundation | **Mandatory** — Layout Spec APPROVED | Optional |
| **VL3a** Instance Resolver | **Mandatory** INSTANCE-heavy sections | Optional |
| **VL3b** Asset Identity | **Mandatory** — full manifest | **Mandatory** — brand/logos only |
| **VL3d** Text Lock | **Mandatory** — FIG extract SSOT; anti-generative-fill **STOP** | Content deck diff; SUPPLEMENT allowed |
| **VL3c** Visual Ordering | **Mandatory** — visual Y primary | Low priority; blueprint order |
| **VL3f** Assembly Decision | **Mandatory** on conflict | AUTO_ASSEMBLE on blueprint reference |

### Mode validation matrix (VL3 domains)

| Check | PIXEL | TEMPLATE | STOP if violated |
|-------|:-----:|:--------:|:----------------:|
| Group / Layout Spec (VL3e) | **M** | Opt | ✓ (PIXEL) |
| Instance Resolver (VL3a) | **M** (INSTANCE-heavy) | Opt | ✓ (PIXEL INSTANCE-heavy) |
| Asset Identity (VL3b) | **M** | **M** (brand) | ✓ |
| Text Lock (VL3d) | **M** | Content deck | ✓ (PIXEL missing) |
| Visual Ordering (VL3c) | **M** | — | ✓ (PIXEL conflict) |
| Assembly Decision (VL3f) | **M** on conflict | Opt | ✓ (PIXEL unresolved) |
| Anti-generative-fill | **STOP** | Allowed in bounds | ✓ (PIXEL) |

*M = mandatory for COMPOSITION_VALIDATED at this mode*

**Cross-ref:** [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) §8 · [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md)

---

## 8. Validation Flow Integration

### 8.1 VL2 → VL3 handoff contract

| VL2 output | VL3 consumer |
|------------|--------------|
| Mapping QA PASS record | Scope boundary for sections/slots |
| APPROVED Production Standards | Token/brand constraints for VL3b |
| FIG extract (full/reduced) | VL3a, VL3d upstream |
| Design Audit conflict list | VL3c, VL3f escalation inputs |
| Component type inventory | VL3a symbol vocabulary |

**Boundary rule:** Mapping QA completes at VL2. VL3 does **not** re-run mapping — it validates **composition truth** against mapping artifacts.

**VL2 exit state required:** `DESIGN_CONTRACT_VALIDATED`

### 8.2 VL3 internal flow

```text
VL3e (Foundation)
  └─► VL3a (Instance Resolver)
        ├─► VL3b (Asset Identity)  ─┐
        └─► VL3d (Text Lock)        ─┤ parallel P2
              └─► VL3c (Visual Ordering)
                    └─► VL3f (Assembly Decision)
                          └─► COMPOSITION_VALIDATED
```

### 8.3 VL3 → VL4 handoff contract

| VL3 artifact | VL4 use |
|--------------|---------|
| `COMPOSITION_VALIDATED` | Generation authorization |
| Instance enumeration | Builder consumes slot map |
| Asset manifest | `src` wiring source of truth |
| Text lock manifest | Verbatim copy injection |
| Visual order record | Section partial sequence |
| Assembly Decision Record | Order override authority |

**Boundary rule:** VL4 **BUILT** does not re-validate VL3. Stale VL3 artifacts after source change invalidate VERIFIED (validation charter §5.5).

**VL3 exit state:** `COMPOSITION_VALIDATED` — **no BUILT claim** at VL3.

### 8.4 Transition table (VL2 → VL3 → VL4)

| Transition | Required evidence | Allowed signals | STOP conditions |
|------------|-------------------|-----------------|-----------------|
| VL2 → VL3 | DESIGN_CONTRACT_VALIDATED; Mapping QA PASS | PASS prerequisites | Mapping QA STOP (PIXEL) |
| VL3e → VL3a | Group Register; APPROVED Layout Spec (PIXEL) | PASS | GL-001, GL-004 |
| VL3a → VL3b/VL3d | Instance enumeration (where applicable) | PASS | IR-003, IR-004 |
| VL3b/VL3d → VL3c | Manifest bound; text states assigned | PASS, PARTIAL disposition | AI-001, TL-003 |
| VL3c → VL3f | Order contract; conflict flags | PASS, ESCALATE | VO-003, VO-004 |
| VL3f → GEN | COMPOSITION_VALIDATED | AUTO_ASSEMBLE, ESCALATE complete | AD-001, AD-002 |
| GEN → VL4 | Approved scope; composition artifacts | — | Upstream STOP |

### 8.5 VL3 → VL5 verification handoff

| VL3 domain | VL5 verification |
|------------|------------------|
| VL3a | Entity completeness — instance cards (Layer C) |
| VL3b | DQ-08 Assets; PF-07; manifest ↔ dist diff |
| VL3d | E3 text lock diff — FIG ↔ HTML |
| VL3c | Section order in dist vs order record |
| VL3f | Assembly Decision cited in REPORT |
| All | VL5 re-runs E3 diffs; VL3 PASS is **necessary not sufficient** for VERIFIED |

---

## 9. COMPOSITION_VALIDATED Rollup

```text
COMPOSITION_VALIDATED =
  VL3e PASS
  AND VL3a PASS (or N/A TEMPLATE non-instance section)
  AND VL3b PASS
  AND VL3d PASS (no UNKNOWN Critical; no FORBIDDEN violation)
  AND VL3c PASS
  AND VL3f ∈ { AUTO_ASSEMBLE, ESCALATE completed }
```

### Minimum artifact bundle

| Artifact | Source domain |
|----------|---------------|
| Group Register | VL3e |
| APPROVED Layout Spec | VL3e |
| Instance enumeration record | VL3a (where applicable) |
| Asset manifest | VL3b |
| Text lock manifest | VL3d |
| Visual order record | VL3c |
| Assembly Decision record | VL3f (when required) |

---

## 10. Cross-surface representation

| Surface | Pointer |
|---------|---------|
| [website-factory-validation-architecture-charter-v1.md](website-factory-validation-architecture-charter-v1.md) | Parent VL3 layer §3 |
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | VL3 Domains row |
| [operational-qa-entry-v1.md](operational-qa-entry-v1.md) | Mode router + VL map |
| [failures/asset-identity-collision-v1.md](failures/asset-identity-collision-v1.md) | AI-003/AI-004 peer authority |
| [roadmap.md](roadmap.md) | WF-A02 Pass 02 |

---

## 11. Document control

| Field | Value |
|-------|-------|
| Version | v1 |
| Created | 2026-06-18 |
| Runtime | **Not claimed** |
| Automation | **Not claimed** |

*VL3 Domains Charter v1 — WF-A02 Pass 02. Human-operated documentation only.*
