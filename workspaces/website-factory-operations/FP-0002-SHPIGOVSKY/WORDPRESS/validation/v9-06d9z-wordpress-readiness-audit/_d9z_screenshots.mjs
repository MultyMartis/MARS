/**
 * FP-0002 V9-06D9-Z — readiness audit screenshot capture (frontend + admin attempt).
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
  { file: 'runtime-home-readiness-d9z.png', url: domain + '/', kind: 'frontend' },
  { file: 'runtime-services-hub-readiness-d9z.png', url: domain + '/uslugi/', kind: 'frontend' },
  { file: 'runtime-service-74-readiness-d9z.png', url: domain + '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', kind: 'frontend' },
  { file: 'runtime-contacts-readiness-d9z.png', url: domain + '/kontakty/', kind: 'frontend' },
  { file: 'runtime-reviews-readiness-d9z.png', url: domain + '/otzyvy/', kind: 'frontend' },
  { file: 'wp-admin-home-readiness-d9z.png', url: domain + '/wp-admin/post.php?post=4&action=edit', kind: 'admin' },
  { file: 'wp-admin-reviews-readiness-d9z.png', url: domain + '/wp-admin/admin.php?page=fp02-reviews', kind: 'admin' },
  { file: 'wp-admin-site-settings-readiness-d9z.png', url: domain + '/wp-admin/admin.php?page=fp02-site-settings', kind: 'admin' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(__dirname, '_chrome-profile-tmp-d9z');
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
      kind: shot.kind,
      url: shot.url,
      bytes: st.size,
      sha256: captured ? sha256(outPath) : null,
      captured,
      result: captured ? 'PASS' : 'FAIL',
    });
    console.log(`OK ${shot.file} bytes=${st.size}`);
  } catch (err) {
    manifest.push({
      file: shot.file,
      kind: shot.kind,
      url: shot.url,
      bytes: 0,
      captured: false,
      error: String(err.message || err),
      result: 'FAIL',
    });
    console.error(`FAIL ${shot.file}: ${err.message || err}`);
  }
}

console.log(JSON.stringify({ manifest }, null, 2));
