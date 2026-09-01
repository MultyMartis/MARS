// Phase Google Sheets instance quota repair — DEDUP 429 → Error Handler bridge
// SYNC: implementation/patches/SheetsQuotaErrorBridge.google-sheets-429-repair.js

const sd = $getWorkflowStaticData('global');
if (!sd.sheetsQuotaDeferByMsgId) sd.sheetsQuotaDeferByMsgId = {};
const DEFER_MS = 5 * 60 * 1000;
const now = Date.now();

let lead = {};
try {
  lead = $('Parse Lead').first().json || {};
} catch (e) {
  lead = {};
}
try {
  const merge = $('Merge AI or Fallback').first().json;
  if (merge && merge.gmail_message_id) lead = { ...lead, ...merge };
} catch (e) {
  // Merge may not have run on early DEDUP failure — Parse Lead is enough.
}

const msgId = String(lead.gmail_message_id || '').trim();
const errIn = $input.first();
const raw = errIn?.json || {};
const err = raw.error || raw;
const errStr = JSON.stringify(err).toLowerCase();
const is429 =
  errStr.includes('429') ||
  errStr.includes('quota exceeded') ||
  errStr.includes('read requests');

if (msgId && is429) {
  sd.sheetsQuotaDeferByMsgId[msgId] = {
    deferUntil: now + DEFER_MS,
    setAt: now,
    reason: 'sheets_429',
  };
}

let stage = 'dedupe_lookup';
try {
  if (!$('Lookup DEDUP_INDEX').isExecuted) stage = 'raw_write';
} catch (e) {
  stage = 'dedupe_lookup';
}

return [{
  json: {
    ...lead,
    error_code: is429 ? 'sheets_quota_exceeded' : 'processing_error',
    error_stage: is429 ? stage : (stage || 'unknown'),
    error_message: is429
      ? 'Google Sheets API quota exceeded (429). Retry deferred.'
      : String(err.message || err.description || 'processing_error').slice(0, 500),
    sheets_quota_429: is429,
    sheets_defer_until:
      msgId && is429 ? sd.sheetsQuotaDeferByMsgId[msgId].deferUntil : undefined,
    telegram_ok: false,
  },
}];
