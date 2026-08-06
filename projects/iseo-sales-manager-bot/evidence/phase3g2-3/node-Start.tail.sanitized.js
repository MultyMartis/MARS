const j = $input.first().json;
try {
  const role = j.auth_role === 'admin' ? 'admin'
    : (j.auth_role === 'moderator' ? 'moderator'
    : (j.auth_role === 'blocked' ? 'blocked' : 'public'));
  let replyName = '';
  try {
    // Phase 3G.2.3 — read-after-rehydrate: prefer Check User Authorization access_upsert
    // (post-rehydrate unified profile) over the pre-rehydrate Read ACCESS_CONTROL snapshot.
    // Proven defect: same-execution Start used blank sheet while access_upsert already had Михаил.
    let row = (j.access_upsert && typeof j.access_upsert === 'object') ? j.access_upsert : null;
    if (!row || !String(row.reply_sender_name || '').trim()) {
      const rows = $('Read ACCESS_CONTROL').all().map((i) => i.json || {});
      const uid = String(j.user_id || '');
      const sheetRow = rows.find((r) => String(r.telegram_user_id || '') === uid) || null;
      if (sheetRow) row = row ? Object.assign({}, sheetRow, row) : sheetRow;
    }
    // Unified resolver contract (iseo-reply-profile-resolver-v1.0): reply_sender_name only.
    // Fail-closed: never display_name / username / nickname fallback.
    replyName = row ? String(row.reply_sender_name || '').trim() : '';
  } catch (e) { replyName = ''; }
  const text = startReply(role, j.config_map || {}, { reply_sender_name: replyName, reply_profile_resolver_version: 'iseo-reply-profile-resolver-v1.0' });
  if (!text || !String(text).trim()) {
    return [{ json: Object.assign({}, j, {
      reply_text: "Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.",
      parse_mode: 'HTML',
      command_response_guard: 'empty_builder',
      deny_reason: 'processing_failure',
      error_node: 'Start',
    }) }];
  }
  // length guard (Telegram hard limit 4096)
  if (String(text).length > 4096) {
    return [{ json: Object.assign({}, j, {
      reply_text: "Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.",
      parse_mode: 'HTML',
      command_response_guard: 'length_overflow',
      deny_reason: 'processing_failure',
      error_node: 'Start',
    }) }];
  }
  return [{ json: Object.assign({}, j, { reply_text: text, parse_mode: 'HTML' }) }];
} catch (e) {
  return [{ json: Object.assign({}, j, {
    reply_text: "Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.",
    parse_mode: 'HTML',
    command_response_guard: 'runtime_exception',
    deny_reason: 'processing_failure',
    error_node: 'Start',
  }) }];
}
