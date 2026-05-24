# RU Typography Governance Integrity Audit v2

> **NOT AUTHORITY** — read-only audit record only.  
> **Authority:** [russian-no-word-splitting-typography-v1.md](../russian-no-word-splitting-typography-v1.md) · **RU QA preset:** [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md).

**Date:** 2026-05-24  
**Lane:** B — Website Factory / Governance Integrity Audit  
**Scope:** `projects/mars-website-factory/`, `agents/frontend-gulp-agent/`, `agents/mars-forge/` (typography/QA routing only)  
**Method:** Read-only cross-doc grep + targeted file review. **No** file fixes, patches, commits, or pushes.  
**Baseline:** Post [ru-typography-stabilization-pass-v1.md](ru-typography-stabilization-pass-v1.md) (2026-05-24).

---

## Authority integrity

### Canon pair: no direct contradictions

| Document | Declared role |
|----------|----------------|
| [russian-no-word-splitting-typography-v1.md](../russian-no-word-splitting-typography-v1.md) | **Authority** — CSS/HTML overflow policy, forbidden patterns, selective `&nbsp;`, allowed `overflow-wrap: break-word` on long body only |
| [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md) | **Canonical preset** — RU commercial viewport matrix + QA checks + mandatory REPORT line |

**Cross-reference shape:** canon → preset for widths/checks; preset → canon for overflow/CSS. This is a **split authority model** (policy vs QA procedure), not a circular claim of duplicate supremacy.

**Verified alignment:**

- Forbidden set (`anywhere`, `break-all`, global body `break-word`, UI/heading fragmentation) is consistent across canon, preset check table, [production-hardening-rules-v1.md](../production-hardening-rules-v1.md), [foundation-systems/responsive-system-v2.md](../foundation-systems/responsive-system-v2.md) §7, and Forge [rhythm-governance-checklist.md](../../agents/mars-forge/rhythm-governance-checklist.md) §10.
- Allowed `overflow-wrap: break-word` on long body copy only — consistent in canon §1.4, hardening, responsive-system.
- REPORT line format is identical everywhere it appears.

### Hierarchy is documented and mostly unambiguous

Stabilization pass documents the intended stack:

```text
1. russian-no-word-splitting-typography-v1.md  — CSS/HTML overflow (authority)
2. ru-landing-qa-preset-v1.md                  — RU commercial QA widths + checks (canonical preset)
3. frontend-production-rules-v0.md §12         — operator summary + pointers
4. Satellite docs                              — pointers; generic widths supplementary
```

**Residual ambiguity (not contradiction):**

| Topic | Issue |
|-------|--------|
| Label collision | Both docs use **canonical** for different domains (CSS policy doc points to “canonical widths”; preset is “canonical viewport”). A hurried reader may conflate “canonical breakpoints” in [responsive-system-v2.md](../foundation-systems/responsive-system-v2.md) (SCSS tokens: 768 / 1280) with “canonical QA widths” (preset: 760 / 1180 / …). |
| `word-break` vs `overflow-wrap` | [production-hardening-rules-v1.md](../production-hardening-rules-v1.md) forbids `word-break: break-word` globally for RU/UI; canon forbids it on UI/headings only. **Stricter satellite rule** — not conflicting for intended use, but a maintainer could treat hardening as overriding canon’s body-copy nuance. |
| Forge §10 shorthand | “UI `break-word`” does not distinguish `word-break` vs `overflow-wrap` property names; canon distinguishes them. Operators applying only the checklist shorthand might mis-scope fixes. |

### Duplicated authority wording (maintenance risk, not active conflict)

| Location | Risk |
|----------|------|
| [reports/no-word-splitting-typography-rule-integration-v1.md](no-word-splitting-typography-rule-integration-v1.md) | Contains **full** forbidden-CSS tables, base CSS snippets, and QA widths — reads like a **live second authority**. Stabilization pass marks it **historical**; file itself has **no** “historical only” banner → **false-authority drift risk**. |
| [reports/ru-typography-stabilization-pass-v1.md](ru-typography-stabilization-pass-v1.md) | Repeats hierarchy + viewport tables for operator clarity — acceptable as REPORT. |

### Circular references

**None found** that create logical loops (A forbids what B requires). Mutual links between canon ↔ preset are intentional delegation.

---

## Cross-link integrity

### Well-linked hub documents (canon + preset present)

| Area | Files |
|------|--------|
| Factory core | `README.md`, `OPERATIONAL-INDEX.md`, `registries.md`, `frontend-production-rules-v0.md`, `frontend-handoff-contract-v0.md`, `operational-qa-entry-v1.md`, `reference-workspace-qa-flow-v1.md`, `production-hardening-rules-v1.md`, `typography-rhythm-governance.md`, `responsive-intent-governance.md`, `visual-regression-workflow-v1.md`, `canonical-implementation-pack-architecture.md`, `frontend-foundation-blueprint-v1.md`, `foundation-systems/responsive-system-v2.md` |
| Gulp agent | `AGENT.md`, `README.md`, `frontend-rules.md`, `qa-checklist.md`, `workflow.md`, `constraints.md`, `prompt-patterns.md` |
| Mars Forge | `AGENT.md`, `README.md`, `rhythm-governance-checklist.md`, `responsive-intent-checklist.md`, `design-token-checklist.md`, `qa-checklist.md` (rhythm layer pointer) |

### Orphan / weak-link documents (no canon/preset link; RU typography bypass risk)

| Document | Gap |
|----------|-----|
| [qa-prompt-rules-v0.md](../qa-prompt-rules-v0.md) §11.4 Frontend QA | Compares against handoff + `frontend-prompt-discipline-v0.md` only — **no** RU typography or preset |
| [reporting-standard-v0.md](../reporting-standard-v0.md) | **No** `RU TYPOGRAPHY / NO WORD-SPLITTING` REPORT line |
| [frontend-prompt-discipline-v0.md](../frontend-prompt-discipline-v0.md) | QA viewports **375 / 768 / 1280** — no RU preset pointer |
| [prompt-structure-standard-v0.md](../prompt-structure-standard-v0.md) | Frontend QA lane lists **375 / 768 / 1280** only |
| [golden-implementation-slice-v1.md](../golden-implementation-slice-v1.md) | Quick verification cites **375px** + reference flow — no explicit preset link in quick path |
| [adoption-validation-flow-v1.md](../adoption-validation-flow-v1.md) | §5 responsive + compact REPORT: **375/768/desktop** only |
| [block-quality-tiers-v1.md](../block-quality-tiers-v1.md) | Responsive requirements: **375 / 768 / desktop** — no supplementary label |
| [implementation-extraction-discipline-v1.md](../implementation-extraction-discipline-v1.md) | Extraction REPORT template: responsive **375/768/desktop PASS** — no RU line |
| [foundation-adoption-rules-v1.md](../foundation-adoption-rules-v1.md) | 375px visual check — no RU typography |
| [compositional-structure-awareness.md](../compositional-structure-awareness.md) | “Responsive QA passes” gate — **no** RU typography coupling |
| [qa-validation-model.md](../qa-validation-model.md) | Lane model — **no** RU typography cross-link |
| Gulp `handoff-rules.md`, `reporting.md` | Delegate to contract / qa-checklist — **no** direct canon link (indirect only) |
| Forge `workflow.md` §4 Responsive validation | **375 / 768 / 1280** spot widths — no preset |
| Forge `foundation-lite-checklist.md` | 375px overflow only |
| Forge `production-readiness-checklist.md` | **No** RU typography |
| Reference case [reference-cases/triumph-manipulator-landing/frontend-handoff-v0.md](../reference-cases/triumph-manipulator-landing/frontend-handoff-v0.md) | Legacy **375 / 768 / 1024 / 1280** matrix — **no** RU preset (historical case artifact) |

### Isolated QA flows still reachable

| Flow | Status |
|------|--------|
| [operational-qa-entry-v1.md](../operational-qa-entry-v1.md) → [reference-workspace-qa-flow-v1.md](../reference-workspace-qa-flow-v1.md) | **Correct primary route** for RU; RU section is mandatory when locale is RU |
| [adoption-validation-flow-v1.md](../adoption-validation-flow-v1.md) | Parallel adoption path — **bypasses** RU preset in compact checklist |
| [visual-regression-workflow-v1.md](../visual-regression-workflow-v1.md) | Supplementary three-width capture — **correctly** defers typography QA to preset |
| [qa-prompt-rules-v0.md](../qa-prompt-rules-v0.md) Frontend QA lane | Formal QA prompts can **bypass** preset if checklist reference stays generic |

---

## Viewport consistency

### Authoritative RU commercial QA widths (preset)

`320` · `375` · `390` · `420` · `760` · `1180` · `1320` · `1440`

### SCSS / design breakpoint tokens (responsive-system-v2)

`576` · `768` · `1024` · `1280` — **implementation** breakpoints, not QA matrix. Documented as separate concern; **not** a contradiction if read in context.

### Generic supplementary lists (correctly downgraded in primary chain)

| Doc | Widths | Supplementary label |
|-----|--------|---------------------|
| `reference-workspace-qa-flow-v1.md` | 375 / 768 / desktop (≥1024) | **Yes** — explicit for RU |
| `visual-regression-workflow-v1.md` | 375 / 768 / ≥1280 | **Yes** |
| `frontend-handoff-contract-v0.md` | 375 / 768 / 1280 in example row | **Yes** (RU row overrides) |
| `operational-qa-entry-v1.md` compact pass | RU preset first, then supplementary 375/768/desktop | **Yes** |

### Generic lists **without** supplementary downgrade (drift risk)

| Doc | Widths | Risk |
|-----|--------|------|
| `prompt-structure-standard-v0.md` | 375 / 768 / 1280 | Reads as **default Frontend QA** authority |
| `frontend-prompt-discipline-v0.md` | 375 / 768 / 1280 | Same |
| `block-quality-tiers-v1.md` | 375 / 768 / desktop | Tier gate may be taken as **complete** responsive QA |
| `adoption-validation-flow-v1.md` | 375 / 768 / desktop | Adoption-ready verdict without RU widths |
| `golden-implementation-slice-v1.md` | 375px quick path | Under-tests RU edge widths (320, 390, 420, 760, …) |
| `implementation-extraction-discipline-v1.md` | 375 / 768 / desktop | Extraction PASS without typography |
| Forge `workflow.md` | 375 / 768 / 1280 | Phase 4 validation default |
| Triumph reference handoff | 375 / 768 / 1024 / 1280 | **Legacy** case; may be copied into new handoffs |

### Near-collision widths (operator confusion, not doc conflict)

| Preset QA | SCSS / generic | Note |
|-----------|----------------|------|
| **760** | **768** (`$bp-md`) | Different purposes; agent may test only 768 and miss 760 typography edge |
| **1180** | **1024** / **1280** | Preset includes 1180 and 1320; generic docs jump 768 → 1280 |

**Verdict:** Primary operational chain (**operational-qa-entry → reference-workspace-qa-flow → ru-landing-qa-preset**) is consistent. **Secondary** prompt/adoption/tier/extraction paths still present **375/768/desktop** as implicit full matrix.

---

## Overflow policy audit

### Factory + agents scope grep (2026-05-24)

All in-scope mentions of `overflow-wrap`, `word-break`, `break-all`, `break-word`, `anywhere`, `hyphens` align with canon **except** historical/integration copies.

| Finding | Severity |
|---------|----------|
| No in-scope doc recommends `overflow-wrap: anywhere` as fix | **Clear** |
| `break-word` appears only with **long body copy only** qualifier or **forbidden on UI** | **Clear** |
| [responsive-system-v2.md](../foundation-systems/responsive-system-v2.md) §7 | Correct: layout first (`min-width: 0`), then scoped body `break-word` |
| [reference-workspace-qa-flow-v1.md](../reference-workspace-qa-flow-v1.md) | Explicit: prefer layout before word-breaking CSS |
| [typography-rhythm-governance.md](../typography-rhythm-governance.md) C-04/C-05 | Blocks `nowrap` / `&nbsp;` chains / fragmentation for orphans |

### Hidden “just use break-word” vectors

| Vector | Mechanism |
|--------|-----------|
| Generic “no horizontal scroll” checks without typography guard | Agent fixes overflow at 375px with global/`body`/`h*` break rules |
| [responsive-system-v2.md](../foundation-systems/responsive-system-v2.md) §2 hierarchy | “No horizontal scroll (hard)” ranked first — mitigated by §7 link to canon, but **skim risk** remains |
| Integration report full CSS examples | Agent copies snippets without reading live canon |
| `frontend-prompt-discipline` / `qa-prompt-rules` | No overflow policy pointer — implementation prompts may improvise |

**No** soft phrases like “simply add `break-word`” found in scoped Factory/agent docs post-stabilization.

---

## Procedural drift audit

### Aligned procedures (primary path)

```text
operational-qa-entry-v1
  → ru-landing-qa-preset (RU commercial mandatory)
  → reference-workspace-qa-flow (RU section + supplementary viewports)
  → REPORT: RU TYPOGRAPHY / NO WORD-SPLITTING — …
```

Also aligned: `frontend-production-rules-v0` §12, Gulp `qa-checklist.md`, Forge `rhythm-governance-checklist.md` §10, Forge `responsive-intent-checklist.md` RU item.

### Flow contradictions / ordering gaps

| Issue | Detail |
|-------|--------|
| Dual REPORT lines | `reference-workspace-qa-flow` encourages **both** `375/768/desktop spot-check PASS` **and** RU typography line. Agent may emit only the generic line. |
| Gulp checklist order | **Responsive** (handoff widths) appears **before** **RU typography** — responsive PASS possible before RU preset run |
| Forge rhythm is conditional | [qa-checklist.md](../../agents/mars-forge/qa-checklist.md): “Rhythm governance … **when typography / section cadence is in scope**” — RU commercial landings always have typography, but **Lite** / narrow tasks may skip rhythm overlay |
| Forge Standard “≤3 specialists” | [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md) optional specialists — rhythm/responsive-intent not guaranteed if operator minimizes |
| Adoption / extraction compact checklists | **Responsive PASS** without mandatory RU line — procedural alternate route |
| Frontend QA prompt spec | [qa-prompt-rules-v0.md](../qa-prompt-rules-v0.md) §11.4 — no RU typography in “compares against” list |

### Old “responsive PASS without typography” logic

Still present in:

- `adoption-validation-flow-v1.md` compact template  
- `implementation-extraction-discipline-v1.md`  
- `block-quality-tiers-v1.md`  
- `compositional-structure-awareness.md` (semantic + responsive pass → visual reconciliation)  
- Operational **examples** under `operational-examples/` (historical PASS strings)

These are **not** contradictions with canon if labeled supplementary/historical — many are **not** labeled.

---

## Duplication risks

| Class | Examples | Classification |
|-------|----------|----------------|
| **Acceptable** | REPORT line repeated in 6+ docs; pointer-only §12 in `frontend-production-rules-v0`; Forge §10 defers to canon | Intentional reinforcement |
| **Dangerous** | [no-word-splitting-typography-rule-integration-v1.md](no-word-splitting-typography-rule-integration-v1.md) full rule tables | **Legacy duplication** — false authority |
| **Maintenance burden** | Forbidden CSS list in canon + hardening + responsive §7 + integration report + rhythm C-05 | Drift on next rule change |
| **Maintenance burden** | Viewport lists in 15+ docs | C-02 partially fixed in primary chain only |
| **Legacy duplication** | Triumph reference handoff QA matrix | Case artifact; may infect new handoffs |

---

## False authority risks

| Document / phrase | Sounds like authority | Actual status |
|-------------------|----------------------|---------------|
| `golden-implementation-slice-v1.md` — “canonical reference” | Implementation quality SoT | **Not** typography/overflow authority |
| `responsive-system-v2.md` — “Canonical breakpoints” | QA viewport authority | **SCSS** tokens only; RU QA → preset |
| `no-word-splitting-typography-rule-integration-v1.md` | Live rule pack | **Historical** integration REPORT (weakly signaled) |
| `block-quality-tiers-v1.md` — “Responsive requirements” | Complete responsive gate | **Partial** spot-check; no RU typography |
| `adoption-validation-flow-v1.md` — “Adoption-ready” | Production sign-off | **No** RU typography in compact verdict |
| `reference-workspace-qa-flow` REPORT line 1 | Overall QA PASS | **Supplementary** interaction pass only for RU |
| `qa-prompt-rules-v0.md` Frontend QA | Lane-complete checklist | **Missing** RU canon in §11.4 |

---

## Failure mode simulations

### FM-1 — Only Forge `qa-checklist.md` (Lite / narrow scope)

**Path:** Lite mode → core slice only → typography “not in scope” → skip `rhythm-governance-checklist.md` → **no RU preset**, no REPORT line.  
**Outcome:** Responsive overflow fixed with forbidden CSS possible; **RU TYPOGRAPHY** line absent.

### FM-2 — Only `responsive-system-v2.md`

**Path:** Read §2 “no horizontal scroll (hard)” + §7 anti-overflow → implement `break-word` on flex child heading to kill scroll.  
**Outcome:** Partial mitigation via §7 canon link **if** agent reads §7; **if** only §2 — mid-word breaks / UI `break-word`.  
**Mitigation in doc:** §7 + §8 RU preset pointer — **not** foolproof on skim.

### FM-3 — Only Gulp `frontend-rules.md`

**Path:** Follow authority links → correct policy.  
**Risk:** `qa-checklist` responsive row (375/768/1280) satisfied first → REPORT claims responsive PASS → RU preset never run.

### FM-4 — Only `qa-prompt-rules-v0.md` §11.4 + `frontend-prompt-discipline-v0.md`

**Path:** Frontend QA prompt at 375/768/1280 → build PASS → responsive spot-check PASS.  
**Outcome:** **No mandatory RU widths**; **no** `RU TYPOGRAPHY` line; word-splitting undetected at 320/390/420/760/1180/1320/1440.

### FM-5 — Only `adoption-validation-flow-v1.md` or `block-quality-tiers-v1.md`

**Path:** Compact checklist → `Responsive 375/768/desktop: PASS`.  
**Outcome:** **False adoption/tier confidence** for RU commercial landing.

### FM-6 — Only `golden-implementation-slice-v1.md` quick verification

**Path:** `375px QA` + reference flow.  
**Outcome:** May open reference flow (has RU section) but quick path **under-specifies** widths; agent may never run full preset.

### FM-7 — Copy from `no-word-splitting-typography-rule-integration-v1.md`

**Path:** Treat integration REPORT as current spec; duplicate tables into project CSS.  
**Outcome:** Policy may match today but **bypasses** preset QA widths and future canon changelog.

### FM-8 — `nowrap` / `&nbsp;` chain abuse

**Path:** `reference-workspace-qa-flow` desktop widows bullet + rhythm C-04 → agent uses `nowrap` or full-heading `&nbsp;` chains to fix orphans.  
**Outcome:** Doc **warns against** this — failure is **operator/agent non-compliance**, not doc contradiction.

### FM-9 — Forge Standard + minimal specialists

**Path:** Skip optional `rhythm-governance` and `responsive-intent` → rely on workflow §4 (375/768/1280).  
**Outcome:** RU checks in specialist checklists **never run**; foundation gulp checklist may still catch RU **if** full foundation QA runs before freeze.

---

## Remaining contradictions

| ID | Description | Severity |
|----|-------------|----------|
| **K-01** | None between `russian-no-word-splitting-typography-v1.md` and `ru-landing-qa-preset-v1.md` on forbidden CSS or QA intent | — |
| **K-02** | `production-hardening-rules-v1.md` forbids `word-break: break-word` more broadly than canon (UI/headings only) | **Low** — stricter satellite |
| **K-03** | Primary REPORT encourages generic `375/768/desktop PASS` **and** RU line — two pass/fail narratives | **Medium** — procedural |
| **K-04** | SCSS breakpoints (768) vs QA preset (760) — different numbers, same “tablet” mental model | **Low** — confusion |

**No** active doc in the primary chain instructs `overflow-wrap: anywhere` or global body `break-word` for RU landings.

---

## Remaining ambiguity

| ID | Topic |
|----|--------|
| **A-01** | When is a landing “RU commercial” vs mixed locale? Canon: mandatory for RU Factory landings; no decision tree in QA entry. |
| **A-02** | Forge rhythm overlay “when in scope” vs always-on for RU commercial. |
| **A-03** | Which REPORT line is gating for freeze: generic responsive PASS or `RU TYPOGRAPHY` line? |
| **A-04** | `UI break-word` shorthand in Forge §10 vs two CSS properties in canon. |
| **A-05** | Historical integration report vs live canon — no in-file deprecation banner. |
| **A-06** | Reference Triumph handoff matrix vs preset — which wins for Triumph-like projects? |

---

## Recommended stabilization actions

*(Documentation recommendations only — **not** executed in this audit.)*

1. **Banner** on `no-word-splitting-typography-rule-integration-v1.md`: `HISTORICAL — authority: russian-no-word-splitting-typography-v1.md`.
2. **Cross-link** RU canon + preset into: `qa-prompt-rules-v0.md` §11.4, `reporting-standard-v0.md` §4.2/4.3, `frontend-prompt-discipline-v0.md`, `prompt-structure-standard-v0.md` (Frontend QA lane).
3. **Amend** compact checklists: `adoption-validation-flow-v1.md`, `implementation-extraction-discipline-v1.md`, `block-quality-tiers-v1.md` — add “RU commercial → ru-landing-qa-preset” + REPORT line; mark generic widths **supplementary**.
4. **Forge** `workflow.md` §4 + `foundation-lite-checklist.md`: pointer to RU preset when locale is RU.
5. **Clarify** in `reference-workspace-qa-flow-v1.md` REPORT block: generic line is **non-gating** for RU commercial when RU line is FAIL/partial.
6. **Reorder** Gulp `qa-checklist.md`: RU typography block **before** generic responsive spot-check for RU projects (or merge into one step).
7. **Forge** `qa-checklist.md`: state RU commercial landings → rhythm §10 **always in scope** (not conditional).
8. **Triumph reference handoff** — footnote: superseded by `ru-landing-qa-preset-v1.md` for RU QA widths.
9. **Terminology** — rename responsive-system heading to “SCSS breakpoint tokens” vs preset “QA viewport matrix” to reduce “canonical” collision.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Runtime/CSS in workspaces (V5, reference-v1, client trees) | **Not audited** — scope excluded |
| Whether operators consistently classify “RU commercial” | **UNKNOWN** — docs assume classification |
| Automated CSS lint for word-break | **Not implemented** (canon §5) — still human DevTools |
| Non-Russian locales | Canon explicit: other locales need their own pack — **not verified** in scope |
| Full 312-file Factory tree — every peripheral doc | **Sampled** via grep + priority reads; Tier-3 governance docs may contain uncited viewport prose |
| Agent behavior in production | **UNKNOWN** — audit is documentation integrity only |

---

*Audit v2 complete — read-only.*
