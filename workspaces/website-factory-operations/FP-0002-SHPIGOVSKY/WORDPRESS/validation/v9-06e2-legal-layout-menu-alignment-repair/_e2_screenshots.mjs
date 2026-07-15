/**
 * FP-0002 V9-06E2 — screenshot capture helper. NOT FOR GIT.
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
  { file: 'runtime-privacy-policy-width-e2.png', url: domain + '/privacy-policy/', kind: 'legal' },
  { file: 'runtime-user-agreement-width-e2.png', url: domain + '/user-agreement/', kind: 'legal' },
  { file: 'runtime-consent-width-e2.png', url: domain + '/consent-personal-data/', kind: 'legal' },
  { file: 'runtime-cookie-policy-width-e2.png', url: domain + '/cookie-files-policy/', kind: 'legal' },
  { file: 'runtime-footer-legal-links-e2.png', url: domain + '/privacy-policy/', kind: 'footer', clip: 'footer' },
  { file: 'runtime-main-menu-e2.png', url: domain + '/', kind: 'menu' },
  { file: 'runtime-home-menu-e2.png', url: domain + '/', kind: 'core' },
  { file: 'runtime-services-menu-e2.png', url: domain + '/uslugi/', kind: 'core' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(__dirname, '_chrome-profile-tmp-e2');
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

const visual = {
  timestamp: new Date().toISOString(),
  browser: chrome,
  shots: manifest,
  captured_count: manifest.filter((m) => m.captured).length,
  total: manifest.length,
  result: manifest.every((m) => m.captured) ? 'PASS' : 'PARTIAL',
};

import { writeFileSync } from 'node:fs';
writeFileSync(join(__dirname, 'screenshot-manifest.json'), JSON.stringify({ manifest, result: visual.result }, null, 2));
writeFileSync(join(__dirname, 'visual-result.json'), JSON.stringify(visual, null, 2));
console.log(JSON.stringify(visual, null, 2));
