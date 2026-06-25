# Figma inspection checklist — MARS Forge (overlay v0)

**Status:** **overlay checklist** for human-supervised Figma inspection QA.  
**Not:** Figma plugin, automated parser, or substitute for Mapping QA or Production PASS.

**Factory methodology:** [`../../projects/mars-website-factory/figma-inspection-authority-rules-v1.md`](../../projects/mars-website-factory/figma-inspection-authority-rules-v1.md).  
**Mapping governance:** [`../../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md`](../../projects/mars-website-factory/design-source-to-frontend-mapping-governance-v1.md).  
**Source interpretation:** [`../../agents/mars-forge/source-interpretation-checklist.md`](source-interpretation-checklist.md).

---

## 1. When to run

- before HTML/CSS transfer from Figma or Dev Mode;
- when FP-0002 or any Factory project registers a new active `.fig` authority;
- alongside source interpretation and visual reconciliation when Figma drives copy or asset selection.

---

## 2. Active file authority

- [ ] **Active design file named** — path, version label, SHA-256 when available.
- [ ] **Historical files disabled** — older `.fig` marked `DO_NOT_USE_FOR_NEW_WORK` and not cited as authority.
- [ ] **Approved frame list named** — desktop/mobile/state frames in scope.

---

## 3. FIGMA-VISIBLE-CONTENT-AUTHORITY

- [ ] **Rendered text recorded** — not layer name alone.
- [ ] **Instance overrides checked** — override beats master and name.
- [ ] **Layer name navigation only** — names not copied to HTML without visible confirmation.
- [ ] **LAYER_NAME_CONTENT_CONFLICT table** — filled when name ≠ visible content.
- [ ] **Alt text** — from visible asset / operator confirmation, not from layer name default.

---

## 4. FIGMA-HIDDEN-LAYER-EXCLUSION

- [ ] **Visibility column present** in audit table.
- [ ] **Parent visibility** checked — hidden parent excludes children.
- [ ] **Opacity 0** treated as non-visible unless approved elsewhere.
- [ ] **EXCLUDED_BY_VISIBILITY** recorded for hidden nodes.
- [ ] **Card/entity counts** use visible nodes only.
- [ ] **Hidden-only assets** not exported to frontend without charter.

---

## 5. Audit completeness

Per material node:

| Node | Visible | Layer name | Visible content | Included | Exclusion reason |
| ---- | ------: | ---------- | --------------- | -------: | ---------------- |

- [ ] `visible` checked
- [ ] `locked` noted
- [ ] `opacity` noted
- [ ] `component state` noted
- [ ] `instance overrides` noted
- [ ] `parent visibility` noted

Audit without these checks is **INCOMPLETE**.

---

## 6. Escalation

| Finding | Action |
|---------|--------|
| Hidden layer required for layout | Operator charter or approved alternate frame |
| Name/content conflict unresolved | HITL — do not implement from name |
| Historical `.fig` cited as authority | **STOP** — wrong source |

---

*Overlay checklist only. Not runtime enforcement.*
