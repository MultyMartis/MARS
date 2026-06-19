# REPORT — WF-R01.3.3 WAVE S4 PAGE-TYPE SHELL MATRIX AND SCAFFOLD CONTRACT

**Artifact ID:** WF-R01.3.3 Wave S4 — Page-Type Shell Matrix and Reference Scaffold Contract (v1)  
**Date:** 2026-06-19  
**Mode:** documentation-only — matrix + scaffold contract publication  
**Honesty boundary:** Human-operated normative publication. **Not** scaffold implementation. **Not** G2 authorization. **Not** WF-R01.3.4 start. **Not** coverage accrual.

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Matrix decision** | **ACCEPTED / PUBLISHED** |
| **Matrix path** | `projects/mars-website-factory/page-type-shell-matrix-v1.md` |
| **Scaffold Contract decision** | **ACCEPTED / PUBLISHED** |
| **Scaffold Contract path** | `projects/mars-website-factory/reference-scaffold-contract-v1.md` |
| **WF-R01.3.3 state** | **ACCEPTED** — Wave **S4 COMPLETE**; Waves S1–S4 done; S5 **NOT STARTED** |
| **Metrics** | RC **32/32** · RPC **17/32** · RSC **1/10 global; 1/1 LANDING** · SC **LANDING PASS** · PC **1/1 LANDING** — **UNCHANGED** |
| **Next task** | **WF-R01.3.3 Wave S5 — Exit Evaluation and WF-R01.3.4 Handoff** |

---

## 2. Git Safety

| Field | Value |
|-------|-------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `9c214e2` — docs(site-002): add git hash to filter UX checkpoint report |
| **Wave S3 push state** | Commits `72e7978` (pagination) · `f97213b` (S3 git result) present in branch history |
| **Staged files before task** | **None** |
| **Foreign WIP** | Present — excluded from selective commit |
| **Selective scope** | S4 paths only (2 contracts + roadmap + OPERATIONAL-INDEX + this REPORT) |

---

## 3. Authority Reviewed

| Document | Path | Role |
|---|---|---|
| WF-R01.3.3 Charter | `projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md` | §11 scaffold · §12 matrix · waves S1–S5 |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Shell order · §13 matrix seed · validation |
| Charter pass | `reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md` | Acceptance baseline |
| Wave S1 REPORT | `reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md` | S1 publication evidence |
| Wave S2 REPORT | `reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md` | BREADCRUMBS Tier B · applicability |
| Wave S3 REPORT | `reports/wf-r01-3-3-wave-s3-pagination-v1.md` | PAGINATION Tier B · applicability |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RSC · SC · PC accounting |
| LANDING completion | `projects/mars-website-factory/wf-r01-3-2-landing-completion-charter-v1.md` | G1 scaffold evidence |
| G1 exit | `reports/wf-r01-3-2-g1-five-dimension-exit-v1.md` | Verified metrics |
| LANDING composition | `workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md` | PC pattern |
| LANDING manifest | `workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md` | Manifest pattern |
| Page Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | 10-type denominator |
| Site Type Registry | `workspaces/website-factory-reference-v1/registry/SITE-TYPE-REGISTRY-v1.md` | site_type binding |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Tier A shell rows |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Block inventory |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Tier B inventory |
| Roadmap | `projects/mars-website-factory/roadmap.md` | Program state |
| Operational Index | `projects/mars-website-factory/OPERATIONAL-INDEX.md` | Operator entry |

---

## 4. Duplicate Contract Check

### Page-Type Shell Matrix

| Search terms | `page-type shell matrix` · `shell matrix` · `PAGE-TYPE-SHELL-MATRIX-v1` |
|---|---|
| **Existing artefacts** | Matrix embedded in charter §12 · Global Shell Contract §13 — **COMPLEMENTARY**, not standalone accepted contracts |
| **Standalone file before S4** | **None** |
| **Competing accepted contract** | **None** |
| **Decision** | **CREATE** canonical standalone `page-type-shell-matrix-v1.md` |

### Reference Scaffold Contract

| Search terms | `scaffold contract` · `reference scaffold` · `REFERENCE-SCAFFOLD-CONTRACT-v1` |
|---|---|
| **Existing artefacts** | Charter §11 Shell Scaffold Contract — **COMPLEMENTARY** draft section |
| **LANDING-SCAFFOLD-MANIFEST-v1.md** | **MANIFEST** — instance artefact, **not** global contract |
| **Competing accepted contract** | **None** |
| **Decision** | **CREATE** canonical standalone `reference-scaffold-contract-v1.md` |

---

## 5. Contract Identities

| Artefact | Name | Version | Status | Authority |
|---|---|---|---|---|
| Page-Type Shell Matrix | Website Factory Page-Type Shell Matrix | v1 | **ACCEPTED** | WF-R01.3.3 Wave S4 |
| Reference Scaffold Contract | Website Factory Reference Scaffold Contract | v1 | **ACCEPTED** | WF-R01.3.3 Wave S4 |

---

## 6. Canonical Page-Type Set

| Page type ID | Canonical name | Registry path |
|---|---|---|
| `LANDING_PAGE` | Conversion landing | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` § LANDING_PAGE |
| `HOME_PAGE` | Site home | same |
| `SERVICE_PAGE` | Service money page | same |
| `CATEGORY_PAGE` | Category PLP (PLP-like) | same |
| `PRODUCT_PAGE` | Product PDP (PDP-like) | same |
| `ABOUT_PAGE` | About / company | same |
| `CONTACT_PAGE` | Contact hub | same |
| `FAQ_PAGE` | FAQ hub | same |
| `REVIEWS_PAGE` | Reviews hub | same |
| `LEGAL_PAGE` | Legal document | same |

**No new page types created.** `SEARCH_RESULTS_PAGE` documented as planned note only — not in v1 minimum Registry.

---

## 7. Applicability Codes

| Code | Meaning |
|---|---|
| **REQ** | Required on reference scaffold |
| **OPT** | Optional / minimal |
| **POL** | Policy-dependent — declare in manifest / composition |
| **FORB** | Forbidden — structural FAIL if present |
| **N/A** | Not applicable — absence expected |

Legacy crosswalk: **O → REQ** · **R/P → POL** · **— → N/A or FORB** by semantics.

---

## 8. Page-Type Shell Matrix

| Page type | HEADER_NAV | MAIN | BREADCRUMBS | PAGINATION | FOOTER | LEGAL_LINKS | SEARCH slot | FILTERS slot |
|---|---|---|---|---|---|---|---|---|
| `LANDING_PAGE` | OPT | REQ | N/A | FORB | REQ | REQ | N/A | N/A |
| `HOME_PAGE` | REQ | REQ | POL | POL | REQ | REQ | POL | N/A |
| `SERVICE_PAGE` | REQ | REQ | POL | N/A | REQ | REQ | N/A | N/A |
| `CATEGORY_PAGE` | REQ | REQ | REQ | REQ | REQ | REQ | POL | POL |
| `PRODUCT_PAGE` | REQ | REQ | REQ | N/A | REQ | REQ | POL | N/A |
| `ABOUT_PAGE` | REQ | REQ | REQ | N/A | REQ | REQ | N/A | N/A |
| `CONTACT_PAGE` | REQ | REQ | POL | N/A | REQ | REQ | N/A | N/A |
| `FAQ_PAGE` | REQ | REQ | POL | POL | REQ | REQ | POL | N/A |
| `REVIEWS_PAGE` | REQ | REQ | POL | POL | REQ | REQ | N/A | N/A |
| `LEGAL_PAGE` | REQ | REQ | POL | N/A | REQ | REQ | N/A | N/A |

---

## 9. Matrix Boundary Decisions

- **Shell vs contextual:** Global shell = HEADER_NAV · MAIN · FOOTER · nested LEGAL_LINKS; contextual = BREADCRUMBS · PAGINATION · future SEARCH/FILTERS slots.
- **BREADCRUMBS policy:** REQ on CATEGORY · PRODUCT · ABOUT; N/A on LANDING; POL elsewhere — aligned with S2 REPORT and charter §9.
- **PAGINATION policy:** REQ on CATEGORY; FORB on LANDING; POL on HOME · FAQ · REVIEWS; N/A on non-list surfaces — aligned with S3 REPORT.
- **SEARCH slot:** **NOT IMPLEMENTED** — POL placement notes only (header utility · results context).
- **FILTERS slot:** **NOT IMPLEMENTED** — POL on CATEGORY_PAGE expected under WF-R01.3.4.
- **Nested LEGAL_LINKS:** REQ nested in FOOTER when FOOTER REQ — all matrix rows.
- **No implementation claims:** Matrix publication does not assert partials beyond existing S2/S3 evidence or scaffolds beyond LANDING.

---

## 10. Scaffold Definition

- **Canonical definition:** Buildable page-type implementation binding registered `page_type` to valid shell, composition, assets, manifest, and validation evidence.
- **What is a scaffold:** Source page + manifest + shell + composition + build PASS + structural validation.
- **What is not a scaffold:** Registry row · single partial · bounded host · policy doc · manifest-only markdown.
- **Bounded host classification:** `breadcrumbs-reference.html` and `pagination-reference.html` = Tier B demonstration hosts — **excluded** from RSC.

---

## 11. Required Scaffold Artefacts

| Artefact | Required | Purpose |
|---|---|---|
| Registered page_type | Yes | RSC identity |
| Buildable source page | Yes | Gulp entry |
| Global shell mapping | Yes | Shell contract compliance |
| Block composition | Yes | MAIN sequence |
| Partial mapping | Yes | Include graph |
| SCSS / asset mapping | Yes | Build completeness |
| JavaScript mapping | When needed | Init evidence |
| Scaffold manifest | Yes | Stub honesty + coverage claims |
| Build evidence | Yes | Reproducible PASS |
| Structural validation | Yes | Matrix checks |
| Known limitations | Yes | Honesty boundary |
| Provenance | Yes | Source trail |

---

## 12. Manifest Contract

- **Required fields:** version · status · page_type · site_type · source/dist paths · shell mapping · block sequence · nested compositions · partial/SCSS/JS paths · assets · provenance · build command/result · validation result · coverage claims · limitations · SAFE UNKNOWN · evidence REPORT link.
- **Evidence binding:** Manifest must reference factual buildable source — pattern from LANDING manifest.
- **SAFE UNKNOWN handling:** Explicit declaration when route model, CMS, or secondary pages undeclared.

---

## 13. Shell Requirements

- Matrix + Global Shell Contract binding for all scaffolds.
- MAIN = exactly **1** on all types.
- HEADER_NAV / FOOTER counts per matrix row.
- LEGAL_LINKS nested in FOOTER when required.
- Contextual slots per REQ · POL · N/A · FORB.
- DOM order: HEADER_NAV → MAIN → FOOTER.
- Tier B components use layout-component identity — not fake Registry rows.

---

## 14. Composition and Block Mapping

- Documented block sequence required inside MAIN.
- Each block: canonical identity · family · partial · style · JS · required/optional state.
- Tier B: BREADCRUMBS · PAGINATION — vocabulary hooks only.
- Future FILTERS/SEARCH — slot policy notes until WF-R01.3.4.
- No accidental LANDING composition reuse on other page types.

---

## 15. Build Evidence Contract

| Evidence | Requirement |
|---|---|
| Build command | Exact (`npm run build`) |
| Exit code | 0 |
| Dist path | Declared output exists |
| Unresolved includes | None |
| Hook presence | Per manifest |
| Duplicate hooks | None |
| Shell order | Matrix compliant in output |
| Assets | Present |
| Warnings | Inventoried |

---

## 16. Structural Validation Contract

| Check | Expected |
|---|---|
| Registered page type | Present |
| Source page | Present |
| Dist page | Present |
| Main landmark | Exactly 1 |
| Shell order | Matrix compliant |
| Required blocks | Present |
| Forbidden blocks | Absent |
| Nested compositions | Correct |
| Duplicate identities | None |
| Unresolved includes | None |
| Required CSS | Present |
| Required JS | Present where declared |
| Build | PASS |

Page-type-specific checks from matrix §8.

---

## 17. Responsive and Accessibility Minimum

- Shell preserves DOM semantics; no persistent horizontal overflow.
- Keyboard-operable navigation; visible focus; synchronized mobile nav state.
- Contextual components must not break layout.
- Text scaling must not break critical regions.
- Multiple landmarks need distinct accessible names.
- **Not** WCAG certification.

---

## 18. Coverage Accounting

| Dimension | Value | S4 delta |
|---|---|---|
| **RC** | **32/32** | None |
| **RPC** | **17/32** | None |
| **RSC** | **1/10 global; 1/1 LANDING** | None |
| **SC** | **LANDING PASS** | None |
| **PC** | **1/1 LANDING** | None |

**Accrual rules published in Reference Scaffold Contract §18** — documentation-only S4 does not accrue.

---

## 19. Scaffold Lifecycle

| State | Meaning | Required evidence |
|---|---|---|
| PLANNED | Selected page type | Charter / wave plan |
| AUTHORIZED | Build permitted | Wave preflight |
| BUILT | Compiles to dist | Build PASS |
| STRUCTURALLY VALIDATED | §16 checks PASS | Validation record |
| COMPOSITION PUBLISHED | PC doc live | Reference Composition |
| COVERAGE ACCEPTED | Operator accepts metrics | Five-dimension REPORT |
| FIDELITY VERIFIED | Design QA (optional) | Fidelity REPORT |
| PRODUCTION PASS | Client acceptance | Out of reference default |

---

## 20. Prohibited Claims

- documentation-only scaffold · manifest-only scaffold
- bounded component host as scaffold
- build PASS as fidelity or production pass
- RSC/SC/PC increment from S4 docs alone
- FILTERS/SEARCH slot as implementation
- G2 ACTIVE · WF-R01.3.3 COMPLETE · WF-R01.3.4 ACTIVE from S4

---

## 21. Files Created

| File | Purpose |
|---|---|
| `projects/mars-website-factory/page-type-shell-matrix-v1.md` | Normative page-type shell matrix |
| `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Normative scaffold minimum contract |
| `reports/wf-r01-3-3-wave-s4-shell-matrix-scaffold-contract-v1.md` | This wave REPORT |

---

## 22. Files Modified

| File | Change |
|---|---|
| `projects/mars-website-factory/roadmap.md` | R01.3.3 Wave S4 COMPLETE; S5 next; changelog entry |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | S4 publication; S5 next; footer timestamp |

---

## 23. Validation

- [x] Both normative artefacts created with status **ACCEPTED**
- [x] Page types from Registry only — 10 minimum set
- [x] No new page types · no Registry edits
- [x] Matrix consistent with Global Shell Contract §13
- [x] BREADCRUMBS/PAGINATION aligned with S2/S3
- [x] FILTERS/SEARCH slots only — **NOT IMPLEMENTED**
- [x] Bounded hosts excluded from scaffold accounting
- [x] LANDING manifest unchanged
- [x] `src/` not modified · Gulp not modified
- [x] Metrics unchanged
- [x] WF-R01.3.4 not started · G2 not activated · S5 not executed
- [x] Historical reports not rewritten

---

## 24. Git Result

| Field | Value |
|-------|-------|
| **Commit hash** | *(populated after commit)* |
| **Commit message** | `foundry: publish WF-R01.3.3 shell matrix scaffold contract` |
| **Push result** | *(populated after push)* |
| **Files committed** | 5 paths — selective S4 scope only |
| **No foreign lane** | Confirmed at staging review |

---

## 25. Drift and Risks

| Severity | Finding | Action |
|---|---|---|
| Low | Charter §12 uses legacy **—** codes; matrix v1 uses unified REQ/OPT/POL/FORB/N/A | Crosswalk documented in matrix §3 |
| Low | Global Shell Contract §19 still shows RPC **15/32** at S1 T0 | Historical surface — active state uses **17/32**; not rewritten |
| Low | Bounded hosts may be mistaken for scaffolds | Explicit exclusion in both contracts + §10 |
| None | Competing accepted matrix/scaffold contract | Not found |

---

## 26. Final Status

```text
COMPLETE
```

---

## 27. Next Task

```text
WF-R01.3.3 Wave S5 — Exit Evaluation and WF-R01.3.4 Handoff
```

---

## 28. Exact Evidence Paths

```text
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/wf-r01-3-3-structural-shell-references-charter-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
reports/wf-r01-3-3-wave-s4-shell-matrix-scaffold-contract-v1.md
reports/wf-r01-3-3-wave-s3-pagination-v1.md
reports/wf-r01-3-3-wave-s2-breadcrumbs-v1.md
reports/wf-r01-3-3-wave-s1-global-shell-contract-v1.md
reports/wf-r01-3-3-structural-shell-references-charter-pass-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
workspaces/website-factory-reference-v1/LANDING-SCAFFOLD-MANIFEST-v1.md
workspaces/website-factory-reference-v1/REFERENCE-COMPOSITION-v1.md
```

---

## 29. Stop Confirmation

```text
Wave S5: NOT STARTED
New reference scaffolds: NOT CREATED
RSC: UNCHANGED
SC: UNCHANGED
PC: UNCHANGED
FILTERS: NOT IMPLEMENTED
SEARCH: NOT IMPLEMENTED
WF-R01.3.4: NOT STARTED
G2 execution: NOT STARTED
Reference workspace src/: NOT MODIFIED
Production readiness: NOT CLAIMED
```

---

*Report version: v1 · Authority: WF-R01.3.3 Wave S4 · T0: 2026-06-19*
