# Triumph Manipulator Landing — V2 Frontend Source of Truth

## 1. Purpose

This document is the **frontend source-of-truth stabilization layer** for **Triumph Manipulator Landing V2** production. It exists to reduce semantic and path drift between design artifacts, written rules, and implementation. It does **not** replace canonical assets; it classifies them and states how they must be used.

**Scope:** documentation discipline and classification only. This file is not an implementation specification by itself; it points to canonical sources and forbids unsafe mixing of V1/V2 material.

---

## 2. Canonical V2 sources

The following paths and artifacts are **CANONICAL** for V2 frontend truth:

| Classification | Path or artifact |
|----------------|------------------|
| **CANONICAL** | `projects/triumph-manipulator-landing/design/v2/` — current V2 **visual** mockups (`01.png` … `07.png`, `full.png`) |
| **RETIRED (do not use)** | `projects/triumph-manipulator-landing/design/TRIUMPH LANDING V2 — DESIGN & FRONTEND RULES.pdf` — **removed** (2026-05-16); it is **not** authoritative. A replacement export may be generated later from the MD source-of-truth stack; see [V2-CLEANUP-DECISION-LOG.md](./V2-CLEANUP-DECISION-LOG.md). |
| **CANONICAL (written rules / process)** | This file, [V2-SECTION-SOURCE-MATRIX.md](./V2-SECTION-SOURCE-MATRIX.md), [V2-VISUAL-SOURCE-MATRIX.md](./V2-VISUAL-SOURCE-MATRIX.md), [docs/TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md](./docs/TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md) |
| **CANONICAL** | `projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md` — design system reference |
| **CANONICAL (implementation tree)** | `workspaces/triumph-manipulator-landing-v2/src/` — active V2 implementation source (this tree is truth for *what is built*; conflicts with MD / PNG mocks must be reported before edits per Section 6) |

---

## 3. Archive / reference-only sources

The following are **ARCHIVE** or **REFERENCE-ONLY**. They must not be treated as current V2 homepage or section truth:

| Classification | Path or artifact |
|----------------|------------------|
| **ARCHIVE / REFERENCE-ONLY / FORBIDDEN FOR V2 IMPLEMENTATION** | `projects/triumph-manipulator-landing/design/v1/` — archived V1 mockup PNG exports (historical strip-era visuals); **do not** use as implementation or copy truth for V2 unless explicitly re-approved in writing |
| **REFERENCE-ONLY** | [`design/mockups-index.md`](./design/mockups-index.md) and similar indexes — when they describe **V1** slices under `design/v1/`, they are **not** V2 truth |
| **REFERENCE-ONLY** | Old **frontend-section-map** (or equivalent) — when they describe **landing-strip V1**, they are not V2 homepage order truth |
| **ARCHIVE / REFERENCE-ONLY** | `workspaces/triumph-manipulator-landing/` — V1 Gulp implementation; **preserved**; not the V2 implementation source of truth |

**Note:** V1 raster slices and continuity docs live under `design/v1/`. Older docs may still say `design/mockups/` — that path is **deprecated** in favour of `design/v1/`; see [`design/README.md`](./design/README.md).

---

## 4. Design version isolation

Normative rules to prevent **semantic contamination** between design generations and between visuals vs structure:

| Rule | Statement |
|------|-----------|
| Active version | Every frontend implementation MUST declare the **active design generation** it follows. For current Triumph V2 work, canonical visuals are **`projects/triumph-manipulator-landing/design/v2/`** only. |
| Single canonical source | Only **one** version folder may be the **canonical implementation source** for that generation at a time (for V2: **`design/v2/`**). Archive folders do not alternate as concurrent canon. |
| Archive semantics | **`design/v1/`** (and any other archived generation folder) MUST NOT define section semantics, DOM order, homepage IA, or copy for **V2** implementation. |
| Shared assets | **`design/shared-assets/`** holds reusable visuals (logos, icons, shared backgrounds). It MUST NOT be treated as authority for **landing structure**, section order, or textual content. |
| Visual ≠ semantic | **Visual references** (paths to PNGs, SVGs, or composites) do **not** substitute for **semantic references**. Inferring section intent, headlines, or meaning from archive assets or `shared-assets` alone is **forbidden** — resolve meaning only via **`design/v2/`** (for V2) plus the written rule stack in §2. |

Folder roles are summarized in [`design/README.md`](./design/README.md).

---

## NEXT IMPLEMENTATION RULE

The **next** frontend implementation cycle must **start from** `projects/triumph-manipulator-landing/design/v2/01.png` and proceed **in file order** through `02.png` … `07.png` (use `full.png` only as a **composite check**, not as a substitute for per-screen work). Work **screen by screen**; do not skip ahead or merge multiple screens into one delivery step.

| Constraint | Rule |
|------------|------|
| DOM / include order | **Do not** continue from **existing DOM assumptions** — current `index.html` and partial wiring are **provisional** until each screen is re-validated against the corresponding `design/v2/*.png`. |
| V1 archive | **Do not** use `design/v1/` as **semantic** source for V2 (archive / reference-only; see §3). |
| `equipment-prices` | **Not** on **`index.html`**. Allowed **only** on **`validation-equipment-prices.html`** (quarantine). **Do not** re-add to homepage without a **new** operator gate ([V2-CLEANUP-DECISION-LOG.md](./V2-CLEANUP-DECISION-LOG.md), [equipment-prices-quarantine.md](./design/v2/validation/equipment-prices-quarantine.md)). |
| Copy | **Do not** invent marketing copy. Text comes only from **locked** copy visible on approved `design/v2/` screens or **explicit operator instruction**. |
| Section meaning | **Do not** change section meaning without **operator approval**. |

### Per-screen validation cycle (mandatory order)

For **each** `design/v2/NN.png` in sequence:

1. **Select** that single screen as the active scope.
2. **Extract** section meaning and **locked text** (headings, CTAs, lists — only what the PNG authorizes).
3. **Confirm** matching partial(s) / SCSS module(s) in `workspaces/triumph-manipulator-landing-v2/src/`, or **mark missing** and plan minimal add — **no** inventing structure from V1 or from legacy DOM.
4. **Implement only** the markup/styles for **that** screen’s scope (one screen per implementation cycle step).
5. Run **semantic QA** — meaning and copy match the PNG; no drift, no “improved” paraphrase.
6. Run **responsive QA** — layout behavior matches rules / design system for the project breakpoints.
7. **Freeze** the section (operator or docs mark it aligned/frozen) **before** opening the next `NN.png**.

Treat **`equipment-prices`** as **non-canonical for the homepage** — it is **validation-only** on `validation-equipment-prices.html` (baseline from 2026-05-16).

---

## 5. Forbidden use rules for V2 implementation

For **V2** work, the following are **explicitly forbidden**:

1. **Copying V1 section content** into V2 (text, headings, or section intent from V1).
2. **Using V1 archive material** (`design/v1/`), **`design/mockups/`** (deprecated path — treat as stale alias for `design/v1/`), or any other **non‑`design/v2/`** mockup tree as **current V2 visual or copy truth**.
3. **Using old frontend maps** as **homepage section order truth** when those maps describe V1 / landing-strip V1.
4. **Inventing new marketing copy** not present in approved V2 mockups and not given by explicit operator instruction.
5. **Changing section meaning** without **operator approval** (including reframing a section’s topic or audience).
6. **Converting a one-machine section into a fleet or multiple-machines section** — where **`design/v2/`** prescribes a **one-machine** story (e.g. `02.png`, `06.png`), do not replace it with a **fleet** or multi-card park narrative. **Do not** treat «третий экран» as synonymous with «третий `<main>` include» without checking **date of docs** — homepage wiring was aligned **2026-05-16** (third `<main>` = cases). **PNG order** (`01.png` … `07.png`) remains the implementation sequence for the rebuild cycle.
7. **Replacing approved headings** with AI-generated variants (paraphrase, “improvement,” or alternate tone).

---

## 6. Semantic source rules

| Rule | Statement |
|------|-----------|
| Visual structure | Comes from **`design/v2/`** PNG exports. |
| Text content | Comes from **approved V2** `design/v2/` copy (as visible in PNGs) or **explicit operator instruction** only. |
| Missing content | Implementation **must not infer** missing headlines, body copy, CTAs, or lists. |
| Unknown | Any required content not present in canonical sources must be marked **SAFE UNKNOWN** and escalated; do not fabricate. |
| Rules export vs PNG | If a **future** canonical rules PDF (if issued) and **`design/v2/`** PNGs conflict on structure or copy, **stop** and **report**; do not pick one silently. |
| MD rules vs `src/` | If **markdown rules** and **live code** under `workspaces/triumph-manipulator-landing-v2/src/` conflict, **report the conflict before editing** implementation. |

---

## 7. Current known conflicts (from audit)

These are **known drift / staleness** items; resolution is **out of scope** for this document (stabilization only):

- **Old docs** may still reference **`design/mockups/`** (deprecated; use **`design/v1/`**) or a **V1 section map**; actual V2 layout may differ. Canonical folder semantics: [`design/README.md`](./design/README.md).
- **Actual V2 index** (`index` / section order in implementation) may differ from **older freeze** or status documents.
- **Legacy residue:** old partials, SCSS, or structural fragments may remain in the V2 workspace without being current truth.
- **Handoff / QA status** documents may be **stale** relative to `src/` or `design/v2/`.
- **Font Awesome Pro** in-repo is a **local licensed asset**; it is **not** a cleanup or deletion target without operator direction.

---

## 8. Stabilization model (classifications)

Use these labels consistently when discussing V2 frontend sources:

| Label | Meaning |
|-------|---------|
| **CANONICAL** | Authoritative for V2 design, copy, or rules as stated in Section 2. |
| **ACTIVE** | Current V2 implementation under `workspaces/triumph-manipulator-landing-v2/` (especially `src/`); must align with canonical sources or conflicts must be reported. |
| **FROZEN** | Explicitly frozen by operator/docs; treat as immutable unless operator unfreezes. |
| **ARCHIVE** | Historical (e.g. V1 workspace, V1 mockups); preserved; not V2 truth. |
| **REFERENCE-ONLY** | May inform context but must not drive V2 section order, copy, or meaning alone. |
| **FORBIDDEN FOR V2** | Actions listed in Section 5; also using ARCHIVE/REFERENCE-ONLY material as if CANONICAL for V2. |

---

## 9. Operator protection notes

- **V1 workspace** (`workspaces/triumph-manipulator-landing/`) is **preserved** and must **not** be damaged, repurposed for V2 truth, or conflated with V2 sources.
- **Protected working projects** (do not treat as cleanup targets without explicit scope):  
  `projects/mars-website-factory/`, `projects/metabot-seo-content-agent/`, `projects/seo-content-agent/`, `mars-runtime/`, `shared/assets/icon-libraries/`, and the V1 workspace above.
- **Destructive cleanup** (deletes, mass renames, removal of licensed assets, or bulk edits across protected trees) requires **explicit operator approval**.

---

## 10. Next cleanup recommendations (non-destructive only)

Recommended follow-ups that **do not** require deleting, moving, or rewriting implementation files as part of *this* stabilization:

1. **Execute the per-screen cycle** — [NEXT IMPLEMENTATION RULE](#next-implementation-rule): `01.png` → `07.png`, freeze each section after semantic + responsive QA.
2. **`equipment-prices` baseline** — **removed from homepage**; validation page only (2026-05-16). A **future** rewrite or homepage return requires **new** written approval.
3. **Classify legacy partials/SCSS** — document what is active vs residue; no bulk removal without approval.
4. **Align `index.html` with `design/v2` order** — only **after** each screen is validated in the cycle above (not by assuming current DOM order).
5. **`design/v2` index** — optional curated index of mockup files and roles (filename → section purpose).

---

## Document control

- **Created for:** V2 frontend source discipline stabilization.  
- **Does not supersede** `design/v2/` pixel mocks; it **binds process** to those sources and to the written rule stack (§2).  
- **Conflicts:** prefer reporting over silent fixes — see Section 6.
