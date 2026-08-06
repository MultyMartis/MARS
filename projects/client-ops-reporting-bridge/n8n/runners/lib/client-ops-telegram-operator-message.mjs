/**
 * Phase 1B-D6F1B — authoritative SITE-002 Telegram operator message formatter.
 *
 * Owns visible Russian operator UX. Plain text only (no Markdown/HTML parse mode).
 * Does not invent counts. Preserves factual underscores in filenames.
 * Timezone: SITE-002 operational UTC+07:00, format DD.MM.YYYY, HH:mm.
 */

import { REPORT_CLASS } from './client-ops-d6d-import-condition.mjs';

export const SITE002_OPERATOR_TZ_OFFSET_MINUTES = 7 * 60;
export const OPERATOR_MESSAGE_VERSION = '1b-d6f1b.1';
/** Canonical glob shown to operators; rendered inside HTML <code> for Telegram safety. */
export const OFFERS_GLOB_DISPLAY = 'offers0_*.xml';
export const CATALOG_GLOB_DISPLAY = 'import0_*.xml';

const TITLE = Object.freeze({
  SUCCESS: '✅ Импорт 1С завершён успешно',
  PARTIAL_OFFERS_MISSING: '⚠️ Импорт 1С выполнен не полностью',
  NO_FRESH: '⚠️ Свежий импорт 1С не обнаружен',
  ERROR: '❌ Импорт 1С завершился с ошибкой',
  WARNINGS: '⚠️ Импорт 1С завершён с предупреждениями',
  MONITOR_UNCONFIRMED: '⚠️ Завершение обмена не подтверждено',
  CONFLICT: '⚠️ Набор файлов обмена неполный или конфликтный',
  RECOVERY: '✅ Обмен с 1С восстановлен',
  ATTENTION_GENERIC: '⚠️ Требует внимания',
});

export const SCENARIO_NAME_RU = Object.freeze({
  T1: 'Успешный импорт',
  T2: 'Каталог загружен, цены и остатки не получены',
  T3: 'Свежий импорт не обнаружен',
  T4: 'Ошибка импорта',
});

/** Escape for Telegram HTML parse mode. Preserves underscores/asterisks inside text. */
export function escapeTelegramHtml(text) {
  return String(text || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

/** Render a factual filename/glob safely under HTML parse mode. */
export function codeFilename(name) {
  return `<code>${escapeTelegramHtml(name)}</code>`;
}

/**
 * Convert authoritative ISO timestamp to SITE-002 local wall time.
 * @param {string} iso
 * @returns {string} DD.MM.YYYY, HH:mm
 */
export function formatSite002LocalTime(iso) {
  const raw = String(iso || '').trim();
  if (!raw) return '';
  const ms = Date.parse(raw);
  if (!Number.isFinite(ms)) return '';
  const local = new Date(ms + SITE002_OPERATOR_TZ_OFFSET_MINUTES * 60_000);
  const dd = String(local.getUTCDate()).padStart(2, '0');
  const mm = String(local.getUTCMonth() + 1).padStart(2, '0');
  const yyyy = String(local.getUTCFullYear());
  const hh = String(local.getUTCHours()).padStart(2, '0');
  const mi = String(local.getUTCMinutes()).padStart(2, '0');
  return `${dd}.${mm}.${yyyy}, ${hh}:${mi}`;
}

function isOperatorPrefixed(text) {
  const t = String(text || '');
  return (
    t.startsWith('🧪 ТЕСТОВОЕ СООБЩЕНИЕ') ||
    t.startsWith('✅ ') ||
    t.startsWith('⚠️ ') ||
    t.startsWith('❌ ')
  );
}

export function isFullOperatorMessage(text) {
  return isOperatorPrefixed(text);
}

function resolveVariant(input = {}) {
  const reportClass = String(input.report_class || '');
  const summary = String(input.summary_code || '');
  const status = String(input.normalized_status || '').toUpperCase();
  const reasons = (input.reason_codes || []).map((r) => String(r || ''));

  if (
    reportClass === REPORT_CLASS.RECOVERY_CONDITION_RESOLVED ||
    summary === 'CONDITION_RESOLVED'
  ) {
    return 'RECOVERY';
  }
  if (
    reportClass === REPORT_CLASS.FULL_SUCCESS ||
    reportClass === REPORT_CLASS.CATALOG_AND_OFFERS_SUCCESS ||
    summary === 'FULL_IMPORT_SUCCESS'
  ) {
    return 'SUCCESS';
  }
  if (
    reportClass === REPORT_CLASS.CATALOG_SUCCESS_OFFERS_INPUT_MISSING ||
    summary === 'OFFERS_INPUT_MISSING' ||
    summary === 'OFFERS_PRESENT_NOT_PROCESSED' ||
    reasons.includes('OFFERS0_XML_ABSENT')
  ) {
    return 'PARTIAL_OFFERS_MISSING';
  }
  if (
    reportClass === REPORT_CLASS.NO_FRESH_IMPORT ||
    summary === 'NO_FRESH_1C_IMPORT' ||
    reasons.includes('NO_FRESH_IMPORT_IN_EXPECTED_WINDOW')
  ) {
    return 'NO_FRESH';
  }
  if (
    reportClass === REPORT_CLASS.IMPORT_ERROR ||
    summary === 'IMPORT_ERROR' ||
    status === 'FAILED' ||
    status === 'ERROR'
  ) {
    return 'ERROR';
  }
  if (
    reportClass === REPORT_CLASS.COMPLETED_WITH_WARNINGS ||
    summary === 'IMPORT_COMPLETED_WITH_WARNINGS'
  ) {
    return 'WARNINGS';
  }
  if (
    reportClass === REPORT_CLASS.MONITOR_COULD_NOT_CONFIRM_COMPLETION ||
    summary === 'MONITOR_COMPLETION_UNCONFIRMED'
  ) {
    return 'MONITOR_UNCONFIRMED';
  }
  if (
    reportClass === REPORT_CLASS.CONFLICT_OR_INCOMPLETE_FILE_SET ||
    summary === 'IMPORT_FILE_SET_INCOMPLETE_OR_CONFLICT' ||
    summary === 'IMPORT_CONDITION_INCOMPLETE'
  ) {
    return 'CONFLICT';
  }
  if (status === 'OK') return 'SUCCESS';
  if (status === 'ATTENTION') return 'ATTENTION_GENERIC';
  return 'ATTENTION_GENERIC';
}

function sanitizeErrorSummary(summary) {
  const s = String(summary || '')
    .replace(/\r?\n/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  if (!s) return '';
  // Drop paths / stacks / internals.
  if (/[\\/]|stack|traceback|node_modules|X:\\|event_id|run_id/i.test(s)) {
    return s.slice(0, 160).replace(/[\\/].*$/, '').trim();
  }
  return s.slice(0, 200);
}

function pushFactualCountLines(lines, counts) {
  if (!counts || typeof counts !== 'object') return;
  const add = counts.added_urls;
  const rem = counts.removed_urls;
  // Only emit when authoritative integers are present AND caller marked them factual.
  if (counts.authoritative !== true) return;
  if (Number.isInteger(add) && Number.isInteger(rem)) {
    if (add > 0 || rem > 0) {
      lines.push(`Изменения каталога: добавлено ${add}, удалено ${rem}.`);
    }
  }
}

/**
 * Build production-visible Telegram body (no test wrapper).
 * Output is HTML-safe for Telegram parse_mode=HTML.
 * @param {object} input
 * @returns {string}
 */
export function formatOperatorTelegramMessage(input = {}) {
  const variant = resolveVariant(input);
  const domain = escapeTelegramHtml(String(input.domain || 'bzpm.ru'));
  const observed = formatSite002LocalTime(
    input.observed_at || input.generated_at || '',
  );
  const timeLabel = variant === 'NO_FRESH' ? 'Время проверки' : 'Время';
  const lines = [];

  lines.push(TITLE[variant] || TITLE.ATTENTION_GENERIC);
  lines.push('');
  lines.push(`Сайт: ${domain}`);
  if (observed) lines.push(`${timeLabel}: ${escapeTelegramHtml(observed)}`);
  lines.push('');

  if (variant === 'SUCCESS') {
    lines.push('Каталог обновлён.');
    lines.push('Цены и остатки обработаны.');
    lines.push('Критических ошибок не обнаружено.');
    pushFactualCountLines(lines, input.factual_counts);
  } else if (variant === 'PARTIAL_OFFERS_MISSING') {
    lines.push('Каталог обработан успешно.');
    lines.push('Файл с ценами и остатками от 1С не получен.');
    lines.push('');
    lines.push('Цены и остатки товаров могли не обновиться.');
    lines.push('');
    lines.push('Что проверить:');
    lines.push(
      `выгрузку предложений из 1С и наличие файла ${codeFilename(OFFERS_GLOB_DISPLAY)}.`,
    );
  } else if (variant === 'NO_FRESH') {
    lines.push('В ожидаемое время новый обмен с 1С не подтверждён.');
    lines.push('');
    lines.push('Каталог, цены и остатки могли остаться без обновления.');
    lines.push('');
    lines.push('Что проверить:');
    lines.push('расписание обмена и журнал выгрузки 1С.');
  } else if (variant === 'ERROR') {
    lines.push('Обмен не был завершён корректно.');
    lines.push('Актуальность каталога, цен и остатков не подтверждена.');
    const err = sanitizeErrorSummary(input.error_summary);
    if (err) {
      lines.push('');
      lines.push(`Ошибка: ${escapeTelegramHtml(err)}`);
    }
    lines.push('');
    lines.push('Что сделать:');
    lines.push('проверить журнал импорта и устранить указанную ошибку.');
  } else if (variant === 'WARNINGS') {
    lines.push('Импорт завершён, но есть некритические предупреждения.');
    lines.push('Каталог, цены и остатки обработаны.');
    lines.push('');
    lines.push('Что проверить:');
    lines.push('предупреждения в журнале импорта.');
  } else if (variant === 'MONITOR_UNCONFIRMED') {
    lines.push('Монитор не подтвердил корректное завершение цикла обмена.');
    lines.push('Достоверность отчёта требует проверки.');
    lines.push('');
    lines.push('Что проверить:');
    lines.push('завершение монитора и повторный запуск при необходимости.');
  } else if (variant === 'CONFLICT') {
    lines.push('Обнаружен неполный или конфликтный набор файлов обмена.');
    lines.push('');
    lines.push('Что проверить:');
    lines.push('состав файлов каталога и цен/остатков перед повторным импортом.');
  } else if (variant === 'RECOVERY') {
    lines.push('Предыдущая проблема больше не обнаружена.');
    lines.push('Каталог, цены и остатки обработаны успешно.');
  } else {
    lines.push('Состояние обмена с 1С требует внимания оператора.');
    lines.push('');
    lines.push('Что проверить:');
    lines.push('журнал импорта и результат последнего обмена с 1С.');
  }

  // Strip trailing empty lines.
  while (lines.length && lines[lines.length - 1] === '') lines.pop();
  return lines.join('\n');
}

/**
 * Wrap production body with test marker for acceptance gallery.
 * @param {string} body
 * @param {string} scenarioNameRu
 */
export function wrapAcceptanceTestMessage(body, scenarioNameRu) {
  return [
    '🧪 ТЕСТОВОЕ СООБЩЕНИЕ',
    '',
    `Проверяемый сценарий: ${escapeTelegramHtml(scenarioNameRu)}`,
    '',
    String(body || '').trim(),
  ].join('\n');
}

/**
 * Build n8n Telegram text expression source (plain text, no parse_mode).
 * Passes through full operator / test messages from action.text.
 */
export function buildTelegramNodeTextExpression() {
  // Kept compact for n8n expression editor; mirrors formatOperatorTelegramMessage.
  return `={{ (() => {
  const body = $('Capture Request Metadata').item.json.body || {};
  const actionText = String((body.action && body.action.text) || '');
  if (
    actionText.indexOf('🧪 ТЕСТОВОЕ СООБЩЕНИЕ') === 0 ||
    actionText.indexOf('✅ ') === 0 ||
    actionText.indexOf('⚠️ ') === 0 ||
    actionText.indexOf('❌ ') === 0
  ) {
    return actionText;
  }
  const status = String((body.run && body.run.normalized_status) || 'OK').toUpperCase();
  const summary = String((body.run && body.run.summary_code) || '');
  const reasons = ((body.run && body.run.reason_codes) || []).map(String);
  const domain = String((body.site && body.site.domain) || 'bzpm.ru');
  const observedRaw = String(body.observed_at || body.generated_at || '');
  let localTime = '';
  if (observedRaw) {
    const ms = Date.parse(observedRaw);
    if (isFinite(ms)) {
      const local = new Date(ms + 7 * 60 * 60 * 1000);
      const p = (n) => String(n).padStart(2, '0');
      localTime = p(local.getUTCDate()) + '.' + p(local.getUTCMonth() + 1) + '.' + local.getUTCFullYear() + ', ' + p(local.getUTCHours()) + ':' + p(local.getUTCMinutes());
    }
  }
  let variant = 'ATTENTION_GENERIC';
  if (summary === 'CONDITION_RESOLVED') variant = 'RECOVERY';
  else if (summary === 'FULL_IMPORT_SUCCESS') variant = 'SUCCESS';
  else if (summary === 'OFFERS_INPUT_MISSING' || summary === 'OFFERS_PRESENT_NOT_PROCESSED' || reasons.indexOf('OFFERS0_XML_ABSENT') >= 0) variant = 'PARTIAL_OFFERS_MISSING';
  else if (summary === 'NO_FRESH_1C_IMPORT' || reasons.indexOf('NO_FRESH_IMPORT_IN_EXPECTED_WINDOW') >= 0) variant = 'NO_FRESH';
  else if (summary === 'IMPORT_ERROR' || status === 'FAILED') variant = 'ERROR';
  else if (summary === 'IMPORT_COMPLETED_WITH_WARNINGS') variant = 'WARNINGS';
  else if (summary === 'MONITOR_COMPLETION_UNCONFIRMED') variant = 'MONITOR_UNCONFIRMED';
  else if (summary === 'IMPORT_FILE_SET_INCOMPLETE_OR_CONFLICT' || summary === 'IMPORT_CONDITION_INCOMPLETE') variant = 'CONFLICT';
  else if (status === 'OK') variant = 'SUCCESS';
  const titles = {
    SUCCESS: '✅ Импорт 1С завершён успешно',
    PARTIAL_OFFERS_MISSING: '⚠️ Импорт 1С выполнен не полностью',
    NO_FRESH: '⚠️ Свежий импорт 1С не обнаружен',
    ERROR: '❌ Импорт 1С завершился с ошибкой',
    WARNINGS: '⚠️ Импорт 1С завершён с предупреждениями',
    MONITOR_UNCONFIRMED: '⚠️ Завершение обмена не подтверждено',
    CONFLICT: '⚠️ Набор файлов обмена неполный или конфликтный',
    RECOVERY: '✅ Обмен с 1С восстановлен',
    ATTENTION_GENERIC: '⚠️ Требует внимания'
  };
  const timeLabel = variant === 'NO_FRESH' ? 'Время проверки' : 'Время';
  const lines = [titles[variant] || titles.ATTENTION_GENERIC, '', 'Сайт: ' + domain];
  if (localTime) lines.push(timeLabel + ': ' + localTime);
  lines.push('');
  if (variant === 'SUCCESS') {
    lines.push('Каталог обновлён.', 'Цены и остатки обработаны.', 'Критических ошибок не обнаружено.');
  } else if (variant === 'PARTIAL_OFFERS_MISSING') {
    lines.push('Каталог обработан успешно.', 'Файл с ценами и остатками от 1С не получен.', '', 'Цены и остатки товаров могли не обновиться.', '', 'Что проверить:', 'выгрузку предложений из 1С и наличие файла <code>offers0_*.xml</code>.');
  } else if (variant === 'NO_FRESH') {
    lines.push('В ожидаемое время новый обмен с 1С не подтверждён.', '', 'Каталог, цены и остатки могли остаться без обновления.', '', 'Что проверить:', 'расписание обмена и журнал выгрузки 1С.');
  } else if (variant === 'ERROR') {
    lines.push('Обмен не был завершён корректно.', 'Актуальность каталога, цен и остатков не подтверждена.', '', 'Что сделать:', 'проверить журнал импорта и устранить указанную ошибку.');
  } else if (variant === 'WARNINGS') {
    lines.push('Импорт завершён, но есть некритические предупреждения.', 'Каталог, цены и остатки обработаны.', '', 'Что проверить:', 'предупреждения в журнале импорта.');
  } else if (variant === 'MONITOR_UNCONFIRMED') {
    lines.push('Монитор не подтвердил корректное завершение цикла обмена.', 'Достоверность отчёта требует проверки.', '', 'Что проверить:', 'завершение монитора и повторный запуск при необходимости.');
  } else if (variant === 'CONFLICT') {
    lines.push('Обнаружен неполный или конфликтный набор файлов обмена.', '', 'Что проверить:', 'состав файлов каталога и цен/остатков перед повторным импортом.');
  } else if (variant === 'RECOVERY') {
    lines.push('Предыдущая проблема больше не обнаружена.', 'Каталог, цены и остатки обработаны успешно.');
  } else {
    lines.push('Состояние обмена с 1С требует внимания оператора.', '', 'Что проверить:', 'журнал импорта и результат последнего обмена с 1С.');
  }
  return lines.join('\\n');
})() }}`;
}
