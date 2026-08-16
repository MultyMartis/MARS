/**
 * FP-0002 V9-06E5 — screenshot capture helper. NOT FOR GIT.
 */
import { spawn } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const shotDir = join(__dirname, 'screenshots');
const domain = 'http://shpigovsky.test';
const staticDist = 'X:/AI MARS/workspaces/fp-0002-shpigovsky-v9/dist';

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
  { file: 'runtime-uslugi-repaired-e5.png', url: domain + '/uslugi/', kind: 'runtime' },
  { file: 'runtime-zavisimosti-repaired-e5.png', url: domain + '/uslugi/zavisimosti/', kind: 'runtime' },
  { file: 'static-v9-uslugi-reference-e5.png', url: 'file:///' + join(staticDist, 'uslugi/index.html').replace(/\\/g, '/'), kind: 'static' },
  { file: 'static-v9-zavisimosti-reference-e5.png', url: 'file:///' + join(staticDist, 'uslugi/zavisimosti/index.html').replace(/\\/g, '/'), kind: 'static' },
  { file: 'runtime-final-form-bg-e5.png', url: domain + '/uslugi/', kind: 'runtime-bg' },
  { file: 'runtime-service-subdivision-start-bg-e5.png', url: domain + '/uslugi/zavisimosti/', kind: 'runtime-bg' },
  { file: 'runtime-rehabilitation-cta-bg-e5.png', url: domain + '/', kind: 'runtime-bg' },
  { file: 'runtime-home-regression-e5.png', url: domain + '/', kind: 'regression' },
  { file: 'runtime-service-74-regression-e5.png', url: domain + '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', kind: 'regression' },
  { file: 'runtime-reviews-regression-e5.png', url: domain + '/otzyvy/', kind: 'regression' },
  { file: 'runtime-privacy-policy-regression-e5.png', url: domain + '/privacy-policy/', kind: 'regression' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(__dirname, '_chrome-profile-tmp-e5');
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
    `--user-data-dir=${userDataDir}`,
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--window-size=1440,900',
    `--screenshot=${outPath}`,
    shot.url,
  ];
  let captured = false;
  let error = null;
  try {
    await runChrome(args);
    captured = existsSync(outPath);
  } catch (e) {
    error = String(e.message || e);
  }
  manifest.push({
    file: shot.file,
    url: shot.url,
    kind: shot.kind,
    captured,
    sha256: captured ? sha256(outPath) : null,
    error,
  });
}

writeFileSync(join(__dirname, 'screenshot-manifest.json'), JSON.stringify({ shots: manifest, captured_at: new Date().toISOString() }, null, 2));
console.log(JSON.stringify({ ok: true, captured: manifest.filter((s) => s.captured).length, total: manifest.length }));
