# REPORT — SITE-002 New Sections Wave A Onboarding Apply 01

## 1. Scope

Wave A applied only to the approved live target roots:

- `hlebopekarnoe-oborudovanie` (`category_id=186`)
- `holodilnoe-oborudovanie` (`category_id=95`)

No structural moves, no importer/mapping work, no baseline refresh, no monitor code changes, no product mutations.

## 2. Operator approval

Operator approval recorded as:

`Ок, давай промт, я согласен`

Interpretation honored:

- proceed with Wave A apply;
- touch only already-live sections with products;
- do not perform DB parent/category placement moves;
- do not refresh monitor baseline;
- do not touch `barnoe`, `posuda`, or `upakovochnoe` apply scope.

## 3. Client Ops boundary

Client Ops, n8n, Telegram, reporting bridge, and unrelated MARS cleanup flows were not touched.

## 4. Preflight

Authority worktree:

`X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`

Verified before any mutation:

- `Get-Location` resolved inside approved `X:\AI MARS STORAGE`
- `Get-Volume -DriveLetter X` returned label `AI WS`
- branch: `docs/site002-offers-recovery-healthcheck-03` (task-authorized worktree)
- `git status --short` clean
- `HEAD` = `origin/mars/canonical-post-recovery` = `296dcdaa`
- no staged changes
- no unpushed commits

Storage evidence:

- `preflight/git-state.txt`
- `preflight/origin-state.txt`

## 5. Current state / charter basis

Authoritative upstream inputs for this apply:

- charter: `SITE-002-PROD-NEW-SECTIONS-ONBOARDING-PLACEMENT-CHARTER-01`
- healthcheck: `SITE-002-PROD-POST-1C-OFFERS-RECOVERY-AND-NEW-SECTIONS-HEALTHCHECK-01`

Accepted strategy remained:

`KEEP_DB_PLACEMENT_AND_SEPARATE_UI_FROM_STRUCTURE`

Baseline remained blocked:

`DO_NOT_REFRESH_BASELINE_YET`

## 6. Production read-only before

### Target categories

`hlebopekarnoe-oborudovanie` (`186`)

- root, `parent_id=0`, `status=1`
- image: `catalog/Category-image/khlebopekarnoe-oborudovanie.webp` (`HTTP 200`)
- `meta_title`: `Хлебопекарное оборудование | ООО «ЗПМ»`
- `meta_description`: present, already acceptable
- `description`: empty
- `seo_keyword`: `hlebopekarnoe-oborudovanie`
- subtree products: `12`
- enabled subtree products: `12`
- public URL `200`
- sitemap present
- public title/H1 already correct

`holodilnoe-oborudovanie` (`95`)

- root, `parent_id=0`, `status=1`
- image: `catalog/Category-image/kholodilno-oborudovanie.webp` (`HTTP 200`)
- `meta_title`: `Холодильное оборудование | ООО «ЗПМ»`
- `meta_description`: thin and overly broad for a branch with `1` enabled product
- `description`: empty
- `seo_keyword`: `holodilnoe-oborudovanie`
- direct products: `1`
- subtree products: `1`
- enabled subtree products: `1`
- public URL `200`
- sitemap present
- representative PDP remained `200`

### Forbidden control state

- `barnoe-oborudovanie` (`171`): live `200`, subtree products `0`, untouched
- `posuda-i-inventar` (`364`): still `parent_id=362`, live `200`, untouched
- `upakovochnoe-oborudovanie`: public `404`, absent from sitemap, not created

Storage evidence:

- `production-readonly-before/target-category-before.csv`
- `production-readonly-before/forbidden-category-before.csv`
- `category-state-before/*.md`

## 7. Content plan

Wave A content decisions:

- `186` title kept as-is
- `186` meta description kept as-is
- `186` intro/description added because page-level description was empty
- `95` title kept as-is
- `95` meta description replaced with more conservative wording matching a 1-product branch
- `95` intro/description added because page-level description was empty
- H1/name unchanged for both categories

Applied copy respected public brand `ЗПМ` and avoided unsupported claims.

Storage evidence:

- `content-plan/content-plan.md`
- `content-plan/category-content-before-after.csv`

## 8. Image plan

No image mutation was required.

Findings:

- `186` image already present and `200`
- `95` image already present and `200`
- no placeholder signal from filename heuristic
- no new generation or FTP upload performed

Storage evidence:

- `image-plan/image-plan.md`
- `image-plan/image-before-after.csv`

## 9. Navigation plan

Navigation/source decision:

`NO_CHANGE`

Reason:

- charter explicitly separates live URL existence from entrypoint promotion;
- Wave A does not require automatic promotion of `hlebopekarnoe` or `holodilnoe` into home `/`, `/katalog/`, or mega menu;
- `barnoe` must remain non-promoted while empty;
- `posuda` placement remains a later decision;
- `upakovochnoe` remains absent.

Storage evidence:

- `navigation-plan/navigation-plan.md`
- `navigation-plan/navigation-before-after.csv`

## 10. Rollback prep

Rollback prepared before apply:

- exact `oc_category_description` row snapshots for categories `186` and `95`
- no file rollback required because no FTP/source mutation was planned

Storage evidence:

- `rollback/db-before-target-categories.sql`
- `rollback/file-before-manifest.csv`
- `rollback/rollback-plan.md`

## 11. Production apply

Actual mutation scope was narrower than the plan:

- category `186`: `description` only
- category `95`: `meta_description` and `description`

No changes to:

- `parent_id`
- `name`
- `meta_title`
- `seo_keyword`
- image bindings
- products
- category relations
- importer or mapping layers
- source templates

SQL apply evidence:

- `production-apply/db-apply.sql`
- `production-apply/apply-summary.md`

Classification:

`WAVE_A_ONBOARDING_COMPLETE`

## 12. Cache handling

Cache action:

`NO_CACHE_CLEAR`

Rationale:

- metadata changes appeared live without cache intervention;
- no `storage/modification` wipe;
- no OCMOD refresh.

Storage evidence:

- `cache/cache-actions.csv`
- `cache/cache-summary.md`

## 13. Production read-only after

Target verification after apply:

- `/hlebopekarnoe-oborudovanie` → `200`
- `/holodilnoe-oborudovanie` → `200`
- `/` → `200`
- `/katalog/` → `200`

Public checks:

- no public `БЗПМ`
- no literal `\n`
- no PHP Notice/Warning/Fatal markers
- target pages still indexable and present in sitemap

After-state delta:

- `186` description added
- `95` meta description changed
- `95` description added
- no parent/status drift

Storage evidence:

- `production-readonly-after/target-category-after.csv`
- `production-readonly-after/forbidden-category-after.csv`
- `public-http/public-smoke.csv`
- `public-http/public-http-summary.md`

## 14. Sitemap check

Live sitemap after apply:

- HTTP `200`
- valid XML
- URL count `1887`
- `/hlebopekarnoe-oborudovanie` present
- `/holodilnoe-oborudovanie` present
- `/upakovochnoe-oborudovanie` absent

Baseline refresh was not performed.

Storage evidence:

- `sitemap/sitemap-after-summary.md`
- `sitemap/target-url-sitemap-check.csv`

## 15. Forms smoke

Read-only regression checks passed:

- home contains dialog `7`
- `/katalog/` contains dialog `7`
- live `main.js` reachable: `200`
- spam guard markers present:
  - `zpm_hp`
  - `zpm_ft`
  - `new FormData(form)`

Storage evidence:

- `forms-smoke/forms-smoke-summary.md`

## 16. Regression / mutation summary

Verified:

- no parent moves
- no category create/delete
- no product changes
- no importer changes
- no mapping table changes
- no monitor changes
- no baseline refresh
- `barnoe` untouched
- `posuda` still under `362`
- `upakovochnoe` still absent/404
- protected header/footer untouched

Storage evidence:

- `regression/regression-check.csv`
- `regression/mutation-summary.csv`
- `regression/regression-summary.md`

## 17. Git/worktree summary

Authority worktree remained clean before repo doc edits.

Planned commit scope:

- this report
- OCPilot state/index updates
- SITE-002 profile/passport/knowledge/tools README documentation sync

No storage artifacts, secrets, raw DB dumps, or external logs are committed.

## 18. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-A-ONBOARDING-APPLY-01\`

Key subfolders created:

- `preflight`
- `reports-read`
- `production-readonly-before`
- `content-plan`
- `image-plan`
- `navigation-plan`
- `production-apply`
- `cache`
- `production-readonly-after`
- `public-http`
- `sitemap`
- `forms-smoke`
- `regression`
- `rollback`
- `decision`

## 19. SAFE UNKNOWN / blockers

- SAFE UNKNOWN: visual quality beyond HTTP presence of category images was not escalated to a new generation/upload wave because both target images already existed and the categories were not promoted into curated entrypoints in Wave A
- SAFE UNKNOWN: public PLP product snippet extraction from sampled HTML remained limited; product counts were verified from DB and page HTTP state
- blocker remains: monitor artifact semantics (`NO_ACTION_REQUIRED` vs `ONBOARDING_REQUIRED`) still need a dedicated diagnostic wave before any baseline decision

## 20. Final verdict

`SITE-002 NEW SECTIONS WAVE A ONBOARDING COMPLETE — ХЛЕБОПЕКАРНОЕ AND ХОЛОДИЛЬНОЕ VERIFIED, BASELINE STILL BLOCKED`

## 21. Next recommendation

1. Open **Wave B** mapping charter for proven identity work without structural guesswork.
2. Open **Wave C** monitor diagnostic to reconcile artifact semantics.
3. Keep baseline refresh blocked until Waves A/B/C are accepted.

## Execution safety
- cwd: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- scope lock honored: yes
- destructive ops: none
- protected zone touch: none
