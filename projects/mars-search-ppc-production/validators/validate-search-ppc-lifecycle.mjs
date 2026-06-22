#!/usr/bin/env node
/**
 * MARS Search PPC Lifecycle Validator v1 (Wave 1)
 * Delegates to runtime/src/validate-lifecycle.mjs
 *
 * Usage:
 *   node validate-search-ppc-lifecycle.mjs <manifest>
 *   node validate-search-ppc-lifecycle.mjs --manifest <path> [--contract <path>] [--out-json <path>] [--out-md <path>]
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadJson, validateLifecycle, formatBlockerReportMd } from '../runtime/src/validate-lifecycle.mjs';
import { DEFAULT_CONTRACT_REL, EXIT_CODES } from '../runtime/src/constants.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../..');
const DEFAULT_CONTRACT = path.resolve(REPO_ROOT, DEFAULT_CONTRACT_REL);

function parseArgs(argv) {
  const args = { manifest: null, contract: DEFAULT_CONTRACT, outJson: null, outMd: null, help: false };
  const rest = argv.slice(2);
  if (rest[0] && !rest[0].startsWith('-')) {
    args.manifest = rest[0];
  }
  for (let i = 0; i < rest.length; i++) {
    const a = rest[i];
    if (a === '--manifest') args.manifest = rest[++i];
    else if (a === '--contract') args.contract = path.resolve(rest[++i]);
    else if (a === '--out-json') args.outJson = rest[++i];
    else if (a === '--out-md') args.outMd = rest[++i];
    else if (a === '--help' || a === '-h') args.help = true;
  }
  return args;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.manifest) {
    console.log(`Usage: node validate-search-ppc-lifecycle.mjs <manifest>
       node validate-search-ppc-lifecycle.mjs --manifest <path> [--contract <path>] [--out-json <path>] [--out-md <path>]`);
    process.exit(args.help ? 0 : 1);
  }

  const manifestPath = path.resolve(args.manifest);
  if (!fs.existsSync(manifestPath)) {
    const result = validateLifecycle(null, { version: '1.0.0', stages: [] });
    console.log(formatBlockerReportMd(result.blocker_report));
    process.exit(EXIT_CODES.BLOCKED);
  }

  const manifest = loadJson(manifestPath);
  manifest._manifestPath = manifestPath;
  manifest._repoRoot = REPO_ROOT;
  const contract = loadJson(args.contract);
  const result = validateLifecycle(manifest, contract, { repoRoot: REPO_ROOT });

  const jsonOut = JSON.stringify(result, null, 2);
  const mdOut = result.status === 'BLOCKED'
    ? formatBlockerReportMd(result.blocker_report)
    : `STATUS: ${result.status}\n\nCurrent stage: ${result.current_stage}\nCompleted: ${result.completed_approved_stages.join(', ') || '(none)'}`;

  if (args.outJson) {
    fs.mkdirSync(path.dirname(path.resolve(args.outJson)), { recursive: true });
    fs.writeFileSync(args.outJson, jsonOut + '\n');
  }
  if (args.outMd) {
    fs.mkdirSync(path.dirname(path.resolve(args.outMd)), { recursive: true });
    fs.writeFileSync(args.outMd, mdOut + '\n');
  }

  console.log(mdOut);
  process.exit(result.exit_code);
}

main();
