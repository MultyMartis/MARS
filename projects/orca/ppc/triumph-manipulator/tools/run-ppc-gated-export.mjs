#!/usr/bin/env node
/**
 * MARS Search PPC — Triumph Commander Gated Export Wrapper (Wave 1.1)
 */
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeExportAction } from './export-ppc-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const args = { manifest: null, document: null, report: null, help: false };
  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === '--manifest') args.manifest = rest[++i];
    else if (rest[i] === '--document') args.document = rest[++i];
    else if (rest[i] === '--report') args.report = rest[++i];
    else if (rest[i] === '--help' || rest[i] === '-h') args.help = true;
  }
  return args;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.manifest) {
    console.log(`Usage: node run-ppc-gated-export.mjs --manifest <path> [--document <orca-ppc-document.json>] [--report <validation-report.json>]`);
    process.exit(args.help ? 0 : 1);
  }

  const auth = authorizeExportAction({
    manifestPath: path.resolve(args.manifest),
    exporter: 'triumph-manipulator-exporter-cli',
    command: 'node run-ppc-gated-export.mjs',
  });

  console.log(JSON.stringify(auth, null, 2));
  if (!auth.allowed) {
    process.exit(auth.exit_code || 2);
  }

  process.env.MARS_SEARCH_PPC_LIFECYCLE_AUTHORIZED = '1';

  if (args.document && args.report) {
    const exportCli = path.join(__dirname, 'exporter-cli/export.js');
    const sub = spawnSync('node', [exportCli, path.resolve(args.document), path.resolve(args.report)], {
      encoding: 'utf8',
      stdio: 'inherit',
    });
    process.exit(sub.status ?? 1);
  }

  process.exit(0);
}

main();
