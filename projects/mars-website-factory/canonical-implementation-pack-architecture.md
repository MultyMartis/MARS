# MARS Website Factory — Canonical Design Implementation Pack (architecture)

**Status:** **documented** — recommended **folder layout and artifact semantics** for **governance**. **Not** a runtime module, **not** a schema-enforced API in MARS v0.

**Purpose:** Define how **approved design** for a specific **version** is expressed as **implementation-safe, machine-readable law** (Markdown-first) for frontend production agents and human operators.

**See also:** [design-governance-layer.md](design-governance-layer.md), [Design Governance Agent](../../agents/design-governance-agent.md).

---

## 1. Canonical folder structure (recommended)

```text
projects/<project>/design/
├── README.md                 # Active version pointer, freeze status, operator notes
├── shared-assets/            # Cross-version physical assets ONLY (see §6)
│   ├── brand/
│   ├── fonts/
│   └── …
├── v1/                       # Archive (when v2+ is active) — read-only for implementation
│   ├── screens/
│   ├── semantics/
│   ├── implementation-pack/
│   ├── exports/
│   └── validation/
└── v2/                       # Example active version
    ├── screens/              # Screen-level intent (not necessarily “all pixels”)
    ├── semantics/            # LOCKED / FLEXIBLE meaning, order, entities, CTAs
    ├── implementation-pack/  # Typography, spacing, responsive, components, assets, constraints
    ├── exports/              # PNG/SVG/PDF — evidence, not sole authority
    └── validation/         # QA, freeze, drift logs
```

### 1.1 What each subtree means

| Subtree | Role | Canonical for implementation? |
|---------|------|--------------------------------|
| **`semantics/`** | **Meaning**: sections, entities, CTAs, order, forbidden rewrites — what must not drift. | **Yes** (for this `vN`). |
| **`implementation-pack/`** | **How to build faithfully**: scales, spacing, breakpoints, component rules, asset usage. | **Yes** (for this `vN`). |
| **`exports/`** | **Visual proof** and Designer/Figma-derived references. Supports QA; **does not replace** semantics. | **Supporting** — canonical **structure** is in `semantics/` + `implementation-pack/`. |
| **`validation/`** | **Human QA contracts**: checklists, observations, freeze records. | **Yes** for **process** and **freeze state** labeling. |
| **`screens/`** | Page/screen-level maps, optional low-fidelity notes, links to exports. | **Yes** where used as signed-off intent; defer to `semantics/` on conflict resolution rules. |
| **`shared-assets/`** | Shared **files** only. | **No** for semantics (see §6). |

### 1.2 What is canonical vs archive

- **Canonical** = the **active `vN`** (recorded in `design/README.md` and frontend handoff `SAFE_UNKNOWN_notes` / freeze metadata) plus **`shared-assets/`** file paths referenced by that version.
- **Archive** = non-active **`v*`** directories — **must not** drive new implementation unless governance **re-opens** version (bump, HITL, new freeze).
- **Blending forbidden:** Do not merge **`semantics/`** or **`implementation-pack/`** across versions into a single “Frankenstein” authority.

---

## 2. Semantic layer (`semantics/`)

**Defines what the site *means* structurally** for implementation: section identity, content model, CTA roles, and locks. Visuals illustrate; semantics **bind**.

### 2.1 Recommended artifacts

| Artifact | Purpose |
|----------|---------|
| **`section-map.md`** | Map each **screen** → **sections** → **`block_id`** (aligned with [block-registry-v0.md](block-registry-v0.md)). Optional instance ids for repeated blocks. |
| **`section-order.md`** | Linear **semantic order** (and responsive **collapsing rules** if order changes by breakpoint — if so, explicit). |
| **`semantic-locks.md`** | Table of **LOCKED** vs **FLEXIBLE** items (copy tone, imagery choice, decorative elements). |
| **`content-authority.md`** | **Authoritative strings** or **refs** (CMS doc, legal-approved file, spreadsheet id). **No invention** beyond listed sources. |
| **`screen-role-map.md`** | Each URL/template: **purpose**, primary CTA, secondary actions, **forbidden** emphasis (e.g. no discount language). |
| **`entity-count-lock.md`** (or section in `semantic-locks.md`) | Counts/min/max for repeatable entities (testimonials, logos, FAQ items, plan cards). |

### 2.2 LOCKED vs FLEXIBLE

| Class | Meaning | Frontend expectation |
|-------|---------|----------------------|
| **LOCKED** | Changing would alter **commercial, legal, UX, or conversion meaning** or **approved entity counts**. | **No** silent rewrites; needs HITL + version bump. |
| **FLEXIBLE** | Styling/substance allowed within **implementation-pack** bounds (e.g. icon choice from approved set). | May vary **only** as allowed in `semantic-locks.md`. |

### 2.3 Forbidden semantic rewrites (normative intent)

Implementation **must not**, unless `semantic-locks.md` explicitly allows:

- Rename sections in user-visible headings such that **blueprint SEO or promise** changes.
- Merge/split **LOCKED** sections in a way that changes **reading order** vs `section-order.md`.
- Change **CTA labels or targets** away from `content-authority.md` / blueprint **without** HITL.
- Add **new** claims, guarantees, numbers, or **entities** not in authority docs.
- **Remove** trust/legally required disclosures present in authority.

### 2.4 Entity-count locks

- Declare **exact**, **min**, **max**, or **enumerated list** for repeatable content.
- **Mutation** (e.g. “3 plans” → “4 plans”) = **structure change** → quarantine implementation, update blueprint/pack, HITL.

### 2.5 CTA meaning locks

- For each primary/secondary CTA: **intent** (submit, call, navigate), **copy source**, **destination**, **tracking** hints if any.
- **Meaning lock** forbids repurposing a button (e.g. “Get quote” → “Read blog”) without explicit approval.

### 2.6 Semantic QA expectations

- Semantic QA is **document review + spot check** against exports: headings, counts, CTA roles, hero promise, FAQ presence.
- Artifacts consumed by QA: **`semantic-qa.md`** (see §4), `section-order.md`, `content-authority.md`.

---

## 3. Implementation pack layer (`implementation-pack/`)

**Defines how to implement** without inventing design system gaps: measurable rules frontend agents can follow.

### 3.1 Recommended artifacts

| Artifact | Purpose |
|----------|---------|
| **`typography-rules.md`** | Roles → type styles; allowed weights; heading **level** ↔ **visual size** mapping; **no fake headings** for styling. |
| **`spacing-system.md`** | Scale, section padding rules, grid/gutter intent, vertical rhythm exceptions. |
| **`responsive-rules.md`** | Breakpoints, **mobile-first** discipline, reflow vs reorder (must match `section-order.md` semantics). |
| **`component-rules.md`** | Blocks/components: states, anatomy, **forbidden DOM patterns**, variants allowed. |
| **`asset-rules.md`** | Raster/SVG usage, `srcset`, lazy rules, license notes; mapping to **`exports/`** and **`shared-assets/`**. |
| **`implementation-constraints.md`** | **Forbidden** patterns (e.g. global `!important` waves, unscoped resets), perf budget hints, third-party constraints. |
| **`frontend-charter.md`** | Short **stack-specific** binding: e.g. Gulp partials + SCSS modules, **`data-*`** hooks — aligned with [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md). |

### 3.2 Implementation-safe rules

Rules should be **testable by inspection**: “max 2 type scales per section”, “breakpoint X: stack order A→B”, “hero min-height not fixed in px on mobile”, etc. Avoid subjective-only language without a measurable proxy.

### 3.3 Responsive discipline

- **Visual** reflow must preserve **semantic** order unless `section-order.md` documents intentional breakpoint-specific order (rare; if present, **LOCKED**).
- **Forbidden:** Using flex/grid `order` to **hide** content that remains in DOM for screen readers unless explicitly designed and signed off (**accessibility** review).

### 3.4 Forbidden implementation patterns (examples; project extends)

Document in **`implementation-constraints.md`**:

- Inventing **new** sections/components for “design balance.”
- **Placeholder** media or copy not listed in **`content-authority.md`** passing as final.
- Hard-coded **magic numbers** without tie to spacing/typography scale.
- Editing **`dist/`** or bypassing agreed **src-first** workflow ([frontend-production-rules-v0.md](frontend-production-rules-v0.md)).

### 3.5 Stack-specific rules

- **`frontend-charter.md`** names the **actual** toolchain (static Gulp, Vite, etc.) — **must match** `target_stack` in Frontend Handoff; if mismatch → **SAFE UNKNOWN**, fix handoff or charter.

---

## 4. Validation layer (`validation/`)

**Process and evidence** that the pack + exports + handoff cohere **before freeze** and **during** implementation.

### 4.1 Recommended artifacts

| Artifact | Purpose |
|----------|---------|
| **`semantic-qa.md`** | Checklist: entity counts, H1 policy, CTA roles, trust blocks, **forbidden rewrites** scan. |
| **`responsive-qa.md`** | Viewport spot matrix, overflow checks, tap targets, **order** vs semantics. |
| **`freeze-checklist.md`** | **Pre-freeze** gates: required files present, version id, sign-off fields, **quarantine** flags cleared. |
| **`drift-observations.md`** | Log of **near-misses** during implementation (for humans; not runtime telemetry). |

### 4.2 Pre-freeze validation

Before marking design **frozen** for build:

1. **`semantics/`** complete for all in-scope screens; **LOCKED** table reviewed.
2. **`implementation-pack/`** consistent with [Design Handoff Contract v0](design-handoff-contract-v0.md) / design system registry when present.
3. **`exports/`** correspond to **active** `vN` (no stray **archive** paths).
4. **`freeze-checklist.md`** signed by role(s) project defines (Design, Content, Tech).

### 4.3 Semantic & responsive QA

- **Semantic QA** validates **meaning** and **counts**; **Responsive QA** validates **layout** against rules without breaking semantic order.
- **Russian commercial landings:** typography/overflow QA — [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md); viewport preset — [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md).

### 4.4 Quarantine rules

Implementation output is **quarantined** (non-canonical / not merge-ready) when:

- Active **`vN`** is ambiguous or **two** versions’ semantics are mixed in one handoff.
- **LOCKED** items fail checklist but ship is attempted “for speed.”
- **Archive** exports or old Figma links are used without explicit re-baseline.

### 4.5 Implementation survivability checks

Lightweight **human** checks that the pack will **survive** real build:

- Can every **`block_id`** map to a partial and SCSS entry?
- Are **all** assets reachable from documented paths?
- Are **content** sources still valid URLs / files (no 404 authority)?

---

## 5. Version isolation

| Topic | Rule |
|-------|------|
| **Active version** | Single **`vN`** referenced in project `design/README.md` + [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md) notes. |
| **Archive versions** | Read-only; **not** inputs to new work. |
| **Semantic isolation** | Each version has **own** `semantics/` + `implementation-pack/`. Do not symlink-merge across versions. |
| **Exports** | Version-scoped under **`exports/`** for that `vN`. |
| **Bump** | New `vN+1` = **copy forward** + intentional diff; archive previous; **freeze** anew. |

**Forbidden source blending:** Using **`v1` semantics** with **`v2` exports**, or **`shared-assets`** copy to imply **section order**, is **disallowed** unless a single signed document lists the **explicit** exception (temporary — should be corrected in pack).

---

## 6. `shared-assets/` behavior

| Rule | Detail |
|------|--------|
| **Purpose** | Deduplicate **binary** originals (logos, font files, shared icons). |
| **Not semantics** | **Does not** define section order, copy, counts, or CTA meaning — only **files** semantics **may reference** by path. |
| **Version references** | Each `vN` **`asset-rules.md`** should list which shared files are **in boundary** for that release. |

**Identity:** `shared-assets/` **≠** `semantics/`. Semantic truth remains versioned under **`design/vN/semantics/`**.

---

## 7. Frontend implementation contracts

**Canonical Design Implementation Pack** does **not** replace [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md); it **constrains** how that handoff is filled.

| Frontend handoff field | Typical pack source |
|------------------------|---------------------|
| **`section_map`**, **`partials_mapping`** | `section-map.md`, `section-order.md`, block registry |
| **`responsive_rules`** | `responsive-rules.md` + semantic order |
| **`asset_requirements`** | `asset-rules.md`, `exports/`, `shared-assets/` |
| **`forbidden_patterns`** | `implementation-constraints.md`, `semantic-locks.md` |
| **`SAFE_UNKNOWN_notes`** | Pointer to **`design/vN`**, freeze id, known gaps |

If handoff and pack **conflict** → **stop**; resolve via HITL; **do not** silently prefer visuals over **LOCKED** semantics.

---

## 8. Design Governance Agent (pointer)

**Authoring** and **refresh** of the pack under human supervision: [Design Governance Agent](../../agents/design-governance-agent.md). **Not** runtime; **not** auto-sync with Figma.

---

## 9. SAFE UNKNOWN (pack-level)

- Exact **minimum** file set for a “valid” pack — **project-defined**; v0 recommends **starting** from §2–4 tables.
- Automated **lint** of packs — **not** claimed by MARS core.
- JSON/YAML **parallel** export of locks — **optional future**.

---

## 10. Changelog (documentation)

| Version | Date | Notes |
|---------|------|--------|
| v0 | 2026-05-16 | Initial Canonical Design Implementation Pack architecture. |
