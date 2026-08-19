# REPORT — SITE-002 New Sections Onboarding and Placement Charter 01

## 1. Scope

- Operation: `SITE-002-PROD-NEW-SECTIONS-ONBOARDING-PLACEMENT-CHARTER-01`
- Mode: read-only classification and bounded apply planning
- Target site: `SITE-002` / ЗПМ Production
- Production URL: `https://bzpm.ru/`
- Working repo authority: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- Scope boundary: docs/report + Storage artifacts only
- Production mutation: forbidden in this run

## 2. Operator approval

Operator approved the next step:

`Ок, утверждаю. Жду промт.`

Interpretation used in this run:

- proceed with new sections onboarding / placement / importer mapping charter;
- do **not** execute production apply;
- do **not** refresh monitor baseline;
- produce explicit decision matrix and next safe apply plan.

## 3. Client Ops boundary

Untouched in this run:

- production DB writes: `0`
- production FTP writes: `0`
- import runs: `0`
- cache clear / OCMOD refresh: `0`
- category/product changes: `0`
- Client Ops / n8n / Telegram: `0`
- dirty main mutations: `0`
- `docs-01` / `docs-02`: `0`

## 4. Preflight

Worktree re-check before mutation:

- path: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- volume label: `AI WS`
- branch: `docs/site002-offers-recovery-healthcheck-03`
- repo top-level: `X:/AI MARS STORAGE/git-sync-site002-offers-recovery-docs-03/repo`
- `git status --short`: empty
- `git status --branch --porcelain=v2`: `branch.ab +0 -0`
- `HEAD`: `a8ce4b2bb5eca486cfcfc2dd04261de87274e549`
- `origin/mars/canonical-post-recovery`: `a8ce4b2bb5eca486cfcfc2dd04261de87274e549`
- `git fetch origin`: success

Decision:

`CLEAN_CANONICAL_WORKTREE_READY`

## 5. Current state after offers recovery

Latest natural import:

- TXT: `mars_1c_import_2026-08-19_080010.txt`
- Run ID: `mars-20260819-080002-61559c39`
- final status: `SUCCESS`
- catalog: `PASS` / `import0_1.xml` / `4.07s`
- offers: `PASS` / `offers0_1.xml` / `3.86s`
- total duration: `7.98s`

Recovered impact:

- total products: `1649`
- enabled: `1647`
- disabled: `2`
- `price > 0`: `1643`
- non-zero quantity: `537`

Sitemap / monitor:

- baseline: `1879`
- live sitemap count: `1887`
- delta: `+8`
- scheduled monitor run: `2026-08-19_12-30-05`
- `run-summary.json`: `NO_ACTION_REQUIRED`
- `monitor-classification.json`: `ONBOARDING_REQUIRED`

Effective monitor classification:

`MONITOR_ONBOARDING_REQUIRED`

## 6. Topology review

Latest XML top-level groups after the 1C fix:

1. `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`
2. `ПОСУДА И ИНВЕНТАРЬ`
3. `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ`
4. `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ`
5. `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ`

Comparison to prior placement forensic:

- Run 4.319 saw only Neutral + Tech as XML top-level groups.
- On 2026-08-19 XML expanded to five top-level groups.
- Public route space now contains live roots for `barnoe`, `hlebopekarnoe`, `holodilnoe`, `posuda`.
- `upakovochnoe-oborudovanie` is still XML-only from the site perspective.

Target category matrix summary:

| Target | XML top-level | DB/site state | Public URL | Sitemap | Key issue |
|---|---|---|---|---|---|
| `barnoe-oborudovanie` | no proof as XML top-level | root id `171`, descendants `15`, subtree products `0` | `200` | yes | live but empty |
| `hlebopekarnoe-oborudovanie` | no proof as XML top-level | root id `186`, descendants `17`, subtree products `12` | `200` | yes | live with products, needs onboarding |
| `holodilnoe-oborudovanie` | yes | root id `95`, subtree products `1` | `200` | yes | live with 1 product, needs onboarding |
| `posuda-i-inventar` | yes | id `364`, parent `362`, direct/enabled products `6` | `200` | yes | live child but XML top-level |
| `upakovochnoe-oborudovanie` | yes | confirmed DB category absent | `404` | no | XML-only |

Known mapping-layer evidence:

- `oc_mars_1c_category_map` exists and is active for `7` known tech GUID rows only.
- Known active mapped IDs: `362/373/375/376/378/379/380`.
- No evidence in current docs that `95`, `171`, `186`, `364`, or `upakovochnoe` have active GUID map rows.
- Importer Phase A keeps auto-create **disabled**.

## 7. Category decision matrix

### `barnoe-oborudovanie`

- classification: `LIVE_EMPTY_NEEDS_CONTENT_DECISION`
- state: live root + sitemap + descendants, subtree products `0`
- public behavior: empty PLP copy already present
- recommendation:
  - keep live URL and sitemap membership;
  - do **not** move category;
  - do **not** include in new navigation wave until products exist;
  - allow meta/H1/image quality pass only if operator wants the empty branch to stay visible as future-facing;
  - otherwise treat as `NEEDS_PRODUCT_WAIT`.

### `hlebopekarnoe-oborudovanie`

- classification: `LIVE_WITH_PRODUCTS_NEEDS_META_IMAGE_NAV_REVIEW`
- state: live root + sitemap + `12` subtree products
- public behavior: working PLP with products, generic title/H1, no proven category image/onboarding package
- recommendation:
  - onboard as a public live branch;
  - add/verify title, meta description, H1, category image, tile policy;
  - keep root placement for now;
  - do **not** change DB parent in this wave;
  - review possible overlap with older tech child `368` before adding it to home/mega.

### `holodilnoe-oborudovanie`

- classification: `LIVE_WITH_PRODUCTS_NEEDS_META_IMAGE_NAV_REVIEW`
- state: live root + sitemap + `1` subtree product
- public behavior: working PLP + working PDP, generic title/H1
- recommendation:
  - keep root placement;
  - onboard meta/image/H1/intro;
  - keep visible by direct URL and sitemap;
  - defer home/mega inclusion until operator confirms whether a 1-product root should be promoted.

### `posuda-i-inventar`

- classification: `LIVE_CHILD_NEEDS_PLACEMENT_DECISION`
- state: XML top-level, but DB child under Tech `362`
- public behavior: live products, direct root-like URL `/posuda-i-inventar`, and tech-child references still exist on home and `/katalog/`
- recommendation:
  - **do not move** in the first apply;
  - preserve DB placement under `362`;
  - separate presentation from structure;
  - backfill/verify importer mapping later if a stable top-level identity is approved;
  - treat current root-like URL behavior as a routing/SEO reality, not proof that DB reparent is required.

### `Упаковочное оборудование` / `upakovochnoe-oborudovanie`

- classification: `XML_ONLY_NEEDS_MAPPING_OR_IMPORTER_REVIEW`
- state: XML top-level present; confirmed live DB category absent; site `404`; sitemap absent
- recommendation:
  - do not create or move anything in onboarding wave A;
  - open mapping/apply wave only after XML GUID/path is confirmed and operator decides whether an empty category should exist before products;
  - current safest interpretation: importer auto-create is off, so XML presence alone is insufficient to materialize a category.

## 8. Placement review

Options evaluated:

### Option A — treat all five XML top-level groups as public site roots

- benefit: mirrors current XML topology
- risk: duplicates legacy/public structures, increases navigation churn, may create parallel branches (`hlebopekarnoe`, `posuda`) without importer identity cleanup
- verdict: **too aggressive**

### Option B — preserve current production taxonomy and only onboard missing metadata

- benefit: lowest DB risk, no structural moves
- risk: XML/site mismatch remains for `posuda`; some roots stay live but under-promoted
- verdict: **safe but incomplete alone**

### Option C — move `posuda-i-inventar` to root now

- benefit: aligns DB with current XML top-level
- risk: route/canonical regressions, importer ambiguity, breadcrumb/menu shifts, unnecessary structural mutation while current public URL already resolves
- verdict: **not recommended for first apply**

### Option D — keep DB placement, adjust presentation and mapping separately

- benefit: decouples UX onboarding from taxonomy surgery; easiest rollback; consistent with current Launch Mode roots `79` + `362`
- risk: requires explicit documentation that public route and DB parent are temporarily different concerns
- verdict: **recommended default safe option**

Recommended placement strategy:

`KEEP_DB_PLACEMENT_AND_SEPARATE_UI_FROM_STRUCTURE`

Implications:

- keep `95`, `171`, `186` as existing roots;
- keep `364` under `362` for now;
- treat `upakovochnoe` as XML-only pending mapping/apply;
- use mapping/backfill and onboarding waves before any parent move discussion.

## 9. Onboarding review

Onboarding candidates:

| Target | Candidate status | Needed work |
|---|---|---|
| `barnoe-oborudovanie` | `NEEDS_PRODUCT_WAIT` | title/meta/image review optional; empty-copy policy; hide from navigation for now |
| `hlebopekarnoe-oborudovanie` | `READY_FOR_META_IMAGE_ONBOARDING` | title, meta, H1, image, tile/nav decision |
| `holodilnoe-oborudovanie` | `READY_FOR_META_IMAGE_ONBOARDING` | title, meta, H1, image, small-branch promotion decision |
| `posuda-i-inventar` | `NEEDS_PLACEMENT_DECISION_FIRST` | decide whether UI should show child identity or root identity; then meta/image polish |
| `upakovochnoe-oborudovanie` | `NEEDS_IMPORTER_MAPPING_FIRST` | no onboarding before DB/site existence |

Common content gaps from public HTTP:

- category titles are mostly generic and thin;
- no evidence of bespoke intro copy for the new branches;
- `barnoe` empty-state copy exists and is acceptable as interim text;
- `posuda` page title currently lacks branding and looks weaker than other branches;
- `hlebopekarnoe` / `holodilnoe` H1 exists, but onboarding quality is still basic rather than curated.

## 10. Importer mapping review

Current importer rules carried forward:

1. resolve by `oc_mars_1c_category_map` GUID row if present;
2. fallback to path / full-path resolution;
3. collision guard blocks unsafe tech collisions;
4. auto-create is **disabled** in current Phase A.

Recommendations by target:

| Target | Mapping recommendation |
|---|---|
| `barnoe-oborudovanie` | `WAIT_1C_OR_OPERATOR_DECISION` |
| `hlebopekarnoe-oborudovanie` | backfill mapping only after XML GUID/path is proven for the root branch, because an older tech child `368` already exists |
| `holodilnoe-oborudovanie` | backfill mapping candidate if XML GUID/path confirms current root `95` |
| `posuda-i-inventar` | map to existing `364` without moving, if XML GUID/path proves that this category is the intended 1C target |
| `upakovochnoe-oborudovanie` | no mapping apply until DB category exists or a create-on-approval wave is authorized |

Why `Упаковочное оборудование` is in XML but absent from DB/site/sitemap:

- most likely cause: auto-create remains off in the importer;
- no proven GUID map row points to a DB category;
- no confirmed existing DB category/path matched the new XML branch safely;
- therefore the importer left it unresolved instead of creating it.

Classification:

`MAPPING_CHARTER_REQUIRED`

## 11. Navigation review

Current rules from code/docs:

- Launch Mode visible roots are `79` and `362`.
- home and `/katalog/` category blocks are driven by `category_visibility.php`.
- neutral and tech section tiles follow dedicated helper rules.
- mega menu parity is driven by `prepareMegamenuCategories()` / `buildHubChildCards()`.

Observed public navigation facts:

- `/` and `/katalog/` do **not** contain `barnoe`, `hlebopekarnoe-oborudovanie`, or `holodilnoe-oborudovanie`.
- `/` and `/katalog/` do contain links involving `posuda-i-inventar` and `tehnologicheskoe-oborudovanie/hlebopekarnoe`.
- this confirms that live URL existence and entrypoint inclusion are separate concerns.

Recommendations:

- home `/` and `/katalog/` should **not** auto-add the new root branches in the first onboarding wave;
- mega menu should stay scoped to current Launch Mode roots until operator approves a dedicated nav expansion;
- `barnoe` should stay hidden from home/katalog/mega while empty;
- `hlebopekarnoe` and `holodilnoe` may remain reachable by direct URL/sitemap but should not be promoted into primary entrypoints before the duplicate/placement review closes;
- `posuda` should remain represented through Tech navigation for now; separate first-level card promotion is a later UI decision, not a structural necessity.

## 12. Monitor review

Likely inconsistency cause:

- route normalization created massive string-level URL churn (`1873` added / `1865` removed) while the net count moved only `+8`;
- `run-summary.json` appears too optimistic for this scenario;
- `monitor-classification.json` correctly retains onboarding attention;
- onboarding count is probably inflated by canonical path replacement noise.

Recommendations:

1. separate monitor diagnostic/fix task;
2. do **not** trust `NO_ACTION_REQUIRED` until artifact semantics are reconciled;
3. keep baseline blocked during onboarding and placement decision window;
4. after approved apply waves and accepted canonical route policy, rerun monitor and only then consider baseline refresh.

Classification:

`MONITOR_DIAGNOSTIC_REQUIRED`

## 13. Sitemap / route normalization review

Accepted current observations:

- sitemap `1887` is operationally plausible;
- live count delta is small;
- root-level replacements such as `/barnoe-oborudovanie/...` vs old `/katalog/...` pattern look like canonical route normalization, not uncontrolled growth;
- `/assum` replacing `/brands/assum` deserves separate SEO/canonical review but is not blocked by this charter.

Proposed stance:

- treat route normalization as **accepted with review debt**;
- do not baseline-refresh yet;
- if redirects/canonicals for `/katalog/...` to root routes are incomplete, track that as a separate SEO hygiene task rather than blocking onboarding planning.

## 14. Public HTTP snapshot

Read-only HTTP result summary:

| URL | HTTP | Notes |
|---|---|---|
| `/barnoe-oborudovanie` | `200` | empty PLP + empty-state copy |
| `/hlebopekarnoe-oborudovanie` | `200` | `12` visible products, H1 present |
| `/holodilnoe-oborudovanie` | `200` | `1` visible product, H1 present |
| `/posuda-i-inventar` | `200` | `6` visible products, title weaker than other branches |
| `/upakovochnoe-oborudovanie` | `404` | not onboarded |

No sampled PHP errors or public `БЗПМ` regressions were observed in the target pages.

## 15. Future apply plan

### Wave A — new sections onboarding apply

Recommended scope:

- `hlebopekarnoe-oborudovanie`
- `holodilnoe-oborudovanie`
- optionally `barnoe-oborudovanie` metadata if operator wants empty branch polish
- `posuda-i-inventar` only after UI/placement wording is confirmed

Allowed actions in future wave:

- title / meta description / H1
- category image
- intro copy / empty copy normalization
- selective navigation visibility decisions

Explicitly exclude:

- DB reparent
- importer code
- new category create
- baseline refresh

### Wave B — importer mapping backfill / charter

- confirm XML GUID/path for the new roots;
- backfill safe rows to existing categories where identity is clear;
- keep auto-create off unless separately approved;
- decide whether `upakovochnoe` should be created only after products exist or as an empty announced branch.

### Wave C — monitor diagnostic / fix

- reconcile `run-summary.json` vs `monitor-classification.json`;
- reduce false onboarding inflation from route normalization;
- document authoritative classification source.

### Wave D — baseline refresh

Allow only when all are true:

1. operator accepts canonical route set;
2. onboarding wave outcome is stable;
3. mapping ambiguity for target set is reduced or explicitly accepted;
4. monitor artifacts classify consistently.

Current gate:

`DO_NOT_REFRESH_BASELINE_YET`

## 16. Docs update

This charter creates canonical documentation for:

- target category classifications;
- safe placement recommendation;
- onboarding candidate list;
- importer mapping review recommendation;
- monitor diagnostic need;
- baseline refresh gate.

No production apply was executed.

## 17. Decision

Classifications:

- `NEW_SECTIONS_CHARTER_COMPLETE`
- `PLACEMENT_DECISION_READY`
- `ONBOARDING_APPLY_READY`
- `MAPPING_CHARTER_REQUIRED`
- `MONITOR_DIAGNOSTIC_REQUIRED`
- `BASELINE_REFRESH_BLOCKED_PENDING_ONBOARDING`

Expected follow-up readiness:

- `READY_FOR_OPERATOR_REVIEW`
- `READY_FOR_ONBOARDING_APPLY_AFTER_APPROVAL`
- `READY_FOR_MAPPING_CHARTER_AFTER_APPROVAL`
- `READY_FOR_MONITOR_DIAGNOSTIC`
- `DO_NOT_REFRESH_BASELINE_YET`

## 18. Regression / mutation summary

Forbidden mutation classes in this charter:

| Mutation class | Count |
|---|---:|
| production DB writes | 0 |
| production FTP writes | 0 |
| import runs | 0 |
| cache clear / OCMOD refresh | 0 |
| source/code/template/JS/image changes | 0 |
| category/product changes | 0 |
| Client Ops / n8n / Telegram changes | 0 |
| dirty main changes | 0 |
| `docs-01` / `docs-02` touched | 0 |

Allowed changes only:

- repo docs/report updates;
- Storage artifacts for this charter.

## 19. Git/worktree summary

- worktree: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- branch: `docs/site002-offers-recovery-healthcheck-03`
- clean entry state: yes
- main repo `X:\AI MARS`: untouched
- stale worktrees `docs-01` / `docs-02`: untouched
- commit scope: docs/report only

## 20. Storage artifacts

Storage root for this charter:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-ONBOARDING-PLACEMENT-CHARTER-01\`

Contains:

- preflight
- reports-read
- topology-review
- category-decision-matrix
- placement-review
- onboarding-review
- importer-mapping-review
- navigation-review
- monitor-review
- sitemap-review
- public-http
- future-apply-plan
- docs-update
- decision
- regression
- reports
- manifests
- logs

## 21. SAFE UNKNOWN / blockers

- SAFE UNKNOWN: exact XML GUIDs for current root branches in this run; current charter relies on verified higher-level XML/DB/site evidence rather than a fresh GUID dump
- SAFE UNKNOWN: whether `barnoe` has a stable future 1C top-level identity or is a legacy/public-only shell
- SAFE UNKNOWN: whether `upakovochnoe` should be created before products exist
- blocker: baseline refresh remains blocked until onboarding and monitor semantics are accepted

## 22. Final verdict

`SITE-002 NEW SECTIONS ONBOARDING AND PLACEMENT CHARTER COMPLETE — APPLY WAVES READY, BASELINE REFRESH BLOCKED`

## 23. Next recommendation

1. Approve **Wave A** onboarding for `hlebopekarnoe-oborudovanie` and `holodilnoe-oborudovanie`, with `barnoe` optional and `posuda` gated by UI wording.
2. Approve **Wave B** mapping review/backfill for `holodilnoe`, `posuda`, and any proven new root GUIDs.
3. Open **Wave C** monitor diagnostic to reconcile artifact semantics before any baseline action.
4. Keep baseline refresh blocked until Waves A/B/C are accepted or the sitemap canonical set is explicitly approved as final.
