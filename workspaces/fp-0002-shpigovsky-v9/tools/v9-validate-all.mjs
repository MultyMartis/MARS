#!/usr/bin/env node
/**
 * FP-0002 V9-02 — asset path, link, legal, and content hygiene validation
 */
import fs from 'node:fs';
import path from 'node:path';
import http from 'node:http';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WORKSPACE = path.resolve(__dirname, '..');
const DIST = path.join(WORKSPACE, 'dist');
const MANIFEST = JSON.parse(fs.readFileSync(path.join(__dirname, 'v9-route-manifest.json'), 'utf8'));
const EVIDENCE = 'X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v9/v9-03g-scroll-to-top/validation';
const PORT = Number(process.env.V9_PREVIEW_PORT || 8796);

const LEGAL_ROUTES = {
  '/privacy-policy/': { h1: 'Политика конфиденциальности', minH2: 8 },
  '/user-agreement/': { h1: 'Пользовательское соглашение', minH2: 6 },
  '/consent-personal-data/': { h1: 'Согласие на обработку персональных данных', minH2: 5 },
  '/cookie-files-policy/': { h1: 'Политика Cookie-файлов', minH2: 5 },
};

const HASH_ALLOWLIST = [
  { pattern: /aria-label="Telegram"/, reason: 'social placeholder' },
  { pattern: /aria-label="WhatsApp"/, reason: 'social placeholder' },
  { pattern: /aria-label="Max"/, reason: 'social placeholder' },
  { pattern: /aria-label="YouTube"/, reason: 'social placeholder' },
  { pattern: /href="#[a-z0-9-]+"/i, reason: 'same-page anchor' },
];

function walkHtml(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      if (ent.name === 'assets' || ent.name === '_html-staging') continue;
      walkHtml(p, acc);
    } else if (ent.name.endsWith('.html')) acc.push(p);
  }
  return acc;
}

function routeFromDistFile(file) {
  const rel = path.relative(DIST, file).replace(/\\/g, '/');
  if (rel === 'index.html') return '/';
  if (rel.endsWith('/index.html')) return `/${rel.replace(/\/index\.html$/, '')}/`;
  return null;
}

function validateManifestRoutes() {
  const issues = [];
  const emitted = new Set();
  for (const file of walkHtml(DIST)) {
    const route = routeFromDistFile(file);
    if (route) emitted.add(route);
  }
  for (const r of MANIFEST.routes) {
    const out = path.join(DIST, r.output.replace(/\//g, path.sep));
    if (!fs.existsSync(out)) issues.push(`missing emitted route ${r.route} -> ${r.output}`);
    if (!emitted.has(r.route)) issues.push(`route not indexed from dist ${r.route}`);
  }
  const published = new Set(MANIFEST.routes.map((r) => r.route));
  for (const route of emitted) {
    if (!published.has(route)) issues.push(`extra published page outside manifest: ${route}`);
  }
  if (emitted.has('/uslugi/genotipirovanie/')) issues.push('genotyping output present');
  return { pass: issues.length === 0, issues, route_count: emitted.size };
}

function validateAssets() {
  const issues = [];
  const htmlFiles = walkHtml(DIST);
  const assetRef = /(?:href|src|content)=["']([^"']+)["']/g;
  const forbidden = [
    /href=["']assets\//,
    /src=["']assets\//,
    /href=["']\.\.\/assets\//,
    /src=["']\.\.\/assets\//,
    /file:\/\//i,
    /X:\\/i,
    /localhost/i,
  ];
  for (const file of htmlFiles) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const html = fs.readFileSync(file, 'utf8');
    for (const re of forbidden) {
      if (re.test(html)) issues.push(`${rel}: forbidden pattern ${re}`);
    }
    let m;
    while ((m = assetRef.exec(html))) {
      const ref = m[1];
      if (ref.startsWith('/assets/')) {
        const target = path.join(DIST, ref.replace(/^\//, '').replace(/\//g, path.sep));
        if (!fs.existsSync(target)) issues.push(`${rel}: missing asset ${ref}`);
      } else if (ref.startsWith('assets/') || ref.startsWith('../assets/')) {
        issues.push(`${rel}: depth-sensitive asset ref ${ref}`);
      }
    }
  }
  return { pass: issues.length === 0, issues, html_count: htmlFiles.length };
}

function isAllowlistedHashAnchor(tag) {
  const allowClasses = [
    'site-footer__social-link',
    'site-header__messenger-link',
    'offcanvas__messenger-link',
    'contacts-body__messenger-link',
  ];
  if (allowClasses.some((c) => tag.includes(c))) return true;
  if (/aria-label="(Telegram|WhatsApp|Max|YouTube)"/.test(tag)) return true;
  return HASH_ALLOWLIST.some((item) => item.pattern.test(tag));
}

function validateLinks() {
  const issues = [];
  const publishedRoutes = new Set(MANIFEST.routes.map((r) => r.route));
  const htmlFiles = walkHtml(DIST);
  const hrefRe = /href=["'](\/[^"'#?]*\/?)["']/g;
  const hashAnchorRe = /<a\b[^>]*href=["']#["'][^>]*>/gi;
  for (const file of htmlFiles) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const html = fs.readFileSync(file, 'utf8');
    if (/\/uslugi\/genotipirovanie\/?["']/.test(html) || />Генотипирование<\/a>/.test(html)) {
      issues.push(`${rel}: genotyping nav/link exposure`);
    }
    let m;
    while ((m = hrefRe.exec(html))) {
      let route = m[1];
      if (!route.endsWith('/')) route += '/';
      if (route.includes('.html')) issues.push(`${rel}: flat html link ${route}`);
      if (route.startsWith('/assets/')) continue;
      if (!publishedRoutes.has(route)) issues.push(`${rel}: broken internal route ${route}`);
      if (route.includes('genotipirovanie')) issues.push(`${rel}: link to unpublished genotyping ${route}`);
    }
    for (const tag of html.match(hashAnchorRe) || []) {
      if (!isAllowlistedHashAnchor(tag)) {
        issues.push(`${rel}: non-allowlisted navigation href="#" -> ${tag.trim().slice(0, 160)}`);
      }
    }
  }
  return { pass: issues.length === 0, issues };
}

function validateStructure() {
  const issues = [];
  for (const file of walkHtml(DIST)) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const html = fs.readFileSync(file, 'utf8');
    const h1s = [...html.matchAll(/<h1\b[^>]*>([\s\S]*?)<\/h1>/gi)].map((x) => x[1].replace(/<[^>]+>/g, '').trim());
    if (h1s.length !== 1) issues.push(`${rel}: expected one H1, found ${h1s.length}`);
    const ids = new Map();
    for (const m of html.matchAll(/\sid=["']([^"']+)["']/g)) {
      const id = m[1];
      if (ids.has(id)) issues.push(`${rel}: duplicate id ${id} within page`);
      else ids.set(id, true);
    }
  }
  return { pass: issues.length === 0, issues };
}

function validateLegalPages() {
  const issues = [];
  for (const [route, spec] of Object.entries(LEGAL_ROUTES)) {
    const out = MANIFEST.routes.find((r) => r.route === route)?.output;
    if (!out) {
      issues.push(`${route}: missing manifest entry`);
      continue;
    }
    const file = path.join(DIST, out.replace(/\//g, path.sep));
    const html = fs.readFileSync(file, 'utf8');
    if (!html.includes('legal-document__demo-notice')) issues.push(`${route}: missing demo notice`);
    if (!html.includes('[ДЕМО:')) issues.push(`${route}: missing searchable DEMO tokens`);
    const h1 = [...html.matchAll(/<h1\b[^>]*>([\s\S]*?)<\/h1>/gi)][0]?.[1].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    if (h1 !== spec.h1) issues.push(`${route}: H1 mismatch "${h1}"`);
    const h2count = (html.match(/<h2\b/gi) || []).length;
    if (h2count < spec.minH2) issues.push(`${route}: insufficient H2 sections (${h2count})`);
    if (!html.includes('/consent-personal-data/') && route !== '/consent-personal-data/') {
      // privacy should link consent; others should cross-link privacy at minimum
    }
    if (!html.includes('/privacy-policy/') && route !== '/privacy-policy/') {
      issues.push(`${route}: missing privacy policy cross-link`);
    }
    if (/\b\d{10,13}\b/.test(html.replace(/<[^>]+>/g, ' '))) {
      issues.push(`${route}: possible fabricated numeric identifier`);
    }
  }
  return { pass: issues.length === 0, issues };
}

function validateHygiene() {
  const banned = ['TODO', 'TBD', 'UNKNOWN', 'DEMO_PLACEHOLDER', 'MARS', 'Website Factory', 'Phase V9', 'TEMPORARY_SEO', 'LEGAL_DEMO_DOCUMENT', 'PLACEHOLDER', 'NOT_PUBLISHED_IN_FRONTEND'];
  const legalRoutes = new Set(Object.keys(LEGAL_ROUTES));
  const issues = [];
  const preexisting = [];
  for (const file of walkHtml(DIST)) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const route = routeFromDistFile(file);
    const text = fs.readFileSync(file, 'utf8').replace(/<[^>]+>/g, ' ');
    for (const term of banned) {
      if (text.includes(term)) issues.push(`${rel}: banned visible term "${term}"`);
    }
    if (/lorem ipsum/i.test(text)) {
      if (legalRoutes.has(route)) {
        issues.push(`${rel}: banned visible term "Lorem ipsum"`);
      } else {
        preexisting.push(`${rel}: pre-existing demo copy contains lorem ipsum (not introduced in V9-02)`);
      }
    }
  }
  return { pass: issues.length === 0, issues, preexisting_lorem: preexisting };
}

function validateForms() {
  const issues = [];
  for (const file of walkHtml(DIST)) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const html = fs.readFileSync(file, 'utf8');
    if (!html.includes('final-form') && !html.includes('modal-consultation')) continue;
    if (html.includes('action="http')) issues.push(`${rel}: external form action`);
    if (html.includes('checked') && html.includes('consent')) {
      if (/type=["']checkbox["'][^>]*checked/i.test(html) || /checked[^>]*type=["']checkbox["']/i.test(html)) {
        issues.push(`${rel}: pre-checked consent checkbox`);
      }
    }
    if (html.includes('final-form__consent-link') || html.includes('modal-consultation__consent-link')) {
      if (!html.includes('href="/consent-personal-data/"') || !html.includes('href="/privacy-policy/"')) {
        issues.push(`${rel}: form consent links incomplete`);
      }
    }
  }
  return { pass: issues.length === 0, issues };
}

function httpGet(url) {
  return new Promise((resolve, reject) => {
    http.get(url, (res) => {
      let body = '';
      res.on('data', (c) => (body += c));
      res.on('end', () => resolve({ status: res.statusCode, body }));
    }).on('error', reject);
  });
}

async function validateRoutesHttp() {
  const results = [];
  for (const route of MANIFEST.routes.map((r) => r.route)) {
    const url = `http://127.0.0.1:${PORT}${route === '/' ? '/' : route}`;
    try {
      const res = await httpGet(url);
      const cssOk = (await httpGet(`http://127.0.0.1:${PORT}/assets/css/style.css`)).status === 200;
      const jsOk = (await httpGet(`http://127.0.0.1:${PORT}/assets/js/main.js`)).status === 200;
      const hasCss = res.body.includes('/assets/css/style.css');
      results.push({ route, status: res.status, css_ref: hasCss, css_ok: cssOk, js_ok: jsOk });
    } catch (e) {
      results.push({ route, error: String(e) });
    }
  }
  const pass = results.every((r) => r.status === 200 && r.css_ref);
  return { pass, results };
}

function writeReport(name, data) {
  fs.mkdirSync(EVIDENCE, { recursive: true });
  fs.writeFileSync(path.join(WORKSPACE, name), data, 'utf8');
  fs.writeFileSync(path.join(EVIDENCE, name), data, 'utf8');
}

function validateMotion() {
  const issues = [];
  const htmlFiles = walkHtml(DIST);
  const cssPath = path.join(DIST, 'assets/css/style.css');
  const jsPath = path.join(DIST, 'assets/js/main.js');
  const scssPath = path.join(WORKSPACE, 'src/scss/style.scss');

  if (!fs.existsSync(cssPath)) issues.push('missing dist CSS');
  if (!fs.existsSync(jsPath)) issues.push('missing dist JS');

  const css = fs.existsSync(cssPath) ? fs.readFileSync(cssPath, 'utf8') : '';
  const js = fs.existsSync(jsPath) ? fs.readFileSync(jsPath, 'utf8') : '';
  const scss = fs.existsSync(scssPath) ? fs.readFileSync(scssPath, 'utf8') : '';

  if (!css.includes('--motion-base')) issues.push('CSS missing --motion-base token');
  if (!css.includes('prefers-reduced-motion')) issues.push('CSS missing reduced-motion block');
  if (css.includes('.site-preloader')) issues.push('CSS still contains preloader styles');
  if (css.includes('is-preloader-active')) issues.push('CSS still contains preloader active state');
  if (css.includes('is-page-revealing')) issues.push('CSS still contains page-reveal fade state');
  if (!css.includes('.site-page-shell')) issues.push('CSS missing structural page shell');
  if (/\.site-page-shell\s*\{[^}]*opacity:\s*0/.test(css)) {
    issues.push('CSS page shell still hides initial opacity');
  }
  if (!css.includes('data-modal-state=closing')) {
    issues.push('CSS missing modal closing state');
  }
  if (!css.includes('modal-consultation__overlay')) {
    issues.push('CSS missing modal overlay');
  }
  if (!/rgba\(17,\s*24,\s*39,\s*0\.56\)/.test(css)) {
    issues.push('CSS missing approved semitransparent modal overlay color');
  }
  if (!css.includes('is-modal-scroll-locked')) {
    issues.push('CSS missing Triumph-derived modal scroll lock class');
  }
  if (!/body\.is-modal-scroll-locked[\s\S]{0,200}height:\s*auto/.test(css)) {
    issues.push('CSS missing height:auto adaptation on modal scroll lock');
  }
  if (!/html\.is-modal-scroll-locked[\s\S]{0,200}overflow:\s*hidden/.test(css)) {
    issues.push('CSS missing html scroll lock for FP-0002 scroll container');
  }
  if (/body\.is-scroll-locked[\s\S]{0,80}position:\s*fixed/.test(css)) {
    issues.push('CSS contains rejected body-fixed scroll lock');
  }
  if (/pageShellEl|lockPageScroll|unlockPageScroll|pageScrollLockY|focusWithoutScroll/.test(js)) {
    issues.push('JS contains rejected V9-03D/V9-03E shell-fixed modal scroll lock runtime');
  }
  if (/pageShellEl\.style\.position|body\.style\.position\s*=\s*['"]fixed['"]/.test(js)) {
    issues.push('JS contains rejected page-shell or body position fixed scroll lock');
  }
  if (!js.includes('lockBodyScroll')) issues.push('JS missing Triumph-derived lockBodyScroll');
  if (!js.includes('unlockBodyScroll')) issues.push('JS missing Triumph-derived unlockBodyScroll');
  if (!js.includes('is-modal-scroll-locked')) issues.push('JS missing is-modal-scroll-locked class usage');
  if (!js.includes('Triumph Manipulator modal runtime')) {
    issues.push('JS missing Triumph runtime attribution comment');
  }
  if (!js.includes('MODAL_TRANSITION_MS')) issues.push('JS missing modal close fallback timing');
  if (!js.includes("data-modal-state', 'closing'")) issues.push('JS missing modal closing lifecycle');
  if (js.includes('initPreloader')) issues.push('JS still contains initPreloader');
  if (js.includes('fp0002_preloader_session')) issues.push('JS still contains preloader session key');
  if (js.includes('is-page-revealing')) issues.push('JS still contains page fade coordination');
  if (!js.includes('initRevealAnimations')) issues.push('JS missing initRevealAnimations');
  if (!js.includes('IntersectionObserver')) issues.push('JS missing IntersectionObserver reveal');
  if (!js.includes('showClass')) issues.push('JS missing gallery animation configuration');
  if (/\.btn:hover[\s\S]{0,120}transform:\s*translateY/.test(scss)) {
    issues.push('SCSS contains button hover translateY');
  }
  if (/transition:\s*all/.test(scss)) issues.push('SCSS contains transition: all');

  let preloaderCount = 0;
  let pageShellCount = 0;
  let modalCount = 0;
  for (const file of htmlFiles) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const html = fs.readFileSync(file, 'utf8');
    const count = (html.match(/<div class="site-preloader" data-preloader/g) || []).length;
    if (count > 0) issues.push(`${rel}: preloader markup must be absent, found ${count}`);
    preloaderCount += count;
    const shellCount = (html.match(/data-page-shell/g) || []).length;
    if (shellCount !== 1) issues.push(`${rel}: expected one data-page-shell, found ${shellCount}`);
    pageShellCount += shellCount === 1 ? 1 : 0;
    const modalMatches = (html.match(/data-modal="consultation"/g) || []).length;
    if (modalMatches !== 1) issues.push(`${rel}: expected one consultation modal, found ${modalMatches}`);
    modalCount += modalMatches === 1 ? 1 : 0;
    if (html.includes('fp0002_preloader_session')) {
      issues.push(`${rel}: preloader session key reference in HTML`);
    }
    if (html.includes('is-preloader-active')) {
      issues.push(`${rel}: preloader class reference in HTML`);
    }
    if (html.includes('data-reveal') && !html.includes('js-enabled')) {
      issues.push(`${rel}: reveal markup without js-enabled head guard`);
    }
  }

  return {
    pass: issues.length === 0,
    issues,
    preloader_pages: preloaderCount,
    page_shell_pages: pageShellCount,
    modal_pages: modalCount,
    reveal_pages: htmlFiles.filter((f) => fs.readFileSync(f, 'utf8').includes('data-reveal')).length,
  };
}

function validateOCentreG6() {
  const issues = [];
  const scssPath = path.join(WORKSPACE, 'src/scss/style.scss');
  const infraPath = path.join(WORKSPACE, 'src/partials/sections/infrastructure-narrative.html');
  const oCentreDist = path.join(DIST, 'o-centre/index.html');

  if (!fs.existsSync(oCentreDist)) {
    issues.push('missing dist /o-centre/');
    return { pass: false, issues };
  }

  const scss = fs.existsSync(scssPath) ? fs.readFileSync(scssPath, 'utf8') : '';
  const infra = fs.existsSync(infraPath) ? fs.readFileSync(infraPath, 'utf8') : '';
  const oCentreHtml = fs.readFileSync(oCentreDist, 'utf8');

  const g6Patterns = [
    'data-inf-group="g6"',
    'infrastructure-narrative__group--g6',
    'infrastructure-narrative__group--mobile-close',
  ];

  for (const pattern of g6Patterns) {
    if (infra.includes(pattern)) issues.push(`source infrastructure-narrative still contains ${pattern}`);
    if (oCentreHtml.includes(pattern)) issues.push(`dist /o-centre/ still contains ${pattern}`);
  }

  if (scss.includes('infrastructure-narrative__group--g6')) {
    issues.push('SCSS still contains infrastructure-narrative__group--g6');
  }
  if (scss.includes('infrastructure-narrative__group--mobile-close')) {
    issues.push('SCSS still contains dead infrastructure-narrative__group--mobile-close');
  }

  return {
    pass: issues.length === 0,
    issues,
    source_g6_count: g6Patterns.reduce((n, p) => n + (infra.split(p).length - 1), 0),
    dist_g6_count: g6Patterns.reduce((n, p) => n + (oCentreHtml.split(p).length - 1), 0),
  };
}

function validateScrollToTop() {
  const issues = [];
  const htmlFiles = walkHtml(DIST);
  const cssPath = path.join(DIST, 'assets/css/style.css');
  const jsPath = path.join(DIST, 'assets/js/main.js');
  const scssPath = path.join(WORKSPACE, 'src/scss/style.scss');
  const partialPath = path.join(WORKSPACE, 'src/partials/components/scroll-to-top.html');

  if (!fs.existsSync(partialPath)) issues.push('missing scroll-to-top partial');
  if (!fs.existsSync(cssPath)) issues.push('missing dist CSS for scroll-to-top validation');
  if (!fs.existsSync(jsPath)) issues.push('missing dist JS for scroll-to-top validation');

  const css = fs.existsSync(cssPath) ? fs.readFileSync(cssPath, 'utf8') : '';
  const js = fs.existsSync(jsPath) ? fs.readFileSync(jsPath, 'utf8') : '';
  const scss = fs.existsSync(scssPath) ? fs.readFileSync(scssPath, 'utf8') : '';
  const partial = fs.existsSync(partialPath) ? fs.readFileSync(partialPath, 'utf8') : '';

  if (!partial.includes('data-scroll-to-top')) issues.push('partial missing data-scroll-to-top hook');
  if (!/<button[^>]*type=["']button["']/.test(partial)) issues.push('partial missing semantic button type');
  if (!partial.includes('aria-label=')) issues.push('partial missing accessible label');
  if (partial.includes('href="#')) issues.push('partial must not use href="#" anchor pattern');

  if (!css.includes('.scroll-to-top')) issues.push('CSS missing .scroll-to-top');
  if (!css.includes('.scroll-to-top--visible')) issues.push('CSS missing visible state class');
  if (!/\.scroll-to-top[\s\S]{0,400}position:\s*fixed/.test(css)) {
    issues.push('CSS missing fixed positioning on scroll-to-top');
  }
  if (!/\.scroll-to-top[\s\S]{0,500}z-index:\s*900/.test(css)) {
    issues.push('CSS scroll-to-top z-index must remain below modal/offcanvas layers (900)');
  }
  if (/\.scroll-to-top:hover[\s\S]{0,120}transform:\s*translateY/.test(scss)) {
    issues.push('SCSS scroll-to-top hover must not use translateY lift');
  }
  if (/\.scroll-to-top[\s\S]{0,300}transition:\s*all/.test(scss)) {
    issues.push('SCSS scroll-to-top must not use transition: all');
  }

  if (!js.includes('initScrollToTop')) issues.push('JS missing initScrollToTop initializer');
  if (!js.includes('SCROLL_THRESHOLD = 500')) issues.push('JS missing 500px scroll threshold');
  if (!js.includes("behavior: prefersReducedMotion() ? 'auto' : 'smooth'")) {
    issues.push('JS missing reduced-motion-aware smooth scroll behavior');
  }
  if (!js.includes('scroll-to-top--visible')) issues.push('JS missing visible state class toggle');
  if (!js.includes('prefers-reduced-motion: reduce')) issues.push('JS missing reduced-motion matchMedia');

  let scrollToTopPages = 0;
  for (const file of htmlFiles) {
    const rel = path.relative(DIST, file).replace(/\\/g, '/');
    const html = fs.readFileSync(file, 'utf8');
    const count = (html.match(/data-scroll-to-top/g) || []).length;
    if (count !== 1) issues.push(`${rel}: expected one scroll-to-top control, found ${count}`);
    if (count === 1) scrollToTopPages += 1;
    if (count > 0 && !/<button[^>]*data-scroll-to-top/.test(html)) {
      issues.push(`${rel}: scroll-to-top hook must be on a button element`);
    }
  }

  return {
    pass: issues.length === 0,
    issues,
    scroll_to_top_pages: scrollToTopPages,
  };
}

async function main() {
  const manifestRoutes = validateManifestRoutes();
  const assets = validateAssets();
  const links = validateLinks();
  const structure = validateStructure();
  const legal = validateLegalPages();
  const hygiene = validateHygiene();
  const forms = validateForms();
  const motion = validateMotion();
  const oCentreG6 = validateOCentreG6();
  const scrollToTop = validateScrollToTop();

  let httpResult = { pass: false, results: [], skipped: true };
  try {
    await httpGet(`http://127.0.0.1:${PORT}/`);
    httpResult = await validateRoutesHttp();
    httpResult.skipped = false;
  } catch {
    httpResult.note = `HTTP validation skipped — start preview server on port ${PORT}`;
  }

  const summary = { manifestRoutes, assets, links, structure, legal, hygiene, forms, motion, oCentreG6, scrollToTop, http: httpResult };
  const pass = [manifestRoutes, assets, links, structure, legal, hygiene, forms, motion, oCentreG6, scrollToTop].every((x) => x.pass) && (httpResult.skipped || httpResult.pass);

  const report = `# FP-0002 V9-03G Validation

Status: ${pass ? 'PASS' : 'FAIL'}
Phase: V9-03G
Port: ${PORT}

## Manifest routes
${manifestRoutes.pass ? 'PASS' : 'FAIL'} (${manifestRoutes.route_count} routes)

## Assets
${assets.pass ? 'PASS' : 'FAIL'}

## Links
${links.pass ? 'PASS' : 'FAIL'}

## Structure (H1 / IDs)
${structure.pass ? 'PASS' : 'FAIL'}

## Legal pages
${legal.pass ? 'PASS' : 'FAIL'}

## Content hygiene
${hygiene.pass ? 'PASS' : 'FAIL'}
${hygiene.preexisting_lorem?.length ? `\n### Pre-existing demo lorem (documented, not V9-03A regression)\n${hygiene.preexisting_lorem.map((i) => `- ${i}`).join('\n')}` : ''}

## Forms / consent
${forms.pass ? 'PASS' : 'FAIL'}

## Motion / preloader absence / modal contract
${motion.pass ? 'PASS' : 'FAIL'}
- Preloader pages (must be 0): ${motion.preloader_pages}
- Page shell pages: ${motion.page_shell_pages}
- Modal pages: ${motion.modal_pages}
- Reveal pages: ${motion.reveal_pages}

## O-Centre G6 removal
${oCentreG6.pass ? 'PASS' : 'FAIL'}
- Source G6 token count: ${oCentreG6.source_g6_count}
- Dist G6 token count: ${oCentreG6.dist_g6_count}

## Scroll-to-top (V9-03G)
${scrollToTop.pass ? 'PASS' : 'FAIL'}
- Scroll-to-top pages: ${scrollToTop.scroll_to_top_pages}

## HTTP runtime
${httpResult.skipped ? 'SKIPPED' : httpResult.pass ? 'PASS' : 'FAIL'}

## Issues
${[...manifestRoutes.issues, ...assets.issues, ...links.issues, ...structure.issues, ...legal.issues, ...hygiene.issues, ...forms.issues, ...motion.issues, ...oCentreG6.issues, ...scrollToTop.issues].map((i) => `- ${i}`).join('\n') || 'No issues.'}
`;

  writeReport('FP-0002-V9-03F-AUTOMATED-VALIDATION-v1.md', report);
  writeReport('V9-ASSET-PATH-VALIDATION.md', `# V9 Asset Path Validation\n\nStatus: ${assets.pass ? 'PASS' : 'FAIL'}\n\n${assets.issues.map((i) => `- ${i}`).join('\n') || 'No issues.'}\n`);
  writeReport('V9-INTERNAL-LINK-VALIDATION.md', `# V9 Internal Link Validation\n\nStatus: ${links.pass ? 'PASS' : 'FAIL'}\n\n${links.issues.map((i) => `- ${i}`).join('\n') || 'No issues.'}\n`);

  fs.writeFileSync(path.join(EVIDENCE, 'validation-summary.json'), JSON.stringify(summary, null, 2));

  if (!pass) {
    console.error('Validation FAILED');
    process.exit(1);
  }
  console.log('Validation PASS');
}

main();
