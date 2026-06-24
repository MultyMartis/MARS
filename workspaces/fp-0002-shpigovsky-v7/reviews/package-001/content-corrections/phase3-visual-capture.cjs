const { chromium } = require('playwright');
const { mkdirSync, writeFileSync } = require('fs');
const path = require('path');

const dist = path.resolve(__dirname, '../../../dist');
const outDir = path.resolve(__dirname, 'implementation');
mkdirSync(outDir, { recursive: true });

const widths = [320, 375, 390, 430, 768, 1024, 1025, 1398];
const pages = [
  { file: 'index.html', key: 'home' },
  { file: 'uslugi.html', key: 'services' },
];

(async () => {
  const browser = await chromium.launch();
  const overflow = { home: {}, services: {} };
  const checks = {
    gallerySwiper: 0,
    reviewsSwiper: 0,
    specialistsSwiper: 0,
    fancybox: false,
    modal: false,
    faq: false,
    finalForm: false,
    faQuote: false,
    svgQuote: 0,
    galleryCaptions: 0,
    gallerySlides: 0,
  };

  for (const pageDef of pages) {
    const url = 'file:///' + path.join(dist, pageDef.file).replace(/\\/g, '/');
    for (const width of widths) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.waitForTimeout(500);
      const hasOverflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
      overflow[pageDef.key][width] = hasOverflow;
      await page.close();
    }
  }

  const home = await browser.newPage({ viewport: { width: 1398, height: 1200 } });
  await home.goto('file:///' + path.join(dist, 'index.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await home.waitForTimeout(800);
  checks.gallerySwiper = await home.locator('[data-gallery-slider].swiper-initialized').count();
  checks.reviewsSwiper = await home.locator('.home-reviews .swiper-initialized').count();
  checks.specialistsSwiper = await home.locator('.home-specialists .swiper-initialized').count();
  checks.fancybox = (await home.locator('[data-fancybox]').count()) > 0;
  checks.modal = (await home.locator('[data-modal-open]').count()) > 0;
  checks.faq = (await home.locator('.home-faq').count()) > 0;
  checks.finalForm = (await home.locator('.home-final-form').count()) > 0;
  checks.faQuote = await home.locator('.home-founder-quote__mark.fas').count();
  checks.svgQuote = await home.locator('svg.home-founder-quote__mark').count();
  checks.galleryCaptions = await home.locator('.home-gallery__caption').count();
  checks.gallerySlides = await home.locator('.home-gallery__slide').count();

  await home.locator('.home-recovery-intro').screenshot({ path: path.join(outDir, 'INTRO-DESKTOP-1398.png') });
  await home.setViewportSize({ width: 390, height: 1200 });
  await home.locator('.home-recovery-intro').screenshot({ path: path.join(outDir, 'INTRO-MOBILE-390.png') });
  await home.setViewportSize({ width: 1398, height: 1200 });
  await home.locator('.home-founder-quote').screenshot({ path: path.join(outDir, 'FOUNDER-QUOTE-DESKTOP.png') });
  await home.setViewportSize({ width: 390, height: 1200 });
  await home.locator('.home-founder-quote').screenshot({ path: path.join(outDir, 'FOUNDER-QUOTE-MOBILE-390.png') });
  await home.setViewportSize({ width: 1398, height: 1200 });
  await home.locator('.home-gallery').screenshot({ path: path.join(outDir, 'GALLERY-DESKTOP-1398.png') });
  await home.setViewportSize({ width: 390, height: 1200 });
  await home.locator('.home-gallery').screenshot({ path: path.join(outDir, 'GALLERY-MOBILE-390.png') });
  await home.setViewportSize({ width: 1398, height: 3000 });
  await home.screenshot({ path: path.join(outDir, 'HOME-FULL-DESKTOP-1398.png'), fullPage: true });
  await home.setViewportSize({ width: 390, height: 3000 });
  await home.screenshot({ path: path.join(outDir, 'HOME-FULL-MOBILE-390.png'), fullPage: true });
  await home.close();

  const services = await browser.newPage({ viewport: { width: 1398, height: 3000 } });
  await services.goto('file:///' + path.join(dist, 'uslugi.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-REGRESSION-DESKTOP.png'), fullPage: true });
  await services.setViewportSize({ width: 390, height: 3000 });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-REGRESSION-MOBILE-390.png'), fullPage: true });
  await services.close();

  await browser.close();

  const result = { overflow, checks };
  writeFileSync(path.join(outDir, 'phase3-visual-checks.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
})();
