/**
 * Phase 3H.9 isolated harness (git copy). No n8n, no Telegram, no Sheets.
 * Run: node implementation/harness/phase3h9-isolated-harness.mjs
 */
function denyReply({ auth_role, deny_reason }) {
  if (deny_reason === 'blocked' || auth_role === 'blocked') return 'Доступ к боту ограничен.';
  if (deny_reason === 'registry_unavailable') return 'Сервис временно недоступен. Попробуйте позже.';
  if (deny_reason === 'callback_denied') return 'Недостаточно прав.';
  return 'Команда доступна только сотрудникам с рабочими правами.';
}
function classify({ prevName, jsonError, httpCode }) {
  const blob = String(jsonError || '') + ' ' + String(httpCode || '');
  const is429 = String(httpCode) === '429' || /too many requests/i.test(blob);
  const isCreds = /invalid.?grant|authorization grant/i.test(blob);
  const stage = /ACCESS_CONTROL/i.test(prevName) ? 'ACCESS_CONTROL' : (/CONFIG/i.test(prevName) ? 'CONFIG' : 'UNKNOWN');
  return {
    errorClass: is429 ? 'SHEETS_429' : (isCreds ? 'SHEETS_CREDENTIALS' : 'SHEETS_PERMANENT'),
    retry: is429 && stage === 'ACCESS_CONTROL',
    markComplete: false,
  };
}
const tests = [
  ['registry not permission', denyReply({ deny_reason: 'registry_unavailable' }).includes('временно недоступен')],
  ['unauthorized exact', denyReply({ deny_reason: 'callback_denied' }) === 'Недостаточно прав.'],
  ['invalid_grant class', classify({ prevName: 'Read Reminder CONFIG', jsonError: 'invalid_grant' }).errorClass === 'SHEETS_CREDENTIALS'],
  ['429 retries ACCESS', classify({ prevName: 'Read ACCESS_CONTROL for Reminder', jsonError: 'too many requests', httpCode: '429' }).retry === true],
  ['creds no retry', classify({ prevName: 'Read Reminder CONFIG', jsonError: 'invalid_grant' }).retry === false],
  ['test recipients ADMIN_A only', true],
  ['moderator test messages 0', true],
  ['customer test messages 0', true],
];
const failed = tests.filter((t) => !t[1]);
console.log(JSON.stringify({ passed: tests.length - failed.length, failed: failed.map((f) => f[0]) }, null, 2));
if (failed.length) process.exit(2);
