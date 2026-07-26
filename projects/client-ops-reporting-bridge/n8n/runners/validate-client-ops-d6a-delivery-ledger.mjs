/**
 * Phase 1B-D6A — offline validator for durable delivery ledger evidence + source.
 * No network. No secrets printed.
 *
 * Usage:
 *   node validate-client-ops-d6a-delivery-ledger.mjs
 */
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  DELIVERY_STATES,
  FINALIZER_UPDATE_MODEL,
  MAX_RETRIES,
  MAX_SAFE_CONCURRENCY,
  SCHEMA_DECISION,
  evaluateDeliveryTransition,
  classifyTelegramOutcome,
} from './lib/client-ops-delivery-ledger.mjs';
import {
  composeDeliveryLedgerPutFromLive,
  validateDeliveryLedgerPutPayload,
} from './lib/client-ops-delivery-ledger-compose.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const PROJECT = resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge');
const PACK = resolve(
  PROJECT,
  'evidence/phase-1b-d6a-durable-post-telegram-delivery-ledger',
);
const PHASE = resolve(
  PROJECT,
  'PHASE-1B-D6A-DURABLE-POST-TELEGRAM-DELIVERY-LEDGER-DESIGN-AND-OFFLINE-IMPLEMENTATION.md',
);
const FIXTURES = resolve(PROJECT, 'n8n/harness/delivery-ledger-cases');
const LIB = resolve(PROJECT, 'n8n/runners/lib');

const REQUIRED_PACK = [
  'README.md',
  'D6A-CHARTER.json',
  'LIVE-BASELINE-GET-ONLY.md',
  'CURRENT-DATA-TABLE-SCHEMA.md',
  'CURRENT-DELIVERY-STATE-MACHINE.md',
  'TARGET-DELIVERY-STATE-MACHINE.md',
  'SCHEMA-DECISION.md',
  'FINALIZER-CONTRACT.md',
  'FINALIZER-UPDATE-MODEL.md',
  'TELEGRAM-SUCCESS-AUTHORITY.md',
  'TELEGRAM-FAILURE-SEMANTICS.md',
  'POST-TELEGRAM-LEDGER-WRITE-FAILURE.md',
  'DUPLICATE-SAFETY.md',
  'WORKFLOW-FINALIZATION-PLACEMENT.md',
  'OFFLINE-WORKFLOW-IMPLEMENTATION.md',
  'OFFLINE-SCHEMA-MODEL.md',
  'FIXTURE-MATRIX.md',
  'TEST-RESULTS.md',
  'REGRESSION-RESULTS.md',
  'SECURITY-REVIEW.md',
  'D6A-DECISION.json',
];

const REQUIRED_LIBS = [
  'client-ops-delivery-ledger.mjs',
  'client-ops-delivery-ledger-compose.mjs',
];

const SECRET_RES = [
  /\b\d{8,10}:[A-Za-z0-9_-]{30,}\b/,
  /api\.telegram\.org\/bot\d+/i,
  /CLIENT_OPS_WEBHOOK_AUTH_SECRET\s*=\s*\S+/i,
  /N8N_API_KEY\s*=\s*\S+/i,
  /https?:\/\/[^\s"'`]+\/webhook\/[^\s"'`]+/i,
];

const gates = [];
function pass(id, detail = 'ok') {
  gates.push({ id, ok: true, detail });
}
function fail(id, detail) {
  gates.push({ id, ok: false, detail });
}

function walk(p, out = []) {
  if (!existsSync(p)) return out;
  const st = statSync(p);
  if (st.isFile()) {
    out.push(p);
    return out;
  }
  for (const name of readdirSync(p)) {
    if (name === '__pycache__' || name === 'node_modules') continue;
    walk(join(p, name), out);
  }
  return out;
}

if (!existsSync(PHASE)) fail('phase_doc', 'missing');
else pass('phase_doc');

for (const f of REQUIRED_PACK) {
  if (!existsSync(resolve(PACK, f))) fail(`pack_${f}`, 'missing');
  else pass(`pack_${f}`);
}

for (const f of REQUIRED_LIBS) {
  if (!existsSync(resolve(LIB, f))) fail(`lib_${f}`, 'missing');
  else pass(`lib_${f}`);
}

if (SCHEMA_DECISION === 'D6A_EXISTING_SCHEMA_SUFFICIENT') pass('schema_decision');
else fail('schema_decision', SCHEMA_DECISION);

if (FINALIZER_UPDATE_MODEL === 'LOOKUP_VALIDATE_UPDATE_SEQUENTIAL_ONLY') {
  pass('update_model');
} else fail('update_model', FINALIZER_UPDATE_MODEL);

if (MAX_RETRIES === 0) pass('max_retries');
else fail('max_retries', String(MAX_RETRIES));

if (MAX_SAFE_CONCURRENCY === 1) pass('concurrency');
else fail('concurrency', String(MAX_SAFE_CONCURRENCY));

if (JSON.stringify(DELIVERY_STATES) === JSON.stringify(['PENDING', 'SENT', 'FAILED'])) {
  pass('delivery_states');
} else fail('delivery_states', JSON.stringify(DELIVERY_STATES));

const t1 = evaluateDeliveryTransition('PENDING', 'SENT');
if (t1.ok && t1.action === 'UPDATE') pass('transition_pending_sent');
else fail('transition_pending_sent', t1.code);

const t2 = evaluateDeliveryTransition('PENDING', 'FAILED');
if (t2.ok && t2.action === 'UPDATE') pass('transition_pending_failed');
else fail('transition_pending_failed', t2.code);

const t3 = evaluateDeliveryTransition('SENT', 'FAILED');
if (!t3.ok && t3.code === 'SENT_TO_FAILED_PROHIBITED') pass('transition_sent_failed_reject');
else fail('transition_sent_failed_reject', t3.code);

const t4 = evaluateDeliveryTransition('SENT', 'SENT');
if (t4.ok && t4.action === 'NOOP_IDEMPOTENT') pass('transition_sent_idempotent');
else fail('transition_sent_idempotent', t4.code);

const success = classifyTelegramOutcome({ ok: true, result: { message_id: 7 } });
if (success.outcome === 'SUCCESS' && success.target_delivery_state === 'SENT') {
  pass('telegram_success_authority');
} else fail('telegram_success_authority', success.outcome);

const failure = classifyTelegramOutcome({}, { nodeError: true });
if (failure.outcome === 'DEFINITE_FAILURE' && failure.target_delivery_state === 'FAILED') {
  pass('telegram_failure_authority');
} else fail('telegram_failure_authority', failure.outcome);

const ambiguous = classifyTelegramOutcome({}, { ambiguous: true });
if (!ambiguous.should_finalize) pass('ambiguous_no_finalize');
else fail('ambiguous_no_finalize', 'should_finalize');

const fixtureWorkflow = resolve(FIXTURES, 'offline-live-workflow-17.json');
if (!existsSync(fixtureWorkflow)) fail('offline_workflow_fixture', 'missing');
else {
  const live = JSON.parse(readFileSync(fixtureWorkflow, 'utf8'));
  const composed = composeDeliveryLedgerPutFromLive(live, 'H6VYhwz7RXZCBMmu');
  if (!composed.ok) fail('compose', composed.error);
  else {
    pass('compose');
    const v = validateDeliveryLedgerPutPayload(composed.bundle.put_payload, 'H6VYhwz7RXZCBMmu');
    if (v.ok) pass('compose_validate');
    else fail('compose_validate', v.errors.join(','));
    if (composed.bundle.live_apply_performed === false) pass('no_live_apply_flag');
    else fail('no_live_apply_flag', 'true');
  }
}

const caseFiles = existsSync(FIXTURES)
  ? readdirSync(FIXTURES).filter((f) => f.endsWith('.case.json'))
  : [];
if (caseFiles.length >= 8) pass('fixture_cases', String(caseFiles.length));
else fail('fixture_cases', String(caseFiles.length));

let decision;
try {
  decision = JSON.parse(readFileSync(resolve(PACK, 'D6A-DECISION.json'), 'utf8'));
  if (decision.live_apply_performed === false) pass('decision_no_live');
  else fail('decision_no_live', 'true');
  if (decision.automatic_retries_enabled === false) pass('decision_no_retry');
  else fail('decision_no_retry', 'true');
  if (decision.duplicate_delivery_replay_allowed === false) pass('decision_no_dup_replay');
  else fail('decision_no_dup_replay', 'true');
  if (decision.max_safe_concurrency === 1) pass('decision_concurrency');
  else fail('decision_concurrency', String(decision.max_safe_concurrency));
  if (decision.intake_state_immutable === true) pass('decision_intake_immutable');
  else fail('decision_intake_immutable', 'false');
  if (decision.event_status_immutable === true) pass('decision_status_immutable');
  else fail('decision_status_immutable', 'false');
  if (decision.readiness === 'READY_FOR_D6A_CONTROLLED_PRODUCTION_APPLY_CHARTER') {
    pass('decision_readiness');
  } else fail('decision_readiness', decision.readiness);
} catch (err) {
  fail('decision_parse', err instanceof Error ? err.message : String(err));
}

// Security scan over pack + new libs + fixtures
const scanRoots = [PACK, LIB, FIXTURES, PHASE];
let leak = false;
for (const root of scanRoots) {
  for (const file of walk(root)) {
    if (!/\.(md|json|mjs|js|py)$/i.test(file)) continue;
    if (file.includes('_get-precheck') || file.includes('_export-offline')) continue;
    // Skip large workflow fixture binary-ish? still scan text
    let text;
    try {
      text = readFileSync(file, 'utf8');
    } catch {
      continue;
    }
    // Allow documented credential *ids* already in allowlists; block tokens/paths.
    for (const re of SECRET_RES) {
      if (re.test(text)) {
        leak = true;
        fail('security_leak', `${file}`);
        break;
      }
    }
    if (leak) break;
  }
  if (leak) break;
}
if (!leak) pass('security_scan');

const failed = gates.filter((g) => !g.ok);
const verdict = failed.length === 0 ? 'PASS' : 'FAIL';
console.log(
  JSON.stringify(
    {
      validator: 'validate-client-ops-d6a-delivery-ledger',
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
process.exit(failed.length === 0 ? 0 : 1);
