#!/usr/bin/env node
/**
 * MARS Search PPC — ORCA Gated Admission Wrapper (Wave 1.1)
 */
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeOrcaAction } from '../src/orca-ppc-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const args = { manifest: null, action: 'admission', fixture: null, diagnostic: false, help: false };
  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === '--manifest') args.manifest = rest[++i];
    else if (rest[i] === '--action') args.action = rest[++i];
    else if (rest[i] === '--fixture') args.fixture = rest[++i];
    else if (rest[i] === '--diagnostic') args.diagnostic = true;
    else if (rest[i] === '--help' || rest[i] === '-h') args.help = true;
  }
  return args;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.manifest) {
    console.log(`Usage: node orca-ppc-gate.mjs --manifest <path> [--action admission|demand_tiers|ownership|clustering|negatives] [--fixture <path>] [--diagnostic]`);
    process.exit(args.help ? 0 : 1);
  }

  const auth = authorizeOrcaAction({
    manifestPath: path.resolve(args.manifest),
    action: args.action,
    diagnosticOnly: args.diagnostic,
    command: `node orca-ppc-gate.mjs --action ${args.action}`,
  });

  console.log(JSON.stringify(auth, null, 2));
  if (!auth.allowed) {
    process.exit(auth.exit_code || 2);
  }

  process.env.MARS_SEARCH_PPC_LIFECYCLE_AUTHORIZED = '1';

  if (args.fixture) {
    const admissionCli = path.join(__dirname, '../cli/orca-admission.mjs');
    const sub = spawnSync('node', [admissionCli, 'integration:run', path.resolve(args.fixture)], {
      encoding: 'utf8',
      stdio: 'inherit',
    });
    process.exit(sub.status ?? 1);
  }

  process.exit(0);
}

main();
