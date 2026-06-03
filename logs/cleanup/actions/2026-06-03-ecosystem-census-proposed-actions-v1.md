# Proposed cleanup actions — Census v1 (NOT EXECUTED)

**Date:** 2026-06-03  
**Rule:** Proposals only. No merge, delete, archive, or registry edit performed in this pass.

| ID | Entity / finding | Action | Rationale |
|----|------------------|--------|-----------|
| A-001 | `continuity/` IdeaBox | **KEEP** | Correctly excluded from project registry by design |
| A-002 | `registry/project-registry.md` rows (all) | **KEEP** | SoT; reconcile prose only |
| A-003 | `seo-content-agent` | **KEEP** (legacy band) | Explicit legacy; add lifecycle pointer if touched |
| A-004 | `metabot-seo-content-agent` | **KEEP** | Canonical external system docs |
| A-005 | HomeGateway `status` column vs narrative | **RECLASSIFY** | Align `planned` vs OPERATIONAL documentation band in one place |
| A-006 | `homegateway-v4-ai` | **INVESTIGATE** | Large WIP doc surface vs registry `planned` |
| A-007 | ISBD `workspaces/isbd-care-landing` | **REGISTER** | Add execution-case row or `project_id` + link to Factory/WPilot — operator choice |
| A-008 | ISBD | **RECLASSIFY** | Document as Website Factory execution case vs standalone program |
| A-009 | GitGuard concept | **REGISTER** or **KEEP** as survivability sub-concept only | Decide if separate `project_id` ever needed |
| A-010 | GitGuard | **INVESTIGATE** | G2 tooling map vs entity-model Program example |
| A-011 | MARS Bridge stub | **KEEP** in `incoming/` | **INVESTIGATE** charter for production contract version |
| A-012 | `incoming/*` drops | **INVESTIGATE** | Promote, quarantine, or document intake SOP |
| A-013 | Triumph workspace versions | **INVESTIGATE** | Name canonical workspace; mark others archive-candidate |
| A-014 | Triumph duplicates (orca nested + factory + workspaces) | **RECLASSIFY** | Single relationship map: program vs ORCA case vs workspace |
| A-015 | `projects/orca/projects/triumph-manipulator-krasnodar/` | **KEEP** | **RECLASSIFY** link to `triumph-manipulator-landing` id |
| A-016 | Lifecycle log gaps 0017–0021 | **REGISTER** (events) | Append-only backfill per `lifecycle-synchronization-review-v0.md` |
| A-017 | `web-gpt-sources/` legacy trees | **ARCHIVE** (candidate) | Mark historical; avoid new edits there |
| A-018 | `workspaces/_sandbox`, `_tmp`, `_quarantine` | **KEEP** | **INVESTIGATE** retention policy |
| A-019 | WPilot future agents | **REGISTER** (cards) | Only if roles become active |
| A-020 | Integration registry | **INVESTIGATE** | Populate v0 rows for MetaBOT, n8n, WordPress, Sheets |
| A-021 | Knowledge Center | **KEEP** (out-of-git) | Document sync cadence with git canvas pack |
| A-022 | `mars-runtime/` R1 JS | **KEEP** | **RECLASSIFY** labels on adapter filenames (seo legacy id) |
| A-023 | Factory block registry duplication | **MERGE** (candidate) | Align v0 doc with reference-v1 — **do not merge without charter** |
| A-024 | ORCA archive/freeze duplicate trees | **ARCHIVE** (candidate) | Compress after operator confirms stable pointer |
| A-025 | `mars-core` example registry row | **RECLASSIFY** or remove example | Reduces registry noise |
| A-026 | `continuity/registry/master-index.md` | **INVESTIGATE** | Populate manual links or deprecate index |
| A-027 | ISBD canvas placeholder | **REGISTER** | Update `website-factory.canvas` when A-007 decided |
| A-028 | `governance/mars-v2-structural-coherence-audit-v0.md` | **KEEP** | Note WPilot row stale claim — add errata pointer |
| A-029 | `projects/mig/archive/pre-pilot-gruzotaxi-krasnodar-v1/` | **ARCHIVE** (candidate) | Historical pilot |
| A-030 | `incoming/website-factory-legal-cleanup/` | **INVESTIGATE** | Promote to Factory legal registry or keep intake-only |

---

*Proposed actions registry — execution deferred.*
