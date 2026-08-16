# Cleanup Candidate Inventory — Pre-Phase (Advisory)

**Generated:** 2026-07-18  
**Mode:** READ-ONLY scan — **DELETE NOTHING**  
**Scope roots:** FP-0002 backups, reports/evidence, Storage git-sync-fp0002-*, selected runtime logs, Storage exports  

Sizes are approximate (MiB), measured by recursive file sum.

---

## 1. Totals (approximate)

| Category | Count (scoped) | Current size | Removable (proposed) | Retained (proposed) | Risk if wrong delete |
|----------|----------------|--------------|----------------------|---------------------|----------------------|
| All backups under `shpigovsky/` | 155 dirs | **~15012 MB** | see §3–4 | Stable+milestones+pre-closeout | **CRITICAL** |
| E54–E63 named wave backups | 23 | **~6974 MB** | **~2830–3940 MB** candidates | **~4140 MB** protected subset | HIGH |
| Evidence `REPORTS/evidence` | all / E54+ 24 | **~369 / ~360 MB** | low (temp only) | keep Git-needed packs | MED |
| git-sync worktrees | 6 | **~8941 MB** | **~5875 MB** stale+empty after verify | keep until cleanup confirm; then e63 deletable | MED–HIGH |
| Runtime debug.log | 1 | **~3.7 MB** | ~3.7 MB | regenerable | LOW |
| Storage exports fp-0002* | 3 | **~280 MB** | MANUAL_REVIEW | preview may KEEP | MED |
| Pre-E54 backup dirs | 132 | **~8038 MB** (15012−6974) | MANUAL_REVIEW staged later | milestone freezes KEEP | HIGH |

**Proposed retained (minimum protected from E54–E63 set):** ~4140 MB  
**Proposed removable among E54–E63 candidates:** ~2830–3940 MB (depends on whether mid-size E59/E61 full checkpoints are archived vs deleted)  
**Worktree removable after remote verify:** empty 0 MB + older syncs ~5875 MB + optionally e63 ~3066 MB  

---

## 2. Protected / retain (do not delete in first cleanup)

| Exact path | Type | Size MB | mtime | Wave | Superseded by | Recommendation | Deletion confidence | Risk | Action | Rationale |
|------------|------|---------|-------|------|---------------|----------------|---------------------|------|--------|-----------|
| `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\v9-stable-v1-near-production-freeze-20260718-004137` | authoritative stable freeze | 1193.97 | 2026-07-18 | E63 | — | retain | n/a | CRITICAL | **KEEP** | Authoritative Stable v1 |
| `…\v9-06e63-before-stable-v1-closeout-20260718-003355` | rollback backup | 1471.90 | 2026-07-18 | E63 | Stable freeze | until cleanup confirmed | n/a | HIGH | **KEEP_UNTIL_PRODUCTION** | Pre-closeout rollback |
| `…\v9-06e58-current-baseline-freeze-before-visual-audit-20260716-225434` | major milestone freeze | 1357.77 | 2026-07-16 | E58 | Stable (partial) | historical + style authority | low | HIGH | **KEEP** | Cited by E60-FIX01 / audit |
| `…\v9-06e53-admin-ux-section-styling-freeze-accepted-before-experience-pack-20260716-053214` | major milestone freeze | 116.40 | 2026-07-16 | E53 | later freezes | Phase 1 anchor | low | MED | **KEEP** | Accepted admin baseline |
| `REPORTS/STABLE-V1/*` + freeze markers | release documentation | (in Git) | 2026-07-18 | E63 | — | retain | n/a | HIGH | **KEEP** | Release truth |
| `WORDPRESS/` source + runtime site | source/runtime authority | n/a | current | — | — | never cleanup-delete | n/a | CRITICAL | **KEEP** | Product |

---

## 3. E54–E63 wave backups (candidates)

| Exact path (under backup root) | Type | Size MB | mtime | Wave | Superseded by | Retention | Del. confidence | Risk | Action | Rationale |
|--------------------------------|------|---------|-------|------|---------------|-----------|-----------------|------|--------|-----------|
| `v9-06e54-after-web-gpt-chat-migration-before-floating-header-work-20260716-150606` | fullish rollback | 1002.34 | 2026-07-16 | E54 | E58/Stable | after verify | MED | MED | **DELETE_IN_CLEANUP_PHASE** | Pre-float; covered later |
| `v9-06e54-fix01-before-background-menu-scroll-fix-20260716-153527` | small intermediate | 0.07 | 2026-07-16 | E54-FIX01 | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny checkpoint |
| `v9-06e55-before-site-settings-admin-ux-20260716-162242` | small intermediate | 0.01 | 2026-07-16 | E55 | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e56-before-operator-refinements-batch-01-20260716-181633` | fullish rollback | 1031.47 | 2026-07-16 | E56 | E58/Stable | — | MED | MED | **DELETE_IN_CLEANUP_PHASE** | Superseded |
| `v9-06e56-fu01-before-hero-slider-font-follow-up-20260716-191824` | small intermediate | 1.90 | 2026-07-16 | E56-FU01 | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e56-fu02-before-libertinus-serif-20260716-210337` | small intermediate | 6.89 | 2026-07-16 | E56-FU02 | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e57-before-lifebuoy-global-parallax-20260716-212623` | small intermediate | 1.38 | 2026-07-16 | E57 | E58 | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e57-fix01-before-lifebuoy-motion-refinement-20260716-214936` | small intermediate | 1.32 | 2026-07-16 | E57-FIX01 | E58 | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e57-fix02-before-lifebuoy-start-reveal-easing-rotation-20260716-220628` | small intermediate | 1.31 | 2026-07-16 | E57-FIX02 | E58 | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e59-before-layout-polish-maps-footer-comfort-admin-20260717-001046` | mid rollback | 279.91 | 2026-07-17 | E59 | Stable | — | MED | MED | **MANUAL_REVIEW** | Mid-size; may ARCHIVE |
| `v9-06e59-fix01-before-comfort-contacts-footer-corrections-20260717-013408` | mid rollback | 281.62 | 2026-07-17 | E59-FIX01 | Stable | — | MED | MED | **MANUAL_REVIEW** | Near-duplicate of E59 |
| `v9-06e60-before-nav-breadcrumb-cta-service-links-20260717-015352` | small intermediate | 7.37 | 2026-07-17 | E60 | FIX01/Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e60-fix01-before-breadcrumb-subnav-reviews-correction-20260717-020758` | small intermediate | 8.80 | 2026-07-17 | E60-FIX01 | Stable | — | MED | LOW | **DELETE_IN_CLEANUP_PHASE** | Evidence in Git reports |
| `v9-06e61-before-admin-controls-contacts-blog-reviews-ocentre-home-20260717-141747` | mid rollback | 280.70 | 2026-07-17 | E61 | Stable | — | MED | MED | **MANUAL_REVIEW** | Demo-seed era DB |
| `v9-06e62a-before-404-breadcrumb-wrapper-phone-mask-20260717-160948` | small intermediate | 6.67 | 2026-07-17 | E62A | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e62b-before-blog-reviews-pagination-seo-demo-content-20260717-162925` | small intermediate | 7.28 | 2026-07-17 | E62B | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e62c-before-ocentre-service-admin-review-anchor-final-regression-20260717-164734` | small intermediate | 8.22 | 2026-07-17 | E62C | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e62d-before-program-mini-descriptions-404-figma-correction-20260717-170730` | small intermediate | 9.81 | 2026-07-17 | E62D | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e62e-before-404-decor-wordpress-search-20260717-173256` | small intermediate | 5.90 | 2026-07-17 | E62E | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |
| `v9-06e62e-fix01-before-search-wrapper-trigger-placement-20260717-174720` | small intermediate | 7.86 | 2026-07-17 | E62E-FIX01 | Stable | — | HIGH | LOW | **DELETE_IN_CLEANUP_PHASE** | Tiny |

Protected rows from §2 omitted here as candidates.

---

## 4. Git-sync worktrees (`X:\AI MARS STORAGE`)

| Exact path | Type | Size MB | Files | Wave | Superseded by | Action | Risk | Rationale |
|------------|------|---------|-------|------|---------------|--------|------|-----------|
| `…\git-sync-fp0002-e63-stable-v1-20260718-004331` | clean Git worktree | 3065.86 | 26082 | E63 | remote `9d5dcc28` | **KEEP** until cleanup confirm, then **DELETE_IN_CLEANUP_PHASE** | MED | Re-creatable; verify remote first |
| `…\git-sync-fp0002-push-divergence-20260716-040930` | stale worktree | 2747.03 | 24859 | E38–E51 push | later pushes | **DELETE_IN_CLEANUP_PHASE** | MED | Superseded |
| `…\git-sync-fp0002-e29b-fix2c-20260710-180821` | stale worktree | 2675.96 | 20385 | E29 | later | **DELETE_IN_CLEANUP_PHASE** | MED | Old |
| `…\git-sync-fp0002-e29c-e35-20260713-032549` | stale worktree | 452.42 | 2040 | E29c–E35 | later | **DELETE_IN_CLEANUP_PHASE** | LOW–MED | Old |
| `…\git-sync-fp0002-e38-e51-20260716-031000` | stale/empty | 0 | 0 | E38–E51 | — | **DELETE_IN_CLEANUP_PHASE** | LOW | Empty |
| `…\git-sync-fp0002-e58-20260716-225851` | stale/empty | 0 | 0 | E58 | — | **DELETE_IN_CLEANUP_PHASE** | LOW | Empty |

---

## 5. Evidence / exports / runtime

| Path | Type | Size MB | Action | Rationale |
|------|------|---------|--------|-----------|
| `FP-0002-SHPIGOVSKY\REPORTS\evidence\` (E54+ packs) | evidence screenshot pack | ~360 | **KEEP** (Git/archive) | Supports accepted baseline |
| Temp HTML dumps inside evidence (if any unreferenced) | temporary evidence | varies | **MANUAL_REVIEW** | Delete only if not cited |
| `X:\AI MARS STORAGE\exports\fp-0002-shpigovsky-preview` | generated export | ~255 | **MANUAL_REVIEW** | Large; may ARCHIVE |
| `…\exports\fp-0002-shpigovsky-persistence` | generated export | ~24 | **MANUAL_REVIEW** | |
| `…\exports\fp-0002-shpigovsky-home-freeze` | generated export | ~0.5 | **KEEP** or ARCHIVE | Home freeze companion |
| `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\wp-content\debug.log` | cache/log | ~3.7 | **DELETE_IN_CLEANUP_PHASE** | Regenerable; smoke after |

---

## 6. Pre-E54 backups (summary only)

- **132** directories not matching E54–E63/Stable naming.
- Sample milestone sizes: E42 freeze ~198 MB; E49 after-FIX01 ~207 MB; E51 placeholder freeze ~202 MB; foundation-001 ~51 MB.
- **Action:** **MANUAL_REVIEW** in a later cleanup stage — retain accepted freezes (E42/E44/E47/E49/E50/E51/E53) until operator map confirms Stable supersession; do not bulk-delete pre-E54 in first cleanup stage.

---

## 7. Explicit non-scan / out of scope

- Unrelated MARS project backups
- Foreign Git WIP under `X:\AI MARS` outside FP-0002 allowlist
- WordPress core binaries as “cleanup”
- DB demo content rows (content charter, not file inventory)

---

## 8. Advisory conclusion

Cleanup can recover **multiple GB** primarily from: (1) superseded E54–E56 full checkpoints, (2) stale git-sync worktrees, (3) optionally mid-size E59/E61 checkpoints after review, (4) logs.  
**Do not touch** Stable freeze, E63 pre-closeout backup, E58 freeze, or E53 freeze in the first pass.

---

## 9. Post-execution pointer (do not rewrite §1–8 measurements)

Actual cleanup execution (V9-06E64) results live under:

- `REPORTS/CLEANUP/` (inventories, allowlists, deletion log, validation)
- `REPORTS/REPORT-FP-0002-V9-06E64-SAFE-CLEANUP.md`
- Feedback: [CLEANUP-EXECUTION-FEEDBACK-FOR-PHASE-03.md](./CLEANUP-EXECUTION-FEEDBACK-FOR-PHASE-03.md)

Historical sizes in this pre-phase inventory remain as measured before cleanup.
