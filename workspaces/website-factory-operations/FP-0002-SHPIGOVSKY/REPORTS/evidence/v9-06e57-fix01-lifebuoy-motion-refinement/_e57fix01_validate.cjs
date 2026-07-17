/**
 * V9-06E57-FIX01 lifebuoy motion refinement validation + screenshots
 */
const puppeteer = require('X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/node_modules/puppeteer');
const fs = require('fs');
const path = require('path');

const outDir = process.argv[2] || __dirname;
const shots = path.join(outDir, 'screenshots');
fs.mkdirSync(shots, { recursive: true });

const viewports = [
  { name: '1440x900', w: 1440, h: 900 },
  { name: '1280x800', w: 1280, h: 800 },
  { name: '1024x768', w: 1024, h: 768 },
  { name: '768x1024', w: 768, h: 1024 },
  { name: '390x844', w: 390, h: 844 },
  { name: '375x812', w: 375, h: 812 },
  { name: '320x568', w: 320, h: 568 },
];

const routes = {
  home: 'http://shpigovsky.test/',
  uslugi: 'http://shpigovsky.test/uslugi/',
  section: 'http://shpigovsky.test/uslugi/zavisimosti/',
  service: 'http://shpigovsky.test/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/',
  blog: 'http://shpigovsky.test/blog/',
  kontakty: 'http://shpigovsky.test/kontakty/',
  ocentre: 'http://shpigovsky.test/o-centre/',
};

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function measure(page) {
  return page.evaluate(() => {
    const el = document.querySelector('[data-fp02-lifebuoy-parallax]');
    const img = el && el.querySelector('.fp02-lifebuoy-parallax__img');
    const doc = document.documentElement;
    const scrollable = Math.max(0, doc.scrollHeight - window.innerHeight);
    const progress = scrollable > 0 ? window.scrollY / scrollable : 0;
    const cs = img ? getComputedStyle(img) : null;
    const rectRaw = img ? img.getBoundingClientRect() : null;
    const rect = rectRaw
      ? {
          x: rectRaw.x,
          y: rectRaw.y,
          width: rectRaw.width,
          height: rectRaw.height,
          top: rectRaw.top,
          left: rectRaw.left,
          right: rectRaw.right,
          bottom: rectRaw.bottom,
        }
      : null;

    let visibleWidthPct = null;
    if (rect) {
      const visibleLeft = Math.max(0, rect.left);
      const visibleRight = Math.min(window.innerWidth, rect.right);
      const visibleW = Math.max(0, visibleRight - visibleLeft);
      visibleWidthPct = rect.width > 0 ? (visibleW / rect.width) * 100 : 0;
    }

    const vars = el
      ? {
          x: el.style.getPropertyValue('--fp02-lb-x').trim(),
          y: el.style.getPropertyValue('--fp02-lb-y').trim(),
          scale: el.style.getPropertyValue('--fp02-lb-scale').trim(),
          rotate: el.style.getPropertyValue('--fp02-lb-rotate').trim(),
        }
      : null;

    return {
      present: !!el,
      count: document.querySelectorAll('[data-fp02-lifebuoy-parallax]').length,
      mode: el ? el.getAttribute('data-fp02-lb-mode') : null,
      attrProgress: el ? el.getAttribute('data-fp02-lb-progress') : null,
      scrollY: window.scrollY,
      scrollable,
      progress,
      opacity: cs ? cs.opacity : null,
      pointerEvents: el ? getComputedStyle(el).pointerEvents : null,
      zIndex: el ? getComputedStyle(el).zIndex : null,
      transform: cs ? cs.transform : null,
      vars,
      visibleWidthPct,
      rect,
      bodyOverflow: getComputedStyle(document.body).overflowX,
      htmlOverflow: getComputedStyle(doc).overflowX,
      docWidth: doc.scrollWidth,
      winWidth: window.innerWidth,
      hasOverflowX: doc.scrollWidth > window.innerWidth + 1,
    };
  });
}

async function setScrollProgress(page, p) {
  await page.evaluate((progress) => {
    const html = document.documentElement;
    html.style.scrollBehavior = 'auto';
    document.body.style.scrollBehavior = 'auto';
    const max = Math.max(0, html.scrollHeight - window.innerHeight);
    window.scrollTo(0, Math.round(max * progress));
  }, p);
  await sleep(80);
  await page.evaluate(() => new Promise((r) => requestAnimationFrame(() => requestAnimationFrame(r))));
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  const matrix = [];
  const regressions = [];
  const consoleErrors = [];

  page.on('console', (msg) => {
    if (msg.type() === 'error') consoleErrors.push({ text: msg.text(), url: page.url() });
  });
  page.on('pageerror', (err) => consoleErrors.push({ text: String(err), url: page.url() }));

  // Long page detailed scroll states @ 1440
  {
    const vp = viewports[0];
    await page.setViewport({ width: vp.w, height: vp.h });
    await page.goto(routes.home, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(300);
    const states = [
      { key: 'top', p: 0 },
      { key: 'p25', p: 0.25 },
      { key: 'p50', p: 0.5 },
      { key: 'p75', p: 0.75 },
      { key: 'bottom', p: 0.98 },
    ];
    for (const st of states) {
      await setScrollProgress(page, st.p);
      const m = await measure(page);
      matrix.push({ route: 'home', viewport: vp.name, state: st.key, ...m });
      await page.screenshot({
        path: path.join(shots, `long-home-${vp.name}-${st.key}.png`),
        fullPage: false,
      });
    }
    for (const st of [
      { key: 'reverse-p75', p: 0.75 },
      { key: 'reverse-p50', p: 0.5 },
      { key: 'reverse-p25', p: 0.25 },
      { key: 'reverse-top', p: 0 },
    ]) {
      await setScrollProgress(page, st.p);
      const m = await measure(page);
      matrix.push({ route: 'home', viewport: vp.name, state: st.key, ...m });
      await page.screenshot({
        path: path.join(shots, `long-home-${vp.name}-${st.key}.png`),
        fullPage: false,
      });
    }

    const reg = await page.evaluate(() => ({
      hero: !!document.querySelector('.hero--home, .hero'),
      floatingHeader: !!document.querySelector('.fp02-floating-header'),
      offcanvasTrigger: !!document.querySelector(
        '[data-menu-open], .site-header__menu-btn, .burger, [data-offcanvas-open]'
      ),
      form: !!document.querySelector('[data-lead-form]'),
      gallery: !!document.querySelector('.gallery, [data-gallery], .home-gallery, .swiper'),
      video: !!document.querySelector('video'),
      lifebuoy: document.querySelectorAll('[data-fp02-lifebuoy-parallax]').length === 1,
    }));
    regressions.push({ route: 'home', ...reg });
  }

  // Short page kontakty
  {
    const vp = viewports[0];
    await page.setViewport({ width: vp.w, height: vp.h });
    await page.goto(routes.kontakty, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(300);
    for (const st of [
      { key: 'top', p: 0 },
      { key: 'mid', p: 0.5 },
      { key: 'bottom', p: 1 },
    ]) {
      await setScrollProgress(page, st.p);
      const m = await measure(page);
      matrix.push({ route: 'kontakty', viewport: vp.name, state: st.key, ...m });
      await page.screenshot({
        path: path.join(shots, `short-kontakty-${vp.name}-${st.key}.png`),
        fullPage: false,
      });
    }
  }

  // Blog as secondary short/generic
  {
    const vp = viewports[0];
    await page.setViewport({ width: vp.w, height: vp.h });
    await page.goto(routes.blog, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(200);
    for (const st of [
      { key: 'top', p: 0 },
      { key: 'mid', p: 0.5 },
      { key: 'bottom', p: 1 },
    ]) {
      await setScrollProgress(page, st.p);
      const m = await measure(page);
      matrix.push({ route: 'blog', viewport: vp.name, state: st.key, ...m });
      await page.screenshot({
        path: path.join(shots, `short-blog-${vp.name}-${st.key}.png`),
        fullPage: false,
      });
    }
  }

  // Viewport matrix (home top + mid; kontakty top)
  for (const vp of viewports) {
    await page.setViewport({ width: vp.w, height: vp.h });
    await page.goto(routes.home, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(200);
    await setScrollProgress(page, 0);
    let m = await measure(page);
    matrix.push({ route: 'home', viewport: vp.name, state: 'vp-top', ...m });
    await page.screenshot({ path: path.join(shots, `vp-home-${vp.name}-top.png`), fullPage: false });
    await setScrollProgress(page, 0.5);
    m = await measure(page);
    matrix.push({ route: 'home', viewport: vp.name, state: 'vp-mid', ...m });
    await page.screenshot({ path: path.join(shots, `vp-home-${vp.name}-mid.png`), fullPage: false });

    await page.goto(routes.kontakty, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(150);
    await setScrollProgress(page, 0.5);
    m = await measure(page);
    matrix.push({ route: 'kontakty', viewport: vp.name, state: 'vp-mid', ...m });
    await page.screenshot({
      path: path.join(shots, `vp-kontakty-${vp.name}-mid.png`),
      fullPage: false,
    });
  }

  // Route smoke long/short
  for (const [name, url] of Object.entries(routes)) {
    await page.setViewport({ width: 1440, height: 900 });
    const resp = await page.goto(url, { waitUntil: 'networkidle2', timeout: 60000 });
    await sleep(200);
    await setScrollProgress(page, 0);
    const top = await measure(page);
    await setScrollProgress(page, 0.5);
    const mid = await measure(page);
    await setScrollProgress(page, 0.95);
    const bot = await measure(page);
    matrix.push({
      route: name,
      viewport: '1440x900',
      state: 'route-top',
      http: resp && resp.status(),
      ...top,
    });
    matrix.push({ route: name, viewport: '1440x900', state: 'route-mid', ...mid });
    matrix.push({ route: name, viewport: '1440x900', state: 'route-bottom', ...bot });
    await page.screenshot({ path: path.join(shots, `route-${name}-mid.png`), fullPage: false });
  }

  // Reduced motion
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto(routes.home, { waitUntil: 'networkidle2', timeout: 60000 });
  await setScrollProgress(page, 0);
  const rm0 = await measure(page);
  await setScrollProgress(page, 1);
  const rm1 = await measure(page);
  matrix.push({ route: 'home', viewport: '1440x900', state: 'reduced-top', ...rm0 });
  matrix.push({ route: 'home', viewport: '1440x900', state: 'reduced-bottom', ...rm1 });
  await page.screenshot({ path: path.join(shots, `reduced-motion-home-top.png`), fullPage: false });
  await page.screenshot({
    path: path.join(shots, `reduced-motion-home-bottom.png`),
    fullPage: false,
  });

  // Performance note
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'no-preference' }]);
  await page.goto(routes.home, { waitUntil: 'networkidle2', timeout: 60000 });
  const perf = await page.evaluate(async () => {
    const start = performance.now();
    const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    for (let i = 0; i <= 20; i++) {
      window.scrollTo(0, Math.round((max * i) / 20));
      await new Promise((r) => requestAnimationFrame(r));
    }
    const elapsed = performance.now();
    return {
      elapsedMs: Math.round(elapsed - start),
      instances: document.querySelectorAll('[data-fp02-lifebuoy-parallax]').length,
    };
  });

  fs.writeFileSync(path.join(outDir, 'scroll-matrix.json'), JSON.stringify(matrix, null, 2));
  fs.writeFileSync(path.join(outDir, 'regression-probes.json'), JSON.stringify(regressions, null, 2));
  fs.writeFileSync(path.join(outDir, 'console-errors.json'), JSON.stringify(consoleErrors, null, 2));
  fs.writeFileSync(path.join(outDir, 'performance-notes.json'), JSON.stringify(perf, null, 2));

  const csvLines = [
    'route,viewport,state,present,count,mode,progress,attrProgress,scale,rotate,visibleWidthPct,scrollable,opacity,pointerEvents,hasOverflowX,docWidth,winWidth',
  ];
  for (const row of matrix) {
    csvLines.push(
      [
        row.route,
        row.viewport,
        row.state,
        row.present,
        row.count,
        row.mode,
        row.progress != null ? Number(row.progress).toFixed(4) : '',
        row.attrProgress || '',
        (row.vars && row.vars.scale) || '',
        (row.vars && row.vars.rotate) || '',
        row.visibleWidthPct != null ? Number(row.visibleWidthPct).toFixed(1) : '',
        row.scrollable,
        row.opacity,
        row.pointerEvents,
        row.hasOverflowX,
        row.docWidth,
        row.winWidth,
      ].join(',')
    );
  }
  fs.writeFileSync(path.join(outDir, 'validation-matrix.csv'), csvLines.join('\n'));

  // Motion model summary from home long scroll
  const homeStates = matrix.filter(
    (r) => r.route === 'home' && r.viewport === '1440x900' && ['top', 'p25', 'p50', 'p75', 'bottom'].includes(r.state)
  );
  fs.writeFileSync(
    path.join(outDir, 'motion-sample-home-1440.json'),
    JSON.stringify(homeStates, null, 2)
  );

  console.log(
    JSON.stringify(
      {
        matrixRows: matrix.length,
        consoleErrors: consoleErrors.length,
        perf,
        shots: fs.readdirSync(shots).length,
        homeMotion: homeStates.map((r) => ({
          state: r.state,
          mode: r.mode,
          scale: r.vars && r.vars.scale,
          rotate: r.vars && r.vars.rotate,
          visibleWidthPct: r.visibleWidthPct,
          x: r.vars && r.vars.x,
        })),
      },
      null,
      2
    )
  );

  await browser.close();
})().catch((err) => {
  console.error(err);
  process.exit(1);
});

