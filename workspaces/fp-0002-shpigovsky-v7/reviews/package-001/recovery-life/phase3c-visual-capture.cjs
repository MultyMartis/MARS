const { chromium } = require('playwright');
const { mkdirSync, writeFileSync } = require('fs');
const path = require('path');

const dist = path.resolve(__dirname, '../../../dist');
const outDir = path.resolve(__dirname, 'implementation');
mkdirSync(outDir, { recursive: true });

const widths = [320, 375, 390, 430, 768, 1024, 1025, 1398];

(async () => {
  const browser = await chromium.launch();
  const overflow = { home: {}, services: {} };
  const checks = {
    gallerySwiper: 0,
    reviewsSwiper: 0,
    specialistsSwiper: 0,
    fancybox: false,
    faq: false,
    modal: false,
    finalForm: false,
    recoveryLife: false,
  };

  for (const pageKey of ['home', 'services']) {
    const file = pageKey === 'home' ? 'index.html' : 'uslugi.html';
    const url = 'file:///' + path.join(dist, file).replace(/\\/g, '/');
    for (const width of widths) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.waitForTimeout(500);
      overflow[pageKey][width] = await page.evaluate(
        () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
      );
      await page.close();
    }
  }

  const home = await browser.newPage({ viewport: { width: 1398, height: 1400 } });
  await home.goto('file:///' + path.join(dist, 'index.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await home.waitForTimeout(800);

  checks.gallerySwiper = await home.locator('[data-gallery-slider].swiper-initialized').count();
  checks.reviewsSwiper = await home.locator('.home-reviews .swiper-initialized').count();
  checks.specialistsSwiper = await home.locator('.home-specialists .swiper-initialized').count();
  checks.fancybox = (await home.locator('[data-fancybox]').count()) > 0;
  checks.modal = (await home.locator('[data-modal-open]').count()) > 0;
  checks.faq = (await home.locator('.home-faq').count()) > 0;
  checks.finalForm = (await home.locator('.home-final-form').count()) > 0;
  checks.recoveryLife = (await home.locator('.home-recovery-life').count()) > 0;

  const section = home.locator('.home-recovery-life');
  await section.screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-DESKTOP-1398.png') });
  await home.setViewportSize({ width: 1025, height: 1400 });
  await section.screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-DESKTOP-1025.png') });
  await home.setViewportSize({ width: 768, height: 1600 });
  await section.screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-TABLET-768.png') });
  await home.setViewportSize({ width: 430, height: 1800 });
  await section.screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-MOBILE-430.png') });
  await home.setViewportSize({ width: 390, height: 1800 });
  await section.screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-MOBILE-390.png') });
  await home.setViewportSize({ width: 320, height: 1800 });
  await section.screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-MOBILE-320.png') });
  await home.setViewportSize({ width: 1398, height: 4000 });
  await home.screenshot({ path: path.join(outDir, 'HOME-FULL-AFTER-RECOVERY-LIFE-1398.png'), fullPage: true });
  await home.setViewportSize({ width: 390, height: 4000 });
  await home.screenshot({ path: path.join(outDir, 'HOME-FULL-AFTER-RECOVERY-LIFE-390.png'), fullPage: true });
  await home.close();

  const services = await browser.newPage({ viewport: { width: 1398, height: 3000 } });
  await services.goto('file:///' + path.join(dist, 'uslugi.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-REGRESSION-1398.png'), fullPage: true });
  await services.setViewportSize({ width: 390, height: 3000 });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-REGRESSION-390.png'), fullPage: true });
  await services.close();

  await browser.close();

  const result = { overflow, checks };
  writeFileSync(path.join(outDir, 'recovery-life-visual-checks.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
})();
