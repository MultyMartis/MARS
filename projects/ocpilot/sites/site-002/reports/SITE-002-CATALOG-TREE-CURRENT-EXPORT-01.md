# REPORT — SITE-002 Catalog Tree Current Export 01

## 1. Scope

`SITE-002-CATALOG-TREE-CURRENT-EXPORT-01` captured the actual SITE-002 Production catalog structure for operator review. Acquisition was read-only: Production DB `SELECT`, public HTTP `GET`, and live sitemap fetch. No Production apply or cleanup was authorized.

Capture window: `2026-08-24T14:16:27+07:00`–`2026-08-24T14:17:41+07:00`.

## 2. Operator request

The operator asked whether new sections appeared, and requested a concrete current catalog tree showing which sections exist and where they are nested. Cleanup of ZPM/MARS backups and tails is explicitly deferred to a separate future dry-run charter.

## 3. Client Ops boundary

Client Ops, n8n, Telegram configuration, scheduled tasks, runtime checkouts, importer code, monitor code, and baselines were out of scope and unchanged. Telegram is referenced only as accepted evidence from the preceding healthcheck.

## 4. Authority preflight

- authority worktree: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`;
- branch: `docs/site002-offers-recovery-healthcheck-03`;
- upstream: `origin/mars/canonical-post-recovery`;
- pre-edit HEAD and origin: `a2cae763e9b2b4e3d37ef59ef442364498581ade`;
- worktree clean; staged changes absent; ahead/behind `+0/-0`;
- authority had previously been safely fast-forwarded to canonical origin before this capture.

## 5. Current accepted state

The preceding accepted healthcheck is `SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01` (`f93eabf8`): monitor run `2026-08-24_12-30-03` exited `0`, returned `NO_ACTION_REQUIRED`, and held `1887 → 1887` with delta `0/0`. Natural 1C import `mars_1c_import_2026-08-24_080010.txt` completed successfully with catalog and offers. Mapping persistence for category `95` and `364` was confirmed.

## 6. Current sitemap

- live `/sitemap.xml`: HTTP `200`;
- URLs: `1887`, unique `1887`;
- `/katalog/` entries: `0`;
- `/brands/` entries: `0`;
- exact DB-category path matches: `225`;
- required present paths: `/holodilnoe-oborudovanie`, `/hlebopekarnoe-oborudovanie`, `/barnoe-oborudovanie`, `/tehnologicheskoe-oborudovanie/posuda-i-inventar`, `/assum`;
- absent from sitemap: `/posuda-i-inventar`, `/upakovochnoe-oborudovanie`, `/brands/assum`.

Comparison to the accepted 1887 URL baseline produced added `0`, removed `0`.

## 7. DB read-only catalog export

DB `oc_category.parent_id` is the hierarchy authority.

- all categories: `226`;
- active: `225`;
- inactive: `1`;
- root categories: `10`;
- maximum depth: `3`;
- active categories matched to sitemap: `225/225`;
- inactive DB-only category: `[96] Запчасти`, subtree products `76` total / `76` enabled, absent from sitemap, public HTTP `404`.

Each flat row records category/parent IDs, status, sort order, Russian name, meta title, slug, reconstructed full SEO path, DB name path, depth/root, direct and subtree product totals, enabled direct and subtree totals, timestamps, store binding, available mapping fields, sitemap membership, and sampled HTTP result.

## 8. Human-readable catalog tree

The complete untruncated DB-parent tree and flat CSV are committed beside this report:

- [SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-TREE.md](SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-TREE.md);
- [SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-FLAT.csv](SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-FLAT.csv).

Root summary:

| ID | Root | Status | Direct enabled/total | Subtree enabled/total | Sitemap | HTTP |
|---:|---|---:|---:|---:|---|---|
| 79 | Нейтральное оборудование | 1 | 0/0 | 1533/1535 | yes | 200 |
| 90 | Тепловое оборудование | 1 | 0/0 | 4/4 | yes | 200 |
| 93 | Инвентарь | 1 | 0/0 | 0/0 | yes | 200 |
| 95 | Холодильное оборудование | 1 | 1/1 | 1/1 | yes | 200 |
| 96 | Запчасти | 0 | 76/76 | 76/76 | no | 404 |
| 171 | Барное оборудование | 1 | 0/0 | 0/0 | yes | 200 |
| 186 | Хлебопекарное оборудование | 1 | 0/0 | 12/12 | yes | 200 |
| 205 | Посудомоечные машины | 1 | 0/0 | 0/0 | yes | 200 |
| 206 | Вентиляционное оборудование | 1 | 0/0 | 0/0 | yes | 200 |
| 362 | Технологическое оборудование | 1 | 0/0 | 21/21 | yes | 200 |

## 9. Public HTTP category smoke

Scope: all roots, every first-level child, and required control/open-item URLs.

- checked: `75`;
- HTTP 200: `73`;
- redirect: `0`;
- HTTP 404: `2`;
- unexpected: `0`.

The two 404 results were inactive `[96] Запчасти` and absent `/upakovochnoe-oborudovanie`. `/katalog/` is HTTP 200 but not in sitemap. The nested posuda URL is HTTP 200 and in sitemap. Flat `/posuda-i-inventar` also returns HTTP 200 but is not in sitemap and did not redirect; therefore the nested path is sitemap-canonical, while the flat path remains a live non-sitemap alias. `/brands/assum` returns HTTP 200 with title/H1 `Производители`; `/assum` returns HTTP 200 with Assum title/H1 and is in sitemap.

## 10. New section check

Classification:

- `NO_NEW_PUBLIC_SECTIONS_DETECTED`;
- `DB_ONLY_SECTIONS_DETECTED` — one existing inactive category, `[96] Запчасти`; this is not evidence of a newly created post-import section;
- `UPAKOVOCHNOE_STILL_ABSENT`.

Evidence:

- current/baseline sitemap URL counts: `1887/1887`;
- added/removed URL sets: `0/0`;
- active DB categories absent from sitemap: `0`;
- DB category IDs added versus the available older `2026-07-27` full snapshot: none;
- no post-import DB-only category creation is evidenced.

Critical observations stayed stable against the preceding healthcheck:

| ID | Category | Parent | Active | Total subtree now/prior | Enabled subtree now | Sitemap |
|---:|---|---:|---:|---:|---:|---|
| 95 | Холодильное оборудование | 0 | 1 | 1/1 | 1 | yes |
| 364 | Посуда и инвентарь | 362 | 1 | 6/6 | 6 | yes |
| 186 | Хлебопекарное оборудование | 0 | 1 | 12/12 | 12 | yes |
| 171 | Барное оборудование | 0 | 1 | 0/0 | 0 | yes |
| 79 | Нейтральное оборудование | 0 | 1 | 1535/1535 | 1533 | yes |
| 362 | Технологическое оборудование | 0 | 1 | 21/21 | 21 | yes |

The comparison proves stability for these accepted critical observations. Material product-count change across every one of the 226 categories is `SAFE UNKNOWN` because an equal-granularity immediately pre-import full-tree count snapshot was not available.

## 11. Open items review

1. `upakovochnoe`: absent from DB and sitemap; public 404.
2. Root `186` / `hlebopekarnoe`: active, subtree 12; root mapping identity remains a separate decision.
3. Root `171` / `barnoe`: active, subtree 0; current XML identity remains `SAFE UNKNOWN`.
4. docs-01/docs-02 cleanup: unchanged and deferred; neither worktree was touched.
5. D6G1A console-hide: unchanged and out of scope.
6. `/brands/assum`: HTTP 200 but resolves as generic `Производители`; canonical `/assum` is HTTP 200 and in sitemap.

## 12. Cleanup later note

No cleanup occurred. After today’s catalog work, create a separate destructive dry-run charter that inventories exact candidates including stale docs-01, stale/dirty docs-02, and known SITE-002 backup/tail paths. Large deployment artifacts remain evidence unless a later approved retention policy says otherwise. No delete, move, restore, stash, reset, or cleanup is allowed without exact paths, dry-run, checkpoint/backup, rollback method, and explicit operator approval.

## 13. Regression / mutation summary

Forbidden mutations: `0`.

- Production DB writes: 0;
- FTP writes: 0;
- import runs: 0;
- cache clear / OCMOD refresh: 0;
- category/product/mapping changes: 0;
- importer/monitor/baseline changes: 0;
- runtime/scheduler/Client Ops/n8n/Telegram changes: 0;
- cleanup/delete actions: 0;
- docs-01/docs-02 touches: 0.

Allowed writes were limited to this Storage evidence tree and the authorized repo documentation/export files.

## 14. Git/worktree summary

The authority worktree was clean and synchronized before repository edits. Only exact allowlisted documentation/export paths are eligible for staging. No broad Git command, dirty main mutation, runtime checkout mutation, baseline mutation, or foreign WIP handling is part of this operation.

## 15. Storage artifacts

Authority evidence:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-TREE-CURRENT-EXPORT-01\`

The directory contains preflight, report-read, sitemap, DB-readonly, full/active/public tree, HTTP smoke, delta, open-item, cleanup-later, regression, decision, manifest, and log artifacts. Raw credentials and DB dumps are not included.

## 16. SAFE UNKNOWN / blockers

- `barnoe` current 1C XML identity is not claimed without matching XML proof.
- Full-tree material product-count delta is unknown without an equal-granularity immediate pre-import snapshot.
- The flat `/posuda-i-inventar` HTTP 200 alias has no redirect; this export records current truth but does not decide routing remediation.

No blocker prevents catalog-tree review.

## 17. Final verdict

- `SITE_002_CATALOG_TREE_EXPORT_COMPLETE`
- `NO_NEW_PUBLIC_SECTIONS_DETECTED`
- `DB_ONLY_SECTIONS_DETECTED`
- `UPAKOVOCHNOE_STILL_ABSENT`
- `CATALOG_TREE_READY_FOR_REVIEW`
- `PRODUCTION_MUTATION_ZERO`

**SITE-002 CATALOG TREE CURRENT EXPORT COMPLETE — TREE READY FOR REVIEW, NO PRODUCTION MUTATIONS**

## 18. Next recommendation

Review the committed tree with the operator and decide the required category/UI work. After all catalog work today is complete, open a separate MARS cleanup dry-run for SITE-002/ZPM tails and backups; do not delete during catalog review.
