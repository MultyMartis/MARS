/**
 * Unified Reply Profile Resolver v1.0
 * reply_profile_resolver_version=iseo-reply-profile-resolver-v1.0
 *
 * Single authoritative contract for:
 * - /reply_profiles, /reply_profile, /my_reply_profile
 * - /start reply-name line
 * - Operational recipient personalization
 *
 * Fail-closed: never derive client-facing names from Telegram display/username/nickname.
 */

import {
  validateReplySenderName,
  normalizeReplyCompanyName,
  parseBoolFlag,
  getProfileNumber,
  isCardRecipient,
  roleLabelRu,
  accessLabelRu,
  introSentence,
  DEFAULT_REPLY_COMPANY_NAME,
  REPLY_PROFILE_VERSION,
  matchApprovedSeedKey,
  APPROVED_INITIAL_PROFILE_NUMBERS,
} from './reply-profile-lib.mjs';

export const REPLY_PROFILE_RESOLVER_VERSION = 'iseo-reply-profile-resolver-v1.0';

const SEED_BY_MATCH = Object.freeze(
  Object.fromEntries(
    APPROVED_INITIAL_PROFILE_NUMBERS.map((p) => [
      p.match,
      {
        profile_number: p.profile_number,
        reply_sender_name: p.reply_sender_name,
        reply_sender_enabled: p.match === 'andrej' || p.match === 'mops',
        label: p.label,
      },
    ]),
  ),
);

/**
 * Normalize one ACCESS_CONTROL-like row into the unified resolver contract.
 * @param {object} row
 * @param {object} [opts]
 * @returns {object}
 */
export function resolveReplyProfile(row = {}, opts = {}) {
  const warnings = [];
  const stable_user_ref = String(row.telegram_user_id || row.stable_user_ref || '').trim();
  const display_name = String(row.display_name || opts.display_name || '').trim();
  const role = String(row.role || '').trim().toLowerCase();
  const access_state = String(row.status || row.access_state || '').trim().toLowerCase();
  const recipient_eligible = isCardRecipient({ role, status: access_state });

  const validation = validateReplySenderName(row.reply_sender_name);
  const company = normalizeReplyCompanyName(row.reply_company_name || DEFAULT_REPLY_COMPANY_NAME);
  const enabledFlag = parseBoolFlag(row.reply_sender_enabled, false);
  const profile_number = getProfileNumber(row);
  const hasValidName = validation.ok;
  const reply_sender_enabled = hasValidName && enabledFlag;
  const reply_sender_name = hasValidName ? validation.normalized : '';

  if (!stable_user_ref) warnings.push('missing_stable_user_ref');
  if (profile_number == null) warnings.push('missing_profile_number');
  if (!hasValidName) warnings.push(validation.reason || 'invalid_or_missing_sender_name');
  if (hasValidName && !enabledFlag) warnings.push('sender_disabled');

  // Fail-closed: never invent names from display/username.
  const profile_valid = profile_number != null && hasValidName;

  return {
    resolver_version: REPLY_PROFILE_RESOLVER_VERSION,
    profile_number,
    stable_user_ref,
    display_name: display_name || '—',
    role,
    access_state,
    recipient_eligible,
    reply_sender_name,
    reply_sender_enabled,
    reply_company_name: company,
    profile_version: String(row.reply_profile_version || REPLY_PROFILE_VERSION).trim() || REPLY_PROFILE_VERSION,
    profile_valid,
    validation_warnings: warnings,
    validation,
    recipient_reply_state: reply_sender_enabled
      ? 'ready'
      : (hasValidName ? 'blocked_sender_disabled' : 'blocked_missing_sender_name'),
    personalization_ready: reply_sender_enabled,
    intro_example: reply_sender_name ? introSentence(reply_sender_name, company) : '',
    role_label_ru: roleLabelRu(role),
    access_label_ru: accessLabelRu(access_state),
  };
}

/**
 * Approved seed values for a row identified by stable identity + existing display/role cues.
 * Used only to restore wiped profile columns onto the same telegram_user_id row.
 * Never used as a client-copy fallback when profile is invalid.
 */
export function approvedSeedForRow(row = {}) {
  const match = matchApprovedSeedKey(row.display_name)
    || matchApprovedSeedKey(row.telegram_username)
    || (
      String(row.role || '').toLowerCase() === 'admin'
      && String(row.status || '').toLowerCase() === 'active'
        ? 'andrej'
        : null
    );
  if (!match || !SEED_BY_MATCH[match]) return null;
  const seed = SEED_BY_MATCH[match];
  return {
    ...seed,
    reply_company_name: DEFAULT_REPLY_COMPANY_NAME,
    reply_profile_version: REPLY_PROFILE_VERSION,
  };
}

/**
 * If profile fields were wiped, return patch fields to restore onto the same stable identity.
 * Does not change role/status. Does not create rows.
 */
export function buildProfileRehydratePatch(row = {}, actorLabel = 'system_rehydrate') {
  const current = resolveReplyProfile(row);
  const seed = approvedSeedForRow(row);
  if (!seed) return null;
  const needsNumber = current.profile_number == null;
  const needsName = !current.reply_sender_name;
  const needsEnabled = row.reply_sender_enabled === '' || row.reply_sender_enabled == null;
  if (!needsNumber && !needsName && !needsEnabled) return null;
  const now = new Date().toISOString();
  return {
    telegram_user_id: String(row.telegram_user_id || '').trim(),
    reply_profile_number: needsNumber ? seed.profile_number : current.profile_number,
    reply_sender_name: needsName ? seed.reply_sender_name : current.reply_sender_name,
    reply_sender_enabled: needsEnabled ? seed.reply_sender_enabled : parseBoolFlag(row.reply_sender_enabled, false),
    reply_company_name: String(row.reply_company_name || '').trim() || seed.reply_company_name,
    reply_profile_version: REPLY_PROFILE_VERSION,
    reply_profile_updated_at: now,
    reply_profile_updated_by: actorLabel,
    seed_label: seed.label,
  };
}

/** Preserve reply-profile columns when projecting ACCESS_CONTROL rows (anti-wipe). */
export const REPLY_PROFILE_ACCESS_FIELDS = Object.freeze([
  'reply_profile_number',
  'reply_sender_name',
  'reply_sender_enabled',
  'reply_company_name',
  'reply_profile_version',
  'reply_profile_updated_at',
  'reply_profile_updated_by',
]);

export function pickReplyProfileFields(row = {}) {
  const out = {};
  for (const k of REPLY_PROFILE_ACCESS_FIELDS) {
    if (row[k] !== undefined) out[k] = row[k];
  }
  return out;
}

export function mergeRehydrateIntoUpsert(row = {}, actorLabel = 'system_rehydrate') {
  const base = { ...row, ...pickReplyProfileFields(row) };
  const patch = buildProfileRehydratePatch(base, actorLabel);
  if (!patch) return base;
  return {
    ...base,
    reply_profile_number: patch.reply_profile_number,
    reply_sender_name: patch.reply_sender_name,
    reply_sender_enabled: patch.reply_sender_enabled,
    reply_company_name: patch.reply_company_name,
    reply_profile_version: patch.reply_profile_version,
    reply_profile_updated_at: patch.reply_profile_updated_at,
    reply_profile_updated_by: patch.reply_profile_updated_by,
  };
}

export function formatResolvedProfileCard(resolved, opts = {}) {
  const lines = [];
  if (opts.withNumberHeader) {
    lines.push(`👤 Профиль ответа клиенту №${resolved.profile_number != null ? resolved.profile_number : '—'}`, '');
  }
  lines.push(
    `Пользователь: ${resolved.display_name || '—'}`,
    `Имя в ответе: ${resolved.reply_sender_name || '—'}`,
    `Персональный ответ: ${resolved.reply_sender_enabled ? 'включён' : 'выключен'}`,
    `Роль: ${resolved.role_label_ru}`,
    `Доступ: ${resolved.access_label_ru}`,
    `Получает карточки: ${resolved.recipient_eligible ? 'да' : 'нет'}`,
  );
  if (opts.withExample && resolved.intro_example) {
    lines.push('', 'Пример представления:', `"${resolved.intro_example}"`);
  }
  return lines.join('\n');
}

export function formatMyReplyProfile(row) {
  if (!row) return 'Профиль ответа не найден. Обратитесь к администратору.';
  const resolved = resolveReplyProfile(row);
  const lines = ['👤 Мой профиль ответа клиенту', '', formatResolvedProfileCard(resolved, { withExample: false })];
  if (resolved.intro_example) {
    lines.push('', 'Пример представления:', `"${resolved.intro_example}"`);
  }
  return lines.join('\n');
}
