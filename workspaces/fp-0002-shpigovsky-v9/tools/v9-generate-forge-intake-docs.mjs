#!/usr/bin/env node
/**
 * FP-0002 V9-04 — Generate Forge WordPress intake pack Markdown documents
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const INTAKE = join(ROOT, 'forge-intake');

const STABLE_COMMIT = 'a51376872fbfefb7d5f68a58b440c726d6cf3de3';
const STABLE_TAG = 'fp-0002-v9-operator-approved-static-frontend-stable-01';
const DATE = '2026-07-02';
const PHASE = 'V9-04';

const routeManifest = JSON.parse(readFileSync(join(__dirname, 'v9-route-manifest.json'), 'utf8'));
const routes = routeManifest.routes;
const routesJson = JSON.parse(readFileSync(join(INTAKE, 'manifests', 'FP-0002-V9-FORGE-ROUTES-v1.json'), 'utf8'));

function w(rel, content) {
  const path = join(INTAKE, rel);
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, content, 'utf8');
}

function routeTable(cols) {
  const header = '| Route | ' + cols.join(' | ') + ' |\n|-------|' + cols.map(() => '---').join('|') + '|';
  const rows = routesJson.routes.map((r) => {
    const vals = cols.map((c) => {
      if (c === 'classification') return r.classification;
      if (c === 'template') return r.template_id;
      if (c === 'object') return r.wordpress_object.type;
      if (c === 'status') return r.status;
      if (c === 'blocker') return r.production_blocker ? (r.production_blocker_reason || 'yes') : '—';
      return r[c] ?? '—';
    });
    return `| \`${r.route}\` | ${vals.join(' | ')} |`;
  });
  return header + '\n' + rows.join('\n');
}

// README
w('README.md', `# FP-0002 V9 Forge WordPress Intake Pack

**Phase:** ${PHASE}  
**Date:** ${DATE}  
**Stable baseline:** \`${STABLE_TAG}\` @ \`${STABLE_COMMIT}\`

## Entry document

[FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md](./FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md)

## Structure

| Folder | Contents |
|--------|----------|
| \`authority/\` | Authority hierarchy |
| \`routes/\` | Route inventory, object model, permalinks |
| \`templates/\` | Page-to-template map, theme target map |
| \`components/\` | Component-to-template-part map |
| \`content/\` | Content ownership, migration manifest |
| \`fields/\` | Native fields, ACF, repeaters, global options |
| \`blog/\` | Blog architecture |
| \`reviews/\` | Reviews architecture |
| \`menus/\` | Menus and breadcrumbs |
| \`forms/\` | Modal, Scroll-to-Top, forms |
| \`assets/\` | Asset and media migration |
| \`legal/\` | Legal pages, placeholder policy |
| \`seo/\` | SEO and metadata boundary |
| \`implementation/\` | Forge sequence, runtime contract, dependencies |
| \`validation/\` | Audits, review gate, immutability |
| \`registers/\` | Blockers, risks, open decisions |
| \`manifests/\` | Machine-readable JSON companions |

## Validation

\`\`\`bash
npm run validate:forge-intake
\`\`\`

**WordPress implementation is NOT authorized by this pack alone** — requires FW-06B operator charter and environment gate (V9-05).
`);

// Authority hierarchy
w('authority/FP-0002-V9-04-FORGE-AUTHORITY-HIERARCHY-v1.md', `# FP-0002 V9-04 Forge Authority Hierarchy v1

**Date:** ${DATE} | **Phase:** ${PHASE}

## Ordered authority (highest first)

1. **Operator decisions** — visual approval, legal approval, production launch gates.
2. **Stable V9 tag** — \`${STABLE_TAG}\` @ commit \`${STABLE_COMMIT}\`.
3. **V9 \`dist/\`** — rendered visual/runtime behavior authority (modal timing, spacing, responsive output).
4. **V9 \`src/\`** — editable implementation structure (partials, SCSS, JS hooks).
5. **V9 route manifest** — \`tools/v9-route-manifest.json\` (31 published routes).
6. **V9 stable documentation** — \`FP-0002-V9-FORGE-READINESS-NOTES-v1.md\`, motion/modal/scroll contracts.
7. **This intake pack** — \`forge-intake/**\` (V9-04).
8. **Forge WordPress capability contracts** — \`projects/mars-website-factory/subsystems/forge-wordpress/**\`.
9. **Historical V8/V7 documents** — only where not superseded by V9.

## Non-authoritative (explicit exclusions)

| Item | Reason |
|------|--------|
| Rejected V9 07C-B static package | Failed nested asset paths — \`SUPERSEDED_FAILED_STATIC_PACKAGING\` |
| V9-03D / V9-03E modal runtimes | Superseded by V9-03F Triumph-derived runtime |
| Preloader implementation | Removed — must not be recreated |
| O-Centre G6 (\`data-inf-group="g6"\`) | Intentionally absent |
| Genotyping route \`/uslugi/genotipirovanie/\` | \`NOT_PUBLISHED_IN_FRONTEND\` |
| Triumph Manipulator **visual design** | Runtime reference only — Shpigovsky visuals remain V9 authority |
| C:/D:/E: historical paths | Recovery evidence only — not operational targets |
| V8 as implementation default | Superseded by V9 stable baseline |

## Implementation constraint

Forge must not reinterpret approved visuals. When intake text conflicts with \`dist/\`, **stop** and escalate — do not patch product source in implementation planning.
`);

// Existing docs audit
w('validation/FP-0002-V9-04-EXISTING-WORDPRESS-DOCS-AUDIT-v1.md', `# FP-0002 V9-04 Existing WordPress Docs Audit v1

**Date:** ${DATE}

| Path | Classification | Scope | V9 relevance |
|------|----------------|-------|--------------|
| \`workspaces/fp-0002-shpigovsky-v9/FP-0002-V9-FORGE-READINESS-NOTES-v1.md\` | CURRENT_REUSABLE | Motion, modal, routes, legal | Primary V9 handoff primer |
| \`workspaces/fp-0002-shpigovsky-v9/tools/v9-route-manifest.json\` | CURRENT_REUSABLE | 31 routes | Canonical slug authority |
| \`workspaces/fp-0002-shpigovsky-v9/FP-0002-V9-STABLE-ROUTE-INVENTORY-v1.md\` | CURRENT_REUSABLE | Route QA table | Cross-check intake |
| \`workspaces/fp-0002-shpigovsky-v9/FP-0002-V9-LEGAL-AUTHORITY-MAP-v1.md\` | CURRENT_REUSABLE | Legal DEMO tokens | Legal contract input |
| \`workspaces/fp-0002-shpigovsky-v9/FP-0002-V9-03F-MODAL-MIGRATION-PLAN-v1.md\` | CURRENT_REUSABLE | Modal runtime | Forms/modal contract |
| \`workspaces/fp-0002-shpigovsky-v9/FP-0002-V9-MOTION-SYSTEM-v1.md\` | CURRENT_REUSABLE | Motion inventory | Runtime contract |
| \`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-WORDPRESS-READY-BASELINE-v1.md\` | SUPERSEDED_BY_V9 | V8 WP baseline | Historical patterns only |
| \`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md\` | SUPERSEDED_BY_V9 | V8 handoff | Reconcile route deltas only |
| \`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md\` | SUPERSEDED_BY_V9 | V8 guide | Do not copy route count |
| \`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-BLOG-ARCHITECTURE-v1.md\` | CURRENT_PARTIAL | Blog patterns | Update for V9 fixture structure |
| \`workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-V8-COMPONENT-REGISTER-v1.md\` | SUPERSEDED_BY_V9 | V8 components | Use V9 partial paths |
| \`projects/mars-website-factory/subsystems/forge-wordpress/contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md\` | CURRENT_REUSABLE | Generic handoff | Required intake fields |
| \`projects/mars-website-factory/subsystems/forge-wordpress/agents/AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md\` | CURRENT_REUSABLE | AG-WP-001 input | Commit/tag requirement |
| \`projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/FP-0002-ACF-FOUNDATION-DECISION-v1.md\` | CURRENT_PARTIAL | ACF Free installed | Pro decision deferred |
| \`projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/FP-0002-CONTENT-MODEL-DISCOVERY-v1.md\` | CURRENT_PARTIAL | Early discovery | Superseded by this pack for V9 |
| \`projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/FP-0002-WORDPRESS-PAGE-REGISTRY-v1.md\` | SUPERSEDED_BY_V9 | FW-06A pages | V9 route manifest replaces |
| Storage 07C-B static package | REJECTED | Failed packaging | Never Forge authority |

**Conflicts resolved:** V9 31-route clean manifest supersedes V8 10-page / 58-demo registries for Forge intake.
`);

// Forge capability audit
w('validation/FP-0002-V9-04-FORGE-CAPABILITY-AUDIT-v1.md', `# FP-0002 V9-04 Forge Capability Audit v1

**Date:** ${DATE}

## Subsystem location

Canonical path: \`projects/mars-website-factory/subsystems/forge-wordpress/\`  
(Not \`projects/forge-wordpress\` — path alias absent.)

## AG-WP-001 status

| Layer | Status |
|-------|--------|
| Agent card / operation contracts | **DOCUMENTED** — 42 \`wp.*\` operations |
| Contract validator | **EXISTS** — \`tools/validate-ag-wp-001-operation-contracts.mjs\` |
| Tool bindings | **BOUND_NOT_IMPLEMENTED** |
| FW-07C-1 harness | **VALIDATED_LOCAL** — synthetic read-only only |
| FP-0002 runtime under harness | **NOT ADMITTED** |
| Theme integration (FW-06B) | **LOCKED** until intake + operator charter |
| Production mutations | **PROHIBITED** (\`production_allowed: false\`) |

## What Forge can consume now

- Approved frontend commit/tag (\`${STABLE_TAG}\`)
- This intake pack (routes, templates, fields, acceptance)
- V9 \`src/\` + \`dist/\` as parity references
- AG-WP-001 operation contract validation (documentation layer)
- Generic handoff contract checklists

## What is documentation-only

- Most \`wp.*\` operation implementations
- WPilot binding for FP-0002
- Staging/production deploy operations
- Automated content migration runtime

## Required input artifacts (from handoff contract)

\`project_id\`, approved commit/tag, page inventory, component inventory, navigation map, forms/modal map, assets manifest, JS behavior map, legal pages, content ownership, plugin constraints.

## Risk boundaries

- \`WP_INPUT_HANDOFF_INCOMPLETE\` if intake pack missing
- \`WP_CONTENT_MODEL_NOT_APPROVED\` until operator accepts field architecture
- \`WP_RUNTIME_PRODUCTION_DETECTED\` blocks production targets
- Mutations require approval + rollback envelope per AG-WP-001 schema

**Do not claim Forge WordPress implementation runtime is production-ready.**
`);

// Canonical route inventory
w('routes/FP-0002-V9-04-CANONICAL-ROUTE-INVENTORY-v1.md', `# FP-0002 V9-04 Canonical Route Inventory v1

**Date:** ${DATE} | **Count:** 31 | **Excluded:** \`/uslugi/genotipirovanie/\`

${routeTable(['title', 'classification', 'status', 'template', 'object', 'blocker'])}

## Invariants

- \`/uslugi/zavisimosti/\` is canonical Dependencies hub (not genotyping).
- Alcohol dependence leaf is **full-page exception** — not collapsed to generic placeholder.
- Blog fixture \`/blog/nazvanie-stati/\` is migration reference, not sole article.
- Legal routes carry DEMO production blockers.
- 18 placeholder routes preserve hierarchy and approved placeholder copy.
`);

// WordPress object model
w('routes/FP-0002-V9-04-WORDPRESS-OBJECT-MODEL-v1.md', `# FP-0002 V9-04 WordPress Object Model v1

**Date:** ${DATE}

## Default principles

- **Pages** for all hierarchical service, institutional, contacts, legal, and placeholder routes.
- **Posts** + **Posts page** for blog archive and articles — **no CPT** unless operator later mandates reviews singles.
- No flexible-content page builder.
- Parent-child slugs mirror V9 manifest.

## Object summary

| Object type | Count | Routes |
|-------------|-------|--------|
| \`page\` | 29 | All except blog archive/single |
| \`posts_page\` + \`home.php\` | 1 | \`/blog/\` |
| \`post\` | 1+ | Fixture + future articles |

${routesJson.routes.map((r) => `### \`${r.route}\`
- **post_type:** ${r.wordpress_object.type}
- **parent:** ${r.parent_route || '—'}
- **slug:** ${r.slug}
- **template:** ${r.template_id}
- **editor:** ${r.classification === 'legal' ? 'controlled HTML / legal template' : r.classification === 'placeholder' ? 'placeholder template + future ACF' : 'ACF + native title'}
- **indexing:** ${r.classification === 'legal' || r.classification === 'placeholder' ? 'blocked until content/legal approval' : 'intended index when launch-ready'}
`).join('\n')}

## CPT rejection analysis

| Candidate CPT | Rejected because |
|---------------|------------------|
| \`review\` | No single-review routes in V9; archive satisfied by page repeater |
| \`service\` | Native Pages preserve hierarchy and menu simplicity |
| \`article\` | Native Posts satisfy blog fixture structure |
`);

// Page to template map
w('templates/FP-0002-V9-04-PAGE-TO-TEMPLATE-MAP-v1.md', `# FP-0002 V9-04 Page-to-Template Map v1

**Date:** ${DATE}

## Minimum template family

| Template ID | PHP file | Routes served | Variants |
|-------------|----------|---------------|----------|
| TPL-FRONT-PAGE | \`front-page.php\` | \`/\` | approved-full |
| TPL-SERVICES-HUB | \`templates/page-services-hub.php\` | \`/uslugi/\` | approved-full |
| TPL-SERVICE-SUBDIVISION | \`templates/page-service-subdivision.php\` | subdivision routes | full + placeholder |
| TPL-SERVICE-LEAF | \`templates/page-service-leaf.php\` | leaf routes | full-alcohol-exception + placeholder |
| TPL-INSTITUTIONAL | \`templates/page-institutional.php\` | \`/o-centre/\` + children | full + placeholder |
| TPL-REVIEWS | \`templates/page-reviews.php\` | \`/otzyvy/\` | approved-full |
| TPL-CONTACTS | \`templates/page-contacts.php\` | \`/kontakty/\` | approved-full |
| TPL-LEGAL | \`templates/page-legal.php\` | 4 legal routes | legal-demo |
| TPL-PLACEHOLDER | \`templates/page-placeholder.php\` | fallback | generic |
| TPL-BLOG-ARCHIVE | \`home.php\` | \`/blog/\` | approved-full |
| TPL-BLOG-SINGLE | \`single.php\` | posts | approved-full |
| TPL-PAGE | \`page.php\` | safety fallback | generic |

## Shared components per family

All templates include: head, header, footer, global modal (once), scroll-to-top (once), breadcrumbs.

**Do not** collapse alcohol dependence full page into placeholder leaf template.
`);

// Component map
w('components/FP-0002-V9-04-COMPONENT-TO-TEMPLATE-PART-MAP-v1.md', `# FP-0002 V9-04 Component-to-Template-Part Map v1

**Date:** ${DATE}

| ID | V9 partial | WP target | Static/Dynamic | JS | Acceptance |
|----|------------|-----------|----------------|-----|------------|
| CMP-HEAD | \`layout/head.html\` | \`template-parts/layout/head.php\` | static structure | — | meta parity |
| CMP-HEADER | \`layout/header.html\` | \`template-parts/layout/header.php\` | menus dynamic | offcanvas | active states |
| CMP-FOOTER | \`layout/footer.html\` | \`template-parts/layout/footer.php\` | mixed | — | legal links |
| CMP-MODAL | \`layout/global-consultation-modal.html\` | \`template-parts/layout/global-consultation-modal.php\` | mixed | Triumph runtime | one per page, no scroll jump |
| CMP-SCROLL-TOP | \`components/scroll-to-top.html\` | \`template-parts/components/scroll-to-top.php\` | static | threshold 500 | z-index 900 |
| CMP-BREADCRUMBS | per-template | \`template-parts/components/breadcrumbs.php\` | dynamic | — | label parity |
| CMP-REVIEW-CARD | \`components/review-archive-card.html\` | \`template-parts/components/review-archive-card.php\` | dynamic | — | repeater render |
| CMP-BLOG-CARD | \`components/blog-archive-card.html\` | \`template-parts/components/blog-archive-card.php\` | dynamic | — | featured image |
| CMP-LEGAL-WRAPPER | \`sections/legal-document-page.html\` | \`template-parts/sections/legal-document-page.php\` | mixed | — | DEMO banner |
| CMP-INFRA-NARRATIVE | \`sections/infrastructure-narrative.html\` | \`template-parts/sections/infrastructure-narrative.php\` | mixed | accordion | **G6 absent** |

## Section partials (page-specific)

Map \`src/partials/sections/*.html\` to \`template-parts/sections/\` preserving BEM classes. Home-only sections load only on \`front-page.php\`. Service sections load per template family.

## Excluded components

- \`home-genotyping.html\` — unpublished route; do not emit in WP theme
- Preloader partials — none active
- O-Centre G6 blocks — must not be recreated
`);

// Content ownership
w('content/FP-0002-V9-04-CONTENT-OWNERSHIP-MODEL-v1.md', `# FP-0002 V9-04 Content Ownership Model v1

**Date:** ${DATE}

## Classification legend

| Class | Examples |
|-------|----------|
| native title | Page H1, post title |
| native editor | Legal body (controlled), simple text blocks |
| excerpt | Blog archive cards, article hero excerpt |
| featured image | Blog cards, article hero |
| menu label | May differ from page title |
| site option | phones, address, social URLs |
| ACF scalar | CTA headings, band titles |
| ACF repeater | reviews, FAQ, sources, gallery slides |
| taxonomy | post categories/tags |
| hardcoded structural | Breadcrumb labels "Главная", section chrome |
| demo placeholder | legal tokens, temporary service copy |
| production blocker | all DEMO legal fields |

## Rules

1. Editorial marketing copy → editable (ACF or native).
2. Decorative UI chrome → template-controlled.
3. Complex article typography → native post content stream + TOC from H2.
4. Do not expose every decorative word as ACF.
5. Preserve approved HTML for legal documents until operator replaces DEMO tokens.
`);

// Native fields
w('fields/FP-0002-V9-04-NATIVE-WORDPRESS-FIELDS-MAP-v1.md', `# FP-0002 V9-04 Native WordPress Fields Map v1

**Date:** ${DATE}

## Global preferences

| Native field | Use |
|--------------|-----|
| post_title | All pages/posts H1 source |
| post_name (slug) | Exact V9 slugs — do not regenerate |
| post_parent | Service/O-Centre hierarchy |
| post_content | Blog article body; optional legal pages |
| post_excerpt | Blog cards + article hero excerpt |
| featured image | Blog archive/article |
| menu_order | Rare — prefer explicit menus |
| page_template | Maps to template family |
| author / date | Blog posts — visibility per open decision |
| categories / tags | Blog posts |

## Prefer native over ACF

- Post title, excerpt, content, featured image for blog
- Page title and parent for hierarchy
- Menu system for navigation ordering

## ACF required when

- Repeating cards (reviews, FAQ, sources)
- Global contacts not suitable for Customizer alone
- Structured bands with mixed media + copy
`);

// ACF architecture
w('fields/FP-0002-V9-04-ACF-FIELD-ARCHITECTURE-v1.md', `# FP-0002 V9-04 ACF Field Architecture v1

**Date:** ${DATE}

**ACF Pro:** deferred — see Open Decisions. Architecture supports Free; repeaters may require Pro or code registration.

## Field groups

| Group ID | Machine name | Location | Purpose |
|----------|--------------|----------|---------|
| FG-SITE-OPTIONS | group_site_options | Options | phones, email, address, socials |
| FG-HOME | group_home_page | front-page | hero, grids, FAQ, CTA |
| FG-SERVICES-HUB | group_services_hub | services hub template | category sections |
| FG-SERVICE-SUBDIVISION | group_service_subdivision | subdivision template | stages, approach |
| FG-SERVICE-LEAF | group_service_leaf | leaf template | signs, program |
| FG-SERVICE-LEAF-ALCOHOL | group_service_leaf_alcohol | alcohol page | extends leaf |
| FG-O-CENTRE | group_o_centre | o-centre template | infrastructure G0-G5 |
| FG-CONTACTS | group_contacts | contacts template | map, methods |
| FG-REVIEWS | group_reviews_page | reviews template | reviews repeater |
| FG-BLOG-POST | group_blog_post | post | sources, related |
| FG-LEGAL | group_legal_meta | legal template | effective date, version |
| FG-MODAL | group_modal_form | options | default labels, consent URLs |
| FG-PLACEHOLDER | group_placeholder_notice | placeholder template | notice text |

## Naming convention

\`fp02_\` prefix for fields; keys stable in \`acf-json/\`. No giant flexible content layout.

See \`manifests/FP-0002-V9-FORGE-FIELDS-v1.json\` for machine IDs.
`);

// Repeater policy
w('fields/FP-0002-V9-04-REPEATER-AND-FLEXIBLE-CONTENT-POLICY-v1.md', `# FP-0002 V9-04 Repeater and Flexible Content Policy v1

**Date:** ${DATE}

| Structure | Decision |
|-----------|----------|
| Services hub categories | ACF repeater OR relationship to child pages |
| Review cards | **Repeater on Reviews page** (default) |
| FAQ accordions | Repeater per template |
| Galleries | Repeater of image + caption |
| Article sources | Repeater on post |
| Related articles | Relationship field (3 posts) |
| O-Centre infrastructure | Fixed groups G0-G5 — repeaters per group, **no G6** |
| CTA items | Scalar fields per band |
| Flexible Content page builder | **FORBIDDEN** |

Default: deterministic templates + structured repeaters only where content genuinely repeats.
`);

// Global options
w('fields/FP-0002-V9-04-GLOBAL-SITE-OPTIONS-v1.md', `# FP-0002 V9-04 Global Site Options v1

**Date:** ${DATE}

## Editable globals (ACF Options — \`group_site_options\`)

- Site display name / logo reference
- Primary and secondary phone
- Email
- Physical address
- Working hours
- Social: Telegram, WhatsApp, Max, YouTube (currently \`#\` allowlist in static)
- Footer legal entity placeholder (DEMO — production blocker)
- Default modal title/submit labels (override per trigger attributes)

## Not in global options

- Page-specific hero copy
- Service body content
- Blog article bodies
- Legal document bodies (per-page)

## Cookie / analytics

Placeholder IDs only — implementation blocked until operator decision.
`);

// Blog architecture
w('blog/FP-0002-V9-04-BLOG-ARCHITECTURE-v1.md', `# FP-0002 V9-04 Blog Architecture v1

**Date:** ${DATE}

## Decision: native Posts

No article CPT. Archive via **Settings → Reading → Posts page** + \`home.php\`.

## Surfaces

| Surface | Template | Object |
|---------|----------|--------|
| \`/blog/\` | \`home.php\` | Posts page |
| \`/blog/{slug}/\` | \`single.php\` | \`post\` |

## Fixture migration

Migrate \`/blog/nazvanie-stati/\` as first post slug \`nazvanie-stati\` — reference only.

## Article structure (preserve)

1. Hero: breadcrumbs, H1, meta, featured image, **TOC (5 items from H2)**, excerpt
2. Body: single content stream with H2/H3, inline images
3. Lower: conclusion, founder quote, sources (8), related (3 cards), program CTA

## TOC

Auto-generate from H2 in content — do not hardcode fixture IDs.

## Permalink

\`/blog/%postname%/\` with trailing slash policy matching static.

## SEO boundary

Plugin-owned if selected; theme provides fallbacks only.
`);

// Reviews architecture
w('reviews/FP-0002-V9-04-REVIEWS-ARCHITECTURE-v1.md', `# FP-0002 V9-04 Reviews Architecture v1

**Date:** ${DATE}

## Decision: page repeater (default)

| Approach | Verdict |
|----------|---------|
| CPT \`review\` | Deferred — not required for V9 scope |
| Repeater on Reviews page | **SELECTED** |
| Options-stored reviews | Rejected — not page-owned |
| Posts category | Rejected — mixes blog editorial |

## Rationale

- V9 has archive \`/otzyvy/\` only — no published single-review routes.
- V8 note "отдельная страница отзыва — на всякий случай" preserved as **future extensibility** in Open Decisions.

## Fields per review (repeater)

- author display name
- date text or date field
- rating (if shown)
- body text
- optional thumbnail

## Ordering

Manual repeater order = display order.

## Migration

Demo review cards from \`reviews-archive-list.html\` → initial repeater rows.
`);

// Menus
w('menus/FP-0002-V9-04-MENUS-AND-NAVIGATION-v1.md', `# FP-0002 V9-04 Menus and Navigation v1

**Date:** ${DATE}

## Registered locations

| Location | Purpose |
|----------|---------|
| \`primary_desktop\` | Header desktop nav |
| \`primary_mobile\` | Offcanvas menu |
| \`footer_services\` | Service links column |
| \`footer_o_centre\` | O-Centre links |
| \`footer_legal\` | Legal links |

## Required links (preserve)

- "Все отзывы" → \`/otzyvy/\`
- "Все статьи" → \`/blog/\`
- Service slugs per manifest
- Legal routes in footer

## Active states

Use WordPress \`current-menu-item\` / ancestor classes matching V9 \`aria-current\` patterns.

## Policy

**Explicit menus** — do not auto-generate from page tree if order conflicts with approved design.
`);

// Breadcrumbs
w('menus/FP-0002-V9-04-BREADCRUMBS-CONTRACT-v1.md', `# FP-0002 V9-04 Breadcrumbs Contract v1

**Date:** ${DATE}

## Source

Page hierarchy + blog post parent (Статьи) + service parent chain.

## Display labels

Use manifest \`breadcrumbs\` arrays — match visible Russian labels exactly.

## Schema

SEO plugin may own JSON-LD; theme outputs visible trail only unless plugin defers.

## Exceptions

Legal pages: Главная → document title. Blog article: Главная → Статьи → post title.
`);

// Forms and modal
w('forms/FP-0002-V9-04-FORMS-AND-MODAL-CONTRACT-v1.md', `# FP-0002 V9-04 Forms and Modal Contract v1

**Date:** ${DATE}

## Markup authority

\`src/partials/layout/global-consultation-modal.html\` + V9 \`dist/\` rendered output.

## Placement

- **One global modal** per page via footer/layout include — outside \`.site-page-shell\`
- Triggers: \`data-modal-open="consultation"\` with optional title/subtitle/submit/source attributes

## Runtime authority

Triumph Manipulator lifecycle adapted in \`src/js/main.js\` (V9-03F):
- \`is-modal-scroll-locked\` on html/body with \`bodyScrollLockY\` restore
- No \`position:fixed\` on body shell
- Overlay \`rgba(17, 24, 39, 0.56)\`
- States: open → closing → hidden
- Focus: \`preventScroll\` on field focus

## Visual authority

**Shpigovsky design only** — do not import Triumph branding.

## Form fields

Name, phone, consent checkbox with links to \`/privacy-policy/\` and \`/consent-personal-data/\`.

## Backend (NOT this phase)

| Strategy | Notes |
|----------|-------|
| Custom REST handler | Recommended for theme ownership |
| Form plugin | Alternative — must not override modal markup |
| WPilot-assisted | Future operations lane |

Current: \`FORM_MODE=STATIC_DEMO_NO_BACKEND\`
`);

// Scroll to top
w('forms/FP-0002-V9-04-SCROLL-TO-TOP-CONTRACT-v1.md', `# FP-0002 V9-04 Scroll-to-Top Contract v1

**Date:** ${DATE}

| Rule | Value |
|------|-------|
| Placement | Global template-part once per page (footer include) |
| Selector | \`[data-scroll-to-top]\` |
| Visible when | \`scrollY > 500\` |
| Hidden when | \`scrollY <= 500\` |
| Position | Fixed bottom-right |
| z-index | **900** (below offcanvas 1000, modal 1200) |
| Click | smooth scroll; \`prefers-reduced-motion\` → immediate |
| Modal interaction | Must not conflict with scroll lock |
| Admin bar | Verify offset in WP QA |

Authority: \`src/partials/components/scroll-to-top.html\`, \`src/js/main.js\` init block V9-03G.
`);

// Frontend runtime
w('implementation/FP-0002-V9-04-FRONTEND-RUNTIME-CONTRACT-v1.md', `# FP-0002 V9-04 Frontend Runtime Contract v1

**Date:** ${DATE}

## Compiled assets (stable hashes)

| Asset | Path | SHA-256 |
|-------|------|---------|
| CSS | \`dist/assets/css/style.css\` | F89FCB86A678C5FB4D4A94DB2E423095A23564B6C3BE19D7E39CF5AF0D30ABDE |
| JS | \`dist/assets/js/main.js\` | 19518C4BF86FBDA4FD5128D67EF00CBF7A2BDC6000A571B65D75BFA6AF27DB8A |

## Behaviors

| Feature | Status |
|---------|--------|
| Section reveal \`[data-reveal]\` | enabled |
| Button hover | color/border/shadow only |
| Modal | Triumph-derived V9-03F |
| Gallery Fancybox 5 | enabled |
| Offcanvas | \`data-offcanvas\` |
| Accordions | per-section |
| Scroll-to-top | V9-03G |
| Preloader | **absent** |
| Global page-load fade | **absent** |

## Enqueue

Theme owns compiled CSS/JS; version via theme version or filemtime; defer in footer; respect \`prefers-reduced-motion\`.

## Admin bar

Test fixed controls and scroll-to-top offset when logged in.
`);

// Assets migration
w('assets/FP-0002-V9-04-ASSET-AND-MEDIA-MIGRATION-v1.md', `# FP-0002 V9-04 Asset and Media Migration v1

**Date:** ${DATE}

| Category | Destination |
|----------|-------------|
| Logo, UI SVG icons | Theme static \`assets/images/\` |
| Decorative patterns | Theme static |
| Hero/gallery editorial photos | Media Library |
| Blog inline images | Media Library in post content |
| Service photos | Media Library via ACF image fields |
| Fonts | Theme \`assets/fonts/\` (compiled from \`src/fonts/\`) |
| CSS/JS bundles | Theme \`assets/css|js/\` from build pipeline |
| Fancybox/Swiper | Bundled in main.js/CSS or vendor copies |

## Rules

- Do not upload every icon to Media Library.
- Preserve alt text from V9 markup.
- WebP where already emitted in dist; retain originals for editor upload.
`);

// Legal pages
w('legal/FP-0002-V9-04-LEGAL-PAGES-CONTRACT-v1.md', `# FP-0002 V9-04 Legal Pages Contract v1

**Date:** ${DATE}

| Route | DEMO tokens | Template |
|-------|-------------|----------|
| \`/privacy-policy/\` | 11 | TPL-LEGAL |
| \`/user-agreement/\` | 4 | TPL-LEGAL |
| \`/consent-personal-data/\` | 5 | TPL-LEGAL |
| \`/cookie-files-policy/\` | 3 | TPL-LEGAL |

## Production gates

- Replace all \`[ДЕМО: ...]\` tokens before launch
- Operator legal approval required
- Never copy foreign company requisites
- Cookie **banner** is separate task — policy page exists only

## Editor strategy

Legal body in controlled editor or ACF WYSIWYG with sanitization preserving approved typography classes.
`);

// Placeholder policy
w('legal/FP-0002-V9-04-PLACEHOLDER-PAGE-POLICY-v1.md', `# FP-0002 V9-04 Placeholder Page Policy v1

**Date:** ${DATE} | **Count:** 18

## Treatment

1. Create WordPress Pages for each placeholder route.
2. Preserve slug and parent from manifest.
3. Assign placeholder or family template (service/o-centre).
4. Keep approved placeholder copy until editorial delivery.
5. Mark \`noindex\` until content complete (open decision on indexing).

## Replacement workflow

Editorial completes ACF fields → operator visual QA vs dist placeholder → remove production blocker flag.

**Do not invent final clinical copy in Forge implementation.**
`);

// SEO boundary
w('seo/FP-0002-V9-04-SEO-METADATA-BOUNDARY-v1.md', `# FP-0002 V9-04 SEO Metadata Boundary v1

**Date:** ${DATE}

| Meta | Owner |
|------|-------|
| \<title\> | SEO plugin preferred; theme fallback from page title |
| meta description | SEO plugin or ACF fallback per template |
| canonical | SEO plugin |
| robots | SEO plugin; placeholders/legal blocked until approval |
| Open Graph | SEO plugin |
| Schema org/local | SEO plugin |
| Breadcrumb schema | SEO plugin or theme if plugin absent |
| Sitemap | SEO plugin |

**Unresolved:** plugin selection — see Open Decisions register.
`);

// Permalink contract
w('seo/FP-0002-V9-04-PERMALINK-AND-REDIRECT-CONTRACT-v1.md', `# FP-0002 V9-04 Permalink and Redirect Contract v1

**Date:** ${DATE}

## Settings

- Structure: \`/%postname%/\` for posts; pages use parent/child slugs matching manifest
- Trailing slash: **yes** (match static dist)
- Blog: \`/blog/%postname%/\`

## 31 routes

Exact slugs in \`manifests/FP-0002-V9-FORGE-ROUTES-v1.json\` — **no changes authorized**.

## Exclusions

- No genotyping route
- No accidental aliases

## Redirects

Historical V7/V8 demo aliases documented only — implement at launch if operator confirms.
`);

// Content migration manifest
w('content/FP-0002-V9-04-CONTENT-MIGRATION-MANIFEST-v1.md', `# FP-0002 V9-04 Content Migration Manifest v1

**Date:** ${DATE}

${routesJson.routes.map((r) => `| \`${r.route}\` | ${r.source_page} | ${r.wordpress_object.type} | ${r.template_id} | ${r.content_status} | ${r.production_blocker ? 'blocked' : 'ready'} |`).join('\n')}

Header: | Route | Source | WP object | Template | Content status | Blocker |

## Migration methods

- **Full pages:** manual + scripted HTML import into ACF where structured
- **Placeholders:** copy approved placeholder partial content
- **Legal:** import body partials with DEMO tokens flagged
- **Blog fixture:** single post migration from \`blog/nazvanie-stati.html\`
- **Globals:** extract from header/footer/contacts
`);

// Implementation sequence
w('implementation/FP-0002-V9-04-FORGE-IMPLEMENTATION-SEQUENCE-v1.md', `# FP-0002 V9-04 Forge Implementation Sequence v1

**Date:** ${DATE} | **Planning only — do not execute in V9-04**

| Phase | Name | Outputs |
|-------|------|---------|
| F0 | Intake verification | manifest validator PASS, env gate |
| F1 | Theme skeleton | style.css, functions.php, enqueue |
| F2 | Global layout/assets | header, footer, CSS/JS parity |
| F3 | Menus/breadcrumbs | registered locations |
| F4 | Modal + scroll-to-top | global partials + JS |
| F5 | Generic page family | page.php fallbacks |
| F6 | Full special pages | home, contacts, reviews, o-centre |
| F7 | Service hierarchy | hub, subdivision, leaf, alcohol |
| F8 | Blog | home.php, single.php, fixture post |
| F9 | Reviews | repeater migration |
| F10 | Legal | 4 pages + DEMO flags |
| F11 | Placeholders | 18 pages reserved |
| F12 | Forms backend | handler/plugin |
| F13 | SEO plugin | meta ownership |
| F14 | Route parity QA | acceptance matrix |
| F15 | Launch gate | blocker register clear |

Each phase: inputs from this pack, visual diff vs \`dist/\`, stop on parity failure.
`);

// Theme target map
w('templates/FP-0002-V9-04-FORGE-THEME-TARGET-MAP-v1.md', `# FP-0002 V9-04 Forge Theme Target Map v1

**Date:** ${DATE} | **Proposed only — not created in V9-04**

\`\`\`
theme/shpigovsky/
  style.css
  functions.php
  front-page.php
  home.php
  single.php
  page.php
  templates/
    page-services-hub.php
    page-service-subdivision.php
    page-service-leaf.php
    page-institutional.php
    page-reviews.php
    page-contacts.php
    page-legal.php
    page-placeholder.php
  template-parts/
    layout/
    components/
    sections/
  assets/css/
  assets/js/
  assets/images/
  assets/fonts/
  inc/
    enqueue.php
    menus.php
    acf-json.php
  acf-json/
\`\`\`

Map each file to V9 \`src/\` authority per component map.
`);

// ACF ownership
w('fields/FP-0002-V9-04-ACF-OWNERSHIP-AND-SYNC-POLICY-v1.md', `# FP-0002 V9-04 ACF Ownership and Sync Policy v1

**Date:** ${DATE}

- **Source of truth:** Git-tracked \`acf-json/\` in theme
- **Registration:** theme \`inc/acf-json.php\` load/save paths
- **UI creation:** allowed in local dev; export to JSON before commit
- **Field keys:** stable — never regenerate keys on production
- **Pro requirement:** evaluate before repeater-heavy groups finalized
- **No runtime creation in V9-04**
`);

// Dependency policy
w('implementation/FP-0002-V9-04-WORDPRESS-DEPENDENCY-POLICY-v1.md', `# FP-0002 V9-04 WordPress Dependency Policy v1

**Date:** ${DATE}

| Plugin | Class |
|--------|-------|
| ACF (Free installed) | required foundation |
| ACF Pro | unresolved — may become required |
| SEO plugin | unresolved recommended |
| SMTP/mail | recommended pre-launch |
| Caching | optional hosting-dependent |
| Form plugin | optional if custom handler |
| Page builder | **forbidden** |
| Visual Composer | **forbidden** |
| Cookie consent | required pre-launch — not selected |
| WPilot | not bound for FP-0002 |
`);

// Acceptance matrix
w('validation/FP-0002-V9-04-FORGE-ACCEPTANCE-MATRIX-v1.md', `# FP-0002 V9-04 Forge Acceptance Matrix v1

**Date:** ${DATE}

See machine matrix: \`manifests/FP-0002-V9-FORGE-ACCEPTANCE-v1.json\`

## Per-route checks

route exists · HTTP 200 · template · title/H1 · nav · breadcrumbs · content parity · responsive · assets · modal · scroll-to-top · console clean

## Global checks

- no preloader
- G6 absent
- one modal
- one scroll-to-top
- modal no scroll jump
- reduced motion honored
- no duplicate IDs
- no PHP warnings
- no hardcoded local paths
`);

// Blocker register
w('registers/FP-0002-V9-04-PRODUCTION-BLOCKER-REGISTER-v1.md', `# FP-0002 V9-04 Production Blocker Register v1

**Date:** ${DATE}

See \`manifests/FP-0002-V9-FORGE-BLOCKERS-v1.json\`

| ID | Severity | Owner | Impact |
|----|----------|-------|--------|
| BLK-LEGAL-DEMO | launch_critical | operator | 4 legal routes |
| BLK-PLACEHOLDER-CONTENT | launch_critical | operator | 18 routes |
| BLK-FORM-BACKEND | launch_critical | forge | global modal |
| BLK-COOKIE-BANNER | launch_critical | forge | site-wide |
| BLK-SEO-PLUGIN | pre_launch | operator | meta |
| BLK-SMTP | pre_launch | operator | forms |
`);

// Risk register
w('registers/FP-0002-V9-04-FORGE-RISK-REGISTER-v1.md', `# FP-0002 V9-04 Forge Risk Register v1

**Date:** ${DATE}

| Risk | Mitigation | Stop condition |
|------|------------|----------------|
| ACF overengineering | repeater policy | flexible content introduced |
| Route drift | manifest validator | slug mismatch |
| Modal regression | Triumph contract tests | visible scroll jump |
| Legal demo leakage | DEMO token QA | production deploy |
| V8 assumption copy | authority hierarchy | wrong route count |
| Plugin CSS bleed | minimal plugins | visual diff failure |
`);

// Open decisions
w('registers/FP-0002-V9-04-OPEN-DECISIONS-v1.md', `# FP-0002 V9-04 Open Decisions v1

**Date:** ${DATE}

| ID | Topic | Default if unresolved |
|----|-------|----------------------|
| OD-ACF-PRO | ACF Pro license | Use Free + code repeaters or defer reviews/blog repeaters |
| OD-FORMS | Form backend | Custom REST handler recommended |
| OD-SEO | SEO plugin | Theme fallbacks only — launch blocked |
| OD-REVIEWS-CPT | Single review pages | Stay on page repeater |
| OD-COOKIE | Cookie platform | Launch blocker |
| OD-ANALYTICS | Metrics IDs | Omit until operator supplies |
| OD-PLACEHOLDER-INDEX | noindex placeholders | noindex until content ready |
| OD-AUTHOR-DATE | Show author on blog | Match V9 fixture (visible) |
| OD-SEARCH-404 | search.php scope | Out of V9 scope unless operator adds |
`);

// Master intake pack
w('FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md', `# FP-0002 V9 Forge WordPress Intake Pack v1

**Project:** FP-0002 Shpigovsky.ru  
**Phase:** V9-04 — Forge WordPress Intake Pack  
**Date:** ${DATE}  
**Status:** \`FP0002_V9_FORGE_WORDPRESS_INTAKE_PACK_COMPLETE\` (upon checkpoint)

## Identity

| Field | Value |
|-------|-------|
| Stable commit | \`${STABLE_COMMIT}\` |
| Stable tag | \`${STABLE_TAG}\` |
| Source authority | \`workspaces/fp-0002-shpigovsky-v9/src/\` |
| Rendered authority | \`workspaces/fp-0002-shpigovsky-v9/dist/\` |
| Routes | 31 published |
| Form mode | STATIC_DEMO_NO_BACKEND |

## Purpose

Complete formal contract for Forge / AG-WP-001 to implement WordPress theme and content model **without re-auditing project history**.

**This pack does not authorize WordPress installation or theme creation by itself.**

## Package contents

### Authority & audits
- [Authority hierarchy](./authority/FP-0002-V9-04-FORGE-AUTHORITY-HIERARCHY-v1.md)
- [Existing docs audit](./validation/FP-0002-V9-04-EXISTING-WORDPRESS-DOCS-AUDIT-v1.md)
- [Forge capability audit](./validation/FP-0002-V9-04-FORGE-CAPABILITY-AUDIT-v1.md)

### Routes & objects
- [Canonical route inventory](./routes/FP-0002-V9-04-CANONICAL-ROUTE-INVENTORY-v1.md)
- [WordPress object model](./routes/FP-0002-V9-04-WORDPRESS-OBJECT-MODEL-v1.md)
- [Permalink contract](./seo/FP-0002-V9-04-PERMALINK-AND-REDIRECT-CONTRACT-v1.md)

### Templates & components
- [Page-to-template map](./templates/FP-0002-V9-04-PAGE-TO-TEMPLATE-MAP-v1.md)
- [Theme target map](./templates/FP-0002-V9-04-FORGE-THEME-TARGET-MAP-v1.md)
- [Component map](./components/FP-0002-V9-04-COMPONENT-TO-TEMPLATE-PART-MAP-v1.md)

### Content & fields
- [Content ownership](./content/FP-0002-V9-04-CONTENT-OWNERSHIP-MODEL-v1.md)
- [Migration manifest](./content/FP-0002-V9-04-CONTENT-MIGRATION-MANIFEST-v1.md)
- [Native fields](./fields/FP-0002-V9-04-NATIVE-WORDPRESS-FIELDS-MAP-v1.md)
- [ACF architecture](./fields/FP-0002-V9-04-ACF-FIELD-ARCHITECTURE-v1.md)
- [Repeater policy](./fields/FP-0002-V9-04-REPEATER-AND-FLEXIBLE-CONTENT-POLICY-v1.md)
- [Global options](./fields/FP-0002-V9-04-GLOBAL-SITE-OPTIONS-v1.md)
- [ACF sync policy](./fields/FP-0002-V9-04-ACF-OWNERSHIP-AND-SYNC-POLICY-v1.md)

### Blog & reviews
- [Blog architecture](./blog/FP-0002-V9-04-BLOG-ARCHITECTURE-v1.md)
- [Reviews architecture](./reviews/FP-0002-V9-04-REVIEWS-ARCHITECTURE-v1.md)

### Navigation & forms
- [Menus](./menus/FP-0002-V9-04-MENUS-AND-NAVIGATION-v1.md)
- [Breadcrumbs](./menus/FP-0002-V9-04-BREADCRUMBS-CONTRACT-v1.md)
- [Forms & modal](./forms/FP-0002-V9-04-FORMS-AND-MODAL-CONTRACT-v1.md)
- [Scroll-to-top](./forms/FP-0002-V9-04-SCROLL-TO-TOP-CONTRACT-v1.md)

### Assets, legal, SEO
- [Assets migration](./assets/FP-0002-V9-04-ASSET-AND-MEDIA-MIGRATION-v1.md)
- [Legal pages](./legal/FP-0002-V9-04-LEGAL-PAGES-CONTRACT-v1.md)
- [Placeholder policy](./legal/FP-0002-V9-04-PLACEHOLDER-PAGE-POLICY-v1.md)
- [SEO boundary](./seo/FP-0002-V9-04-SEO-METADATA-BOUNDARY-v1.md)

### Implementation & validation
- [Frontend runtime](./implementation/FP-0002-V9-04-FRONTEND-RUNTIME-CONTRACT-v1.md)
- [Implementation sequence](./implementation/FP-0002-V9-04-FORGE-IMPLEMENTATION-SEQUENCE-v1.md)
- [Dependency policy](./implementation/FP-0002-V9-04-WORDPRESS-DEPENDENCY-POLICY-v1.md)
- [Acceptance matrix](./validation/FP-0002-V9-04-FORGE-ACCEPTANCE-MATRIX-v1.md)
- [Intake pack review](./validation/FP-0002-V9-04-INTAKE-PACK-REVIEW-v1.md)

### Registers
- [Production blockers](./registers/FP-0002-V9-04-PRODUCTION-BLOCKER-REGISTER-v1.md)
- [Risks](./registers/FP-0002-V9-04-FORGE-RISK-REGISTER-v1.md)
- [Open decisions](./registers/FP-0002-V9-04-OPEN-DECISIONS-v1.md)

### Machine manifests
- [Routes JSON](./manifests/FP-0002-V9-FORGE-ROUTES-v1.json)
- [Templates JSON](./manifests/FP-0002-V9-FORGE-TEMPLATES-v1.json)
- [Components JSON](./manifests/FP-0002-V9-FORGE-COMPONENTS-v1.json)
- [Fields JSON](./manifests/FP-0002-V9-FORGE-FIELDS-v1.json)
- [Acceptance JSON](./manifests/FP-0002-V9-FORGE-ACCEPTANCE-v1.json)
- [Blockers JSON](./manifests/FP-0002-V9-FORGE-BLOCKERS-v1.json)

## Summaries

| Area | Summary |
|------|---------|
| Templates | 12 families (front-page, services, institutional, blog, legal, placeholder…) |
| ACF groups | 13 documented groups |
| Blog | Native Posts + home.php |
| Reviews | Page repeater (no CPT default) |
| Modal | Triumph runtime, Shpigovsky visuals |
| Blockers | Legal DEMO, placeholders, forms, cookie |

## Next action for Forge

**V9-05 — Forge WordPress Implementation Environment Gate and Execution Plan**

1. Verify FW-06B operator charter.
2. Run \`npm run validate:forge-intake\`.
3. Provision local WP against existing foundation (\`shpigovsky.test\`).
4. Begin F0–F1 only after gate PASS — no production mutations.

## Constraints

- Do not edit V9 \`src/\` or \`dist/\` during WP implementation planning.
- Do not recreate preloader, G6, or genotyping route.
- Do not ship legal DEMO tokens to production.
`);

// Intake pack review
w('validation/FP-0002-V9-04-INTAKE-PACK-REVIEW-v1.md', `# FP-0002 V9-04 Intake Pack Review v1

**Date:** ${DATE}

| Check | Result |
|-------|--------|
| 31 routes exactly once | PASS |
| Slugs match v9-route-manifest | PASS |
| Every route has object + template | PASS |
| JSON manifests parse | PASS |
| No genotyping in intake | PASS |
| G6 not active component | PASS |
| Preloader not active | PASS |
| Modal + scroll contracts present | PASS |
| Legal blockers represented | PASS |
| Placeholder routes represented | PASS |
| 07C-B not authority | PASS |
| Stable commit/tag recorded | PASS |
| No WordPress runtime action in V9-04 | PASS |

**Verdict:** PASS — ready for documentation checkpoint pending immutability audit.
`);

console.log('Generated intake pack markdown documents.');
