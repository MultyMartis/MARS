/**
 * Reply Profile Contract v1 — approved client-facing sender names.
 * Version: recipient_personalization_version=iseo-recipient-name-v1.0
 * Never derive client-facing names from Telegram display/username/actor/role.
 */

export const RECIPIENT_PERSONALIZATION_VERSION = 'iseo-recipient-name-v1.0';
export const REPLY_PROFILE_VERSION = 'iseo-recipient-name-v1.0';
export const DEFAULT_REPLY_COMPANY_NAME = 'INTLSEO';
export const REPLY_SENDER_NAME_MAX_LEN = 32;
export const REPLY_SENDER_NAME_MIN_LEN = 2;

/** Approved initial mapping (internal display label → client-facing first name). */
export const APPROVED_INITIAL_SENDER_NAMES = Object.freeze({
  'Андрей': 'Андрей',
  'Мопс': 'Михаил',
  'Оля': 'Оля',
  'Никита': 'Никита',
});

const ROLE_LABELS = new Set([
  'admin', 'administrator', 'moderator', 'модератор', 'админ', 'администратор',
  'менеджер', 'manager', 'сотрудник', 'operator', 'оператор', 'user', 'пользователь',
]);

const COMPANY_TOKENS = new Set([
  'intlseo', 'i-seo', 'iseo', 'seo', 'компания', 'company', 'агентство',
]);

/**
 * Validate an approved client-facing first name.
 * Requires a normal human first name (letters, optional hyphen/apostrophe/space for compound given names).
 * Rejects @, URLs, phones, emoji, role labels, company names, surnames-as-full-names are NOT auto-shortened —
 * multi-token names fail unless explicitly a known compound given name form with <=2 tokens of letters.
 */
export function validateReplySenderName(raw) {
  const warnings = [];
  const name = String(raw ?? '').trim().replace(/\s+/g, ' ');
  if (!name) {
    return { ok: false, reason: 'empty', normalized: '', warnings };
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
  if (/[<>{}[\]\\|^=+#*$%~`]/.test(name)) {
    return { ok: false, reason: 'forbidden_punctuation', normalized: name, warnings };
  }
  // Allow letters (Latin/Cyrillic), hyphen, apostrophe, single internal spaces
  if (!/^[A-Za-zА-Яа-яЁё]+(?:[\-'][A-Za-zА-Яа-яЁё]+)?(?:\s[A-Za-zА-Яа-яЁё]+(?:[\-'][A-Za-zА-Яа-яЁё]+)?)?$/.test(name)) {
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
  // Full name (3+ tokens) or Surname+Given without Admin correction → reject (do not auto-shorten)
  if (tokens.length >= 3) {
    return { ok: false, reason: 'looks_like_full_name', normalized: name, warnings };
  }
  // Two-token: allow only if both look like given-name forms (short, no typical surname endings required —
  // but require Admin intent: treat 2-token as full name requiring correction unless hyphenated single token)
  if (tokens.length === 2) {
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

/**
 * Resolve recipient reply profile from an ACCESS_CONTROL-like row.
 * Never falls back to display_name / username / actor.
 */
export function resolveRecipientReplyProfile(row = {}) {
  const validation = validateReplySenderName(row.reply_sender_name);
  const company = normalizeReplyCompanyName(row.reply_company_name);
  const enabledFlag = parseBoolFlag(row.reply_sender_enabled, false);
  const hasValidName = validation.ok;
  const enabled = hasValidName && enabledFlag;
  return {
    reply_sender_name: hasValidName ? validation.normalized : '',
    reply_sender_enabled: enabled,
    reply_company_name: company,
    reply_profile_version: String(row.reply_profile_version || REPLY_PROFILE_VERSION).trim() || REPLY_PROFILE_VERSION,
    reply_profile_updated_at: String(row.reply_profile_updated_at || '').trim(),
    reply_profile_updated_by: String(row.reply_profile_updated_by || '').trim(),
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

/**
 * Build additive ACCESS_CONTROL field defaults for migration.
 */
export function replyProfileFieldDefaults() {
  return {
    reply_sender_name: '',
    reply_sender_enabled: false,
    reply_company_name: DEFAULT_REPLY_COMPANY_NAME,
    reply_profile_version: REPLY_PROFILE_VERSION,
    reply_profile_updated_at: '',
    reply_profile_updated_by: '',
  };
}

/**
 * Seed plan for approved initial names (does not restore revoked users).
 * Matching is by internal display_name only when operator-approved.
 */
export function approvedSeedPlan() {
  return [
    { internal_display_name: 'Андрей', reply_sender_name: 'Андрей', reply_sender_enabled: true },
    { internal_display_name: 'Мопс', reply_sender_name: 'Михаил', reply_sender_enabled: true },
    { internal_display_name: 'Оля', reply_sender_name: 'Оля', reply_sender_enabled: true, note: 'revoked_remain_ineligible' },
    { internal_display_name: 'Никита', reply_sender_name: 'Никита', reply_sender_enabled: true, note: 'revoked_remain_ineligible' },
  ];
}

export function formatReplyProfileCard(row, opts = {}) {
  const profile = resolveRecipientReplyProfile(row);
  const display = String(row.display_name || opts.internal_display_name || '—').trim() || '—';
  const role = String(row.role || '').trim().toLowerCase();
  const status = String(row.status || '').trim().toLowerCase();
  const roleRu = role === 'admin' ? 'Админ' : (role === 'moderator' ? 'Модератор' : (role || '—'));
  const statusRu = status === 'active' ? 'Активен'
    : (status === 'revoked' ? 'Отозван'
      : (status === 'pending' ? 'Ожидает' : (status || '—')));
  const eligible = role === 'admin' || role === 'moderator'
    ? (status === 'active' ? 'да' : 'нет (не активен)')
    : 'нет';
  const lines = [
    `Пользователь: ${display}`,
    `Имя для клиента: ${profile.reply_sender_name || '—'}`,
    `Персональный ответ: ${profile.reply_sender_enabled ? 'включён' : 'выключен'}`,
    `Роль: ${roleRu}`,
    `Статус доступа: ${statusRu}`,
    `Получатель карточек: ${eligible}`,
  ];
  if (!profile.validation.ok && String(row.reply_sender_name || '').trim()) {
    lines.push(`Проверка имени: отклонено (${profile.validation.reason})`);
  }
  return lines.join('\n');
}
