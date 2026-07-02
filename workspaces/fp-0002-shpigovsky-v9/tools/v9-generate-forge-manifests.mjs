#!/usr/bin/env node
/**
 * FP-0002 V9-04 — Generate Forge WordPress intake JSON manifests from v9-route-manifest.json
 */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const MANIFEST_DIR = join(ROOT, 'forge-intake', 'manifests');

const STABLE_COMMIT = 'a51376872fbfefb7d5f68a58b440c726d6cf3de3';
const STABLE_TAG = 'fp-0002-v9-operator-approved-static-frontend-stable-01';
const PACK_VERSION = '1.0.0';

const routeManifest = JSON.parse(readFileSync(join(__dirname, 'v9-route-manifest.json'), 'utf8'));
const routes = routeManifest.routes;

const TEMPLATE_MAP = {
  HOME: { id: 'TPL-FRONT-PAGE', file: 'front-page.php', family: 'front-page' },
  SERVICES_HUB: { id: 'TPL-SERVICES-HUB', file: 'templates/page-services-hub.php', family: 'services-hub' },
  SERVICE_SUBDIVISION: { id: 'TPL-SERVICE-SUBDIVISION', file: 'templates/page-service-subdivision.php', family: 'service-subdivision' },
  SERVICE_LEAF: { id: 'TPL-SERVICE-LEAF', file: 'templates/page-service-leaf.php', family: 'service-leaf' },
  INSTITUTIONAL: { id: 'TPL-INSTITUTIONAL', file: 'templates/page-institutional.php', family: 'institutional' },
  REVIEWS: { id: 'TPL-REVIEWS', file: 'templates/page-reviews.php', family: 'reviews' },
  BLOG_ARCHIVE: { id: 'TPL-BLOG-ARCHIVE', file: 'home.php', family: 'blog-archive' },
  BLOG_ARTICLE: { id: 'TPL-BLOG-SINGLE', file: 'single.php', family: 'blog-single' },
  CONTACTS: { id: 'TPL-CONTACTS', file: 'templates/page-contacts.php', family: 'contacts' },
  LEGAL: { id: 'TPL-LEGAL', file: 'templates/page-legal.php', family: 'legal' },
};

function wpObject(r) {
  if (r.page_type === 'BLOG_ARCHIVE') return { type: 'posts_page', id: 'OBJ-BLOG-ARCHIVE' };
  if (r.page_type === 'BLOG_ARTICLE') return { type: 'post', id: 'OBJ-BLOG-FIXTURE', note: 'fixture reference; future posts use same template' };
  return { type: 'page', id: `OBJ-PAGE-${slugId(r.route)}` };
}

function slugId(route) {
  return route.replace(/^\/|\/$/g, '').replace(/\//g, '-') || 'home';
}

function templateFor(r) {
  if (r.status === 'PLACEHOLDER') {
    if (r.page_type === 'SERVICE_LEAF') return { ...TEMPLATE_MAP.SERVICE_LEAF, variant: 'placeholder' };
    if (r.page_type === 'SERVICE_SUBDIVISION') return { ...TEMPLATE_MAP.SERVICE_SUBDIVISION, variant: 'placeholder' };
    if (r.page_type === 'INSTITUTIONAL') return { ...TEMPLATE_MAP.INSTITUTIONAL, variant: 'placeholder' };
    return { id: 'TPL-PLACEHOLDER', file: 'templates/page-placeholder.php', family: 'placeholder', variant: 'generic' };
  }
  if (r.page_type === 'SERVICE_LEAF' && r.route.includes('lechenie-alkogolnoy-zavisimosti')) {
    return { ...TEMPLATE_MAP.SERVICE_LEAF, variant: 'full-alcohol-exception' };
  }
  const base = TEMPLATE_MAP[r.page_type];
  return base ? { ...base, variant: 'approved-full' } : { id: 'TPL-PAGE', file: 'page.php', family: 'generic' };
}

function parentRoute(route) {
  const parts = route.replace(/^\/|\/$/g, '').split('/');
  if (parts.length <= 1) return null;
  parts.pop();
  return '/' + parts.join('/') + '/';
}

function classify(r) {
  if (r.page_type === 'LEGAL' || r.status === 'LEGAL_DEMO_DOCUMENT') return 'legal';
  if (r.status === 'PLACEHOLDER') return 'placeholder';
  if (r.status === 'APPROVED_FULL') return 'full';
  return 'other';
}

mkdirSync(MANIFEST_DIR, { recursive: true });

const routeRecords = routes.map((r, i) => {
  const tpl = templateFor(r);
  const obj = wpObject(r);
  const slug = r.route === '/' ? 'home' : r.route.replace(/^\/|\/$/g, '');
  return {
    id: `ROUTE-${String(i + 1).padStart(2, '0')}`,
    route: r.route,
    slug,
    source_page: r.source_page,
    output: r.output,
    title: r.page_name,
    h1: r.page_name,
    page_type: r.page_type,
    classification: classify(r),
    status: r.status,
    content_status: r.content_status,
    wordpress_object: obj,
    template_id: tpl.id,
    template_file: tpl.file,
    template_variant: tpl.variant,
    parent_route: parentRoute(r.route),
    breadcrumbs: r.breadcrumbs,
    menu_exposure: r.menu_exposure,
    production_blocker: r.production_ready === false || r.status === 'LEGAL_DEMO_DOCUMENT' || r.status === 'PLACEHOLDER',
    production_blocker_reason:
      r.status === 'LEGAL_DEMO_DOCUMENT'
        ? 'LEGAL_DEMO_TOKENS'
        : r.status === 'PLACEHOLDER'
          ? 'PLACEHOLDER_CONTENT_PENDING'
          : null,
    wordpress_family: r.wordpress_family,
  };
});

const templates = {};
for (const rec of routeRecords) {
  if (!templates[rec.template_id]) {
    templates[rec.template_id] = {
      id: rec.template_id,
      file: rec.template_file,
      routes: [],
      variants: new Set(),
    };
  }
  templates[rec.template_id].routes.push(rec.route);
  templates[rec.template_id].variants.add(rec.template_variant);
}
const templateList = Object.values(templates).map((t) => ({
  id: t.id,
  file: t.file,
  route_count: t.routes.length,
  routes: t.routes,
  variants: [...t.variants],
}));

const components = [
  { id: 'CMP-HEAD', v9_partial: 'src/partials/layout/head.html', wp_path: 'template-parts/layout/head.php', scope: 'global', js: [], static: true },
  { id: 'CMP-HEADER', v9_partial: 'src/partials/layout/header.html', wp_path: 'template-parts/layout/header.php', scope: 'global', js: ['offcanvas'], static: 'mixed' },
  { id: 'CMP-FOOTER', v9_partial: 'src/partials/layout/footer.html', wp_path: 'template-parts/layout/footer.php', scope: 'global', js: [], static: 'mixed' },
  { id: 'CMP-BODY-START', v9_partial: 'src/partials/layout/body-start.html', wp_path: 'template-parts/layout/body-start.php', scope: 'global', js: [], static: true },
  { id: 'CMP-BREADCRUMBS', v9_partial: 'inline per template', wp_path: 'template-parts/components/breadcrumbs.php', scope: 'per-page', js: [], static: 'dynamic' },
  { id: 'CMP-MODAL', v9_partial: 'src/partials/layout/global-consultation-modal.html', wp_path: 'template-parts/layout/global-consultation-modal.php', scope: 'global-once', js: ['modal-triumph-runtime'], static: 'mixed' },
  { id: 'CMP-SCROLL-TOP', v9_partial: 'src/partials/components/scroll-to-top.html', wp_path: 'template-parts/components/scroll-to-top.php', scope: 'global-once', js: ['scroll-to-top'], static: true },
  { id: 'CMP-REVIEW-CARD', v9_partial: 'src/partials/components/review-archive-card.html', wp_path: 'template-parts/components/review-archive-card.php', scope: 'reviews', js: [], static: 'dynamic' },
  { id: 'CMP-BLOG-CARD', v9_partial: 'src/partials/components/blog-archive-card.html', wp_path: 'template-parts/components/blog-archive-card.php', scope: 'blog', js: [], static: 'dynamic' },
  { id: 'CMP-PLACEHOLDER-BC', v9_partial: 'src/partials/components/placeholder-breadcrumbs.html', wp_path: 'template-parts/components/placeholder-breadcrumbs.php', scope: 'placeholder', js: [], static: 'dynamic' },
  { id: 'CMP-LEGAL-WRAPPER', v9_partial: 'src/partials/sections/legal-document-page.html', wp_path: 'template-parts/sections/legal-document-page.php', scope: 'legal', js: [], static: 'mixed' },
  { id: 'CMP-BLOG-ARTICLE-CONTENT', v9_partial: 'src/partials/sections/blog-article-content.html', wp_path: 'template-parts/sections/blog-article-content.php', scope: 'single-post', js: ['toc-generate'], static: 'dynamic' },
  { id: 'CMP-BLOG-LOWER', v9_partial: 'src/partials/sections/blog-article-lower-stack.html', wp_path: 'template-parts/sections/blog-article-lower-stack.php', scope: 'single-post', js: [], static: 'dynamic' },
  { id: 'CMP-INFRA-NARRATIVE', v9_partial: 'src/partials/sections/infrastructure-narrative.html', wp_path: 'template-parts/sections/infrastructure-narrative.php', scope: 'o-centre', js: ['accordion'], static: 'mixed', note: 'G0-G5 only; G6 excluded' },
];

const fieldGroups = [
  { id: 'FG-SITE-OPTIONS', name: 'group_site_options', location: 'options', fields: ['site_phone_primary', 'site_phone_secondary', 'site_email', 'site_address', 'site_hours', 'social_telegram', 'social_whatsapp', 'social_max', 'social_youtube', 'footer_legal_entity_demo'] },
  { id: 'FG-HOME', name: 'group_home_page', location: 'front-page', fields: ['hero_slides', 'feature_grid', 'treatment_prevention', 'rehab_program', 'gallery', 'articles_teaser', 'faq', 'final_cta'] },
  { id: 'FG-SERVICES-HUB', name: 'group_services_hub', location: 'page-template-services-hub', fields: ['category_sections', 'program_band', 'founder_quote', 'comfort', 'mid_cta', 'faq'] },
  { id: 'FG-SERVICE-SUBDIVISION', name: 'group_service_subdivision', location: 'page-template-service-subdivision', fields: ['intro', 'nature', 'stages', 'approach', 'specialists', 'reviews_teaser', 'faq'] },
  { id: 'FG-SERVICE-LEAF', name: 'group_service_leaf', location: 'page-template-service-leaf', fields: ['intro', 'bordered_info', 'signs', 'approach', 'stages', 'program'] },
  { id: 'FG-SERVICE-LEAF-ALCOHOL', name: 'group_service_leaf_alcohol', location: 'page-lechenie-alkogolnoy-zavisimosti', fields: ['extends_group_service_leaf'], note: 'full-page exception template' },
  { id: 'FG-O-CENTRE', name: 'group_o_centre', location: 'page-template-o-centre', fields: ['infrastructure_groups_g0_g5', 'clinic_landscape', 'specialists', 'faq'] },
  { id: 'FG-CONTACTS', name: 'group_contacts', location: 'page-template-contacts', fields: ['contact_methods', 'map_embed', 'rehab_steps'] },
  { id: 'FG-REVIEWS', name: 'group_reviews_page', location: 'page-template-reviews', fields: ['reviews_repeater', 'requirements_band'] },
  { id: 'FG-BLOG-POST', name: 'group_blog_post', location: 'post', fields: ['reading_time_override', 'sources_repeater', 'related_posts', 'founder_quote_block'] },
  { id: 'FG-LEGAL', name: 'group_legal_meta', location: 'page-template-legal', fields: ['effective_date', 'document_version', 'demo_token_inventory'] },
  { id: 'FG-MODAL', name: 'group_modal_form', location: 'options', fields: ['default_modal_title', 'default_submit_label', 'consent_links', 'form_endpoint_placeholder'] },
  { id: 'FG-PLACEHOLDER', name: 'group_placeholder_notice', location: 'page-template-placeholder', fields: ['placeholder_notice_text'] },
];

const blockers = [
  { id: 'BLK-LEGAL-DEMO', severity: 'launch_critical', owner: 'operator', routes: routes.filter((r) => r.status === 'LEGAL_DEMO_DOCUMENT').map((r) => r.route), resolution: 'Replace DEMO tokens with approved legal data' },
  { id: 'BLK-PLACEHOLDER-CONTENT', severity: 'launch_critical', owner: 'operator', routes: routes.filter((r) => r.status === 'PLACEHOLDER').map((r) => r.route), resolution: 'Complete editorial content before launch indexing' },
  { id: 'BLK-FORM-BACKEND', severity: 'launch_critical', owner: 'forge', routes: ['global-modal'], resolution: 'Implement form handler; currently STATIC_DEMO_NO_BACKEND' },
  { id: 'BLK-COOKIE-BANNER', severity: 'launch_critical', owner: 'forge', routes: ['global'], resolution: 'Cookie consent banner not implemented' },
  { id: 'BLK-SEO-PLUGIN', severity: 'pre_launch', owner: 'operator', routes: ['global'], resolution: 'Select SEO plugin and meta ownership' },
  { id: 'BLK-SMTP', severity: 'pre_launch', owner: 'operator', routes: ['global-modal'], resolution: 'Configure mail delivery' },
];

const acceptance = routeRecords.map((r) => ({
  route_id: r.id,
  route: r.route,
  checks: {
    route_exists: true,
    http_200: true,
    template_id: r.template_id,
    title_h1_match: true,
    breadcrumbs_match: true,
    modal_present: true,
    scroll_to_top_present: true,
    responsive_parity: true,
    content_parity_vs_dist: r.classification === 'full',
    legal_demo_blocker: r.classification === 'legal',
    placeholder_blocker: r.classification === 'placeholder',
    console_clean: true,
    admin_editable: r.classification !== 'legal' || 'controlled_html',
  },
}));

const baseMeta = {
  schema: 'fp-0002-v9-forge-intake',
  version: PACK_VERSION,
  generated: new Date().toISOString().slice(0, 10),
  stable_commit: STABLE_COMMIT,
  stable_tag: STABLE_TAG,
  route_count: routes.length,
  excluded_routes: routeManifest.unpublished_routes?.map((u) => u.route) || [],
};

writeFileSync(join(MANIFEST_DIR, 'FP-0002-V9-FORGE-ROUTES-v1.json'), JSON.stringify({ ...baseMeta, routes: routeRecords }, null, 2));
writeFileSync(join(MANIFEST_DIR, 'FP-0002-V9-FORGE-TEMPLATES-v1.json'), JSON.stringify({ ...baseMeta, templates: templateList }, null, 2));
writeFileSync(join(MANIFEST_DIR, 'FP-0002-V9-FORGE-COMPONENTS-v1.json'), JSON.stringify({ ...baseMeta, components }, null, 2));
writeFileSync(join(MANIFEST_DIR, 'FP-0002-V9-FORGE-FIELDS-v1.json'), JSON.stringify({ ...baseMeta, field_groups: fieldGroups }, null, 2));
writeFileSync(join(MANIFEST_DIR, 'FP-0002-V9-FORGE-ACCEPTANCE-v1.json'), JSON.stringify({ ...baseMeta, global_checks: ['no_preloader', 'no_g6', 'one_modal', 'one_scroll_to_top', 'modal_no_scroll_jump', 'reduced_motion'], acceptance }, null, 2));
writeFileSync(join(MANIFEST_DIR, 'FP-0002-V9-FORGE-BLOCKERS-v1.json'), JSON.stringify({ ...baseMeta, blockers }, null, 2));

console.log('Generated 6 manifests in', MANIFEST_DIR);
console.log('Routes:', routeRecords.length);
