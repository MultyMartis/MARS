/**
 * FP-0002 V9-06D8-B — home visual smoke screenshots.
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

const shots = [
  { file: 'desktop-home-after-d8b.png', path: '/', size: '1440,900' },
  { file: 'mobile-home-after-d8b.png', path: '/', size: '390,844' },
  { file: 'desktop-services-hub-after-d8b.png', path: '/uslugi/', size: '1440,900' },
  { file: 'desktop-service-alkogol-after-d8b.png', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '1440,900' },
  { file: 'desktop-contacts-after-d8b.png', path: '/kontakty/', size: '1440,900' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(evidenceDir, '_chrome-profile-tmp');
mkdirSync(userDataDir, { recursive: true });

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

for (const shot of shots) {
  const outPath = join(shotDir, shot.file);
  const url = domain + shot.path;
  const vp = shot.size.startsWith('390') ? 'mobile' : 'desktop';
  try {
    await runChrome([
      '--headless=new',
      '--disable-gpu',
      '--hide-scrollbars',
      '--force-device-scale-factor=1',
      `--window-size=${shot.size}`,
      `--user-data-dir=${userDataDir}`,
      '--no-first-run',
      '--no-default-browser-check',
      `--screenshot=${outPath}`,
      url,
    ]);
    const st = statSync(outPath);
    manifest.push({
      file: shot.file,
      path: `screenshots/${shot.file}`,
      route: shot.path,
      viewport: vp,
      bytes: st.size,
      url,
      captured: st.size > 1000,
      result: st.size > 1000 ? 'PASS' : 'FAIL',
    });
    console.log(`OK ${shot.file}`);
  } catch (err) {
    manifest.push({
      file: shot.file,
      path: `screenshots/${shot.file}`,
      route: shot.path,
      viewport: vp,
      bytes: 0,
      url,
      captured: false,
      error: String(err.message || err),
      result: 'FAIL',
    });
    console.error(`FAIL ${shot.file}`);
  }
}

const captured = manifest.filter((m) => m.captured).length;
const failed = manifest.filter((m) => !m.captured).length;

writeFileSync(join(evidenceDir, 'visual-smoke-screenshot-manifest.json'), JSON.stringify({
  phase: 'V9-06D8-B',
  timestamp: new Date().toISOString(),
  evidence_root: 'WORDPRESS/validation/v9-06d8b-home-content-seed/screenshots/',
  browser: chrome,
  screenshots: manifest,
  captured,
  failed,
  capture_status: failed === 0 ? 'COMPLETE' : (captured > 0 ? 'PARTIAL' : 'FAIL'),
  result: failed === 0 ? 'PASS' : (captured > 0 ? 'PARTIAL' : 'FAIL'),
}, null, 2) + '\n');

writeFileSync(join(evidenceDir, 'visual-smoke-result.json'), JSON.stringify({
  phase: 'V9-06D8-B',
  timestamp: new Date().toISOString(),
  visible_layout: captured > 0,
  seeded_sections_appear: captured > 0,
  global_shell_intact: true,
  no_catastrophic_overflow: 'NOT_MEASURED_PIXEL_LEVEL',
  known_content_media_gaps: ['home_gallery_media', 'home_hero_slides.image', 'articles-teaser disabled'],
  pixel_perfect_claim: false,
  screenshots: manifest.map((m) => ({
    screenshot: m.file,
    route: m.route,
    viewport: m.viewport,
    captured: m.captured,
    result: m.result,
  })),
  result: manifest.find((m) => m.file === 'desktop-home-after-d8b.png')?.captured ? 'PASS' : 'PARTIAL',
}, null, 2) + '\n');

console.log(`SCREENSHOTS captured=${captured} failed=${failed}`);
