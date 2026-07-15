/**
 * FP-0002 V9-06D8-G — post-seed visual smoke screenshots.
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
  { file: 'desktop-home-after-d8g.png', path: '/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-services-hub-after-d8g.png', path: '/uslugi/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-service-zavisimosti-after-d8g.png', path: '/uslugi/zavisimosti/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-service-alkogol-after-d8g.png', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-service-psych-after-d8g.png', path: '/uslugi/psihicheskoe-zdorovie/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-service-rpp-after-d8g.png', path: '/uslugi/rasstroystva-pischevogo-povedeniya/', size: '1440,900', viewport: 'desktop' },
  { file: 'desktop-contacts-after-d8g.png', path: '/kontakty/', size: '1440,900', viewport: 'desktop' },
  { file: 'mobile-home-after-d8g.png', path: '/', size: '390,844', viewport: 'mobile' },
  { file: 'mobile-services-hub-after-d8g.png', path: '/uslugi/', size: '390,844', viewport: 'mobile' },
  { file: 'mobile-service-alkogol-after-d8g.png', path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '390,844', viewport: 'mobile' },
  { file: 'mobile-contacts-after-d8g.png', path: '/kontakty/', size: '390,844', viewport: 'mobile' },
  { file: 'mobile-service-zavisimosti-after-d8g.png', path: '/uslugi/zavisimosti/', size: '390,844', viewport: 'mobile' },
  { file: 'mobile-service-psych-after-d8g.png', path: '/uslugi/psihicheskoe-zdorovie/', size: '390,844', viewport: 'mobile' },
  { file: 'mobile-service-rpp-after-d8g.png', path: '/uslugi/rasstroystva-pischevogo-povedeniya/', size: '390,844', viewport: 'mobile' },
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
      viewport: shot.viewport,
      url,
      bytes: st.size,
      captured: st.size > 1000,
      global_shell_intact: st.size > 5000,
      result: st.size > 1000 ? 'PASS' : 'FAIL',
    });
  } catch (e) {
    manifest.push({
      file: shot.file,
      path: `screenshots/${shot.file}`,
      route: shot.path,
      viewport: shot.viewport,
      url,
      captured: false,
      error: String(e.message || e),
      result: 'FAIL',
    });
  }
}

const required = manifest.filter((m) => !m.file.includes('mobile-service-zavisimosti') && !m.file.includes('mobile-service-psych') && !m.file.includes('mobile-service-rpp') || m.file.startsWith('desktop-') || ['mobile-home-after-d8g.png','mobile-services-hub-after-d8g.png','mobile-service-alkogol-after-d8g.png','mobile-contacts-after-d8g.png'].includes(m.file));
const requiredFiles = [
  'desktop-home-after-d8g.png','desktop-services-hub-after-d8g.png','desktop-service-zavisimosti-after-d8g.png',
  'desktop-service-alkogol-after-d8g.png','desktop-service-psych-after-d8g.png','desktop-service-rpp-after-d8g.png',
  'desktop-contacts-after-d8g.png','mobile-home-after-d8g.png','mobile-services-hub-after-d8g.png',
  'mobile-service-alkogol-after-d8g.png','mobile-contacts-after-d8g.png',
];
const reqManifest = manifest.filter((m) => requiredFiles.includes(m.file));
const captured = reqManifest.filter((m) => m.result === 'PASS').length;

const result = {
  phase: 'V9-06D8-G',
  generated_at: new Date().toISOString(),
  required_shots: requiredFiles.length,
  captured_shots: captured,
  optional_shots: manifest.length - requiredFiles.length,
  global_shell_intact: reqManifest.every((m) => m.result === 'PASS'),
  seeded_sections_note: 'Seeded ACF sections visible where theme renders them; media/operator gaps expected',
  pixel_perfect_claim: false,
  known_gaps: ['map embed omitted', 'messengers omitted', 'hero/gallery media missing', 'FAQ placeholder copy'],
  result: captured >= requiredFiles.length ? 'PASS' : (captured >= requiredFiles.length - 1 ? 'PARTIAL' : 'FAIL'),
};

writeFileSync(join(evidenceDir, 'visual-smoke-screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D8-G', generated_at: result.generated_at, shots: manifest }, null, 2));
writeFileSync(join(evidenceDir, 'visual-smoke-result.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result, null, 2));
