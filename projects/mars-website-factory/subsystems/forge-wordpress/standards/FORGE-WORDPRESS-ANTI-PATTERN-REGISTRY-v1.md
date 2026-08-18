# Forge WordPress — Anti-Pattern Registry v1

**ID:** FW-S-21  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Evidence:** FP-0002 production + V9 Admin waves

Each ID is reusable. Client facts are generalized.

---

## AP-001 — Generic Page where a CPT is required

| | |
|--|--|
| Symptom | Editors fight parent/generic/template fields; weak list table; search mixes with Pages |
| Cause | “It already has a URL under a hub” |
| Risk | Bad Admin UX; wrong template; migration later under production |
| Prevention | CPT decision matrix in P1 |
| Replacement | Dedicated CPT + hub Page |
| Evidence | P11 specialists |

## AP-002 — Duplicate custom permalink UI over native WordPress

| | |
|--|--|
| Symptom | Two “Постоянная ссылка” rows; slug not saving; native Edit missing |
| Cause | Custom metabox + cloned sample permalink + `wp_insert_post_data` preferring custom field |
| Risk | URL drift; editor confusion |
| Prevention | Native `#edit-slug-box` only |
| Replacement | Core permalink UX + optional uniqueness data-layer |
| Evidence | P12 → P13-FU01 |

## AP-003 — Source deploy without fresh production drift intake

| | |
|--|--|
| Symptom | Operator CSS/PHP overwritten; “we uploaded the theme” |
| Cause | Assuming Git source is newer than live FS |
| Risk | Lost accepted visual work |
| Prevention | Fetch → hash → classify → canonize → exact upload |
| Replacement | [SOURCE-RUNTIME-AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) |
| Evidence | P09-FU01; P14 |

## AP-004 — Broad DB typography rewrite

| | |
|--|--|
| Symptom | Temptation to “fix all NBSP in MySQL” |
| Cause | Treating typography as stored content |
| Risk | HTML/shortcode/URL corruption |
| Prevention | Render-time HTML-aware pipeline |
| Replacement | [TYPOGRAPHY](FORGE-WORDPRESS-TYPOGRAPHY-PIPELINE-STANDARD-v1.md) |
| Evidence | P08 STOP; P16 |

## AP-005 — Global developer notices polluting Admin

| | |
|--|--|
| Symptom | LOCAL / env / MARS banners on every screen |
| Cause | Convenient `admin_notices` |
| Risk | Editor distrust; ignored real errors |
| Prevention | One operations Dashboard widget |
| Replacement | MetaCODE / system status widget |
| Evidence | P13 |

## AP-006 — Raw Options / debug screen for ordinary Admin

| | |
|--|--|
| Symptom | `options.php` or dump screens in the menu |
| Cause | Developer convenience left on |
| Risk | Accidental option wipes; secret exposure |
| Prevention | Menu hygiene; capability gates |
| Replacement | Curated Site Settings |
| Evidence | P13 AdminMenuHygiene |

## AP-007 — Hardcoded social links across templates

| | |
|--|--|
| Symptom | Footer/header disagree; code edits for URL changes |
| Cause | Static HTML leftovers |
| Risk | Drift; empty icons |
| Prevention | Registry + options SoT |
| Replacement | [SOCIAL-CONTACT](FORGE-WORDPRESS-SOCIAL-CONTACT-MODULE-SPEC-v1.md) |
| Evidence | P13 |

## AP-008 — Separate frontend consumers with independent contact settings

| | |
|--|--|
| Symptom | Header phone ≠ footer phone ≠ contacts page |
| Cause | Per-partial ACF |
| Risk | Operator cannot “set it once” |
| Prevention | One SoT, many consumers |
| Replacement | [SITE-SETTINGS](FORGE-WORDPRESS-SITE-SETTINGS-STANDARD-v1.md) |
| Evidence | contacts helpers / Site Settings |

## AP-009 — Demo fallback when Admin data is empty

| | |
|--|--|
| Symptom | Frontend still shows lorem after fields cleared |
| Cause | Template fallbacks left as normal SoT |
| Risk | False content on production |
| Prevention | Empty → hide; emergency fallbacks documented as emergency-only |
| Replacement | ACF SoT + empty-safe FE |
| Evidence | E46-FIX05; P07 Lorem cleanup; P12 nature demo removed |

## AP-010 — Emulation accepted as physical iOS proof

| | |
|--|--|
| Symptom | “Mobile Chrome DevTools PASS” while iPhone is static |
| Cause | WebKit compositor ≠ Blink |
| Risk | Ship-broken Apple UX |
| Prevention | Physical device gate |
| Replacement | [REAL-DEVICE-QA](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md) |
| Evidence | P12; P13 FIX02 |

## AP-011 — Multiple competing CSS/JS transform owners

| | |
|--|--|
| Symptom | Parallax vs header vs contain vs img transform |
| Cause | Layered “safe” patches |
| Risk | iOS freeze; un-debuggable motion |
| Prevention | One transform owner |
| Replacement | Bounded engine-specific fallback if needed |
| Evidence | lifebuoy series |

## AP-012 — Migration scripts left executable in public webroot

| | |
|--|--|
| Symptom | `/mars-runtime/*.php` 200 |
| Cause | Local helpers copied with the site |
| Risk | Unauthenticated mutation |
| Prevention | Hygiene gate; delete after use |
| Replacement | [WEBROOT HYGIENE](FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md) |
| Evidence | P17-FU02 |

## AP-013 — Probing unknown mutating script by GET

| | |
|--|--|
| Symptom | GET “to see what it does” creates posts/menus |
| Cause | Assuming diagnostic = read-only |
| Risk | Live content pollution |
| Prevention | Read source first; never HTTP-probe mutators |
| Replacement | Same hygiene standard |
| Evidence | `populate-fp-0002-pages.php` GET |

## AP-014 — DNS NS migration without mail-zone preservation

| | |
|--|--|
| Symptom | Website moves; mail dies (MX/SPF/DKIM left behind) |
| Cause | Treating NS switch as “point A records” |
| Risk | Business email outage |
| Prevention | Full zone inventory; copy MX/TXT before NS change |
| Replacement | [DNS-NS](../runbooks/FORGE-WORDPRESS-DNS-NS-CUTOVER-STANDARD-v1.md) |
| Evidence | P17 REG.RU mail vs Beget web |

## AP-015 — Opening indexing before SMTP/forms proof

| | |
|--|--|
| Symptom | Domain live, robots Allow, forms not delivering |
| Cause | “Site is up” confusion |
| Risk | Indexed broken UX; lost leads |
| Prevention | Indexing gate after SMTP; explicit human OPEN; never auto-open on deploy |
| Replacement | [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) · [SEARCH-INDEXING-CONTROL](FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md) |
| Evidence | P10–P18B indexing closed on purpose |

## AP-016 — Hardcoded future-domain redirects before cutover

| | |
|--|--|
| Symptom | Rules point at final host that is not live yet |
| Cause | Eager `.htaccess` |
| Risk | Loops, downtime, wrong host |
| Prevention | Path-relative 301s on temporary host; host-conditional after smoke |
| Replacement | [REDIRECT-STANDARD](../runbooks/FORGE-WORDPRESS-REDIRECT-STANDARD-v1.md) |
| Evidence | P17 CONT1 |

## AP-017 — Duplicate sitemap / search / SEO ownership

| | |
|--|--|
| Symptom | Two sitemaps; two title tags; search hitting Pages and CPT duplicates |
| Cause | Plugin + custom + leftover Page queries |
| Risk | Indexing chaos |
| Prevention | One owner each; migrate search/sitemap with CPT |
| Replacement | [SEO](FORGE-WORDPRESS-SEO-AND-SITEMAP-STANDARD-v1.md) |
| Evidence | P10; P11 |

## AP-018 — Broad Git operations in a shared dirty MARS monorepo

| | |
|--|--|
| Symptom | `git add .`, stash, reset, clean |
| Cause | Generic agent Git habits |
| Risk | Foreign WIP loss; secret commit |
| Prevention | Exact paths; clean worktree; no destructive git |
| Replacement | [GIT-SOP](../runbooks/FORGE-WORDPRESS-GIT-SOP-v1.md) |
| Evidence | MARS rules; P14+ checkpoints |

## AP-019 — Executing a stale cutover runbook after the operator already changed production

| | |
|--|--|
| Symptom | Wave still “changes home/siteurl” or “wait for NS” after the operator already did it |
| Cause | Plan-as-truth; no fresh intake |
| Risk | Revert of legitimate production; dual-origin confusion |
| Prevention | Fresh verify → accept/canonize legitimate drift → rewrite remaining steps |
| Replacement | [SOURCE-RUNTIME-AUTHORITY](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md) · [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) |
| Evidence | P18A operator `home`/`siteurl` + NS |

## AP-020 — Collapsing stored boolean false into unset/default

| | |
|--|--|
| Symptom | Admin checkbox OFF; frontend still shows the “default on” state |
| Cause | `$value ?: $default`; `empty()`; hardcoded template ignoring the field |
| Risk | Editors cannot turn a warning/feature off |
| Prevention | Three-state read (`unset` / `false` / `true`); `metadata_exists` |
| Replacement | [ACF FIELD MODELING](FORGE-WORDPRESS-ACF-FIELD-MODELING-STANDARD-v1.md) §6.1 |
| Evidence | P18A legal DEMO banner |

## AP-021 — Stale operator status dashboard after a major production wave

| | |
|--|--|
| Symptom | Widget still says “future host / NS switch pending / SSL in progress” after cutover and HTTPS are live |
| Cause | Treating the Dashboard as historical notes; updating reports but not the operator UI |
| Risk | Olya/operator act on false remaining work; accidental re-cutover |
| Prevention | Status panel is production state; update it in the same wave ([DoD](FORGE-WORDPRESS-DEFINITION-OF-DONE-v1.md)) |
| Replacement | [ADMIN UX](FORGE-WORDPRESS-ADMIN-UX-STANDARD-v1.md) §10.3 · [SEARCH-INDEXING-CONTROL](FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md) |
| Evidence | P18B MetaCODE Dashboard |

## AP-022 — FORM-001 Successful UI depends solely on email transport

| | |
|--|--|
| Symptom | Visitor sees error though the request existed; or success claimed only after SMTP |
| Cause | Persist-after-mail or no persist |
| Risk | Lost leads |
| Prevention | Persist lead before `wp_mail`; frontend success = accepted submission |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §9 |
| Evidence | FP-0002 P18C |

## AP-023 — FORM-002 No internal record of submitted leads

| | |
|--|--|
| Symptom | Inbox is the only history |
| Cause | Forms treated as mail scripts |
| Risk | Unrecoverable missed requests |
| Prevention | Dedicated lead table; business Admin list |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §9 |
| Evidence | FP-0002 P18C |

## AP-024 — FORM-003 Metrika goal fires on button click

| | |
|--|--|
| Symptom | Goals fire on invalid or unsent clicks |
| Cause | `reachGoal` in submit handler before backend |
| Risk | False conversion stats |
| Prevention | Fire only after backend-confirmed success JSON |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §10 |
| Evidence | FP-0002 P18C |

## AP-025 — FORM-004 SMTP password stored in source/Git

| | |
|--|--|
| Symptom | Password in wp-config, theme, reports |
| Cause | Convenience |
| Risk | Credential leak |
| Prevention | Admin write-only field; never render/log/commit |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §7 |
| Evidence | FP-0002 P18C |

## AP-026 — FORM-005 Visitor email used as From

| | |
|--|--|
| Symptom | SPF/DKIM fail; spoofed From |
| Cause | “Reply goes to the visitor” implemented as From |
| Risk | Spam folder; domain reputation |
| Prevention | From = `noreply@<domain>`; Reply-To = visitor only if valid |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §12 |
| Evidence | FP-0002 P18C |

## AP-027 — FORM-006 Mail suppression left forever after launch

| | |
|--|--|
| Symptom | MU `pre_wp_mail` still false after SMTP is live |
| Cause | Temporary suppress without retirement |
| Risk | Silent non-delivery |
| Prevention | Explicit VERIFIED + activate; then retire MU |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §11 |
| Evidence | FP-0002 P18C |

## AP-028 — FORM-007 SMTP “configured” confused with SMTP “verified”

| | |
|--|--|
| Symptom | Dashboard says SMTP ready because fields are non-empty |
| Cause | Completeness treated as proof |
| Risk | False launch claims |
| Prevention | Separate states; test action; no auto-activate on Save |
| Replacement | [FORMS-AND-SMTP](FORGE-WORDPRESS-FORMS-AND-SMTP-STANDARD-v1.md) §11 |
| Evidence | FP-0002 P18C |

---

## CMS modeling namespace (`AP-CMS-*`)

Do **not** reuse AP-001–021 numbers. Full entries: [CMS-ANTI-PATTERNS](FORGE-WORDPRESS-CMS-ANTI-PATTERNS-v1.md).

| ID | Title | Related ops ID |
|----|-------|----------------|
| AP-CMS-001 | Everything becomes a Page | AP-001 |
| AP-CMS-002 | Everything becomes an ACF repeater | — |
| AP-CMS-003 | Everything is editable | — |
| AP-CMS-004 | Same business value stored in multiple locations | AP-007, AP-008 |
| AP-CMS-005 | Internal destination stored as absolute manual URL | — |
| AP-CMS-006 | Editor exposed to raw CSS / classes | — |
| AP-CMS-007 | Giant flat ACF editor | — |
| AP-CMS-008 | Nested repeater as a pseudo-database | — |
| AP-CMS-009 | Demo content as production fallback | AP-009 |
| AP-CMS-010 | Frontend component without empty-state contract | AP-009 |
| AP-CMS-011 | GUI field-schema change without source / version control | — |
| AP-CMS-012 | WYSIWYG used instead of structured data | — |
| AP-CMS-013 | Hardcoded design copied into content fields unnecessarily | — |
| AP-CMS-014 | Relation modeled as free text | — |
| AP-CMS-015 | No editor workflow validation before launch | — |
| AP-CMS-016 | Stored false collapsed into default true | AP-020 |

---

*FW-S-21 v1.4 — 28 operational anti-patterns (AP-022–028 = FORM-001–007) + AP-CMS-001–016 index. Add IDs; do not reuse numbers.*
