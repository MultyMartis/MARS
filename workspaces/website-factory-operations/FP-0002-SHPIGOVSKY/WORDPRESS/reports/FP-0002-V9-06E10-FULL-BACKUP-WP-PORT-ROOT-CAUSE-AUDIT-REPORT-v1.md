# REPORT — FP-0002 V9-06E10 FULL BACKUP + WORDPRESS PORT ROOT CAUSE AUDIT

**Date:** 2026-07-07  
**HEAD note:** Required E9 `7559f1ac` is ancestor; actual HEAD `8764185d` (+1 governance commit after E9); local/remote synced 0/0

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 8764185dddea64686e519e8e4ca6d4b76fa31437
- Local short HEAD: 8764185d
- Remote HEAD: 8764185dddea64686e519e8e4ca6d4b76fa31437
- Remote short HEAD: 8764185d
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unrelated modified/untracked; not staged)
- Pre-existing staged files: none
- E9 ancestor check: PASS
- Result: PASS

## 2. Authorization and scope

- Operator authorization: V9-06E10 authorized
- Task mode: FULL BACKUP + FORENSIC AUDIT — NO REPAIR
- Full backup: YES
- DB writes: 0
- Source/theme changes: 0
- Project plugin changes: 0
- Third-party plugin changes: 0
- ACF JSON changes: 0
- Runtime delivery: NO
- Native content writes: 0
- Legal text writes: 0
- Reviews writes: 0
- Media uploads: 0
- Attachment creation: 0
- Menu writes: 0
- Privacy setting writes: 0
- Rewrite/permalink changes: NO
- Plugin install/update/delete: NO
- OCPilot writes: 0
- Documentation/evidence writes: YES
- Result: PASS

## 3. Full backup

| Backup component | Result | Path / notes |
|---|---|---|
| Git metadata | PASS | `X:\AI MARS STORAGE\backups\fp-0002-shpigovsky\v9-06e10-root-cause-pre-audit-20260706-212334\git-metadata.json` |
| Runtime theme | PASS | 589 files → `runtime/themes/shpigovsky/` |
| Runtime plugin shpigovsky-core | PASS | 20 files → `runtime/plugins/shpigovsky-core/` |
| MU-plugins | PASS | 1 file |
| Uploads inventory | PASS | 39 files metadata → `uploads-inventory.json` |
| wp-config metadata | PASS | secrets redacted → `wp-config-metadata.json` |
| DB dump mars_wp_fp0002 | PASS | 1,434,216 bytes → `database/mars_wp_fp0002.sql` (fallback with DB user after credential-less attempt) |
| Static V9 src hashes | PASS | 220 files → `static-v9-src-hashes.json` |
| Static V9 dist hashes | PASS | 501 files → `static-v9-dist-hashes.json` |
| Runtime screenshots | PASS | 5 routes → `validation/.../screenshots/runtime-*.png` |
| Static V9 screenshots | PASS | 5 routes → `validation/.../screenshots/static-v9-*.png` |
| Checksum manifest | PASS | `checksum-manifest.json` |
| Restore instructions | PASS | `RESTORE-INSTRUCTIONS.json` |

## 4. Operator screenshot diff analysis

| Area | Static V9 | WordPress current | Difference | Likely source |
|---|---|---|---|---|
| Section stack (alcohol leaf) | 18 main nav/section classes | 18 classes, same order | **No missing/extra sections at class level** | E10 DOM probe |
| Inner markup (specialists/reviews/comfort) | Service-leaf partials in static HTML | `template-parts/home/*` on alcohol stack | Pixel/layout drift despite class match | `alcohol-stack.php` |
| Program block | V9 fixture lorem + 4 image cards | Same fixture via `v9-static-content.php` | Operator may read lorem as "invented" | Static + WP both DEMO |
| Signs / FAQ copy | Static partial text | ACF seed or helper fallback | Possible text drift | D8-C + `service/signs.php` |
| Hero image/copy | Static hero block | ACF hero_media + fallbacks | Source mix | E7B seed + `inner-hero.php` |
| Operator PNGs | `вёрстка.png` | `Вордпресс.png` | Not in local workspace | Web-GPT chat only |

## 5. Static V9 authority trace audit

| Route | Static V9 source | WP template/partials | Authority status | Notes |
|---|---|---|---|---|
| `/` | index.html | front-page.php + home/* | ADAPTED_V9 | D9-D 19-section orchestration |
| `/uslugi/` | uslugi-v2.html | services-hub.php | SEMANTIC_REBUILD | CPT-driven groups |
| `/uslugi/zavisimosti/` | usluga-podrazdel-v1.html | subdivision-stack.php | ADAPTED_PARTIAL | Home partial reuse |
| `/uslugi/.../lechenie-alkogolnoy-zavisimosti/` | usluga-konechnaya-v1.html | alcohol-stack.php | DOM_MATCH / VISUAL_DRIFT | E9 insufficient |
| `/kontakty/` | kontakty.html | contacts.php | ADAPTED_V9 | E8 layout repair |
| `/otzyvy/` | otzyvy.html | reviews.php | ADAPTED_V9 | D9-W archive layout |
| Legal | privacy/user/cookie/consent pages | legal.php + post_content | CONTENT_EXACT | E1 seeded copy |

## 6. Template partial provenance audit

| Partial | Used by | Provenance | Risk | Notes |
|---|---|---|---|---|
| service/leaf-stack.php | Generic leaf CPT | SEMANTIC_RECONSTRUCTION | high | 10 vs 17 static sections |
| service/alcohol-stack.php | Alcohol leaf | SEMANTIC_RECONSTRUCTION | medium | Correct order; home partials |
| home/specialists.php | Home + service | V9_ADAPTED_PARTIAL | medium | Shared across stacks |
| home/reviews.php | Home + service | V9_ADAPTED_PARTIAL | medium | Slider wrapper |
| service/program.php | Service routes | DEMO_FALLBACK | high | V9 lorem fixture |
| inc/v9-static-content.php | Hub + alcohol | DEMO_FALLBACK | high | PHP not HTML port |
| services-hub/service-groups.php | /uslugi/ | SEMANTIC_RECONSTRUCTION | medium | CPT not static includes |

## 7. Content source authority audit

| Route | Expected source | Current source | Drift risk | Notes |
|---|---|---|---|---|
| Alcohol leaf hero | static hero | ACF + inner-hero fallbacks | medium | E7B media seed |
| Alcohol intro/approach | static partials | v9-static-content.php | low | EXACT_V9 path for alcohol-special |
| Alcohol signs | static signs | ACF signs / fallback | high | D8-C may override |
| Alcohol reviews | static slider | OPTIONS fp02-reviews | medium | Admin-editable |
| /uslugi/ hub cards | static uslugi-v2 | v9-static-content + CPT | medium | Demo lorem on some slugs |
| Home FAQ | static faq | home-fallbacks demo text | high | D9-D transplant typo history |

## 8. Agent failure mode audit

| Failure mode | Evidence | Impact | Fix |
|---|---|---|---|
| Semantic rebuild as "V9 parity" | D7-D architecture | HIGH | Governance contract §2 |
| Probe-only PASS | E8 rejection; E9 DOM PASS vs operator drift | HIGH | Screenshot gate §4 |
| PARTIAL PASS normalization | E5/E6/E8 partial | MEDIUM | Hard FAIL on gap |
| Home partials on service pages | alcohol-stack.php | HIGH | Service-specific partials |
| Truncated leaf-stack | 10 vs 17 sections | HIGH | Align to static |
| No pre-repair section map | E9 alcohol-only | HIGH | E11 inventory |
| V6-centric SOURCE-AUTHORITY | SOURCE-AUTHORITY.md | MEDIUM | V9 HTML primacy rule |

## 9. Root cause matrix

| Root cause | Evidence | Severity | Recommended fix |
|---|---|---|---|
| No direct V9 HTML port | All routes PHP-orchestrated | CRITICAL | E11 + E12 strict replacement |
| D7-D semantic architecture | service-template-loader.php | HIGH | Governance ban |
| Home partial reuse | alcohol-stack.php | HIGH | Fork/parameterize |
| Probe-only false PASS | E10: classes match, operator sees drift | HIGH | Screenshot mandatory |
| Truncated leaf-stack | leaf-stack.php | HIGH | 17-section authority |
| ACF seed overrides | D8-C service #74 | MEDIUM | EXACT_V9 classification |

## 10. Static V9 WP port governance contract

Ten mandatory rules created — see `architecture/FP-0002-V9-06E10-STATIC-V9-WP-PORT-GOVERNANCE-CONTRACT-v1.md`. Core: static V9 HTML is primary authority; direct section-stack parity required; no PASS without screenshots; content classes EXACT_V9 | DEMO | OPERATOR | DEFERRED.

## 11. Proposed remediation plan

| Phase | Goal | Notes |
|---|---|---|
| E11 | Static-to-WP page contract inventory | All V9 routes; read-only |
| E12 | One-page strict V9 replacement | Start alcohol leaf |
| E13 | Stable checkpoint refresh | Screenshot parity required |

## 12. Screenshots / evidence

| Evidence | Captured | Result |
|---|---:|---|
| runtime-home.png | YES | PASS |
| runtime-uslugi-hub.png | YES | PASS |
| runtime-kontakty.png | YES | PASS |
| runtime-uslugi-zavisimosti-subdivision.png | YES | PASS |
| runtime-alcohol-leaf.png | YES | PASS |
| static-v9-home.png | YES | PASS |
| static-v9-uslugi-hub.png | YES | PASS |
| static-v9-kontakty.png | YES | PASS |
| static-v9-uslugi-zavisimosti-subdivision.png | YES | PASS |
| static-v9-alcohol-leaf.png | YES | PASS |
| operator v9-layout-reference | NO | Web-GPT only |
| operator wp-runtime-drift | NO | Web-GPT only |

## 13. No-scope-drift

- Backup performed: YES
- DB writes: 0
- Source/theme changes: 0
- Project plugin changes: 0
- Third-party plugin changes: 0
- ACF JSON changes: 0
- Runtime delivery: NO
- Native content writes: 0
- Legal text writes: 0
- Reviews writes: 0
- Media uploads: 0
- Attachment creation: 0
- Menu writes: 0
- Privacy setting writes: 0
- Rewrite flush: NO
- Plugin install/update/delete: NO
- OCPilot writes: 0
- V9 src/dist changes: 0
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Helpers/temp staged: NO
- Secrets staged: NO
- Result: PASS

## 14. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06E10-FULL-BACKUP-WP-PORT-ROOT-CAUSE-AUDIT-REPORT-v1.md | CREATE | Main audit report |
| architecture/FP-0002-V9-06E10-*.md (9 files) | CREATE | Audit deliverables |
| validation/v9-06e10-.../*.json (13 files) | CREATE | Machine evidence |
| validation/v9-06e10-.../screenshots/*.png (10) | CREATE | Visual evidence |
| WORDPRESS/README.md | UPDATE | E10 status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | E10 audit entry |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | UPDATE | E10 status |

## 15. Git checkpoint

- Exact staged files: E10 report, architecture docs, validation JSON, screenshots (not helper `_e10_runner.py`, not backup payload)
- Staged list inspected: pending
- Theme source files staged: NO
- Project plugin files staged: NO
- Third-party plugin files staged: NO
- ACF JSON staged: NO
- Runtime files staged: NO
- OCPilot files staged: NO
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Uploaded media files staged: NO
- Helper/temp files staged: NO
- Secrets staged: NO
- Commit: pending
- Commit hash: pending
- Push: pending
- Local HEAD: 8764185d (pre-commit)
- Remote HEAD: 8764185d (pre-commit)
- Result: pending

## 16. Final verdict

**PASS**

V9-06E10 Full Backup + WordPress Port Root Cause Audit: **COMPLETE**

Full backup: **PASS**

Root cause identified: **YES**

Static V9 authority trace: **COMPLETE**

Template provenance audit: **COMPLETE**

Content source authority audit: **COMPLETE**

Governance contract: **CREATED**

Remediation plan: **CREATED**

No-scope-drift: **PASS**

Recommended next phase: **E11 static-to-WP page contract inventory**

## 17. Recommended next action

**CREATE_V9_06E11_STATIC_TO_WP_PAGE_CONTRACT_INVENTORY_TASK**

## 18. Final safety statement

Target folder:
X:\AI MARS

V9-06E10 Full Backup + WordPress Port Root Cause Audit performed:
YES

Full backup:
PASS

DB writes:
0

Source/theme changes:
0

Project plugin changes:
0

Third-party plugin changes:
0

ACF JSON changes:
0

Runtime delivery:
NO

Native content writes:
0

Legal text writes:
0

Reviews writes:
0

Media uploads:
0

Attachment creation:
0

Menu writes:
0

Privacy setting writes:
0

Rewrite flush performed:
NO

OCPilot writes:
0

Production migration performed:
NO

V9 source changed:
NO

V9 dist changed:
NO

DB dump committed:
NO

Backup payload committed:
NO

Runtime snapshot committed:
NO

Helper/temp committed:
NO

Secrets committed:
0
