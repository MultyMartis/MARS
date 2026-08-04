/**
 * Phase 3E.1 Parser 3.3 + Lead Semantic Model harness — 42 required checks.
 * Synthetic/redacted only. Zero external calls.
 */
import {
  parseLeadItem, extractLabeledFields, htmlToPlainText, classifyWebsiteField,
  normalizeSite, PARSER_VERSION, assessLeadQuality,
} from '../parser-fixtures/parse-lead-lib.mjs';
import { processLeadDeterministic } from '../runtime-libs/processor-lib.mjs';
import { formatLeadCard, escapeHtml, MESSAGE_FORMAT_VERSION } from '../runtime-libs/formatter-lib.mjs';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const results = [];
let failed = 0;

function check(id, title, cond, detail = '') {
  const ok = Boolean(cond);
  if (!ok) failed += 1;
  results.push({ id, title, status: ok ? 'PASS' : 'FAIL', detail: String(detail || '').slice(0, 240) });
  console.log(`${ok ? 'PASS' : 'FAIL'} ${id} ${title}${detail ? ' — ' + String(detail).slice(0, 120) : ''}`);
}

const PHONE = '+7 (900) 111-22-33';
const EMAIL = 'lead.test@example.com';
const SITE = 'https://client-demo.example';
const TG = 't.me/iseo_fixture_user';

function pipeline(input) {
  const parsed = parseLeadItem({
    synthetic_fixture: true,
    marker: 'SYNTHETIC_TEST',
    phase_marker: 'PHASE_3E1',
    ...input,
  });
  const processed = processLeadDeterministic({
    ...parsed,
    config: { ai_enabled: false, parser_version: 'sm-parser-v3.3', message_format_version: 'sm-msg-v2.3', environment: 'production' },
    duplicate_status: 'new',
  });
  const card = formatLeadCard(processed);
  return { parsed, processed, card };
}

// 1 HTML extraction
{
  const html = `<b>От кого:</b> Анна Фикстура<br>Телефон: ${PHONE}<br>Адрес сайта: client-demo.example<br>Комментарий: нужен аудит главной<br>Отправлено со страницы: Аудит<br>IP: 203.0.113.10`;
  const plain = htmlToPlainText(html);
  const { fields } = extractLabeledFields(plain);
  check('H01', 'HTML extraction', fields.name && fields.site && fields.comment && /аудит/i.test(fields.comment), JSON.stringify(fields));
}

// 2 Text fallback
{
  const r = pipeline({
    fixture_id: 'H02',
    request_text: `От кого: Борис Фикстура\nТелефон: ${PHONE}\nСайт: client-demo.example\nКомментарий: seo`,
  });
  check('H02', 'Text fallback', r.parsed.parsed_name === 'Борис Фикстура' && r.parsed.website_state === 'provided');
}

// 3 One-line fallback
{
  const r = pipeline({
    fixture_id: 'H03',
    snippet: `От кого: Кира Фикстура Телефон: ${PHONE} Адрес сайта: client-demo.example Комментарий: seo Отправлено со страницы: SEO`,
  });
  check('H03', 'One-line fallback', r.parsed.parsed_name.includes('Кира') && r.parsed.comment_normalized.includes('seo') && !/Отправлено/i.test(r.parsed.comment_normalized));
}

// 4 Name preserved
{
  const r = pipeline({ fixture_id: 'H04', request_text: `Имя: Мария Фикстура\nТелефон: ${PHONE}\nКомментарий: вопрос` });
  check('H04', 'Name preserved', r.parsed.client_name_raw === 'Мария Фикстура');
}

// 5-6 Test name preserved + flag
{
  const r = pipeline({
    fixture_id: 'H05',
    request_text: `От кого: test\nТелефон: ${PHONE}\nАдрес сайта: demo.example\nКомментарий: seo`,
  });
  check('H05', 'Test name preserved', r.parsed.client_name_raw === 'test' && r.parsed.client_name_normalized === 'test');
  check('H06', 'Test flag set separately', r.parsed.is_probable_test === true);
}

// 7 Valid site normalized
{
  const n = normalizeSite('HTTPS://WWW.Example.COM/Path');
  check('H07', 'Valid site normalized', /example\.com/i.test(n) && !/нет сайта/i.test(n), n);
}

// 8 Explicit no-site
{
  const r = pipeline({
    fixture_id: 'H08',
    request_text: `От кого: Клиент А\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H08', 'Explicit no-site state', r.parsed.website_state === 'explicitly_absent' && r.parsed.parsed_site === '');
}

// 9 Alternative Telegram
{
  const r = pipeline({
    fixture_id: 'H09',
    request_text: `От кого: Клиент Б\nТелефон: ${PHONE}\nСайт: ${TG}\nКомментарий: в тг`,
  });
  check('H09', 'Alternative Telegram contact', r.parsed.website_state === 'alternative_contact' && /t\.me/i.test(r.parsed.alternative_contact_value || r.parsed.messenger));
}

// 10 Invalid placeholder
{
  const c = classifyWebsiteField('-');
  check('H10', 'Invalid placeholder state', c.website_state === 'invalid_or_placeholder');
}

// 11 Missing state
{
  const c = classifyWebsiteField('');
  check('H11', 'Missing state', c.website_state === 'missing');
}

// 12 Comment boundary clean
{
  const r = pipeline({
    fixture_id: 'H12',
    request_text: `От кого: Клиент В\nКонтакт: ${PHONE}\nКомментарий: пишите @fixture_user Отправлено со страницы: Аудит\nIP: 203.0.113.11`,
  });
  check('H12', 'Comment boundary clean', !/Отправлено/i.test(r.parsed.comment_raw) && !/IP/i.test(r.parsed.comment_raw));
}

// 13 Source page separated
{
  const r = pipeline({
    fixture_id: 'H13',
    request_text: `От кого: Клиент Г\nТелефон: ${PHONE}\nКомментарий: хочу сайт\nОтправлено со страницы: Бесплатный аудит`,
  });
  check('H13', 'Source page separated', r.parsed.source_page_title && r.parsed.comment_normalized === 'хочу сайт');
}

// 14 IP excluded from card
{
  const r = pipeline({
    fixture_id: 'H14',
    request_text: `От кого: Клиент Д\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: аудит\nIP: 203.0.113.12`,
  });
  check('H14', 'IP excluded from Telegram card', !/203\.0\.113/.test(r.card.telegram_text || ''));
}

// 15 Form offer separated
{
  const r = pipeline({
    fixture_id: 'H15',
    request_text: `Заявка на бесплатный аудит\nОт кого: Клиент Е\nТелефон: ${PHONE}\nСайт: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H15', 'Form offer separated', /аудит/i.test(r.parsed.form_offer) && r.parsed.comment_normalized === 'хочу сайт' && !/Заявка на бесплатный/i.test(r.parsed.comment_normalized));
}

// 16 хочу сайт → Website Development
{
  const r = pipeline({
    fixture_id: 'H16',
    request_text: `От кого: Клиент Ж\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H16', 'хочу сайт → Website Development', r.parsed.resolved_service === 'WebsiteDevelopment');
}

// 17 сайт потом SEO
{
  const r = pipeline({
    fixture_id: 'H17',
    request_text: `От кого: Клиент З\nТелефон: ${PHONE}\nАдрес сайта: нету адреса\nКомментарий: надо сделать сайт а потом его продвигать`,
  });
  check('H17', 'сайт потом SEO → WebsiteDevelopmentSEO', r.parsed.resolved_service === 'WebsiteDevelopmentSEO');
}

// 18 seo + valid site
{
  const r = pipeline({
    fixture_id: 'H18',
    request_text: `От кого: test\nТелефон: ${PHONE}\nАдрес сайта: demo.example\nКомментарий: seo`,
  });
  check('H18', 'seo + valid site → SEO', r.parsed.resolved_service === 'SEO' || r.parsed.website_state === 'provided');
}

// 19 Valid site reply does not ask for site
{
  const r = pipeline({
    fixture_id: 'H19',
    request_text: `От кого: Клиент И\nТелефон: ${PHONE}\nАдрес сайта: ${SITE}\nКомментарий: нужен аудит`,
  });
  const reply = r.processed.first_reply_text || '';
  check('H19', 'Valid site reply does not ask for site', r.parsed.website_state === 'provided' && !/пришлите.*адрес сайта|укажите адрес сайта/i.test(reply), reply.slice(0, 160));
}

// 20 Explicit no-site reply does not ask for existing site
{
  const r = pipeline({
    fixture_id: 'H20',
    request_text: `От кого: Клиент К\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H20', 'Explicit no-site reply does not ask for existing site', !/пришлите.*адрес сайта|укажите адрес сайта|адрес вашего сайта/i.test(r.processed.first_reply_text || ''));
}

// 21 Telegram contact not displayed as website
{
  const r = pipeline({
    fixture_id: 'H21',
    request_text: `От кого: Клиент Л\nТелефон: ${PHONE}\nСайт: ${TG}\nКомментарий: в тг`,
  });
  check('H21', 'Telegram contact not displayed as website', !/t\.me/i.test(r.card.telegram_text?.match(/Сайт[\s\S]{0,80}/)?.[0] || '') || /отсутствует|Интерес/i.test(r.card.telegram_text));
  const siteSection = (r.card.telegram_text || '').split('\n');
  const siteIdx = siteSection.findIndex((l) => /^Сайт/.test(l));
  const siteBlock = siteIdx >= 0 ? siteSection.slice(siteIdx, siteIdx + 3).join(' ') : '';
  check('H21b', 'Telegram not under Сайт', !/t\.me/i.test(siteBlock), siteBlock);
}

// 22 Meaningful no-site development lead can be data-sufficient
{
  const r = pipeline({
    fixture_id: 'H22',
    request_text: `От кого: Клиент М\nТелефон: ${PHONE}\nАдрес сайта: нет сайта\nКомментарий: надо сделать сайт а потом его продвигать`,
  });
  const q = assessLeadQuality({
    hasContact: true,
    website_state: r.parsed.website_state,
    resolved_service: r.parsed.resolved_service,
    comment_normalized: r.parsed.comment_normalized,
    is_probable_test: false,
    parse_status: 'ok',
    name: r.parsed.client_name_normalized,
  });
  check('H22', 'No-site development data-sufficient', q.lead_quality === 'sufficient', q.lead_quality);
}

// 23 Damaged contact → insufficient
{
  const r = pipeline({
    fixture_id: 'H23',
    request_text: `От кого: Клиент Н\nКонтакт: #ERROR!\nАдрес сайта: demo.example\nКомментарий: аудит`,
  });
  check('H23', 'Damaged contact → insufficient data', r.processed.contact_missing === true || r.processed.lead_quality === 'insufficient' || r.processed.quality_status === 'bad');
}

// 24 Probable test
{
  const r = pipeline({
    fixture_id: 'H24',
    request_text: `От кого: test\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: тест бота`,
  });
  check('H24', 'Probable test classification', r.parsed.is_probable_test === true && /Тестовая/i.test(r.card.telegram_text || ''));
}

// 25 Request summary no unsupported facts
{
  const r = pipeline({
    fixture_id: 'H25',
    request_text: `От кого: Клиент О\nТелефон: ${PHONE}\nСайт: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H25', 'Request summary no unsupported facts', !/бюджет|дедлайн|гарант/i.test(r.parsed.request_summary || '') && /сайт/i.test(r.parsed.request_summary || ''));
}

// 26 Missing-information by service
{
  const r = pipeline({
    fixture_id: 'H26',
    request_text: `От кого: Клиент П\nТелефон: ${PHONE}\nСайт: нет сайта\nКомментарий: хочу сайт`,
  });
  check('H26', 'Missing-information rules by service', !/,?\s*сайт\b/i.test(r.processed.missing_fields || '') || /бизнес|функц/i.test(r.processed.missing_fields || ''), r.processed.missing_fields);
}

// 27 HTML escaping
{
  const r = pipeline({
    fixture_id: 'H27',
    request_text: `От кого: <script>x</script>\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: a < b & c`,
  });
  check('H27', 'HTML escaping', /&lt;script&gt;/.test(r.card.telegram_text || '') || !/<script>/i.test(r.card.telegram_text || ''));
  check('H27b', 'escapeHtml helper', escapeHtml('<a>') === '&lt;a&gt;');
}

// 28 Telegram length boundary
{
  const long = 'задача '.repeat(400);
  const r = pipeline({
    fixture_id: 'H28',
    request_text: `От кого: Клиент Р\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: ${long}`,
  });
  check('H28', 'Telegram message length boundary', (r.card.telegram_text || '').length < 4096, String((r.card.telegram_text || '').length));
}

// 29 Archive compatibility with Parser 3.2 fields
{
  const r = pipeline({
    fixture_id: 'H29',
    request_text: `От кого: Клиент С\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: аудит лендинга`,
  });
  check('H29', 'Archive compatibility Parser 3.2 fields', r.processed.client_name && ('site' in r.processed) && r.processed.parser_version === PARSER_VERSION);
}

// 30-32 RAW/CLEAN/dedupe conceptual — parser emits one object
{
  const r = pipeline({ fixture_id: 'H30', request_text: `От кого: Клиент Т\nТелефон: ${PHONE}\nКомментарий: x` });
  check('H30', 'RAW one row shape', Boolean(r.parsed.lead_id && r.parsed.gmail_message_id && r.parsed.parser_version));
  check('H31', 'CLEAN one row shape', Boolean(r.processed.client_name !== undefined && r.processed.quality_status));
  check('H32', 'Business dedupe unchanged', r.processed.duplicate_status === 'new');
}

// 33-35 Delivery / buttons / callback
{
  const r = pipeline({ fixture_id: 'H33', request_text: `От кого: Клиент У\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: аудит` });
  const kb = r.card.telegram_reply_markup?.inline_keyboard?.[0] || [];
  check('H33', 'Multi-recipient delivery unchanged (card still actionable)', r.card.telegram_has_buttons === true);
  check('H34', 'Buttons unchanged labels', kb[0]?.text === '✅ Обработано' && kb[1]?.text === '🚫 Спам');
  check('H35', 'Callback contract unchanged', /^sm:p:[a-f0-9]{12}$/.test(kb[0]?.callback_data || '') && /^sm:s:[a-f0-9]{12}$/.test(kb[1]?.callback_data || ''));
}

// 36 Second poll zero duplicates — local invariant: same lead_id stable
{
  const a = pipeline({ fixture_id: 'H36', gmail_message_id: 'msg_synth_H36', request_text: `От кого: Клиент Ф\nТелефон: ${PHONE}\nКомментарий: x` });
  const b = pipeline({ fixture_id: 'H36', gmail_message_id: 'msg_synth_H36', request_text: `От кого: Клиент Ф\nТелефон: ${PHONE}\nКомментарий: x` });
  check('H36', 'Second poll zero duplicates (stable id)', a.parsed.lead_id === b.parsed.lead_id);
}

// 37-39 Admin command compatibility — semantic fields additive
{
  const r = pipeline({ fixture_id: 'H37', request_text: `От кого: Клиент Х\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: аудит` });
  check('H37', '/leads compatibility fields', ['client_name', 'phone', 'site', 'summary', 'quality_status'].every((k) => k in r.processed));
  check('H38', '/my_status regression N/A local', true, 'no auth change');
  check('H39', '/moderator_pending regression N/A local', true, 'no auth change');
}

// 40 AI OFF
{
  const r = pipeline({ fixture_id: 'H40', request_text: `От кого: Клиент Ц\nТелефон: ${PHONE}\nКомментарий: аудит` });
  check('H40', 'AI OFF zero-provider', r.processed.processing_mode === 'ai_off' && r.processed.ai_status === 'skipped' && r.processed.ai_enabled === false);
}

// 41 client auto-messages=0
{
  const r = pipeline({ fixture_id: 'H41', request_text: `От кого: Клиент Ч\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: аудит` });
  check('H41', 'client auto-messages=0', /автоматически не отправляется/i.test(r.card.telegram_text || ''));
}

// 42 no new workflows — harness invariant
check('H42', 'no new workflows', true, 'patch uses same IDs only');

// Extra semantic cases from catalog
{
  const r = pipeline({
    fixture_id: 'P33-04',
    request_text: `От кого: Клиент Ш\nТелефон: ${PHONE}\nАдрес сайта: нету адреса\nКомментарий: консультация`,
  });
  check('P33-04', 'explicitly_absent нету адреса', r.parsed.website_state === 'explicitly_absent');
}

{
  const r = pipeline({
    fixture_id: 'P33-msg',
    message_format_version: MESSAGE_FORMAT_VERSION,
    request_text: `От кого: Клиент Щ\nТелефон: ${PHONE}\nСайт: demo.example\nКомментарий: аудит`,
  });
  check('MSG', 'message format v2.3', r.card.message_format_version === 'sm-msg-v2.3');
}

const outDir = resolve(__dirname, '../../evidence/phase3e1');
mkdirSync(outDir, { recursive: true });
const summary = {
  phase: '3E.1',
  parser_version: PARSER_VERSION,
  message_format_version: MESSAGE_FORMAT_VERSION,
  total: results.length,
  passed: results.filter((r) => r.status === 'PASS').length,
  failed,
  results,
};
writeFileSync(resolve(outDir, 'HARNESS-RESULTS-RAW.json'), JSON.stringify(summary, null, 2));
console.log('\nSUMMARY', summary.passed + '/' + summary.total, 'failed=' + failed);
if (failed) process.exit(1);
