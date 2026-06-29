# FP-0002 PRIORITY VISUAL IMPLEMENTATION PROTOCOL

```
Status: ACTIVE TEMPORARY PRIORITY RULE
Scope: FP-0002 SHPIGOVSKY FRONTEND IMPLEMENTATION
Activation: OPERATOR APPROVED
Must read before: ANY FP-0002 FRONTEND TASK
Visual approval authority: OPERATOR ONLY
Commit before visual approval: PROHIBITED
Deactivation: ONLY BY EXPLICIT OPERATOR DECISION
```

**Protocol ID:** `FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL`
**Machine-readable:** [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.json](FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.json)
**Activated:** 2026-06-29
**Source commit:** `06096d51d41c0fee3639d94bb3b30855e08f79ad`

---

## Purpose

Temporary project-level frontend authority rule for FP-0002 «Шпиговский». Mandatory for all subsequent FP-0002 frontend tasks until the operator explicitly cancels or replaces it.

Protects the project from repeating these failure modes:

- one huge multi-phase prompt for an entire page;
- formal checklist closure instead of visual result;
- MARS/Cursor self-declaring visual PASS;
- commit before operator visual review;
- using Figma parse instead of actual PNG mockup;
- adding hidden Figma content absent from PNG;
- treating reuse as proof of visual match;
- checking only DOM/assets without crop-to-crop comparison;
- overwriting operator manual edits;
- moving to mobile before desktop approval;
- moving to the next block before current block approval.

---

## Authority hierarchy

| Rank | Layer |
|------|-------|
| 1 | Direct operator decision |
| 2 | Safety and destructive-operation rules |
| 3 | **FP-0002 PRIORITY VISUAL IMPLEMENTATION PROTOCOL** (this document) |
| 4 | Current manually approved operator-canonical source |
| 5 | Fresh approved design PNG (desktop/mobile) |
| 6 | Canonical `Spig_v1.2.fig` |
| 7 | Approved shared components |
| 8 | Page audits, charters, inventories, node maps |
| 9 | Historical source |

### Role clarifications

| Source | Role |
|--------|------|
| Operator decision | Highest priority |
| Fresh approved PNG | Visual/composition SSOT |
| Current operator-canonical source | Implementation authority |
| `Spig_v1.2.fig` | Technical design source |
| Audits and inventories | **Cannot** override visible PNG composition |
| Historical Figma `Шпиговский.fig` | **Not** authority |

### Conflict handling

If an existing audit or charter conflicts with this protocol: **use the protocol** and **record the conflict** — do not silently rewrite history.

---

## PNG vs Figma separation

### Fresh approved PNG

**Defines:**

- visible block order;
- presence and absence of blocks;
- element grouping;
- card and image counts;
- proportions;
- composition;
- rhythm;
- final visual picture;
- desktop/mobile presentation.

**PNG must NOT be used as:**

- frontend asset;
- section background;
- screenshot replacement for HTML;
- flattened implementation.

### Canonical `Spig_v1.2.fig`

**Used for:**

- exact text;
- original assets;
- node/frame identity;
- dimensions;
- component boundaries;
- crop/transform;
- visible/hidden state;
- desktop/mobile node correspondence;
- extraction of original resources.

**Rules:**

- Figma parse must not add runtime elements absent from fresh approved PNG.
- Hidden Figma content is not implemented if absent from PNG.
- Before page or block work, confirm exact PNG ↔ Figma frame match:
  - page identity;
  - desktop/mobile variant;
  - dimensions;
  - visible composition;
  - frame/node reference.

---

## Mandatory workflow

```
FRESH APPROVED PNG
→ EXACT MATCHING FIGMA FRAME
→ ONE DESIGN CROP
→ LOCAL BLOCK ANATOMY
→ COMPONENT BOUNDARY
→ REUSE DECISION
→ ONE BLOCK / ONE VIEWPORT IMPLEMENTATION
→ BUILD + DOM + ASSET TECHNICAL CHECK
→ ONE RUNTIME CROP
→ PNG-TO-RUNTIME CROP COMPARISON
→ HARD STOP WITHOUT COMMIT
→ OPERATOR VISUAL REVIEW
→ CORRECTION
→ OPERATOR APPROVAL
→ SELECTIVE CHECKPOINT
→ NEXT VIEWPORT OR NEXT BLOCK
```

### Unit of work

- one visual block;
- one viewport;
- one design crop;
- one runtime crop;
- one limited task.

**Desktop first.** Mobile starts only after explicit operator approval of desktop for that block.

After all approved blocks: separate page rhythm/integration pass.

---

## Reuse policy

Reuse is a **means**, not proof of quality.

Before reuse, determine:

- visual anatomy of the block;
- component boundary;
- exact structural similarity;
- parameters;
- difference between current component and design crop.

**Visual similarity ≠ component equivalence.**

**Prohibited:**

- starting from an existing partial and patching to PNG;
- assuming shared component fit from name alone;
- duplicating shared component without proven need;
- changing shared base for one page when page context or safe function-based modifier suffices.

Even with correct reuse, separately verify:

- placement;
- surrounding composition;
- dimensions;
- content count;
- image order;
- gaps;
- desktop/mobile behavior.

---

## Technical PASS vs Visual PASS

### MARS/Cursor may self-confirm

- build PASS;
- DOM PASS;
- duplicate IDs = 0;
- broken ARIA = 0;
- assets loaded;
- missing assets = 0;
- console errors = 0;
- horizontal overflow = 0;
- source scope compliance.

### MARS/Cursor may NOT self-confirm

- visual PASS;
- match with Figma;
- pixel parity;
- operator approval;
- readiness for final checkpoint on visual work.

**Allowed status before operator decision:** `IMPLEMENTED_PENDING_OPERATOR_VISUAL_REVIEW`

**Visual PASS:** operator only — after viewing actual runtime crop or page.

**Not proof of visual match:**

- `20/20 assets in DOM`;
- `7/7 groups present`;
- `correct include order`;
- `full-page screenshot captured`.

---

## Commit policy

For frontend visual implementation:

1. implementation without commit;
2. after build — preview;
3. MARS provides exact URL;
4. runtime crop of the block;
5. MARS stops;
6. **commit prohibited** until explicit operator visual approval.

After operator approval: separate selective checkpoint task.

Exceptions: direct operator decision only.

Documentation and safety tasks may have separate selective commits.

---

## Operator manual source authority

If the operator manually changed HTML/SCSS via watcher:

- current source becomes new canonical source-state;
- must not be overwritten;
- must not be reverted;
- must not be normalized;
- must not be auto-replaced with old audit/Figma values;
- must not format adjacent ranges;
- future tasks build on this state.

After manual pass:

- operator stops watcher;
- MARS runs build and technical QA;
- selective checkpoint only after operator permission.

---

## Prompt format

Each FP-0002 frontend Cursor prompt must be short and operational.

**Required parts:**

1. `ACTIVE STRATEGY`
2. one concrete goal;
3. visual authority PNG/crop;
4. technical Figma frame/node;
5. current operator-canonical source;
6. exact allowed files;
7. protected files;
8. visible acceptance points;
9. build + preview;
10. hard stop without commit.

**Do not use** huge multi-phase prompts combining audit, asset extraction, multiple blocks, desktop, mobile, visual QA, documentation, commit.

If multiple independent visual regions: split into multiple prompts.

---

## Mandatory report header

Every FP-0002 frontend MARS/Cursor report must start with this block:

```text
ACTIVE STRATEGY: FP-0002 PRIORITY VISUAL IMPLEMENTATION PROTOCOL

Visual authority:
- Approved PNG:
- Design crop:
- PNG status/hash:

Technical design source:
- Figma:
- Frame:
- Node/block:

Current unit of work:
- Page:
- Block:
- Viewport:

Current source authority:
- Operator-canonical source:
- Manual edits protected:

Commit policy:
- NO COMMIT BEFORE OPERATOR VISUAL APPROVAL

Operator visual approval:
- PENDING / APPROVED / REJECTED
```

**If header absent:**

- report is protocol-noncompliant;
- visual result cannot be auto-accepted;
- next implementation task cannot start until protocol context is restored.

---

## WEB-GPT RECOVERY NOTE

> **Recovery trigger:** If Web-GPT again creates a large multi-phase implementation prompt, combines multiple visual blocks, allows desktop and mobile of a complex block simultaneously, allows MARS to self-declare visual PASS, allows commit before operator review, starts from partial/reuse assumption instead of PNG, or forgets crop-by-crop comparison — **do not continue implementation automatically.**

**Required recovery action:**

1. Stop.
2. Request from MARS the main file: `FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md`.
3. Include its content in active context.
4. Only then form the next short micro-pass prompt.

This section exists specifically to restore Web-GPT context from MARS when the strategy is forgotten again.

**Recovery source:** this protocol file.

---

## O-Centre current status (2026-06-29)

| Field | Value |
|-------|-------|
| Page | O-Centre |
| Technical baseline | `06096d51d41c0fee3639d94bb3b30855e08f79ad` |
| Visual status | `STRUCTURAL_REGRESSION_REQUIRES_FIX` |
| Operator approval | `REJECTED` |
| Deployment | `BLOCKED` |
| Stable tag | `BLOCKED` |
| WordPress | `BLOCKED` |

**Next work mode:** micro-pass · desktop only · one narrow problem · no commit · preview + runtime crop · operator review required.

### DEC-01

- extracted asset may remain in repository;
- rendering/use is **not** approved;
- lifebuoy decoration is **prohibited**;
- next visual task must remove/disable it from rendering;
- Figma resource existence does not override PNG/operator authority.

---

## Registration

Entry points linking to this protocol:

- [FP-0002-V8-OPERATIONAL-STATUS.md](../../../fp-0002-shpigovsky-v8/foundation/FP-0002-V8-OPERATIONAL-STATUS.md)
- [FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md](FP-0002-OCENTRE-VISUAL-AUDIT-STATUS-v1.md)
- [PROJECT-STATUS.md](PROJECT-STATUS.md)
- [fp-0002-shpigovsky-v8/README.md](../../../fp-0002-shpigovsky-v8/README.md)
- [execution-cases-registry-v1.md](../../../projects/mars-website-factory/execution-cases-registry-v1.md) (FP-0002 factory project lane)

---

*FP-0002 Priority Visual Implementation Protocol — active temporary priority rule. Deactivation: operator only.*
