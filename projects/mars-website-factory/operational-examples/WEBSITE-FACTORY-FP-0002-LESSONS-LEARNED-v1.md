# Website Factory — FP-0002 Lessons Learned v1

**Date:** 2026-07-01  
**Source case:** FP-0002 Shpigovsky — V8 operator-approved baseline  
**Location:** `projects/mars-website-factory/operational-examples/`  
**Status:** Case-derived **frontend** lessons (V8). **WordPress production operating knowledge (2026-08-18)** lives in [WP Forge knowledge hub](../subsystems/forge-wordpress/knowledge/README.md) — use that for the next WordPress site. This file is **not** the production SOP.

**Not:** Mandatory global law until promoted. **Not:** Proof of automated Factory runtime.

---

## 1. Authority hierarchy

**Canonical hierarchy (reusable):**

1. Explicit operator decision  
2. Approved visual reference PNG  
3. Current approved source implementation  
4. Figma details and geometry  
5. Approved shared components  
6. Audits and historical documents  

**Lessons:**

- Figma does **not** override explicit operator-approved implementation.  
- Historical documentation does **not** override current approved source.  
- Automated visual checks are **evidence**, not final authority.  
- Missing authority must trigger **STOP** — not generic invention.

**FP-0002 evidence:** Priority Visual Implementation Protocol; V8 baseline closure after operator approval despite prior audit conflicts.

---

## 2. Visual implementation passes

**Successful pass model:**

```text
authority recovery → snapshot → source/DOM planning → desktop implementation
  → operator review → micro-pass → mobile implementation → operator review
  → final baseline → documentation → demo assembly → CMS handoff
```

**Lessons:**

- Small focused **micro-passes** after partial approval beat broad rewrites.  
- Blog Article Pass 06 pattern: hero → body → lower stack as separate review gates.  
- Do not batch multiple visual blocks when protocol requires one block per delivery.

---

## 3. Operator approval

| Lesson | Detail |
|--------|--------|
| Visual PASS | Operator only |
| Technical PASS | Necessary, not sufficient |
| Pixel/height automation | Evidence for operator — not veto/approve by itself |
| Stable checkpoint | Requires recorded operator approval |
| Later polish | Legitimate phase — not drift |

**Evidence:** Tag `fp-0002-v8-operator-approved-frontend-stable-01` only after operator sign-off.

---

## 4. Component reuse

| Lesson | Detail |
|--------|--------|
| Reuse anatomy | Not necessarily identical partial file |
| Shared mutation | Do not change shared components for one new page |
| Page-owned adaptation | When CMS ownership or fields differ |
| Over-generalization | Avoid early — prove stable consumers first |
| Stable pages | Preserve during new-page work |

**Examples (pattern only):** Founder quote on home vs `blog-article-founder-quote`; related cards vs archive cards — similar visuals, different ownership.

---

## 5. Page and content ownership

| Lesson | Detail |
|--------|--------|
| Editor vs template | Make explicit before CMS |
| Article body | One `the_content()` stream |
| Chapter partials in CMS | Avoid |
| Excerpt | Separate field |
| TOC | Generate from semantic headings |
| Query blocks | Outside body stream |

**Evidence:** Blog Article architecture; WordPress-ready baseline.

---

## 6. Responsive implementation

| Lesson | Detail |
|--------|--------|
| One semantic DOM | Required |
| Mobile | SCSS + safe reorder |
| Duplicate mobile content | Prohibited |
| Mobile authority | Verify from mobile design/export — not shrink-desktop only |
| Desktop regression | Check during mobile work |

**Evidence:** Blog hero mobile order; site-wide `1024/1025` split.

---

## 7. Build, evidence, and checkpoints

| Lesson | Detail |
|--------|--------|
| Snapshot | Before risky work |
| Clean build | Required for stable baseline |
| Incremental watch | Insufficient for release |
| Evidence | Storage on `X:\AI MARS STORAGE` |
| `dist/` | Artifact — do not hand-edit |
| Git staging | Full-file selective only — no `git add .` |
| Foreign WIP | Classify and exclude |
| Recovery ZIP + hashes | Important baselines |
| Tag | After operator approval |

---

## 8. Static demo release

| Lesson | Detail |
|--------|--------|
| Separate product | Demo ≠ CMS ≠ dev workspace |
| Structure authority | May come from Excel/inventory — not only existing routes |
| Reconciliation | Intended vs implemented matrix required |
| Placeholders | Label in manifest |
| Package | Standalone relative paths + checksums |
| Confusion guard | Do not claim demo is WordPress |

**Evidence:** V7 demo process; V8 07C spec.

---

## 9. CMS handoff

| Lesson | Detail |
|--------|--------|
| Start point | Approved frontend baseline |
| Visual contract | Frontend output |
| WP adapts to frontend | Not reverse |
| Field mapping | Follow content ownership |
| Logic isolation | CMS-specific code separate where practical |
| Validation | Dynamic output vs static baseline |

**Evidence:** Forge handoff map; FW-06B waiting on intake.

---

## Cross-references

- [implementation-extraction-discipline-v1.md](../implementation-extraction-discipline-v1.md)  
- [FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md](../../workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-PRIORITY-VISUAL-IMPLEMENTATION-PROTOCOL.md)  
- [execution-cases-registry-v1.md](../execution-cases-registry-v1.md)

---

*FP-0002 lessons learned v1 — Website Factory operational examples.*
