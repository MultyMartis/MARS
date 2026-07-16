import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const evidenceDir = path.resolve(__dirname, '..');
const baseUrl = 'http://shpigovsky.test';

const viewports = [
  { name: 'desktop-1440', width: 1440, height: 900, scrollTarget: 800 },
  { name: 'desktop-1280', width: 1280, height: 800, scrollTarget: 800 },
  { name: 'desktop-1024', width: 1024, height: 768, scrollTarget: 800 },
  { name: 'mobile-390', width: 390, height: 844, scrollTarget: 700 },
  { name: 'mobile-375', width: 375, height: 812, scrollTarget: 700 },
  { name: 'mobile-320', width: 320, height: 568, scrollTarget: 700 },
];

const routes = ['/', '/uslugi/', '/o-centre/', '/kontakty/', '/blog/'];

async function gotoRoute(page, route) {
  const url = route === '/' ? `${baseUrl}/` : `${baseUrl}${route}`;
  return page.goto(url, { waitUntil: 'domcontentloaded' });
}

async function probeRoute(page, route, viewport) {
  await gotoRoute(page, route);
  await page.waitForTimeout(400);

  const scrollTarget = viewport.scrollTarget;
  await page.evaluate((y) => window.scrollTo(0, y), scrollTarget);
  await page.waitForTimeout(500);

  const before = await page.evaluate(() => {
    const marker = document.querySelector('main, .site-main, #content, body > .container');
    return {
      scrollY: window.scrollY,
      url: location.href,
      hash: location.hash,
      floatingVisible: !!document.querySelector('.fp02-floating-header.is-visible'),
      bg: getComputedStyle(document.querySelector('.fp02-floating-header') || document.body).backgroundColor,
      markerTop: marker ? marker.getBoundingClientRect().top : null,
    };
  });

  const menuBtn = page.locator('.fp02-floating-header__menu-button');
  await menuBtn.waitFor({ state: 'visible', timeout: 5000 });
  await menuBtn.click();
  await page.waitForTimeout(400);

  const afterOpen = await page.evaluate(() => {
    const marker = document.querySelector('main, .site-main, #content, body > .container');
    return {
      scrollY: window.scrollY,
      url: location.href,
      hash: location.hash,
      offcanvasOpen: document.body.getAttribute('data-offcanvas-state') === 'open',
      bodyPosition: getComputedStyle(document.body).position,
      bodyLockClass: document.body.classList.contains('is-offcanvas-scroll-locked'),
      bg: getComputedStyle(document.querySelector('.fp02-floating-header')).backgroundColor,
      markerTop: marker ? marker.getBoundingClientRect().top : null,
    };
  });

  const shotOpen = `${viewport.name}-${route.replace(/\//g, '_') || 'home'}-menu-open.png`;
  await page.screenshot({ path: path.join(evidenceDir, shotOpen), fullPage: false });

  await page.keyboard.press('Escape');
  await page.waitForTimeout(400);

  const afterClose = await page.evaluate(() => {
    const marker = document.querySelector('main, .site-main, #content, body > .container');
    return {
      scrollY: window.scrollY,
      url: location.href,
      hash: location.hash,
      offcanvasOpen: document.body.getAttribute('data-offcanvas-state') === 'open',
      markerTop: marker ? marker.getBoundingClientRect().top : null,
    };
  });

  const deltaOpen = Math.abs(afterOpen.scrollY - before.scrollY);
  const deltaClose = Math.abs(afterClose.scrollY - before.scrollY);
  const visualDeltaOpen = before.markerTop !== null && afterOpen.markerTop !== null
    ? Math.abs(afterOpen.markerTop - before.markerTop)
    : null;
  const pass = deltaOpen <= 2 && deltaClose <= 2 && afterOpen.hash === before.hash && afterOpen.offcanvasOpen
    && (visualDeltaOpen === null || visualDeltaOpen <= 2);

  return {
    viewport: viewport.name,
    route,
    scrollBefore: before.scrollY,
    scrollAfterOpen: afterOpen.scrollY,
    scrollAfterClose: afterClose.scrollY,
    deltaOpen,
    deltaClose,
    urlBefore: before.url,
    urlAfterOpen: afterOpen.url,
    hashBefore: before.hash,
    hashAfterOpen: afterOpen.hash,
    floatingVisibleBefore: before.floatingVisible,
    backgroundRgb: afterOpen.bg,
    visualDeltaOpen,
    bodyPosition: afterOpen.bodyPosition,
    result: pass ? 'PASS' : 'FAIL',
  };
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const results = [];
  const errors = [];

  for (const viewport of viewports) {
    const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height } });
    const page = await context.newPage();
    page.on('pageerror', (e) => errors.push({ viewport: viewport.name, error: e.message }));

    try {
      const row = await probeRoute(page, '/', viewport);
      results.push(row);

      const shotBg = `${viewport.name}-home-floating-bg.png`;
      await page.evaluate((y) => window.scrollTo(0, y), viewport.scrollTarget);
      await page.waitForTimeout(300);
      await page.screenshot({ path: path.join(evidenceDir, shotBg), fullPage: false });
    } catch (e) {
      results.push({ viewport: viewport.name, route: '/', result: 'FAIL', error: String(e) });
    }

    await context.close();
  }

  // Regression routes desktop only
  const regContext = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const regPage = await regContext.newPage();
  for (const route of routes) {
    try {
      const resp = await gotoRoute(regPage, route);
      await regPage.evaluate(() => window.scrollTo(0, 800));
      await regPage.waitForTimeout(400);
      const ok = resp && resp.status() === 200;
      const floating = await regPage.locator('.fp02-floating-header.is-visible').count();
      results.push({
        viewport: 'desktop-1440-regression',
        route,
        httpStatus: resp ? resp.status() : 0,
        floatingVisible: floating > 0,
        result: ok && floating > 0 ? 'PASS' : 'FAIL',
      });
    } catch (e) {
      results.push({ viewport: 'desktop-1440-regression', route, result: 'FAIL', error: String(e) });
    }
  }
  await regContext.close();
  await browser.close();

  const outJson = path.join(evidenceDir, 'scroll-probe-results.json');
  fs.writeFileSync(outJson, JSON.stringify({ results, errors, generatedAt: new Date().toISOString() }, null, 2));

  const csvLines = ['viewport,route,scrollBefore,scrollAfterOpen,scrollAfterClose,deltaOpen,deltaClose,hashBefore,hashAfterOpen,result'];
  for (const r of results) {
    if (r.scrollBefore !== undefined) {
      csvLines.push([
        r.viewport, r.route, r.scrollBefore, r.scrollAfterOpen, r.scrollAfterClose,
        r.deltaOpen, r.deltaClose, r.hashBefore || '', r.hashAfterOpen || '', r.result,
      ].join(','));
    }
  }
  fs.writeFileSync(path.join(evidenceDir, 'scroll-probe-results.csv'), csvLines.join('\n'));

  console.log(JSON.stringify({ resultsCount: results.length, errorsCount: errors.length, outJson }, null, 2));
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
