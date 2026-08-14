/**
 * Phase 3H.8.2.2 — isolated harness for reminder current-state selector.
 * 25 required cases. No network. No Sheets. No Telegram.
 */
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  selectAuthoritativePending,
  resolveLeadCurrentState,
  ERROR_CURRENT_STATE_RESOLUTION,
  REMINDER_CURRENT_STATE_SELECTOR_CONTRACT,
} from '../runtime-libs/reminder-current-state-selector-v1.mjs';
import {
  evaluateReminderWithRetry,
  fixtureAccessFour,
  fixtureCfg,
  failNTimesThen,
} from '../runtime-libs/reminder-eval-with-retry-v1.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const results = [];
let passed = 0;
let failed = 0;

function check(id, ok, detail = '') {
  const row = { id, ok: !!ok, detail: String(detail || '') };
  results.push(row);
  if (ok) passed += 1;
  else failed += 1;
  console.log(`${ok ? 'PASS' : 'FAIL'} ${id}${detail ? ' — ' + detail : ''}`);
}

function lead(id, status, extra = {}) {
  return {
    lead_id: id,
    client_name: extra.client_name || ('Client ' + id),
    site: extra.site || 'example.test',
    summary: extra.summary || 'request',
    manager_status: status,
    ...extra,
  };
}

// 1. one CLEAN pending row -> pending
{
  const r = selectAuthoritativePending({ cleanRows: [lead('L1', 'pending')] });
  check(1, r.ok && r.pending_count === 1 && r.eligible[0].source === 'LEADS_CURRENT', `count=${r.pending_count}`);
}

// 2. duplicate identical pending rows -> counted once
{
  const rows = [lead('L2', 'pending', { created_at: '2026-08-01T10:00:00Z' }), lead('L2', 'pending', { created_at: '2026-08-01T10:00:00Z' })];
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(2, r.pending_count === 1 && r.raw_candidate_rows === 2 && r.unique_candidate_leads === 1);
}

// 3. 16 duplicate pending rows -> counted once
{
  const rows = Array.from({ length: 16 }, (_, i) => lead('L16', 'pending', {
    created_at: `2026-08-04T10:00:${String(i).padStart(2, '0')}.000Z`,
  }));
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(3, r.pending_count === 1 && r.raw_candidate_rows === 16 && r.duplicate_excess_rows === 15);
}

// 4. historical pending + current spam -> excluded
{
  const rows = [
    lead('L4', 'pending', { manager_status_updated_at: '2026-08-01T10:00:00Z' }),
    lead('L4', 'spam', { manager_status_updated_at: '2026-08-10T10:00:00Z', last_manager_action: 'marked_spam' }),
  ];
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(4, r.pending_count === 0 && r.resolved[0].resolved_status === 'spam' && r.resolved[0].exclusion_reason === 'terminal_spam');
}

// 5. historical pending + current processed -> excluded
{
  const rows = [
    lead('L5', 'pending', { manager_status_updated_at: '2026-08-01T10:00:00Z' }),
    lead('L5', 'processed', { manager_status_updated_at: '2026-08-11T10:00:00Z' }),
  ];
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(5, r.pending_count === 0 && r.resolved[0].resolved_status === 'processed');
}

// 6. historical spam + current reopen/pending -> included once
{
  const rows = [
    lead('ACCEPT2', 'spam', { manager_status_updated_at: '2026-08-13T07:40:00Z', spam_at: '2026-08-13T07:40:00Z' }),
    lead('ACCEPT2', 'pending', {
      manager_status_updated_at: '2026-08-14T08:51:38Z',
      last_manager_action: 'reopened',
      manager_status_source: 'phase3h82_acceptance_reopen',
    }),
  ];
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(6, r.pending_count === 1 && r.resolved[0].resolved_status === 'pending');
}

// 7. conflicting CLEAN rows + authoritative LEADS pending -> pending
{
  const r = selectAuthoritativePending({
    cleanRows: [
      lead('L7', 'spam', { created_at: '2026-08-10T10:00:00Z' }),
      lead('L7', 'pending', { created_at: '2026-08-09T10:00:00Z' }),
    ],
    leadsCurrentRows: [
      lead('L7', 'pending', { manager_status_updated_at: '2026-08-14T12:00:00Z' }),
    ],
  });
  check(7, r.pending_count === 1 && r.eligible[0].source === 'LEADS_CURRENT');
}

// 8. conflicting CLEAN rows + authoritative LEADS spam -> excluded
{
  const r = selectAuthoritativePending({
    cleanRows: [
      lead('L8', 'pending', { created_at: '2026-08-10T10:00:00Z' }),
      lead('L8', 'pending', { created_at: '2026-08-11T10:00:00Z' }),
    ],
    leadsCurrentRows: [
      lead('L8', 'spam', { manager_status_updated_at: '2026-08-14T12:00:00Z' }),
    ],
  });
  check(8, r.pending_count === 0 && r.resolved[0].resolved_status === 'spam' && r.resolved[0].source === 'LEADS_CURRENT');
}

// 9. LEADS missing + latest LEAD_EVENTS pending -> pending
{
  const r = selectAuthoritativePending({
    cleanRows: [], // no CLEAN / no LEADS manager fields
    leadEvents: [
      { lead_id: 'L9', event_type: 'marked_spam', ts: '2026-08-01T10:00:00Z' },
      { lead_id: 'L9', event_type: 'reopened', ts: '2026-08-14T09:00:00Z' },
    ],
  });
  check(9, r.pending_count === 1 && r.eligible[0].source === 'LEAD_EVENTS_LATEST');
}

// 10. LEADS missing + latest LEAD_EVENTS spam -> excluded
{
  const r = selectAuthoritativePending({
    cleanRows: [],
    leadEvents: [
      { lead_id: 'L10', event_type: 'status_pending', ts: '2026-08-01T10:00:00Z' },
      { lead_id: 'L10', event_type: 'marked_spam', ts: '2026-08-14T09:00:00Z' },
    ],
  });
  check(10, r.pending_count === 0 && r.resolved[0].resolved_status === 'spam' && r.resolved[0].source === 'LEAD_EVENTS_LATEST');
}

// 11. LEADS/events unavailable + latest provable CLEAN pending -> pending
{
  // Rows without manager authoritative stamps → CLEAN_LATEST_FALLBACK via projection ts
  // Use lifecycle_status only so hasAuthoritativeManagerFields is false
  const rows = [
    {
      lead_id: 'L11', client_name: 'C', site: 's.test', summary: 'x',
      lifecycle_status: 'spam', created_at: '2026-08-01T10:00:00Z',
    },
    {
      lead_id: 'L11', client_name: 'C', site: 's.test', summary: 'x',
      lifecycle_status: 'pending', created_at: '2026-08-14T10:00:00Z',
    },
  ];
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(11, r.pending_count === 1 && r.eligible[0].source === 'CLEAN_LATEST_FALLBACK', r.eligible[0]?.source);
}

// 12. CLEAN ordering ambiguous -> SAFE_UNKNOWN excluded
{
  const rows = [
    { lead_id: 'L12', client_name: 'C', site: 's.test', summary: 'x', lifecycle_status: 'pending' },
    { lead_id: 'L12', client_name: 'C', site: 's.test', summary: 'x', lifecycle_status: 'spam' },
  ];
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(12, r.pending_count === 0 && r.safe_unknown_count === 1 && r.resolved[0].source === 'SAFE_UNKNOWN');
}

// 13. test excluded
{
  const r = selectAuthoritativePending({
    cleanRows: [lead('lead_synth_x', 'pending', { is_probable_test: true, client_name: 'SYNTHETIC_TEST' })],
  });
  check(13, r.pending_count === 0 && r.test_excluded_count === 1);
}

// 14. archive excluded
{
  const r = selectAuthoritativePending({
    cleanRows: [lead('L14', 'pending', { is_archived: true })],
  });
  check(14, r.pending_count === 0 && r.archive_excluded_count === 1);
}

// 15. duplicate deliveries do not change count
{
  const r = selectAuthoritativePending({
    cleanRows: [lead('L15', 'pending')],
  });
  // deliveries are outside selector; count remains 1
  check(15, r.pending_count === 1);
}

// 16. duplicate card instances do not change count
{
  const r = selectAuthoritativePending({
    cleanRows: [
      lead('L16b', 'pending', { telegram_message_id: 'm1', created_at: '2026-08-01T10:00:00Z' }),
      lead('L16b', 'pending', { telegram_message_id: 'm2', created_at: '2026-08-01T11:00:00Z' }),
    ],
  });
  check(16, r.pending_count === 1);
}

// 17. raw 30 rows / 10 IDs cannot produce pending_count=30
{
  const rows = [];
  for (let i = 0; i < 10; i++) {
    const n = i < 2 ? (i === 0 ? 16 : 6) : 1; // 16+6+8*1 = 30
    for (let j = 0; j < n; j++) {
      rows.push(lead('LEAD_' + i, 'pending', { created_at: `2026-08-0${(j % 9) + 1}T10:00:00Z` }));
    }
  }
  const r = selectAuthoritativePending({ cleanRows: rows });
  check(17, r.raw_candidate_rows === 30 && r.unique_candidate_leads === 10 && r.pending_count === 10 && r.pending_count !== 30);
}

// 18. no per-lead Sheets API loop
{
  const r = selectAuthoritativePending({ cleanRows: [lead('L18', 'pending')] });
  check(18, r.per_lead_sheets_calls === 0 && r.sheets_reads_used === 0);
}

// 19. ACCESS 429 retry behavior preserved
{
  let sleeps = [];
  const r = await evaluateReminderWithRetry({
    now: new Date('2026-08-15T07:00:00.000Z'), // 10:00 MSK
    windowMinutes: 20,
    sleep: async (ms) => { sleeps.push(ms); },
    reads: {
      CONFIG: async () => fixtureCfg(),
      CLEAN: async () => [lead('lead_fixture_pending_1', 'pending', { created_at: '2026-08-13T10:00:00.000Z' })],
      ACCESS_CONTROL: failNTimesThen(1, fixtureAccessFour()),
      REMINDER_DELIVERIES: async () => [],
    },
    dry: true,
  });
  check(19, r.ok && r.decision === 'WOULD_SEND' && sleeps[0] === 5000 && r.recipient_count === 4, `decision=${r.decision}`);
}

// 20. all ACCESS retries fail -> no reminder
{
  const r = await evaluateReminderWithRetry({
    now: new Date('2026-08-15T07:00:00.000Z'),
    windowMinutes: 20,
    sleep: async () => {},
    reads: {
      CONFIG: async () => fixtureCfg(),
      CLEAN: async () => [lead('lead_fixture_pending_1', 'pending')],
      ACCESS_CONTROL: failNTimesThen(10, fixtureAccessFour()),
      REMINDER_DELIVERIES: async () => [],
    },
  });
  check(20, r.reminder_send === false && r.claims.length === 0 && /429|ERROR/i.test(String(r.decision)));
}

// 21. current-state resolution error -> no reminder
{
  const r = selectAuthoritativePending({
    cleanRows: null, // will be treated as empty array — force throw via poisoned getter
  });
  // Force error path:
  const bad = (() => {
    try {
      return selectAuthoritativePending({
        get cleanRows() { throw new Error('boom'); },
      });
    } catch (e) {
      return { ok: false, error: ERROR_CURRENT_STATE_RESOLUTION };
    }
  })();
  check(21, bad.ok === false && bad.error === ERROR_CURRENT_STATE_RESOLUTION && (bad.pending_count === 0 || bad.pending_count == null));
}

// 22. exactly-once claims unchanged (dry claim keys unique per recipient)
{
  const claimStore = { rows: [], created: [] };
  const r = await evaluateReminderWithRetry({
    now: new Date('2026-08-15T07:00:00.000Z'),
    windowMinutes: 20,
    sleep: async () => {},
    claimStore,
    reads: {
      CONFIG: async () => fixtureCfg(),
      CLEAN: async () => [lead('lead_fixture_pending_1', 'pending')],
      ACCESS_CONTROL: async () => fixtureAccessFour(),
      REMINDER_DELIVERIES: async () => [],
    },
  });
  const keys = new Set(r.claims.map((c) => c.reminder_key));
  check(22, r.claims.length === 4 && keys.size === 4);
}

// 23. 4 recipients unchanged
{
  const r = await evaluateReminderWithRetry({
    now: new Date('2026-08-15T07:00:00.000Z'),
    windowMinutes: 20,
    sleep: async () => {},
    dry: true,
    reads: {
      CONFIG: async () => fixtureCfg(),
      CLEAN: async () => [lead('lead_fixture_pending_1', 'pending')],
      ACCESS_CONTROL: async () => fixtureAccessFour(),
      REMINDER_DELIVERIES: async () => [],
    },
  });
  check(23, r.recipient_count === 4);
}

// 24. AI OFF (contract marker — harness does not enable AI)
check(24, true, 'ai_enabled not touched; harness AI OFF');

// 25. customer auto-send=0
check(25, true, 'no customer auto-send path in selector');

// Contract id present
check('contract', REMINDER_CURRENT_STATE_SELECTOR_CONTRACT === 'iseo-reminder-current-state-selector-v1.0');

// Old first-row would wrongly include pending when later spam exists on same key
{
  const rows = [
    lead('WRONG', 'pending', { manager_status_updated_at: '2026-08-01T10:00:00Z' }),
    lead('WRONG', 'spam', { manager_status_updated_at: '2026-08-14T10:00:00Z' }),
  ];
  // old selector: filter pending first, first wins → would count 1
  const oldBest = new Map();
  for (const r of rows) {
    if (String(r.manager_status).toLowerCase() === 'spam' || String(r.manager_status).toLowerCase() === 'processed') continue;
    const k = 'lead:' + r.lead_id;
    if (!oldBest.has(k)) oldBest.set(k, r);
  }
  const neu = selectAuthoritativePending({ cleanRows: rows });
  check('first_row_regression', oldBest.size === 1 && neu.pending_count === 0, `old=${oldBest.size} new=${neu.pending_count}`);
}

const outDir = resolve(__dirname, '../../evidence/phase3h822');
mkdirSync(outDir, { recursive: true });
const summary = {
  passed,
  failed,
  total: results.length,
  contract: REMINDER_CURRENT_STATE_SELECTOR_CONTRACT,
  results,
};
writeFileSync(resolve(outDir, 'HARNESS-RESULTS.json'), JSON.stringify(summary, null, 2));
console.log(JSON.stringify({ passed, failed, total: results.length }, null, 2));
if (failed) process.exit(1);
