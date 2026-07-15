/**
 * FP-0002 V9-06E28 — final readiness visual smoke screenshots.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
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
  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ result: 'NO_BROWSER', shots: [] }, null, 2));
  process.exit(0);
}

const shots = [
  { file: 'desktop-home-e28.png', path: '/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-home-e28.png', path: '/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-o-centre-e28.png', path: '/o-centre/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-o-centre-e28.png', path: '/o-centre/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-blog-e28.png', path: '/blog/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-blog-e28.png', path: '/blog/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-blog-single-e28.png', path: '/blog/nazvanie-stati/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-blog-single-e28.png', path: '/blog/nazvanie-stati/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-uslugi-e28.png', path: '/uslugi/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-uslugi-e28.png', path: '/uslugi/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-zavisimosti-e28.png', path: '/uslugi/zavisimosti/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-zavisimosti-e28.png', path: '/uslugi/zavisimosti/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-alkogol-e28.png', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-alkogol-e28.png', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '390,844', viewport: 'mobile' },
  { file: 'desktop-kontakty-e28.png', path: '/kontakty/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-otzyvy-e28.png', path: '/otzyvy/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-privacy-e28.png', path: '/privacy-policy/', size: '1440,900', viewport: 'desktop' },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(evidenceDir, '_chrome-profile-tmp-e28');
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
  try {
    await runChrome([
      '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
      `--window-size=${shot.size}`, `--user-data-dir=${userDataDir}`,
      '--no-first-run', '--no-default-browser-check', `--screenshot=${outPath}`, url,
    ]);
    const st = statSync(outPath);
    manifest.push({ file: shot.file, path: shot.path, viewport: shot.viewport, url, bytes: st.size, result: 'PASS' });
  } catch (e) {
    manifest.push({ file: shot.file, path: shot.path, viewport: shot.viewport, url, result: 'FAIL', error: String(e) });
  }
}

const out = { task_id: 'V9-06E28', generated_at: new Date().toISOString(), shots: manifest, captured: manifest.filter((s) => s.result === 'PASS').length, result: manifest.every((s) => s.result === 'PASS') ? 'PASS' : 'PARTIAL' };
writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify(out, null, 2) + '\n');
console.log('screenshots:', out.captured, '/', manifest.length);
