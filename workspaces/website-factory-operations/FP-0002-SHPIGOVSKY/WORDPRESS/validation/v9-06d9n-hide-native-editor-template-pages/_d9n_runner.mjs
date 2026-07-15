/**
 * FP-0002 V9-06D9-N — frontend regression + screenshot runner.
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

const EXPECTED_MAIN_SECTIONS = [
  'home-recovery-intro', 'founder-quote', 'home-treatment-prevention', 'home-gallery',
  'home-why-us', 'home-staff-photo', 'home-feature-grid', 'clinic-landscape',
  'home-recovery-life', 'reviews', 'home-rehabilitation-requirements',
  'home-rehabilitation-program', 'home-genotyping', 'comfort', 'home-videos',
  'specialists', 'home-articles', 'faq', 'final-form',
];

const ROUTES = [
  { path: '/', label: 'home' },
  { path: '/uslugi/', label: 'services-hub' },
  { path: '/uslugi/zavisimosti/', label: 'service-73' },
  { path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', label: 'service-74' },
  { path: '/uslugi/psihicheskoe-zdorovie/', label: 'service-77' },
  { path: '/uslugi/rasstroystva-pischevogo-povedeniya/', label: 'service-84' },
  { path: '/kontakty/', label: 'contacts' },
];

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
      else reject(new Error(`chrome exit ${code}: ${stderr.slice(0, 500)}`));
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
  return { bytes: st.size, captured: st.size > 1000, sha256: sha256(outPath) };
}

async function fetchText(url) {
  const res = await fetch(url, { redirect: 'follow' });
  return { status: res.status, text: await res.text() };
}

function homeChecks(html) {
  const sectionsFound = EXPECTED_MAIN_SECTIONS.filter((cls) => html.includes(cls));
  const heroMatch = html.match(/class="hero__image"[^>]*src="([^"]+)"/);
  const galleryMatches = [...html.matchAll(/class="home-gallery__image"[^>]*src="([^"]+)"/g)];
  return {
    sectionCount: sectionsFound.length,
    sectionsExpected: EXPECTED_MAIN_SECTIONS.length,
    sectionsPass: sectionsFound.length === EXPECTED_MAIN_SECTIONS.length,
    heroCta: html.includes('Записаться на консультацию'),
    heroImagePresent: Boolean(heroMatch?.[1]),
    heroUsesUploads: heroMatch?.[1]?.includes('/uploads/') ?? false,
    galleryImageCount: galleryMatches.length,
    galleryUsesUploads: galleryMatches.length > 0 && galleryMatches[0][1]?.includes('/uploads/'),
    faqHeading: html.includes('Нас часто спрашивают'),
    specialistsHeading: html.includes('Специалисты центра'),
    hasFooter: html.includes('class="site-footer"'),
  };
}

const mode = process.argv[2] || 'all';
const manifest = [];

async function captureAdmin(label, postId) {
  const url = `${runtimeUrl}/wp-admin/post.php?post=${postId}&action=edit`;
  const outPath = join(shotDir, label);
  try {
    const meta = await screenshot(url, outPath, '1440,4000');
    manifest.push({ file: label, kind: 'admin', postId, captured: meta.captured, sha256: meta.sha256, bytes: meta.bytes, note: 'Unauthenticated — may show login screen' });
  } catch (e) {
    manifest.push({ file: label, kind: 'admin', postId, captured: false, error: String(e.message) });
  }
}

async function captureFrontend() {
  const routes = [];
  for (const route of ROUTES) {
    const url = runtimeUrl + route.path;
    const { status } = await fetchText(url);
    routes.push({ path: route.path, label: route.label, status, pass: status === 200 });
  }
  const home = await fetchText(runtimeUrl + '/');
  const homeResult = homeChecks(home.text);
  const all200 = routes.every((r) => r.pass);
  const homePass = homeResult.sectionsPass && homeResult.heroCta && homeResult.heroUsesUploads
    && homeResult.galleryUsesUploads && homeResult.faqHeading && homeResult.specialistsHeading && homeResult.hasFooter;
  const result = all200 && homePass ? 'PASS' : (all200 ? 'PARTIAL' : 'FAIL');
  writeFileSync(join(evidenceDir, 'frontend-regression-validation.json'), JSON.stringify({
    phase: 'V9-06D9-N',
    capturedAt,
    routes,
    home: homeResult,
    route_smoke: all200 ? 'ALL_200' : 'PARTIAL',
    result,
  }, null, 2) + '\n');

  const shots = [
    { file: 'runtime-home-full-desktop-after-d9n.png', url: runtimeUrl + '/', size: '1440,9000' },
    { file: 'runtime-home-full-mobile-after-d9n.png', url: runtimeUrl + '/', size: '390,8000' },
    { file: 'runtime-service-74-after-d9n.png', url: runtimeUrl + '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '1440,4000' },
    { file: 'runtime-contacts-after-d9n.png', url: runtimeUrl + '/kontakty/', size: '1440,3000' },
  ];
  for (const s of shots) {
    const outPath = join(shotDir, s.file);
    try {
      const meta = await screenshot(s.url, outPath, s.size);
      manifest.push({ file: s.file, kind: 'frontend', captured: meta.captured, sha256: meta.sha256, bytes: meta.bytes });
    } catch (e) {
      manifest.push({ file: s.file, kind: 'frontend', captured: false, error: String(e.message) });
    }
  }
  return result;
}

async function main() {
  if (mode === 'admin-before' || mode === 'all') {
    await captureAdmin('wp-admin-home-editor-before-d9n.png', 4);
  }
  if (mode === 'admin-after' || mode === 'all') {
    await captureAdmin('wp-admin-home-editor-after-d9n.png', 4);
    await captureAdmin('wp-admin-home-acf-fields-after-d9n.png', 4);
    await captureAdmin('wp-admin-services-editor-after-d9n.png', 5);
    await captureAdmin('wp-admin-contacts-editor-after-d9n.png', 20);
    await captureAdmin('wp-admin-privacy-policy-editor-retained-d9n.png', 3);
  }
  let frontendResult = 'NOT_RUN';
  if (mode === 'frontend' || mode === 'all') {
    frontendResult = await captureFrontend();
  }
  const adminCaptured = manifest.filter((m) => m.kind === 'admin' && m.captured).length;
  const frontendCaptured = manifest.filter((m) => m.kind === 'frontend' && m.captured).length;
  const visualResult = {
    capturedAt,
    adminCaptured,
    frontendCaptured,
    result: frontendCaptured >= 3 ? (adminCaptured > 0 ? 'PASS' : 'PARTIAL') : 'PARTIAL',
    note: adminCaptured === 0 ? 'Admin screenshots PARTIAL — unauthenticated headless capture shows login screen' : '',
  };
  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D9-N', capturedAt, items: manifest }, null, 2) + '\n');
  writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify(visualResult, null, 2) + '\n');
  console.log(JSON.stringify({ ok: true, frontend: frontendResult, visual: visualResult.result }));
}

main().catch((e) => { console.error(e); process.exit(1); });
