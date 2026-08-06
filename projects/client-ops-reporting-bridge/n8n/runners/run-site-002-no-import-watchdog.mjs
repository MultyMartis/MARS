/**
 * Phase 1B-D6G — daily no-import watchdog (not a normal success/error delivery timer).
 * Sends ATTENTION only when no expected scheduled terminal exists in the reporting window.
 */
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createHash, randomUUID } from 'node:crypto';

const __dirname = dirname(fileURLToPath(import.meta.url));
const MAIN_ROOT = process.env.MARS_MAIN_ROOT || 'X:\\AI MARS';
const PRODUCER_REPO =
  process.env.MARS_PRODUCER_REPO ||
  'X:\\AI MARS STORAGE\\runtime-checkouts\\client-ops-site-002-producer\\repo';
const STATE_ROOT =
  process.env.MARS_PRODUCER_STATE ||
  'X:\\AI MARS STORAGE\\runtime-state\\client-ops-site-002-producer';
const TERMINALS_ROOT = join(STATE_ROOT, 'import-terminals');
const WATCHDOG_STATE = join(STATE_ROOT, 'state', 'no-import-watchdog');
// Expected scheduled import ~12:00 Barnaul; watchdog after completion window + margin.
const EXPECTED_LOCAL_HOUR = 12;
const DEADLINE_LOCAL_HOUR = 13; // 13:00 Barnaul — after typical import + margin
const TZ_OFFSET_MIN = 7 * 60;

function writeJson(path, obj) {
  mkdirSync(dirname(path), { recursive: true });
  writeFileSync(path, `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
}

function localNowParts() {
  const ms = Date.now() + TZ_OFFSET_MIN * 60_000;
  const d = new Date(ms);
  return {
    y: d.getUTCFullYear(),
    m: d.getUTCMonth() + 1,
    d: d.getUTCDate(),
    h: d.getUTCHours(),
    mi: d.getUTCMinutes(),
    isoDate: `${d.getUTCFullYear()}-${String(d.getUTCMonth() + 1).padStart(2, '0')}-${String(d.getUTCDate()).padStart(2, '0')}`,
  };
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

async function importLib(rel) {
  return import(pathToFileURL(join(PRODUCER_REPO, 'projects/client-ops-reporting-bridge/n8n/runners/lib', rel)).href);
}

function listTodayTerminals(isoDate) {
  if (!existsSync(TERMINALS_ROOT)) return [];
  const out = [];
  for (const name of readdirSync(TERMINALS_ROOT)) {
    const p = join(TERMINALS_ROOT, name, 'terminal.json');
    if (!existsSync(p)) continue;
    try {
      const t = JSON.parse(readFileSync(p, 'utf8'));
      const completed = String(t.completed_at || t.started_at || '');
      if (completed.includes(isoDate) || String(t.run_id || '').includes(isoDate.replace(/-/g, ''))) {
        out.push(t);
      }
    } catch { /* ignore */ }
  }
  return out;
}

async function main() {
  const local = localNowParts();
  const eventDate = local.isoDate;
  const eventId = `site002-no-fresh-import-${eventDate}`;
  const marker = join(WATCHDOG_STATE, `${eventDate}.sent.json`);
  if (existsSync(marker)) {
    console.log(JSON.stringify({ ok: true, skipped: true, reason: 'ALREADY_SENT_TODAY', event_id: eventId }, null, 2));
    return;
  }
  if (local.h < DEADLINE_LOCAL_HOUR) {
    console.log(JSON.stringify({ ok: true, skipped: true, reason: 'BEFORE_DEADLINE', local_hour: local.h }, null, 2));
    return;
  }

  const terminals = listTodayTerminals(eventDate);
  const hasTerminal = terminals.some((t) => t.final_status);
  const importActive = terminals.some((t) => !t.final_status && t.current_phase && t.current_phase !== 'DONE');
  // Also check current-run mirror if present
  const currentPath = join(STATE_ROOT, 'import-terminals', '_current', 'run-state.json');
  if (existsSync(currentPath)) {
    try {
      const cur = JSON.parse(readFileSync(currentPath, 'utf8'));
      if (cur && !cur.final_status && cur.current_phase && !['DONE', 'QUEUED'].includes(cur.current_phase)) {
        console.log(JSON.stringify({ ok: true, skipped: true, reason: 'IMPORT_STILL_RUNNING', run_id: cur.run_id }, null, 2));
        return;
      }
      if (cur?.final_status) {
        console.log(JSON.stringify({ ok: true, skipped: true, reason: 'TERMINAL_EXISTS', run_id: cur.run_id }, null, 2));
        return;
      }
    } catch { /* ignore */ }
  }

  if (hasTerminal) {
    console.log(JSON.stringify({ ok: true, skipped: true, reason: 'TERMINAL_EXISTS', count: terminals.length }, null, 2));
    return;
  }
  if (importActive) {
    console.log(JSON.stringify({ ok: true, skipped: true, reason: 'IMPORT_STILL_RUNNING' }, null, 2));
    return;
  }

  const { formatOperatorTelegramMessage } = await importLib('client-ops-telegram-operator-message.mjs');
  const { classifyImportReport } = await importLib('client-ops-d6d-import-condition.mjs');
  const classification = classifyImportReport({
    fresh_import_confirmed: false,
    monitor_completion_confirmed: true,
  });
  const observedAt = new Date().toISOString();
  const telegram_text = formatOperatorTelegramMessage({
    report_class: classification.report_class,
    summary_code: classification.summary_code,
    reason_codes: classification.reason_codes,
    normalized_status: 'ATTENTION',
    domain: 'bzpm.ru',
    observed_at: observedAt,
  });

  const envelope = {
    schema_version: 1,
    event_id: eventId,
    site_id: 'SITE-002',
    domain: 'bzpm.ru',
    source_system: 'mars-1c-no-import-watchdog',
    run_id: `watchdog-${eventDate}`,
    observed_at: observedAt,
    generated_at: observedAt,
    normalized_status: 'ATTENTION',
    severity: 'ATTENTION',
    title: telegram_text.split('\n')[0],
    summary: classification.action_text,
    telegram_text,
    report_class: classification.report_class,
    summary_code: classification.summary_code,
    reason_codes: classification.reason_codes,
    producer: { name: 'mars.client-ops.site-002.no-import-watchdog', version: '1b-d6g.1' },
  };

  // Reuse completion dispatcher webhook posting by dynamic import of same helpers
  const secrets = loadEnvFile(join(MAIN_ROOT, 'local/client-ops-reporting-bridge/bzpm.ru/secrets.local.env'));
  const n8n = loadEnvFile(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
  const token =
    secrets.CLIENT_OPS_WEBHOOK_AUTH_SECRET ||
    secrets.CLIENT_OPS_WEBHOOK_TOKEN ||
    secrets.WEBHOOK_TOKEN ||
    secrets.MARS_CLIENT_OPS_TOKEN;
  const apiUrl = (n8n.N8N_API_URL || '').replace(/\/$/, '');
  if (!token || !apiUrl) {
    console.log(JSON.stringify({ ok: false, reason: 'WEBHOOK_CREDS_MISSING' }, null, 2));
    process.exit(2);
  }
  const transport = await importLib('client-ops-d6e2-readonly-transport.mjs');
  const creds = transport.loadCredentials(join(MAIN_ROOT, 'local/tokens/n8n-api.env'));
  const wf = await transport.getAllowlistedWorkflow(creds);
  if (!wf?.active) {
    console.log(JSON.stringify({ ok: false, reason: 'WORKFLOW_NOT_ACTIVE' }, null, 2));
    process.exit(2);
  }
  const path = (wf.nodes || []).find((n) => n.name === 'Webhook Intake')?.parameters?.path;
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
  const ok = response.status === 200 || response.status === 202;
  const receipt = {
    event_id: eventId,
    ok,
    http_status: response.status,
    finished_at: new Date().toISOString(),
  };
  if (ok) writeJson(marker, receipt);
  writeJson(join(WATCHDOG_STATE, `${eventDate}.last-attempt.json`), receipt);
  console.log(JSON.stringify({ ok, receipt, watchdog_only: true }, null, 2));
  process.exit(ok ? 0 : 1);
}

main().catch((e) => {
  console.log(JSON.stringify({ ok: false, reason: String(e?.message || e) }, null, 2));
  process.exit(1);
});
