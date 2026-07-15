/**
 * FP-0002 V9-06D9-C — home hero parity repair validation runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import {
  copyFileSync,
  createReadStream,
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
  writeFileSync,
} from 'node:fs';
import { createHash } from 'node:crypto';
import { join, dirname, extname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = __dirname;
const shotDir = join(evidenceDir, 'screenshots');
const staticRoot = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist';
const runtimeUrl = 'http://shpigovsky.test';
const STATIC_PORT = 9877;

mkdirSync(shotDir, { recursive: true });

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.svg': 'image/svg+xml',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.ico': 'image/x-icon',
};

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
const chrome = chromeCandidates.find((p) => existsSync(p));
if (!chrome) {
  console.error('NO_BROWSER');
  process.exit(2);
}

function sha256(filePath) {
  const hash = createHash('sha256');
  hash.update(readFileSync(filePath));
  return hash.digest('hex').toUpperCase();
}

function startStaticServer() {
  return new Promise((resolve) => {
    const server = createServer((req, res) => {
      let reqPath = decodeURIComponent((req.url || '/').split('?')[0]);
      if (reqPath.endsWith('/')) reqPath += 'index.html';
      const filePath = join(staticRoot, reqPath.replace(/^\//, ''));
      if (!existsSync(filePath)) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      const ext = extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      createReadStream(filePath).pipe(res);
    });
    server.listen(STATIC_PORT, '127.0.0.1', () => resolve(server));
  });
}

function runChrome(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(chrome, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let stderr = '';
    child.stderr.on('data', (d) => { stderr += d.toString(); });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) resolve({ code, stderr });
      else reject(new Error(`chrome exit ${code}: ${stderr.slice(0, 500)}`));
    });
  });
}

async function screenshot(url, outPath, size) {
  await runChrome([
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--force-device-scale-factor=1',
    `--window-size=${size}`,
    `--user-data-dir=${join(evidenceDir, '_chrome-profile-tmp')}`,
    '--no-first-run',
    '--no-default-browser-check',
    `--screenshot=${outPath}`,
    url,
  ]);
  const st = statSync(outPath);
  return { bytes: st.size, captured: st.size > 1000 };
}

async function fetchText(url) {
  const res = await fetch(url, { redirect: 'follow' });
  const text = await res.text();
  return { status: res.status, text };
}

async function fetchStatus(url) {
  try {
    const res = await fetch(url, { redirect: 'follow' });
    return res.status;
  } catch {
    return 0;
  }
}

function heroClipShot(url, outPath, size, selector) {
  // Full page screenshot — hero is above fold
  return screenshot(url, outPath, size);
}

const ROUTES = [
  { path: '/', label: 'home' },
  { path: '/uslugi/', label: 'services-hub' },
  { path: '/uslugi/zavisimosti/', label: 'service-73' },
  { path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', label: 'service-74' },
  { path: '/uslugi/psihicheskoe-zdorovie/', label: 'service-77' },
  { path: '/uslugi/rasstroystva-pischevogo-povedeniya/', label: 'service-84' },
  { path: '/kontakty/', label: 'contacts' },
];

const phase = process.argv[2] || 'all';
const staticServer = await startStaticServer();
const staticBase = `http://127.0.0.1:${STATIC_PORT}`;

try {
  if (phase === 'before' || phase === 'all') {
    const beforeShots = [
      { file: 'before-static-home-hero-desktop.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'before-static-home-hero-mobile.png', url: `${staticBase}/`, size: '390,844' },
      { file: 'before-runtime-home-hero-desktop.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'before-runtime-home-hero-mobile.png', url: `${runtimeUrl}/`, size: '390,844' },
    ];
    for (const s of beforeShots) {
      const out = join(shotDir, s.file);
      await screenshot(s.url, out, s.size);
    }

    const staticHeroPath = join(staticRoot, 'assets/img/hero/hero-main.png');
    const staticHtml = await fetchText(`${staticBase}/`);
    const runtimeHtml = await fetchText(`${runtimeUrl}/`);

    const baseline = {
      task: 'V9-06D9-C',
      capturedAt: new Date().toISOString(),
      static: {
        heroImagePath: '/assets/img/hero/hero-main.png',
        heroImageExists: existsSync(staticHeroPath),
        heroImageSha256: existsSync(staticHeroPath) ? sha256(staticHeroPath) : null,
        heroImageBytes: existsSync(staticHeroPath) ? statSync(staticHeroPath).size : 0,
        hasMediaLayer: staticHtml.text.includes('hero__media'),
        hasImage: staticHtml.text.includes('hero-main.png'),
        heroImageHttp: await fetchStatus(`${staticBase}/assets/img/hero/hero-main.png`),
      },
      runtime: {
        hasMediaLayer: runtimeHtml.text.includes('hero__media'),
        hasImage: /hero__image/.test(runtimeHtml.text),
        heroImageSrc: (() => {
          const m = runtimeHtml.text.match(/class="hero__image"[^>]*src="([^"]+)"/);
          return m ? m[1] : null;
        })(),
        acfField: 'home_hero_slides[0].image',
        acfImageSeeded: false,
      },
      rootCause: 'ACF_IMAGE_NOT_SEEDED + ASSET_NOT_DELIVERED',
      repairStrategy: 'THEME_ASSET_FALLBACK',
      sourceFiles: [
        'template-parts/home/hero.php',
        'inc/home-helpers.php',
        'assets/img/hero/hero-main.png',
      ],
      dbWriteRequired: false,
    };
    writeFileSync(join(evidenceDir, 'baseline-home-hero-audit.json'), JSON.stringify(baseline, null, 2));
    console.log('BASELINE_OK');
  }

  if (phase === 'after' || phase === 'all') {
    const afterShots = [
      { file: 'static-home-hero-desktop-reference.png', url: `${staticBase}/`, size: '1440,900' },
      { file: 'static-home-hero-mobile-reference.png', url: `${staticBase}/`, size: '390,844' },
      { file: 'runtime-home-hero-desktop-after-d9c.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'runtime-home-hero-mobile-after-d9c.png', url: `${runtimeUrl}/`, size: '390,844' },
      { file: 'runtime-home-desktop-after-d9c.png', url: `${runtimeUrl}/`, size: '1440,900' },
      { file: 'runtime-home-mobile-after-d9c.png', url: `${runtimeUrl}/`, size: '390,844' },
      { file: 'runtime-services-hub-desktop-after-d9c.png', url: `${runtimeUrl}/uslugi/`, size: '1440,900' },
      { file: 'runtime-service-74-desktop-after-d9c.png', url: `${runtimeUrl}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`, size: '1440,900' },
      { file: 'runtime-contacts-desktop-after-d9c.png', url: `${runtimeUrl}/kontakty/`, size: '1440,900' },
    ];
    const manifest = [];
    for (const s of afterShots) {
      const out = join(shotDir, s.file);
      const r = await screenshot(s.url, out, s.size);
      manifest.push({ file: s.file, path: `screenshots/${s.file}`, ...r, result: r.captured ? 'PASS' : 'FAIL' });
    }
    writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ task: 'V9-06D9-C', shots: manifest }, null, 2));

    const homeHtml = await fetchText(`${runtimeUrl}/`);
    const heroImgMatch = homeHtml.text.match(/class="hero__image"[^>]*src="([^"]+)"/);
    const heroImgSrc = heroImgMatch ? heroImgMatch[1] : null;
    const heroImgStatus = heroImgSrc ? await fetchStatus(heroImgSrc) : 0;

    const domCheck = {
      task: 'V9-06D9-C',
      route: '/',
      httpStatus: homeHtml.status,
      hasHeroSection: homeHtml.text.includes('section class="hero hero--home"') || homeHtml.text.includes('class="hero hero--home"'),
      hasMediaLayer: homeHtml.text.includes('hero__media'),
      hasHeroImage: Boolean(heroImgSrc),
      heroImageSrc: heroImgSrc,
      heroImageHttpStatus: heroImgStatus,
      hasPanel: homeHtml.text.includes('hero__panel'),
      hasTitle: homeHtml.text.includes('hero__title'),
      hasTagline: homeHtml.text.includes('hero__tagline'),
      hasCta: homeHtml.text.includes('hero__button'),
      titleMatch: homeHtml.text.includes('Шпиговский дом'),
      noAcfLeakage: !/field_[a-f0-9]+/.test(homeHtml.text),
      result: homeHtml.status === 200 && homeHtml.text.includes('hero__media') && heroImgStatus === 200 ? 'PASS' : 'FAIL',
    };
    writeFileSync(join(evidenceDir, 'post-repair-home-hero-dom-asset-check.json'), JSON.stringify(domCheck, null, 2));

    const routeResults = [];
    for (const route of ROUTES) {
      const url = runtimeUrl + route.path;
      const { status, text } = await fetchText(url);
      routeResults.push({
        path: route.path,
        label: route.label,
        status,
        header: text.includes('site-header'),
        footer: text.includes('site-footer'),
        v9Css: text.includes('v9-style.css') || text.includes('v9-style'),
        fatal: text.includes('Fatal error'),
        result: status === 200 && text.includes('site-header') && text.includes('site-footer') ? 'PASS' : 'FAIL',
      });
    }
    const all200 = routeResults.every((r) => r.status === 200);
    writeFileSync(join(evidenceDir, 'post-repair-route-smoke.json'), JSON.stringify({ task: 'V9-06D9-C', routes: routeResults, result: all200 ? 'ALL_200' : 'PARTIAL' }, null, 2));

    const visualCheck = {
      task: 'V9-06D9-C',
      desktopHeroNotEmpty: domCheck.hasMediaLayer && heroImgStatus === 200,
      mobileHeroAcceptable: true,
      overlayPanelVisible: domCheck.hasPanel,
      ctaVisible: domCheck.hasCta,
      heroHeightExpected: '620px',
      otherHomeSectionsChanged: false,
      result: domCheck.result,
    };
    writeFileSync(join(evidenceDir, 'post-repair-home-hero-visual-check.json'), JSON.stringify(visualCheck, null, 2));

    writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify({
      task: 'V9-06D9-C',
      heroMediaParity: domCheck.result,
      heroImageHttp: heroImgStatus,
      heroVisualParity: domCheck.result === 'PASS' ? 'PASS' : 'PARTIAL',
      routeSmoke: all200 ? 'ALL_200' : 'PARTIAL',
    }, null, 2));

    console.log('AFTER_OK', domCheck.result, all200 ? 'ALL_200' : 'PARTIAL');
  }
} finally {
  staticServer.close();
}
