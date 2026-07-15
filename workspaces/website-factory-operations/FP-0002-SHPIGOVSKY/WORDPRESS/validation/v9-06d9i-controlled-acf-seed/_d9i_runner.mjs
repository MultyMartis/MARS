/**
 * FP-0002 V9-06D9-I — post-seed visual validation + screenshots.
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
  const faqHeading = html.match(/<h2[^>]*id="faq-heading"[^>]*>([^<]+)/i);
  return {
    sectionCount: sectionsFound.length,
    sectionsExpected: EXPECTED_MAIN_SECTIONS.length,
    sectionsPass: sectionsFound.length === EXPECTED_MAIN_SECTIONS.length,
    heroCta: html.includes('Записаться на консультацию'),
    faqHeadingText: faqHeading?.[1]?.replace(/\s+/g, ' ').trim() || null,
    faqHeadingPass: faqHeading?.[1]?.includes('Нас часто спрашивают') ?? false,
    featureGrid: html.includes('home-feature-grid'),
    recoveryIntro: html.includes('home-recovery-intro'),
    hasGalleryPagination: html.includes('data-gallery-pagination'),
    hasFooter: html.includes('class="site-footer"'),
    rawAcfLeak: (() => {
      const main = html.match(/<main[\s\S]*?<\/main>/i)?.[0] || '';
      return /home_[a-z_]+/i.test(main) && /Array|field_fp02/i.test(main);
    })(),
    phpFatal: /Fatal error|Parse error/i.test(html),
  };
}

async function main() {
  const routeResults = [];
  for (const route of ROUTES) {
    const fullUrl = route.path === '/' ? `${runtimeUrl}/` : `${runtimeUrl}${route.path}`;
    try {
      const { status } = await fetchText(fullUrl);
      routeResults.push({ path: route.path, label: route.label, status, pass: status === 200 });
    } catch (e) {
      routeResults.push({ path: route.path, label: route.label, status: 0, pass: false, error: String(e) });
    }
  }

  const home = await fetchText(`${runtimeUrl}/`);
  const checks = homeChecks(home.text);

  const shots = [
    { name: 'runtime-home-full-desktop-after-d9i.png', url: `${runtimeUrl}/`, size: '1440,9000' },
    { name: 'runtime-home-full-mobile-after-d9i.png', url: `${runtimeUrl}/`, size: '390,12000' },
    { name: 'runtime-hero-after-d9i.png', url: `${runtimeUrl}/`, size: '1440,1200' },
    { name: 'runtime-faq-after-d9i.png', url: `${runtimeUrl}/`, size: '1440,5000' },
    { name: 'runtime-feature-grid-after-d9i.png', url: `${runtimeUrl}/`, size: '1440,4000' },
    { name: 'runtime-recovery-intro-after-d9i.png', url: `${runtimeUrl}/`, size: '1440,3500' },
    { name: 'runtime-footer-after-d9i.png', url: `${runtimeUrl}/`, size: '1440,2000' },
    { name: 'runtime-services-hub-after-d9i.png', url: `${runtimeUrl}/uslugi/`, size: '1440,3000' },
    { name: 'runtime-service-74-after-d9i.png', url: `${runtimeUrl}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`, size: '1440,3000' },
    { name: 'runtime-contacts-after-d9i.png', url: `${runtimeUrl}/kontakty/`, size: '1440,3000' },
  ];

  const screenshotManifest = [];
  for (const shot of shots) {
    const outPath = join(shotDir, shot.name);
    try {
      const meta = await screenshot(shot.url, outPath, shot.size);
      screenshotManifest.push({ file: shot.name, ...meta, result: meta.captured ? 'PASS' : 'FAIL' });
    } catch (e) {
      screenshotManifest.push({ file: shot.name, captured: false, result: 'FAIL', error: String(e) });
    }
  }

  const routeSmoke = {
    task: 'V9-06D9-I', captured_at: capturedAt, routes: routeResults,
    all_200: routeResults.every((r) => r.pass),
    result: routeResults.every((r) => r.pass) ? 'ALL_200' : 'PARTIAL',
  };

  const homeVisual = {
    task: 'V9-06D9-I', captured_at: capturedAt, http_status: home.status, ...checks,
    result: checks.sectionsPass && checks.heroCta && checks.faqHeadingPass && !checks.phpFatal ? 'PASS' : 'PARTIAL',
  };

  const consoleNetwork = {
    task: 'V9-06D9-I', captured_at: capturedAt,
    php_fatal_on_home: checks.phpFatal, raw_acf_leak: checks.rawAcfLeak,
    result: !checks.phpFatal && !checks.rawAcfLeak ? 'PASS' : 'FAIL',
  };

  writeFileSync(join(evidenceDir, 'post-seed-route-smoke.json'), JSON.stringify(routeSmoke, null, 2));
  writeFileSync(join(evidenceDir, 'post-seed-home-visual-regression-check.json'), JSON.stringify(homeVisual, null, 2));
  writeFileSync(join(evidenceDir, 'post-seed-console-network-check.json'), JSON.stringify(consoleNetwork, null, 2));
  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ captured_at: capturedAt, screenshots: screenshotManifest }, null, 2));
  writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify({
    captured_at: capturedAt,
    home_visual: homeVisual.result,
    screenshots_captured: screenshotManifest.filter((s) => s.captured).length,
    screenshots_total: screenshotManifest.length,
    result: homeVisual.result,
  }, null, 2));

  console.log(JSON.stringify({ routeSmoke: routeSmoke.result, homeVisual: homeVisual.result, shots: screenshotManifest.filter((s) => s.captured).length }));
}

main().catch((e) => { console.error(e); process.exit(1); });
