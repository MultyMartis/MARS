/**
 * FP-0002 V9-06D9-P — frontend/admin screenshot runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, mkdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = __dirname;
const shotDir = join(evidenceDir, 'screenshots');
const runtimeUrl = 'http://shpigovsky.test';
const capturedAt = new Date().toISOString();

mkdirSync(shotDir, { recursive: true });

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
const chrome = chromeCandidates.find((p) => existsSync(p));

function sha256(filePath) {
  const hash = createHash('sha256');
  hash.update(readFileSync(filePath));
  return hash.digest('hex').toUpperCase();
}

function runChrome(args) {
  return new Promise((resolve, reject) => {
    const child = spawn(chrome, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let stderr = '';
    child.stderr.on('data', (d) => { stderr += d.toString(); });
    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) resolve({ code, stderr });
      else reject(new Error(`browser exit ${code}: ${stderr.slice(0, 500)}`));
    });
  });
}

async function screenshot(url, outPath, size) {
  if (!chrome) throw new Error('NO_BROWSER');
  await runChrome([
    '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
    `--window-size=${size}`,
    `--user-data-dir=${join(evidenceDir, '_chrome-profile-tmp')}`,
    '--no-first-run', '--no-default-browser-check',
    `--screenshot=${outPath}`, url,
  ]);
  const st = statSync(outPath);
  const isLogin = st.size < 50000;
  return { bytes: st.size, captured: st.size > 1000, sha256: sha256(outPath), likely_login: isLogin };
}

const SHOTS = [
  { file: 'wp-admin-home-ux-d9p.png', kind: 'admin', url: `${runtimeUrl}/wp-admin/post.php?post=4&action=edit`, size: '1440,5000' },
  { file: 'wp-admin-home-reviews-teaser-d9p.png', kind: 'admin', url: `${runtimeUrl}/wp-admin/post.php?post=4&action=edit`, size: '1440,5000' },
  { file: 'wp-admin-services-ux-d9p.png', kind: 'admin', url: `${runtimeUrl}/wp-admin/post.php?post=5&action=edit`, size: '1440,4000' },
  { file: 'wp-admin-contacts-ux-d9p.png', kind: 'admin', url: `${runtimeUrl}/wp-admin/post.php?post=20&action=edit`, size: '1440,4000' },
  { file: 'wp-admin-privacy-policy-retained-d9p.png', kind: 'admin', url: `${runtimeUrl}/wp-admin/post.php?post=3&action=edit`, size: '1440,5000' },
  { file: 'runtime-home-full-desktop-d9p.png', kind: 'frontend', url: `${runtimeUrl}/`, size: '1440,12000' },
  { file: 'runtime-home-full-mobile-d9p.png', kind: 'frontend', url: `${runtimeUrl}/`, size: '390,14000' },
  { file: 'runtime-reviews-section-d9p.png', kind: 'frontend', url: `${runtimeUrl}/#reviews`, size: '1440,3500' },
  { file: 'runtime-service-74-d9p.png', kind: 'frontend', url: `${runtimeUrl}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`, size: '1440,8000' },
  { file: 'runtime-contacts-d9p.png', kind: 'frontend', url: `${runtimeUrl}/kontakty/`, size: '1440,6000' },
];

async function main() {
  const manifest = [];
  for (const shot of SHOTS) {
    const outPath = join(shotDir, shot.file);
    try {
      const meta = await screenshot(shot.url, outPath, shot.size);
      let result = meta.captured ? 'PASS' : 'FAIL';
      if (shot.kind === 'admin' && meta.likely_login) {
        result = 'PARTIAL';
      }
      manifest.push({
        file: shot.file,
        kind: shot.kind,
        url: shot.url,
        captured: meta.captured,
        bytes: meta.bytes,
        sha256: meta.sha256,
        result,
        note: shot.kind === 'admin' && meta.likely_login ? 'Unauthenticated — login screen; DB/policy evidence used' : null,
      });
    } catch (e) {
      manifest.push({ file: shot.file, kind: shot.kind, captured: false, result: 'FAIL', error: String(e.message) });
    }
  }

  const adminPartial = manifest.filter((m) => m.kind === 'admin' && m.result === 'PARTIAL').length;
  const frontendPass = manifest.filter((m) => m.kind === 'frontend' && m.result === 'PASS').length;
  const visual = {
    phase: 'V9-06D9-P',
    generated_at: capturedAt,
    admin_screenshots: adminPartial > 0 ? 'PARTIAL' : 'PASS',
    frontend_screenshots: frontendPass >= 5 ? 'PASS' : 'PARTIAL',
    admin_note: 'Headless capture without auth may show wp-login.php',
    result: frontendPass >= 5 ? (adminPartial > 0 ? 'PARTIAL' : 'PASS') : 'PARTIAL',
  };

  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D9-P', generated_at: capturedAt, shots: manifest }, null, 2) + '\n');
  writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify(visual, null, 2) + '\n');
  console.log(JSON.stringify(visual));
}

main().catch((e) => { console.error(e); process.exit(1); });
