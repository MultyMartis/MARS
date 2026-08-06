// Phase 3H.4.1 — Status: authoritative last-production-processed readback (iseo-last-production-processed-v1.0)
// Precedence in this Admin path (CONFIG cache; LEADS/LEAD_EVENTS are SoT for cache writers):
// 1) last_production_processed_at (non-empty, non-synthetic)
// 2) last_processed_at after production_stats_epoch (non-synthetic)
// 3) optional embedded leads_rows / processed event hints on the item (if present)
// Never use last_lead_success_at / last_success_at for the operator production line.
const j = $input.first().json;
const m = j.config_map || {};

const CONTRACT = 'iseo-last-production-processed-v1.0';

function formatMoscow(v) {
  if (v instanceof Date) {
    if (Number.isNaN(v.getTime())) return '';
    return formatMoscow(v.toISOString());
  }
  const s = String(v || '').trim();
  if (!s) return '';
  const d = new Date(s);
  if (Number.isNaN(d.getTime())) return '';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return `${get('day')}.${get('month')}.${get('year')} ${get('hour')}:${get('minute')} МСК`;
}

function envKey() {
  return String(m.environment || 'dev').toLowerCase();
}
function isProd() {
  const k = envKey();
  return k === 'production' || k === 'prod';
}
function contourRu() {
  if (isProd()) return 'рабочий контур';
  const map = { dev: 'разработка', development: 'разработка', sandbox: 'песочница' };
  return map[envKey()] || 'разработка';
}

function parseHeartbeat() {
  const raw = m.gmail_poll_heartbeat;
  if (!raw) return null;
  try {
    const o = typeof raw === 'string' ? JSON.parse(raw) : raw;
    if (o && typeof o === 'object') return o;
  } catch (e) { /* ignore */ }
  return null;
}

function isTestishId(id) {
  const s = String(id || '').toLowerCase();
  return /synth|synthetic|probe_|test_|msg_synth|fixture|archive.?test|probable_test/.test(s);
}

function isExcludedLeadHint(row) {
  if (!row || typeof row !== 'object') return true;
  if (isTestishId(row.lead_id || row.id)) return true;
  if (String(row.is_probable_test).toLowerCase() === 'true') return true;
  if (String(row.is_real_lead).toLowerCase() === 'false') return true;
  const arch = String(row.archive_state || '').toLowerCase();
  if (/test|synth|fixture/.test(arch)) return true;
  return false;
}

function isExcludedEventHint(ev) {
  if (!ev || typeof ev !== 'object') return true;
  const t = String(ev.event_type || ev.type || '').toLowerCase();
  if (!t) return true;
  if (/delivery|reminder|profile|generated.?reply|telegram|technical|synth|test|fixture/.test(t)) return true;
  if (/spam|pending/.test(t) && !/processed/.test(t)) return true;
  if (!/processed/.test(t)) return true;
  if (isTestishId(ev.lead_id)) return true;
  return false;
}

function parseTs(v) {
  if (v instanceof Date) return Number.isNaN(v.getTime()) ? 0 : v.getTime();
  const s = String(v || '').trim();
  if (!s) return 0;
  const ms = Date.parse(s);
  return Number.isFinite(ms) ? ms : 0;
}

function resolveFromLeadsHints() {
  const rows = Array.isArray(j.leads_rows) ? j.leads_rows
    : (Array.isArray(j.leads) ? j.leads : []);
  const epochMs = parseTs(m.production_stats_epoch);
  const candidates = [];
  for (const row of rows) {
    if (isExcludedLeadHint(row)) continue;
    if (String(row.lifecycle_status || row.status || '').toLowerCase() !== 'processed') continue;
    const ts = row.lifecycle_changed_at || row.processed_at || row.status_changed_at || '';
    const ms = parseTs(ts);
    if (!ms) continue;
    if (epochMs && ms < epochMs) continue;
    candidates.push({ ts, ms, source: 'leads_hint' });
  }
  candidates.sort((a, b) => b.ms - a.ms);
  return candidates[0] || null;
}

function resolveFromEventHints() {
  const rows = Array.isArray(j.lead_events) ? j.lead_events
    : (Array.isArray(j.events) ? j.events : []);
  const epochMs = parseTs(m.production_stats_epoch);
  const candidates = [];
  for (const ev of rows) {
    if (isExcludedEventHint(ev)) continue;
    const ts = ev.ts || ev.event_at || ev.created_at || '';
    const ms = parseTs(ts);
    if (!ms) continue;
    if (epochMs && ms < epochMs) continue;
    candidates.push({ ts, ms, source: 'lead_events_hint' });
  }
  candidates.sort((a, b) => b.ms - a.ms);
  return candidates[0] || null;
}

function resolvePoll() {
  const hb = parseHeartbeat();
  const completed =
    (hb && (hb.last_poll_completed_at || hb.last_poll_started_at)) ||
    m.last_poll_completed_at ||
    m.last_poll_success_at ||
    '';
  const state = (hb && hb.last_poll_state) || m.last_poll_state || (completed ? 'success' : '');
  const matching =
    hb && hb.last_poll_matching_messages !== undefined && hb.last_poll_matching_messages !== null
      ? Number(hb.last_poll_matching_messages)
      : (m.last_poll_matching_messages !== undefined && m.last_poll_matching_messages !== ''
        ? Number(m.last_poll_matching_messages)
        : null);
  const interval =
    (hb && hb.polling_interval_minutes) ||
    m.polling_interval_minutes ||
    '2';
  const source = (hb && hb.last_poll_source) || m.last_poll_source || 'scheduled';
  return { completed, state, matching, interval, source, hb };
}

function resolveLastProcessed() {
  // Optional live hints (when upstream attaches LEADS / LEAD_EVENTS rows).
  const fromEvents = resolveFromEventHints();
  if (fromEvents) return { ts: fromEvents.ts, source: fromEvents.source, contract: CONTRACT };
  const fromLeads = resolveFromLeadsHints();
  if (fromLeads) return { ts: fromLeads.ts, source: fromLeads.source, contract: CONTRACT };

  const prodAt = String(m.last_production_processed_at || '').trim();
  if (prodAt) {
    const id = m.last_production_processed_lead_id || '';
    if (!isTestishId(id) && parseTs(prodAt)) {
      return { ts: prodAt, source: 'last_production_processed_at', contract: CONTRACT };
    }
  }

  // Do not trust last_lead_success_at / last_success_at — may be synthetic delivery.
  const processedAt = String(m.last_processed_at || '').trim();
  if (processedAt && parseTs(processedAt)) {
    const id = m.last_processed_lead_id || '';
    const epochMs = parseTs(m.production_stats_epoch);
    const tsMs = parseTs(processedAt);
    if (!isTestishId(id) && (!epochMs || tsMs >= epochMs)) {
      return { ts: processedAt, source: 'last_processed_at', contract: CONTRACT };
    }
  }
  return { ts: '', source: 'none', contract: CONTRACT };
}

function errorStatusLine() {
  if (!m.last_error_at) return 'нет';
  const life = String(m.last_error_lifecycle || '').toLowerCase();
  const errorTs = formatMoscow(m.last_error_at) || 'не подтверждено';
  if (life === 'open') return errorTs;
  return 'нет';
}

const ai = (m.ai_enabled === 'true' || m.ai_enabled === true) ? 'включён' : 'выключен';
const poll = resolvePoll();
const processed = resolveLastProcessed();
const pollTs = formatMoscow(poll.completed);
const leadTs = formatMoscow(processed.ts);

const STALE_MS = 7 * 60 * 1000; // > ~3 intervals @ 2 min
const completedMs = Date.parse(String(poll.completed || '')) || 0;
const stale = !completedMs || (Date.now() - completedMs > STALE_MS);

let lines;
if (!isProd()) {
  lines = [
    'Статус Sales Manager',
    '',
    'Контур: ' + contourRu(),
    'Рабочий процесс: выключен',
    'Админ-процесс: включён',
    'Режим ИИ: ' + ai,
    '',
    'Последний тестовый успех: ' + (leadTs || 'нет данных'),
    'Последняя тестовая ошибка: ' + (formatMoscow(m.last_error_at) || '—'),
    '',
    'Рабочие лиды сейчас не обрабатываются новым контуром.',
  ];
} else {
  const opsLabel = (m.operational_workflow_active === 'true' || m.operational_workflow_active === true) ? 'включён' : 'выключен';
  const adminLabel = (m.admin_workflow_active === 'false' || m.admin_workflow_active === false) ? 'выключен' : 'включён';
  const matchLabel =
    poll.matching === null || Number.isNaN(poll.matching)
      ? 'не подтверждено'
      : String(poll.matching);
  const resultLabel =
    poll.state === 'success'
      ? ('успешно, подходящих писем: ' + matchLabel)
      : (poll.state === 'failure' || poll.state === 'error'
        ? ('ошибка' + (m.last_poll_error_code ? (': ' + m.last_poll_error_code) : ''))
        : 'не подтверждено');

  lines = [
    'Статус Sales Manager',
    '',
    'Контур: ' + contourRu(),
    'Рабочий процесс: ' + opsLabel,
    'Админ-процесс: ' + adminLabel,
    'Режим ИИ: ' + ai,
    '',
    'Последний автоматический опрос Gmail: ' + (pollTs || 'не подтверждено'),
    'Результат опроса: ' + resultLabel,
    'Интервал опроса: ' + String(poll.interval) + ' минуты',
  ];
  if (stale) {
    lines.push('⚠️ Автоматический опрос Gmail давно не выполнялся.');
  }
  lines.push('');
  lines.push('Последний обработанный лид: ' + (leadTs || 'нет данных'));
  lines.push('');
  lines.push('Последняя активная ошибка: ' + errorStatusLine());

  const healthAt = formatMoscow(m.last_health_gmail_check_at);
  if (healthAt) {
    lines.push('');
    lines.push('Последняя проверка Gmail через /health: ' + healthAt);
  }
}

return [{
  json: {
    ...j,
    reply_text: lines.join('\n'),
    last_production_processed_contract: CONTRACT,
    last_production_processed_source: processed.source,
  },
}];
