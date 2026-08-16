# REPORT — FP-0002 PROD-P07 Olya UX/Admin Refinement

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p07-olya-ux-admin-refinement/`  
**Layer B:** `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-layer-b-pre\`

```text
FP-0002 OLYA UX/ADMIN REFINEMENT APPLIED ON BEGET — REUSABLE BLOCK OWNERSHIP CLARIFIED — APPROACH CARDS ADMIN PARITY RESTORED — DESKTOP CARD ALIGNMENT FIXED — GUEST VISIT CTA CONTEXT CORRECT — DEMO/TEST FRONTEND MARKERS CLEANED — IMPORTED CONTENT PRESERVED — SOURCE/PRODUCTION PARITY MAINTAINED
```

---

## 1. Status

* **PASS / PARTIAL**
* production file writes: **YES** (exact allowlisted theme/plugin/ACF JSON)
* DB/Admin writes: **YES** (bounded postmeta repairs + `#13` reusable selector)
* WPilot business writes: **0** (`write_enabled=false`)
* commit/push: **none**

PARTIAL residuals (deferred, not blockers for approved core):

* `/uslugi/` hub leaf cards still showing some `DEMO —` mini-descriptions
* alcohol leaf FAQ/signs still contain Lorem in non-approach fields

**Follow-up (2026-08-14):** Operator `P07 CONDITIONALLY ACCEPTED`. Residual closeout wave `PROD-P07-FU01` attempted and **BLOCKED** on missing post-P07 Layer A — see `REPORTS/REPORT-FP-0002-PROD-P07-FU01-RESIDUAL-DEMO-LOREM-CLEANUP.md`. No FU01 mutations.

---

## 2. Backup Gate

| Item | State |
|------|--------|
| Layer A | FU01 **OPERATOR CONFIRMED** post-reimport files+DB (same day). No separate post-FU01 full archive downloaded by MARS. |
| Layer B | **YES** — exact pre-overwrite snapshots of all deployed files outside WordPress |
| DB object snapshots | `db-before-mutations.txt` / `db-after-mutations.txt` (+ lorem cleanup notes) |
| Rollback readiness | **YES** per-file Layer B + per-object DB restore |

Recommendation: operator may refresh Beget full Layer A after this wave for a clean post-P07 restore point.

---

## 3. Ownership Map

Canonical evidence: `REPORTS/evidence/prod-p07-olya-ux-admin-refinement/OWNERSHIP-MAP.md`

| Component | Frontend | Admin/content | Fallback | CSS/JS |
|-----------|----------|---------------|----------|--------|
| Program cards + equal-height | `services-program-v2` partials | treatment-program children / section program fields | theme assets | `v9-style.css` |
| Approach cards | `team-stats.php` / leaf approach | `section_approach_cards` / `service_general_approach_cards` | sanitized reserve texts | feature-grid CSS |
| Guest Visit CTA | `program-cta-band` via `shpigovsky_get_about_guest_cta_band()` | static guest copy + phone option | static V9 guest strings | CTA band CSS |
| «Остались вопросы?» | `final-form` + service mid-CTA defaults | `fp02-block-final-form` / `cta_band_default_*` | static questions copy | final-form CSS |
| Rehab requirements | `home/rehabilitation-requirements.php` + subdivision `stages.php` | comfort options / section stages | static steps | rehab CSS |
| Generic body | `generic/content-page.php` | `generic_page_*` | empty hide | `.plain-page-content__body` |
| Reusable on Generic | same + comfort/rehab partials | `generic_page_reusable_blocks` | none (selection only) | reusable spacing CSS |

---

## 4. Card Alignment

* Implementation: `.services-program-v2__item` flex column; body `flex:1`; media `margin-top:auto`; mobile ≤1024 resets to natural height
* Desktop: images in a row share a common baseline
* Mobile: stacked natural heights (no forced empty equal-height)
* Routes: `/uslugi/`, `/uslugi/zavisimosti/`, `/o-centre/`, service leaves with program grid

---

## 5. Guest Visit CTA

| Context | Previous | New |
|---------|----------|-----|
| Subdivision stages («Что нужно…») | `shpigovsky_get_service_cta_band()` → «Остались вопросы?» | `shpigovsky_get_about_guest_cta_band()` → Guest Visit |
| Guest helper itself | inherited `cta_band_default_*` (polluted) | uses static Guest Visit copy only |
| Mid-CTA / Final form | «Остались вопросы?» | **unchanged** |
| Home rehab CTA / contacts / hub program CTA | Guest Visit | preserved |

---

## 6. Demo/Test Marker Cleanup

See `DEMO-TEST-MARKER-BEFORE-AFTER.md`.

Removed/fixed:

* `#73` `подробнее о программе ТЕСТ`
* `#84` `тест020` prefix
* Lorem/DEMO approach card texts on `#73/#77/#84`
* `#73` program/deps Lorem chrome
* `#11` about program Lorem + who-treat card Lorem

Preserved/deferred:

* legitimate Russian words containing «тест»
* revisions
* broader hub `DEMO —` short descriptions
* alcohol FAQ/signs Lorem

---

## 7. Approach Cards Admin Parity

| Item | Detail |
|------|--------|
| Prior owner | ACF `section_approach_cards`, but `#73` count meta empty + orphan 1-based rows → FE showed images only |
| Resulting owner | same repeater; rebuilt 0-based count; FE helper recovers orphans + sanitizes Lorem/DEMO |
| Admin UX | clearer instructions on section/general «Карточки подхода» |
| Frontend | `/uslugi/zavisimosti/` now renders approach cards with production-safe texts |

---

## 8. Reusable Blocks

| Item | Detail |
|------|--------|
| Supported page type | Generic Content (`page-templates/generic.php`) |
| Supported blocks | `rehab_requirements`, `about_home` (Comfort) |
| Storage | page checkbox `generic_page_reusable_blocks` (selection only) |
| Order | fixed: requirements → about_home |
| Duplication avoided | **YES** |
| Enabled on | page `#13` `/o-centre/programma-lecheniya/` |

---

## 9. Generic Content Long-Form

* Scoped typography for H2–H4, p, ul/ol, links, strong/em
* Readable `max-width: 820px`
* Vertical rhythm + footer-safe page padding preserved
* Validated on `/o-centre/programma-lecheniya/`

---

## 10. Demo/Fallback Visuals

| Finding | Action |
|---------|--------|
| Approach section images without cards | restored structured cards |
| Lorem emergency fallback in PHP | replaced with RU production-safe texts |
| Static program Lorem on o-centre | replaced in static helper + page `#11` ACF |
| Legitimate photography | preserved |

---

## 11. ACF

* Schema changes: **YES** — `group_fp02_page_generic_content` (+ reusable checkbox/message)
* Also Admin instruction text updates in section/general approach repeaters (PHP groups)
* Exact groups only — **no broad sync**
* Source/runtime: PHP `FieldGroups.php` + JSON deployed

---

## 12. Files Changed (source-owned)

Theme:

* `assets/css/v9-style.css` (prod-promoted then edited)
* `template-parts/service/stages.php`
* `template-parts/service/team-stats.php`
* `template-parts/service/alcohol-direct-v9/stages.php`
* `template-parts/generic/content-page.php`
* `template-parts/home/rehabilitation-requirements.php`
* `inc/institutional-helpers.php`
* `inc/institutional-about-v9-content.php`
* `inc/service-section-helpers.php`
* `inc/service-general-helpers.php`
* `inc/v9-static-content.php`
* `inc/fancybox-vendors.php`

Plugin:

* `src/Fields/FieldGroups.php`
* `src/Fields/ServiceSectionParity.php`
* `src/Fields/ServiceGeneralParity.php`

ACF JSON:

* `group_fp02_page_generic_content.json`

Docs/status:

* `PROJECT-STATUS.md`
* `REPORTS/evidence/prod-p07-olya-ux-admin-refinement/*`

---

## 13. Content/Admin Objects Changed

* `#73` approach cards + footer label + program/deps Lorem fields
* `#77` / `#84` approach cards; `#84` short_description prefix
* `#13` `generic_page_reusable_blocks`
* `#11` about program lead/intros + who-treat card texts

No full content dump. Details in evidence `db-mutation-map.json` / follow-up scripts.

---

## 14. Frontend QA

| Route | Desktop result |
|-------|----------------|
| `/uslugi/` | Guest Visit program CTA OK; residual DEMO mini-texts deferred |
| `/uslugi/zavisimosti/` | approach cards visible; stages Guest Visit; mid-CTA questions preserved; TEST foot gone; Lorem chrome cleaned |
| alcohol leaf | Guest Visit in stages; mid-CTA questions; residual FAQ/signs Lorem deferred |
| `/o-centre/` | Guest Visit restored; program Lorem cleaned |
| `/o-centre/programma-lecheniya/` | long-form + reusable rehab + comfort |
| Home / Contacts | no regression on required CTAs |

Public CSS hash MATCH local (`e7e51ec0…`); equal-height rule present.

---

## 15. Admin QA

* Approach cards: discoverable SoT + repaired rows on `#73/#77/#84`
* Generic reusable selector: present in schema + enabled on `#13`
* Imported Olya content otherwise preserved (no DB restore / no broad overwrite)
* Note: open Generic page `#13` once in wp-admin if ACF UI needs local group refresh after PHP/JSON deploy

---

## 16. Production/Source Parity

* Modified product surfaces: **MATCH** after exact deploy
* Pre-wave CSS drift (`aef44d1b…` prod vs old local `1ccc5a8f…`) **canonized** into source before edits

---

## 17. Write Safety

* WPilot `write_enabled`: **false**
* Content mutations: SSH-local MySQL bounded UPDATEs/INSERTs with before/after evidence
* Rollback: Layer B file restore + DB snapshot restore per object

---

## 18. Migration Tails (still deferred)

* broad `.test` cleanup
* `blogname` «локальная разработка»
* `WP_DEBUG` / `WP_ENVIRONMENT_TYPE`
* final `home`/`siteurl`
* HTTPS / sitemap / DNS cutover
* hub residual `DEMO —` short descriptions
* alcohol FAQ/signs Lorem residual

---

## 19. Secret Safety

* exposed values in Git/evidence: **0**
* tracked secrets: **0**

---

## 20. Git

* commit: **none**
* push: **none**
* foreign WIP: **untouched**

---

## 21. Next Recommendation

1. Operator visual acceptance of P07 on Beget (desktop card alignment + Admin approach rows + program page reusable blocks)
2. Optional fresh Beget Layer A after P07
3. Later wave: residual DEMO short-descriptions / alcohol FAQ Lorem
4. Separate charter: `PROD-P06` migration/environment normalization
5. DNS/HTTPS only after explicit cutover charter

Do not execute automatically.
