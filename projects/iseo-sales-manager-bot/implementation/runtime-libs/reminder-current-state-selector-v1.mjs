/**
 * iseo-reminder-current-state-selector-v1.0
 *
 * Resolve reminder eligibility from authoritative current business state
 * per unique lead_id — NOT "first CLEAN pending row wins".
 *
 * Precedence:
 *   1. LEADS_CURRENT (authoritative current-state row; in this product = lead_clean_v2)
 *   2. LEAD_EVENTS_LATEST (most recent valid status transition)
 *   3. CLEAN_LATEST_FALLBACK (latest provable CLEAN projection)
 *   conflict / unprovable → SAFE_UNKNOWN → eligible=false (fail closed)
 *
 * Bulk-only: operates on already-loaded row arrays. per-lead Sheets API calls = 0.
 */

export const REMINDER_CURRENT_STATE_SELECTOR_CONTRACT = 'iseo-reminder-current-state-selector-v1.0';
export const ERROR_CURRENT_STATE_RESOLUTION = 'ERROR_CURRENT_STATE_RESOLUTION';

const INVALID_EXACT = new Set([
  'unknown', '44', '#error!', '#value!', '#ref!', '#n/a', 'n/a', 'na', '-', '—', 'null', 'undefined',
]);

export function isValidContactValue(value) {
  const v = String(value ?? '').trim();
  if (!v) return false;
  const lower = v.toLowerCase();
  if (INVALID_EXACT.has(lower)) return false;
  if (/#error!|#value!|#ref!|#n\/a/i.test(v)) return false;
  if (/formula\s*parse\s*error/i.test(v)) return false;
  if (/^#\w+!/i.test(v)) return false;
  return true;
}

export function isProbableTest(r) {
  if (!r || typeof r !== 'object') return false;
  const marker = String(r.phase_marker || r.marker || '');
  const name = String(r.client_name || '');
  const summary = String(r.summary || '');
  const leadId = String(r.lead_id || '');
  const flag = String(r.is_probable_test ?? r.probable_test ?? '').toLowerCase();
  if (flag === 'true' || flag === '1' || r.is_probable_test === true) return true;
  if (r.__synthetic === true || r.synthetic_fixture === true || r.fixture_id) return true;
  if (String(r.marker || '') === 'SYNTHETIC_TEST') return true;
  if (/SYNTHETIC_TEST/i.test(name)) return true;
  if (/PHASE_3[A-Z0-9._-]*/i.test(marker)) return true;
  if (/synthetic|synth[_ -]/i.test(leadId + ' ' + String(r.source || ''))) return true;
  if (/\b(test|synth)\b/i.test(name) || /тест/i.test(name)) return true;
  if (/phase[_\s-]?3|sheets probe|стабилизац/i.test(name + ' ' + summary + ' ' + marker)) return true;
  return false;
}

export function isArchive(r) {
  if (!r || typeof r !== 'object') return false;
  if (r.is_archived === true || r.archived === true) return true;
  const a = String(r.is_archived ?? r.archive_state ?? r.archived ?? r.archive_flag ?? '').trim().toLowerCase();
  if (!a) return false;
  return a === 'true' || a === '1' || a === 'yes' || a === 'archived' || a === 'archive';
}

export function isTechnicalRetryOnly(r) {
  const t = String(r.row_kind || r.record_kind || r.entry_type || '').toLowerCase();
  if (t === 'technical_retry' || t === 'retry_only' || t === 'tech_retry') return true;
  if (r.technical_retry === true || r.is_technical_retry === true) return true;
  return false;
}

export function businessKey(r) {
  if (!r || typeof r !== 'object') return '';
  const stable = String(r.stable_lead_ref || '').trim();
  if (stable) return 'stable:' + stable;
  const leadId = String(r.lead_id || '').trim();
  if (leadId) return 'lead:' + leadId;
  const gmail = String(r.source_message_id || r.gmail_message_id || '').trim();
  if (gmail) return 'gmail:' + gmail;
  return '';
}

export function normalizeStatus(raw) {
  const s = String(raw ?? '').trim().toLowerCase();
  if (!s) return '';
  if (s === 'processed' || s === 'done' || s === 'closed') return 'processed';
  if (s === 'spam') return 'spam';
  if (s === 'pending' || s === 'new' || s === 'open' || s === 'reopened' || s === 'reopen') return 'pending';
  return '';
}

/** Row lifecycle from CLEAN / LEADS current-state fields. */
export function statusFromRow(r) {
  if (!r || typeof r !== 'object') return '';
  const primary = normalizeStatus(r.manager_status);
  if (primary === 'processed' || primary === 'spam' || primary === 'pending') {
    if (primary === 'pending') return 'pending';
    return primary;
  }
  // Explicit manager_status empty: secondary fields
  const secondary = normalizeStatus(r.lifecycle_status);
  if (secondary === 'processed' || secondary === 'spam') return secondary;
  const close = normalizeStatus(r.close_reason);
  if (close === 'spam' || close === 'processed') return close;
  // Legacy CRM-ish: non-empty non-terminal manager_status (e.g. new) → pending
  const rawMgr = String(r.manager_status || '').trim();
  if (rawMgr) return 'pending';
  if (secondary === 'pending') return 'pending';
  // Empty everything — unknown at row level
  if (!rawMgr && !String(r.lifecycle_status || '').trim() && !String(r.close_reason || '').trim()) {
    return '';
  }
  return 'pending';
}

export function parseTsValue(c) {
  if (c == null || c === '') return null;
  if (typeof c === 'number' && Number.isFinite(c)) return c;
  const d = new Date(c);
  if (!Number.isNaN(d.getTime())) return d.getTime();
  return null;
}

/** Authoritative status-change timestamp preference for current-state rows. */
export function authorityTimestamp(r) {
  if (!r || typeof r !== 'object') return null;
  const candidates = [
    r.manager_status_updated_at,
    r.lifecycle_changed_at,
    r.status_changed_at,
    r.last_manager_action_at,
    r.updated_at,
    r.spam_at,
    r.processed_at,
    r.reopened_at,
    r.lead_received_at,
    r.received_at,
    r.created_at,
    r.telegram_card_sent_at,
  ];
  for (const c of candidates) {
    const t = parseTsValue(c);
    if (t != null) return t;
  }
  return null;
}

/** Projection / CLEAN ordering timestamp (fallback). */
export function projectionTimestamp(r) {
  if (!r || typeof r !== 'object') return null;
  const candidates = [
    r.updated_at,
    r.manager_status_updated_at,
    r.created_at,
    r.lead_received_at,
    r.received_at,
    r.processed_at,
    r.telegram_card_sent_at,
  ];
  for (const c of candidates) {
    const t = parseTsValue(c);
    if (t != null) return t;
  }
  return null;
}

export function hasAuthoritativeManagerFields(r) {
  if (!r || typeof r !== 'object') return false;
  if (String(r.manager_status || '').trim()) return true;
  if (String(r.manager_status_source || '').trim()) return true;
  if (String(r.last_manager_action || '').trim()) return true;
  if (r.manager_status_updated_at) return true;
  return false;
}

/**
 * Map LEAD_EVENTS types → business status.
 * Uses existing production event names only.
 */
export function statusFromEvent(ev) {
  if (!ev || typeof ev !== 'object') return '';
  const t = String(ev.event_type || ev.type || ev.action || ev.last_manager_action || '').trim().toLowerCase();
  if (!t) {
    return normalizeStatus(ev.status || ev.manager_status || ev.new_status || ev.to_status);
  }
  if (/marked_spam|status_spam|^spam$|spam_marked/.test(t)) return 'spam';
  if (/marked_processed|status_processed|^processed$|closed|done/.test(t)) return 'processed';
  if (/reopened|^reopen$|status_pending|^pending$|status_new|set_pending/.test(t)) return 'pending';
  // Explicit nested status on event payload
  const nested = normalizeStatus(ev.status || ev.manager_status || ev.new_status || ev.to_status);
  if (nested) return nested;
  return '';
}

export function eventTimestamp(ev) {
  if (!ev || typeof ev !== 'object') return null;
  for (const c of [ev.ts, ev.event_at, ev.at, ev.created_at, ev.timestamp, ev.updated_at]) {
    const t = parseTsValue(c);
    if (t != null) return t;
  }
  return null;
}

function pickLatestRows(rows, tsFn) {
  let bestTs = null;
  const atBest = [];
  for (const r of rows) {
    const t = tsFn(r);
    if (t == null) continue;
    if (bestTs == null || t > bestTs) {
      bestTs = t;
      atBest.length = 0;
      atBest.push(r);
    } else if (t === bestTs) {
      atBest.push(r);
    }
  }
  return { bestTs, atBest };
}

function statusesAgree(rows, statusFn) {
  const statuses = [...new Set(rows.map(statusFn).filter(Boolean))];
  if (statuses.length === 0) return { ok: false, status: '', reason: 'no_status' };
  if (statuses.length > 1) return { ok: false, status: '', reason: 'conflict' };
  return { ok: true, status: statuses[0], reason: '' };
}

function resultBase(leadKey, extra = {}) {
  return {
    lead_id: leadKey,
    resolved_status: '',
    source: 'SAFE_UNKNOWN',
    source_timestamp: null,
    confidence: 'SAFE_UNKNOWN_CURRENT_STATE',
    reminder_eligible: false,
    exclusion_reason: '',
    is_test: false,
    is_archive: false,
    clean_row_count: 0,
    ...extra,
  };
}

/**
 * Resolve one unique lead's current state from bulk arrays.
 * @param {object} input
 * @param {string} input.leadKey
 * @param {object[]} [input.leadsCurrentRows] — optional separate LEADS tab rows for this key
 * @param {object[]} [input.cleanRows] — CLEAN / lead_clean_v2 rows for this key
 * @param {object[]} [input.leadEvents] — LEAD_EVENTS rows for this key
 * @param {boolean} [input.includeTests]
 * @param {boolean} [input.includeArchive]
 */
export function resolveLeadCurrentState(input = {}) {
  const leadKey = String(input.leadKey || '');
  const includeTests = input.includeTests === true;
  const includeArchive = input.includeArchive === true;
  const leadsCurrent = (input.leadsCurrentRows || []).filter((r) => r && typeof r === 'object');
  const cleanRows = (input.cleanRows || []).filter((r) => r && typeof r === 'object' && !isTechnicalRetryOnly(r));
  const leadEvents = (input.leadEvents || []).filter((r) => r && typeof r === 'object');

  const out = resultBase(leadKey, { clean_row_count: cleanRows.length });

  // --- Priority 1: LEADS_CURRENT ---
  // Product SoT: lead_clean_v2 rows with manager lifecycle fields act as LEADS current-state.
  const leadsPool = leadsCurrent.length
    ? leadsCurrent
    : cleanRows.filter(hasAuthoritativeManagerFields);

  if (leadsPool.length) {
    const picked = pickLatestRows(leadsPool, authorityTimestamp);
    let sample = leadsPool[0];
    if (picked.bestTs == null) {
      // Have authoritative fields but no provable ordering → try unanimous status
      const agree = statusesAgree(leadsPool, statusFromRow);
      if (agree.ok && agree.status) {
        out.resolved_status = agree.status;
        out.source = 'LEADS_CURRENT';
        out.source_timestamp = null;
        out.confidence = 'AUTHORITATIVE_UNORDERED_UNANIMOUS';
      } else {
        out.source = 'SAFE_UNKNOWN';
        out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
        out.exclusion_reason = 'leads_current_ordering_ambiguous';
        return finalizeEligibility(out, sample, includeTests, includeArchive);
      }
    } else {
      sample = picked.atBest[0] || sample;
      const agree = statusesAgree(picked.atBest, statusFromRow);
      if (!agree.ok || !agree.status) {
        out.source = 'SAFE_UNKNOWN';
        out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
        out.exclusion_reason = agree.reason === 'conflict'
          ? 'leads_current_status_conflict_same_timestamp'
          : 'leads_current_status_unresolved';
        return finalizeEligibility(out, sample, includeTests, includeArchive);
      }
      out.resolved_status = agree.status;
      out.source = 'LEADS_CURRENT';
      out.source_timestamp = picked.bestTs;
      out.confidence = 'AUTHORITATIVE';
    }
    return finalizeEligibility(out, sample, includeTests, includeArchive);
  }

  // --- Priority 2: LEAD_EVENTS_LATEST ---
  const statusEvents = leadEvents
    .map((ev) => ({ ev, status: statusFromEvent(ev), ts: eventTimestamp(ev) }))
    .filter((x) => x.status);

  if (statusEvents.length) {
    let bestTs = null;
    const atBest = [];
    for (const x of statusEvents) {
      if (x.ts == null) continue;
      if (bestTs == null || x.ts > bestTs) {
        bestTs = x.ts;
        atBest.length = 0;
        atBest.push(x);
      } else if (x.ts === bestTs) {
        atBest.push(x);
      }
    }
    if (bestTs == null) {
      // Events without timestamps: only accept if unanimous
      const statuses = [...new Set(statusEvents.map((x) => x.status))];
      if (statuses.length === 1) {
        out.resolved_status = statuses[0];
        out.source = 'LEAD_EVENTS_LATEST';
        out.confidence = 'EVENTS_UNORDERED_UNANIMOUS';
      } else {
        out.source = 'SAFE_UNKNOWN';
        out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
        out.exclusion_reason = 'lead_events_ordering_ambiguous';
        return finalizeEligibility(out, cleanRows[0] || null, includeTests, includeArchive);
      }
    } else {
      const statuses = [...new Set(atBest.map((x) => x.status))];
      if (statuses.length !== 1) {
        out.source = 'SAFE_UNKNOWN';
        out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
        out.exclusion_reason = 'lead_events_status_conflict_same_timestamp';
        return finalizeEligibility(out, cleanRows[0] || null, includeTests, includeArchive);
      }
      out.resolved_status = statuses[0];
      out.source = 'LEAD_EVENTS_LATEST';
      out.source_timestamp = bestTs;
      out.confidence = 'EVENTS_LATEST';
    }
    return finalizeEligibility(out, cleanRows[0] || (atBest[0] && atBest[0].ev) || null, includeTests, includeArchive);
  }

  // --- Priority 3: CLEAN_LATEST_FALLBACK ---
  if (cleanRows.length) {
    const picked = pickLatestRows(cleanRows, projectionTimestamp);
    let sample = cleanRows[0];
    if (picked.bestTs == null) {
      const agree = statusesAgree(cleanRows, statusFromRow);
      if (agree.ok && agree.status) {
        out.resolved_status = agree.status;
        out.source = 'CLEAN_LATEST_FALLBACK';
        out.confidence = 'CLEAN_UNORDERED_UNANIMOUS';
      } else {
        out.source = 'SAFE_UNKNOWN';
        out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
        out.exclusion_reason = 'clean_ordering_ambiguous';
        return finalizeEligibility(out, sample, includeTests, includeArchive);
      }
    } else {
      sample = picked.atBest[0] || sample;
      const agree = statusesAgree(picked.atBest, statusFromRow);
      if (!agree.ok || !agree.status) {
        out.source = 'SAFE_UNKNOWN';
        out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
        out.exclusion_reason = agree.reason === 'conflict'
          ? 'clean_status_conflict_same_timestamp'
          : 'clean_status_unresolved';
        return finalizeEligibility(out, sample, includeTests, includeArchive);
      }
      out.resolved_status = agree.status;
      out.source = 'CLEAN_LATEST_FALLBACK';
      out.source_timestamp = picked.bestTs;
      out.confidence = 'CLEAN_LATEST';
    }
    return finalizeEligibility(out, sample, includeTests, includeArchive);
  }

  out.source = 'SAFE_UNKNOWN';
  out.confidence = 'SAFE_UNKNOWN_CURRENT_STATE';
  out.exclusion_reason = 'no_current_state_source';
  return out;
}

function finalizeEligibility(out, sampleRow, includeTests, includeArchive) {
  const test = sampleRow ? isProbableTest(sampleRow) : false;
  const arch = sampleRow ? isArchive(sampleRow) : false;
  out.is_test = test;
  out.is_archive = arch;

  if (out.source === 'SAFE_UNKNOWN' || out.confidence === 'SAFE_UNKNOWN_CURRENT_STATE') {
    out.reminder_eligible = false;
    if (!out.exclusion_reason) out.exclusion_reason = 'safe_unknown_current_state';
    return out;
  }

  if (test && !includeTests) {
    out.reminder_eligible = false;
    out.exclusion_reason = 'test_excluded';
    return out;
  }
  if (arch && !includeArchive) {
    out.reminder_eligible = false;
    out.exclusion_reason = 'archive_excluded';
    return out;
  }
  if (out.resolved_status === 'pending') {
    out.reminder_eligible = true;
    out.exclusion_reason = '';
    return out;
  }
  out.reminder_eligible = false;
  out.exclusion_reason = out.resolved_status === 'spam'
    ? 'terminal_spam'
    : (out.resolved_status === 'processed' ? 'terminal_processed' : 'not_pending');
  return out;
}

/**
 * Build unique current-state objects + pending count from bulk CLEAN (+ optional LEADS/EVENTS).
 * Does not perform any Sheets I/O.
 */
export function selectAuthoritativePending(input = {}) {
  try {
    const includeTests = input.includeTests === true;
    const includeArchive = input.includeArchive === true;
    const cleanAll = Array.isArray(input.cleanRows) ? input.cleanRows.filter((r) => r && typeof r === 'object' && !r.error) : [];
    const leadsAll = Array.isArray(input.leadsCurrentRows) ? input.leadsCurrentRows.filter((r) => r && typeof r === 'object' && !r.error) : [];
    const eventsAll = Array.isArray(input.leadEvents) ? input.leadEvents.filter((r) => r && typeof r === 'object' && !r.error) : [];

    const byKeyClean = new Map();
    for (const r of cleanAll) {
      if (isTechnicalRetryOnly(r)) continue;
      const k = businessKey(r);
      if (!k) continue;
      if (!byKeyClean.has(k)) byKeyClean.set(k, []);
      byKeyClean.get(k).push(r);
    }
    const byKeyLeads = new Map();
    for (const r of leadsAll) {
      const k = businessKey(r);
      if (!k) continue;
      if (!byKeyLeads.has(k)) byKeyLeads.set(k, []);
      byKeyLeads.get(k).push(r);
    }
    const byKeyEvents = new Map();
    for (const ev of eventsAll) {
      const k = businessKey(ev) || (String(ev.lead_id || '').trim() ? 'lead:' + String(ev.lead_id).trim() : '');
      if (!k) continue;
      if (!byKeyEvents.has(k)) byKeyEvents.set(k, []);
      byKeyEvents.get(k).push(ev);
    }

    const keys = new Set([...byKeyClean.keys(), ...byKeyLeads.keys(), ...byKeyEvents.keys()]);
    const resolved = [];
    for (const leadKey of keys) {
      resolved.push(resolveLeadCurrentState({
        leadKey,
        cleanRows: byKeyClean.get(leadKey) || [],
        leadsCurrentRows: byKeyLeads.get(leadKey) || [],
        leadEvents: byKeyEvents.get(leadKey) || [],
        includeTests,
        includeArchive,
      }));
    }

    // Old first-row pending candidate metrics (for observability / proof)
    let rawPendingCandidateRows = 0;
    const oldFirst = new Map();
    for (const r of cleanAll) {
      if (isTechnicalRetryOnly(r)) continue;
      const st = statusFromRow(r);
      if (st !== 'pending') continue;
      if (isProbableTest(r) && !includeTests) continue;
      if (isArchive(r) && !includeArchive) continue;
      const k = businessKey(r);
      if (!k) continue;
      rawPendingCandidateRows += 1;
      if (!oldFirst.has(k)) oldFirst.set(k, r);
    }

    const eligible = resolved.filter((x) => x.reminder_eligible);
    const safeUnknown = resolved.filter((x) => x.source === 'SAFE_UNKNOWN' || x.confidence === 'SAFE_UNKNOWN_CURRENT_STATE');
    const terminalRemoved = resolved.filter((x) => x.exclusion_reason === 'terminal_spam' || x.exclusion_reason === 'terminal_processed');
    const testExcluded = resolved.filter((x) => x.exclusion_reason === 'test_excluded');
    const archiveExcluded = resolved.filter((x) => x.exclusion_reason === 'archive_excluded');

    return {
      ok: true,
      contract: REMINDER_CURRENT_STATE_SELECTOR_CONTRACT,
      pending_count: eligible.length,
      raw_candidate_rows: rawPendingCandidateRows,
      unique_candidate_leads: oldFirst.size,
      authoritative_pending: eligible.length,
      safe_unknown_count: safeUnknown.length,
      terminal_removed_count: terminalRemoved.length,
      test_excluded_count: testExcluded.length,
      archive_excluded_count: archiveExcluded.length,
      duplicate_excess_rows: Math.max(0, rawPendingCandidateRows - oldFirst.size),
      resolved,
      eligible,
      sheets_reads_used: 0,
      per_lead_sheets_calls: 0,
      error: null,
    };
  } catch (e) {
    return {
      ok: false,
      contract: REMINDER_CURRENT_STATE_SELECTOR_CONTRACT,
      pending_count: 0,
      raw_candidate_rows: 0,
      unique_candidate_leads: 0,
      authoritative_pending: 0,
      safe_unknown_count: 0,
      terminal_removed_count: 0,
      test_excluded_count: 0,
      archive_excluded_count: 0,
      duplicate_excess_rows: 0,
      resolved: [],
      eligible: [],
      sheets_reads_used: 0,
      per_lead_sheets_calls: 0,
      error: ERROR_CURRENT_STATE_RESOLUTION,
      error_message_safe: 'current-state resolution failed',
      detail: String(e && e.message ? e.message : e).slice(0, 200),
    };
  }
}

export function formatReminderMessageFromCount(pendingCount, items = []) {
  const over24 = items.filter((i) => i.age_minutes != null && i.age_minutes >= 1440).length;
  const oldest = items[0];
  const lines = [
    '⏰ Напоминание о заявках',
    '',
    'Необработанных заявок: ' + pendingCount,
  ];
  if (over24) lines.push('Старше суток: ' + over24);
  if (oldest && oldest.age_display) lines.push('Самая старая: ' + oldest.age_display);
  lines.push('');
  lines.push('Посмотреть список: /pending_leads');
  if (over24 > 0) {
    lines.push('');
    lines.push('Сначала обратите внимание на самые старые заявки.');
  }
  return lines.join('\n');
}

export function ageDisplay(mins, unk) {
  if (unk || mins == null) return 'возраст неизвестен';
  const m = Math.max(0, Math.floor(mins));
  if (m < 60) return '< 1 ч';
  const h = Math.floor(m / 60);
  if (h < 24) return h + ' ч';
  const d = Math.floor(h / 24);
  const rh = h % 24;
  return rh ? (d + ' д ' + rh + ' ч') : (d + ' д');
}
