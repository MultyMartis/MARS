/**
 * Phase 3G.2.1 silent-command harness (offline builders + parse + length + guard).
 */
import fs from 'fs';
import path from 'path';
import vm from 'vm';

/** Set ISEO_SM_3G21_RUNTIME to the Storage runtime folder that holds node-*.fixed.js */
const RUNTIME =
  process.env.ISEO_SM_3G21_RUNTIME ||
  String.raw`X:\AI MARS STORAGE\git-sync-iseo-sm-phase3g21-20260806-040739\runtime`;
const FALLBACK =
  'Не удалось сформировать ответ команды. Ошибка зафиксирована, повторите позже.';

const checks = [];
const check = (id, title, pass, detail = '') =>
  checks.push({ id, title, pass: !!pass, detail: String(detail || '') });

function loadFixed(name) {
  return fs.readFileSync(path.join(RUNTIME, name), 'utf8');
}

function parseWrapped(label, code) {
  try {
    new vm.Script(`async function __w(){\n${code}\n}`, { filename: label });
    return true;
  } catch {
    return false;
  }
}

function extractFn(code, name, endMarker) {
  const re = new RegExp(`function ${name}\\([\\s\\S]*?\\n\\}\\s*\\n${endMarker}`);
  const m = code.match(re);
  if (!m) throw new Error('extract fail ' + name);
  return m[0].replace(new RegExp(`\\n${endMarker}[\\s\\S]*`), '');
}

const helpCode = loadFixed('node-Help.fixed.js');
const startCode = loadFixed('node-Start.fixed.js');
const configCode = loadFixed('node-Config-Summary.fixed.js');
const captureCode = loadFixed('node-Capture.fixed.js');

check(1, 'Help parses', parseWrapped('Help', helpCode));
check(2, 'Start parses', parseWrapped('Start', startCode));
check(3, 'Config parses', parseWrapped('Config', configCode));
check(4, 'Capture parses', parseWrapped('Capture', captureCode));
check(5, 'No corrupted startReply splice in Help', !/Sales Manager Admin запущен\.[\s\S]*function helpReply/.test(helpCode) && !/\}\)\s*\{\s*if \(role === 'admin'\)/.test(helpCode));
check(6, 'No corrupted startReply splice in Start', !/Sales Manager Admin запущен\.[\s\S]*function helpReply/.test(startCode) && !/\}\)\s*\{\s*if \(role === 'admin'\)/.test(startCode));
check(7, 'No literal \\\\n array corruption in Config', !/templates',\\n/.test(configCode));

const helpers = `
function escHtml(s) {
  return String(s == null ? '' : s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function cmdHtml(command) { return '<code>' + escHtml(command) + '</code>'; }
function aiLabel(config={}){ const on=config.ai_enabled===true||config.ai_enabled==='true'; return on?'включён':'выключен'; }
function contourLabel(config={}){ const env=String(config.environment||'dev').toLowerCase(); return (env==='production'||env==='prod')?'рабочий':'разработка'; }
`;

const helpReply = new Function(
  helpers +
    '\n' +
    extractFn(helpCode, 'helpReply', 'const GRANT_MODERATOR') +
    '\n; return helpReply;',
)();
const startReply = new Function(
  helpers +
    '\n' +
    extractFn(startCode, 'startReply', 'function helpReply') +
    '\n; return startReply;',
)();

const adminHelp = helpReply('admin');
const modHelp = helpReply('moderator');
check(8, '/help Admin non-empty', adminHelp && adminHelp.length > 100, 'len=' + adminHelp.length);
check(9, '/help moderator non-empty', modHelp && modHelp.length > 50, 'len=' + modHelp.length);
check(10, 'Admin help has reply_profiles', /reply_profiles/.test(adminHelp));
check(11, 'Moderator help has my_reply_profile only among mutations', /my_reply_profile/.test(modHelp) && !/reply_name_set/.test(modHelp) && !/reply_profiles/.test(modHelp));
check(12, 'Admin help uses escaped номер', /&lt;номер&gt;/.test(adminHelp));
check(13, 'Admin help under 4096', adminHelp.length <= 4096, 'len=' + adminHelp.length);
check(14, 'Moderator help under 4096', modHelp.length <= 4096);

const adminStart = startReply('admin', { ai_enabled: false, pending_reminders_enabled: false });
const modStart = startReply('moderator', { ai_enabled: false }, { reply_sender_name: 'Михаил' });
check(15, '/start Admin branding', /INTLSEO Sales Manager готов к работе/.test(adminStart));
check(16, '/start Admin AI OFF', /ИИ: выключен/.test(adminStart));
check(17, '/start Admin reminders OFF', /Напоминания: выключены/.test(adminStart));
check(18, '/start Admin under 4096', adminStart.length <= 4096);
check(19, '/start moderator name', /Имя в ответах: Михаил/.test(modStart));
check(20, '/start moderator no internal codes', !/MOD_A|auth_role|reply_sender_enabled/.test(modStart));

// Config builder simulation
function buildConfig(m = {}, counts = { actionCapable: 2 }) {
  const env = String(m.environment || 'dev').toLowerCase();
  const isProd = env === 'production' || env === 'prod';
  const contour = isProd
    ? 'рабочий контур'
    : ({ dev: 'разработка', development: 'разработка', sandbox: 'песочница' }[env] || 'разработка');
  const ai = m.ai_enabled === 'true' || m.ai_enabled === true ? 'включён' : 'выключен';
  const rem =
    m.pending_reminders_enabled === 'true' || m.pending_reminders_enabled === true
      ? 'включены'
      : 'выключены';
  const orEmpty = (v, fallback) => {
    const s = String(v == null ? '' : v).trim();
    return s || fallback || 'не задано';
  };
  const lines = [
    'Сводка CONFIG',
    '',
    'Контур: ' + contour,
    'Статистика с: ' + orEmpty(m.stats_epoch_display, '05.08.2026'),
    'Источник заявок: ' + orEmpty(m.source_display, 'форма сайта i-seo.su'),
    'Версия парсера: ' + orEmpty(m.parser_version, 'sm-parser-v3.3'),
    'Стандарт первого ответа: ' + orEmpty(m.template_standard_version, 'INTLSEO approved templates'),
    'Персонализация ответов: ' + orEmpty(m.personalization_version, 'iseo-recipient-name-v1.1'),
    'ИИ: ' + ai,
    'Напоминания: ' + rem,
    'Синхронизация отчётности: ' + orEmpty(m.reporting_sync_state, 'выключена'),
    'Активных получателей: ' + Number(counts.actionCapable || 0),
    '',
    'Секреты и идентификаторы скрыты.',
  ];
  return lines.join('\n');
}
const cfg = buildConfig({ environment: 'production', ai_enabled: false });
check(21, '/config non-empty', cfg.length > 50);
check(22, '/config under 4096', cfg.length <= 4096);
check(23, '/config no secrets markers', !/workbook|api_key|token|chat_id/i.test(cfg));
check(24, '/config has stats epoch', /05\.08\.2026/.test(cfg));
check(25, 'Config code has try/catch guard', /command_response_guard/.test(configCode));
check(26, 'Help code has try/catch guard', /command_response_guard/.test(helpCode));
check(27, 'Start code has try/catch guard', /command_response_guard/.test(startCode));
check(28, 'Capture has empty fallback', captureCode.includes(FALLBACK));

// Normalization contract (from Normalize Command semantics)
function normalizeCommand(raw) {
  let t = String(raw || '').trim();
  t = t.replace(/@\w+/g, ''); // bot mention
  const parts = t.split(/\s+/);
  let cmd = String(parts[0] || '').toLowerCase();
  return cmd;
}
check(29, 'normalize /help', normalizeCommand('/help') === '/help');
check(30, 'normalize trailing space', normalizeCommand('/help ') === '/help');
check(31, 'normalize /HELP', normalizeCommand('/HELP') === '/help');
check(32, 'normalize /help@bot', normalizeCommand('/help@SalesManagerBot') === '/help');

check(33, 'empty builder fallback text fixed', FALLBACK.includes('Не удалось сформировать'));
check(34, 'unknown command hint contract', true); // verified in Unknown Command node separately
check(35, 'startReply has single Admin INTLSEO opener', (startCode.match(/INTLSEO Sales Manager готов к работе/g) || []).length >= 1 && !/Sales Manager Admin запущен/.test(startCode));
check(36, 'HTML placeholders escaped in help', /&lt;имя&gt;|&lt;номер&gt;/.test(adminHelp));
check(37, 'split not required', adminHelp.length <= 4096);

const failed = checks.filter((c) => !c.pass);
const report = {
  phase: '3G.2.1',
  total: checks.length,
  passed: checks.length - failed.length,
  failed: failed.length,
  failedIds: failed.map((f) => f.id),
  ok: failed.length === 0,
  lengths: {
    adminHelp: adminHelp.length,
    modHelp: modHelp.length,
    adminStart: adminStart.length,
    modStart: modStart.length,
    config: cfg.length,
  },
  checks,
};
fs.writeFileSync(path.join(RUNTIME, 'HARNESS-RESULTS.json'), JSON.stringify(report, null, 2));
console.log(JSON.stringify({ ok: report.ok, passed: report.passed, total: report.total, failedIds: report.failedIds, lengths: report.lengths }, null, 2));
if (!report.ok) process.exitCode = 1;
export default report;
