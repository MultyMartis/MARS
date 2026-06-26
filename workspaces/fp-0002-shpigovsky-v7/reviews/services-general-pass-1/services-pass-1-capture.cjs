const { chromium } = require('playwright');
const { mkdirSync, writeFileSync } = require('fs');
const path = require('path');

const dist = path.resolve(__dirname, '../../dist');
const outDir = path.resolve(__dirname, 'screenshots');
mkdirSync(outDir, { recursive: true });

const baseUrl = process.env.PREVIEW_URL || 'http://127.0.0.1:4174';

(async () => {
  const browser = await chromium.launch();
  const report = {
    overflow: { services: {}, home: {} },
    services: {},
    home: {},
    consoleErrors: { services: [], home: [] },
    missingAssets: { services: [], home: [] },
  };

  async function capturePage(pageKey, pagePath, checks) {
    const url = `${baseUrl}/${pagePath}`;
    const page = await browser.newPage({ viewport: { width: 1398, height: 1200 } });
    const consoleErrors = [];
    const failedRequests = [];

    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('requestfailed', (req) => {
      failedRequests.push(`${req.method()} ${req.url()} — ${req.failure()?.errorText || 'failed'}`);
    });

    await page.goto(url, { waitUntil: 'networkidle' });
    await page.waitForTimeout(800);

    for (const width of [390, 768, 1024, 1025, 1398, 1440, 1920]) {
      await page.setViewportSize({ width, height: 900 });
      await page.waitForTimeout(200);
      report.overflow[pageKey][width] = await page.evaluate(
        () => document.documentElement.scrollWidth > document.documentElement.clientWidth
      );
    }

    Object.assign(report[pageKey], await checks(page));
    report.consoleErrors[pageKey] = consoleErrors;
    report.missingAssets[pageKey] = failedRequests.filter((r) => !r.includes('favicon'));
    await page.close();
  }

  await capturePage('services', 'uslugi.html', async (page) => {
    const order = await page.evaluate(() =>
      [...document.querySelectorAll('main.page-uslugi > *')].map((el) => el.className || el.nodeName)
    );

    await page.setViewportSize({ width: 1398, height: 4000 });
    await page.screenshot({ path: path.join(outDir, 'SERVICES-PASS-1-FULL-1398.png'), fullPage: true });
    await page.locator('.hero--inner').screenshot({ path: path.join(outDir, 'SERVICES-PASS-1-HERO-1398.png') });
    await page.setViewportSize({ width: 390, height: 1200 });
    await page.locator('.hero--inner').screenshot({ path: path.join(outDir, 'SERVICES-PASS-1-HERO-390.png') });
    await page.setViewportSize({ width: 1398, height: 4000 });
    await page.locator('.home-rehabilitation-program').screenshot({
      path: path.join(outDir, 'SERVICES-PASS-1-REUSE-SECTIONS-1398.png'),
    });
    await page.setViewportSize({ width: 390, height: 4000 });
    const reuseStart = page.locator('.home-rehabilitation-program');
    const reuseEnd = page.locator('.home-final-form');
    const reuseBox = await reuseStart.boundingBox();
    const endBox = await reuseEnd.boundingBox();
    if (reuseBox && endBox) {
      await page.screenshot({
        path: path.join(outDir, 'SERVICES-PASS-1-REUSE-SECTIONS-390.png'),
        clip: {
          x: 0,
          y: reuseBox.y,
          width: 390,
          height: Math.min(endBox.y + endBox.height - reuseBox.y, 4000),
        },
      });
    }

    const heroCta = await page.locator('.hero--inner [data-modal-open]').count();
    const founderCtaWorks = await page.locator('.home-founder-quote [data-modal-open]').count();
    await page.locator('.home-founder-quote [data-modal-open]').first().click();
    await page.waitForTimeout(300);
    const modalOpen = await page.locator('[data-modal].is-open, .modal.is-open, [data-modal][aria-hidden="false"]').count();
    await page.keyboard.press('Escape');
    await page.waitForTimeout(200);

    const faqBtn = page.locator('.home-faq [data-accordion-button]').first();
    await faqBtn.click();
    await page.waitForTimeout(200);
    const faqExpanded = await faqBtn.getAttribute('aria-expanded');

    return {
      sectionOrder: order,
      heroPresent: (await page.locator('.hero--inner').count()) > 0,
      heroH1: await page.locator('.hero__title').textContent(),
      categoryPlaceholderVisible: (await page.locator('.services-category-hub').count()) > 0,
      heroCtaCount: heroCta,
      founderCtaCount: founderCtaWorks,
      modalOpens: modalOpen > 0,
      faqExpanded,
      comfortFancybox: (await page.locator('.home-comfort [data-fancybox]').count()) > 0,
      finalForm: (await page.locator('.home-final-form [data-lead-form]').count()) > 0,
      leadSource: await page.locator('.home-final-form [data-lead-hidden="lead_source"]').inputValue(),
      headerNav: (await page.locator('.site-header__nav-link--active').count()) > 0,
    };
  });

  await capturePage('home', 'index.html', async (page) => {
    await page.setViewportSize({ width: 1398, height: 4000 });
    await page.screenshot({ path: path.join(outDir, 'HOME-SMOKE-1398.png'), fullPage: true });
    await page.setViewportSize({ width: 390, height: 4000 });
    await page.screenshot({ path: path.join(outDir, 'HOME-SMOKE-390.png'), fullPage: true });

    return {
      variantB: (await page.locator('.home-founder-quote--variant-b').count()) > 0,
      recoveryIntro: (await page.locator('.home-recovery-intro').count()) > 0,
      gallerySwiper: await page.locator('[data-gallery-slider].swiper-initialized').count(),
      reviewsSwiper: await page.locator('.home-reviews .swiper-initialized').count(),
      specialistsSwiper: await page.locator('.home-specialists .swiper-initialized').count(),
      fancybox: (await page.locator('[data-fancybox]').count()) > 0,
    };
  });

  await browser.close();
  writeFileSync(path.join(outDir, 'capture-report.json'), JSON.stringify(report, null, 2));
  console.log(JSON.stringify(report, null, 2));
})();
