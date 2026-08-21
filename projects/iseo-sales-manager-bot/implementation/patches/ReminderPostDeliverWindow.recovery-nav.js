/**
 * After Telegram reminder delivery: mark business window complete when all intended
 * recipients are delivered (ledger + this item). Runs even if Sheets upsert later 429s.
 */
const items = $input.all().map((i) => i.json || {});
const primary = items[0] || {};
const windowKey = String(primary.reminder_window || '');
const intended = Number(primary.reminder_intended_recipient_count || 0) || items.length || 1;

function isDelivered(j) {
  const st = String(j.status || '').toLowerCase();
  return j.telegram_send_ok === true || st === 'delivered' || st === 'sent';
}

const deliveredHere = items.filter(isDelivered);
if (!deliveredHere.length) {
  return [];
}

let ledgerDeliveredKeys = new Set();
try {
  const rows = $('Read REMINDER_DELIVERIES').all().map((i) => i.json).filter((r) => r && r.reminder_key && !r.error);
  for (const row of rows) {
    if (String(row.reminder_window || '') !== windowKey) continue;
    const st = String(row.status || '').toLowerCase();
    if (st === 'delivered' || st === 'sent') ledgerDeliveredKeys.add(String(row.reminder_key));
  }
} catch (e) {}

for (const j of deliveredHere) {
  if (j.reminder_key) ledgerDeliveredKeys.add(String(j.reminder_key));
}

const complete = ledgerDeliveredKeys.size >= intended;
if (!complete) {
  // Do not stamp ERROR / last_window yet — recovery may finish remaining recipients.
  return [];
}
return [{ json: {
  ...primary,
  reminder_send: false,
  reminder_mark_window_complete: true,
  reminder_skip_reason: 'all_recipients_done',
  reminder_last_recipient_count: ledgerDeliveredKeys.size,
  reminder_intended_recipient_count: intended,
  pending_count_snapshot: primary.pending_count_snapshot,
  reminder_post_deliver: true,
  reminder_window: windowKey,
} }];
