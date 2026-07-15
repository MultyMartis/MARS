/**
 * FP-0002 V9-06D9-A — visual parity audit runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { createReadStream, existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { join, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = __dirname;
const shotDir = join(evidenceDir, 'screenshots');
const staticRoot = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist';
const runtimeUrl = 'http://shpigovsky.test';
const STATIC_PORT = 9876;

mkdirSync(shotDir, { recursive: true });

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.ico': 'image/x-icon',
};

function startStaticServer() {
  return new Promise((resolve) => {
    const server = createServer((req, res) => {
      let reqPath = decodeURIComponent((req.url || '/').split('?')[0]);
      if (reqPath.endsWith('/')) reqPath += 'index.html';
      const filePath = join(staticRoot, reqPath.replace(/^\//, ''));
      if (!filePath.startsWith(staticRoot.replace(/\//g, '\\')) && !filePath.startsWith(staticRoot)) {
        res.writeHead(403); res.end(); return;
      }
      if (!existsSync(filePath)) {
        res.writeHead(404); res.end('Not found'); return;
      }
      const ext = extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      createReadStream(filePath).pipe(res);
    });
    server.listen(STATIC_PORT, '127.0.0.1', () => resolve(server));
  });
}

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

async function loadPuppeteer() {
  try {
    const require = createRequire(import.meta.url);
    return require('puppeteer');
  } catch {
    // fallback: dynamic import from npx cache not reliable; use puppeteer-core path
    try {
      const require = createRequire(join(process.cwd(), 'package.json'));
      return require('puppeteer-core');
    } catch {
      return null;
    }
  }
}

async function runWithPuppeteerCore() {
  let puppeteer;
  try {
    puppeteer = await import('puppeteer-core');
    puppeteer = puppeteer.default || puppeteer;
  } catch {
    try {
      const require = createRequire(import.meta.url);
      puppeteer = require('puppeteer-core');
    } catch (e) {
      throw new Error('puppeteer-core unavailable: ' + e.message);
    }
  }

  const browser = await puppeteer.launch({
    executablePath: chrome,
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--force-device-scale-factor=1'],
  });

  return browser;
}

const STYLE_PROPS = [
  'font-family', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'color', 'opacity',
  'text-transform', 'text-decoration', 'font-style', 'font-stretch', 'font-synthesis',
  '-webkit-font-smoothing', 'text-rendering', 'display', 'align-items', 'gap', 'padding', 'margin',
  'transform', 'filter', 'zoom',
];

const NAV_ITEMS = ['Главная', 'Услуги', 'Специалисты', 'О центре', 'Отзывы', 'Статьи', 'Контакты'];

const SELECTORS = [
  { key: 'header_root', selector: 'header.site-header' },
  { key: 'logo_area', selector: '.site-header__logo-image' },
  { key: 'address_text', selector: '.site-header__address-line' },
  { key: 'schedule_text', selector: '.site-header__schedule-line' },
  { key: 'phone_primary', selector: '.site-header__phones .site-header__phone' },
  { key: 'nav_container', selector: 'nav.site-header__nav' },
  { key: 'callback_button', selector: '.site-header__btns-wrap .btn' },
  { key: 'search_area', selector: '.site-header__search' },
  { key: 'hero_section', selector: 'section.hero.hero--home' },
  { key: 'hero_title', selector: '.hero__title' },
  { key: 'hero_tagline', selector: '.hero__tagline' },
  { key: 'hero_image', selector: '.hero__image' },
  { key: 'body', selector: 'body' },
];

async function extractStyles(page, baseLabel) {
  const results = [];
  for (const { key, selector } of SELECTORS) {
    const data = await page.evaluate((sel, props) => {
      const el = document.querySelector(sel);
      if (!el) return { found: false, selector: sel };
      const cs = getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      const out = { found: true, selector: sel, text: (el.textContent || '').trim().slice(0, 80), bbox: { x: rect.x, y: rect.y, width: rect.width, height: rect.height } };
      for (const p of props) out[p] = cs.getPropertyValue(p) || cs[p] || '';
      out.fontFamily = cs.fontFamily;
      out.color = cs.color;
      // parent chain
      let parent = el.parentElement;
      const parents = [];
      for (let i = 0; i < 3 && parent; i++) {
        const pcs = getComputedStyle(parent);
        parents.push({ tag: parent.tagName, className: parent.className, opacity: pcs.opacity, transform: pcs.transform, filter: pcs.filter, fontSize: pcs.fontSize, lineHeight: pcs.lineHeight, color: pcs.color });
        parent = parent.parentElement;
      }
      out.parents = parents;
      return out;
    }, selector, STYLE_PROPS);
    results.push({ key, base: baseLabel, ...data });
  }

  for (const label of NAV_ITEMS) {
    const data = await page.evaluate((text, props) => {
      const links = [...document.querySelectorAll('.site-header__nav-link')];
      const el = links.find((a) => (a.textContent || '').trim() === text);
      if (!el) return { found: false, text };
      const cs = getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      const out = { found: true, text, selector: '.site-header__nav-link', bbox: { x: rect.x, y: rect.y, width: rect.width, height: rect.height } };
      for (const p of props) out[p] = cs.getPropertyValue(p) || cs[p] || '';
      out.fontFamily = cs.fontFamily;
      out.color = cs.color;
      return out;
    }, label, STYLE_PROPS);
    results.push({ key: `nav_${label}`, base: baseLabel, ...data });
  }
  return results;
}

async function extractSections(page) {
  return page.evaluate(() => {
    const sections = [...document.querySelectorAll('section[data-reveal], section.hero, section.faq, section.final-form, section.home-articles, section.reviews, section.specialists, main > section')];
    return sections.map((s, i) => ({
      index: i,
      tag: s.tagName.toLowerCase(),
      className: s.className,
      id: s.id || null,
      ariaLabel: s.getAttribute('aria-label') || s.getAttribute('aria-labelledby') || null,
      textMarker: (s.querySelector('h1,h2,h3')?.textContent || s.textContent || '').trim().slice(0, 60),
      hasImage: !!s.querySelector('img'),
      childImgCount: s.querySelectorAll('img').length,
    }));
  });
}

async function extractHeroAudit(page) {
  return page.evaluate(() => {
    const hero = document.querySelector('section.hero.hero--home');
    if (!hero) return { found: false };
    const cs = getComputedStyle(hero);
    const img = hero.querySelector('.hero__image');
    const media = hero.querySelector('.hero__media');
    const imgCs = img ? getComputedStyle(img) : null;
    return {
      found: true,
      selector: 'section.hero.hero--home',
      hasMediaLayer: !!media,
      hasImage: !!img,
      imageSrc: img?.getAttribute('src') || null,
      imageDisplay: imgCs?.display || null,
      imageVisibility: imgCs?.visibility || null,
      heroMinHeight: cs.minHeight,
      heroHeight: cs.height,
      heroPaddingTop: cs.paddingTop,
      heroPaddingBottom: cs.paddingBottom,
      heroBackgroundImage: cs.backgroundImage,
      title: hero.querySelector('.hero__title')?.textContent?.trim() || null,
      tagline: hero.querySelector('.hero__tagline')?.textContent?.trim() || null,
      hasCta: !!hero.querySelector('.hero__button'),
      ctaText: hero.querySelector('.hero__button')?.textContent?.trim() || null,
      rect: (() => { const r = hero.getBoundingClientRect(); return { width: r.width, height: r.height }; })(),
    };
  });
}

async function extractNetworkAudit(page) {
  const requests = [];
  page.on('response', async (res) => {
    const url = res.url();
    if (/\.(woff2?|ttf|css|png|jpe?g|webp|svg)(\?|$)/i.test(url) || url.includes('/assets/')) {
      requests.push({ url, status: res.status(), type: res.request().resourceType() });
    }
  });
  return requests;
}

async function captureScreenshot(page, outPath, clip = null) {
  await page.screenshot({ path: outPath, fullPage: !clip, clip, type: 'png' });
  const st = statSync(outPath);
  return { path: outPath, bytes: st.size };
}

const server = await startStaticServer();
const staticUrl = `http://127.0.0.1:${STATIC_PORT}/`;

const browser = await runWithPuppeteerCore();
const screenshotManifest = [];
const headerDiff = { static: [], runtime: [], pairs: [] };

const viewports = {
  desktop: { width: 1440, height: 900 },
  mobile: { width: 390, height: 844 },
};

const pagesToShot = [
  { staticPath: '/', runtimePath: '/', prefix: 'home' },
  { staticPath: '/uslugi/', runtimePath: '/uslugi/', prefix: 'services-hub', desktopOnly: true },
  { staticPath: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', runtimePath: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', prefix: 'service-74', desktopOnly: true },
  { staticPath: '/kontakty/', runtimePath: '/kontakty/', prefix: 'contacts', desktopOnly: true },
];

let staticSections = [];
let runtimeSections = [];
let staticHero = null;
let runtimeHero = null;
let staticNetwork = [];
let runtimeNetwork = [];

for (const [vpName, vp] of Object.entries(viewports)) {
  for (const target of ['static', 'runtime']) {
    const page = await browser.newPage();
    await page.setViewport({ ...vp, deviceScaleFactor: 1 });
    const baseUrl = target === 'static' ? staticUrl : runtimeUrl;
    const network = [];
    page.on('response', (res) => {
      const url = res.url();
      if (/\.(woff2?|ttf|css|png|jpe?g|webp|svg)(\?|$)/i.test(url) || url.includes('/assets/')) {
        network.push({ url, status: res.status() });
      }
    });
    await page.goto(baseUrl + (target === 'static' ? '' : ''), { waitUntil: 'networkidle2', timeout: 60000 });

    if (target === 'static' && vpName === 'desktop') {
      staticSections = await extractSections(page);
      staticHero = await extractHeroAudit(page);
      staticNetwork = [...network];
    }
    if (target === 'runtime' && vpName === 'desktop') {
      runtimeSections = await extractSections(page);
      runtimeHero = await extractHeroAudit(page);
      runtimeNetwork = [...network];
    }

    const styles = await extractStyles(page, target);
    if (target === 'static') headerDiff.static.push(...styles);
    else headerDiff.runtime.push(...styles);

    // home + header shots
    const homeFull = join(shotDir, `${target}-${pagesToShot[0].prefix}-${vpName}-full.png`);
    const homeTop = join(shotDir, `${target}-${pagesToShot[0].prefix}-${vpName}-top.png`);
    const headerShot = join(shotDir, `${target}-header-${vpName}.png`);

    screenshotManifest.push({ file: `${target}-${pagesToShot[0].prefix}-${vpName}-full.png`, ...await captureScreenshot(page, homeFull) });
    screenshotManifest.push({ file: `${target}-${pagesToShot[0].prefix}-${vpName}-top.png`, ...await captureScreenshot(page, homeTop, { x: 0, y: 0, width: vp.width, height: Math.min(vp.height, 500) }) });
    screenshotManifest.push({ file: `${target}-header-${vpName}.png`, ...await captureScreenshot(page, headerShot, { x: 0, y: 0, width: vp.width, height: vpName === 'mobile' ? 120 : 180 }) });

    if (vpName === 'desktop') {
      for (const pg of pagesToShot.slice(1)) {
        await page.goto(baseUrl.replace(/\/$/, '') + pg[target === 'static' ? 'staticPath' : 'runtimePath'], { waitUntil: 'networkidle2', timeout: 60000 });
        const fname = `${target}-${pg.prefix}-desktop.png`;
        screenshotManifest.push({ file: fname, ...await captureScreenshot(page, join(shotDir, fname)) });
      }
    }
    await page.close();
  }
}

// Build header diff pairs
for (const sel of SELECTORS) {
  const s = headerDiff.static.find((x) => x.key === sel.key && x.found);
  const r = headerDiff.runtime.find((x) => x.key === sel.key && x.found);
  if (!s && !r) continue;
  const pair = { key: sel.key, selector: sel.selector, static: s || { found: false }, runtime: r || { found: false }, diffs: [] };
  if (s?.found && r?.found) {
    for (const p of [...STYLE_PROPS, 'fontFamily']) {
      const sv = s[p] ?? s.fontFamily;
      const rv = r[p] ?? r.fontFamily;
      if (String(sv).trim() !== String(rv).trim()) {
        pair.diffs.push({ property: p, static: sv, runtime: rv, match: false });
      }
    }
  }
  headerDiff.pairs.push(pair);
}

for (const label of NAV_ITEMS) {
  const key = `nav_${label}`;
  const s = headerDiff.static.find((x) => x.key === key);
  const r = headerDiff.runtime.find((x) => x.key === key);
  const pair = { key, text: label, static: s, runtime: r, diffs: [] };
  if (s?.found && r?.found) {
    for (const p of [...STYLE_PROPS, 'fontFamily']) {
      const sv = s[p] ?? s.fontFamily;
      const rv = r[p] ?? r.fontFamily;
      if (String(sv).trim() !== String(rv).trim()) pair.diffs.push({ property: p, static: sv, runtime: rv, match: false });
    }
  }
  headerDiff.pairs.push(pair);
}

await browser.close();
server.close();

// Font failure analysis
function analyzeFonts(network, label) {
  const fonts = network.filter((n) => /\.woff2?|\.ttf/i.test(n.url));
  const failed = fonts.filter((f) => f.status >= 400);
  const css = network.filter((n) => /\.css/i.test(n.url));
  return { label, fontRequests: fonts.length, fontFailed: failed.length, failedUrls: failed.map((f) => ({ url: f.url, status: f.status })), cssRequests: css };
}

const staticFontAudit = analyzeFonts(staticNetwork, 'static');
const runtimeFontAudit = analyzeFonts(runtimeNetwork, 'runtime');

writeFileSync(join(evidenceDir, 'static-runtime-audit-setup.json'), JSON.stringify({
  task: 'V9-06D9-A',
  timestamp: new Date().toISOString(),
  staticServerMethod: 'node:http read-only file server',
  staticRoot,
  staticUrl,
  runtimeUrl,
  browser: chrome.includes('chrome') ? 'Google Chrome (headless via puppeteer-core)' : 'Microsoft Edge (headless via puppeteer-core)',
  viewports,
  deviceScaleFactor: 1,
  screenshotCount: screenshotManifest.length,
}, null, 2));

writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ task: 'V9-06D9-A', screenshots: screenshotManifest }, null, 2));

writeFileSync(join(evidenceDir, 'header-nav-computed-style-diff.json'), JSON.stringify({
  task: 'V9-06D9-A',
  viewport: viewports.desktop,
  staticStyles: headerDiff.static,
  runtimeStyles: headerDiff.runtime,
  pairs: headerDiff.pairs,
  staticFontAudit,
  runtimeFontAudit,
}, null, 2));

writeFileSync(join(evidenceDir, 'home-hero-parity-audit.json'), JSON.stringify({
  task: 'V9-06D9-A',
  static: staticHero,
  runtime: runtimeHero,
  staticHeroImageUrl: staticHero?.imageSrc ? staticUrl.replace(/\/$/, '') + staticHero.imageSrc : null,
  runtimeHeroImagePresent: runtimeHero?.hasImage || false,
  likelyRootCause: !runtimeHero?.hasImage ? 'ACF_IMAGE_NOT_SEEDED' : 'UNKNOWN',
}, null, 2));

// Section transfer audit
const staticSectionNames = staticSections.map((s) => s.className.split(' ')[0] || s.className);
const runtimeSectionNames = runtimeSections.map((s) => s.className.split(' ')[0] || s.className);

const sectionMap = [
  { name: 'intro-section + hero', staticSelector: '.intro-section > section.hero.hero--home', wpPartial: 'template-parts/home/hero.php' },
  { name: 'home-recovery-intro', staticSelector: 'section.home-recovery-intro', wpPartial: null },
  { name: 'founder-quote', staticSelector: 'section.founder-quote', wpPartial: null },
  { name: 'home-treatment-prevention', staticSelector: 'section.home-treatment-prevention', wpPartial: 'template-parts/home/treatment-prevention.php' },
  { name: 'home-gallery', staticSelector: 'section.home-gallery', wpPartial: 'template-parts/home/gallery.php' },
  { name: 'home-why-us', staticSelector: 'section.home-why-us', wpPartial: null },
  { name: 'home-staff-photo', staticSelector: 'section.home-staff-photo', wpPartial: null },
  { name: 'home-feature-grid', staticSelector: 'section.home-feature-grid', wpPartial: 'template-parts/home/feature-grid.php' },
  { name: 'clinic-landscape', staticSelector: 'section.clinic-landscape', wpPartial: null },
  { name: 'home-recovery-life', staticSelector: 'section.home-recovery-life', wpPartial: null },
  { name: 'reviews', staticSelector: 'section.reviews', wpPartial: null },
  { name: 'home-rehabilitation-requirements', staticSelector: 'section.home-rehabilitation-requirements', wpPartial: null },
  { name: 'home-rehabilitation-program', staticSelector: 'section.home-rehabilitation-program', wpPartial: 'template-parts/home/rehabilitation-program.php' },
  { name: 'home-genotyping', staticSelector: 'section.home-genotyping', wpPartial: null },
  { name: 'comfort', staticSelector: 'section.comfort', wpPartial: null },
  { name: 'home-videos', staticSelector: 'section.home-videos', wpPartial: null },
  { name: 'specialists', staticSelector: 'section.specialists', wpPartial: null },
  { name: 'home-articles', staticSelector: 'section.home-articles', wpPartial: 'template-parts/home/articles-teaser.php' },
  { name: 'faq', staticSelector: 'section.faq', wpPartial: 'template-parts/home/faq.php' },
  { name: 'final-form', staticSelector: 'section.final-form', wpPartial: 'template-parts/components/final-form.php' },
];

const homeSectionAudit = sectionMap.map((item, idx) => {
  const staticMatch = staticSections.find((s) => s.className.includes(item.staticSelector.replace('section.', '').split('.')[0]));
  const runtimeMatch = runtimeSections.find((s) => s.className.includes(item.staticSelector.replace('section.', '').split('.')[0]));
  let status = 'UNKNOWN_NEEDS_SOURCE_TRACE';
  let severity = 'MEDIUM';
  if (!item.wpPartial) { status = 'MISSING_FROM_WP_TEMPLATE'; severity = staticMatch ? 'HIGH' : 'LOW'; }
  else if (runtimeMatch) status = 'TRANSFERRED_AND_VISIBLE';
  else if (item.wpPartial) { status = 'TRANSFERRED_BUT_EMPTY'; severity = 'HIGH'; }
  if (item.name.includes('hero') && runtimeHero && !runtimeHero.hasImage) { status = 'TRANSFERRED_BUT_VISUALLY_DEGRADED'; severity = 'CRITICAL'; }
  return { ...item, orderIndex: idx + 1, staticPresent: !!staticMatch, runtimePresent: !!runtimeMatch, staticSection: staticMatch || null, runtimeSection: runtimeMatch || null, status, severity, recommendedRepairPhase: item.wpPartial ? (runtimeMatch ? 'D9-E' : 'D9-D') : 'D9-D' };
});

writeFileSync(join(evidenceDir, 'home-section-transfer-audit.json'), JSON.stringify({ task: 'V9-06D9-A', staticSectionCount: staticSections.length, runtimeSectionCount: runtimeSections.length, staticSections, runtimeSections, sections: homeSectionAudit }, null, 2));

writeFileSync(join(evidenceDir, 'global-typography-asset-font-audit.json'), JSON.stringify({
  task: 'V9-06D9-A',
  staticCss: staticNetwork.filter((n) => n.url.includes('.css')),
  runtimeCss: runtimeNetwork.filter((n) => n.url.includes('.css')),
  staticFontAudit,
  runtimeFontAudit,
  cssFontPathIssue: {
    description: 'v9-style.css @font-face uses absolute /assets/fonts/ paths valid on static dist but 404 on WordPress unless root alias exists',
    staticRootFontStatus: staticFontAudit.failedUrls,
    runtimeRootFontStatus: runtimeFontAudit.failedUrls,
  },
  keyTokens: {
    staticBody: headerDiff.static.find((x) => x.key === 'body'),
    runtimeBody: headerDiff.runtime.find((x) => x.key === 'body'),
  },
}, null, 2));

console.log('AUDIT_COMPLETE');
console.log(JSON.stringify({ screenshots: screenshotManifest.length, staticSections: staticSections.length, runtimeSections: runtimeSections.length, runtimeFontFailures: runtimeFontAudit.failedUrls.length }));
