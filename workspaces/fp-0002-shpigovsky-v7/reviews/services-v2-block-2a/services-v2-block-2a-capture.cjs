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

  async function overflowCheck() {
    return page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth,
    }));
  }

  async function shotTextBlock(suffix) {
    const box = await page.locator('.services-category-section-v2__container').boundingBox();
    if (box) {
      await page.screenshot({
        path: path.join(outDir, `SERVICES-V2-CATEGORY-01-TEXT-${suffix}.png`),
        clip: { x: box.x, y: box.y, width: box.width, height: Math.min(420, box.height) },
      });
    }
  }

  await page.setViewportSize({ width: 1398, height: 1600 });
  await page.goto(`${baseUrl}/uslugi-v2.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'SERVICES-V2-BLOCK-2A-FULL-1398.png'), fullPage: true });
  await page.locator('.services-category-section-v2').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-1398.png') });
  await shotTextBlock('1398');
  await page.locator('.services-category-section-v2__services').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-SERVICES-1398.png') });
  await page.locator('.services-category-section-v2__gallery').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-GALLERY-1398.png') });
  await page.locator('.services-category-section-v2__decor').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-DECOR-1398.png') });
  const overflow1398 = await overflowCheck();

  await page.setViewportSize({ width: 390, height: 2400 });
  await page.goto(`${baseUrl}/uslugi-v2.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'SERVICES-V2-BLOCK-2A-FULL-390.png'), fullPage: true });
  await page.locator('.services-category-section-v2').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-390.png') });
  await shotTextBlock('390');
  await page.locator('.services-category-section-v2__services').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-SERVICES-390.png') });
  await page.locator('.services-category-section-v2__gallery').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-GALLERY-390.png') });
  await page.locator('.services-category-section-v2__decor').screenshot({ path: path.join(outDir, 'SERVICES-V2-CATEGORY-01-DECOR-390.png') });
  const overflow390 = await overflowCheck();

  await page.setViewportSize({ width: 1398, height: 1600 });
  await page.goto(`${baseUrl}/uslugi.html`, { waitUntil: 'networkidle' });
  await page.locator('.services-category-hub--addictions').screenshot({ path: path.join(outDir, 'SERVICES-V1-CATEGORY-01-1398.png') });

  await page.setViewportSize({ width: 390, height: 2400 });
  await page.goto(`${baseUrl}/uslugi.html`, { waitUntil: 'networkidle' });
  await page.locator('.services-category-hub--addictions').screenshot({ path: path.join(outDir, 'SERVICES-V1-CATEGORY-01-390.png') });

  await page.setViewportSize({ width: 1398, height: 1200 });
  await page.goto(`${baseUrl}/index.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'HOME-SMOKE-AFTER-SERVICES-V2-BLOCK-2A-1398.png'), fullPage: true });

  await page.setViewportSize({ width: 390, height: 1400 });
  await page.goto(`${baseUrl}/index.html`, { waitUntil: 'networkidle' });
  await page.screenshot({ path: path.join(outDir, 'HOME-SMOKE-AFTER-SERVICES-V2-BLOCK-2A-390.png'), fullPage: true });

  await browser.close();

  fs.writeFileSync(
    path.join(outDir, 'capture-report.json'),
    JSON.stringify({ baseUrl, overflow1398, overflow390 }, null, 2),
    'utf8'
  );
}

capture().catch((err) => {
  console.error(err);
  process.exit(1);
});
