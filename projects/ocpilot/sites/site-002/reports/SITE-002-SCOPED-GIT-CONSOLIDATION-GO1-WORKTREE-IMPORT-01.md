# SITE-002-SCOPED-GIT-CONSOLIDATION-GO1-WORKTREE-IMPORT-01

**Verdict:** SITE-002 SCOPED GIT CONSOLIDATION GO1 COMPLETE — READY FOR OPERATOR GO2

**Date:** 2026-09-07  
**Operation ID:** SITE-002-SCOPED-GIT-CONSOLIDATION-GO1-WORKTREE-IMPORT-01  
**Site:** SITE-002 / ЗПМ Production  

---

## 1. Scope

GO-1 only: create unique clean worktree from `origin/mars/canonical-post-recovery`, import accepted SITE-002 allowlist, validate, produce GO-2 readiness package. No commit, no push, no production/DB/FTP/cache writes.

## 2. Operator GO

Operator authorized **GO-1 only**. GO-2 commit and GO-3 push require separate confirmations.

## 3. No-commit / no-push boundary

| action | performed |
|---|---|
| commit | **NO** |
| push | **NO** |
| production write | **NO** |
| DB write | **NO** |
| FTP write | **NO** |
| cache clear | **NO** |
| dirty-main pull/reset/clean/stash/restore | **NO** |
| `git add .` / `-A` / `commit -a` | **NO** |

## 4. Clean worktree created

| field | value |
|---|---|
| Path | `X:\AI MARS STORAGE\git-sync-site002-m9-pdp-consolidation-20260907-212425\repo` |
| Base | `origin/mars/canonical-post-recovery` |
| HEAD | `131882bdfdcfc4e11ad68b32f133201e66b17407` (detached) |
| Create command | `git worktree add --detach "<path>\repo" origin/mars/canonical-post-recovery` |
| Pre-import status | clean |

Dirty main (untouched for Git mutation):

| field | value |
|---|---|
| Root | `X:\AI MARS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `8b26b07a65a4e7b45f029f78dd9bd781163feb46` |

## 5. Source file resolution

Priority applied: dirty-main accepted WC → Storage payload. Live FTP GET not required.

| path | source | note |
|---|---|---|
| filter_profiles/86_stellazhi.php | dirty-main | SHA8 `69ed7773` |
| filter_profiles/301_stoly.php | dirty-main | SHA8 `df7233ea` |
| filter_profiles/331_polki.php | dirty-main | SHA8 `ab301a5c` |
| filter_profiles/186_hlebopekarnoe.php | dirty-main | SHA8 `e4863b92` |
| filter_profile_resolver.php | dirty-main LF WC | registrations 86/301/331/186 |
| product_hero_specs_resolver.php | Storage HLEBOPEKARNOE-186 payload | 4309 bytes, SHA8 `19c9bc82` |
| 9 report markdown files | dirty-main | accepted reports |
| product.php | **DEFERRED** | not imported |

Evidence: `source-files/source-file-resolution.csv`

## 6. Imported files

**15 files** copied into clean worktree (no staging):

### Profiles + resolvers
1. `.../filter_profiles/86_stellazhi.php` (new)
2. `.../filter_profiles/301_stoly.php` (modified vs origin)
3. `.../filter_profiles/331_polki.php` (new)
4. `.../filter_profiles/186_hlebopekarnoe.php` (new)
5. `.../filter_profile_resolver.php` (modified vs origin)
6. `.../product_hero_specs_resolver.php` (new)

### Reports (new)
7–15. Nine SITE-002 report markdown files from plan allowlist.

Evidence: `imported-files/imported-files.csv`

## 7. Resolver validation

**PASS**

- Contains `86_stellazhi.php`, `301_stoly.php`, `331_polki.php`, `186_hlebopekarnoe.php`
- `registered_branch_roots = array(80, 86, 207, 301, 322, 326, 331, 186)`
- No conflict markers
- PHP CLI not available in environment (`php_not_found`); content inspection used

## 8. Product hero resolver validation

**PASS**

- Exists at repo mirror path under SITE-002 patch
- Bytes `4309`, SHA8 `19c9bc82`
- Family maps for `86` (shelving) and `186` (bakery)
- Accepted Storage payload; bakery comment labels abbreviated vs charter wording but payload accepted
- No secrets / conflict markers

## 9. Product.php review

**PRODUCT_PHP_IMPORT_DEFERRED_NEEDS_OPERATOR_REVIEW**

- Not imported in GO-1
- Storage STELLAZHI-86 payload exists
- Exact dirty-main mirror path / accepted delta not fully established for safe GO-1 include
- Recommendation: leave deferred until operator confirms include for GO-2

## 10. Reports import

**PASS** — all 9 plan report files present in clean worktree as untracked new files.

## 11. Diff review

Clean worktree after import (allowlist only):

- **Modified (tracked):** filter_profile_resolver.php, 301_stoly.php
- **Untracked (new):** 86/331/186 profiles, product_hero_specs_resolver.php, 9 reports
- Classification: **EXPECTED=15**, **FORBIDDEN=0**, **SUSPICIOUS=0**
- Note: large net-line reduction on resolver vs origin is expected consolidation toward accepted WC; functional registrations verified present
- CRLF warning on resolver working copy (Windows)

Evidence under `diff-review/`.

## 12. GO-2 readiness

**READY FOR OPERATOR GO-2** (with product.php deferred).

Package:

- `operator-go2/go2-readiness.md`
- `operator-go2/go2-exact-add-commands.txt`
- `operator-go2/go2-commit-message-options.md` (prefer split Option B)
- `operator-go2/go2-deferred-files.md`
- `operator-go2/go2-forbidden-files.md`

## 13. Deferred files

- `product.php` — PRODUCT_PHP_IMPORT_DEFERRED_NEEDS_OPERATOR_REVIEW

## 14. Forbidden files

Foreign WIP, secrets, Storage evidence trees, backups, runtime checkouts, cache files — excluded. No forbidden paths in clean worktree diff.

## 15. Risks

See `risk-register/go1-risk-register.md`. Key open items: local dirty main ~290 ahead of origin not included in this worktree; GO-3 push conflict review required later.

## 16. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-SCOPED-GIT-CONSOLIDATION-GO1-WORKTREE-IMPORT-01\`

Subfolders: preflight, worktree, source-files, imported-files, resolver-validation, product-hero-resolver, product-php-review, reports-import, diff-review, git-clean-worktree, operator-go2, risk-register, reports, logs, manifests.

## 17. Final verdict

**SITE-002 SCOPED GIT CONSOLIDATION GO1 COMPLETE — READY FOR OPERATOR GO2**

Next operator choice:

1. **GO-2** — authorize selective stage + commit in clean worktree only (confirm whether to include deferred `product.php`)
2. Hold — review deferred product.php / resolver CRLF before commit
3. Do **not** push until separate **GO-3**
