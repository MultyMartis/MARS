/**
 * Phase 1B-D6G — completion-driven SITE-002 import report dispatch.
 * Targets exact import run_id from canonical terminal.json.
 * Idempotent per run_id via Data Table / workflow dedupe event_id.
 */
import { mkdirSync, writeFileSync, readFileSync, existsSync, readdirSync, renameSync, unlinkSync } from 'node:fs';
import { createHash, randomUUID } from 'node:crypto';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { spawnSync } from 'node:child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));
const MAIN_ROOT = process.env.MARS_MAIN_ROOT || 'X:\\AI MARS';
const PRODUCER_REPO =
  process.env.MARS_PRODUCER_REPO ||
  'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo';
const STATE_ROOT =
  process.env.MARS_PRODUCER_STATE ||
  'X:\\AI MARS STORAGE\\runtime-state\\client-ops-site-002-producer';
const DISPATCH_STATE = join(STATE_ROOT, 'state', 'import-completion-dispatch');
const ARTIFACT_ROOT =
  process.env.MARS_MONITOR_ARTIFACT_ROOT ||
  'X:\\AI MARS STORAGE\\ocpilot\\project-sites\\site-002\\production\\scheduled-monitors\\post-1c';
const WORKFLOW_ID = 'tkM4H0G0gM3q9Foi';

function writeJson(path, obj) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function loadEnvFile(p) {
  const out = {};
  if (!existsSync(p)) return out;
  for (const line of readFileSync(p, 'utf8').split(/\r?\n/)) {
    const m = line.match(/^\s*([A-Za-z0-9_]+)\s*=\s*(.*)\s*$/);
    if (!m) continue;
    let v = m[2];
    if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
    out[m[1]] = v;
  }
  return out;
}

function argValue(name) {
  const pref = `--${name}=`;
  for (const a of process.argv.slice(2)) {
    if (a.startsWith(pref)) return a.slice(pref.length);
  }
  const idx = process.argv.indexOf(`--${name}`);
  if (idx >= 0) return process.argv[idx + 1];
  return null;
}

async function importLib(rel) {
  const base = join(PRODUCER_REPO, 'projects/client-ops-reporting-bridge/n8n/runners/lib');
  return import(pathToFileURL(join(base, rel)).href);
}

function buildEnvelopeFromTerminal(terminal, { classifyImportReport, formatOperatorTelegramMessage, computeEventId }) {
  const catalogFiles = (terminal.catalog_input_inventory || [])
    .map((x) => String(x).split(' ')[0])
    .filter((x) => /import0_.*\.xml/i.test(x));
  const offersFiles = (terminal.offers_input_inventory || [])
    .map((x) => String(x).split(' ')[0])
    .filter((x) => /offers0_.*\.xml/i.test(x));
  const catalogOk = String(terminal.catalog_phase_result?.status || '').toUpperCase() === 'PASS';
  const offersStatus = String(terminal.offers_phase_result?.status || '').toUpperCase();
  const offersOk = offersStatus === 'PASS';
  const classification = classifyImportReport({
    fresh_import_confirmed: true,
    catalog_input_files: catalogFiles,
    offers_input_files: offersFiles,
    catalog_phase_ok: catalogOk,
    offers_phase_ok: offersOk && offersFiles.length > 0,
    offers_processed_count: offersFiles.length,
    import_error: String(terminal.final_status || '') === 'FAILED',
    warnings_present: String(terminal.final_status || '') === 'ATTENTION_COMPLETED_WITH_WARNINGS',
    monitor_completion_confirmed: true,
  });

  const observedAt = terminal.completed_at || terminal.started_at || new Date().toISOString();
  const telegram_text = formatOperatorTelegramMessage({
    report_class: classification.report_class,
    summary_code: classification.summary_code,
    reason_codes: classification.reason_codes,
    normalized_status: classification.severity,
    domain: 'bzpm.ru',
    observed_at: observedAt,
    error_summary: terminal.sanitized_error_summary || '',
  });

  const runId = String(terminal.run_id);
  const severity =
    classification.severity === 'OK'
      ? 'OK'
      : classification.severity === 'ERROR'
        ? 'FAILED'
        : 'ATTENTION';
  const event_id = computeEventId({
    action_code: classification.action_code || 'NONE',
    event_type: 'site.post_1c_monitor',
    metrics: {
      added_urls: 0,
      baseline_count: 0,
      current_count: 0,
      onboarding_needed_count: 0,
      removed_urls: 0,
    },
    normalized_status: severity === 'FAILED' ? 'FAILED' : severity,
    observed_at: observedAt,
    reason_codes: classification.reason_codes || [],
    run_id: runId,
    schema_major: 1,
    site_id: 'SITE-002',
    summary_code: classification.summary_code || 'IMPORT_COMPLETION',
  });

  return {
    schema_name: 'mars.client_ops.report',
    schema_version: '1.0',
    event_id,
    event_type: 'site.post_1c_monitor',
    generated_at: new Date().toISOString(),
    observed_at: observedAt,
    environment: 'production',
    site: {
      site_id: 'SITE-002',
      site_name: 'BZPM',
      domain: 'bzpm.ru',
    },
    producer: {
      name: 'mars.client-ops.site-002.completion-dispatcher',
      version: '1b-d6g.1',
    },
    run: {
      run_id: runId,
      source_status:
        severity === 'OK'
          ? 'CLEAN'
          : severity === 'FAILED'
            ? 'FAILURE_REVIEW_REQUIRED'
            : 'ATTENTION_REQUIRED',
      normalized_status: severity === 'FAILED' ? 'FAILED' : severity,
      summary_code: classification.summary_code,
      reason_codes: ['D6G_IMPORT_COMPLETION', ...(classification.reason_codes || [])],
    },
    action: {
      required: severity !== 'OK',
      code: classification.action_code || 'NONE',
      text: telegram_text,
    },
    metrics: {
      baseline_count: 0,
      current_count: 0,
      added_urls: 0,
      removed_urls: 0,
      onboarding_needed_count: 0,
    },
    freshness: { age_seconds: 30, stale: false },
    security: {
      classification: 'internal',
      contains_secrets: false,
      redacted: true,
    },
    // Non-secret operator aids (workflow may ignore)
    report_class: classification.report_class,
    import_final_status: terminal.final_status,
    trigger_source: terminal.trigger_source || null,
  };
}

async function postWebhookEnvelope(envelope) {
  const secrets = loadEnvFile(join(MAIN_ROOT, 'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env'));
  const n8n = loadEnvFile(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
  const token =
    secrets.CLIENT_OPS_WEBHOOK_AUTH_SECRET ||
    secrets.CLIENT_OPS_WEBHOOK_TOKEN ||
    secrets.WEBHOOK_TOKEN ||
    secrets.MARS_CLIENT_OPS_TOKEN;
  const apiUrl = (n8n.N8N_API_URL || '').replace(/\/$/, '');
  if (!token || !apiUrl) return { ok: false, reason: 'WEBHOOK_CREDS_MISSING' };

  const transport = await importLib('client-ops-d6e2-readonly-transport.mjs');
  const creds = transport.loadCredentials(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
  transport.assertGetOnlyAction('GET', 'workflow_for_webhook_path');
  const wf = await transport.getAllowlistedWorkflow(creds);
  if (!wf?.active) return { ok: false, reason: 'WORKFLOW_NOT_ACTIVE' };
  const webhook = (wf.nodes || []).find((n) => n.name === 'Webhook Intake');
  const path = webhook?.parameters?.path;
  if (!path) return { ok: false, reason: 'WEBHOOK_PATH_MISSING' };
  const url = `${apiUrl}/webhook/${path}`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'x-mars-client-ops-token': token,
    },
    body: JSON.stringify(envelope),
  });
  const text = await response.text();
  let data = null;
  try { data = text ? JSON.parse(text) : null; } catch { data = { body_len: text.length }; }
  return {
    ok: response.status === 200 || response.status === 202,
    http_status: response.status,
    intake_state: data?.intake_state ?? data?.data?.intake_state ?? null,
    delivery_state: data?.delivery_state ?? data?.data?.delivery_state ?? null,
    event_id: envelope.event_id,
  };
}

function alreadyDispatched(runId) {
  const marker = join(DISPATCH_STATE, `${runId}.delivered.json`);
  return existsSync(marker);
}

function markDispatched(runId, receipt) {
  writeJson(join(DISPATCH_STATE, `${runId}.delivered.json`), receipt);
}

async function dispatchTerminal(terminalPath) {
  const terminal = JSON.parse(readFileSync(terminalPath, 'utf8'));
  const runId = String(terminal.run_id || '');
  if (!runId) return { ok: false, reason: 'MISSING_RUN_ID' };
  if (alreadyDispatched(runId)) {
    return { ok: true, duplicate: true, run_id: runId, reason: 'ALREADY_DISPATCHED' };
  }

  const { classifyImportReport } = await importLib('client-ops-d6d-import-condition.mjs');
  const { formatOperatorTelegramMessage } = await importLib('client-ops-telegram-operator-message.mjs');
  const { computeEventId } = await importLib('client-ops-d6d-artifact.mjs');
  const { acquireProducerLock, releaseProducerLock } = await importLib('client-ops-d6d-producer-lock.mjs');

  const lockPath = join(STATE_ROOT, 'locks', 'producer.lock.json');
  const owner = randomUUID();
  const acq = acquireProducerLock({
    lockPath,
    siteId: 'SITE-002',
    producerIdentity: 'mars.client-ops.site-002.completion-dispatcher',
    ownerToken: owner,
    sessionId: randomUUID(),
    runtimeCheckoutIdentity: 'd6g-completion',
    nowMs: Date.now(),
    leaseMs: 180_000,
    pid: process.pid,
    processIdentity: 'd6g-completion-dispatch',
    processAlive: () => true,
  });
  if (!acq.ok) return { ok: false, reason: 'PRODUCER_LOCK_HELD', run_id: runId };

  try {
    const envelope = buildEnvelopeFromTerminal(terminal, {
      classifyImportReport,
      formatOperatorTelegramMessage,
      computeEventId,
    });
    // Materialize a lightweight completed artifact for audit (not selected by timer backlog).
    const artDir = join(ARTIFACT_ROOT, 'completion-dispatch', runId);
    mkdirSync(artDir, { recursive: true });
    writeJson(join(artDir, 'terminal.json'), terminal);
    writeJson(join(artDir, 'envelope.json'), envelope);
    writeJson(join(artDir, 'completion-marker.json'), {
      schema_version: 1,
      completed: true,
      run_id: runId,
      source: 'd6g-completion-dispatcher',
      completed_at: new Date().toISOString(),
    });

    const post = await postWebhookEnvelope(envelope);
    const receipt = {
      phase: '1B-D6G',
      run_id: runId,
      event_id: envelope.event_id,
      report_class: envelope.report_class,
      post,
      finished_at: new Date().toISOString(),
    };
    if (post.ok) markDispatched(runId, receipt);
    writeJson(join(DISPATCH_STATE, `${runId}.last-attempt.json`), receipt);
    return { ok: post.ok, run_id: runId, receipt };
  } finally {
    releaseProducerLock(lockPath, owner);
  }
}

async function main() {
  const mode = argValue('mode') || 'run-id';
  const runId = argValue('run-id');
  const terminalPathArg = argValue('terminal');
  let terminalPath = terminalPathArg;
  if (!terminalPath && runId) {
    // Local mirror path used by deploy/fetch tooling
    terminalPath = join(STATE_ROOT, 'import-terminals', runId, 'terminal.json');
  }
  if (!terminalPath || !existsSync(terminalPath)) {
    console.log(JSON.stringify({ ok: false, reason: 'TERMINAL_NOT_FOUND', run_id: runId, terminalPath }, null, 2));
    process.exit(2);
  }
  const result = await dispatchTerminal(terminalPath);
  console.log(JSON.stringify(result, null, 2));
  process.exit(result.ok ? 0 : 1);
}

main().catch((e) => {
  console.log(JSON.stringify({ ok: false, reason: 'EXCEPTION', message: String(e?.message || e) }, null, 2));
  process.exit(1);
});
