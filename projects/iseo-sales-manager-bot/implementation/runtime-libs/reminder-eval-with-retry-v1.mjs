/**
 * Reminder pre-decision evaluation with per-logical-read 429 retry.
 * Isolated harness / documentation mirror. No production mutations unless callers inject them.
 */
import {
  isReminderWindowDue,
  reminderDeliveryKey,
  selectActiveStaffRecipients,
  formatReminderMessage,
  buildPendingView,
} from './pending-leads-lib.mjs';
import {
  readWith429Retry,
  classifySheetsError,
  errorObservability,
  decisionForSheetsError,
  SHEETS_429_RETRY_CONTRACT,
} from './sheets-429-retry-v1.mjs';
import {
  selectAuthoritativePending,
  ERROR_CURRENT_STATE_RESOLUTION,
  REMINDER_CURRENT_STATE_SELECTOR_CONTRACT,
} from './reminder-current-state-selector-v1.mjs';

export { SHEETS_429_RETRY_CONTRACT, REMINDER_CURRENT_STATE_SELECTOR_CONTRACT };

const CLAIMABLE = new Set(['claimed', 'delivered', 'sent', 'reconcile']);

function cfgMap(rows) {
  const map = {};
  for (const r of rows || []) {
    const k = String(r.key || r.KEY || r.config_key || '').trim();
    if (!k) continue;
    map[k] = r.value ?? r.VALUE ?? r.config_value ?? '';
  }
  return map;
}

export async function evaluateReminderWithRetry(input = {}) {
  const now = input.now instanceof Date ? input.now : new Date(input.now || Date.now());
  const nowIso = now.toISOString();
  const reads = input.reads || {};
  const retryOpts = {
    maxAttempts: input.maxAttempts,
    sleep: input.sleep,
  };
  const cache = {};
  const retryLog = {};
  const claimStore = input.claimStore || { rows: [], created: [] };
  const sendLog = input.sendLog || [];
  const configWrites = [];
  const errorsWrites = [];

  async function logicalRead(stage, fn) {
    if (cache[stage] && input.reusePerExecution !== false) {
      return { ok: true, value: cache[stage], attempt: 0, retries: 0, reused: true, stage };
    }
    const result = await readWith429Retry(fn, { ...retryOpts, stage });
    cache[stage] = result.value;
    retryLog[stage] = { attempts: result.attempts, retries: result.retries, delaysMs: result.delaysMs };
    return result;
  }

  function stampError(err, stage, pendingCount = 'not_computed') {
    const obs = errorObservability(err, {
      stage,
      nowIso,
      businessDate: input.businessDate || '',
      pendingCount,
    });
    configWrites.push(obs);
    errorsWrites.push({
      at: nowIso,
      code: obs.reminder_decision,
      stage: obs.last_error_stage,
      error_class: obs.last_error_class,
      retry_attempts: obs.retry_attempts,
      message_safe: obs.last_error_safe,
    });
    return {
      ok: false,
      reminder_send: false,
      reminder_mark_window_complete: false,
      decision: obs.reminder_decision,
      last_decision: 'ERROR',
      observability: obs,
      claims: [],
      sendLog,
      configWrites,
      errorsWrites,
      retryLog,
      pending_count: pendingCount,
      recipient_count: 0,
      contract: SHEETS_429_RETRY_CONTRACT,
    };
  }

  let cfgRows;
  try {
    const r = await logicalRead('CONFIG', reads.CONFIG);
    cfgRows = r.value;
  } catch (e) {
    return stampError(e, 'CONFIG');
  }
  const cfg = { ...cfgMap(cfgRows), ...(input.cfg || {}) };
  const gate = isReminderWindowDue(now, cfg, { windowMinutes: input.windowMinutes ?? 20 });
  if (!gate.due) {
    const decision = gate.reason === 'already_completed'
      ? 'SKIPPED_ALREADY_SENT'
      : (gate.reason === 'outside_window' ? 'SKIPPED_OUTSIDE_WINDOW' : (gate.reason === 'disabled' ? 'SKIPPED_DISABLED' : 'ERROR'));
    const obs = {
      last_evaluation_at: nowIso,
      last_decision: decision,
      last_error_class: '',
      last_error_stage: '',
      last_error_at: '',
      retry_attempts: 0,
      business_date: gate.local?.date || '',
      pending_count: 'not_computed',
      reminder_send: false,
      reminder_mark_window_complete: false,
    };
    configWrites.push(obs);
    return {
      ok: true,
      reminder_send: false,
      decision,
      observability: obs,
      claims: [],
      sendLog,
      configWrites,
      errorsWrites,
      retryLog,
      pending_count: 'not_computed',
      recipient_count: 0,
      gate,
    };
  }

  let cleanRows;
  try {
    const r = await logicalRead('CLEAN', reads.CLEAN);
    cleanRows = r.value;
  } catch (e) {
    return stampError(e, 'CLEAN');
  }

  let leadsRows = [];
  let eventRows = [];
  if (typeof reads.LEADS_CURRENT === 'function') {
    try {
      const r = await logicalRead('LEADS_CURRENT', reads.LEADS_CURRENT);
      leadsRows = r.value || [];
    } catch (e) {
      return stampError(e, 'LEADS_CURRENT');
    }
  }
  if (typeof reads.LEAD_EVENTS === 'function') {
    try {
      const r = await logicalRead('LEAD_EVENTS', reads.LEAD_EVENTS);
      eventRows = r.value || [];
    } catch (e) {
      // Events are priority-2 fallback only; CLEAN/LEADS may still resolve. Fail closed only if caller requires events.
      if (input.requireLeadEvents === true) return stampError(e, 'LEAD_EVENTS');
      eventRows = [];
    }
  }

  const selection = selectAuthoritativePending({
    cleanRows,
    leadsCurrentRows: leadsRows,
    leadEvents: eventRows,
    includeTests: String(cfg.pending_reminder_include_tests || 'false') === 'true',
    includeArchive: String(cfg.pending_reminder_include_archive || 'false') === 'true',
  });
  if (!selection.ok) {
    const out = stampError(new Error(ERROR_CURRENT_STATE_RESOLUTION), 'CURRENT_STATE', 'not_computed');
    out.decision = ERROR_CURRENT_STATE_RESOLUTION;
    out.observability.reminder_decision = ERROR_CURRENT_STATE_RESOLUTION;
    out.observability.last_error_class = ERROR_CURRENT_STATE_RESOLUTION;
    out.observability.last_error_stage = 'CURRENT_STATE';
    out.selection = selection;
    return out;
  }

  // Message age helpers still use pending view over eligible CLEAN rows only.
  const view = buildPendingView(
    selection.eligible.map((e) => {
      const id = String(e.lead_id || '').replace(/^lead:/, '').replace(/^stable:/, '').replace(/^gmail:/, '');
      return (cleanRows || []).find((r) => String(r.lead_id || '') === id || String(r.stable_lead_ref || '') === id) || {
        lead_id: id,
        manager_status: 'pending',
        client_name: 'lead',
        site: 'n/a',
        summary: 'pending',
      };
    }),
    {
      includeTests: String(cfg.pending_reminder_include_tests || 'false') === 'true',
      nowMs: now.getTime(),
    },
  );
  const pendingCount = selection.pending_count;
  const minCount = Number(cfg.pending_reminder_min_count || 1);

  let accessRows;
  try {
    const r = await logicalRead('ACCESS_CONTROL', reads.ACCESS_CONTROL);
    accessRows = r.value;
  } catch (e) {
    const out = stampError(e, 'ACCESS_CONTROL', 'not_computed');
    out.decision = classifySheetsError(e).errorClass === 'SHEETS_429'
      ? 'ERROR_SHEETS_429_ACCESS'
      : decisionForSheetsError(e);
    out.observability.reminder_decision = out.decision;
    return out;
  }

  const recipients = selectActiveStaffRecipients(accessRows);
  if (!recipients.length) {
    const obs = {
      last_evaluation_at: nowIso,
      last_decision: 'ERROR',
      last_error_class: 'NO_RECIPIENTS',
      last_error_stage: 'ACCESS_CONTROL',
      last_error_at: nowIso,
      last_error_safe: 'нет активных получателей',
      retry_attempts: retryLog.ACCESS_CONTROL?.attempts || 0,
      business_date: gate.local.date,
      pending_count: pendingCount,
      reminder_send: false,
      reminder_mark_window_complete: false,
    };
    configWrites.push(obs);
    return {
      ok: false,
      decision: 'ERROR',
      reminder_send: false,
      observability: obs,
      claims: [],
      sendLog,
      configWrites,
      errorsWrites,
      retryLog,
      pending_count: pendingCount,
      recipient_count: 0,
    };
  }

  if (pendingCount < minCount) {
    const decision = 'SKIPPED_ZERO_PENDING';
    const obs = {
      last_evaluation_at: nowIso,
      last_decision: decision,
      last_error_class: '',
      last_error_stage: '',
      last_error_at: '',
      retry_attempts: 0,
      business_date: gate.local.date,
      pending_count: pendingCount,
      reminder_send: false,
      reminder_mark_window_complete: false,
    };
    configWrites.push(obs);
    return {
      ok: true,
      decision,
      reminder_send: false,
      observability: obs,
      claims: [],
      sendLog,
      configWrites,
      errorsWrites,
      retryLog,
      pending_count: pendingCount,
      recipient_count: recipients.length,
      gate,
    };
  }

  let ledgerRows;
  try {
    const r = await logicalRead('REMINDER_DELIVERIES', reads.REMINDER_DELIVERIES || (async () => claimStore.rows));
    ledgerRows = r.value;
  } catch (e) {
    return stampError(e, 'REMINDER_DELIVERIES', pendingCount);
  }

  const claimed = new Set();
  for (const row of ledgerRows || []) {
    if (String(row.reminder_window || '') !== gate.windowKey) continue;
    const st = String(row.status || '').toLowerCase();
    if (CLAIMABLE.has(st)) claimed.add(String(row.reminder_key || ''));
  }

  const replyText = formatReminderMessage(view);
  const claims = [];
  for (const rec of recipients) {
    const reminder_key = reminderDeliveryKey(gate.windowKey, rec.recipient_ref);
    if (claimed.has(reminder_key)) continue;
    claims.push({
      reminder_send: true,
      reminder_window: gate.windowKey,
      reminder_key,
      recipient_ref: rec.recipient_ref,
      role_snapshot: rec.role_snapshot,
      chat_id: rec.delivery_chat_id,
      reply_text: replyText,
      pending_count_snapshot: pendingCount,
      claimed_at: nowIso,
      status: 'claimed',
    });
  }

  if (input.dry === true) {
    return {
      ok: true,
      decision: claims.length ? 'WOULD_SEND' : 'SKIPPED_ALREADY_SENT',
      reminder_send: false,
      claims,
      pending_count: pendingCount,
      recipient_count: recipients.length,
      retryLog,
      gate,
      sendLog,
      configWrites,
      errorsWrites,
    };
  }

  const created = [];
  for (const claim of claims) {
    if (claimStore.rows.some((r) => r.reminder_key === claim.reminder_key && CLAIMABLE.has(String(r.status || '').toLowerCase()))) {
      continue;
    }
    claimStore.rows.push({ ...claim });
    claimStore.created.push(claim.reminder_key);
    created.push(claim);
    if (typeof input.sendFn === 'function') {
      const sent = await input.sendFn(claim);
      sendLog.push({ reminder_key: claim.reminder_key, ok: sent !== false, at: nowIso });
      const row = claimStore.rows.find((r) => r.reminder_key === claim.reminder_key);
      if (row) {
        row.status = sent === false ? 'claim_send_failed' : 'delivered';
        row.sent_at = sent === false ? '' : nowIso;
      }
    } else {
      sendLog.push({ reminder_key: claim.reminder_key, ok: true, at: nowIso, simulated: true });
      const row = claimStore.rows.find((r) => r.reminder_key === claim.reminder_key);
      if (row) {
        row.status = 'delivered';
        row.sent_at = nowIso;
      }
    }
  }

  const successes = sendLog.filter((s) => s.ok).length;
  const markComplete = successes > 0 && created.length > 0;
  const decision = created.length === 0 ? 'SKIPPED_ALREADY_SENT' : 'SENT';
  const obs = {
    last_evaluation_at: nowIso,
    last_decision: decision,
    last_error_class: '',
    last_error_stage: '',
    last_error_at: '',
    retry_attempts: Object.values(retryLog).reduce((n, x) => n + (x.retries || 0), 0),
    business_date: gate.local.date,
    pending_count: pendingCount,
    reminder_send: created.length > 0,
    reminder_mark_window_complete: markComplete,
    last_successful_send: markComplete ? nowIso : '',
    sent_date: markComplete ? gate.windowKey : '',
    sent_recipient_count: markComplete ? String(successes) : '',
  };
  configWrites.push(obs);

  return {
    ok: true,
    decision,
    reminder_send: created.length > 0,
    reminder_mark_window_complete: markComplete,
    claims: created,
    pending_count: pendingCount,
    recipient_count: recipients.length,
    successes,
    duplicates: 0,
    retryLog,
    gate,
    sendLog,
    configWrites,
    errorsWrites,
    observability: obs,
    contract: SHEETS_429_RETRY_CONTRACT,
  };
}

export function fixtureAccessFour() {
  return [
    { role: 'admin', status: 'active', telegram_user_id: '1001', telegram_user_hash: 'r:admin', display_name: 'ADMIN_A' },
    { role: 'moderator', status: 'active', telegram_user_id: '1002', telegram_user_hash: 'r:mod-a', display_name: 'MOD_A' },
    { role: 'moderator', status: 'active', telegram_user_id: '1003', telegram_user_hash: 'r:mod-b', display_name: 'MOD_B' },
    { role: 'moderator', status: 'active', telegram_user_id: '1004', telegram_user_hash: 'r:mod-c', display_name: 'MOD_C' },
  ];
}

export function fixtureCfg(extra = {}) {
  return [{
    key: 'pending_reminders_enabled', value: 'true',
  }, {
    key: 'pending_reminder_time', value: '10:00',
  }, {
    key: 'pending_reminder_timezone', value: 'Europe/Moscow',
  }, {
    key: 'pending_reminder_min_count', value: '1',
  }, {
    key: 'pending_reminder_include_tests', value: 'false',
  }, {
    key: 'pending_reminder_include_archive', value: 'false',
  }, {
    key: 'pending_reminder_last_window', value: '',
  }, ...Object.entries(extra).map(([key, value]) => ({ key, value }))];
}

export function fixturePendingLead() {
  return [{
    lead_id: 'lead_fixture_pending_1',
    client_name: 'Fixture Pending',
    site: 'example.test',
    summary: 'isolated harness pending',
    manager_status: 'pending',
    created_at: '2026-08-13T10:00:00.000Z',
  }];
}

export function fixtureZeroPending() {
  return [{
    lead_id: 'lead_fixture_spam_1',
    client_name: 'Fixture Spam',
    site: 'example.test',
    summary: 'isolated harness spam',
    manager_status: 'spam',
    created_at: '2026-08-13T10:00:00.000Z',
  }];
}

export function failNTimesThen(n, value, httpStatus = 429) {
  let left = n;
  return async () => {
    if (left > 0) {
      left -= 1;
      const err = new Error(
        httpStatus === 429
          ? 'The service is receiving too many requests from you'
          : `Google Sheets API HTTP ${httpStatus}`,
      );
      err.httpStatus = httpStatus;
      throw err;
    }
    return value;
  };
}
