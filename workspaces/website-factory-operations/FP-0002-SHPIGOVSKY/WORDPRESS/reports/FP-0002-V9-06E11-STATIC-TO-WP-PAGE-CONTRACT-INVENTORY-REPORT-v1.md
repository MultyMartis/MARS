# REPORT — FP-0002 V9-06E11 STATIC-TO-WP PAGE CONTRACT INVENTORY

**Date:** 2026-07-07  
**HEAD note:** Required E10 `a373e3fb` is ancestor; actual HEAD `6a51da94`; local/remote synced 0/0

## 1. Safety preflight

- Volume: X
- Label: AI WS
- Repository: X:\AI MARS
- Branch: mars/canonical-post-recovery
- Local HEAD: 6a51da9473740f9216b1f8fb563ab0850b4c4a1e
- Local short HEAD: 6a51da94
- Remote HEAD: 6a51da9473740f9216b1f8fb563ab0850b4c4a1e
- Remote short HEAD: 6a51da94
- Ahead: 0
- Behind: 0
- Foreign WIP: present (unrelated modified/untracked; not staged)
- Pre-existing staged files: none
- E10 ancestor check: PASS
- Result: PASS

## 2. Authorization and scope

- Operator authorization: V9-06E11 authorized
- Task mode: STATIC-TO-WP PAGE CONTRACT INVENTORY — NO REPAIR
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

## 3. Static V9 page inventory

**Authority:** `workspaces/fp-0002-shpigovsky-v9/src/pages/` (33 files) + `dist/` counterparts  
**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/static-v9-page-inventory.json`

| Static page | Type | Route | Sections | WP required status | Notes |
|---|---|---|---:|---|---|
| index.html | HOME | / | 19 | EXACT_V9_REQUIRED | CURRENT_DEMO_CONTENT |
| uslugi-v2.html | SERVICES_HUB | /uslugi/ | 9 | EXACT_V9_REQUIRED | CURRENT_DEMO_CONTENT |
| usluga-podrazdel-v1.html | SERVICE_SUBDIVISION | /uslugi/zavisimosti/ | 14 | EXACT_V9_REQUIRED | TEMPLATE_FIXTURE |
| usluga-konechnaya-v1.html | SERVICE_LEAF | /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | 17 | V9_LAYOUT_DEMO_CONTENT_ALLOWED | TEMPLATE_FIXTURE |
| kontakty.html | CONTACTS | /kontakty/ | 3 | EXACT_V9_REQUIRED | CURRENT_DEMO_CONTENT |
| otzyvy.html | REVIEWS | /otzyvy/ | 3 | V9_LAYOUT_DEMO_CONTENT_ALLOWED | CURRENT_DEMO_CONTENT |
| privacy-policy.html | LEGAL | /privacy-policy/ | 4 | OPERATOR_REAL_CONTENT | LEGAL_DEMO_PENDING_OPERATOR_DATA |
| user-agreement.html | LEGAL | /user-agreement/ | 4 | OPERATOR_REAL_CONTENT | LEGAL_DEMO_PENDING_OPERATOR_DATA |
| consent-personal-data.html | LEGAL | /consent-personal-data/ | 4 | OPERATOR_REAL_CONTENT | LEGAL_DEMO_PENDING_OPERATOR_DATA |
| cookie-files-policy.html | LEGAL | /cookie-files-policy/ | 4 | OPERATOR_REAL_CONTENT | LEGAL_DEMO_PENDING_OPERATOR_DATA |
| o-centre.html | INSTITUTIONAL | /o-centre/ | 3 | V9_LAYOUT_DEMO_CONTENT_ALLOWED | CURRENT_DEMO_CONTENT |
| blog.html | BLOG_INDEX | /blog/ | 5 | DEFERRED | CURRENT_DEMO_CONTENT |
| blog/nazvanie-stati.html | BLOG_ARTICLE | /blog/nazvanie-stati/ | 8 | DEFERRED | CURRENT_DEMO_CONTENT |
| uslugi/psihicheskoe-zdorovie.html | SERVICE_SUBDIVISION | /uslugi/psihicheskoe-zdorovie/ | 14 | DEMO_ONLY | PLACEHOLDER_PENDING_CONTENT |
| uslugi/rasstroystva-pischevogo-povedeniya.html | SERVICE_SUBDIVISION | /uslugi/rasstroystva-pischevogo-povedeniya/ | 14 | DEMO_ONLY | PLACEHOLDER_PENDING_CONTENT |
| 6× placeholder leaf pages (zavisimosti) | SERVICE_LEAF | various | 17 | DEMO_ONLY | PLACEHOLDER |
| 6× placeholder leaf pages (psihicheskoe) | SERVICE_LEAF | various | 17 | DEMO_ONLY | PLACEHOLDER |
| 3× placeholder leaf pages (rpp) | SERVICE_LEAF | various | 17 | DEMO_ONLY | PLACEHOLDER |
| 5× o-centre subpages | INSTITUTIONAL | /o-centre/* | varies | DEMO_ONLY | PLACEHOLDER |
| uslugi.html | OTHER | /uslugi/ (superseded) | — | — | Legacy; authority is uslugi-v2.html |
| uslugi/genotipirovanie.html | SERVICE_LEAF | /uslugi/genotipirovanie/ | — | EXACT_V9_REQUIRED | NOT_PUBLISHED_IN_FRONTEND manifest |

Full 33-row inventory: `architecture/FP-0002-V9-06E11-STATIC-V9-PAGE-INVENTORY-v1.md`

## 4. WordPress route inventory

**Runtime:** http://shpigovsky.test/ · DB `mars_wp_fp0002`  
**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/wp-route-inventory.json`

| Route | WP object | Template | Main/hero | Current stack | Notes |
|---|---|---|---|---|---|
| / | 4 | front-page.php | site-main--front / hero=yes | 19 sections MATCH static | DEMO content via ACF/fallbacks |
| /uslugi/ | 5 | services-hub.php | page-uslugi-v2__main / hero=yes | 9 sections class MATCH | CPT-driven groups |
| /uslugi/zavisimosti/ | 73 (service) | subdivision-stack | page-service-subdivision-v1 / hero=yes | 14 sections class MATCH | home partial reuse |
| /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | 74 | alcohol-stack | page-service-leaf-v1 / hero=yes | 18 classes match static | SEMANTIC_REBUILD inner markup |
| /kontakty/ | 20 | contacts.php | site-main--contacts / hero=no | 3 sections (breadcrumbs+body+steps) | contacts-body vs static contacts-map-body |
| /otzyvy/ | 18 | reviews.php | reviews archive / hero=no | archive-list + rehab-requirements | ADMIN_DYNAMIC_CONTENT |
| /privacy-policy/ | 3 | legal.php | page-plain-content / hero=no | breadcrumbs + legal-document | NATIVE_LEGAL_CONTENT; missing subnav/final-form |
| /user-agreement/ | 22 | legal.php | — | breadcrumbs + legal-document | same shell gap |
| /consent-personal-data/ | 23 | legal.php | — | breadcrumbs + legal-document | same |
| /cookie-files-policy/ | 24 | legal.php | — | breadcrumbs + legal-document | same |
| /o-centre/ | 11 | institutional.php | institutional / hero=yes | hero + narrative | not static o-centre stack |
| /blog/ | 19 | skeleton | shpigovsky-skeleton--blog-archive | 1 section skeleton | DEFERRED |
| /blog/nazvanie-stati/ | — | — | 404 | skeleton breadcrumbs | not published |
| /uslugi/psihicheskoe-zdorovie/ | 77 | subdivision-stack | subdivision / hero=yes | truncated vs static placeholder | DEMO_ACCEPTED |
| /uslugi/rasstroystva-pischevogo-povedeniya/ | 84 | subdivision-stack | subdivision / hero=yes | truncated vs static placeholder | DEMO_ACCEPTED |
| placeholder leaf routes | 75–87 | leaf-stack / placeholder | page-service-leaf-v1 | 7 sections (truncated) | leaf-stack 10 vs static 17 |

## 5. Static-to-WP route mapping contract

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/static-to-wp-route-mapping-contract.json`

| Static V9 source | WP route | Mapping confidence | Expected status | Notes |
|---|---|---|---|---|
| index.html | / | HIGH | EXACT_V9_REQUIRED | 19-section stack class MATCH |
| uslugi-v2.html | /uslugi/ | HIGH | EXACT_V9_REQUIRED | Semantic hub rebuild |
| usluga-podrazdel-v1.html | /uslugi/zavisimosti/ | HIGH | EXACT_V9_REQUIRED | Class MATCH; home partials |
| usluga-konechnaya-v1.html | /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | HIGH | V9_LAYOUT_DEMO_CONTENT_ALLOWED | E12 priority |
| kontakty.html | /kontakty/ | HIGH | EXACT_V9_REQUIRED | Wrapper/class drift |
| otzyvy.html | /otzyvy/ | HIGH | V9_LAYOUT_DEMO_CONTENT_ALLOWED | Admin dynamic OK |
| privacy-policy.html | /privacy-policy/ | HIGH | OPERATOR_REAL_CONTENT | E1 seeded copy |
| placeholder subdivisions/leaves | demo routes | HIGH | DEMO_ONLY | Classified DEMO_ACCEPTED |
| blog.html | /blog/ | HIGH | DEFERRED | Skeleton only |
| uslugi/genotipirovanie.html | /uslugi/genotipirovanie/ | UNMAPPED | EXACT_V9_REQUIRED | Not published in V9 manifest |

## 6. Section stack contract

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/section-stack-contract.json`

| Route | Static sections | WP sections | Result | Notes |
|---|---:|---:|---|---|
| / | 19 | 19 | MATCH | Content still DEMO via helpers |
| /uslugi/ | 9 | 9 | MATCH | Semantic CPT rebuild underneath |
| /uslugi/zavisimosti/ | 14 | 14 | MATCH | Home partial reuse risk |
| /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | 17 | 18 | SEMANTIC_REBUILD | Classes match; inner markup drift (E10) |
| /kontakty/ | 3 | 3 | SEMANTIC_REBUILD | contacts-body vs contacts-map-body |
| /otzyvy/ | 3 | 2 | SEMANTIC_REBUILD | Archive layout adapted D9-W |
| /privacy-policy/ | 4 | 2 | SEMANTIC_REBUILD | Missing subnav + final-form shell |
| placeholder leaves | 17 | 7 | SEMANTIC_REBUILD | leaf-stack truncated |
| /blog/ | 5 | 1 | SEMANTIC_REBUILD | DEFERRED |

**Governance note:** Per E10 contract §4, alcohol leaf class-level MATCH is **not** sufficient for visual PASS — classified SEMANTIC_REBUILD for E12 direct port.

## 7. Template provenance contract

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/template-provenance-contract.json`

| Template/partial | Used by | Provenance | Risk | Future use |
|---|---|---|---|---|
| alcohol-stack.php | alcohol leaf | SEMANTIC_RECONSTRUCTION | HIGH | REPLACE_WITH_DIRECT_V9 |
| leaf-stack.php | generic leaves | SEMANTIC_RECONSTRUCTION | BLOCKER | REPLACE_WITH_DIRECT_V9 |
| subdivision-stack.php | subdivisions | SEMANTIC_RECONSTRUCTION | HIGH | REPLACE_WITH_DIRECT_V9 |
| services-hub.php | /uslugi/ | SEMANTIC_RECONSTRUCTION | HIGH | REPLACE_WITH_DIRECT_V9 |
| front-page.php | / | V9_ADAPTED_PARTIAL | MEDIUM | KEEP_WITH_LIMITS |
| contacts.php | /kontakty/ | V9_ADAPTED_PARTIAL | MEDIUM | KEEP_WITH_LIMITS |
| reviews.php | /otzyvy/ | V9_ADAPTED_PARTIAL | MEDIUM | KEEP_WITH_LIMITS |
| legal.php | legal routes | V9_ADAPTED_PARTIAL | LOW | KEEP |
| v9-static-content.php | hub/alcohol | DEMO_FALLBACK | HIGH | DEPRECATE |
| home-fallbacks.php | home | DEMO_FALLBACK | HIGH | DEPRECATE |
| home/specialists.php | home+service | V9_ADAPTED_PARTIAL | MEDIUM | KEEP_WITH_LIMITS |
| home/reviews.php | home+service | V9_ADAPTED_PARTIAL | MEDIUM | KEEP_WITH_LIMITS |
| service/signs.php | leaves | DEMO_FALLBACK | HIGH | REPLACE_WITH_DIRECT_V9 |
| service/program.php | service routes | DEMO_FALLBACK | HIGH | REPLACE_WITH_DIRECT_V9 |

## 8. Content authority contract

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/content-authority-contract.json`

| Route | Expected content source | Current content source | Status | Notes |
|---|---|---|---|---|
| / | EXACT_V9_CONTENT | ACF+home-fallbacks | DEMO_CONTENT | mutation risk medium |
| /uslugi/ | EXACT_V9_CONTENT | v9-static-content+CPT | DEMO_CONTENT | mutation risk high |
| /uslugi/zavisimosti/ | EXACT_V9_CONTENT | ACF+helpers | DEMO_CONTENT | mutation risk medium |
| /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | EXACT_V9_CONTENT | v9-static+ACF #74 | V9_FIXTURE_DEMO | signs/hero ACF override risk |
| /kontakty/ | EXACT_V9_CONTENT | ACF+contacts-helpers | EXACT_V9_CONTENT | low risk |
| /otzyvy/ | V9_FIXTURE_DEMO | fp02-reviews options | ADMIN_DYNAMIC_CONTENT | operator-approved path |
| /privacy-policy/ | NATIVE_LEGAL_CONTENT | post_content E1 | NATIVE_LEGAL_CONTENT | operator review pending |
| legal ×3 | NATIVE_LEGAL_CONTENT | post_content E1 | NATIVE_LEGAL_CONTENT | same |
| /o-centre/ | V9_FIXTURE_DEMO | institutional template | DEMO_CONTENT | medium |
| /blog/ | DEFERRED | skeleton | UNKNOWN | deferred |
| placeholder leaves | DEFERRED | leaf-stack generic | DEMO_CONTENT | classify DEMO_ONLY |

## 9. Screenshot evidence

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/screenshot-manifest.json`  
**Index:** `validation/v9-06e11-static-to-wp-page-contract-inventory/visual-evidence-index.json`

| Evidence | Captured | Result | Notes |
|---|---:|---|---|
| static-v9-home.png | YES | PASS | dist/index.html |
| runtime-home.png | YES | PASS | http://shpigovsky.test/ |
| static-v9-uslugi-hub.png | YES | PASS | |
| runtime-uslugi-hub.png | YES | PASS | |
| static-v9-uslugi-zavisimosti-subdivision.png | YES | PASS | |
| runtime-uslugi-zavisimosti-subdivision.png | YES | PASS | |
| static-v9-alcohol-leaf.png | YES | PASS | |
| runtime-alcohol-leaf.png | YES | PASS | E12 baseline pair |
| static-v9-kontakty.png | YES | PASS | |
| runtime-kontakty.png | YES | PASS | |
| static-v9-otzyvy.png | YES | PASS | |
| runtime-otzyvy.png | YES | PASS | |
| static-v9-privacy-policy.png | YES | PASS | |
| runtime-privacy-policy.png | YES | PASS | |
| runtime-psihicheskoe-zdorovie.png | YES | PASS | demo route |
| runtime-rasstroystva-pischevogo-povedeniya.png | YES | PASS | demo route |

**16/16 captured — PASS**

## 10. Priority remediation matrix

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/priority-remediation-matrix.json`

| Route | Severity | Repair type | Recommended phase | Notes |
|---|---|---|---|---|
| /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | CRITICAL | DIRECT_V9_REPLACEMENT | E12 | screenshot=YES |
| /uslugi/ | HIGH | DIRECT_V9_REPLACEMENT | E13 | after E12 |
| /uslugi/zavisimosti/ | HIGH | SECTION_STACK_REPAIR | E13 | class MATCH; partial fork |
| / | HIGH | CONTENT_RESEED | E14 | stack MATCH |
| /kontakty/ | MEDIUM | DIRECT_V9_REPLACEMENT | E14 | screenshot=YES |
| /otzyvy/ | LOW | NO_ACTION | — | ADMIN_DYNAMIC_READY |
| legal routes | LOW | SECTION_STACK_REPAIR | E15+ | shell gaps only |
| placeholder leaves | LOW | DEMO_CLASSIFICATION_ONLY | — | DEMO_ACCEPTED |
| /blog/ | LOW | DEFER | — | DEFERRED |

## 11. Final page contract register

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/final-page-contract-register.json`

| Route | Final classification | Next action | Notes |
|---|---|---|---|
| /uslugi/.../lechenie-alkogolnoy-zavisimosti/ | NEEDS_DIRECT_V9_REPLACEMENT | DIRECT_V9_REPLACEMENT | E12 start |
| /uslugi/ | NEEDS_CONTENT_RESEED | CONTENT_RESEED | stack MATCH |
| /uslugi/zavisimosti/ | NEEDS_CONTENT_RESEED | CONTENT_RESEED | stack MATCH |
| / | NEEDS_CONTENT_RESEED | CONTENT_RESEED | stack MATCH |
| /kontakty/ | NEEDS_DIRECT_V9_REPLACEMENT | DIRECT_V9_REPLACEMENT | wrapper drift |
| /o-centre/ | NEEDS_DIRECT_V9_REPLACEMENT | DIRECT_V9_REPLACEMENT | institutional rebuild |
| /otzyvy/ | ADMIN_DYNAMIC_READY | NO_ACTION | |
| /privacy-policy/ | NEEDS_SECTION_STACK_REPAIR | SECTION_STACK_REPAIR | content OK |
| legal ×3 | NEEDS_SECTION_STACK_REPAIR | SECTION_STACK_REPAIR | |
| placeholder/demo routes | DEMO_ACCEPTED | DEMO_CLASSIFICATION_ONLY | |
| /blog/ | DEFERRED | NO_ACTION | |

## 12. No-scope-drift

**JSON:** `validation/v9-06e11-static-to-wp-page-contract-inventory/no-scope-drift-validation.json`

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
- Production migration: NO
- V9 src/dist changes: 0
- DB dumps staged: 0
- Backup payload staged: 0
- Runtime snapshots staged: 0
- Helpers/temp staged: 0
- Secrets/API keys: 0
- Result: PASS

## 13. Documentation changes

| File | Action | Reason |
|---|---|---|
| reports/FP-0002-V9-06E11-STATIC-TO-WP-PAGE-CONTRACT-INVENTORY-REPORT-v1.md | CREATE | Main E11 report |
| architecture/FP-0002-V9-06E11-STATIC-V9-PAGE-INVENTORY-v1.md | CREATE | Static page authority |
| architecture/FP-0002-V9-06E11-WP-ROUTE-INVENTORY-v1.md | CREATE | WP route inventory |
| architecture/FP-0002-V9-06E11-STATIC-TO-WP-ROUTE-MAPPING-CONTRACT-v1.md | CREATE | Route mapping |
| architecture/FP-0002-V9-06E11-SECTION-STACK-CONTRACT-v1.md | CREATE | Section stack contract |
| architecture/FP-0002-V9-06E11-TEMPLATE-PROVENANCE-CONTRACT-v1.md | CREATE | Template provenance |
| architecture/FP-0002-V9-06E11-CONTENT-AUTHORITY-CONTRACT-v1.md | CREATE | Content authority |
| architecture/FP-0002-V9-06E11-PRIORITY-REMEDIATION-MATRIX-v1.md | CREATE | E12+ sequence |
| architecture/FP-0002-V9-06E11-FINAL-PAGE-CONTRACT-REGISTER-v1.md | CREATE | Contract register |
| architecture/FP-0002-V9-06E11-NEXT-STEP-RECOMMENDATION-v1.md | CREATE | E12 recommendation |
| validation/v9-06e11-static-to-wp-page-contract-inventory/*.json | CREATE | Machine-readable contracts |
| validation/v9-06e11-static-to-wp-page-contract-inventory/screenshots/*.png | CREATE | Visual evidence |
| WORDPRESS/README.md | UPDATE | E11 status |
| WORDPRESS/SOURCE-AUTHORITY.md | UPDATE | E11 authority trace |
| FP-0002-SHPIGOVSKY/PROJECT-STATUS.md | UPDATE | E11 status |

## 14. Git checkpoint

- Exact staged files: (see commit wave)
- Staged list inspected: YES
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
- Commit: (pending)
- Commit hash: (pending)
- Push: (pending)
- Local HEAD: 6a51da94
- Remote HEAD: 6a51da94
- Result: PENDING

## 15. Final verdict

**PASS**

V9-06E11 Static-to-WP Page Contract Inventory: **COMPLETE**

Static V9 page inventory: **COMPLETE**

WP route inventory: **COMPLETE**

Static-to-WP mapping contract: **COMPLETE**

Section stack contract: **COMPLETE**

Template provenance contract: **COMPLETE**

Content authority contract: **COMPLETE**

Screenshot evidence: **PASS**

Final page contract register: **COMPLETE**

No-scope-drift: **PASS**

Recommended next phase: **E12 direct static V9 port — alcohol leaf**

## 16. Recommended next action

**CREATE_V9_06E12_DIRECT_STATIC_PORT_REPAIR_ALCOHOL_LEAF_TASK**

## 17. Final safety statement

Target folder:
X:\AI MARS

V9-06E11 Static-to-WP Page Contract Inventory performed:
YES

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
