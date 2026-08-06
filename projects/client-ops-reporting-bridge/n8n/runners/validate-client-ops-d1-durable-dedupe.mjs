/**
 * Static validator for Phase 1B-D1 durable dedupe evidence pack.
 * Offline. No network.
 */

import { existsSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EV = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/n8n/evidence/phase-1b-d1-durable-dedupe',
);
const PHASE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/PHASE-1B-D1-DURABLE-DEDUPE-DESIGN-AND-INACTIVE-SANDBOX-IMPLEMENTATION.md',
);

const required = [
  'README.md',
  'D1-CHARTER.json',
  'DATATABLE-CAPABILITY-MATRIX.md',
  'DATATABLE-INSTALLED-SCHEMA.json',
  'DEDUP-STATE-MACHINE.md',
  'DEDUP-ROW-SCHEMA.json',
  'EVENT-FINGERPRINT-CONTRACT.md',
  'CONCURRENCY-ASSESSMENT.md',
  'PRE-APPLY-MANIFEST.json',
  'DATATABLE-CREATE-EVIDENCE.json',
  'SANITIZED-STRUCTURAL-DIFF.json',
  'POST-APPLY-WORKFLOW-STATE.json',
  'FIRST-SEEN-RESULT.json',
  'EXACT-REPLAY-RESULT.json',
  'EVENT-ID-CONFLICT-RESULT.json',
  'DATATABLE-POST-TEST-STATE.json',
  'TELEGRAM-DELIVERY-EVIDENCE.json',
  'CONTAINMENT-STATUS.md',
  'ROLLBACK-READINESS.md',
  'TEST-RESULTS.md',
  'SECURITY-REVIEW.md',
  'D1-DECISION.json',
];

function load(name) {
  return JSON.parse(readFileSync(resolve(EV, name), 'utf8'));
}

const gates = [];
function pass(id, detail = 'ok') {
  gates.push({ id, ok: true, detail });
}
function fail(id, detail) {
  gates.push({ id, ok: false, detail });
}

if (!existsSync(PHASE)) fail('phase_doc', 'missing');
else pass('phase_doc');

for (const f of required) {
  if (!existsSync(resolve(EV, f))) fail(`file_${f}`, 'missing');
  else pass(`file_${f}`);
}

const first = load('FIRST-SEEN-RESULT.json');
const replay = load('EXACT-REPLAY-RESULT.json');
const conflict = load('EVENT-ID-CONFLICT-RESULT.json');
const tg = load('TELEGRAM-DELIVERY-EVIDENCE.json');
const decision = load('D1-DECISION.json');
const table = load('DATATABLE-POST-TEST-STATE.json');

if (first.http_status === 202 && first.response_dedupe === 'FIRST_SEEN') pass('first_seen');
else fail('first_seen', JSON.stringify({ s: first.http_status, d: first.response_dedupe }));

if (replay.http_status === 200 && replay.response_result === 'DUPLICATE_SUPPRESSED') pass('replay');
else fail('replay', String(replay.response_result));

if (conflict.http_status === 409 && conflict.response_result === 'EVENT_ID_CONFLICT') pass('conflict');
else fail('conflict', String(conflict.response_result));

if (first.execution_summary?.telegram_runs === 1) pass('tg_first');
else fail('tg_first', String(first.execution_summary?.telegram_runs));

if (replay.execution_summary?.telegram_runs === 0) pass('tg_replay_zero');
else fail('tg_replay_zero', 'nonzero');

if (conflict.execution_summary?.telegram_runs === 0) pass('tg_conflict_zero');
else fail('tg_conflict_zero', 'nonzero');

if (tg.delivered === 1 && tg.duplicates === 0) pass('tg_total');
else fail('tg_total', JSON.stringify(tg));

if (table.row_count_for_event === 1 && table.original_fingerprint_retained) pass('table_row');
else fail('table_row', 'bad');

if (decision.readiness === 'READY_FOR_DURABLE_DEDUPE_BASELINE_COMMIT') pass('readiness');
else fail('readiness', decision.readiness);

if (decision.concurrency_class === 'DEDUPE_SEQUENTIAL_SAFE_CONCURRENCY_UNPROVEN') {
  pass('concurrency_class');
} else fail('concurrency_class', decision.concurrency_class);

const blob = readFileSync(resolve(EV, 'FIRST-SEEN-RESULT.json'), 'utf8')
  + readFileSync(resolve(EV, 'D1-DECISION.json'), 'utf8');
if (/N8N_API_KEY\s*=\s*\S+/i.test(blob)) fail('api_key_leak', 'found');
else pass('api_key_leak');
if (/\/webhook\/[A-Za-z0-9_-]{8,}/.test(blob)) fail('full_webhook_path', 'found');
else pass('full_webhook_path');

const failed = gates.filter((g) => !g.ok);
const verdict = failed.length === 0 ? 'PASS' : 'FAIL';
console.log(
  JSON.stringify(
    {
      validator: 'validate-client-ops-d1-durable-dedupe',
      gates: gates.length,
      pass_count: gates.filter((g) => g.ok).length,
      fail_count: failed.length,
      failed,
      verdict,
    },
    null,
    2,
  ),
);
process.exitCode = failed.length === 0 ? 0 : 1;
