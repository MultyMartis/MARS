import { chromium } from '../v9-06e60-nav-breadcrumb-cta-service-links/node_modules/playwright/index.mjs';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const OUT = __dirname;
const BASE = 'http://shpigovsky.test';

const VIEWPORTS = [
  { name: '1440x900', width: 1440, height: 900 },
  { name: '1024x768', width: 1024, height: 768 },
  { name: '480x900', width: 480, height: 900 },
  { name: '370x812', width: 370, height: 812 },
];

const BREADCRUMB_ROUTES = [
  '/uslugi/',
  '/uslugi/zavisimosti/',
  '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
  '/o-centre/',
  '/kontakty/',
  '/blog/',
  '/otzyvy/',
];

const SUBNAV_ROUTES = [
  '/uslugi/',
  '/uslugi/zavisimosti/',
  '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
];

const PROPS = [
  'fontSize',
  'lineHeight',
  'fontWeight',
  'letterSpacing',
  'display',
  'gap',
  'padding',
  'margin',
  'whiteSpace',
  'overflow',
  'color',
  'textDecoration',
  'flexWrap',
  'alignItems',
];

async function cs(page, selector) {
  return page.$eval(selector, (el, props) => {
    const s = getComputedStyle(el);
    const out = {};
    for (const p of props) out[p] = s[p];
    out.tagName = el.tagName;
    out.className = el.className;
    out.scrollWidth = document.documentElement.scrollWidth;
    out.clientWidth = document.documentElement.clientWidth;
    return out;
  }, PROPS).catch(() => null);
}

async function pageErrors(page) {
  const errors = [];
  page.on('pageerror', (e) => errors.push(String(e)));
  page.on('console', (msg) => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  return errors;
}

const report = {
  breadcrumb: [],
  subnav: [],
  reviews: [],
  overflow: [],
  phpWarnings: [],
  jsErrors: [],
  blogSingle: null,
};

const browser = await chromium.launch({ headless: true });

// Discover a blog single URL
{
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto(`${BASE}/blog/`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  const blogHref = await page.$eval(
    '.blog-card a[href], .blog-page a[href*="/blog/"]',
    (a) => a.href
  ).catch(() => null);
  report.blogSingle = blogHref;
  await page.close();
}

const crumbRoutes = [...BREADCRUMB_ROUTES];
if (report.blogSingle) {
  try {
    const u = new URL(report.blogSingle);
    crumbRoutes.push(u.pathname);
  } catch {}
}

for (const vp of VIEWPORTS) {
  for (const route of crumbRoutes) {
    const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
    const errs = [];
    page.on('pageerror', (e) => errs.push(String(e.message || e)));
    const res = await page.goto(`${BASE}${route}`, { waitUntil: 'networkidle', timeout: 90000 }).catch((e) => ({ ok: () => false, status: () => 0, err: String(e) }));
    const html = await page.content();
    if (/Warning:|Fatal error:|Parse error:/i.test(html)) {
      report.phpWarnings.push({ route, vp: vp.name, snippet: html.match(/Warning:|Fatal error:|Parse error:[^<]*/i)?.[0] });
    }
    const link = await cs(page, '.breadcrumbs__link, .breadcrumbs a, .internal-page-nav .breadcrumbs__link');
    const current = await cs(page, '.breadcrumbs__current, .internal-page-nav .breadcrumbs__current');
    const list = await cs(page, '.breadcrumbs__list, .internal-page-nav .breadcrumbs__list');
    const bodyOverflow = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      overflowX: getComputedStyle(document.documentElement).overflowX,
    }));
    report.breadcrumb.push({
      route,
      viewport: vp.name,
      status: typeof res.status === 'function' ? res.status() : 0,
      link,
      current,
      list,
    });
    if (bodyOverflow.scrollWidth > bodyOverflow.clientWidth + 1) {
      report.overflow.push({ route, viewport: vp.name, ...bodyOverflow });
    }
    if (errs.length) report.jsErrors.push({ route, viewport: vp.name, errs });
    const shotName = `crumb-${route.replace(/\//g, '_').replace(/^_|_$/g, '') || 'root'}-${vp.name}.png`;
    await page.screenshot({ path: path.join(OUT, 'screenshots', shotName), fullPage: false }).catch(() => {});
    await page.close();
  }

  for (const route of SUBNAV_ROUTES) {
    const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
    await page.goto(`${BASE}${route}`, { waitUntil: 'networkidle', timeout: 90000 });
    const subnav = await cs(page, '.services-page-subnav__link');
    const list = await cs(page, '.services-page-subnav__list');
    const count = await page.locator('.services-page-subnav__link').count();
    report.subnav.push({ route, viewport: vp.name, count, link: subnav, list });
    await page.screenshot({
      path: path.join(OUT, 'screenshots', `subnav-${route.replace(/\//g, '_').replace(/^_|_$/g, '')}-${vp.name}.png`),
      fullPage: false,
    }).catch(() => {});
    await page.close();
  }

  // Reviews page audit
  {
    const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
    const errs = [];
    page.on('pageerror', (e) => errs.push(String(e.message || e)));
    await page.goto(`${BASE}/otzyvy/`, { waitUntil: 'networkidle', timeout: 90000 });
    const nameInfo = await page.evaluate(() => {
      const el = document.querySelector('.review-archive-card__name');
      if (!el) return null;
      const s = getComputedStyle(el);
      return {
        tagName: el.tagName,
        className: el.className,
        fontSize: s.fontSize,
        lineHeight: s.lineHeight,
        fontWeight: s.fontWeight,
        margin: s.margin,
        marginTop: s.marginTop,
        marginBottom: s.marginBottom,
      };
    });
    const card = await page.evaluate(() => {
      const el = document.querySelector('.review-archive-card');
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        width: Math.round(r.width),
        padding: s.padding,
        gap: s.gap,
        borderRadius: s.borderRadius,
        backgroundColor: s.backgroundColor,
        boxShadow: s.boxShadow,
        minHeight: s.minHeight,
      };
    });
    const list = await page.evaluate(() => {
      const el = document.querySelector('.reviews-archive__list');
      if (!el) return null;
      const s = getComputedStyle(el);
      return {
        display: s.display,
        flexDirection: s.flexDirection,
        gap: s.gap,
        columns: s.columnCount,
        gridTemplateColumns: s.gridTemplateColumns,
        childCount: el.children.length,
      };
    });
    const body = await page.evaluate(() => {
      const el = document.querySelector('.review-archive-card__body');
      if (!el) return null;
      const s = getComputedStyle(el);
      return { fontSize: s.fontSize, lineHeight: s.lineHeight, color: s.color };
    });
    const h2Names = await page.locator('h2.review-archive-card__name').count();
    const divNames = await page.locator('div.review-archive-card__name').count();
    const overflow = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
    }));
    report.reviews.push({
      viewport: vp.name,
      nameInfo,
      card,
      list,
      body,
      h2Names,
      divNames,
      overflow,
      jsErrors: errs,
    });
    fs.mkdirSync(path.join(OUT, 'screenshots'), { recursive: true });
    await page.screenshot({ path: path.join(OUT, 'screenshots', `otzyvy-${vp.name}.png`), fullPage: true });
    // body crop focus
    const main = page.locator('.reviews-archive, .page-otzyvy__main').first();
    if (await main.count()) {
      await main.screenshot({ path: path.join(OUT, 'screenshots', `otzyvy-body-${vp.name}.png`) }).catch(() => {});
    }
    await page.close();
  }
}

// Regression smoke (header/footer presence)
const regression = {};
for (const route of ['/', '/uslugi/', '/otzyvy/', '/kontakty/']) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto(`${BASE}${route}`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  regression[route] = await page.evaluate(() => ({
    header: !!document.querySelector('.site-header, header.site-header'),
    floatingHeader: !!document.querySelector('.floating-header, .site-header--floating, [data-floating-header]'),
    footer: !!document.querySelector('.site-footer, footer.site-footer'),
    lifebuoy: !!document.querySelector('.fp02-lifebuoy, [data-lifebuoy], .lifebuoy'),
    programCta: !!document.querySelector('.program-cta-band, .home-rehabilitation-requirements__cta-band'),
  }));
  await page.close();
}
report.regression = regression;

fs.mkdirSync(path.join(OUT, 'screenshots'), { recursive: true });
fs.writeFileSync(path.join(OUT, 'validation-report.json'), JSON.stringify(report, null, 2), 'utf8');
console.log(JSON.stringify({
  crumbSamples: report.breadcrumb.filter((r) => r.viewport === '1440x900').map((r) => ({
    route: r.route,
    fs: r.link?.fontSize,
    lh: r.link?.lineHeight,
    color: r.link?.color,
  })),
  subnav1440: report.subnav.filter((r) => r.viewport === '1440x900').map((r) => ({
    route: r.route,
    count: r.count,
    fs: r.link?.fontSize,
    lh: r.link?.lineHeight,
    color: r.link?.color,
  })),
  reviews: report.reviews.map((r) => ({
    vp: r.viewport,
    tag: r.nameInfo?.tagName,
    fs: r.nameInfo?.fontSize,
    lh: r.nameInfo?.lineHeight,
    h2: r.h2Names,
    div: r.divNames,
    cardW: r.card?.width,
    overflow: r.overflow,
  })),
  overflowCount: report.overflow.length,
  phpWarnings: report.phpWarnings.length,
  jsErrors: report.jsErrors.length,
}, null, 2));

await browser.close();
