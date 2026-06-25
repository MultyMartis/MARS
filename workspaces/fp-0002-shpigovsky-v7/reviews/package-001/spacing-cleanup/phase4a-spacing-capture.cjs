const { chromium } = require('playwright');
const { mkdirSync, writeFileSync } = require('fs');
const path = require('path');

const mode = process.argv[2] || 'before';
const dist = path.resolve(__dirname, '../../../dist');
const outDir = path.resolve(__dirname, 'implementation');
mkdirSync(outDir, { recursive: true });

const widths = [320, 375, 390, 430, 768, 1024, 1025, 1398];

const homeSections = [
  'hero',
  'home-recovery-intro',
  'home-founder-quote',
  'home-treatment-prevention',
  'home-gallery',
  'home-why-us',
  'home-staff-photo',
  'home-feature-grid',
  'home-clinic-landscape',
  'home-recovery-life',
  'home-reviews',
  'home-rehabilitation-requirements',
  'home-rehabilitation-program',
  'home-genotyping',
  'home-comfort',
  'home-videos',
  'home-specialists',
  'home-articles',
  'home-faq',
  'home-final-form',
];

const servicesSections = [
  'home-rehabilitation-program',
  'home-founder-quote',
  'home-comfort',
  'home-faq',
  'home-final-form',
];

(async () => {
  const browser = await chromium.launch();
  const overflow = { home: {}, services: {} };
  const measurements = { home: {}, services: {} };
  const checks = {
    gallerySwiper: 0,
    reviewsSwiper: 0,
    specialistsSwiper: 0,
    fancybox: false,
    faq: false,
    modal: false,
    finalForm: false,
  };

  async function measureSections(page, sections, key, width) {
    const result = {};
    for (const cls of sections) {
      const sel = cls === 'hero' ? '.hero' : `.${cls}`;
      const el = page.locator(sel).first();
      if ((await el.count()) === 0) {
        result[cls] = null;
        continue;
      }
      const box = await el.boundingBox();
      const styles = await el.evaluate((node) => {
        const cs = getComputedStyle(node);
        return {
          paddingTop: cs.paddingTop,
          paddingBottom: cs.paddingBottom,
        };
      });
      result[cls] = {
        top: box ? Math.round(box.y) : null,
        bottom: box ? Math.round(box.y + box.height) : null,
        height: box ? Math.round(box.height) : null,
        paddingTop: styles.paddingTop,
        paddingBottom: styles.paddingBottom,
      };
    }
    measurements[key][width] = result;
  }

  for (const pageKey of ['home', 'services']) {
    const file = pageKey === 'home' ? 'index.html' : 'uslugi.html';
    const url = 'file:///' + path.join(dist, file).replace(/\\/g, '/');
    for (const width of widths) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.waitForTimeout(400);
      overflow[pageKey][width] = await page.evaluate(
        () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
      );
      await page.close();
    }
  }

  const home = await browser.newPage({ viewport: { width: 1398, height: 5000 } });
  await home.goto('file:///' + path.join(dist, 'index.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await home.waitForTimeout(800);
  await measureSections(home, homeSections, 'home', 1398);
  await home.screenshot({
    path: path.join(outDir, `HOME-SPACING-${mode.toUpperCase()}-1398.png`),
    fullPage: true,
  });
  await home.setViewportSize({ width: 390, height: 6000 });
  await home.waitForTimeout(400);
  await measureSections(home, homeSections, 'home', 390);
  await home.screenshot({
    path: path.join(outDir, `HOME-SPACING-${mode.toUpperCase()}-390.png`),
    fullPage: true,
  });

  checks.gallerySwiper = await home.locator('[data-gallery-slider].swiper-initialized').count();
  checks.reviewsSwiper = await home.locator('.home-reviews .swiper-initialized').count();
  checks.specialistsSwiper = await home.locator('.home-specialists .swiper-initialized').count();
  checks.fancybox = (await home.locator('[data-fancybox]').count()) > 0;
  checks.modal = (await home.locator('[data-modal-open]').count()) > 0;
  checks.faq = (await home.locator('.home-faq').count()) > 0;
  checks.finalForm = (await home.locator('.home-final-form').count()) > 0;
  await home.close();

  const services = await browser.newPage({ viewport: { width: 1398, height: 3000 } });
  await services.goto('file:///' + path.join(dist, 'uslugi.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await services.waitForTimeout(600);
  await measureSections(services, servicesSections, 'services', 1398);
  await services.screenshot({
    path: path.join(outDir, `SERVICES-SPACING-${mode.toUpperCase()}-1398.png`),
    fullPage: true,
  });
  await services.setViewportSize({ width: 390, height: 3000 });
  await services.waitForTimeout(400);
  await measureSections(services, servicesSections, 'services', 390);
  await services.screenshot({
    path: path.join(outDir, `SERVICES-SPACING-${mode.toUpperCase()}-390.png`),
    fullPage: true,
  });
  await services.close();
  await browser.close();

  const payload = { mode, overflow, measurements, checks };
  writeFileSync(path.join(outDir, `spacing-${mode}-metrics.json`), JSON.stringify(payload, null, 2));
  console.log(JSON.stringify(payload, null, 2));
})();
