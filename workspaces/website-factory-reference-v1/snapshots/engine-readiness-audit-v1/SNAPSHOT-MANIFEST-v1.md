# SNAPSHOT-MANIFEST-v1 — Engine Readiness Audit Snapshot

**Snapshot ID:** `engine-readiness-audit-v1`  
**Snapshot date:** 2026-06-04  
**Source workspace:** `workspaces/website-factory-reference-v1/`  
**Snapshot path:** `workspaces/website-factory-reference-v1/snapshots/engine-readiness-audit-v1/`  
**Operator:** Website Factory Engine Readiness Audit v1 (Phase 1)

---

## Snapshot purpose

Full **pre-Engine** point-in-time copy of Website Factory Foundation documentation stack immediately before **Factory Engine Architecture v1** readiness evaluation.

This snapshot:

- preserves accepted layer artefacts without modifying source documents;
- provides an integrity baseline for [ENGINE-READINESS-AUDIT-v1.md](../../ENGINE-READINESS-AUDIT-v1.md);
- complements prior [runtime-foundation-v1](../runtime-foundation-v1/) inventory snapshot (2026-06-01).

**Honesty:** snapshot contains **documentation only** — no shipped Website Factory runtime, Factory Engine, validators CLI, workflow engine, or agents.

---

## Included folders

| Folder | File count | Entry document (reference) |
|--------|------------|----------------------------|
| `legal/` | 21 | `legal/LEGAL-PACK-v1-FREEZE.md` |
| `legal-entity/` | 8 | `legal-entity/LEGAL-ENTITY-WORKFLOW-v1.md` |
| `registry/` | 6 | `registry/SITE-TYPE-REGISTRY-v1.md` |
| `blueprints/` | 10 | `blueprints/BLUEPRINT-SYSTEM-v1.md` |
| `page-architecture/` | 9 | `page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md` |
| `block-registry/` | 14 | `block-registry/BLOCK-REGISTRY-v1.md` |
| `page-block-validation/` | 9 | `page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md` |
| `seo-architecture/` | 8 | `seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md` |
| `design-system/` | 8 | `design-system/DESIGN-SYSTEM-MAPPING-v1.md` |
| `content-contracts/` | 8 | `content-contracts/CONTENT-SYSTEM-v1.md` |
| `content-validation/` | 8 | `content-validation/CONTENT-VALIDATION-SYSTEM-v1.md` |
| `generation-contracts/` | 8 | `generation-contracts/GENERATION-SYSTEM-v1.md` |
| `production-qa/` | 9 | `production-qa/PRODUCTION-QA-SYSTEM-v1.md` |
| `runtime-architecture/` | 9 | `runtime-architecture/RUNTIME-ARCHITECTURE-SYSTEM-v1.md` |

**Layer files subtotal:** 135

---

## Included root `*.md` files

| File |
|------|
| `ARCHITECTURE-FOUNDATION-v1.md` |
| `BRAIN-CONSISTENCY-PASS-v1.md` |
| `FOUNDATION-FINALIZATION-PASS-v1.md` |
| `HYGIENE-PASS-v1.md` |
| `PRE-ENGINE-INTEGRITY-AUDIT-v1.md` |
| `README.md` |
| `WEBSITE-FACTORY-FOUNDATION-CHECKPOINT-v1.md` |
| `WEBSITE-FACTORY-FOUNDATION-v1-FREEZE.md` |
| `WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md` |
| `WEBSITE-FACTORY-RUNTIME-FOUNDATION-SNAPSHOT-v1.md` |

**Root markdown subtotal:** 10

---

## Included snapshot references

| Path | Files | Notes |
|------|-------|-------|
| `snapshots-reference/` | 2 | Copy of `snapshots/runtime-foundation-v1/` (`SNAPSHOT-MANIFEST-v1.json`, `README.md`) |

**Reference subtotal:** 2

---

## Excluded from snapshot (by charter)

| Exclusion | Reason |
|-----------|--------|
| `node_modules/` | Build dependency cache |
| `dist/` | Build output |
| `.cache/` | Transient cache |
| `logs/tmp/` | Temporary logs |
| `temp/` | Temporary files |
| `src/` | Reference implementation — out of pre-Engine documentation snapshot scope |
| `docs/` | Demo scripts — not foundation layer |
| `package.json`, `package-lock.json` | Build tooling — not architecture layer |
| `snapshots/engine-readiness-audit-v1/` (self) | Prevents recursive copy |

Robocopy `/XD` flags applied during copy for `node_modules`, `dist`, `.cache`, `logs`, `tmp`, `temp` if present under layer trees.

---

## File counts summary

| Category | Count |
|----------|-------|
| Layer directories | 14 |
| Layer files | 135 |
| Root foundation `*.md` files (copied from workspace root) | 10 |
| Snapshot reference files | 2 |
| This manifest | 1 |
| **Grand total (files in snapshot tree)** | **148** |

Layer file count **matches** prior `runtime-foundation-v1/SNAPSHOT-MANIFEST-v1.json` inventory (135 layer artefacts).

---

## Integrity notes

| Check | Result |
|-------|--------|
| All 14 required layer folders present | **PASS** |
| Layer file count vs runtime-foundation-v1 manifest | **PASS** (135 = 135) |
| Source documents modified during snapshot | **NO** — copy-only operation |
| Cryptographic checksums | **NOT GENERATED** — file-path inventory only |
| Physical copy outside repo clone | **SAFE UNKNOWN** |
| `src/` reference partials | **EXCLUDED** — not part of this snapshot charter |

**Method:** PowerShell directory creation + `robocopy /E` with exclusion directories; root `*.md` copied via `Copy-Item`; prior snapshot reference copied to `snapshots-reference/`.

**Prior snapshot relationship:** `runtime-foundation-v1` (2026-06-01) remains historical inventory baseline; this snapshot adds post-finalization root docs and precedes Engine charter evaluation.

---

*SNAPSHOT-MANIFEST-v1 — 2026-06-04. Canonical location: `workspaces/website-factory-reference-v1/snapshots/engine-readiness-audit-v1/`.*
