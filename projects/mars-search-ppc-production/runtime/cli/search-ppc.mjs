#!/usr/bin/env node
/**
 * MARS Search PPC Lifecycle CLI v1
 *
 * Usage:
 *   node search-ppc.mjs status <manifest>
 *   node search-ppc.mjs can-start <manifest> <stage-id>
 *   node search-ppc.mjs transition <manifest> <stage-id> <status> [--dry-run]
 *   node search-ppc.mjs report <manifest> [--out-json <path>] [--out-md <path>]
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  loadJson,
  validateLifecycle,
  validateCanStart,
  validateTransitionDryRun,
  formatBlockerReportMd,
} from '../src/validate-lifecycle.mjs';
import { DEFAULT_CONTRACT_REL, EXIT_CODES } from '../src/constants.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../..');
const DEFAULT_CONTRACT = path.resolve(REPO_ROOT, DEFAULT_CONTRACT_REL);

function parseArgs(argv) {
  const args = { command: null, manifest: null, stageId: null, status: null, dryRun: false, outJson: null, outMd: null, contract: DEFAULT_CONTRACT };
  const rest = argv.slice(2);
  args.command = rest[0];
  args.manifest = rest[1];
  if (args.command === 'can-start') {
    args.stageId = rest[2];
  }
  if (args.command === 'transition') {
    args.stageId = rest[2];
    args.status = rest[3];
  }
  for (let i = 2; i < rest.length; i++) {
    if (rest[i] === '--dry-run') args.dryRun = true;
    if (rest[i] === '--out-json') args.outJson = rest[++i];
    if (rest[i] === '--out-md') args.outMd = rest[++i];
    if (rest[i] === '--contract') args.contract = path.resolve(rest[++i]);
  }
  return args;
}

function prepareManifest(manifestPath) {
  const manifest = loadJson(manifestPath);
  manifest._manifestPath = path.resolve(manifestPath);
  manifest._repoRoot = REPO_ROOT;
  return manifest;
}

function writeOutputs(json, md, args) {
  if (args.outJson) {
    fs.mkdirSync(path.dirname(args.outJson), { recursive: true });
    fs.writeFileSync(args.outJson, JSON.stringify(json, null, 2) + '\n');
  }
  if (args.outMd) {
    fs.mkdirSync(path.dirname(args.outMd), { recursive: true });
    fs.writeFileSync(args.outMd, md + '\n');
  }
}

function usage() {
  console.log(`Usage:
  node search-ppc.mjs status <manifest> [--out-json <path>] [--out-md <path>]
  node search-ppc.mjs can-start <manifest> <stage-id>
  node search-ppc.mjs transition <manifest> <stage-id> <status> [--dry-run]
  node search-ppc.mjs report <manifest> [--out-json <path>] [--out-md <path>]`);
}

function main() {
  const args = parseArgs(process.argv);
  if (!args.command || !args.manifest || args.command === 'help') {
    usage();
    process.exit(args.command === 'help' ? 0 : 1);
  }

  const contract = loadJson(args.contract);
  const manifest = prepareManifest(args.manifest);

  if (args.command === 'status' || args.command === 'report') {
    const result = validateLifecycle(manifest, contract, { repoRoot: REPO_ROOT });
    const md = result.status === 'BLOCKED'
      ? formatBlockerReportMd(result.blocker_report)
      : `STATUS: ${result.status}\n\nProject: ${result.project_id}\nCurrent stage: ${result.current_stage}\nCompleted: ${result.completed_approved_stages.join(', ') || '(none)'}\nAllowed: ${result.allowed_next_action.join('; ')}`;
    writeOutputs(result, md, args);
    console.log(md);
    process.exit(result.exit_code);
  }

  if (args.command === 'can-start') {
    if (!args.stageId) {
      usage();
      process.exit(1);
    }
    const check = validateCanStart(manifest, contract, args.stageId, { repoRoot: REPO_ROOT });
    const out = { command: 'can-start', stage_id: args.stageId, ...check };
    console.log(JSON.stringify(out, null, 2));
    process.exit(check.allowed ? EXIT_CODES.OK : EXIT_CODES.BLOCKED);
  }

  if (args.command === 'transition') {
    if (!args.stageId || !args.status) {
      usage();
      process.exit(1);
    }
    const result = validateTransitionDryRun(manifest, contract, args.stageId, args.status, { repoRoot: REPO_ROOT });
    console.log(JSON.stringify(result, null, 2));
    process.exit(result.allowed ? EXIT_CODES.OK : EXIT_CODES.BLOCKED);
  }

  usage();
  process.exit(1);
}

main();
