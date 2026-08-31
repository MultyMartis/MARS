// Phase 3G.2.1 — Capture Admin Reply + no-silent recognized-command guard
const FALLBACK = "Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.";
const out = [];
for (const item of $input.all()) {
  const j = item.json || {};
  const nowIso = new Date().toISOString();
  let reply_text = j.reply_text;
  let guard = j.command_response_guard || '';
  if (j.command && (!reply_text || !String(reply_text).trim())) {
    reply_text = FALLBACK;
    guard = guard || 'empty_at_capture';
  }
  if (reply_text && /<(?!/?\s*(b|strong|i|em|u|s|code|pre|a)\b)[^>]+>/i.test(String(reply_text))) {
    // allow only known tags; otherwise do not block — cmdHtml already escapes. No-op.
  }
  const failed = Boolean(
    j.deny_reason === 'processing_failure' ||
    (j.callback_outcome === 'error' && !reply_text) ||
    guard === 'runtime_exception' ||
    guard === 'empty_builder' ||
    guard === 'empty_at_capture' ||
    guard === 'length_overflow'
  );
  // CARD_EDIT_SUPPRESS_REPLY — skip visible chat send when in-place card edit already delivered content
  if (j.suppress_visible_reply === true && !String(reply_text || '').trim()) continue;
  out.push({
    json: Object.assign({}, j, {
      reply_text,
      admin_reply_captured: true,
      reply_len: String(reply_text || '').length,
      command_response_guard_applied: guard || false,
      last_admin_command_success_at: failed ? j.last_admin_command_success_at : nowIso,
      last_admin_command_error_at: failed ? nowIso : j.last_admin_command_error_at,
      last_admin_command_error_code: failed
        ? String(j.deny_reason || j.callback_outcome || guard || 'processing_failure')
        : j.last_admin_command_error_code,
      last_admin_command_error_node: failed
        ? String(j.error_node || 'Capture Admin Reply')
        : j.last_admin_command_error_node,
    }),
  });
}
return out;
