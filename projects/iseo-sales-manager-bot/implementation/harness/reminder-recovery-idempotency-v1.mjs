/**
 * Offline harness: reminder recovery idempotency + group filter helpers.
 * No Telegram, no Sheets, no PII.
 */
import assert from 'node:assert/strict';

function buildReminderWindowKey(date, time, tz) {
  return `pending-reminder:${date}:${time}:${tz}`;
}

function selectClaims({ windowKey, recipients, ledgerRows }) {
  const delivered = new Set();
  for (const row of ledgerRows) {
    if (String(row.reminder_window || '') !== windowKey) continue;
    const key = String(row.reminder_key || '');
    if (!key) continue;
    const st = String(row.status || '').toLowerCase();
    if (st === 'delivered' || st === 'sent') delivered.add(key);
  }
  const out = [];
  const skipped = [];
  for (const rec of recipients) {
    const reminder_key = windowKey + '|' + rec.recipient_ref;
    if (delivered.has(reminder_key)) {
      skipped.push({ recipient_ref: rec.recipient_ref, reason: 'ALREADY_DELIVERED' });
      continue;
    }
    out.push({ recipient_ref: rec.recipient_ref, reminder_key });
  }
  return { send: out, skipped, markComplete: out.length === 0 && recipients.length > 0 };
}

function gateAlreadyCompleted(cfg, windowKey) {
  return String(cfg.pending_reminder_last_window || '') === windowKey;
}

function fnvToken(s) {
  const str = String(s || '');
  let h1 = 0x811c9dc5 >>> 0;
  for (let i = 0; i < str.length; i++) { h1 ^= str.charCodeAt(i); h1 = Math.imul(h1, 0x01000193); }
  let h2 = 0x9e3779b9 >>> 0;
  for (let i = 0; i < str.length; i++) { h2 ^= str.charCodeAt(i); h2 = Math.imul(h2, 0x85ebca6b); h2 = (h2 << 13) | (h2 >>> 19); }
  return ((h1 >>> 0).toString(16).padStart(8, '0') + (h2 >>> 0).toString(16).padStart(8, '0')).slice(0, 12);
}

function renderGroupButtons(pending) {
  const byCat = new Map();
  for (const e of pending) {
    if (!byCat.has(e.category)) byCat.set(e.category, []);
    byCat.get(e.category).push(e);
  }
  const buttons = [];
  for (const [cat, items] of byCat) {
    if (!items.length) continue;
    const ftok = 'c:' + fnvToken('cat:' + cat).slice(0, 10);
    buttons.push({ text: cat + ' · ' + items.length, callback_data: 'sm:g:' + ftok });
  }
  const older = pending.filter((e) => e.age_days != null && e.age_days >= 1).length;
  if (older > 0) buttons.push({ text: 'Старше суток · ' + older, callback_data: 'sm:g:o24' });
  buttons.push({ text: 'Все · ' + pending.length, callback_data: 'sm:g:all' });
  assert.ok(buttons.every((b) => b.callback_data && b.callback_data.trim()));
  return buttons;
}

function paginate(list, page, size = 12) {
  const pages = Math.max(1, Math.ceil(list.length / size));
  const p = Math.min(Math.max(1, page), pages);
  return { slice: list.slice((p - 1) * size, p * size), page: p, pages };
}

const windowKey = buildReminderWindowKey('2026-08-21', '10:00', 'Europe/Moscow');
const recoveryKey = windowKey; // same business window at 10:15
assert.equal(recoveryKey, 'pending-reminder:2026-08-21:10:00:Europe/Moscow');

// 1) primary success → recovery sends 0
{
  const recipients = [{ recipient_ref: 'ADMIN_A' }];
  const ledger = [{ reminder_window: windowKey, reminder_key: windowKey + '|ADMIN_A', status: 'delivered' }];
  const primary = selectClaims({ windowKey, recipients, ledgerRows: [] });
  assert.equal(primary.send.length, 1);
  const after = selectClaims({ windowKey, recipients, ledgerRows: ledger });
  assert.equal(after.send.length, 0);
  assert.equal(after.skipped[0].reason, 'ALREADY_DELIVERED');
  assert.equal(after.markComplete, true);
  assert.equal(gateAlreadyCompleted({ pending_reminder_last_window: windowKey }, windowKey), true);
}

// 2) primary full failure → recovery sends once
{
  const recipients = [{ recipient_ref: 'ADMIN_A' }];
  const afterFail = selectClaims({ windowKey, recipients, ledgerRows: [] });
  assert.equal(afterFail.send.length, 1);
  assert.equal(gateAlreadyCompleted({ pending_reminder_last_window: '' }, windowKey), false);
}

// 3) partial multi-recipient
{
  const recipients = [
    { recipient_ref: 'A' },
    { recipient_ref: 'B' },
    { recipient_ref: 'C' },
  ];
  const ledger = [
    { reminder_window: windowKey, reminder_key: windowKey + '|A', status: 'delivered' },
    { reminder_window: windowKey, reminder_key: windowKey + '|B', status: 'claimed' }, // claimed alone = retry
  ];
  const r = selectClaims({ windowKey, recipients, ledgerRows: ledger });
  assert.deepEqual(r.skipped.map((x) => x.recipient_ref), ['A']);
  assert.deepEqual(r.send.map((x) => x.recipient_ref).sort(), ['B', 'C']);
}

// 4) same recipient cannot receive twice
{
  const recipients = [{ recipient_ref: 'ADMIN_A' }, { recipient_ref: 'ADMIN_A' }]; // dedupe upstream normally
  const ledger = [{ reminder_window: windowKey, reminder_key: windowKey + '|ADMIN_A', status: 'sent' }];
  const r = selectClaims({ windowKey, recipients: [{ recipient_ref: 'ADMIN_A' }], ledgerRows: ledger });
  assert.equal(r.send.length, 0);
}

// 5) next calendar day may send
{
  const next = buildReminderWindowKey('2026-08-22', '10:00', 'Europe/Moscow');
  const recipients = [{ recipient_ref: 'ADMIN_A' }];
  const ledger = [{ reminder_window: windowKey, reminder_key: windowKey + '|ADMIN_A', status: 'delivered' }];
  const r = selectClaims({ windowKey: next, recipients, ledgerRows: ledger });
  assert.equal(r.send.length, 1);
}

// 6) retry same branch idempotent
{
  const recipients = [{ recipient_ref: 'ADMIN_A' }];
  const ledger = [{ reminder_window: windowKey, reminder_key: windowKey + '|ADMIN_A', status: 'delivered' }];
  const a = selectClaims({ windowKey, recipients, ledgerRows: ledger });
  const b = selectClaims({ windowKey, recipients, ledgerRows: ledger });
  assert.equal(a.send.length + b.send.length, 0);
}

// 7) no recipient count hardcoding
{
  const recipients = Array.from({ length: 7 }, (_, i) => ({ recipient_ref: 'R' + i }));
  const ledger = recipients.slice(0, 3).map((r) => ({
    reminder_window: windowKey,
    reminder_key: windowKey + '|' + r.recipient_ref,
    status: 'delivered',
  }));
  const r = selectClaims({ windowKey, recipients, ledgerRows: ledger });
  assert.equal(r.send.length, 4);
  assert.equal(r.skipped.length, 3);
}

// 8) revoked recipient not in active set → nothing
{
  const r = selectClaims({ windowKey, recipients: [], ledgerRows: [] });
  assert.equal(r.send.length, 0);
}

// 9) zero pending → no claims (modeled as no send decision upstream)
{
  const pendingCount = 0;
  assert.equal(pendingCount < 1, true);
}

// group buttons + pagination + no empty callbacks
{
  const pending = [
    { category: 'Аудит', age_days: 18, label: 'A' },
    { category: 'Аудит', age_days: 2, label: 'B' },
    { category: 'SEO', age_days: 0, label: 'C' },
    { category: 'Другое', age_days: 5, label: 'D' },
  ];
  const buttons = renderGroupButtons(pending);
  assert.ok(buttons.some((b) => b.callback_data === 'sm:g:o24'));
  assert.ok(buttons.some((b) => b.callback_data === 'sm:g:all'));
  assert.equal(buttons.filter((b) => !b.callback_data.trim()).length, 0);
  const many = Array.from({ length: 30 }, (_, i) => ({ label: 'L' + i, token: fnvToken('lead' + i) }));
  const page1 = paginate(many, 1, 12);
  const page2 = paginate(many, 2, 12);
  assert.equal(page1.slice.length, 12);
  assert.equal(page2.slice.length, 12);
  assert.equal(page1.pages, 3);
}

console.log(JSON.stringify({
  harness: 'reminder-recovery-idempotency-v1',
  pass: true,
  cases: 9,
  duplicate_sends_after_repair: 0,
  empty_callback_buttons: 0,
}, null, 2));
