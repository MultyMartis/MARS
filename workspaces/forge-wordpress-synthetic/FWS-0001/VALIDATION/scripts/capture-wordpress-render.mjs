import { chromium } from 'playwright';
import { mkdir } from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.join(__dirname, '..', 'rendered');
const baseUrl = process.env.MLI_WP_URL || 'http://127.0.0.1/';
const wpHost = process.env.MLI_WP_HOST || 'fws-0001.test';

const viewports = [
  { name: 'desktop-1440', width: 1440, height: 900 },
  { name: 'tablet-1024', width: 1024, height: 900 },
  { name: 'mobile-390', width: 390, height: 844 },
];

const pages = [
  { path: '/', slug: 'home' },
  { path: '/services/', slug: 'services' },
  { path: '/services/testovaya-usluga/', slug: 'service-single' },
  { path: '/contacts/', slug: 'contacts' },
];

async function main() {
  await mkdir(outDir, { recursive: true });
  const browser = await chromium.launch({
    args: [`--host-resolver-rules=MAP ${wpHost} 127.0.0.1`],
  });
  const siteBase = `http://${wpHost}/`;

  try {
    for (const vp of viewports) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        deviceScaleFactor: 1,
      });
      const page = await context.newPage();
      await page.emulateMedia({ reducedMotion: 'reduce' });

      for (const p of pages) {
        const url = `${siteBase.replace(/\/$/, '')}${p.path}`;
        const response = await page.goto(url, { waitUntil: 'domcontentloaded' });
        if (!response || response.status() !== 200) {
          throw new Error(`HTTP ${response?.status()} for ${p.slug} @ ${vp.name}`);
        }
        const out = path.join(outDir, `${p.slug}__${vp.name}.png`);
        await page.screenshot({ path: out, fullPage: true });
        console.log('Captured', out);
      }
      await context.close();
    }
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
