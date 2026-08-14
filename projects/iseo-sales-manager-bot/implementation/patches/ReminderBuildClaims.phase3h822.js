// Phase 3H.8.2.2 — Reminder Build Claims + iseo-reminder-current-state-selector-v1.0
// Phase 3H.8 — authoritative CLEAN sheet is lead_clean_v2 (manager_status = LEADS current-state).
// Resolves: unique lead_id → authoritative current status → reminder eligibility.
// NOT first CLEAN pending row wins. Bulk only — per-lead Sheets API calls = 0.
// Inputs: gate + CLEAN + ACCESS_CONTROL + REMINDER_DELIVERIES (same reads as 3H.8.2).
// Fail closed: ERROR_CURRENT_STATE_RESOLUTION → claims=0, no send, no day stamp.

const gate = $('Reminder Schedule Gate').first().json;
if (!gate.reminder_proceed) {
  return [{ json: { ...gate, reminder_send: false } }];
}

const cleanRows = $('Read CLEAN for Reminder').all().map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error);
const accessRows = $('Read ACCESS_CONTROL for Reminder').all().map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error);
const ledgerRows = $('Read REMINDER_DELIVERIES').all().map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error);

const accessErr = $('Read ACCESS_CONTROL for Reminder').all().some((i) => i.json && i.json.error);
const ledgerErr = $('Read REMINDER_DELIVERIES').all().some((i) => i.json && i.json.error);
if (accessErr) {
  return [{ json: { reminder_send: false, reminder_skip_reason: 'access_read_error', reminder_window: gate.reminder_window } }];
}
if (ledgerErr) {
  return [{ json: { reminder_send: false, reminder_skip_reason: 'ledger_read_error', reminder_window: gate.reminder_window } }];
}

const includeTests = gate.pending_reminder_include_tests === true;
const includeArchive = gate.pending_reminder_include_archive === true;
const nowMs = Date.now();
const CONTRACT = 'iseo-reminder-current-state-selector-v1.0';

function isTest(r) {
  const marker = String(r.phase_marker || r.marker || '');
  const name = String(r.client_name || '');
  const summary = String(r.summary || '');
  const leadId = String(r.lead_id || '');
  const flag = String(r.is_probable_test ?? '').toLowerCase();
  if (flag === 'true' || flag === '1' || r.is_probable_test === true) return true;
  if (r.__synthetic === true || r.synthetic_fixture === true || r.fixture_id) return true;
  if (String(r.marker || '') === 'SYNTHETIC_TEST') return true;
  if (/SYNTHETIC_TEST/i.test(name)) return true;
  if (/PHASE_3/i.test(marker)) return true;
  if (/synthetic|synth[_ -]/i.test(leadId + ' ' + String(r.source || ''))) return true;
  if (/\b(test|synth)\b/i.test(name) || /тест/i.test(name)) return true;
  if (/phase[_\s-]?3|sheets probe|стабилизац/i.test(name + ' ' + summary + ' ' + marker)) return true;
  return false;
}
function isArchive(r) {
  if (r.is_archived === true || r.archived === true) return true;
  const a = String(r.is_archived ?? r.archive_state ?? r.archived ?? '').trim().toLowerCase();
  return a === 'true' || a === '1' || a === 'yes' || a === 'archived' || a === 'archive';
}
function isTech(r) {
  const t = String(r.row_kind || r.record_kind || r.entry_type || '').toLowerCase();
  return t === 'technical_retry' || t === 'retry_only' || t === 'tech_retry' || r.technical_retry === true;
}
function bkey(r) {
  const stable = String(r.stable_lead_ref || '').trim();
  if (stable) return 'stable:' + stable;
  const leadId = String(r.lead_id || '').trim();
  if (leadId) return 'lead:' + leadId;
  const gmail = String(r.source_message_id || '').trim();
  if (gmail) return 'gmail:' + gmail;
  return '';
}
function normStatus(raw) {
  const s = String(raw ?? '').trim().toLowerCase();
  if (!s) return '';
  if (s === 'processed' || s === 'done' || s === 'closed') return 'processed';
  if (s === 'spam') return 'spam';
  if (s === 'pending' || s === 'new' || s === 'open' || s === 'reopened' || s === 'reopen') return 'pending';
  return '';
}
function statusFromRow(r) {
  const primary = normStatus(r.manager_status);
  if (primary === 'processed' || primary === 'spam' || primary === 'pending') return primary;
  const secondary = normStatus(r.lifecycle_status);
  if (secondary === 'processed' || secondary === 'spam') return secondary;
  const close = normStatus(r.close_reason);
  if (close === 'spam' || close === 'processed') return close;
  if (String(r.manager_status || '').trim()) return 'pending';
  if (secondary === 'pending') return 'pending';
  if (!String(r.manager_status || '').trim() && !String(r.lifecycle_status || '').trim() && !String(r.close_reason || '').trim()) return '';
  return 'pending';
}
function hasAuth(r) {
  return !!(String(r.manager_status || '').trim() || String(r.manager_status_source || '').trim() || String(r.last_manager_action || '').trim() || r.manager_status_updated_at);
}
function parseTs(c) {
  if (c == null || c === '') return null;
  const d = new Date(c);
  return Number.isNaN(d.getTime()) ? null : d.getTime();
}
function authTs(r) {
  for (const c of [r.manager_status_updated_at, r.lifecycle_changed_at, r.status_changed_at, r.last_manager_action_at, r.updated_at, r.spam_at, r.processed_at, r.reopened_at, r.lead_received_at, r.received_at, r.created_at]) {
    const t = parseTs(c);
    if (t != null) return t;
  }
  return null;
}
function projTs(r) {
  for (const c of [r.updated_at, r.manager_status_updated_at, r.created_at, r.lead_received_at, r.received_at, r.processed_at]) {
    const t = parseTs(c);
    if (t != null) return t;
  }
  return null;
}
function ageDisp(mins, unk) {
  if (unk || mins == null) return 'возраст неизвестен';
  const m = Math.max(0, Math.floor(mins));
  if (m < 60) return '< 1 ч';
  const h = Math.floor(m / 60);
  if (h < 24) return h + ' ч';
  const d = Math.floor(h / 24);
  const rh = h % 24;
  return rh ? (d + ' д ' + rh + ' ч') : (d + ' д');
}
function pickLatest(rows, tsFn) {
  let bestTs = null;
  const atBest = [];
  for (const r of rows) {
    const t = tsFn(r);
    if (t == null) continue;
    if (bestTs == null || t > bestTs) { bestTs = t; atBest.length = 0; atBest.push(r); }
    else if (t === bestTs) atBest.push(r);
  }
  return { bestTs, atBest };
}
function agreeStatus(rows) {
  const statuses = [...new Set(rows.map(statusFromRow).filter(Boolean))];
  if (statuses.length === 0) return { ok: false, status: '', reason: 'no_status' };
  if (statuses.length > 1) return { ok: false, status: '', reason: 'conflict' };
  return { ok: true, status: statuses[0], reason: '' };
}

let selection;
try {
  const byKey = new Map();
  for (const r of cleanRows) {
    if (isTech(r)) continue;
    const k = bkey(r);
    if (!k) continue;
    if (!byKey.has(k)) byKey.set(k, []);
    byKey.get(k).push(r);
  }

  const resolved = [];
  for (const [leadKey, rows] of byKey.entries()) {
    const item = {
      lead_id: leadKey,
      resolved_status: '',
      source: 'SAFE_UNKNOWN',
      source_timestamp: null,
      confidence: 'SAFE_UNKNOWN_CURRENT_STATE',
      reminder_eligible: false,
      exclusion_reason: '',
      is_test: false,
      is_archive: false,
      clean_row_count: rows.length,
      sample: rows[0],
    };
    const leadsPool = rows.filter(hasAuth);
    let done = false;
    if (leadsPool.length) {
      const picked = pickLatest(leadsPool, authTs);
      let sample = leadsPool[0];
      if (picked.bestTs == null) {
        const a = agreeStatus(leadsPool);
        if (a.ok) {
          item.resolved_status = a.status;
          item.source = 'LEADS_CURRENT';
          item.confidence = 'AUTHORITATIVE_UNORDERED_UNANIMOUS';
        } else {
          item.exclusion_reason = 'leads_current_ordering_ambiguous';
          done = true;
        }
      } else {
        sample = picked.atBest[0] || sample;
        const a = agreeStatus(picked.atBest);
        if (!a.ok) {
          item.exclusion_reason = a.reason === 'conflict' ? 'leads_current_status_conflict_same_timestamp' : 'leads_current_status_unresolved';
          done = true;
        } else {
          item.resolved_status = a.status;
          item.source = 'LEADS_CURRENT';
          item.source_timestamp = picked.bestTs;
          item.confidence = 'AUTHORITATIVE';
        }
      }
      item.sample = sample;
      done = true;
    }
    if (!item.resolved_status && item.source === 'SAFE_UNKNOWN' && !item.exclusion_reason) {
      // Priority 3 CLEAN latest fallback (no separate LEAD_EVENTS read — quota-safe; events path is library/harness)
      const picked = pickLatest(rows, projTs);
      let sample = rows[0];
      if (picked.bestTs == null) {
        const a = agreeStatus(rows);
        if (a.ok) {
          item.resolved_status = a.status;
          item.source = 'CLEAN_LATEST_FALLBACK';
          item.confidence = 'CLEAN_UNORDERED_UNANIMOUS';
        } else {
          item.exclusion_reason = 'clean_ordering_ambiguous';
        }
      } else {
        sample = picked.atBest[0] || sample;
        const a = agreeStatus(picked.atBest);
        if (!a.ok) {
          item.exclusion_reason = a.reason === 'conflict' ? 'clean_status_conflict_same_timestamp' : 'clean_status_unresolved';
        } else {
          item.resolved_status = a.status;
          item.source = 'CLEAN_LATEST_FALLBACK';
          item.source_timestamp = picked.bestTs;
          item.confidence = 'CLEAN_LATEST';
        }
      }
      item.sample = sample;
    }

    const sample = item.sample;
    item.is_test = sample ? isTest(sample) : false;
    item.is_archive = sample ? isArchive(sample) : false;
    if (item.source === 'SAFE_UNKNOWN' || !item.resolved_status) {
      item.reminder_eligible = false;
      if (!item.exclusion_reason) item.exclusion_reason = 'safe_unknown_current_state';
    } else if (item.is_test && !includeTests) {
      item.reminder_eligible = false;
      item.exclusion_reason = 'test_excluded';
    } else if (item.is_archive && !includeArchive) {
      item.reminder_eligible = false;
      item.exclusion_reason = 'archive_excluded';
    } else if (item.resolved_status === 'pending') {
      item.reminder_eligible = true;
      item.exclusion_reason = '';
    } else {
      item.reminder_eligible = false;
      item.exclusion_reason = item.resolved_status === 'spam' ? 'terminal_spam' : (item.resolved_status === 'processed' ? 'terminal_processed' : 'not_pending');
    }
    resolved.push(item);
  }

  let rawPendingCandidateRows = 0;
  const oldFirst = new Map();
  for (const r of cleanRows) {
    if (isTech(r)) continue;
    if (statusFromRow(r) !== 'pending') continue;
    if (isTest(r) && !includeTests) continue;
    if (isArchive(r) && !includeArchive) continue;
    const k = bkey(r);
    if (!k) continue;
    rawPendingCandidateRows += 1;
    if (!oldFirst.has(k)) oldFirst.set(k, r);
  }

  const eligible = resolved.filter((x) => x.reminder_eligible);
  selection = {
    ok: true,
    contract: CONTRACT,
    pending_count: eligible.length,
    raw_candidate_rows: rawPendingCandidateRows,
    unique_candidate_leads: oldFirst.size,
    authoritative_pending: eligible.length,
    safe_unknown_count: resolved.filter((x) => x.source === 'SAFE_UNKNOWN' || !x.resolved_status).length,
    terminal_removed_count: resolved.filter((x) => x.exclusion_reason === 'terminal_spam' || x.exclusion_reason === 'terminal_processed').length,
    test_excluded_count: resolved.filter((x) => x.exclusion_reason === 'test_excluded').length,
    archive_excluded_count: resolved.filter((x) => x.exclusion_reason === 'archive_excluded').length,
    duplicate_excess_rows: Math.max(0, rawPendingCandidateRows - oldFirst.size),
    eligible,
    resolved,
    per_lead_sheets_calls: 0,
  };
} catch (e) {
  return [{ json: {
    reminder_send: false,
    reminder_mark_window_complete: false,
    reminder_skip_reason: 'current_state_resolution_error',
    reminder_decision_code: 'ERROR_CURRENT_STATE_RESOLUTION',
    pending_count_snapshot: 'not_computed',
    reminder_window: gate.reminder_window,
    reminder_selector_contract: CONTRACT,
  } }];
}

const pendingCount = selection.pending_count;
const minCount = Number(gate.pending_reminder_min_count || 1) || 1;

const ageItems = selection.eligible.map((e) => {
  const r = e.sample || {};
  let ts = null;
  for (const c of [r.lead_received_at, r.received_at, r.created_at, r.processed_at]) {
    const t = parseTs(c);
    if (t != null) { ts = t; break; }
  }
  const unk = ts == null;
  const ageMinutes = unk ? null : Math.max(0, Math.floor((nowMs - ts) / 60000));
  return { age_minutes: ageMinutes, age_display: ageDisp(ageMinutes, unk), sort: ts == null ? Number.MAX_SAFE_INTEGER : ts };
}).sort((a, b) => a.sort - b.sort);

if (pendingCount < minCount) {
  return [{ json: {
    reminder_send: false,
    reminder_skip_reason: pendingCount === 0 ? 'zero_pending' : 'below_min_count',
    pending_count_snapshot: pendingCount,
    raw_candidate_rows: selection.raw_candidate_rows,
    unique_candidate_leads: selection.unique_candidate_leads,
    authoritative_pending_count: selection.authoritative_pending,
    safe_unknown_count: selection.safe_unknown_count,
    reminder_selector_contract: CONTRACT,
    reminder_window: gate.reminder_window,
  } }];
}

const over24 = ageItems.filter((i) => i.age_minutes != null && i.age_minutes >= 1440).length;
const oldest = ageItems[0];
const msgLines = [
  '⏰ Напоминание о заявках',
  '',
  'Необработанных заявок: ' + pendingCount,
];
if (over24) msgLines.push('Старше суток: ' + over24);
if (oldest) msgLines.push('Самая старая: ' + oldest.age_display);
msgLines.push('');
msgLines.push('Посмотреть список: /pending_leads');
if (over24 > 0) {
  msgLines.push('');
  msgLines.push('Сначала обратите внимание на самые старые заявки.');
}
const reply_text = msgLines.join('\n');

const recipients = [];
const seen = new Set();
for (const r of accessRows) {
  const role = String(r.role || '').toLowerCase();
  const status = String(r.status || '').toLowerCase();
  if (status !== 'active') continue;
  if (role !== 'admin' && role !== 'moderator') continue;
  const chat = String(r.telegram_user_id || '').trim();
  if (!chat) continue;
  const ref = String(r.telegram_user_hash || '').trim() || ('r:' + chat.slice(-4));
  if (seen.has(ref)) continue;
  seen.add(ref);
  recipients.push({ recipient_ref: ref, role_snapshot: role, chat_id: chat });
}

if (!recipients.length) {
  return [{ json: {
    reminder_send: false,
    reminder_skip_reason: 'no_recipients',
    pending_count_snapshot: pendingCount,
    raw_candidate_rows: selection.raw_candidate_rows,
    unique_candidate_leads: selection.unique_candidate_leads,
    authoritative_pending_count: selection.authoritative_pending,
    reminder_selector_contract: CONTRACT,
    reminder_window: gate.reminder_window,
  } }];
}

const windowKey = gate.reminder_window;
const delivered = new Set();
const claimed = new Set();
for (const row of ledgerRows) {
  if (String(row.reminder_window || '') !== windowKey) continue;
  const key = String(row.reminder_key || '');
  const st = String(row.status || '').toLowerCase();
  if (st === 'delivered' || st === 'sent') delivered.add(key);
  if (st === 'claimed' || st === 'delivered' || st === 'sent' || st === 'reconcile') claimed.add(key);
}

const nowIso = new Date().toISOString();
const out = [];
for (const rec of recipients) {
  const reminder_key = windowKey + '|' + rec.recipient_ref;
  if (delivered.has(reminder_key) || claimed.has(reminder_key)) continue;
  out.push({
    json: {
      reminder_send: true,
      reminder_window: windowKey,
      reminder_key,
      recipient_ref: rec.recipient_ref,
      role_snapshot: rec.role_snapshot,
      chat_id: rec.chat_id,
      reply_text,
      parse_mode: 'HTML',
      pending_count_snapshot: pendingCount,
      raw_candidate_rows: selection.raw_candidate_rows,
      unique_candidate_leads: selection.unique_candidate_leads,
      authoritative_pending_count: selection.authoritative_pending,
      safe_unknown_count: selection.safe_unknown_count,
      reminder_selector_contract: CONTRACT,
      oldest_age_minutes_snapshot: oldest && oldest.age_minutes != null ? oldest.age_minutes : '',
      claimed_at: nowIso,
      status: 'claimed',
      reminder_version: gate.reminder_version || 'sm-pending-reminder-v1.0',
      reminder_key_write: reminder_key,
      telegram_message_ref_safe: '',
      error_code_safe: '',
      sent_at: '',
      reconciled_at: '',
    },
  });
}

if (!out.length) {
  return [{ json: {
    reminder_send: false,
    reminder_skip_reason: 'all_recipients_done',
    pending_count_snapshot: pendingCount,
    raw_candidate_rows: selection.raw_candidate_rows,
    unique_candidate_leads: selection.unique_candidate_leads,
    authoritative_pending_count: selection.authoritative_pending,
    reminder_selector_contract: CONTRACT,
    reminder_window: windowKey,
    reminder_mark_window_complete: true,
  } }];
}

return out;
