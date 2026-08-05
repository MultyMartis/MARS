/**
 * Phase 3F.1 — Pending leads view + reminder window helpers.
 * Pure JS for harness and documentation mirror. n8n nodes use inlined private copies.
 * No PII logging. No Telegram IDs in outputs.
 */

export const PENDING_REMINDER_VERSION = 'sm-pending-reminder-v1.0';
export const DEFAULT_PAGE_SIZE = 5;
export const MAX_PAGE_SIZE = 10;

export const FALLBACK = {
  name: 'Без имени',
  contact: 'Контакт не указан',
  website: 'Сайт не указан',
  service: 'Задача требует уточнения',
};

const INVALID_EXACT = new Set([
  'unknown', '44', '#error!', '#value!', '#ref!', '#n/a', 'n/a', 'na', '-', '—', 'null', 'undefined',
]);

export function escHtml(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

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

export function isTechnicalRetryOnly(r) {
  const t = String(r.row_kind || r.record_kind || r.entry_type || '').toLowerCase();
  if (t === 'technical_retry' || t === 'retry_only' || t === 'tech_retry') return true;
  if (r.technical_retry === true || r.is_technical_retry === true) return true;
  return false;
}

export function isProbableInvalidRecord(r) {
  if (!r || typeof r !== 'object') return true;
  const key = businessKey(r);
  if (!key) return true;
  // Empty shell rows
  const name = String(r.client_name || '').trim();
  const site = String(r.site || r.website || '').trim();
  const summary = String(r.summary || r.request_summary || '').trim();
  if (!name && !site && !summary && !String(r.phone || '').trim() && !String(r.email || '').trim()) {
    return true;
  }
  return false;
}

/**
 * Authoritative pending lifecycle rule (Phase 3F.1 forensic):
 * Live mutations write CLEAN.manager_status = pending|processed|spam.
 * lifecycle_status is a secondary compatibility field when present.
 * Legacy rows without modern fields: treat as pending unless processed/spam.
 */
export function resolveLifecycle(r) {
  const primary = String(r.manager_status || '').trim().toLowerCase();
  const secondary = String(r.lifecycle_status || '').trim().toLowerCase();
  const close = String(r.close_reason || '').trim().toLowerCase();
  for (const raw of [primary, secondary]) {
    if (raw === 'processed' || raw === 'spam') return raw;
  }
  if (close === 'spam') return 'spam';
  if (close === 'processed') return 'processed';
  // Legacy CRM-ish statuses that are not closed/spam remain pending for Olya queue.
  return 'pending';
}

export function businessKey(r) {
  const stable = String(r.stable_lead_ref || '').trim();
  if (stable) return 'stable:' + stable;
  const leadId = String(r.lead_id || '').trim();
  if (leadId) return 'lead:' + leadId;
  const gmail = String(r.source_message_id || r.gmail_message_id || '').trim();
  if (gmail) return 'gmail:' + gmail;
  const created = String(r.created_at || r.processed_at || r.updated_at || '').trim();
  const site = String(r.site || r.website || '').trim();
  const name = String(r.client_name || '').trim();
  const fb = [name, site, created].filter(Boolean).join('|');
  return fb ? 'fb:' + fb : '';
}

export function parseReceivedTs(r) {
  const candidates = [
    r.lead_received_at, r.received_at, r.created_at, r.processed_at,
    r.telegram_card_sent_at, r.updated_at, r.manager_status_updated_at,
  ];
  for (const c of candidates) {
    if (!c) continue;
    const d = new Date(c);
    if (!Number.isNaN(d.getTime())) return d.getTime();
  }
  return null;
}

function fieldScore(r) {
  let s = 0;
  for (const k of ['client_name', 'phone', 'email', 'messenger', 'site', 'website', 'summary', 'first_reply_text']) {
    const v = String(r[k] ?? '').trim();
    if (v && isValidContactValue(v)) s += 2;
  }
  if (String(r.manager_status || '').trim()) s += 1;
  if (String(r.first_reply_text || '').trim()) s += 2;
  return s;
}

function prefer(a, b) {
  const ta = parseReceivedTs(a) || 0;
  const tb = parseReceivedTs(b) || 0;
  if (tb !== ta) return tb > ta ? b : a;
  return fieldScore(b) > fieldScore(a) ? b : a;
}

export function formatAge(ageMinutes, ageUnknown = false) {
  if (ageUnknown || ageMinutes == null || !Number.isFinite(ageMinutes)) return 'возраст неизвестен';
  const m = Math.max(0, Math.floor(ageMinutes));
  if (m < 60) return '< 1 ч';
  const h = Math.floor(m / 60);
  if (h < 24) return `${h} ч`;
  const d = Math.floor(h / 24);
  const remH = h % 24;
  if (remH === 0) return `${d} д`;
  return `${d} д ${remH} ч`;
}

export function serviceLabel(r) {
  const raw = String(r.resolved_service_label || r.resolved_service || r.service || '').trim();
  if (!raw) return FALLBACK.service;
  const map = {
    audit: 'Аудит', seo: 'SEO', direct: 'Директ', site: 'Сайт',
    website: 'Сайт', website_development: 'Разработка сайта', other: 'Другое',
  };
  return map[raw.toLowerCase()] || raw;
}

export function clientDisplayName(r) {
  const n = String(r.client_name || r.client_display_name || '').trim();
  return isValidContactValue(n) ? n : FALLBACK.name;
}

export function contactSummary(r) {
  for (const k of ['phone', 'email', 'messenger', 'primary_contact']) {
    const v = String(r[k] ?? '').trim();
    if (isValidContactValue(v)) return v;
  }
  return FALLBACK.contact;
}

export function websiteSummary(r) {
  const v = String(r.site || r.website || r.website_summary || '').trim();
  return isValidContactValue(v) ? v : FALLBACK.website;
}

export function requestSummary(r) {
  const v = String(r.summary || r.request_summary || r.quality_comment || '').trim();
  if (!v) return 'Запрос без краткого описания';
  return v.length > 120 ? v.slice(0, 117) + '…' : v;
}

export function firstReplyReady(r) {
  const flag = String(r.first_reply_ready ?? '').toLowerCase();
  if (flag === 'true' || flag === '1' || r.first_reply_ready === true) return true;
  return Boolean(String(r.first_reply_text || '').trim());
}

export function deliveryStateSummary(r) {
  if (String(r.telegram_card_sent_at || r.telegram_message_id || r.telegram_message_ref || '').trim()) {
    return 'карточка доставлена';
  }
  return 'доставка не подтверждена';
}

export function sourceContextShort(r) {
  const src = String(r.source || '').trim();
  if (!src) return 'источник не указан';
  return src.length > 40 ? src.slice(0, 37) + '…' : src;
}

/**
 * Build normalized pending view from CLEAN rows.
 * @param {object[]} rows
 * @param {object} opts
 * @param {boolean} [opts.includeTests=false]
 * @param {number} [opts.nowMs]
 */
export function buildPendingView(rows, opts = {}) {
  const includeTests = opts.includeTests === true;
  const nowMs = opts.nowMs || Date.now();
  const warnings = [];
  const raw = Array.isArray(rows) ? rows.filter((r) => r && typeof r === 'object') : [];

  const candidates = [];
  for (const r of raw) {
    if (isTechnicalRetryOnly(r)) continue;
    if (isProbableInvalidRecord(r)) continue;
    const life = resolveLifecycle(r);
    if (life !== 'pending') continue;
    const test = isProbableTest(r);
    if (test && !includeTests) continue;
    candidates.push(r);
  }

  const bestByKey = new Map();
  for (const r of candidates) {
    const key = businessKey(r);
    if (!key) continue;
    if (!bestByKey.has(key)) bestByKey.set(key, r);
    else bestByKey.set(key, prefer(bestByKey.get(key), r));
  }

  const items = [];
  for (const r of bestByKey.values()) {
    const ts = parseReceivedTs(r);
    const ageUnknown = ts == null;
    if (ageUnknown) warnings.push('missing_timestamp');
    const ageMinutes = ageUnknown ? null : Math.max(0, Math.floor((nowMs - ts) / 60000));
    const ageHours = ageMinutes == null ? null : ageMinutes / 60;
    const ageDays = ageMinutes == null ? null : ageMinutes / 1440;
    const stable = String(r.stable_lead_ref || r.lead_id || businessKey(r));
    const sortKey = String(ts == null ? Number.MAX_SAFE_INTEGER : ts).padStart(15, '0') + '|' + stable;
    items.push({
      stable_lead_ref: stable,
      received_at: ts == null ? '' : new Date(ts).toISOString(),
      age_minutes: ageMinutes,
      age_hours: ageHours,
      age_days: ageDays,
      age_display: formatAge(ageMinutes, ageUnknown),
      client_display_name: clientDisplayName(r),
      contact_summary: contactSummary(r),
      website_summary: websiteSummary(r),
      resolved_service_label: serviceLabel(r),
      request_summary: requestSummary(r),
      lifecycle: 'pending',
      is_probable_test: isProbableTest(r),
      source_context_short: sourceContextShort(r),
      first_reply_ready: firstReplyReady(r),
      delivery_state_summary: deliveryStateSummary(r),
      pending_sort_key: sortKey,
    });
  }

  // Oldest first — operational attention order.
  items.sort((a, b) => String(a.pending_sort_key).localeCompare(String(b.pending_sort_key)));

  const buckets = { under_2h: 0, from_2h_to_24h: 0, over_24h: 0, unknown: 0 };
  for (const it of items) {
    if (it.age_minutes == null) buckets.unknown += 1;
    else if (it.age_minutes < 120) buckets.under_2h += 1;
    else if (it.age_minutes < 1440) buckets.from_2h_to_24h += 1;
    else buckets.over_24h += 1;
  }

  return {
    items,
    total: items.length,
    buckets,
    oldest_age_minutes: items.length && items[0].age_minutes != null ? items[0].age_minutes : null,
    oldest_age_display: items.length ? items[0].age_display : null,
    warnings: [...new Set(warnings)],
  };
}

export function formatPendingCountReply(view, opts = {}) {
  const adminDiag = opts.adminDiagnostics === true;
  const testCount = opts.testCount || 0;
  if (view.total === 0) {
    const lines = ['Необработанных заявок сейчас нет.'];
    if (adminDiag && testCount > 0) lines.push(`Тестовых заявок: ${testCount}`);
    return lines.join('\n');
  }
  const lines = [`Необработанных заявок: ${view.total}`];
  const b = view.buckets;
  const parts = [];
  if (b.under_2h) parts.push(`до 2 часов: ${b.under_2h}`);
  if (b.from_2h_to_24h) parts.push(`2–24 часа: ${b.from_2h_to_24h}`);
  if (b.over_24h) parts.push(`старше суток: ${b.over_24h}`);
  if (parts.length) lines.push(parts.join(' · '));
  if (adminDiag && testCount > 0) lines.push(`Тестовых заявок: ${testCount}`);
  return lines.join('\n');
}

export function paginatePending(view, pageRaw, pageSize = DEFAULT_PAGE_SIZE) {
  const size = Math.min(MAX_PAGE_SIZE, Math.max(1, Number(pageSize) || DEFAULT_PAGE_SIZE));
  const total = view.total;
  const pageCount = Math.max(1, Math.ceil(total / size) || 1);
  let page = Number.parseInt(String(pageRaw ?? '1'), 10);
  if (!Number.isFinite(page) || page < 1) page = 1;
  if (page > pageCount) page = pageCount;
  const start = (page - 1) * size;
  const slice = view.items.slice(start, start + size);
  return { page, pageCount, pageSize: size, total, items: slice, startOrdinal: start + 1 };
}

export function formatPendingListReply(pageResult) {
  const { page, pageCount, total, items, startOrdinal } = pageResult;
  if (total === 0) {
    return 'Необработанных заявок сейчас нет.';
  }
  const lines = [];
  items.forEach((it, idx) => {
    const n = startOrdinal + idx;
    const name = escHtml(it.client_display_name);
    const svc = escHtml(it.resolved_service_label);
    const site = escHtml(it.website_summary);
    const req = escHtml(it.request_summary);
    const age = escHtml(it.age_display);
    const draft = it.first_reply_ready ? 'Черновик ответа: готов' : 'Черновик ответа: нет';
    lines.push(`${n}. ${age} · ${name}`);
    lines.push(`${svc} · ${site}`);
    lines.push(req);
    lines.push(draft);
    lines.push('');
  });
  lines.push(`Страница ${page} из ${pageCount} · всего ${total}`);
  return lines.join('\n').trim();
}

export function parsePendingLeadsArgs(args) {
  const a = Array.isArray(args) ? args.map((x) => String(x).trim()).filter(Boolean) : [];
  let includeTests = false;
  let page = 1;
  for (const tok of a) {
    if (/^test$/i.test(tok)) {
      includeTests = true;
      continue;
    }
    if (/^\d+$/.test(tok)) {
      page = Number(tok);
      continue;
    }
    return { ok: false, error: 'usage' };
  }
  if (!Number.isFinite(page) || page < 1) page = 1;
  return { ok: true, page, includeTests };
}

/** Reminder window key: pending-reminder:<YYYY-MM-DD>:<HH:MM>:<timezone> */
export function buildReminderWindowKey(localDate, hhmm, timezone) {
  const d = String(localDate || '').trim();
  const t = String(hhmm || '').trim();
  const tz = String(timezone || '').trim();
  return `pending-reminder:${d}:${t}:${tz}`;
}

export function validateHhMm(s) {
  const m = String(s || '').trim().match(/^([01]\d|2[0-3]):([0-5]\d)$/);
  if (!m) return { ok: false };
  return { ok: true, value: `${m[1]}:${m[2]}` };
}

export function validateIanaTimezone(tz) {
  const t = String(tz || '').trim();
  if (!t || t.length > 64) return { ok: false };
  if (!/^[A-Za-z_]+\/[A-Za-z0-9_+\-]+(?:\/[A-Za-z0-9_+\-]+)?$/.test(t) && t !== 'UTC') {
    return { ok: false };
  }
  try {
    Intl.DateTimeFormat('en-US', { timeZone: t }).format(new Date());
    return { ok: true, value: t };
  } catch {
    return { ok: false };
  }
}

export function localPartsInTimezone(date, timeZone) {
  const fmt = new Intl.DateTimeFormat('en-CA', {
    timeZone,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hourCycle: 'h23',
  });
  const parts = Object.fromEntries(fmt.formatToParts(date).filter((p) => p.type !== 'literal').map((p) => [p.type, p.value]));
  return {
    date: `${parts.year}-${parts.month}-${parts.day}`,
    hour: Number(parts.hour),
    minute: Number(parts.minute),
    hhmm: `${parts.hour}:${parts.minute}`,
  };
}

/**
 * Due if local clock is within [configured, configured+windowMinutes) on that local date.
 * Tolerates schedule drift for a 15-minute checker (default window 20 minutes).
 */
export function isReminderWindowDue(now, cfg, opts = {}) {
  if (String(cfg.pending_reminders_enabled || '').toLowerCase() !== 'true' && cfg.pending_reminders_enabled !== true) {
    return { due: false, reason: 'disabled' };
  }
  const tzCheck = validateIanaTimezone(cfg.pending_reminder_timezone || 'Europe/Moscow');
  const timeCheck = validateHhMm(cfg.pending_reminder_time || '10:00');
  if (!tzCheck.ok || !timeCheck.ok) return { due: false, reason: 'invalid_config' };
  const local = localPartsInTimezone(now, tzCheck.value);
  const [th, tm] = timeCheck.value.split(':').map(Number);
  const nowMins = local.hour * 60 + local.minute;
  const targetMins = th * 60 + tm;
  const windowMinutes = opts.windowMinutes ?? 20;
  if (nowMins < targetMins || nowMins >= targetMins + windowMinutes) {
    return { due: false, reason: 'outside_window', local, target: timeCheck.value, timezone: tzCheck.value };
  }
  const windowKey = buildReminderWindowKey(local.date, timeCheck.value, tzCheck.value);
  if (String(cfg.pending_reminder_last_window || '') === windowKey) {
    return { due: false, reason: 'already_completed', windowKey, local, timezone: tzCheck.value };
  }
  return {
    due: true,
    reason: 'due',
    windowKey,
    local,
    timezone: tzCheck.value,
    time: timeCheck.value,
  };
}

export function reminderDeliveryKey(windowKey, recipientRef) {
  return `${windowKey}|${recipientRef}`;
}

export function selectActiveStaffRecipients(accessRows) {
  const rows = Array.isArray(accessRows) ? accessRows : [];
  const out = [];
  const seen = new Set();
  for (const r of rows) {
    const role = String(r.role || '').toLowerCase();
    const status = String(r.status || '').toLowerCase();
    if (status !== 'active') continue;
    if (role !== 'admin' && role !== 'moderator') continue;
    const ref = String(r.telegram_user_hash || r.opaque_user_ref || r.recipient_ref || '').trim();
    const chat = String(r.telegram_user_id || r.delivery_chat_id || '').trim();
    if (!chat) continue;
    const dedupe = ref || chat;
    if (seen.has(dedupe)) continue;
    seen.add(dedupe);
    out.push({
      recipient_ref: ref || ('uidhash:' + String(chat).slice(0, 4) + '…'),
      role_snapshot: role,
      delivery_chat_id: chat,
      display_name: String(r.display_name || '').trim(),
    });
  }
  return out;
}

export function formatReminderMessage(view) {
  if (!view || view.total <= 0) return null;
  const lines = [
    '⏰ Напоминание о заявках',
    '',
    `Необработанных заявок: ${view.total}`,
  ];
  if (view.buckets.over_24h) lines.push(`Старше суток: ${view.buckets.over_24h}`);
  if (view.oldest_age_display) lines.push(`Самая старая: ${view.oldest_age_display}`);
  lines.push('');
  lines.push('Посмотреть список: /pending_leads');
  if (view.buckets.over_24h > 0) {
    lines.push('');
    lines.push('Сначала обратите внимание на самые старые заявки.');
  }
  return lines.join('\n');
}

export function formatReminderStatusReply(cfg, opts = {}) {
  const enabled = String(cfg.pending_reminders_enabled || '').toLowerCase() === 'true';
  const time = cfg.pending_reminder_time || '10:00';
  const tz = cfg.pending_reminder_timezone || 'Europe/Moscow';
  if (opts.moderatorShort) {
    return [
      '⏰ Напоминания о заявках',
      `Статус: ${enabled ? 'включены' : 'выключены'}`,
      `Время: ${time}`,
      `Часовой пояс: ${tz}`,
    ].join('\n');
  }
  return [
    '⏰ Напоминания о заявках',
    `Статус: ${enabled ? 'включены' : 'выключены'}`,
    `Время: ${time}`,
    `Часовой пояс: ${tz}`,
    `Минимум заявок: ${cfg.pending_reminder_min_count || '1'}`,
    `Тестовые в напоминании: ${String(cfg.pending_reminder_include_tests || 'false') === 'true' ? 'да' : 'нет'}`,
    `Последнее окно: ${cfg.pending_reminder_last_window || '—'}`,
    `Последняя отправка: ${cfg.pending_reminder_last_success_at || '—'}`,
    `Заявок в последней отправке: ${cfg.pending_reminder_last_pending_count || '—'}`,
    `Получателей: ${cfg.pending_reminder_last_recipient_count || '—'}`,
    cfg.pending_reminder_last_error_safe ? `Последняя ошибка: ${cfg.pending_reminder_last_error_safe}` : null,
  ].filter(Boolean).join('\n');
}

export function authorizePendingCommand({ auth_role, status, command }) {
  const role = String(auth_role || '').toLowerCase();
  const st = String(status || 'active').toLowerCase();
  const cmd = String(command || '').toLowerCase();
  const staff = (role === 'admin' || role === 'moderator') && st === 'active';
  const admin = role === 'admin' && st === 'active';
  const staffCmds = new Set(['/pending_count', '/pending_leads', '/reminder_status']);
  const adminCfg = new Set([
    '/pending_leads_test', '/reminder_on', '/reminder_off',
    '/reminder_time', '/reminder_timezone', '/reminder_min',
  ]);
  if (role === 'revoked' || st === 'revoked') return { allowed: false, reason: 'revoked' };
  if (role === 'pending' || st === 'pending') return { allowed: false, reason: 'pending' };
  if (role === 'public' || role === 'blocked') return { allowed: false, reason: 'denied' };
  if (staffCmds.has(cmd)) return { allowed: staff, reason: staff ? null : 'staff_only' };
  if (adminCfg.has(cmd)) return { allowed: admin, reason: admin ? null : 'admin_only' };
  return { allowed: false, reason: 'unknown' };
}

export const DEFAULT_REMINDER_CONFIG = {
  pending_reminders_enabled: 'false',
  pending_reminder_time: '10:00',
  pending_reminder_timezone: 'Europe/Moscow',
  pending_reminder_min_count: '1',
  pending_reminder_include_tests: 'false',
  pending_reminder_last_window: '',
  pending_reminder_last_success_at: '',
  pending_reminder_last_recipient_count: '',
  pending_reminder_last_pending_count: '',
  pending_reminder_version: PENDING_REMINDER_VERSION,
};

export const REMINDER_DELIVERY_HEADERS = [
  'reminder_key',
  'reminder_window',
  'recipient_ref',
  'role_snapshot',
  'pending_count_snapshot',
  'oldest_age_minutes_snapshot',
  'claimed_at',
  'sent_at',
  'status',
  'telegram_message_ref_safe',
  'error_code_safe',
  'reminder_version',
  'reconciled_at',
];
