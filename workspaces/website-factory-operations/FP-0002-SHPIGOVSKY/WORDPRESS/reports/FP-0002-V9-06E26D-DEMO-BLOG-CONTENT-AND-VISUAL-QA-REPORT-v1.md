# REPORT — FP-0002 V9-06E26D DEMO BLOG CONTENT AND VISUAL QA

**Wave:** V9-06E26D  
**Date:** 2026-07-09  
**Baseline:** `0b5dadf132a9b7f20568fcd02933659a4f80988d` (ancestor PASS; HEAD advanced to `c32cdb52`)  
**Verdict:** PASS

## 1. Safety preflight

- Volume: X:
- Label: AI WS
- Repository: `X:\AI MARS`
- Branch: `mars/canonical-post-recovery`
- Local HEAD: `c32cdb52a3ac19b918b32caae209bc4e10319e73`
- Local short HEAD: `c32cdb52`
- Remote HEAD: `c32cdb52a3ac19b918b32caae209bc4e10319e73`
- Remote short HEAD: `c32cdb52`
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unstaged/untracked; not staged)
- Pre-existing staged files: none
- E26C baseline ancestor check: PASS
- Result: PASS

## 2. Authorization and scope

- Operator authorization: V9-06E26D Demo Blog Content And Visual QA
- Task mode: bounded DB seed + visual QA
- DB checkpoint: YES
- Fresh DB dump: YES
- DB writes: one demo post + meta (14 writes)
- Runtime delivery: NO
- Theme source changes: 0
- Project plugin changes: 0
- ACF JSON changes: 0
- WordPress post writes: 1 published demo article
- Published demo article seed: YES
- Demo post ID: 750
- Blog archive source changes: 0
- Blog single source changes: 0
- Blog permalink changes: NO
- Rewrite flush: NO
- WPilot implementation: NO
- Word import automation: NO
- Obsolete page cleanup: NO
- Service duplicate changes: 0
- Global hero settings: NO
- `Настройки сайта → Герои`: NO
- Reviews alias restore: NO
- Reviews data writes: 0
- Legal text writes: 0
- WP nav menu DB writes: 0
- Privacy setting writes: 0
- OCPilot writes: 0
- Documentation/evidence writes: YES
- Result: PASS

## 3. DB checkpoint

| Item | Result | Path/notes |
|---|---|---|
| Fresh full DB dump | PASS | `v9-06e26d-demo-blog-content-and-visual-qa-pre-20260709-143210` |
| SHA256 | PASS | `74E91983D8321B0AFA7A92DDAF703B1C91C4DE3DA2673BAEDC1DD7E85FC1FD28` |
| WP options snapshot | PASS | `page_for_posts=19`, permalink `/blog/%postname%/` |
| Posts snapshot (pre) | PASS | 0 published; 1 auto-draft |
| Categories/tags snapshot | PASS | unchanged |
| Blog archive settings | PASS | preserved on page 19 |
| Article meta group | PASS | 23 fields |
| Preservation markers | PASS | `/o-centre/` hero CTA preserved; reviews options present |
| Restore instructions | PASS | `RESTORE.md` in checkpoint dir |

## 4. Static fixture extraction audit

| Fixture item | Static V9 | WP target | Decision | Notes |
|---|---|---|---|---|
| canonical_route | `/blog/nazvanie-stati/` | post permalink | SEED | slug `nazvanie-stati` |
| title | Лечение алкогольной зависимости… | `post_title` | SEED | from hero H1 |
| slug | `nazvanie-stati` | `post_name` | SEED | fixture slug |
| lead | `blog-article-hero__excerpt` | `article_lead` | SEED | ACF |
| card excerpt | archive card text | `post_excerpt` | SEED | short card copy |
| date | 2026-05-05 | `post_date` | SEED | archive/single meta |
| reading_time | 5 минут | `article_reading_time` | SEED | ACF minutes |
| author | Шпиговский С.Ю. | `article_author_label` + hide=0 | SEED | meta row |
| featured_image | article-alcohol-dependence.webp | theme fallback | NO_UPLOAD | no media library upload |
| body | 5 h2 / 12 h3 / 4 figures | `post_content` | SEED | inline theme asset URLs |
| conclusion_quote | founder-quote block | `article_conclusion_quote` | SEED | ACF |
| sources | 8 bibliography items | `article_source_items` | SEED | repeater |
| faq | none | hidden | SKIP | no FAQ in fixture |
| related | static placeholder cards | hidden | SAFE_EMPTY | only 1 post exists |
| final_cta | program-cta-band | archive CTA fallback | TEMPLATE_FALLBACK | no per-post override |

## 5. Demo content seed plan

| Field/item | Planned value | Source | Safety | Notes |
|---|---|---|---|---|
| title | V9 hero H1 | `blog-article-content.html` | SAFE | fixture title |
| slug | `nazvanie-stati` | V9 route | SAFE | canonical demo slug |
| status | `publish` | local QA | SAFE | local runtime only |
| post_type | `post` | WP model | SAFE | standard post |
| content | body HTML | static partial | SAFE | theme asset image URLs |
| excerpt | card excerpt | archive card | SAFE | archive card text |
| category/tag | none | static V9 | SAFE | card has no category label |
| date | 2026-05-05 | static meta | SAFE | |
| featured image | theme fallback | no upload | SAFE | `article-alcohol-dependence.webp` |
| ACF fields | 13 article meta | E26C model | SAFE | demo metadata only |
| existing slug check | auto-draft only | DB probe | SAFE | no real post conflict |

## 6. Demo content seed result

| Item | Result | Notes |
|---|---|---|
| post ID | 750 | created |
| title | Лечение алкогольной зависимости: почему сила воли здесь ни при чём | |
| slug | `nazvanie-stati` | |
| status | `publish` | |
| URL | `http://shpigovsky.test/blog/nazvanie-stati/` | HTTP 200 |
| category/tags | none | matches static card |
| ACF fields | 13 written | lead, reading time, author, TOC, conclusion, sources, demo status |
| content sections | 5 h2, 12 h3, 4 inline images, 8 sources | |
| media strategy | theme_asset_fallback_no_upload | no attachment upload |
| DB writes | 14 | post + meta |

## 7. Source bugfix gate

| Area | Needed | Result | Notes |
|---|:---:|---|---|
| Blog archive template | NO | PASS | card renders with seeded post |
| Blog single template | NO | PASS | TOC, lead, body, lower stack OK |
| Theme CSS | NO | PASS | no changes |
| Plugin/ACF | NO | PASS | no changes |
| Runtime delivery | NO | PASS | 0 files delivered |

## 8. Post-seed frontend validation

| Route/check | Result | Notes |
|---|---|---|
| `/blog/` HTTP 200 | PASS | archive live |
| Archive card visible | PASS | `blog-archive-card` present |
| Empty state hidden | PASS | no `blog-archive__empty-state` |
| Card links to single | PASS | `/blog/nazvanie-stati/` in card |
| `/blog/nazvanie-stati/` HTTP 200 | PASS | was 404 pre-seed |
| Breadcrumbs | PASS | `breadcrumbs__list` in HTML |
| H1 title | PASS | hero title present |
| Lead/excerpt | PASS | `blog-article-hero__excerpt` |
| Meta row | PASS | date, reading time, author |
| Featured image/fallback | PASS | theme asset hero image |
| TOC | PASS | auto h2 anchors |
| Body typography | PASS | `blog-article-body` |
| Conclusion/quote | PASS | `blog-article-conclusion` |
| Sources | PASS | 8 items |
| FAQ | PASS | hidden (none seeded) |
| Related posts | PASS | hidden safely (1 post) |
| Final CTA | PASS | `program-cta-band-section` |
| Regression routes (8) | PASS | all HTTP 200 |

## 9. Admin validation

| Admin context | Result | Notes |
|---|---|---|
| Demo post exists | PASS | ID 750, publish |
| Article meta populated | PASS | 21 meta keys |
| Archive settings preserved | PASS | blog page 19 meta intact |
| No global Герои | PASS | no global hero options |
| `/o-centre/` preserved | PASS | `hero_cta_label` present |
| Service duplicate UI | PASS | no E26D service writes |
| Reviews preserved | PASS | reviews options present |
| No WPilot UI | PASS | passive demo metadata only |
| Admin screenshots | PARTIAL | auth required |

## 10. Visual evidence

| Evidence | Captured | Result | Notes |
|---|:---:|---|---|
| runtime-blog-archive-with-card-desktop-e26d.png | YES | PASS | 1440px |
| runtime-blog-archive-with-card-mobile-e26d.png | YES | PASS | 390px |
| runtime-blog-single-desktop-e26d.png | YES | PASS | 1440px |
| runtime-blog-single-mobile-e26d.png | YES | PASS | 390px |
| runtime-blog-single-toc-e26d.png | YES | PASS | hero/TOC region |
| runtime-blog-single-final-cta-e26d.png | YES | PASS | CTA band |
| admin-demo-post-article-meta-e26d.png | NO | PARTIAL | login gate |
| admin-demo-post-status-e26d.png | NO | PARTIAL | login gate |

## 11. Final E26D demo blog contract

| Item | Final state | Notes |
|---|---|---|
| Demo post ID | 750 | local publish |
| Route | `/blog/nazvanie-stati/` | permalink preserved |
| Archive | 1 card, no empty state | pagination N/A (1 post) |
| Single | full V9 stack rendered | TOC, conclusion, sources, CTA |
| Media | theme fallback only | no upload |
| WPilot | not implemented | future boundary |
| Limitations | 1 post; related hidden; admin shots partial | expected |
| Next phase | operator visual QA | sign-off task |

## 12. No-scope-drift

- DB writes: one demo post + meta only — PASS
- Published demo article seed: YES — PASS
- WordPress post writes: 1 — PASS
- Blog archive source changes: 0 — PASS
- Blog single source changes: 0 — PASS
- Blog permalink changes: NO — PASS
- Rewrite flush: NO — PASS
- WPilot implementation: NO — PASS
- Word import automation: NO — PASS
- Obsolete page cleanup: NO — PASS
- Service duplicate changes: 0 — PASS
- Service content writes: 0 — PASS
- /o-centre/ changes: 0 — PASS
- Global hero settings: NO — PASS
- `Настройки сайта → Герои`: NO — PASS
- Reviews alias restore: NO — PASS
- Reviews data writes: 0 — PASS
- Legal text writes: 0 — PASS
- WP nav menu DB writes: 0 — PASS
- Privacy setting writes: 0 — PASS
- Theme source changes: 0 — PASS
- Project plugin changes: 0 — PASS
- Third-party plugin changes: 0 — PASS
- ACF JSON changes: 0 — PASS
- Runtime delivery: NO — PASS
- OCPilot writes: 0 — PASS
- Production migration: NO — PASS
- V9 src/dist changes: 0 — PASS
- DB dumps staged: NO — PASS
- Backup payload staged: NO — PASS
- Runtime snapshots staged: NO — PASS
- Helpers/temp staged: NO — PASS
- Secrets/API keys: 0 — PASS
- Result: PASS

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| `reports/FP-0002-V9-06E26D-DEMO-BLOG-CONTENT-AND-VISUAL-QA-REPORT-v1.md` | created | wave report |
| `architecture/FP-0002-V9-06E26D-*.md` (7) | created | checkpoint, audit, plan, result, bugfix, contract, next step |
| `validation/v9-06e26d-demo-blog-content-and-visual-qa/*.json` (13) | created | evidence |
| `validation/.../screenshots/*.png` (6) | created | visual QA |
| `WORDPRESS/README.md` | updated | E26D status |
| `WORDPRESS/SOURCE-AUTHORITY.md` | updated | E26D authority note |
| `FP-0002-SHPIGOVSKY/PROJECT-STATUS.md` | updated | phase status |

## 14. Git checkpoint

- Exact staged files: E26D report, architecture docs, validation JSON, screenshots, status docs only
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
- Commit: pending operator wave commit
- Push: pending

## 15. Final verdict

**PASS**

V9-06E26D Demo Blog Content And Visual QA: **COMPLETE**

DB checkpoint: **PASS**  
Fresh DB dump: **PASS**  
Static fixture extraction: **PASS**  
Demo content seed: **PASS**  
/blog/ archive with card: **PASS**  
/blog/nazvanie-stati/ single: **PASS**  
Desktop visual QA: **PASS**  
Mobile visual QA: **PASS**  
Blog archive preserved: **PASS**  
Blog single validated: **PASS**  
WPilot untouched: **PASS**  
No-scope-drift: **PASS**

Recommended next phase: **CREATE_V9_06E26D_OPERATOR_BLOG_VISUAL_QA_TASK**

## 16. Recommended next action

**CREATE_V9_06E26D_OPERATOR_BLOG_VISUAL_QA_TASK**

## 17. Final safety statement

Target folder:  
X:\AI MARS

V9-06E26D Demo Blog Content And Visual QA performed:  
YES

DB checkpoint:  
YES

Fresh DB dump:  
YES

DB writes:  
14

Published demo article seed:  
YES

Demo post ID:  
750

WordPress post writes:  
1

Blog archive source changes:  
0

Blog single source changes:  
0

Blog permalink changes:  
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
