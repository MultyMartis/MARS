/**
 * Phase 1B-D6F1B — focused operator UX regression (U1–U20 offline + structural).
 */
import assert from 'node:assert/strict';
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  classifyImportReport,
  REPORT_CLASS,
  offersFilesPresent,
} from './lib/client-ops-d6d-import-condition.mjs';
import {
  formatOperatorTelegramMessage,
  wrapAcceptanceTestMessage,
  formatSite002LocalTime,
  SCENARIO_NAME_RU,
  buildTelegramNodeTextExpression,
} from './lib/client-ops-telegram-operator-message.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const EVIDENCE = resolve(
  __dirname,
  '../../evidence/phase-1b-d6f1b-telegram-operator-ux-polish',
);

const observed = '2026-08-06T11:20:00Z'; // => 06.08.2026, 18:20 UTC+07

function assertNoForbidden(text) {
  const bad = [
    'TEST-GALLERY',
    'Offers',
    'ATTENTION',
    ' ERROR',
    '\nERROR\n',
    'Статус: OK',
    'Статус: ATTENTION',
    'UTC',
    'event_id',
    'run_id',
    'Может затронуть: нет',
    'Счётчики:',
    'offers0-N.xml',
    'import0-N',
    'marker/summary',
    '≈',
  ];
  for (const b of bad) {
    assert.equal(text.includes(b), false, `forbidden visible token: ${b}`);
  }
}

const checks = [];

function check(id, fn) {
  try {
    fn();
    checks.push({ id, pass: true });
  } catch (err) {
    checks.push({ id, pass: false, error: String(err.message || err) });
  }
}

const t1 = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.FULL_SUCCESS,
  summary_code: 'FULL_IMPORT_SUCCESS',
  normalized_status: 'OK',
  observed_at: observed,
});
const t2 = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.CATALOG_SUCCESS_OFFERS_INPUT_MISSING,
  summary_code: 'OFFERS_INPUT_MISSING',
  normalized_status: 'ATTENTION',
  observed_at: observed,
});
const t3 = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.NO_FRESH_IMPORT,
  summary_code: 'NO_FRESH_1C_IMPORT',
  normalized_status: 'ATTENTION',
  observed_at: observed,
});
const t4 = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.IMPORT_ERROR,
  summary_code: 'IMPORT_ERROR',
  normalized_status: 'FAILED',
  observed_at: observed,
  error_summary: 'Ошибка фазы импорта каталога',
});
const recovery = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.RECOVERY_CONDITION_RESOLVED,
  summary_code: 'CONDITION_RESOLVED',
  normalized_status: 'OK',
  observed_at: observed,
});
const warnings = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.COMPLETED_WITH_WARNINGS,
  summary_code: 'IMPORT_COMPLETED_WITH_WARNINGS',
  normalized_status: 'ATTENTION',
  observed_at: observed,
});
const conflict = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.CONFLICT_OR_INCOMPLETE_FILE_SET,
  summary_code: 'IMPORT_FILE_SET_INCOMPLETE_OR_CONFLICT',
  normalized_status: 'ATTENTION',
  observed_at: observed,
});
const monitorUnknown = formatOperatorTelegramMessage({
  report_class: REPORT_CLASS.MONITOR_COULD_NOT_CONFIRM_COMPLETION,
  summary_code: 'MONITOR_COMPLETION_UNCONFIRMED',
  normalized_status: 'ATTENTION',
  observed_at: observed,
});

check('U1', () => {
  assert.match(t1, /^✅ Импорт 1С завершён успешно/);
  assert.match(t2, /^⚠️ Импорт 1С выполнен не полностью/);
});
check('U2', () => {
  assert.equal(formatSite002LocalTime(observed), '06.08.2026, 18:20');
  assert.match(t1, /Время: 06\.08\.2026, 18:20/);
});
check('U3', () => {
  assert.equal(t1.includes('UTC'), false);
  assert.equal(t3.includes('UTC'), false);
});
check('U4', () => {
  for (const t of [t1, t2, t3, t4]) {
    assert.equal(/\bOK\b/.test(t), false);
    assert.equal(t.includes('ATTENTION'), false);
    assert.equal(/\bERROR\b/.test(t), false);
  }
});
check('U5', () => {
  assert.equal(t2.includes('Offers'), false);
  assert.match(t2, /Цены и остатки/);
});
check('U6', () => {
  const wrapped = wrapAcceptanceTestMessage(t1, SCENARIO_NAME_RU.T1);
  assert.equal(wrapped.includes('TEST-GALLERY'), false);
  assert.equal(wrapped.includes('G1'), false);
  assert.match(wrapped, /^🧪 ТЕСТОВОЕ СООБЩЕНИЕ/);
  assert.match(wrapped, /Проверяемый сценарий: Успешный импорт/);
});
check('U7', () => {
  for (const t of [t1, t2, t3, t4]) {
    assert.equal(t.toLowerCase().includes('event_id'), false);
    assert.equal(t.toLowerCase().includes('run_id'), false);
  }
});
check('U8', () => {
  assert.equal(t1.includes('Может затронуть'), false);
});
check('U9', () => {
  assert.equal(t1.includes('Счётчики'), false);
  assert.equal(t1.includes('≈'), false);
});
check('U10', () => {
  assert.match(t2, /offers0_\*\.xml/);
  assert.match(t2, /<code>offers0_\*\.xml<\/code>/);
  assert.equal(t2.includes('offers0-N'), false);
});
check('U11', () => {
  assert.match(t2, /offers0_/);
  assert.equal(/offers0-[0-9]/.test(t2), false);
});
check('U12', () => {
  const noCounts = formatOperatorTelegramMessage({
    report_class: REPORT_CLASS.FULL_SUCCESS,
    observed_at: observed,
    factual_counts: { added_urls: 12, removed_urls: 3 }, // not authoritative
  });
  assert.equal(noCounts.includes('добавлено'), false);
});
check('U13', () => {
  assert.match(t2, /могли не обновиться/);
});
check('U14', () => {
  assert.equal(t2.toLowerCase().includes('отключен'), false);
  assert.equal(t2.toLowerCase().includes('disabled'), false);
});
check('U15', () => {
  assert.match(t3, /^⚠️/);
  const cls = classifyImportReport({ fresh_import_confirmed: false });
  assert.equal(cls.severity, 'ATTENTION');
  assert.equal(cls.report_class, REPORT_CLASS.NO_FRESH_IMPORT);
});
check('U16', () => {
  assert.equal(t4.includes('Каталог обновлён'), false);
  assert.equal(t4.includes('обработаны успешно'), false);
  assert.match(t4, /не подтверждена/);
});
check('U17', () => {
  assert.match(warnings, /^⚠️ Импорт 1С завершён с предупреждениями/);
  assert.match(conflict, /^⚠️ Набор файлов обмена/);
  assert.match(recovery, /^✅ Обмен с 1С восстановлен/);
  assert.match(monitorUnknown, /^⚠️ Завершение обмена не подтверждено/);
  assert.equal(monitorUnknown.includes('marker'), false);
  for (const t of [warnings, conflict, recovery, monitorUnknown]) assertNoForbidden(t);
});
check('U18', () => {
  for (const t of [t1, t2, t3, t4]) {
    assertNoForbidden(t);
    assert.match(t, /Сайт: bzpm\.ru/);
  }
});
check('U19', () => {
  // Structural: same event retry is handled by Data Table dedupe (live U19).
  assert.equal(typeof buildTelegramNodeTextExpression(), 'string');
  assert.match(buildTelegramNodeTextExpression(), /ТЕСТОВОЕ СООБЩЕНИЕ/);
});
check('U20', () => {
  assert.notEqual(SCENARIO_NAME_RU.T1, SCENARIO_NAME_RU.T2);
  assert.equal(offersFilesPresent(['offers0_1.xml']), true);
  assert.equal(offersFilesPresent(['offers0-1.xml']), false);
});

const failed = checks.filter((c) => !c.pass);
mkdirSync(EVIDENCE, { recursive: true });
writeFileSync(
  resolve(EVIDENCE, 'REGRESSION.md'),
  [
    '# D6F1B Operator UX Regression',
    '',
    `Pass: ${checks.length - failed.length}/${checks.length}`,
    '',
    ...checks.map((c) => `- ${c.id}: ${c.pass ? 'PASS' : `FAIL — ${c.error}`}`),
    '',
  ].join('\n'),
  'utf8',
);
writeFileSync(
  resolve(EVIDENCE, 'MESSAGE-FIXTURES-RU.json'),
  `${JSON.stringify({ t1, t2, t3, t4, warnings, conflict, recovery, monitorUnknown }, null, 2)}\n`,
  'utf8',
);

console.log(
  JSON.stringify(
    {
      ok: failed.length === 0,
      pass: checks.length - failed.length,
      total: checks.length,
      failed: failed.map((f) => f.id),
    },
    null,
    2,
  ),
);
if (failed.length) process.exit(1);
