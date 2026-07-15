/**
 * FP-0002 V9-06D9-M — frontend regression + screenshot runner.
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
const adminUrl = 'http://shpigovsky.test/wp-admin/post.php?post=4&action=edit';
const capturedAt = new Date().toISOString();

mkdirSync(shotDir, { recursive: true });

const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe',
];
const chrome = chromeCandidates.find((p) => existsSync(p));
if (!chrome) {
  console.error('NO_BROWSER');
  process.exit(2);
}

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
    heroImageUrl: heroMatch?.[1] || null,
    heroUsesUploads: heroMatch?.[1]?.includes('/uploads/') ?? false,
    galleryImageCount: galleryMatches.length,
    galleryUrls: galleryMatches.map((m) => m[1]),
    galleryUsesUploads: galleryMatches.length > 0 && galleryMatches[0][1]?.includes('/uploads/'),
    faqHeading: html.includes('Нас часто спрашивают'),
    specialistsHeading: html.includes('Специалисты центра'),
    hasFooter: html.includes('class="site-footer"'),
    hasGalleryPagination: html.includes('data-gallery-pagination'),
  };
}

const mode = process.argv[2] || 'all';
const manifest = [];
const frontendResults = { routes: [], home: null, result: 'FAIL' };
const visualResult = { capturedAt, screenshots: [], result: 'FAIL' };

async function captureFrontend() {
  for (const route of ROUTES) {
    const url = runtimeUrl + route.path;
    const { status } = await fetchText(url);
    frontendResults.routes.push({ path: route.path, label: route.label, status, pass: status === 200 });
  }
  const home = await fetchText(runtimeUrl + '/');
  frontendResults.home = homeChecks(home.text);
  const all200 = frontendResults.routes.every((r) => r.pass);
  const homePass = frontendResults.home.sectionsPass && frontendResults.home.heroCta
    && frontendResults.home.heroUsesUploads && frontendResults.home.galleryUsesUploads
    && frontendResults.home.faqHeading && frontendResults.home.specialistsHeading && frontendResults.home.hasFooter;
  frontendResults.result = all200 && homePass ? 'PASS' : (all200 ? 'PARTIAL' : 'FAIL');
  writeFileSync(join(evidenceDir, 'frontend-regression-validation.json'), JSON.stringify({
    phase: 'V9-06D9-M',
    capturedAt,
    routes: frontendResults.routes,
    home: frontendResults.home,
    route_smoke: all200 ? 'ALL_200' : 'PARTIAL',
    result: frontendResults.result,
  }, null, 2) + '\n');

  const shots = [
    { file: 'runtime-home-full-desktop-after-d9m.png', url: runtimeUrl + '/', size: '1440,9000' },
    { file: 'runtime-home-full-mobile-after-d9m.png', url: runtimeUrl + '/', size: '390,8000' },
    { file: 'runtime-hero-gallery-after-d9m.png', url: runtimeUrl + '/#home-gallery', size: '1440,1200' },
    { file: 'runtime-service-74-after-d9m.png', url: runtimeUrl + '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', size: '1440,4000' },
    { file: 'runtime-contacts-after-d9m.png', url: runtimeUrl + '/kontakty/', size: '1440,3000' },
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
}

async function captureAdmin(label) {
  const outPath = join(shotDir, label);
  try {
    const meta = await screenshot(adminUrl, outPath, '1440,4000');
    manifest.push({ file: label, kind: 'admin', captured: meta.captured, sha256: meta.sha256, bytes: meta.bytes, note: 'Unauthenticated — may show login screen' });
  } catch (e) {
    manifest.push({ file: label, kind: 'admin', captured: false, error: String(e.message) });
  }
}

async function patchGateHttp() {
  const gatePath = join(evidenceDir, 'runtime-db-availability-gate.json');
  if (!existsSync(gatePath)) return;
  const gate = JSON.parse(readFileSync(gatePath, 'utf8'));
  try {
    const res = await fetch(runtimeUrl + '/');
    const check = gate.checks.find((c) => c.check === 'runtime_http_home');
    if (check) {
      check.result = res.status === 200 ? 'PASS' : 'FAIL';
      check.notes = `HTTP ${res.status}`;
    }
    const fail = gate.checks.some((c) => c.result === 'FAIL');
    gate.result = fail ? 'FAIL' : 'PASS';
    writeFileSync(gatePath, JSON.stringify(gate, null, 2) + '\n');
  } catch (e) {
    // keep PENDING
  }
}

async function main() {
  if (mode === 'admin-before' || mode === 'all') {
    await captureAdmin('wp-admin-home-native-editor-before-cleanup-d9m.png');
  }
  if (mode === 'frontend' || mode === 'all') {
    await captureFrontend();
  }
  if (mode === 'admin-after' || mode === 'all') {
    await captureAdmin('wp-admin-home-native-editor-after-cleanup-d9m.png');
    await captureAdmin('wp-admin-home-acf-fields-after-cleanup-d9m.png');
  }
  if (mode === 'gate-http' || mode === 'all') {
    await patchGateHttp();
  }
  visualResult.screenshots = manifest;
  visualResult.result = manifest.filter((m) => m.captured).length >= 5 ? 'PASS' : 'PARTIAL';
  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D9-M', capturedAt, items: manifest }, null, 2) + '\n');
  writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify(visualResult, null, 2) + '\n');
  console.log(JSON.stringify({ ok: true, frontend: frontendResults.result, visual: visualResult.result }));
}

main().catch((e) => { console.error(e); process.exit(1); });
