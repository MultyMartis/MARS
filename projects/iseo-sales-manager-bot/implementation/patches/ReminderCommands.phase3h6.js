// Phase 3H.6 — Reminder Commands: live ACCESS recipient count + Phase 3H.4 syntax repair.
// Phase 3H.4 — Reminder Commands repair (syntax + truthful status text).
// Emits reply_text and optional single config_write for Prepare Config Write path.
// Never throws to Telegram silence: all paths return reply_text.

const j = $input.first().json;
const cmd = String(j.command || '').toLowerCase();
const args = Array.isArray(j.args) ? j.args.map((a) => String(a).trim()).filter(Boolean) : [];
const role = String(j.auth_role || '').toLowerCase();
const map = j.config_map || {};

function esc(s) {
  return String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function validTime(s) {
  return /^([01]\d|2[0-3]):([0-5]\d)$/.test(String(s || '').trim());
}
function validTz(tz) {
  const t = String(tz || '').trim();
  if (!t) return false;
  try {
    Intl.DateTimeFormat('en-US', { timeZone: t }).format(new Date());
    return true;
  } catch (e) {
    return false;
  }
}

function formatMoscow(v) {
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

function ynExcluded(flag, defaultExcluded) {
  const raw = map[flag];
  if (raw === undefined || raw === null || String(raw).trim() === '') {
    return defaultExcluded ? 'исключены' : 'не подтверждено';
  }
  const on = String(raw).toLowerCase() === 'true';
  // include_tests=true means tests are included; display "исключены" when false
  if (flag === 'pending_reminder_include_tests') return on ? 'включены' : 'исключены';
  if (flag === 'pending_reminder_include_archive') return on ? 'включены' : 'исключены';
  return on ? 'да' : 'нет';
}

function countActiveRecipients() {
  // Phase 3H.6 — prefer live ACCESS_CONTROL (same staff predicate as Reminder Build Claims).
  // Falls back to CONFIG cache only if ACCESS read is unavailable in this execution.
  try {
    const accessRows = $('Read ACCESS_CONTROL').all().map((i) => i.json).filter((r) => r && typeof r === 'object' && !r.error);
    const seen = new Set();
    let n = 0;
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
      n += 1;
    }
    if (n > 0) return String(n);
  } catch (e) {
    // fall through to CONFIG cache
  }
  const fromCfg = map.pending_reminder_active_recipients_count || map.active_recipients_count;
  if (fromCfg !== undefined && String(fromCfg).trim() !== '') return String(fromCfg);
  return 'не подтверждено';
}

function statusText(moderatorShort) {
  const enabledRaw = map.pending_reminders_enabled;
  const enabledKnown = !(enabledRaw === undefined || enabledRaw === null || String(enabledRaw).trim() === '');
  const enabled = String(enabledRaw || '').toLowerCase() === 'true';
  const time = map.pending_reminder_time || 'не подтверждено';
  const tz = map.pending_reminder_timezone || 'не подтверждено';
  const min = map.pending_reminder_min_count || 'не подтверждено';
  const testsLine = ynExcluded('pending_reminder_include_tests', true);
  const archiveLine = ynExcluded('pending_reminder_include_archive', true);
  const once = String(map.pending_reminder_once_per_business_date || 'true').toLowerCase() !== 'false';

  const lastCheck =
    formatMoscow(map.pending_reminder_last_check_at) ||
    formatMoscow(map.pending_reminder_last_window) ||
    'не подтверждено';
  const lastSendRaw = map.pending_reminder_last_success_at;
  const lastSend = lastSendRaw && String(lastSendRaw).trim()
    ? (formatMoscow(lastSendRaw) || String(lastSendRaw))
    : 'не было';

  if (moderatorShort) {
    return [
      '⏰ Ежедневные напоминания',
      '',
      'Состояние: ' + (enabledKnown ? (enabled ? 'включены' : 'выключены') : 'не подтверждено'),
      'Время: ' + time,
      'Часовой пояс: ' + tz,
      'Тестовые заявки: ' + testsLine,
      'Архивные записи: ' + archiveLine,
    ].join('\n');
  }

  const lines = [
    '⏰ Ежедневные напоминания',
    '',
    'Состояние: ' + (enabledKnown ? (enabled ? 'включены' : 'выключены') : 'не подтверждено'),
    'Время: ' + time,
    'Часовой пояс: ' + tz,
    'Минимум необработанных заявок: ' + min,
    'Тестовые заявки: ' + testsLine,
    'Архивные записи: ' + archiveLine,
    'Получателей: ' + countActiveRecipients(),
    'Повторная отправка в течение дня: ' + (once ? 'исключена' : 'разрешена'),
    'Последняя проверка: ' + lastCheck,
    'Последняя отправка: ' + lastSend,
  ];
  return lines.join('\n');
}

function write(key, value, description) {
  return {
    key,
    value: String(value),
    type: 'string',
    updated_at: new Date().toISOString(),
    updated_by: 'admin_telegram',
    description: description || '',
  };
}

try {
  if (cmd === '/reminder_status') {
    return [{ json: { ...j, reply_text: statusText(role !== 'admin'), parse_mode: 'HTML', config_write: null } }];
  }

  if (role !== 'admin') {
    return [{ json: {
      ...j,
      reply_text: 'Изменять настройки напоминаний может только администратор.\nСмотреть статус: /reminder_status',
      parse_mode: 'HTML',
      config_write: null,
    } }];
  }

  if (cmd === '/reminder_on') {
    return [{ json: {
      ...j,
      reply_text: 'Ежедневные напоминания включены.\nВремя: ' + (map.pending_reminder_time || '10:00') + ' (' + (map.pending_reminder_timezone || 'Europe/Moscow') + ')',
      parse_mode: 'HTML',
      config_write: write('pending_reminders_enabled', 'true', 'Phase 3F.1 reminder enable'),
    } }];
  }

  if (cmd === '/reminder_off') {
    return [{ json: {
      ...j,
      reply_text: 'Ежедневные напоминания выключены.',
      parse_mode: 'HTML',
      config_write: write('pending_reminders_enabled', 'false', 'Phase 3F.1 reminder disable'),
    } }];
  }

  if (cmd === '/reminder_time') {
    const t = args[0] || '';
    if (!validTime(t)) {
      return [{ json: {
        ...j,
        reply_text: 'Укажите время в формате ЧЧ:ММ.\nНапример: /reminder_time 10:00',
        parse_mode: 'HTML',
        config_write: null,
      } }];
    }
    return [{ json: {
      ...j,
      reply_text: 'Время напоминания установлено: ' + t,
      parse_mode: 'HTML',
      config_write: write('pending_reminder_time', t, 'Phase 3F.1 reminder time'),
    } }];
  }

  if (cmd === '/reminder_timezone') {
    const tz = args[0] || '';
    if (!validTz(tz)) {
      return [{ json: {
        ...j,
        reply_text: 'Укажите корректный часовой пояс IANA.\nНапример: /reminder_timezone Europe/Moscow',
        parse_mode: 'HTML',
        config_write: null,
      } }];
    }
    return [{ json: {
      ...j,
      reply_text: 'Часовой пояс напоминания: ' + esc(tz),
      parse_mode: 'HTML',
      config_write: write('pending_reminder_timezone', tz, 'Phase 3F.1 reminder timezone'),
    } }];
  }

  if (cmd === '/reminder_min') {
    const n = Number(args[0]);
    if (!Number.isInteger(n) || n < 1 || n > 100) {
      return [{ json: {
        ...j,
        reply_text: 'Укажите целое число от 1 до 100.\nНапример: /reminder_min 1',
        parse_mode: 'HTML',
        config_write: null,
      } }];
    }
    return [{ json: {
      ...j,
      reply_text: 'Минимум необработанных заявок для напоминания: ' + n,
      parse_mode: 'HTML',
      config_write: write('pending_reminder_min_count', String(n), 'Phase 3F.1 reminder min count'),
    } }];
  }

  return [{ json: { ...j, reply_text: 'Неизвестная команда напоминаний.', parse_mode: 'HTML', config_write: null } }];
} catch (e) {
  return [{ json: {
    ...j,
    reply_text: 'Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.',
    parse_mode: 'HTML',
    config_write: null,
    command_response_guard: 'runtime_exception',
    error_node: 'Reminder Commands',
    deny_reason: 'processing_failure',
  } }];
}
