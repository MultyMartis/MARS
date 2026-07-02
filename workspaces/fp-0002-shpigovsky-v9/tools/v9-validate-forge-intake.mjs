#!/usr/bin/env node
/**
 * FP-0002 V9-04 — Validate Forge WordPress intake pack consistency
 */
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const INTAKE = join(ROOT, 'forge-intake');
const MANIFESTS = join(INTAKE, 'manifests');

const STABLE_COMMIT = 'a51376872fbfefb7d5f68a58b440c726d6cf3de3';
const STABLE_TAG = 'fp-0002-v9-operator-approved-static-frontend-stable-01';
const REQUIRED_ROUTE_COUNT = 31;
const FORBIDDEN_ROUTES = ['/uslugi/genotipirovanie/'];
const REQUIRED_CONTRACTS = [
  'forms/FP-0002-V9-04-FORMS-AND-MODAL-CONTRACT-v1.md',
  'forms/FP-0002-V9-04-SCROLL-TO-TOP-CONTRACT-v1.md',
  'implementation/FP-0002-V9-04-FRONTEND-RUNTIME-CONTRACT-v1.md',
  'FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md',
];

const errors = [];
const warnings = [];

function err(msg) {
  errors.push(msg);
}
function warn(msg) {
  warnings.push(msg);
}

function loadJson(path) {
  try {
    return JSON.parse(readFileSync(path, 'utf8'));
  } catch (e) {
    err(`JSON parse failed: ${path} — ${e.message}`);
    return null;
  }
}

// Route manifest authority
const v9Manifest = loadJson(join(__dirname, 'v9-route-manifest.json'));
if (!v9Manifest) process.exit(1);

const authorityRoutes = v9Manifest.routes.map((r) => r.route).sort();

// Generated manifests
const routesJson = loadJson(join(MANIFESTS, 'FP-0002-V9-FORGE-ROUTES-v1.json'));
const templatesJson = loadJson(join(MANIFESTS, 'FP-0002-V9-FORGE-TEMPLATES-v1.json'));
const componentsJson = loadJson(join(MANIFESTS, 'FP-0002-V9-FORGE-COMPONENTS-v1.json'));
const fieldsJson = loadJson(join(MANIFESTS, 'FP-0002-V9-FORGE-FIELDS-v1.json'));
const acceptanceJson = loadJson(join(MANIFESTS, 'FP-0002-V9-FORGE-ACCEPTANCE-v1.json'));
const blockersJson = loadJson(join(MANIFESTS, 'FP-0002-V9-FORGE-BLOCKERS-v1.json'));

if (routesJson) {
  if (routesJson.stable_commit !== STABLE_COMMIT) err(`routes manifest stable_commit mismatch`);
  if (routesJson.stable_tag !== STABLE_TAG) err(`routes manifest stable_tag mismatch`);
  const intakeRoutes = routesJson.routes.map((r) => r.route).sort();
  if (intakeRoutes.length !== REQUIRED_ROUTE_COUNT) err(`route count ${intakeRoutes.length} !== ${REQUIRED_ROUTE_COUNT}`);
  for (const r of authorityRoutes) {
    if (!intakeRoutes.includes(r)) err(`missing route in intake: ${r}`);
  }
  for (const r of intakeRoutes) {
    if (!authorityRoutes.includes(r)) err(`extra route in intake: ${r}`);
  }
  for (const r of FORBIDDEN_ROUTES) {
    if (intakeRoutes.includes(r)) err(`forbidden route present: ${r}`);
  }
  const ids = routesJson.routes.map((r) => r.id);
  if (new Set(ids).size !== ids.length) err('duplicate route IDs');
  for (const rec of routesJson.routes) {
    if (!rec.template_id) err(`route ${rec.route} missing template_id`);
    if (!rec.wordpress_object?.type) err(`route ${rec.route} missing wordpress_object`);
  }
}

if (templatesJson && routesJson) {
  const templateIds = new Set(templatesJson.templates.map((t) => t.id));
  for (const rec of routesJson.routes) {
    if (!templateIds.has(rec.template_id)) err(`template ${rec.template_id} not in template map`);
  }
}

if (acceptanceJson && routesJson) {
  if (acceptanceJson.acceptance.length !== routesJson.routes.length) {
    err('acceptance count !== route count');
  }
}

// Required markdown contracts
for (const rel of REQUIRED_CONTRACTS) {
  if (!existsSync(join(INTAKE, rel))) err(`missing contract: ${rel}`);
}

// G6 / preloader authority scan in intake docs only
function scanIntakeDocs(dir) {
  const hits = { g6: [], preloader: [], rejected07cb: [] };
  function walk(d) {
    for (const name of readdirSync(d)) {
      const p = join(d, name);
      const st = statSync(p);
      if (st.isDirectory()) walk(p);
      else if (name.endsWith('.md')) {
        const text = readFileSync(p, 'utf8').toLowerCase();
        if (/\bg6\b/.test(text) && text.includes('data-inf-group') && !text.includes('excluded') && !text.includes('absent') && !text.includes('must not')) {
          hits.g6.push(p);
        }
        if (text.includes('preloader') && !text.includes('no preloader') && !text.includes('not recreate') && !text.includes('none')) {
          hits.preloader.push(p);
        }
        if (text.includes('07c-b') && text.includes('authority') && !text.includes('non-authoritative') && !text.includes('rejected') && !text.includes('superseded')) {
          hits.rejected07cb.push(p);
        }
      }
    }
  }
  if (existsSync(INTAKE)) walk(INTAKE);
  return hits;
}

const scan = scanIntakeDocs(INTAKE);
if (scan.g6.length) warn(`G6 mentions to review: ${scan.g6.length} files`);
if (scan.preloader.length) warn(`preloader mentions to review: ${scan.preloader.length} files`);

// Master pack exists
if (!existsSync(join(INTAKE, 'FP-0002-V9-FORGE-WORDPRESS-INTAKE-PACK-v1.md'))) {
  err('master intake pack missing');
}

console.log('FP-0002 V9 Forge Intake Validator');
console.log('================================');
console.log(`Authority routes: ${authorityRoutes.length}`);
console.log(`Intake routes: ${routesJson?.routes?.length ?? 'N/A'}`);
console.log(`Templates: ${templatesJson?.templates?.length ?? 'N/A'}`);
console.log(`Components: ${componentsJson?.components?.length ?? 'N/A'}`);
console.log(`Field groups: ${fieldsJson?.field_groups?.length ?? 'N/A'}`);
console.log(`Errors: ${errors.length}`);
console.log(`Warnings: ${warnings.length}`);

if (errors.length) {
  errors.forEach((e) => console.error('ERROR:', e));
  process.exit(1);
}
warnings.forEach((w) => console.warn('WARN:', w));
console.log('PASS');
