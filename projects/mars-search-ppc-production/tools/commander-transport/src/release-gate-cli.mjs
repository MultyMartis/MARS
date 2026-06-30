#!/usr/bin/env node
/**
 * Release gate CLI entry point.
 * Usage: node src/release-gate-cli.mjs --project <id> --package <path> --authority <path> --receipt <path>
 */
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { runReleaseGate } from './release-gate.mjs';
import { COMMANDER_TEMPLATE_PATH } from './constants.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

function parseArgs(argv) {
  const args = { guardOptions: { skipVolumeCheck: process.env.MARS_SKIP_VOLUME_CHECK === '1' } };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--project') args.project_id = argv[++i];
    else if (a === '--package') args.package_root = argv[++i];
    else if (a === '--authority') args.authority_path = argv[++i];
    else if (a === '--receipt') args.receipt_path = argv[++i];
    else if (a === '--template') args.template_path = argv[++i];
    else if (a === '--group-plan') args.group_plan_path = argv[++i];
    else if (a === '--architecture') args.architecture_path = argv[++i];
    else if (a === '--checksum-manifest') args.checksum_manifest_path = argv[++i];
    else if (a === '--no-require-approval') args.require_operator_approval = false;
    else if (a === '--json') args.json = true;
  }
  if (!args.template_path) args.template_path = COMMANDER_TEMPLATE_PATH;
  return args;
}

async function main() {
  const args = parseArgs(process.argv);
  const result = await runReleaseGate(args);

  if (args.json) {
    console.log(JSON.stringify(result, null, 2));
  } else {
    console.log(`Release Gate: ${result.status}`);
    console.log(`Script: ${result.script_status}`);
    console.log(`Phase: ${result.current_release_phase}`);
    console.log(`Violations: ${result.violation_count}`);
    for (const v of result.violations) {
      console.log(`  FAIL: ${v.code} — ${v.message}`);
    }
  }

  process.exit(result.status === 'RELEASE_GATE_PASS' ? 0 : 1);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
