/**
 * FP-0002 V9-06E1 — legal static copy seed screenshot capture.
 * Local helper — not for Git staging.
 */
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, statSync, readFileSync } from 'node:fs';
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
  { file: 'runtime-privacy-policy-seeded-e1.png', url: domain + '/privacy-policy/', kind: 'frontend' },
  { file: 'runtime-user-agreement-seeded-e1.png', url: domain + '/user-agreement/', kind: 'frontend' },
  { file: 'runtime-consent-personal-data-seeded-e1.png', url: domain + '/consent-personal-data/', kind: 'frontend' },
  { file: 'runtime-cookie-policy-seeded-e1.png', url: domain + '/cookie-files-policy/', kind: 'frontend' },
  { file: 'wp-admin-privacy-policy-editor-e1.png', url: domain + '/wp-admin/post.php?post=3&action=edit', kind: 'admin' },
  { file: 'wp-admin-user-agreement-editor-e1.png', url: domain + '/wp-admin/post.php?post=22&action=edit', kind: 'admin' },
  { file: 'wp-admin-consent-editor-e1.png', url: domain + '/wp-admin/post.php?post=23&action=edit', kind: 'admin' },
  { file: 'wp-admin-cookie-policy-editor-e1.png', url: domain + '/wp-admin/post.php?post=24&action=edit', kind: 'admin' },
  { file: 'wp-admin-privacy-setting-e1.png', url: domain + '/wp-admin/options-privacy.php', kind: 'admin' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(__dirname, '_chrome-profile-tmp-e1');
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
      notes: shot.kind === 'admin' ? 'Login gate may apply; PARTIAL if login screen' : '',
    });
  } catch (err) {
    manifest.push({
      file: shot.file,
      url: shot.url,
      kind: shot.kind,
      captured: false,
      result: 'FAIL',
      notes: String(err.message || err).slice(0, 200),
    });
  }
}

const frontendCaptured = manifest.filter((m) => m.kind === 'frontend' && m.captured).length;
const adminCaptured = manifest.filter((m) => m.kind === 'admin' && m.captured).length;

const screenshotManifest = {
  phase: 'V9-06E1',
  generated_at: new Date().toISOString(),
  screenshots: manifest,
  frontend_captured: frontendCaptured,
  admin_captured: adminCaptured,
  result: frontendCaptured === 4 ? 'PASS' : 'PARTIAL',
};

const visualResult = {
  phase: 'V9-06E1',
  generated_at: new Date().toISOString(),
  frontend_screenshots: frontendCaptured,
  admin_screenshots: adminCaptured,
  admin_auth_available: false,
  result: frontendCaptured === 4 ? (adminCaptured > 0 ? 'PASS' : 'PARTIAL') : 'PARTIAL',
  notes: 'Admin screenshots may show login gate without authenticated session',
};

import { writeFileSync } from 'node:fs';
writeFileSync(join(__dirname, 'screenshot-manifest.json'), JSON.stringify(screenshotManifest, null, 2));
writeFileSync(join(__dirname, 'visual-result.json'), JSON.stringify(visualResult, null, 2));
console.log(JSON.stringify({ screenshotManifest, visualResult }, null, 2));
