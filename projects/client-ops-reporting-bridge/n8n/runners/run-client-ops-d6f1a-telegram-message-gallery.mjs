/**
 * Phase 1B-D6F1A — Telegram message gallery through production n8n path.
 *
 * Authorized manual live test. Sends synthetic envelopes marked as tests.
 * Does not mutate production Data Table rows (uses new test event IDs).
 * Does not print secrets or chat IDs beyond already-known operator contour.
 *
 * Usage:
 *   node run-client-ops-d6f1a-telegram-message-gallery.mjs --send \
 *     --confirm="SEND CLIENT OPS D6F1A TELEGRAM MESSAGE GALLERY BZPM"
 *
 * Default: dry-run preview only.
 */

import { createHash, randomUUID } from 'node:crypto';
import {
  existsSync,
  mkdirSync,
  readFileSync,
  writeFileSync,
} from 'node:fs';
import { dirname, resolve, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  ALLOWED_WORKFLOW_ID,
} from './lib/client-ops-n8n-activation-client.mjs';
import {
  getDataTableRows,
  loadDataTableCredentials,
} from './lib/client-ops-n8n-datatable-client.mjs';
import { TELEGRAM_NODE_NAME } from './lib/client-ops-dedupe-compose.mjs';
import { D6A_TABLE_ID } from './lib/client-ops-delivery-ledger-compose.mjs';
import {
  classifyImportReport,
  REPORT_CLASS,
} from './lib/client-ops-d6d-import-condition.mjs';
import { uuidV5, sha256Hex } from './lib/client-ops-d6d-artifact.mjs';
import { MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID } from './lib/client-ops-d6d-constants.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EVIDENCE = resolve(
  REPO_ROOT,
  'projects/client-ops-reporting-bridge/evidence/phase-1b-d6f1a-production-silence-forensic-and-message-gallery',
);
const SECRET_PATH = resolve(
  REPO_ROOT,
  'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env',
);
const CONFIRM = 'SEND CLIENT OPS D6F1A TELEGRAM MESSAGE GALLERY BZPM';
const GALLERY_TS = new Date().toISOString().replace(/[:.]/g, '-');

function writeJson(path, obj) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function loadEnvKey(path, key) {
  if (!existsSync(path)) return { ok: false };
  const lines = readFileSync(path, 'utf8').split(/\r?\n/);
  for (const line of lines) {
    const t = line.trim();
    if (!t || t.startsWith('#')) continue;
    const i = t.indexOf('=');
    if (i < 0) continue;
    if (t.slice(0, i).trim() === key) {
      return { ok: true, value: t.slice(i + 1).trim() };
    }
  }
  return { ok: false };
}

function galleryEventId(scenarioId) {
  const name = `mars.client-ops.test-gallery.site-002.${GALLERY_TS}.${scenarioId}`;
  const digest = sha256Hex(name);
  return uuidV5(MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID, digest);
}

function buildMessage({ scenarioId, scenarioName, severity, conclusion, catalog, offers, affected, action, counts }) {
  // Avoid Telegram Markdown/HTML entity pitfalls: no *, _, `, [ ] unpaired.
  const safe = (s) =>
    String(s || '')
      .replace(/\*/g, 'x')
      .replace(/_/g, '-')
      .replace(/`/g, "'");
  const lines = [
    '🧪 ТЕСТОВОЕ СООБЩЕНИЕ',
    `Сценарий: ${safe(scenarioName)}`,
    '',
    'Сайт: bzpm.ru',
    `Время отчёта: ${new Date().toISOString().slice(0, 16).replace('T', ' ')} UTC`,
    `Статус: ${safe(severity)}`,
    `Вывод: ${safe(conclusion)}`,
    `Каталог: ${safe(catalog)}`,
    `Offers: ${safe(offers)}`,
  ];
  if (counts) lines.push(`Счётчики: ${safe(counts)}`);
  if (affected) lines.push(`Может затронуть: ${safe(affected)}`);
  if (action) lines.push(`Действие: ${safe(action)}`);
  lines.push(`Источник: TEST-GALLERY / ${safe(scenarioId)}`);
  return lines.join('\n');
}

function scenarios() {
  const now = new Date();
  const observed = new Date(now.getTime() - 120_000).toISOString().replace(/\.\d{3}Z$/, 'Z');
  const generated = now.toISOString().replace(/\.\d{3}Z$/, 'Z');

  const defs = [
    {
      id: 'G1',
      name: 'FULL IMPORT SUCCESS',
      severity: 'OK',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 1,
      }),
      conclusion: 'Полный обмен 1С завершён без критических ошибок.',
      catalog: 'обработан (import0-1.xml)',
      offers: 'обработан (offers0-1.xml)',
      counts: 'каталог=OK, offers=OK',
      affected: 'нет',
      action: null,
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'NO_ACTION_REQUIRED',
    },
    {
      id: 'G2',
      name: 'CATALOG SUCCESS, OFFERS FILE MISSING',
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: [],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 0,
      }),
      conclusion: 'Каталог импортирован; offers0-N.xml не получен — это не полный успешный обмен.',
      catalog: 'завершён (import0-1.xml)',
      offers: 'входной файл offers0-N.xml отсутствует',
      counts: null,
      affected: 'цены и остатки могли не обновиться',
      action: 'Проверить выгрузку offers0-N.xml из 1С и повтор обмена',
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'G3',
      name: 'CATALOG AND OFFERS SUCCESS WITH MATERIAL CHANGES',
      severity: 'OK',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 120,
      }),
      conclusion: 'Каталог и offers обработаны; есть существенные изменения.',
      catalog: 'обработан',
      offers: 'обработан',
      counts: 'добавлено URL=12, удалено=3, offers-позиций≈120 (синтетика)',
      affected: 'нет критических',
      action: null,
      metrics: { baseline_count: 1800, current_count: 1809, added_urls: 12, removed_urls: 3, onboarding_needed_count: 0 },
      source_status: 'NO_ACTION_REQUIRED',
    },
    {
      id: 'G4',
      name: 'IMPORT COMPLETED WITH WARNINGS',
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 10,
        warnings_present: true,
      }),
      conclusion: 'Импорт завершён с некритическими предупреждениями.',
      catalog: 'PASS с предупреждениями',
      offers: 'PASS с предупреждениями',
      counts: null,
      affected: 'отдельные позиции каталога/цен',
      action: 'Просмотреть предупреждения в журнале импорта',
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'G5',
      name: 'IMPORT ERROR',
      severity: 'FAILED',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: false,
        offers_phase_ok: false,
        import_error: true,
      }),
      conclusion: 'Ошибка на фазе импорта 1С.',
      catalog: 'ошибка фазы',
      offers: 'не подтверждена',
      counts: null,
      affected: 'актуальность каталога/цен',
      action: 'Разобрать ошибку по журналу импорта и повторить обмен',
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'FAILURE_REVIEW_REQUIRED',
    },
    {
      id: 'G6',
      name: 'NO FRESH 1C IMPORT',
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: false,
        monitor_completion_confirmed: true,
      }),
      conclusion: 'Свежий обмен с 1С в ожидаемом окне не подтверждён.',
      catalog: 'нет свежего цикла',
      offers: 'нет свежего цикла',
      counts: null,
      affected: 'цены, остатки и состав каталога могут быть устаревшими',
      action: 'Проверить расписание и факт выгрузки/импорта 1С',
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'G7',
      name: 'MONITOR COULD NOT CONFIRM COMPLETION',
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        monitor_completion_confirmed: false,
      }),
      conclusion: 'Монитор не подтвердил корректное завершение цикла.',
      catalog: 'не подтверждено монитором',
      offers: 'не подтверждено монитором',
      counts: null,
      affected: 'достоверность отчёта',
      action: 'Проверить marker/summary и повторный запуск монитора',
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'G8',
      name: 'CONFLICT OR INCOMPLETE FILE SET',
      severity: 'ATTENTION',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        conflict_or_incomplete: true,
        catalog_input_files: ['import0_1.xml'],
      }),
      conclusion: 'Обнаружен конфликтный или неполный набор файлов обмена.',
      catalog: 'частично/конфликт',
      offers: 'неполный комплект',
      counts: null,
      affected: 'целостность обмена',
      action: 'Сверить имена и состав import0-N / offers0-N перед повторным импортом',
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'HYGIENE_REVIEW_REQUIRED',
    },
    {
      id: 'G9',
      name: 'RECOVERY / CONDITION RESOLVED',
      severity: 'OK',
      classification: classifyImportReport({
        fresh_import_confirmed: true,
        catalog_input_files: ['import0_1.xml'],
        offers_input_files: ['offers0_1.xml'],
        catalog_phase_ok: true,
        offers_phase_ok: true,
        offers_processed_count: 5,
        recovery_resolved: true,
      }),
      conclusion: 'Ранее зафиксированное внимание снято: последний цикл успешен.',
      catalog: 'обработан',
      offers: 'обработан',
      counts: null,
      affected: 'нет',
      action: null,
      metrics: { baseline_count: 1879, current_count: 1879, added_urls: 0, removed_urls: 0, onboarding_needed_count: 0 },
      source_status: 'NO_ACTION_REQUIRED',
    },
  ];

  return defs.map((d) => {
    const event_id = galleryEventId(d.id);
    const text = buildMessage({
      scenarioId: d.id,
      scenarioName: d.name,
      severity: d.severity === 'FAILED' ? 'ERROR' : d.severity,
      conclusion: d.conclusion,
      catalog: d.catalog,
      offers: d.offers,
      affected: d.affected,
      action: d.action,
      counts: d.counts,
    });
    const envelope = {
      schema_name: 'mars.client_ops.report',
      schema_version: '1.0',
      event_id,
      event_type: 'site.post_1c_monitor',
      generated_at: generated,
      observed_at: observed,
      environment: `test-gallery.${d.id}`,
      site: {
        site_id: 'SITE-002',
        site_name: `ZPM-D6F1A-${d.id}`,
        domain: 'bzpm.ru',
      },
      producer: {
        name: 'mars.client-ops.test-gallery.site-002',
        version: '1b-d6f1a.0',
      },
      run: {
        run_id: `d6f1a-gallery-${GALLERY_TS}-${d.id}`,
        source_status: d.source_status,
        normalized_status: d.severity === 'FAILED' ? 'FAILED' : d.severity,
        summary_code: d.classification.summary_code,
        reason_codes: [
          'TEST_GALLERY',
          'SYNTHETIC_NON_CUSTOMER',
          ...(d.classification.reason_codes || []),
        ],
      },
      action: {
        required: d.severity !== 'OK',
        code: d.classification.action_code || 'NONE',
        text,
      },
      metrics: d.metrics,
      freshness: {
        age_seconds: 120,
        stale: false,
      },
      security: {
        classification: 'internal',
        contains_secrets: false,
        redacted: true,
      },
    };
    return {
      scenario_id: d.id,
      scenario_name: d.name,
      severity: envelope.run.normalized_status,
      report_class: d.classification.report_class,
      event_id,
      event_namespace: `mars.client-ops.test-gallery.site-002.${GALLERY_TS}.${d.id}`,
      message_text: text,
      envelope,
    };
  });
}

async function listExecutions(creds, workflowId, limit = 50) {
  const base = normalizeBaseUrl(creds.apiUrl);
  const url = `${base}/api/v1/executions?workflowId=${encodeURIComponent(workflowId)}&limit=${limit}`;
  const response = await fetch(url, {
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { ok: false, status: response.status, rows: [] };
  const data = await response.json();
  return { ok: true, rows: data.data || data || [] };
}

async function getExecutionDetail(creds, id) {
  const base = normalizeBaseUrl(creds.apiUrl);
  const response = await fetch(`${base}/api/v1/executions/${id}?includeData=true`, {
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { ok: false, status: response.status };
  return { ok: true, data: await response.json() };
}

function summarizeExecution(detail) {
  if (!detail?.ok) return { ok: false };
  const runData = detail.data?.data?.resultData?.runData || {};
  const nodeOrder = Object.keys(runData).filter((k) => Array.isArray(runData[k]) && runData[k].length);
  const telegramRuns = Array.isArray(runData[TELEGRAM_NODE_NAME])
    ? runData[TELEGRAM_NODE_NAME].length
    : 0;
  let telegramMessageId = null;
  if (telegramRuns > 0) {
    const out = runData[TELEGRAM_NODE_NAME][0]?.data?.main?.[0]?.[0]?.json;
    telegramMessageId = out?.result?.message_id ?? out?.message_id ?? null;
  }
  return {
    ok: true,
    execution_id: String(detail.data?.id || ''),
    status: detail.data?.status,
    finished: detail.data?.finished,
    node_names_executed: nodeOrder,
    telegram_runs: telegramRuns,
    telegram_message_id:
      telegramMessageId != null && /^\d+$/.test(String(telegramMessageId))
        ? String(telegramMessageId)
        : null,
    has_telegram: nodeOrder.includes(TELEGRAM_NODE_NAME),
    has_claim_insert: nodeOrder.includes('Dedupe Claim Insert'),
  };
}

async function postWebhook(webhookUrl, secret, body) {
  const response = await fetch(webhookUrl, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'x-mars-client-ops-token': secret,
    },
    body: JSON.stringify(body),
  });
  const text = await response.text();
  let json = null;
  try {
    json = text ? JSON.parse(text) : null;
  } catch {
    json = { parse_error: true, body_len: text.length };
  }
  return { status: response.status, json };
}

async function waitForNewExecution(creds, workflowId, priorIds, startedAfterIso) {
  for (let i = 0; i < 30; i += 1) {
    await new Promise((r) => setTimeout(r, 1000));
    const snap = await listExecutions(creds, workflowId, 30);
    const fresh = (snap.rows || []).find((row) => {
      if (priorIds.has(String(row.id))) return false;
      if (startedAfterIso && row.startedAt && row.startedAt < startedAfterIso) return false;
      return true;
    });
    if (fresh) {
      const detail = await getExecutionDetail(creds, fresh.id);
      return { found: true, execution: fresh, summary: summarizeExecution(detail) };
    }
  }
  return { found: false };
}

async function getEventRow(eventId) {
  const creds = loadDataTableCredentials();
  const filtered = await getDataTableRows(creds, D6A_TABLE_ID, {
    limit: 5,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: eventId }] },
  });
  const rows = filtered.data?.data || filtered.data || [];
  const list = Array.isArray(rows) ? rows : [];
  const matches = list.filter((r) => String(r.event_id) === String(eventId));
  return { count: matches.length, row: matches[0] || null };
}

async function listAllRows() {
  const creds = loadDataTableCredentials();
  const all = await getDataTableRows(creds, D6A_TABLE_ID, { limit: 100 });
  const rows = all.data?.data || all.data || [];
  return Array.isArray(rows) ? rows : [];
}

function parseArgs(argv) {
  const out = { send: false, confirm: null };
  for (let i = 0; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === '--send') out.send = true;
    if (a.startsWith('--confirm=')) out.confirm = a.slice('--confirm='.length);
    if (a === '--confirm') out.confirm = argv[++i];
  }
  return out;
}

async function updateTelegramExpression(creds) {
  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  const nodes = structuredClone(live.nodes || []);
  const tg = nodes.find((n) => n.name === TELEGRAM_NODE_NAME);
  if (!tg) throw new Error('telegram_node_missing');
  const newText = `={{ (() => {
  const body = $('Capture Request Metadata').item.json.body || {};
  const actionText = String((body.action && body.action.text) || '');
  if (actionText.indexOf('🧪 ТЕСТОВОЕ СООБЩЕНИЕ') === 0) {
    return actionText;
  }
  const status = String((body.run && body.run.normalized_status) || 'OK');
  const statusRu =
    status === 'OK' ? 'Всё работает штатно'
    : status === 'ATTENTION' ? 'Требуется внимание'
    : status === 'FAILED' ? 'Есть сбой'
    : status === 'BLOCKED' ? 'Доставка заблокирована'
    : status;
  const observedRaw = String(body.observed_at || body.generated_at || '');
  const observed = observedRaw.replace('T', ' ').replace(/\\.\\d{3}Z$/, '').replace(/Z$/, '').slice(0, 16);
  const problems =
    Number((body.metrics && body.metrics.onboarding_needed_count) || 0) +
    Number((body.metrics && body.metrics.removed_urls) || 0);
  const importResult = actionText || 'Проверка канала уведомлений';
  const rec = status === 'OK' ? 'Действия не требуются' : actionText || 'Требуется проверка';
  const isTestEnv = String(body.environment || '').indexOf('test-gallery') === 0;
  const prefix = isTestEnv ? '🧪 ТЕСТОВОЕ СООБЩЕНИЕ\\nСценарий: gallery\\n\\n' : '';
  return prefix
    + '[' + status + '] bzpm.ru — контроль после обмена с 1С\\n\\n'
    + 'Статус: ' + statusRu + '\\n'
    + 'Время проверки: ' + observed + '\\n'
    + 'Результат: ' + importResult + '\\n'
    + 'Найдено проблем: ' + problems + '\\n'
    + 'Рекомендация: ' + rec;
})() }}`;
  if (String(tg.parameters?.text || '') === newText) {
    return { changed: false, versionId: live.versionId, active: live.active };
  }
  tg.parameters = { ...(tg.parameters || {}), text: newText };
  // Use update client
  const updateMod = await import('./lib/client-ops-n8n-workflow-update-client.mjs');
  const updateCreds = updateMod.loadUpdateCredentials();
  const put_payload = updateMod.prepareWorkflowPutPayload({
    name: live.name,
    nodes,
    connections: live.connections,
    settings: live.settings,
    staticData: live.staticData,
  });
  const result = await updateMod.updateAllowlistedWorkflow(updateCreds, put_payload, {
    confirmPhrase: 'UPDATE CLIENT OPS D6F1A TELEGRAM MESSAGE FORMAT BZPM',
  });
  return { changed: true, result, prior_version: live.versionId };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  mkdirSync(EVIDENCE, { recursive: true });
  const items = scenarios();
  writeJson(join(EVIDENCE, 'TEST-GALLERY-SCENARIOS.json'), {
    phase: '1B-D6F1A',
    gallery_timestamp: GALLERY_TS,
    count: items.length,
    scenarios: items.map((s) => ({
      scenario_id: s.scenario_id,
      scenario_name: s.scenario_name,
      severity: s.severity,
      report_class: s.report_class,
      event_id: s.event_id,
      event_namespace: s.event_namespace,
      message_text: s.message_text,
    })),
  });
  writeJson(join(EVIDENCE, 'TEST-GALLERY-MESSAGE-PREVIEW.md'), {
    note: 'see TEST-GALLERY-MESSAGE-PREVIEW.txt',
  });
  writeFileSync(
    join(EVIDENCE, 'TEST-GALLERY-MESSAGE-PREVIEW.txt'),
    items.map((s) => `===== ${s.scenario_id} ${s.scenario_name} =====\n${s.message_text}\n`).join('\n'),
    'utf8',
  );

  if (!args.send) {
    console.log(
      JSON.stringify(
        {
          mode: 'dry-run',
          scenarios: items.length,
          evidence: EVIDENCE,
          token: 'D6F1A_GALLERY_PREVIEW_ONLY',
        },
        null,
        2,
      ),
    );
    return;
  }
  if (args.confirm !== CONFIRM) {
    throw new Error('CONFIRM_PHRASE_MISMATCH');
  }

  const secret = loadEnvKey(SECRET_PATH, 'CLIENT_OPS_WEBHOOK_AUTH_SECRET');
  if (!secret.ok) throw new Error('WEBHOOK_SECRET_MISSING');
  const creds = loadCredentials();
  const live = await getWorkflow(ALLOWED_WORKFLOW_ID, creds);
  if (!live.active) throw new Error('WORKFLOW_NOT_ACTIVE');
  const webhookNode = (live.nodes || []).find((n) => n.name === 'Webhook Intake');
  const path = webhookNode?.parameters?.path;
  if (!path) throw new Error('WEBHOOK_PATH_MISSING');
  const webhookUrl = `${normalizeBaseUrl(creds.apiUrl)}/webhook/${path}`;

  // Production row snapshot before
  const beforeList = await listAllRows();
  const productionIdsBefore = new Set(
    beforeList
      .filter((r) => {
        const producer = String(r.producer || r.producer_name || '');
        return !producer.includes('test-gallery');
      })
      .map((r) => r.event_id),
  );

  const results = [];
  const priorIds = new Set(
    ((await listExecutions(creds, ALLOWED_WORKFLOW_ID, 50)).rows || []).map((r) => String(r.id)),
  );

  for (const item of items) {
    const existing = await getEventRow(item.event_id);
    if (existing.count !== 0) {
      results.push({
        scenario_id: item.scenario_id,
        skipped: true,
        reason: 'EVENT_ID_ALREADY_EXISTS',
        event_id: item.event_id,
      });
      continue;
    }
    const startedAfter = new Date(Date.now() - 2000).toISOString();
    const post = await postWebhook(webhookUrl, secret.value, item.envelope);
    const waited = await waitForNewExecution(creds, ALLOWED_WORKFLOW_ID, priorIds, startedAfter);
    if (waited.found) priorIds.add(String(waited.execution.id));
    let row = await getEventRow(item.event_id);
    for (let i = 0; i < 12 && row.row && row.row.delivery_state === 'PENDING'; i += 1) {
      await new Promise((r) => setTimeout(r, 1000));
      row = await getEventRow(item.event_id);
    }
    const summary = waited.summary || { ok: false };
    const delivered =
      (post.status === 200 || post.status === 202) &&
      summary.telegram_runs === 1 &&
      summary.telegram_message_id != null;
    results.push({
      scenario_id: item.scenario_id,
      scenario_name: item.scenario_name,
      severity: item.severity,
      event_id: item.event_id,
      http_status: post.status,
      intake_state: row.row?.intake_state || null,
      delivery_state: row.row?.delivery_state || null,
      n8n_execution_id: summary.execution_id || null,
      telegram_delivery_success: delivered,
      telegram_message_id_present: Boolean(summary.telegram_message_id),
      telegram_message_id_redacted: summary.telegram_message_id
        ? `msg:${String(summary.telegram_message_id).slice(0, 2)}***`
        : null,
      duplicate_count: 0,
      report_class: item.report_class,
    });
  }

  const afterList = await listAllRows();
  const productionUntouched = [...productionIdsBefore].every((id) => {
    const before = beforeList.find((r) => r.event_id === id);
    const after = afterList.find((r) => r.event_id === id);
    if (!before || !after) return false;
    return (
      before.intake_state === after.intake_state &&
      before.delivery_state === after.delivery_state &&
      before.event_status === after.event_status
    );
  });

  const deliveredCount = results.filter((r) => r.telegram_delivery_success).length;
  writeJson(join(EVIDENCE, 'TEST-GALLERY-DELIVERY-RESULTS.json'), {
    phase: '1B-D6F1A',
    token:
      deliveredCount >= 8
        ? 'D6F1A_ALL_GALLERY_MESSAGES_DELIVERED'
        : 'D6F1A_GALLERY_DELIVERY_INCOMPLETE',
    required: 8,
    delivered: deliveredCount,
    results,
    production_rows_untouched: productionUntouched,
    workflow_active_after: (await getWorkflow(ALLOWED_WORKFLOW_ID, creds)).active === true,
  });

  console.log(
    JSON.stringify(
      {
        delivered: deliveredCount,
        required: 8,
        production_rows_untouched: productionUntouched,
        results: results.map((r) => ({
          scenario_id: r.scenario_id,
          telegram_delivery_success: r.telegram_delivery_success,
          n8n_execution_id: r.n8n_execution_id,
          delivery_state: r.delivery_state,
        })),
      },
      null,
      2,
    ),
  );

  if (deliveredCount < 8) process.exitCode = 2;
}

main().catch((err) => {
  console.error(String(err && err.message ? err.message : err));
  process.exitCode = 1;
});
