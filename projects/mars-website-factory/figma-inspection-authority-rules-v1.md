# MARS Website Factory — Figma Inspection Authority Rules v1

**Status:** **documented** — canonical human-operated Figma read discipline for Website Factory frontend work.  
**Not:** Figma plugin, automated layer parser, runtime enforcement, or computer-vision extraction product.

**Purpose:** Fix authoritative rules for **visible content**, **instance overrides**, **layer-name conflicts**, and **hidden-layer exclusion** when Figma is an approved design source.

**Authority order:** [frontend-production-authority-order-v1.md](frontend-production-authority-order-v1.md) — rank 3 Factory governance detail; rank 1 Project Production Standards and rank 2 Operator Laws win on conflict.

**Registry:** [registries.md §6](registries.md#6-frontend-production-rules).

**Peer integration (not duplication):**

| Document | Role |
|----------|------|
| [design-source-to-frontend-mapping-governance-v1.md](design-source-to-frontend-mapping-governance-v1.md) | Extraction chain; §12 Figma inspection cross-ref |
| [source-interpretation-governance.md](source-interpretation-governance.md) | Observed / Inferred / Assumed / Unknown read discipline |
| [pixel-fidelity-audit-rules-v1.md](pixel-fidelity-audit-rules-v1.md) | PF-* numeric fidelity after authority is fixed |
| [frontend-design-qa-matrix-v1.md](frontend-design-qa-matrix-v1.md) | DQ gate vocabulary |

**Forge checklist:** [`../../agents/mars-forge/figma-inspection-checklist.md`](../../agents/mars-forge/figma-inspection-checklist.md).

---

## Rule tokens

| Token | Summary |
|-------|---------|
| **FIGMA-VISIBLE-CONTENT-AUTHORITY** | Visible rendered content wins over layer / component / group names |
| **FIGMA-INSTANCE-OVERRIDE-PRIORITY** | Instance text and property overrides outrank master defaults and names |
| **FIGMA-LAYER-NAME-CONFLICT** | Mandatory conflict status when name ≠ visible content |
| **FIGMA-HIDDEN-LAYER-EXCLUSION** | Hidden, off, or non-visible layers are excluded from active design |

---

## FIGMA-VISIBLE-CONTENT-AUTHORITY

When a layer, component, instance, or group **name** does not match **factually visible content**, the source of truth is **visible content**, not the name.

**Priority order:**

1. Visible value of text node (rendered string).
2. Visible instance override (text, boolean, swap, exposed nested override).
3. Visible asset or image fill on the rendered frame.
4. Visible component state (selected variant / property set as rendered).
5. Layer name — **navigation hint only**; never automatic HTML authority.

**Layer names must not be used to:**

- transfer copy into HTML automatically;
- treat name as alternate copy variant;
- add name-only strings to audit as separate content;
- override visible instance text;
- set `alt` without visible asset / operator confirmation.

**Conflict status:** `LAYER_NAME_CONTENT_CONFLICT` — record:

| Layer name | Visible content | Selected authority | Reason |
| ---------- | --------------- | ------------------ | ------ |

**Example (FP-0002 class):**

```text
Layer name:           8 (800) 777-02-05
Visible rendered text: 8 (925) 183-64-64 / 8 (995) 023-92-26
Implementation authority: VISIBLE RENDERED TEXT
```

---

## FIGMA-INSTANCE-OVERRIDE-PRIORITY

For component instances:

- **Rendered override** beats component master default.
- **Rendered override** beats layer name.
- **Rendered override** beats historical copy from another frame.
- Master-only text visible only when instance is selected in editor but **not** in exported/rendered output is **not** active design.

Audit must note `instanceOverrides` when present.

---

## FIGMA-HIDDEN-LAYER-EXCLUSION

Hidden, disabled, or non-visible layers **do not** belong to the active design layout.

**Excluded elements must not:**

- be counted in section composition;
- be counted in card totals;
- be transferred to HTML;
- be exported as frontend assets (unless separate approved export charter);
- enter the primary content map;
- define dimensions of a visible sibling block;
- be declared mandatory UI state;
- enter WordPress / ACF models without explicit charter.

**Status:** `EXCLUDED_BY_VISIBILITY`

**Visibility inheritance — treat as non-visible when any applies:**

- layer `visible: false`;
- parent hidden;
- opacity `0`;
- locked-only reference frames not in approved export set;
- component state not selected in the approved frame;
- off-canvas draft not in approved artboard list.

**Permitted read of hidden layers (reference only):**

- possible hover;
- possible expanded state;
- mobile alternate;
- designer draft;
- alternate asset candidate;
- working scrap.

**Implementation of hidden-only content allowed only if:**

1. Element is visible in another **approved** frame/state, or
2. Element is explicitly tied to documented interactive state, or
3. Operator separately authorizes implementation.

Otherwise: **DO NOT IMPLEMENT**.

---

## FIGMA visibility audit contract

Figma audits are **incomplete** unless these fields exist per material node:

| Node | Visible | Layer name | Visible content | Included | Exclusion reason |
| ---- | ------: | ---------- | --------------- | -------: | ---------------- |

**Mandatory checks:** `visible`, `locked`, `opacity`, `component state`, `instance overrides`, `parent visibility`.

---

## Agent / operator behavior

| Situation | Response |
|-----------|----------|
| Name says phone A, canvas shows phone B | `LAYER_NAME_CONTENT_CONFLICT`; implement B |
| Hidden card in frame | `EXCLUDED_BY_VISIBILITY`; do not HTML |
| Opacity 0 text still in layer list | Exclude unless approved state elsewhere |
| Master label vs instance override | Instance override wins |
| Name used as SEO copy without visible check | **STOP** — violates visible-content authority |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-24 | v1 — FP-0002 Package #001 Phase 1: visible content, overrides, layer-name conflict, hidden-layer exclusion, audit contract |
