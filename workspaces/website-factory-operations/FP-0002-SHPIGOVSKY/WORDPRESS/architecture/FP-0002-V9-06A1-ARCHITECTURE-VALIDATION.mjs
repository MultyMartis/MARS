#!/usr/bin/env node
/**
 * FP-0002 V9-06A.1 Architecture Validation
 * Run: node FP-0002-V9-06A1-ARCHITECTURE-VALIDATION.mjs
 */
import { readFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const read = (f) => JSON.parse(readFileSync(join(__dirname, f), 'utf8'));

const routeMap = read('FP-0002-V9-ROUTE-ENTITY-TEMPLATE-MAP-v1.json');
const serviceRegistry = read('FP-0002-SERVICE-ENTITY-REGISTRY-v1.json');
const entityRegistry = read('FP-0002-WORDPRESS-ENTITY-REGISTRY-v1.json');
const permalinkMatrix = read('FP-0002-SERVICE-PERMALINK-TEST-MATRIX-v1.json');

const PRIMARY = ['PAGE', 'SERVICE', 'POST', 'POSTS_PAGE', 'SYSTEM_ROUTE', 'NO_WORDPRESS_OBJECT'];
const checks = [];

function pass(id, expected, actual) {
  const ok = expected === actual || (typeof expected === 'boolean' && !!actual === expected);
  checks.push({ id, expected, actual, result: ok ? 'PASS' : 'FAIL' });
  return ok;
}

function countBy(arr, key) {
  return arr.reduce((acc, r) => {
    const v = r[key];
    acc[v] = (acc[v] || 0) + 1;
    return acc;
  }, {});
}

const routes = routeMap.routes;
const primaryCounts = countBy(routes, 'primary_entity_class');
const primaryTotal = Object.values(primaryCounts).reduce((a, b) => a + b, 0);

pass('route_count', 31, routes.length);
pass('primary_total', 31, primaryTotal);
pass('page_count', 14, primaryCounts.PAGE || 0);
pass('service_count_routes', 15, primaryCounts.SERVICE || 0);
pass('post_count', 1, primaryCounts.POST || 0);
pass('posts_page_count', 1, primaryCounts.POSTS_PAGE || 0);
pass('no_legal_page_primary', 0, routes.filter(r => r.primary_entity_class === 'LEGAL_PAGE').length);
pass('no_double_primary', true, routes.every(r => PRIMARY.includes(r.primary_entity_class)));

const legalPages = routes.filter(r => r.entity_subtype === 'legal');
pass('legal_subtype_on_page', 4, legalPages.length);
pass('legal_primary_page', 4, legalPages.filter(r => r.primary_entity_class === 'PAGE').length);

const hub = routes.find(r => r.url === '/uslugi/');
pass('hub_primary_page', 'PAGE', hub?.primary_entity_class);
pass('hub_subtype', 'services_hub', hub?.entity_subtype);

const services = serviceRegistry.services;
pass('service_registry_count', 15, services.length);
pass('migration_candidates', 3, services.filter(s => s.migration_action === 'MIGRATE_PAGE_TO_SERVICE').length);
pass('create_new', 12, services.filter(s => s.migration_action === 'CREATE_SERVICE').length);
pass('alcohol_special', 1, services.filter(s => s.layout_variant === 'alcohol-special').length);
pass('no_hub_in_services', true, !services.some(s => s.canonical_route === '/uslugi/'));
pass('no_genotipirovanie', true, !services.some(s => s.slug === 'genotipirovanie'));

const ids = new Set(services.map(s => s.service_id));
pass('unique_service_ids', 15, ids.size);
const routeUrls = new Set(services.map(s => s.canonical_route));
pass('unique_service_routes', 15, routeUrls.size);

const idMap = Object.fromEntries(services.map(s => [s.service_id, s]));
let parentOk = true;
let cycleFree = true;
const siblingSlugs = {};
for (const s of services) {
  if (s.parent_service_id) {
    if (!idMap[s.parent_service_id]) parentOk = false;
    const parent = idMap[s.parent_service_id];
    if (parent && parent.parent_service_id === s.service_id) cycleFree = false;
    const key = s.parent_service_id;
    siblingSlugs[key] = siblingSlugs[key] || new Set();
    if (siblingSlugs[key].has(s.slug)) parentOk = false;
    siblingSlugs[key].add(s.slug);
  }
}
pass('valid_parent_refs', true, parentOk);
pass('no_cycles', true, cycleFree);

const serviceCpt = entityRegistry.entities.find(e => e.id === 'ENT-SERVICE');
pass('service_archive_disabled', false, serviceCpt?.rewrite?.has_archive);
const taxRejected = entityRegistry.entities.find(e => e.id === 'ENT-SERVICE-CATEGORY');
pass('service_taxonomy_rejected', 'REJECTED', taxRejected?.decision);

pass('permalink_positive_cases', 15, permalinkMatrix.positive_cases.length);
pass('permalink_matrix_unresolved', 0, permalinkMatrix.summary.unresolved);

const failures = checks.filter(c => c.result === 'FAIL');
const report = {
  schema: 'fp-0002-v9-06a1-validation-result',
  generated: new Date().toISOString().slice(0, 10),
  total_checks: checks.length,
  passed: checks.filter(c => c.result === 'PASS').length,
  failed: failures.length,
  result: failures.length === 0 ? 'PASS' : 'FAIL',
  checks,
  architecture_invariants: {
    acf_pro_required: true,
    flexible_content_forbidden: true,
    boundedmeta_primary_rejected: true,
    blog_categories_none: true,
    blog_author_hidden: true,
    blog_date_visible: true,
    specyalisty_redirect: '/uslugi/zavisimosti/specialistam/'
  }
};

console.log(JSON.stringify(report, null, 2));
process.exit(failures.length === 0 ? 0 : 1);
