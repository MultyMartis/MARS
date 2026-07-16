import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const evidenceDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const baseUrl = 'http://shpigovsky.test';

async function capture(name, width, height, scrollY, openMenu = false) {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto(baseUrl + '/', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(400);
  await page.evaluate((y) => window.scrollTo(0, y), scrollY);
  await page.waitForTimeout(500);
  if (openMenu) {
    await page.locator('.fp02-floating-header__menu-button').click();
    await page.waitForTimeout(400);
  }
  await page.screenshot({ path: path.join(evidenceDir, name), fullPage: false });
  await browser.close();
}

await capture('desktop-1440-home-floating-bg.png', 1440, 900, 800, false);
await capture('mobile-390-home-floating-bg.png', 390, 844, 700, false);
await capture('desktop-1440-home-menu-open.png', 1440, 900, 800, true);
await capture('mobile-390-home-menu-open.png', 390, 844, 700, true);
console.log('screenshots saved to', evidenceDir);
