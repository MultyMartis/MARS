/**
 * FP-0002 V9-06E26D — screenshot capture helper. NOT FOR GIT.
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

const desktopShots = [
  { file: 'runtime-blog-archive-with-card-desktop-e26d.png', url: domain + '/blog/', width: 1440, height: 1200 },
  { file: 'runtime-blog-single-desktop-e26d.png', url: domain + '/blog/nazvanie-stati/', width: 1440, height: 2200 },
  { file: 'runtime-blog-single-toc-e26d.png', url: domain + '/blog/nazvanie-stati/', width: 1440, height: 900 },
  { file: 'runtime-blog-single-final-cta-e26d.png', url: domain + '/blog/nazvanie-stati/#blog-article-cta-01', width: 1440, height: 900 },
];

const mobileShots = [
  { file: 'runtime-blog-archive-with-card-mobile-e26d.png', url: domain + '/blog/', width: 390, height: 1400 },
  { file: 'runtime-blog-single-mobile-e26d.png', url: domain + '/blog/nazvanie-stati/', width: 390, height: 2600 },
];

mkdirSync(shotDir, { recursive: true });
const userDataDir = join(__dirname, '_chrome-profile-tmp-e26d');
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

async function captureShot(shot) {
  const outPath = join(shotDir, shot.file);
  const args = [
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--force-device-scale-factor=1',
    `--window-size=${shot.width},${shot.height}`,
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
    return {
      file: shot.file,
      url: shot.url,
      viewport: `${shot.width}x${shot.height}`,
      captured,
      bytes: st.size,
      sha256: captured ? sha256(outPath) : null,
      result: captured ? 'PASS' : 'FAIL',
    };
  } catch (err) {
    return {
      file: shot.file,
      url: shot.url,
      viewport: `${shot.width}x${shot.height}`,
      captured: false,
      error: String(err.message || err),
      result: 'FAIL',
    };
  }
}

const manifest = [];
for (const shot of [...desktopShots, ...mobileShots]) {
  manifest.push(await captureShot(shot));
}

const adminShots = [
  { file: 'admin-demo-post-article-meta-e26d.png', url: domain + '/wp-admin/post.php?post=DEMO_ID&action=edit' },
  { file: 'admin-demo-post-status-e26d.png', url: domain + '/wp-admin/edit.php' },
];
for (const shot of adminShots) {
  manifest.push({
    file: shot.file,
    url: shot.url,
    captured: false,
    result: 'PARTIAL',
    note: 'Auth required; not captured in headless E26D',
  });
}

const frontendCaptured = manifest.filter((m) => m.captured).length;
const visual = {
  timestamp: new Date().toISOString(),
  browser: chrome,
  captured_count: frontendCaptured,
  total_frontend: desktopShots.length + mobileShots.length,
  desktop_captured: manifest.filter((m) => m.file.includes('desktop') && m.captured).length,
  mobile_captured: manifest.filter((m) => m.file.includes('mobile') && m.captured).length,
  result: frontendCaptured >= 4 ? 'PASS' : frontendCaptured >= 2 ? 'PARTIAL' : 'FAIL',
  admin_result: 'PARTIAL',
};

writeFileSync(join(__dirname, 'screenshot-manifest.json'), JSON.stringify({ manifest, result: visual.result }, null, 2));
writeFileSync(join(__dirname, 'visual-evidence-result.json'), JSON.stringify(visual, null, 2));
console.log(JSON.stringify(visual, null, 2));
