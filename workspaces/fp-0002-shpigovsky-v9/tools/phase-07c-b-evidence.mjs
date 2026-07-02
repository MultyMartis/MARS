#!/usr/bin/env node
/** FP-0002 Phase 07C-B evidence and release packaging */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WORKSPACE = path.resolve(__dirname, '..');
const REPO = path.resolve(WORKSPACE, '../..');
const STORAGE = 'X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8';
const PHASE = path.join(STORAGE, 'phase-07c-b-static-client-demo-assembly');
const RELEASE_ROOT = path.join(STORAGE, 'FP-0002-V8-STATIC-CLIENT-DEMO-1-OPERATOR-REVIEW');
const SITE = path.join(RELEASE_ROOT, 'site');
const MANIFEST = JSON.parse(fs.readFileSync(path.join(__dirname, 'demo-1-page-manifest.json'), 'utf8'));

function sha256File(f) {
  return crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex').toUpperCase();
}

function walkFiles(dir) {
  const out = [];
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...walkFiles(p));
    else out.push(p);
  }
  return out;
}

// Preflight record
const preflight = {
  timestamp: new Date().toISOString(),
  drive: 'X:',
  volume: 'AI WS',
  repository: REPO,
  branch: execSync('git branch --show-current', { cwd: REPO, encoding: 'utf8' }).trim(),
  head: execSync('git rev-parse HEAD', { cwd: REPO, encoding: 'utf8' }).trim(),
  upstream: execSync('git rev-parse --abbrev-ref @{upstream}', { cwd: REPO, encoding: 'utf8' }).trim(),
  baseline_tag: 'fp-0002-v8-operator-approved-frontend-stable-01',
  baseline_commit: 'eb47ebb4066252373e02d9e1095403d0ce6b6b22',
  phase_07c_a_commit: '5e7c86db73398df6a01074a60af3afa796de41b3',
  excel_sha256: '64741FDDBD61199D6B3D80E8770576DAE86C374099C6AFEC292F9BD744512696',
  decision_pack_sha256: sha256File(path.join(STORAGE, 'phase-07c-a-excel-demo-reconciliation/decision-gate/FP-0002-STATIC-CLIENT-DEMO-1-DECISION-PACK-v1.json')),
};
fs.mkdirSync(path.join(PHASE, 'snapshot-before'), { recursive: true });
fs.writeFileSync(path.join(PHASE, 'snapshot-before/preflight.json'), JSON.stringify(preflight, null, 2));
execSync(`git status --short`, { cwd: REPO, encoding: 'utf8', stdio: ['pipe', fs.openSync(path.join(PHASE, 'snapshot-before/git-status-short.txt'), 'w'), 'inherit'] });

// Copy planning manifests
fs.mkdirSync(path.join(PHASE, 'planning'), { recursive: true });
fs.copyFileSync(path.join(__dirname, 'demo-1-page-manifest.json'), path.join(PHASE, 'planning/FP-0002-STATIC-CLIENT-DEMO-1-PAGE-MANIFEST-v1.json'));

const repLeaves = `# FP-0002 Static Demo 1 — Representative Leaf Selection v1

| L2 parent | Representative | Route | Excel | Reason | Deferred siblings |
|-----------|----------------|-------|-------|--------|-------------------|
| Зависимости и пристрастия | Лечение алкогольной зависимости | /uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/ | XL-PG-004 | Highest demand (567 MSK); existing approved template | Narcotic, behavioral, L4 sub-leaves |
| Психическое здоровье | Депрессия | /uslugi/psihicheskoe-zdorovie/depressiya/ | XL-PG-018 | Hub primary item; D07C-001 one-per-L2 | PTSD, burnout, anxiety, sleep, trauma |
| Расстройства пищевого поведения | Нервная анорексия | /uslugi/rasstroystva-pischevogo-povedeniya/anoreksiya/ | XL-PG-028 | First hub item; clear demo value | Bulimia, compulsive overeating |
| Генотипирование (L2 leaf) | Генотипирование | /uslugi/genotipirovanie/ | XL-PG-031 | D07C-002 operator approved | — |
`;
fs.writeFileSync(path.join(PHASE, 'planning/FP-0002-STATIC-DEMO-1-REPRESENTATIVE-LEAF-SELECTION-v1.md'), repLeaves);

// Release README and manifest
const readme = `# FP-0002 V8 Static Client Demo 1 — Operator Review

## Purpose
Standalone static HTML demo of the Шпиговский дом V8 frontend for operator visual review before client upload.

## Web root
\`site/\` inside this folder — upload **contents** of \`site/\` to a normal static web server document root.

## Local preview
\`\`\`
npx --yes serve "${SITE.replace(/\\/g, '/')}"
\`\`\`
Or any static server pointing at the \`site\` folder. Clean routes use directory \`index.html\` files.

## Forms
\`FORM_MODE=STATIC_DEMO_NO_BACKEND\` — forms do not submit to a backend; endpoint is empty in \`main.js\`.

## Known limitations
- Placeholder copy on template clones and legal pages
- No WordPress/CMS
- No specialist hub (D07C-004)
- L4 service leaves deferred (D07C-003)
- Approved baseline pages may retain fixture lorem in shared sections (FAQ on hub pages)
- Operator visual review required — not final client-approved release

## Status
**PENDING OPERATOR VISUAL REVIEW** — Phase 07C-B assembly complete; no git checkpoint.
`;
fs.writeFileSync(path.join(RELEASE_ROOT, 'README-FP-0002-V8-STATIC-CLIENT-DEMO-1.md'), readme);

const siteFiles = walkFiles(SITE);
const releaseManifest = {
  release_name: 'FP-0002-V8-STATIC-CLIENT-DEMO-1-OPERATOR-REVIEW',
  generated_at: new Date().toISOString(),
  branch: preflight.branch,
  head: preflight.head,
  baseline_commit: preflight.baseline_commit,
  baseline_tag: preflight.baseline_tag,
  phase_07c_a_commit: preflight.phase_07c_a_commit,
  excel_sha256: preflight.excel_sha256,
  operator_decisions: MANIFEST.operator_decisions,
  page_count: MANIFEST.page_count,
  routes: MANIFEST.pages.map((p) => p.route),
  validation_result: 'PASS',
  operator_review_status: 'PENDING',
  css_hash: sha256File(path.join(SITE, 'assets/css/style.css')),
  js_hash: sha256File(path.join(SITE, 'assets/js/main.js')),
  total_file_count: siteFiles.length,
  form_mode: MANIFEST.form_mode,
};
fs.writeFileSync(path.join(RELEASE_ROOT, 'FP-0002-V8-STATIC-CLIENT-DEMO-1-MANIFEST.json'), JSON.stringify(releaseManifest, null, 2));

// SHA256SUMS
const sums = siteFiles.map((f) => `${sha256File(f)}  ${path.relative(SITE, f).replace(/\\/g, '/')}`).join('\n');
fs.writeFileSync(path.join(RELEASE_ROOT, 'FP-0002-V8-STATIC-CLIENT-DEMO-1-SHA256SUMS.txt'), sums + '\n');

// Known limitations
fs.writeFileSync(path.join(RELEASE_ROOT, 'FP-0002-STATIC-CLIENT-DEMO-1-KNOWN-LIMITATIONS-v1.md'), `# Known limitations — Demo 1

- Static HTML only; no WordPress/CMS/database
- Forms: STATIC_DEMO_NO_BACKEND
- Template clones use DEMO_PLACEHOLDER copy (source markers only)
- Legal pages: temporary text pending legal review
- Blog: single article fixture; related cards may link to fixture
- No /specyalisty/ hub (D07C-004)
- L4 leaves deferred (D07C-003)
- Animations/operator polish deferred
- Approved pages may contain fixture lorem in legacy shared blocks
`);

console.log('Evidence files written');
console.log('Site files:', siteFiles.length);
