/**
 * FP-0002 V9-06E3 — screenshot capture helper. NOT FOR GIT.
 */
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, statSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const shotDir = join(__dirname, 'screenshots');
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
  { file: 'runtime-home-stable-e3.png', url: domain + '/', kind: 'frontend' },
  { file: 'runtime-services-stable-e3.png', url: domain + '/uslugi/', kind: 'frontend' },
  { file: 'runtime-service-74-stable-e3.png', url: domain + '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', kind: 'frontend' },
  { file: 'runtime-contacts-stable-e3.png', url: domain + '/kontakty/', kind: 'frontend' },
  { file: 'runtime-reviews-stable-e3.png', url: domain + '/otzyvy/', kind: 'frontend' },
  { file: 'runtime-privacy-policy-stable-e3.png', url: domain + '/privacy-policy/', kind: 'legal' },
  { file: 'runtime-user-agreement-stable-e3.png', url: domain + '/user-agreement/', kind: 'legal' },
  { file: 'runtime-consent-stable-e3.png', url: domain + '/consent-personal-data/', kind: 'legal' },
  { file: 'runtime-cookie-policy-stable-e3.png', url: domain + '/cookie-files-policy/', kind: 'legal' },
  { file: 'runtime-footer-legal-stable-e3.png', url: domain + '/privacy-policy/', kind: 'footer' },
  { file: 'runtime-main-menu-stable-e3.png', url: domain + '/', kind: 'menu' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(__dirname, '_chrome-profile-tmp-e3');
mkdirSync(userDataDir, { recursive: true });

function sha256(path) {
  return createHash('sha256').update(readFileSync(path)).digest('hex').toUpperCase();
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

const manifest = [];

for (const shot of shots) {
  const outPath = join(shotDir, shot.file);
  const args = [
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--force-device-scale-factor=1',
    '--window-size=1440,900',
    `--user-data-dir=${userDataDir}`,
    '--no-first-run',
    '--no-default-browser-check',
    `--screenshot=${outPath}`,
    shot.url,
  ];
  try {
    await runChrome(args);
    const st = statSync(outPath);
    const captured = st.size > 1000;
    manifest.push({
      file: shot.file,
      url: shot.url,
      kind: shot.kind,
      captured,
      bytes: st.size,
      sha256: captured ? sha256(outPath) : null,
      result: captured ? 'PASS' : 'FAIL',
    });
  } catch (err) {
    manifest.push({
      file: shot.file,
      url: shot.url,
      kind: shot.kind,
      captured: false,
      error: String(err.message || err),
      result: 'FAIL',
    });
  }
}

const adminShots = [
  { file: 'wp-admin-home-stable-e3.png', url: domain + '/wp-admin/post.php?post=4&action=edit', kind: 'admin' },
  { file: 'wp-admin-reviews-stable-e3.png', url: domain + '/wp-admin/admin.php?page=fp02-reviews', kind: 'admin' },
  { file: 'wp-admin-legal-editor-stable-e3.png', url: domain + '/wp-admin/post.php?post=22&action=edit', kind: 'admin' },
  { file: 'wp-admin-site-settings-stable-e3.png', url: domain + '/wp-admin/admin.php?page=fp02-site-settings', kind: 'admin' },
];

for (const shot of adminShots) {
  manifest.push({
    file: shot.file,
    url: shot.url,
    kind: shot.kind,
    captured: false,
    result: 'PARTIAL',
    note: 'Auth required; login gate — not captured in headless E3',
  });
}

const visual = {
  timestamp: new Date().toISOString(),
  browser: chrome,
  frontend_shots: manifest.filter((m) => m.kind !== 'admin'),
  admin_shots: manifest.filter((m) => m.kind === 'admin'),
  captured_count: manifest.filter((m) => m.captured).length,
  frontend_captured: manifest.filter((m) => m.kind !== 'admin' && m.captured).length,
  admin_captured: manifest.filter((m) => m.kind === 'admin' && m.captured).length,
  total_frontend: shots.length,
  total_admin: adminShots.length,
  result: manifest.filter((m) => m.kind !== 'admin').every((m) => m.captured) ? 'PASS' : 'PARTIAL',
  admin_result: 'PARTIAL',
};

writeFileSync(join(__dirname, 'screenshot-manifest.json'), JSON.stringify({ manifest, result: visual.result, admin_result: visual.admin_result }, null, 2));
writeFileSync(join(__dirname, 'visual-result.json'), JSON.stringify(visual, null, 2));
console.log(JSON.stringify(visual, null, 2));
