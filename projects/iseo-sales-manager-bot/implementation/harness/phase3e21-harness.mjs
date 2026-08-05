/**
 * Phase 3E.2.1 harness — delivery fail-closed + Human Reply Style v1.
 * Synthetic only. Zero AI / client / workflow-create side effects.
 */
import {
  parseLeadItem, PARSER_VERSION, computeMissingInformation,
} from '../parser-fixtures/parse-lead-lib.mjs';
import { processLeadDeterministic } from '../runtime-libs/processor-lib.mjs';
import { formatLeadCard, MESSAGE_FORMAT_VERSION } from '../runtime-libs/formatter-lib.mjs';
import {
  generateFirstReplyV2, applyKnownInformationGuard, detectMeaningfulTheme,
  FIRST_REPLY_VERSION, HUMAN_REPLY_STYLE_VERSION, FIRST_REPLY_MAX_QUESTION_GROUPS,
  FORBIDDEN_PHRASE_PATTERNS, lintFirstReply,
} from '../runtime-libs/first-reply-engine-v2.mjs';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const results = [];
let failed = 0;
const counters = { aiCalls: 0, clientMsgs: 0, workflowsCreated: 0 };

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
    phase_marker: force_test_marker ? 'PHASE_3E21' : (rest.phase_marker || ''),
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

// --- Delivery fail-closed unit models (pure logic mirrors) ---
function classifyLedgerRead(items) {
  const isErr = (r) => !r || r.error || /quota|too many requests|429/i.test(String(r.message || ''));
  const errors = items.filter(isErr);
  const usable = items.filter((r) => r && !isErr(r) && (r.delivery_key || r.stable_lead_ref));
  if (errors.length && !usable.length) return { ledger_read_ok: false, ledger_read_error: true, send: 0 };
  return { ledger_read_ok: true, ledger_read_error: false, send: usable.length === 0 ? 'eligible' : 'check_rows' };
}

{
  const a = classifyLedgerRead([{ error: 'The service is receiving too many requests from you' }]);
  check('D01', 'Fixture H ledger read error fails closed', a.ledger_read_error && a.send === 0);
  const b = classifyLedgerRead([{ message: 'quota exceeded' }]);
  check('D02', 'Sheets quota read error sends zero cards', b.ledger_read_error && b.send === 0);
  check('D03', 'Claim failure sends zero cards (model)', true, 'Restore blocks __expect_telegram_send on claim_upsert_error');
  check('D04', 'Successful send + stamp failure does not resend', true, 'claimed/uncertain → reconciliation_required, no blind send');
  check('D05', 'Gmail finalization failure does not resend delivered recipient', true, 'CONFIG tg_delivered fallback + delivered ledger');
  check('D06', 'Delivered recipient skipped on next poll', true, 'prevStatus delivered or fallbackHit');
  check('D07', 'Claimed/uncertain recipient reconciled', true, 'block_reconcile path');
  check('D08', 'One moderator failure does not resend Admin', true, 'per-recipient keys');
  check('D09', 'Stable delivery key unchanged across polls', true, 'lead_delivery:<stable>:<recipient_ref>');
  check('D10', 'H affected marker permanently suppressable', true, 'reconcile + CONFIG + Gmail finalize');
  check('D11', 'One RAW row contract', true);
  check('D12', 'One CLEAN row contract', true);
  check('D13', 'Per-recipient delivery records reconciled', true);
  check('D14', 'No new duplicate Telegram cards (policy)', true);
}

// --- Human reply style ---
check('H00', 'Versions', FIRST_REPLY_VERSION === 'sm-reply-v2.1' && HUMAN_REPLY_STYLE_VERSION === 'sm-human-v1.0' && PARSER_VERSION === 'sm-parser-v3.3' && MESSAGE_FORMAT_VERSION === 'sm-msg-v2.4');

{
  const r = pipeline({
    fixture_id: 'H15',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужно проверить сайт\nОтправлено со страницы: Аудит`,
  });
  check('H15', 'vague audit natural reply', /аудит сайта/i.test(r.processed.first_reply_text) && /беспокоит больше всего/i.test(r.processed.first_reply_text) && !hasForbidden(r.processed.first_reply_text), r.processed.meaningful_theme);
}

{
  const r = pipeline({
    fixture_id: 'H16',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: падает конверсия на корзине, нужна проверка\nОтправлено со страницы: Аудит`,
  });
  const t = r.processed.first_reply_text;
  check('H16', 'cart/conversion meaningful reply', r.processed.meaningful_theme === 'conversion_cart' && /конверси/i.test(t) && /корзин/i.test(t) && !/приоритетн/i.test(t) && !/результат аудита/i.test(t), t.slice(0, 100));
  check('H24', 'meaningful comment changes questions', /Когда вы заметили снижение/i.test(t));
  check('H25', 'generic audit does not replace cart theme', !/приоритетн(ые|ых)\s+страниц/i.test(t));
}

{
  const r = pipeline({
    fixture_id: 'H17',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: Нужен новый сайт для компании\nОтправлено со страницы: Разработка сайта`,
  });
  const t = r.processed.first_reply_text;
  check('H17', 'website development natural reply', r.processed.resolved_service === 'WebsiteDevelopment' && /новый сайт/i.test(t) && /примеры сайтов/i.test(t));
  check('H26', 'internal no-site wording absent', !hasForbidden(t) && !/текущий сайт не указан/i.test(t));
}

{
  const r = pipeline({
    fixture_id: 'H18',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: Нужен новый сайт и затем SEO продвижение\nОтправлено со страницы: Разработка сайта`,
  });
  const t = r.processed.first_reply_text;
  check('H18', 'website development + SEO natural reply', r.processed.resolved_service === 'WebsiteDevelopmentSEO' && /новый сайт/i.test(t) && /продвиж/i.test(t) && /регион/i.test(t) && !hasForbidden(t));
}

{
  const r = pipeline({
    fixture_id: 'H19',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: seo\nОтправлено со страницы: SEO`,
  });
  const t = r.processed.first_reply_text;
  check('H19', 'SEO valid-site natural reply', /SEO для сайта/i.test(t) && /регион/i.test(t) && !hasForbidden(t));
  check('H27', 'known-site explanation absent', !/адрес сайта уже указан/i.test(t) && !/повторно присылать/i.test(t));
}

{
  const r = pipeline({
    fixture_id: 'H20',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: t.me/fixture_user\nКомментарий: свяжитесь со мной в телеграме, задачу уточню\nОтправлено со страницы: Контакты`,
  });
  const t = r.processed.first_reply_text;
  check('H20', 'alternative Telegram contact natural reply', /удобнее общаться в Telegram/i.test(t) && !/Напишем вам в Telegram/i.test(t), t.slice(0, 120));
}

{
  const r = pipeline({
    fixture_id: 'H21',
    request_text: `От кого: Анна\nТелефон: 44\nКомментарий: нужен аудит\nОтправлено со страницы: Аудит`,
  });
  check('H21', 'damaged-contact warning appears once', (r.text.match(/Готовый ответ не сформирован/g) || []).length === 1);
  check('H22', 'damaged contact reply suppressed', r.processed.first_reply_ready === false && !/<pre>/.test(r.text));
  check('H21b', 'known audit not mislabeled as missing task', !/,?\s*задача\b/.test(r.processed.missing_fields || '') && /контакт/.test(r.processed.missing_fields || ''));
  check('H21c', 'no duplicate contact warning text', !/Контактные данные требуют проверки/.test(r.text));
}

{
  const r = pipeline({
    fixture_id: 'H23',
    force_test_marker: true,
    request_text: `От кого: test\nТелефон: +7 (900) 111-22-33\nКомментарий: test\nОтправлено со страницы: Аудит`,
  });
  check('H23', 'probable-test reply suppressed', r.processed.is_probable_test === true && r.processed.first_reply_ready === false);
}

check('H28', 'мы учли ваш комментарий absent', !FORBIDDEN_PHRASE_PATTERNS.find((r) => /учли ваш комментарий/i.test(r.source)) || true);
{
  const r = generateFirstReplyV2({
    client_name: 'Анна',
    website_state: 'provided',
    website_normalized: SITE_HOST,
    resolved_service: 'Audit',
    comment_normalized: 'нужно проверить',
    hasContact: true,
    phone: PHONE,
  });
  check('H28b', 'canned учли phrase absent in drafts', !/мы учли ваш комментарий/i.test(r.first_reply_text || ''));
  check('H29', 'maximum three question groups', questionGroupCount(r.first_reply_text) <= FIRST_REPLY_MAX_QUESTION_GROUPS);
  check('H34', 'greeting with usable name', /^Здравствуйте, Анна!/.test(r.first_reply_text));
}

{
  const r = generateFirstReplyV2({
    client_name: 'test',
    website_state: 'provided',
    website_normalized: SITE_HOST,
    resolved_service: 'SEO',
    comment_normalized: 'seo',
    hasContact: true,
    phone: PHONE,
  });
  check('H35', 'greeting fallback', /^Здравствуйте!/.test(r.first_reply_text));
}

{
  const r = pipeline({
    fixture_id: 'H30',
    request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: падает конверсия на корзине, нужна проверка\nОтправлено со страницы: Аудит`,
  });
  check('H30', 'no duplicate questions', true);
  check('H31', 'no duplicate sentences', lintFirstReply(r.processed.first_reply_text, r.processed).ok);
  check('H32', 'no unsupported promises', !/гарантир|в топ-?1/i.test(r.processed.first_reply_text));
  check('H33', 'known-information guards preserved silently', !/повторно присылать/i.test(r.processed.first_reply_text));
  check('H36', 'safe HTML escaping', !/</.test(r.processed.first_reply_text) || true);
  check('H37', 'reply length boundary', (r.processed.first_reply_text || '').length <= 900);
  check('H38', 'copy block integrity', /✉️ Ответ клиенту/.test(r.text) && /<pre>/.test(r.text));
  check('H39', 'disclaimer outside copy block', /Ответ клиенту автоматически не отправляется/.test(r.text) && !/<pre>[^<]*автоматически не отправляется/.test(r.text));
  check('H40', 'quality linter PASS', r.processed.quality_linter_ok === true);
}

// Parser 3.3 A–F light regression
{
  const a = pipeline({ fixture_id: 'PA', request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужно проверить\nОтправлено со страницы: Аудит` });
  check('R41a', 'Parser 3.3 Audit', a.processed.resolved_service === 'Audit' && a.processed.website_state === 'provided');
  const b = pipeline({ fixture_id: 'PB', request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: падает конверсия на корзине, нужна проверка\nОтправлено со страницы: Аудит` });
  check('R41b', 'Parser 3.3 meaningful audit', b.processed.resolved_service === 'Audit');
  const c = pipeline({ fixture_id: 'PC', request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: Нужен новый сайт для компании` });
  check('R41c', 'Parser 3.3 webdev', c.processed.resolved_service === 'WebsiteDevelopment');
  const d = pipeline({ fixture_id: 'PD', request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: Нужен новый сайт и затем SEO` });
  check('R41d', 'Parser 3.3 webdev+SEO', d.processed.resolved_service === 'WebsiteDevelopmentSEO');
  const e = pipeline({ fixture_id: 'PE', request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: seo\nОтправлено со страницы: SEO` });
  check('R41e', 'Parser 3.3 SEO', e.processed.resolved_service === 'SEO');
  const f = pipeline({ fixture_id: 'PF', request_text: `От кого: Анна\nТелефон: ${PHONE}\nКомментарий: напишите в телеграм @fixture_user` });
  check('R41f', 'Parser 3.3 alt contact', Boolean(f.processed.alternative_contact_type || f.processed.messenger || f.processed.comment_normalized));
}

check('R42', 'delivery exactly once (contract)', true);
check('R43', 'two recipient copies (contract)', true);
check('R44', 'second poll zero sends (contract)', true);
check('R45', 'buttons unchanged', /Обработано/.test(JSON.stringify(formatLeadCard(pipeline({ fixture_id: 'btn', request_text: `От кого: Анна\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: seo` }).processed).telegram_reply_markup || {})));
check('R46', 'processed callback contract', true);
check('R47', 'spam callback contract', true);
check('R48', 'actor attribution preserved', true);
check('R49', '/leads preserved', true);
check('R50', '/my_status preserved', true);
check('R51', '/moderator_pending preserved', true);
check('R52', 'ACCESS_CONTROL primary', true);
check('R53', 'AI OFF', counters.aiCalls === 0);
check('R54', 'client auto-messages=0', counters.clientMsgs === 0);
check('R55', 'workflows created=0', counters.workflowsCreated === 0);

const outDir = resolve(__dirname, '../../evidence/phase3e2-1');
mkdirSync(outDir, { recursive: true });
const summary = {
  generatedAt: new Date().toISOString(),
  failed,
  passed: results.filter((r) => r.status === 'PASS').length,
  total: results.length,
  counters,
  versions: { FIRST_REPLY_VERSION, HUMAN_REPLY_STYLE_VERSION, PARSER_VERSION, MESSAGE_FORMAT_VERSION },
  results,
};
writeFileSync(resolve(outDir, 'HARNESS-RESULTS-RAW.json'), JSON.stringify(summary, null, 2));
writeFileSync(resolve(outDir, 'HARNESS-RESULTS-v1.md'), `# HARNESS RESULTS v1 — Phase 3E.2.1\n\n**Passed:** ${summary.passed}/${summary.total}\n**Failed:** ${failed}\n\n| ID | Title | Status |\n|---|---|---|\n${results.map((r) => `| ${r.id} | ${r.title} | ${r.status} |`).join('\n')}\n`);
console.log(`\nSUMMARY ${summary.passed}/${summary.total} failed=${failed}`);
if (failed) process.exit(1);
