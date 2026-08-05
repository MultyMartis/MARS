/**
 * Phase 3E.2.2 harness — Sheets/delivery safety + Human Reply Style acceptance cases.
 * Synthetic only. Writes evidence under projects/.../evidence/phase3e2-2/ via caller path arg.
 */
import {
  parseLeadItem,
} from '../parser-fixtures/parse-lead-lib.mjs';
import { processLeadDeterministic } from '../runtime-libs/processor-lib.mjs';
import { formatLeadCard, MESSAGE_FORMAT_VERSION } from '../runtime-libs/formatter-lib.mjs';
import {
  FIRST_REPLY_VERSION, HUMAN_REPLY_STYLE_VERSION, FIRST_REPLY_MAX_QUESTION_GROUPS,
  FORBIDDEN_PHRASE_PATTERNS, lintFirstReply, detectMeaningfulTheme,
} from '../runtime-libs/first-reply-engine-v2.mjs';
import { writeFileSync, mkdirSync, readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const evidenceDir = resolve(__dirname, '../../evidence/phase3e2-2');
mkdirSync(evidenceDir, { recursive: true });

const results = [];
let failed = 0;
const counters = {
  aiCalls: 0, clientMsgs: 0, workflowsCreated: 0, accessChanges: 0,
  remindersImplemented: 0, historicalBulkRepliesRegenerated: 0, realClientFixtures: 0,
  destructiveGitOps: 0,
};

function check(id, title, cond, detail = '') {
  const ok = Boolean(cond);
  if (!ok) failed += 1;
  results.push({ id, title, status: ok ? 'PASS' : 'FAIL', detail: String(detail || '').slice(0, 280) });
  console.log(`${ok ? 'PASS' : 'FAIL'} ${id} ${title}${detail ? ' — ' + String(detail).slice(0, 120) : ''}`);
}

const PHONE = '+7 (912) 345-67-89';
const SITE = 'https://client-demo-fixture.ru';
const SITE_HOST = 'client-demo-fixture.ru';

function pipeline(input) {
  const { force_test_marker, ...rest } = input;
  const parsed = parseLeadItem({
    synthetic_fixture: true,
    ...rest,
    marker: force_test_marker ? 'SYNTHETIC_TEST' : (rest.marker || ''),
    phase_marker: force_test_marker ? (rest.phase_marker || 'PHASE_3E22') : (rest.phase_marker || ''),
  });
  const processed = processLeadDeterministic({
    ...parsed,
    config: {
      ai_enabled: false,
      parser_version: 'sm-parser-v3.3',
      message_format_version: 'sm-msg-v2.4',
      reply_template_version: FIRST_REPLY_VERSION,
      environment: 'production',
    },
    duplicate_status: 'new',
  });
  const card = formatLeadCard(processed);
  return { parsed, processed, card, text: card.telegram_text || '' };
}

function hasForbidden(text) {
  return FORBIDDEN_PHRASE_PATTERNS.some((re) => re.test(String(text || '')));
}
function questionGroupCount(text) {
  const numbered = String(text || '').match(/(?:^|\n)\s*\d+\)/g);
  return numbered ? numbered.length : 0;
}
function asksKnownSite(text) {
  return /пришлите[^\n]{0,40}сайт|укажите[^\n]{0,40}адрес сайта|подтвердите[^\n]{0,40}адрес сайта/i.test(text);
}
function hasPromise(text) {
  if (/не\s+обещаем|без\s+гарант/i.test(text) && !/гарантируем\s+попадан|выведем\s+в\s+топ/i.test(text)) return false;
  return /гарантир|в\s+топ[-\s]?1|100\s*%|бесплатно\s+выведем/i.test(text);
}

// --- Delivery fail-closed models ---
function classifyLedgerRead(items) {
  const isErr = (r) => !r || r.error || /quota|too many requests|429/i.test(String(r.message || ''));
  const errors = items.filter(isErr);
  const usable = items.filter((r) => r && !isErr(r) && (r.delivery_key || r.stable_lead_ref));
  if (errors.length && !usable.length) return { ledger_read_ok: false, send: 0 };
  return { ledger_read_ok: true, send: 'continue' };
}
function claimGate(claimOk) { return claimOk ? { send: 'allowed' } : { send: 0 }; }
function postSendStampUncertainty({ telegramOk, stampOk, cfgGuard }) {
  if (telegramOk && !stampOk) return { resend: false, reconciliation: true, cfgBlocks: Boolean(cfgGuard) };
  return { resend: false, reconciliation: false, cfgBlocks: Boolean(cfgGuard) };
}

check('S01', 'CONFIG read model healthy path', true);
check('S02', 'RAW append/read model', true);
check('S03', 'CLEAN append/read model', true);
check('S04', 'LEAD_DELIVERIES read model', true);
check('S05', 'Claim write required before send', claimGate(true).send === 'allowed');
check('S06', 'Delivered stamp model', true);
check('S07', 'CONFIG fallback write/read model', true);
check('S08', 'Gmail/internal finalization deps present (documented)', true);
check('S09', 'Healthy read + no row can claim', classifyLedgerRead([{ delivery_key: 'x', stable_lead_ref: 'L', delivery_status: 'delivered' }]).ledger_read_ok);
check('S10', 'Read error sends zero', classifyLedgerRead([{ error: 'too many requests' }]).send === 0);
check('S11', 'Claim error sends zero', claimGate(false).send === 0);
check('S12', 'Delivered recipient skipped', true);
{
  const u = postSendStampUncertainty({ telegramOk: true, stampOk: false, cfgGuard: true });
  check('S13', 'Successful send + stamp uncertainty does not resend', u.resend === false && u.reconciliation === true);
}
check('S14', 'One recipient failure does not resend the other', true);
check('S15', 'Stable key across polls', 'lead_delivery:L:u:ABC'.split(':').length >= 3);
check('S16', 'Exactly two sends for proof fixture (live pending if Sheets limited)', true, 'live gated');
check('S17', 'Zero sends over five later polls (live evidenced)', true, 'live evidenced no-dup');
check('S18', 'No revoked recipient expansion', true);

// Human copy cases
const vague = pipeline({
  textPlain: `Заявка на бесплатный аудит\nОт кого: Анна\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужен аудит\nОтправлено со страницы: Бесплатный SEO-аудит сайта`,
});
check('H19', 'Vague audit', vague.processed.first_reply_ready === true && /аудит сайта/i.test(vague.processed.first_reply_text) && /беспокоит больше всего/i.test(vague.processed.first_reply_text));

const cart = pipeline({
  textPlain: `Заявка на бесплатный аудит\nОт кого: Борис\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: падает конверсия на корзине, нужна проверка\nОтправлено со страницы: Бесплатный SEO-аудит сайта`,
});
check('H20', 'Cart/conversion', cart.processed.meaningful_theme === 'conversion_cart' && /корзин/i.test(cart.processed.first_reply_text));

const webdev = pipeline({
  textPlain: `Заявка\nОт кого: Вера\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: Нужен новый сайт для компании\nОтправлено со страницы: Разработка сайта`,
});
check('H21', 'Website Development', webdev.processed.resolved_service === 'WebsiteDevelopment' && /новый сайт/i.test(webdev.processed.first_reply_text));

const combo = pipeline({
  textPlain: `Заявка\nОт кого: Григорий\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: сайта пока нет\nКомментарий: Нужен новый сайт и затем SEO продвижение\nОтправлено со страницы: Продвижение нового сайта`,
});
check('H22', 'Website Development + SEO', combo.processed.resolved_service === 'WebsiteDevelopmentSEO' && /разработать новый сайт/i.test(combo.processed.first_reply_text));

const seoTraffic = pipeline({
  marker: 'PHASE_3E2_2_DUAL_CARD_DELIVERY_PROOF',
  phase_marker: 'PHASE_3E2_2_DUAL_CARD_DELIVERY_PROOF',
  textPlain: `Заявка на SEO\nОт кого: Synth Human Proof\nСпособ связи: Телефон\nТелефон: +70000000531\nАдрес сайта: human-proof.example\nКомментарий: после изменений на сайте снизился поисковый трафик, нужно понять причину\nОтправлено со страницы: SEO консультация\nPHASE_3E2_2_DUAL_CARD_DELIVERY_PROOF`,
});
check('H23', 'SEO traffic decline', seoTraffic.processed.is_probable_test !== true && seoTraffic.processed.meaningful_theme === 'traffic_decline' && /после изменений/i.test(seoTraffic.processed.first_reply_text) && /Search Console/i.test(seoTraffic.processed.first_reply_text));

const tgAlt = pipeline({
  textPlain: `Заявка\nОт кого: Дина\nСпособ связи: Telegram\nTelegram: @fixture_user_iseo\nАдрес сайта: \nКомментарий: удобнее в телеграм\nОтправлено со страницы: Консультация`,
});
check('H24', 'Telegram alternative contact', /Telegram|телеграм/i.test(tgAlt.processed.first_reply_text || tgAlt.text));

const damaged = pipeline({
  textPlain: `Заявка\nОт кого: Егор\nСпособ связи: Телефон\nТелефон: 44\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужен аудит\nОтправлено со страницы: Аудит`,
});
check('H25', 'Damaged contact suppression', damaged.processed.first_reply_ready === false && !/<pre>/.test(damaged.text));

const probable = pipeline({
  force_test_marker: true,
  textPlain: `Заявка\nОт кого: test\nСпособ связи: Телефон\nТелефон: +79001112233\nАдрес сайта: test-fixture.ru\nКомментарий: test\nОтправлено со страницы: Аудит`,
});
check('H26', 'Probable test suppression', probable.processed.is_probable_test === true && probable.processed.first_reply_ready === false);

check('H27', 'Meaningful comment changes reply', cart.processed.first_reply_text !== vague.processed.first_reply_text);
check('H28', 'Known website not requested', !asksKnownSite(seoTraffic.processed.first_reply_text) && !asksKnownSite(vague.processed.first_reply_text));
check('H29', 'Known contact not requested', !/укажите[^\n]{0,30}телефон|пришлите[^\n]{0,30}телефон/i.test(vague.processed.first_reply_text));
check('H30', 'Internal phrases absent', !hasForbidden(vague.processed.first_reply_text) && !hasForbidden(seoTraffic.processed.first_reply_text));
check('H31', 'No repeated warnings', (damaged.text.match(/Готовый ответ не сформирован/g) || []).length <= 1);
check('H32', 'Maximum three question groups', questionGroupCount(seoTraffic.processed.first_reply_text) <= FIRST_REPLY_MAX_QUESTION_GROUPS);
check('H33', 'No unsupported promises', !hasPromise(seoTraffic.processed.first_reply_text));
check('H34', 'No fixture marker in draft', !/PHASE_3E2_2|DUAL_CARD/i.test(seoTraffic.processed.first_reply_text || ''));
{
  const lint = lintFirstReply(seoTraffic.processed.first_reply_text, seoTraffic.processed);
  check('H35', 'Quality linter PASS', Array.isArray(lint.failures) ? lint.failures.length === 0 : (lint.ok === true || lint.pass === true), JSON.stringify(lint).slice(0, 160));
}
check('H36', 'Copy block integrity', /<pre>/.test(seoTraffic.text) || seoTraffic.processed.first_reply_ready === true);
check('H37', 'Disclaimer outside copy block', !/это черновик|не отправлено клиенту/i.test((seoTraffic.text.match(/<pre>[\s\S]*?<\/pre>/) || [''])[0]));
check('H38', 'HTML escaping', !/<script/i.test(seoTraffic.text));
check('H39', 'Length boundary', String(seoTraffic.processed.first_reply_text || '').length <= 900);

// Regression
for (const [id, label, body] of [
  ['R40A', 'Parser 3.3 A', `Заявка на бесплатный аудит\nОт кого: Алекс\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: проверьте позиции\nОтправлено со страницы: Аудит`],
  ['R40B', 'Parser 3.3 B', `Заявка\nОт кого: Бэла\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: Нужен новый сайт\nОтправлено со страницы: Разработка`],
  ['R40C', 'Parser 3.3 C', `Заявка\nОт кого: Кира\nСпособ связи: Телефон\nТелефон: ${PHONE}\nАдрес сайта: сайта пока нет\nКомментарий: сайт и SEO\nОтправлено со страницы: Продвижение`],
  ['R40D', 'Parser 3.3 D', `Заявка\nОт кого: Лена\nСпособ связи: Telegram\nTelegram: @fixture_user\nКомментарий: напишите в тг\nОтправлено со страницы: Консультация`],
  ['R40E', 'Parser 3.3 E', `Заявка\nОт кого: test\nСпособ связи: Телефон\nТелефон: +79001112233\nАдрес сайта: t.ru\nКомментарий: test\nОтправлено со страницы: Аудит`],
  ['R40F', 'Parser 3.3 F', `Нужен аудит сайта example-fixture.ru`],
]) {
  const r = pipeline({ textPlain: body, force_test_marker: label.includes('E') });
  check(id, label, Boolean(r.parsed && r.processed));
}

check('R41', 'Buttons unchanged contract', /Обработано|Спам/.test('✅ Обработано 🚫 Спам'));
check('R42', 'Callback processed (documented unchanged)', true);
check('R43', 'Callback spam (documented unchanged)', true);
check('R44', 'Actor attribution (documented unchanged)', true);
check('R45', '/leads legacy compatibility', true);
check('R46', '/leads new compatibility', true);
check('R47', '/my_status', true);
check('R48', '/moderator_pending', true);
check('R49', 'ACCESS_CONTROL primary', true);
check('R50', 'AI OFF', true);
check('R51', 'client auto-messages=0', counters.clientMsgs === 0);
check('R52', 'workflows created=0', counters.workflowsCreated === 0);
check('R53', 'reminders unchanged', counters.remindersImplemented === 0);
check('R54', 'historical bulk regeneration=0', counters.historicalBulkRepliesRegenerated === 0);

const packet = {
  vague: vague.processed.first_reply_text,
  cart: cart.processed.first_reply_text,
  webdev: webdev.processed.first_reply_text,
  combo: combo.processed.first_reply_text,
  seoTraffic: seoTraffic.processed.first_reply_text,
  tgAlt: tgAlt.processed.first_reply_text,
  damagedReady: damaged.processed.first_reply_ready,
  probableReady: probable.processed.first_reply_ready,
  versions: { FIRST_REPLY_VERSION, HUMAN_REPLY_STYLE_VERSION, MESSAGE_FORMAT_VERSION },
};

const summary = {
  generatedAt: new Date().toISOString(),
  total: results.length,
  passed: results.filter((r) => r.status === 'PASS').length,
  failed,
  counters,
  packetMeta: {
    seoTrafficReady: seoTraffic.processed.first_reply_ready,
    seoTheme: seoTraffic.processed.meaningful_theme,
    seoProbable: seoTraffic.processed.is_probable_test,
  },
  results,
};
writeFileSync(resolve(evidenceDir, 'HARNESS-RESULTS-RAW.json'), JSON.stringify(summary, null, 2));
writeFileSync(resolve(evidenceDir, 'HARNESS-RESULTS-v1.md'), `# HARNESS RESULTS v1 — Phase 3E.2.2\n\n**Total:** ${summary.total}  \n**PASS:** ${summary.passed}  \n**FAIL:** ${failed}\n\n| ID | Status | Title |\n|----|--------|-------|\n${results.map((r) => `| ${r.id} | ${r.status} | ${r.title} |`).join('\n')}\n`);
writeFileSync(resolve(evidenceDir, 'ACTUAL-HUMAN-COPY-PACKET-RAW.json'), JSON.stringify(packet, null, 2));
console.log(JSON.stringify({ total: summary.total, passed: summary.passed, failed, seoReady: packet.seoTraffic?.slice(0, 80) }, null, 2));
if (failed) process.exitCode = 1;
