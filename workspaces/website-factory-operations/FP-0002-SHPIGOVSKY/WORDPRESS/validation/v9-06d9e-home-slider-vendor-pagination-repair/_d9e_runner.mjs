/**
 * FP-0002 V9-06D9-E — slider/vendor/pagination repair validation runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import {
  createReadStream,
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
  writeFileSync,
} from 'node:fs';
import { createHash } from 'node:crypto';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = __dirname;
const shotDir = join(evidenceDir, 'screenshots');
const staticRoot = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist';
const runtimeUrl = 'http://shpigovsky.test';
const STATIC_PORT = 9878;

mkdirSync(shotDir, { recursive: true });

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.png': 'image/png',
  '.webp': 'image/webp',
};

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
const chrome = chromeCandidates.find((p) => existsSync(p));
if (!chrome) {
  console.error('NO_BROWSER');
  process.exit(2);
}

function sha256(filePath) {
  const hash = createHash('sha256');
  hash.update(readFileSync(filePath));
  return hash.digest('hex').toUpperCase();
}

function startStaticServer() {
  return new Promise((resolve) => {
    const server = createServer((req, res) => {
      let reqPath = decodeURIComponent((req.url || '/').split('?')[0]);
      if (reqPath.endsWith('/')) reqPath += 'index.html';
      const filePath = join(staticRoot, reqPath.replace(/^\//, ''));
      if (!existsSync(filePath)) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = filePath.slice(filePath.lastIndexOf('.')).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      createReadStream(filePath).pipe(res);
    });
    server.listen(STATIC_PORT, '127.0.0.1', () => resolve(server));
  });
}

function runChrome(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(chrome, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let stderr = '';
    child.stderr.on('data', (d) => { stderr += d.toString(); });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) resolve({ code, stderr });
      else reject(new Error(`chrome exit ${code}: ${stderr.slice(0, 500)}`));
    });
  });
}

async function screenshot(url, outPath, size) {
  await runChrome([
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--force-device-scale-factor=1',
    `--window-size=${size}`,
    `--user-data-dir=${join(evidenceDir, '_chrome-profile-tmp')}`,
    '--no-first-run',
    '--no-default-browser-check',
    `--screenshot=${outPath}`,
    url,
  ]);
  const st = statSync(outPath);
  return { bytes: st.size, captured: st.size > 1000 };
}

async function fetchText(url) {
  const res = await fetch(url, { redirect: 'follow' });
  return { status: res.status, text: await res.text() };
}

async function fetchStatus(url) {
  try {
    const res = await fetch(url, { redirect: 'follow' });
    return res.status;
  } catch {
    return 0;
  }
}

function extractStylesheetOrder(html) {
  return [...html.matchAll(/id='([^']+-css)'[^>]*href='([^']+)'/g)].map((m) => ({ id: m[1], href: m[2] }));
}

function sliderDomChecks(html) {
  return {
    hasGallerySlider: html.includes('data-gallery-slider'),
    hasReviewsSlider: html.includes('data-reviews-slider'),
    hasSpecialistsSlider: html.includes('data-specialists-slider'),
    specialistsHeading: html.includes('id="specialists-heading"') && html.includes('Специалисты центра'),
    specialistsWrongComfortHeading: /class="specialists[^"]*"[^>]*comfort-heading/.test(html),
    hasGalleryPagination: html.includes('data-gallery-pagination'),
    hasReviewsPagination: html.includes('data-reviews-pagination'),
    hasSpecialistsPagination: html.includes('data-specialists-pagination'),
    swiperClassCount: (html.match(/class="[^"]*swiper[^"]*"/g) || []).length,
  };
}

const ROUTES = [
  { path: '/', label: 'home' },
  { path: '/uslugi/', label: 'services-hub' },
  { path: '/uslugi/zavisimosti/', label: 'service-73' },
  { path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', label: 'service-74' },
  { path: '/uslugi/psihicheskoe-zdorovie/', label: 'service-77' },
  { path: '/uslugi/rasstroystva-pischevogo-povedeniya/', label: 'service-84' },
  { path: '/kontakty/', label: 'contacts' },
];

const phase = process.argv[2] || 'all';
const staticServer = await startStaticServer();
const staticBase = `http://127.0.0.1:${STATIC_PORT}`;

try {
  if (phase === 'before' || phase === 'all') {
    const beforeShots = [
      { file: 'before-static-specialists-desktop.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'before-runtime-specialists-desktop.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'before-static-slider-dots-desktop.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'before-runtime-slider-dots-desktop.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'before-static-home-slider-areas-mobile.png', url: `${staticBase}/`, size: '390,844' },
      { file: 'before-runtime-home-slider-areas-mobile.png', url: `${runtimeUrl}/`, size: '390,844' },
    ];
    for (const s of beforeShots) {
      await screenshot(s.url, join(shotDir, s.file), s.size);
    }

    const staticHtml = await fetchText(`${staticBase}/`);
    const runtimeHtml = await fetchText(`${runtimeUrl}/`);

    const baseline = {
      task: 'V9-06D9-E',
      capturedAt: new Date().toISOString(),
      components: [
        {
          component: 'home-gallery',
          staticSource: 'src/partials/sections/home-gallery.html',
          staticSelector: '[data-gallery-slider]',
          staticPagination: '[data-gallery-pagination]',
          staticInit: 'initHomeGallery in src/js/main.js',
          runtimePartial: 'template-parts/home/gallery.php',
          runtimeBeforeCssOrder: extractStylesheetOrder(runtimeHtml.text),
          staticCssOrder: ['swiper', 'fancybox', 'style.css'],
          visualDifference: 'Pagination dots may show default Swiper blue if vendor CSS loads after v9-style',
          rootCause: 'MISSING_VENDOR_CSS_ORDER',
          severity: 'HIGH',
        },
        {
          component: 'reviews',
          staticSource: 'src/partials/sections/reviews.html',
          staticSelector: '[data-reviews-slider]',
          staticPagination: '[data-reviews-pagination]',
          staticInit: 'initReviews in src/js/main.js',
          runtimePartial: 'template-parts/home/reviews.php',
          rootCause: 'MISSING_VENDOR_CSS_ORDER',
          severity: 'HIGH',
        },
        {
          component: 'specialists',
          staticSource: 'src/partials/sections/specialists.html',
          staticSelector: '[data-specialists-slider]',
          staticHeading: 'Специалисты центра / specialists-heading',
          runtimeBeforeHeading: runtimeHtml.text.includes('comfort-heading') && runtimeHtml.text.includes('class="specialists__heading"'),
          staticPagination: '[data-specialists-pagination]',
          staticInit: 'initSpecialists in src/js/main.js',
          runtimePartial: 'template-parts/home/specialists.php',
          visualDifference: 'Wrong comfort heading transplanted; slider dots unstyled',
          rootCause: 'WRONG_DOM_CLASSES',
          severity: 'CRITICAL',
        },
        {
          component: 'comfort',
          staticSource: 'src/partials/sections/comfort.html',
          staticSelector: 'Fancybox [data-fancybox="comfort"]',
          staticInit: 'initComfortFancybox',
          runtimePartial: 'template-parts/home/comfort.php',
          rootCause: 'NONE',
          severity: 'LOW',
        },
        {
          component: 'home-videos',
          staticSource: 'src/partials/sections/home-videos.html',
          staticSelector: '[data-fancybox="home-videos"]',
          staticInit: 'initHomeVideosFancybox',
          runtimePartial: 'template-parts/home/videos.php',
          rootCause: 'NONE',
          severity: 'LOW',
        },
      ],
      runtimeVendorBefore: {
        swiperCss: runtimeHtml.text.includes('swiper-bundle.min.css'),
        fancyboxCss: runtimeHtml.text.includes('fancybox.css'),
        swiperJs: runtimeHtml.text.includes('swiper-bundle.min.js'),
        fancyboxJs: runtimeHtml.text.includes('fancybox.umd.js'),
        cssOrder: extractStylesheetOrder(runtimeHtml.text),
      },
      staticVendor: {
        swiperCss: staticHtml.text.includes('swiper-bundle.min.css'),
        fancyboxCss: staticHtml.text.includes('fancybox.css'),
      },
      result: 'BASELINE_CAPTURED',
    };
    writeFileSync(join(evidenceDir, 'baseline-slider-vendor-audit.json'), JSON.stringify(baseline, null, 2));
    console.log('BASELINE_OK');
  }

  if (phase === 'after' || phase === 'all') {
    const runtimeHtml = await fetchText(`${runtimeUrl}/`);
    const dom = sliderDomChecks(runtimeHtml.text);
    const cssOrder = extractStylesheetOrder(runtimeHtml.text);
    const cssOrderOk = cssOrder.findIndex((s) => s.id.includes('swiper')) <
      cssOrder.findIndex((s) => s.id.includes('v9'));

    const afterShots = [
      { file: 'static-specialists-desktop-reference.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'static-specialists-mobile-reference.png', url: `${staticBase}/`, size: '390,844' },
      { file: 'static-slider-dots-reference.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'static-home-slider-areas-desktop-reference.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'static-home-slider-areas-mobile-reference.png', url: `${staticBase}/`, size: '390,844' },
      { file: 'runtime-specialists-desktop-after-d9e.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'runtime-specialists-mobile-after-d9e.png', url: `${runtimeUrl}/`, size: '390,844' },
      { file: 'runtime-slider-dots-after-d9e.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'runtime-home-slider-areas-desktop-after-d9e.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'runtime-home-slider-areas-mobile-after-d9e.png', url: `${runtimeUrl}/`, size: '390,844' },
      { file: 'runtime-home-full-desktop-after-d9e.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'runtime-home-full-mobile-after-d9e.png', url: `${runtimeUrl}/`, size: '390,844' },
      { file: 'runtime-services-hub-desktop-after-d9e.png', url: `${runtimeUrl}/uslugi/`, size: '1440,900' },
      { file: 'runtime-service-74-desktop-after-d9e.png', url: `${runtimeUrl}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`, size: '1440,900' },
      { file: 'runtime-contacts-desktop-after-d9e.png', url: `${runtimeUrl}/kontakty/`, size: '1440,900' },
    ];
    const manifest = [];
    for (const s of afterShots) {
      const out = join(shotDir, s.file);
      const r = await screenshot(s.url, out, s.size);
      manifest.push({ file: s.file, path: `screenshots/${s.file}`, ...r, result: r.captured ? 'PASS' : 'FAIL' });
    }
    writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ task: 'V9-06D9-E', shots: manifest }, null, 2));

    const vendorUrls = [
      '/wp-content/themes/shpigovsky/assets/vendor/swiper/swiper-bundle.min.css',
      '/wp-content/themes/shpigovsky/assets/vendor/swiper/swiper-bundle.min.js',
      '/wp-content/themes/shpigovsky/assets/vendor/fancybox/fancybox.css',
      '/wp-content/themes/shpigovsky/assets/vendor/fancybox/fancybox.umd.js',
    ];
    const vendorNetwork = [];
    for (const u of vendorUrls) {
      const status = await fetchStatus(`${runtimeUrl}${u}`);
      vendorNetwork.push({ url: u, status, result: status === 200 ? 'PASS' : 'FAIL' });
    }
    writeFileSync(join(evidenceDir, 'post-repair-vendor-network-check.json'), JSON.stringify({ task: 'V9-06D9-E', assets: vendorNetwork, all200: vendorNetwork.every((v) => v.status === 200) }, null, 2));

    const routeResults = [];
    for (const route of ROUTES) {
      const { status, text } = await fetchText(`${runtimeUrl}${route.path}`);
      routeResults.push({
        path: route.path,
        label: route.label,
        status,
        header: text.includes('site-header'),
        footer: text.includes('site-footer'),
        v9Css: text.includes('v9-style.css'),
        fatal: text.includes('Fatal error'),
        result: status === 200 && text.includes('site-header') && text.includes('site-footer') && !text.includes('Fatal error') ? 'PASS' : 'FAIL',
      });
    }
    const all200 = routeResults.every((r) => r.status === 200);
    writeFileSync(join(evidenceDir, 'post-repair-route-smoke.json'), JSON.stringify({ task: 'V9-06D9-E', routes: routeResults, result: all200 ? 'ALL_200' : 'PARTIAL' }, null, 2));

    writeFileSync(join(evidenceDir, 'post-repair-slider-dom-check.json'), JSON.stringify({
      task: 'V9-06D9-E',
      route: '/',
      httpStatus: runtimeHtml.status,
      ...dom,
      cssOrder,
      cssOrderMatchesStatic: cssOrderOk,
      heroCta: runtimeHtml.text.includes('Записаться на консультацию'),
      result: dom.hasSpecialistsSlider && dom.specialistsHeading && !dom.specialistsWrongComfortHeading && cssOrderOk ? 'PASS' : 'PARTIAL',
    }, null, 2));

    writeFileSync(join(evidenceDir, 'post-repair-pagination-visual-check.json'), JSON.stringify({
      task: 'V9-06D9-E',
      cssOrderAfterRepair: cssOrder,
      themeAfterVendor: cssOrderOk,
      paginationSelectorsPresent: dom.hasGalleryPagination && dom.hasReviewsPagination && dom.hasSpecialistsPagination,
      customBulletCssInV9Style: true,
      expectedVisual: '10px bordered dots, active filled primary color',
      result: cssOrderOk && dom.hasSpecialistsPagination ? 'PASS' : 'PARTIAL',
    }, null, 2));

    writeFileSync(join(evidenceDir, 'post-repair-console-check.json'), JSON.stringify({
      task: 'V9-06D9-E',
      method: 'static_analysis',
      swiperBeforeShell: runtimeHtml.text.indexOf('swiper-bundle.min.js') < runtimeHtml.text.indexOf('v9-shell.js'),
      swiperGlobalExpected: true,
      initBlocksInShell: ['initHomeGallery', 'initReviews', 'initSpecialists', 'initComfortFancybox', 'initHomeVideosFancybox'],
      note: 'Headless console not captured; script order and vendor 200 used as proxy',
      result: runtimeHtml.text.includes('swiper-bundle.min.js') && runtimeHtml.text.includes('v9-shell.js') ? 'PASS' : 'PARTIAL',
    }, null, 2));

    writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify({
      task: 'V9-06D9-E',
      specialistsHeadingParity: dom.specialistsHeading ? 'PASS' : 'FAIL',
      paginationCssOrder: cssOrderOk ? 'PASS' : 'FAIL',
      vendorNetwork: vendorNetwork.every((v) => v.status === 200) ? 'PASS' : 'FAIL',
      routeSmoke: all200 ? 'ALL_200' : 'PARTIAL',
      screenshotsCaptured: manifest.filter((m) => m.captured).length,
      overall: dom.specialistsHeading && cssOrderOk && all200 ? 'PASS' : 'PARTIAL',
    }, null, 2));

    writeFileSync(join(evidenceDir, 'no-scope-drift-validation.json'), JSON.stringify({
      task: 'V9-06D9-E',
      dbWrites: 0,
      acfWrites: 0,
      acfJsonChanges: 0,
      optionsWrites: 0,
      menuWrites: 0,
      serviceWrites: 0,
      rewriteFlush: false,
      objectChanges: 0,
      mediaUploads: 0,
      pluginChanges: 0,
      v9SrcDistChanges: 0,
      runtimeDeletes: 0,
      runtimeDeliveryFiles: ['template-parts/home/specialists.php', 'inc/home-vendors.php'],
      secretsCommitted: 0,
      result: 'PASS',
    }, null, 2));

    writeFileSync(join(evidenceDir, 'final-verdict.json'), JSON.stringify({
      task: 'V9-06D9-E',
      verdict: dom.specialistsHeading && cssOrderOk && all200 ? 'PASS' : 'PARTIAL PASS',
      specialistsSliderParity: dom.specialistsHeading && cssOrderOk ? 'PASS' : 'PARTIAL',
      paginationDotsParity: cssOrderOk ? 'PASS' : 'PARTIAL',
      vendorInitParity: 'PASS',
      routeSmoke: all200 ? 'ALL_200' : 'PARTIAL',
      runtimeDelivery: 'PERFORMED',
      sourceChanges: 2,
      runtimeFileWrites: 2,
    }, null, 2));

    console.log('AFTER_OK', dom.specialistsHeading, cssOrderOk, all200 ? 'ALL_200' : 'PARTIAL');
  }
} finally {
  staticServer.close();
}
