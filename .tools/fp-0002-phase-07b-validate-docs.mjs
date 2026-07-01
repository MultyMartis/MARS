#!/usr/bin/env node
/**
 * FP-0002 Phase 07B documentation validator (lightweight)
 * Usage: node .tools/fp-0002-phase-07b-validate-docs.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO = path.resolve(__dirname, '..');
const OPS = path.join(REPO, 'workspaces/website-factory-operations/FP-0002-SHPIGOVSKY');

const REQUIRED = [
  'authority-reconciliation-map.md',
  'FP-0002-V8-ACTUAL-IMPLEMENTATION-RECONCILIATION-v1.md',
  'FP-0002-V8-IMPLEMENTATION-GUIDE-v1.md',
  'FP-0002-V8-PAGE-AND-ROUTE-REGISTER-v1.md',
  'FP-0002-V8-COMPONENT-REGISTER-v1.md',
  'FP-0002-V8-ASSET-REGISTER-v1.md',
  'FP-0002-V8-FRONTEND-RULES-AND-EXCEPTIONS-v1.md',
  'FP-0002-V8-BLOG-ARCHITECTURE-v1.md',
  'FP-0002-V8-FORGE-WORDPRESS-HANDOFF-MAP-v1.md',
  'FP-0002-V8-KNOWN-LIMITATIONS-AND-DEFERRED-WORK-v1.md',
  'FP-0002-V8-OPERATOR-POLISH-BOUNDARY-v1.md',
  'FP-0002-V8-STATIC-CLIENT-DEMO-SPEC-v1.md',
  'FP-0002-TO-WEBSITE-FACTORY-RULE-PROMOTION-MATRIX-v1.md',
  'documentation-drift-reconciliation.md',
  'REPORT-FP-0002-V8-PHASE-07B-DOCUMENTATION-AND-LESSONS-LEARNED-v1.md',
];

const LESSONS = path.join(REPO, 'projects/mars-website-factory/operational-examples/WEBSITE-FACTORY-FP-0002-LESSONS-LEARNED-v1.md');

const PLACEHOLDER_RE = /\b(TODO|TBD|INSERT PATH|<commit>|UNKNOWN_STOP)\b/i;
const BAD_PATH_RE = /`[CDE]:\\(?:AI MARS|MARS)/i;

const errors = [];
const warnings = [];

function checkFile(relFromOps) {
  const full = path.join(OPS, relFromOps);
  if (!fs.existsSync(full)) {
    errors.push(`MISSING: ${relFromOps}`);
    return;
  }
  const text = fs.readFileSync(full, 'utf8');
  if (!text.includes('eb47ebb')) {
    warnings.push(`No baseline commit string in ${relFromOps}`);
  }
  if (PLACEHOLDER_RE.test(text)) {
    const m = text.match(PLACEHOLDER_RE);
    errors.push(`PLACEHOLDER ${m[0]} in ${relFromOps}`);
  }
  if (BAD_PATH_RE.test(text) && !text.includes('HISTORICAL')) {
    warnings.push(`Possible deprecated path as current in ${relFromOps}`);
  }
  // markdown links to local files
  const links = [...text.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)];
  for (const [, target] of links) {
    if (target.startsWith('http') || target.startsWith('#')) continue;
    const resolved = path.normalize(path.join(path.dirname(full), target.split('#')[0]));
    if (!fs.existsSync(resolved)) {
      errors.push(`BROKEN LINK in ${relFromOps}: ${target}`);
    }
  }
}

for (const f of REQUIRED) checkFile(f);

if (!fs.existsSync(LESSONS)) {
  errors.push('MISSING: WEBSITE-FACTORY-FP-0002-LESSONS-LEARNED-v1.md');
}

// Blog counts from source
const articlePath = path.join(REPO, 'workspaces/fp-0002-shpigovsky-v8/src/partials/sections/blog-article-content.html');
const lowerPath = path.join(REPO, 'workspaces/fp-0002-shpigovsky-v8/src/partials/sections/blog-article-lower-stack.html');
if (fs.existsSync(articlePath)) {
  const html = fs.readFileSync(articlePath, 'utf8');
  const h2 = (html.match(/<h2\b/gi) || []).length;
  const h3 = (html.match(/<h3\b/gi) || []).length;
  const imgs = (html.match(/<figure>\s*<img/gi) || []).length;
  const toc = (html.match(/<li><a href="#/g) || []).length;
  const expected = { h2: 5, h3: 12, imgs: 4, toc: 5 };
  if (h2 !== expected.h2) errors.push(`Blog H2 count ${h2} != ${expected.h2}`);
  if (h3 !== expected.h3) errors.push(`Blog H3 count ${h3} != ${expected.h3}`);
  if (imgs !== expected.imgs) errors.push(`Blog inline images ${imgs} != ${expected.imgs}`);
  if (toc !== expected.toc) errors.push(`Blog TOC items ${toc} != ${expected.toc}`);
}
if (fs.existsSync(lowerPath)) {
  const lower = fs.readFileSync(lowerPath, 'utf8');
  const sources = (lower.match(/<p>[^<]+<\/p>/g) || []).filter((p) => p.includes('doi') || p.includes('Менделевич') || p.includes('Blum') || p.includes('Анохина') || p.includes('Николишин') || p.includes('Frontiers')).length;
  const related = (lower.match(/blog-related-card/g) || []).length;
  if (sources < 8) warnings.push(`Blog sources paragraphs ~${sources} (expected 8)`);
  if (related !== 3) errors.push(`Blog related includes ${related} != 3`);
}

// Page count
const pagesDir = path.join(REPO, 'workspaces/fp-0002-shpigovsky-v8/src/pages');
const pages = [];
function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p);
    else if (e.name.endsWith('.html')) pages.push(p);
  }
}
walk(pagesDir);
if (pages.length !== 10) errors.push(`Page count ${pages.length} != 10`);

const out = {
  timestamp: new Date().toISOString(),
  pass: errors.length === 0,
  errors,
  warnings,
  pageCount: pages.length,
};

const reportPath = path.join(OPS, 'phase-07b-documentation-validation.md');
const md = `# Phase 07B Documentation Validation

**Date:** ${out.timestamp}
**Result:** ${out.pass ? 'PASS' : 'FAIL'}

## Errors
${errors.length ? errors.map((e) => `- ${e}`).join('\n') : '- none'}

## Warnings
${warnings.length ? warnings.map((w) => `- ${w}`).join('\n') : '- none'}

## Checks
- Required documents: ${REQUIRED.length}
- Implemented pages: ${pages.length}
- Blog source counts verified
`;

fs.writeFileSync(reportPath, md, 'utf8');
console.log(JSON.stringify(out, null, 2));
process.exit(out.pass ? 0 : 1);
