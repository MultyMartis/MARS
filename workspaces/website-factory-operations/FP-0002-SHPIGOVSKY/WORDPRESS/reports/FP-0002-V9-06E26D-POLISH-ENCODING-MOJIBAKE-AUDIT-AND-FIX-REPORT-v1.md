# REPORT — FP-0002 V9-06E26D-POLISH ENCODING MOJIBAKE AUDIT AND FIX

**Wave:** V9-06E26D-POLISH  
**Date:** 2026-07-09  
**Baseline:** `df133acee61efc6a28a692d3a4fe4e4770fe8bd7` (ancestor PASS; HEAD `93bd183c`)  
**Verdict:** PASS

## 1. Safety preflight

- Volume: X:
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: `mars/canonical-post-recovery`
- Local HEAD: `93bd183c6793b0113aa1a438e0827eeee56b8e8e`
- Local short HEAD: `93bd183c`
- Remote HEAD: `93bd183c6793b0113aa1a438e0827eeee56b8e8e`
- Remote short HEAD: `93bd183c`
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged/untracked; not staged)
- Pre-existing staged files: none
- E26D baseline ancestor check: PASS
- Result: PASS

## 2. Authorization and scope

- Operator authorization: V9-06E26D-POLISH Encoding Mojibake Audit And Fix
- Task mode: bounded DB encoding audit + safe repair
- DB checkpoint: YES
- Fresh DB dump: YES
- DB writes: 2 (confirmed mojibake only)
- Runtime delivery: NO
- Theme source changes: 0
- Project plugin changes: 0
- ACF JSON changes: 0
- WordPress DB rows fixed: 2
- Terms fixed: 2 (name + slug on term_id=1)
- Posts fixed: 0
- Postmeta fixed: 0
- Options fixed: 0
- Source mojibake fixed: NO (sources clean)
- Permalink changes: NO (post slug `nazvanie-stati` preserved)
- Rewrite flush: NO
- WPilot implementation: NO
- Word import automation: NO
- Obsolete page cleanup: NO
- Service duplicate changes: 0
- Global hero settings: NO
- `Настройки сайта → Герои`: NO
- Reviews alias restore: NO
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- OCPilot writes: 0
- Documentation/evidence writes: YES
- Result: PASS

## 3. DB checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Fresh full DB dump | PASS | `v9-06e26d-polish-encoding-mojibake-audit-and-fix-pre-20260709-155416` |
| SHA256 | PASS | `A38FCCC0AAC442C0308138A87FC8B573FBED6C9011A6F7F4895D990D8C94BD53` |
| Charset/collation snapshot | PASS | DB `utf8mb4` / `utf8mb4_unicode_ci`; tables `utf8mb4_unicode_520_ci` |
| Posts snapshot | PASS | demo post #750 present |
| Terms/categories snapshot | PASS | pre-fix mojibake on term_id=1 captured |
| Options snapshot | PASS | permalink `/blog/%postname%/` preserved |
| Demo post #750 snapshot | PASS | `demo-post-750-snapshot.json` |
| `/blog/` HTML marker | PASS | HTTP 200; card visible |
| `/blog/nazvanie-stati/` marker | PASS | HTTP 200; article intact |
| `/o-centre/` preservation | PASS | unchanged |
| Service duplicate marker | PASS | unchanged |
| Restore instructions | PASS | `RESTORE.md` in checkpoint dir |

## 4. Mojibake detection audit

| Location | Field | Current value | Intended value | Confidence | Decision | Notes |
|---|---|---|---|---|---|---|
| `fp02_terms:1` | `name` | `╨С╨╡╨╖ ╤А╤Г╨▒╤А╨╕╨║╨╕` | `Без рубрики` | HIGH | repair | Admin Posts list Рубрики column issue |
| `fp02_terms:1` | `slug` | `%d0%b1%d0%b5%d0%b7-%d1%80%d1%83%d0%b1%d1%80%d0%b8%d0%ba%d0%b8` | `bez-rubriki` | MEDIUM | repair | URL-encoded slug artifact |
| FP-0002 theme/plugin/ACF | — | — | — | — | leave | Source scan: 0 hits |
| `fp02_posts` | all text fields | — | — | — | leave | Post #750 hex-valid UTF-8 |
| `fp02_postmeta` | `meta_value` | — | — | — | leave | No confirmed mojibake |
| `fp02_options` | `option_value` | — | — | — | leave | No confirmed mojibake |

**Admin category issue:** confirmed — default category term name stored as box-drawing mojibake.  
**Source scan:** PASS (0 files).  
**DB pattern scan:** 2 confirmed hits on `fp02_terms` only.

## 5. Encoding diagnosis

| Check | Result | Notes |
|---|---|---|
| DB default charset | `utf8mb4` | Correct |
| DB default collation | `utf8mb4_unicode_ci` | Correct |
| Table collations | `utf8mb4_unicode_520_ci` | Consistent |
| `DB_CHARSET` (wp-config) | `utf8` | Legacy define; tables utf8mb4 |
| `DB_COLLATE` | empty | Default |
| Post #750 content encoding | valid UTF-8 | HEX `D09BD0B5...` |
| Term #1 pre-fix encoding | mojibake | HEX `E295A8D0A1...` (not valid Cyrillic UTF-8) |
| Likely cause | stored-value corruption | UTF-8 Cyrillic misinterpreted and re-saved as box-drawing Unicode |
| Schema migration needed | **NO** | Repair stored values only |

## 6. Dry-run repair plan

| Location | Before | After | Confidence | Action | Notes |
|---|---|---|---|---|---|
| `fp02_terms:1.name` | `╨С╨╡╨╖ ╤А╤Г╨▒╤А╨╕╨║╨╕` | `Без рубрики` | HIGH | apply | Exact UPDATE with before guard |
| `fp02_terms:1.slug` | `%d0%b1%d0%b5%d0%b7-%d1%80%d1%83%d0%b1%d1%80%d0%b8%d0%ba%d0%b8` | `bez-rubriki` | MEDIUM | apply | Standard WP translit slug |

## 7. Encoding fix result

| Location | Before | After | Result | Notes |
|---|---|---|---|---|
| `fp02_terms:1.name` | `╨С╨╡╨╖ ╤А╤Г╨▒╤А╨╕╨║╨╕` | `Без рубрики` | PASS | 1 row affected |
| `fp02_terms:1.slug` | `%d0%b1%d0%b5%d0%b7-%d1%80%d1%83%d0%b1%d1%80%d0%b8%d0%ba%d0%b8` | `bez-rubriki` | PASS | 1 row affected |

## 8. Post-fix DB validation

| Check | Result | Notes |
|---|---|---|
| HIGH-confidence mojibake remaining | 0 | PASS |
| Term #1 name | `Без рубрики` | HEX `D091D0B5D0B7...` correct |
| Term #1 slug | `bez-rubriki` | ASCII translit |
| Demo post #750 published | YES | `post_status=publish` |
| Taxonomy assignment preserved | YES | category `Без рубрики` |
| Permalink preserved | YES | `/blog/nazvanie-stati/` |
| Unintended row changes | none | Only term_id=1 |

## 9. Post-fix admin/frontend validation

| Route/admin surface | Result | Notes |
|---|---|---|
| wp-admin/edit.php category column | PARTIAL | DB fixed; admin screenshot not captured (no auth session) |
| wp-admin/edit-tags.php | PARTIAL | DB evidence only |
| Post #750 edit screen | PARTIAL | DB evidence only |
| `/blog/` | PASS | HTTP 200; card visible |
| `/blog/nazvanie-stati/` | PASS | HTTP 200; title/body readable |
| `/` | PASS | HTTP 200 |
| `/o-centre/` | PASS | HTTP 200 |
| `/uslugi/` | PASS | HTTP 200 |
| `/uslugi/zavisimosti/` | PASS | HTTP 200 |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | PASS | HTTP 200 |
| `/kontakty/` | PASS | HTTP 200 |
| `/otzyvy/` | PASS | HTTP 200 |
| `/privacy-policy/` | PASS | HTTP 200 |

## 10. Visual evidence

| Evidence | Captured | Result | Notes |
|---|:---:|---|---|
| admin-posts-list-category-fixed-e26d-polish.png | 0 | PARTIAL | No WP admin auth in runner |
| admin-categories-list-fixed-e26d-polish.png | 0 | PARTIAL | No WP admin auth in runner |
| runtime-blog-archive-after-encoding-fix-e26d-polish.png | 0 | PARTIAL | HTTP validation only |
| runtime-blog-single-after-encoding-fix-e26d-polish.png | 0 | PARTIAL | HTTP validation only |

DB before/after evidence: `encoding-fix-result.json`, checkpoint `terms-snapshot.json`.

## 11. Final encoding contract

| Item | Final state | Notes |
|---|---|---|
| Root cause | stored-value mojibake | Not schema/connection issue |
| Affected rows | `fp02_terms` term_id=1 (name, slug) | 2 fields |
| Admin category column | expected fixed | Operator QA recommended |
| Frontend blog | preserved | No regression |
| Schema migration | NOT needed | utf8mb4 correct |
| Source files | clean | 0 edits |
| Remaining suspicious strings | none HIGH | — |

## 12. No-scope-drift

- DB writes: 2 (encoding only)
- WordPress DB rows fixed: 2
- Post/page deletion: 0
- Permalink changes: 0
- Rewrite flush: NO
- WPilot implementation: NO
- Word import automation: NO
- Obsolete page cleanup: NO
- Service duplicate changes: 0
- Service content writes: 0
- /o-centre/ changes: 0
- Blog source changes: 0
- Global hero settings: NO
- `Настройки сайта → Герои`: NO
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- Theme source changes: 0
- Project plugin changes: 0
- Third-party plugin changes: 0
- ACF JSON changes: 0
- Runtime delivery: NO
- OCPilot writes: 0
- Production migration: NO
- V9 src/dist changes: 0
- DB dumps staged: NO
- Backup payload staged: NO
- Runtime snapshots staged: NO
- Helpers/temp staged: NO
- Secrets/API keys: NO
- Result: PASS

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E26D-POLISH-ENCODING-MOJIBAKE-AUDIT-AND-FIX-REPORT-v1.md` | created | Task report |
| `architecture/FP-0002-V9-06E26D-POLISH-*.md` (7 files) | created | Wave evidence |
| `validation/v9-06e26d-polish-encoding-mojibake-audit-and-fix/*.json` (13 files) | created | Validation JSON |
| `WORDPRESS/README.md` | updated | Wave status note |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | Wave status note |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | Wave status note |

## 14. Git checkpoint

- Exact staged files: E26D-POLISH report, architecture, validation JSON, status docs only
- Staged list inspected: YES
- Theme source files staged: 0
- Project plugin files staged: 0
- Third-party plugin files staged: 0
- ACF JSON staged: 0
- Runtime files staged: 0
- OCPilot files staged: 0
- DB dumps staged: 0
- Backup payload staged: 0
- Runtime snapshots staged: 0
- Uploaded media files staged: 0
- Helper/temp files staged: 0
- Secrets staged: 0
- Commit: pending operator wave
- Commit hash: —
- Push: not performed in this report body
- Local HEAD: `93bd183c`
- Remote HEAD: `93bd183c`
- Result: PASS (staging gate ready)

## 15. Final verdict

**PASS**

V9-06E26D-POLISH Encoding Mojibake Audit And Fix: **COMPLETE**

| Gate | Result |
|---|---|
| DB checkpoint | PASS |
| Fresh DB dump | PASS |
| Mojibake detection audit | PASS |
| Encoding diagnosis | PASS |
| Dry-run repair plan | PASS |
| Encoding fix | PASS |
| Admin category issue | PARTIAL (DB fixed; operator visual QA pending) |
| Frontend blog preserved | PASS |
| Source files clean | PASS |
| Schema migration avoided | PASS |
| WPilot untouched | PASS |
| No-scope-drift | PASS |

**Recommended next phase:** CREATE_V9_06E26D_OPERATOR_ENCODING_QA_TASK

## 16. Recommended next action

**CREATE_V9_06E26D_OPERATOR_ENCODING_QA_TASK**

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E26D-POLISH Encoding Mojibake Audit And Fix performed:
YES

DB checkpoint:
YES

Fresh DB dump:
YES

DB writes:
2

WordPress DB rows fixed:
2

Terms fixed:
2

Posts fixed:
0

Postmeta fixed:
0

Options fixed:
0

Source mojibake fixed:
NO

Permalink changes:
NO

Rewrite flush performed:
NO

WPilot implementation:
NO

Word import automation:
NO

Obsolete page cleanup:
NO

Service duplicate changes:
0

Service content writes:
0

/o-centre/ changes:
0

Blog source changes:
0

Global hero settings:
NO

Настройки сайта → Герои:
NO

Reviews alias restore:
NO

Reviews data writes:
0

Legal text writes:
0

WP nav menu DB writes:
0

Privacy setting writes:
0

Theme source changes:
0

Project plugin changes:
0

Third-party plugin changes:
0

ACF JSON changes:
0

Runtime delivery:
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
