/**
 * V9-06E54 floating header validation — screenshots + probes.
 */
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright-core';

const BASE = 'http://shpigovsky.test';
const OUT = path.join(
  'X:',
  'AI MARS',
  'workspaces',
  'website-factory-operations',
  'FP-0002-SHPIGOVSKY',
  'REPORTS',
  'evidence',
  'v9-06e54-floating-header'
);

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  process.env.LOCALAPPDATA + '\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
const executablePath = chromeCandidates.find((c) => c && fs.existsSync(c));

const routes = [
  { name: 'home', path: '/' },
  { name: 'uslugi', path: '/uslugi/' },
  { name: 'section', path: '/uslugi/zavisimosti/' },
  { name: 'service', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' },
  { name: 'generic', path: '/politika-konfidentsialnosti/' },
  { name: 'o-centre', path: '/o-centre/' },
  { name: 'kontakty', path: '/kontakty/' },
  { name: 'blog', path: '/blog/' },
  { name: 'blog-single', path: '/blog/lechenie-zavisimosti-v-domashnih-usloviyah/' },
];

const viewports = [
  { id: 'desktop-1440', width: 1440, height: 900, mobile: false },
  { id: 'desktop-1280', width: 1280, height: 800, mobile: false },
  { id: 'desktop-1024', width: 1024, height: 768, mobile: false },
  { id: 'tablet-768', width: 768, height: 1024, mobile: true },
  { id: 'mobile-390', width: 390, height: 844, mobile: true },
  { id: 'mobile-375', width: 375, height: 812, mobile: true },
  { id: 'mobile-320', width: 320, height: 568, mobile: true },
];

function thresholdFor(width) {
  return width >= 1025 ? 500 : 650;
}

async function probeFloating(page, mobile) {
  return page.evaluate((isMobile) => {
    const root = document.querySelector('[data-fp02-floating-header]');
    const mainHeader = document.querySelector('.site-header');
    const offcanvas = document.querySelector('[data-offcanvas]');
    const menuBtn = document.querySelector('.fp02-floating-header__menu-button');
    const rect = root ? root.getBoundingClientRect() : null;
    const cs = root ? getComputedStyle(root) : null;
    return {
      hasFloating: !!root,
      hasMainHeader: !!mainHeader,
      floatingHeight: rect ? Math.round(rect.height) : null,
      floatingVisible: root ? root.classList.contains('is-visible') : false,
      ariaHidden: root ? root.getAttribute('aria-hidden') : null,
      opacity: cs ? cs.opacity : null,
      transform: cs ? cs.transform : null,
      overflowX: document.documentElement.scrollWidth > window.innerWidth + 1,
      menuBtn: !!menuBtn,
      offcanvasId: offcanvas ? offcanvas.id : null,
      scrollY: window.scrollY,
      threshold: isMobile ? 650 : 500,
    };
  }, mobile);
}

async function scrollProbe(page, viewport) {
  const threshold = thresholdFor(viewport.width);
  const results = { viewport: viewport.id, threshold, steps: [] };

  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(400);
  results.steps.push({ phase: 'top', ...(await probeFloating(page, viewport.mobile)) });

  await page.evaluate((y) => window.scrollTo(0, y), threshold - 50);
  await page.waitForTimeout(400);
  results.steps.push({ phase: 'below-threshold', ...(await probeFloating(page, viewport.mobile)) });

  await page.evaluate((y) => window.scrollTo(0, y), threshold + 200);
  await page.waitForTimeout(400);
  await page.evaluate((y) => window.scrollTo(0, y + 120));
  await page.waitForTimeout(500);
  const afterDown = await probeFloating(page, viewport.mobile);
  results.steps.push({ phase: 'scroll-down', ...afterDown });

  await page.evaluate((y) => window.scrollTo(0, y - 80), threshold + 320);
  await page.waitForTimeout(500);
  const afterUp = await probeFloating(page, viewport.mobile);
  results.steps.push({ phase: 'scroll-up', ...afterUp });

  return results;
}

async function menuProbe(page, shotPath) {
  const menuBtn = page.locator('.fp02-floating-header__menu-button');
  if ((await menuBtn.count()) === 0) {
    return { opened: false, reason: 'no-button' };
  }

  await page.evaluate((y) => window.scrollTo(0, y), 900);
  await page.waitForTimeout(300);
  await page.evaluate(() => window.scrollBy(0, 200));
  await page.waitForTimeout(500);

  await menuBtn.click();
  await page.waitForTimeout(400);

  const state = await page.evaluate(() => ({
    offcanvasState: document.querySelector('[data-offcanvas]')?.getAttribute('data-offcanvas-state'),
    bodyState: document.body.getAttribute('data-offcanvas-state'),
    ariaExpanded: document.querySelector('.fp02-floating-header__menu-button')?.getAttribute('aria-expanded'),
    hasPhones: !!document.querySelector('.offcanvas__phone'),
    hasMessengers: !!document.querySelector('.offcanvas__messengers'),
    hasCta: !!document.querySelector('.offcanvas__cta'),
    bodyOverflow: getComputedStyle(document.body).overflow,
  }));

  if (shotPath) {
    await page.screenshot({ path: shotPath, fullPage: false });
  }

  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  const afterEscape = await page.evaluate(() => ({
    offcanvasState: document.querySelector('[data-offcanvas]')?.getAttribute('data-offcanvas-state'),
    ariaExpanded: document.querySelector('.fp02-floating-header__menu-button')?.getAttribute('aria-expanded'),
  }));

  return { opened: state.offcanvasState === 'open', state, afterEscape };
}

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const report = {
    ts: new Date().toISOString(),
    base: BASE,
    routes: [],
    scroll: [],
    menu: [],
    consoleErrors: [],
    pageErrors: [],
  };

  const browser = await chromium.launch({ headless: true, executablePath });
  const context = await browser.newContext();

  for (const route of routes) {
    const page = await context.newPage();
    page.on('console', (msg) => {
      if (msg.type() === 'error') report.consoleErrors.push({ route: route.name, text: msg.text() });
    });
    page.on('pageerror', (e) => report.pageErrors.push({ route: route.name, text: String(e) }));

    const resp = await page.goto(BASE + route.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    const status = resp ? resp.status() : 0;
    const hasFloating = await page.locator('[data-fp02-floating-header]').count();
    const hasMain = await page.locator('.site-header').count();
    report.routes.push({
      route: route.name,
      path: route.path,
      status,
      hasFloating: hasFloating > 0,
      hasMainHeader: hasMain > 0,
    });
    await page.close();
  }

  // Scroll + screenshot matrix on home
  for (const vp of viewports) {
    const page = await context.newPage({ viewport: { width: vp.width, height: vp.height } });
    await page.goto(BASE + '/', { waitUntil: 'networkidle', timeout: 60000 });

    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(OUT, `${vp.id}-before.png`), fullPage: false });

    const scroll = await scrollProbe(page, vp);
    report.scroll.push(scroll);

    const visible = scroll.steps.find((s) => s.phase === 'scroll-down');
    if (visible && visible.floatingVisible) {
      await page.screenshot({ path: path.join(OUT, `${vp.id}-after-scroll-down.png`), fullPage: false });
    }

    if (vp.id === 'desktop-1440') {
      const menu = await menuProbe(page, path.join(OUT, 'desktop-1440-menu-open.png'));
      report.menu.push({ viewport: vp.id, ...menu });
    }

    if (vp.id === 'mobile-390') {
      const menu = await menuProbe(page, path.join(OUT, 'mobile-390-menu-open.png'));
      report.menu.push({ viewport: vp.id, ...menu });
    }

    if (vp.id === 'mobile-320') {
      await page.screenshot({ path: path.join(OUT, 'mobile-320-min.png'), fullPage: false });
    }

    await page.close();
  }

  // Regression screenshots
  for (const route of [
    { id: 'regression-home', path: '/' },
    { id: 'regression-uslugi', path: '/uslugi/' },
  ]) {
    const page = await context.newPage({ viewport: { width: 1440, height: 900 } });
    await page.goto(BASE + route.path, { waitUntil: 'networkidle', timeout: 60000 });
    await page.evaluate(() => window.scrollTo(0, 700));
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(OUT, `${route.id}.png`), fullPage: false });
    await page.close();
  }

  await browser.close();

  const outJson = path.join(OUT, 'validation-results.json');
  fs.writeFileSync(outJson, JSON.stringify(report, null, 2));
  console.log('VALIDATION_OUT=' + outJson);
  console.log('ROUTES_PASS=' + report.routes.filter((r) => r.status === 200 && r.hasFloating).length + '/' + report.routes.length);
  console.log('JS_ERRORS=' + report.pageErrors.length);
  console.log('CONSOLE_ERRORS=' + report.consoleErrors.length);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
