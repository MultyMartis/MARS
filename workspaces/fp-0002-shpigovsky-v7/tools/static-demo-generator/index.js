'use strict';

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const { WORKSPACE_ROOT, ensureFinalRegistries } = require('./registry-loader');
const { validateRegistry, validateGeneratedHtml } = require('./validation');
const { applyTemplateInstance } = require('./template-renderer');
const { renderPlaceholderPage } = require('./placeholder-renderer');
const { rewriteAssetPathsToRoot, normalizeTypoUrlsInHtml } = require('./path-utils');

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

function writeOutput(page, html) {
  const outputRelative = page.output;
  const outputPath = path.join(DIST_DIR, outputRelative);
  fs.mkdirSync(path.dirname(outputPath), { recursive: true });
  const finalHtml = normalizeTypoUrlsInHtml(rewriteAssetPathsToRoot(html, outputRelative));
  fs.writeFileSync(outputPath, finalHtml, 'utf8');
  return outputPath;
}

function sha256File(filePath) {
  const data = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(data).digest('hex');
}

function generatePages(registry) {
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
      const homeHtml = normalizeTypoUrlsInHtml(fs.readFileSync(homePath, 'utf8'));
      fs.writeFileSync(homePath, homeHtml, 'utf8');
      skipped.push({ id: page.id, reason: 'canonical_home_from_gulp' });
      results.push({ id: page.id, output: page.output, mode: 'skipped_home' });
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

    const outputPath = writeOutput(page, html);
    results.push({ id: page.id, output: page.output, outputPath, mode: 'generated' });
  });

  return { results, skipped };
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

function writeReceipt({ registry, registryValidation, generation, durationMs, command }) {
  fs.mkdirSync(EVIDENCE_DIR, { recursive: true });

  const registryHash = crypto
    .createHash('sha256')
    .update(fs.readFileSync(path.join(WORKSPACE_ROOT, 'src/data/static-demo/demo-page-registry.json')))
    .digest('hex');

  const templateHashesBefore = fs.readFileSync(
    path.join(EVIDENCE_DIR, 'PASS-2-CANONICAL-TEMPLATE-HASHES-BEFORE.txt'),
    'utf8'
  );

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

  const receipt = {
    timestamp: new Date().toISOString(),
    source_commit: '797dab58',
    stable_baseline_tag: 'fp-0002-v7-four-template-canonical-demo-baseline-01',
    registry_sha256: registryHash,
    generated_page_count: registry.pages.length,
    counts_by_template: registryValidation.counts,
    placeholder_count: registryValidation.counts.PLACEHOLDER_PAGE || 0,
    output_paths: registry.pages.map((p) => p.output),
    skipped_pages: generation.skipped,
    validation_errors: [...registryValidation.errors, ...outputErrors],
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

  const md = `# PASS 2 Generation Receipt

- Timestamp: ${receipt.timestamp}
- Registry SHA-256: \`${registryHash}\`
- Generated pages: ${receipt.generated_page_count}
- Placeholder pages: ${receipt.placeholder_count}
- Duration: ${durationMs}ms
- Command: \`${command}\`
- Validation errors: ${receipt.validation_errors.length}

## Template counts

${Object.entries(registryValidation.counts)
  .map(([k, v]) => `- ${k}: ${v}`)
  .join('\n')}
`;
  fs.writeFileSync(path.join(EVIDENCE_DIR, 'PASS-2-GENERATION-RECEIPT.md'), md, 'utf8');

  const afterHashLines = [
    '# FP-0002 PASS 2 — Canonical template SHA-256 (after)',
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
  const command = process.argv[1].includes('index.js') ? 'node tools/static-demo-generator/index.js' : process.argv.join(' ');

  const { registry } = ensureFinalRegistries();
  const registryValidation = validateRegistry(registry);
  if (!registryValidation.valid) {
    console.error('Registry validation failed:');
    registryValidation.errors.forEach((err) => console.error(` - ${err}`));
    process.exit(1);
  }

  const generation = generatePages(registry);
  const receipt = writeReceipt({
    registry,
    registryValidation,
    generation,
    durationMs: Date.now() - started,
    command: 'npm run build:demo',
  });

  if (receipt.validation_errors.length) {
    console.error('Output validation errors:', receipt.validation_errors.length);
    receipt.validation_errors.slice(0, 10).forEach((err) => console.error(JSON.stringify(err)));
    process.exit(1);
  }

  console.log(`FP-0002 static demo generator: ${registry.pages.length} pages, ${generation.results.length} processed`);
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
