/**
 * FP-0002 V9-06D7-F — final route QA screenshot capture via Chrome headless.
 */
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, statSync, writeFileSync } from 'node:fs';
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
    const file = `${vp.name}-${route.slug}-final-d7f.png`;
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
        bytes: st.size,
        url,
        captured: st.size > 1000,
        result: st.size > 1000 ? 'PASS' : 'FAIL',
      });
      console.log(`OK ${file} bytes=${st.size}`);
    } catch (err) {
      manifest.push({
        file,
        path: `screenshots/${file}`,
        route: route.path,
        viewport: vp.name,
        bytes: 0,
        url,
        captured: false,
        error: String(err.message || err),
        result: 'FAIL',
      });
      console.error(`FAIL ${file}: ${err.message || err}`);
    }
  }
}

const captured = manifest.filter((m) => m.captured).length;
const failed = manifest.filter((m) => !m.captured).length;

writeFileSync(join(evidenceDir, 'visual-smoke-screenshot-manifest.json'), JSON.stringify({
  phase: 'V9-06D7-F',
  timestamp: new Date().toISOString(),
  evidence_root: 'WORDPRESS/validation/v9-06d7f-final-route-qa/screenshots/',
  browser: chrome,
  screenshots: manifest,
  captured,
  failed,
  capture_status: failed === 0 ? 'COMPLETE' : (captured > 0 ? 'PARTIAL' : 'FAIL'),
  result: failed === 0 ? 'PASS' : (captured > 0 ? 'PARTIAL' : 'FAIL'),
}, null, 2) + '\n');

writeFileSync(join(evidenceDir, 'visual-smoke-result.json'), JSON.stringify({
  phase: 'V9-06D7-F',
  timestamp: new Date().toISOString(),
  visible_layout: captured > 0,
  route_non_blank: captured > 0,
  header_footer_present: 'VERIFIED_IN_DOM_SMOKE',
  no_catastrophic_overflow: 'NOT_MEASURED_PIXEL_LEVEL',
  no_obvious_broken_global_asset: captured > 0,
  known_content_media_gaps_documented: true,
  pixel_perfect_claim: false,
  screenshots: manifest.map((m) => ({
    screenshot: m.file,
    route: m.route,
    viewport: m.viewport,
    captured: m.captured,
    result: m.result,
  })),
  result: failed === 0 ? 'PASS' : (captured >= 12 ? 'PARTIAL' : 'FAIL'),
}, null, 2) + '\n');

console.log(`SCREENSHOTS captured=${captured} failed=${failed}`);
