# MARS Website Factory — Failure Class: Asset Identity Collision v1

**Status:** **Canonical Foundation Authority** — documented **human-operated** failure class and mitigation strategy for Website Factory brand-asset selection from design sources.  
**Not:** runtime orchestration, automated logo detector, CI gate, vision parser, or policy engine.

**Version:** v1  
**Date:** 2026-06-17

**Registry token:** `ASSET_IDENTITY_COLLISION`

**Registry:** [registries.md §7](../registries.md#7-factory-failure-classes)

**Provenance:** FP-0002 Shpigovsky.ru — Header build from `Шпиговский.fig` (2026-06). Automated FIG parse selected **first discovered image node** as logo; forensic review proved **wrong brand raster** shipped to production path.

**Peer authorities (detail — do not duplicate here):**

| Document | Role |
|----------|------|
| [design-source-to-frontend-mapping-governance-v1.md](../design-source-to-frontend-mapping-governance-v1.md) | L-07 Assets layer — provenance and mapping obligations |
| [website-factory-source-discovery-v1.md](../website-factory-source-discovery-v1.md) | SOURCE-007 Assets intake |
| [frontend-failure-attribution-model-v1.md](../frontend-failure-attribution-model-v1.md) | FAILURE EVENT → Expected Gate → Attribution Verdict |
| [frontend-design-qa-matrix-v1.md](../frontend-design-qa-matrix-v1.md) | DQ-08 Assets — downstream wrong-asset detection |
| [pixel-fidelity-audit-rules-v1.md](../pixel-fidelity-audit-rules-v1.md) | PF-07 Asset fidelity |
| [production-standards-governance-v1.md](../production-standards-governance-v1.md) | C-09 Assets — per-project SSOT |
| [website-factory-production-roadmap-v2-draft.md](../website-factory-production-roadmap-v2-draft.md) | Lesson L-13 |

**Honesty boundary:** This document is **documentation discipline**. It does **not** claim an in-repo Brand Asset Detection engine unless a project explicitly adopts checklists as tooling. **Does not** modify FP-0002 workspace artefacts, build workflow, or executable code.

**Scope boundary:** Factory-wide failure taxonomy and operator mitigation only. **No** runtime change. **No** FP-0002 artefact edits.

---

## 1. Definition — ASSET IDENTITY COLLISION

| Field | Value |
|-------|-------|
| **Class ID** | `ASSET IDENTITY COLLISION` |
| **Registry token** | `ASSET_IDENTITY_COLLISION` |
| **Definition** | A **brand-critical asset** (logo, wordmark raster, favicon source, institutional mark) was **selected or wired** from a design file containing **multiple competing brand identities**, because selection relied on **positional or traversal heuristics** (e.g. first image node, first `IMAGE` fill, first logo-sized rectangle) **without** confirming that the chosen node belongs to the **chartered client brand** for the active project. |
| **Collision** | Two or more distinct brand marks coexist in one FIG / design pack; the system or agent picks a node that is **visually plausible as a logo** but **semantically belongs to another brand** embedded in the same file (prior client work, library component, hidden frame, alternate page, or reused template art). |
| **Distinct from** | Placeholder asset (no real file); wrong **variant** of the **correct** brand (color-on-background — PF-07 Major); compressed crop drift; project-identity erosion via cross-project template reuse ([transfer-drift-taxonomy.md](../transfer-drift-taxonomy.md)) |

**Core failure shape:**

```text
One FIG file
  ├── brand A logo raster (first in traversal order)  ← WRONGLY SELECTED
  └── brand B logo raster (correct for chartered project)  ← CORRECT BUT SKIPPED
```

---

## 2. Real Incident — FP-0002

| Field | Value |
|-------|-------|
| **Execution case** | FP-0002 — Shpigovsky.ru (`Шпиговский.fig`) |
| **Scope** | Header logo during FIG-driven Header assembly |
| **Chartered brand** | **Шпиговский дом** / Shpigovsky Dom |
| **Wrong selection** | Figma node **`1:880`** · image hash **`de219c6e462c8bf42469bb33751a81252eedc07f`** · brand identity **Skinerica** (foreign mark embedded in same FIG) |
| **Correct selection** | Figma node **`1:6720`** · image hash **`262f79db29ec4dc2b9ae2e793d5c8cc6382c307b`** · brand identity **Шпиговский дом** |
| **Selection rule that failed** | **First discovered image node** in Header scope treated as logo |
| **Forensic evidence** | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/logo_forensic_out.json` — multiple `image 219` nodes; two dominant logo-sized hash groups (`de219c6e…` × 13 instances; `262f79db…` × 11 instances) |
| **Production impact** | Wrong client branding in production build path until caught by forensic / operator review |

**Read-only instance artefacts (do not edit per promotion scope):** FP-0002 REPORTS under `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/`.

---

## 3. Root Cause

| Cause | Explanation |
|-------|-------------|
| **Heuristic: first image = logo** | FIG traversal returns image nodes in document order. The **first** logo-sized `ROUNDED_RECTANGLE` with `IMAGE` fill is **not** guaranteed to be the chartered brand mark. |
| **Multi-brand FIG hygiene** | Design files may retain **prior client marks**, **component library** instances, **hidden** or **off-canvas** frames, and **duplicate** raster names (e.g. generic `image 219`) across pages. |
| **Missing identity binding** | L-07 / C-09 rows did not require **hash + node id + brand text association** before wiring `src/img/` or header partial. |
| **Upstream gate gap** | Composition gates (Group Decomposition, Layout Spec) address **structure**, not **which raster** represents brand identity. |

**Root cause statement (normative):**  
**The first found image node is not a guaranteed brand asset.**

---

## 4. Detection Signals

Operators and agents **must treat the following as collision warnings** — not as auto-resolution hints:

| Signal | Description |
|--------|-------------|
| **Multiple logo candidates** | More than one image node in logo aspect-ratio band (typical header width 120–320px, height 30–80px) within Header scope or whole FIG |
| **Identical dimensions, different hashes** | Same `w×h` (e.g. `205×46`) on multiple nodes with **different** `imageHash` / content hash |
| **Different hashes, same generic name** | Nodes named `image 219`, `logo`, `image`, `Frame` with distinct raster payloads |
| **Different brand texts nearby** | Adjacent TEXT nodes reference **different** institutional names (e.g. «Шпиговский дом» vs foreign clinic brand) while multiple image candidates exist |
| **Cross-page asset scatter** | Logo-sized images on **non-chartered** pages or sections inside the same FIG (portfolio, template, alternate home) |
| **Hidden / library components** | Instances from shared components; assets on **non-visible** layers; symbols reused across unrelated brands |
| **Hash group count > 1** | Forensic grouping shows **two or more** dominant hash clusters in logo dimension band |
| **Repeated usage imbalance** | One hash appears more often because of **template reuse**, not because it is the chartered mark |

**When ≥2 signals present:** **STOP** — do not wire asset to production. Run **Recommended Selection Chain** (§7).

---

## 5. Risk

| Risk | Severity |
|------|----------|
| **Wrong client branding in production build** | **Critical** — displays another organization's mark on a live or staging client site |
| **Trust / legal exposure** | Misattribution of medical, financial, or institutional identity |
| **Late discovery cost** | Defect may pass technical build and composition gates; caught only at operator visual review or forensic audit |
| **False confidence from build PASS** | Compiled output is **valid** but **brand-wrong** — ROOT COMPLIANCE and Layout Spec gates do not inspect raster identity |

---

## 6. Mitigation — Forbidden Rule

### FORBIDDEN: `FIRST IMAGE = LOGO`

| Forbidden heuristic | Why |
|---------------------|-----|
| First `IMAGE` fill in traversal order | Document order ≠ brand authority |
| First `ROUNDED_RECTANGLE` in Header frame | Header may contain foreign or legacy raster |
| First node matching logo dimensions | Multiple brands may share similar bounds |
| First export from FIG auto-parser | Parser has no charter context without identity layer |
| Lowest node id | Id order is not semantic |

**Normative rule:** No agent, script, or operator shorthand may treat **first discovered image** as the **approved logo** without completing the **Brand Asset Detection Layer** (§7) and recording provenance on L-07 / C-09.

---

## 7. Recommended Selection Chain — Brand Asset Detection Layer

Human-operated or tooling-assisted chain. **Not** claimed as automated runtime in-repo.

```text
candidate discovery
        ↓
hash grouping
        ↓
text association
        ↓
aspect ratio validation
        ↓
repeated usage analysis
        ↓
operator review (if confidence low)
```

| Step | Action | Output |
|------|--------|--------|
| **1. Candidate discovery** | Enumerate **all** image nodes in chartered scope (Header logo group, C-09 list, hero brand zone) **and** flag whole-FIG logo-band candidates | Candidate table: `node_id`, `name`, `w×h`, `parent chain`, `page/frame` |
| **2. Hash grouping** | Group by content hash (`imageHash` / exported file hash) | Hash clusters with instance counts |
| **3. Text association** | For each cluster, bind nearest institutional TEXT (brand name, tagline, domain) and project charter brand | `hash → brand text evidence` matrix |
| **4. Aspect ratio validation** | Drop outliers that fail logo-band plausibility **or** mark as **non-logo** decorative raster | Remaining logo candidates |
| **5. Repeated usage analysis** | Prefer cluster whose instances appear on **chartered pages** and **Header/Hero**; **down-rank** clusters confined to foreign sections or library-only frames | Confidence score (documentation only) |
| **6. Operator review** | If **>1 cluster** remains tied to plausible brand text, or charter brand ambiguous → **HITL** before L-07 APPROVED | Operator sign-off: `BRAND ASSET — APPROVED — node <id> hash <prefix>` |

**Gate:** **Brand Asset Detection Gate** — before logo wired to `src/img/`, favicon pipeline, or Header partial; before L-07 row marked complete.

**Reporting (minimum):**

```text
BRAND ASSET CANDIDATES — <n>
BRAND ASSET SELECTED — node <id> — hash <prefix> — confidence HIGH | LOW
BRAND ASSET GATE — PASS (APPROVED) | FAIL (COLLISION) | PENDING (OPERATOR)
```

---

## 8. Registry

| Token | Class name | Expected capture point | Failure cause token | Attribution |
|-------|------------|------------------------|---------------------|-------------|
| `ASSET_IDENTITY_COLLISION` | **ASSET IDENTITY COLLISION** | **Brand Asset Detection Gate** · Mapping L-07 · DQ-08 / PF-07 (if escaped) | **ASSET_IDENTITY_COLLISION** | **Brand Asset Detection Gate** · Mapping QA |

**Cross-reference:** [frontend-failure-attribution-model-v1.md](../frontend-failure-attribution-model-v1.md) §4 matrix · CASE G.

**Related failure classes (not duplicates):**

| Class | Focus |
|-------|-------|
| **GROUP AGGREGATION BEFORE DECOMPOSITION** | Composition grouping — not raster identity |
| **VISUAL INTERPRETATION WITHOUT LAYOUT SPEC** | Layout structure — not which logo file |
| **PRE-LAYOUT-SPEC STARTER RESIDUE** | Starter demo chrome — not FIG multi-brand |
| DQ-08 / PF-07 wrong asset | **Downstream** fidelity — may be symptom of this class |

---

## 9. Lessons Learned — FP-0002 Summary

| # | Lesson |
|---|--------|
| **1** | A single `.fig` file may contain **multiple real brand marks** from template reuse or prior work — not only the chartered client. |
| **2** | Generic node names (`image 219`) and similar dimensions **mask** identity collision; hash grouping is mandatory. |
| **3** | **First image in Header** selected **Skinerica** (`1:880`, `de219c6e…`); correct **Шпиговский дом** mark was **`1:6720`**, `262f79db…`. |
| **4** | Composition laws (Clean Shell, Group Decomposition, Layout Spec) **do not** prevent wrong-brand raster selection. |
| **5** | Forensic pass after build caught the defect — selection chain must run **before** asset wire. |
| **6** | Promoted as Factory failure class **ASSET_IDENTITY_COLLISION** — documentation only; no runtime or workflow change in FP-0002. |

---

## 10. Adoption

| Field | Value |
|-------|-------|
| **Factory-wide** | **Yes** — all projects using FIG / Figma / mixed design packs for brand marks |
| **Does not modify** | FP-0002 workspace artefacts, build scripts, gulp pipeline, Enforcement Pack gates |
| **Operator duty** | Run §7 chain when SOURCE-007 or FIG intake shows multi-candidate signals (§4) |
| **Promotion path** | Pointer integration in registries, Failure Attribution Model, mapping governance, Source Discovery, QA matrix — **not** a new governance wave |

---

## 11. Changelog

| Date | Change |
|------|--------|
| 2026-06-17 | v1 — Failure class **ASSET IDENTITY COLLISION** promoted from FP-0002 forensic incident; registry token `ASSET_IDENTITY_COLLISION`; Brand Asset Detection Layer; forbidden **FIRST IMAGE = LOGO** rule. |
