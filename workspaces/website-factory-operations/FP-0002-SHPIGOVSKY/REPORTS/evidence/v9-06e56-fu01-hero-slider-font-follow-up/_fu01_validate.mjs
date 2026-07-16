import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = __dirname;
const shots = path.join(outDir, 'screenshots');
fs.mkdirSync(shots, { recursive: true });

const base = 'http://shpigovsky.test';

function round(n) {
  return Math.round(n * 100) / 100;
}

async function measureHero(page, label) {
  return page.evaluate(() => {
    const home = document.querySelector('.hero--home');
    const ordinary = document.querySelector('.services-inner-hero-v2__media');
    const homeTitle = document.querySelector('.hero__title');
    const ordinaryTitle = document.querySelector('.services-inner-hero-v2__title');
    const box = (el) => {
      if (!el) return null;
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return {
        w: r.width,
        h: r.height,
        aspect: r.width && r.height ? r.width / r.height : null,
        aspectRatioCss: cs.aspectRatio,
        heightCss: cs.height,
        maxHeightCss: cs.maxHeight,
        fontFamily: cs.fontFamily,
        fontSize: cs.fontSize,
        fontWeight: cs.fontWeight,
        lineHeight: cs.lineHeight,
        letterSpacing: cs.letterSpacing,
      };
    };
    const slides = [...document.querySelectorAll('.hero--home .hero__slide')].map((s, i) => {
      const title = s.querySelector('.hero__title');
      const tag = s.querySelector('.hero__tagline');
      return {
        index: i,
        title: title ? title.textContent.trim() : null,
        tagline: tag ? tag.textContent.trim() : null,
        hasTaglineEl: !!tag,
        hasTitleEl: !!title,
      };
    });
    return {
      home: box(home),
      ordinary: box(ordinary),
      homeTitle: homeTitle
        ? {
            fontFamily: getComputedStyle(homeTitle).fontFamily,
            fontSize: getComputedStyle(homeTitle).fontSize,
            fontWeight: getComputedStyle(homeTitle).fontWeight,
            lineHeight: getComputedStyle(homeTitle).lineHeight,
            letterSpacing: getComputedStyle(homeTitle).letterSpacing,
          }
        : null,
      ordinaryTitle: ordinaryTitle
        ? {
            fontFamily: getComputedStyle(ordinaryTitle).fontFamily,
            fontSize: getComputedStyle(ordinaryTitle).fontSize,
            fontWeight: getComputedStyle(ordinaryTitle).fontWeight,
            lineHeight: getComputedStyle(ordinaryTitle).lineHeight,
            letterSpacing: getComputedStyle(ordinaryTitle).letterSpacing,
          }
        : null,
      slides,
      jsErrors: window.__fu01Errors || [],
    };
  });
}

async function measureGallery(page, rootSel, imageSel) {
  return page.evaluate(
    ({ rootSel, imageSel }) => {
      const root = document.querySelector(rootSel);
      if (!root) return { found: false };
      const swiper = root.swiper || null;
      const slides = [...root.querySelectorAll('.swiper-slide')];
      const visible = slides.filter((s) => {
        const r = s.getBoundingClientRect();
        const pr = root.getBoundingClientRect();
        return r.left < pr.right - 2 && r.right > pr.left + 2;
      });
      const img = root.querySelector(imageSel);
      const ics = img ? getComputedStyle(img) : null;
      const first = slides[0];
      const second = slides[1];
      let gap = null;
      if (first && second) {
        gap = second.getBoundingClientRect().left - first.getBoundingClientRect().right;
      }
      const pageOverflow = document.documentElement.scrollWidth > document.documentElement.clientWidth + 1;
      return {
        found: true,
        slidesPerViewParam: swiper ? swiper.params.slidesPerView : null,
        spaceBetween: swiper ? swiper.params.spaceBetween : null,
        breakpoints: swiper ? swiper.params.breakpoints : null,
        loop: swiper ? swiper.params.loop : null,
        autoplay: swiper ? !!swiper.params.autoplay : null,
        navigation: swiper ? !!swiper.params.navigation : null,
        watchOverflow: swiper ? swiper.params.watchOverflow : null,
        visibleCount: visible.length,
        slideWidth: first ? first.getBoundingClientRect().width : null,
        gap,
        imageHeight: img ? img.getBoundingClientRect().height : null,
        imageCssHeight: ics ? ics.height : null,
        imageMaxHeight: ics ? ics.maxHeight : null,
        imageObjectFit: ics ? ics.objectFit : null,
        pageOverflow,
        wrapperDisplay: (() => {
          const w = root.querySelector('.swiper-wrapper, .home-gallery__wrapper, .services-category-section-v2__gallery-wrapper');
          return w ? getComputedStyle(w).display : null;
        })(),
      };
    },
    { rootSel, imageSel }
  );
}

const browser = await chromium.launch({ headless: true });
const results = {
  aspect: [],
  gallery: [],
  heroSlides: null,
  fonts: {},
  routes: [],
  consoleErrors: [],
};

const aspectViewports = [
  { w: 767, h: 1024 },
  { w: 390, h: 844 },
  { w: 375, h: 812 },
  { w: 320, h: 568 },
];

for (const vp of aspectViewports) {
  const page = await browser.newPage({ viewport: { width: vp.w, height: vp.h } });
  page.on('pageerror', (e) => results.consoleErrors.push({ route: '/', vp, msg: String(e) }));
  page.on('console', (msg) => {
    if (msg.type() === 'error') results.consoleErrors.push({ route: '/', vp, msg: msg.text() });
  });
  await page.goto(`${base}/`, { waitUntil: 'networkidle' });
  const homeMeas = await measureHero(page);
  await page.screenshot({ path: path.join(shots, `home-hero-${vp.w}x${vp.h}.png`), fullPage: false });
  if (!results.heroSlides) results.heroSlides = homeMeas.slides;

  await page.goto(`${base}/uslugi/zavisimosti/`, { waitUntil: 'networkidle' });
  const ordinaryMeas = await measureHero(page);
  await page.locator('.services-inner-hero-v2__media').first().screenshot({
    path: path.join(shots, `ordinary-hero-media-${vp.w}x${vp.h}.png`),
  }).catch(async () => {
    await page.screenshot({ path: path.join(shots, `ordinary-hero-page-${vp.w}x${vp.h}.png`), fullPage: false });
  });

  const homeH = homeMeas.home;
  const ordH = ordinaryMeas.ordinary;
  const delta =
    homeH && ordH && homeH.aspect && ordH.aspect ? Math.abs(homeH.aspect - ordH.aspect) : null;
  const pass = delta !== null && delta < 0.05;
  results.aspect.push({
    viewport: `${vp.w}x${vp.h}`,
    ordinary: ordH,
    home: homeH,
    deltaAspect: delta,
    pass,
  });
  if (vp.w === 390) {
    results.fonts.homeTitle = homeMeas.homeTitle;
    results.fonts.ordinaryTitle = ordinaryMeas.ordinaryTitle;
  }
  await page.close();
}

const galleryViewports = [
  { w: 1440, h: 900 },
  { w: 1280, h: 800 },
  { w: 1024, h: 768 },
  { w: 768, h: 1024 },
  { w: 390, h: 844 },
  { w: 375, h: 812 },
  { w: 320, h: 568 },
];

for (const vp of galleryViewports) {
  const page = await browser.newPage({ viewport: { width: vp.w, height: vp.h } });
  await page.goto(`${base}/`, { waitUntil: 'networkidle' });
  const homeGal = await measureGallery(page, '[data-gallery-slider]', '.home-gallery__image');
  await page.locator('[data-gallery-slider]').first().screenshot({
    path: path.join(shots, `home-gallery-${vp.w}x${vp.h}.png`),
  }).catch(() => {});

  await page.goto(`${base}/uslugi/`, { waitUntil: 'networkidle' });
  const svcGal = await measureGallery(
    page,
    '[data-services-category-gallery]',
    '.services-category-section-v2__gallery-image'
  );
  await page.locator('[data-services-category-gallery]').first().screenshot({
    path: path.join(shots, `service-gallery-${vp.w}x${vp.h}.png`),
  }).catch(() => {});

  const sameSpv =
    homeGal.found &&
    svcGal.found &&
    String(homeGal.slidesPerViewParam) === String(svcGal.slidesPerViewParam) &&
    Number(homeGal.spaceBetween) === Number(svcGal.spaceBetween);
  const imgDelta =
    homeGal.imageHeight && svcGal.imageHeight
      ? Math.abs(homeGal.imageHeight - svcGal.imageHeight)
      : null;
  results.gallery.push({
    viewport: `${vp.w}x${vp.h}`,
    home: homeGal,
    service: svcGal,
    sameSwiperParams: sameSpv,
    imageHeightDelta: imgDelta,
    pass: sameSpv && !svcGal.pageOverflow && (imgDelta === null || imgDelta < 4),
  });
  await page.close();
}

const smoke = [
  '/',
  '/uslugi/',
  '/uslugi/zavisimosti/',
  '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
  '/uslugi/psihicheskie-rasstroystva/',
  '/o-centre/',
  '/kontakty/',
  '/blog/',
];
for (const route of smoke) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const errors = [];
  page.on('pageerror', (e) => errors.push(String(e)));
  const resp = await page.goto(`${base}${route}`, { waitUntil: 'domcontentloaded' });
  results.routes.push({ route, status: resp ? resp.status() : null, jsErrors: errors });
  await page.close();
}

await browser.close();

fs.writeFileSync(path.join(outDir, 'validation-matrix.json'), JSON.stringify(results, null, 2), 'utf8');

const aspectCsv = [
  'viewport,ordinary_w,ordinary_h,ordinary_aspect,home_w,home_h,home_aspect,delta,pass',
  ...results.aspect.map((r) =>
    [
      r.viewport,
      r.ordinary?.w,
      r.ordinary?.h,
      r.ordinary?.aspect,
      r.home?.w,
      r.home?.h,
      r.home?.aspect,
      r.deltaAspect,
      r.pass ? 'PASS' : 'FAIL',
    ].join(',')
  ),
].join('\n');
fs.writeFileSync(path.join(outDir, 'aspect-ratio-comparison.csv'), aspectCsv, 'utf8');

const galCsv = [
  'viewport,home_spv,svc_spv,home_gap,svc_gap,home_img_h,svc_img_h,overflow,same_params,pass',
  ...results.gallery.map((r) =>
    [
      r.viewport,
      r.home.slidesPerViewParam,
      r.service.slidesPerViewParam,
      r.home.gap,
      r.service.gap,
      r.home.imageHeight,
      r.service.imageHeight,
      r.service.pageOverflow,
      r.sameSwiperParams,
      r.pass ? 'PASS' : 'FAIL',
    ].join(',')
  ),
].join('\n');
fs.writeFileSync(path.join(outDir, 'gallery-comparison.csv'), galCsv, 'utf8');

console.log(JSON.stringify({
  aspectPass: results.aspect.filter((x) => x.pass).length,
  aspectTotal: results.aspect.length,
  galleryPass: results.gallery.filter((x) => x.pass).length,
  galleryTotal: results.gallery.length,
  heroSlides: results.heroSlides,
  fonts: results.fonts,
  routeFails: results.routes.filter((r) => r.status !== 200 || r.jsErrors.length),
  consoleErrors: results.consoleErrors.slice(0, 10),
}, null, 2));
