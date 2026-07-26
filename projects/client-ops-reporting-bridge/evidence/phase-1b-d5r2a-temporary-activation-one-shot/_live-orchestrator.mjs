/**
 * D5R2A one-shot: activate → webhook-ready check → one producer POST → observe → deactivate.
 * Deactivate ALWAYS runs in finally. Max 1 POST. No retry.
 */
import { spawnSync } from 'node:child_process';
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  getWorkflow,
  loadCredentials,
  normalizeBaseUrl,
} from '../../../metabot-seo-content-agent/integrations/n8n-readonly-exporter/lib/n8n-api-client.mjs';
import {
  activateAllowlistedWorkflow,
  deactivateAllowlistedWorkflow,
  loadActivationCredentials,
  ALLOWED_WORKFLOW_ID,
  D5_ACTIVATION_CONFIRM_PHRASE,
  D5_DEACTIVATION_CONFIRM_PHRASE,
  D5_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
} from '../../n8n/runners/lib/client-ops-n8n-activation-client.mjs';
import {
  getDataTable,
  getDataTableRows,
  loadDataTableCredentials,
} from '../../n8n/runners/lib/client-ops-n8n-datatable-client.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, '../../../..');
const EVIDENCE = __dirname;
const WORKFLOW_ID = ALLOWED_WORKFLOW_ID;
const TABLE_ID = 'H6VYhwz7RXZCBMmu';
const EVENT_ID = 'c84e29bf-79b1-5aea-98c4-9dc8d651fc96';
const SOURCE =
  'X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\scheduled-monitors\\post-1c\\2026-07-26_17-48-38';
const EXPECTED_VERSION = '3d2fd6fc-bc17-4e0f-b9e5-086c959afd29';
const STALE_AFTER = 93600;
const OBSERVED_AT = '2026-07-26T10:52:32Z';
const TELEGRAM_NODE_NAME = 'Telegram';
const PYTHON = process.env.CLIENT_OPS_PYTHON || 'py';

const LIVE_AUTH_PHRASE =
  'APPROVE D5R2A TEMPORARY ACTIVATE + ONE REAL SOURCE POST + DEACTIVATE — EVENT c84e29bf-79b1-5aea-98c4-9dc8d651fc96 — NO RETRY';

function writeJson(name, obj) {
  writeFileSync(resolve(EVIDENCE, name), `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function ageSeconds(now = new Date()) {
  const observed = new Date(OBSERVED_AT);
  return Math.floor((now.getTime() - observed.getTime()) / 1000);
}

function freshnessSnap(label) {
  const now = new Date();
  const age = ageSeconds(now);
  return {
    label,
    validation_time_utc: now.toISOString().replace(/\.\d{3}Z$/, 'Z'),
    observed_at: OBSERVED_AT,
    source_age_seconds: age,
    stale_after_seconds: STALE_AFTER,
    delivery_eligibility: age <= STALE_AFTER ? 'FRESH' : 'STALE',
    verdict: age <= STALE_AFTER ? 'D5R2A_CANDIDATE_FRESH' : 'D5R2A_CANDIDATE_STALE',
  };
}

async function executionSnapshot(creds) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions?workflowId=${encodeURIComponent(WORKFLOW_ID)}&limit=100`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { observable: false, reason: `HTTP_${response.status}` };
  const data = await response.json();
  const rows = Array.isArray(data) ? data : data?.data;
  if (!Array.isArray(rows)) return { observable: false, reason: 'unexpected_shape' };
  return {
    observable: true,
    count: typeof data?.count === 'number' ? data.count : rows.length,
    running: rows.filter((r) => r.status === 'running').length,
    latest: rows[0]
      ? {
          id: String(rows[0].id),
          status: rows[0].status,
          finished: rows[0].finished,
          startedAt: rows[0].startedAt,
          stoppedAt: rows[0].stoppedAt,
          mode: rows[0].mode,
        }
      : null,
    ids: rows.slice(0, 5).map((r) => String(r.id)),
  };
}

async function getExecutionDetail(creds, executionId) {
  const url = `${normalizeBaseUrl(creds.apiUrl)}/api/v1/executions/${encodeURIComponent(executionId)}?includeData=true`;
  const response = await fetch(url, {
    method: 'GET',
    headers: { Accept: 'application/json', 'X-N8N-API-KEY': creds.apiKey },
  });
  if (!response.ok) return { ok: false, status: response.status };
  return { ok: true, data: await response.json() };
}

function summarizeTelegram(detail) {
  if (!detail?.ok) return { attempted: 0, delivered: 0, node_ok: null, message_id: null };
  const runData = detail.data?.data?.resultData?.runData || {};
  // Prefer exact Telegram node; fall back to type match without dumping payload
  let telegramKey = null;
  for (const name of Object.keys(runData)) {
    if (name === TELEGRAM_NODE_NAME || /telegram/i.test(name)) {
      telegramKey = name;
      break;
    }
  }
  if (!telegramKey) return { attempted: 0, delivered: 0, node_ok: null, message_id: null, node_name: null };
  const runs = runData[telegramKey];
  const attempted = Array.isArray(runs) ? runs.length : 0;
  let messageId = null;
  let nodeOk = null;
  if (Array.isArray(runs) && runs[0]) {
    nodeOk = runs[0].error ? false : true;
    try {
      const json = runs[0].data?.main?.[0]?.[0]?.json;
      if (json && typeof json === 'object') {
        if (json.message_id != null) messageId = String(json.message_id);
        else if (json.result?.message_id != null) messageId = String(json.result.message_id);
      }
    } catch {
      /* ignore */
    }
  }
  return {
    attempted,
    delivered: nodeOk && messageId ? 1 : nodeOk ? 1 : 0,
    node_ok: nodeOk,
    message_id: messageId,
    node_name: telegramKey,
  };
}

async function eventRowCount(dtCreds) {
  const filtered = await getDataTableRows(dtCreds, TABLE_ID, {
    limit: 20,
    filter: { filters: [{ columnName: 'event_id', condition: 'eq', value: EVENT_ID }] },
  });
  const rows = filtered.data?.data || filtered.data || [];
  return Array.isArray(rows) ? rows.length : null;
}

async function tableRowCount(dtCreds) {
  const table = await getDataTable(dtCreds, TABLE_ID);
  const tableData = table.data || table;
  if (typeof tableData.rowsCount === 'number') return tableData.rowsCount;
  const all = await getDataTableRows(dtCreds, TABLE_ID, { limit: 50 });
  const rows = all.data?.data || all.data || [];
  return Array.isArray(rows) ? rows.length : null;
}

function runProducerPost() {
  const env = {
    ...process.env,
    PYTHONPATH: resolve(REPO_ROOT, 'projects/client-ops-reporting-bridge/src'),
    PYTHONIOENCODING: 'utf-8',
  };
  const args = [
    '-3',
    '-m',
    'client_ops_reporting_bridge.cli',
    'site002-controlled-live',
    '--source',
    SOURCE,
    '--apply',
    '--confirm-enable=ENABLE ONE MANUAL SITE002 REAL SOURCE D5 BZPM',
    '--confirm-send=SEND ONE MANUAL SITE002 REAL SOURCE EVENT D5 BZPM',
    '--event-unseen',
    '--preview-approved',
    '--concurrency=1',
    '--max-retries=0',
  ];
  const result = spawnSync(PYTHON, args, {
    cwd: REPO_ROOT,
    env,
    encoding: 'utf8',
    windowsHide: true,
    timeout: 120000,
  });
  const stdout = String(result.stdout || '');
  const stderr = String(result.stderr || '');
  let parsed = null;
  try {
    const lines = stdout.trim().split(/\r?\n/).filter(Boolean);
    for (let i = lines.length - 1; i >= 0; i -= 1) {
      try {
        parsed = JSON.parse(lines[i]);
        break;
      } catch {
        /* continue */
      }
    }
  } catch {
    parsed = null;
  }
  return {
    status: result.status,
    parsed,
    stdout_len: stdout.length,
    stderr_sanitized: stderr
      .replace(/[A-Za-z]:\\[^\s]+/g, '<path>')
      .replace(/https?:\/\/[^\s]+/g, '<url>')
      .slice(0, 800),
  };
}

async function main() {
  mkdirSync(EVIDENCE, { recursive: true });
  const args = process.argv.slice(2);
  if (!args.includes('--apply')) {
    writeJson('_orchestrator-dry.json', {
      ok: false,
      reason: 'missing --apply',
      live_auth_phrase_required: LIVE_AUTH_PHRASE,
    });
    process.exit(2);
  }
  if (!args.includes(`--confirm-live=${LIVE_AUTH_PHRASE}`)) {
    writeJson('_orchestrator-dry.json', {
      ok: false,
      reason: 'live authorization phrase mismatch',
    });
    process.exit(2);
  }

  let activationChanges = 0;
  let realHttpRequests = 0;
  let charterConsumed = false;
  let workflowWasActivated = false;
  const creds = loadCredentials();
  const actCreds = loadActivationCredentials();
  const dtCreds = loadDataTableCredentials();

  const preFresh = freshnessSnap('pre_activation');
  writeJson('FINAL-PREACTIVATION-FRESHNESS.json', preFresh);
  if (preFresh.delivery_eligibility !== 'FRESH') {
    writeJson('D5R2A-DECISION.json', {
      aborted: 'D5R2A_ABORTED_BEFORE_ACTIVATION_SOURCE_BECAME_STALE',
      activation_changes: 0,
      real_http_requests: 0,
    });
    process.exit(3);
  }

  const wfPre = await getWorkflow(WORKFLOW_ID, creds);
  const execPre = await executionSnapshot(creds);
  writeJson('ACTIVATION-PRESTATE.json', {
    active: Boolean(wfPre.active),
    nodes: (wfPre.nodes || []).length,
    versionId: wfPre.versionId,
    executions: execPre.count,
    running: execPre.running,
  });
  if (wfPre.active) {
    writeJson('D5R2A-DECISION.json', {
      aborted: 'WORKFLOW_UNEXPECTEDLY_ACTIVE_BEFORE_ACTIVATION',
      activation_changes: 0,
    });
    process.exit(4);
  }

  const result = {
    live_auth_phrase: LIVE_AUTH_PHRASE,
    activation_changes: 0,
    real_http_requests: 0,
    charter_consumed: false,
  };

  try {
    // ACTIVATE
    await activateAllowlistedWorkflow(actCreds, D5_ACTIVATION_CONFIRM_PHRASE);
    activationChanges = 1;
    workflowWasActivated = true;
    result.activation_changes = activationChanges;

    const wfActive = await getWorkflow(WORKFLOW_ID, creds);
    const execAfterAct = await executionSnapshot(creds);
    const webhookNodes = (wfActive.nodes || []).filter((n) =>
      String(n?.type || '').toLowerCase().includes('webhook'),
    );
    const activationResult = {
      activation_mutation: 'POST /api/v1/workflows/tkM4H0G0gM3q9Foi/activate',
      confirm_phrase_class: 'D5_ACTIVATE',
      activation_changes: 1,
      get_verify: {
        active: Boolean(wfActive.active),
        nodes: (wfActive.nodes || []).length,
        versionId: wfActive.versionId,
        version_unchanged: wfActive.versionId === EXPECTED_VERSION,
        nodes_unchanged: (wfActive.nodes || []).length === 17,
      },
      executions_after_activation: execAfterAct.count,
      running_after_activation: execAfterAct.running,
      unexpected_execution_on_activation:
        execAfterAct.count !== execPre.count || execAfterAct.running > 0,
      verdict: wfActive.active
        ? 'D5R2A_WORKFLOW_TEMPORARILY_ACTIVE'
        : 'D5R2A_ACTIVATION_FAILED',
    };
    writeJson('ACTIVATION-RESULT.json', activationResult);

    if (!wfActive.active) {
      result.activation_failed = true;
      return result;
    }

    const webhookReady = {
      method:
        'control-plane GET workflow after activation: active=true + webhook node webhookId present + established n8n production webhook semantics (no probe POST)',
      active: true,
      webhook_nodes: webhookNodes.length,
      webhook_id_present: webhookNodes.some((n) => Boolean(n.webhookId)),
      webhook_path_configured: webhookNodes.some(
        (n) => Boolean(n.parameters?.path) || Boolean(n.parameters?.options?.path),
      ),
      probe_post: false,
      verdict: null,
    };
    webhookReady.verdict =
      webhookReady.webhook_id_present && webhookReady.webhook_path_configured
        ? 'D5R2A_PRODUCTION_WEBHOOK_READY'
        : 'D5R2A_PRODUCTION_WEBHOOK_NOT_READY';
    writeJson('WEBHOOK-READY-CHECK.json', webhookReady);

    if (webhookReady.verdict !== 'D5R2A_PRODUCTION_WEBHOOK_READY') {
      result.webhook_not_ready = true;
      return result;
    }

    if (activationResult.unexpected_execution_on_activation) {
      result.unexpected_execution = true;
      return result;
    }

    const prePostFresh = freshnessSnap('pre_post');
    writeJson('FINAL-PREPOST-FRESHNESS.json', prePostFresh);
    if (prePostFresh.delivery_eligibility !== 'FRESH') {
      result.aborted_stale_before_post = true;
      return result;
    }

    // Re-check event unseen GET-only before POST
    const eventRowsPrePost = await eventRowCount(dtCreds);
    writeJson('EVENT-UNSEEN-PREPOST.json', {
      event_id: EVENT_ID,
      rows: eventRowsPrePost,
      verdict:
        eventRowsPrePost === 0
          ? 'D5R2A_EVENT_UNSEEN'
          : 'D5R2A_EVENT_ALREADY_SEEN_LIVE_POST_NOT_AUTHORIZED',
    });
    if (eventRowsPrePost !== 0) {
      result.event_already_seen = true;
      return result;
    }

    // ONE POST — charter consumed on initiate
    charterConsumed = true;
    realHttpRequests = 1;
    result.charter_consumed = true;
    result.real_http_requests = 1;
    writeJson('LIVE-REQUEST-INITIATED.json', {
      charter_consumed: true,
      real_http_requests: 1,
      event_id: EVENT_ID,
      concurrency: 1,
      retries: 0,
      replay: 0,
      initiated_at_utc: new Date().toISOString().replace(/\.\d{3}Z$/, 'Z'),
    });

    const post = runProducerPost();
    const httpStatus = post.parsed?.http_status ?? post.parsed?.request_sanitized?.http_status ?? null;
    const httpResult = {
      http_status: post.parsed?.http_status ?? null,
      intake_accepted: Boolean(post.parsed?.intake_accepted),
      business_result: post.parsed?.business_result ?? null,
      dedupe_result: post.parsed?.dedupe_result ?? null,
      final_state: post.parsed?.final_state ?? null,
      failure_category: post.parsed?.failure_category ?? null,
      producer_exit_status: post.status,
      network_calls: post.parsed?.network_calls ?? null,
      retry_count: post.parsed?.retry_count ?? 0,
      interpretation: null,
    };
    if (httpResult.http_status === 202) {
      httpResult.interpretation = 'HTTP_202_INTAKE_ACCEPTED — continue observation';
    } else if (httpResult.http_status === 404) {
      httpResult.interpretation = 'HTTP_404 — request rejected before workflow intake';
    } else if (httpResult.http_status === 200) {
      httpResult.interpretation = 'HTTP_200_UNEXPECTED_DUPLICATE';
    } else if (httpResult.http_status === 409) {
      httpResult.interpretation = 'HTTP_409_UNEXPECTED_CONFLICT';
    } else if (httpResult.http_status == null) {
      httpResult.interpretation = 'AMBIGUOUS_OR_PARSE_FAILURE';
    } else {
      httpResult.interpretation = `HTTP_${httpResult.http_status}_NO_RETRY`;
    }
    writeJson('HTTP-RESULT.json', httpResult);

    const liveSanitized = {
      request_count: 1,
      event_id: EVENT_ID,
      source_run_id: '2026-07-26_17-48-38',
      concurrency: 1,
      retry: 0,
      replay: 0,
      method: 'POST',
      auth_header_name: 'X-MARS-Client-Ops-Token',
      auth_header_present: true,
      auth_header_value: '<redacted>',
      webhook_url: '<redacted>',
      host_class: 'n8n-client-ops',
      content_type: 'application/json',
      body_schema_name: post.parsed?.request_sanitized?.body_schema_name || 'mars.client_ops.report',
      body_event_id: EVENT_ID,
      producer_run_id: post.parsed?.producer_run_id || null,
      charter_consumed_on_initiate: true,
      http_status: httpResult.http_status,
    };
    writeJson('LIVE-REQUEST-SANITIZED.json', liveSanitized);
    writeJson('LIVE-POST-CONSOLE-SANITIZED.json', {
      ...(post.parsed || { parse_failed: true }),
      // force redaction markers
      auth_header_value: '<redacted>',
    });

    // Bounded observation
    let execPost = await executionSnapshot(creds);
    let waited = 0;
    while (execPost.running > 0 && waited < 45000) {
      await sleep(1500);
      waited += 1500;
      execPost = await executionSnapshot(creds);
    }
    // If count increased, fetch latest execution detail
    let newExecId = null;
    if (execPost.observable && execPre.observable && execPost.count > execPre.count) {
      newExecId = execPost.latest?.id || null;
    } else if (execPost.latest && execPre.ids && !execPre.ids.includes(execPost.latest.id)) {
      newExecId = execPost.latest.id;
    }

    let execDetail = null;
    let telegram = { attempted: 0, delivered: 0, node_ok: null, message_id: null };
    if (newExecId) {
      // wait briefly for terminal if needed
      for (let i = 0; i < 20; i += 1) {
        execDetail = await getExecutionDetail(creds, newExecId);
        const st = execDetail?.data?.status;
        if (st && st !== 'running') break;
        await sleep(1500);
      }
      telegram = summarizeTelegram(execDetail);
    }

    const tableRowsPost = await tableRowCount(dtCreds);
    const eventRowsPost = await eventRowCount(dtCreds);

    writeJson('N8N-EXECUTION-RESULT.json', {
      pre_count: execPre.count,
      post_count: execPost.count,
      running_final: execPost.running,
      selected_execution_id: newExecId,
      selected_status: execDetail?.data?.status || execPost.latest?.status || null,
      finished: execDetail?.data?.finished ?? execPost.latest?.finished ?? null,
      mode: execDetail?.data?.mode || execPost.latest?.mode || null,
      attributable_to_event: Boolean(newExecId),
    });
    writeJson('DATA-TABLE-RESULT.json', {
      table_id: TABLE_ID,
      total_rows_pre: 2,
      total_rows_post: tableRowsPost,
      event_rows_pre: 0,
      event_rows_post: eventRowsPost,
      event_id: EVENT_ID,
      manual_mutations: 0,
    });
    writeJson('TELEGRAM-DELIVERY-RESULT.json', {
      attempted: telegram.attempted,
      delivered: telegram.delivered,
      node_ok: telegram.node_ok,
      node_name: telegram.node_name || null,
      message_id: telegram.message_id,
      direct_api_calls: 0,
      credential_id: '2bIC5376l7ElXb4B',
      credential_name: 'MARS Client Ops Telegram — bzpm.ru',
    });

    result.http = httpResult;
    result.execution = {
      pre: execPre.count,
      post: execPost.count,
      id: newExecId,
    };
    result.datatable = { total: tableRowsPost, event: eventRowsPost };
    result.telegram = telegram;
    return result;
  } finally {
    // MANDATORY DEACTIVATION
    let deactOk = false;
    let finalActive = null;
    let deactError = null;
    try {
      let wf = await getWorkflow(WORKFLOW_ID, creds);
      if (wf.active || workflowWasActivated || activationChanges >= 1) {
        try {
          await deactivateAllowlistedWorkflow(actCreds, D5_DEACTIVATION_CONFIRM_PHRASE);
        } catch (e1) {
          await deactivateAllowlistedWorkflow(
            actCreds,
            D5_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
          );
        }
        // inactive→active (1) + active→inactive (2)
        if (workflowWasActivated || activationChanges >= 1) {
          activationChanges = 2;
        }
      }
      wf = await getWorkflow(WORKFLOW_ID, creds);
      finalActive = Boolean(wf.active);
      if (finalActive) {
        await deactivateAllowlistedWorkflow(
          actCreds,
          D5_EMERGENCY_DEACTIVATION_CONFIRM_PHRASE,
        );
        wf = await getWorkflow(WORKFLOW_ID, creds);
        finalActive = Boolean(wf.active);
      }
      deactOk = finalActive === false;
      const execFinal = await executionSnapshot(creds);
      writeJson('DEACTIVATION-RESULT.json', {
        deactivation_mutation: 'POST /api/v1/workflows/tkM4H0G0gM3q9Foi/deactivate',
        activation_changes: activationChanges,
        get_verify_active: finalActive,
        nodes: (wf.nodes || []).length,
        versionId: wf.versionId,
        version_unchanged: wf.versionId === EXPECTED_VERSION,
        running: execFinal.running,
        verdict: deactOk
          ? 'D5R2A_WORKFLOW_RECONTAINED'
          : 'D5R2A_WORKFLOW_RECONTAINMENT_FAILED',
      });
    } catch (err) {
      deactError = err instanceof Error ? err.message : String(err);
      writeJson('DEACTIVATION-RESULT.json', {
        activation_changes: activationChanges,
        error: deactError.replace(/[A-Za-z]:\\[^\s]+/g, '<path>'),
        verdict: 'D5R2A_WORKFLOW_RECONTAINMENT_FAILED',
      });
    }
    writeJson('_orchestrator-result.json', {
      ...result,
      activation_changes: activationChanges,
      real_http_requests: realHttpRequests,
      charter_consumed: charterConsumed,
      final_active: finalActive,
      recontainment_ok: deactOk,
    });
  }
}

main().catch((err) => {
  writeFileSync(
    resolve(EVIDENCE, '_orchestrator-fatal.json'),
    `${JSON.stringify({ error: String(err?.message || err).slice(0, 500) }, null, 2)}\n`,
  );
  process.exit(1);
});
