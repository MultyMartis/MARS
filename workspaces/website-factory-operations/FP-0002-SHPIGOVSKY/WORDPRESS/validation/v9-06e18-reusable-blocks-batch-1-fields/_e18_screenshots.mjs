import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(__dirname, 'screenshots');
const shots = [
  { file: 'runtime-home-batch1-blocks-e18.png', url: 'http://shpigovsky.test/', fullPage: true },
  { file: 'runtime-home-specialists-e18.png', url: 'http://shpigovsky.test/', selector: '.specialists' },
  { file: 'runtime-home-reviews-e18.png', url: 'http://shpigovsky.test/', selector: '.reviews' },
  { file: 'runtime-home-final-form-e18.png', url: 'http://shpigovsky.test/', selector: '.final-form' },
  { file: 'runtime-zavisimosti-specialists-e18.png', url: 'http://shpigovsky.test/uslugi/zavisimosti/', selector: '#service-subdivision-specialists' },
  { file: 'runtime-zavisimosti-reviews-e18.png', url: 'http://shpigovsky.test/uslugi/zavisimosti/', selector: '.reviews' },
  { file: 'runtime-alcohol-specialists-e18.png', url: 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', selector: '#service-leaf-specialists' },
  { file: 'runtime-alcohol-final-form-e18.png', url: 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', selector: '.final-form' },
  { file: 'runtime-contacts-final-form-e18.png', url: 'http://shpigovsky.test/kontakty/', selector: '.page-kontakty__main' },
  { file: 'runtime-otzyvy-reviews-e18.png', url: 'http://shpigovsky.test/otzyvy/', selector: '.reviews-archive' },
  { file: 'runtime-privacy-regression-e18.png', url: 'http://shpigovsky.test/privacy-policy/', fullPage: true },
];

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1200 } });
for (const shot of shots) {
  await page.goto(shot.url, { waitUntil: 'networkidle', timeout: 60000 });
  const filePath = path.join(outDir, shot.file);
  if (shot.fullPage) {
    await page.screenshot({ path: filePath, fullPage: true });
  } else if (shot.selector) {
    const locator = page.locator(shot.selector).first();
    await locator.scrollIntoViewIfNeeded().catch(() => {});
    await locator.screenshot({ path: filePath }).catch(async () => {
      await page.screenshot({ path: filePath, fullPage: true });
    });
  } else {
    await page.screenshot({ path: filePath, fullPage: true });
  }
  console.log('captured', shot.file);
}
await browser.close();
