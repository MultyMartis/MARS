# REPORT — SITE-002-POLKI-PDP-HERO-SPECS-GO1-BUILD-01

**Final verdict:** `SITE-002 POLKI PDP HERO SPECS GO1 BUILD COMPLETE — READY FOR OPERATOR GO2`

**Date:** 2026-09-08  
**Timestamp:** 2026-09-08 20:11:54 +07:00 (operation start)  
**Site:** SITE-002 / ЗПМ Production / https://bzpm.ru/  
**Target:** category `[331]` — Полки (PDP hero specs family mapping)  
**Operation:** `SITE-002-POLKI-PDP-HERO-SPECS-GO1-BUILD-01`  
**Environment:** `POLKI_PDP_HERO_SPECS_GO1_BUILD_NO_DEPLOY_NO_COMMIT`

---

## 1. Scope

GO-1 build/validate only: add `[331]` Полки family mapping to `ProductHeroSpecsResolver` in a **clean git-sync worktree** based on canonical remote `origin/mars/canonical-post-recovery` @ `36c98686cd6b914571bb5d5238148632cbc0c384`.

Authorized:

- create unique clean worktree
- edit one resolver file
- PHP lint
- Git diff/status inside the worktree
- HTTP GET current public PDPs (read-only baseline)
- Storage evidence + untracked worktree report

Not authorized and **not performed:**

- production deploy / FTP PUT
- DB write
- cache clear
- commit
- push
- dirty-main Git mutation
- L/W/H slider changes
- `product.php` / Twig / JS / category / M9 profile / `global_hidden.php` edits

---

## 2. Model routing

| Item | Value |
|------|--------|
| Required | Cursor Composer / Grok only |
| Used | Cursor Composer / Grok (`cursor-grok-4.6`) |
| Other / premium / deep-reasoning models | **not used** |
| Unnecessary model switching | **none** |

This was a small scoped PHP resolver change. Routing matches the charter.

---

## 3. Operator decision

Operator selected **D**: defer L/W/H sliders; do `[331]` Polki PDP hero specs only.

Prior plan: `SITE-002-FILTER-SLIDERS-AND-POLKI-PDP-READONLY-PLAN-01`.

Sliders remain isolated (`oc_product.length/width/height` via `filterssidebar.twig`, `category.php` `len_`/`w_`/`h_`, `getCategoryPhysicalLimits()`, theme `[data-range]` JS). **Not touched.**

---

## 4. No-deploy / no-commit boundary

| Gate | Allowed | Actual |
|------|---------|--------|
| Production write | false | **none** |
| FTP write | false | **none** |
| DB write | false | **none** |
| Cache clear | false | **none** |
| Deploy | false | **none** |
| Commit | false | **none** |
| Push | false | **none** |
| Dirty-main Git | false | **untouched** (HEAD still `c47d733975ec1c673d90c4de374cf53dbd6f189a`, pre-existing foreign WIP) |
| Slider changes | false | **none** |
| product.php changes | false | **none** |
| Twig changes | false | **none** |

Dirty main remains diverged from canonical remote and was **not** used as the edit base.

---

## 5. Worktree

| Item | Value |
|------|--------|
| Path | `X:\AI MARS STORAGE\git-sync-site002-polki-pdp-hero-specs-20260908-201154\repo` |
| Created from | `origin/mars/canonical-post-recovery` |
| HEAD | `36c98686cd6b914571bb5d5238148632cbc0c384` (detached) |
| Matches expected remote tip | **yes** |
| Dirty main used | **no** |

Evidence: `worktree/worktree-create-command.txt`, `worktree/worktree-create-result.txt`, `worktree/git-head-before-edit.txt`, `worktree/git-status-before-edit.txt`.

Before edit: clean tree at canonical tip. After patch: one modified resolver file. After this report: that modification plus **untracked** GO-1 report (not committed).

---

## 6. Resolver analysis

Canonical `product.php` already loads `ProductHeroSpecsResolver` and calls `resolveAttributeIds($product_id, $path_category_id)` generically. Adding a family in the resolver is sufficient; **no product.php change required**.

Pre-patch architecture:

| Constant / family | IDs |
|-------------------|-----|
| `FAMILY_ROOT_STELLAZHI = 86` | `21, 114, 122, 26, 33` |
| `FAMILY_ROOT_HLEBOPEKARNOE = 186` | `127, 135, 134, 130, 129, 128, 132, 137` |
| Fallback | `SUPER_ATTS` (typically `21` Конструкция, sometimes `115` Усиление) |

Ancestry: path category under branch root via `isUnderBranchRoot` / `oc_category_path`, else `product_to_category` ∩ `category_path`. Empty attribute values are skipped by the existing product.php/Twig pipeline, not by the resolver returning IDs.

Evidence: `resolver-analysis/current-resolver-architecture.md`, `resolver-analysis/current-mapping-summary.md`.

---

## 7. Patch summary

**Edited file (worktree only):**

`projects/ocpilot/sites/site-002/m9-phase3-remaining-work/patch/system/library/zpm/product_hero_specs_resolver.php`

Implementation:

- `FAMILY_ROOT_POLKI = 331`
- `isPolkiProduct` (same ancestry pattern as shelving/bakery)
- `$family_attr_map[331] => array(51, 112, 21, 122, 26, 123, 115)`
- Resolve order: `[86]` → `[186]` → **`[331]`** → `SUPER_ATTS`
- `[86]` and `[186]` maps **unchanged**
- `114` **omitted** from `[331]` only (still present on `[86]`)
- Dimensions/mass logic **unchanged** (not in this file)

After SHA256: `B518AFAB998CD13DC50D7DE5B9A6B492F06E4275F9B9569622DAC038963AFBB4`

Evidence: `patch/patch-summary.md`, `patch/target-file-after-sha.txt`.

---

## 8. Validation

| Check | Result |
|-------|--------|
| PHP lint (`php-7.4.33-p02 php.exe -l`) | **No syntax errors detected** |
| Conflict markers | **none** |
| Secrets | **none** |
| `[86]` mapping present | `21, 114, 122, 26, 33` |
| `[186]` mapping present | `127, 135, 134, 130, 129, 128, 132, 137` |
| `[331]` mapping present | `51, 112, 21, 122, 26, 123, 115` |
| Planned IDs exact order | **yes** |
| Omit `114` on `[331]` | **yes** |
| product.php unchanged | **yes** |
| Slider-related files unchanged | **yes** |
| Twig / JS / category / M9 profiles unchanged | **yes** |

Evidence: `validation/php-lint.txt`, `validation/mapping-validation.md`, `validation/no-forbidden-file-change.md`, `validation/secret-conflict-scan.md`.

---

## 9. Diff review

Inside clean worktree:

| Command | Result |
|---------|--------|
| `git status --short` | `M` resolver only (plus later untracked GO-1 report) |
| `git diff --name-status` | one modified PHP file |
| `git diff --stat` | 41 insertions / 2 deletions (resolver) |
| `git diff --check` | empty (no whitespace errors) |

**Not in diff:** `product.php`, sliders, Twig, JS, `category.php`, M9 profiles, `global_hidden.php`.

Evidence: `diff-review/`.

---

## 10. Current public baseline

HTTP GET only. **No deploy.** Live `[331]` PDPs still use SUPER_ATTS fallback.

| n | kind | HTTP | PHP warn | public БЗПМ | hero | Характеристики |
|---|------|------|----------|-------------|------|----------------|
| 1 | polki | 200 | no | no | yes | yes |
| 2 | polki | 200 | no | no | yes | yes |
| 3 | polki | 200 | no | no | yes | yes |
| 4 | reg-86 | 200 | no | no | yes | yes |
| 5 | reg-186 | 200 | no | no | yes | yes |
| 6 | reg-186 | 200 | no | no | yes | yes |

Pre-deploy `[331]` hero (after L/W/H/mass):

- sample 1: Конструкция + Усиление (`21`, `115`)
- sample 2: Конструкция only (`21`)
- sample 3: Конструкция + Усиление (`21`, `115`)

Missing from hero when present in lower Характеристики (as planned): `51`, `112`, `122`, `123`.

Trap URL **not used as PDP:** `/katalog/.../polka-nastennaya-pn-p-9-3-900h300h220` (HTTP 200 PLP trap).

Evidence: `public-http/current-public-baseline.csv`, `public-http/current-public-baseline-summary.md`.

---

## 11. GO-2 readiness

**Recommended sequence (production validate first):**

1. **GO-2** — deploy **one** PHP file to production: `/public_html/system/library/zpm/product_hero_specs_resolver.php` from this worktree. No Git commit/push. Narrow cache clear only if required. **Avoid OCMOD modification cache** unless required (admin topbar button risk).
2. **GO-3** — after production PASS, commit **from this clean worktree** (not dirty main).
3. **GO-4** — push that commit.

If project policy prefers Git-before-deploy: commit from this worktree first, then GO-2 deploy the same file. Dirty main must still not be the commit source.

`product.php` needed for GO-2: **NO**  
Sliders touched: **NO**

Evidence: `operator-go2/go2-readiness.md`, `operator-go2/go2-deploy-plan.md`, `operator-go2/go2-verification-urls.txt`, `operator-go2/go2-risk-summary.md`.

---

## 12. Risks

- One resolver file only; production still needs explicit GO-2.
- `[86]` / `[186]` regression required after deploy.
- Empty values already skipped; `115` remains optional if empty.
- Dirty main remains diverged; do not commit from it.
- Narrow cache only if required; avoid modification cache unless required.
- Sliders deferred; not in this change.

Evidence: `risk-register/risk-register.md`.

---

## 13. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-POLKI-PDP-HERO-SPECS-GO1-BUILD-01\`

Includes: `manifests/operation.json`, `preflight/`, `worktree/`, `resolver-analysis/`, `patch/`, `validation/`, `diff-review/`, `public-http/`, `operator-go2/`, `risk-register/`, `reports/`, `logs/`.

Worktree report (untracked, not committed):

`X:\AI MARS STORAGE\git-sync-site002-polki-pdp-hero-specs-20260908-201154\repo\projects\ocpilot\sites\site-002\reports\SITE-002-POLKI-PDP-HERO-SPECS-GO1-BUILD-01.md`

---

## 14. Final verdict

**SITE-002 POLKI PDP HERO SPECS GO1 BUILD COMPLETE — READY FOR OPERATOR GO2**

Answers to primary questions:

1. Clean worktree created from canonical remote `36c98686…`? **Yes.**
2. Only `product_hero_specs_resolver.php` edited (plus untracked report)? **Yes.**
3. Sliders untouched? **Yes.**
4. product.php untouched? **Yes.**
5. Twig/DB/M9 profile files untouched? **Yes.**
6. Resolver supports `[331]` Polki family? **Yes.**
7. Proposed IDs exact (`51, 112, 21, 122, 26, 123, 115`; omit `114`)? **Yes.**
8. PHP lint pass? **Yes.**
9. GO-2 production deploy safe later (one file, after operator GO)? **Yes — ready for operator GO-2, not executed.**
10. GO-2 commit/deploy plan ready? **Yes** (deploy-first then GO-3 commit from this worktree).

**Next operator choice:** authorize GO-2 one-file production PUT; or Git-first commit from this worktree; or hold.
