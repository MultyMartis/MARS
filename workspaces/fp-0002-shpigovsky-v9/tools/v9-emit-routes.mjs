#!/usr/bin/env node
/**
 * FP-0002 V9 — emit clean-route dist from staging HTML + manifest
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WORKSPACE = path.resolve(__dirname, '..');
const DIST = path.join(WORKSPACE, 'dist');
const STAGING = path.join(DIST, '_html-staging');
const MANIFEST_PATH = path.join(__dirname, 'v9-route-manifest.json');
const EVIDENCE_ROOT = 'X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v9/v9-01-workspace-creation';

function normalizeAssetPaths(content) {
  let out = content;
  out = out.replace(/(\s(?:href|src|content)=["'])assets\//g, '$1/assets/');
  out = out.replace(/(\s(?:href|src|content)=[''])assets\//g, "$1/assets/");
  out = out.replace(/url\(\s*(['"]?)assets\//g, 'url($1/assets/');
  out = out.replace(/url\(\s*(['"]?)\.\.\/fonts\//g, 'url($1/assets/fonts/');
  out = out.replace(/url\(\s*(['"]?)\.\.\/img\//g, 'url($1/assets/img/');
  out = out.replace(/url\(\s*(['"]?)\.\.\/webfonts\//g, 'url($1/assets/webfonts/');
  return out;
}

function normalizeCssFile(cssPath) {
  if (!fs.existsSync(cssPath)) return;
  const raw = fs.readFileSync(cssPath, 'utf8');
  const normalized = normalizeAssetPaths(raw);
  if (normalized !== raw) fs.writeFileSync(cssPath, normalized, 'utf8');
}

function routeToOutputDir(route) {
  if (route === '/') return DIST;
  const clean = route.replace(/^\/|\/$/g, '');
  return path.join(DIST, ...clean.split('/'));
}

function loadManifest() {
  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  const routes = manifest.routes || [];
  const routeSet = new Set();
  const outputSet = new Set();
  for (const entry of routes) {
    if (!entry.published) throw new Error(`Unpublished route in manifest output list: ${entry.route}`);
    if (routeSet.has(entry.route)) throw new Error(`Duplicate route: ${entry.route}`);
    if (outputSet.has(entry.output)) throw new Error(`Duplicate output: ${entry.output}`);
    routeSet.add(entry.route);
    outputSet.add(entry.output);
    const srcPath = path.join(WORKSPACE, entry.source_page.replace(/\//g, path.sep));
    if (!fs.existsSync(srcPath)) throw new Error(`Missing source page: ${entry.source_page}`);
  }
  for (const u of manifest.unpublished_routes || []) {
    if (routes.some((r) => r.route === u.route)) {
      throw new Error(`Unpublished route must not appear in published routes: ${u.route}`);
    }
  }
  if (routes.some((r) => r.route.includes('genotipirovanie'))) {
    throw new Error('Genotyping route must not be published in V9 manifest');
  }
  return manifest;
}

function removeFlatStagingHtml() {
  if (!fs.existsSync(STAGING)) throw new Error(`Missing HTML staging dir: ${STAGING}`);
  function walk(dir) {
    for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, ent.name);
      if (ent.isDirectory()) walk(p);
      else if (ent.name.endsWith('.html')) fs.unlinkSync(p);
    }
  }
  walk(STAGING);
}

function emitRoutes(manifest) {
  const emitted = [];
  for (const entry of manifest.routes) {
    const stagingFile = path.join(STAGING, entry.dist_source.replace(/\//g, path.sep));
    if (!fs.existsSync(stagingFile)) {
      throw new Error(`Missing staging HTML for ${entry.route}: ${stagingFile}`);
    }
    let html = fs.readFileSync(stagingFile, 'utf8');
    html = normalizeAssetPaths(html);
    const outDir = routeToOutputDir(entry.route);
    fs.mkdirSync(outDir, { recursive: true });
    const outFile = path.join(outDir, 'index.html');
    fs.writeFileSync(outFile, html, 'utf8');
    emitted.push({ route: entry.route, file: path.relative(DIST, outFile).replace(/\\/g, '/') });
    console.log(`EMIT ${entry.route} -> ${emitted[emitted.length - 1].file}`);
  }
  return emitted;
}

function sha256File(filePath) {
  const hash = crypto.createHash('sha256');
  hash.update(fs.readFileSync(filePath));
  return hash.digest('hex').toUpperCase();
}

function main() {
  if (!fs.existsSync(STAGING)) {
    throw new Error('Run gulp build first — staging HTML missing');
  }
  const manifest = loadManifest();
  normalizeCssFile(path.join(DIST, 'assets/css/style.css'));
  const emitted = emitRoutes(manifest);
  removeFlatStagingHtml();
  fs.rmSync(STAGING, { recursive: true, force: true });

  const genotypingDist = path.join(DIST, 'uslugi/genotipirovanie/index.html');
  if (fs.existsSync(genotypingDist)) {
    throw new Error('Genotyping must not be emitted to dist');
  }

  const cssHash = sha256File(path.join(DIST, 'assets/css/style.css'));
  const jsHash = sha256File(path.join(DIST, 'assets/js/main.js'));
  const buildLog = {
    timestamp: new Date().toISOString(),
    emitted_count: emitted.length,
    css_sha256: cssHash,
    js_sha256: jsHash,
    routes: emitted,
  };
  const buildEvidence = path.join(EVIDENCE_ROOT, 'build');
  fs.mkdirSync(buildEvidence, { recursive: true });
  fs.writeFileSync(path.join(buildEvidence, 'v9-emit-log.json'), JSON.stringify(buildLog, null, 2));
  console.log(`V9 routes emitted: ${emitted.length}`);
  console.log(`CSS SHA256: ${cssHash}`);
  console.log(`JS SHA256: ${jsHash}`);
}

main();
