#!/usr/bin/env node
/**
 * Prepare operator-assisted capture bundle folder with metadata template.
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadJson, writeJson, sha256File } from '../lib/utils.mjs';
import { hashAssistedManifestBody } from '../lib/assisted-capture-validator.mjs';
import {
  RAW_FIREFOX_MANIFEST,
  NORMALIZED_MANIFEST,
  CANONICAL_MANIFEST,
  writeNormalizedBundleManifests,
  resolveBundleHtmlRef,
} from '../lib/assisted-manifest-normalizer.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 2; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--bundle') args.bundle = argv[++i];
    if (a === '--finalize') args.finalize = true;
    if (a === '--manifest') args.manifest = argv[++i];
    if (a === '--query-id') args.queryId = argv[++i];
    if (a === '--query') args.query = argv[++i];
    if (a === '--session') args.sessionId = argv[++i];
  }
  return args;
}

function attachChecksums(manifest, bundleDir) {
  const screenshotPath = path.join(bundleDir, manifest.files?.screenshot || 'screenshot.png');
  const htmlName = resolveBundleHtmlRef(bundleDir, manifest);
  const htmlPath = path.join(bundleDir, htmlName);
  manifest.files = { ...manifest.files, html: htmlName };
  manifest.checksums = {
    screenshot_sha256: fs.existsSync(screenshotPath) ? sha256File(screenshotPath) : null,
    html_sha256: fs.existsSync(htmlPath) ? sha256File(htmlPath) : null,
    manifest_sha256: hashAssistedManifestBody(manifest),
  };
  return manifest;
}

function main() {
  const args = parseArgs(process.argv);
  const bundleDir = path.resolve(
    args.bundle ||
      `C:/AI MARS STORAGE/incoming/mig/live-validation/w2-2-assisted/incoming/${args.queryId || 'bundle-pending'}`,
  );

  fs.mkdirSync(bundleDir, { recursive: true });
  const manifestPath = path.join(bundleDir, CANONICAL_MANIFEST);

  if (!args.finalize) {
    const template = {
      schema_version: '1.0.0',
      acquisition_mode: 'OPERATOR-ASSISTED LIVE SERP CAPTURE',
      project_id: 'MIG-W2-3-TECH-PAID-SERP',
      session_id: args.sessionId || 'w2-3-assisted-session-001',
      query_id: args.queryId || 'w2-3-q02',
      query: args.query || 'ремонт квартир под ключ',
      captured_at: null,
      timezone: 'Europe/Moscow',
      region: 'Москва',
      region_lr: 213,
      device_browser: null,
      page_url: null,
      page_title: null,
      files: { screenshot: 'screenshot.png', html: 'page.html' },
      operator_attestation: {
        attested: false,
        attested_at: null,
        statement: 'I observed this page live in an interactive browser session.',
      },
      production_authority: false,
      technical_test_only: true,
      operator_instructions: [
        '1. Open Yandex in normal browser; verify Москва region.',
        '2. Run query during approved business-hours window.',
        '3. Save screenshot.png and page.html or page.htm into this folder.',
        '4. Run Firefox snippet or fill manifest; set operator_attestation.attested=true.',
        '5. Re-run with --finalize to normalize IDs and compute checksums.',
      ],
    };
    writeJson(manifestPath, template);
    fs.writeFileSync(path.join(bundleDir, 'OPERATOR-INSTRUCTIONS.txt'), template.operator_instructions.join('\n'), 'utf8');
    console.log(JSON.stringify({ status: 'BUNDLE PREPARED', bundle_dir: bundleDir, manifest: manifestPath }, null, 2));
    return;
  }

  let manifest;
  const explicitManifest = args.manifest ? path.resolve(args.manifest) : null;
  if (explicitManifest && fs.existsSync(explicitManifest)) {
    manifest = loadJson(explicitManifest);
    writeJson(path.join(bundleDir, CANONICAL_MANIFEST), manifest);
  } else if (fs.existsSync(path.join(bundleDir, RAW_FIREFOX_MANIFEST))) {
    const { manifest: normalized } = writeNormalizedBundleManifests(bundleDir, { syncCanonical: true });
    manifest = normalized;
  } else if (fs.existsSync(path.join(bundleDir, NORMALIZED_MANIFEST))) {
    manifest = loadJson(path.join(bundleDir, NORMALIZED_MANIFEST));
    writeJson(path.join(bundleDir, CANONICAL_MANIFEST), manifest);
  } else {
    manifest = loadJson(manifestPath);
  }

  manifest = attachChecksums(manifest, bundleDir);
  writeJson(path.join(bundleDir, NORMALIZED_MANIFEST), manifest);
  writeJson(path.join(bundleDir, CANONICAL_MANIFEST), manifest);

  console.log(
    JSON.stringify(
      {
        status: 'BUNDLE FINALIZED',
        bundle_dir: bundleDir,
        html_file: manifest.files?.html,
        checksums: manifest.checksums,
        normalized_manifest: path.join(bundleDir, NORMALIZED_MANIFEST),
      },
      null,
      2,
    ),
  );
}

main();
