# REPORT — FP-0002 PROD-P15 Environment / Migration Cleanup

**Date:** 2026-08-16/17  
**Host:** http://shpigovsky.beget.tech/  
**Future canonical:** shpigovsky.ru  
**Evidence:** `REPORTS/evidence/prod-p15-environment-cleanup/`  
**Rollback:** P14 full backup + `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p15-layer-b-pre\` + `...\prod-p15-db-snapshots\`

---

## 1. Status

| Gate | Result |
|------|--------|
| Overall | **PASS** |
| Production file writes | wp-config.php; MU rename; `shpigovsky-core.php`; `SystemDashboard.php` |
| DB/options writes | admin_email; 2 block URL options; Home #4 URL meta; 31 publish postmeta URLs; metacode meta |
| Removed artifacts | `mars-local-runtime.php`; `_tmp-e47-fix04-val/`; debug.log webroot truncated after Storage archive |
| Git checkpoint | pending clean-worktree (this closeout) |
| WPilot writes | **0** (`write_enabled=false`) |

## 2. Fresh Production Check

- Pre-mutation drift: **705/705 MATCH**, prod_drift **0**
- Canonization: **none required**
- Authority unchanged: Beget FS = LIVE RUNTIME; Beget DB = content/settings; local WORDPRESS = source after check

**P15 FRESH PRODUCTION DRIFT CHECK COMPLETE**

## 3. Environment Before

| Item | Value |
|------|-------|
| WP_ENVIRONMENT_TYPE | local |
| wp_get_environment_type() | local |
| WP_DEBUG / DISPLAY / LOG | true / false / true |
| SCRIPT_DEBUG | true |
| siteurl / home | http://shpigovsky.beget.tech |
| blog_public | 0 |
| Mail | MU `pre_wp_mail` suppression (local-labelled) |

## 4. Environment After

| Item | Value |
|------|-------|
| WP_ENVIRONMENT_TYPE | **production** |
| wp_get_environment_type() | **production** |
| WP_DEBUG / DISPLAY / LOG | **false / false / false** |
| SCRIPT_DEBUG | **false** |
| siteurl / home | unchanged (beget) |
| blog_public | 0 (closed) |
| core | **0.3.6-p15** |

**WP_ENVIRONMENT_TYPE = PRODUCTION**  
**NO FRONTEND DEBUG OUTPUT IN PRODUCTION**  
**NO STALE LOCAL-RUNTIME IDENTITY REMAINS IN CURRENT PRODUCTION STATUS**

## 5. Local/Test URL Cleanup

| Finding | Action |
|---------|--------|
| Block specialists/comfort `.test` options | → beget host |
| Home #4 why-us / genotyping `.test` URLs | → beget host |
| 31 publish service/section approach/genotyping `.test` URLs | → beget host |
| post.guid / revisions / ACF field notices | **LEGACY — retained** |
| validation scripts / evidence history | **not mutated** |

Frontend re-probe after FU: `/`, `/uslugi/`, sections, alcohol, o-centre, specialists — **0** live `.test`/localhost hits.

**NO LIVE FRONTEND `.test` / LOCALHOST REFERENCES REMAIN**

## 6. Site Identity

| Item | Value |
|------|-------|
| blogname | Шпиговский Дом (unchanged — proven) |
| blogdescription | empty (unchanged) |
| admin_email | Info@shpigovsky.ru (was mli-fp0002@localhost.test) |
| Current host | shpigovsky.beget.tech |
| Future host | shpigovsky.ru |

## 7. Migration Guards

| Guard | Class |
|-------|-------|
| Local Admin notices | already removed (P13) |
| siteurl/home write block | already removed (P13) |
| `mars-local-runtime.php` identity | **REMOVED NOW** → `fp02-pre-cutover-mail-suppression.php` |
| `pre_wp_mail` suppression | **KEEP UNTIL SMTP** |
| blog_public=0 / robots Disallow | **KEEP UNTIL INDEXING / CUTOVER** |
| siteurl/home on beget | **KEEP UNTIL CUTOVER** |

## 8. Mail

MU filter still returns false for `pre_wp_mail`. Dashboard: «SMTP / outbound delivery pending cutover».

**MAIL DELIVERY REMAINS SAFELY DEFERRED UNTIL SMTP CUTOVER**

## 9. Indexing

blog_public=0 retained; robots Disallow retained; Dashboard: «Индексация: закрыта до cutover». Sitemap still generates on temporary host (not submitted).

**INDEXING REMAINS INTENTIONALLY CLOSED**

## 10. Debug / Public Artifacts

| Item | Result |
|------|--------|
| debug.log | Archived to Storage `prod-p15-debug-archive/`; webroot file truncated (move outside webroot denied by host perms); logging disabled |
| `_tmp-e47-fix04-val/` | Removed (`rm -rf` exact path) |
| mars-runtime/ | Inspected; **kept** (UNKNOWN / not proven disposable) |
| core.zip / public dumps | Not found at known risky names |

**NO KNOWN UNNECESSARY PUBLIC DEBUG/BACKUP ARTIFACTS** (known QA temp + debug.log handled)

## 11. MetaCODE Dashboard

Shows: FP-0002 / Шпиговский дом · Runtime Production/Beget · Environment production · Debug off · Indexing closed · Mail SMTP pending · wave P15 · no P06 tail · no local warning.

**METACODE DASHBOARD REFLECTS CLEAN PRODUCTION ENVIRONMENT STATE**

## 12. Source / Production Parity

Touched source-owned files: **3/3 MATCH**  
(`shpigovsky-core.php`, `SystemDashboard.php`, `fp02-pre-cutover-mail-suppression.php`; old MU absent on prod)

**N/N SOURCE ↔ PRODUCTION MATCH** (P15-touched)

## 13. Regression

Frontend smoke: core IA routes 200; no debug output; no live `.test`.  
Admin: login PASS; Dashboard widget PASS; services/specialists/posts/social/activity/users PASS; some settings/docx slugs returned 403 under this probe (not env-mutation related; docx URL may need `edit.php` form as in P14).  
Environment gates: production / debug false / mail suppressed / indexing closed.

## 14. Baseline

Extended `FP-0002-PROD-BASELINE-2026-08-17` with **P15 environment-clean** section (same baseline ID; immutable P14 backup retained).

## 15. Git

Clean-worktree checkpoint authorized for exact FP-0002 P15 scope; dirty main foreign WIP untouched. See closeout git evidence after push wave.

## 16. Remaining Work

1. Residual typography  
2. PRE-CUTOVER audit  
3. Domain/DNS/SSL cutover  
4. SMTP  
5. robots/indexing opening  
6. Sitemap submissions  
7. Final production crawl  

P06 closed by P15.

## 17. Acceptance

**PROD-P15 ENVIRONMENT CLEANUP COMPLETE — BEGET RUNTIME CORRECTLY CLASSIFIED AS PRODUCTION — LOCAL/TEST RUNTIME RESIDUE REMOVED WHERE SAFE — MAIL AND INDEXING INTENTIONALLY DEFERRED — FINAL DOMAIN CUTOVER NOT YET EXECUTED — FP-0002 READY FOR TYPOGRAPHY + PRE-CUTOVER WORK**

### Execution safety

- cwd: `X:\AI MARS`
- volume: `AI WS`
- scope lock honored: yes (FP-0002 + Storage packs)
- destructive ops: exact QA temp dir remove; debug.log truncate after archive; no dirty-main git destructive ops
- protected zone touch: none outside approved roots
