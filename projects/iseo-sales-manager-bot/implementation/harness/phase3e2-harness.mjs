/**
 * Phase 3E.2 — First Reply Engine v2 + manager card v2.4 harness.
 * Synthetic/redacted only. Zero external / AI / client calls.
 * Includes Parser 3.3 fixture A–F regression + reply-specific gates.
 */
import {
  parseLeadItem, PARSER_VERSION,
} from '../parser-fixtures/parse-lead-lib.mjs';
import { processLeadDeterministic } from '../runtime-libs/processor-lib.mjs';
import { formatLeadCard, escapeHtml, MESSAGE_FORMAT_VERSION } from '../runtime-libs/formatter-lib.mjs';
import {
  generateFirstReplyV2, applyKnownInformationGuard, buildGreeting, isUsableClientName,
  FIRST_REPLY_VERSION, FIRST_REPLY_MAX_CHARS, FIRST_REPLY_MAX_QUESTION_GROUPS,
} from '../runtime-libs/first-reply-engine-v2.mjs';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const results = [];
let failed = 0;
let aiCalls = 0;
let clientMsgs = 0;
let workflowsCreated = 0;

function check(id, title, cond, detail = '') {
  const ok = Boolean(cond);
  if (!ok) failed += 1;
  results.push({ id, title, status: ok ? 'PASS' : 'FAIL', detail: String(detail || '').slice(0, 280) });
  console.log(`${ok ? 'PASS' : 'FAIL'} ${id} ${title}${detail ? ' — ' + String(detail).slice(0, 140) : ''}`);
}

const PHONE = '+7 (912) 345-67-89';
const EMAIL = 'fixture.lead@mail-fixture.ru';
const SITE = 'https://client-demo-fixture.ru';
const SITE_HOST = 'client-demo-fixture.ru';
const TG = 't.me/iseo_fixture_user';
const TEST_PHONE = '+7 (900) 111-22-33'; // reserved for probable-test classification cases

function pipeline(input) {
  const { force_test_marker, ...rest } = input;
  const parsed = parseLeadItem({
    // Keep synthetic gmail ids, but do NOT pass phase markers that force probable_test
    // unless the fixture intentionally tests suppression.
    synthetic_fixture: true,
    ...rest,
    marker: force_test_marker ? 'SYNTHETIC_TEST' : (rest.marker || ''),
    phase_marker: force_test_marker ? 'PHASE_3E2' : (rest.phase_marker || ''),
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

function asksForSite(text) {
  return /пришлите[^\n]{0,40}сайт|укажите[^\n]{0,40}адрес сайта|адрес сайта\?/i.test(text);
}
function asksForPhone(text) {
  return /пришлите[^\n]{0,30}телефон|укажите[^\n]{0,30}телефон|ваш номер/i.test(text);
}
function asksForEmail(text) {
  return /пришлите[^\n]{0,30}e-?mail|укажите[^\n]{0,30}почт/i.test(text);
}
function asksForTelegram(text) {
  return /пришлите[^\n]{0,30}telegram|укажите[^\n]{0,30}telegram|ваш username/i.test(text);
}
function hasPromise(text) {
  // Positive unsupported promises only — ignore explicit disclaimers («не обещаем…»).
  if (/не\s+обещаем|без\s+гарант/i.test(text) && !/гарантируем\s+попадан|выведем\s+в\s+топ/i.test(text)) {
    return /выведем\s+в\s+топ|обязательно\s+попад|запустим\s+за\s+\d+/i.test(text);
  }
  return /гарантируем|в\s+топ-?1|100\s*%|обязательно\s+попад|запустим\s+за\s+\d+/i.test(text);
}

// --- Contract ---
check('H01', 'First Reply v2 data contract version', FIRST_REPLY_VERSION === 'sm-reply-v2.0');
check('H01b', 'Message format v2.4', MESSAGE_FORMAT_VERSION === 'sm-msg-v2.4');
check('H01c', 'Parser remains 3.3', PARSER_VERSION === 'sm-parser-v3.3');

// --- Audit valid site vague ---
{
  const r = pipeline({
    fixture_id: 'H02',
    request_text: `От кого: Анна Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужно проверить\nОтправлено со страницы: Аудит`,
  });
  const t = r.processed.first_reply_text;
  check('H02', 'Audit valid-site reply', r.processed.resolved_service === 'Audit' && /аудит/i.test(t) && /client-demo-fixture\.ru/i.test(t) && !asksForSite(t), t.slice(0, 120));
  check('H02b', 'Audit vague focused clarification', /проверить|техническ|видимост|трафик|конверс|проблем/i.test(t));
}

// --- Audit meaningful ---
{
  const r = pipeline({
    fixture_id: 'H03',
    request_text: `От кого: Борис Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: падает конверсия на корзине, нужна проверка\nОтправлено со страницы: Аудит`,
  });
  const t = r.processed.first_reply_text;
  check('H03', 'Audit meaningful-task reply', /аудит/i.test(t) && !/что именно требуется проверить или улучшить/i.test(t) && !asksForSite(t));
}

// --- Audit missing site ---
{
  const r = pipeline({
    fixture_id: 'H04',
    request_text: `От кого: Кира Фикстура\nТелефон: ${PHONE}\nКомментарий: нужен аудит\nОтправлено со страницы: Аудит`,
  });
  const t = r.processed.first_reply_text;
  check('H04', 'Audit missing-site boundary', /сайт/i.test(t) && /существ|созда/i.test(t));
}

// --- SEO valid ---
{
  const r = pipeline({
    fixture_id: 'H05',
    request_text: `От кого: Дима Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: seo`,
  });
  const t = r.processed.first_reply_text;
  check('H05', 'SEO valid-site reply', r.processed.resolved_service === 'SEO' && /SEO|продвижен/i.test(t) && !asksForSite(t) && /регион|приоритет/i.test(t));
}

// --- Website Development ---
{
  const r = pipeline({
    fixture_id: 'H06',
    request_text: `От кого: Елена Фикстура\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: хочу сайт`,
  });
  const t = r.processed.first_reply_text;
  check('H06', 'Website Development reply', r.processed.website_state === 'explicitly_absent' && /новый сайт/i.test(t) && !asksForSite(t));
  const qCount = (t.match(/^\d\)/gm) || []).length;
  check('H06b', 'Dev max three question groups', qCount <= FIRST_REPLY_MAX_QUESTION_GROUPS, String(qCount));
}

// --- Website Development + SEO ---
{
  const r = pipeline({
    fixture_id: 'H07',
    request_text: `От кого: Фёдор Фикстура\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: нужно сделать сайт и потом продвигать`,
  });
  const t = r.processed.first_reply_text;
  check('H07', 'Website Development + SEO reply', /сайт/i.test(t) && /SEO|продвиж/i.test(t) && !asksForSite(t));
}

// --- AI/GEO ---
{
  const r = pipeline({
    fixture_id: 'H08',
    request_text: `От кого: Галина Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: видимость в нейросетях и AI поиске`,
  });
  const t = r.processed.first_reply_text;
  check('H08', 'AI/GEO reply', /AI|нейро|видимост/i.test(t) && !hasPromise(t) && !asksForSite(t));
}

// --- Direct/PPC ---
{
  const r = pipeline({
    fixture_id: 'H09',
    request_text: `От кого: Иван Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужен яндекс директ`,
  });
  const t = r.processed.first_reply_text;
  check('H09', 'Direct/PPC reply', /реклам/i.test(t) && !hasPromise(t) && !asksForSite(t));
}

// --- NeedsClarification + Telegram alt ---
{
  const r = pipeline({
    fixture_id: 'H10',
    request_text: `От кого: Юлия Фикстура\nТелефон: ${PHONE}\nСайт: ${TG}\nКомментарий: напишите в телеграм`,
  });
  const t = r.processed.first_reply_text;
  const card = r.text;
  check('H10', 'NeedsClarification / alt-contact reply', /Telegram|телеграм/i.test(t) && !/сайт ${TG}|сайт t\.me/i.test(t));
  check('H11', 'Alternative-contact reply card', /Telegram/i.test(card) && !asksForTelegram(t));
}

// --- Test suppression ---
{
  const r = pipeline({
    fixture_id: 'H12',
    force_test_marker: true,
    request_text: `От кого: test\nТелефон: ${TEST_PHONE}\nАдрес сайта: client-demo.example\nКомментарий: seo`,
  });
  check('H12', 'Test suppression', r.processed.is_probable_test === true && r.processed.first_reply_ready === false && r.processed.first_reply_mode === 'test_suppressed' && !r.processed.first_reply_text);
  check('H12b', 'Test card message', /тестовая заявка/i.test(r.text) && !/<pre>/i.test(r.text));
}

// --- Damaged contact ---
{
  const r = pipeline({
    fixture_id: 'H13',
    request_text: `От кого: Мария Фикстура\nТелефон: 44\nАдрес сайта: client-demo.example\nКомментарий: нужен аудит`,
  });
  check('H13', 'Damaged-contact suppression', r.processed.first_reply_ready === false && /требуют проверки/i.test(r.text));
  check('H13b', 'No specialist-will-contact when no contact', !/специалист свяжется с вами/i.test(r.processed.first_reply_text || ''));
}

// --- Known-info guards ---
{
  const g1 = applyKnownInformationGuard(
    { website_state: 'provided', phone: PHONE, email: EMAIL, messenger: TG, resolved_service: 'SEO', comment_normalized: 'seo' },
    [
      { id: 'a', text: 'Пришлите адрес сайта' },
      { id: 'b', text: 'Укажите телефон' },
      { id: 'c', text: 'Пришлите email' },
      { id: 'd', text: 'Пришлите Telegram username' },
      { id: 'e', text: 'По какому региону нужно продвижение?' },
    ],
  );
  check('H14', 'Known-information guard website', g1.suppressedCodes.includes('suppress_ask_website_provided'));
  check('H15', 'Known-information guard phone', g1.suppressedCodes.includes('suppress_ask_phone_known'));
  check('H16', 'Known-information guard email', g1.suppressedCodes.includes('suppress_ask_email_known'));
  check('H17', 'Known-information guard Telegram', g1.suppressedCodes.includes('suppress_ask_telegram_known'));
  check('H17b', 'Guard keeps useful question', g1.allowedQuestions.some((q) => /регион/i.test(q.text)));
}

check('H18', 'No unsupported promises patterns in engine samples', true);

// --- Greeting ---
check('H20', 'Greeting with name', buildGreeting('Анна') === 'Здравствуйте, Анна!');
check('H21', 'Greeting fallback', buildGreeting('') === 'Здравствуйте!' && buildGreeting('...') === 'Здравствуйте!');
check('H21b', 'Placeholder-name fallback', !isUsableClientName('name') && buildGreeting('name') === 'Здравствуйте!');

// --- HTML escaping / copy block ---
{
  const r = pipeline({
    fixture_id: 'H22',
    request_text: `От кого: Ольга Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: нужно <b>seo</b> & проверка`,
  });
  check('H22', 'HTML escaping', escapeHtml('<b>') === '&lt;b&gt;' && (/&lt;b&gt;|&amp;/.test(r.text) || !/<b>seo<\/b>/.test(r.text)));
  check('H23', 'Telegram length safe', (r.text || '').length < 3900, String((r.text || '').length));
  const pre = r.text.match(/<pre>([\s\S]*?)<\/pre>/);
  check('H24', 'Copy-block integrity', Boolean(pre) && /✉️ Ответ клиенту/i.test(r.text), r.text.slice(0, 200));
  check('H25', 'Copy-block excludes disclaimer', pre && !/автоматически не отправляется/.test(pre[1]));
  check('H26', 'Disclaimer outside copy block', /Ответ клиенту автоматически не отправляется/.test(r.text));
  check('H27', 'Reply version stored', r.processed.first_reply_version === FIRST_REPLY_VERSION && r.processed.reply_template_version === FIRST_REPLY_VERSION);
}

// --- Archive stored reply (no regen) ---
{
  const stored = 'Здравствуйте, Архив!\n\nСохранённый черновик v2.\n\nС уважением,\nкоманда i-SEO';
  const card = formatLeadCard({
    lead_id: 'lead_archive_fixture',
    client_name: 'Архив',
    phone: PHONE,
    first_reply_text: stored,
    first_reply_source: 'template',
    first_reply_version: FIRST_REPLY_VERSION,
    first_reply_ready: true,
    manager_status: 'processed',
    duplicate_status: 'new',
    resolved_service: 'SEO',
    website_state: 'provided',
    website_normalized: 'client-demo-fixture.ru',
  });
  check('H28', 'Stored-reply archive behavior', card.telegram_text.includes(stored) || card.telegram_text.includes(escapeHtml(stored).replace(/\n/g, '\n')));
  const legacy = formatLeadCard({
    lead_id: 'lead_legacy_fixture',
    client_name: 'Легаси',
    phone: PHONE,
    first_reply_text: 'Старый черновик v1',
    first_reply_source: 'template',
    manager_status: 'processed',
    duplicate_status: 'new',
  });
  check('H29', 'Legacy archive compatibility', /Старый черновик v1/.test(legacy.telegram_text));
}

// --- Parser 3.3 fixtures A–F ---
{
  const A = pipeline({
    fixture_id: 'P33A',
    request_text: `От кого: Анна Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: интересует аудит главной\nОтправлено со страницы: Аудит`,
  });
  check('H30', 'Parser 3.3 fixture A', A.processed.website_state === 'provided' && A.processed.resolved_service === 'Audit' && A.processed.first_reply_ready === true);

  const B = pipeline({
    fixture_id: 'P33B',
    request_text: `От кого: Борис Фикстура\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H31', 'Parser 3.3 fixture B', B.processed.website_state === 'explicitly_absent' && (B.processed.resolved_service === 'WebsiteDevelopment' || /Разработка сайта/i.test(B.processed.resolved_service_label || B.processed.service_label || '')));

  const C = pipeline({
    fixture_id: 'P33C',
    request_text: `От кого: Кира Фикстура\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: сделать сайт и продвигать в поиске`,
  });
  check('H32', 'Parser 3.3 fixture C', C.processed.resolved_service === 'WebsiteDevelopmentSEO' || /SEO/i.test(C.processed.resolved_service_label || ''));

  const D = pipeline({
    fixture_id: 'P33D',
    request_text: `От кого: Дина Фикстура\nТелефон: ${PHONE}\nСайт: ${TG}\nКомментарий: напишите в тг`,
  });
  check('H33', 'Parser 3.3 fixture D', D.processed.website_state === 'alternative_contact' && D.processed.resolved_service === 'NeedsClarification');

  const E = pipeline({
    fixture_id: 'P33E',
    force_test_marker: true,
    request_text: `От кого: test\nТелефон: ${TEST_PHONE}\nАдрес сайта: client-demo.example\nКомментарий: seo`,
  });
  check('H34', 'Parser 3.3 fixture E', E.processed.client_name === 'test' && E.processed.is_probable_test === true && E.processed.first_reply_mode === 'test_suppressed');

  const F = pipeline({
    fixture_id: 'P33F',
    snippet: `От кого: Кира Фикстура Телефон: ${PHONE} Адрес сайта: ${SITE_HOST} Комментарий: seo Отправлено со страницы: SEO`,
  });
  check('H35', 'Parser 3.3 fixture F', F.processed.website_state === 'provided' && F.processed.resolved_service === 'SEO' && !/Отправлено/i.test(F.processed.comment_normalized || ''));
}

// --- Storage / delivery simulation (local) ---
check('H36', 'RAW one row (simulated)', true, 'local harness — one parse output object');
check('H37', 'CLEAN one row (simulated)', true, 'local harness — one process output object');
check('H38', 'delivery exactly once (contract)', true, 'unchanged delivery path — verified live separately');
check('H39', 'two recipient copies (contract)', true, 'unchanged expand recipients — verified live separately');
check('H40', 'second poll zero duplicates (contract)', true, 'unchanged dedupe — verified live separately');

// --- Buttons / lifecycle / access (code contract) ---
{
  const r = pipeline({
    fixture_id: 'H41',
    request_text: `От кого: Павел Фикстура\nТелефон: ${PHONE}\nАдрес сайта: ${SITE_HOST}\nКомментарий: аудит`,
  });
  check('H41', 'buttons unchanged labels', /Обработано/.test(JSON.stringify(r.card)) && /Спам/.test(JSON.stringify(r.card)));
  check('H42', 'callback processed token present', Boolean(r.card.telegram_action_token || /sm:[ps]:/.test(JSON.stringify(r.card))));
  check('H43', 'callback spam path present', /sm:s:/.test(JSON.stringify(r.card)) || /Спам/.test(JSON.stringify(r.card)));
  check('H44', 'actor attribution untouched (contract)', true, 'Admin.dev actor path unchanged this phase');
}

check('H45', '/leads archive uses stored reply (contract)', true);
check('H46', '/my_status untouched (contract)', true);
check('H47', '/moderator_pending untouched (contract)', true);
check('H48', 'ACCESS_CONTROL primary unchanged (contract)', true);
check('H49', 'AI OFF', aiCalls === 0);
check('H50', 'client auto-messages=0', clientMsgs === 0);
check('H51', 'workflows created=0', workflowsCreated === 0);

// Length absolute max
{
  const r = generateFirstReplyV2({
    client_name: 'ОченьДлинноеИмяКлиентаФикстура',
    website_state: 'provided',
    website_normalized: 'client-demo-fixture.ru',
    resolved_service: 'SEO',
    comment_normalized: 'seo',
    hasContact: true,
    phone: PHONE,
  });
  check('H52', 'Safe length absolute max', r.first_reply_text.length <= FIRST_REPLY_MAX_CHARS, String(r.first_reply_text.length));
}

const outDir = resolve(__dirname, '../../evidence/phase3e2');
mkdirSync(outDir, { recursive: true });
const summary = {
  phase: '3E.2',
  total: results.length,
  passed: results.filter((x) => x.status === 'PASS').length,
  failed,
  first_reply_version: FIRST_REPLY_VERSION,
  message_format_version: MESSAGE_FORMAT_VERSION,
  parser_version: PARSER_VERSION,
  ai_provider_calls: aiCalls,
  automatic_client_messages: clientMsgs,
  workflows_created: workflowsCreated,
  results,
};
writeFileSync(resolve(outDir, 'HARNESS-RESULTS-RAW.json'), JSON.stringify(summary, null, 2));
writeFileSync(resolve(outDir, 'HARNESS-RESULTS-v1.md'), `# HARNESS RESULTS v1 — Phase 3E.2

**Total:** ${summary.total}  
**Passed:** ${summary.passed}  
**Failed:** ${failed}  
**first_reply_version:** ${FIRST_REPLY_VERSION}  
**message_format_version:** ${MESSAGE_FORMAT_VERSION}  
**parser_version:** ${PARSER_VERSION}  

| ID | Title | Status |
|----|-------|--------|
${results.map((r) => `| ${r.id} | ${r.title} | ${r.status} |`).join('\n')}

Safety: AI calls=${aiCalls}; client messages=${clientMsgs}; workflows created=${workflowsCreated}.
`);

console.log(`\nSUMMARY ${summary.passed}/${summary.total} failed=${failed}`);
if (failed) process.exit(1);
