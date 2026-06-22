#!/usr/bin/env node
/**
 * MARS Search PPC — Web-GPT Handoff Validator (Wave 1.1)
 * Validates generated handoff blocks contain required lifecycle fields.
 */
import fs from 'node:fs';

const REQUIRED_PATTERNS = [
  /project_id/i,
  /manifest_path|manifest path/i,
  /lifecycle_stage|current lifecycle stage/i,
  /requested_action|requested action/i,
  /blockers|STATUS:\s*BLOCKED/i,
  /validate-search-ppc-lifecycle|search-ppc-gate/i,
];

const BLOCKER = 'BLOCKED — WEB-GPT HANDOFF INVALID';

function main() {
  const file = process.argv[2];
  if (!file || process.argv.includes('--help')) {
    console.log('Usage: node validate-webgpt-handoff.mjs <handoff.md|.txt>');
    process.exit(file ? 0 : 1);
  }
  const text = fs.readFileSync(file, 'utf8');
  const missing = [];
  for (const p of REQUIRED_PATTERNS) {
    if (!p.test(text)) missing.push(p.toString());
  }
  if (missing.length) {
    console.error(BLOCKER);
    for (const m of missing) console.error(`- missing pattern: ${m}`);
    process.exit(2);
  }
  console.log(JSON.stringify({ status: 'VALID', file }, null, 2));
  process.exit(0);
}

main();
