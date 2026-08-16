# Forge Proger Experience Pack — Phase 2 (FP-0002 V9 Stable v1)

**Status:** DOCUMENTATION ONLY  
**Integration into Forge Proger brains/rules:** **NOT DONE** (explicitly deferred to later charter)  
**Project:** FP-0002 — Шпиговский  
**Covered wave range:** V9-06E54 → V9-06E63 (post–Experience Pack Phase 1 through Stable v1 closeout)  
**Created:** 2026-07-18  
**Location:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/DOCS/FORGE-PROGER-EXPERIENCE-PACK/v9-stable-v1-phase-02/`

## Purpose of Phase 2

Preserve all important operational experience and reusable Forge Proger knowledge accumulated **after** Phase 1 (E26–E53 admin-parity batch), especially the path from accepted admin UX freeze (E53) to **Stable local near-production baseline** (E63 / `FP-0002-V9-STABLE-V1`).

This pack exists so workspace cleanup can begin later **without losing**:

- what was built after E53;
- how it was built safely under runtime-operator canon;
- which approaches worked vs failed / false-PASS;
- how to close, freeze, and push a long WordPress wave in a dirty MARS monorepository.

## Relationship to Phase 1

| Pack | Path | Wave range | Focus |
|------|------|------------|-------|
| **Phase 1** | [`../v9-06-batch-01/`](../v9-06-batch-01/) | E26–E53 | Admin parity, ACF SoT, placeholder mode, selective Git persistence |
| **Phase 2 (this)** | `./` | E54–E63 | Visual polish, operator runtime canon, reusable FE/admin patterns, Stable v1 closeout, cleanup policy |
| **Phase 3 (planned)** | not created | after production launch experience | Polish, generalize, SOP consolidation |

Phase 2 **extends** Phase 1. It does not rewrite Phase 1. Where topics overlap (admin UX, Git, ACF), Phase 2 adds **post-E53 evidence** and points back to Phase 1 for earlier foundations.

Master index: [`../INDEX.md`](../INDEX.md).

## Stable v1 identity (project fact)

| Field | Value |
|-------|-------|
| Release | FP-0002 V9 Stable v1 |
| Release code | `FP-0002-V9-STABLE-V1` |
| Status | STABLE / NEAR-PRODUCTION |
| Release wave | V9-06E63 |
| Content release commit | `d1befe9b8bfc8688f2f286998ec048e6be49beb6` |
| Final canonical remote tip | `9d5dcc285eb45c827231bfe89c7611fb84e850d2` |
| Branch | `origin/mars/canonical-post-recovery` |
| Authoritative freeze | `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-stable-v1-near-production-freeze-20260718-004137` |
| Production deployment | **not performed** |

## Document map

| File | Purpose |
|------|---------|
| [FORGE-PROGER-EXPERIENCE-FP0002-V9-STABLE-V1-PHASE-02.md](./FORGE-PROGER-EXPERIENCE-FP0002-V9-STABLE-V1-PHASE-02.md) | Primary narrative E53→Stable v1 |
| [TIMELINE-E54-E63.md](./TIMELINE-E54-E63.md) | Chronological wave timeline with PASS-reliability marks |
| [RUNTIME-OPERATOR-CANON-PATTERN.md](./RUNTIME-OPERATOR-CANON-PATTERN.md) | Runtime-first operator canon + preflight algorithm |
| [ADMIN-UX-AND-ACF-OWNERSHIP-PATTERNS.md](./ADMIN-UX-AND-ACF-OWNERSHIP-PATTERNS.md) | Site Settings, page vs block ownership, ACF patterns |
| [REUSABLE-FRONTEND-COMPONENT-PATTERNS.md](./REUSABLE-FRONTEND-COMPONENT-PATTERNS.md) | Shared CTA, Founder, crumbs, reviews, search, 404 |
| [VISUAL-AUDIT-AND-FIGMA-PARITY-LESSONS.md](./VISUAL-AUDIT-AND-FIGMA-PARITY-LESSONS.md) | E58 audit, visual authority hierarchy |
| [ANTI-PATTERNS-AND-FAILURES-PHASE-02.md](./ANTI-PATTERNS-AND-FAILURES-PHASE-02.md) | Failures, false PASS, near-misses after E53 |
| [WORDPRESS-PROJECT-CLOSEOUT-AND-FREEZE-PATTERN.md](./WORDPRESS-PROJECT-CLOSEOUT-AND-FREEZE-PATTERN.md) | E63 release / freeze / Git pattern |
| [BACKUP-EVIDENCE-AND-CLEANUP-POLICY.md](./BACKUP-EVIDENCE-AND-CLEANUP-POLICY.md) | Artifact classes + retention rules |
| [FORGE-PROGER-CAPABILITY-BACKLOG-AFTER-FP0002.md](./FORGE-PROGER-CAPABILITY-BACKLOG-AFTER-FP0002.md) | Future Forge Proger capabilities |
| [PHASE-03-POLISH-BACKLOG.md](./PHASE-03-POLISH-BACKLOG.md) | What Phase 3 must revisit |
| [SOURCE-TRACEABILITY-MATRIX.md](./SOURCE-TRACEABILITY-MATRIX.md) | Lesson → evidence links |
| [CLEANUP-CANDIDATE-INVENTORY-PRE-PHASE.md](./CLEANUP-CANDIDATE-INVENTORY-PRE-PHASE.md) | Read-only cleanup inventory (advisory; historical pre-phase sizes) |
| [CLEANUP-PLAN-AFTER-EXPERIENCE-PHASE-02.md](./CLEANUP-PLAN-AFTER-EXPERIENCE-PHASE-02.md) | Staged cleanup plan for next wave |
| [CLEANUP-EXECUTION-FEEDBACK-FOR-PHASE-03.md](./CLEANUP-EXECUTION-FEEDBACK-FOR-PHASE-03.md) | E64 + E65 cleanup execution feedback (Phase 3 input; Phase 3 not started) |
| E65 report (outside this folder) | [`../../../REPORTS/REPORT-FP-0002-V9-06E65-MANUAL-REVIEW-CLEANUP.md`](../../../REPORTS/REPORT-FP-0002-V9-06E65-MANUAL-REVIEW-CLEANUP.md) — manual-review resolution |
| E65 remaining queue | [`../../../REPORTS/CLEANUP/E65-REMAINING-MANUAL-REVIEW.txt`](../../../REPORTS/CLEANUP/E65-REMAINING-MANUAL-REVIEW.txt) |

## Recommended reading order

1. This INDEX  
2. Primary narrative  
3. Timeline E54–E63  
4. Runtime-operator canon pattern  
5. Anti-patterns Phase 02  
6. Admin UX / ACF ownership  
7. Reusable frontend patterns  
8. Visual audit / Figma lessons  
9. Closeout and freeze pattern  
10. Traceability matrix (as needed)  
11. Cleanup policy → inventory → cleanup plan (before any cleanup charter)  
12. Capability backlog + Phase 3 backlog  

## Project-specific vs reusable

| Class | Examples | How to use |
|-------|----------|------------|
| **Project-specific facts** | Shpigovsky paths, page IDs, exact CSS hashes, Stable v1 commit SHAs, clinic copy | Cite as evidence; do not hard-code into Forge Proger brains |
| **Reusable Forge Proger knowledge** | Runtime-operator canon, visual authority hierarchy, ACF ownership matrix, monorepo closeout checklist, cleanup gates | Candidates for later SOP / capability design under explicit charter |

## Future Phase 3 purpose

Polish and generalize this pack closer to **public production launch**: consolidate Phase 1+2 overlap, convert patterns into standard operating procedures, validate against another WordPress project, incorporate SMTP/forms/indexing deployment experience, and update cleanup policy after a real cleanup wave. See [PHASE-03-POLISH-BACKLOG.md](./PHASE-03-POLISH-BACKLOG.md). **Do not execute Phase 3 in this wave.**

## Guardrails (this pack)

- Do **not** modify Forge Proger brain/system/rules from this pack alone.
- Do **not** treat pack text as automated enforcement.
- Do **not** delete backups, evidence, worktrees, or product files because this pack exists.
- Cleanup requires a **separate explicit destructive charter**.
