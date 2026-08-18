# FP-0002 remaining knowledge gap map

**Date:** 2026-08-18  
**Wave:** Engineering / design-system / plugin-governance / production-operations assimilation  
**Does not replace:** [FP-0002-KNOWLEDGE-HARVEST-MAP](FP-0002-KNOWLEDGE-HARVEST-MAP.md) (ops+CMS harvest) or the CMS architecture pack.

**Method:** Compare FP-0002 production source/history against the two completed knowledge waves. Record only **recurring future-project problems** that were still implicit, project-local, scattered, or not operationalized.

**Classification (this wave):**

| Code | Meaning |
|------|---------|
| **CANONICAL DEFAULT** | New sites start with this unless a WAD says otherwise |
| **OPTIONAL STANDARD** | Use when the requirement exists |
| **OPERATIONS STANDARD** | How we run production, not a product feature |
| **QA STANDARD** | Acceptance / regression / device evidence |
| **SECOND-SITE VALIDATION** | Proven once; promote or reject after site #2 |
| **PROJECT-SPECIFIC / DO NOT GENERALIZE** | Clinical IA, brand, exact pixels, client URLs, credentials |

---

## Already canonical (do not duplicate)

| Area | Where it already lives |
|------|------------------------|
| Page / CPT / repeater / Options / P1b | CMS architecture pack (FW-S-22–31) |
| Site Settings SoT, Admin IA, editor UX | FW-S-11, FW-S-25, FW-S-26, FW-S-30 |
| Cutover, DNS/mail, indexing gate, hygiene | FW-RB-05–08, FW-S-20 |
| Source/runtime authority, exact-file deploy | FW-RB-01, FW-RB-02 |
| SEO/sitemap one-owner (high level) | FW-S-12 |
| Forms/SMTP sequencing | FW-S-13 |
| Real-device QA for compositor bugs | FW-S-17 |
| Theme vs plugin at FW-02 grain | FW-S-03, FW-S-04 |
| Plugin register (inventory fields) | FW-S-06 (2026-06-22) |

Those documents remain the SoT for their topics. This wave **adds** engineering shell, module lifecycle, design-system architecture, CSS/JS ownership, media, performance, plugin collision, updates, release classes, regression, observability, maintenance, handoff, and second-site bootstrap.

---

## Gaps found → closed this wave

| Recurring problem | Was | Now | Class |
|-------------------|-----|-----|-------|
| Theme still accumulates CPT/ACF/forms “because the template needs it” | Implicit in FW-S-03/04; not a survival test | [CODE-OWNERSHIP-BOUNDARIES](../standards/FORGE-WORDPRESS-CODE-OWNERSHIP-BOUNDARIES-STANDARD-v1.md) | CANONICAL DEFAULT |
| Modules lack ID/deps/Admin/endpoints/uninstall | FP-0002 `ModuleRegistry` is project code | [MODULE-LIFECYCLE](../standards/FORGE-WORDPRESS-MODULE-LIFECYCLE-STANDARD-v1.md) | CANONICAL DEFAULT |
| Disabled modules leave runners/menus/cron | `mars-runtime` + leftover importers | same + temporary-tool register | OPERATIONS STANDARD |
| Brand tokens copied as architecture | CSS in one huge `v9-style.css` + extras | [DESIGN-SYSTEM-FOUNDATION](../standards/FORGE-WORDPRESS-DESIGN-SYSTEM-FOUNDATION-v1.md) | CANONICAL DEFAULT (architecture only) |
| Duplicate card/header CSS/JS owners | Scattered theme CSS files | [CSS-COMPONENT-ARCHITECTURE](../standards/FORGE-WORDPRESS-CSS-COMPONENT-ARCHITECTURE-STANDARD-v1.md) · [COMPONENT-INVENTORY](../templates/FORGE-WORDPRESS-COMPONENT-INVENTORY-TEMPLATE-v1.md) | CANONICAL DEFAULT |
| Multiple JS libraries on one DOM state | Search/menu/slider/parallax lessons | [FRONTEND-INTERACTION-OWNERSHIP](../standards/FORGE-WORDPRESS-FRONTEND-INTERACTION-OWNERSHIP-STANDARD-v1.md) | CANONICAL DEFAULT |
| Stacked transform/fixed/contain on iOS | Documented as QA, not as frontend law | same (transform/scroll ownership) | QA STANDARD + CANONICAL DEFAULT |
| Accessibility = one DoD row | Not an acceptance layer | [ACCESSIBILITY-BASELINE](../standards/FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md) | CANONICAL DEFAULT (not WCAG cert) |
| `prefers-reduced-motion` discovered at launch | Implicit in DoD | [ACCESSIBILITY-BASELINE](../standards/FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md) § reduced motion | CANONICAL DEFAULT |
| Attachment IDs vs hardcoded host URLs | Project practice | [MEDIA-ARCHITECTURE](../standards/FORGE-WORDPRESS-MEDIA-ARCHITECTURE-STANDARD-v1.md) | CANONICAL DEFAULT |
| Custom image sizes / SVG / video policy | Implicit | same | CANONICAL DEFAULT / OPTIONAL |
| Performance = “make it fast later” | FW-D-09 tooling design only | [PERFORMANCE-BASELINE](../standards/FORGE-WORDPRESS-PERFORMANCE-BASELINE-v1.md) | OPERATIONS STANDARD |
| Several cache/minify/CDN plugins | FW-S-06 said “one cache” thinly | FW-S-06 addendum + performance ownership | CANONICAL DEFAULT |
| Domain change without purge checklist | Launch SOP mentions rewrite/cache | [PERFORMANCE-BASELINE](../standards/FORGE-WORDPRESS-PERFORMANCE-BASELINE-v1.md) § cutover purge | OPERATIONS STANDARD |
| Install another plugin without collision check | Register existed; install questions weak | [PLUGIN-GOVERNANCE](../standards/FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md) v1.1 | CANONICAL DEFAULT |
| “Update all” in production | Not an SOP | [PRODUCTION-UPDATE-SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md) | OPERATIONS STANDARD |
| No dependency/version register | Plugin register only | [DEPENDENCY-REGISTER](../templates/FORGE-WORDPRESS-DEPENDENCY-REGISTER-TEMPLATE-v1.md) | OPERATIONS STANDARD |
| Form UX (pending/errors/a11y) vs SMTP architecture | FW-S-13 is delivery sequencing | [FORMS-UX](../standards/FORGE-WORDPRESS-FORMS-UX-STANDARD-v1.md) | CANONICAL DEFAULT |
| UI success ≠ mail delivery | Pre-SMTP honesty only | same § observability | OPERATIONS STANDARD |
| Client editor vs site admin vs technical operator | Admin UX, not a capability model | [CONTENT-OPERATIONS](../standards/FORGE-WORDPRESS-CONTENT-OPERATIONS-STANDARD-v1.md) | CANONICAL DEFAULT (roles J if custom) |
| Programmer required for “change the phone” | CMS pack covers ownership; ops workflow missing | same | CANONICAL DEFAULT |
| No client handoff pack | WPilot handoff ≠ client editor guide | [CLIENT-HANDOFF](../templates/FORGE-WORDPRESS-CLIENT-HANDOFF-TEMPLATE-v1.md) | OPERATIONS STANDARD |
| Every change treated as cutover or as a typo | Wave model implicit | [CHANGE-RELEASE](../standards/FORGE-WORDPRESS-CHANGE-RELEASE-MANAGEMENT-STANDARD-v1.md) | OPERATIONS STANDARD |
| Dashboard version not tied to runtime | FP-0002 lesson in catalog | CHANGE-RELEASE § versioning | CANONICAL DEFAULT |
| Baseline = informal freeze | P14 practice | CHANGE-RELEASE § baseline | OPERATIONS STANDARD |
| Regression = whatever the agent remembers | QA matrix exists, not a pack | [REGRESSION-PACK](../standards/FORGE-WORDPRESS-REGRESSION-PACK-v1.md) | QA STANDARD |
| Testing on live content | Hygiene incident | REGRESSION-PACK § fixtures | QA STANDARD |
| All devices for every change | FW-S-17 is feature-triggered | REGRESSION-PACK § risk matrix | QA STANDARD |
| No bounded observability | Dashboard widget only | [OBSERVABILITY-DEBUG](../runbooks/FORGE-WORDPRESS-OBSERVABILITY-AND-DEBUG-STANDARD-v1.md) | OPERATIONS STANDARD |
| Persistent `debug.log` in webroot | FW-S-07 row | same | OPERATIONS STANDARD |
| Incidents without stop/snapshot/lesson | INC-01–10 exist as stories | [INCIDENT-RESPONSE](../runbooks/FORGE-WORDPRESS-INCIDENT-RESPONSE-SOP-v1.md) | OPERATIONS STANDARD |
| Post-launch maintenance undefined | Blueprint P14 thin | [POST-LAUNCH-MAINTENANCE](../runbooks/FORGE-WORDPRESS-POST-LAUNCH-MAINTENANCE-STANDARD-v1.md) | OPERATIONS STANDARD |
| Content vs design vs settings vs infra edits | Implicit | [CONTENT-OPERATIONS](../standards/FORGE-WORDPRESS-CONTENT-OPERATIONS-STANDARD-v1.md) § editor vs code | CANONICAL DEFAULT |
| Site #2 starts from blank theme | Blueprint day-1 list, not a bootstrap shell | [SECOND-SITE-BOOTSTRAP](../standards/FORGE-WORDPRESS-SECOND-SITE-BOOTSTRAP-v1.md) | CANONICAL DEFAULT |
| Extraction backlog without R1–R4 gates | [MODULE-EXTRACTION-BACKLOG](FORGE-WORDPRESS-MODULE-EXTRACTION-BACKLOG-v1.md) | [EXTRACTION-ROADMAP](FORGE-WORDPRESS-REUSABLE-CODE-EXTRACTION-ROADMAP-v1.md) | SECOND-SITE VALIDATION |
| `wp-forge-core` treated as if it existed | Explicit THEORY | [EXTRACTION-ROADMAP](FORGE-WORDPRESS-REUSABLE-CODE-EXTRACTION-ROADMAP-v1.md) § core candidate | SECOND-SITE VALIDATION |
| Screenshot parity = frontend done | DoD mentions empty states | [FRONTEND-ACCEPTANCE](../standards/FORGE-WORDPRESS-FRONTEND-ACCEPTANCE-STANDARD-v1.md) | QA STANDARD |
| Perfect demo content only | CMS anti-patterns | FRONTEND-ACCEPTANCE § stress tests | QA STANDARD |
| Temporary tools without REMOVE WHEN | AP-012 | MODULE-LIFECYCLE + [TEMPORARY-TOOL-REGISTER](../templates/FORGE-WORDPRESS-TEMPORARY-TOOL-REGISTER-TEMPLATE-v1.md) | OPERATIONS STANDARD |
| Forgotten launch flags (index/mail/debug) | Env migration | [ENVIRONMENT-FLAGS](../templates/FORGE-WORDPRESS-ENVIRONMENT-FLAGS-REGISTER-TEMPLATE-v1.md) | OPERATIONS STANDARD |
| Secrets / SVG / WPilot write hygiene scattered | FW-S-07, FW-S-20, FW-RB-09 | [SECURITY-OWNERSHIP](../standards/FORGE-WORDPRESS-SECURITY-OWNERSHIP-BASELINE-v1.md) | CANONICAL DEFAULT |
| Analytics/SMTP/maps depend on a developer laptop | Settings practice | [EXTERNAL-INTEGRATION-OWNERSHIP](../standards/FORGE-WORDPRESS-EXTERNAL-INTEGRATION-OWNERSHIP-STANDARD-v1.md) | CANONICAL DEFAULT |
| Maturity states collapsed (“we documented it so it ships”) | Maturity map started | [PRODUCTION-MATURITY-MAP](FORGE-WORDPRESS-PRODUCTION-MATURITY-MAP-v1.md) v1.1 | CANONICAL DEFAULT (discipline) |
| Site #2 has no validation charter | J items listed | [SECOND-PROJECT-VALIDATION](FORGE-WORDPRESS-SECOND-PROJECT-VALIDATION-PLAN-v1.md) | SECOND-SITE VALIDATION |
| Harvest stops at FP-0002 | FWP-12 exists as methodology | [EXPERIENCE-HARVEST-LOOP](FORGE-WORDPRESS-EXPERIENCE-HARVEST-LOOP-v1.md) | CANONICAL DEFAULT (process) |

---

## Project-specific / do not generalize

| Item | Why |
|------|-----|
| Clinical service tree, layout roles, medical taxonomies | Domain IA |
| Lifebuoy asset and brand motion values | Brand |
| Exact image pixel sizes from the Shpigovsky design | Design-dependent; **categories** are reusable |
| Exact legacy 301 list, phones, emails, staff names | Client |
| Reviews stored as options repeater | J — second site must re-decide |
| Service duplicate / layout governance modules | Proven locally; not CORE |
| Host-specific Beget jail / `*.beget.tech` paths | Hosting incident class is reusable; paths are not |
| `shpigovsky-core` PHP namespaces and text domain | Project plugin identity |

---

## Intentionally not closed (genuine second-project gaps)

| Gap | Why it stays open |
|-----|-------------------|
| Custom WordPress roles vs capability filters only | FP-0002 used editor restrictions; custom roles are J |
| Shared `wp-forge-core` package | Knowledge only; **no** extraction this wave |
| WCAG conformance claim | Baseline ≠ certification |
| Universal maintenance calendar (weekly/monthly dates) | Cadence **classes** exist; dates are operator/hosting-specific |
| AG-WP-001 production autonomy | Remains **NOT PRODUCTION READY** |

---

## CMS replay mapping (git)

| Role | SHA |
|------|-----|
| Approved local CMS commit (ISEO ancestry — **not** pushed) | `9b05bd38ce51e94958d277cc13ecdcc66203c75f` |
| Canonical replay on `origin/mars/canonical-post-recovery` | `0ed1c0440d36c13c03957a77972fdc7064181809` |

Foreign WIP on dirty main was not staged, restored, or pushed.

---

*Gap map v1 — every new standard in this wave traces to a row above.*
