import { chromium } from 'playwright';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(__dirname, 'screenshots');
const shots = [
  { file: 'runtime-home-header-e21.png', url: 'http://shpigovsky.test/', selector: '.site-header' },
  { file: 'runtime-home-hero-e21.png', url: 'http://shpigovsky.test/', selector: '.home-hero' },
  { file: 'runtime-home-comfort-or-benefits-e21.png', url: 'http://shpigovsky.test/', selector: '.comfort' },
  { file: 'runtime-home-footer-e21.png', url: 'http://shpigovsky.test/', selector: '.site-footer' },
  { file: 'runtime-uslugi-header-footer-e21.png', url: 'http://shpigovsky.test/uslugi/', selector: '.site-header' },
  { file: 'runtime-zavisimosti-hero-and-shared-blocks-e21.png', url: 'http://shpigovsky.test/uslugi/zavisimosti/', selector: '.services-inner-hero-v2' },
  { file: 'runtime-alcohol-hero-and-footer-e21.png', url: 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', selector: '.services-inner-hero-v2' },
  { file: 'runtime-contacts-header-footer-e21.png', url: 'http://shpigovsky.test/kontakty/', selector: '.site-footer' },
  { file: 'runtime-otzyvy-regression-e21.png', url: 'http://shpigovsky.test/otzyvy/', selector: '.reviews-archive' },
  { file: 'runtime-privacy-legal-footer-e21.png', url: 'http://shpigovsky.test/privacy-policy/', selector: '.site-footer' },
];

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1200 } });
for (const shot of shots) {
  await page.goto(shot.url, { waitUntil: 'networkidle', timeout: 60000 });
  const filePath = path.join(outDir, shot.file);
  const locator = page.locator(shot.selector).first();
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await locator.screenshot({ path: filePath }).catch(async () => {
    await page.screenshot({ path: filePath, fullPage: true });
  });
  console.log('captured', shot.file);
}
await browser.close();
