/**
 * Phase 3D.1 parser fixture suite — sanitized only.
 */
import { parseLeadItem, extractLabeledFields } from './parse-lead-lib.mjs';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const PHONE = '+7 (900) 111-22-33';
const PHONE_DIGITS_OK = true;
const EMAIL = 'lead.test@example.com';
const TG = '@iseo_test_user';
const SITE = 'test-stabilization.example';
const SITE_HTTPS = 'https://www.example.ru/path';

function assert(cond, msg) {
  if (!cond) throw new Error(msg);
}

function noLabelBleed(value) {
  const s = String(value || '');
  return !/(?:От\s*кого|Способ\s*связи|Контакт|Адрес\s*сайта|Комментарий|Сообщение|Имя|Телефон|Сайт)\s*[:：]/i.test(s);
}

const fixtures = [
  {
    id: 'F-AF01',
    title: 'multiline audit form with phone',
    input: {
      fixture_id: 'AF01',
      synthetic_fixture: true,
      subject: 'Website form',
      request_text: [
        'Заявка на бесплатный аудит',
        'От кого: Тест Стабилизация',
        'Способ связи: Телефон',
        `Контакт: ${PHONE}`,
        `Адрес сайта: ${SITE}`,
        'Комментарий: Тест стабильности нового Sales Manager',
      ].join('\n'),
    },
    expect: {
      parsed_name: 'Тест Стабилизация',
      parsed_phone: true,
      parsed_site: SITE,
      contact_method: 'phone',
      form_audit: true,
      comment_has: 'стабильности',
    },
  },
  {
    id: 'F-AF02',
    title: 'collapsed single-line audit form with phone',
    input: {
      fixture_id: 'AF02',
      synthetic_fixture: true,
      snippet: `Заявка на бесплатный аудит От кого: Тест Стабилизация Способ связи: Телефон Контакт: ${PHONE} Адрес сайта: ${SITE} Комментарий: Тест стабильности нового Sales Manager`,
    },
    expect: {
      parsed_name: 'Тест Стабилизация',
      parsed_phone: true,
      parsed_site: SITE,
      contact_method: 'phone',
      form_audit: true,
      comment_has: 'стабильности',
    },
  },
  {
    id: 'F-AF03',
    title: 'audit form with email',
    input: {
      fixture_id: 'AF03',
      synthetic_fixture: true,
      request_text: [
        'Заявка на бесплатный аудит',
        'От кого: Анна Пример',
        'Способ связи: Email',
        `Контакт: ${EMAIL}`,
        'Адрес сайта: example.ru',
        'Комментарий: Нужен аудит лендинга',
      ].join('\n'),
    },
    expect: {
      parsed_name: 'Анна Пример',
      parsed_email: EMAIL,
      contact_method: 'email',
      parsed_site: 'example.ru',
    },
  },
  {
    id: 'F-AF04',
    title: 'audit form with Telegram',
    input: {
      fixture_id: 'AF04',
      synthetic_fixture: true,
      request_text: [
        'Заявка на бесплатный аудит',
        'От кого: Иван Тестов',
        'Способ связи: Telegram',
        `Контакт: ${TG}`,
        'Сайт: www.example.com',
        'Сообщение: Свяжитесь в Telegram',
      ].join('\n'),
    },
    expect: {
      parsed_name: 'Иван Тестов',
      parsed_messenger: true,
      contact_method: 'telegram',
      parsed_site: 'www.example.com',
    },
  },
  {
    id: 'F-AF05',
    title: 'optional spaces / NBSP around colon',
    input: {
      fixture_id: 'AF05',
      synthetic_fixture: true,
      request_text: `От кого\u00a0:  Тест\u00a0NBSP\nСпособ связи : Телефон\nКонтакт： ${PHONE}\nАдрес сайта: example.org\nКомментарий: nbsp case`,
    },
    expect: {
      parsed_name: 'Тест NBSP',
      parsed_phone: true,
      parsed_site: 'example.org',
    },
  },
  {
    id: 'F-AF06',
    title: 'reordered optional fields',
    input: {
      fixture_id: 'AF06',
      synthetic_fixture: true,
      request_text: [
        'Комментарий: Сначала комментарий',
        `Адрес сайта: ${SITE_HTTPS}`,
        `Контакт: ${PHONE}`,
        'Способ связи: Телефон',
        'От кого: Реордер Тест',
        'Заявка на бесплатный аудит',
      ].join('\n'),
    },
    expect: {
      parsed_name: 'Реордер Тест',
      parsed_phone: true,
      parsed_site: SITE_HTTPS,
      comment_has: 'комментарий',
    },
  },
  {
    id: 'F-AF07',
    title: 'missing name but valid phone/site',
    input: {
      fixture_id: 'AF07',
      synthetic_fixture: true,
      request_text: `Способ связи: Телефон Контакт: ${PHONE} Адрес сайта: example.net Комментарий: Без имени`,
    },
    expect: {
      parsed_name: '',
      parsed_phone: true,
      parsed_site: 'example.net',
    },
  },
  {
    id: 'F-AF08',
    title: 'valid name/contact missing site',
    input: {
      fixture_id: 'AF08',
      synthetic_fixture: true,
      request_text: `От кого: Без Сайта Способ связи: Телефон Контакт: ${PHONE} Комментарий: Сайт не указан`,
    },
    expect: {
      parsed_name: 'Без Сайта',
      parsed_phone: true,
      parsed_site: '',
    },
  },
  {
    id: 'F-AF09',
    title: 'malformed contact',
    input: {
      fixture_id: 'AF09',
      synthetic_fixture: true,
      request_text: 'От кого: Плохой Контакт Способ связи: Телефон Контакт: 44 Адрес сайта: example.com Комментарий: bad phone',
    },
    expect: {
      parsed_name: 'Плохой Контакт',
      parsed_phone: false,
      parsed_site: 'example.com',
      has_contact: false,
    },
  },
  {
    id: 'F-AF10',
    title: 'previous accepted lead format regression (pre-parsed fields)',
    input: {
      fixture_id: 'AF10',
      synthetic_fixture: true,
      parsed_name: 'Legacy Lead',
      parsed_phone: PHONE,
      parsed_site: 'legacy.example.ru',
      request_text: 'Хочу SEO продвижение',
    },
    expect: {
      parsed_name: 'Legacy Lead',
      parsed_phone: true,
      parsed_site: 'legacy.example.ru',
    },
  },
  {
    id: 'F-AF11',
    title: 'special characters in comment',
    input: {
      fixture_id: 'AF11',
      synthetic_fixture: true,
      request_text: `От кого: Спец Символ Способ связи: Email Контакт: ${EMAIL} Адрес сайта: example.com Комментарий: Нужен аудит <главной> & "лендинга" — срочно!`,
    },
    expect: {
      parsed_name: 'Спец Символ',
      parsed_email: EMAIL,
      comment_has: 'лендинга',
    },
  },
  {
    id: 'F-AF12',
    title: 'duplicated quoted email content',
    input: {
      fixture_id: 'AF12',
      synthetic_fixture: true,
      request_text: [
        'Заявка на бесплатный аудит',
        'От кого: Дубль Тест',
        'Способ связи: Телефон',
        `Контакт: ${PHONE}`,
        'Адрес сайта: dup.example',
        'Комментарий: Первичное сообщение',
        '',
        '----- Forwarded -----',
        'От кого: Чужой Человек',
        'Способ связи: Email',
        'Контакт: other@example.com',
        'Адрес сайта: evil.example',
        'Комментарий: Цитата',
      ].join('\n'),
    },
    expect: {
      // first wins — no greedy takeover by quoted block
      parsed_name: 'Дубль Тест',
      parsed_phone: true,
      parsed_email: '',
      parsed_site: 'dup.example',
      comment_has: 'Первичное',
    },
  },
];

const results = [];
let failed = 0;

for (const fx of fixtures) {
  try {
    const out = parseLeadItem(fx.input);
    const e = fx.expect;
    if (e.parsed_name != null) assert(out.parsed_name === e.parsed_name, `name want=${e.parsed_name} got=${out.parsed_name}`);
    if (e.parsed_phone === true) assert(!!out.parsed_phone && out.parsed_phone.replace(/\D/g, '').length >= 10, `phone missing: ${out.parsed_phone}`);
    if (e.parsed_phone === false) assert(!out.parsed_phone, `phone should be empty got=${out.parsed_phone}`);
    if (e.parsed_email) assert(out.parsed_email === e.parsed_email, `email want=${e.parsed_email} got=${out.parsed_email}`);
    if (e.parsed_email === '') assert(!out.parsed_email, `email should be empty`);
    if (e.parsed_messenger === true) assert(!!out.parsed_messenger, 'messenger missing');
    if (e.parsed_site != null) assert(out.parsed_site === e.parsed_site, `site want=${e.parsed_site} got=${out.parsed_site}`);
    if (e.contact_method) assert(out.contact_method === e.contact_method, `method want=${e.contact_method} got=${out.contact_method}`);
    if (e.form_audit) assert(/аудит/i.test(out.form_name + out.request_text), 'audit form not detected');
    if (e.comment_has) assert(String(out.request_text).includes(e.comment_has), `comment missing ${e.comment_has} in ${out.request_text}`);
    if (e.has_contact === false) assert(!(out.parsed_phone || out.parsed_email || out.parsed_messenger), 'contact should be absent');

    for (const v of [out.parsed_name, out.parsed_phone, out.parsed_email, out.parsed_messenger, out.parsed_site, out.request_text]) {
      assert(noLabelBleed(v), `label bleed in value: ${v}`);
    }

    // structural: next-label delimiting
    const { fields } = extractLabeledFields(fx.input.request_text || fx.input.snippet || '');
    if (fields.name) assert(noLabelBleed(fields.name), 'name bleed');
    if (fields.contact) assert(noLabelBleed(fields.contact), 'contact bleed');

    results.push({ id: fx.id, title: fx.title, pass: true, parser_version: out.parser_version });
  } catch (err) {
    failed++;
    results.push({ id: fx.id, title: fx.title, pass: false, error: String(err.message || err) });
  }
}

const summary = {
  total: fixtures.length,
  passed: results.filter((r) => r.pass).length,
  failed,
  results,
};

mkdirSync(resolve(__dirname, '..'), { recursive: true });
writeFileSync(resolve(__dirname, '../PARSER-FIXTURE-RESULTS.json'), JSON.stringify(summary, null, 2));
console.log(JSON.stringify(summary, null, 2));
if (failed) process.exit(1);
