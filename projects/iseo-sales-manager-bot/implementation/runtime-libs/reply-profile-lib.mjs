/**
 * Reply Profile Contract v1.1 — numbered profiles + approved client-facing names.
 * Version: recipient_personalization_version=iseo-recipient-name-v1.1
 * Never derive client-facing names from Telegram display/username/actor/role.
 * reply_profile_number is immutable after assignment; independent of row order / Telegram ID.
 */

export const RECIPIENT_PERSONALIZATION_VERSION = 'iseo-recipient-name-v1.1';
export const REPLY_PROFILE_VERSION = 'iseo-recipient-name-v1.1';
/** Alias kept for Operational / Admin dual embedding; authoritative resolver id. */
export const REPLY_PROFILE_RESOLVER_VERSION = 'iseo-reply-profile-resolver-v1.0';
export const DEFAULT_REPLY_COMPANY_NAME = 'INTLSEO';
export const REPLY_SENDER_NAME_MAX_LEN = 32;
export const REPLY_SENDER_NAME_MIN_LEN = 2;
export const REPLY_PROFILES_PAGE_SIZE = 10;

/** Approved initial mapping (internal display label → client-facing first name). */
export const APPROVED_INITIAL_SENDER_NAMES = Object.freeze({
  'Андрей': 'Андрей',
  'Мопс': 'Михаил',
  'Оля': 'Оля',
  'Никита': 'Никита',
});

/** Stable initial profile numbers — never renumber. */
export const APPROVED_INITIAL_PROFILE_NUMBERS = Object.freeze([
  { profile_number: 1, match: 'andrej', reply_sender_name: 'Андрей', label: 'ADMIN_A' },
  { profile_number: 2, match: 'ola', reply_sender_name: 'Оля', label: 'MOD_B_REVOKED' },
  { profile_number: 3, match: 'mops', reply_sender_name: 'Михаил', label: 'MOD_A' },
  { profile_number: 4, match: 'nikita', reply_sender_name: 'Никита', label: 'MOD_C_REVOKED' },
]);

const ROLE_LABELS = new Set([
  'admin', 'administrator', 'moderator', 'модератор', 'админ', 'администратор',
  'менеджер', 'manager', 'сотрудник', 'operator', 'оператор', 'user', 'пользователь',
]);

const COMPANY_TOKENS = new Set([
  'intlseo', 'i-seo', 'iseo', 'seo', 'компания', 'company', 'агентство',
]);

export function roleLabelRu(role) {
  const r = String(role || '').trim().toLowerCase();
  if (r === 'admin') return 'Администратор';
  if (r === 'moderator') return 'Модератор';
  if (r === 'public') return 'Публичный';
  if (r === 'blocked') return 'Заблокирован';
  return r ? String(role) : '—';
}

export function statusLabelRu(status) {
  const s = String(status || '').trim().toLowerCase();
  if (s === 'active') return 'Активен';
  if (s === 'revoked') return 'Отозван';
  if (s === 'pending') return 'Ожидает';
  if (s === 'blocked') return 'Заблокирован';
  return s ? String(status) : '—';
}

export function accessLabelRu(status) {
  const s = String(status || '').trim().toLowerCase();
  if (s === 'active') return 'Активен';
  if (s === 'revoked') return 'Доступ отозван';
  if (s === 'pending') return 'Ожидает';
  if (s === 'blocked') return 'Заблокирован';
  return s ? String(status) : '—';
}

export function parseProfileNumber(raw) {
  const s = String(raw ?? '').trim();
  if (!/^\d+$/.test(s)) return { ok: false, reason: 'not_integer', value: null };
  const n = Number(s);
  if (!Number.isInteger(n) || n < 1) return { ok: false, reason: 'not_positive', value: null };
  return { ok: true, reason: 'ok', value: n };
}

export function getProfileNumber(row = {}) {
  const raw = row.reply_profile_number ?? row.profile_number;
  const parsed = parseProfileNumber(raw);
  return parsed.ok ? parsed.value : null;
}

export function matchApprovedSeedKey(displayName) {
  const s = String(displayName || '').trim();
  if (/андрей/i.test(s)) return 'andrej';
  if (s === 'Мопс' || /^мопс$/i.test(s)) return 'mops';
  if (/ola4seo/i.test(s) || s === 'Оля' || /^оля$/i.test(s)) return 'ola';
  if (/никита/i.test(s)) return 'nikita';
  return null;
}

/**
 * Validate an approved client-facing first name.
 * One token only. Rejects @, URLs, phones, emoji, role labels, company names, multi-token full names.
 */
export function validateReplySenderName(raw) {
  const warnings = [];
  const name = String(raw ?? '').trim().replace(/\s+/g, ' ');
  if (!name) {
    return { ok: false, reason: 'empty', normalized: '', warnings };
  }
  if (/\r|\n/.test(String(raw ?? ''))) {
    return { ok: false, reason: 'line_break', normalized: name, warnings };
  }
  if (name.length < REPLY_SENDER_NAME_MIN_LEN) {
    return { ok: false, reason: 'too_short', normalized: name, warnings };
  }
  if (name.length > REPLY_SENDER_NAME_MAX_LEN) {
    return { ok: false, reason: 'too_long', normalized: name, warnings };
  }
  if (/@/.test(name)) {
    return { ok: false, reason: 'contains_at', normalized: name, warnings };
  }
  if (/https?:|www\.|\.ru\/|\.com\/|t\.me\//i.test(name)) {
    return { ok: false, reason: 'contains_url', normalized: name, warnings };
  }
  if (/\d{3,}/.test(name) || /\+?\d[\d\s\-()]{6,}/.test(name)) {
    return { ok: false, reason: 'contains_phone_or_digits', normalized: name, warnings };
  }
  if (/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(name)) {
    return { ok: false, reason: 'contains_emoji', normalized: name, warnings };
  }
  if (/[<>{}[\]\\|^=+#*$%~`.,;:!?]/.test(name)) {
    return { ok: false, reason: 'forbidden_punctuation', normalized: name, warnings };
  }
  if (!/^[A-Za-zА-Яа-яЁё]+(?:[\-'][A-Za-zА-Яа-яЁё]+)?$/.test(name)) {
    return { ok: false, reason: 'invalid_charset', normalized: name, warnings };
  }
  const lower = name.toLowerCase();
  if (ROLE_LABELS.has(lower)) {
    return { ok: false, reason: 'role_label', normalized: name, warnings };
  }
  if (COMPANY_TOKENS.has(lower.replace(/\s+/g, ''))) {
    return { ok: false, reason: 'company_name', normalized: name, warnings };
  }
  const tokens = name.split(/\s+/);
  if (tokens.length >= 2) {
    return { ok: false, reason: 'looks_like_full_name', normalized: name, warnings };
  }
  return { ok: true, reason: 'ok', normalized: name, warnings };
}

export function normalizeReplyCompanyName(raw) {
  const c = String(raw ?? '').trim();
  return c || DEFAULT_REPLY_COMPANY_NAME;
}

export function parseBoolFlag(v, defaultValue = false) {
  if (v === true || v === 'true' || v === '1' || v === 1) return true;
  if (v === false || v === 'false' || v === '0' || v === 0) return false;
  return defaultValue;
}

export function isCardRecipient(row = {}) {
  const role = String(row.role || '').trim().toLowerCase();
  const status = String(row.status || '').trim().toLowerCase();
  return (role === 'admin' || role === 'moderator') && status === 'active';
}

/**
 * Resolve recipient reply profile from an ACCESS_CONTROL-like row.
 * Never falls back to display_name / username / actor.
 * Field contract aligned with iseo-reply-profile-resolver-v1.0.
 */
export function resolveRecipientReplyProfile(row = {}) {
  const validation = validateReplySenderName(row.reply_sender_name);
  const company = normalizeReplyCompanyName(row.reply_company_name);
  const enabledFlag = parseBoolFlag(row.reply_sender_enabled, false);
  const hasValidName = validation.ok;
  const enabled = hasValidName && enabledFlag;
  const profile_number = getProfileNumber(row);
  const warnings = [];
  if (profile_number == null) warnings.push('missing_profile_number');
  if (!hasValidName) warnings.push(validation.reason || 'invalid_or_missing_sender_name');
  if (hasValidName && !enabledFlag) warnings.push('sender_disabled');
  return {
    resolver_version: REPLY_PROFILE_RESOLVER_VERSION,
    profile_number,
    reply_profile_number: profile_number,
    stable_user_ref: String(row.telegram_user_id || '').trim(),
    display_name: String(row.display_name || '').trim(),
    role: String(row.role || '').trim().toLowerCase(),
    access_state: String(row.status || '').trim().toLowerCase(),
    recipient_eligible: isCardRecipient(row),
    reply_sender_name: hasValidName ? validation.normalized : '',
    reply_sender_enabled: enabled,
    reply_company_name: company,
    profile_version: String(row.reply_profile_version || REPLY_PROFILE_VERSION).trim() || REPLY_PROFILE_VERSION,
    reply_profile_version: String(row.reply_profile_version || REPLY_PROFILE_VERSION).trim() || REPLY_PROFILE_VERSION,
    reply_profile_updated_at: String(row.reply_profile_updated_at || '').trim(),
    reply_profile_updated_by: String(row.reply_profile_updated_by || '').trim(),
    profile_valid: profile_number != null && hasValidName,
    validation_warnings: warnings,
    validation,
    recipient_reply_state: enabled
      ? 'ready'
      : (hasValidName ? 'blocked_sender_disabled' : 'blocked_missing_sender_name'),
    personalization_ready: enabled,
  };
}

export function introSentence(senderName, companyName = DEFAULT_REPLY_COMPANY_NAME) {
  const name = String(senderName || '').trim();
  const company = normalizeReplyCompanyName(companyName);
  return `Меня зовут ${name}, компания ${company}.`;
}

export function missingSenderNameWarning() {
  return '⚠️ Не задано имя для ответа клиенту. Обратитесь к администратору.';
}

export function replyProfileFieldDefaults() {
  return {
    reply_profile_number: '',
    reply_sender_name: '',
    reply_sender_enabled: false,
    reply_company_name: DEFAULT_REPLY_COMPANY_NAME,
    reply_profile_version: REPLY_PROFILE_VERSION,
    reply_profile_updated_at: '',
    reply_profile_updated_by: '',
  };
}

export function approvedSeedPlan() {
  return APPROVED_INITIAL_PROFILE_NUMBERS.map((p) => ({
    profile_number: p.profile_number,
    match: p.match,
    label: p.label,
    reply_sender_name: p.reply_sender_name,
    reply_sender_enabled: p.match === 'andrej' || p.match === 'mops',
    note: (p.match === 'ola' || p.match === 'nikita') ? 'revoked_remain_ineligible' : undefined,
  }));
}

export function nextProfileNumber(rows) {
  let max = 0;
  for (const r of (Array.isArray(rows) ? rows : [])) {
    const n = getProfileNumber(r);
    if (n != null && n > max) max = n;
  }
  return max + 1;
}

export function formatReplyProfileCard(row, opts = {}) {
  const profile = resolveRecipientReplyProfile(row);
  const display = String(row.display_name || opts.internal_display_name || '—').trim() || '—';
  const num = profile.reply_profile_number;
  const lines = [];
  if (opts.withNumberHeader && num != null) {
    lines.push(`👤 Профиль ответа клиенту №${num}`, '');
  }
  lines.push(
    `Пользователь: ${display}`,
    `Имя в ответе: ${profile.reply_sender_name || '—'}`,
    `Персональный ответ: ${profile.reply_sender_enabled ? 'включён' : 'выключен'}`,
    `Роль: ${roleLabelRu(row.role)}`,
    `Доступ: ${accessLabelRu(row.status)}`,
    `Получает карточки: ${isCardRecipient(row) ? 'да' : 'нет'}`,
  );
  if (opts.withExample && profile.reply_sender_name) {
    lines.push('', 'Пример представления:', `"${introSentence(profile.reply_sender_name, profile.reply_company_name)}"`);
  }
  if (!profile.validation.ok && String(row.reply_sender_name || '').trim()) {
    lines.push('Проверка имени: отклонено');
  }
  return lines.join('\n');
}

export function nameValidationErrorText(exampleNumber = 3) {
  return [
    'Укажите только имя, которое будет использоваться в сообщениях клиенту.',
    '',
    'Пример:',
    `/reply_name_set ${exampleNumber} Михаил`,
  ].join('\n');
}

export function adminOnlyCommandText() {
  return 'Эта команда доступна только администратору.';
}
