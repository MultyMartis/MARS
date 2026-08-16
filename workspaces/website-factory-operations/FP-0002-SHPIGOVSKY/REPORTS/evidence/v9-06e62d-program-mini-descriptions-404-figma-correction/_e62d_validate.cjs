const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const evidence = String.raw`X:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\REPORTS\evidence\v9-06e62d-program-mini-descriptions-404-figma-correction`;
const afterDir = path.join(evidence, 'after');
const homeDir = path.join(evidence, 'home');
fs.mkdirSync(afterDir, { recursive: true });
fs.mkdirSync(homeDir, { recursive: true });

const routes = [
  '/',
  '/uslugi/',
  '/uslugi/zavisimosti/lechenie-alkogolnoj-zavisimosti/',
  '/o-centre/',
  '/kontakty/',
  '/blog/',
  '/otzyvy/',
  '/o-centre/programma-lecheniya/genotipirovanie/',
  '/o-centre/programma-lecheniya/neyropsihologicheskaya-korrektsiya/',
  '/o-centre/programma-lecheniya/psihokorrektsiya/',
  '/o-centre/programma-lecheniya/kinezioterapiya/',
  '/this-page-definitely-does-not-exist-e62d/',
  '/uslugi/zavisimosti/this-service-does-not-exist-e62d/',
  '/blog/this-blog-post-does-not-exist-e62d/',
];

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  const jsErrors = [];
  page.on('pageerror', (e) => jsErrors.push(String(e)));

  const regression = [];
  for (const route of routes) {
    const resp = await page.goto('http://shpigovsky.test' + route, { waitUntil: 'networkidle2', timeout: 60000 });
    const phpWarn = await page.evaluate(() => /Warning:|Notice:|Fatal error:/i.test(document.body ? document.body.innerText : ''));
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1);
    const robots = await page.evaluate(() => (document.querySelector('meta[name="robots"]') || {}).content || '');
    const canonical = await page.evaluate(() => (document.querySelector('link[rel="canonical"]') || {}).href || '');
    regression.push({
      route,
      http: resp.status(),
      phpWarn,
      overflow,
      robots,
      canonical,
    });
    console.log('ROUTE', route, resp.status(), 'warn', phpWarn, 'ovf', overflow);
  }

  const metrics = [];
  for (const vp of [
    { w: 1440, h: 900 },
    { w: 1024, h: 768 },
    { w: 480, h: 900 },
    { w: 370, h: 812 },
  ]) {
    await page.setViewport({ width: vp.w, height: vp.h, deviceScaleFactor: 1 });
    await page.goto('http://shpigovsky.test/this-page-definitely-does-not-exist-e62d/', { waitUntil: 'networkidle2', timeout: 60000 });
    const m = await page.evaluate(() => {
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
        };
      };
      return {
        title: pick('.page-404__title'),
        lead: pick('.page-404__lead'),
        logo: pick('.page-404__logo'),
        brand: pick('.page-404__brand'),
        button: pick('.page-404__home-link'),
        visual: pick('.page-404__visual'),
        contentPad: getComputedStyle(document.querySelector('.page-404__content')).padding,
        bg: getComputedStyle(document.querySelector('.page-404')).backgroundColor,
      };
    });
    metrics.push({ viewport: `${vp.w}x${vp.h}`, ...m });
    await page.screenshot({ path: path.join(afterDir, `404-after-${vp.w}.png`), fullPage: true });

    await page.goto('http://shpigovsky.test/', { waitUntil: 'networkidle2', timeout: 60000 });
    await page.screenshot({ path: path.join(homeDir, `home-rehab-${vp.w}.png`), fullPage: false });
    console.log('SHOT', vp.w);
  }

  fs.writeFileSync(path.join(evidence, '404-after-computed.json'), JSON.stringify(metrics, null, 2));
  fs.writeFileSync(path.join(evidence, 'regression-matrix.json'), JSON.stringify({ jsErrors, regression }, null, 2));
  console.log('JS_ERRORS', jsErrors.length);
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
