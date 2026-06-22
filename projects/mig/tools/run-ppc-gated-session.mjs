#!/usr/bin/env node
/**
 * MARS Search PPC — MIG Gated Session Wrapper (Wave 1.1)
 * Requires lifecycle authorization before MIG session execution.
 */
import { createRequire } from 'node:module';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeMigAction } from './mig-ppc-gate.mjs';

const require = createRequire(import.meta.url);
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../..');

function parseArgs(argv) {
  const args = { manifest: null, action: null, help: false, passthrough: [] };
  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === '--manifest') args.manifest = rest[++i];
    else if (rest[i] === '--action') args.action = rest[++i];
    else if (rest[i] === '--help' || rest[i] === '-h') args.help = true;
    else args.passthrough.push(rest[i]);
  }
  return args;
}

async function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.manifest || !args.action) {
    console.log(`Usage: node mig-ppc-gate.mjs --manifest <path> --action <source_registration|corpus_intake|normalization|paid_serp|competitor_audit> [-- ...mig args]`);
    process.exit(args.help ? 0 : 1);
  }

  const auth = authorizeMigAction({
    manifestPath: path.resolve(args.manifest),
    action: args.action,
    command: `node mig-ppc-gate.mjs --action ${args.action}`,
  });

  console.log(JSON.stringify(auth, null, 2));
  if (!auth.allowed) {
    process.exit(auth.exit_code || 2);
  }

  if (args.passthrough.length) {
    const { runMigSession } = require('../lib/runtime/run-mig-session.js');
    const body = JSON.parse(args.passthrough[0]);
    await runMigSession(body);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
