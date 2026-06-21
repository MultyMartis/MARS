# REPORT — FP-0002 WORKSPACE RESET V2

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Date:** 2026-06-14  
**Scope:** Infrastructure only — **no** HTML/SCSS/JS production work  
**Authority:** Workspace Archive Rule · [website-factory-production-roadmap-v2-draft.md](../../../../projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md) Phase B

---

## 1. Archived

| Field | Value |
|-------|-------|
| **What** | Complete pre-v2 frontend workspace (M2 Foundation Extraction residue) |
| **Former path** | `C:\AI MARS\workspaces\fp-0002-shpigovsky-frontend\` |
| **Phase at archive** | M2 — ui-demo, header/footer/mobile shell, M2 components |
| **File count** | 57 files (excluding `node_modules`) |
| **Lifecycle** | **ARCHIVED** · **READ ONLY** · **REFERENCE ONLY** |

### Archive verification

| Item | In archive |
|------|------------|
| `src/` | YES |
| `dist/` | YES |
| `package.json` | YES |
| `gulpfile.js` | YES |
| `README.md` | YES |
| `reports/` | N/A — never existed in source workspace |
| `backups/` | N/A — never existed in source workspace |

Nothing present in the source workspace was lost during move.

---

## 2. Archive destination

```
C:\AI MARS STORAGE\website-factory\archive\fp-0002-shpigovsky-frontend-pre-v2\
```

Marker file: `ARCHIVED.md`

---

## 3. Created anew

| Item | Path / detail |
|------|---------------|
| **Active workspace** | `C:\AI MARS\workspaces\fp-0002-shpigovsky-frontend\` |
| **Starter source** | `workspaces/triumph-manipulator-landing/` (canonical gulp-starter) |
| **`reports/`** | Created (`.gitkeep`) |
| **`backups/`** | Created (`.gitkeep`) |
| **`versions/`** | Created (`.gitkeep`) |
| **`src/`** | From starter copy |
| **`dist/`** | Generated via `npm run build` — **Build succeeded** |
| **`package.json`** | Renamed to `fp-0002-shpigovsky-frontend@2.0.0` |
| **`README.md`** | FP-0002 cycle v2 workspace doc |

**Lifecycle:** **ACTIVE** · **CANONICAL** · **PRODUCTION**

---

## 4. Governance files changed

| File | Change |
|------|--------|
| [workspace-reset-governance.md](../../../../projects/mars-website-factory/workspace-reset-governance.md) | Added **§8 Workspace Archive Rule** (WA-01…WA-06); changelog v1 |
| [website-factory-production-roadmap-v2-draft.md](../../../../projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md) | Phase B.1 + authority table — archive rule cross-reference |

---

## 5. New files created

| File | Location |
|------|----------|
| `ARCHIVED.md` | `C:\AI MARS STORAGE\website-factory\archive\fp-0002-shpigovsky-frontend-pre-v2\` |
| `FP-0002-WORKSPACE-STATUS-v1.md` | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` |
| `FP-0002-WORKSPACE-RESET-V2-REPORT.md` | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/` (this file) |
| `reports/.gitkeep` | Active workspace |
| `backups/.gitkeep` | Active workspace |
| `versions/.gitkeep` | Active workspace |

---

## 6. Design sources verified

| Source | Path | Exists |
|--------|------|--------|
| Design PDFs | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/` | **YES** (24 PDF + README + home-v2 subfolder) |
| Content / IA XLSX | `INCOMING/02_CONTENT/Предварит структура и спрос.xlsx` | **YES** |

New workspace references these paths in README and `FP-0002-WORKSPACE-STATUS-v1.md` — **not** duplicated into `src/assets/design/`.

---

## 7. Readiness check

| Gate | Document | Status |
|------|----------|--------|
| **A0 Source Discovery** | [FP-0002-SOURCE-DISCOVERY-REPORT-v1.md](FP-0002-SOURCE-DISCOVERY-REPORT-v1.md) | **COMPLETE** (2026-06-14) |
| **A1 Design Audit** | [FP-0002-DESIGN-AUDIT-v1.md](FP-0002-DESIGN-AUDIT-v1.md) | **COMPLETE** (2026-06-14) |
| **Design Approval Sheet** | [FP-0002-DESIGN-APPROVAL-SHEET-v1.md](FP-0002-DESIGN-APPROVAL-SHEET-v1.md) | **COMPLETE** (2026-06-14) |
| **Operator Decisions** | `DECISIONS.md` (ADR journal) | **Empty** — no formal ADR rows; D-001…D-022 coordinator columns **unsigned** in v2 sheet |
| **Production Standards** | [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](../FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) | **APPROVED** (Lead 2026-06-13) |
| **D-021** | Shell token authority | **Variant A** — Production Standards v3 for shell (recommended in approval sheet; aligned with approved v3 SSOT) |
| **Shell standard** | Production Standards v3 | **YES** — shell builds per v3 per D-021 Variant A |

---

## 8. Confirmations

| Check | Result |
|-------|--------|
| **WORKSPACE READY** | **YES** |
| **DESKTOP SHELL READY TO START** | **YES** |
| **HEADER NOT STARTED** | **YES** — no FP-0002 Shpigovsky shell/header work |
| **FOOTER NOT STARTED** | **YES** — no FP-0002 Shpigovsky shell/footer work |
| **HOME NOT STARTED** | **YES** — no PG-001; starter `index.html` is generic gulp-starter demo only |
| **NEXT PHASE** | **DESKTOP SHELL** (Phase C) |

---

## 9. Build validation

```text
npm install — OK
npm run build — OK (gulp build, 2026-06-14)
```

---

## 10. UNKNOWN / notes

| Item | Note |
|------|------|
| D-001…D-022 coordinator sign-off | **Unsigned** in `FP-0002-DESIGN-APPROVAL-SHEET-v2.md` — does not block Phase C shell start per roadmap; D-021 resolved via Variant A + approved v3 |
| Starter demo content | Generic Triumph demo pages remain from gulp-starter — **not** FP-0002 deliverables; replace during Phase C/D |

---

## Changed files summary

**In repo (`C:\AI MARS`):**

- `projects/mars-website-factory/workspace-reset-governance.md` (modified)
- `projects/mars-website-factory/website-factory-production-roadmap-v2-draft.md` (modified)
- `workspaces/fp-0002-shpigovsky-frontend/` (recreated — starter copy + npm install/build)
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-WORKSPACE-STATUS-v1.md` (new)
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/FP-0002-WORKSPACE-RESET-V2-REPORT.md` (new)

**Outside repo (bulk storage):**

- `C:\AI MARS STORAGE\website-factory\archive\fp-0002-shpigovsky-frontend-pre-v2\` (moved + `ARCHIVED.md`)

**Commit / push:** not performed (default policy).
