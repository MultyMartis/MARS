// Phase Google Sheets instance quota repair — defer gate (Operational.dev)
// SYNC: implementation/patches/SheetsQuotaDeferGate.google-sheets-429-repair.js

const DEFER_MS = 5 * 60 * 1000;
const sd = $getWorkflowStaticData('global');
if (!sd.sheetsQuotaDeferByMsgId) sd.sheetsQuotaDeferByMsgId = {};
const now = Date.now();
const j = $input.first().json;
const msgId = String(j.gmail_message_id || '').trim();

let deferred = false;
let deferUntil = 0;
if (msgId) {
  const entry = sd.sheetsQuotaDeferByMsgId[msgId];
  if (entry && Number(entry.deferUntil) > now) {
    deferred = true;
    deferUntil = Number(entry.deferUntil);
  } else if (entry && Number(entry.deferUntil) <= now) {
    delete sd.sheetsQuotaDeferByMsgId[msgId];
  }
}

return [{
  json: {
    ...j,
    __sheets_quota_deferred: deferred,
    __sheets_quota_defer_until: deferUntil || undefined,
    __sheets_quota_defer_ms_remaining: deferred ? Math.max(0, deferUntil - now) : 0,
  },
}];
