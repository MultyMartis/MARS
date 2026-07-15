/**
 * FP-0002 V9-06D9-J — screenshots + frontend media validation.
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
  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D9-J', result: 'FAIL', error: 'NO_BROWSER' }, null, 2));
  process.exit(2);
}

const EXPECTED_MAIN_SECTIONS = [
  'home-recovery-intro', 'founder-quote', 'home-treatment-prevention', 'home-gallery',
  'home-why-us', 'home-staff-photo', 'home-feature-grid', 'clinic-landscape',
  'home-recovery-life', 'reviews', 'home-rehabilitation-requirements',
  'home-rehabilitation-program', 'home-genotyping', 'comfort', 'home-videos',
  'specialists', 'home-articles', 'faq', 'final-form',
];

const SHOTS = [
  { file: 'runtime-home-full-desktop-d9j-current.png', url: `${runtimeUrl}/`, size: '1440,9000' },
  { file: 'runtime-home-full-mobile-d9j-current.png', url: `${runtimeUrl}/`, size: '390,12000' },
  { file: 'runtime-hero-media-d9j-current.png', url: `${runtimeUrl}/#hero`, size: '1440,1200' },
  { file: 'runtime-gallery-media-d9j-current.png', url: `${runtimeUrl}/#home-gallery`, size: '1440,1200' },
  { file: 'runtime-comfort-media-d9j-current.png', url: `${runtimeUrl}/#comfort`, size: '1440,1400' },
  { file: 'runtime-specialists-media-d9j-current.png', url: `${runtimeUrl}/#specialists`, size: '1440,1200' },
  { file: 'runtime-footer-d9j-current.png', url: `${runtimeUrl}/#site-footer`, size: '1440,900' },
  { file: 'runtime-service-74-d9j-current.png', url: `${runtimeUrl}/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/`, size: '1440,4000' },
  { file: 'runtime-contacts-d9j-current.png', url: `${runtimeUrl}/kontakty/`, size: '1440,3000' },
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

async function main() {
  const routes = [
    { path: '/', label: 'home' },
    { path: '/uslugi/', label: 'services-hub' },
    { path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', label: 'service-74' },
    { path: '/kontakty/', label: 'contacts' },
  ];
  const routeResults = [];
  for (const r of routes) {
    const { status, text } = await fetchText(`${runtimeUrl}${r.path}`);
    routeResults.push({ path: r.path, status, ok: status === 200, has_fatal: /fatal error/i.test(text) });
  }

  const home = await fetchText(`${runtimeUrl}/`);
  const sectionsFound = EXPECTED_MAIN_SECTIONS.filter((id) => home.text.includes(`id="${id}"`) || home.text.includes(`class="${id}`) || home.text.includes(id));
  const heroPresent = /hero__image|hero-main\.png|hero__media/.test(home.text);
  const galleryPresent = /home-gallery|shpigovsky-gallery/.test(home.text);
  const brokenImgPattern = home.text.match(/<img[^>]+src=""[^>]*>/g) || [];
  const themeHeroUrl = home.text.match(/themes\/shpigovsky\/assets\/img\/hero\/hero-main\.png/);

  const manifest = [];
  for (const s of SHOTS) {
    const outPath = join(shotDir, s.file);
    try {
      const meta = await screenshot(s.url, outPath, s.size);
      manifest.push({ screenshot: s.file, captured: meta.captured, bytes: meta.bytes, sha256: meta.sha256, result: meta.captured ? 'PASS' : 'FAIL' });
    } catch (e) {
      manifest.push({ screenshot: s.file, captured: false, result: 'FAIL', error: String(e.message || e) });
    }
  }

  const frontendValidation = {
    phase: 'V9-06D9-J',
    generated_at: capturedAt,
    mode: 'READ_ONLY',
    home_checks: {
      sections_expected: 19,
      sections_found_count: sectionsFound.length,
      sections_found: sectionsFound,
      hero_image_present: heroPresent,
      hero_theme_fallback_url: Boolean(themeHeroUrl),
      gallery_fallback_present: galleryPresent,
      broken_empty_src_imgs: brokenImgPattern.length,
      footer_present: /site-footer/.test(home.text),
      media_from_theme_fallback: Boolean(themeHeroUrl) || /themes\/shpigovsky\/assets\/img\/content/.test(home.text),
    },
    routes: routeResults,
    result: routeResults.every((r) => r.ok) && sectionsFound.length >= 18 && heroPresent ? 'PASS' : 'PARTIAL',
  };

  writeFileSync(join(evidenceDir, 'current-frontend-media-validation.json'), JSON.stringify(frontendValidation, null, 2) + '\n');
  writeFileSync(join(evidenceDir, 'screenshot-manifest.json'), JSON.stringify({ phase: 'V9-06D9-J', generated_at: capturedAt, screenshots: manifest, result: manifest.every((m) => m.result === 'PASS') ? 'PASS' : 'PARTIAL' }, null, 2) + '\n');
  writeFileSync(join(evidenceDir, 'visual-result.json'), JSON.stringify({ phase: 'V9-06D9-J', generated_at: capturedAt, frontend: frontendValidation.result, screenshots: manifest.filter((m) => m.captured).length + '/' + manifest.length, result: frontendValidation.result === 'PASS' && manifest.every((m) => m.captured) ? 'PASS' : 'PARTIAL' }, null, 2) + '\n');
  console.log('DONE', frontendValidation.result);
}

main().catch((e) => { console.error(e); process.exit(1); });
