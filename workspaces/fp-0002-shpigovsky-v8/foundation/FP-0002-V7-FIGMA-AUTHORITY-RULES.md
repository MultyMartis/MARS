# FP-0002 V7 FIGMA AUTHORITY RULES

**Project:** FP-0002 Shpigovsky  
**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`  
**Package:** #001 Phase 1  
**Factory rules:** [`../../../projects/mars-website-factory/figma-inspection-authority-rules-v1.md`](../../../projects/mars-website-factory/figma-inspection-authority-rules-v1.md)

---

## Active design source

| Field | Value |
|-------|-------|
| File | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Spig_v1.2.fig` |
| Status | **ACTIVE** |
| SHA-256 | `BAE5D91C74B5A22AFC610F7C7845B9BADC6B87EC8DA85C5705ECF4EEC4DE3041` |

All new design reads, audits, asset exports, and content migration for V7 use **Spig_v1.2.fig** only.

---

## Historical design source

| Field | Value |
|-------|-------|
| File | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/Шпиговский.fig` |
| Status | **DO_NOT_USE_FOR_NEW_WORK** |
| SHA-256 | `D25A13617664040045A88AE9B804FEB737076007CB317D49699196F92232B64B` |

Historical file is retained for reference only. Do not delete. Do not implement from it unless operator explicitly re-authorizes.

---

## Visible content authority

**Rule:** If layer / component / instance / group **name** ≠ **visible rendered content**, authority = **visible content**.

**Priority:**

1. Visible text node value  
2. Visible instance override  
3. Visible asset or image fill  
4. Visible component state  
5. Layer name — navigation hint only  

**Conflict status:** `LAYER_NAME_CONTENT_CONFLICT`

| Layer name | Visible content | Selected authority | Reason |
| ---------- | --------------- | ------------------ | ------ |
| *(record per audit)* | *(record per audit)* | VISIBLE RENDERED TEXT | Name must not override canvas |

---

## Instance override priority

Rendered instance overrides beat:

- component master defaults;
- layer names;
- copy remembered from other frames.

Master-only text not visible in approved export is **not** active design.

---

## Layer-name conflicts

Layer names **must not**:

- auto-transfer to HTML;
- act as alternate copy variants;
- enter audit as separate content without visible proof;
- set `alt` without visible asset check.

---

## Hidden layer exclusion

Hidden, off, or non-visible layers are **not** part of the active layout.

**Status:** `EXCLUDED_BY_VISIBILITY`

Forbidden uses: HTML transfer, card counts, content map, dimension authority, mandatory state, WordPress/ACF without charter.

---

## Visibility inheritance

Treat as **non-visible** when any applies:

- `visible: false`
- hidden parent
- opacity `0`
- unselected component state in approved frame
- off-artboard draft not in approved list

---

## Permitted inspection of hidden layers

Reference-only for: hover candidate, expanded state, mobile alternate, designer draft, alternate asset, working scrap.

**Implement only if:** visible in another approved frame/state, tied to documented interaction, or operator explicitly authorizes.

Otherwise: **DO NOT IMPLEMENT**.

---

## Asset export rules

- Export only from **visible** nodes in **Spig_v1.2.fig** unless operator charter says otherwise.
- Favicon uses simplified **emblem mark** from approved branding (not full wordmark at 16×16).
- Do not export hidden-layer assets to `src/img` without charter.

---

## Text extraction rules

- Copy for HTML comes from **visible text** or approved operator copy charter.
- Phone/email conflicts: visible rendered strings win (see Factory example in `figma-inspection-authority-rules-v1.md`).

---

## Dev Mode measurement rules

- Measure visible frames only.
- Do not size visible blocks from hidden siblings.
- Record `LAYER_NAME_CONTENT_CONFLICT` when Dev Mode label ≠ canvas.

---

## Prohibited assumptions

- Layer name = SEO copy  
- Hidden layer = future mandatory block  
- Master label = instance output  
- Historical `.fig` = active authority  
- First image in file = logo (see `ASSET_IDENTITY_COLLISION`)

---

## Audit evidence requirements

Mandatory audit columns:

| Node | Visible | Layer name | Visible content | Included | Exclusion reason |
| ---- | ------: | ---------- | --------------- | -------: | ---------------- |

Checks required: `visible`, `locked`, `opacity`, `component state`, `instance overrides`, `parent visibility`.

Incomplete audit = **BLOCKED** for implementation sign-off.
