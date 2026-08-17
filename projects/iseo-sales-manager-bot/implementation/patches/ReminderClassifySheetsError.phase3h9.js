// Phase 3H.9 — classify reminder Sheets errors; bounded 429 retry via Wait loop.
// Distinguishes SHEETS_429 vs SHEETS_CREDENTIALS (invalid_grant) vs SHEETS_PERMANENT.
// Credential failures are not retried (retry cannot restore OAuth).
const item = $input.first();
const j = item.json || {};
const err = item.error || {};
const je = j.error;
const msg = [
  err && err.message,
  err && err.description,
  typeof je === 'string' ? je : (je && (je.message || je.description)),
  j.message,
  j.errorMessage,
  j.errorDescription,
].filter(Boolean).join(' ');
const http = String(err.httpCode || err.httpStatus || j.httpCode || (je && je.httpCode) || '');
const prev = String($prevNode?.name || '');
let stage = 'UNKNOWN';
if (/ACCESS_CONTROL/i.test(prev)) stage = 'ACCESS_CONTROL';
else if (/CLEAN/i.test(prev)) stage = 'CLEAN';
else if (/REMINDER_DELIVERIES/i.test(prev)) stage = 'REMINDER_DELIVERIES';
else if (/CONFIG/i.test(prev) && /Reminder/i.test(prev)) stage = 'CONFIG';

const blob = String(msg) + ' ' + String(http);
const is429 = http === '429' || /quota|rate.?limit|too many requests|RESOURCE_EXHAUSTED|userRateLimitExceeded/i.test(blob);
const isCreds = /invalid.?grant|unauthorized|invalid_client|401|403|refresh token is invalid|authorization grant/i.test(blob);
const sd = $getWorkflowStaticData('node');
const execId = String(($execution && $execution.id) || ('e' + Date.now()));
if (sd.p3h82_exec !== execId) { sd.p3h82_exec = execId; sd.p3h82_n = 0; }
sd.p3h82_n = Number(sd.p3h82_n || 0) + 1;
const failCount = sd.p3h82_n;
const maxFailsThenStop = 4;
const retry = is429 && stage === 'ACCESS_CONTROL' && failCount < maxFailsThenStop;
const waits = [5, 15, 30];
const wait_seconds = retry ? waits[Math.min(failCount - 1, waits.length - 1)] : 0;

let gate = {};
try { gate = $('Reminder Schedule Gate').first().json || {}; } catch (e) { gate = {}; }

const errorClass = is429 ? 'SHEETS_429' : (isCreds ? 'SHEETS_CREDENTIALS' : 'SHEETS_PERMANENT');
const decision = (is429 && stage === 'ACCESS_CONTROL')
  ? 'ERROR_SHEETS_429_ACCESS'
  : (is429 ? ('ERROR_SHEETS_429_' + stage) : (isCreds ? 'ERROR_SHEETS_CREDENTIALS' : 'ERROR'));
const skipReason = is429
  ? (stage === 'ACCESS_CONTROL' ? 'access_read_error' : 'sheets_429')
  : (isCreds ? 'sheets_credentials' : 'sheets_permanent');
const safe = is429
  ? 'лимит Google Sheets API'
  : (isCreds ? 'нет доступа к таблице. Нужна повторная авторизация Google Sheets.' : 'ошибка чтения таблицы');

return [{ json: {
  reminder_send: false,
  reminder_mark_window_complete: false,
  reminder_skip_reason: skipReason,
  reminder_window: gate.reminder_window || '',
  pending_count_snapshot: 'not_computed',
  reminder_sheets_retry: retry,
  wait_seconds,
  sheets_fail_count: failCount,
  sheets_retry_attempts: failCount,
  last_error_class: errorClass,
  last_error_stage: stage,
  last_error_safe: safe,
  reminder_decision_code: decision,
} }];
