/**
 * FP-0002 V9-06D8-D — services hub visual smoke screenshots.
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
  console.error('NO_BROWSER');
  process.exit(2);
}

const shots = [
  { file: 'desktop-services-hub-after-d8d.png', path: '/uslugi/', size: '1440,900' },
  { file: 'mobile-services-hub-after-d8d.png', path: '/uslugi/', size: '390,844' },
  { file: 'desktop-home-after-d8d.png', path: '/', size: '1440,900' },
  { file: 'desktop-service-alkogol-after-d8d.png', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '1440,900' },
  { file: 'desktop-contacts-after-d8d.png', path: '/kontakty/', size: '1440,900' },
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
  } catch (e) {
    manifest.push({
      file: shot.file,
      path: `screenshots/${shot.file}`,
      route: shot.path,
      viewport: vp,
      captured: false,
      error: String(e.message || e),
      result: 'FAIL',
    });
  }
}

const required = manifest.filter((m) => m.file.includes('services-hub'));
const passCount = manifest.filter((m) => m.result === 'PASS').length;
const result = {
  phase: 'V9-06D8-D',
  generated_at: new Date().toISOString(),
  required_shots: 2,
  captured_shots: required.filter((m) => m.result === 'PASS').length,
  services_hub_visible: required.every((m) => m.result === 'PASS'),
  seeded_faq_expected: true,
  global_shell_intact: manifest.filter((m) => m.file.startsWith('desktop-home') || m.file.startsWith('desktop-contacts')).every((m) => m.result === 'PASS'),
  pixel_perfect_claim: false,
  known_gaps: ['founder-quote/comfort/genotyping/galleries deferred', 'hero image media not seeded'],
  result: required.filter((m) => m.result === 'PASS').length >= 2 ? 'PASS' : 'PARTIAL',
};

writeFileSync(join(evidenceDir, 'visual-smoke-screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D8-D', generated_at: result.generated_at, shots: manifest }, null, 2));
writeFileSync(join(evidenceDir, 'visual-smoke-result.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
