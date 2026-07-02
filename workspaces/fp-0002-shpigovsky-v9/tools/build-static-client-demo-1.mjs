#!/usr/bin/env node
/**
 * FP-0002 Phase 07C-B — static client Demo 1 packaging + validation
 * Task-scoped; only writes to approved Storage release roots.
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import http from 'node:http';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const WORKSPACE = path.resolve(__dirname, '..');
const MANIFEST_PATH = path.join(__dirname, 'demo-1-page-manifest.json');
const DIST = path.join(WORKSPACE, 'dist');
const STORAGE_ROOT = 'X:/AI MARS STORAGE/website-factory/fp-0002-shpigovsky-v8';
const RELEASE_WEB = path.join(STORAGE_ROOT, 'FP-0002-V8-STATIC-CLIENT-DEMO-1-OPERATOR-REVIEW', 'site');
const DEMO_BUILD = path.join(STORAGE_ROOT, 'phase-07c-b-static-client-demo-assembly', 'demo-build');
const EVIDENCE_BUILD = path.join(STORAGE_ROOT, 'phase-07c-b-static-client-demo-assembly', 'build');

function assertStoragePath(target) {
  const normalized = path.resolve(target).replace(/\\/g, '/').toLowerCase();
  const allowed = path.resolve(STORAGE_ROOT).replace(/\\/g, '/').toLowerCase();
  if (!normalized.startsWith(allowed)) {
    throw new Error(`Refusing path outside Storage root: ${target}`);
  }
}

function sha256File(filePath) {
  const hash = crypto.createHash('sha256');
  hash.update(fs.readFileSync(filePath));
  return hash.digest('hex').toUpperCase();
}

function sha256DirSummary(dir) {
  const files = [];
  function walk(d) {
    for (const ent of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, ent.name);
      if (ent.isDirectory()) walk(p);
      else files.push(p);
    }
  }
  walk(dir);
  files.sort();
  const h = crypto.createHash('sha256');
  for (const f of files) {
    h.update(path.relative(dir, f).replace(/\\/g, '/'));
    h.update(sha256File(f));
  }
  return h.digest('hex').toUpperCase();
}

function copyDir(src, dest, filter) {
  fs.mkdirSync(dest, { recursive: true });
  for (const ent of fs.readdirSync(src, { withFileTypes: true })) {
    const s = path.join(src, ent.name);
    const d = path.join(dest, ent.name);
    if (ent.isDirectory()) {
      copyDir(s, d, filter);
    } else if (!filter || filter(s)) {
      fs.mkdirSync(path.dirname(d), { recursive: true });
      fs.copyFileSync(s, d);
    }
  }
}

function routeToDir(route) {
  if (route === '/') return '';
  const clean = route.replace(/^\/|\/$/g, '');
  return clean;
}

function rewriteHtmlLinks(html, routePrefix) {
  let out = html;
  // depth from route segments for relative asset paths when needed — assets stay root-relative
  const linkFixes = [
    [/href="\/uslugi-v2\.html"/g, 'href="/uslugi/"'],
    [/href="\/usluga-podrazdel-v1\.html"/g, 'href="/uslugi/zavisimosti/"'],
    [/href="\/usluga-konechnaya-v1\.html"/g, 'href="/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/"'],
    [/href="\/o-centre\.html"/g, 'href="/o-centre/"'],
    [/href="\/kontakty\.html"/g, 'href="/kontakty/"'],
    [/href="\/otzyvy\.html"/g, 'href="/otzyvy/"'],
    [/href="\/blog\.html"/g, 'href="/blog/"'],
    [/href="\/index\.html"/g, 'href="/"'],
  ];
  for (const [re, rep] of linkFixes) out = out.replace(re, rep);
  return out;
}

function packageDemo(manifest) {
  assertStoragePath(RELEASE_WEB);
  assertStoragePath(DEMO_BUILD);
  if (fs.existsSync(RELEASE_WEB)) {
    fs.rmSync(RELEASE_WEB, { recursive: true, force: true });
  }
  if (fs.existsSync(DEMO_BUILD)) {
    fs.rmSync(DEMO_BUILD, { recursive: true, force: true });
  }
  fs.mkdirSync(RELEASE_WEB, { recursive: true });
  fs.mkdirSync(DEMO_BUILD, { recursive: true });

  const emitted = [];
  const routes = new Set();

  // Copy shared assets once
  for (const dir of ['assets']) {
    const src = path.join(DIST, dir);
    if (fs.existsSync(src)) {
      copyDir(src, path.join(RELEASE_WEB, dir));
      copyDir(src, path.join(DEMO_BUILD, dir));
    }
  }

  for (const page of manifest.pages) {
    const srcFile = path.join(DIST, page.dist_source.replace(/\//g, path.sep));
    if (!fs.existsSync(srcFile)) {
      throw new Error(`Missing dist page for manifest route ${page.route}: ${srcFile}`);
    }
    if (routes.has(page.route)) {
      throw new Error(`Duplicate route: ${page.route}`);
    }
    routes.add(page.route);

    const dirPart = routeToDir(page.route);
    const outDir = dirPart ? path.join(RELEASE_WEB, dirPart) : RELEASE_WEB;
    const outDemo = dirPart ? path.join(DEMO_BUILD, dirPart) : DEMO_BUILD;
    fs.mkdirSync(outDir, { recursive: true });
    fs.mkdirSync(outDemo, { recursive: true });

    let html = fs.readFileSync(srcFile, 'utf8');
    html = rewriteHtmlLinks(html, page.route);
    const outFile = path.join(outDir, 'index.html');
    const outFileDemo = path.join(outDemo, 'index.html');
    fs.writeFileSync(outFile, html, 'utf8');
    fs.writeFileSync(outFileDemo, html, 'utf8');
    emitted.push({ route: page.route, file: outFile });
    console.log(`EMIT ${page.route} -> ${path.relative(RELEASE_WEB, outFile)}`);
  }

  const log = { emitted, timestamp: new Date().toISOString(), page_count: emitted.length };
  fs.mkdirSync(EVIDENCE_BUILD, { recursive: true });
  fs.writeFileSync(path.join(EVIDENCE_BUILD, 'packaging-log.json'), JSON.stringify(log, null, 2));
  return { emitted, routes: [...routes] };
}

function crawlLinks(html, baseRoute) {
  const links = [];
  const re = /href="([^"]+)"/g;
  let m;
  while ((m = re.exec(html))) links.push(m[1]);
  return links;
}

function validateDemo(manifest) {
  const issues = [];
  const internalRoutes = new Set(manifest.pages.map((p) => p.route));
  const deferred = new Set(manifest.deferred_routes || []);
    const forbidden = [/DEMO_PLACEHOLDER/i, /\bTODO\b/, /\bTBD\b/, /\bMARS\b/, /Website Factory/i, /Phase 07C/i];
    const loremCheck = /lorem ipsum/i;
    const approvedUnchanged = new Set(
      manifest.pages.filter((p) => p.regression === 'OPERATOR_APPROVED_UNCHANGED').map((p) => p.route)
    );

  for (const page of manifest.pages) {
    const dirPart = routeToDir(page.route);
    const htmlPath = path.join(RELEASE_WEB, dirPart, 'index.html');
    if (!fs.existsSync(htmlPath)) {
      issues.push(`MISSING ${page.route}`);
      continue;
    }
    const html = fs.readFileSync(htmlPath, 'utf8');
    const h1s = (html.match(/<h1\b/gi) || []).length;
    if (h1s !== 1) issues.push(`${page.route}: h1 count ${h1s}`);
    for (const f of forbidden) {
      if (f.test(html.replace(/<!--[\s\S]*?-->/g, '').replace(/data-content-status="[^"]*"/g, ''))) {
        issues.push(`${page.route}: forbidden visible text ${f}`);
      }
    }
    if (!approvedUnchanged.has(page.route) && loremCheck.test(html.replace(/<!--[\s\S]*?-->/g, ''))) {
      issues.push(`${page.route}: lorem ipsum on non-approved clone`);
    }
    if (/\/specyalisty\//.test(html) && page.route !== '/specyalisty/') {
      // allow only if link removed — flag if present
      if (html.includes('href="/specyalisty/"')) issues.push(`${page.route}: specialist link present`);
    }
    for (const href of crawlLinks(html, page.route)) {
      if (href.startsWith('http') || href.startsWith('tel:') || href.startsWith('mailto:') || href.startsWith('#')) continue;
      if (href.includes('.html') && !href.includes('/assets/')) {
        issues.push(`${page.route}: raw html link ${href}`);
      }
      if (href.startsWith('/')) {
        const normalized = href.endsWith('/') ? href : href.replace(/[^/]+$/, (x) => (x.includes('.') ? x : x + '/'));
        const routeKey = normalized.endsWith('/') ? normalized : normalized + '/';
        if (deferred.has(routeKey) || deferred.has(href)) {
          issues.push(`${page.route}: deferred link ${href}`);
        }
        if (href.startsWith('/') && !href.startsWith('//') && !internalRoutes.has(routeKey) && !internalRoutes.has(href + (href.endsWith('/') ? '' : '/'))) {
          // allow asset paths
          if (!href.startsWith('/assets/')) {
            const testRoute = href.endsWith('/') ? href : path.posix.dirname(href + '/').replace(/\/$/, '') + '/';
            if (![...internalRoutes].some((r) => href === r || href + '/' === r || href === r.replace(/\/$/, ''))) {
              if (!href.match(/^\/assets\//) && !href.match(/^\/uslugi\/$/) && href !== '/') {
                // strict: must resolve to manifest route prefix
                const match = [...internalRoutes].find((r) => href === r || href + '/' === r || r.startsWith(href));
                if (!match && !href.includes('cdn.jsdelivr')) issues.push(`${page.route}: unresolved internal ${href}`);
              }
            }
          }
        }
      }
    }
  }

  return issues;
}

function serveAndSmoke(port, manifest) {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      let urlPath = req.url.split('?')[0];
      if (urlPath.endsWith('/')) urlPath += 'index.html';
      if (urlPath === '/') urlPath = '/index.html';
      const filePath = path.join(RELEASE_WEB, urlPath.replace(/^\//, '').split('/').join(path.sep));
      if (!filePath.startsWith(RELEASE_WEB)) {
        res.writeHead(403);
        res.end();
        return;
      }
      if (!fs.existsSync(filePath)) {
        res.writeHead(404);
        res.end('Not found');
        return;
      }
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(fs.readFileSync(filePath));
    });
    server.listen(port, '127.0.0.1', async () => {
      const results = [];
      for (const page of manifest.pages) {
        const url = `http://127.0.0.1:${port}${page.route}`;
        try {
          const r = await fetch(url);
          results.push({ route: page.route, status: r.status, ok: r.status === 200 });
        } catch (e) {
          results.push({ route: page.route, status: 0, ok: false, error: String(e) });
        }
      }
      server.close();
      resolve({ port, pid: process.pid, results });
    });
    server.on('error', reject);
  });
}

async function main() {
  const manifest = JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8'));
  if (!fs.existsSync(DIST)) {
    console.error('dist/ missing — run npm run build first');
    process.exit(1);
  }
  const { emitted } = packageDemo(manifest);
  const issues = validateDemo(manifest);
  const port = 18742;
  const smoke = await serveAndSmoke(port, manifest);
  const failedSmoke = smoke.results.filter((r) => !r.ok);
  if (failedSmoke.length) issues.push(...failedSmoke.map((r) => `HTTP ${r.route} ${r.status}`));

  const summary = {
    packaged_pages: emitted.length,
    validation_issues: issues,
    smoke,
    css_hash: fs.existsSync(path.join(RELEASE_WEB, 'assets/css/style.css')) ? sha256File(path.join(RELEASE_WEB, 'assets/css/style.css')) : null,
    js_hash: fs.existsSync(path.join(RELEASE_WEB, 'assets/js/main.js')) ? sha256File(path.join(RELEASE_WEB, 'assets/js/main.js')) : null,
    site_hash: sha256DirSummary(RELEASE_WEB),
  };
  fs.writeFileSync(path.join(EVIDENCE_BUILD, 'validation-summary.json'), JSON.stringify(summary, null, 2));
  console.log(JSON.stringify(summary, null, 2));
  if (issues.length) {
    console.error('VALIDATION FAILED', issues);
    process.exit(2);
  }
  console.log('PACKAGING OK');
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
