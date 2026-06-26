const { chromium } = require('playwright');
const { mkdirSync, writeFileSync } = require('fs');
const path = require('path');

const outDir = path.resolve(__dirname, 'screenshots');
mkdirSync(outDir, { recursive: true });

const baseUrl = process.env.PREVIEW_URL || 'http://127.0.0.1:4174';

(async () => {
  const browser = await chromium.launch();
  const report = {
    overflow: { services: {}, home: {} },
    consoleErrors: { services: [], home: [] },
    missingAssets: { services: [], home: [] },
    duplicateIds: { services: [], home: [] },
  };

  async function attachListeners(page, key) {
    page.on('console', (msg) => {
      if (msg.type() === 'error') report.consoleErrors[key].push(msg.text());
    });
    page.on('requestfailed', (req) => {
      report.missingAssets[key].push(`${req.method()} ${req.url()} — ${req.failure()?.errorText || 'failed'}`);
    });
  }

  const servicesPage = await browser.newPage();
  attachListeners(servicesPage, 'services');
  await servicesPage.goto(`${baseUrl}/uslugi.html`, { waitUntil: 'networkidle' });
  await servicesPage.waitForTimeout(800);

  report.duplicateIds.services = await servicesPage.evaluate(() => {
    const ids = [...document.querySelectorAll('[id]')].map((el) => el.id);
    return ids.filter((id, i) => ids.indexOf(id) !== i);
  });

  for (const width of [320, 390, 430, 768, 1024, 1025, 1280, 1398, 1440, 1920]) {
    await servicesPage.setViewportSize({ width, height: 900 });
    await servicesPage.waitForTimeout(150);
    report.overflow.services[width] = await servicesPage.evaluate(
      () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
    );
  }

  async function shot(page, filePath, locator) {
    if (locator) {
      await locator.scrollIntoViewIfNeeded();
      await locator.screenshot({ path: filePath });
      return;
    }
    await page.screenshot({ path: filePath, fullPage: true });
  }

  await servicesPage.setViewportSize({ width: 1398, height: 5000 });
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-FULL-1398.png'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HERO-1398.png'), servicesPage.locator('.hero--inner'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-01-1398.png'), servicesPage.locator('.services-category-hub--addictions'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-02-1398.png'), servicesPage.locator('.services-category-hub--mental-health'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-03-1398.png'), servicesPage.locator('.services-category-hub--eating-disorders'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-04-1398.png'), servicesPage.locator('.services-category-hub--genotyping'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-LOWER-1398.png'), servicesPage.locator('.home-rehabilitation-program'));

  await servicesPage.setViewportSize({ width: 390, height: 5000 });
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-FULL-390.png'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HERO-390.png'), servicesPage.locator('.hero--inner'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-01-390.png'), servicesPage.locator('.services-category-hub--addictions'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-02-390.png'), servicesPage.locator('.services-category-hub--mental-health'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-03-390.png'), servicesPage.locator('.services-category-hub--eating-disorders'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-HUB-04-390.png'), servicesPage.locator('.services-category-hub--genotyping'));
  await shot(servicesPage, path.join(outDir, 'SERVICES-FINAL-LOWER-390.png'), servicesPage.locator('.home-rehabilitation-program'));
  await servicesPage.close();

  const homePage = await browser.newPage();
  attachListeners(homePage, 'home');
  await homePage.goto(`${baseUrl}/index.html`, { waitUntil: 'networkidle' });
  report.duplicateIds.home = await homePage.evaluate(() => {
    const ids = [...document.querySelectorAll('[id]')].map((el) => el.id);
    return ids.filter((id, i) => ids.indexOf(id) !== i);
  });
  for (const width of [320, 390, 430, 768, 1024, 1025, 1280, 1398, 1440, 1920]) {
    await homePage.setViewportSize({ width, height: 900 });
    await homePage.waitForTimeout(100);
    report.overflow.home[width] = await homePage.evaluate(
      () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
    );
  }
  await homePage.setViewportSize({ width: 1398, height: 3000 });
  await homePage.screenshot({ path: path.join(outDir, 'HOME-SMOKE-AFTER-SERVICES-FINAL-1398.png'), fullPage: true });
  await homePage.setViewportSize({ width: 390, height: 3000 });
  await homePage.screenshot({ path: path.join(outDir, 'HOME-SMOKE-AFTER-SERVICES-FINAL-390.png'), fullPage: true });
  await homePage.close();

  writeFileSync(path.join(outDir, 'capture-report.json'), JSON.stringify(report, null, 2));
  await browser.close();
  console.log(JSON.stringify(report, null, 2));
})();
