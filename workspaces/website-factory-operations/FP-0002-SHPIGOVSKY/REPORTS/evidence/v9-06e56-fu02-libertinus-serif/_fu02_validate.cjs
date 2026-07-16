const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

const outDir = process.argv[2] || __dirname;
const shots = path.join(outDir, 'screenshots');
fs.mkdirSync(shots, { recursive: true });

const viewports = [
  { w: 1440, h: 900 },
  { w: 1024, h: 768 },
  { w: 767, h: 1024 },
  { w: 390, h: 844 },
  { w: 375, h: 812 },
  { w: 320, h: 568 },
];

const routes = {
  home: 'http://shpigovsky.test/',
  uslugi: 'http://shpigovsky.test/uslugi/',
  section: 'http://shpigovsky.test/uslugi/zavisimosti/',
  service1: 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
  service2: 'http://shpigovsky.test/uslugi/psihicheskoe-zdorovie/depressiya/',
  generic: 'http://shpigovsky.test/o-centre/',
  ocentre: 'http://shpigovsky.test/o-centre/',
  kontakty: 'http://shpigovsky.test/kontakty/',
  blog: 'http://shpigovsky.test/blog/',
};

const typoRoutes = ['home', 'section', 'service1', 'uslugi'];

function familyStartsLibertinus(family) {
  if (!family) return false;
  const cleaned = family.replace(/^["']/, '');
  return cleaned.startsWith('Libertinus Serif');
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox'],
  });
  const page = await browser.newPage();
  const matrix = [];
  const fontNet = [];
  const regression = [];

  for (const name of typoRoutes) {
    const url = routes[name];
    const fontReqs = [];
    const consoleErrors = [];

    const onRes = async (res) => {
      const u = res.url();
      if (u.includes('libertinus')) {
        fontReqs.push({
          url: u,
          status: res.status(),
          contentType: res.headers()['content-type'] || '',
        });
      }
    };
    const onConsole = (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    };
    const onPageError = (err) => consoleErrors.push(String(err));

    page.on('response', onRes);
    page.on('console', onConsole);
    page.on('pageerror', onPageError);

    await page.goto(url, { waitUntil: 'networkidle2', timeout: 60000 });
    await page.evaluate(async () => {
      try {
        await document.fonts.ready;
      } catch (e) {}
    });

    for (const vp of viewports) {
      await page.setViewport({ width: vp.w, height: vp.h });
      await new Promise((r) => setTimeout(r, 350));
      const data = await page.evaluate(async () => {
        await document.fonts.ready;
        const measure = (sel) => {
          const el = document.querySelector(sel);
          if (!el) return null;
          const cs = getComputedStyle(el);
          const faces = [...document.fonts]
            .filter((f) => f.family.replace(/["']/g, '') === 'Libertinus Serif' && f.status === 'loaded')
            .map((f) => ({ family: f.family, weight: String(f.weight), style: f.style, status: f.status }));
          return {
            fontFamily: cs.fontFamily,
            fontSize: cs.fontSize,
            fontWeight: cs.fontWeight,
            lineHeight: cs.lineHeight,
            letterSpacing: cs.letterSpacing,
            textTransform: cs.textTransform,
            overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
            titleText: (el.textContent || '').trim().slice(0, 80),
            loadedLibertinus: faces,
          };
        };
        return {
          heroTitle: measure('.hero__title'),
          servicesTitle: measure('.services-inner-hero-v2__title'),
        };
      });

      const entries = [];
      if (data.heroTitle) entries.push({ selector: '.hero__title', m: data.heroTitle });
      if (data.servicesTitle) entries.push({ selector: '.services-inner-hero-v2__title', m: data.servicesTitle });
      if (!entries.length) {
        matrix.push({
          phase: 'after',
          route: name,
          url,
          viewport: `${vp.w}x${vp.h}`,
          selector: null,
          pass: 'N/A_NO_SELECTOR',
        });
      } else {
        for (const { selector, m } of entries) {
          const familyOk = familyStartsLibertinus(m.fontFamily);
          const pass = familyOk && m.fontWeight === '400' && !m.overflowX ? 'PASS' : 'FAIL';
          matrix.push({
            phase: 'after',
            route: name,
            url,
            viewport: `${vp.w}x${vp.h}`,
            selector,
            family: m.fontFamily,
            size: m.fontSize,
            weight: m.fontWeight,
            lineHeight: m.lineHeight,
            letterSpacing: m.letterSpacing,
            textTransform: m.textTransform,
            overflowX: m.overflowX,
            loaded: m.loadedLibertinus,
            pass,
            consoleErrors: [...consoleErrors],
          });
        }
      }

      if ([1440, 390, 320].includes(vp.w)) {
        await page.screenshot({
          path: path.join(shots, `${name}-${vp.w}x${vp.h}.png`),
          fullPage: false,
        });
      }
      consoleErrors.length = 0;
    }

    page.off('response', onRes);
    page.off('console', onConsole);
    page.off('pageerror', onPageError);
    fontNet.push({ route: name, url, requests: fontReqs });
  }

  for (const [name, url] of Object.entries(routes)) {
    const consoleErrors = [];
    page.removeAllListeners('console');
    page.removeAllListeners('pageerror');
    page.on('console', (msg) => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('pageerror', (err) => consoleErrors.push(String(err)));
    const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.setViewport({ width: 1440, height: 900 });
    await new Promise((r) => setTimeout(r, 250));
    const smoke = await page.evaluate(() => {
      const body = document.body ? document.body.innerText : '';
      const phpWarn = /Warning:|Fatal error:|Notice:|Parse error:/i.test(body);
      const floating = !!document.querySelector(
        '.fp02-floating-header, [data-fp02-floating-header], .fp02-fh, header.fp02-floating-header'
      );
      const form = !!document.querySelector('form');
      const homeHero = !!document.querySelector('.hero--home');
      const gallery = !!document.querySelector('[data-services-category-gallery], .home-gallery');
      return { phpWarn, floating, form, homeHero, gallery, title: document.title };
    });
    regression.push({
      route: name,
      url,
      http: resp.status(),
      phpWarn: smoke.phpWarn,
      jsErrors: consoleErrors.slice(0, 5),
      floating: smoke.floating,
      form: smoke.form,
      homeHero: smoke.homeHero,
      gallery: smoke.gallery,
      pass: resp.status() === 200 && !smoke.phpWarn ? 'PASS' : 'FAIL',
    });
  }

  await page.goto(routes.home, { waitUntil: 'networkidle2' });
  const fontFaceInfo = await page.evaluate(async () => {
    await document.fonts.ready;
    const all = [...document.fonts].map((f) => ({
      family: f.family,
      weight: String(f.weight),
      style: f.style,
      status: f.status,
    }));
    const lib = all.filter((f) => f.family.includes('Libertinus'));
    const el = document.querySelector('.hero__title');
    return {
      lib,
      used: el ? getComputedStyle(el).fontFamily : null,
      check: el ? document.fonts.check('400 70px "Libertinus Serif"') : null,
    };
  });

  // Direct font URL probe via page
  const fontUrl =
    'http://shpigovsky.test/wp-content/themes/shpigovsky/assets/fonts/libertinus-serif/libertinus-serif-regular.ttf';
  const fontProbe = await page.evaluate(async (u) => {
    const r = await fetch(u);
    const buf = await r.arrayBuffer();
    return {
      status: r.status,
      contentType: r.headers.get('content-type'),
      bytes: buf.byteLength,
      magic: String.fromCharCode(...new Uint8Array(buf.slice(0, 4))),
    };
  }, fontUrl);

  fs.writeFileSync(path.join(outDir, 'after-computed-styles.json'), JSON.stringify(matrix, null, 2));
  fs.writeFileSync(path.join(outDir, 'font-network.json'), JSON.stringify(fontNet, null, 2));
  fs.writeFileSync(path.join(outDir, 'regression.json'), JSON.stringify(regression, null, 2));
  fs.writeFileSync(path.join(outDir, 'font-face-runtime.json'), JSON.stringify(fontFaceInfo, null, 2));
  fs.writeFileSync(path.join(outDir, 'font-http-probe.json'), JSON.stringify(fontProbe, null, 2));

  console.log('matrix', matrix.length);
  console.log('PASS', matrix.filter((r) => r.pass === 'PASS').length);
  console.log('FAIL', matrix.filter((r) => r.pass === 'FAIL').length);
  console.log('NA', matrix.filter((r) => String(r.pass).startsWith('N/A')).length);
  console.log('regression PASS', regression.filter((r) => r.pass === 'PASS').length, '/', regression.length);
  console.log('fontFace', JSON.stringify(fontFaceInfo));
  console.log('fontProbe', JSON.stringify(fontProbe));
  console.log(
    'home1440',
    JSON.stringify(matrix.find((r) => r.route === 'home' && r.viewport === '1440x900' && r.selector === '.hero__title'))
  );
  console.log(
    'section1440',
    JSON.stringify(
      matrix.find((r) => r.route === 'section' && r.viewport === '1440x900' && r.selector === '.services-inner-hero-v2__title')
    )
  );
  console.log(
    'service11440',
    JSON.stringify(
      matrix.find((r) => r.route === 'service1' && r.viewport === '1440x900' && r.selector === '.services-inner-hero-v2__title')
    )
  );

  await browser.close();
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
