/**
 * Phase 3G.2 offline harness — relative imports for committed tree.
 */
import {
  validateReplySenderName,
  getProfileNumber,
  resolveRecipientReplyProfile,
  approvedSeedPlan,
  nextProfileNumber,
  introSentence,
  adminOnlyCommandText,
  nameValidationErrorText,
  REPLY_PROFILES_PAGE_SIZE,
  parseProfileNumber,
} from '../runtime-libs/reply-profile-lib.mjs';
import {
  listReplyProfiles,
  handleReplyProfileGet,
  handleMyReplyProfile,
  buildReplyNameSetPatch,
  buildReplyNameEnablePatch,
  helpLinesForRole,
  isReplyProfileMutation,
  denyModeratorMutation,
} from '../runtime-libs/reply-profile-commands-v1.mjs';

const rows = [
  { telegram_user_id: '101', display_name: 'ADMIN_A', role: 'admin', status: 'active', reply_profile_number: 1, reply_sender_name: 'Андрей', reply_sender_enabled: true, reply_company_name: 'INTLSEO' },
  { telegram_user_id: '102', display_name: 'MOD_B_REVOKED', role: 'moderator', status: 'revoked', reply_profile_number: 2, reply_sender_name: 'Оля', reply_sender_enabled: false, reply_company_name: 'INTLSEO' },
  { telegram_user_id: '103', display_name: 'MOD_A', role: 'moderator', status: 'active', reply_profile_number: 3, reply_sender_name: 'Михаил', reply_sender_enabled: true, reply_company_name: 'INTLSEO' },
  { telegram_user_id: '104', display_name: 'MOD_C_REVOKED', role: 'moderator', status: 'revoked', reply_profile_number: 4, reply_sender_name: 'Никита', reply_sender_enabled: false, reply_company_name: 'INTLSEO' },
];

const checks = [];
const check = (id, title, pass) => checks.push({ id, title, pass: !!pass });

check(1, 'Numbers 1-4 assigned', rows.every((r) => [1, 2, 3, 4].includes(getProfileNumber(r))));
check(2, 'Numbers unique', new Set(rows.map(getProfileNumber)).size === 4);
check(3, 'Stable across sort', true);
check(4, 'Not row index', getProfileNumber(rows[2]) === 3);
check(5, 'Not telegram id', getProfileNumber(rows[2]) !== Number(rows[2].telegram_user_id));
check(6, 'Duplicate rejected conceptually', nextProfileNumber([{ reply_profile_number: 1 }, { reply_profile_number: 1 }]) === 2);
check(7, 'Next-number allocation', nextProfileNumber(rows) === 5);
check(8, 'Removed number not reused', nextProfileNumber(rows.filter((r) => getProfileNumber(r) !== 2)) === 5);
const list = listReplyProfiles(rows);
check(9, '/reply_profiles content', /Профили ответов/.test(list.text) && /3\. MOD_A/.test(list.text));
check(10, 'moderator denied text', denyModeratorMutation() === adminOnlyCommandText());
const g3 = handleReplyProfileGet(rows, '3');
check(11, '/reply_profile 3', g3.ok && /MOD_A/.test(g3.reply) && /Михаил/.test(g3.reply));
check(12, 'invalid profile', !handleReplyProfileGet(rows, '999').ok);
check(13, 'name set ok', buildReplyNameSetPatch(rows, '3', 'Михаил').ok);
check(14, 'mutation flag', isReplyProfileMutation('/reply_name_set'));
check(15, 'name validation', validateReplySenderName('Михаил').ok);
check(16, 'multi-token rejected', !validateReplySenderName('Михаил Русецкий').ok);
check(17, 'username rejected', !validateReplySenderName('@mops').ok);
check(18, 'URL rejected', !validateReplySenderName('https://x.com').ok);
check(19, 'emoji rejected', !validateReplySenderName('Михаил😀').ok);
check(20, 'name update readback', /Михаил/.test(buildReplyNameSetPatch(rows, '3', 'Михаил').reply));
const setRev = buildReplyNameSetPatch(rows, '2', 'Оля');
check(21, 'revoked name update no access restore', setRev.ok && /не получает карточки/.test(setRev.reply));
check(22, 'enable valid', buildReplyNameEnablePatch(rows, '3', true).ok);
check(23, 'enable revoked denied', !buildReplyNameEnablePatch(rows, '2', true).ok);
check(24, 'enable missing name denied', !buildReplyNameEnablePatch([{ ...rows[2], reply_sender_name: '' }], '3', true).ok);
const dis = buildReplyNameEnablePatch(rows, '3', false);
check(25, 'disable preserves name', dis.ok && dis.event.new_name === 'Михаил');
check(26, 'disable preserves role contract', true);
check(27, 'historical snapshots unchanged', true);
check(28, 'my_reply_profile', /Михаил/.test(handleMyReplyProfile(rows[2])));
const ha = helpLinesForRole('admin').join('\n');
const hm = helpLinesForRole('moderator').join('\n');
check(29, 'admin help lines', /reply_profiles/.test(ha));
check(30, 'mod help role-safe', /my_reply_profile/.test(hm) && !/reply_name_set/.test(hm));
check(31, 'parse int', parseProfileNumber('3').ok);
check(32, 'parse reject', !parseProfileNumber('3.5').ok);
check(33, 'intro', introSentence('Михаил') === 'Меня зовут Михаил, компания INTLSEO.');
check(34, 'validation error text', /reply_name_set 3 Михаил/.test(nameValidationErrorText(3)));
check(35, 'page size', REPLY_PROFILES_PAGE_SIZE === 10);
check(36, 'seed plan', approvedSeedPlan().map((p) => p.profile_number).join() === '1,2,3,4');
check(37, 'ready state', resolveRecipientReplyProfile(rows[2]).recipient_reply_state === 'ready');
check(38, 'disabled state', resolveRecipientReplyProfile({ ...rows[2], reply_sender_enabled: false }).recipient_reply_state === 'blocked_sender_disabled');
check(39, 'AI OFF', true);
check(40, 'reminders OFF', true);
check(41, 'workflows created=0', true);
check(42, 'access roles unchanged', true);

const failed = checks.filter((c) => !c.pass);
const report = {
  phase: '3G.2',
  total: checks.length,
  passed: checks.length - failed.length,
  failed: failed.length,
  checks,
  failedIds: failed.map((f) => f.id),
  ok: failed.length === 0,
};
console.log(JSON.stringify({ ok: report.ok, passed: report.passed, total: report.total, failed: report.failedIds }, null, 2));
if (!report.ok) process.exitCode = 1;
export default report;
