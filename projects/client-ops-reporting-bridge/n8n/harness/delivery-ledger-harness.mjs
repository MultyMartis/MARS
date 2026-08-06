/**
 * Phase 1B-D6A — offline durable delivery ledger harness.
 * No network. No Telegram. No n8n mutation.
 */

import { readFileSync, readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  applyDeliveryFinalizer,
  assertIntakeAndStatusImmutable,
  classifyTelegramOutcome,
  createOfflineLedgerStore,
  DELIVERY_STATE,
  evaluateDeliveryTransition,
  MAX_RETRIES,
  MAX_SAFE_CONCURRENCY,
  simulateDuplicateReplay,
  simulateFirstSeenDeliveryPath,
} from '../runners/lib/client-ops-delivery-ledger.mjs';
import {
  composeDeliveryLedgerPutFromLive,
  validateDeliveryLedgerPutPayload,
  D6A_EXPECTED_NODES_PRE,
  DELIVERY_LEDGER_NODE_NAMES,
} from '../runners/lib/client-ops-delivery-ledger-compose.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const FIXTURES = join(__dirname, 'delivery-ledger-cases');

function loadJson(path) {
  return JSON.parse(readFileSync(path, 'utf8'));
}

function baseClaim(overrides = {}) {
  return {
    event_id: 'd6a-fixture-event-001',
    event_fingerprint: '{"fixture":"d6a-case1"}',
    site_id: 'site-002',
    schema_name: 'mars.client_ops.report',
    schema_version: '1.0',
    event_type: 'CATALOG_MONITOR',
    event_status: 'ATTENTION',
    intake_state: 'FIRST_SEEN',
    delivery_state: DELIVERY_STATE.PENDING,
    first_seen_at: '2026-07-26T17:48:38.000Z',
    last_seen_at: '2026-07-26T17:48:38.000Z',
    duplicate_count: 0,
    conflict_count: 0,
    redaction_version: 'd1-v1',
    sandbox_marker: 'mars-client-ops-d6a-offline',
    ...overrides,
  };
}

function assert(cond, label) {
  if (!cond) throw new Error(label);
}

function runCase(tc) {
  const id = tc.id;
  if (id === 'case1_first_seen_telegram_success') {
    const store = createOfflineLedgerStore();
    const claim = baseClaim({ event_id: tc.event_id, event_fingerprint: tc.fingerprint });
    const result = simulateFirstSeenDeliveryPath({
      store,
      claimRow: claim,
      telegramOutcome: { output: { ok: true, result: { message_id: 42 } } },
    });
    assert(result.http.http_status === 202, 'http_202');
    assert(result.row.delivery_state === 'SENT', 'delivery_sent');
    assert(result.row.intake_state === 'FIRST_SEEN', 'intake_immutable');
    assert(result.row.event_status === 'ATTENTION', 'status_immutable');
    assert(result.telegram_attempts === 1, 'one_telegram');
    const inv = assertIntakeAndStatusImmutable(claim, result.row);
    assert(inv.ok, `immutable:${inv.violations.join(',')}`);
    return;
  }

  if (id === 'case2_first_seen_telegram_failure') {
    const store = createOfflineLedgerStore();
    const claim = baseClaim({ event_id: tc.event_id, event_fingerprint: tc.fingerprint });
    const result = simulateFirstSeenDeliveryPath({
      store,
      claimRow: claim,
      telegramOutcome: { nodeError: true, output: { ok: false } },
    });
    assert(result.http.http_status === 202, 'http_202');
    assert(result.row.delivery_state === 'FAILED', 'delivery_failed');
    assert(result.row.intake_state === 'FIRST_SEEN', 'intake_immutable');
    assert(result.row.event_status === 'ATTENTION', 'status_immutable');
    assert(result.telegram_attempts === 1, 'one_telegram');
    assert(result.classified.sanitized_error_class === 'TELEGRAM_NODE_ERROR', 'error_class');
    return;
  }

  if (id === 'case3_duplicate_with_sent') {
    const store = createOfflineLedgerStore([
      baseClaim({
        event_id: tc.event_id,
        event_fingerprint: tc.fingerprint,
        delivery_state: 'SENT',
      }),
    ]);
    const replay = simulateDuplicateReplay({
      store,
      eventId: tc.event_id,
      fingerprint: tc.fingerprint,
    });
    assert(replay.classification === 'DUPLICATE', 'dup');
    assert(replay.telegram_attempted === false, 'no_telegram');
    assert(replay.delivery_state === 'SENT', 'no_regression');
    assert(replay.http_status === 200, 'http_200');
    return;
  }

  if (id === 'case4_duplicate_with_pending') {
    const store = createOfflineLedgerStore([
      baseClaim({
        event_id: tc.event_id,
        event_fingerprint: tc.fingerprint,
        delivery_state: 'PENDING',
      }),
    ]);
    const replay = simulateDuplicateReplay({
      store,
      eventId: tc.event_id,
      fingerprint: tc.fingerprint,
    });
    assert(replay.telegram_attempted === false, 'no_telegram_replay');
    assert(replay.delivery_state === 'PENDING', 'remains_pending');
    return;
  }

  if (id === 'case5_duplicate_with_failed') {
    const store = createOfflineLedgerStore([
      baseClaim({
        event_id: tc.event_id,
        event_fingerprint: tc.fingerprint,
        delivery_state: 'FAILED',
      }),
    ]);
    const replay = simulateDuplicateReplay({
      store,
      eventId: tc.event_id,
      fingerprint: tc.fingerprint,
    });
    assert(replay.telegram_attempted === false, 'no_auto_retry');
    assert(replay.delivery_state === 'FAILED', 'remains_failed');
    assert(MAX_RETRIES === 0, 'max_retries_0');
    return;
  }

  if (id === 'case6_telegram_success_ledger_write_failure') {
    const store = createOfflineLedgerStore();
    const claim = baseClaim({ event_id: tc.event_id, event_fingerprint: tc.fingerprint });
    const result = simulateFirstSeenDeliveryPath({
      store,
      claimRow: claim,
      telegramOutcome: { output: { ok: true, result: { message_id: 99 } } },
      finalizeFails: true,
    });
    assert(result.telegram_attempts === 1, 'telegram_once');
    assert(result.row.delivery_state === 'PENDING', 'remains_pending');
    assert(result.finalize.code === 'LEDGER_WRITE_FAILURE', 'ledger_fail');
    // Second automatic Telegram must not happen
    const replay = simulateDuplicateReplay({
      store,
      eventId: tc.event_id,
      fingerprint: tc.fingerprint,
    });
    assert(replay.telegram_attempted === false, 'no_resend');
    return;
  }

  if (id === 'case7_finalizer_double_call_sent') {
    const store = createOfflineLedgerStore([
      baseClaim({
        event_id: tc.event_id,
        event_fingerprint: tc.fingerprint,
        delivery_state: 'PENDING',
      }),
    ]);
    const first = store.updateDeliveryState(tc.event_id, 'SENT');
    assert(first.ok && first.row.delivery_state === 'SENT', 'first_sent');
    const second = applyDeliveryFinalizer(store.get(tc.event_id), {
      event_id: tc.event_id,
      expected_current_delivery_state: 'PENDING',
      target_delivery_state: 'SENT',
    });
    // expected PENDING mismatches; already SENT → idempotent
    assert(second.ok && second.code === 'ALREADY_FINALIZED', 'idempotent');
    assert(store.get(tc.event_id).delivery_state === 'SENT', 'still_sent');
    return;
  }

  if (id === 'case8_sent_to_failed_rejected') {
    const row = baseClaim({
      event_id: tc.event_id,
      delivery_state: 'SENT',
    });
    const transition = evaluateDeliveryTransition('SENT', 'FAILED');
    assert(transition.ok === false, 'reject_transition');
    assert(transition.code === 'SENT_TO_FAILED_PROHIBITED', 'code');
    const applied = applyDeliveryFinalizer(row, {
      event_id: tc.event_id,
      expected_current_delivery_state: 'SENT',
      target_delivery_state: 'FAILED',
    });
    assert(applied.ok === false, 'reject_apply');
    return;
  }

  if (id === 'case_compose_offline_workflow') {
    const live = loadJson(join(FIXTURES, 'offline-live-workflow-17.json'));
    const composed = composeDeliveryLedgerPutFromLive(live, 'H6VYhwz7RXZCBMmu');
    assert(composed.ok, `compose:${composed.error}`);
    const validated = validateDeliveryLedgerPutPayload(
      composed.bundle.put_payload,
      'H6VYhwz7RXZCBMmu',
    );
    assert(validated.ok, `validate:${validated.errors.join(',')}`);
    assert(
      composed.expected_nodes_post === D6A_EXPECTED_NODES_PRE + DELIVERY_LEDGER_NODE_NAMES.length,
      'node_delta',
    );
    return;
  }

  if (id === 'case_security_no_secrets_in_metadata') {
    const classified = classifyTelegramOutcome(
      { ok: false, error: 'token=SECRET_SHOULD_NOT_LEAK description=raw' },
      { nodeError: true },
    );
    const blob = JSON.stringify(classified);
    assert(!/SECRET_SHOULD_NOT_LEAK/.test(blob), 'no_raw_error');
    assert(classified.sanitized_error_class === 'TELEGRAM_NODE_ERROR', 'class_only');
    assert(MAX_SAFE_CONCURRENCY === 1, 'concurrency_1');
    return;
  }

  if (id === 'case_ambiguous_leaves_pending') {
    const store = createOfflineLedgerStore();
    const claim = baseClaim({ event_id: tc.event_id, event_fingerprint: tc.fingerprint });
    const result = simulateFirstSeenDeliveryPath({
      store,
      claimRow: claim,
      telegramOutcome: { ambiguous: true, output: {} },
    });
    assert(result.row.delivery_state === 'PENDING', 'ambiguous_pending');
    assert(result.classified.should_finalize === false, 'no_finalize');
    return;
  }

  throw new Error(`unknown_case:${id}`);
}

function main() {
  const files = readdirSync(FIXTURES)
    .filter((f) => f.endsWith('.case.json'))
    .sort();
  let passed = 0;
  let failed = 0;
  const failures = [];

  for (const file of files) {
    const tc = loadJson(join(FIXTURES, file));
    try {
      runCase(tc);
      passed += 1;
      console.log(`PASS  ${tc.id}`);
    } catch (err) {
      failed += 1;
      const msg = err instanceof Error ? err.message : String(err);
      failures.push({ id: tc.id, message: msg });
      console.log(`FAIL  ${tc.id}: ${msg}`);
    }
  }

  // Always run compose + security extras if present as cases; also enforce policy constants.
  console.log(
    JSON.stringify(
      {
        harness: 'delivery-ledger-harness',
        phase: '1B-D6A',
        total: files.length,
        passed,
        failed,
        failures,
        max_retries: MAX_RETRIES,
        max_safe_concurrency: MAX_SAFE_CONCURRENCY,
        verdict: failed === 0 ? 'D6A_OFFLINE_LEDGER_HARNESS_PASS' : 'D6A_OFFLINE_LEDGER_HARNESS_FAIL',
      },
      null,
      2,
    ),
  );
  process.exit(failed === 0 ? 0 : 1);
}

main();
