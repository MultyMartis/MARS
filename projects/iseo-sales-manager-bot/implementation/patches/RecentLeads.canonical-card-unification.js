// phase3f21_canonical_lead_view + iseo-canonical-lead-card-unification-v1.0
// /leads cards: lifecycle-aware header + pending action keyboard (canonical semantics).

const j = $('Check User Authorization').first().json;
const rowsRaw = $('Read CLEAN for Leads').all().map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error);

const SOURCE_DISPLAY_WEBSITE_FORM = 'Сайт i-seo.su';
const LIFE_DISPLAY = { pending: '🕓 Ожидает обработки', processed: '✅ Обработан', spam: '🚫 Спам' };

function fnvToken(s) {
  const str = String(s || '');
  let h1 = 0x811c9dc5 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h1 ^= str.charCodeAt(i);
    h1 = Math.imul(h1, 0x01000193);
  }
  let h2 = 0x9e3779b9 >>> 0;
  for (let i = 0; i < str.length; i++) {
    h2 ^= str.charCodeAt(i);
    h2 = Math.imul(h2, 0x85ebca6b);
    h2 = (h2 << 13) | (h2 >>> 19);
  }
  const hex1 = (h1 >>> 0).toString(16).padStart(8, '0');
  const hex2 = (h2 >>> 0).toString(16).padStart(8, '0');
  return (hex1 + hex2).slice(0, 12);
}


function esc(s) {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
function dash(s) {
  const v = String(s ?? '').trim();
  return v ? esc(v) : '—';
}
function formatBusinessTs(raw) {
  if (!raw) return '';
  const s = String(raw).trim();
  if (/^\d{2}\.\d{2}\.\d{4}/.test(s)) return /МСК/.test(s) ? s : (s + (/\d{2}:\d{2}/.test(s) ? ' МСК' : ''));
  if (/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/.test(s) && !/[zZ]|[+\-]\d{2}:?\d{2}$/.test(s)) {
    const m = s.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/);
    if (m) return m[3] + '.' + m[2] + '.' + m[1] + ' ' + m[4] + ':' + m[5] + ' МСК';
  }
  const d = new Date(s);
  if (Number.isNaN(d.getTime())) return s;
  const parts = new Intl.DateTimeFormat('ru-RU', { timeZone: 'Europe/Moscow', day: '2-digit', month: '2-digit', year: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(d);
  const get = (t) => (parts.find((p) => p.type === t) || {}).value || '';
  return get('day') + '.' + get('month') + '.' + get('year') + ' ' + get('hour') + ':' + get('minute') + ' МСК';
}
function resolveLifecycle(r) {
  const raw = String(r.lifecycle_status || r.manager_status || '').trim().toLowerCase();
  if (raw === 'processed' || raw === 'spam' || raw === 'pending') return raw;
  return 'pending';
}
function resolveService(r) {
  const label = String(r.resolved_service_label || '').trim();
  if (label) return label;
  if (String(r.resolved_service_code || '') === 'NeedsClarification') return 'Требует уточнения';
  return String(r.service || r.service_label || '').trim();
}
function resolveRequest(r) {
  const c = String(r.client_comment || '').trim();
  if (c) return { kind: 'comment', text: c };
  const s = String(r.request_summary || r.summary || '').trim();
  if (s) return { kind: 'summary', text: s };
  return { kind: 'absent', text: '' };
}
function resolveSourceDisplay(r) {
  const explicit = String(r.source_display || '').trim();
  if (explicit) return explicit;
  const channel = String(r.source_channel || r.source || '').trim().toLowerCase();
  if (!channel || channel === 'gmail_form' || channel === 'website_form' || channel === 'site_form') return SOURCE_DISPLAY_WEBSITE_FORM;
  return channel;
}
function adapt(r, n) {
  const life = resolveLifecycle(r);
  const req = resolveRequest(r);
  const service = resolveService(r);
  const received = r.received_at_business || r.received_at_utc || r.received_at || r.created_at || '';
  const changed = r.lifecycle_changed_at || r.manager_status_updated_at || '';
  const reply = String(r.first_reply_text || '').trim();
  return {
    public_list_number: n,
    client_name: String(r.client_name || r.name || '').trim(),
    phone: String(r.phone || '').trim(),
    resolved_service_label: service || '—',
    request_kind: req.kind,
    client_comment: req.kind === 'comment' ? req.text : '',
    request_display: req.text || '—',
    first_reply_text: reply,
    lifecycle_status: life,
    lifecycle_display: LIFE_DISPLAY[life] || LIFE_DISPLAY.pending,
    received_at_display: formatBusinessTs(received),
    lifecycle_changed_at_display: formatBusinessTs(changed),
    lifecycle_changed_by: String(r.lifecycle_changed_by || r.manager_status_updated_by || '').trim(),
    source_display: resolveSourceDisplay(r),
    lead_id: String(r.lead_id || ''),
    is_probable_test: String(r.is_probable_test).toLowerCase() === 'true',
    archive_state: String(r.archive_state || 'active'),
    stats_included: String(r.stats_included).toLowerCase() !== 'false',
    is_real_lead: String(r.is_real_lead).toLowerCase() !== 'false',
    production_generation: String(r.production_generation || ''),
    parseTs: (() => { const d = new Date(received); return Number.isNaN(d.getTime()) ? 0 : d.getTime(); })(),
  };
}
function buildCard(v, idx, total) {
  const isPending = v.lifecycle_status === 'pending';
  const lines = [];
  lines.push((isPending ? '📋 Лид ' : '📁 Архивная карточка ') + idx + ' из ' + total);
  lines.push(v.lifecycle_display);
  lines.push('');
  if (v.received_at_display) lines.push('Поступил: ' + esc(v.received_at_display));
  if (v.lifecycle_changed_at_display) lines.push('Статус изменён: ' + esc(v.lifecycle_changed_at_display));
  if (v.lifecycle_changed_by) lines.push('Кем: ' + esc(v.lifecycle_changed_by));
  lines.push('');
  lines.push('Клиент');
  lines.push(dash(v.client_name));
  lines.push('');
  if (v.phone) { lines.push('Телефон'); lines.push('<code>' + esc(v.phone) + '</code>'); lines.push(''); }
  lines.push('Интерес');
  lines.push(dash(v.resolved_service_label === '—' ? '' : v.resolved_service_label));
  lines.push('');
  if (v.request_kind === 'comment' && v.client_comment) {
    lines.push('Комментарий клиента'); lines.push(esc(v.client_comment)); lines.push('');
  } else if (v.request_display && v.request_display !== '—') {
    lines.push('Запрос'); lines.push(esc(v.request_display)); lines.push('');
  }
  lines.push('Источник');
  lines.push(esc(v.source_display));
  lines.push('');
  if (v.first_reply_text) {
    lines.push('✉️ Ответ клиенту — нажмите на блок, чтобы скопировать');
    lines.push('<pre>' + esc(v.first_reply_text) + '</pre>');
    lines.push('');
  }
  if (isPending) {
    lines.push('Рабочая карточка. Используйте кнопки ниже для обработки.');
  } else if (v.lifecycle_status === 'processed' || v.lifecycle_status === 'spam') {
    lines.push('Архивная карточка. Статус можно вернуть в обработку кнопкой ниже.');
  } else {
    lines.push('Архивная карточка.');
  }
  return lines.join('\n');
}

const args = Array.isArray(j.args) ? j.args.map((a) => String(a).trim()).filter(Boolean) : [];
let limit = 5;
let invalid = false;
if (args.length === 0) limit = 5;
else if (args.length !== 1 || !/^(3|5|10)$/.test(args[0])) invalid = true;
else limit = Number(args[0]);
if (invalid) {
  return [{ json: { ...j, leads_recovery_outcome: 'invalid_arg', reply_text: '⚠️ Укажите количество: 3, 5 или 10.\nНапример: /leads 5', events_to_append: [] } }];
}

const production = rowsRaw.filter((r) => {
  if (String(r.is_probable_test).toLowerCase() === 'true') return false;
  if (String(r.archive_state || 'active').toLowerCase() === 'archived') return false;
  if (String(r.is_real_lead).toLowerCase() === 'false') return false;
  if (String(r.stats_included).toLowerCase() === 'false') return false;
  if (String(r.production_generation || 'v2') !== 'v2') return false;
  return true;
});
const adapted = production.map((r) => adapt(r, 0)).sort((a, b) => b.parseTs - a.parseTs);
const unique = [];
const seen = new Set();
for (const v of adapted) {
  const key = v.lead_id || (v.client_name + '|' + v.received_at_display);
  if (!key || seen.has(key)) continue;
  seen.add(key);
  unique.push(v);
}
unique.forEach((v, i) => { v.public_list_number = i + 1; });
const picked = unique.slice(0, limit);
const total = picked.length;
if (total === 0) {
  return [{ json: { ...j, leads_recovery_outcome: 'empty', reply_text: '📁 Архив пуст: подходящих карточек не найдено.', requested_count: limit, returned_count: 0, available_unique: 0, events_to_append: [] } }];
}
const cards = picked.map((v, idx) => {
  const token = v.lead_id ? fnvToken(v.lead_id) : '';
  const isPending = v.lifecycle_status === 'pending';
  const canReopen = (v.lifecycle_status === 'processed' || v.lifecycle_status === 'spam') && token;
  let markup = null;
  if (isPending && token) {
    markup = {
      inline_keyboard: [
        [{ text: '✅ Обработано', callback_data: 'sm:p:' + token }],
        [{ text: '🚫 Спам', callback_data: 'sm:s:' + token }],
        [{ text: '📄 Исходная заявка', callback_data: 'sm:i:' + token }],
      ],
    };
  } else if (canReopen) {
    markup = {
      inline_keyboard: [[{ text: '↩️ Вернуть в обработку', callback_data: 'sm:r:' + token }]],
    };
  }
  return {
    json: {
      reply_text: buildCard(v, idx + 1, total),
      chat_id: j.chat_id,
      message_format_version: 'sm-msg-v2.4',
      leads_recovery_outcome: 'card',
      archive_card_index: idx + 1,
      archive_card_total: total,
      requested_count: limit,
      returned_count: total,
      available_unique: unique.length,
      lead_id: v.lead_id || '',
      manager_status: v.lifecycle_status,
      lifecycle_status: v.lifecycle_status,
      telegram_has_buttons: Boolean(markup),
      telegram_reply_markup: markup,
      telegram_callback_reopen: canReopen ? ('sm:r:' + token) : '',
      telegram_action_token: token,
      events_to_append: [],
    },
  };
});
cards.push({
  json: {
    reply_text: total < limit
      ? ('📋 Доступно уникальных лидов: ' + unique.length + ' (запрошено /leads ' + limit + '). Показано: ' + total + '.')
      : ('📋 Показано карточек: ' + total + ' (лимит /leads ' + limit + ').'),
    chat_id: j.chat_id,
    message_format_version: 'sm-msg-v2.4',
    leads_recovery_outcome: 'notice',
    archive_notice: true,
    requested_count: limit,
    returned_count: total,
    available_unique: unique.length,
    events_to_append: [],
  },
});
return cards;
