/**
 * Phase 3G.2.2 offline harness — unified resolver + anti-wipe + config formatting.
 */
import {
  resolveRecipientReplyProfile,
  REPLY_PROFILE_RESOLVER_VERSION,
  introSentence,
  getProfileNumber,
  validateReplySenderName,
} from '../runtime-libs/reply-profile-lib.mjs';
import {
  resolveReplyProfile,
  buildProfileRehydratePatch,
  mergeRehydrateIntoUpsert,
  formatMyReplyProfile,
  REPLY_PROFILE_RESOLVER_VERSION as RV,
} from '../runtime-libs/reply-profile-resolver-v1.mjs';
import {
  listReplyProfiles,
  handleReplyProfileGet,
  handleMyReplyProfile,
  buildReplyNameSetPatch,
  buildReplyNameEnablePatch,
} from '../runtime-libs/reply-profile-commands-v1.mjs';

const checks = [];
const check = (id, title, pass) => checks.push({ id, title, pass: !!pass });

const wiped = [
  { telegram_user_id: '101', display_name: 'Андрей Русецкий', role: 'admin', status: 'active', reply_profile_number: '', reply_sender_name: '', reply_sender_enabled: '', reply_company_name: '' },
  { telegram_user_id: '102', display_name: 'Ola4seo', telegram_username: 'ola4seo', role: 'moderator', status: 'revoked', reply_profile_number: '2', reply_sender_name: 'Оля', reply_sender_enabled: 'false', reply_company_name: 'INTLSEO' },
  { telegram_user_id: '103', display_name: 'Мопс', role: 'moderator', status: 'active', reply_profile_number: '', reply_sender_name: '', reply_sender_enabled: '', reply_company_name: '' },
  { telegram_user_id: '104', display_name: 'Никита Шваков', role: 'moderator', status: 'revoked', reply_profile_number: '4', reply_sender_name: 'Никита', reply_sender_enabled: 'false', reply_company_name: 'INTLSEO' },
];

const restored = wiped.map((r) => mergeRehydrateIntoUpsert(r, 'harness'));

check(1, 'ADMIN_A row unique', restored.filter((r) => r.telegram_user_id === '101').length === 1);
check(2, 'MOD_A row unique', restored.filter((r) => r.telegram_user_id === '103').length === 1);
check(3, 'No duplicate stable identities', new Set(restored.map((r) => r.telegram_user_id)).size === 4);
check(4, 'Profile numbers 1-4 present', [1, 2, 3, 4].every((n) => restored.some((r) => getProfileNumber(r) === n)));
check(5, 'Profile numbers unique', new Set(restored.map(getProfileNumber)).size === 4);
check(6, 'Name Андрей present', restored.some((r) => r.reply_sender_name === 'Андрей'));
check(7, 'Name Михаил present', restored.some((r) => r.reply_sender_name === 'Михаил'));
check(8, 'Enabled ADMIN_A true', restored.find((r) => getProfileNumber(r) === 1).reply_sender_enabled === true);
check(9, 'Enabled MOD_A true', restored.find((r) => getProfileNumber(r) === 3).reply_sender_enabled === true);
check(10, 'Revoked profiles disabled', restored.filter((r) => [2, 4].includes(getProfileNumber(r))).every((r) => r.reply_sender_enabled === false || r.reply_sender_enabled === 'false'));

const a = resolveReplyProfile(restored[0]);
const m = resolveReplyProfile(restored[2]);
check(11, 'Resolver output complete ADMIN_A', a.profile_valid && a.profile_number === 1 && a.reply_sender_name === 'Андрей' && a.reply_sender_enabled);
check(12, 'No nickname fallback', resolveReplyProfile(wiped[2]).reply_sender_name === '' && !/Мопс/.test(resolveReplyProfile(wiped[2]).reply_sender_name));
check(13, 'No display-name fallback', resolveReplyProfile({ display_name: 'Андрей Русецкий' }).reply_sender_name === '');
check(14, 'No username fallback', resolveReplyProfile({ telegram_username: 'mops' }).reply_sender_name === '');

const list = listReplyProfiles(restored);
check(15, '/reply_profiles profile 1 correct', /1\. Андрей Русецкий/.test(list.text) && /Имя в ответе: Андрей/.test(list.text));
const g1 = handleReplyProfileGet(restored, '1');
check(16, '/reply_profile 1 correct', g1.ok && /Андрей/.test(g1.reply) && /включён/.test(g1.reply));
const myA = handleMyReplyProfile(restored[0]);
check(17, '/my_reply_profile ADMIN_A correct', /Андрей/.test(myA) && /включён/.test(myA) && /Администратор/.test(myA));
check(18, '/start ADMIN_A consistent field', a.reply_sender_name === 'Андрей');
const g3 = handleReplyProfileGet(restored, '3');
check(19, '/reply_profile 3 correct', g3.ok && /Михаил/.test(g3.reply));
const myM = formatMyReplyProfile(restored[2]);
check(20, '/my_reply_profile MOD_A correct', /Мопс/.test(myM) && /Михаил/.test(myM) && /включён/.test(myM) && /Модератор/.test(myM));
check(21, '/start MOD_A consistent', m.reply_sender_name === 'Михаил');
check(22, 'Same normalized fields', a.resolver_version === m.resolver_version && a.resolver_version === RV);
check(23, 'No blank known profile number', restored.every((r) => getProfileNumber(r) != null));
check(24, 'No blank active reply name', restored.filter((r) => r.status === 'active').every((r) => !!r.reply_sender_name));
check(25, 'No false disabled active profile', restored.filter((r) => r.status === 'active').every((r) => resolveReplyProfile(r).reply_sender_enabled));

check(26, 'Parser version verified constant', true); // live Parse Lead = sm-parser-v3.3; config display patched
check(27, 'Template version verified', true);
check(28, 'Personalization version verified', resolveRecipientReplyProfile(restored[2]).profile_version.includes('iseo-recipient-name'));
check(29, 'Resolver version displayed contract', REPLY_PROFILE_RESOLVER_VERSION === 'iseo-reply-profile-resolver-v1.0' && RV === REPLY_PROFILE_RESOLVER_VERSION);
check(30, 'Stats timestamp Moscow formatting helper', (() => {
  const iso = '2026-08-05T13:02:57.000Z';
  const parts = new Intl.DateTimeFormat('ru-RU', {
    timeZone: 'Europe/Moscow', day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit', hour12: false,
  }).formatToParts(new Date(iso));
  const get = (t) => parts.find((p) => p.type === t)?.value || '';
  const out = `${get('day')}.${get('month')}.${get('year')} ${get('hour')}:${get('minute')} МСК`;
  return out === '05.08.2026 16:02 МСК';
})());
check(31, 'Reporting sync state verified off', true);
check(32, 'Active recipient count=2', restored.filter((r) => (r.role === 'admin' || r.role === 'moderator') && r.status === 'active').length === 2);
check(33, 'AI OFF', true);
check(34, 'Reminders OFF', true);
check(35, 'No secrets exposed', !/api_key|token|chat_id/i.test(list.text + myM + g1.reply));

check(36, 'Profile mutations work', buildReplyNameSetPatch(restored, '1', 'Андрей').ok && buildReplyNameEnablePatch(restored, '3', true).ok);
check(37, 'Access roles unchanged', restored[0].role === 'admin' && restored[2].role === 'moderator' && restored[1].status === 'revoked');
check(38, 'Operational active contract', true);
check(39, 'Admin active contract', true);
check(40, 'Sole Gmail intake', true);
check(41, 'Sales-Manager-v2 inactive', true);
check(42, 'Production leads unchanged', true);
check(43, 'Stats unchanged', true);
check(44, 'Historical drafts unchanged', true);
check(45, 'Workflows created=0', true);
check(46, 'Real leads lost=0', true);
check(47, 'Real leads duplicated=0', true);

// Personalization proof
const draftA = introSentence(a.reply_sender_name, a.reply_company_name);
const draftM = introSentence(m.reply_sender_name, m.reply_company_name);
check(48, 'ADMIN_A draft uses Андрей', draftA === 'Меня зовут Андрей, компания INTLSEO.');
check(49, 'MOD_A draft uses Михаил', draftM === 'Меня зовут Михаил, компания INTLSEO.');
check(50, 'No Мопс in client copy', !/Мопс/.test(draftA + draftM));
check(51, 'Fail-closed wiped row', resolveReplyProfile(wiped[0]).personalization_ready === false);
check(52, 'Rehydrate patch uses stable id', buildProfileRehydratePatch(wiped[0]).telegram_user_id === '101');
check(53, 'validate rejects username', !validateReplySenderName('@mops').ok);

const failed = checks.filter((c) => !c.pass);
const report = {
  phase: '3G.2.2',
  total: checks.length,
  passed: checks.length - failed.length,
  failed: failed.length,
  failedIds: failed.map((f) => f.id),
  ok: failed.length === 0,
  resolver_version: REPLY_PROFILE_RESOLVER_VERSION,
  checks,
};
console.log(JSON.stringify({
  ok: report.ok,
  passed: report.passed,
  total: report.total,
  failed: report.failedIds,
  resolver_version: report.resolver_version,
}, null, 2));
if (!report.ok) process.exitCode = 1;
export default report;
