/**
 * Reply profile Admin commands — pure helpers for Help / Route integration.
 * Admin-only mutations. Moderators may view only /my_reply_profile.
 */

import {
  validateReplySenderName,
  resolveRecipientReplyProfile,
  formatReplyProfileCard,
  DEFAULT_REPLY_COMPANY_NAME,
  REPLY_PROFILE_VERSION,
  parseBoolFlag,
} from './reply-profile-lib.mjs';

export const REPLY_PROFILE_COMMANDS = Object.freeze({
  LIST: '/reply_profiles',
  GET: '/reply_profile',
  SET: '/reply_name_set',
  ENABLE: '/reply_name_enable',
  DISABLE: '/reply_name_disable',
  MY: '/my_reply_profile',
});

export function isReplyProfileCommand(cmd) {
  return Object.values(REPLY_PROFILE_COMMANDS).includes(String(cmd || '').trim());
}

export function isReplyProfileMutation(cmd) {
  const c = String(cmd || '').trim();
  return c === REPLY_PROFILE_COMMANDS.SET
    || c === REPLY_PROFILE_COMMANDS.ENABLE
    || c === REPLY_PROFILE_COMMANDS.DISABLE;
}

function normName(s) {
  return String(s || '').trim().toLowerCase().replace(/^@/, '');
}

/**
 * Resolve ACCESS_CONTROL row by display_name or username (never require raw chat IDs).
 */
export function resolveAccessRowByUserToken(rows, token) {
  const t = normName(token);
  if (!t) return null;
  const list = Array.isArray(rows) ? rows : [];
  const exact = list.find((r) => normName(r.display_name) === t || normName(r.telegram_username) === t);
  if (exact) return exact;
  const partial = list.filter((r) => normName(r.display_name).includes(t) || normName(r.telegram_username).includes(t));
  if (partial.length === 1) return partial[0];
  return null;
}

export function listReplyProfiles(rows) {
  const list = (Array.isArray(rows) ? rows : [])
    .filter((r) => {
      const role = String(r.role || '').toLowerCase();
      return role === 'admin' || role === 'moderator';
    })
    .sort((a, b) => String(a.display_name || '').localeCompare(String(b.display_name || ''), 'ru'));
  if (!list.length) return 'Профили ответа: записей не найдено.';
  const lines = ['Профили ответа клиенту', ''];
  for (const r of list) {
    const p = resolveRecipientReplyProfile(r);
    const st = String(r.status || '').toLowerCase() === 'active' ? 'активен' : String(r.status || '—');
    lines.push(`• ${r.display_name || '—'}: ${p.reply_sender_name || '—'} · ${p.reply_sender_enabled ? 'вкл' : 'выкл'} · доступ: ${st}`);
  }
  return lines.join('\n');
}

export function handleMyReplyProfile(actorRow) {
  if (!actorRow) return 'Профиль ответа не найден. Обратитесь к администратору.';
  return formatReplyProfileCard(actorRow);
}

export function handleReplyProfileGet(rows, userToken) {
  const row = resolveAccessRowByUserToken(rows, userToken);
  if (!row) return 'Пользователь не найден. Укажите имя из списка доступа.';
  return formatReplyProfileCard(row);
}

export function buildReplyNameSetPatch(rows, userToken, nameRaw, actorLabel = 'admin') {
  const row = resolveAccessRowByUserToken(rows, userToken);
  if (!row) return { ok: false, reply: 'Пользователь не найден. Укажите имя из списка доступа.' };
  const v = validateReplySenderName(nameRaw);
  if (!v.ok) {
    return {
      ok: false,
      reply: `Имя отклонено (${v.reason}). Укажите обычное имя без фамилии, @, ссылок и эмодзи.`,
    };
  }
  const now = new Date().toISOString();
  return {
    ok: true,
    reply: [
      'Имя для клиента обновлено.',
      formatReplyProfileCard({
        ...row,
        reply_sender_name: v.normalized,
        reply_sender_enabled: true,
        reply_company_name: row.reply_company_name || DEFAULT_REPLY_COMPANY_NAME,
        reply_profile_version: REPLY_PROFILE_VERSION,
        reply_profile_updated_at: now,
        reply_profile_updated_by: actorLabel,
      }),
    ].join('\n\n'),
    patch: {
      telegram_user_id: row.telegram_user_id,
      reply_sender_name: v.normalized,
      reply_sender_enabled: true,
      reply_company_name: row.reply_company_name || DEFAULT_REPLY_COMPANY_NAME,
      reply_profile_version: REPLY_PROFILE_VERSION,
      reply_profile_updated_at: now,
      reply_profile_updated_by: actorLabel,
    },
  };
}

export function buildReplyNameEnablePatch(rows, userToken, enabled, actorLabel = 'admin') {
  const row = resolveAccessRowByUserToken(rows, userToken);
  if (!row) return { ok: false, reply: 'Пользователь не найден. Укажите имя из списка доступа.' };
  const profile = resolveRecipientReplyProfile(row);
  if (enabled && !profile.validation.ok) {
    return { ok: false, reply: 'Сначала задайте корректное имя: /reply_name_set <пользователь> <имя>' };
  }
  const now = new Date().toISOString();
  return {
    ok: true,
    reply: formatReplyProfileCard({
      ...row,
      reply_sender_enabled: enabled,
      reply_profile_updated_at: now,
      reply_profile_updated_by: actorLabel,
    }),
    patch: {
      telegram_user_id: row.telegram_user_id,
      reply_sender_enabled: enabled,
      reply_profile_version: REPLY_PROFILE_VERSION,
      reply_profile_updated_at: now,
      reply_profile_updated_by: actorLabel,
    },
  };
}

export function helpLinesForRole(role) {
  const r = String(role || '').toLowerCase();
  if (r === 'admin') {
    return [
      '/reply_profiles — профили имён для ответа клиенту',
      '/reply_profile <пользователь> — профиль ответа',
      '/reply_name_set <пользователь> <имя> — задать имя для клиента',
      '/reply_name_enable <пользователь> — включить персональный ответ',
      '/reply_name_disable <пользователь> — выключить персональный ответ',
      '/my_reply_profile — мой профиль ответа',
    ];
  }
  if (r === 'moderator') {
    return [
      '/my_reply_profile — мой профиль ответа клиенту',
    ];
  }
  return [];
}

export function denyModeratorMutation() {
  return 'Изменение имени для ответа доступно только администратору.';
}

export { parseBoolFlag, formatReplyProfileCard, resolveRecipientReplyProfile, validateReplySenderName };
