/**
 * FP-0002 V9-06D.5 — read-only screenshot capture via Chrome headless.
 * Writes PNGs under validation/v9-06d5-visual-route-qa/screenshots/ only.
 */
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, statSync, writeFileSync, readFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = __dirname;
const shotDir = join(evidenceDir, 'screenshots');
const domain = 'http://shpigovsky.test';

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];

const chrome = chromeCandidates.find((p) => existsSync(p));
if (!chrome) {
  console.error('NO_BROWSER');
  process.exit(2);
}

const routes = [
  { slug: 'home', path: '/' },
  { slug: 'services-hub', path: '/uslugi/' },
  { slug: 'service-zavisimosti', path: '/uslugi/zavisimosti/' },
  { slug: 'service-alkogol', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/' },
  { slug: 'service-psych', path: '/uslugi/psihicheskoe-zdorovie/' },
  { slug: 'service-rpp', path: '/uslugi/rasstroystva-pischevogo-povedeniya/' },
  { slug: 'contacts', path: '/kontakty/' },
];

const viewports = [
  { name: 'desktop', size: '1440,900' },
  { name: 'mobile', size: '390,844' },
];

mkdirSync(shotDir, { recursive: true });

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

const manifest = [];
const userDataDir = join(evidenceDir, '_chrome-profile-tmp');
mkdirSync(userDataDir, { recursive: true });

for (const vp of viewports) {
  for (const route of routes) {
    const file = `${vp.name}-${route.slug}.png`;
    const outPath = join(shotDir, file);
    const url = domain + route.path;
    const args = [
      '--headless=new',
      '--disable-gpu',
      '--hide-scrollbars',
      '--force-device-scale-factor=1',
      `--window-size=${vp.size}`,
      `--user-data-dir=${userDataDir}`,
      '--no-first-run',
      '--no-default-browser-check',
      `--screenshot=${outPath}`,
      url,
    ];
    try {
      await runChrome(args);
      const st = statSync(outPath);
      manifest.push({
        file,
        path: `screenshots/${file}`,
        route: route.path,
        viewport: vp.name,
        viewport_size: vp.size.replace(',', 'x'),
        bytes: st.size,
        url,
        result: st.size > 1000 ? 'CAPTURED' : 'TOO_SMALL',
      });
      console.log(`OK ${file} bytes=${st.size}`);
    } catch (err) {
      manifest.push({
        file,
        path: `screenshots/${file}`,
        route: route.path,
        viewport: vp.name,
        viewport_size: vp.size.replace(',', 'x'),
        bytes: 0,
        url,
        error: String(err.message || err),
        result: 'FAIL',
      });
      console.error(`FAIL ${file}: ${err.message || err}`);
    }
  }
}

const captured = manifest.filter((m) => m.result === 'CAPTURED').length;
const failed = manifest.filter((m) => m.result !== 'CAPTURED').length;

const screenshotManifest = {
  phase: 'V9-06D.5',
  timestamp: new Date().toISOString(),
  evidence_root: 'WORDPRESS/validation/v9-06d5-visual-route-qa/screenshots/',
  browser: chrome,
  screenshots: manifest,
  captured,
  failed,
  capture_status: failed === 0 ? 'COMPLETE' : (captured > 0 ? 'PARTIAL' : 'FAIL'),
  result: failed === 0 ? 'PASS' : (captured > 0 ? 'PARTIAL' : 'FAIL'),
};

writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify(screenshotManifest, null, 4) + '\n');

// Patch smoke JSON files
function patchSmoke(file, viewportLabel) {
  const p = join(evidenceDir, file);
  const data = JSON.parse(readFileSync(p, 'utf8'));
  data.screenshot_capture = screenshotManifest.capture_status;
  data.timestamp = screenshotManifest.timestamp;
  for (const route of data.routes) {
    const shot = manifest.find((m) => m.path === route.screenshot);
    route.screenshot_bytes = shot ? shot.bytes : 0;
    route.screenshot_result = shot ? shot.result : 'MISSING';
    if (viewportLabel === 'mobile') {
      route.no_obvious_horizontal_overflow = shot && shot.result === 'CAPTURED' ? 'NOT_MEASURED_PIXEL_LEVEL_ASSUMED_OK_FROM_DOM' : null;
    }
    if (shot && shot.result === 'CAPTURED' && route.result === 'PASS') {
      route.result = 'PASS';
    } else if (shot && shot.result !== 'CAPTURED' && route.result === 'PASS') {
      route.result = 'PASS_DOM_EVIDENCE_SCREENSHOT_FAIL';
      route.dom_evidence_only = true;
    }
  }
  data.result = failed === 0 ? 'PASS' : (captured > 0 ? 'PARTIAL' : 'FAIL');
  writeFileSync(p, JSON.stringify(data, null, 4) + '\n');
}

patchSmoke('route-visual-smoke-desktop.json', 'desktop');
patchSmoke('route-visual-smoke-mobile.json', 'mobile');

console.log(`SCREENSHOTS captured=${captured} failed=${failed}`);
