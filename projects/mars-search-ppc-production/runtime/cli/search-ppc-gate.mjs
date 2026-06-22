#!/usr/bin/env node
/**
 * MARS Search PPC — Canonical Lifecycle Gate CLI (Wave 1.1)
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeAction } from '../src/lifecycle-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../../../');
const DEFAULT_RECEIPT_DIR = path.resolve(__dirname, '../receipts');

function parseArgs(argv) {
  const args = {
    manifest: null,
    stage: null,
    action: null,
    actor: 'operator',
    tool: 'search-ppc-gate',
    command: null,
    receiptDir: DEFAULT_RECEIPT_DIR,
    noReceipt: false,
    outJson: null,
  };
  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    const a = rest[i];
    if (a === '--manifest') args.manifest = rest[++i];
    else if (a === '--stage') args.stage = rest[++i];
    else if (a === '--action') args.action = rest[++i];
    else if (a === '--actor') args.actor = rest[++i];
    else if (a === '--tool') args.tool = rest[++i];
    else if (a === '--command') args.command = rest[++i];
    else if (a === '--receipt-dir') args.receiptDir = path.resolve(rest[++i]);
    else if (a === '--no-receipt') args.noReceipt = true;
    else if (a === '--out-json') args.outJson = rest[++i];
    else if (a === '--help' || a === '-h') args.help = true;
  }
  return args;
}

function usage() {
  console.log(`Usage:
  node search-ppc-gate.mjs --manifest <path> --action <action> [--stage <SPPC-XX>] [--actor <name>] [--tool <tool>] [--command <cmd>] [--receipt-dir <dir>] [--out-json <path>]`);
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.action) {
    usage();
    process.exit(args.help ? 0 : 1);
  }

  const result = authorizeAction({
    manifestPath: args.manifest,
    requestedStage: args.stage,
    requestedAction: args.action,
    actor: args.actor,
    tool: args.tool,
    command: args.command || `search-ppc-gate --action ${args.action}`,
    repoRoot: REPO_ROOT,
    writeReceipt: !args.noReceipt,
    receiptDir: args.receiptDir,
  });

  const json = JSON.stringify(result, null, 2);
  if (args.outJson) {
    fs.mkdirSync(path.dirname(path.resolve(args.outJson)), { recursive: true });
    fs.writeFileSync(args.outJson, json + '\n');
  }
  console.log(json);
  process.exit(result.exit_code);
}

main();
