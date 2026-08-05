/**
 * Reply profile Admin commands v2 — stable profile numbers.
 * Admin-only mutations. Moderators may view only /my_reply_profile.
 */

import {
  validateReplySenderName,
  resolveRecipientReplyProfile,
  formatReplyProfileCard,
  DEFAULT_REPLY_COMPANY_NAME,
  REPLY_PROFILE_VERSION,
  REPLY_PROFILES_PAGE_SIZE,
  parseBoolFlag,
  parseProfileNumber,
  getProfileNumber,
  isCardRecipient,
  introSentence,
  roleLabelRu,
  accessLabelRu,
  nameValidationErrorText,
  adminOnlyCommandText,
} from './reply-profile-lib.mjs';
import {
  REPLY_PROFILE_RESOLVER_VERSION,
  resolveReplyProfile,
  formatMyReplyProfile,
  buildProfileRehydratePatch,
  mergeRehydrateIntoUpsert,
} from './reply-profile-resolver-v1.mjs';

export {
  REPLY_PROFILE_RESOLVER_VERSION,
  resolveReplyProfile,
  buildProfileRehydratePatch,
  mergeRehydrateIntoUpsert,
};

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

function profileRows(rows) {
  return (Array.isArray(rows) ? rows : [])
    .filter((r) => {
      const role = String(r.role || '').toLowerCase();
      return role === 'admin' || role === 'moderator';
    })
    .slice()
    .sort((a, b) => {
      const na = getProfileNumber(a) ?? Number.MAX_SAFE_INTEGER;
      const nb = getProfileNumber(b) ?? Number.MAX_SAFE_INTEGER;
      if (na !== nb) return na - nb;
      return String(a.display_name || '').localeCompare(String(b.display_name || ''), 'ru');
    });
}

export function resolveAccessRowByProfileNumber(rows, numberRaw) {
  const parsed = parseProfileNumber(numberRaw);
  if (!parsed.ok) return { ok: false, reason: parsed.reason, row: null, number: null };
  const list = profileRows(rows).filter((r) => getProfileNumber(r) === parsed.value);
  if (list.length === 0) return { ok: false, reason: 'not_found', row: null, number: parsed.value };
  if (list.length > 1) return { ok: false, reason: 'duplicate', row: null, number: parsed.value };
  return { ok: true, reason: 'ok', row: list[0], number: parsed.value };
}

/** @deprecated Prefer resolveAccessRowByProfileNumber for Admin mutations. */
export function resolveAccessRowByUserToken(rows, token) {
  const t = String(token || '').trim().toLowerCase().replace(/^@/, '');
  if (!t) return null;
  const list = Array.isArray(rows) ? rows : [];
  const exact = list.find((r) =>
    String(r.display_name || '').trim().toLowerCase() === t
    || String(r.telegram_username || '').trim().toLowerCase().replace(/^@/, '') === t
  );
  if (exact) return exact;
  const partial = list.filter((r) =>
    String(r.display_name || '').toLowerCase().includes(t)
    || String(r.telegram_username || '').toLowerCase().includes(t)
  );
  if (partial.length === 1) return partial[0];
  return null;
}

function listBlock(row) {
  const p = resolveRecipientReplyProfile(row);
  const n = p.reply_profile_number;
  const head = n != null ? `${n}. ${row.display_name || '—'}` : `—. ${row.display_name || '—'}`;
  return [
    head,
    `Имя в ответе: ${p.reply_sender_name || '—'}`,
    `Персональный ответ: ${p.reply_sender_enabled ? 'включён' : 'выключен'}`,
    `Роль: ${roleLabelRu(row.role)}`,
    `Доступ: ${accessLabelRu(row.status)}`,
    `Получает карточки: ${isCardRecipient(row) ? 'да' : 'нет'}`,
  ].join('\n');
}

export function listReplyProfiles(rows, page = 1, pageSize = REPLY_PROFILES_PAGE_SIZE) {
  const list = profileRows(rows);
  if (!list.length) {
    return { text: '👤 Профили ответов клиентам\n\nЗаписей не найдено.', page: 1, pages: 1, total: 0 };
  }
  const size = Math.max(1, Number(pageSize) || REPLY_PROFILES_PAGE_SIZE);
  const pages = Math.max(1, Math.ceil(list.length / size));
  const p = Math.min(Math.max(1, Number(page) || 1), pages);
  const slice = list.slice((p - 1) * size, p * size);
  const lines = ['👤 Профили ответов клиентам', ''];
  for (const r of slice) {
    lines.push(listBlock(r), '');
  }
  if (pages > 1) {
    lines.push(`Страница ${p} из ${pages}. Следующая: /reply_profiles ${p + 1 <= pages ? p + 1 : p}`);
  }
  return { text: lines.join('\n').trim(), page: p, pages, total: list.length };
}

export function handleMyReplyProfile(actorRow) {
  return formatMyReplyProfile(actorRow);
}

export function handleReplyProfileGet(rows, numberRaw) {
  if (numberRaw == null || String(numberRaw).trim() === '') {
    return {
      ok: false,
      reply: ['Укажите номер профиля.', '', 'Пример:', '/reply_profile 3'].join('\n'),
    };
  }
  const parsed = parseProfileNumber(numberRaw);
  if (!parsed.ok) {
    return { ok: false, reply: 'Номер профиля должен быть целым положительным числом.' };
  }
  const found = resolveAccessRowByProfileNumber(rows, parsed.value);
  if (!found.ok) {
    return {
      ok: false,
      reply: 'Профиль с таким номером не найден. Посмотрите доступные номера командой /reply_profiles.',
    };
  }
  return {
    ok: true,
    reply: formatReplyProfileCard(found.row, { withNumberHeader: true, withExample: true }),
  };
}

function bumpVersion(row) {
  const raw = String(row.reply_profile_version || REPLY_PROFILE_VERSION).trim();
  const m = raw.match(/^(.*?)(\d+)\s*$/);
  if (!m) return REPLY_PROFILE_VERSION;
  // keep contract family; stamp update time separately — version field stays contract id + optional counter
  return REPLY_PROFILE_VERSION;
}

export function buildReplyNameSetPatch(rows, numberRaw, nameRaw, actorLabel = 'admin') {
  if (numberRaw == null || String(numberRaw).trim() === '' || nameRaw == null || String(nameRaw).trim() === '') {
    return {
      ok: false,
      reply: ['Укажите номер профиля и имя.', '', 'Пример:', '/reply_name_set 3 Михаил'].join('\n'),
    };
  }
  const parsed = parseProfileNumber(numberRaw);
  if (!parsed.ok) return { ok: false, reply: 'Номер профиля должен быть целым положительным числом.' };
  const found = resolveAccessRowByProfileNumber(rows, parsed.value);
  if (!found.ok) {
    return {
      ok: false,
      reply: 'Профиль с таким номером не найден. Посмотрите доступные номера командой /reply_profiles.',
    };
  }
  const v = validateReplySenderName(nameRaw);
  if (!v.ok) return { ok: false, reply: nameValidationErrorText(parsed.value) };

  const row = found.row;
  const prevEnabled = parseBoolFlag(row.reply_sender_enabled, false);
  const prevName = String(row.reply_sender_name || '').trim();
  const now = new Date().toISOString();
  // Update name only — do not auto-enable; do not restore access.
  const updated = {
    ...row,
    reply_sender_name: v.normalized,
    reply_sender_enabled: prevEnabled,
    reply_company_name: row.reply_company_name || DEFAULT_REPLY_COMPANY_NAME,
    reply_profile_version: bumpVersion(row),
    reply_profile_updated_at: now,
    reply_profile_updated_by: actorLabel,
  };
  const status = String(row.status || '').toLowerCase();
  const lines = [
    'Имя для ответа клиенту обновлено.',
    '',
    `Пользователь: ${row.display_name || '—'}`,
    `Имя в ответе: ${v.normalized}`,
    `Персональный ответ: ${prevEnabled ? 'включён' : 'выключен'}`,
    `Доступ: ${accessLabelRu(row.status)}`,
  ];
  if (status === 'active' && prevEnabled) {
    lines.push('', 'В новых черновиках будет использоваться:', `"${introSentence(v.normalized, updated.reply_company_name)}"`);
  } else if (status !== 'active') {
    lines.push('', 'Имя сохранено, но пользователь не получает карточки.');
  } else {
    lines.push('', 'Имя сохранено. Чтобы использовать его в карточках, включите персональный ответ командой /reply_name_enable.');
  }
  return {
    ok: true,
    reply: lines.join('\n'),
    patch: {
      telegram_user_id: row.telegram_user_id,
      reply_profile_number: getProfileNumber(row),
      reply_sender_name: v.normalized,
      reply_sender_enabled: prevEnabled,
      reply_company_name: updated.reply_company_name,
      reply_profile_version: updated.reply_profile_version,
      reply_profile_updated_at: now,
      reply_profile_updated_by: actorLabel,
    },
    event: {
      action: 'reply_name_set',
      profile_number: getProfileNumber(row),
      previous_name: prevName,
      new_name: v.normalized,
      previous_enabled: prevEnabled,
      new_enabled: prevEnabled,
      profile_version: updated.reply_profile_version,
    },
  };
}

export function buildReplyNameEnablePatch(rows, numberRaw, enabled, actorLabel = 'admin') {
  const parsed = parseProfileNumber(numberRaw);
  if (!parsed.ok) {
    if (numberRaw == null || String(numberRaw).trim() === '') {
      return { ok: false, reply: ['Укажите номер профиля.', '', 'Пример:', `/reply_name_${enabled ? 'enable' : 'disable'} 3`].join('\n') };
    }
    return { ok: false, reply: 'Номер профиля должен быть целым положительным числом.' };
  }
  const found = resolveAccessRowByProfileNumber(rows, parsed.value);
  if (!found.ok) {
    return {
      ok: false,
      reply: 'Профиль с таким номером не найден. Посмотрите доступные номера командой /reply_profiles.',
    };
  }
  const row = found.row;
  const profile = resolveRecipientReplyProfile(row);
  const prevEnabled = parseBoolFlag(row.reply_sender_enabled, false);
  const now = new Date().toISOString();

  if (enabled) {
    if (!profile.validation.ok || !String(row.reply_sender_name || '').trim()) {
      return {
        ok: false,
        reply: 'Нельзя включить персональные ответы: сначала задайте имя командой /reply_name_set.',
      };
    }
    if (!isCardRecipient(row)) {
      return {
        ok: false,
        reply: [
          'Нельзя включить персональные ответы: доступ пользователя отозван.',
          '',
          'Имя сохранено и будет доступно после восстановления доступа.',
        ].join('\n'),
      };
    }
    const updated = {
      ...row,
      reply_sender_enabled: true,
      reply_profile_version: bumpVersion(row),
      reply_profile_updated_at: now,
      reply_profile_updated_by: actorLabel,
    };
    return {
      ok: true,
      reply: [
        'Персональные ответы включены.',
        '',
        `Пользователь: ${row.display_name || '—'}`,
        `Имя в ответе: ${profile.reply_sender_name}`,
      ].join('\n'),
      patch: {
        telegram_user_id: row.telegram_user_id,
        reply_profile_number: getProfileNumber(row),
        reply_sender_enabled: true,
        reply_profile_version: updated.reply_profile_version,
        reply_profile_updated_at: now,
        reply_profile_updated_by: actorLabel,
      },
      event: {
        action: 'reply_name_enabled',
        profile_number: getProfileNumber(row),
        previous_name: profile.reply_sender_name,
        new_name: profile.reply_sender_name,
        previous_enabled: prevEnabled,
        new_enabled: true,
        profile_version: updated.reply_profile_version,
      },
    };
  }

  const updated = {
    ...row,
    reply_sender_enabled: false,
    reply_profile_version: bumpVersion(row),
    reply_profile_updated_at: now,
    reply_profile_updated_by: actorLabel,
  };
  return {
    ok: true,
    reply: [
      'Персональные ответы выключены.',
      '',
      `Пользователь: ${row.display_name || '—'}`,
      'Новые карточки будут приходить без готового клиентского текста, пока профиль не будет включён снова.',
    ].join('\n'),
    patch: {
      telegram_user_id: row.telegram_user_id,
      reply_profile_number: getProfileNumber(row),
      reply_sender_enabled: false,
      reply_profile_version: updated.reply_profile_version,
      reply_profile_updated_at: now,
      reply_profile_updated_by: actorLabel,
    },
    event: {
      action: 'reply_name_disabled',
      profile_number: getProfileNumber(row),
      previous_name: String(row.reply_sender_name || '').trim(),
      new_name: String(row.reply_sender_name || '').trim(),
      previous_enabled: prevEnabled,
      new_enabled: false,
      profile_version: updated.reply_profile_version,
    },
  };
}

export function helpLinesForRole(role) {
  const r = String(role || '').toLowerCase();
  if (r === 'admin') {
    return [
      '/reply_profiles — профили ответов клиентам',
      '/reply_profile <номер> — профиль ответа по номеру',
      '/reply_name_set <номер> <имя> — задать имя для клиента',
      '/reply_name_enable <номер> — включить персональный ответ',
      '/reply_name_disable <номер> — выключить персональный ответ',
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
  return adminOnlyCommandText();
}

export {
  parseBoolFlag,
  formatReplyProfileCard,
  resolveRecipientReplyProfile,
  validateReplySenderName,
  parseProfileNumber,
  getProfileNumber,
  adminOnlyCommandText,
};
