'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const { WORKSPACE_ROOT, ensureFinalRegistries } = require('./registry-loader');
const { validateRegistry, validateGeneratedHtml } = require('./validation');
const { applyTemplateInstance } = require('./template-renderer');
const { renderPlaceholderPage } = require('./placeholder-renderer');
const { rewriteAssetPathsToRoot, normalizeTypoUrlsInHtml } = require('./path-utils');
const { buildPageIndexes } = require('./navigation-loader');
const { applyNavigationRewrites } = require('./link-rewriter');
const { writePass3NavigationRegistry } = require('./build-navigation-registry');
const { writePass3Evidence } = require('./pass-3-evidence');
const { crawlGeneratedSite } = require('./link-validator');
const { renderLegacyGenotipirovanieAlias } = require('./legacy-alias-renderer');

const DIST_DIR = path.join(WORKSPACE_ROOT, 'dist');
const EVIDENCE_DIR = path.join(WORKSPACE_ROOT, 'plans/static-client-demo/evidence');

const TEMPLATE_SOURCES = {
  SERVICES_HUB_INTERNAL_PAGE: 'uslugi-v2.html',
  SERVICE_SUBDIVISION_INTERNAL_PAGE: 'usluga-podrazdel-v1.html',
  SERVICE_LEAF_INTERNAL_PAGE: 'usluga-konechnaya-v1.html',
};

function readDistTemplate(fileName) {
  const filePath = path.join(DIST_DIR, fileName);
  if (!fs.existsSync(filePath)) {
    throw new Error(`Compiled template missing: ${filePath}. Run gulp build first.`);
  }
  return fs.readFileSync(filePath, 'utf8');
}

function writeOutput(page, html, indexes) {
  const outputRelative = page.output;
  let processed = applyNavigationRewrites(html, page, indexes);
  processed = normalizeTypoUrlsInHtml(rewriteAssetPathsToRoot(processed, outputRelative));
  const outputPath = path.join(DIST_DIR, outputRelative);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, processed, 'utf8');
  return outputPath;
}

function sha256File(filePath) {
  const data = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(data).digest('hex');
}

function generatePages(registry, indexes) {
  const templateCache = {};
  const shellHtml = readDistTemplate('uslugi-v2.html');
  const results = [];
  const skipped = [];

  registry.pages.forEach((page) => {
    if (page.template === 'HOME_PAGE_TEMPLATE') {
      const homePath = path.join(DIST_DIR, 'index.html');
      if (!fs.existsSync(homePath)) {
        throw new Error('Home output missing after gulp build');
      }
      writeOutput(page, fs.readFileSync(homePath, 'utf8'), indexes);
      skipped.push({ id: page.id, reason: 'canonical_home_from_gulp_with_pass3_nav' });
      results.push({ id: page.id, output: page.output, mode: 'home_nav_wired' });
      return;
    }

    let html;
    if (page.template === 'PLACEHOLDER_PAGE') {
      html = renderPlaceholderPage(shellHtml, page);
    } else {
      const sourceFile = TEMPLATE_SOURCES[page.template];
      if (!sourceFile) {
        throw new Error(`No template source for ${page.template}`);
      }
      if (!templateCache[sourceFile]) {
        templateCache[sourceFile] = readDistTemplate(sourceFile);
      }
      html = applyTemplateInstance(templateCache[sourceFile], page);
    }

    const outputPath = writeOutput(page, html, indexes);
    results.push({ id: page.id, output: page.output, outputPath, mode: 'generated' });
  });

  return { results, skipped };
}

function generateLegacyAliases() {
  const outputPath = path.join(DIST_DIR, 'genotipirovanie/index.html');
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  fs.writeFileSync(outputPath, renderLegacyGenotipirovanieAlias(), 'utf8');
  return outputPath;
}

function validateOutputs(registry) {
  const pageErrors = [];
  registry.pages.forEach((page) => {
    const outputPath = path.join(DIST_DIR, page.output);
    if (!fs.existsSync(outputPath)) {
      pageErrors.push({ id: page.id, errors: ['Missing output file'] });
      return;
    }
    const stat = fs.statSync(outputPath);
    if (stat.size === 0) {
      pageErrors.push({ id: page.id, errors: ['Empty output file'] });
      return;
    }
    const html = fs.readFileSync(outputPath, 'utf8');
    const errors = validateGeneratedHtml(html, page);
    if (errors.length) {
      pageErrors.push({ id: page.id, errors });
    }
  });
  return pageErrors;
}

function writeReceipt({ registry, registryValidation, generation, durationMs, command, navigation }) {
  fs.mkdirSync(EVIDENCE_DIR, { recursive: true });

  const registryHash = crypto
    .createHash('sha256')
    .update(fs.readFileSync(path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-page-registry.json')))
    .digest('hex');

  const templateHashesBefore = fs.existsSync(
    path.join(EVIDENCE_DIR, 'PASS-2-CANONICAL-TEMPLATE-HASHES-BEFORE.txt')
  )
    ? fs.readFileSync(path.join(EVIDENCE_DIR, 'PASS-2-CANONICAL-TEMPLATE-HASHES-BEFORE.txt'), 'utf8')
    : '';

  const canonicalFiles = [
    'src/pages/index.html',
    'src/pages/uslugi-v2.html',
    'src/pages/usluga-podrazdel-v1.html',
    'src/pages/usluga-konechnaya-v1.html',
  ];
  const templateHashesAfter = canonicalFiles.map((rel) => {
    const abs = path.join(WORKSPACE_ROOT, rel);
    return { file: rel, sha256: sha256File(abs) };
  });

  const outputErrors = validateOutputs(registry);
  const indexes = buildPageIndexes(registry);
  const crawl = crawlGeneratedSite({ distDir: DIST_DIR, registry, indexes });

  const receipt = {
    timestamp: new Date().toISOString(),
    pass: 'PASS-3',
    source_commit: '1d9e5dfb',
    stable_baseline_tag: 'fp-0002-v7-four-template-canonical-demo-baseline-01',
    registry_sha256: registryHash,
    navigation_link_count: navigation.links.length,
    generated_page_count: registry.pages.length,
    counts_by_template: registryValidation.counts,
    placeholder_count: registryValidation.counts.PLACEHOLDER_PAGE || 0,
    output_paths: registry.pages.map((p) => p.output),
    skipped_pages: generation.skipped,
    validation_errors: [...registryValidation.errors, ...outputErrors],
    link_crawl_stats: crawl.stats,
    template_hashes_before: templateHashesBefore.trim(),
    template_hashes_after: templateHashesAfter,
    duration_ms: durationMs,
    command,
  };

  fs.writeFileSync(
    path.join(EVIDENCE_DIR, 'PASS-2-GENERATION-RECEIPT.json'),
    `${JSON.stringify(receipt, null, 2)}\n`,
    'utf8'
  );

  const md = `# PASS 3 Generation Receipt

- Timestamp: ${receipt.timestamp}
- Registry SHA-256: \`${registryHash}\`
- Generated pages: ${receipt.generated_page_count}
- Navigation links: ${receipt.navigation_link_count}
- Placeholder pages: ${receipt.placeholder_count}
- Duration: ${durationMs}ms
- Command: \`${command}\`
- Validation errors: ${receipt.validation_errors.length}
- Internal 404: ${crawl.stats.internal404}
- Client-facing hash links: ${crawl.stats.clientFacingHash}

## Template counts

${Object.entries(registryValidation.counts)
  .map(([k, v]) => `- ${k}: ${v}`)
  .join('\n')}
`;
  fs.writeFileSync(path.join(EVIDENCE_DIR, 'PASS-2-GENERATION-RECEIPT.md'), md, 'utf8');

  const afterHashLines = [
    '# FP-0002 PASS 3 — Canonical template SHA-256 (after)',
    '',
    ...templateHashesAfter.map((item) => `${item.sha256}  ${item.file}`),
  ];
  fs.writeFileSync(
    path.join(EVIDENCE_DIR, 'PASS-2-CANONICAL-TEMPLATE-HASHES-AFTER.txt'),
    `${afterHashLines.join('\n')}\n`,
    'utf8'
  );

  return receipt;
}

function main() {
  const started = Date.now();
  const { registry } = ensureFinalRegistries();
  const navigation = writePass3NavigationRegistry(registry);
  const indexes = buildPageIndexes(registry);

  const registryValidation = validateRegistry(registry);
  if (!registryValidation.valid) {
    console.error('Registry validation failed:');
    registryValidation.errors.forEach((err) => console.error(` - ${err}`));
    process.exit(1);
  }

  const generation = generatePages(registry, indexes);
  generateLegacyAliases();
  const receipt = writeReceipt({
    registry,
    registryValidation,
    generation,
    durationMs: Date.now() - started,
    command: 'npm run build:demo',
    navigation,
  });

  const pass3Receipt = writePass3Evidence({
    registry,
    navigation,
    receipt,
    durationMs: Date.now() - started,
  });

  if (receipt.validation_errors.length) {
    console.error('Output validation errors:', receipt.validation_errors.length);
    receipt.validation_errors.slice(0, 10).forEach((err) => console.error(JSON.stringify(err)));
    process.exit(1);
  }

  if (pass3Receipt.result !== 'PASS') {
    console.error('PASS 3 link validation failed:', pass3Receipt);
    process.exit(1);
  }

  console.log(
    `FP-0002 static demo generator PASS 3: ${registry.pages.length} pages, ${navigation.links.length} nav links`
  );
}

if (require.main === module) {
  main();
}

module.exports = {
  generatePages,
  validateOutputs,
  writeReceipt,
  main,
};
