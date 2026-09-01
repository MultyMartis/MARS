const j = $input.first().json;
const now = new Date().toISOString();
const isTgFail =
  j.telegram_ok === false ||
  j.force_telegram_fail === true ||
  j.error_code === 'telegram_delivery_failed';
const isSheets429 =
  j.error_code === 'sheets_quota_exceeded' || j.sheets_quota_429 === true;

const STAGES = new Set([
  'schedule_trigger', 'gmail_read', 'parse_lead', 'raw_write', 'config_read', 'deterministic_processing',
  'ai_request', 'ai_validation', 'dedupe_lookup', 'clean_write',
  'telegram_send', 'gmail_labels', 'runtime_state',
]);

let error_code = j.error_code;
let stage = j.error_stage || j.stage;
let message = j.error_message || j.message;

if (isTgFail) {
  error_code = 'telegram_delivery_failed';
  stage = 'telegram_send';
  message = 'Не удалось доставить карточку в Telegram.';
} else if (isSheets429) {
  error_code = 'sheets_quota_exceeded';
  stage = STAGES.has(String(j.error_stage || '')) ? String(j.error_stage) : 'dedupe_lookup';
  message = 'Google Sheets API quota exceeded (429). Retry deferred.';
} else {
  error_code = error_code || 'processing_error';
  stage = STAGES.has(String(stage || '')) ? String(stage) : (stage || 'unknown');
  message = String(message || 'Ошибка обработки').slice(0, 500);
  message = message
    .replace(/stack\s:[\s\S]*/i, '')
    .replace(/https?:\/\/\S+/gi, '[url]')
    .replace(/chat[_\s-]?id\s*[:=]\s*-?\d+/gi, 'chat_id=[redacted]')
    .slice(0, 500);
}

const safeLeadRef = String(j.fixture_id || j.readable_ref || j.synthetic_marker || 'SYNTHETIC_TEST').slice(0, 120);

return [{
  json: {
    ...j,
    ts: now,
    error_ts: now,
    error_code,
    stage,
    message,
    error_message: message,
    lead_id: safeLeadRef,
    workflow: 'Operational.dev',
    resolved: false,
    telegram_ok: false,
    last_error_code: error_code,
    last_error_stage: stage,
    last_error_at: now,
  },
}];
