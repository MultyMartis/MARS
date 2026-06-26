const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const outDir = path.resolve(__dirname, 'screenshots');
const baseUrl = process.env.PREVIEW_URL || 'http://127.0.0.1:4174';

async function capture() {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();

  const shots = [];

  async function shot(name, width, fn) {
    await page.setViewportSize({ width, height: 900 });
    await fn();
    const file = path.join(outDir, name);
    await page.screenshot({ path: file, fullPage: false });
    shots.push({ name, width, file });
  }

  await page.goto(`${baseUrl}/uslugi-v2.html`, { waitUntil: 'networkidle' });

  await page.setViewportSize({ width: 1398, height: 1200 });
  await page.screenshot({ path: path.join(outDir, 'SERVICES-V2-BLOCK-1-FULL-1398.png'), fullPage: true });
  await page.locator('.services-inner-hero-v2').screenshot({ path: path.join(outDir, 'SERVICES-V2-HERO-1398.png') });
  await page.locator('.breadcrumbs').screenshot({ path: path.join(outDir, 'SERVICES-V2-BREADCRUMBS-1398.png') });
  await page.locator('.services-page-subnav').screenshot({ path: path.join(outDir, 'SERVICES-V2-SUBNAV-1398.png') });

  await page.setViewportSize({ width: 390, height: 1400 });
  await page.goto(`${baseUrl}/uslugi-v2.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'SERVICES-V2-BLOCK-1-FULL-390.png'), fullPage: true });
  await page.locator('.services-inner-hero-v2').screenshot({ path: path.join(outDir, 'SERVICES-V2-HERO-390.png') });
  await page.locator('.breadcrumbs').screenshot({ path: path.join(outDir, 'SERVICES-V2-BREADCRUMBS-390.png') });
  await page.locator('.services-page-subnav').screenshot({ path: path.join(outDir, 'SERVICES-V2-SUBNAV-390.png') });

  await page.setViewportSize({ width: 1398, height: 1200 });
  await page.goto(`${baseUrl}/uslugi.html`, { waitUntil: 'networkidle' });
  await page.locator('.hero--inner').screenshot({ path: path.join(outDir, 'SERVICES-V1-UPPER-1398.png') });

  await page.setViewportSize({ width: 390, height: 1200 });
  await page.goto(`${baseUrl}/uslugi.html`, { waitUntil: 'networkidle' });
  await page.locator('.hero--inner').screenshot({ path: path.join(outDir, 'SERVICES-V1-UPPER-390.png') });

  await page.setViewportSize({ width: 1398, height: 1200 });
  await page.goto(`${baseUrl}/index.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'HOME-SMOKE-AFTER-SERVICES-V2-BLOCK-1-1398.png'), fullPage: true });

  await page.setViewportSize({ width: 390, height: 1400 });
  await page.goto(`${baseUrl}/index.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'HOME-SMOKE-AFTER-SERVICES-V2-BLOCK-1-390.png'), fullPage: true });

  const overflowV2 = await page.evaluate(async () => {
    await new Promise((r) => setTimeout(r, 100));
    return {
      v2_390: document.documentElement.scrollWidth > document.documentElement.clientWidth,
      v2_scrollWidth: document.documentElement.scrollWidth,
      v2_clientWidth: document.documentElement.clientWidth,
    };
  });

  await browser.close();

  fs.writeFileSync(
    path.join(outDir, 'capture-report.json'),
    JSON.stringify({ baseUrl, shots, overflowV2 }, null, 2),
    'utf8'
  );
}

capture().catch((err) => {
  console.error(err);
  process.exit(1);
});
