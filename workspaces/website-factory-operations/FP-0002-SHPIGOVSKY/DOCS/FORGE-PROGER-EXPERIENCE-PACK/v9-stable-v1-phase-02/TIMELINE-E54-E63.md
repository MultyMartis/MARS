# Timeline — FP-0002 V9-06E54 → E63 (Experience Phase 02)

Chronological reconstruction for Forge Proger learning.  
**Reliability rule:** local PASS ≠ operator acceptance. Marks below call out rejected / corrected / deferred outcomes.

Primary project ledger: `PROJECT-STATUS.md` (E54–E63 entries).  
Stable closeout: `REPORTS/REPORT-FP-0002-V9-06E63-STABLE-V1-CLOSEOUT.md`.

---

## Legend

| Mark | Meaning |
|------|---------|
| LOCAL_PASS | Automated/local validation green |
| OP_PENDING | Operator review not yet recorded for that wave |
| OP_ACCEPTED_LATER | Accepted as part of later freeze/Stable (not necessarily same-day) |
| CORRECTED | Follow-up FIX required after local PASS or operator feedback |
| FALSE_ASSUMPTION | Approach or claim later proven wrong |
| RUNTIME_CANON | Operator runtime edit was the real authority |

---

## E54 — Floating Header

| | |
|--|--|
| **Objective** | Implement floating header behavior after Web-GPT chat migration |
| **Systems** | Theme header templates, floating-header partial, CSS/JS shell |
| **Major decision** | Add floating header as product shell feature without rewriting operator CSS |
| **Operator feedback** | Visual defects: background + menu scroll jump from floating state |
| **Defects / corrections** | → E54-FIX01 |
| **Final accepted state** | Accepted via later Stable baseline (shell present) |
| **Reusable lesson** | Shell UX needs FIX budget; preserve operator CSS hashes |
| **PASS reliability** | LOCAL_PASS; OP_PENDING at wave time; CORRECTED |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E54-floating-header.md`; backup `v9-06e54-after-web-gpt-chat-migration-…` |

### E54-FIX01 — Background + menu scroll

| | |
|--|--|
| **Objective** | Floating header background `#e5ecf4`; offcanvas scroll-lock preserves `scrollY` |
| **Systems** | Floating header CSS; `initOffcanvas()` |
| **Major decision** | Scoped fix only; exact-file delivery (2 files); DB 0 |
| **Operator feedback** | Awaiting visual acceptance at wave time |
| **Final state** | Included in Stable v1 shell |
| **Lesson** | Menu-open from floating header must not jump page position |
| **Marks** | LOCAL_PASS; OP_PENDING → OP_ACCEPTED_LATER |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E54-FIX01-floating-header-background-menu-scroll.md` |

---

## E55 — Site Settings Admin UX

| | |
|--|--|
| **Objective** | Extend E53 admin styling to Site Settings / `fp02-block-*` options screens |
| **Systems** | `admin-fp02-acf.css`, enqueue rules, `body.fp02-site-settings-admin` |
| **Major decision** | Options-page `.postbox` DOM differs from post `.acf-postbox` — style both |
| **Operator feedback** | Visual review pending at wave time |
| **Final state** | Admin UX model accepted into Stable |
| **Lesson** | Admin CSS is product; options screens need separate selectors |
| **Marks** | LOCAL_PASS; DB 0; OP_PENDING → OP_ACCEPTED_LATER |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E55-site-settings-admin-ux.md` |

---

## E56 — Operator Refinements Batch 01

| | |
|--|--|
| **Objective** | Mixed operator requests: footer OverSEO, theme meta, lead forms, images, video, Max messenger, gallery CSS, Comfort admin split |
| **Systems** | Theme, forms, media, options |
| **Major decision** | Promote runtime operator CSS/HTML first, then apply batch |
| **Operator feedback** | Waiting on Libertinus asset (Task D) |
| **Defects** | Oversized mixed charter → PARTIAL; font deferred |
| **Final state** | Completed items carried into Stable; font in FU02 |
| **Lesson** | Broad “operator refinements” batches hide unfinished tails |
| **Marks** | PARTIAL LOCAL_PASS; RUNTIME_CANON; CORRECTED via FU01/FU02 |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E56-operator-refinements-batch-01.md` |

### E56-FU01 — Hero / slider / font follow-up

| | |
|--|--|
| **Objective** | Remove Home hero empty-field demo fallback; mobile hero aspect parity; gallery CSS display parity |
| **Major decision** | Preserve promoted operator CSS; additive FU only |
| **Marks** | PARTIAL (Libertinus WAITING_FOR_OPERATOR_ASSET) |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E56-FU01-hero-slider-font-follow-up.md` |

### E56-FU02 — Libertinus Serif

| | |
|--|--|
| **Objective** | Apply operator Libertinus Regular to hero titles |
| **Major decision** | TTF fallback acceptable when no local WOFF2 converter; `lifebuoy.webp` reserved untouched |
| **Lesson** | Wait for operator assets; do not invent font substitutions as “done” |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E56-FU02-libertinus-serif.md` |

---

## E57 — Lifebuoy global parallax (+ FIX01 / FIX02)

| Wave | Objective | Key decision | Marks |
|------|-----------|--------------|-------|
| E57 | Global fixed lifebuoy + scroll-progress parallax | Mount in `body-start`; reduced-motion freeze; preserve operator CSS | LOCAL_PASS; OP_PENDING |
| E57-FIX01 | Size/reveal/scale/rotation refinement | Tune existing motion only | LOCAL_PASS |
| E57-FIX02 | Start reveal ~50%, long-page ~80%, easing, +rotation | Operator continued manual CSS after FIX02 (`307A111E…`) | RUNTIME_CANON |

**Reusable lesson:** motion features need iterative operator tuning; do not freeze motion CSS against an older hash after operator continues editing.

**Evidence:** `REPORTS/REPORT-FP-0002-V9-06E57-*.md`; later captured in E58 freeze.

---

## E58 — Freeze + Figma visual audit (+ FU01)

| | |
|--|--|
| **Objective** | Freeze current baseline **before** visual audit; audit Figma vs runtime; produce operator decision pack |
| **Systems** | Full backup; audit scripts; decision matrices |
| **Major decision** | Freeze first; audit findings-only; exclude lifebuoy/heroes/main header/floating header/footer from forced “fixes” |
| **Operator feedback** | Confirmed **E58-VA-001** only for E59 implementation |
| **Defects / false positives** | FU01: VA-002/003/006/007/008 recommended REJECT as false positives (brittle DOM-index pairing); VA-004 intentional multi-size H2; VA-005 HOLD |
| **Final accepted state** | Freeze marker + remote push via clean worktree `29c07d21`; operator CSS protected |
| **Reusable lesson** | Automated metric mismatch ≠ visual bug; operator decides; freeze protects against audit thrash |
| **Marks** | FREEZE PASS; AUDIT COMPLETE (findings); FU01 COMPLETE; OP decision selective |
| **Evidence** | `REPORTS/FREEZE-FP-0002-V9-06E58-CURRENT-BASELINE-BEFORE-VISUAL-AUDIT-ACCEPTED.md`; `REPORTS/REPORT-FP-0002-V9-06E58-*.md`; backup `v9-06e58-current-baseline-freeze-…` |

---

## E59 — Layout polish / maps / footer / Comfort CTA (+ FIX01)

| Wave | Objective | Key outcomes | Marks |
|------|-----------|--------------|-------|
| E59 | Restore Home `no-top-padding` (VA-001); Contacts `contacts_locations` maps; footer heading links; Comfort `cta_lead_text` | Runtime CSS/HTML canonized then additive | LOCAL_PASS; OP_PENDING |
| E59-FIX01 | Comfort gallery decor outside gallery; remove obsolete Contacts fields; footer hover exact `accent-hover` | Legacy Contacts postmeta **dormant** (not deleted); future Site Settings IA task registered | LOCAL_PASS |

**Lesson:** `active` field removal ≠ data deletion; keep dormant meta when FE ownership moves.

**Evidence:** `REPORTS/REPORT-FP-0002-V9-06E59-*.md`.

---

## E60 — Nav / breadcrumb / CTA unify / service links (+ FIX01)

| Wave | Objective | Key outcomes | Marks |
|------|-----------|--------------|-------|
| E60 | Audit nav/crumb typography; unify `.program-cta-band` with Comfort CTA; service-name links; accent-hover classification | Claimed “no unwanted typography change”; applied breadcrumb **hover** → `accent-hover` | LOCAL_PASS then **CORRECTED** |
| E60-FIX01 | Restore breadcrumb hover to E58 `accent`; Reviews name `h2`→`div` (18/24) | **E58 freeze backup** used as style authority — not “current source” alone | CORRECTED; FALSE_ASSUMPTION on “typography restored” narratives |

**Critical reliability note:** E60 LOCAL_PASS was insufficient. Operator-visible breadcrumb hover + Reviews typography needed FIX01. “Matches E58 typography” was already true for font-size; the real regression was **hover color** and Reviews name element.

**Evidence:** `REPORTS/REPORT-FP-0002-V9-06E60-*.md`; `REPORTS/evidence/v9-06e60-fix01-breadcrumb-subnav-reviews/`.

---

## E61 — Admin controls + Contacts / Blog / Reviews / O-centre / Home

| | |
|--|--|
| **Objective** | Large multi-surface admin + FE refinements in one wave |
| **Systems** | Breadcrumb toggles; Contacts phones/messengers; Blog archive admin + demo posts; Reviews expand + `reviews_per_page`; O-centre reuse Home blocks; span wrappers |
| **Major decision** | Promote runtime CSS/JS first; seed demos for pagination proof |
| **Operator feedback** | Pending; tails left open |
| **Defects** | PARTIAL: incomplete admin/viewport screenshots; Founder Quote still fallback-heavy; **nested `<section>` CTA** in who-we-treat; oversized scope |
| **Final state** | Core behaviors carried forward; structural defects fixed in E62* |
| **Lesson** | Do not close “No follow-up needed” with open tails; split mega-waves |
| **Marks** | PARTIAL LOCAL_PASS; OP_PENDING; CORRECTED by E62A–E62E |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E61-admin-controls-contacts-blog-reviews-ocentre-home.md` |

---

## E62A — 404 + breadcrumb wrapper + phone mask

| | |
|--|--|
| **Objective** | Figma 404 baseline; unify Generic/Specialist crumbs under `.internal-page-nav > .container > .breadcrumbs`; Triumph Manipulator phone mask |
| **Major decision** | Canonize operator CSS first; DB 0 |
| **Lesson** | Cross-project reuse (phone mask) is OK when vanilla and scoped |
| **Marks** | LOCAL_PASS; OP_PENDING → OP_ACCEPTED_LATER |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E62A-404-breadcrumb-wrapper-phone-mask.md` |

---

## E62B — Blog/Reviews pagination + SEO + slider links + demo content

| | |
|--|--|
| **Objective** | Pagination SEO self-canonicals; demo Blog thumbs; +20 demo Reviews; slider “read full” → archive anchors; Founder Quote ownership seed |
| **Major decision** | Reviews are **ACF Options repeater**, not CPT |
| **Defects** | Index-based anchors `#review-{n}` later superseded by stable UID |
| **Marks** | LOCAL_PASS; FALSE_ASSUMPTION risk if assumed CPT; CORRECTED in E62C |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E62B-blog-reviews-pagination-seo-slider-links.md` |

---

## E62C — O-centre + Service admin hide + stable review UID + regression

| | |
|--|--|
| **Objective** | O-centre lead/bullets; nested CTA → `<div class="program-cta-band">`; hide Structured Sections + Relationships (`active:false`); `review_uid` ×30; 64 viewport shots |
| **Major decision** | Hide obsolete groups without deleting field keys/data; stable UID anchors |
| **Lesson** | `active:false` + filter > data deletion; UID > row index |
| **Marks** | LOCAL_PASS; demo cleanup deferred (documented backlog) |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E62C-…`; `DOCS/REVIEWS-STABLE-UID-ANCHORS-v1.md`; `DOCS/DEMO-CONTENT-CLEANUP-BACKLOG-v1.md` |

---

## E62D — Treatment Program mini-descriptions + 404 Figma correction

| | |
|--|--|
| **Objective** | Move Home mini-descriptions from hardcoded helpers → page ACF; retune 404 CSS to Figma PNG metrics |
| **Major decision** | Seed #1053–1056 from former hardcoded texts; empty ACF → empty (no permanent hardcoded array) |
| **Lesson** | Hardcoded “temporary” Home copy becomes ownership debt |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E62D-program-mini-descriptions-404-figma-correction.md` |

---

## E62E — 404 decor + WordPress Search (+ FIX01)

| Wave | Objective | Key outcomes | Marks |
|------|-----------|--------------|-------|
| E62E | Install operator `404-decor.png`; Header search dropdown + native WP Search (`post`/`page`/`service`) | Search baseline accepted for Stable; advanced relevance deferred | LOCAL_PASS; OP review pending at wave |
| E62E-FIX01 | Search crumbs → internal-page-nav wrapper; remove search triggers from floating + mobile header; mobile offcanvas link only | Operator did **not** want triggers everywhere | CORRECTED |

**Lesson:** Search trigger ownership is UX product design, not “add toggle to every chrome surface.”

**Evidence:** `REPORTS/REPORT-FP-0002-V9-06E62E-*.md`.

---

## E63 — Stable v1 closeout

| | |
|--|--|
| **Objective** | Operator-accepted Stable local near-production baseline: canonize, backup, validate, freeze, document, Git allowlist, clean-worktree commit+push |
| **Systems** | Source/runtime/DB freeze; `REPORTS/STABLE-V1/*`; Storage clean worktree |
| **Major decision** | Accept deferred tails explicitly; no production deploy; no force push; dirty main untouched |
| **Operator feedback** | Current result good; closeout requested |
| **Final accepted state** | Freeze `v9-stable-v1-near-production-freeze-20260718-004137`; content commit `d1befe9b…`; remote tip `9d5dcc28…` |
| **Reusable lesson** | Closeout is a multi-gate release pattern, not a single commit on dirty main |
| **Marks** | PASS (Stable); production OUT_OF_SCOPE |
| **Evidence** | `REPORTS/REPORT-FP-0002-V9-06E63-STABLE-V1-CLOSEOUT.md`; `REPORTS/FREEZE-FP-0002-V9-STABLE-V1.md`; `REPORTS/STABLE-V1/*` |

---

## PASS reliability summary (Phase 2)

| Pattern | Waves |
|---------|-------|
| LOCAL_PASS later needing FIX | E54→FIX01; E57→FIX01/02; E59→FIX01; E60→FIX01; E62E→FIX01 |
| PARTIAL with open tails | E56, E61 |
| Freeze before further risk | E58, E63 |
| Operator runtime newer than source | Multiple (esp. E56–E63 CSS/JS hashes) |
| Backup used as style authority | E60-FIX01 ← E58 freeze |
| Explicit deferred at Stable | Demo Blog/Reviews, SMTP, Search refinement, source-only ACF, production |

Do **not** treat every LOCAL_PASS report in E54–E62 as final operator acceptance. Stable v1 operator acceptance is recorded at E63.
