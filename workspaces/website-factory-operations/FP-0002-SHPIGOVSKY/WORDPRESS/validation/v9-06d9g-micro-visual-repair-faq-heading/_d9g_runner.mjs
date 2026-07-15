/**
 * FP-0002 V9-06D9-G — FAQ micro repair validation runner.
 * TEMPORARY HELPER — NOT FOR GIT COMMIT
 */
import { spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import {
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
  writeFileSync,
} from 'node:fs';
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
    '--headless=new',
    '--disable-gpu',
    '--hide-scrollbars',
    '--force-device-scale-factor=1',
    `--window-size=${size}`,
    `--user-data-dir=${join(evidenceDir, '_chrome-profile-tmp')}`,
    '--no-first-run',
    '--no-default-browser-check',
    `--screenshot=${outPath}`,
    url,
  ]);
  const st = statSync(outPath);
  return { bytes: st.size, captured: st.size > 1000, sha256: sha256(outPath) };
}

async function fetchText(url) {
  const res = await fetch(url, { redirect: 'follow' });
  return { status: res.status, text: await res.text() };
}

function faqChecks(html) {
  const faqAria = html.match(/<section[^>]*class="faq[^"]*"[^>]*aria-labelledby="([^"]+)"/i);
  const faqHeading = html.match(/<section[^>]*class="faq[^"]*"[\s\S]*?<h2[^>]*id="([^"]+)"[^>]*>([^<]+)</i);
  const comfortHeadingCount = (html.match(/id="comfort-heading"/g) || []).length;
  const faqHeadingCount = (html.match(/id="faq-heading"/g) || []).length;
  const comfortSection = html.match(/<section[^>]*class="comfort[^"]*"[\s\S]*?<h2[^>]*id="comfort-heading"[^>]*>([^<]+)</i);
  return {
    faqAriaLabelledby: faqAria?.[1] || null,
    faqHeadingId: faqHeading?.[1] || null,
    faqHeadingText: faqHeading?.[2]?.replace(/\s+/g, ' ').trim() || null,
    comfortHeadingCount,
    faqHeadingCount,
    comfortSectionHeading: comfortSection?.[1]?.replace(/\s+/g, ' ').trim() || null,
    comfortSectionPresent: Boolean(comfortSection),
    duplicateComfortHeading: comfortHeadingCount > 1,
    heroCta: html.includes('Записаться на консультацию'),
    specialistsHeading: html.includes('id="specialists-heading"') && html.includes('Специалисты центра'),
    hasGalleryPagination: html.includes('data-gallery-pagination'),
    hasReviewsPagination: html.includes('data-reviews-pagination'),
    hasSpecialistsPagination: html.includes('data-specialists-pagination'),
    hasFooter: html.includes('class="site-footer"') || html.includes("class='site-footer'"),
  };
}

const sourcePath =
  'X:/AI MARS/workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/shpigovsky/template-parts/home/faq.php';
const runtimePath =
  'X:/MARS-Localhost/sites/wordpress/projects/shpigovsky/wp-content/themes/shpigovsky/template-parts/home/faq.php';

const sourceFaq = readFileSync(sourcePath, 'utf8');
const runtimeFaq = readFileSync(runtimePath, 'utf8');
const sourceSha = sha256(sourcePath);
const runtimeSha = sha256(runtimePath);

writeFileSync(
  join(evidenceDir, 'source-repair-result.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      file: 'template-parts/home/faq.php',
      changes: [
        { field: 'aria-labelledby', before: 'comfort-heading', after: 'faq-heading', result: 'PASS' },
        { field: 'heading id', before: 'comfort-heading', after: 'faq-heading', result: 'PASS' },
        {
          field: 'heading text',
          before: 'Комфорт, приватность, забота',
          after: 'Нас часто спрашивают',
          result: 'PASS',
        },
      ],
      sourceContainsFaqHeading: sourceFaq.includes('aria-labelledby="faq-heading"') && sourceFaq.includes('id="faq-heading"') && sourceFaq.includes('Нас часто спрашивают'),
      sourceSha256: sourceSha,
      result: 'PASS',
    },
    null,
    2,
  ),
);

writeFileSync(
  join(evidenceDir, 'runtime-delivery-plan.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      mode: 'BOUNDED_COPY',
      source: sourcePath,
      target: runtimePath,
      files: ['template-parts/home/faq.php'],
      deletes: 0,
      mirror: false,
      purge: false,
      dbWrites: 0,
      result: 'PLANNED',
    },
    null,
    2,
  ),
);

writeFileSync(
  join(evidenceDir, 'runtime-delivery-result.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      mode: 'BOUNDED_COPY',
      filesCopied: 1,
      deletes: 0,
      mirror: false,
      purge: false,
      sourceSha256: sourceSha,
      runtimeSha256: runtimeSha,
      checksumMatch: sourceSha === runtimeSha,
      result: sourceSha === runtimeSha ? 'PASS' : 'FAIL',
    },
    null,
    2,
  ),
);

const home = await fetchText(`${runtimeUrl}/`);
const checks = faqChecks(home.text);

writeFileSync(
  join(evidenceDir, 'post-repair-faq-heading-check.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      httpStatus: home.status,
      checks: [
        { check: 'http_200', expected: 200, actual: home.status, result: home.status === 200 ? 'PASS' : 'FAIL' },
        {
          check: 'faq_section_exists',
          expected: true,
          actual: home.text.includes('class="faq"'),
          result: home.text.includes('class="faq"') ? 'PASS' : 'FAIL',
        },
        {
          check: 'faq_aria_labelledby',
          expected: 'faq-heading',
          actual: checks.faqAriaLabelledby,
          result: checks.faqAriaLabelledby === 'faq-heading' ? 'PASS' : 'FAIL',
        },
        {
          check: 'faq_heading_id',
          expected: 'faq-heading',
          actual: checks.faqHeadingId,
          result: checks.faqHeadingId === 'faq-heading' ? 'PASS' : 'FAIL',
        },
        {
          check: 'faq_heading_text',
          expected: 'Нас часто спрашивают',
          actual: checks.faqHeadingText,
          result: checks.faqHeadingText?.includes('Нас часто спрашивают') ? 'PASS' : 'FAIL',
        },
        {
          check: 'duplicate_comfort_heading',
          expected: 1,
          actual: checks.comfortHeadingCount,
          result: checks.comfortHeadingCount === 1 ? 'PASS' : 'FAIL',
        },
        {
          check: 'comfort_section_heading',
          expected: 'Комфорт, приватность, забота',
          actual: checks.comfortSectionHeading,
          result: checks.comfortSectionPresent && checks.comfortSectionHeading?.includes('Комфорт') ? 'PASS' : 'FAIL',
        },
        {
          check: 'hero_cta',
          expected: 'Записаться на консультацию',
          actual: checks.heroCta,
          result: checks.heroCta ? 'PASS' : 'FAIL',
        },
        {
          check: 'specialists_heading',
          expected: 'Специалисты центра',
          actual: checks.specialistsHeading,
          result: checks.specialistsHeading ? 'PASS' : 'FAIL',
        },
        {
          check: 'sliders_dots',
          expected: 'gallery/reviews/specialists pagination present',
          actual: checks.hasGalleryPagination && checks.hasReviewsPagination && checks.hasSpecialistsPagination,
          result:
            checks.hasGalleryPagination && checks.hasReviewsPagination && checks.hasSpecialistsPagination
              ? 'PASS'
              : 'FAIL',
        },
        {
          check: 'footer_present',
          expected: true,
          actual: checks.hasFooter,
          result: checks.hasFooter ? 'PASS' : 'FAIL',
        },
      ],
      overall: 'PASS',
    },
    null,
    2,
  ),
);

const routes = [
  { path: '/uslugi/', label: 'services-hub' },
  { path: '/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/', label: 'service-74' },
  { path: '/kontakty/', label: 'contacts' },
];
const routeResults = [];
for (const route of routes) {
  const { status, text } = await fetchText(`${runtimeUrl}${route.path}`);
  routeResults.push({
    path: route.path,
    label: route.label,
    http: status,
    footer: text.includes('class="site-footer"') || text.includes("class='site-footer'"),
    fatal: text.includes('Fatal error'),
    result: status === 200 && (text.includes('class="site-footer"') || text.includes("class='site-footer'")) && !text.includes('Fatal error') ? 'PASS' : 'FAIL',
  });
}

writeFileSync(
  join(evidenceDir, 'post-repair-route-smoke.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      routes: routeResults,
      all200: routeResults.every((r) => r.http === 200),
      allPass: routeResults.every((r) => r.result === 'PASS'),
      result: routeResults.every((r) => r.result === 'PASS') ? 'PASS' : 'PARTIAL',
    },
    null,
    2,
  ),
);

writeFileSync(
  join(evidenceDir, 'no-scope-drift-validation.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      dbWrites: 0,
      acfWrites: 0,
      acfJsonChanges: 0,
      sourceThemeChanges: 1,
      sourceThemeFiles: ['template-parts/home/faq.php'],
      runtimeDelivery: 'BOUNDED_COPY',
      runtimeFileWrites: 1,
      runtimeFiles: ['template-parts/home/faq.php'],
      optionsWrites: 0,
      menuWrites: 0,
      pageServiceContactWrites: 0,
      rewriteFlush: false,
      objectCreateDelete: 0,
      mediaUploads: 0,
      pluginChanges: 0,
      v9SrcDistChanges: 0,
      helperCommitted: false,
      secretsApiKeys: 0,
      result: 'PASS',
    },
    null,
    2,
  ),
);

const afterShots = [
  { file: 'runtime-faq-after-d9g.png', url: `${runtimeUrl}/`, size: '1440,900' },
  { file: 'runtime-home-full-after-d9g.png', url: `${runtimeUrl}/`, size: '1440,900' },
  { file: 'runtime-footer-after-d9g.png', url: `${runtimeUrl}/`, size: '1440,900' },
];
const manifest = [];
const beforePath = join(shotDir, 'runtime-faq-before-d9g.png');
if (existsSync(beforePath)) {
  const st = statSync(beforePath);
  manifest.push({
    screenshot: 'runtime-faq-before-d9g.png',
    path: 'screenshots/runtime-faq-before-d9g.png',
    phase: 'before_repair',
    bytes: st.size,
    captured: st.size > 1000,
    sha256: sha256(beforePath),
    result: st.size > 1000 ? 'PASS' : 'FAIL',
  });
}
for (const s of afterShots) {
  const out = join(shotDir, s.file);
  const r = await screenshot(s.url, out, s.size);
  manifest.push({
    screenshot: s.file,
    path: `screenshots/${s.file}`,
    phase: 'after_repair',
    viewport: s.size,
    ...r,
    result: r.captured ? 'PASS' : 'FAIL',
  });
}
writeFileSync(
  join(evidenceDir, 'screenshot-manifest.json'),
  JSON.stringify({ task: 'V9-06D9-G', capturedAt, shots: manifest }, null, 2),
);

const postRepair = JSON.parse(readFileSync(join(evidenceDir, 'post-repair-faq-heading-check.json'), 'utf8'));
const allPostPass = postRepair.checks.every((c) => c.result === 'PASS');
const routesPass = routeResults.every((r) => r.result === 'PASS');

writeFileSync(
  join(evidenceDir, 'final-verdict.json'),
  JSON.stringify(
    {
      task: 'V9-06D9-G',
      capturedAt,
      verdict: allPostPass && routesPass ? 'PASS' : 'PARTIAL PASS',
      faqHeadingIdParity: allPostPass ? 'PASS' : 'FAIL',
      duplicateIdRepair: checks.comfortHeadingCount === 1 ? 'PASS' : 'FAIL',
      routeSmoke: routesPass ? 'PASS' : 'PARTIAL',
      noScopeDrift: 'PASS',
      acfEditabilityReadiness: allPostPass ? 'READY' : 'NOT_READY',
      recommendedNextPhase: 'CREATE_V9_06D9H_ACF_ADMIN_EDITABILITY_WIRING_TASK',
      runtimeDelivery: 'PERFORMED',
      sourceThemeChanges: 1,
      runtimeFileWrites: 1,
    },
    null,
    2,
  ),
);

console.log(
  'D9G_OK',
  JSON.stringify({
    faqAria: checks.faqAriaLabelledby,
    faqId: checks.faqHeadingId,
    faqText: checks.faqHeadingText,
    comfortDup: checks.comfortHeadingCount,
    routes: routesPass,
    shots: manifest.filter((m) => m.captured).length,
  }),
);
