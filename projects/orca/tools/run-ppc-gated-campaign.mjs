#!/usr/bin/env node
/**
 * MARS Search PPC — Campaign Production Gated Wrapper (Wave 1.1)
 */
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { authorizeCampaignAction } from './campaign-ppc-gate.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = path.resolve(__dirname, '../../..');

function parseArgs(argv) {
  const args = { manifest: null, action: null, config: null, help: false };
  const rest = argv.slice(2);
  for (let i = 0; i < rest.length; i++) {
    if (rest[i] === '--manifest') args.manifest = rest[++i];
    else if (rest[i] === '--action') args.action = rest[++i];
    else if (rest[i] === '--config') args.config = rest[++i];
    else if (rest[i] === '--help' || rest[i] === '-h') args.help = true;
  }
  return args;
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.manifest || !args.action) {
    console.log(`Usage: node run-ppc-gated-campaign.mjs --manifest <path> --action <campaign_architecture|keyword_distribution|ad_production|landing_alignment|bidding_budget|campaign_qa> [--config <audit-config.json>]`);
    process.exit(args.help ? 0 : 1);
  }

  const auth = authorizeCampaignAction({
    manifestPath: path.resolve(args.manifest),
    action: args.action,
    command: `node run-ppc-gated-campaign.mjs --action ${args.action}`,
  });

  console.log(JSON.stringify(auth, null, 2));
  if (!auth.allowed) {
    process.exit(auth.exit_code || 2);
  }

  if (args.config && args.action === 'campaign_qa') {
    const validator = path.join(__dirname, 'validate-campaign-production-contract.mjs');
    const sub = spawnSync('node', [validator, '--config', path.resolve(args.config)], {
      cwd: REPO_ROOT,
      encoding: 'utf8',
      stdio: 'inherit',
    });
    process.exit(sub.status ?? 1);
  }

  process.exit(0);
}

main();
