// Phase 3D.6 — ADMIN Deny Reply
/**
 * Phase 3D.5 — public access + ACCESS_CONTROL registry authorization.
 * Pure module for harness + n8n Code sync. No raw Telegram IDs in fixtures.
 */

const ACCESS_HEADERS = [
  'telegram_user_id',
  'telegram_user_hash',
  'telegram_username',
  'display_name',
  'role',
  'status',
  'first_seen_at',
  'last_seen_at',
  'requested_at',
  'approved_at',
  'approved_by',
  'revoked_at',
  'revoked_by',
  'source',
  'notes',
];

const ACCESS_EVENT_HEADERS = [
  'ts',
  'opaque_user_ref',
  'event',
  'prior_role',
  'prior_status',
  'new_role',
  'new_status',
  'actor_ref',
  'source',
  'outcome',
  'detail',
];

const ADMIN_ONLY_COMMANDS = new Set([
  '/config',
  '/health',
  '/status',
  '/stats',
  '/last_error',
  '/ai_on',
  '/ai_off',
  '/ai_status',
    '/test_lead',
  '/aistatus',
  '/lasterror',
  '/moderators',
  '/moderator_pending',
  '/moderator_info',
  '/moderator_add',
  '/moderator_remove',
]);

const PUBLIC_COMMANDS = new Set(['/start', '/help', '/my_status']);

/** Admin bootstrap (CONFIG admin_user_ids) — recovery-only when ACCESS_CONTROL read fails technically. */
const ADMIN_BOOTSTRAP_COMMANDS = new Set([
  '/start',
  '/help',
  '/my_status',
  '/status',
  '/health',
  '/config',
  '/moderators',
  '/moderator_pending',
]);

/**
 * Pure JS SHA-256 (hex lowercase). n8n task-runner disallows the Node crypto module.
 * Must remain bit-compatible with Node createHash('sha256').
 */
function sha256hex(ascii) {
  const mathPow = Math.pow;
  const maxWord = mathPow(2, 32);
  const lengthProperty = 'length';
  let i, j;
  let result = '';

  const words = [];
  const asciiBitLength = ascii[lengthProperty] * 8;

  let hash = (sha256hex.h = sha256hex.h || []);
  const k = (sha256hex.k = sha256hex.k || []);
  let primeCounter = k[lengthProperty];

  const isComposite = {};
  for (let candidate = 2; primeCounter < 64; candidate++) {
    if (!isComposite[candidate]) {
      for (i = 0; i < 313; i += candidate) isComposite[i] = candidate;
      hash[primeCounter] = (mathPow(candidate, 0.5) * maxWord) | 0;
      k[primeCounter++] = (mathPow(candidate, 1 / 3) * maxWord) | 0;
    }
  }

  ascii += '\x80';
  while ((ascii[lengthProperty] % 64) - 56) ascii += '\x00';
  for (i = 0; i < ascii[lengthProperty]; i++) {
    j = ascii.charCodeAt(i);
    if (j >> 8) return ''; // ASCII only path for our IDs/codes
    words[i >> 2] |= j << (((3 - i) % 4) * 8);
  }
  words[words[lengthProperty]] = (asciiBitLength / maxWord) | 0;
  words[words[lengthProperty]] = asciiBitLength;

  for (j = 0; j < words[lengthProperty]; ) {
    const w = words.slice(j, (j += 16));
    const oldHash = hash;
    hash = hash.slice(0, 8);

    for (i = 0; i < 64; i++) {
      const w15 = w[i - 15];
      const w2 = w[i - 2];
      const a = hash[0];
      const e = hash[4];
      const temp1 =
        hash[7] +
        (((e >>> 6) | (e << 26)) ^ ((e >>> 11) | (e << 21)) ^ ((e >>> 25) | (e << 7))) +
        ((e & hash[5]) ^ (~e & hash[6])) +
        k[i] +
        (w[i] =
          i < 16
            ? w[i]
            : (w[i - 16] +
                (((w15 >>> 7) | (w15 << 25)) ^ ((w15 >>> 18) | (w15 << 14)) ^ (w15 >>> 3)) +
                w[i - 7] +
                (((w2 >>> 17) | (w2 << 15)) ^ ((w2 >>> 19) | (w2 << 13)) ^ (w2 >>> 10))) |
              0);
      const temp2 =
        (((a >>> 2) | (a << 30)) ^ ((a >>> 13) | (a << 19)) ^ ((a >>> 22) | (a << 10))) +
        ((a & hash[1]) ^ (a & hash[2]) ^ (hash[1] & hash[2]));
      hash = [(temp1 + temp2) | 0].concat(hash);
      hash[4] = (hash[4] + temp1) | 0;
      hash.pop();
    }
    for (i = 0; i < 8; i++) hash[i] = (hash[i] + oldHash[i]) | 0;
  }

  for (i = 0; i < 8; i++) {
    for (j = 3; j + 1; j--) {
      const b = (hash[i] >> (j * 8)) & 255;
      result += (b < 16 ? '0' : '') + b.toString(16);
    }
  }
  return result;
}

function idHash(v) {
  return sha256hex(v).slice(0, 16).toUpperCase();
}

/** Short opaque approval / moderator code — never raw Telegram ID. */
function accessCode(userId) {
  return sha256hex('sm-access:' + String(userId || '')).slice(0, 6).toUpperCase();
}

function opaqueUserRef(userId) {
  return 'u:' + idHash(userId).slice(0, 12);
}

function parseIds(value) {
  if (Array.isArray(value)) return value.map((v) => String(v).trim()).filter(Boolean);
  return String(value || '').split(/[,;\s]+/).map((v) => v.trim()).filter(Boolean);
}

function normalizeUsername(u) {
  const s = String(u || '').trim();
  if (!s) return '';
  return s.startsWith('@') ? s : '@' + s;
}

function displayNameFrom(parts = {}) {
  const dn = String(parts.display_name || '').trim();
  if (dn) return dn;
  const joined = [parts.first_name, parts.last_name].filter(Boolean).join(' ').trim();
  if (joined) return joined;
  const un = normalizeUsername(parts.username || parts.telegram_username);
  if (un) return un;
  return 'Пользователь';
}

function fmtDate(iso) {
  if (!iso) return '—';
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return '—';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit', month: '2-digit', year: 'numeric',
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return get('day') + '.' + get('month') + '.' + get('year');
}

function fmtDateTime(iso) {
  if (!iso) return '—';
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return '—';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow',
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit', hour12: false,
  }).formatToParts(d);
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  return get('day') + '.' + get('month') + '.' + get('year') + ' ' + get('hour') + ':' + get('minute');
}

function rowFromSheet(r = {}) {
  return {
    telegram_user_id: String(r.telegram_user_id ?? ''),
    telegram_user_hash: String(r.telegram_user_hash ?? ''),
    telegram_username: normalizeUsername(r.telegram_username),
    display_name: String(r.display_name ?? ''),
    role: String(r.role ?? '').toLowerCase(),
    status: String(r.status ?? '').toLowerCase(),
    first_seen_at: String(r.first_seen_at ?? ''),
    last_seen_at: String(r.last_seen_at ?? ''),
    requested_at: String(r.requested_at ?? ''),
    approved_at: String(r.approved_at ?? ''),
    approved_by: String(r.approved_by ?? ''),
    revoked_at: String(r.revoked_at ?? ''),
    revoked_by: String(r.revoked_by ?? ''),
    source: String(r.source ?? ''),
    notes: String(r.notes ?? ''),
  };
}

function findAccessRow(rows, userId) {
  const uid = String(userId || '');
  if (!uid) return null;
  const list = (rows || []).map(rowFromSheet).filter((r) => r.telegram_user_id);
  return list.find((r) => r.telegram_user_id === uid) || null;
}

function findByAccessCode(rows, code) {
  const c = String(code || '').trim().toUpperCase();
  if (!c) return null;
  const list = (rows || []).map(rowFromSheet).filter((r) => r.telegram_user_id);
  return list.find((r) => accessCode(r.telegram_user_id) === c) || null;
}

/**
 * Resolve effective role from ACCESS_CONTROL (primary SoT).
 * Explicit ACCESS_CONTROL row always wins (including revoked/blocked).
 * CONFIG admin_user_ids = emergency Admin bootstrap ONLY when registry read fails technically.
 * CONFIG manager_action_user_ids is legacy — never an active authorization source.
 */
function resolveIdentity({
  user_id,
  access_rows,
  admin_user_ids,
  manager_action_user_ids,
  registry_read_ok = true,
}) {
  const uid = String(user_id || '');
  const row = findAccessRow(access_rows, uid);
  const admins = parseIds(admin_user_ids);
  const configAdmin = admins.includes(uid);
  // manager_action_user_ids intentionally unused for authorization (legacy only).
  void manager_action_user_ids;

  if (row) {
    if (row.status === 'blocked' || row.role === 'blocked') {
      return { role: 'blocked', status: 'blocked', row, registry_source: 'ACCESS_CONTROL' };
    }
    if (row.role === 'admin' && row.status === 'active') {
      return { role: 'admin', status: 'active', row, registry_source: 'ACCESS_CONTROL' };
    }
    if (row.role === 'moderator' && row.status === 'active') {
      return { role: 'moderator', status: 'active', row, registry_source: 'ACCESS_CONTROL' };
    }
    if (row.status === 'revoked') {
      return { role: 'public', status: 'revoked', row, registry_source: 'ACCESS_CONTROL' };
    }
    // pending / public
    return {
      role: row.role === 'public' || !row.role ? 'public' : row.role,
      status: row.status || 'pending',
      row,
      registry_source: 'ACCESS_CONTROL',
    };
  }

  // No matching row — Admin bootstrap only on technical registry failure (never moderator fail-open).
  if (!registry_read_ok && configAdmin) {
    return { role: 'admin', status: 'active', row: null, registry_source: 'ADMIN_BOOTSTRAP', authorization_source: 'admin_bootstrap_recovery' };
  }
  return {
    role: 'public',
    status: 'none',
    row: null,
    registry_source: registry_read_ok ? 'none' : 'registry_unavailable',
  };
}

function authorizeUser({
  user_id,
  command,
  access_rows,
  admin_user_ids,
  manager_action_user_ids,
  registry_read_ok = true,
}) {
  const cmd = String(command || '').trim().toLowerCase();
  const identity = resolveIdentity({
    user_id,
    access_rows,
    admin_user_ids,
    manager_action_user_ids,
    registry_read_ok,
  });
  const { role, status } = identity;
  const actionCapable = (role === 'admin' || role === 'moderator') && status === 'active';
  const bootstrap = identity.registry_source === 'ADMIN_BOOTSTRAP';
  const isMyStatus = cmd === '/my_status';

  // /my_status is allowed for blocked users (status-only response).
  if ((role === 'blocked' || status === 'blocked') && !isMyStatus) {
    return {
      authorized: false,
      auth_role: 'blocked',
      manager_action_authorized: false,
      deny_reason: 'blocked',
      identity,
    };
  }

  // Technical registry failure for non-bootstrap users.
  if (!registry_read_ok && !bootstrap) {
    if (isMyStatus) {
      return {
        authorized: false,
        auth_role: role === 'public' ? 'public' : role,
        manager_action_authorized: false,
        deny_reason: 'registry_unavailable',
        identity,
      };
    }
    if (PUBLIC_COMMANDS.has(cmd)) {
      return {
        authorized: true,
        auth_role: 'public',
        manager_action_authorized: false,
        deny_reason: null,
        identity,
      };
    }
    return {
      authorized: false,
      auth_role: role === 'public' ? 'public' : role,
      manager_action_authorized: false,
      deny_reason: 'registry_unavailable',
      identity,
    };
  }

  if (bootstrap) {
    if (ADMIN_BOOTSTRAP_COMMANDS.has(cmd) || cmd === '/__callback') {
      if (cmd === '/__callback') {
        return {
          authorized: false,
          auth_role: 'admin',
          manager_action_authorized: false,
          deny_reason: 'registry_unavailable',
          identity,
        };
      }
      return {
        authorized: true,
        auth_role: 'admin',
        manager_action_authorized: true,
        deny_reason: null,
        identity,
        authorization_source: 'admin_bootstrap_recovery',
      };
    }
    return {
      authorized: false,
      auth_role: 'admin',
      manager_action_authorized: false,
      deny_reason: 'bootstrap_limited',
      identity,
      authorization_source: 'admin_bootstrap_recovery',
    };
  }

  if (cmd === '/__callback') {
    if (actionCapable) {
      return {
        authorized: true,
        auth_role: role,
        manager_action_authorized: true,
        deny_reason: null,
        identity,
      };
    }
    return {
      authorized: false,
      auth_role: role === 'public' || status === 'pending' || status === 'revoked' ? role : 'public',
      manager_action_authorized: false,
      deny_reason: 'callback_denied',
      identity,
    };
  }

  if (isMyStatus) {
    const rowRole = identity.row ? String(identity.row.role || '').toLowerCase() : role;
    let auth_role = 'public';
    if (role === 'blocked' || status === 'blocked') auth_role = 'blocked';
    else if (role === 'admin' && status === 'active') auth_role = 'admin';
    else if (role === 'moderator' && status === 'active') auth_role = 'moderator';
    else if (status === 'revoked' || (rowRole === 'moderator' && status === 'revoked')) auth_role = 'revoked';
    else if ((role === 'public' || rowRole === 'public') && status === 'pending') auth_role = 'pending';
    else auth_role = 'public';
    return {
      authorized: true,
      auth_role,
      manager_action_authorized: actionCapable,
      deny_reason: null,
      identity,
    };
  }

  if (PUBLIC_COMMANDS.has(cmd)) {
    return {
      authorized: true,
      auth_role: role === 'admin' ? 'admin' : (role === 'moderator' && status === 'active' ? 'moderator' : 'public'),
      manager_action_authorized: actionCapable,
      deny_reason: null,
      identity,
    };
  }

  if (ADMIN_ONLY_COMMANDS.has(cmd)) {
    if (role === 'admin' && status === 'active') {
      return {
        authorized: true,
        auth_role: 'admin',
        manager_action_authorized: true,
        deny_reason: null,
        identity,
      };
    }
    if (role === 'moderator' && status === 'active') {
      return {
        authorized: false,
        auth_role: 'moderator',
        manager_action_authorized: true,
        deny_reason: 'admin_only',
        identity,
      };
    }
    return {
      authorized: false,
      auth_role: 'public',
      manager_action_authorized: false,
      deny_reason: 'staff_only',
      identity,
    };
  }

  return {
    authorized: true,
    auth_role: role === 'admin' && status === 'active' ? 'admin'
      : (role === 'moderator' && status === 'active' ? 'moderator' : 'public'),
    manager_action_authorized: actionCapable,
    deny_reason: null,
    identity,
    unknown_command: true,
  };
}

function contourLabel(config = {}) {
  const env = String(config.environment || 'dev').toLowerCase();
  const isProd = env === 'production' || env === 'prod';
  return isProd ? 'рабочий' : 'разработка';
}

function aiLabel(config = {}) {
  const on = config.ai_enabled === true || config.ai_enabled === 'true';
  return on ? 'включён' : 'выключен';
}

/** Escape plain text for Telegram HTML parse_mode. */
function escHtml(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/** Render a canonical command so underscores cannot be eaten by Markdown/legacy parse modes. */
function cmdHtml(command) {
  return '<code>' + escHtml(command) + '</code>';
}

function startReply(role, config = {}) {
  if (role === 'admin') {
    return [
      'Sales Manager Admin запущен.',
      '',
      'Контур: ' + escHtml(contourLabel(config)),
      'Режим ИИ: ' + escHtml(aiLabel(config)),
      '',
      'Используйте ' + cmdHtml('/help') + ', чтобы посмотреть доступные команды.',
    ].join('\n');
  }
  if (role === 'moderator') {
    return [
      'Sales Manager готов к работе.',
      '',
      'Здесь приходят заявки клиентов.',
      'В карточках можно скопировать контакт и готовый ответ, а также отметить лид обработанным или как спам.',
    ].join('\n');
  }
  if (role === 'blocked') {
    return 'Доступ к боту ограничен.';
  }
  return [
    'Sales Manager',
    '',
    'Бот помогает сотрудникам i-SEO работать с заявками клиентов.',
    '',
    'Доступные команды:',
    cmdHtml('/help') + ' — информация о боте',
    cmdHtml('/my_status') + ' — ваши текущие права',
    '',
    'Для получения рабочих прав обратитесь к администратору.',
  ].join('\n');
}

function helpReply(role) {
  if (role === 'moderator') {
    return [
      'Помощь по работе с лидами',
      '',
      cmdHtml('/my_status') + ' — ваш текущий рабочий статус',
      '',
      'Индикаторы типа лида:',
      '🟢 Новый лид — новая заявка',
      '🟡 Повторный — контакт уже встречался',
      '🟠 Возможный повтор — совпал сайт',
      '🔵 Повторная обработка — техническое повторное прохождение',
      '',
      'Блоки для копирования: имя, контакт и готовый ответ.',
      '',
      'Кнопки:',
      '✅ Обработан — вы связались с клиентом',
      '🚫 Спам — заявка нецелевая или мусорная',
      '',
      'Статус в v1 нельзя обратить назад.',
      'При ошибке обратитесь к администратору.',
    ].join('\n');
  }
  if (role === 'public') {
    return [
      'Помощь Sales Manager',
      '',
      'Бот используется командой i-SEO для работы с заявками.',
      '',
      'Обычному пользователю доступна справочная информация.',
      cmdHtml('/my_status') + ' — ваши текущие права',
      'Рабочие права выдаёт администратор индивидуально.',
    ].join('\n');
  }
  return [
    '📖 Команды Sales Manager Admin',
    '',
    '🚀 Начало:',
    cmdHtml('/start') + ' — открыть панель бота',
    cmdHtml('/my_status') + ' — ваш текущий статус доступа',
    '',
    '📊 Состояние:',
    cmdHtml('/status') + ' — состояние процессов',
    cmdHtml('/health') + ' — проверка зависимостей',
    cmdHtml('/stats') + ' — статистика за 7 дней',
    cmdHtml('/last_error') + ' — последняя ошибка',
    '',
    '🕘 История:',
    cmdHtml('/leads') + ' 3 — последние 3 карточки лидов из архива',
    cmdHtml('/leads') + ' 5 — последние 5 карточек лидов из архива',
    cmdHtml('/leads') + ' 10 — последние 10 карточек лидов из архива',
    '',
    '🤖 ИИ:',
    cmdHtml('/ai_status') + ' — текущий режим',
    cmdHtml('/ai_on') + ' — включить ИИ',
    cmdHtml('/ai_off') + ' — выключить ИИ',
    '',
    '⚙️ Настройки:',
    cmdHtml('/config') + ' — безопасная сводка',
    cmdHtml('/help') + ' — список команд',
    '',
    'Пользователи:',
    cmdHtml('/moderators') + ' — активные модераторы',
    cmdHtml('/moderator_pending') + ' — новые заявки и временно отозванные модераторы',
    cmdHtml('/moderator_info') + ' — информация о пользователе',
    cmdHtml('/moderator_add') + ' — выдать права модератора',
    cmdHtml('/moderator_remove') + ' — отозвать права модератора',
  ].join('\n');
}

const GRANT_MODERATOR_NOTIFY_TEXT = [
  'Вам выданы права модератора Sales Manager.',
  '',
  'Теперь вы можете работать с карточками лидов и отмечать их обработанными или как спам.',
  '',
  'Используйте /start или /help.',
].join('\n');

const REVOKE_MODERATOR_NOTIFY_TEXT = [
  'Ваши права модератора Sales Manager отозваны.',
  '',
  'Публичные команды /start, /help и /my_status остаются доступны.',
].join('\n');

const NOTIFY_PARTIAL_ADMIN_REPLY = 'Права изменены, но уведомление пользователю доставить не удалось.';

function myStatusReply({ auth_role, identity, bootstrap = false } = {}) {
  if (bootstrap) {
    return [
      'Ваш статус',
      '',
      'Роль: администратор',
      'Статус: активен (восстановление)',
      '',
      'Реестр доступа временно недоступен. Базовые команды восстановления доступны.',
    ].join('\n');
  }
  const role = String(auth_role || '').toLowerCase();
  const row = identity && identity.row ? identity.row : null;
  const st = String((row && row.status) || (identity && identity.status) || '').toLowerCase();
  const rr = String((row && row.role) || (identity && identity.role) || '').toLowerCase();

  if (role === 'blocked' || rr === 'blocked' || st === 'blocked') {
    return ['Ваш статус', '', 'Доступ к боту ограничен.'].join('\n');
  }
  if (role === 'revoked' || (rr === 'moderator' && st === 'revoked')) {
    return [
      'Ваш статус',
      '',
      'Роль: бывший модератор',
      'Рабочие права: отозваны',
      '',
      'Публичные команды остаются доступны.',
      'Для восстановления прав обратитесь к администратору.',
    ].join('\n');
  }
  if (role === 'admin' || (rr === 'admin' && st === 'active')) {
    return [
      'Ваш статус',
      '',
      'Роль: администратор',
      'Статус: активен',
      '',
      'Доступны административные команды и управление модераторами.',
    ].join('\n');
  }
  if (role === 'moderator' || (rr === 'moderator' && st === 'active')) {
    return [
      'Ваш статус',
      '',
      'Роль: модератор',
      'Статус: активен',
      '',
      'Доступно:',
      '— работа с карточками лидов;',
      '— отметка «Обработан»;',
      '— отметка «Спам».',
      '',
      'Административные настройки недоступны.',
    ].join('\n');
  }
  if (role === 'pending' || (rr === 'public' && st === 'pending')) {
    return [
      'Ваш статус',
      '',
      'Роль: обычный пользователь',
      'Заявка на рабочий доступ: ожидает подтверждения',
      '',
      'Администратор ещё не выдал права модератора.',
    ].join('\n');
  }
  return [
    'Ваш статус',
    '',
    'Роль: обычный пользователь',
    'Рабочие права: не выданы',
    '',
    'Доступно:',
    cmdHtml('/start'),
    cmdHtml('/help'),
    cmdHtml('/my_status'),
    '',
    'Чтобы получить права модератора, обратитесь к администратору.',
  ].join('\n');
}

function buildNotificationEvent({
  kind,
  sent,
  user_id,
  actor_ref,
  role,
  status,
  error_code = '',
  nowIso,
}) {
  const grant = kind === 'grant';
  const event = sent
    ? (grant ? 'moderator_grant_notification_sent' : 'moderator_revoke_notification_sent')
    : (grant ? 'moderator_grant_notification_failed' : 'moderator_revoke_notification_failed');
  return {
    ts: nowIso || new Date().toISOString(),
    opaque_user_ref: opaqueUserRef(user_id),
    event,
    prior_role: role || '',
    prior_status: status || '',
    new_role: role || '',
    new_status: status || '',
    actor_ref: actor_ref || '',
    source: 'telegram_notify',
    outcome: sent ? 'ok' : 'failed',
    detail: error_code ? ('err:' + error_code) : (sent ? 'delivered' : 'undelivered'),
  };
}

function detectNotifyDeliveryFailure(notifyResult = {}, notify_chat_id = '') {
  if (!String(notify_chat_id || '').trim()) {
    return { failed: true, error_code: 'notify_target_unavailable' };
  }
  const j = notifyResult || {};
  if (j.error || j.errorMessage) return { failed: true, error_code: 'telegram_delivery_failed' };
  if (j.name === 'NodeApiError' || j.name === 'NodeOperationError') {
    return { failed: true, error_code: 'telegram_delivery_failed' };
  }
  const msg = String(j.message || j.description || '');
  if (/forbidden|chat not found|bot was blocked|unauthorized|ECONN|ETIMEDOUT|429/i.test(msg)) {
    return { failed: true, error_code: 'telegram_delivery_failed' };
  }
  if (j.ok === false) return { failed: true, error_code: 'telegram_delivery_failed' };
  return { failed: false, error_code: '' };
}

function denyReply({ auth_role, deny_reason }) {
  if (deny_reason === 'blocked' || auth_role === 'blocked') {
    return 'Доступ к боту ограничен.';
  }
  if (deny_reason === 'registry_unavailable') {
    return 'Сервис временно недоступен. Попробуйте позже.';
  }
  if (deny_reason === 'bootstrap_limited') {
    return 'Сервис временно недоступен. Попробуйте позже.';
  }
  if (deny_reason === 'processing_failure') {
    return 'Не удалось обработать команду. Ошибка зарегистрирована.';
  }
  if (deny_reason === 'admin_only' && auth_role === 'moderator') {
    return 'Команда доступна только администратору.';
  }
  if (deny_reason === 'callback_denied') {
    return 'Недостаточно прав.';
  }
  if (deny_reason === 'staff_only') {
    return 'Команда доступна только сотрудникам с рабочими правами.';
  }
  return 'Команда доступна только сотрудникам с рабочими правами.';
}

function unknownCommandReply() {
  return 'Команда не найдена. Используйте /help.';
}

function buildPublicStartUpsert({ user_id, username, display_name, existing, nowIso }) {
  const uid = String(user_id || '');
  const un = normalizeUsername(username);
  const dn = displayNameFrom({ display_name, username: un });
  const code = accessCode(uid);
  if (existing && existing.telegram_user_id === uid) {
    // preserve first_seen; refresh username/last_seen; do not escalate role
    const role = existing.role === 'admin' || existing.role === 'moderator' || existing.role === 'blocked'
      ? existing.role
      : 'public';
    const status = existing.status === 'active' || existing.status === 'blocked' || existing.status === 'revoked'
      ? existing.status
      : 'pending';
    return {
      mutate: true,
      is_new: false,
      row: {
        ...existing,
        telegram_user_id: uid,
        telegram_user_hash: idHash(uid),
        telegram_username: un || existing.telegram_username,
        display_name: dn !== 'Пользователь' ? dn : (existing.display_name || dn),
        role,
        status,
        first_seen_at: existing.first_seen_at || nowIso,
        last_seen_at: nowIso,
        requested_at: existing.requested_at || (status === 'pending' ? nowIso : existing.requested_at),
        source: existing.source || 'telegram_start',
        notes: existing.notes || ('code:' + code),
      },
      event: status === 'pending' && role === 'public' ? {
        event: existing.requested_at ? 'public_user_seen' : 'moderator_requested',
        prior_role: existing.role,
        prior_status: existing.status,
        new_role: role,
        new_status: status,
      } : {
        event: 'public_user_seen',
        prior_role: existing.role,
        prior_status: existing.status,
        new_role: role,
        new_status: status,
      },
      notify_admin: false,
    };
  }
  return {
    mutate: true,
    is_new: true,
    row: {
      telegram_user_id: uid,
      telegram_user_hash: idHash(uid),
      telegram_username: un,
      display_name: dn,
      role: 'public',
      status: 'pending',
      first_seen_at: nowIso,
      last_seen_at: nowIso,
      requested_at: nowIso,
      approved_at: '',
      approved_by: '',
      revoked_at: '',
      revoked_by: '',
      source: 'telegram_start',
      notes: 'code:' + code,
    },
    event: {
      event: 'moderator_requested',
      prior_role: '',
      prior_status: '',
      new_role: 'public',
      new_status: 'pending',
    },
    notify_admin: false,
  };
}

function listActiveModerators(rows) {
  return (rows || []).map(rowFromSheet).filter((r) => r.role === 'moderator' && r.status === 'active');
}

function listPending(rows, limit = 20) {
  return (rows || [])
    .map(rowFromSheet)
    .filter((r) => (r.role === 'public' || !r.role) && (r.status === 'pending' || r.status === 'none'))
    .sort((a, b) => String(b.requested_at || b.first_seen_at).localeCompare(String(a.requested_at || a.first_seen_at)))
    .slice(0, limit);
}

function formatModeratorsList(rows) {
  const mods = listActiveModerators(rows);
  if (!mods.length) {
    return 'Модераторы\n\nАктивных модераторов нет.\n\nВсего модераторов: 0';
  }
  const lines = ['Модераторы', ''];
  mods.forEach((m, i) => {
    const name = m.display_name || 'Без имени';
    const un = m.telegram_username || '—';
    lines.push((i + 1) + '. ' + name + ' · ' + un);
    lines.push('   Статус: активен');
    lines.push('   Добавлена: ' + fmtDate(m.approved_at || m.first_seen_at));
    lines.push('   Код: ' + accessCode(m.telegram_user_id));
    lines.push('');
  });
  lines.push('Всего модераторов: ' + mods.length);
  return lines.join('\n');
}

function listRevokedFormerModerators(rows, limit = 20) {
  return (rows || [])
    .map(rowFromSheet)
    .filter((r) => {
      if (r.status !== 'revoked') return false;
      if (r.role === 'admin' || r.role === 'blocked' || r.role === 'public') return false;
      if (r.role !== 'moderator') {
        const notes = String(r.notes || '').toLowerCase();
        if (!notes.includes('former_moderator') && !notes.includes('was_moderator')) return false;
      }
      return Boolean(accessCode(r.telegram_user_id));
    })
    .sort((a, b) => String(b.revoked_at || '').localeCompare(String(a.revoked_at || '')))
    .slice(0, limit);
}

function formatPendingList(rows) {
  const pending = listPending(rows);
  const revoked = listRevokedFormerModerators(rows);
  const lines = [];
  if (pending.length) {
    lines.push('Ожидают подтверждения', '');
    pending.forEach((p, i) => {
      const name = p.display_name || 'Новый пользователь';
      const un = p.telegram_username || '';
      lines.push((i + 1) + '. ' + (un ? (name + ' · ' + un) : name));
      lines.push('   Код заявки: ' + accessCode(p.telegram_user_id));
      lines.push('   Первый вход: ' + fmtDateTime(p.first_seen_at || p.requested_at));
      lines.push('');
    });
  } else {
    lines.push('Новых заявок на рабочий доступ нет.');
  }
  if (revoked.length) {
    if (lines.length) lines.push('');
    lines.push('Права временно отозваны', '');
    revoked.forEach((r, i) => {
      const name = r.display_name || 'Пользователь';
      const un = r.telegram_username || '';
      lines.push((i + 1) + '. ' + (un ? (name + ' · ' + un) : name));
      lines.push('   Код: ' + accessCode(r.telegram_user_id));
      lines.push('   Права отозваны: ' + fmtDate(r.revoked_at));
      lines.push('');
    });
  } else if (!pending.length) {
    lines.push('');
    lines.push('Пользователей с временно отозванными правами нет.');
  }
  return lines.join('\n').replace(/\n+$/, '');
}

function formatModeratorInfo(row) {
  if (!row) return 'Пользователь с таким кодом не найден.';
  const r = rowFromSheet(row);
  return [
    'Информация о пользователе',
    '',
    'Имя: ' + (r.display_name || '—'),
    'Username: ' + (r.telegram_username || '—'),
    'Роль: ' + (r.role || '—'),
    'Статус: ' + (r.status || '—'),
    'Первый вход: ' + fmtDateTime(r.first_seen_at),
    'Одобрен: ' + fmtDateTime(r.approved_at),
    'Отозван: ' + fmtDateTime(r.revoked_at),
    'Последняя активность: ' + fmtDateTime(r.last_seen_at),
    'Код: ' + accessCode(r.telegram_user_id),
  ].join('\n');
}

function approveModerator({ rows, code, actor_ref, nowIso }) {
  const row = findByAccessCode(rows, code);
  if (!row) return { ok: false, reply: 'Заявка с таким кодом не найдена.' };
  if (row.status === 'blocked' || row.role === 'blocked') {
    return { ok: false, reply: 'Пользователь заблокирован. Выдача прав невозможна.' };
  }
  if (row.role === 'admin') {
    return { ok: false, reply: 'Это администратор. Команда модератора не применяется.' };
  }
  if (row.role === 'moderator' && row.status === 'active') {
    return {
      ok: true,
      idempotent: true,
      reply: 'Права модератора уже выданы: ' + (row.display_name || 'Пользователь') + ' · ' + (row.telegram_username || '—'),
      row,
      notify_text: null,
      event: null,
    };
  }
  const updated = {
    ...row,
    role: 'moderator',
    status: 'active',
    approved_at: nowIso,
    approved_by: actor_ref,
    revoked_at: '',
    revoked_by: '',
    last_seen_at: nowIso,
  };
  return {
    ok: true,
    idempotent: false,
    reply: 'Права модератора выданы: ' + (updated.display_name || 'Пользователь') + ' · ' + (updated.telegram_username || '—'),
    row: updated,
    notify_chat_id: updated.telegram_user_id,
    notify_text: GRANT_MODERATOR_NOTIFY_TEXT,
    notify_kind: 'grant',
    event: {
      event: 'moderator_approved',
      prior_role: row.role,
      prior_status: row.status,
      new_role: 'moderator',
      new_status: 'active',
    },
  };
}

function revokeModerator({ rows, code, actor_ref, nowIso, admin_user_ids }) {
  const row = findByAccessCode(rows, code);
  if (!row) return { ok: false, reply: 'Модератор с таким кодом не найден.' };
  if (row.role === 'admin' || (row.status === 'active' && parseIds(admin_user_ids).includes(row.telegram_user_id) && row.role !== 'moderator')) {
    return { ok: false, reply: 'Нельзя отозвать права администратора командой модератора.' };
  }
  if (row.role === 'admin') {
    return { ok: false, reply: 'Нельзя отозвать права администратора командой модератора.' };
  }
  // protect last admin indirectly — moderator command cannot target admin
  if (row.role !== 'moderator' && row.status !== 'active') {
    return { ok: false, reply: 'Активный модератор с таким кодом не найден.' };
  }
  if (row.status === 'revoked') {
    return {
      ok: true,
      idempotent: true,
      reply: 'Права модератора отозваны.',
      row,
      notify_text: null,
      event: null,
    };
  }
  const updated = {
    ...row,
    role: 'moderator',
    status: 'revoked',
    revoked_at: nowIso,
    revoked_by: actor_ref,
    last_seen_at: nowIso,
  };
  return {
    ok: true,
    idempotent: false,
    reply: 'Права модератора отозваны.',
    row: updated,
    notify_chat_id: updated.telegram_user_id,
    notify_text: REVOKE_MODERATOR_NOTIFY_TEXT,
    notify_kind: 'revoke',
    event: {
      event: 'moderator_revoked',
      prior_role: row.role,
      prior_status: row.status,
      new_role: 'moderator',
      new_status: 'revoked',
    },
  };
}

function countActionCapable(rows, admin_user_ids, manager_action_user_ids) {
  // Counts always come from ACCESS_CONTROL (primary SoT). CONFIG allowlists are not count sources.
  void admin_user_ids;
  void manager_action_user_ids;
  const fromRegistry = (rows || []).map(rowFromSheet).filter((r) =>
    (r.role === 'admin' || r.role === 'moderator') && r.status === 'active');
  const admins = fromRegistry.filter((r) => r.role === 'admin').length;
  const mods = fromRegistry.filter((r) => r.role === 'moderator').length;
  return {
    adminCount: admins,
    moderatorCount: mods,
    actionCapable: admins + mods,
    source: 'ACCESS_CONTROL',
  };
}

/** Validate role / status vocabulary (rejects numeric metadata such as "42"). */
function isValidAccessRole(role) {
  return ['public', 'moderator', 'admin', 'blocked'].includes(String(role || '').toLowerCase());
}
function isValidAccessStatus(status) {
  return ['pending', 'active', 'revoked', 'blocked'].includes(String(status || '').toLowerCase());
}


const j = $input.first().json;
const text = denyReply({ auth_role: j.auth_role, deny_reason: j.deny_reason, command: j.command });
return [{ json: { ...j, reply_text: text, answer_text: text } }];
