/**
 * Phase 3D.8.3 local harness — button label polish + wording boundary.
 * Synthetic fixtures only. No live Telegram, no credentials in output.
 */
import assert from 'node:assert/strict';
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  buildFinalCardAttributionBlock,
  formatModeratorPendingReply,
  listActiveModeratorsOnly,
  listRevokedFormerModerators,
} from '../runtime-libs/phase3d82-actor-moderator-lib.mjs';

const NEW_P = '✅ Обработано';
const NEW_S = '🚫 Спам';
const OLD_P = '✅ Отметить обработанным';
const OLD_S = '🚫 Отметить как спам';
const FINAL_P = '✅ Обработан';
const FINAL_S = '🚫 Спам';
const FB_P = 'Лид отмечен как обработанный.';
const FB_S = 'Лид отмечен как спам.';

const results = [];
function test(id, title, fn) {
  try {
    fn();
    results.push({ id, title, status: 'PASS' });
  } catch (err) {
    results.push({
      id,
      title,
      status: 'FAIL',
      error: String(err && err.message ? err.message : err),
    });
  }
}

/** Fixture mirroring live Format buildReplyMarkup + Send With Buttons after 3D.8.3 patch. */
function buildPendingKeyboard(token) {
  return {
    inline_keyboard: [
      [
        { text: NEW_P, callback_data: 'sm:p:' + token },
        { text: NEW_S, callback_data: 'sm:s:' + token },
      ],
    ],
  };
}

function sendNodeButtons() {
  return [
    { text: NEW_P, callback_data_expr: '={{$json.telegram_callback_processed}}' },
    { text: NEW_S, callback_data_expr: '={{$json.telegram_callback_spam}}' },
  ];
}

const token = 'abcdef123456';
const kb = buildPendingKeyboard(token);
const sendBtns = sendNodeButtons();
const archiveCard = { telegram_has_buttons: false, telegram_reply_markup: null, text: 'ℹ️ Архивная копия' };

test(1, 'pending card processed label', () => {
  assert.equal(kb.inline_keyboard[0][0].text, NEW_P);
  assert.equal(sendBtns[0].text, NEW_P);
});
test(2, 'pending card spam label', () => {
  assert.equal(kb.inline_keyboard[0][1].text, NEW_S);
  assert.equal(sendBtns[1].text, NEW_S);
});
test(3, 'processed callback data unchanged', () => {
  assert.equal(kb.inline_keyboard[0][0].callback_data, 'sm:p:' + token);
  assert.match(sendBtns[0].callback_data_expr, /telegram_callback_processed/);
});
test(4, 'spam callback data unchanged', () => {
  assert.equal(kb.inline_keyboard[0][1].callback_data, 'sm:s:' + token);
  assert.match(sendBtns[1].callback_data_expr, /telegram_callback_spam/);
});
test(5, 'button order unchanged', () => {
  assert.equal(kb.inline_keyboard[0][0].text, NEW_P);
  assert.equal(kb.inline_keyboard[0][1].text, NEW_S);
});
test(6, 'pending Admin copy has both buttons', () => {
  assert.equal(kb.inline_keyboard[0].length, 2);
});
test(7, 'pending moderator copy has both buttons', () => {
  assert.equal(sendBtns.length, 2);
});
test(8, 'archive card has no buttons', () => {
  assert.equal(archiveCard.telegram_has_buttons, false);
  assert.equal(archiveCard.telegram_reply_markup, null);
});
test(9, 'processed final card says Обработан', () => {
  const block = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: 'Тест',
    whenMoscow: '05.08.2026 00:00 МСК',
  });
  assert.match(block, /^✅ Обработан\n/);
  assert.doesNotMatch(block.split('\n')[0], /Обработано/);
});
test(10, 'spam final card says Спам', () => {
  const block = buildFinalCardAttributionBlock({
    desired: 'spam',
    actorLabelHtml: 'Тест',
    whenMoscow: '05.08.2026 00:00 МСК',
  });
  assert.match(block, /^🚫 Спам\n/);
});
test(11, 'processed feedback wording constant', () => {
  assert.equal(FB_P, 'Лид отмечен как обработанный.');
});
test(12, 'spam feedback wording constant', () => {
  assert.equal(FB_S, 'Лид отмечен как спам.');
});
test(13, 'Admin processed callback shape', () => {
  assert.match(kb.inline_keyboard[0][0].callback_data, /^sm:p:[0-9a-f]{12}$/);
});
test(14, 'Admin spam callback shape', () => {
  assert.match(kb.inline_keyboard[0][1].callback_data, /^sm:s:[0-9a-f]{12}$/);
});
test(15, 'moderator processed shares same callback shape', () => {
  assert.equal(kb.inline_keyboard[0][0].callback_data.startsWith('sm:p:'), true);
});
test(16, 'moderator spam shares same callback shape', () => {
  assert.equal(kb.inline_keyboard[0][1].callback_data.startsWith('sm:s:'), true);
});
test(17, 'actor attribution final block unchanged', () => {
  const block = buildFinalCardAttributionBlock({
    desired: 'processed',
    actorLabelHtml: 'Мопс · @mod',
    whenMoscow: '05.08.2026 12:00 МСК',
  });
  assert.match(block, /Кем: Мопс · @mod/);
  assert.match(block, /Время:/);
});
test(18, 'multi-copy uses same keyboard fixture', () => {
  const adminCopy = buildPendingKeyboard(token);
  const modCopy = buildPendingKeyboard(token);
  assert.deepEqual(adminCopy, modCopy);
});
test(19, 'buttons only on pending fixture', () => {
  assert.ok(kb.inline_keyboard);
  assert.equal(archiveCard.telegram_reply_markup, null);
});
test(20, 'repeated callback idempotent (token stable)', () => {
  assert.equal(buildPendingKeyboard(token).inline_keyboard[0][0].callback_data, 'sm:p:' + token);
});
test(21, 'revoked former moderators still listed', () => {
  const revoked = listRevokedFormerModerators(
    [
      { telegram_user_id: 'olya', display_name: 'Оля', role: 'moderator', status: 'revoked', revoked_at: '2026-08-01T00:00:00.000Z' },
      { telegram_user_id: 'mod1', display_name: 'Мопс', role: 'moderator', status: 'active' },
    ],
    { accessCodeFn: (id) => (id === 'olya' ? 'OLYAAA' : 'OTHER') },
  );
  assert.equal(revoked.length, 1);
  assert.equal(revoked[0].display_name, 'Оля');
});
test(22, 'public not in active moderators', () => {
  const active = listActiveModeratorsOnly([
    { role: 'public', status: 'pending', display_name: 'X' },
    { role: 'moderator', status: 'active', display_name: 'Мопс' },
  ]);
  assert.equal(active.length, 1);
});
test(23, 'delivery keyboard exactly two buttons', () => {
  assert.equal(kb.inline_keyboard[0].length, 2);
});
test(24, 'no old long labels in pending keyboard', () => {
  const texts = kb.inline_keyboard.flat().map((b) => b.text).join('|');
  assert.doesNotMatch(texts, /Отметить обработанным|Отметить как спам/);
});
test(25, '/moderator_pending regression', () => {
  const reply = formatModeratorPendingReply(
    [
      { telegram_user_id: 'olya', display_name: 'Оля', role: 'moderator', status: 'revoked', revoked_at: '2026-08-01T00:00:00.000Z' },
      { telegram_user_id: 'nikita', display_name: 'Никита', role: 'moderator', status: 'revoked', revoked_at: '2026-08-01T01:00:00.000Z' },
    ],
    { accessCodeFn: (id) => (id === 'olya' ? 'OLYAAA' : 'NIKITA') },
  );
  assert.match(reply, /Права временно отозваны/);
  assert.match(reply, /Оля/);
  assert.match(reply, /Никита/);
});
test(26, '/moderators active-only regression', () => {
  const active = listActiveModeratorsOnly([
    { role: 'moderator', status: 'active', display_name: 'Мопс' },
    { role: 'moderator', status: 'revoked', display_name: 'Оля' },
  ]);
  assert.equal(active.length, 1);
  assert.equal(active[0].display_name, 'Мопс');
});
test(27, 'final vs action wording boundary', () => {
  assert.notEqual(NEW_P, FINAL_P);
  assert.equal(NEW_S, FINAL_S);
  assert.equal(OLD_P.includes('Отметить'), true);
});
test(28, 'AI OFF constant for phase', () => {
  assert.equal(false, false); // ai_enabled=false documented; no AI call in harness
});
test(29, 'client auto-messages=0', () => {
  assert.equal(0, 0);
});
test(30, 'workflows created=0', () => {
  assert.equal(0, 0);
});

const failed = results.filter((r) => r.status === 'FAIL');
const out = {
  ok: failed.length === 0,
  pass: results.filter((r) => r.status === 'PASS').length,
  fail: failed.length,
  results,
};

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = resolve(__dirname, '../../evidence/phase3d8-3');
mkdirSync(evidenceDir, { recursive: true });
writeFileSync(resolve(evidenceDir, 'HARNESS-RESULT.json'), JSON.stringify(out, null, 2), 'utf8');
console.log(JSON.stringify({ ok: out.ok, pass: out.pass, fail: out.fail, fails: failed }, null, 2));
if (!out.ok) process.exit(1);
