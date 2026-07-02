# V9-03G Working Tree Ownership Audit

**Phase:** V9-03G Scroll-to-top  
**Date:** 2026-07-02

| Lane | Ownership |
|------|-----------|
| V9-01 carried WIP | preserved (foreign to this phase) |
| V9-02 carried WIP | preserved |
| V9-03B approved motion | preserved |
| V9-03C approved G6 removal | preserved |
| V9-03F approved Triumph modal runtime | **protected — unchanged** |
| V9-03G scroll-to-top | **this phase** — shared partial, footer include, SCSS, JS append, validator |
| Validation tooling | updated `v9-validate-all.mjs` |
| Documentation/status | V9 workspace docs + Forge readiness + PROJECT-STATUS |
| Storage evidence | excluded from git |
| Foreign WIP | preserved — no broad staging |

## V9-03G changed files (this phase)

**Created:**
- `src/partials/components/scroll-to-top.html`
- `FP-0002-V9-03F-APPROVED-PRE-SCROLL-TO-TOP-BACKUP-MANIFEST.md`
- `FP-0002-V9-03G-*-v1.md` (audit/validation set)
- `REPORT-FP-0002-V9-PHASE-03G-SCROLL-TO-TOP-v1.md`
- `V9-03G-WORKING-TREE-OWNERSHIP-AUDIT.md`

**Modified:**
- `src/partials/layout/footer.html` (shared include after page shell)
- `src/scss/style.scss` (scroll-to-top block + reduced-motion entry)
- `src/js/main.js` (append-only `initScrollToTop`)
- `tools/v9-validate-all.mjs`
- `README.md`, `foundation/FP-0002-V9-OPERATIONAL-STATUS.md`
- `FP-0002-V9-FORGE-READINESS-NOTES-v1.md`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/PROJECT-STATUS.md`

**Removed:** none

**Git checkpoint:** none (per phase boundary)

**Final status:** `FP0002_V9_03G_SCROLL_TO_TOP_COMPLETE_PENDING_OPERATOR_VISUAL_REVIEW_FOREIGN_WIP_PRESERVED`
