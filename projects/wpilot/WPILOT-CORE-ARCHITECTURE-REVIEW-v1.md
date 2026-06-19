# WPilot Core Architecture Review v1

**Classification:** Architecture audit — Core Model v1 completeness and consistency review.  
**Status:** Review pass (2026-06-19).  
**Scope:** Documentation only. No code, roadmap, runtime, or new layers.  
**Audited stack:** Mission, Operations Manifest, Risk Classes, Target Registry, Operation Bindings, ChangeSet, Rollback, Proven Capabilities, Site Snapshot Model, Diff Model.

---

## Executive Summary

WPilot Core Model v1 forms a **coherent, human-operated policy stack** with clear separation between taxonomy (Target Registry), operation catalog (Manifest), risk policy (Risk Classes), cross-layer bindings (Operation Bindings), execution unit (ChangeSet), recovery semantics (Rollback), state description (Site Snapshot), change description (Diff), and evidence register (Proven Capabilities).

**Verdict:** Core Model v1 is **Stable** as a documentation architecture. Known gaps are documented (not hidden). Runtime alignment remains **PARTIAL** overall.

**Recommendation:** **A — Stop Core Modeling, move to Runtime Contracts.**

---

## 1. Architecture Completeness

### 1.1 Layer inventory (as documented)

| # | Layer | Document | Role |
|---|-------|----------|------|
| 1 | Mission | WPILOT-MISSION-v1.md | Charter, principles, non-goals, ecosystem boundaries |
| 2 | Site Snapshot Model | WPILOT-SITE-SNAPSHOT-MODEL-v1.md | State / observation layer |
| 3 | Diff Model | WPILOT-DIFF-MODEL-v1.md | Change / comparison layer |
| 4 | Operations Manifest | WPILOT-OPERATIONS-MANIFEST-v1.md | Typed operation catalog |
| 5 | Risk Classes | WPILOT-RISK-CLASSES-v1.md | Risk taxonomy R0–R5 |
| 6 | Target Registry | WPILOT-TARGET-REGISTRY-v1.md | Canonical target taxonomy |
| 7 | Operation Bindings | WPILOT-OPERATION-BINDINGS-v1.md | operation ↔ target ↔ risk ↔ policy matrix |
| 8 | ChangeSet | WPILOT-CHANGESET-v1.md | Change execution unit |
| 9 | Rollback | WPILOT-ROLLBACK-v1.md | Recovery policy |
| 10 | Proven Capabilities | WPILOT-PROVEN-CAPABILITIES-v1.md | Evidence register |

Mission sits above policy; Snapshot/Diff sit as state/change layers feeding policy and execution; Proven Capabilities sits as evidence overlay.

### 1.2 GAPs (documented, not created)

| GAP | Причина | Влияние | Критичность |
|-----|---------|---------|-------------|
| **Approval Record Model** | Approval semantics spread across Mission, Risk Classes, ChangeSet, Bindings; no standalone canonical approval entity or approval_id schema | Operators infer approval from ChangeSet fields; no reusable approval artifact for multi-step workflows | **Medium** — workable via ChangeSet v1; friction for audit trails spanning multiple runs |
| **Validation Model** | `validate_change` exists as operation; validation checklists live in Rollback (post-rollback) and Diff (severity); no unified Validation Layer document | Validation expectations clear per risk class but not as a single canonical validation schema | **Medium** — mitigated by Risk Classes + ChangeSet evidence fields |
| **General Evidence Schema** | ChangeSet evidence fields + Proven Capabilities register + local-storage-policy; no cross-cutting Evidence Model | Evidence paths cited but no unified evidence_type / evidence_ref vocabulary beyond ChangeSet optional fields | **Low–Medium** — acceptable for human-operated v1 |
| **Runtime Execution Contract (Core)** | Explicitly deferred; plugin-mvp v0 contracts exist separately from Core Model v1 | Core Model describes *what*; runtime describes *how* — gap is intentional but blocks automated enforcement | **High for runtime** — **not a Core Model documentation gap** per charter scope |
| **Endpoint / API Mapping Layer** | Mentioned as out-of-scope in Manifest, Bindings, ChangeSet Notes | No canonical operation_id → REST endpoint map in Core Model | **Medium for plugin** — belongs in Runtime Contracts, not Core Model v1 |
| **inspect_plugin target** | Approved operation without canonical `plugin` target in Target Registry v1 | `inspect_plugin` binding status = `target_gap`; ChangeSet cannot set canonical `target_type` | **Low** — explicitly documented; R0 read-only |
| **apply_change umbrella resolution** | Abstract apply operation blocked until subtype resolved | Prevents ambiguous apply runs; requires operator/tooling to resolve subtype | **Low** — intentional safety gate |

**Conclusion:** No critically missing Core Model layer that would block v1 human-operated workflows. Remaining GAPs are either **intentionally deferred** (runtime/API) or **addressable without new Core layers** (approval/validation as ChangeSet extensions or runtime contract fields).

---

## 2. Layer Responsibilities

### 2.1 Layer Responsibility Matrix

| Layer | Purpose | Owner | Inputs | Outputs |
|-------|---------|-------|--------|---------|
| **Mission** | Define WPilot identity, principles, non-goals, ecosystem boundaries | Program owner (Andrey / MetaCODE) | Strategic intent, MARS ecosystem context | Charter constraints for all layers |
| **Site Snapshot Model** | Describe site state at a point in time (structured, scoped) | Documentation / operator workflow | REST reads, HTML evidence, exports, operator verification | Snapshot objects, relationships, evidence refs, scope/level markers |
| **Diff Model** | Describe deltas between two states | Documentation / operator workflow | Snapshot bundles, live state, backup-derived state, operator verified source | Diff objects (change_type, severity, target refs) |
| **Operations Manifest** | Catalog allowed typed operations | Documentation (policy) | Mission constraints, Target Registry scope | `operation_id`, categories, lifecycle, scope rules, forbidden list |
| **Risk Classes** | Classify operation danger and policy expectations | Documentation (policy) | Manifest operation catalog | R0–R5 mapping, approval/backup/validation/rollback matrix |
| **Target Registry** | Canonical target taxonomy | Documentation (policy) | WordPress/CMS entity model, Manifest scope needs | `target_id`, categories, scope model (Entity/Site/Environment) |
| **Operation Bindings** | Bind operation + target + risk + policy flags | Documentation (policy) | Manifest, Registry, Risk Classes | Binding records, binding matrix, gap/blocked statuses |
| **ChangeSet** | Unit of change execution with lifecycle and evidence | Operator / human-supervised workflow | Binding-resolved operation, target, risk policy | ChangeSet record, status transitions, evidence trail |
| **Rollback** | Recovery semantics, sources, validation after restore | Operator / human-supervised workflow | ChangeSet context, Risk Classes expectations, Target scope | Rollback plan expectations, source types, post-rollback checklist |
| **Proven Capabilities** | Register only evidence-backed capabilities | Operator / evidence maintainer | Completed DEV work, reports, local STORAGE artifacts | Proven / not-yet-proven capability lists |

### 2.2 Overlap analysis (requested pairs)

#### Operations Manifest vs Risk Classes vs Operation Bindings

| Concern | Manifest | Risk Classes | Bindings |
|---------|----------|--------------|----------|
| Operation catalog | **Owner** | References | References |
| `operation_id` semantics | **Owner** | References | References |
| `risk_class` (R0–R5) | default risk label only (low/medium/high) | **Owner** | Uses canonical value |
| approval / backup / validation / rollback flags | High-level in tables | Policy matrix by R-class | **Operational binding record** |
| operation ↔ target pairing | Scope rules (summary) | Examples only | **Owner (matrix)** |

**Overlap:** Manifest tables duplicate orientational risk labels; Bindings duplicates Risk Classes expectations in per-operation form.

**Assessment:** **Justified redundancy.** Manifest = catalog; Risk Classes = taxonomy; Bindings = resolved cross-product. Bindings explicitly states it does not override Risk Classes. **No responsibility collision** if Bindings treated as canonical for operation-level policy flags and Risk Classes for class-level rules.

#### ChangeSet vs Rollback

| Concern | ChangeSet | Rollback |
|---------|-----------|----------|
| Execution lifecycle (Draft→Apply→Validate→Close) | **Owner** | Rollback stage nested inside |
| `rollback_available`, `rollback_source` fields | **Owner (fields)** | Semantics **Owner** |
| Rollback sources (ChangeSet backup, hosting, operator verified) | References | **Owner** |
| Post-rollback validation checklist | References validation | **Owner (checklist)** |
| Recovery operations (`rollback_change`, `restore_backup`) | Via `operation_id` | Context and policy |

**Assessment:** **Complementary, not duplicate.** ChangeSet = run container; Rollback = recovery policy detail. Rollback explicitly does not replace ChangeSet. Minor overlap in evidence field names (`rollback_source`, `validation_result`) is **intentional linkage**, not competing ownership.

#### Site Snapshot vs Diff

| Concern | Site Snapshot | Diff |
|---------|---------------|------|
| State at one moment | **Owner** | Consumes as input |
| Delta between states | References in usage | **Owner** |
| `object_type` vs diff `target_type` | object_type (observed) | target_type (changed entity) |
| Levels L0–L4 vs Identity–Environment diff levels | **Owner (capture depth)** | **Owner (compare domain)** — aligned but differently named |

**Assessment:** **Clean separation.** Snapshot = state layer; Diff = change layer. Both documents explicitly differentiate from backup. **No merge recommended.**

### 2.3 Minor responsibility blur

| Area | Issue | Severity |
|------|-------|----------|
| README Core Model stack | Lists 6 layers; omits Bindings, Snapshot, Diff, Proven in stack line | Documentation navigation only |
| Manifest / Bindings footer | «Current documentation stack» lists 6–7 layers, inconsistent with full 10-layer model | Low |
| `backup-rollback-rules.md` | Phase 1 operational rules overlap Rollback v1 themes | Complementary (Phase 1 vs Core policy); Rollback v1 declared canonical |

---

## 3. Circular Dependencies

### 3.1 Dependency graph (logical definition order)

```
Mission (root)
  → Target Registry (taxonomy)
  → Operations Manifest (operations scoped to targets)
  → Risk Classes (risk mapping for operations)
  → Operation Bindings (cross-product)
  → Site Snapshot Model (state vocabulary, uses target taxonomy)
  → Diff Model (consumes snapshot, uses target taxonomy)
  → ChangeSet (execution unit, consumes bindings + registry + risk)
  → Rollback (recovery policy, consumes changeset + registry + risk)
  → Proven Capabilities (evidence overlay, references all)
```

### 3.2 Cross-reference cycles (documentation links)

| Cycle | Description | Risk |
|-------|-------------|------|
| **Manifest ↔ Risk Classes** | Each references the other for operation/risk mapping | **Low** — acyclic definition: Manifest defines ops first, Risk maps them; bidirectional links are navigation only |
| **Target Registry ↔ ChangeSet** | Registry references ChangeSet fields; ChangeSet references Registry for `target_type` | **Low** — taxonomy precedes execution unit; no definitional cycle |
| **ChangeSet ↔ Rollback** | Rollback nested in ChangeSet lifecycle; Rollback references ChangeSet fields | **Low** — Rollback policy extends ChangeSet; ChangeSet does not depend on Rollback for core schema |
| **Snapshot ↔ Diff** | Snapshot mentions diff in usage; Diff consumes snapshot | **Low** — state before change description; acyclic |
| **Bindings ↔ ChangeSet** | Bindings require ChangeSet compliance; ChangeSet header does not list Bindings as Related (minor) | **Low** — Bindings is derivative of Manifest+Registry+Risk |

**Conclusion:** **No harmful circular dependencies.** Documentation cross-links form reference cycles only; logical definition order is acyclic. **No cycle requires redesign.**

---

## 4. Terminology Consistency Audit

Terms reviewed across all WPILOT-*-v1.md documents. **No automatic fixes applied.**

### 4.1 Consistent terms

| Term | Canonical source | Consistency |
|------|-------------------|-------------|
| `css_fragment` | Target Registry `target_id` | Consistent across Registry, Manifest scope, Bindings, Snapshot, Diff, Risk scope rules |
| `theme_option` | Target Registry | Consistent; write paths marked future/outside Manifest v1 |
| `header` / `footer` | Target Registry (Structure) | Consistent as zone-level structure targets |
| `site` / `environment` | Target Registry | Distinction documented (WP instance vs hosting/runtime); consistent |
| `target_type` / `target_id` | Target Registry + ChangeSet | Consistent in ChangeSet, Bindings, Diff, Registry |
| `risk_class` | Risk Classes (R0–R5) | Consistent; Manifest uses separate `default risk` (low/medium/high) with documented subordination |
| `operation_id` | Operations Manifest | Consistent kebab-case identifiers across all layers |
| `changeset_id` | ChangeSet | Consistent |
| `rollback_change` / `restore_backup` | Operations Manifest (Recovery) | Consistent semantics; Rollback owns execution detail |
| `validate_change` | Operations Manifest (Recovery, R0) | Consistent as read-only verification |

### 4.2 Documented divergences (findings)

| Term / usage | Finding | Documents affected | Severity |
|--------------|---------|-------------------|----------|
| **`default risk` vs `risk_class`** | Manifest uses low/medium/high; Risk Classes uses R0–R5. **Documented** as non-canonical vs canonical | Manifest, Risk Classes | **Low** — explicit Notes |
| **`object_type` vs `target_type`** | Snapshot uses `object_type`; ChangeSet/Diff use `target_type`. Documented as aligned-with-Registry where applicable | Snapshot, ChangeSet, Diff | **Low** — intentional field naming by layer |
| **`snapshot` (3 meanings)** | (1) Site Snapshot Model = structured state; (2) HTML/JSON capture artifact; (3) `rollback-snapshots/` filesystem folder in backup-rollback-rules | Snapshot Model, Proven Capabilities, backup-rollback-rules, README | **Medium** — Snapshot Model explicitly disambiguates vs HTML; **rollback snapshot** colloquial use persists in Phase 1 docs |
| **`backup` vs `snapshot`** | Both docs state Snapshot ≠ Backup; Diff ≠ Backup. Operational prose sometimes says «HTML snapshot» for backup artifacts | Snapshot, Diff, Proven Capabilities, local-storage-policy | **Low–Medium** — core layers disambiguate; evidence prose informal |
| **`restore` vs `rollback`** | `restore_backup` = R4 recovery op; `rollback_change` = R3 entity rollback. «Restore» used generically in Rollback lifecycle («Restore Attempt») | Rollback, Manifest, Risk Classes | **Low** — context-dependent but documented |
| **`validation` (noun vs operation)** | `validate_change` = operation_id; validation = policy requirement; validation = post-rollback checklist | Risk Classes, ChangeSet, Rollback, Diff | **Low** — layered meanings, no direct contradiction |
| **`diff_level` naming** | Diff uses Identity/Structure/Content/Configuration/Environment; Snapshot uses L0–L4 | Diff, Snapshot | **Low** — aligned conceptually, different labels; not cross-document enforced |
| **`active_theme` / `active_plugins`** | Snapshot `object_type` values; **not** Target Registry `target_id` | Snapshot, Diff (Configuration level) | **Medium** — documented as snapshot objects; Registry lists `plugin` as future target only |
| **`plugin` object_type** | Snapshot catalog includes `plugin` object; Registry has no `plugin` target (future) | Snapshot, Registry, Proven Capabilities | **Medium** — parallel to inspect_plugin gap |
| **ChangeSet example target mismatch** | Example: `apply_footer_change` + `target_type: shortcode` + `target_id: footer_contacts`; Bindings/Manifest primary target for `apply_footer_change` = `footer` | ChangeSet, Target Registry (Notes clarify zone vs mechanism) | **Medium** — illustrative example conflicts with binding primary target; Registry Notes explain dual-level scoping |
| **Proven ops not in Manifest** | `inspect_rendered_html`, `inspect_page_storage` listed as proven; **no** matching `operation_id` in Manifest v1 | Proven Capabilities, Manifest | **Medium** — proven without model (evidence uses operational aliases) |
| **Bindings fully_bound count** | Section says «Fully bound (20)» but enumerated list contains **21** operations | Operation Bindings | **Low** — internal arithmetic inconsistency |
| **`environment` field in ChangeSet** | Optional ChangeSet field `environment` (DEV/staging/prod) vs Target Registry `environment` target_id | ChangeSet, Registry | **Low** — homonym; different namespaces (run context vs inspect target) |

---

## 5. Canonical Sources

| Entity / concept | Canonical source | Notes |
|------------------|-------------------|-------|
| `operation_id` | **Operations Manifest v1** | Bindings matrix confirms coverage; forbidden ops have no id |
| `risk_class` (R0–R5) | **Risk Classes v1** | Manifest `default risk` is non-canonical hint |
| `target_id` / `target_type` | **Target Registry v1** | ChangeSet enum subordinate; Snapshot `object_type` aligned where applicable |
| operation ↔ target ↔ policy binding | **Operation Bindings v1** | Resolves Manifest + Registry + Risk into executable policy record |
| ChangeSet schema / lifecycle | **ChangeSet v1** | Templates are pre-formalization aids |
| Rollback semantics / sources / scope | **Rollback v1** | backup-rollback-rules.md = Phase 1 operational companion |
| Site state description | **Site Snapshot Model v1** | HTML/JSON files = evidence, not canonical state model |
| Delta / comparison description | **Diff Model v1** | Plugin dry-run = implementation preview; Diff Model = canonical logical layer |
| Proven capability status | **Proven Capabilities v1** | Manifest alone does not prove execution |
| Mission principles / non-goals | **Mission v1** | Overrides aspirational claims elsewhere |
| `changeset_id` | **ChangeSet v1** | Operator-assigned stable id |
| `diff_id` / diff bundle | **Diff Model v1** | Optional `diff_bundle_id` — convention only in v1 |
| `snapshot_id` | **Site Snapshot Model v1** | Convention only; no persistence format mandated |
| Approval posture by risk | **Risk Classes v1** (matrix) + **Bindings v1** (per operation) | No standalone Approval Model |
| Evidence storage policy | **local-storage-policy.md** | Paths; not evidence schema |
| Plugin REST / runtime behavior | **plugin-mvp/** (v0 contracts) | **Not** Core Model v1; planned implementation docs |

---

## 6. Redundancy Audit

### 6.1 Operations Manifest + Operation Bindings

| Aspect | Assessment |
|--------|------------|
| **Overlap** | Manifest scope rules + default risk tables; Bindings full matrix with approval/backup/validation/rollback |
| **Merge possible?** | Technically yes — single «Operations Policy» document |
| **Pros of merge** | Single file for operators; eliminates Manifest/Bindings navigation split |
| **Cons of merge** | Very large document; Mixes «what exists» (catalog) with «how it binds» (matrix); harder to version independently |
| **Recommendation** | **Do not merge.** Bindings is derivative index; separation matches taxonomy vs cross-product pattern. |

### 6.2 ChangeSet + Rollback

| Aspect | Assessment |
|--------|------------|
| **Overlap** | Shared lifecycle stage Rollback; shared evidence fields; Rollback expectations in ChangeSet flags |
| **Merge possible?** | Partially — Rollback could be ChangeSet appendix |
| **Pros of merge** | Single change-management document |
| **Cons of merge** | Rollback sources, scope levels, post-rollback checklist deserve standalone reference; Rollback used in planning before ChangeSet exists |
| **Recommendation** | **Do not merge.** Complementary layers with intentional nesting. |

### 6.3 Site Snapshot + Diff

| Aspect | Assessment |
|--------|------------|
| **Overlap** | Shared target taxonomy; shared level concepts; Snapshot usage mentions diff |
| **Merge possible?** | Could be «State & Change Model» |
| **Pros of merge** | Unified state/change vocabulary |
| **Cons of merge** | Violates clean state-vs-delta separation; Diff depends on two snapshots — different lifecycle |
| **Recommendation** | **Do not merge.** Both documents already cross-reference; separation is architecturally sound. |

### 6.4 Risk Classes + Operation Bindings (bonus)

| Aspect | Assessment |
|--------|------------|
| **Overlap** | Per-operation risk and policy flags appear in both |
| **Recommendation** | **Do not merge.** Risk Classes = taxonomy; Bindings = operationalized matrix. Bindings defers to Risk Classes explicitly. |

### 6.5 Legacy overlap: backup-rollback-rules.md vs Rollback v1

| Aspect | Assessment |
|--------|------------|
| **Overlap** | Backup confirmation, rollback plan, MVP targets |
| **Recommendation** | **Do not merge** — different maturity (Phase 1 ops vs Core policy). Rollback v1 declared canonical for Core Model; keep backup-rollback-rules as Phase 1 entry point with pointer. |

---

## 7. Evidence Alignment (Proven Capabilities vs Model)

### 7.1 Proven with model support

| Proven area | Model alignment |
|-------------|-----------------|
| Inspection (`inspect_site`, `inspect_page`, `inspect_environment`, `inspect_footer`, `inspect_shortcode`, `inspect_css`, `inspect_plugin`) | Manifest + Bindings + Registry (except plugin target gap) |
| Content/style apply (shortcode, footer, page content, css_fragment) | Manifest apply/draft ops + Registry targets + R2 |
| Backup before apply, validation after apply | ChangeSet lifecycle + Risk Classes R2 + Rollback sources |
| Workflow inspect→backup→apply→validate | Manifest lifecycle + ChangeSet stages |
| Proven targets: page, shortcode, footer, css_fragment, environment, site | Subset of Registry v1 |

### 7.2 Proven without model (or partial model)

| Proven capability | Gap |
|-------------------|-----|
| `inspect_rendered_html` | **No** `operation_id` in Manifest v1 — operational alias for browser/layout audit |
| `inspect_page_storage` | **No** `operation_id` in Manifest v1 — maps loosely to inspect_page + evidence export |
| Phase 2A dry-run semantics | Maps to `draft_shortcode_change` semantics but not formal draft engine |
| Helper-based writes on DEV | Proven practically; **not** via formal plugin REST apply endpoints (v0.1 read+dry-run only) |

### 7.3 Model without proof

| Model element | Proof status |
|---------------|--------------|
| `rollback_change` completed + post-rollback validation | **Not yet proven** (Proven Capabilities explicit) |
| `restore_backup` completed run | **Not yet proven** |
| `apply_menu_change` via formal plugin API | **Not yet proven** |
| `draft_*` as automated ChangeSet product | **Not yet proven** (dry-run semantics partially proven) |
| Targets: post, widget, menu, header, theme_option, media, plugin | **Not yet proven** as isolated apply/inspect targets (menu/footer work exists but not as direct menu API write) |
| `apply_change` umbrella | Blocked by design — N/A for proof |
| Site Snapshot / Diff as formal persisted bundles | **Model only** — evidence exists as ad-hoc JSON/HTML, not canonical snapshot_id/diff_bundle_id artifacts |
| Full Bindings enforcement | **Model only** — no runtime refusal engine proven against full matrix |

### 7.4 Alignment score

| Metric | Value |
|--------|------:|
| Manifest operations with some DEV evidence | ~18 / 29 |
| Manifest operations fully proven end-to-end via plugin MVP | **0** apply ops (helpers used) |
| Registry targets proven | 6 / 12 |
| Critical recovery ops proven | 0 / 2 (`rollback_change`, `restore_backup`) |

**Conclusion:** Proven Capabilities **honestly diverges** from Manifest where evidence used operational aliases or helpers. Core Model is **broader than proof** — expected for v1 policy-first stack.

---

## 8. Runtime Readiness

Assessment: **ready for runtime use** per layer (documentation → implementation bridge). Not a runtime design pass.

| Layer | Ready | Rationale |
|-------|-------|-----------|
| **Mission** | **YES** | Stable charter; sufficient for runtime boundary decisions |
| **Operations Manifest** | **PARTIAL** | Complete catalog; inspect_plugin gap; apply_change blocked; no endpoint map |
| **Risk Classes** | **YES** | Complete R0–R5 mapping; scope escalation rules documented |
| **Target Registry** | **PARTIAL** | Complete v1 taxonomy; missing `plugin`; several targets read-only only |
| **Operation Bindings** | **PARTIAL** | Full matrix documented; 1 target_gap, 1 blocked, 7 partially_bound; no enforcement engine |
| **ChangeSet** | **PARTIAL** | Schema and lifecycle clear; no persistence/API; Bindings compliance not automated |
| **Rollback** | **PARTIAL** | Policy complete; no proven automated rollback execution |
| **Site Snapshot Model** | **PARTIAL** | Logical model ready; no acquisition pipeline, snapshot_id persistence, or plugin schema |
| **Diff Model** | **PARTIAL** | Logical model ready; plugin dry-run v0 partial alignment only |
| **Proven Capabilities** | **YES** | Fulfills evidence register role; not intended as runtime input |

**Overall runtime readiness:** **PARTIAL** — policy stack is implementable; execution layer (plugin-mvp v0, operator helpers) lag Core Model.

---

## 9. Core Model Stability

**Status: Stable**

### Argumentation

**For Stable (chosen):**

- Ten Core layers documented with explicit purposes, non-goals, and cross-references.
- Canonical sources identified for all primary entities.
- Known gaps (`inspect_plugin`, `apply_change`, proven/model divergences) are **explicitly recorded**, not silent drift.
- No harmful circular dependencies or responsibility collisions requiring redesign.
- Redundancy (Bindings, Rollback vs ChangeSet) is **justified** and documented.
- Snapshot/Diff addition completes state/change vocabulary without breaking policy stack.
- Human-supervised v1 workflows can operate using ChangeSet + templates + Proven Capabilities without new Core layers.

**Not Mature because:**

- Recovery operations not proven end-to-end.
- Plugin MVP implements subset (read + dry-run); Core Model not enforced in code.
- Terminology homonyms (snapshot, environment) still appear in Phase 1 operational docs.

**Not Emerging because:**

- Layer boundaries are settled; further work is runtime contracts and evidence growth, not Core taxonomy discovery.

**Not Incomplete because:**

- No critical undocumented layer blocks v1 policy operation; deferred items are runtime/API, not Core Model holes.

---

## 10. Architecture Recommendation

### Selected: **A — Stop Core Modeling, move to Runtime Contracts**

### Reason

1. **Core Model v1 is internally coherent** — audit found no structural flaw requiring redesign (option C) or mandatory new Core layer (option B).
2. **Documented GAPs are operational/runtime**, not missing Core taxonomy — Approval/Validation/Evidence schemas can emerge as **Runtime Contract fields** tied to ChangeSet, not as new Core layers.
3. **Proven Capabilities demonstrates model is usable** — DEV evidence maps to most layers; gaps are implementation and proof, not model absence.
4. **plugin-mvp v0 already exists** as the natural next documentation surface — reconciliation-map-v0 explicitly bridges Core → plugin.
5. **Further Core modeling risks drift** — Mission/Bindings/Snapshot/Diff stack is complete for human-operated v1; expansion without runtime pressure violates controlled operationalization discipline.

### Why not B (One more Core Layer)

- Approval, Validation, Evidence gaps do not warrant standalone Core layers; they are ** facets of ChangeSet execution** already partially specified.
- Adding a layer now would duplicate ChangeSet/Rollback/Proven Capabilities without new semantic territory.

### Why not C (Significant redesign)

- No circular dependency or responsibility collision requires restructuring.
- Terminology divergences are documentable and minor.
- inspect_plugin gap is a **Registry extension candidate**, not architecture failure.

### Suggested next focus (documentation only, out of audit scope)

- Runtime Contracts pass: map Core Model → plugin-mvp v0/v1 contracts.
- Resolve proven-without-model aliases (`inspect_rendered_html`, `inspect_page_storage`) via Manifest amendment **or** Proven Capabilities relabeling — in Runtime/charter pass, not Core redesign.
- Close inspect_plugin gap when charter approves `plugin` target in Registry.

---

## Appendix A — Suggested logical stack (post-audit reference)

Documentation-only ordering for navigation (not a new layer):

```
Mission
  ↓
Site Snapshot Model (state)
  ↓
Diff Model (change)
  ↓
Target Registry (taxonomy)
  ↓
Operations Manifest (operations)
  ↓
Risk Classes (risk)
  ↓
Operation Bindings (cross-product)
  ↓
ChangeSet (execution unit)
  ↓
Rollback (recovery)
  ↓
Proven Capabilities (evidence overlay)
```

---

## Appendix B — Audit metadata

| Field | Value |
|-------|-------|
| Review version | v1 |
| Review date | 2026-06-19 |
| Code changed | No |
| Roadmap changed | No |
| New layers created | No |
| Runtime changed | No |
