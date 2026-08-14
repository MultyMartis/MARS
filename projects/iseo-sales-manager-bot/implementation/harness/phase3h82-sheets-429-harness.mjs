/**
 * Phase 3H.8.2 — isolated reminder 429 / exactly-once / zero-pending / one-pending harness.
 * No production customer data. No live Telegram. No live Sheets.
 */
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  evaluateReminderWithRetry,
  fixtureAccessFour,
  fixtureCfg,
  fixturePendingLead,
  fixtureZeroPending,
  failNTimesThen,
} from '../runtime-libs/reminder-eval-with-retry-v1.mjs';
import { formatReminderErrorStatusLines } from '../runtime-libs/sheets-429-retry-v1.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const OUT = resolve(__dirname, '../../evidence/phase3h82');
mkdirSync(OUT, { recursive: true });

const WINDOW_NOW = new Date('2026-08-15T07:00:10.000Z'); // 10:00:10 Europe/Moscow
const delays = [];
const sleep = async (ms) => { delays.push(ms); };

function accessReads(failCount = 0, status = 429) {
  return failNTimesThen(failCount, fixtureAccessFour(), status);
}

async function runCase(name, extra) {
  delays.length = 0;
  const claimStore = extra.claimStore || { rows: [], created: [] };
  const sendLog = extra.sendLog || [];
  const result = await evaluateReminderWithRetry({
    now: extra.now || WINDOW_NOW,
    sleep,
    claimStore,
    sendLog,
    reads: {
      CONFIG: extra.reads?.CONFIG || (async () => fixtureCfg()),
      CLEAN: extra.reads?.CLEAN || (async () => fixturePendingLead()),
      ACCESS_CONTROL: extra.reads?.ACCESS_CONTROL || accessReads(0),
      REMINDER_DELIVERIES: extra.reads?.REMINDER_DELIVERIES || (async () => claimStore.rows),
    },
    sendFn: extra.sendFn,
    dry: extra.dry,
    maxAttempts: extra.maxAttempts,
  });
  return { name, delays: delays.slice(), result, claimStore, sendLog };
}

const results = [];
const checks = [];
function check(id, ok, detail) {
  checks.push({ id, ok: !!ok, detail: detail || '' });
}

// A. first 429 then success
{
  const r = await runCase('A_one_429_then_success', { reads: { ACCESS_CONTROL: accessReads(1) } });
  results.push(r);
  check(6, r.result.decision === 'SENT' && r.result.pending_count === 1 && r.result.recipient_count === 4, 'resume after one 429');
  check(5, r.result.retryLog.ACCESS_CONTROL.retries === 1, 'one retry');
  check(12, r.result.claims.length === 4, 'claims 4');
  check(15, r.result.successes === 4, 'successes 4');
}

// B. two 429 then success
{
  const r = await runCase('B_two_429_then_success', { reads: { ACCESS_CONTROL: accessReads(2) } });
  results.push(r);
  check(7, r.result.decision === 'SENT' && r.result.claims.length === 4 && r.result.retryLog.ACCESS_CONTROL.retries === 2, 'two 429 recover');
}

// C. all retries 429
{
  const r = await runCase('C_all_retries_fail', { reads: { ACCESS_CONTROL: accessReads(9) } });
  results.push(r);
  check(8, r.result.decision === 'ERROR_SHEETS_429_ACCESS', 'ERROR_SHEETS_429_ACCESS');
  check(10, r.result.retryLog.ACCESS_CONTROL == null && r.result.observability.retry_attempts === 4, 'bounded 4 attempts');
  check(11, r.result.claims.length === 0 && r.result.sendLog.length === 0, 'no claims/sends');
  check(17, r.result.observability.reminder_mark_window_complete === false && !r.result.observability.sent_date, 'date not poisoned');
}

// D. non-429 fatal — no quota loop
{
  const r = await runCase('D_non429_fatal', {
    reads: {
      ACCESS_CONTROL: failNTimesThen(9, fixtureAccessFour(), 500),
    },
  });
  results.push(r);
  const attempts = r.result.observability.retry_attempts;
  check(9, r.result.last_decision === 'ERROR' && r.result.decision === 'ERROR' && attempts === 1, 'non-429 no retry loop');
  check(11, r.result.claims.length === 0, 'non-429 no claims');
}

// E. success first attempt — no delay
{
  const r = await runCase('E_first_attempt_success', {});
  results.push(r);
  check(5, r.result.retryLog.ACCESS_CONTROL.retries === 0 && r.delays.length === 0, 'no unnecessary delay');
}

// Exactly-once under retry: recover then second eval same date
{
  const claimStore = { rows: [], created: [] };
  const sendLog = [];
  const r1 = await runCase('F_retry_then_send', {
    claimStore, sendLog,
    reads: { ACCESS_CONTROL: accessReads(1) },
  });
  const r2 = await runCase('F_second_eval_same_window', {
    claimStore, sendLog,
    reads: { ACCESS_CONTROL: accessReads(0) },
  });
  results.push(r1, r2);
  check(12, r1.result.claims.length === 4, 'first claims 4');
  check(13, r2.result.claims.length === 0, 'second eval 0 additional claims');
  check(16, r2.result.decision === 'SKIPPED_ALREADY_SENT' || r2.result.claims.length === 0, 'no duplicate sends');
  const keys = claimStore.rows.map((x) => x.reminder_key);
  check(13, new Set(keys).size === keys.length, 'no duplicate recipient rows');
}

// Failed run does not poison date — subsequent eval can still send
{
  const claimStore = { rows: [], created: [] };
  const fail = await runCase('G_fail_then_recover_eval1', {
    claimStore,
    reads: { ACCESS_CONTROL: accessReads(9) },
  });
  const ok = await runCase('G_fail_then_recover_eval2', {
    claimStore,
    reads: { ACCESS_CONTROL: accessReads(0) },
  });
  results.push(fail, ok);
  check(17, fail.result.observability.reminder_mark_window_complete === false && ok.result.decision === 'SENT' && ok.result.claims.length === 4, 'failed run does not poison date');
}

// Zero pending
{
  const r = await runCase('H_zero_pending', {
    reads: { CLEAN: async () => fixtureZeroPending(), ACCESS_CONTROL: accessReads(0) },
  });
  results.push(r);
  check(14, r.result.decision === 'SKIPPED_ZERO_PENDING' && r.result.claims.length === 0 && r.result.sendLog.length === 0, 'zero pending zero sends');
}

// One pending four recipients
{
  const r = await runCase('I_one_pending_four', {});
  results.push(r);
  check(15, r.result.pending_count === 1 && r.result.recipient_count === 4 && r.result.claims.length === 4 && r.result.successes === 4, 'one pending 4/4');
}

// Observability + reminder_status lines
{
  const r = await runCase('J_status_error_lines', { reads: { ACCESS_CONTROL: accessReads(9) } });
  results.push(r);
  const lines = formatReminderErrorStatusLines(r.result.observability);
  check(18, r.result.observability.last_evaluation_at && r.result.observability.last_decision === 'ERROR', 'last evaluation recorded');
  check(19, r.result.observability.retry_attempts === 4, 'retry count recorded');
  check(20, r.result.observability.last_error_stage === 'ACCESS_CONTROL', 'error stage recorded');
  check(21, lines.decisionLine === 'Ошибка' && lines.reasonLine === 'лимит Google Sheets API' && lines.stageLine === 'ACCESS_CONTROL', '/reminder_status error truth');
}

const summary = {
  contract: 'iseo-sheets-429-retry-v1.0',
  window_now: WINDOW_NOW.toISOString(),
  checks,
  pass: checks.filter((c) => c.ok).length,
  fail: checks.filter((c) => !c.ok).length,
  cases: results.map((r) => ({
    name: r.name,
    decision: r.result.decision,
    pending_count: r.result.pending_count,
    recipient_count: r.result.recipient_count,
    claims: r.result.claims?.length || 0,
    sends: r.result.sendLog?.length || 0,
    successes: r.result.successes || 0,
    retries: r.result.retryLog,
    delays: r.delays,
    last_decision: r.result.observability?.last_decision || r.result.last_decision,
    error_class: r.result.observability?.last_error_class,
    mark_complete: r.result.observability?.reminder_mark_window_complete,
  })),
};

writeFileSync(resolve(OUT, 'HARNESS-RESULTS.json'), JSON.stringify(summary, null, 2));
console.log(JSON.stringify({ pass: summary.pass, fail: summary.fail, total: checks.length, failed: checks.filter((c) => !c.ok) }, null, 2));
if (summary.fail) process.exit(1);
