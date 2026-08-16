const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const evidence = String.raw`X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\v9-06e62d-program-mini-descriptions-404-figma-correction`;
const outDir = path.join(evidence, 'before');
fs.mkdirSync(outDir, { recursive: true });

const viewports = [
  { w: 1440, h: 900 },
  { w: 1024, h: 768 },
  { w: 480, h: 900 },
  { w: 370, h: 812 },
];

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  const matrix = [];

  for (const vp of viewports) {
    await page.setViewport({ width: vp.w, height: vp.h, deviceScaleFactor: 1 });
    const resp = await page.goto('http://shpigovsky.test/this-page-definitely-does-not-exist-e62d/', {
      waitUntil: 'networkidle2',
      timeout: 60000,
    });
    const metrics = await page.evaluate(() => {
      const pick = (sel) => {
        const el = document.querySelector(sel);
        if (!el) return null;
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        return {
          fontFamily: cs.fontFamily,
          fontSize: cs.fontSize,
          fontWeight: cs.fontWeight,
          lineHeight: cs.lineHeight,
          letterSpacing: cs.letterSpacing,
          color: cs.color,
          width: Math.round(r.width),
          height: Math.round(r.height),
          top: Math.round(r.top),
          bottom: Math.round(r.bottom),
        };
      };
      const pageEl = document.querySelector('.page-404');
      const content = document.querySelector('.page-404__content');
      const pageCs = pageEl ? getComputedStyle(pageEl) : null;
      const contentCs = content ? getComputedStyle(content) : null;
      return {
        statusHint: document.title,
        bg: pageCs ? pageCs.backgroundColor : null,
        contentPadding: contentCs
          ? {
              top: contentCs.paddingTop,
              bottom: contentCs.paddingBottom,
            }
          : null,
        title: pick('.page-404__title'),
        lead: pick('.page-404__lead'),
        logo: pick('.page-404__logo'),
        brand: pick('.page-404__brand'),
        actions: pick('.page-404__actions'),
        button: pick('.page-404__home-link'),
        visual: pick('.page-404__visual'),
        visualImg: pick('.page-404__visual-img'),
        overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
        robots: (document.querySelector('meta[name="robots"]') || {}).content || null,
        canonical: (document.querySelector('link[rel="canonical"]') || {}).href || null,
      };
    });
    matrix.push({
      viewport: `${vp.w}x${vp.h}`,
      http: resp.status(),
      ...metrics,
    });
    await page.screenshot({
      path: path.join(outDir, `404-before-${vp.w}.png`),
      fullPage: true,
    });
    console.log('BEFORE', vp.w, resp.status(), metrics.title && metrics.title.fontSize, metrics.lead && metrics.lead.fontSize);
  }

  fs.writeFileSync(path.join(evidence, '404-before-computed.json'), JSON.stringify(matrix, null, 2), 'utf8');
  await browser.close();
  console.log('DONE');
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
