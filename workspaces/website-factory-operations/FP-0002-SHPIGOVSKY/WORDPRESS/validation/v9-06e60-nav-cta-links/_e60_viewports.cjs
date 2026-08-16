/**
 * V9-06E60 viewport + computed typography + CTA/service-link smoke.
 * Uses Playwright if available, else puppeteer-core skip.
 */
const fs = require('fs');
const path = require('path');

const outDir = 'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/evidence/v9-06e60-nav-breadcrumb-cta-service-links';
const viewports = [
  { name: '1440x900', width: 1440, height: 900 },
  { name: '1024x768', width: 1024, height: 768 },
  { name: '480x900', width: 480, height: 900 },
  { name: '370x812', width: 370, height: 812 },
];

async function main() {
  let chromium;
  try {
    ({ chromium } = require('playwright'));
  } catch (e) {
    fs.writeFileSync(path.join(outDir, 'viewport-validation.json'), JSON.stringify({ status: 'SKIP', reason: 'playwright not installed' }, null, 2));
    console.log('SKIP playwright');
    return;
  }

  const browser = await chromium.launch({ headless: true });
  const report = { status: 'OK', pages: {} };

  const pages = [
    { key: 'home', url: 'http://shpigovsky.test/' },
    { key: 'uslugi', url: 'http://shpigovsky.test/uslugi/' },
    { key: 'zavisimosti', url: 'http://shpigovsky.test/uslugi/zavisimosti/' },
    { key: 'blog', url: 'http://shpigovsky.test/blog/' },
  ];

  for (const pageDef of pages) {
    report.pages[pageDef.key] = {};
    for (const vp of viewports) {
      const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
      const errors = [];
      page.on('pageerror', (err) => errors.push(String(err)));
      const resp = await page.goto(pageDef.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      const metrics = await page.evaluate(() => {
        const pick = (sel) => {
          const el = document.querySelector(sel);
          if (!el) return null;
          const cs = getComputedStyle(el);
          return {
            fontSize: cs.fontSize,
            lineHeight: cs.lineHeight,
            fontWeight: cs.fontWeight,
            textDecorationLine: cs.textDecorationLine,
            color: cs.color,
          };
        };
        const overflow = document.documentElement.scrollWidth > document.documentElement.clientWidth + 1;
        const serviceNames = [...document.querySelectorAll('a.services-category-section-v2__service-name')].slice(0, 5).map((a) => ({ href: a.href, text: a.textContent.trim() }));
        const cta = {
          home: !!document.querySelector('.home-rehabilitation-requirements__cta-band .home-rehabilitation-requirements__cta-wrap01'),
          program: !!document.querySelector('.program-cta-band .program-cta-band__wrap01'),
          programLead: !!document.querySelector('.program-cta-band__lead'),
          oldTitle: !!document.querySelector('.program-cta-band__title'),
        };
        return {
          overflow,
          nav: pick('.site-header__nav-link'),
          offcanvas: pick('.offcanvas__nav-link'),
          crumb: pick('.breadcrumbs__link, .internal-page-nav .breadcrumbs__link'),
          serviceNames,
          cta,
        };
      });
      const shot = path.join(outDir, `shot-${pageDef.key}-${vp.name}.png`);
      await page.screenshot({ path: shot, fullPage: false });
      report.pages[pageDef.key][vp.name] = {
        http: resp ? resp.status() : 0,
        jsErrors: errors,
        ...metrics,
        screenshot: shot,
      };
      await page.close();
    }
  }

  await browser.close();
  fs.writeFileSync(path.join(outDir, 'viewport-validation.json'), JSON.stringify(report, null, 2));
  console.log('WROTE viewport-validation.json');
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
