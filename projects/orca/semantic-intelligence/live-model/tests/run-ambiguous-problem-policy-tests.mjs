#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const policy = JSON.parse(fs.readFileSync(path.join(__dirname, '../supplementary/policies/ambiguous-problem-query-policy-v1.json'), 'utf8'));

let passed = 0;
let failed = 0;
function assert(name, cond) {
  if (cond) { passed++; console.log(`  [PASS] ${name}`); }
  else { failed++; console.log(`  [FAIL] ${name}`); }
}

assert('policy has ACCEPT class', !!policy.classes.ACCEPT);
assert('policy has ABSTAIN class', !!policy.classes.ABSTAIN);
assert('policy has REJECT class', !!policy.classes.REJECT);
assert('geography alone never accept', policy.hard_rules.geography_alone_never_accept === true);
assert('decision factors include urgency', policy.decision_factors.includes('urgency'));
assert('ACCEPT examples include urgent specialist', policy.classes.ACCEPT.examples.some((e) => /срочно/i.test(e)));
assert('ABSTAIN examples include generic problem', policy.classes.ABSTAIN.examples.some((e) => /не работает/i.test(e)));
assert('REJECT examples include DIY', policy.classes.REJECT.examples.some((e) => /самостоятельно/i.test(e)));

console.log(`Ambiguous problem policy tests: ${passed}/${passed + failed}`);
process.exit(failed ? 1 : 0);
