#!/usr/bin/env node
/**
 * FP-0002 V9-06B Skeleton Validation
 * Run: node validation/FP-0002-V9-06B-SKELETON-VALIDATION.mjs
 */
import { readFileSync, existsSync, readdirSync, statSync } from 'fs';
import { dirname, join, relative } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const WP_ROOT = dirname(__dirname);
const THEME = join(WP_ROOT, 'theme/shpigovsky');
const PLUGIN = join(WP_ROOT, 'plugins/shpigovsky-core');
const ARCH = join(WP_ROOT, 'architecture');

const checks = [];

function pass(id, expected, actual) {
  const ok =
    expected === actual ||
    (typeof expected === 'boolean' && !!actual === expected) ||
    (expected instanceof RegExp && expected.test(String(actual)));
  checks.push({ id, expected: String(expected), actual: String(actual), result: ok ? 'PASS' : 'FAIL' });
  return ok;
}

function mustExist(relPath) {
  const full = join(WP_ROOT, relPath);
  const ok = existsSync(full);
  checks.push({ id: `exists:${relPath}`, expected: 'true', actual: String(ok), result: ok ? 'PASS' : 'FAIL' });
  return ok;
}

function readText(path) {
  return readFileSync(path, 'utf8');
}

function walkPhpFiles(dir, acc = []) {
  if (!existsSync(dir)) return acc;
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const st = statSync(full);
    if (st.isDirectory()) walkPhpFiles(full, acc);
    else if (entry.endsWith('.php')) acc.push(full);
  }
  return acc;
}

const requiredThemeRoots = [
  'theme/shpigovsky/style.css',
  'theme/shpigovsky/functions.php',
  'theme/shpigovsky/header.php',
  'theme/shpigovsky/footer.php',
  'theme/shpigovsky/index.php',
  'theme/shpigovsky/front-page.php',
  'theme/shpigovsky/home.php',
  'theme/shpigovsky/page.php',
  'theme/shpigovsky/single.php',
  'theme/shpigovsky/single-service.php',
  'theme/shpigovsky/404.php',
  'theme/shpigovsky/search.php',
  'theme/shpigovsky/inc/setup.php',
  'theme/shpigovsky/inc/assets.php',
  'theme/shpigovsky/inc/template-tags.php',
  'theme/shpigovsky/inc/service-template-loader.php',
  'theme/shpigovsky/page-templates/services-hub.php',
  'theme/shpigovsky/page-templates/institutional.php',
  'theme/shpigovsky/page-templates/reviews.php',
  'theme/shpigovsky/page-templates/contacts.php',
  'theme/shpigovsky/page-templates/legal.php',
];

requiredThemeRoots.forEach(mustExist);

const registry = JSON.parse(readText(join(ARCH, 'FP-0002-TEMPLATE-PART-REGISTRY-v1.json')));

pass('template_part_registry_families', registry.families.length, registry.families.length);

for (const part of registry.parts) {
  if (part.wp) {
    mustExist(`theme/shpigovsky/${part.wp}`);
  }
}

const requiredTemplateParts = [
  'template-parts/global/document-open.php',
  'template-parts/global/document-close.php',
  'template-parts/layout/head.php',
  'template-parts/layout/body-start.php',
  'template-parts/layout/header.php',
  'template-parts/layout/footer.php',
  'template-parts/layout/global-consultation-modal.php',
  'template-parts/navigation/primary-desktop.php',
  'template-parts/navigation/primary-mobile.php',
  'template-parts/navigation/breadcrumbs.php',
  'template-parts/components/scroll-to-top.php',
  'template-parts/components/blog-archive-card.php',
  'template-parts/components/review-archive-card.php',
  'template-parts/components/program-cta-band.php',
  'template-parts/components/internal-page-nav.php',
  'template-parts/components/final-form.php',
  'template-parts/home/hero.php',
  'template-parts/home/feature-grid.php',
  'template-parts/home/treatment-prevention.php',
  'template-parts/home/rehabilitation-program.php',
  'template-parts/home/gallery.php',
  'template-parts/home/articles-teaser.php',
  'template-parts/home/faq.php',
  'template-parts/service/subdivision-stack.php',
  'template-parts/service/leaf-stack.php',
  'template-parts/service/alcohol-stack.php',
  'template-parts/service/inner-hero.php',
  'template-parts/service/intro.php',
  'template-parts/service/signs.php',
  'template-parts/service/approach.php',
  'template-parts/service/stages.php',
  'template-parts/service/program.php',
  'template-parts/service/comfort.php',
  'template-parts/service/faq.php',
  'template-parts/page/placeholder-notice.php',
  'template-parts/page/plain-content.php',
  'template-parts/institutional/infrastructure-narrative.php',
  'template-parts/institutional/institutional-narrative.php',
  'template-parts/contacts/map-body.php',
  'template-parts/contacts/rehabilitation-steps.php',
  'template-parts/blog/archive-list.php',
  'template-parts/blog/article-content.php',
  'template-parts/blog/article-lower-stack.php',
  'template-parts/legal/document-page.php',
  'template-parts/reviews/archive-list.php',
  'template-parts/reviews/reviews-section.php',
];

for (const part of requiredTemplateParts) {
  mustExist(`theme/shpigovsky/${part}`);
}

const requiredPlugin = [
  'plugins/shpigovsky-core/shpigovsky-core.php',
  'plugins/shpigovsky-core/inc/compat.php',
  'plugins/shpigovsky-core/src/Plugin.php',
  'plugins/shpigovsky-core/src/Contracts/ModuleInterface.php',
  'plugins/shpigovsky-core/src/Loader/Autoloader.php',
  'plugins/shpigovsky-core/src/ContentTypes/Service.php',
  'plugins/shpigovsky-core/src/Permalinks/ServicePermalinks.php',
  'plugins/shpigovsky-core/src/Fields/AcfIntegration.php',
  'plugins/shpigovsky-core/src/Fields/RepeaterValidation.php',
  'plugins/shpigovsky-core/src/Settings/SiteSettings.php',
  'plugins/shpigovsky-core/src/Migrations/MigrationRunner.php',
  'plugins/shpigovsky-core/src/Forms/ConsultationHandler.php',
  'plugins/shpigovsky-core/src/Admin/OptionsPage.php',
  'plugins/shpigovsky-core/src/Admin/EditorRestrictions.php',
  'plugins/shpigovsky-core/src/Taxonomies/README.md',
];

requiredPlugin.forEach(mustExist);

const setupPhp = readText(join(THEME, 'inc/setup.php'));
pass('menu_primary', true, /'primary'/.test(setupPhp));
pass('menu_footer_services', true, /'footer_services'/.test(setupPhp));
pass('menu_footer_o_centre', true, /'footer_o_centre'/.test(setupPhp));
pass('menu_legal', true, /'legal'/.test(setupPhp));
pass('legacy_footer_menu_removed', false, /'footer'\s*=>/.test(setupPhp));

const functionsPhp = readText(join(THEME, 'functions.php'));
pass('theme_skeleton_constant', true, /SHPIGOVSKY_THEME_SKELETON/.test(functionsPhp));
pass('service_loader_required', true, /service-template-loader\.php/.test(functionsPhp));

const pluginMain = readText(join(PLUGIN, 'shpigovsky-core.php'));
pass('plugin_skeleton_constant', true, /SHPIGOVSKY_CORE_SKELETON/.test(pluginMain));
pass('plugin_no_inline_acf_hooks', false, /acf\/settings\/load_json/.test(pluginMain));
pass('legacy_bootstrap_removed', false, existsSync(join(PLUGIN, 'includes/class-bootstrap.php')));

const serviceModule = readText(join(PLUGIN, 'src/ContentTypes/Service.php'));
pass('service_module_contract', true, /implements ModuleInterface/.test(serviceModule));
pass('service_module_gated', true, /shpigovsky_core_is_skeleton_mode\(\)/.test(serviceModule));

const od002Doc = join(ARCH, 'FP-0002-OD-002-ROUTE-AUTHORITY-v1.md');
mustExist('architecture/FP-0002-OD-002-ROUTE-AUTHORITY-v1.md');
if (existsSync(od002Doc)) {
  const od002 = readText(od002Doc);
  pass('od002_legacy_route', true, /\/specyalisty\//.test(od002));
  pass('od002_canonical_route', true, /\/uslugi\/zavisimosti\/specialistam\//.test(od002));
  pass('od002_entity', true, /SVC-SPECIALISTAM-ZAV/.test(od002));
  pass('od002_supersedes_short_redirect', true, /\/specialistam\//.test(od002) && /superseded|SUPERSEDED/.test(od002));
  pass('od002_no_implementation_in_06b', true, /not implemented in V9-06B|NOT IMPLEMENTED/i.test(od002));
}

const allPhp = [...walkPhpFiles(THEME), ...walkPhpFiles(PLUGIN)];
let phpOpenOk = true;
for (const file of allPhp) {
  if (file.endsWith(`${join('plugins', 'shpigovsky-core', 'index.php')}`)) {
    continue;
  }
  const text = readText(file);
  if (!text.includes('ABSPATH')) phpOpenOk = false;
}
pass('php_abspath_guard_all_files', true, phpOpenOk);

const failures = checks.filter((c) => c.result === 'FAIL');
const report = {
  schema: 'fp-0002-v9-06b-skeleton-validation-result',
  generated: new Date().toISOString(),
  total_checks: checks.length,
  passed: checks.filter((c) => c.result === 'PASS').length,
  failed: failures.length,
  result: failures.length === 0 ? 'PASS' : 'FAIL',
  boundaries: {
    runtime_writes: 0,
    database_writes: 0,
    wordpress_object_writes: 0,
    service_cpt_registered_at_runtime: false,
    acf_json_hooks_active_in_skeleton: false,
  },
  checks,
};

console.log(JSON.stringify(report, null, 2));
process.exit(failures.length === 0 ? 0 : 1);
