const { chromium } = require('playwright');
const { mkdirSync, writeFileSync } = require('fs');
const path = require('path');

const dist = path.resolve(__dirname, '../../../dist');
const outDir = path.resolve(__dirname, 'implementation');
mkdirSync(outDir, { recursive: true });

const widths = [320, 360, 375, 390, 430, 768, 1024, 1025, 1280, 1398, 1440];
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
    galleryCaptions: 0,
    gallerySlides: 0,
    captionOverlay: false,
  };

  for (const pageDef of pages) {
    const url = 'file:///' + path.join(dist, pageDef.file).replace(/\\/g, '/');
    for (const width of widths) {
      const page = await browser.newPage({ viewport: { width, height: 900 } });
      await page.goto(url, { waitUntil: 'networkidle' });
      await page.waitForTimeout(500);
      overflow[pageDef.key][width] = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth);
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
  checks.galleryCaptions = await home.locator('.home-gallery__caption').count();
  checks.gallerySlides = await home.locator('.home-gallery__slide').count();

  checks.captionOverlay = await home.evaluate(() => {
    const caption = document.querySelector('.home-gallery__caption');
    const image = document.querySelector('.home-gallery__image');
    if (!caption || !image) return true;
    const cs = getComputedStyle(caption);
    if (cs.position === 'absolute' || cs.position === 'fixed') return true;
    const cr = caption.getBoundingClientRect();
    const ir = image.getBoundingClientRect();
    return cr.top < ir.bottom - 1;
  });

  const shots = [
    ['HOME-FINAL-DESKTOP-1398.png', 1398, 3000, true],
    ['HOME-FINAL-DESKTOP-1280.png', 1280, 3000, true],
    ['HOME-FINAL-TABLET-1024.png', 1024, 3000, true],
    ['HOME-FINAL-MOBILE-430.png', 430, 3000, true],
    ['HOME-FINAL-MOBILE-390.png', 390, 3000, true],
    ['HOME-FINAL-MOBILE-320.png', 320, 3000, true],
    ['GALLERY-CAPTIONS-DESKTOP.png', 1398, 600, false, '.home-gallery'],
    ['RECOVERY-LIFE-DESKTOP.png', 1398, 800, false, '.home-recovery-life'],
    ['HEADER-DESKTOP.png', 1398, 200, false, '.site-header'],
    ['FOOTER-DESKTOP.png', 1398, 500, false, '.site-footer'],
  ];

  for (const [name, w, h, full] of shots.filter((s) => s.length === 4)) {
    await home.setViewportSize({ width: w, height: h });
    await home.screenshot({ path: path.join(outDir, name), fullPage: full });
  }

  for (const [name, w, h, , sel] of shots.filter((s) => s.length === 5)) {
    await home.setViewportSize({ width: w, height: h });
    await home.locator(sel).screenshot({ path: path.join(outDir, name) });
  }

  await home.setViewportSize({ width: 390, height: 1200 });
  await home.locator('.home-gallery').screenshot({ path: path.join(outDir, 'GALLERY-CAPTIONS-MOBILE-390.png') });
  await home.locator('.home-recovery-life').screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-MOBILE-390.png') });
  await home.locator('.site-header').screenshot({ path: path.join(outDir, 'HEADER-MOBILE.png') });
  await home.locator('.site-footer').screenshot({ path: path.join(outDir, 'FOOTER-MOBILE.png') });
  await home.setViewportSize({ width: 1398, height: 900 });
  await home.locator('.site-header__btns-wrap .btn[data-modal-open]').click();
  await home.waitForTimeout(400);
  await home.screenshot({ path: path.join(outDir, 'MODAL-DESKTOP.png') });
  await home.setViewportSize({ width: 390, height: 900 });
  await home.waitForTimeout(300);
  await home.screenshot({ path: path.join(outDir, 'MODAL-MOBILE.png') });
  await home.keyboard.press('Escape');
  await home.waitForTimeout(200);
  await home.setViewportSize({ width: 1024, height: 1200 });
  await home.locator('.home-recovery-life').screenshot({ path: path.join(outDir, 'RECOVERY-LIFE-TABLET-1024.png') });
  await home.close();

  const services = await browser.newPage({ viewport: { width: 1398, height: 3000 } });
  await services.goto('file:///' + path.join(dist, 'uslugi.html').replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-FINAL-DESKTOP-1398.png'), fullPage: true });
  await services.setViewportSize({ width: 1024, height: 3000 });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-FINAL-TABLET-1024.png'), fullPage: true });
  await services.setViewportSize({ width: 390, height: 3000 });
  await services.screenshot({ path: path.join(outDir, 'SERVICES-FINAL-MOBILE-390.png'), fullPage: true });
  await services.close();

  await browser.close();

  const result = { overflow, checks };
  writeFileSync(path.join(outDir, 'final-polish-visual-checks.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify(result, null, 2));
})();
